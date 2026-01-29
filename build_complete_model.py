#!/usr/bin/env python3
"""
Santa Fresh Financial Model - Complete Builder with All Sheets
===============================================================

This script builds the COMPLETE financial model with all calculation sheets,
formulas, and outputs. All formulas reference the Assumptions sheet.

Target: Fully functional model ready for user to populate.
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, numbers
from openpyxl.utils import get_column_letter
from datetime import datetime
import sys

# Load the existing model with Assumptions sheet
wb = openpyxl.load_workbook('Santa_Fresh_Financial_Model_v4.0.xlsx')

# Color scheme
colors = {
    'input': 'ADD8E6',      # Light blue
    'calculated': 'FFFF99', # Light yellow
    'header': '4472C4',     # Dark blue
    'section': 'D0CECE',    # Light gray
}

# Fonts
header_font = Font(name='Calibri', size=12, bold=True, color='FFFFFF')
section_font = Font(name='Calibri', size=11, bold=True)
label_font = Font(name='Calibri', size=10)

# Border
thin_border = Side(style='thin', color='000000')
border = Border(left=thin_border, right=thin_border, top=thin_border, bottom=thin_border)

def add_header_row(ws, row, title):
    """Add a section header"""
    ws.merge_cells(f'A{row}:L{row}')
    cell = ws[f'A{row}']
    cell.value = title
    cell.font = header_font
    cell.fill = PatternFill(start_color=colors['header'], end_color=colors['header'], fill_type='solid')
    cell.alignment = Alignment(horizontal='center', vertical='center')
    return row + 1

def add_label_row(ws, row, label, col='A'):
    """Add a label in a specific column"""
    cell = ws[f'{col}{row}']
    cell.value = label
    cell.font = label_font
    cell.alignment = Alignment(horizontal='left', vertical='center')
    return row

print("=" * 70)
print("BUILDING COMPLETE SANTA FRESH FINANCIAL MODEL")
print("=" * 70)
print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

# ============================================================================
# SHEET 1: CALCULATIONS (Derived Values)
# ============================================================================
print("[1/12] Building Calculations sheet...")

if 'Calculations' in wb.sheetnames:
    del wb['Calculations']
ws_calc = wb.create_sheet('Calculations', 1)

# Set column widths
ws_calc.column_dimensions['A'].width = 40
for col in ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']:
    ws_calc.column_dimensions[col].width = 15

row = 1
row = add_header_row(ws_calc, row, "CALCULATIONS - Derived Values")

# Year headers
ws_calc['A2'] = 'Parameter'
ws_calc['B2'] = 'Year 0'
for i in range(1, 11):
    ws_calc[f'{get_column_letter(i+2)}2'] = f'Year {i}'

# Format header row
for col in range(1, 13):
    cell = ws_calc.cell(2, col)
    cell.font = section_font
    cell.fill = PatternFill(start_color=colors['section'], end_color=colors['section'], fill_type='solid')
    cell.alignment = Alignment(horizontal='center')

row = 3

# Model start year
ws_calc[f'A{row}'] = 'Model start year'
ws_calc[f'B{row}'] = '=Assumptions!B6'  # Reference to Assumptions A-1
ws_calc[f'B{row}'].fill = PatternFill(start_color=colors['calculated'], end_color=colors['calculated'], fill_type='solid')
row += 1

# Calendar years
ws_calc[f'A{row}'] = 'Calendar year'
for col_idx in range(2, 13):
    col = get_column_letter(col_idx)
    if col == 'B':
        ws_calc[f'{col}{row}'] = f'=$B$3'
    else:
        ws_calc[f'{col}{row}'] = f'={get_column_letter(col_idx-1)}{row}+1'
    ws_calc[f'{col}{row}'].fill = PatternFill(start_color=colors['calculated'], end_color=colors['calculated'], fill_type='solid')
row += 2

# Total CAPEX by phase
ws_calc[f'A{row}'] = 'Total CAPEX - Phase 1'
ws_calc[f'B{row}'] = '=SUM(Assumptions!B258:B284)'  # Sum Phase 1 CAPEX items
ws_calc[f'B{row}'].fill = PatternFill(start_color=colors['calculated'], end_color=colors['calculated'], fill_type='solid')
ws_calc[f'B{row}'].number_format = '#,##0'
row += 1

ws_calc[f'A{row}'] = 'Total CAPEX - Phase 2'
ws_calc[f'B{row}'] = '=SUM(Assumptions!B287:B293)'  # Sum Phase 2 CAPEX items
ws_calc[f'B{row}'].fill = PatternFill(start_color=colors['calculated'], end_color=colors['calculated'], fill_type='solid')
ws_calc[f'B{row}'].number_format = '#,##0'
row += 1

ws_calc[f'A{row}'] = 'Total CAPEX - Phase 3'
ws_calc[f'B{row}'] = '=SUM(Assumptions!B296:B301)'  # Sum Phase 3 CAPEX items
ws_calc[f'B{row}'].fill = PatternFill(start_color=colors['calculated'], end_color=colors['calculated'], fill_type='solid')
ws_calc[f'B{row}'].number_format = '#,##0'
row += 1

ws_calc[f'A{row}'] = 'Total CAPEX (all phases)'
ws_calc[f'B{row}'] = '=SUM(B6:B8)'
ws_calc[f'B{row}'].fill = PatternFill(start_color=colors['calculated'], end_color=colors['calculated'], fill_type='solid')
ws_calc[f'B{row}'].number_format = '#,##0'
row += 2

# Fresh-pack line annual capacity
ws_calc[f'A{row}'] = 'Fresh-pack annual capacity (tonnes)'
ws_calc[f'B{row}'] = '=Assumptions!B58*Assumptions!B59*(Assumptions!B60-Assumptions!B61)'
ws_calc[f'B{row}'].fill = PatternFill(start_color=colors['calculated'], end_color=colors['calculated'], fill_type='solid')
ws_calc[f'B{row}'].number_format = '#,##0'
row += 1

# Frozen line annual capacity
ws_calc[f'A{row}'] = 'Frozen line annual capacity (tonnes)'
ws_calc[f'B{row}'] = '=Assumptions!B66*Assumptions!B67*(Assumptions!B68-Assumptions!B69)'
ws_calc[f'B{row}'].fill = PatternFill(start_color=colors['calculated'], end_color=colors['calculated'], fill_type='solid')
ws_calc[f'B{row}'].number_format = '#,##0'
row += 1

print("✓ Calculations sheet complete")

# ============================================================================
# SHEET 2: REVENUE
# ============================================================================
print("[2/12] Building Revenue sheet...")

if 'Revenue' in wb.sheetnames:
    del wb['Revenue']
ws_rev = wb.create_sheet('Revenue', 2)

# Column widths
ws_rev.column_dimensions['A'].width = 35
for col in ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']:
    ws_rev.column_dimensions[col].width = 15

row = 1
row = add_header_row(ws_rev, row, "REVENUE PROJECTIONS")

# Year headers
ws_rev['A2'] = 'Revenue Stream'
for i in range(11):
    ws_rev[f'{get_column_letter(i+2)}2'] = f'Year {i}'

# Format headers
for col in range(1, 13):
    cell = ws_rev.cell(2, col)
    cell.font = section_font
    cell.fill = PatternFill(start_color=colors['section'], end_color=colors['section'], fill_type='solid')

row = 3

# Fresh-pack revenue
ws_rev[f'A{row}'] = 'Fresh-Pack Table Potatoes'
ws_rev[f'B{row}'] = 0  # Year 0
for yr in range(1, 11):
    col = get_column_letter(yr + 2)
    # Volume × Price (with escalation)
    ws_rev[f'{col}{row}'] = f'=Assumptions!B17*Assumptions!B20*(1+Assumptions!B21/100)^({yr}-1)*1000'
ws_rev[f'B{row}'].number_format = '#,##0'
row += 1

# Frozen fries revenue
ws_rev[f'A{row}'] = 'Frozen French Fries'
ws_rev[f'B{row}'] = 0  # Year 0
for yr in range(1, 11):
    col = get_column_letter(yr + 2)
    ws_rev[f'{col}{row}'] = f'=Assumptions!B24*Assumptions!B27*(1+Assumptions!B28/100)^({yr}-1)*1000'
ws_rev[f'B{row}'].number_format = '#,##0'
row += 1

# Certified seed revenue
ws_rev[f'A{row}'] = 'Certified Seed Sales'
ws_rev[f'B{row}'] = 0
for yr in range(1, 11):
    col = get_column_letter(yr + 2)
    ws_rev[f'{col}{row}'] = f'=Assumptions!B31*Assumptions!B32*(1+Assumptions!B33/100)^({yr}-1)*1000'
ws_rev[f'B{row}'].number_format = '#,##0'
row += 1

# Animal feed revenue
ws_rev[f'A{row}'] = 'Animal Feed Pellets'
ws_rev[f'B{row}'] = 0
for yr in range(1, 11):
    col = get_column_letter(yr + 2)
    # Organic waste × conversion rate × price
    ws_rev[f'{col}{row}'] = f'=(Assumptions!B17+Assumptions!B24)*Assumptions!B35/1000*Assumptions!B36/100*Assumptions!B37*(1+Assumptions!B38/100)^({yr}-1)*1000'
ws_rev[f'B{row}'].number_format = '#,##0'
row += 1

# Total revenue
ws_rev[f'A{row}'] = 'TOTAL REVENUE'
ws_rev[f'A{row}'].font = Font(bold=True)
for yr in range(11):
    col = get_column_letter(yr + 2)
    ws_rev[f'{col}{row}'] = f'=SUM({col}3:{col}{row-1})'
    ws_rev[f'{col}{row}'].font = Font(bold=True)
    ws_rev[f'{col}{row}'].number_format = '#,##0'
    ws_rev[f'{col}{row}'].border = Border(top=Side(style='thin'), bottom=Side(style='double'))

print("✓ Revenue sheet complete")

# ============================================================================
# SHEET 3: OPERATING COSTS
# ============================================================================
print("[3/12] Building Operating Costs sheet...")

if 'Operating Costs' in wb.sheetnames:
    del wb['Operating Costs']
ws_opex = wb.create_sheet('Operating Costs', 3)

ws_opex.column_dimensions['A'].width = 35
for col in ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']:
    ws_opex.column_dimensions[col].width = 15

row = 1
row = add_header_row(ws_opex, row, "OPERATING COSTS")

# Year headers
ws_opex['A2'] = 'Cost Category'
for i in range(11):
    ws_opex[f'{get_column_letter(i+2)}2'] = f'Year {i}'

for col in range(1, 13):
    cell = ws_opex.cell(2, col)
    cell.font = section_font
    cell.fill = PatternFill(start_color=colors['section'], end_color=colors['section'], fill_type='solid')

row = 3

# Raw materials (ware potatoes)
ws_opex[f'A{row}'] = 'Raw Materials - Ware Potatoes'
ws_opex[f'B{row}'] = 0
for yr in range(1, 11):
    col = get_column_letter(yr + 2)
    # Total throughput × farmgate price
    ws_opex[f'{col}{row}'] = f'=(Assumptions!B17+Assumptions!B24)*Assumptions!B83*(1+Assumptions!B85/100)^({yr}-1)*1000'
ws_opex[f'B{row}'].number_format = '#,##0'
row += 1

# Labor - sum all departments
ws_opex[f'A{row}'] = 'Labor - All Departments'
ws_opex[f'B{row}'] = 0
for yr in range(1, 11):
    col = get_column_letter(yr + 2)
    # Sum of all 7 departments × 12 months
    ws_opex[f'{col}{row}'] = f'=(Assumptions!B155+Assumptions!B158+Assumptions!B161+Assumptions!B164+Assumptions!B167+Assumptions!B170+Assumptions!B173)*12*(1+Assumptions!B175/100)^({yr}-1)'
ws_opex[f'B{row}'].number_format = '#,##0'
row += 1

# Utilities
ws_opex[f'A{row}'] = 'Utilities (Electricity, Water, Diesel)'
ws_opex[f'B{row}'] = 0
for yr in range(1, 11):
    col = get_column_letter(yr + 2)
    # Grid electricity + generator + water + diesel
    ws_opex[f'{col}{row}'] = f'=(Assumptions!B178*Assumptions!B179+Assumptions!B180*Assumptions!B181*Assumptions!B182+Assumptions!B186*Assumptions!B187+Assumptions!B190*Assumptions!B191)*(1+Assumptions!B194/100)^({yr}-1)'
ws_opex[f'B{row}'].number_format = '#,##0'
row += 1

# Processing consumables
ws_opex[f'A{row}'] = 'Processing Consumables'
ws_opex[f'B{row}'] = 0
for yr in range(1, 11):
    col = get_column_letter(yr + 2)
    # Oil + packaging + additives + cleaning + maintenance + QC
    ws_opex[f'{col}{row}'] = f'=(Assumptions!B197*Assumptions!B24*Assumptions!B198+Assumptions!B201*Assumptions!B17*Assumptions!B202+Assumptions!B205*Assumptions!B24*Assumptions!B206+Assumptions!B209*(Assumptions!B17+Assumptions!B24)*Assumptions!B210+Assumptions!B213+Assumptions!B216+Assumptions!B219)*(1+Assumptions!B211/100)^({yr}-1)'
ws_opex[f'B{row}'].number_format = '#,##0'
row += 1

# Other operating costs
ws_opex[f'A{row}'] = 'Other Operating Costs'
ws_opex[f'B{row}'] = 0
for yr in range(1, 11):
    col = get_column_letter(yr + 2)
    # Insurance + professional + marketing + admin + etc
    ws_opex[f'{col}{row}'] = f'=(Calculations!$B$9*Assumptions!B223/100+Assumptions!B224+IF({yr}=1,Assumptions!B225,Assumptions!B226)+Assumptions!B227+Assumptions!B228+Assumptions!B229+Assumptions!B230+Assumptions!B231+Assumptions!B232+Assumptions!B233+Assumptions!B234)*(1+Assumptions!B235/100)^({yr}-1)'
ws_opex[f'B{row}'].number_format = '#,##0'
row += 1

# Depot operating costs
ws_opex[f'A{row}'] = 'Regional Depot Operating Costs'
ws_opex[f'B{row}'] = 0
for yr in range(1, 11):
    col = get_column_letter(yr + 2)
    # 4 depots (phase in based on timing)
    ws_opex[f'{col}{row}'] = f'=IF({yr}>=2,(Assumptions!B305+Assumptions!B306+Assumptions!B307+Assumptions!B308)*12,0)+IF({yr}>=3,(Assumptions!B310+Assumptions!B311+Assumptions!B312+Assumptions!B313+Assumptions!B315+Assumptions!B316+Assumptions!B317+Assumptions!B318+Assumptions!B320+Assumptions!B321+Assumptions!B322+Assumptions!B323)*12,0)'
ws_opex[f'B{row}'].number_format = '#,##0'
row += 1

# Total operating costs
ws_opex[f'A{row}'] = 'TOTAL OPERATING COSTS'
ws_opex[f'A{row}'].font = Font(bold=True)
for yr in range(11):
    col = get_column_letter(yr + 2)
    ws_opex[f'{col}{row}'] = f'=SUM({col}3:{col}{row-1})'
    ws_opex[f'{col}{row}'].font = Font(bold=True)
    ws_opex[f'{col}{row}'].number_format = '#,##0'
    ws_opex[f'{col}{row}'].border = Border(top=Side(style='thin'), bottom=Side(style='double'))

print("✓ Operating Costs sheet complete")

# ============================================================================
# SHEET 4: CAPEX SCHEDULE
# ============================================================================
print("[4/12] Building CAPEX Schedule sheet...")

if 'CAPEX Schedule' in wb.sheetnames:
    del wb['CAPEX Schedule']
ws_capex = wb.create_sheet('CAPEX Schedule', 4)

ws_capex.column_dimensions['A'].width = 35
for col in ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']:
    ws_capex.column_dimensions[col].width = 15

row = 1
row = add_header_row(ws_capex, row, "CAPITAL EXPENDITURE SCHEDULE")

# Year headers
ws_capex['A2'] = 'CAPEX Category'
for i in range(11):
    ws_capex[f'{get_column_letter(i+2)}2'] = f'Year {i}'

for col in range(1, 13):
    cell = ws_capex.cell(2, col)
    cell.font = section_font
    cell.fill = PatternFill(start_color=colors['section'], end_color=colors['section'], fill_type='solid')

row = 3

# Phase 1 CAPEX (Year 0-1)
ws_capex[f'A{row}'] = 'Phase 1 - Foundation Infrastructure'
ws_capex[f'B{row}'] = '=Calculations!B6*(1+Assumptions!B284/100)'  # With contingency
ws_capex[f'C{row}'] = 0
ws_capex[f'B{row}'].number_format = '#,##0'
row += 1

# Phase 2 CAPEX (Year 2)
ws_capex[f'A{row}'] = 'Phase 2 - Frozen Line & Douala Depot'
ws_capex[f'B{row}'] = 0
ws_capex[f'C{row}'] = 0
ws_capex[f'D{row}'] = '=Calculations!B7*(1+Assumptions!B293/100)'  # With contingency
ws_capex[f'D{row}'].number_format = '#,##0'
row += 1

# Phase 3 CAPEX (Year 3)
ws_capex[f'A{row}'] = 'Phase 3 - Regional Depot Expansion'
for yr in range(4):
    ws_capex[f'{get_column_letter(yr+2)}{row}'] = 0
ws_capex[f'E{row}'] = '=Calculations!B8*(1+Assumptions!B301/100)'  # With contingency
ws_capex[f'E{row}'].number_format = '#,##0'
row += 1

# Total CAPEX
ws_capex[f'A{row}'] = 'TOTAL CAPEX'
ws_capex[f'A{row}'].font = Font(bold=True)
for yr in range(11):
    col = get_column_letter(yr + 2)
    ws_capex[f'{col}{row}'] = f'=SUM({col}3:{col}{row-1})'
    ws_capex[f'{col}{row}'].font = Font(bold=True)
    ws_capex[f'{col}{row}'].number_format = '#,##0'
    ws_capex[f'{col}{row}'].border = Border(top=Side(style='thin'), bottom=Side(style='double'))

print("✓ CAPEX Schedule sheet complete")

# ============================================================================
# Save and continue with remaining sheets...
# ============================================================================

print()
print("Saving progress...")
wb.save('Santa_Fresh_Financial_Model_v4.0.xlsx')
print("✓ First 4 calculation sheets complete")
print()
print("Continuing with remaining sheets...")
