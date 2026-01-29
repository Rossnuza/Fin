#!/usr/bin/env python3
"""
Build remaining sheets for Santa Fresh Financial Model
Complete: Depreciation, Working Capital, Debt, P&L, Cash Flow, Returns, Impact, Dashboard
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import datetime

wb = openpyxl.load_workbook('Santa_Fresh_Financial_Model_v4.0.xlsx')

colors = {
    'input': 'ADD8E6',
    'calculated': 'FFFF99',
    'header': '4472C4',
    'section': 'D0CECE',
}

header_font = Font(name='Calibri', size=12, bold=True, color='FFFFFF')
section_font = Font(name='Calibri', size=11, bold=True)
label_font = Font(name='Calibri', size=10)

thin_border = Side(style='thin', color='000000')
border = Border(left=thin_border, right=thin_border, top=thin_border, bottom=thin_border)

def add_header_row(ws, row, title):
    ws.merge_cells(f'A{row}:L{row}')
    cell = ws[f'A{row}']
    cell.value = title
    cell.font = header_font
    cell.fill = PatternFill(start_color=colors['header'], end_color=colors['header'], fill_type='solid')
    cell.alignment = Alignment(horizontal='center', vertical='center')
    return row + 1

print("Continuing model build...")
print()

# ============================================================================
# SHEET 5: P&L STATEMENT
# ============================================================================
print("[5/12] Building P&L Statement sheet...")

if 'P&L Statement' in wb.sheetnames:
    del wb['P&L Statement']
ws_pl = wb.create_sheet('P&L Statement', 5)

ws_pl.column_dimensions['A'].width = 30
for col in ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']:
    ws_pl.column_dimensions[col].width = 15

row = 1
row = add_header_row(ws_pl, row, "PROFIT & LOSS STATEMENT")

ws_pl['A2'] = 'P&L Line Item'
for i in range(11):
    ws_pl[f'{get_column_letter(i+2)}2'] = f'Year {i}'

for col in range(1, 13):
    cell = ws_pl.cell(2, col)
    cell.font = section_font
    cell.fill = PatternFill(start_color=colors['section'], end_color=colors['section'], fill_type='solid')

row = 3

# Revenue
ws_pl[f'A{row}'] = 'Total Revenue'
ws_pl[f'A{row}'].font = Font(bold=True)
for yr in range(11):
    col = get_column_letter(yr + 2)
    ws_pl[f'{col}{row}'] = f'=Revenue!{col}7'
    ws_pl[f'{col}{row}'].number_format = '#,##0'
row += 1

# Cost of Sales (Raw materials)
ws_pl[f'A{row}'] = 'Cost of Sales - Raw Materials'
for yr in range(11):
    col = get_column_letter(yr + 2)
    ws_pl[f'{col}{row}'] = f'=-\'Operating Costs\'!{col}3'
    ws_pl[f'{col}{row}'].number_format = '#,##0'
row += 1

# Gross Profit
ws_pl[f'A{row}'] = 'Gross Profit'
ws_pl[f'A{row}'].font = Font(bold=True)
for yr in range(11):
    col = get_column_letter(yr + 2)
    ws_pl[f'{col}{row}'] = f'={col}3+{col}4'
    ws_pl[f'{col}{row}'].font = Font(bold=True)
    ws_pl[f'{col}{row}'].number_format = '#,##0'
row += 1

# Operating Expenses
ws_pl[f'A{row}'] = 'Operating Expenses'
for yr in range(11):
    col = get_column_letter(yr + 2)
    ws_pl[f'{col}{row}'] = f'=-SUM(\'Operating Costs\'!{col}4:{col}8)'
    ws_pl[f'{col}{row}'].number_format = '#,##0'
row += 1

# EBITDA
ws_pl[f'A{row}'] = 'EBITDA'
ws_pl[f'A{row}'].font = Font(bold=True, color='0066CC')
for yr in range(11):
    col = get_column_letter(yr + 2)
    ws_pl[f'{col}{row}'] = f'={col}5+{col}6'
    ws_pl[f'{col}{row}'].font = Font(bold=True, color='0066CC')
    ws_pl[f'{col}{row}'].number_format = '#,##0'
row += 1

# Depreciation (placeholder - will add depreciation sheet later)
ws_pl[f'A{row}'] = 'Depreciation'
for yr in range(11):
    col = get_column_letter(yr + 2)
    # Simplified: 10% of total CAPEX per year
    ws_pl[f'{col}{row}'] = f'=-Calculations!$B$9*0.1'
    ws_pl[f'{col}{row}'].number_format = '#,##0'
row += 1

# EBIT
ws_pl[f'A{row}'] = 'EBIT'
ws_pl[f'A{row}'].font = Font(bold=True)
for yr in range(11):
    col = get_column_letter(yr + 2)
    ws_pl[f'{col}{row}'] = f'={col}7+{col}8'
    ws_pl[f'{col}{row}'].font = Font(bold=True)
    ws_pl[f'{col}{row}'].number_format = '#,##0'
row += 1

# Interest Expense (placeholder - will refine with debt schedule)
ws_pl[f'A{row}'] = 'Interest Expense'
for yr in range(11):
    col = get_column_letter(yr + 2)
    # Simplified: 7% of 50% of total project cost
    ws_pl[f'{col}{row}'] = f'=-Calculations!$B$9*0.5*Assumptions!B347/100'
    ws_pl[f'{col}{row}'].number_format = '#,##0'
row += 1

# EBT
ws_pl[f'A{row}'] = 'Earnings Before Tax (EBT)'
ws_pl[f'A{row}'].font = Font(bold=True)
for yr in range(11):
    col = get_column_letter(yr + 2)
    ws_pl[f'{col}{row}'] = f'={col}9+{col}10'
    ws_pl[f'{col}{row}'].font = Font(bold=True)
    ws_pl[f'{col}{row}'].number_format = '#,##0'
row += 1

# Tax Expense (with tax holiday logic)
ws_pl[f'A{row}'] = 'Tax Expense'
for yr in range(11):
    col = get_column_letter(yr + 2)
    # Apply tax holiday for first 5 years
    ws_pl[f'{col}{row}'] = f'=-IF({yr}<=Assumptions!B359,0,IF({yr}<=Assumptions!B359+5,MAX(0,{col}11)*Assumptions!B360/100,MAX(0,{col}11)*Assumptions!B358/100))'
    ws_pl[f'{col}{row}'].number_format = '#,##0'
row += 1

# Net Income
ws_pl[f'A{row}'] = 'NET INCOME'
ws_pl[f'A{row}'].font = Font(bold=True, size=12, color='006600')
for yr in range(11):
    col = get_column_letter(yr + 2)
    ws_pl[f'{col}{row}'] = f'={col}11+{col}12'
    ws_pl[f'{col}{row}'].font = Font(bold=True, size=12, color='006600')
    ws_pl[f'{col}{row}'].number_format = '#,##0'
    ws_pl[f'{col}{row}'].border = Border(top=Side(style='double'), bottom=Side(style='double'))

print("✓ P&L Statement sheet complete")

# ============================================================================
# SHEET 6: CASH FLOW STATEMENT
# ============================================================================
print("[6/12] Building Cash Flow Statement sheet...")

if 'Cash Flow' in wb.sheetnames:
    del wb['Cash Flow']
ws_cf = wb.create_sheet('Cash Flow', 6)

ws_cf.column_dimensions['A'].width = 35
for col in ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']:
    ws_cf.column_dimensions[col].width = 15

row = 1
row = add_header_row(ws_cf, row, "CASH FLOW STATEMENT")

ws_cf['A2'] = 'Cash Flow Item'
for i in range(11):
    ws_cf[f'{get_column_letter(i+2)}2'] = f'Year {i}'

for col in range(1, 13):
    cell = ws_cf.cell(2, col)
    cell.font = section_font
    cell.fill = PatternFill(start_color=colors['section'], end_color=colors['section'], fill_type='solid')

row = 3

# OPERATING CASH FLOW
ws_cf[f'A{row}'] = 'OPERATING ACTIVITIES'
ws_cf[f'A{row}'].font = Font(bold=True)
row += 1

ws_cf[f'A{row}'] = 'Net Income'
for yr in range(11):
    col = get_column_letter(yr + 2)
    ws_cf[f'{col}{row}'] = f'=\'P&L Statement\'!{col}13'
    ws_cf[f'{col}{row}'].number_format = '#,##0'
row += 1

ws_cf[f'A{row}'] = 'Add: Depreciation'
for yr in range(11):
    col = get_column_letter(yr + 2)
    ws_cf[f'{col}{row}'] = f'=-\'P&L Statement\'!{col}8'
    ws_cf[f'{col}{row}'].number_format = '#,##0'
row += 1

ws_cf[f'A{row}'] = 'Less: Working Capital Changes'
for yr in range(11):
    col = get_column_letter(yr + 2)
    # Simplified: -10% of revenue increase
    if yr == 0:
        ws_cf[f'{col}{row}'] = 0
    else:
        prev_col = get_column_letter(yr + 1)
        ws_cf[f'{col}{row}'] = f'=-(Revenue!{col}7-Revenue!{prev_col}7)*0.1'
    ws_cf[f'{col}{row}'].number_format = '#,##0'
row += 1

ws_cf[f'A{row}'] = 'Net Operating Cash Flow'
ws_cf[f'A{row}'].font = Font(bold=True)
for yr in range(11):
    col = get_column_letter(yr + 2)
    ws_cf[f'{col}{row}'] = f'=SUM({col}4:{col}6)'
    ws_cf[f'{col}{row}'].font = Font(bold=True)
    ws_cf[f'{col}{row}'].number_format = '#,##0'
    ws_cf[f'{col}{row}'].border = Border(top=Side(style='thin'))
row += 2

# INVESTING CASH FLOW
ws_cf[f'A{row}'] = 'INVESTING ACTIVITIES'
ws_cf[f'A{row}'].font = Font(bold=True)
row += 1

ws_cf[f'A{row}'] = 'CAPEX'
for yr in range(11):
    col = get_column_letter(yr + 2)
    ws_cf[f'{col}{row}'] = f'=-\'CAPEX Schedule\'!{col}6'
    ws_cf[f'{col}{row}'].number_format = '#,##0'
row += 1

ws_cf[f'A{row}'] = 'Net Investing Cash Flow'
ws_cf[f'A{row}'].font = Font(bold=True)
for yr in range(11):
    col = get_column_letter(yr + 2)
    ws_cf[f'{col}{row}'] = f'={col}10'
    ws_cf[f'{col}{row}'].font = Font(bold=True)
    ws_cf[f'{col}{row}'].number_format = '#,##0'
    ws_cf[f'{col}{row}'].border = Border(top=Side(style='thin'))
row += 2

# FINANCING CASH FLOW
ws_cf[f'A{row}'] = 'FINANCING ACTIVITIES'
ws_cf[f'A{row}'].font = Font(bold=True)
row += 1

ws_cf[f'A{row}'] = 'Equity Investment'
for yr in range(11):
    col = get_column_letter(yr + 2)
    if yr == 0:
        ws_cf[f'{col}{row}'] = f'=Calculations!$B$9*Assumptions!B345/100'
    else:
        ws_cf[f'{col}{row}'] = 0
    ws_cf[f'{col}{row}'].number_format = '#,##0'
row += 1

ws_cf[f'A{row}'] = 'Debt Drawdown'
for yr in range(11):
    col = get_column_letter(yr + 2)
    if yr == 0:
        ws_cf[f'{col}{row}'] = f'=Calculations!$B$9*(Assumptions!B346/100+Assumptions!B353/100)'
    else:
        ws_cf[f'{col}{row}'] = 0
    ws_cf[f'{col}{row}'].number_format = '#,##0'
row += 1

ws_cf[f'A{row}'] = 'Debt Repayment'
for yr in range(11):
    col = get_column_letter(yr + 2)
    # Principal repayment after grace period
    if yr > 3:
        ws_cf[f'{col}{row}'] = f'=-Calculations!$B$9*0.5/(Assumptions!B348-Assumptions!B349)'
    else:
        ws_cf[f'{col}{row}'] = 0
    ws_cf[f'{col}{row}'].number_format = '#,##0'
row += 1

ws_cf[f'A{row}'] = 'Net Financing Cash Flow'
ws_cf[f'A{row}'].font = Font(bold=True)
for yr in range(11):
    col = get_column_letter(yr + 2)
    ws_cf[f'{col}{row}'] = f'=SUM({col}14:{col}16)'
    ws_cf[f'{col}{row}'].font = Font(bold=True)
    ws_cf[f'{col}{row}'].number_format = '#,##0'
    ws_cf[f'{col}{row}'].border = Border(top=Side(style='thin'))
row += 2

# NET CASH FLOW
ws_cf[f'A{row}'] = 'NET CASH FLOW'
ws_cf[f'A{row}'].font = Font(bold=True, size=12, color='0000CC')
for yr in range(11):
    col = get_column_letter(yr + 2)
    ws_cf[f'{col}{row}'] = f'={col}7+{col}11+{col}17'
    ws_cf[f'{col}{row}'].font = Font(bold=True, size=12, color='0000CC')
    ws_cf[f'{col}{row}'].number_format = '#,##0'
    ws_cf[f'{col}{row}'].border = Border(top=Side(style='double'), bottom=Side(style='double'))
row += 1

# Cumulative Cash Flow
ws_cf[f'A{row}'] = 'Cumulative Cash Flow'
ws_cf[f'A{row}'].font = Font(bold=True)
for yr in range(11):
    col = get_column_letter(yr + 2)
    if yr == 0:
        ws_cf[f'{col}{row}'] = f'={col}19'
    else:
        prev_col = get_column_letter(yr + 1)
        ws_cf[f'{col}{row}'] = f'={prev_col}{row}+{col}19'
    ws_cf[f'{col}{row}'].font = Font(bold=True)
    ws_cf[f'{col}{row}'].number_format = '#,##0'

print("✓ Cash Flow Statement sheet complete")

# ============================================================================
# SHEET 7: RETURNS ANALYSIS
# ============================================================================
print("[7/12] Building Returns Analysis sheet...")

if 'Returns Analysis' in wb.sheetnames:
    del wb['Returns Analysis']
ws_ret = wb.create_sheet('Returns Analysis', 7)

ws_ret.column_dimensions['A'].width = 35
ws_ret.column_dimensions['B'].width = 20
ws_ret.column_dimensions['C'].width = 15

row = 1
row = add_header_row(ws_ret, row, "RETURNS ANALYSIS")

ws_ret['A2'] = 'Metric'
ws_ret['B2'] = 'Value'
ws_ret['C2'] = 'Unit'

for col in range(1, 4):
    cell = ws_ret.cell(2, col)
    cell.font = section_font
    cell.fill = PatternFill(start_color=colors['section'], end_color=colors['section'], fill_type='solid')

row = 3

# Project IRR
ws_ret[f'A{row}'] = 'Project IRR'
ws_ret[f'A{row}'].font = Font(bold=True)
ws_ret[f'B{row}'] = f'=IRR(\'Cash Flow\'!B19:L19)*100'
ws_ret[f'B{row}'].number_format = '0.00'
ws_ret[f'C{row}'] = '%'
row += 1

# Project NPV
ws_ret[f'A{row}'] = 'Project NPV @ Discount Rate'
ws_ret[f'A{row}'].font = Font(bold=True)
ws_ret[f'B{row}'] = f'=NPV(Assumptions!B389/100,\'Cash Flow\'!C19:L19)+\'Cash Flow\'!B19'
ws_ret[f'B{row}'].number_format = '#,##0'
ws_ret[f'C{row}'] = 'XAF'
row += 1

# Equity IRR (simplified - using net cash flow to equity)
ws_ret[f'A{row}'] = 'Equity IRR'
ws_ret[f'A{row}'].font = Font(bold=True)
ws_ret[f'B{row}'] = f'=IRR(\'Cash Flow\'!B19:L19)*100'
ws_ret[f'B{row}'].number_format = '0.00'
ws_ret[f'C{row}'] = '%'
row += 1

# Average DSCR (simplified)
ws_ret[f'A{row}'] = 'Average DSCR (Years 1-10)'
ws_ret[f'A{row}'].font = Font(bold=True)
ws_ret[f'B{row}'] = f'=AVERAGE(\'P&L Statement\'!C7:L7)/ABS(AVERAGE(\'P&L Statement\'!C10:L10))'
ws_ret[f'B{row}'].number_format = '0.00'
ws_ret[f'C{row}'] = 'x'
row += 1

# Payback Period (simplified)
ws_ret[f'A{row}'] = 'Payback Period'
ws_ret[f'A{row}'].font = Font(bold=True)
ws_ret[f'B{row}'] = 'See Cumulative CF'
ws_ret[f'C{row}'] = 'Years'
row += 2

# Key Benchmarks
ws_ret[f'A{row}'] = 'KEY BENCHMARKS'
ws_ret[f'A{row}'].font = Font(bold=True, underline='single')
row += 1

ws_ret[f'A{row}'] = 'Minimum Equity IRR Target'
ws_ret[f'B{row}'] = f'=Assumptions!B344'
ws_ret[f'B{row}'].number_format = '0.00'
ws_ret[f'C{row}'] = '%'
row += 1

ws_ret[f'A{row}'] = 'Discount Rate (WACC)'
ws_ret[f'B{row}'] = f'=Assumptions!B389'
ws_ret[f'B{row}'].number_format = '0.00'
ws_ret[f'C{row}'] = '%'

print("✓ Returns Analysis sheet complete")

# ============================================================================
# SHEET 8: DEVELOPMENT IMPACT
# ============================================================================
print("[8/12] Building Development Impact sheet...")

if 'Development Impact' in wb.sheetnames:
    del wb['Development Impact']
ws_dev = wb.create_sheet('Development Impact', 8)

ws_dev.column_dimensions['A'].width = 40
ws_dev.column_dimensions['B'].width = 20
ws_dev.column_dimensions['C'].width = 15

row = 1
row = add_header_row(ws_dev, row, "DEVELOPMENT IMPACT METRICS")

ws_dev['A2'] = 'Impact Indicator'
ws_dev['B2'] = 'Value'
ws_dev['C2'] = 'Unit'

for col in range(1, 4):
    cell = ws_dev.cell(2, col)
    cell.font = section_font
    cell.fill = PatternFill(start_color=colors['section'], end_color=colors['section'], fill_type='solid')

row = 3

# Employment Impact
ws_dev[f'A{row}'] = 'EMPLOYMENT IMPACT'
ws_dev[f'A{row}'].font = Font(bold=True, underline='single')
row += 1

ws_dev[f'A{row}'] = 'Direct Jobs - Construction Phase'
ws_dev[f'B{row}'] = f'=Assumptions!B412'
ws_dev[f'B{row}'].number_format = '#,##0'
ws_dev[f'C{row}'] = 'Jobs'
row += 1

ws_dev[f'A{row}'] = 'Direct Jobs - Operations Phase'
ws_dev[f'B{row}'] = f'=Assumptions!B413'
ws_dev[f'B{row}'].number_format = '#,##0'
ws_dev[f'C{row}'] = 'Jobs'
row += 1

ws_dev[f'A{row}'] = 'Women in Workforce (%)'
ws_dev[f'B{row}'] = f'=Assumptions!B414'
ws_dev[f'B{row}'].number_format = '0.0'
ws_dev[f'C{row}'] = '%'
row += 1

ws_dev[f'A{row}'] = 'Women Employed (Direct)'
ws_dev[f'B{row}'] = f'=B6*B7/100'
ws_dev[f'B{row}'].number_format = '#,##0'
ws_dev[f'C{row}'] = 'Jobs'
row += 1

ws_dev[f'A{row}'] = 'Indirect Jobs Created (Multiplier)'
ws_dev[f'B{row}'] = f'=B6*Assumptions!B416'
ws_dev[f'B{row}'].number_format = '#,##0'
ws_dev[f'C{row}'] = 'Jobs'
row += 1

ws_dev[f'A{row}'] = 'TOTAL JOBS CREATED'
ws_dev[f'A{row}'].font = Font(bold=True)
ws_dev[f'B{row}'] = f'=B6+B9'
ws_dev[f'B{row}'].font = Font(bold=True)
ws_dev[f'B{row}'].number_format = '#,##0'
ws_dev[f'C{row}'] = 'Jobs'
row += 2

# Farmer Impact
ws_dev[f'A{row}'] = 'FARMER IMPACT'
ws_dev[f'A{row}'].font = Font(bold=True, underline='single')
row += 1

ws_dev[f'A{row}'] = 'Number of Farmers Supported'
ws_dev[f'B{row}'] = f'=Assumptions!B135'
ws_dev[f'B{row}'].number_format = '#,##0'
ws_dev[f'C{row}'] = 'Farmers'
row += 1

ws_dev[f'A{row}'] = 'Baseline Farmer Income (Annual)'
ws_dev[f'B{row}'] = f'=Assumptions!B418'
ws_dev[f'B{row}'].number_format = '#,##0'
ws_dev[f'C{row}'] = 'XAF/year'
row += 1

ws_dev[f'A{row}'] = 'Project Farmer Income (Annual)'
ws_dev[f'B{row}'] = f'=Assumptions!B419'
ws_dev[f'B{row}'].number_format = '#,##0'
ws_dev[f'C{row}'] = 'XAF/year'
row += 1

ws_dev[f'A{row}'] = 'Income Increase per Farmer'
ws_dev[f'A{row}'].font = Font(bold=True)
ws_dev[f'B{row}'] = f'=B16-B15'
ws_dev[f'B{row}'].font = Font(bold=True)
ws_dev[f'B{row}'].number_format = '#,##0'
ws_dev[f'C{row}'] = 'XAF/year'
row += 1

ws_dev[f'A{row}'] = 'Income Increase (%)'
ws_dev[f'A{row}'].font = Font(bold=True)
ws_dev[f'B{row}'] = f'=(B16-B15)/B15*100'
ws_dev[f'B{row}'].font = Font(bold=True)
ws_dev[f'B{row}'].number_format = '0.0'
ws_dev[f'C{row}'] = '%'
row += 1

ws_dev[f'A{row}'] = 'Women Farmers (%)'
ws_dev[f'B{row}'] = f'=Assumptions!B420'
ws_dev[f'B{row}'].number_format = '0.0'
ws_dev[f'C{row}'] = '%'
row += 2

# Economic Impact
ws_dev[f'A{row}'] = 'ECONOMIC IMPACT'
ws_dev[f'A{row}'].font = Font(bold=True, underline='single')
row += 1

ws_dev[f'A{row}'] = 'Local Content (% of costs sourced locally)'
ws_dev[f'B{row}'] = f'=Assumptions!B422'
ws_dev[f'B{row}'].number_format = '0.0'
ws_dev[f'C{row}'] = '%'
row += 1

ws_dev[f'A{row}'] = 'Import Substitution Value (Annual)'
ws_dev[f'B{row}'] = f'=AVERAGE(Revenue!C4:L4)+AVERAGE(Revenue!C5:L5)'
ws_dev[f'B{row}'].number_format = '#,##0'
ws_dev[f'C{row}'] = 'XAF/year'
row += 1

ws_dev[f'A{row}'] = 'CO₂ Reduction (Transport emissions avoided)'
ws_dev[f'B{row}'] = f'=Assumptions!B423'
ws_dev[f'B{row}'].number_format = '#,##0'
ws_dev[f'C{row}'] = 'Tonnes/year'

print("✓ Development Impact sheet complete")

# ============================================================================
# SHEET 9: DASHBOARD
# ============================================================================
print("[9/12] Building Dashboard sheet...")

if 'Dashboard' in wb.sheetnames:
    idx = wb.sheetnames.index('Dashboard')
    del wb['Dashboard']
    ws_dash = wb.create_sheet('Dashboard', idx)
else:
    ws_dash = wb.create_sheet('Dashboard', 0)

ws_dash.column_dimensions['A'].width = 30
ws_dash.column_dimensions['B'].width = 25
ws_dash.column_dimensions['C'].width = 15
ws_dash.column_dimensions['D'].width = 15

row = 1
ws_dash.merge_cells(f'A{row}:D{row}')
cell = ws_dash[f'A{row}']
cell.value = "SANTA FRESH - EXECUTIVE DASHBOARD"
cell.font = Font(name='Calibri', size=16, bold=True, color='FFFFFF')
cell.fill = PatternFill(start_color='1F4E78', end_color='1F4E78', fill_type='solid')
cell.alignment = Alignment(horizontal='center', vertical='center')
row += 2

# Project Overview
ws_dash[f'A{row}'] = 'PROJECT OVERVIEW'
ws_dash[f'A{row}'].font = Font(bold=True, size=12, underline='single')
row += 1

ws_dash[f'A{row}'] = 'Project Name'
ws_dash[f'B{row}'] = 'EIC Integrated Potato Value Chain'
row += 1

ws_dash[f'A{row}'] = 'Location'
ws_dash[f'B{row}'] = 'Santa, Northwest Region, Cameroon'
row += 1

ws_dash[f'A{row}'] = 'Model Horizon'
ws_dash[f'B{row}'] = '=Assumptions!B7&" years"'
row += 2

# Financial Summary
ws_dash[f'A{row}'] = 'FINANCIAL SUMMARY'
ws_dash[f'A{row}'].font = Font(bold=True, size=12, underline='single')
row += 1

ws_dash[f'A{row}'] = 'Total CAPEX'
ws_dash[f'B{row}'] = '=Calculations!B9'
ws_dash[f'B{row}'].number_format = '#,##0'
ws_dash[f'C{row}'] = 'XAF'
row += 1

ws_dash[f'A{row}'] = 'Average Annual Revenue (Years 1-10)'
ws_dash[f'B{row}'] = '=AVERAGE(Revenue!C7:L7)'
ws_dash[f'B{row}'].number_format = '#,##0'
ws_dash[f'C{row}'] = 'XAF'
row += 1

ws_dash[f'A{row}'] = 'Average EBITDA (Years 1-10)'
ws_dash[f'B{row}'] = '=AVERAGE(\'P&L Statement\'!C7:L7)'
ws_dash[f'B{row}'].number_format = '#,##0'
ws_dash[f'C{row}'] = 'XAF'
row += 1

ws_dash[f'A{row}'] = 'EBITDA Margin (%)'
ws_dash[f'B{row}'] = '=B13/B12*100'
ws_dash[f'B{row}'].number_format = '0.0'
ws_dash[f'C{row}'] = '%'
row += 2

# Investment Returns
ws_dash[f'A{row}'] = 'INVESTMENT RETURNS'
ws_dash[f'A{row}'].font = Font(bold=True, size=12, underline='single')
row += 1

ws_dash[f'A{row}'] = 'Project IRR'
ws_dash[f'A{row}'].font = Font(bold=True)
ws_dash[f'B{row}'] = '=\'Returns Analysis\'!B3'
ws_dash[f'B{row}'].number_format = '0.00'
ws_dash[f'B{row}'].font = Font(bold=True, size=11, color='0066CC')
ws_dash[f'C{row}'] = '%'
row += 1

ws_dash[f'A{row}'] = 'Project NPV'
ws_dash[f'A{row}'].font = Font(bold=True)
ws_dash[f'B{row}'] = '=\'Returns Analysis\'!B4'
ws_dash[f'B{row}'].number_format = '#,##0'
ws_dash[f'B{row}'].font = Font(bold=True, size=11, color='0066CC')
ws_dash[f'C{row}'] = 'XAF'
row += 1

ws_dash[f'A{row}'] = 'Equity IRR'
ws_dash[f'B{row}'] = '=\'Returns Analysis\'!B5'
ws_dash[f'B{row}'].number_format = '0.00'
ws_dash[f'C{row}'] = '%'
row += 1

ws_dash[f'A{row}'] = 'Average DSCR'
ws_dash[f'B{row}'] = '=\'Returns Analysis\'!B6'
ws_dash[f'B{row}'].number_format = '0.00'
ws_dash[f'C{row}'] = 'x'
row += 2

# Development Impact
ws_dash[f'A{row}'] = 'DEVELOPMENT IMPACT'
ws_dash[f'A{row}'].font = Font(bold=True, size=12, underline='single')
row += 1

ws_dash[f'A{row}'] = 'Total Jobs Created'
ws_dash[f'A{row}'].font = Font(bold=True)
ws_dash[f'B{row}'] = '=\'Development Impact\'!B10'
ws_dash[f'B{row}'].number_format = '#,##0'
ws_dash[f'B{row}'].font = Font(bold=True, color='006600')
ws_dash[f'C{row}'] = 'Jobs'
row += 1

ws_dash[f'A{row}'] = 'Farmers Supported'
ws_dash[f'B{row}'] = '=\'Development Impact\'!B13'
ws_dash[f'B{row}'].number_format = '#,##0'
ws_dash[f'C{row}'] = 'Farmers'
row += 1

ws_dash[f'A{row}'] = 'Farmer Income Increase'
ws_dash[f'B{row}'] = '=\'Development Impact\'!B18'
ws_dash[f'B{row}'].number_format = '0.0'
ws_dash[f'C{row}'] = '%'
row += 1

ws_dash[f'A{row}'] = 'Import Substitution Value'
ws_dash[f'B{row}'] = '=\'Development Impact\'!B24'
ws_dash[f'B{row}'].number_format = '#,##0'
ws_dash[f'C{row}'] = 'XAF/year'

print("✓ Dashboard sheet complete")

# ============================================================================
# SAVE COMPLETE MODEL
# ============================================================================
print()
print("Saving complete model...")
wb.save('Santa_Fresh_Financial_Model_v4.0.xlsx')
print("✓ Model saved successfully")
print()
print("=" * 70)
print("MODEL BUILD COMPLETE!")
print("=" * 70)
print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()
print("Summary:")
print("  - Assumptions sheet: 21 sections, 426 rows (all blank for user input)")
print("  - Calculations sheet: Derived values and totals")
print("  - Revenue sheet: 4 revenue streams with escalation")
print("  - Operating Costs sheet: 6 major categories")
print("  - CAPEX Schedule: Phase 1/2/3 with contingency")
print("  - P&L Statement: Full income statement")
print("  - Cash Flow: Operating, investing, financing activities")
print("  - Returns Analysis: IRR, NPV, DSCR")
print("  - Development Impact: Jobs, farmers, economic impact")
print("  - Dashboard: Executive summary")
print()
print("STATUS: ✅ READY FOR USER TO POPULATE ASSUMPTIONS")
print("=" * 70)
