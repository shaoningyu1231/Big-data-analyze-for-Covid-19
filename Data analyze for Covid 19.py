#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Data analyze for Covid 19


# In[5]:


get_ipython().system('pip install pandas')


# In[8]:


import pandas as pd 
confirmed_data = pd.read_csv("/Users/shaoningyu/Downloads/COVID-19/time_series_covid19_recovered_global.csv")
deaths_data = pd.read_csv('/Users/shaoningyu/Downloads/COVID-19/time_series_covid19_deaths_global.csv')
recovered_data = pd.read_csv('/Users/shaoningyu/Downloads/COVID-19/time_series_covid19_recovered_global.csv')


# In[9]:


# Just put TAIWAN into our country as it should be.
confirmed_data['Country/Region']=confirmed_data['Country/Region'].apply(lambda x: 'United States' if x == 'US' else x)
deaths_data['Country/Region']=deaths_data['Country/Region'].apply(lambda x: 'United States' if x == 'US' else x)
recovered_data['Country/Region']=recovered_data['Country/Region'].apply(lambda x: 'United States' if x == 'US' else x)


idx = confirmed_data[confirmed_data['Country/Region'] == 'Taiwan*'].index[0]
confirmed_data.loc[idx, 'Province/State'] = 'Taiwan'
confirmed_data.loc[idx, 'Country/Region'] = 'China'

idx = deaths_data[deaths_data['Country/Region'] == 'Taiwan*'].index[0]
deaths_data.loc[idx, 'Province/State'] = 'Taiwan'
deaths_data.loc[idx, 'Country/Region'] = 'China'

idx = recovered_data[recovered_data['Country/Region'] == 'Taiwan*'].index[0]
recovered_data.loc[idx, 'Province/State'] = 'Taiwan'
recovered_data.loc[idx, 'Country/Region'] = 'China'


# In[10]:


# Creating the country map.
country_map = {
    'Singapore Rep.': '新加坡', 'Dominican Rep.': '多米尼加', 'Palestine': '巴勒斯坦', 'Bahamas': '巴哈马', 'Timor-Leste': '东帝汶',
    'Afghanistan': '阿富汗', 'Guinea-Bissau': '几内亚比绍', "Côte d'Ivoire": '科特迪瓦', 'Siachen Glacier': '锡亚琴冰川',
    "Br. Indian Ocean Ter.": '英属印度洋领土', 'Angola': '安哥拉', 'Albania': '阿尔巴尼亚', 'United Arab Emirates': '阿联酋',
    'Argentina': '阿根廷', 'Armenia': '亚美尼亚', 'French Southern and Antarctic Lands': '法属南半球和南极领地', 'Australia': '澳大利亚',
    'Austria': '奥地利', 'Azerbaijan': '阿塞拜疆', 'Burundi': '布隆迪', 'Belgium': '比利时', 'Benin': '贝宁', 'Burkina Faso': '布基纳法索',
    'Bangladesh': '孟加拉国', 'Bulgaria': '保加利亚', 'The Bahamas': '巴哈马', 'Bosnia and Herz.': '波斯尼亚和黑塞哥维那', 'Belarus': '白俄罗斯',
    'Belize': '伯利兹', 'Bermuda': '百慕大', 'Bolivia': '玻利维亚', 'Brazil': '巴西', 'Brunei': '文莱', 'Bhutan': '不丹',
    'Botswana': '博茨瓦纳', 'Central African Rep.': '中非', 'Canada': '加拿大', 'Switzerland': '瑞士', 'Chile': '智利',
    'China': '中国', 'Ivory Coast': '象牙海岸', 'Cameroon': '喀麦隆', 'Dem. Rep. Congo': '刚果民主共和国', 'Congo': '刚果',
    'Colombia': '哥伦比亚', 'Costa Rica': '哥斯达黎加', 'Cuba': '古巴', 'N. Cyprus': '北塞浦路斯', 'Cyprus': '塞浦路斯', 'Czech Rep.': '捷克',
    'Germany': '德国', 'Djibouti': '吉布提', 'Denmark': '丹麦', 'Algeria': '阿尔及利亚', 'Ecuador': '厄瓜多尔', 'Egypt': '埃及',
    'Eritrea': '厄立特里亚', 'Spain': '西班牙', 'Estonia': '爱沙尼亚', 'Ethiopia': '埃塞俄比亚', 'Finland': '芬兰', 'Fiji': '斐',
    'Falkland Islands': '福克兰群岛', 'France': '法国', 'Gabon': '加蓬', 'United Kingdom': '英国', 'Georgia': '格鲁吉亚',
    'Ghana': '加纳', 'Guinea': '几内亚', 'Gambia': '冈比亚', 'Guinea Bissau': '几内亚比绍', 'Eq. Guinea': '赤道几内亚', 'Greece': '希腊',
    'Greenland': '格陵兰', 'Guatemala': '危地马拉', 'French Guiana': '法属圭亚那', 'Guyana': '圭亚那', 'Honduras': '洪都拉斯',
    'Croatia': '克罗地亚', 'Haiti': '海地', 'Hungary': '匈牙利', 'Indonesia': '印度尼西亚', 'India': '印度', 'Ireland': '爱尔兰',
    'Iran': '伊朗', 'Iraq': '伊拉克', 'Iceland': '冰岛', 'Israel': '以色列', 'Italy': '意大利', 'Jamaica': '牙买加', 'Jordan': '约旦',
    'Japan': '日本', 'Kazakhstan': '哈萨克斯坦', 'Kenya': '肯尼亚', 'Kyrgyzstan': '吉尔吉斯斯坦', 'Cambodia': '柬埔寨', 'Korea': '韩国',
    'Kosovo': '科索沃', 'Kuwait': '科威特', 'Lao PDR': '老挝', 'Lebanon': '黎巴嫩', 'Liberia': '利比里亚', 'Libya': '利比亚',
    'Sri Lanka': '斯里兰卡', 'Lesotho': '莱索托', 'Lithuania': '立陶宛', 'Luxembourg': '卢森堡', 'Latvia': '拉脱维亚', 'Morocco': '摩洛哥',
    'Moldova': '摩尔多瓦', 'Madagascar': '马达加斯加', 'Mexico': '墨西哥', 'Macedonia': '马其顿', 'Mali': '马里', 'Myanmar': '缅甸',
    'Montenegro': '黑山', 'Mongolia': '蒙古', 'Mozambique': '莫桑比克', 'Mauritania': '毛里塔尼亚', 'Malawi': '马拉维',
    'Malaysia': '马来西亚', 'Namibia': '纳米比亚', 'New Caledonia': '新喀里多尼亚', 'Niger': '尼日尔', 'Nigeria': '尼日利亚',
    'Nicaragua': '尼加拉瓜', 'Netherlands': '荷兰', 'Norway': '挪威', 'Nepal': '尼泊尔', 'New Zealand': '新西兰', 'Oman': '阿曼',
    'Pakistan': '巴基斯坦', 'Panama': '巴拿马', 'Peru': '秘鲁', 'Philippines': '菲律宾', 'Papua New Guinea': '巴布亚新几内亚',
    'Poland': '波兰', 'Puerto Rico': '波多黎各', 'Dem. Rep. Korea': '朝鲜', 'Portugal': '葡萄牙', 'Paraguay': '巴拉圭',
    'Qatar': '卡塔尔', 'Romania': '罗马尼亚', 'Russia': '俄罗斯', 'Rwanda': '卢旺达', 'W. Sahara': '西撒哈拉', 'Saudi Arabia': '沙特阿拉伯',
    'Sudan': '苏丹', 'S. Sudan': '南苏丹', 'Senegal': '塞内加尔', 'Solomon Is.': '所罗门群岛', 'Sierra Leone': '塞拉利昂',
    'El Salvador': '萨尔瓦多', 'Somaliland': '索马里兰', 'Somalia': '索马里', 'Serbia': '塞尔维亚', 'Suriname': '苏里南',
    'Slovakia': '斯洛伐克', 'Slovenia': '斯洛文尼亚', 'Sweden': '瑞典', 'Swaziland': '斯威士兰', 'Syria': '叙利亚', 'Chad': '乍得',
    'Togo': '多哥', 'Thailand': '泰国', 'Tajikistan': '塔吉克斯坦', 'Turkmenistan': '土库曼斯坦', 'East Timor': '东帝汶',
    'Trinidad and Tobago': '特里尼达和多巴哥', 'Tunisia': '突尼斯', 'Turkey': '土耳其', 'Tanzania': '坦桑尼亚', 'Uganda': '乌干达',
    'Ukraine': '乌克兰', 'Uruguay': '乌拉圭', 'United States': '美国', 'Uzbekistan': '乌兹别克斯坦', 'Venezuela': '委内瑞拉',
    'Vietnam': '越南', 'Vanuatu': '瓦努阿图', 'West Bank': '西岸', 'Yemen': '也门', 'South Africa': '南非', 'Zambia': '赞比亚',
    'Zimbabwe': '津巴布韦', 'Comoros': '科摩罗'
}

province_map = {
    'Anhui': '安徽', 'Beijing': '北京', 'Chongqing': '重庆', 'Fujian': '新疆', 'Gansu': '甘肃', 'Guangdong': '广东',
    'Guangxi': '广西', 'Guizhou': '贵州', 'Hainan': '海南', 'Hebei': '河北', 'Heilongjiang': '黑龙江', 'Henan': '河南',
    'Hong Kong': '香港', 'Hubei': '湖北', 'Hunan': '湖南', 'Inner Mongolia': '内蒙古', 'Jiangsu': '江苏',
    'Jiangxi': '江西', 'Jilin': '吉林', 'Liaoning': '辽宁', 'Macau': '澳门', 'Ningxia': '宁夏', 'Qinghai': '青海',
    'Shaanxi': '陕西', 'Shandong': '山东', 'Shanghai': '上海', 'Shanxi': '山西', 'Sichuan': '四川', 'Tianjin': '天津',
    'Tibet': '西藏', 'Xinjiang': '新疆', 'Yunnan': '云南', 'Zhejiang': '浙江', 'Fujian':'福建', 'Taiwan': '台湾'
}

confirmed_data['Country/Region_zh'] = confirmed_data['Country/Region'].apply(lambda x: country_map.get(x, x))
deaths_data['Country/Region_zh'] = deaths_data['Country/Region'].apply(lambda x: country_map.get(x, x))
recovered_data['Country/Region_zh'] = recovered_data['Country/Region'].apply(lambda x: country_map.get(x, x))

confirmed_data['Province/State_zh'] = confirmed_data['Province/State'].apply(lambda x: province_map.get(x, x))
deaths_data['Province/State_zh'] = deaths_data['Province/State'].apply(lambda x: province_map.get(x, x))
recovered_data['Province/State_zh'] = recovered_data['Province/State'].apply(lambda x: province_map.get(x, x))

# arrange the order 
confirmed_data = confirmed_data[['Province/State_zh', 'Country/Region_zh'] + confirmed_data.columns[:-2].to_list()]
deaths_data = deaths_data[['Province/State_zh', 'Country/Region_zh'] + deaths_data.columns[:-2].to_list()]
recovered_data = recovered_data[['Province/State_zh', 'Country/Region_zh'] + recovered_data.columns[:-2].to_list()]


# In[23]:


confirmed = confirmed_data.groupby('Country/Region').agg({lastdate: 'sum'}).to_dict()[lastdate]
deaths = deaths_data.groupby('Country/Region').agg({lastdate: 'sum'}).to_dict()[lastdate]
recovered = recovered_data.groupby('Country/Region').agg({lastdate: 'sum'}).to_dict()[lastdate]
exists_confirmed = {key: value - deaths[key] - recovered[key]  for key, value in confirmed.items()}
c = (
    Map()
    .add("Confirmed", [*confirmed.items()], "world", is_map_symbol_show=False)
    .add("Cured", [*recovered.items()], "world", is_map_symbol_show=False)
    .add("Death", [*deaths.items()], "world", is_map_symbol_show=False)
    .add("Confirmed(now)", [*exists_confirmed.items()], "world", is_map_symbol_show=False)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title=f'({lastdate})World condition'),
        visualmap_opts=opts.VisualMapOpts(max_=200000),  

    )
)
c.render_notebook()


# In[22]:


from pyecharts import options as opts
from pyecharts.charts import Map, Timeline, Bar, Line
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts

lastdate = confirmed_data.columns[-1]
confirmed_total = confirmed_data[lastdate].sum()
deaths_total = deaths_data[lastdate].sum()
recovered_total = recovered_data[lastdate].sum()
deaths_rate = deaths_total / confirmed_total
recovered_rate = recovered_total / confirmed_total

table = Table()

headers = ['Confirmed', 'Death', 'Cured', 'Death rate', 'Curing rate']
rows = [
    [confirmed_total, deaths_total, recovered_total, f'{deaths_rate:.2%}', f'{recovered_rate:.2%}'],    
]
table.add(headers, rows)
table.set_global_opts(
    title_opts=ComponentTitleOpts(title=f'({lastdate})World condition')
)
table.render_notebook()


# In[12]:


get_ipython().system('pip install pyecharts')


# In[25]:


tl = Timeline()
tl.add_schema(
#         is_auto_play=True,
        is_loop_play=False,
        play_interval=200,
    )
target = confirmed_data.columns[6:].to_list()
target.reverse()
target = target[::7]
target.reverse()
for dt in target:    
    confirmed = confirmed_data.groupby('Country/Region').agg({dt: 'sum'}).to_dict()[dt]
    c = (
        Map()
        .add("Confirmed", [*confirmed.items()], "world", is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="World Condition"),
            visualmap_opts=opts.VisualMapOpts(max_=200000),  
            
        )
    )
    tl.add(c, dt)
tl.render_notebook()


# In[26]:


tl = Timeline()
tl.add_schema(
#         is_auto_play=True,
        is_loop_play=False,
        play_interval=100,
    )

for dt in confirmed_data.columns[6:]:
    confirmed = confirmed_data.groupby('Country/Region_zh').agg({dt: 'sum'}).sort_values(by=dt, ascending=False)[:20].sort_values(by=dt).to_dict()[dt]
    bar = (
        Bar()
        .add_xaxis([*confirmed.keys()])
        .add_yaxis("确诊人数", [*confirmed.values()], label_opts=opts.LabelOpts(position="right"))
        .reversal_axis()
        .set_global_opts(
            title_opts=opts.TitleOpts("各国确诊人数排行 TOP20")
        )
    )
    tl.add(bar, dt)
tl.render_notebook()


# In[ ]:





# In[28]:


from pyecharts import options as opts
from pyecharts.charts import Map, Timeline, Bar, Line
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts

lastdate = confirmed_data.columns[-1]
confirmed_data_china = confirmed_data[confirmed_data['Country/Region'] == 'China']
deaths_data_china = deaths_data[deaths_data['Country/Region'] == 'China']
recovered_data_china = recovered_data[recovered_data['Country/Region'] == 'China']

confirmed_total_china = confirmed_data_china[lastdate].sum()
deaths_total_china = deaths_data_china[lastdate].sum()
recovered_total_china = recovered_data_china[lastdate].sum()
exists_confirmed_china = confirmed_total_china - deaths_total_china - recovered_total_china

deaths_rate_china = deaths_total_china / confirmed_total_china
recovered_rate_china = recovered_total_china / confirmed_total_china

table = Table()

headers = ['确诊人数', '死亡人数', '治愈人数', '死亡率', '治愈率', '现有确诊人数']
rows = [
    [confirmed_total_china, deaths_total_china, recovered_total_china, f'{deaths_rate_china:.2%}', f'{recovered_rate_china:.2%}', exists_confirmed_china],    
]
table.add(headers, rows)
table.set_global_opts(
    title_opts=ComponentTitleOpts(title=f'({lastdate})中国疫情情况')
)
table.render_notebook()


# In[29]:


tl = Timeline()
tl.add_schema(
#         is_auto_play=True,
        is_loop_play=False,
        play_interval=200,
    )
target = confirmed_data_china.columns[6:].to_list()
target.reverse()
target = target[::7]
target.reverse()
for dt in target:    
    confirmed = confirmed_data_china.groupby('Province/State_zh').agg({dt: 'sum'}).to_dict()[dt]
    c = (
        Map()
        .add("确诊人数", [*confirmed.items()], "china", is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        .set_global_opts(
            title_opts=opts.TitleOpts(title='中国疫情历史发展情况'),
            visualmap_opts=opts.VisualMapOpts(max_=1000),            
        )
    )
    tl.add(c, dt)
tl.render_notebook()


# In[30]:


tl = Timeline()
tl.add_schema(
#         is_auto_play=True,
        is_loop_play=False,
        play_interval=100,
    )

for dt in confirmed_data.columns[6:]:
    confirmed = confirmed_data_china.groupby('Province/State_zh').agg({dt: 'sum'}).sort_values(by=dt, ascending=False)[:20].sort_values(by=dt).to_dict()[dt]
    bar = (
        Bar()
        .add_xaxis([*confirmed.keys()])
        .add_yaxis("确诊人数", [*confirmed.values()], label_opts=opts.LabelOpts(position="right"))
        .reversal_axis()
        .set_global_opts(
            title_opts=opts.TitleOpts("各省确诊人数排行 TOP20")
        )
    )
    tl.add(bar, dt)
tl.render_notebook()


# In[ ]:




