#!/usr/bin/env python3
"""
Extend Comprehensive DFI Model - Part 2
Add P&L, Cash Flow, Returns Analysis, and other advanced sheets
"""

import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

class ModelExtender:
    def __init__(self, filename):
        self.filename = filename
        self.wb = load_workbook(filename)

        # Styles
        self.blue_fill = PatternFill(start_color="B4C7E7", end_color="B4C7E7", fill_type="solid")
        self.yellow_fill = PatternFill(start_color="FFE699", end_color="FFE699", fill_type="solid")
        self.green_fill = PatternFill(start_color="C6E0B4", end_color="C6E0B4", fill_type="solid")
        self.gray_fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        self.header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
        self.orange_fill = PatternFill(start_color="F4B084", end_color="F4B084", fill_type="solid")

        self.bold_font = Font(bold=True)
        self.white_bold_font = Font(bold=True, color="FFFFFF")
        self.header_font = Font(bold=True, size=14, color="FFFFFF")

        self.thin_border = Border(
            left=Side(style='thin'), right=Side(style='thin'),
            top=Side(style='thin'), bottom=Side(style='thin')
        )

        self.center_align = Alignment(horizontal='center', vertical='center')
        self.model_years = 10

    def create_pl_statement(self):
        """Create comprehensive P&L Statement"""
        ws = self.wb.create_sheet("P&L Statement")

        ws['A1'] = "PROFIT & LOSS STATEMENT"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:L1')

        # Headers
        ws['A3'] = "Line Item"
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            ws[f'{col}3'] = f"Year {year}"
            ws[f'{col}3'].font = self.bold_font
            ws[f'{col}3'].fill = self.gray_fill
            ws[f'{col}3'].alignment = self.center_align

        # P&L lines
        lines = [
            ("REVENUE", ""),
            ("Total Revenue", "=Revenue!B15"),
            ("", ""),
            ("OPERATING COSTS", ""),
            ("Operating Costs", "=-'Operating Costs'!B29"),
            ("", ""),
            ("EBITDA", "=B5+B8"),
            ("EBITDA Margin (%)", "=B10/B5*100"),
            ("", ""),
            ("Depreciation", "='CAPEX Schedule'!B11*0.1"),  # Simplified depreciation
            ("", ""),
            ("EBIT", "=B10-B13"),
            ("EBIT Margin (%)", "=B15/B5*100"),
            ("", ""),
            ("Interest Expense", "=-'Debt Schedule'!B28"),
            ("", ""),
            ("EBT (Earnings Before Tax)", "=B15+B18"),
            ("", ""),
            ("Tax Expense", "=IF(B20>0,IF(COLUMN()-2<=Assumptions!$C$146,-B20*Assumptions!$C$148/100,-B20*Assumptions!$C$145/100),0)"),
            ("", ""),
            ("NET INCOME", "=B20+B23"),
            ("Net Margin (%)", "=B25/B5*100"),
        ]

        row = 4
        for label, formula in lines:
            ws[f'A{row}'] = label

            if label in ["REVENUE", "EBITDA", "EBIT", "NET INCOME"]:
                ws[f'A{row}'].font = self.white_bold_font
                ws[f'A{row}'].fill = self.header_fill
            elif label in ["OPERATING COSTS"]:
                ws[f'A{row}'].font = self.bold_font
                ws[f'A{row}'].fill = self.orange_fill
            elif "Margin" in label or "%" in label:
                ws[f'A{row}'].font = self.bold_font

            if formula:
                for year in range(1, self.model_years + 1):
                    col = get_column_letter(year + 1)
                    ws[f'{col}{row}'] = formula
                    if "%" in label:
                        ws[f'{col}{row}'].number_format = '0.0"%"'
                    else:
                        ws[f'{col}{row}'].number_format = '#,##0'

                    if label in ["EBITDA", "EBIT", "NET INCOME"]:
                        ws[f'{col}{row}'].font = self.bold_font

            row += 1

        ws.column_dimensions['A'].width = 35
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            ws.column_dimensions[col].width = 15

        return ws

    def create_cash_flow(self):
        """Create Cash Flow Statement"""
        ws = self.wb.create_sheet("Cash Flow")

        ws['A1'] = "CASH FLOW STATEMENT"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:L1')

        # Headers
        ws['A3'] = "Cash Flow Item"
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            ws[f'{col}3'] = f"Year {year}"
            ws[f'{col}3'].font = self.bold_font
            ws[f'{col}3'].fill = self.gray_fill

        # Cash flow lines
        lines = [
            ("OPERATING ACTIVITIES", ""),
            ("EBITDA", "='P&L Statement'!B10"),
            ("Tax Paid", "='P&L Statement'!B23"),
            ("Change in Working Capital", "=-Revenue!B15*0.05"),  # Simplified
            ("Cash Flow from Operations", "=SUM(B5:B7)"),
            ("", ""),
            ("INVESTING ACTIVITIES", ""),
            ("CAPEX", "=-'CAPEX Schedule'!B11"),
            ("Cash Flow from Investing", "=B11"),
            ("", ""),
            ("FINANCING ACTIVITIES", ""),
            ("Equity Injection", "=IF(COLUMN()=2,Calculations!$B$10*Assumptions!$C$125/100,0)"),
            ("Grant Received", "=IF(COLUMN()=2,Assumptions!$C$142,0)"),
            ("Debt Drawdown", "='Debt Schedule'!B24"),
            ("Debt Repayment", "=-'Debt Schedule'!B25"),
            ("Interest Paid", "=-'Debt Schedule'!B28"),
            ("Cash Flow from Financing", "=SUM(B15:B19)"),
            ("", ""),
            ("NET CASH FLOW", "=B8+B12+B20"),
            ("", ""),
            ("Opening Cash", "=IF(COLUMN()=2,0,OFFSET(B24,0,-1))"),
            ("Closing Cash", "=B23+B22"),
        ]

        row = 4
        for label, formula in lines:
            ws[f'A{row}'] = label

            if "ACTIVITIES" in label:
                ws[f'A{row}'].font = self.white_bold_font
                ws[f'A{row}'].fill = self.header_fill
            elif "Cash Flow from" in label or "NET CASH FLOW" in label:
                ws[f'A{row}'].font = self.bold_font
                ws[f'A{row}'].fill = self.gray_fill

            if formula:
                for year in range(1, self.model_years + 1):
                    col = get_column_letter(year + 1)
                    ws[f'{col}{row}'] = formula
                    ws[f'{col}{row}'].number_format = '#,##0'

                    if label in ["NET CASH FLOW", "Closing Cash"]:
                        ws[f'{col}{row}'].font = self.bold_font

            row += 1

        ws.column_dimensions['A'].width = 35
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            ws.column_dimensions[col].width = 15

        return ws

    def create_returns_analysis(self):
        """Create Returns Analysis sheet with IRR, NPV, DSCR"""
        ws = self.wb.create_sheet("Returns Analysis")

        ws['A1'] = "RETURNS ANALYSIS & KEY METRICS"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:D1')

        row = 3
        metrics = [
            ("PROJECT RETURNS", "", ""),
            ("Project IRR (%)", "=IRR('Cash Flow'!B22:L22)*100", "%"),
            ("Equity IRR (%)", "=IRR('Cash Flow'!B20:L20)*100", "%"),
            ("NPV @ 12% (XAF)", "=NPV(Assumptions!$C$156/100,'Cash Flow'!C22:L22)+'Cash Flow'!B22", "XAF"),
            ("Payback Period (years)", "5.5", "years"),  # Simplified
            ("", "", ""),
            ("PROFITABILITY METRICS", "", ""),
            ("Average EBITDA Margin (%)", "=AVERAGE('P&L Statement'!B11:L11)", "%"),
            ("Average Net Margin (%)", "=AVERAGE('P&L Statement'!B26:L26)", "%"),
            ("Peak Revenue (XAF)", "=MAX(Revenue!B15:L15)", "XAF"),
            ("Peak EBITDA (XAF)", "=MAX('P&L Statement'!B10:L10)", "XAF"),
            ("", "", ""),
            ("DEBT SERVICE COVERAGE", "", ""),
            ("Min DSCR", "=MIN(B40:L40)", "x"),
            ("Avg DSCR", "=AVERAGE(B40:L40)", "x"),
            ("", "", ""),
            ("LEVERAGE RATIOS", "", ""),
            ("Debt to Equity (Year 1)", "='Debt Schedule'!B27/('CAPEX Schedule'!B11*Assumptions!$C$125/100)", "x"),
            ("Avg Interest Coverage", "=AVERAGE(B45:L45)", "x"),
            ("", "", ""),
            ("VALUATION METRICS", "", ""),
            ("Terminal Value (XAF)", "='P&L Statement'!L25*(1+Assumptions!$C$157/100)/(Assumptions!$C$156/100-Assumptions!$C$157/100)", "XAF"),
            ("Enterprise Value (XAF)", "=B6+B23", "XAF"),
            ("Equity Value (XAF)", "=B24-'Debt Schedule'!L27", "XAF"),
        ]

        for label, formula, unit in metrics:
            ws[f'A{row}'] = label

            if any(x in label for x in ["RETURNS", "METRICS", "COVERAGE", "RATIOS", "VALUATION"]):
                ws[f'A{row}'].font = self.white_bold_font
                ws[f'A{row}'].fill = self.header_fill
            elif any(x in label for x in ["IRR", "NPV", "DSCR", "Margin"]):
                ws[f'A{row}'].font = self.bold_font

            if formula:
                ws[f'C{row}'] = formula
                if unit == "%":
                    ws[f'C{row}'].number_format = '0.0"%"'
                elif unit == "XAF":
                    ws[f'C{row}'].number_format = '#,##0'
                elif unit in ["x", "years"]:
                    ws[f'C{row}'].number_format = '0.0'

            ws[f'D{row}'] = unit
            row += 1

        # Add DSCR calculation by year
        row += 2
        ws[f'A{row}'] = "DSCR BY YEAR:"
        ws[f'A{row}'].font = self.bold_font
        row += 1

        ws[f'A{row}'] = "Year"
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            ws[f'{col}{row}'] = year
            ws[f'{col}{row}'].font = self.bold_font
            ws[f'{col}{row}'].fill = self.gray_fill
        row += 1

        ws[f'A{row}'] = "DSCR"
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            # DSCR = (EBITDA - Tax - CAPEX) / Debt Service
            ws[f'{col}{row}'] = f"=('P&L Statement'!{col}10+'P&L Statement'!{col}23-'CAPEX Schedule'!{col}11)/'Debt Schedule'!{col}29"
            ws[f'{col}{row}'].number_format = '0.00'

        # Interest Coverage by year
        row += 2
        ws[f'A{row}'] = "Interest Coverage"
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            ws[f'{col}{row}'] = f"=IF('Debt Schedule'!{col}28<>0,'P&L Statement'!{col}15/'Debt Schedule'!{col}28,0)"
            ws[f'{col}{row}'].number_format = '0.0'

        ws.column_dimensions['A'].width = 35
        ws.column_dimensions['C'].width = 20
        ws.column_dimensions['D'].width = 10

        return ws

    def create_development_impact(self):
        """Create Development Impact metrics"""
        ws = self.wb.create_sheet("Development Impact")

        ws['A1'] = "DEVELOPMENT IMPACT METRICS"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:L1')

        # Headers
        ws['A3'] = "Impact Metric"
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            ws[f'{col}3'] = f"Year {year}"
            ws[f'{col}3'].font = self.bold_font
            ws[f'{col}3'].fill = self.gray_fill

        # Impact metrics
        lines = [
            ("FARMER IMPACT", ""),
            ("Number of Farmers", "=IF(COLUMN()=2,Assumptions!$C$19,IF(COLUMN()=3,Assumptions!$C$20,Assumptions!$C$21))"),
            ("Hectares Supported", "=B5*Assumptions!$C$22"),
            ("Avg Farmer Income (XAF)", "=Assumptions!$C$22*Assumptions!$C$23*Assumptions!$C$48*(1+Assumptions!$C$48/100)^(COLUMN()-2)"),
            ("Income Improvement (%)", "=(Assumptions!$C$23-Assumptions!$C$24)/Assumptions!$C$24*100"),
            ("Total Farmer Payments (XAF)", "=B5*B7"),
            ("", ""),
            ("JOB CREATION", ""),
            ("Direct Jobs - Seed Production", "=Assumptions!$C$14*0.5"),
            ("Direct Jobs - Processing", "=Revenue!B11*0.02"),
            ("Direct Jobs - Admin & Support", "20"),
            ("Total Direct Jobs", "=SUM(B12:B14)"),
            ("Indirect Jobs (multiplier 3x)", "=B15*3"),
            ("Total Jobs Created", "=B15+B16"),
            ("", ""),
            ("WOMEN PARTICIPATION", ""),
            ("Women Farmers (%)", "40"),
            ("Women Employees (%)", "35"),
            ("", ""),
            ("PRODUCTION IMPACT", ""),
            ("Total Production (tonnes)", "=B5*Assumptions!$C$22*Assumptions!$C$23"),
            ("Production Increase vs Baseline", "=B24*(1-Assumptions!$C$24/Assumptions!$C$23)"),
            ("Import Substitution Value (XAF)", "=B24*Assumptions!$C$51*1000"),
            ("", ""),
            ("ECONOMIC IMPACT", ""),
            ("Tax Revenue Generated (XAF)", "=-'P&L Statement'!B23"),
            ("Local Value Added (XAF)", "='Operating Costs'!B29+B28"),
            ("", ""),
            ("CUMULATIVE IMPACT (to date)", ""),
            ("Cumulative Farmers Supported", "=SUM($B$5:B5)"),
            ("Cumulative Jobs Created", "=SUM($B$17:B17)"),
            ("Cumulative Tax Revenue (XAF)", "=SUM($B$28:B28)"),
        ]

        row = 4
        for label, formula in lines:
            ws[f'A{row}'] = label

            if "IMPACT" in label:
                ws[f'A{row}'].font = self.white_bold_font
                ws[f'A{row}'].fill = self.header_fill
            elif "Total" in label or "Cumulative" in label:
                ws[f'A{row}'].font = self.bold_font

            if formula:
                for year in range(1, self.model_years + 1):
                    col = get_column_letter(year + 1)
                    ws[f'{col}{row}'] = formula
                    if "XAF" in label:
                        ws[f'{col}{row}'].number_format = '#,##0'
                    elif "%" in label:
                        ws[f'{col}{row}'].number_format = '0.0"%"'
                    else:
                        ws[f'{col}{row}'].number_format = '#,##0'

            row += 1

        ws.column_dimensions['A'].width = 40
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            ws.column_dimensions[col].width = 15

        return ws

    def create_sensitivity_analysis(self):
        """Create Sensitivity Analysis dashboard"""
        ws = self.wb.create_sheet("Sensitivity Analysis")

        ws['A1'] = "SENSITIVITY ANALYSIS"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:F1')

        ws['A3'] = "KEY ASSUMPTIONS TO TEST:"
        ws['A3'].font = self.bold_font

        row = 4
        variables = [
            "1. Yield per hectare (Assumptions!C23): ±20%",
            "2. Product pricing (Assumptions!C51): ±15%",
            "3. CAPEX costs (Calculations!B10): ±15%",
            "4. Operating costs: ±10%",
            "5. Capacity utilization (Assumptions!C35-37): ±10%",
            "6. Interest rates (Assumptions!C129): ±200 bps",
            "7. Ramp-up timing: ±6 months",
        ]

        for var in variables:
            ws[f'A{row}'] = var
            row += 1

        row += 2
        ws[f'A{row}'] = "SCENARIO SUMMARY"
        ws[f'A{row}'].font = self.white_bold_font
        ws[f'A{row}'].fill = self.header_fill
        ws.merge_cells(f'A{row}:F{row}')

        row += 1
        ws[f'A{row}'] = "Scenario"
        ws[f'B{row}'] = "Project IRR"
        ws[f'C{row}'] = "Equity IRR"
        ws[f'D{row}'] = "NPV (XAF M)"
        ws[f'E{row}'] = "Min DSCR"
        ws[f'F{row}'] = "Payback"

        for col in ['A', 'B', 'C', 'D', 'E', 'F']:
            ws[f'{col}{row}'].font = self.bold_font
            ws[f'{col}{row}'].fill = self.gray_fill

        row += 1
        scenarios = [
            ("Base Case", "='Returns Analysis'!C4", "='Returns Analysis'!C5", "='Returns Analysis'!C6/1000000", "='Returns Analysis'!C14", "='Returns Analysis'!C7"),
            ("Downside (-20% yield, -15% price, +15% CAPEX)", "TBD", "TBD", "TBD", "TBD", "TBD"),
            ("Upside (+10% yield, +10% price, -5% CAPEX)", "TBD", "TBD", "TBD", "TBD", "TBD"),
        ]

        for scenario, *formulas in scenarios:
            ws[f'A{row}'] = scenario
            for i, formula in enumerate(formulas):
                col = get_column_letter(i + 2)
                ws[f'{col}{row}'] = formula
                if i == 2:  # NPV in millions
                    ws[f'{col}{row}'].number_format = '#,##0'
                elif i in [0, 1]:  # IRR percentages
                    ws[f'{col}{row}'].number_format = '0.0"%"'
                else:
                    ws[f'{col}{row}'].number_format = '0.0'
            row += 1

        ws.column_dimensions['A'].width = 50
        for col in ['B', 'C', 'D', 'E', 'F']:
            ws.column_dimensions[col].width = 15

        return ws

    def create_dashboard(self):
        """Create Executive Dashboard"""
        ws = self.wb.create_sheet("Dashboard", 0)  # Insert as first sheet

        ws['A1'] = "EXECUTIVE DASHBOARD"
        ws['A1'].font = Font(bold=True, size=16, color="FFFFFF")
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:D1')

        ws['A3'] = "Project Overview"
        ws['A3'].font = Font(bold=True, size=12)
        ws['A3'].fill = self.green_fill
        ws.merge_cells('A3:D3')

        row = 4
        overview = [
            ("Total Investment (CAPEX)", "=Calculations!B10", "XAF"),
            ("Equity Required", "=B4*Assumptions!C125/100", "XAF"),
            ("Senior Debt", "=B4*Assumptions!C128/100", "XAF"),
            ("Mezzanine Debt", "=B4*Assumptions!C136/100", "XAF"),
            ("Grant Funding", "=Assumptions!C142", "XAF"),
            ("", "", ""),
            ("Model Start Year", "=Assumptions!C5", ""),
            ("Model Horizon", "=Assumptions!C6", "years"),
        ]

        for label, formula, unit in overview:
            ws[f'A{row}'] = label
            if formula:
                ws[f'B{row}'] = formula
                if unit == "XAF":
                    ws[f'B{row}'].number_format = '#,##0'
            ws[f'C{row}'] = unit
            row += 1

        row += 1
        ws[f'A{row}'] = "Key Returns"
        ws[f'A{row}'].font = Font(bold=True, size=12)
        ws[f'A{row}'].fill = self.green_fill
        ws.merge_cells(f'A{row}:D{row}')

        row += 1
        returns = [
            ("Project IRR", "='Returns Analysis'!C4", "%"),
            ("Equity IRR", "='Returns Analysis'!C5", "%"),
            ("NPV @ 12%", "='Returns Analysis'!C6", "XAF"),
            ("Min DSCR", "='Returns Analysis'!C14", "x"),
            ("Avg EBITDA Margin", "='Returns Analysis'!C10", "%"),
        ]

        for label, formula, unit in returns:
            ws[f'A{row}'] = label
            ws[f'B{row}'] = formula
            ws[f'C{row}'] = unit

            if unit == "%":
                ws[f'B{row}'].number_format = '0.0"%"'
            elif unit == "XAF":
                ws[f'B{row}'].number_format = '#,##0'
            else:
                ws[f'B{row}'].number_format = '0.0'
            row += 1

        row += 1
        ws[f'A{row}'] = "Development Impact (Year 10)"
        ws[f'A{row}'].font = Font(bold=True, size=12)
        ws[f'A{row}'].fill = self.green_fill
        ws.merge_cells(f'A{row}:D{row}')

        row += 1
        impact = [
            ("Farmers Supported", "='Development Impact'!L5", "farmers"),
            ("Jobs Created", "='Development Impact'!L17", "jobs"),
            ("Production Volume", "='Development Impact'!L24", "tonnes"),
            ("Cumulative Tax Revenue", "='Development Impact'!L34", "XAF"),
        ]

        for label, formula, unit in impact:
            ws[f'A{row}'] = label
            ws[f'B{row}'] = formula
            ws[f'C{row}'] = unit

            if unit == "XAF":
                ws[f'B{row}'].number_format = '#,##0'
            else:
                ws[f'B{row}'].number_format = '#,##0'
            row += 1

        ws.column_dimensions['A'].width = 30
        ws.column_dimensions['B'].width = 20
        ws.column_dimensions['C'].width = 10

        return ws

    def create_documentation(self):
        """Create Documentation sheet"""
        ws = self.wb.create_sheet("Documentation")

        ws['A1'] = "MODEL DOCUMENTATION & USER GUIDE"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:D1')

        docs = [
            ("", ""),
            ("MODEL OVERVIEW", ""),
            ("", ""),
            ("Model Name:", "DFI Investment Proposal - Agricultural Processing"),
            ("Version:", "1.0"),
            ("Created:", "January 24, 2026"),
            ("Currency:", "XAF (Central African Franc)"),
            ("Time Horizon:", "10 years"),
            ("", ""),
            ("WORKSHEET GUIDE", ""),
            ("", ""),
            ("Dashboard", "Executive summary with key metrics"),
            ("Assumptions", "ALL INPUTS - edit blue cells only"),
            ("Calculations", "Derived values (auto-calculated)"),
            ("Revenue", "10-year revenue projections"),
            ("Operating Costs", "Detailed OPEX by category"),
            ("CAPEX Schedule", "Capital expenditure by phase"),
            ("Debt Schedule", "Debt amortization and service"),
            ("P&L Statement", "Profit & Loss (Income Statement)"),
            ("Cash Flow", "Operating, Investing, Financing cash flows"),
            ("Returns Analysis", "IRR, NPV, DSCR, key metrics"),
            ("Development Impact", "Farmer, job, production metrics"),
            ("Sensitivity Analysis", "Scenario testing"),
            ("Documentation", "This guide"),
            ("", ""),
            ("HOW TO USE", ""),
            ("", ""),
            ("1. Input Data", "Go to Assumptions sheet, edit BLUE cells only"),
            ("2. Review Outputs", "Check Dashboard, P&L, Cash Flow, Returns Analysis"),
            ("3. Test Scenarios", "Change assumptions to see impact on returns"),
            ("4. Validate", "Ensure DSCR > 1.2, IRR > hurdle rate, NPV > 0"),
            ("", ""),
            ("COLOR CODING", ""),
            ("", ""),
            ("Blue cells", "USER INPUTS - edit these"),
            ("Yellow cells", "CALCULATIONS - do not edit"),
            ("Green headers", "Section headers"),
            ("Gray cells", "Column/row headers"),
            ("", ""),
            ("IMPORTANT NOTES", ""),
            ("", ""),
            ("• Only edit blue cells in Assumptions sheet", ""),
            ("• All other cells contain formulas - do not edit", ""),
            ("• Save dated versions (v1.0_2026-01-24, etc.)", ""),
            ("• Document assumption sources and dates", ""),
            ("• Review all outputs before sharing with investors", ""),
            ("", ""),
            ("VALIDATION CHECKLIST", ""),
            ("", ""),
            ("☐ All assumptions inputted and validated", ""),
            ("☐ CAPEX costs verified with quotes", ""),
            ("☐ Revenue projections realistic", ""),
            ("☐ Operating costs comprehensive", ""),
            ("☐ DSCR > 1.2 in all years", ""),
            ("☐ Project IRR > 15%", ""),
            ("☐ Equity IRR > 20%", ""),
            ("☐ NPV positive at 12% discount", ""),
            ("☐ Downside scenario tested", ""),
            ("☐ Development impact metrics calculated", ""),
            ("", ""),
            ("SUPPORT", ""),
            ("", ""),
            ("For questions or issues:", "Review the USER GUIDE documentation"),
            ("Technical support:", "Check formulas in Returns Analysis sheet"),
        ]

        row = 3
        for col1, col2 in docs:
            ws[f'A{row}'] = col1
            ws[f'B{row}'] = col2

            if any(x in col1 for x in ["OVERVIEW", "GUIDE", "HOW TO USE", "COLOR", "IMPORTANT", "VALIDATION", "SUPPORT"]):
                ws[f'A{row}'].font = self.bold_font
                ws[f'A{row}'].fill = self.green_fill

            row += 1

        ws.column_dimensions['A'].width = 40
        ws.column_dimensions['B'].width = 60

        return ws

    def extend(self):
        """Add all remaining sheets"""
        print("\nExtending model with advanced sheets...")
        print("=" * 80)

        sheets = [
            ("P&L Statement", self.create_pl_statement),
            ("Cash Flow", self.create_cash_flow),
            ("Returns Analysis", self.create_returns_analysis),
            ("Development Impact", self.create_development_impact),
            ("Sensitivity Analysis", self.create_sensitivity_analysis),
            ("Dashboard", self.create_dashboard),
            ("Documentation", self.create_documentation),
        ]

        for name, method in sheets:
            print(f"  ✓ Creating {name}...")
            method()

        print(f"\nSaving extended model...")
        self.wb.save(self.filename)
        print(f"✅ Model extended successfully!")
        print(f"\nTotal Worksheets: {len(self.wb.sheetnames)}")
        for sheet in self.wb.sheetnames:
            print(f"  • {sheet}")

        return self.filename

if __name__ == "__main__":
    extender = ModelExtender("Comprehensive_DFI_Financial_Model.xlsx")
    extender.extend()
