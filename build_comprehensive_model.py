#!/usr/bin/env python3
"""
Comprehensive DFI Financial Model Builder
Expands the base model to full investment proposal standards
"""

import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import datetime

class ComprehensiveModelBuilder:
    def __init__(self):
        self.wb = Workbook()
        self.wb.remove(self.wb.active)

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

    def create_assumptions_sheet(self):
        """Create comprehensive Assumptions sheet"""
        ws = self.wb.create_sheet("Assumptions")

        ws['A1'] = "FINANCIAL MODEL - ASSUMPTIONS & CONTROL PANEL"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:D1')

        ws['A2'] = "Instructions: ALL BLUE CELLS are inputs. Change these to update the entire model."
        ws['A2'].font = Font(italic=True, color="0000FF")
        ws.merge_cells('A2:D2')

        row = 4

        # All assumptions from the audit - keeping the same structure
        sections = [
            ("A. PROJECT TIMELINE & PHASING", [
                ("Model start year", 2026, "INPUT"),
                ("Model horizon (years)", 10, "INPUT"),
                ("Construction period - Phase 1 (months)", 18, "INPUT"),
                ("Construction period - Phase 2 (months)", 24, "INPUT"),
                ("Construction period - Phase 3 (months)", 36, "INPUT"),
            ]),

            ("B. PRODUCTION & CAPACITY", [
                ("SEED PRODUCTION", "", ""),
                ("G0 seed import (tonnes/year)", 100, "INPUT"),
                ("Multiplication ratio (G0→G1)", 15, "INPUT"),
                ("Seed wastage factor (%)", 5, "INPUT"),
                ("", "", ""),
                ("OUTGROWER NETWORK", "", ""),
                ("Target farmers - Year 1", 100, "INPUT"),
                ("Target farmers - Year 2", 375, "INPUT"),
                ("Target farmers - Year 3+", 800, "INPUT"),
                ("Hectares per farmer", 1.0, "INPUT"),
                ("Yield with certified seed (tonnes/ha)", 25, "INPUT"),
                ("Yield baseline (tonnes/ha)", 8, "INPUT"),
                ("", "", ""),
                ("PROCESSING CAPACITY", "", ""),
                ("French fry line capacity (tonnes/hour)", 2.0, "INPUT"),
                ("Fresh-pack line capacity (tonnes/hour)", 15.0, "INPUT"),
                ("Operating hours per day", 8, "INPUT"),
                ("Operating days per year", 300, "INPUT"),
                ("Capacity utilization - Year 1 (%)", 40, "INPUT"),
                ("Capacity utilization - Year 2 (%)", 60, "INPUT"),
                ("Capacity utilization - Year 3+ (%)", 80, "INPUT"),
            ]),

            ("C. PRICING & REVENUE", [
                ("SEED PRICING", "", ""),
                ("G1 certified seed price (XAF/kg)", 800, "INPUT"),
                ("Seed price escalation (%/year)", 3, "INPUT"),
                ("", "", ""),
                ("WARE POTATO PRICING", "", ""),
                ("Farmgate price - processing grade (XAF/kg)", 200, "INPUT"),
                ("Farmgate price - table stock (XAF/kg)", 250, "INPUT"),
                ("Fresh-pack retail price (XAF/kg)", 400, "INPUT"),
                ("Price escalation (%/year)", 2, "INPUT"),
                ("", "", ""),
                ("PROCESSED PRODUCTS", "", ""),
                ("Frozen french fries price (XAF/kg)", 1200, "INPUT"),
                ("Animal feed price (XAF/kg)", 150, "INPUT"),
                ("Fry conversion rate (%)", 62.5, "INPUT"),
                ("Feed by-product rate (%)", 80, "INPUT"),
                ("Product mix - French fries (%)", 70, "INPUT"),
                ("Product mix - Fresh pack (%)", 30, "INPUT"),
            ]),

            ("D. OPERATING COSTS", [
                ("SEED PRODUCTION COSTS", "", ""),
                ("G0 import cost (XAF/kg)", 2500, "INPUT"),
                ("Multiplication cost per kg output (XAF/kg)", 150, "INPUT"),
                ("Seed storage cost (XAF/kg/month)", 10, "INPUT"),
                ("", "", ""),
                ("OUTGROWER SUPPORT", "", ""),
                ("Input package cost per farmer (XAF)", 500000, "INPUT"),
                ("Extension cost per farmer (XAF)", 50000, "INPUT"),
                ("Farmer payment terms (days)", 0, "INPUT"),
                ("", "", ""),
                ("PROCESSING COSTS (per kg output)", "", ""),
                ("Direct labor (XAF/kg)", 50, "INPUT"),
                ("Utilities - electricity (XAF/kg)", 20, "INPUT"),
                ("Utilities - water (XAF/kg)", 10, "INPUT"),
                ("Packaging materials (XAF/kg)", 80, "INPUT"),
                ("Quality control & lab (XAF/kg)", 5, "INPUT"),
                ("Maintenance (% of processing CAPEX/year)", 3, "INPUT"),
                ("", "", ""),
                ("OVERHEAD & ADMINISTRATION", "", ""),
                ("Management salaries (XAF/month)", 15000000, "INPUT"),
                ("Administrative staff (XAF/month)", 3000000, "INPUT"),
                ("Office & utilities (XAF/month)", 1500000, "INPUT"),
                ("Insurance (% of total assets/year)", 1.5, "INPUT"),
                ("Professional services (XAF/year)", 10000000, "INPUT"),
                ("", "", ""),
                ("LOGISTICS & DISTRIBUTION", "", ""),
                ("Transport cost per tonne-km (XAF)", 50, "INPUT"),
                ("Average distribution distance (km)", 300, "INPUT"),
                ("Cold storage cost (XAF/tonne/month)", 25000, "INPUT"),
                ("", "", ""),
                ("COST ESCALATION", "", ""),
                ("General cost inflation (%/year)", 3, "INPUT"),
            ]),

            ("E. CAPITAL EXPENDITURE (XAF)", [
                ("PHASE 1: SEED MULTIPLICATION", "", ""),
                ("Aeroponic EGS facility", 600000000, "INPUT"),
                ("Seed cold storage (500T)", 300000000, "INPUT"),
                ("Nucleus farm equipment", 200000000, "INPUT"),
                ("Greenhouse structures", 150000000, "INPUT"),
                ("Phase 1 contingency (%)", 10, "INPUT"),
                ("", "", ""),
                ("PHASE 2: OUTGROWER NETWORK", "", ""),
                ("Training center & demo farm", 150000000, "INPUT"),
                ("Field equipment & tools", 250000000, "INPUT"),
                ("Input supply warehouse", 100000000, "INPUT"),
                ("Working capital facility", 500000000, "INPUT"),
                ("Phase 2 contingency (%)", 10, "INPUT"),
                ("", "", ""),
                ("PHASE 3: PROCESSING FACILITY", "", ""),
                ("French fry line (Baixin)", 5000000000, "INPUT"),
                ("Fresh-pack line (Manter)", 2000000000, "INPUT"),
                ("CA storage facility (10,000T)", 3000000000, "INPUT"),
                ("Factory building & civil works", 2000000000, "INPUT"),
                ("Utilities infrastructure", 500000000, "INPUT"),
                ("Effluent treatment plant", 300000000, "INPUT"),
                ("Phase 3 contingency (%)", 15, "INPUT"),
                ("", "", ""),
                ("PHASE 4: LOGISTICS & DISTRIBUTION", "", ""),
                ("Reefer trucks (number)", 5, "INPUT"),
                ("Cost per reefer truck (XAF)", 150000000, "INPUT"),
                ("Delivery vans (number)", 10, "INPUT"),
                ("Cost per van (XAF)", 25000000, "INPUT"),
                ("Regional cold storage depots", 400000000, "INPUT"),
                ("Phase 4 contingency (%)", 10, "INPUT"),
                ("", "", ""),
                ("PHASE 5: CIRCULAR ECONOMY", "", ""),
                ("Feed pelletizer line", 200000000, "INPUT"),
                ("Water recycling system", 150000000, "INPUT"),
                ("Biogas digester", 100000000, "INPUT"),
                ("Phase 5 contingency (%)", 10, "INPUT"),
            ]),

            ("F. DEPRECIATION", [
                ("Buildings useful life (years)", 30, "INPUT"),
                ("Heavy machinery useful life (years)", 10, "INPUT"),
                ("Light equipment useful life (years)", 7, "INPUT"),
                ("Vehicles useful life (years)", 5, "INPUT"),
                ("Residual value (% of cost)", 5, "INPUT"),
                ("", "", ""),
                ("ASSET CLASSIFICATION (%)", "", ""),
                ("Buildings proportion", 25, "INPUT"),
                ("Heavy machinery proportion", 50, "INPUT"),
                ("Light equipment proportion", 15, "INPUT"),
                ("Vehicles proportion", 10, "INPUT"),
            ]),

            ("G. FINANCING STRUCTURE", [
                ("EQUITY", "", ""),
                ("Sponsor equity (% of total CAPEX)", 25, "INPUT"),
                ("Equity IRR hurdle rate (%)", 20, "INPUT"),
                ("", "", ""),
                ("SENIOR DEBT (DFI)", "", ""),
                ("Senior debt (% of total CAPEX)", 55, "INPUT"),
                ("Interest rate - fixed (%)", 8.0, "INPUT"),
                ("Tenor (years)", 10, "INPUT"),
                ("Grace period (years)", 3, "INPUT"),
                ("Arrangement fee (%)", 1.5, "INPUT"),
                ("Commitment fee (% on undrawn)", 0.5, "INPUT"),
                ("", "", ""),
                ("SUBORDINATED DEBT / MEZZANINE", "", ""),
                ("Mezzanine (% of total CAPEX)", 10, "INPUT"),
                ("Interest rate (%)", 12.0, "INPUT"),
                ("Tenor (years)", 8, "INPUT"),
                ("Grace period (years)", 5, "INPUT"),
                ("", "", ""),
                ("GRANT / TECHNICAL ASSISTANCE", "", ""),
                ("Grant amount (XAF)", 500000000, "INPUT"),
            ]),

            ("H. TAX & INCENTIVES (Cameroon)", [
                ("Standard corporate income tax rate (%)", 33, "INPUT"),
                ("Installation phase duration (years)", 5, "INPUT"),
                ("CIT holiday period (years)", 5, "INPUT"),
                ("Reduced CIT rate after holiday (%)", 16.5, "INPUT"),
                ("Tax credit (% - Category C project)", 75, "INPUT"),
                ("Loss carry-forward period (years)", 5, "INPUT"),
                ("Minimum corporate tax (% revenue)", 1, "INPUT"),
                ("Withholding tax on dividends (%)", 16.5, "INPUT"),
            ]),

            ("I. WORKING CAPITAL ASSUMPTIONS", [
                ("Raw materials inventory (days)", 30, "INPUT"),
                ("Finished goods inventory (days)", 45, "INPUT"),
                ("Accounts receivable (days)", 30, "INPUT"),
                ("Accounts payable (days)", 30, "INPUT"),
                ("Seasonal working capital peak multiplier", 1.5, "INPUT"),
                ("Cash buffer (days of operating costs)", 15, "INPUT"),
            ]),

            ("J. MACROECONOMIC ASSUMPTIONS", [
                ("XAF/USD exchange rate", 600, "INPUT"),
                ("General inflation rate (%/year)", 3, "INPUT"),
                ("Discount rate for NPV (%)", 12, "INPUT"),
                ("Terminal growth rate (%)", 2, "INPUT"),
            ]),

            ("K. SCENARIO ADJUSTMENTS", [
                ("DOWNSIDE SCENARIO", "", ""),
                ("Yield adjustment (%)", -20, "INPUT"),
                ("Price adjustment (%)", -15, "INPUT"),
                ("CAPEX overrun (%)", 15, "INPUT"),
                ("Operating cost increase (%)", 10, "INPUT"),
                ("Ramp-up delay (months)", 6, "INPUT"),
                ("", "", ""),
                ("UPSIDE SCENARIO", "", ""),
                ("Yield adjustment (%)", 10, "INPUT"),
                ("Price adjustment (%)", 10, "INPUT"),
                ("CAPEX savings (%)", -5, "INPUT"),
                ("Operating cost reduction (%)", -5, "INPUT"),
                ("Accelerated ramp-up (months)", -3, "INPUT"),
            ]),
        ]

        for section_name, items in sections:
            ws[f'A{row}'] = section_name
            ws[f'A{row}'].font = self.white_bold_font
            ws[f'A{row}'].fill = self.header_fill
            ws.merge_cells(f'A{row}:D{row}')
            row += 1

            for label, value, cell_type in items:
                ws[f'A{row}'] = label

                if cell_type == "INPUT":
                    ws[f'C{row}'] = value
                    ws[f'C{row}'].fill = self.blue_fill
                    ws[f'C{row}'].font = self.bold_font
                    ws[f'D{row}'] = "INPUT"
                    ws[f'D{row}'].fill = self.blue_fill

                    if isinstance(value, (int, float)) and value >= 100:
                        ws[f'C{row}'].number_format = '#,##0'
                    elif isinstance(value, float):
                        ws[f'C{row}'].number_format = '0.0'

                elif label:
                    ws[f'A{row}'].font = Font(bold=True, italic=True)

                for col in ['A', 'B', 'C', 'D']:
                    ws[f'{col}{row}'].border = self.thin_border

                row += 1
            row += 1

        ws.column_dimensions['A'].width = 45
        ws.column_dimensions['B'].width = 15
        ws.column_dimensions['C'].width = 15
        ws.column_dimensions['D'].width = 12

        return ws

    def create_calculations_sheet(self):
        """Create Calculations sheet for derived values"""
        ws = self.wb.create_sheet("Calculations")

        ws['A1'] = "CALCULATIONS (Auto-Calculated from Assumptions)"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:C1')

        row = 3
        ws['A3'] = "DERIVED VALUES"
        ws['A3'].font = self.bold_font

        calcs = [
            ("G1 seed output (tonnes/year)", "=Assumptions!C14*Assumptions!C15*(1-Assumptions!C16/100)", "tonnes"),
            ("Total Phase 1 CAPEX", "=(Assumptions!C84+Assumptions!C85+Assumptions!C86+Assumptions!C87)*(1+Assumptions!C88/100)", "XAF"),
            ("Total Phase 2 CAPEX", "=(Assumptions!C91+Assumptions!C92+Assumptions!C93+Assumptions!C94)*(1+Assumptions!C95/100)", "XAF"),
            ("Total Phase 3 CAPEX", "=(Assumptions!C98+Assumptions!C99+Assumptions!C100+Assumptions!C101+Assumptions!C102+Assumptions!C103)*(1+Assumptions!C104/100)", "XAF"),
            ("Total Phase 4 CAPEX", "=(Assumptions!C107*Assumptions!C108+Assumptions!C109*Assumptions!C110+Assumptions!C111)*(1+Assumptions!C112/100)", "XAF"),
            ("Total Phase 5 CAPEX", "=(Assumptions!C115+Assumptions!C116+Assumptions!C117)*(1+Assumptions!C118/100)", "XAF"),
            ("TOTAL PROJECT CAPEX", "=SUM(B4:B8)", "XAF"),
        ]

        row = 4
        for label, formula, unit in calcs:
            ws[f'A{row}'] = label
            if formula:
                ws[f'B{row}'] = formula
                ws[f'B{row}'].fill = self.yellow_fill
                if "XAF" in unit or "tonnes" in unit:
                    ws[f'B{row}'].number_format = '#,##0'
            ws[f'C{row}'] = unit

            if "TOTAL" in label:
                ws[f'A{row}'].font = self.bold_font
            row += 1

        ws.column_dimensions['A'].width = 35
        ws.column_dimensions['B'].width = 20
        ws.column_dimensions['C'].width = 10

        return ws

    def create_revenue_sheet(self):
        """Create Revenue projections sheet"""
        ws = self.wb.create_sheet("Revenue")

        ws['A1'] = "REVENUE PROJECTIONS"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:L1')

        # Headers
        ws['A3'] = "Revenue Stream"
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            ws[f'{col}3'] = f"Year {year}"
            ws[f'{col}3'].font = self.bold_font
            ws[f'{col}3'].fill = self.gray_fill
            ws[f'{col}3'].alignment = self.center_align

        # Revenue lines
        lines = [
            ("SEED REVENUE", ""),
            ("G1 seed sales volume (kg)", "=Calculations!$B$4*1000"),
            ("G1 seed price (XAF/kg)", "=Assumptions!$C$43*(1+Assumptions!$C$44/100)^(COLUMN()-2)"),
            ("Seed revenue (XAF)", "=B5*B6"),
            ("", ""),
            ("PROCESSED PRODUCTS REVENUE", ""),
            ("Processing volume (tonnes)", "=Assumptions!$C$32*Assumptions!$C$33*Assumptions!$C$34*IF(COLUMN()=2,Assumptions!$C$35,IF(COLUMN()=3,Assumptions!$C$36,Assumptions!$C$37))/100"),
            ("French fries revenue (XAF)", "=B11*Assumptions!$C$55/100*Assumptions!$C$51*(1+Assumptions!$C$48/100)^(COLUMN()-2)*1000"),
            ("Fresh pack revenue (XAF)", "=B11*(100-Assumptions!$C$55)/100*Assumptions!$C$50*(1+Assumptions!$C$48/100)^(COLUMN()-2)*1000"),
            ("", ""),
            ("TOTAL REVENUE (XAF)", "=B8+B12+B13"),
        ]

        row = 4
        for label, base_formula in lines:
            ws[f'A{row}'] = label

            if "REVENUE" in label and label != "TOTAL REVENUE (XAF)":
                ws[f'A{row}'].font = self.bold_font
                ws[f'A{row}'].fill = self.green_fill
            elif label == "TOTAL REVENUE (XAF)":
                ws[f'A{row}'].font = self.white_bold_font
                ws[f'A{row}'].fill = self.header_fill

            if base_formula:
                for year in range(1, self.model_years + 1):
                    col = get_column_letter(year + 1)
                    ws[f'{col}{row}'] = base_formula
                    ws[f'{col}{row}'].number_format = '#,##0'

            row += 1

        ws.column_dimensions['A'].width = 35
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            ws.column_dimensions[col].width = 15

        return ws

    def create_operating_costs_sheet(self):
        """Create detailed Operating Costs sheet"""
        ws = self.wb.create_sheet("Operating Costs")

        ws['A1'] = "OPERATING COSTS"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:L1')

        # Headers
        ws['A3'] = "Cost Category"
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            ws[f'{col}3'] = f"Year {year}"
            ws[f'{col}3'].font = self.bold_font
            ws[f'{col}3'].fill = self.gray_fill
            ws[f'{col}3'].alignment = self.center_align

        # Cost lines
        lines = [
            ("SEED PRODUCTION COSTS", ""),
            ("G0 import cost", "=Assumptions!$C$68*Assumptions!$C$14*1000*(1+Assumptions!$C$119/100)^(COLUMN()-2)"),
            ("Multiplication cost", "=Assumptions!$C$69*Calculations!$B$4*1000*(1+Assumptions!$C$119/100)^(COLUMN()-2)"),
            ("Total seed costs", "=SUM(B5:B6)"),
            ("", ""),
            ("OUTGROWER COSTS", ""),
            ("Input packages", "=IF(COLUMN()=2,Assumptions!$C$19,IF(COLUMN()=3,Assumptions!$C$20,Assumptions!$C$21))*Assumptions!$C$73*(1+Assumptions!$C$119/100)^(COLUMN()-2)"),
            ("Extension services", "=IF(COLUMN()=2,Assumptions!$C$19,IF(COLUMN()=3,Assumptions!$C$20,Assumptions!$C$21))*Assumptions!$C$74*(1+Assumptions!$C$119/100)^(COLUMN()-2)"),
            ("Total outgrower costs", "=SUM(B10:B11)"),
            ("", ""),
            ("PROCESSING COSTS", ""),
            ("Direct labor", "=Revenue!B11*1000*(Assumptions!$C$78+Assumptions!$C$79+Assumptions!$C$80+Assumptions!$C$81+Assumptions!$C$82)*(1+Assumptions!$C$119/100)^(COLUMN()-2)"),
            ("Maintenance", "=Calculations!$B$7*Assumptions!$C$83/100*(1+Assumptions!$C$119/100)^(COLUMN()-2)"),
            ("Total processing costs", "=SUM(B15:B16)"),
            ("", ""),
            ("OVERHEAD & ADMINISTRATION", ""),
            ("Salaries", "=(Assumptions!$C$86+Assumptions!$C$87+Assumptions!$C$88)*12*(1+Assumptions!$C$119/100)^(COLUMN()-2)"),
            ("Professional services", "=Assumptions!$C$90*(1+Assumptions!$C$119/100)^(COLUMN()-2)"),
            ("Total overhead", "=SUM(B20:B21)"),
            ("", ""),
            ("LOGISTICS", ""),
            ("Transport", "=Revenue!B11*Assumptions!$C$93*Assumptions!$C$94*(1+Assumptions!$C$119/100)^(COLUMN()-2)"),
            ("Cold storage", "=Revenue!B11*Assumptions!$C$95*(1+Assumptions!$C$119/100)^(COLUMN()-2)"),
            ("Total logistics", "=SUM(B25:B26)"),
            ("", ""),
            ("TOTAL OPERATING COSTS", "=B7+B12+B17+B22+B27"),
        ]

        row = 4
        for label, base_formula in lines:
            ws[f'A{row}'] = label

            if "COSTS" in label and "Total" not in label and "TOTAL" not in label:
                ws[f'A{row}'].font = self.bold_font
                ws[f'A{row}'].fill = self.orange_fill
            elif "Total" in label or "TOTAL" in label:
                ws[f'A{row}'].font = self.bold_font
                ws[f'A{row}'].fill = self.gray_fill

            if base_formula:
                for year in range(1, self.model_years + 1):
                    col = get_column_letter(year + 1)
                    ws[f'{col}{row}'] = base_formula
                    ws[f'{col}{row}'].number_format = '#,##0'

            row += 1

        ws.column_dimensions['A'].width = 35
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            ws.column_dimensions[col].width = 15

        return ws

    def create_capex_schedule(self):
        """Create detailed CAPEX Schedule with phasing"""
        ws = self.wb.create_sheet("CAPEX Schedule")

        ws['A1'] = "CAPITAL EXPENDITURE SCHEDULE"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:M1')

        # Headers
        ws['A3'] = "Phase / Asset"
        ws['B3'] = "Total Budget"
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 2)
            ws[f'{col}3'] = f"Year {year}"
            ws[f'{col}3'].font = self.bold_font
            ws[f'{col}3'].fill = self.gray_fill

        # CAPEX by phase
        lines = [
            ("PHASE 1: Seed Multiplication", "=Calculations!$B$5", [(1, 0.6), (2, 0.4)]),
            ("PHASE 2: Outgrower Network", "=Calculations!$B$6", [(2, 0.5), (3, 0.5)]),
            ("PHASE 3: Processing Facility", "=Calculations!$B$7", [(2, 0.2), (3, 0.5), (4, 0.3)]),
            ("PHASE 4: Logistics", "=Calculations!$B$8", [(4, 0.7), (5, 0.3)]),
            ("PHASE 5: Circular Economy", "=Calculations!$B$9", [(5, 1.0)]),
            ("", "", []),
            ("TOTAL ANNUAL CAPEX", "=Calculations!$B$10", None),
            ("", "", []),
            ("Cumulative CAPEX", "", None),
        ]

        row = 4
        for label, budget_formula, schedule in lines:
            ws[f'A{row}'] = label

            if budget_formula:
                ws[f'B{row}'] = budget_formula
                ws[f'B{row}'].number_format = '#,##0'

            if "PHASE" in label:
                ws[f'A{row}'].font = self.bold_font
                ws[f'A{row}'].fill = self.green_fill
            elif "TOTAL" in label:
                ws[f'A{row}'].font = self.white_bold_font
                ws[f'A{row}'].fill = self.header_fill
                ws[f'B{row}'].font = self.bold_font

            # Distribute spending
            if schedule is not None:
                for year in range(1, self.model_years + 1):
                    col = get_column_letter(year + 2)

                    if schedule == []:  # Empty schedule
                        ws[f'{col}{row}'] = 0
                    elif schedule is None:  # Sum or cumulative
                        if "TOTAL" in label:
                            ws[f'{col}{row}'] = f"=SUM({col}4:{col}{row-2})"
                        elif "Cumulative" in label:
                            if year == 1:
                                ws[f'{col}{row}'] = f"={col}{row-2}"
                            else:
                                prev_col = get_column_letter(year + 1)
                                ws[f'{col}{row}'] = f"={prev_col}{row}+{col}{row-2}"
                    else:
                        # Find allocation for this year
                        allocation = next((pct for y, pct in schedule if y == year), 0)
                        if allocation > 0:
                            ws[f'{col}{row}'] = f"=$B{row}*{allocation}"
                        else:
                            ws[f'{col}{row}'] = 0

                    ws[f'{col}{row}'].number_format = '#,##0'

            row += 1

        ws.column_dimensions['A'].width = 35
        ws.column_dimensions['B'].width = 18
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 2)
            ws.column_dimensions[col].width = 15

        return ws

    def create_debt_schedule(self):
        """Create Debt Schedule with amortization"""
        ws = self.wb.create_sheet("Debt Schedule")

        ws['A1'] = "DEBT SCHEDULE & AMORTIZATION"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:M1')

        # Headers
        ws['A3'] = "Item"
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            ws[f'{col}3'] = f"Year {year}"
            ws[f'{col}3'].font = self.bold_font
            ws[f'{col}3'].fill = self.gray_fill

        row = 4

        # Senior Debt
        senior_lines = [
            ("SENIOR DEBT", ""),
            ("Opening balance", "=IF(COLUMN()=2,0,OFFSET($B6,0,COLUMN()-3))"),
            ("Drawdowns", "='CAPEX Schedule'!C11*Assumptions!$C$128/100"),
            ("Principal repayment", "=IF(COLUMN()-2<=Assumptions!$C$131,0,Calculations!$B$10*Assumptions!$C$128/100/(Assumptions!$C$130-Assumptions!$C$131))"),
            ("Closing balance", "=B5+B6-B7"),
            ("Interest expense", "=(B5+B8)/2*Assumptions!$C$129/100"),
            ("Commitment fee", "=(Calculations!$B$10*Assumptions!$C$128/100-B8)*Assumptions!$C$133/100"),
            ("Total debt service", "=B7+B9+B10"),
        ]

        for label, formula in senior_lines:
            ws[f'A{row}'] = label

            if "SENIOR DEBT" in label:
                ws[f'A{row}'].font = self.bold_font
                ws[f'A{row}'].fill = self.green_fill
            elif "Total" in label:
                ws[f'A{row}'].font = self.bold_font

            if formula:
                for year in range(1, self.model_years + 1):
                    col = get_column_letter(year + 1)
                    ws[f'{col}{row}'] = formula
                    ws[f'{col}{row}'].number_format = '#,##0'

            row += 1

        row += 1

        # Mezzanine Debt
        mezz_lines = [
            ("MEZZANINE DEBT", ""),
            ("Opening balance", "=IF(COLUMN()=2,0,OFFSET($B14,0,COLUMN()-3))"),
            ("Drawdowns", "='CAPEX Schedule'!C11*Assumptions!$C$136/100"),
            ("Principal repayment", "=IF(COLUMN()-2<=Assumptions!$C$139,0,Calculations!$B$10*Assumptions!$C$136/100/(Assumptions!$C$138-Assumptions!$C$139))"),
            ("Closing balance", "=B13+B14-B15"),
            ("Interest expense", "=(B13+B16)/2*Assumptions!$C$137/100"),
            ("Total debt service", "=B15+B17"),
        ]

        for label, formula in mezz_lines:
            ws[f'A{row}'] = label

            if "MEZZANINE" in label:
                ws[f'A{row}'].font = self.bold_font
                ws[f'A{row}'].fill = self.green_fill
            elif "Total" in label:
                ws[f'A{row}'].font = self.bold_font

            if formula:
                for year in range(1, self.model_years + 1):
                    col = get_column_letter(year + 1)
                    ws[f'{col}{row}'] = formula
                    ws[f'{col}{row}'].number_format = '#,##0'

            row += 1

        row += 1

        # Total Debt
        total_lines = [
            ("TOTAL DEBT", ""),
            ("Total opening balance", "=B5+B13"),
            ("Total drawdowns", "=B6+B14"),
            ("Total principal repayment", "=B7+B15"),
            ("Total closing balance", "=B8+B16"),
            ("Total interest expense", "=B9+B17"),
            ("Total debt service", "=B11+B18"),
        ]

        for label, formula in total_lines:
            ws[f'A{row}'] = label

            if "TOTAL DEBT" in label:
                ws[f'A{row}'].font = self.white_bold_font
                ws[f'A{row}'].fill = self.header_fill
            elif "Total" in label:
                ws[f'A{row}'].font = self.bold_font

            if formula:
                for year in range(1, self.model_years + 1):
                    col = get_column_letter(year + 1)
                    ws[f'{col}{row}'] = formula
                    ws[f'{col}{row}'].number_format = '#,##0'
                    if "Total debt service" in label:
                        ws[f'{col}{row}'].font = self.bold_font

            row += 1

        ws.column_dimensions['A'].width = 30
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            ws.column_dimensions[col].width = 15

        return ws

    def build(self, filename="Comprehensive_DFI_Financial_Model.xlsx"):
        """Build the comprehensive model"""
        print("Building Comprehensive DFI Investment Proposal Model...")
        print("=" * 80)

        sheets = [
            ("Assumptions", self.create_assumptions_sheet),
            ("Calculations", self.create_calculations_sheet),
            ("Revenue", self.create_revenue_sheet),
            ("Operating Costs", self.create_operating_costs_sheet),
            ("CAPEX Schedule", self.create_capex_schedule),
            ("Debt Schedule", self.create_debt_schedule),
        ]

        for name, method in sheets:
            print(f"  ✓ Creating {name}...")
            method()

        print(f"\nSaving to {filename}...")
        self.wb.save(filename)
        print(f"✅ Model created successfully!")
        print(f"\nWorksheets: {len(self.wb.sheetnames)}")
        for sheet in self.wb.sheetnames:
            print(f"  • {sheet}")

        return filename

if __name__ == "__main__":
    builder = ComprehensiveModelBuilder()
    builder.build()
