#!/usr/bin/env python3
"""
Santa Fresh Potato Value Chain - Financial Model Builder
=========================================================

This script builds a comprehensive DFI-grade financial model customized for
the EIC Integrated Potato Value Chain project.

Key Design Principles:
- NO hard-coded values in Assumptions (all blank/placeholder for user input)
- All formulas reference Assumptions sheet
- Medium granularity (20-30 cost categories)
- Scenario analysis with Base/Downside/Upside toggles
- Phased CAPEX deployment (Phase 1/2/3)
- Development impact metrics

Target completion: 4-5 days
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import datetime

class SantaFreshModelBuilder:
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.wb.remove(self.wb.active)  # Remove default sheet

        # Define color scheme
        self.colors = {
            'input': 'ADD8E6',      # Light blue for user inputs
            'calculated': 'FFFF99', # Light yellow for calculated values
            'header': '4472C4',     # Dark blue for headers
            'section': 'D0CECE',    # Light gray for section headers
            'toggle': '90EE90',     # Light green for scenario toggles
        }

        # Define fonts
        self.fonts = {
            'header': Font(name='Calibri', size=12, bold=True, color='FFFFFF'),
            'section': Font(name='Calibri', size=11, bold=True),
            'label': Font(name='Calibri', size=10),
            'input': Font(name='Calibri', size=10),
        }

        # Border styles
        thin_border = Side(style='thin', color='000000')
        self.border = Border(left=thin_border, right=thin_border,
                            top=thin_border, bottom=thin_border)

    def create_assumptions_sheet(self):
        """
        Create the master Assumptions sheet with Sections A-U.
        ALL inputs are blank/placeholder for user population.
        """
        ws = self.wb.create_sheet("Assumptions", 0)

        # Set column widths
        ws.column_dimensions['A'].width = 50
        ws.column_dimensions['B'].width = 20
        ws.column_dimensions['C'].width = 20
        ws.column_dimensions['D'].width = 15

        row = 1

        # Main header
        ws.merge_cells(f'A{row}:D{row}')
        ws[f'A{row}'] = "SANTA FRESH POTATO VALUE CHAIN - FINANCIAL MODEL ASSUMPTIONS"
        ws[f'A{row}'].font = Font(name='Calibri', size=14, bold=True, color='FFFFFF')
        ws[f'A{row}'].fill = PatternFill(start_color=self.colors['header'],
                                          end_color=self.colors['header'],
                                          fill_type='solid')
        ws[f'A{row}'].alignment = Alignment(horizontal='center', vertical='center')
        row += 1

        # Instructions
        ws.merge_cells(f'A{row}:D{row}')
        ws[f'A{row}'] = "INSTRUCTIONS: BLUE cells = Your inputs (editable) | YELLOW cells = Auto-calculated | GREEN cells = Scenario toggles"
        ws[f'A{row}'].font = Font(name='Calibri', size=9, italic=True)
        ws[f'A{row}'].fill = PatternFill(start_color='E7E6E6', end_color='E7E6E6', fill_type='solid')
        row += 2

        # Column headers
        headers = ['Parameter', 'Value', 'Unit', 'Notes']
        for col_idx, header in enumerate(headers, start=1):
            cell = ws.cell(row=row, column=col_idx, value=header)
            cell.font = self.fonts['header']
            cell.fill = PatternFill(start_color=self.colors['header'],
                                   end_color=self.colors['header'],
                                   fill_type='solid')
            cell.alignment = Alignment(horizontal='center', vertical='center')
        row += 1

        # ===================================================================
        # SECTION A: PROJECT TIMELINE & PHASING
        # ===================================================================
        row = self._add_section_header(ws, row, "A. PROJECT TIMELINE & PHASING")

        timeline_params = [
            ("Model start year", "", "Year", "e.g., 2026"),
            ("Model horizon (years)", "", "Years", "e.g., 10"),
            ("Construction start date", "", "Date", "e.g., Q2 2026"),
            ("Phase 1 duration (months)", "", "Months", "Seed/farm/fresh-pack/storage foundation"),
            ("Phase 2 duration (months)", "", "Months", "Frozen line + Douala depot"),
            ("Phase 3 duration (months)", "", "Months", "3 additional depots"),
            ("Operations start - Fresh-pack", "", "Date", "e.g., Q1 2027"),
            ("Operations start - Frozen line", "", "Date", "e.g., Q3 2028"),
        ]

        for label, value, unit, note in timeline_params:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1

        # ===================================================================
        # SECTION B: REVENUE STREAMS & PRODUCTS
        # ===================================================================
        row = self._add_section_header(ws, row, "B. REVENUE STREAMS & PRODUCTS")

        # B1: Fresh-Pack Table Potatoes
        row = self._add_subsection_header(ws, row, "B1: Fresh-Pack Table Potatoes")

        freshpack_params = [
            ("Annual target volume - Year 1", "", "Tonnes", ""),
            ("Annual target volume - Year 2", "", "Tonnes", ""),
            ("Annual target volume - Year 3+", "", "Tonnes", ""),
            ("Selling price (XAF/kg)", "", "XAF/kg", ""),
            ("Price escalation", "", "%/year", ""),
            ("Customer payment terms", "", "Days", "Weighted average across segments"),
        ]

        for label, value, unit, note in freshpack_params:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1

        # B2: Frozen French Fries
        row = self._add_subsection_header(ws, row, "B2: Frozen French Fries")

        frozen_params = [
            ("Annual target volume - Year 1", "", "Tonnes", ""),
            ("Annual target volume - Year 2", "", "Tonnes", ""),
            ("Annual target volume - Year 3+", "", "Tonnes", ""),
            ("Selling price (XAF/kg)", "", "XAF/kg", ""),
            ("Price escalation", "", "%/year", ""),
            ("Customer payment terms", "", "Days", ""),
        ]

        for label, value, unit, note in frozen_params:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1

        # B3: Certified Seed Sales
        row = self._add_subsection_header(ws, row, "B3: Certified Seed Sales")

        seed_params = [
            ("Annual sales volume", "", "Tonnes", "G1 seed sold to external customers"),
            ("Selling price (XAF/kg)", "", "XAF/kg", ""),
            ("Price escalation", "", "%/year", ""),
        ]

        for label, value, unit, note in seed_params:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1

        # B4: Animal Feed Pellets
        row = self._add_subsection_header(ws, row, "B4: Animal Feed Pellets (Byproduct)")

        feed_params = [
            ("Organic waste generation rate", "", "kg/tonne", "Peels + rejects per tonne processed"),
            ("Feed conversion rate", "", "%", "Waste to finished pellets"),
            ("Feed selling price (XAF/kg)", "", "XAF/kg", ""),
            ("Feed price escalation", "", "%/year", ""),
        ]

        for label, value, unit, note in feed_params:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1

        # B5: Revenue Seasonality
        row = self._add_subsection_header(ws, row, "B5: Revenue Seasonality (Monthly Distribution)")

        months = ['January', 'February', 'March', 'April', 'May', 'June',
                 'July', 'August', 'September', 'October', 'November', 'December']

        for month in months:
            row = self._add_input_row(ws, row, f"{month} revenue", "", "% of annual", "")

        row += 1

        # ===================================================================
        # SECTION C: PROCESSING CAPACITY & UTILIZATION
        # ===================================================================
        row = self._add_section_header(ws, row, "C. PROCESSING CAPACITY & UTILIZATION")

        # C1: Fresh-Pack Line
        row = self._add_subsection_header(ws, row, "C1: Fresh-Pack Line")

        freshpack_capacity = [
            ("Installed capacity", "", "Tonnes/hour", ""),
            ("Operating hours per day", "", "Hours", ""),
            ("Operating days per year", "", "Days", ""),
            ("Maintenance downtime", "", "Days/year", ""),
            ("Year 1 utilization", "", "%", ""),
            ("Year 2 utilization", "", "%", ""),
            ("Year 3+ utilization", "", "%", ""),
        ]

        for label, value, unit, note in freshpack_capacity:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1

        # C2: Frozen French Fry Line
        row = self._add_subsection_header(ws, row, "C2: Frozen French Fry Line")

        frozen_capacity = [
            ("Installed capacity (raw input)", "", "Tonnes/hour", ""),
            ("Operating hours per day", "", "Hours", ""),
            ("Operating days per year", "", "Days", ""),
            ("Maintenance downtime", "", "Days/year", ""),
            ("Year 1 utilization", "", "%", ""),
            ("Year 2 utilization", "", "%", ""),
            ("Year 3+ utilization", "", "%", ""),
        ]

        for label, value, unit, note in frozen_capacity:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1

        # C3: Processing Yield Factors
        row = self._add_subsection_header(ws, row, "C3: Processing Yield Factors")

        yield_factors = [
            ("Fresh-pack yield", "", "%", "% of raw input yielding finished product"),
            ("Frozen fry conversion rate", "", "%", "Raw potato to finished frozen fries"),
            ("Peeling loss rate", "", "%", ""),
            ("Reject rate (quality)", "", "%", ""),
        ]

        for label, value, unit, note in yield_factors:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1

        print(f"Built Assumptions sheet up to row {row} - Sections A, B, C complete")

        # Store the current row for continuing in next method
        return ws, row

    def _add_section_header(self, ws, row, title):
        """Add a major section header (A, B, C, etc.)"""
        ws.merge_cells(f'A{row}:D{row}')
        ws[f'A{row}'] = title
        ws[f'A{row}'].font = Font(name='Calibri', size=12, bold=True)
        ws[f'A{row}'].fill = PatternFill(start_color=self.colors['section'],
                                         end_color=self.colors['section'],
                                         fill_type='solid')
        ws[f'A{row}'].alignment = Alignment(horizontal='left', vertical='center')
        return row + 1

    def _add_subsection_header(self, ws, row, title):
        """Add a subsection header (B1, B2, etc.)"""
        ws.merge_cells(f'A{row}:D{row}')
        ws[f'A{row}'] = title
        ws[f'A{row}'].font = Font(name='Calibri', size=10, bold=True, italic=True)
        ws[f'A{row}'].fill = PatternFill(start_color='F2F2F2',
                                         end_color='F2F2F2',
                                         fill_type='solid')
        ws[f'A{row}'].alignment = Alignment(horizontal='left', vertical='center', indent=2)
        return row + 1

    def _add_input_row(self, ws, row, label, value, unit, note):
        """Add an input parameter row"""
        ws[f'A{row}'] = label
        ws[f'A{row}'].font = self.fonts['label']
        ws[f'A{row}'].alignment = Alignment(horizontal='left', vertical='center', indent=1)

        # Value cell (BLUE for input)
        ws[f'B{row}'] = value
        ws[f'B{row}'].font = self.fonts['input']
        ws[f'B{row}'].fill = PatternFill(start_color=self.colors['input'],
                                         end_color=self.colors['input'],
                                         fill_type='solid')
        ws[f'B{row}'].alignment = Alignment(horizontal='right', vertical='center')
        ws[f'B{row}'].border = self.border

        # Unit cell
        ws[f'C{row}'] = unit
        ws[f'C{row}'].font = Font(name='Calibri', size=9, italic=True)
        ws[f'C{row}'].alignment = Alignment(horizontal='left', vertical='center')

        # Note cell
        ws[f'D{row}'] = note
        ws[f'D{row}'].font = Font(name='Calibri', size=9, color='666666')
        ws[f'D{row}'].alignment = Alignment(horizontal='left', vertical='center')

        return row + 1

    def _add_calculated_row(self, ws, row, label, formula, unit, note):
        """Add a calculated parameter row (YELLOW)"""
        ws[f'A{row}'] = label
        ws[f'A{row}'].font = self.fonts['label']
        ws[f'A{row}'].alignment = Alignment(horizontal='left', vertical='center', indent=1)

        # Formula cell (YELLOW for calculated)
        ws[f'B{row}'] = formula
        ws[f'B{row}'].font = self.fonts['input']
        ws[f'B{row}'].fill = PatternFill(start_color=self.colors['calculated'],
                                         end_color=self.colors['calculated'],
                                         fill_type='solid')
        ws[f'B{row}'].alignment = Alignment(horizontal='right', vertical='center')
        ws[f'B{row}'].border = self.border

        # Unit cell
        ws[f'C{row}'] = unit
        ws[f'C{row}'].font = Font(name='Calibri', size=9, italic=True)
        ws[f'C{row}'].alignment = Alignment(horizontal='left', vertical='center')

        # Note cell
        ws[f'D{row}'] = note
        ws[f'D{row}'].font = Font(name='Calibri', size=9, color='666666')
        ws[f'D{row}'].alignment = Alignment(horizontal='left', vertical='center')

        return row + 1

    def build_model(self):
        """Main method to build the complete model"""
        print("=" * 70)
        print("SANTA FRESH FINANCIAL MODEL BUILDER")
        print("=" * 70)
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()

        print("[1/6] Building Assumptions sheet (Sections A-C)...")
        ws_assumptions, row = self.create_assumptions_sheet()

        # Continue building remaining sections D-U
        print("[2/6] Building Assumptions sheet (Sections D-U)...")
        # This will be added in the next iteration

        print()
        print("Model structure created. Saving...")

        # Save the workbook
        filename = "Santa_Fresh_Financial_Model_v4.0_WIP.xlsx"
        self.wb.save(filename)

        print(f"✓ Saved: {filename}")
        print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 70)

        return filename

if __name__ == "__main__":
    builder = SantaFreshModelBuilder()
    builder.build_model()
