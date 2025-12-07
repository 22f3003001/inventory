"""
Retail Performance Analysis - Inventory Turnover Ratio
Author: 22f3003001@ds.study.iitm.ac.in
Generated with LLM assistance for data-driven strategic decision making
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Quarterly Inventory Turnover Data - 2024
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
turnover_ratios = [3.54, 2.51, 8.81, 7.56]
industry_target = 8.0

# Calculate average
average_turnover = np.mean(turnover_ratios)

print("=" * 60)
print("RETAIL PERFORMANCE ANALYSIS")
print("Inventory Turnover Ratio - 2024")
print("=" * 60)
print(f"\nQuarterly Data:")
for q, ratio in zip(quarters, turnover_ratios):
    status = "✓ Above Target" if ratio >= industry_target else "✗ Below Target"
    print(f"  {q}: {ratio:.2f} {status}")

print(f"\nAverage Turnover Ratio: {average_turnover:.2f}")
print(f"Industry Target: {industry_target}")
print(f"Gap to Target: {industry_target - average_turnover:.2f}")

# Calculate percentage of target achieved
target_percentage = (average_turnover / industry_target) * 100
print(f"Current Performance: {target_percentage:.1f}% of target")

# Create comprehensive visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Inventory Turnover Ratio Analysis - 2024\n22f3003001@ds.study.iitm.ac.in', 
             fontsize=16, fontweight='bold')

# 1. Bar chart with target line
ax1 = axes[0, 0]
bars = ax1.bar(quarters, turnover_ratios, color=['#e74c3c' if x < industry_target else '#27ae60' 
                                                   for x in turnover_ratios], 
               edgecolor='black', linewidth=2)
ax1.axhline(y=industry_target, color='#3498db', linestyle='--', linewidth=2, label='Industry Target (8.0)')
ax1.axhline(y=average_turnover, color='#e67e22', linestyle=':', linewidth=2, label=f'Average ({average_turnover:.2f})')
ax1.set_ylabel('Turnover Ratio', fontsize=12, fontweight='bold')
ax1.set_title('Quarterly Performance vs Target', fontsize=13, fontweight='bold')
ax1.legend()
ax1.grid(axis='y', alpha=0.3)
for i, (bar, val) in enumerate(zip(bars, turnover_ratios)):
    ax1.text(i, val + 0.3, f'{val:.2f}', ha='center', fontweight='bold')

# 2. Line chart showing trend
ax2 = axes[0, 1]
ax2.plot(quarters, turnover_ratios, marker='o', linewidth=3, markersize=10, 
         color='#9b59b6', label='Actual Performance')
ax2.axhline(y=industry_target, color='#3498db', linestyle='--', linewidth=2, label='Target')
ax2.fill_between(range(len(quarters)), turnover_ratios, industry_target, 
                  where=[x >= industry_target for x in turnover_ratios], 
                  alpha=0.3, color='green', label='Above Target')
ax2.fill_between(range(len(quarters)), turnover_ratios, industry_target, 
                  where=[x < industry_target for x in turnover_ratios], 
                  alpha=0.3, color='red', label='Below Target')
ax2.set_ylabel('Turnover Ratio', fontsize=12, fontweight='bold')
ax2.set_title('Trend Analysis', fontsize=13, fontweight='bold')
ax2.legend()
ax2.grid(True, alpha=0.3)

# 3. Gap analysis
ax3 = axes[1, 0]
gaps = [industry_target - x for x in turnover_ratios]
colors = ['#e74c3c' if g > 0 else '#27ae60' for g in gaps]
ax3.bar(quarters, gaps, color=colors, edgecolor='black', linewidth=2)
ax3.axhline(y=0, color='black', linewidth=1)
ax3.set_ylabel('Gap to Target', fontsize=12, fontweight='bold')
ax3.set_title('Performance Gap Analysis', fontsize=13, fontweight='bold')
ax3.grid(axis='y', alpha=0.3)
for i, gap in enumerate(gaps):
    ax3.text(i, gap + (0.2 if gap > 0 else -0.2), f'{abs(gap):.2f}', 
             ha='center', fontweight='bold')

# 4. Performance summary
ax4 = axes[1, 1]
ax4.axis('off')
summary_text = f"""
KEY INSIGHTS

Current Status:
  • Average Ratio: {average_turnover:.2f}
  • Target: {industry_target}
  • Performance: {target_percentage:.1f}% of target
  • Gap: {industry_target - average_turnover:.2f} points

Quarterly Performance:
  • Q1: {turnover_ratios[0]:.2f} (Below target)
  • Q2: {turnover_ratios[1]:.2f} (Lowest point)
  • Q3: {turnover_ratios[2]:.2f} (Best quarter)
  • Q4: {turnover_ratios[3]:.2f} (Strong finish)

Critical Observation:
  Q2 showed significant decline (2.51)
  but recovery began in Q3 (8.81)

Action Required:
  Focus on optimizing supply chain
  and demand forecasting to maintain
  Q3/Q4 performance levels
"""
ax4.text(0.1, 0.95, summary_text, fontsize=11, verticalalignment='top',
         fontfamily='monospace', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('inventory_turnover_analysis.png', dpi=300, bbox_inches='tight')
print(f"\n✓ Visualization saved as 'inventory_turnover_analysis.png'")
print("=" * 60)

plt.show()
