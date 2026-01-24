#!/usr/bin/env python3
"""
Detailed Financial Model Analysis
Focus on formula patterns, Google Sheets compatibility, and recommendations
"""

import openpyxl
from openpyxl import load_workbook
import re
from collections import defaultdict, Counter

class DetailedAuditor:
    def __init__(self, filename):
        self.filename = filename
        self.wb = load_workbook(filename, data_only=False)
        self.formula_functions = Counter()
        self.recommendations = []

    def analyze_formula_patterns(self):
        """Analyze all formulas for patterns and functions used"""
        print("\n" + "=" * 80)
        print("DETAILED FORMULA ANALYSIS")
        print("=" * 80)

        all_formulas = []

        for sheet_name in self.wb.sheetnames:
            ws = self.wb[sheet_name]
            for row in ws.iter_rows():
                for cell in row:
                    if cell.value and isinstance(cell.value, str) and cell.value.startswith('='):
                        formula = cell.value
                        all_formulas.append({
                            'sheet': sheet_name,
                            'cell': cell.coordinate,
                            'formula': formula
                        })

                        # Extract Excel functions
                        functions = re.findall(r'([A-Z]+)\(', formula)
                        for func in functions:
                            self.formula_functions[func] += 1

        print(f"\nTotal Formulas Analyzed: {len(all_formulas)}")
        print("\nExcel Functions Used:")
        print("-" * 80)

        if self.formula_functions:
            for func, count in self.formula_functions.most_common():
                print(f"  {func}: {count} times")
        else:
            print("  (No complex functions detected - simple arithmetic only)")

        return all_formulas

    def check_google_sheets_compatibility(self):
        """Check for Google Sheets compatibility issues"""
        print("\n" + "=" * 80)
        print("GOOGLE SHEETS COMPATIBILITY CHECK")
        print("=" * 80)

        incompatible_functions = {
            'XLOOKUP': 'Use INDEX/MATCH or VLOOKUP instead',
            'XMATCH': 'Use MATCH instead',
            'LET': 'Not supported - use helper cells',
            'LAMBDA': 'Not supported',
            'XIRR': 'May have precision differences',
            'XNPV': 'May have precision differences',
            'FILTER': 'Google Sheets has different syntax',
            'SORT': 'Google Sheets has different syntax',
            'UNIQUE': 'Google Sheets has different syntax',
            'SEQUENCE': 'Google Sheets uses different function',
            'RANDARRAY': 'Google Sheets uses different function'
        }

        issues_found = []

        for func, count in self.formula_functions.items():
            if func in incompatible_functions:
                issues_found.append({
                    'function': func,
                    'count': count,
                    'recommendation': incompatible_functions[func]
                })

        if not issues_found:
            print("✅ FULLY COMPATIBLE with Google Sheets")
            print("\nAll functions used are compatible:")
            for func in self.formula_functions.keys():
                print(f"  ✓ {func}")
        else:
            print("⚠️  POTENTIAL COMPATIBILITY ISSUES")
            print("\nIncompatible Functions:")
            for issue in issues_found:
                print(f"  ✗ {issue['function']} ({issue['count']} uses)")
                print(f"    Recommendation: {issue['recommendation']}")

        return len(issues_found)

    def analyze_formula_examples(self):
        """Show example formulas from each sheet"""
        print("\n" + "=" * 80)
        print("FORMULA EXAMPLES BY WORKSHEET")
        print("=" * 80)

        for sheet_name in self.wb.sheetnames:
            ws = self.wb[sheet_name]
            formulas_shown = 0

            print(f"\n{sheet_name}:")
            print("-" * 80)

            for row in ws.iter_rows():
                for cell in row:
                    if cell.value and isinstance(cell.value, str) and cell.value.startswith('='):
                        if formulas_shown < 3:  # Show first 3 formulas
                            print(f"  {cell.coordinate}: {cell.value}")
                            formulas_shown += 1

            if formulas_shown == 0:
                print("  (No formulas in this sheet)")

    def validate_revenue_calculations(self):
        """Validate revenue calculation logic"""
        print("\n" + "=" * 80)
        print("REVENUE CALCULATION VALIDATION")
        print("=" * 80)

        if "Revenue" not in self.wb.sheetnames:
            print("⚠️  No Revenue sheet found")
            return

        ws = self.wb["Revenue"]

        print("\nRevenue Formula Structure:")
        print("-" * 80)

        # Check revenue formulas
        revenue_formulas = []
        for row in ws.iter_rows(min_row=4):
            cell = row[1] if len(row) > 1 else None  # Column B
            if cell and cell.value and isinstance(cell.value, str) and cell.value.startswith('='):
                revenue_formulas.append({
                    'row': cell.row,
                    'formula': cell.value
                })

        if revenue_formulas:
            print(f"Revenue formulas found: {len(revenue_formulas)}")
            for rf in revenue_formulas[:5]:
                print(f"  Row {rf['row']}: {rf['formula'][:70]}...")

            # Check for common patterns
            has_assumptions_ref = any('Assumptions!' in rf['formula'] for rf in revenue_formulas)
            has_calculations_ref = any('Calculations!' in rf['formula'] for rf in revenue_formulas)

            if has_assumptions_ref:
                print("\n✓ Revenue formulas reference Assumptions sheet")
            if has_calculations_ref:
                print("✓ Revenue formulas reference Calculations sheet")
        else:
            print("⚠️  No revenue formulas detected")

    def check_number_formatting(self):
        """Check number formatting consistency"""
        print("\n" + "=" * 80)
        print("NUMBER FORMATTING CHECK")
        print("=" * 80)

        format_counts = defaultdict(int)

        for sheet_name in self.wb.sheetnames:
            ws = self.wb[sheet_name]
            for row in ws.iter_rows():
                for cell in row:
                    if cell.value is not None and not isinstance(cell.value, str):
                        format_counts[cell.number_format] += 1

        print("\nNumber Formats Used:")
        print("-" * 80)
        for fmt, count in sorted(format_counts.items(), key=lambda x: -x[1])[:10]:
            print(f"  {fmt}: {count} cells")

    def generate_recommendations(self):
        """Generate recommendations for model improvements"""
        print("\n" + "=" * 80)
        print("RECOMMENDATIONS FOR ENHANCEMENT")
        print("=" * 80)

        recommendations = []

        # Check for missing worksheets
        expected_sheets = ['Dashboard', 'Assumptions', 'Calculations', 'Revenue',
                          'Operating Costs', 'CAPEX Schedule', 'Debt Schedule',
                          'P&L Statement', 'Cash Flow', 'Balance Sheet',
                          'Returns Analysis', 'Sensitivity Analysis']

        missing = [s for s in expected_sheets if s not in self.wb.sheetnames]

        if missing:
            recommendations.append({
                'priority': 'HIGH',
                'category': 'Structure',
                'recommendation': f'Add missing worksheets: {", ".join(missing)}'
            })

        # Check current worksheets
        current = self.wb.sheetnames
        if len(current) < 10:
            recommendations.append({
                'priority': 'MEDIUM',
                'category': 'Completeness',
                'recommendation': f'Model has only {len(current)} worksheets. Consider expanding to include P&L, Cash Flow, Balance Sheet, and analysis sheets'
            })

        # Check for IRR/NPV calculations
        has_irr = 'IRR' in self.formula_functions or 'XIRR' in self.formula_functions
        has_npv = 'NPV' in self.formula_functions or 'XNPV' in self.formula_functions

        if not has_irr:
            recommendations.append({
                'priority': 'HIGH',
                'category': 'Financial Metrics',
                'recommendation': 'Add IRR calculation for investment returns analysis'
            })

        if not has_npv:
            recommendations.append({
                'priority': 'HIGH',
                'category': 'Financial Metrics',
                'recommendation': 'Add NPV calculation for project valuation'
            })

        # Print recommendations
        if recommendations:
            print("\nPriority Recommendations:")
            print("-" * 80)

            for rec in sorted(recommendations, key=lambda x: x['priority']):
                print(f"\n[{rec['priority']}] {rec['category']}")
                print(f"  → {rec['recommendation']}")
        else:
            print("\n✅ No critical recommendations - model structure is appropriate for current scope")

        # Always suggest enhancements
        print("\n\nSuggested Enhancements for DFI Investment Proposal:")
        print("-" * 80)
        enhancements = [
            "1. Add detailed P&L Statement with EBITDA calculations",
            "2. Add Cash Flow Statement with debt service coverage",
            "3. Add Balance Sheet with asset/liability tracking",
            "4. Add Debt Schedule with amortization table",
            "5. Add Returns Analysis (IRR, NPV, DSCR, payback period)",
            "6. Add Sensitivity Analysis dashboard",
            "7. Add Development Impact metrics (jobs, farmer income)",
            "8. Add Charts/Visualizations for executive presentation",
            "9. Add Scenario comparison (Base/Conservative/Optimistic)",
            "10. Add Documentation/Instructions worksheet"
        ]

        for enhancement in enhancements:
            print(f"  {enhancement}")

        return recommendations

    def run_detailed_audit(self):
        """Execute detailed audit"""
        print("\n" + "╔" + "=" * 78 + "╗")
        print("║" + " " * 20 + "DETAILED TECHNICAL ANALYSIS" + " " * 31 + "║")
        print("╚" + "=" * 78 + "╝")

        self.analyze_formula_patterns()
        self.check_google_sheets_compatibility()
        self.analyze_formula_examples()
        self.validate_revenue_calculations()
        self.check_number_formatting()
        self.generate_recommendations()

if __name__ == "__main__":
    auditor = DetailedAuditor("Financial_Model_Agricultural_Processing.xlsx")
    auditor.run_detailed_audit()
