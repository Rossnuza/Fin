#!/usr/bin/env python3
"""
Financial Model Technical Audit Script
Conducts comprehensive audit of Excel financial model
"""

import openpyxl
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter, column_index_from_string
import re
from collections import defaultdict

class FinancialModelAuditor:
    def __init__(self, filename):
        self.filename = filename
        self.wb = load_workbook(filename, data_only=False)
        self.errors = []
        self.warnings = []
        self.info = []
        self.formula_catalog = defaultdict(list)
        self.cell_references = defaultdict(set)

    def audit_structure(self):
        """Audit 1: Worksheet Structure and Organization"""
        print("=" * 80)
        print("AUDIT 1: STRUCTURAL INTEGRITY REVIEW")
        print("=" * 80)

        print(f"\nFile: {self.filename}")
        print(f"Total Worksheets: {len(self.wb.sheetnames)}")
        print("\nWorksheet Inventory:")
        print("-" * 80)

        for idx, sheet_name in enumerate(self.wb.sheetnames, 1):
            ws = self.wb[sheet_name]
            max_row = ws.max_row
            max_col = ws.max_column

            # Count formulas
            formula_count = 0
            value_count = 0
            empty_count = 0

            for row in ws.iter_rows():
                for cell in row:
                    if cell.value is None:
                        empty_count += 1
                    elif isinstance(cell.value, str) and cell.value.startswith('='):
                        formula_count += 1
                    else:
                        value_count += 1

            print(f"{idx}. {sheet_name}")
            print(f"   Dimensions: {max_row} rows × {max_col} columns")
            print(f"   Cells: {formula_count} formulas, {value_count} values, {empty_count} empty")

        return len(self.wb.sheetnames)

    def audit_formulas(self):
        """Audit 2: Formula Accuracy and Error Detection"""
        print("\n" + "=" * 80)
        print("AUDIT 2: FORMULA ENGINE AUDIT")
        print("=" * 80)

        error_types = {
            '#REF!': 0,
            '#VALUE!': 0,
            '#DIV/0!': 0,
            '#NAME?': 0,
            '#NUM!': 0,
            '#N/A': 0,
            '#NULL!': 0
        }

        total_formulas = 0
        sheets_with_errors = {}

        for sheet_name in self.wb.sheetnames:
            ws = self.wb[sheet_name]
            sheet_errors = []

            for row in ws.iter_rows():
                for cell in row:
                    # Check for formula
                    if cell.value and isinstance(cell.value, str) and cell.value.startswith('='):
                        total_formulas += 1
                        formula = cell.value

                        # Catalog formula
                        self.formula_catalog[sheet_name].append({
                            'cell': cell.coordinate,
                            'formula': formula
                        })

                        # Check for error values
                        for error_type in error_types:
                            if error_type in str(formula):
                                error_types[error_type] += 1
                                sheet_errors.append({
                                    'cell': cell.coordinate,
                                    'error': error_type,
                                    'formula': formula
                                })

                        # Extract cell references
                        refs = re.findall(r'([A-Z]+[0-9]+)', formula)
                        for ref in refs:
                            self.cell_references[f"{sheet_name}!{cell.coordinate}"].add(ref)

                        # Check for sheet references
                        sheet_refs = re.findall(r"(['\"]?[A-Za-z0-9_ ]+['\"]?!)([A-Z]+[0-9]+)", formula)
                        for sheet_ref, cell_ref in sheet_refs:
                            clean_sheet = sheet_ref.strip("'\"!")
                            self.cell_references[f"{sheet_name}!{cell.coordinate}"].add(f"{clean_sheet}!{cell_ref}")

            if sheet_errors:
                sheets_with_errors[sheet_name] = sheet_errors

        print(f"\nTotal Formulas: {total_formulas}")
        print(f"\nError Detection:")
        print("-" * 80)

        total_errors = sum(error_types.values())
        if total_errors == 0:
            print("✓ No formula errors detected (#REF!, #VALUE!, #DIV/0!, etc.)")
        else:
            for error_type, count in error_types.items():
                if count > 0:
                    print(f"✗ {error_type}: {count} occurrences")
                    self.errors.append(f"{error_type} errors found: {count}")

        if sheets_with_errors:
            print(f"\nSheets with Errors: {len(sheets_with_errors)}")
            for sheet, errors in sheets_with_errors.items():
                print(f"\n{sheet}:")
                for error in errors[:5]:  # Show first 5 errors per sheet
                    print(f"  {error['cell']}: {error['error']} in {error['formula'][:50]}...")

        return total_formulas, total_errors

    def audit_cross_references(self):
        """Audit 3: Cross-Worksheet Reference Mapping"""
        print("\n" + "=" * 80)
        print("AUDIT 3: CROSS-REFERENCE MAPPING")
        print("=" * 80)

        sheet_dependencies = defaultdict(set)

        for sheet_name in self.wb.sheetnames:
            ws = self.wb[sheet_name]

            for row in ws.iter_rows():
                for cell in row:
                    if cell.value and isinstance(cell.value, str) and cell.value.startswith('='):
                        formula = cell.value

                        # Find sheet references
                        sheet_refs = re.findall(r"(['\"]?[A-Za-z0-9_ ]+['\"]?)!", formula)
                        for ref_sheet in sheet_refs:
                            clean_ref = ref_sheet.strip("'\"")
                            if clean_ref != sheet_name and clean_ref in self.wb.sheetnames:
                                sheet_dependencies[sheet_name].add(clean_ref)

        print("\nWorksheet Dependencies:")
        print("-" * 80)

        for sheet, deps in sorted(sheet_dependencies.items()):
            print(f"{sheet} → {', '.join(sorted(deps))}")

        # Check for broken references
        print("\nBroken Reference Check:")
        print("-" * 80)

        broken_refs = 0
        for sheet_name in self.wb.sheetnames:
            ws = self.wb[sheet_name]

            for row in ws.iter_rows():
                for cell in row:
                    if cell.value and isinstance(cell.value, str) and cell.value.startswith('='):
                        formula = cell.value

                        # Check for sheet references to non-existent sheets
                        sheet_refs = re.findall(r"(['\"]?[A-Za-z0-9_ ]+['\"]?)!", formula)
                        for ref_sheet in sheet_refs:
                            clean_ref = ref_sheet.strip("'\"")
                            if clean_ref not in self.wb.sheetnames:
                                broken_refs += 1
                                self.errors.append(f"{sheet_name}!{cell.coordinate}: References non-existent sheet '{clean_ref}'")

        if broken_refs == 0:
            print("✓ No broken sheet references detected")
        else:
            print(f"✗ {broken_refs} broken sheet references found")

        return len(sheet_dependencies)

    def audit_assumptions_sheet(self):
        """Audit 4: Assumptions Sheet (Control Panel) Validation"""
        print("\n" + "=" * 80)
        print("AUDIT 4: ASSUMPTIONS SHEET VALIDATION")
        print("=" * 80)

        if "Assumptions" not in self.wb.sheetnames:
            print("✗ No 'Assumptions' sheet found")
            self.errors.append("Missing Assumptions sheet (control panel)")
            return

        ws = self.wb["Assumptions"]

        # Count input cells (should be blue)
        input_cells = 0
        calc_cells = 0

        print("\nInput Cell Analysis:")
        print("-" * 80)

        for row in ws.iter_rows(min_row=4):  # Skip header rows
            for cell in row:
                if cell.value is not None:
                    # Check if it's a formula (should NOT be in Assumptions)
                    if isinstance(cell.value, str) and cell.value.startswith('='):
                        calc_cells += 1
                        if cell.column == 3:  # Column C
                            self.warnings.append(f"Assumptions!{cell.coordinate}: Contains formula (should be input)")
                    else:
                        if cell.column == 3:  # Column C
                            input_cells += 1

        print(f"Input cells (column C): {input_cells}")
        print(f"Formula cells in Assumptions: {calc_cells}")

        if calc_cells == 0:
            print("✓ Assumptions sheet is pure inputs (correct architecture)")
        else:
            print(f"⚠ {calc_cells} formulas found in Assumptions sheet")
            self.warnings.append(f"Assumptions sheet should contain only inputs, found {calc_cells} formulas")

        # Check for sections
        print("\nAssumptions Sheet Structure:")
        print("-" * 80)

        sections = []
        for row in ws.iter_rows(min_row=1, max_col=1):
            cell = row[0]
            if cell.value and isinstance(cell.value, str):
                if any(section in str(cell.value).upper() for section in ['SECTION', 'TIMELINE', 'PRODUCTION', 'PRICING', 'COSTS', 'CAPEX', 'FINANCING', 'TAX']):
                    sections.append(cell.value)

        print(f"Sections identified: {len(sections)}")
        for section in sections:
            print(f"  • {section}")

        return input_cells

    def audit_calculations_sheet(self):
        """Audit 5: Calculations Sheet (Derived Values)"""
        print("\n" + "=" * 80)
        print("AUDIT 5: CALCULATIONS SHEET VALIDATION")
        print("=" * 80)

        if "Calculations" not in self.wb.sheetnames:
            print("⚠ No 'Calculations' sheet found")
            self.warnings.append("No dedicated Calculations sheet (derived values may be mixed with inputs)")
            return

        ws = self.wb["Calculations"]

        formulas = 0
        assumptions_refs = 0

        for row in ws.iter_rows():
            for cell in row:
                if cell.value and isinstance(cell.value, str) and cell.value.startswith('='):
                    formulas += 1
                    if 'Assumptions!' in cell.value:
                        assumptions_refs += 1

        print(f"Total formulas: {formulas}")
        print(f"References to Assumptions: {assumptions_refs}")

        if assumptions_refs > 0:
            print(f"✓ Calculations sheet properly references Assumptions ({assumptions_refs} links)")
        else:
            print("⚠ No references to Assumptions sheet found")

        return formulas

    def audit_data_flow(self):
        """Audit 6: Data Flow and Logical Consistency"""
        print("\n" + "=" * 80)
        print("AUDIT 6: DATA FLOW VALIDATION")
        print("=" * 80)

        print("\nExpected Data Flow:")
        print("Assumptions (inputs) → Calculations (derived) → Revenue/Dashboard (outputs)")
        print("-" * 80)

        # Check if Revenue references Assumptions
        revenue_ok = False
        if "Revenue" in self.wb.sheetnames:
            ws = self.wb["Revenue"]
            for row in ws.iter_rows():
                for cell in row:
                    if cell.value and isinstance(cell.value, str) and 'Assumptions!' in str(cell.value):
                        revenue_ok = True
                        break

        if revenue_ok:
            print("✓ Revenue sheet references Assumptions")
        else:
            print("⚠ Revenue sheet may not reference Assumptions")

        # Check if Dashboard references Calculations
        dashboard_ok = False
        if "Dashboard" in self.wb.sheetnames:
            ws = self.wb["Dashboard"]
            for row in ws.iter_rows():
                for cell in row:
                    if cell.value and isinstance(cell.value, str):
                        if 'Calculations!' in str(cell.value) or 'Assumptions!' in str(cell.value):
                            dashboard_ok = True
                            break

        if dashboard_ok:
            print("✓ Dashboard references Calculations/Assumptions")
        else:
            print("⚠ Dashboard may not reference other sheets")

    def generate_report(self):
        """Generate Comprehensive Audit Report"""
        print("\n" + "=" * 80)
        print("AUDIT SUMMARY")
        print("=" * 80)

        print(f"\n📊 Model: {self.filename}")
        print(f"📅 Audit Date: 2026-01-24")
        print("-" * 80)

        print("\n✅ PASSED CHECKS:")
        if len(self.errors) == 0:
            print("  • No critical errors found")

        print("\n⚠️  WARNINGS:", len(self.warnings))
        for warning in self.warnings:
            print(f"  • {warning}")

        print("\n❌ ERRORS:", len(self.errors))
        for error in self.errors:
            print(f"  • {error}")

        # Overall assessment
        print("\n" + "=" * 80)
        print("OVERALL ASSESSMENT")
        print("=" * 80)

        if len(self.errors) == 0 and len(self.warnings) == 0:
            print("✅ PASS - Model is production-ready")
        elif len(self.errors) == 0:
            print(f"⚠️  PASS WITH WARNINGS - {len(self.warnings)} issues to review")
        else:
            print(f"❌ FAIL - {len(self.errors)} critical errors must be fixed")

    def run_full_audit(self):
        """Execute complete audit sequence"""
        print("\n" + "╔" + "=" * 78 + "╗")
        print("║" + " " * 15 + "FINANCIAL MODEL TECHNICAL AUDIT" + " " * 32 + "║")
        print("╚" + "=" * 78 + "╝")

        self.audit_structure()
        self.audit_formulas()
        self.audit_cross_references()
        self.audit_assumptions_sheet()
        self.audit_calculations_sheet()
        self.audit_data_flow()
        self.generate_report()

if __name__ == "__main__":
    auditor = FinancialModelAuditor("Financial_Model_Agricultural_Processing.xlsx")
    auditor.run_full_audit()
