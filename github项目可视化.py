import requests
import plotly.express as px
url = 'https://api.github.com/search/repositories'
# url += '?q=language:python+sort:stars+stars:>10000'
headers = {"Accept": "application/vnd.github.v3+json"}
params = {
    'q':'language:python stars:>10000',  #搜索条件：Python项目，Stars > 10000
    'sort':'stars',                      #按 Stars 数排序
    'order':'desc'                       #降序排列
}
r = requests.get(url,headers= headers,params= params)
print(f'Status code:{r.status_code}')
'''存储响应为字典'''
response_dict = r.json()
print(f'Total repositories:{response_dict['total_count']}')
print(f'Complete_results:{not response_dict['total_count']}')
'''打印仓库信息'''
repo_info_dicts = response_dict['items']
repo_links, stars, hover_texts = [],[],[]
for repo_info_dict in repo_info_dicts:
    '''获取仓库url链接和名称'''
    repo_name = repo_info_dict['name']
    repo_url = repo_info_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    '''获取星星数量'''
    stars.append(repo_info_dict['stargazers_count'])
    '''获取用户信息和描述用于悬停文本'''
    owner = repo_info_dict['owner']['login']
    description = repo_info_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)
'''plotly绘制图形'''
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x = repo_links,y = stars,title = title,labels = labels,hover_name = hover_texts)
fig.update_layout(
    title_font_size = 28,
    xaxis_title_font_size = 20,
    yaxis_title_font_size = 20
)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()