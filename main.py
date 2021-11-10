import pandas

data = pandas.read_csv('2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')
color_nums = data['Primary Fur Color'].value_counts().to_list()
color_list = pandas.Series(data['Primary Fur Color'].unique()).to_list()[1:]
color_stats = pandas.DataFrame({
    'Primary Color': color_list,
    'Count': color_nums
})
color_stats.to_csv('color_stats.csv')
# color_names = colors.unique()
# color_stats = {}
# for color in color_names:
#     color_number = colors[]
#     color_stats.update()
print(color_stats)



