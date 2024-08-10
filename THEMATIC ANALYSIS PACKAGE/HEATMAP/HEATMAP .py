import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Participant": ["P01", "P02", "P03", "P04", "P05", "P06", "P07", "P08", "P09", "P10", "P11", "P12", "P13", "P14"],
    "Digital Vulnerability and Exposure": [8, 5, 7, 9, 4, 6, 3, 7, 8, 2, 5, 6, 7, 4],
    "Impact on Professional Life": [3, 7, 6, 2, 8, 5, 6, 4, 5, 7, 9, 3, 6, 8],
    "Psychological and Emotional Effects": [9, 4, 6, 7, 5, 8, 9, 6, 3, 5, 4, 8, 7, 9],
    "Awareness and Prevention Measures": [2, 8, 5, 4, 7, 3, 6, 8, 5, 6, 7, 2, 8, 6]
}

df = pd.DataFrame(data)

df.set_index('Participant', inplace=True)

plt.figure(figsize=(12, 8))  # Adjusted for better fit of text
ax = sns.heatmap(df, annot=True, cmap='coolwarm', linewidths=.5, cbar_kws={'label': 'Theme Intensity'})

ax.set_xticklabels(ax.get_xticklabels(), rotation=40, horizontalalignment='right', wrap=True)


plt.title('Intensity of Themes Across the 14 Participants', fontsize=16, fontweight='bold')
plt.xlabel('Themes', fontsize=14, fontweight='bold')
plt.ylabel('Participants', fontsize=14, fontweight='bold')
plt.show()
