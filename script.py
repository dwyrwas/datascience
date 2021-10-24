import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())
click_source = ad_clicks.groupby('utm_source').user_id.count().reset_index()
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
clicks_by_source = ad_clicks.groupby([('utm_source'), ('is_click')]).user_id.count().reset_index()
clicks_pivot = clicks_by_source.pivot(
  index = 'utm_source',
  columns = 'is_click' ,
  values = 'user_id',
)
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[False] + clicks_pivot[True])

print(ad_clicks.groupby('experimental_group').user_id.count())

group_clicks = ad_clicks.groupby([('experimental_group'), ('is_click')]).user_id.count().reset_index()
group_clicks_pivot = group_clicks.pivot(
  index = 'experimental_group',
  columns = 'is_click',
  values = 'user_id'
)
print(group_clicks_pivot)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

a_clicks_by_day = a_clicks.groupby([('day'),('is_click')]).user_id.count().reset_index()
a_clicks_by_day_pivot =a_clicks_by_day.pivot(
  index ='day',
  columns ='is_click',
  values ='user_id',
)
a_clicks_by_day_pivot['percent_clicked']=a_clicks_by_day_pivot[True]/(a_clicks_by_day_pivot[True]+a_clicks_by_day_pivot[False])

print(a_clicks_by_day_pivot)

b_clicks_by_day = b_clicks.groupby([('day'),('is_click')]).user_id.count().reset_index()
b_clicks_by_day_pivot = b_clicks_by_day.pivot(
  index ='day',
  columns ='is_click',
  values ='user_id',
)
b_clicks_by_day_pivot['percent_clicked']=b_clicks_by_day_pivot[True]/(b_clicks_by_day_pivot[True]+b_clicks_by_day_pivot[False])

print(b_clicks_by_day_pivot)


