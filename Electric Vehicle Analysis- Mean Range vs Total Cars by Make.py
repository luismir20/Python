import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

file_path = '/Users/fernando/Desktop/Code/Sources/Electric_Vehicle_Population_Data.csv'
data = pd.read_csv(file_path)

data_filtered = data[data['Electric Range'] != 0]

counted_data = (
    data_filtered
    .groupby(['Model Year','Make', 'Model'])
    .size()
    .reset_index(name='TotalCars')
    .sort_values('TotalCars', ascending=False) 
    .reset_index(drop=True)  
)

# I assign the rank column and start it from 1 up to length of data set
counted_data['Rank'] = range(1, len(counted_data) + 1)
rank_col = counted_data.pop('Rank')
counted_data.insert(0, 'Rank', rank_col)

# Creating the range with stats view
range_stats = (
    data_filtered.groupby(['Make','Model'])
    ['Electric Range']
    .describe()
    .loc[:, ['mean', 'max', 'min', 'std']]
    .sort_values('mean', ascending=False)
)

formatted_range_stats = range_stats.head(10).reset_index()

# Formatting the 'mean', 'max', 'min', and 'std' columns as strings with 2 decimal places
formatted_range_stats['mean'] = formatted_range_stats['mean'].apply(lambda x: f"{x:.2f}")
formatted_range_stats['max'] = formatted_range_stats['max'].apply(lambda x: f"{x:.2f}")
formatted_range_stats['min'] = formatted_range_stats['min'].apply(lambda x: f"{x:.2f}")
formatted_range_stats['std'] = formatted_range_stats['std'].apply(lambda x: f"{x:.2f}")

formatted_range_stats = formatted_range_stats.rename(columns={'mean': 'MeanRange',
                        'max': 'MaxRange',
                        'min': 'MinRange',
                        'std': 'StandardDeviation'})

formatted_range_stats['Rank'] = range(1, len(formatted_range_stats) + 1)
rank_col = formatted_range_stats.pop('Rank')
formatted_range_stats.insert(0, 'Rank', rank_col)

# Box Plot
make_counts = data_filtered['Make'].value_counts().sort_values(ascending=False)
top_10_makes = make_counts.head(10).index
data_filtered_top_10_makes = data_filtered[data_filtered['Make'].isin(top_10_makes)]

data_filtered_top_10_makes.boxplot(column='Electric Range', by='Make', figsize=(12,8))
plt.title('Boxplot of Mean Electric Range by Make (Top 10)')
plt.suptitle('')
plt.ylabel('Mean Electric Range (Miles)')
plt.xlabel('Make')
plt.xticks(rotation=45)
plt.show()

merged_data = pd.merge(range_stats, counted_data,  on=['Make', 'Model'])

merged_data = merged_data.sort_values('TotalCars', ascending=False).head(20)

fig, ax = plt.subplots(figsize=(10, 6))

colors = cm.rainbow(np.linspace(0, 1, len(merged_data['Make'].unique())))

for i, (make, group) in enumerate(merged_data.groupby('Make')):
    ax.scatter(group['mean'], group['TotalCars'], color=colors[i], alpha=0.6, label=make)

ax.set_title('Mean Range vs Total Cars')
ax.set_xlabel('Mean Range')
ax.set_ylabel('Total Cars')

# move the legend to the right outside the plot area
ax.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))

plt.show()
