#!/usr/bin/env python3
"""
Financial Model Builder - Control Panel Architecture
Creates a comprehensive financial model for agricultural processing project
"""

import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import datetime
from dateutil.relativedelta import relativedelta

class FinancialModelBuilder:
    def __init__(self):
        self.wb = Workbook()
        self.wb.remove(self.wb.active)  # Remove default sheet

        # Define styles
        self.blue_fill = PatternFill(start_color="B4C7E7", end_color="B4C7E7", fill_type="solid")
        self.yellow_fill = PatternFill(start_color="FFE699", end_color="FFE699", fill_type="solid")
        self.green_fill = PatternFill(start_color="C6E0B4", end_color="C6E0B4", fill_type="solid")
        self.gray_fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        self.header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")

        self.bold_font = Font(bold=True)
        self.white_bold_font = Font(bold=True, color="FFFFFF")
        self.header_font = Font(bold=True, size=14, color="FFFFFF")

        self.thin_border = Border(
            left=Side(style='thin'),
            right=Side(style='thin'),
            top=Side(style='thin'),
            bottom=Side(style='thin')
        )

        self.center_align = Alignment(horizontal='center', vertical='center')
        self.right_align = Alignment(horizontal='right', vertical='center')

        # Model parameters
        self.model_years = 10
        self.start_date = datetime(2026, 1, 1)

    def create_assumptions_sheet(self):
        """Create the main Assumptions/Control Panel sheet"""
        ws = self.wb.create_sheet("Assumptions")

        # Header
        ws['A1'] = "FINANCIAL MODEL - ASSUMPTIONS & CONTROL PANEL"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:D1')

        ws['A2'] = "Instructions: ALL BLUE CELLS are inputs. Change these to update the entire model."
        ws['A2'].font = Font(italic=True, color="0000FF")
        ws.merge_cells('A2:D2')

        row = 4

        # Section A: Project Timeline
        row = self._add_section_header(ws, row, "A. PROJECT TIMELINE & PHASING")
        assumptions = [
            ("Model start date", "=DATE(2026,1,1)", "DATE"),
            ("Model horizon (years)", 10, "INPUT"),
            ("Construction period - Phase 1 (months)", 18, "INPUT"),
            ("Construction period - Phase 2 (months)", 24, "INPUT"),
            ("Construction period - Phase 3 (months)", 36, "INPUT"),
            ("", "", ""),
            ("Seed operations start date", "=DATE(2027,7,1)", "CALC"),
            ("Processing operations start date", "=DATE(2029,1,1)", "CALC"),
        ]
        row = self._add_assumptions_block(ws, row, assumptions)

        # Section B: Production & Capacity
        row = self._add_section_header(ws, row, "B. PRODUCTION & CAPACITY")
        assumptions = [
            ("SEED PRODUCTION", "", ""),
            ("G0 seed import (tonnes/year)", 100, "INPUT"),
            ("Multiplication ratio (G0→G1)", 15, "INPUT"),
            ("G1 seed output (tonnes/year)", "=C{}-2*C{}-1".format(row+2, row+2), "CALC"),
            ("Seed wastage factor (%)", 5, "INPUT"),
            ("", "", ""),
            ("OUTGROWER NETWORK", "", ""),
            ("Target farmers - Year 1", 100, "INPUT"),
            ("Target farmers - Year 2", 375, "INPUT"),
            ("Target farmers - Year 3+", 800, "INPUT"),
            ("Hectares per farmer", 1.0, "INPUT"),
            ("Yield with certified seed (tonnes/ha)", 25, "INPUT"),
            ("Yield baseline (tonnes/ha)", 8, "INPUT"),
            ("Yield improvement (%)", "=(C{}-2-C{}-1)/C{}-1".format(row+12, row+12, row+12), "CALC"),
            ("", "", ""),
            ("PROCESSING CAPACITY", "", ""),
            ("French fry line capacity (tonnes/hour)", 2.0, "INPUT"),
            ("Fresh-pack line capacity (tonnes/hour)", 15.0, "INPUT"),
            ("Operating hours per day", 8, "INPUT"),
            ("Operating days per year", 300, "INPUT"),
            ("Capacity utilization - Year 1 (%)", 40, "INPUT"),
            ("Capacity utilization - Year 2 (%)", 60, "INPUT"),
            ("Capacity utilization - Year 3+ (%)", 80, "INPUT"),
        ]
        row = self._add_assumptions_block(ws, row, assumptions)

        # Section C: Pricing & Revenue
        row = self._add_section_header(ws, row, "C. PRICING & REVENUE")
        assumptions = [
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
        ]
        row = self._add_assumptions_block(ws, row, assumptions)

        # Section D: Operating Costs
        row = self._add_section_header(ws, row, "D. OPERATING COSTS")
        assumptions = [
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
        ]
        row = self._add_assumptions_block(ws, row, assumptions)

        # Section E: Capital Expenditure
        row = self._add_section_header(ws, row, "E. CAPITAL EXPENDITURE (XAF)")
        assumptions = [
            ("PHASE 1: SEED MULTIPLICATION", "", ""),
            ("Aeroponic EGS facility", 600000000, "INPUT"),
            ("Seed cold storage (500T)", 300000000, "INPUT"),
            ("Nucleus farm equipment", 200000000, "INPUT"),
            ("Greenhouse structures", 150000000, "INPUT"),
            ("Phase 1 contingency (%)", 10, "INPUT"),
            ("Phase 1 Total", "=SUM(C{}-5:C{}-2)*(1+C{}-1/100)".format(row+5, row+5, row+5), "CALC"),
            ("", "", ""),
            ("PHASE 2: OUTGROWER NETWORK", "", ""),
            ("Training center & demo farm", 150000000, "INPUT"),
            ("Field equipment & tools", 250000000, "INPUT"),
            ("Input supply warehouse", 100000000, "INPUT"),
            ("Working capital facility", 500000000, "INPUT"),
            ("Phase 2 contingency (%)", 10, "INPUT"),
            ("Phase 2 Total", "=SUM(C{}-5:C{}-2)*(1+C{}-1/100)".format(row+13, row+13, row+13), "CALC"),
            ("", "", ""),
            ("PHASE 3: PROCESSING FACILITY", "", ""),
            ("French fry line (Baixin)", 5000000000, "INPUT"),
            ("Fresh-pack line (Manter)", 2000000000, "INPUT"),
            ("CA storage facility (10,000T)", 3000000000, "INPUT"),
            ("Factory building & civil works", 2000000000, "INPUT"),
            ("Utilities infrastructure", 500000000, "INPUT"),
            ("Effluent treatment plant", 300000000, "INPUT"),
            ("Phase 3 contingency (%)", 15, "INPUT"),
            ("Phase 3 Total", "=SUM(C{}-7:C{}-2)*(1+C{}-1/100)".format(row+24, row+24, row+24), "CALC"),
            ("", "", ""),
            ("PHASE 4: LOGISTICS & DISTRIBUTION", "", ""),
            ("Reefer trucks (number)", 5, "INPUT"),
            ("Cost per reefer truck (XAF)", 150000000, "INPUT"),
            ("Delivery vans (number)", 10, "INPUT"),
            ("Cost per van (XAF)", 25000000, "INPUT"),
            ("Regional cold storage depots", 400000000, "INPUT"),
            ("Phase 4 contingency (%)", 10, "INPUT"),
            ("Phase 4 Total", "=(C{}-6*C{}-5+C{}-4*C{}-3+C{}-2)*(1+C{}-1/100)".format(row+31, row+31, row+31, row+31, row+31, row+31), "CALC"),
            ("", "", ""),
            ("PHASE 5: CIRCULAR ECONOMY", "", ""),
            ("Feed pelletizer line", 200000000, "INPUT"),
            ("Water recycling system", 150000000, "INPUT"),
            ("Biogas digester", 100000000, "INPUT"),
            ("Phase 5 contingency (%)", 10, "INPUT"),
            ("Phase 5 Total", "=SUM(C{}-4:C{}-2)*(1+C{}-1/100)".format(row+42, row+42, row+42), "CALC"),
            ("", "", ""),
            ("TOTAL PROJECT CAPEX", "=C{}-37+C{}-23+C{}-10+C{}-5+C{}-0".format(row+45, row+45, row+45, row+45, row+45), "CALC"),
        ]
        row = self._add_assumptions_block(ws, row, assumptions)

        # Section F: Depreciation
        row = self._add_section_header(ws, row, "F. DEPRECIATION")
        assumptions = [
            ("Buildings useful life (years)", 30, "INPUT"),
            ("Heavy machinery useful life (years)", 10, "INPUT"),
            ("Light equipment useful life (years)", 7, "INPUT"),
            ("Vehicles useful life (years)", 5, "INPUT"),
            ("Residual value (% of cost)", 5, "INPUT"),
            ("Depreciation method", "Straight-line", "INPUT"),
            ("", "", ""),
            ("ASSET CLASSIFICATION (%)", "", ""),
            ("Buildings proportion", 25, "INPUT"),
            ("Heavy machinery proportion", 50, "INPUT"),
            ("Light equipment proportion", 15, "INPUT"),
            ("Vehicles proportion", 10, "INPUT"),
        ]
        row = self._add_assumptions_block(ws, row, assumptions)

        # Section G: Financing
        row = self._add_section_header(ws, row, "G. FINANCING STRUCTURE")
        assumptions = [
            ("EQUITY", "", ""),
            ("Sponsor equity (% of total CAPEX)", 25, "INPUT"),
            ("Equity IRR hurdle rate (%)", 20, "INPUT"),
            ("Dividend policy", "After debt service", "INPUT"),
            ("", "", ""),
            ("SENIOR DEBT (DFI)", "", ""),
            ("Senior debt (% of total CAPEX)", 55, "INPUT"),
            ("Interest rate - fixed (%)", 8.0, "INPUT"),
            ("Tenor (years)", 10, "INPUT"),
            ("Grace period (years)", 3, "INPUT"),
            ("Repayment schedule", "Equal principal", "INPUT"),
            ("Arrangement fee (%)", 1.5, "INPUT"),
            ("Commitment fee (% on undrawn)", 0.5, "INPUT"),
            ("", "", ""),
            ("SUBORDINATED DEBT / MEZZANINE", "", ""),
            ("Mezzanine (% of total CAPEX)", 10, "INPUT"),
            ("Interest rate (%)", 12.0, "INPUT"),
            ("Payment-in-kind (PIK) option", "Yes", "INPUT"),
            ("PIK rate if applicable (%)", 14.0, "INPUT"),
            ("Tenor (years)", 8, "INPUT"),
            ("Grace period (years)", 5, "INPUT"),
            ("", "", ""),
            ("GRANT / TECHNICAL ASSISTANCE", "", ""),
            ("Grant amount (XAF)", 500000000, "INPUT"),
            ("Grant purpose", "TA & Training", "INPUT"),
            ("Grant disbursement timing", "Year 1", "INPUT"),
        ]
        row = self._add_assumptions_block(ws, row, assumptions)

        # Section H: Tax & Incentives
        row = self._add_section_header(ws, row, "H. TAX & INCENTIVES (Cameroon)")
        assumptions = [
            ("Standard corporate income tax rate (%)", 33, "INPUT"),
            ("Installation phase duration (years)", 5, "INPUT"),
            ("Customs duty exemption", "Yes", "INPUT"),
            ("VAT exemption on imports", "Yes", "INPUT"),
            ("CIT holiday period (years)", 5, "INPUT"),
            ("Reduced CIT rate after holiday (%)", 16.5, "INPUT"),
            ("Tax credit (% - Category C project)", 75, "INPUT"),
            ("Loss carry-forward period (years)", 5, "INPUT"),
            ("Minimum corporate tax (% revenue)", 1, "INPUT"),
            ("Withholding tax on dividends (%)", 16.5, "INPUT"),
        ]
        row = self._add_assumptions_block(ws, row, assumptions)

        # Section I: Working Capital
        row = self._add_section_header(ws, row, "I. WORKING CAPITAL ASSUMPTIONS")
        assumptions = [
            ("Raw materials inventory (days)", 30, "INPUT"),
            ("Finished goods inventory (days)", 45, "INPUT"),
            ("Accounts receivable (days)", 30, "INPUT"),
            ("Accounts payable (days)", 30, "INPUT"),
            ("Farmer payment terms", "Immediate", "INPUT"),
            ("Seasonal working capital peak multiplier", 1.5, "INPUT"),
            ("Cash buffer (days of operating costs)", 15, "INPUT"),
        ]
        row = self._add_assumptions_block(ws, row, assumptions)

        # Section J: Macroeconomic
        row = self._add_section_header(ws, row, "J. MACROECONOMIC ASSUMPTIONS")
        assumptions = [
            ("XAF/USD exchange rate", 600, "INPUT"),
            ("General inflation rate (%/year)", 3, "INPUT"),
            ("USD reporting required", "Yes", "INPUT"),
            ("Discount rate for NPV (%)", 12, "INPUT"),
            ("Terminal growth rate (%)", 2, "INPUT"),
        ]
        row = self._add_assumptions_block(ws, row, assumptions)

        # Section K: Scenario Analysis
        row = self._add_section_header(ws, row, "K. SCENARIO TOGGLES")
        assumptions = [
            ("Active scenario", "Base", "DROPDOWN"),
            ("", "", ""),
            ("DOWNSIDE SCENARIO ADJUSTMENTS", "", ""),
            ("Yield adjustment (%)", -20, "INPUT"),
            ("Price adjustment (%)", -15, "INPUT"),
            ("CAPEX overrun (%)", 15, "INPUT"),
            ("Operating cost increase (%)", 10, "INPUT"),
            ("Ramp-up delay (months)", 6, "INPUT"),
            ("", "", ""),
            ("UPSIDE SCENARIO ADJUSTMENTS", "", ""),
            ("Yield adjustment (%)", 10, "INPUT"),
            ("Price adjustment (%)", 10, "INPUT"),
            ("CAPEX savings (%)", -5, "INPUT"),
            ("Operating cost reduction (%)", -5, "INPUT"),
            ("Accelerated ramp-up (months)", -3, "INPUT"),
        ]
        row = self._add_assumptions_block(ws, row, assumptions)

        # Format columns
        ws.column_dimensions['A'].width = 45
        ws.column_dimensions['B'].width = 15
        ws.column_dimensions['C'].width = 15
        ws.column_dimensions['D'].width = 12

        return ws

    def _add_section_header(self, ws, row, title):
        """Add a section header"""
        ws[f'A{row}'] = title
        ws[f'A{row}'].font = self.white_bold_font
        ws[f'A{row}'].fill = self.header_fill
        ws.merge_cells(f'A{row}:D{row}')
        ws[f'A{row}'].alignment = Alignment(horizontal='left', vertical='center')
        return row + 1

    def _add_assumptions_block(self, ws, start_row, assumptions):
        """Add a block of assumptions with proper formatting"""
        row = start_row
        for label, value, cell_type in assumptions:
            ws[f'A{row}'] = label

            if cell_type == "INPUT":
                ws[f'C{row}'] = value
                ws[f'C{row}'].fill = self.blue_fill
                ws[f'C{row}'].font = self.bold_font
                ws[f'D{row}'] = "INPUT"
                ws[f'D{row}'].fill = self.blue_fill
            elif cell_type == "CALC":
                if isinstance(value, str) and value.startswith("="):
                    # Replace row placeholders if present
                    formula = value.format(row=row)
                    ws[f'C{row}'] = formula
                else:
                    ws[f'C{row}'] = value
                ws[f'C{row}'].fill = self.yellow_fill
                ws[f'D{row}'] = "CALC"
                ws[f'D{row}'].fill = self.yellow_fill
            elif cell_type == "DATE":
                ws[f'C{row}'] = value
                ws[f'C{row}'].fill = self.blue_fill
                ws[f'C{row}'].number_format = 'mmm-yyyy'
                ws[f'D{row}'] = "INPUT"
                ws[f'D{row}'].fill = self.blue_fill
            elif cell_type == "DROPDOWN":
                ws[f'C{row}'] = value
                ws[f'C{row}'].fill = self.blue_fill
                ws[f'C{row}'].font = self.bold_font
                ws[f'D{row}'] = "SELECT"
                ws[f'D{row}'].fill = self.blue_fill
            elif label:  # Subsection header
                ws[f'A{row}'].font = Font(bold=True, italic=True)

            # Add borders
            for col in ['A', 'B', 'C', 'D']:
                ws[f'{col}{row}'].border = self.thin_border

            row += 1

        return row + 1  # Extra space after block

    def create_timeline_sheet(self):
        """Create monthly timeline for the model"""
        ws = self.wb.create_sheet("Timeline")

        # Headers
        ws['A1'] = "PROJECT TIMELINE"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:D1')

        ws['A3'] = "Month"
        ws['B3'] = "Date"
        ws['C3'] = "Quarter"
        ws['D3'] = "Year"
        ws['E3'] = "Phase"
        ws['F3'] = "Milestone"

        for col in ['A', 'B', 'C', 'D', 'E', 'F']:
            ws[f'{col}3'].font = self.bold_font
            ws[f'{col}3'].fill = self.gray_fill
            ws[f'{col}3'].border = self.thin_border

        # Generate monthly timeline (120 months = 10 years)
        current_date = self.start_date
        for month in range(1, 121):
            row = month + 3
            ws[f'A{row}'] = month
            ws[f'B{row}'] = current_date
            ws[f'B{row}'].number_format = 'mmm-yyyy'
            ws[f'C{row}'] = f"Q{((month-1) % 12) // 3 + 1}"
            ws[f'D{row}'] = f"Year {(month-1) // 12 + 1}"

            # Determine phase
            if month <= 18:
                phase = "Phase 1: Seed"
            elif month <= 42:
                phase = "Phase 2: Outgrower"
            elif month <= 78:
                phase = "Phase 3: Processing"
            elif month <= 96:
                phase = "Phase 4: Logistics"
            else:
                phase = "Phase 5: Circular"

            ws[f'E{row}'] = phase

            current_date += relativedelta(months=1)

        ws.column_dimensions['A'].width = 8
        ws.column_dimensions['B'].width = 12
        ws.column_dimensions['C'].width = 10
        ws.column_dimensions['D'].width = 10
        ws.column_dimensions['E'].width = 25
        ws.column_dimensions['F'].width = 40

        return ws

    def create_revenue_sheet(self):
        """Create revenue calculations sheet"""
        ws = self.wb.create_sheet("Revenue")

        # Header
        ws['A1'] = "REVENUE CALCULATIONS"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:M1')

        # Year headers
        ws['A3'] = "Revenue Stream"
        ws['B3'] = "Unit"
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 2)
            ws[f'{col}3'] = f"Year {year}"
            ws[f'{col}3'].font = self.bold_font
            ws[f'{col}3'].fill = self.gray_fill
            ws[f'{col}3'].alignment = self.center_align

        # Revenue streams
        row = 4
        streams = [
            ("SEED REVENUE", ""),
            ("G1 seed sales volume", "kg"),
            ("G1 seed price", "XAF/kg"),
            ("Seed revenue", "XAF"),
            ("", ""),
            ("WARE POTATO REVENUE", ""),
            ("Outgrower harvest volume", "tonnes"),
            ("Farmgate purchase value", "XAF"),
            ("", ""),
            ("PROCESSED PRODUCTS REVENUE", ""),
            ("French fries sales volume", "tonnes"),
            ("French fries price", "XAF/kg"),
            ("French fries revenue", "XAF"),
            ("", ""),
            ("Fresh pack sales volume", "tonnes"),
            ("Fresh pack price", "XAF/kg"),
            ("Fresh pack revenue", "XAF"),
            ("", ""),
            ("Animal feed sales volume", "tonnes"),
            ("Feed price", "XAF/kg"),
            ("Feed revenue", "XAF"),
            ("", ""),
            ("TOTAL REVENUE", "XAF"),
        ]

        for label, unit in streams:
            ws[f'A{row}'] = label
            ws[f'B{row}'] = unit

            if label in ["SEED REVENUE", "WARE POTATO REVENUE", "PROCESSED PRODUCTS REVENUE"]:
                ws[f'A{row}'].font = self.bold_font
                ws[f'A{row}'].fill = self.green_fill
            elif label == "TOTAL REVENUE":
                ws[f'A{row}'].font = self.bold_font
                ws[f'A{row}'].fill = self.header_fill
                ws[f'A{row}'].font = self.white_bold_font

            # Add formulas for each year
            for year in range(1, self.model_years + 1):
                col = get_column_letter(year + 2)

                # Reference assumptions sheet and build formulas
                if "G1 seed sales volume" in label:
                    ws[f'{col}{row}'] = f"=Assumptions!$C$15*1000"  # Convert tonnes to kg
                elif "G1 seed price" in label:
                    ws[f'{col}{row}'] = f"=Assumptions!$C$45*(1+Assumptions!$C$46/100)^({year}-1)"
                elif "Seed revenue" in label and "XAF" in unit:
                    ws[f'{col}{row}'] = f"={col}{row-2}*{col}{row-1}"
                    ws[f'{col}{row}'].number_format = '#,##0'
                elif "Outgrower harvest volume" in label:
                    if year == 1:
                        farmers = "Assumptions!$C$23"
                    elif year == 2:
                        farmers = "Assumptions!$C$24"
                    else:
                        farmers = "Assumptions!$C$25"
                    ws[f'{col}{row}'] = f"={farmers}*Assumptions!$C$26*Assumptions!$C$27"
                elif "French fries sales volume" in label:
                    capacity_util = f"Assumptions!$C${50 + min(year-1, 2)}"  # Years 1,2,3+
                    ws[f'{col}{row}'] = f"=Assumptions!$C$47*Assumptions!$C$48*Assumptions!$C$49*{capacity_util}/100*Assumptions!$C$68/100"
                elif "French fries price" in label:
                    ws[f'{col}{row}'] = f"=Assumptions!$C$65*(1+Assumptions!$C$57/100)^({year}-1)"
                elif "French fries revenue" in label:
                    ws[f'{col}{row}'] = f"={col}{row-2}*{col}{row-1}*1000"
                    ws[f'{col}{row}'].number_format = '#,##0'
                elif "TOTAL REVENUE" in label:
                    ws[f'{col}{row}'] = f"={col}{row-19}+{col}{row-11}+{col}{row-4}"
                    ws[f'{col}{row}'].number_format = '#,##0'
                    ws[f'{col}{row}'].font = self.bold_font

            row += 1

        # Format columns
        ws.column_dimensions['A'].width = 35
        ws.column_dimensions['B'].width = 12
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 2)
            ws.column_dimensions[col].width = 15

        return ws

    def create_operating_costs_sheet(self):
        """Create operating costs sheet"""
        ws = self.wb.create_sheet("Operating Costs")

        # Header
        ws['A1'] = "OPERATING COSTS"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:M1')

        # Year headers
        ws['A3'] = "Cost Category"
        ws['B3'] = "Unit"
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 2)
            ws[f'{col}3'] = f"Year {year}"
            ws[f'{col}3'].font = self.bold_font
            ws[f'{col}3'].fill = self.gray_fill

        # Cost categories
        row = 4
        categories = [
            ("SEED PRODUCTION COSTS", ""),
            ("G0 import cost", "XAF"),
            ("Multiplication cost", "XAF"),
            ("Storage cost", "XAF"),
            ("Total seed costs", "XAF"),
            ("", ""),
            ("OUTGROWER COSTS", ""),
            ("Input packages", "XAF"),
            ("Extension services", "XAF"),
            ("Total outgrower costs", "XAF"),
            ("", ""),
            ("PROCESSING COSTS", ""),
            ("Direct labor", "XAF"),
            ("Utilities", "XAF"),
            ("Packaging", "XAF"),
            ("Maintenance", "XAF"),
            ("Total processing costs", "XAF"),
            ("", ""),
            ("OVERHEAD & ADMIN", ""),
            ("Management & staff", "XAF"),
            ("Office expenses", "XAF"),
            ("Insurance", "XAF"),
            ("Professional services", "XAF"),
            ("Total overhead", "XAF"),
            ("", ""),
            ("LOGISTICS", ""),
            ("Transport", "XAF"),
            ("Cold storage", "XAF"),
            ("Total logistics", "XAF"),
            ("", ""),
            ("TOTAL OPERATING COSTS", "XAF"),
        ]

        for label, unit in categories:
            ws[f'A{row}'] = label
            ws[f'B{row}'] = unit

            if "COSTS" in label and "Total" not in label and "XAF" not in unit:
                ws[f'A{row}'].font = self.bold_font
                ws[f'A{row}'].fill = PatternFill(start_color="F4B084", end_color="F4B084", fill_type="solid")
            elif "Total" in label or "TOTAL" in label:
                ws[f'A{row}'].font = self.bold_font
                ws[f'A{row}'].fill = self.gray_fill

            # Add formulas
            for year in range(1, self.model_years + 1):
                col = get_column_letter(year + 2)
                inflation = f"(1+Assumptions!$C$119/100)^({year}-1)"

                if "G0 import cost" in label:
                    ws[f'{col}{row}'] = f"=Assumptions!$C$86*Assumptions!$C$14*1000*{inflation}"
                elif "Multiplication cost" in label:
                    ws[f'{col}{row}'] = f"=Assumptions!$C$87*Assumptions!$C$15*1000*{inflation}"
                elif "Total seed costs" in label:
                    ws[f'{col}{row}'] = f"=SUM({col}{row-3}:{col}{row-1})"
                elif "Input packages" in label:
                    if year == 1:
                        farmers = "Assumptions!$C$23"
                    elif year == 2:
                        farmers = "Assumptions!$C$24"
                    else:
                        farmers = "Assumptions!$C$25"
                    ws[f'{col}{row}'] = f"={farmers}*Assumptions!$C$93*{inflation}"
                elif "Extension services" in label:
                    if year == 1:
                        farmers = "Assumptions!$C$23"
                    elif year == 2:
                        farmers = "Assumptions!$C$24"
                    else:
                        farmers = "Assumptions!$C$25"
                    ws[f'{col}{row}'] = f"={farmers}*Assumptions!$C$94*{inflation}"
                elif "Total outgrower costs" in label:
                    ws[f'{col}{row}'] = f"=SUM({col}{row-2}:{col}{row-1})"
                elif "Management & staff" in label:
                    ws[f'{col}{row}'] = f"=(Assumptions!$C$107+Assumptions!$C$108)*12*{inflation}"
                elif "TOTAL OPERATING COSTS" in label:
                    ws[f'{col}{row}'] = f"={col}{row-26}+{col}{row-20}+{col}{row-13}+{col}{row-6}+{col}{row-2}"
                    ws[f'{col}{row}'].font = self.bold_font

                if "XAF" in unit:
                    ws[f'{col}{row}'].number_format = '#,##0'

            row += 1

        # Format columns
        ws.column_dimensions['A'].width = 35
        ws.column_dimensions['B'].width = 12
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 2)
            ws.column_dimensions[col].width = 15

        return ws

    def create_capex_sheet(self):
        """Create CAPEX schedule"""
        ws = self.wb.create_sheet("CAPEX Schedule")

        # Header
        ws['A1'] = "CAPITAL EXPENDITURE SCHEDULE"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:M1')

        # Year headers
        ws['A3'] = "Phase / Item"
        ws['B3'] = "Total Budget"
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 2)
            ws[f'{col}3'] = f"Year {year}"
            ws[f'{col}3'].font = self.bold_font
            ws[f'{col}3'].fill = self.gray_fill

        # CAPEX by phase
        row = 4
        phases = [
            ("PHASE 1: Seed Multiplication", "=Assumptions!$C$130"),
            ("PHASE 2: Outgrower Network", "=Assumptions!$C$138"),
            ("PHASE 3: Processing Facility", "=Assumptions!$C$149"),
            ("PHASE 4: Logistics", "=Assumptions!$C$159"),
            ("PHASE 5: Circular Economy", "=Assumptions!$C$167"),
            ("", ""),
            ("TOTAL CAPEX", "=Assumptions!$C$170"),
            ("", ""),
            ("Cumulative CAPEX", ""),
        ]

        for label, formula in phases:
            ws[f'A{row}'] = label
            if formula:
                ws[f'B{row}'] = formula
                ws[f'B{row}'].number_format = '#,##0'

            if "PHASE" in label:
                ws[f'A{row}'].font = self.bold_font
                ws[f'A{row}'].fill = self.green_fill
            elif "TOTAL" in label:
                ws[f'A{row}'].font = self.white_bold_font
                ws[f'A{row}'].fill = self.header_fill
                ws[f'B{row}'].font = self.bold_font

            # Distribute CAPEX over construction periods
            for year in range(1, self.model_years + 1):
                col = get_column_letter(year + 2)

                if "PHASE 1" in label:
                    # 18 months = 1.5 years, spend in Year 1 and Year 2
                    if year == 1:
                        ws[f'{col}{row}'] = f"=$B{row}*0.6"
                    elif year == 2:
                        ws[f'{col}{row}'] = f"=$B{row}*0.4"
                    else:
                        ws[f'{col}{row}'] = 0
                elif "PHASE 2" in label:
                    # 24 months = 2 years, spend in Year 2 and Year 3
                    if year == 2:
                        ws[f'{col}{row}'] = f"=$B{row}*0.5"
                    elif year == 3:
                        ws[f'{col}{row}'] = f"=$B{row}*0.5"
                    else:
                        ws[f'{col}{row}'] = 0
                elif "PHASE 3" in label:
                    # 36 months = 3 years, spend in Year 2, 3, 4
                    if year == 2:
                        ws[f'{col}{row}'] = f"=$B{row}*0.2"
                    elif year == 3:
                        ws[f'{col}{row}'] = f"=$B{row}*0.5"
                    elif year == 4:
                        ws[f'{col}{row}'] = f"=$B{row}*0.3"
                    else:
                        ws[f'{col}{row}'] = 0
                elif "PHASE 4" in label:
                    if year == 4:
                        ws[f'{col}{row}'] = f"=$B{row}*0.7"
                    elif year == 5:
                        ws[f'{col}{row}'] = f"=$B{row}*0.3"
                    else:
                        ws[f'{col}{row}'] = 0
                elif "PHASE 5" in label:
                    if year == 5:
                        ws[f'{col}{row}'] = f"=$B{row}"
                    else:
                        ws[f'{col}{row}'] = 0
                elif "TOTAL CAPEX" in label:
                    ws[f'{col}{row}'] = f"=SUM({col}{row-6}:{col}{row-2})"
                    ws[f'{col}{row}'].font = self.bold_font
                elif "Cumulative" in label:
                    if year == 1:
                        ws[f'{col}{row}'] = f"={col}{row-2}"
                    else:
                        prev_col = get_column_letter(year + 1)
                        ws[f'{col}{row}'] = f"={prev_col}{row}+{col}{row-2}"

                ws[f'{col}{row}'].number_format = '#,##0'

            row += 1

        # Format columns
        ws.column_dimensions['A'].width = 35
        ws.column_dimensions['B'].width = 18
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 2)
            ws.column_dimensions[col].width = 15

        return ws

    def create_debt_schedule_sheet(self):
        """Create debt schedule"""
        ws = self.wb.create_sheet("Debt Schedule")

        # Header
        ws['A1'] = "DEBT SCHEDULE"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:M1')

        # Year headers
        ws['A3'] = "Item"
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            ws[f'{col}3'] = f"Year {year}"
            ws[f'{col}3'].font = self.bold_font
            ws[f'{col}3'].fill = self.gray_fill

        row = 4

        # Senior Debt section
        items = [
            ("SENIOR DEBT", ""),
            ("Opening balance", ""),
            ("Drawdowns", ""),
            ("Principal repayment", ""),
            ("Closing balance", ""),
            ("Interest expense", ""),
            ("Commitment fee", ""),
            ("Total debt service", ""),
            ("", ""),
            ("SUBORDINATED DEBT", ""),
            ("Opening balance", ""),
            ("Drawdowns", ""),
            ("Principal repayment", ""),
            ("Closing balance", ""),
            ("Interest expense", ""),
            ("PIK interest", ""),
            ("Total debt service", ""),
            ("", ""),
            ("TOTAL DEBT", ""),
            ("Total opening balance", ""),
            ("Total drawdowns", ""),
            ("Total principal repayment", ""),
            ("Total closing balance", ""),
            ("Total interest expense", ""),
            ("Total debt service", ""),
        ]

        for label, desc in items:
            ws[f'A{row}'] = label

            if "SENIOR DEBT" in label or "SUBORDINATED" in label or "TOTAL DEBT" in label:
                ws[f'A{row}'].font = self.bold_font
                ws[f'A{row}'].fill = self.green_fill

            # Add formulas for each year
            for year in range(1, self.model_years + 1):
                col = get_column_letter(year + 1)

                # Senior debt calculations
                if label == "Opening balance" and row == 5:
                    if year == 1:
                        ws[f'{col}{row}'] = 0
                    else:
                        prev_col = get_column_letter(year)
                        ws[f'{col}{row}'] = f"={prev_col}{row+3}"
                elif label == "Drawdowns" and row == 6:
                    ws[f'{col}{row}'] = f"='CAPEX Schedule'!{col}11*Assumptions!$C$189/100"
                elif label == "Principal repayment" and row == 7:
                    grace_period = 3
                    tenor = 10
                    if year <= grace_period:
                        ws[f'{col}{row}'] = 0
                    else:
                        # Equal principal repayment
                        ws[f'{col}{row}'] = f"=(Assumptions!$C$170*Assumptions!$C$189/100)/({tenor}-{grace_period})"
                elif label == "Closing balance" and row == 8:
                    ws[f'{col}{row}'] = f"={col}{row-3}+{col}{row-2}-{col}{row-1}"
                elif label == "Interest expense" and row == 9:
                    ws[f'{col}{row}'] = f"=({col}{row-4}+{col}{row-1})/2*Assumptions!$C$190/100"
                elif label == "Total debt service" and row == 11:
                    ws[f'{col}{row}'] = f"={col}{row-4}+{col}{row-2}+{col}{row-1}"

                # Subordinated debt calculations
                elif label == "Opening balance" and row == 14:
                    if year == 1:
                        ws[f'{col}{row}'] = 0
                    else:
                        prev_col = get_column_letter(year)
                        ws[f'{col}{row}'] = f"={prev_col}{row+3}"
                elif label == "Drawdowns" and row == 15:
                    ws[f'{col}{row}'] = f"='CAPEX Schedule'!{col}11*Assumptions!$C$198/100"
                elif label == "Principal repayment" and row == 16:
                    grace_period = 5
                    tenor = 8
                    if year <= grace_period:
                        ws[f'{col}{row}'] = 0
                    else:
                        ws[f'{col}{row}'] = f"=(Assumptions!$C$170*Assumptions!$C$198/100)/({tenor}-{grace_period})"
                elif label == "Closing balance" and row == 17:
                    ws[f'{col}{row}'] = f"={col}{row-3}+{col}{row-2}-{col}{row-1}"
                elif label == "Interest expense" and row == 18:
                    ws[f'{col}{row}'] = f"=({col}{row-4}+{col}{row-1})/2*Assumptions!$C$199/100"
                elif label == "Total debt service" and row == 20:
                    ws[f'{col}{row}'] = f"={col}{row-4}+{col}{row-2}"

                # Total debt
                elif label == "Total opening balance":
                    ws[f'{col}{row}'] = f"={col}{row-18}+{col}{row-9}"
                elif label == "Total drawdowns":
                    ws[f'{col}{row}'] = f"={col}{row-18}+{col}{row-9}"
                elif label == "Total principal repayment":
                    ws[f'{col}{row}'] = f"={col}{row-18}+{col}{row-9}"
                elif label == "Total closing balance":
                    ws[f'{col}{row}'] = f"={col}{row-18}+{col}{row-9}"
                elif label == "Total interest expense":
                    ws[f'{col}{row}'] = f"={col}{row-18}+{col}{row-11}"
                elif label == "Total debt service":
                    ws[f'{col}{row}'] = f"={col}{row-15}+{col}{row-6}"
                    ws[f'{col}{row}'].font = self.bold_font

                ws[f'{col}{row}'].number_format = '#,##0'

            row += 1

        # Format columns
        ws.column_dimensions['A'].width = 30
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            ws.column_dimensions[col].width = 15

        return ws

    def create_financial_statements(self):
        """Create P&L, Balance Sheet, and Cash Flow statements"""

        # P&L Statement
        ws_pl = self.wb.create_sheet("P&L Statement")
        ws_pl['A1'] = "PROFIT & LOSS STATEMENT"
        ws_pl['A1'].font = self.header_font
        ws_pl['A1'].fill = self.header_fill
        ws_pl.merge_cells('A1:M1')

        # Headers
        ws_pl['A3'] = "Line Item"
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            ws_pl[f'{col}3'] = f"Year {year}"
            ws_pl[f'{col}3'].font = self.bold_font
            ws_pl[f'{col}3'].fill = self.gray_fill

        row = 4
        pl_items = [
            ("Revenue", "=Revenue!C26"),
            ("", ""),
            ("Operating Costs", "=-'Operating Costs'!C34"),
            ("", ""),
            ("EBITDA", "=B4+B6"),
            ("EBITDA margin (%)", "=B8/B4*100"),
            ("", ""),
            ("Depreciation", "=0"),  # Will add depreciation sheet
            ("", ""),
            ("EBIT", "=B8+B11"),
            ("EBIT margin (%)", "=B13/B4*100"),
            ("", ""),
            ("Interest expense", "=-'Debt Schedule'!B27"),
            ("", ""),
            ("EBT", "=B13+B16"),
            ("", ""),
            ("Tax expense", "=0"),  # Will add tax calculation
            ("", ""),
            ("Net Income", "=B18+B21"),
            ("Net margin (%)", "=B23/B4*100"),
        ]

        for label, formula in pl_items:
            ws_pl[f'A{row}'] = label

            if label in ["Revenue", "EBITDA", "EBIT", "EBT", "Net Income"]:
                ws_pl[f'A{row}'].font = self.bold_font

            if formula:
                for year in range(1, self.model_years + 1):
                    col = get_column_letter(year + 1)
                    # Adjust column in formula
                    year_formula = formula.replace('!B', f'!{col}').replace('!C', f'!{col}')
                    ws_pl[f'{col}{row}'] = year_formula
                    if "%" in label:
                        ws_pl[f'{col}{row}'].number_format = '0.0%'
                    else:
                        ws_pl[f'{col}{row}'].number_format = '#,##0'

            row += 1

        ws_pl.column_dimensions['A'].width = 30
        for year in range(1, self.model_years + 1):
            col = get_column_letter(year + 1)
            ws_pl.column_dimensions[col].width = 15

        return ws_pl

    def create_returns_analysis(self):
        """Create returns and ratios analysis"""
        ws = self.wb.create_sheet("Returns Analysis")

        ws['A1'] = "RETURNS & FINANCIAL RATIOS"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:D1')

        row = 3
        metrics = [
            ("PROJECT RETURNS", "", ""),
            ("Project IRR (%)", "=IRR('Cash Flow'!C50:L50)", "%"),
            ("Equity IRR (%)", "=IRR('Cash Flow'!C52:L52)", "%"),
            ("NPV @ 12% (XAF)", "=NPV(12%,'Cash Flow'!D50:L50)+'Cash Flow'!C50", "#,##0"),
            ("Payback period (years)", "", ""),
            ("", "", ""),
            ("PROFITABILITY RATIOS", "", ""),
            ("Average EBITDA margin (%)", "=AVERAGE('P&L Statement'!C9:L9)", "%"),
            ("Average net margin (%)", "=AVERAGE('P&L Statement'!C24:L24)", "%"),
            ("Return on assets (%)", "", "%"),
            ("Return on equity (%)", "", "%"),
            ("", "", ""),
            ("LEVERAGE RATIOS", "", ""),
            ("Debt to equity (average)", "", ""),
            ("Debt to EBITDA (Year 5)", "", ""),
            ("Interest coverage (average)", "", ""),
            ("DSCR - minimum", "", ""),
            ("DSCR - average", "", ""),
            ("", "", ""),
            ("OPERATIONAL METRICS", "", ""),
            ("Revenue CAGR (%)", "", "%"),
            ("EBITDA CAGR (%)", "", "%"),
            ("Capacity utilization (Year 5, %)", "=Assumptions!$C$52", "%"),
            ("", "", ""),
            ("VALUATION", "", ""),
            ("Terminal value (XAF)", "", "#,##0"),
            ("Enterprise value (XAF)", "", "#,##0"),
            ("Equity value (XAF)", "", "#,##0"),
        ]

        for label, formula, fmt in metrics:
            ws[f'A{row}'] = label
            if formula:
                ws[f'C{row}'] = formula
                if fmt == "%":
                    ws[f'C{row}'].number_format = '0.0%'
                elif fmt:
                    ws[f'C{row}'].number_format = fmt

            if any(x in label for x in ["PROJECT", "PROFITABILITY", "LEVERAGE", "OPERATIONAL", "VALUATION"]):
                ws[f'A{row}'].font = self.bold_font
                ws[f'A{row}'].fill = self.green_fill

            row += 1

        ws.column_dimensions['A'].width = 35
        ws.column_dimensions['B'].width = 5
        ws.column_dimensions['C'].width = 20

        return ws

    def create_sensitivity_analysis(self):
        """Create sensitivity analysis dashboard"""
        ws = self.wb.create_sheet("Sensitivity Analysis")

        ws['A1'] = "SENSITIVITY ANALYSIS"
        ws['A1'].font = self.header_font
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:F1')

        ws['A3'] = "KEY ASSUMPTIONS TO TEST:"
        ws['A3'].font = self.bold_font

        row = 4
        variables = [
            "1. Yield per hectare (±20%)",
            "2. Product pricing (±15%)",
            "3. CAPEX costs (±15%)",
            "4. Operating costs (±10%)",
            "5. Capacity utilization (±10%)",
            "6. Interest rates (±200 bps)",
            "7. Ramp-up timing (±6 months)",
        ]

        for var in variables:
            ws[f'A{row}'] = var
            row += 1

        row += 2
        ws[f'A{row}'] = "SCENARIO SUMMARY"
        ws[f'A{row}'].font = self.bold_font
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
        scenarios = ["Base Case", "Downside", "Upside"]
        for scenario in scenarios:
            ws[f'A{row}'] = scenario
            # Formulas will reference scenario toggles in Assumptions
            row += 1

        ws.column_dimensions['A'].width = 25
        for col in ['B', 'C', 'D', 'E', 'F']:
            ws.column_dimensions[col].width = 15

        return ws

    def create_dashboard(self):
        """Create executive dashboard"""
        ws = self.wb.create_sheet("Dashboard", 0)  # Insert as first sheet

        ws['A1'] = "FINANCIAL MODEL - EXECUTIVE DASHBOARD"
        ws['A1'].font = Font(bold=True, size=16, color="FFFFFF")
        ws['A1'].fill = self.header_fill
        ws.merge_cells('A1:F1')

        ws['A3'] = "Project Overview"
        ws['A3'].font = Font(bold=True, size=12)
        ws['A3'].fill = self.green_fill
        ws.merge_cells('A3:F3')

        row = 4
        overview = [
            ("Total Investment (CAPEX)", "=Assumptions!C170", "XAF"),
            ("Equity Required", "=Assumptions!C170*Assumptions!C186/100", "XAF"),
            ("Senior Debt", "=Assumptions!C170*Assumptions!C189/100", "XAF"),
            ("Mezzanine Debt", "=Assumptions!C170*Assumptions!C198/100", "XAF"),
            ("Grant Funding", "=Assumptions!C205", "XAF"),
            ("", "", ""),
            ("Construction Period", "=Assumptions!C10", "months"),
            ("Operations Start", "=Assumptions!C17", "date"),
            ("Model Horizon", "=Assumptions!C9", "years"),
        ]

        for label, formula, unit in overview:
            ws[f'A{row}'] = label
            ws[f'C{row}'] = formula if formula else ""
            ws[f'D{row}'] = unit

            if formula:
                if unit == "XAF":
                    ws[f'C{row}'].number_format = '#,##0'
                elif unit == "date":
                    ws[f'C{row}'].number_format = 'mmm-yyyy'
            row += 1

        row += 1
        ws[f'A{row}'] = "Key Returns"
        ws[f'A{row}'].font = Font(bold=True, size=12)
        ws[f'A{row}'].fill = self.green_fill
        ws.merge_cells(f'A{row}:F{row}')

        row += 1
        returns = [
            ("Project IRR", "='Returns Analysis'!C4", "%"),
            ("Equity IRR", "='Returns Analysis'!C5", "%"),
            ("NPV @ 12%", "='Returns Analysis'!C6", "XAF"),
            ("Min DSCR", "='Returns Analysis'!C20", "x"),
            ("Avg EBITDA Margin", "='Returns Analysis'!C10", "%"),
        ]

        for label, formula, unit in returns:
            ws[f'A{row}'] = label
            ws[f'C{row}'] = formula
            ws[f'D{row}'] = unit

            if "%" in unit:
                ws[f'C{row}'].number_format = '0.0%'
            elif unit == "XAF":
                ws[f'C{row}'].number_format = '#,##0'
            else:
                ws[f'C{row}'].number_format = '0.0'
            row += 1

        ws.column_dimensions['A'].width = 30
        ws.column_dimensions['C'].width = 20
        ws.column_dimensions['D'].width = 10

        return ws

    def build(self, filename="Financial_Model_Agricultural_Processing.xlsx"):
        """Build the complete financial model"""
        print("Building financial model...")

        # Create all sheets
        print("  Creating Assumptions sheet...")
        self.create_assumptions_sheet()

        print("  Creating Timeline...")
        self.create_timeline_sheet()

        print("  Creating Revenue calculations...")
        self.create_revenue_sheet()

        print("  Creating Operating Costs...")
        self.create_operating_costs_sheet()

        print("  Creating CAPEX Schedule...")
        self.create_capex_sheet()

        print("  Creating Debt Schedule...")
        self.create_debt_schedule_sheet()

        print("  Creating Financial Statements...")
        self.create_financial_statements()

        print("  Creating Returns Analysis...")
        self.create_returns_analysis()

        print("  Creating Sensitivity Analysis...")
        self.create_sensitivity_analysis()

        print("  Creating Dashboard...")
        self.create_dashboard()

        # Save workbook
        print(f"\nSaving workbook to {filename}...")
        self.wb.save(filename)
        print(f"✓ Financial model created successfully: {filename}")

        return filename

if __name__ == "__main__":
    builder = FinancialModelBuilder()
    builder.build()
