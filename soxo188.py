import config
import requests
import pandas as pd
from ast import literal_eval
import plotly.figure_factory as ff

def parse_soxo188_api(province):
    url = config.PROVINCES[province]
    resp = requests.get(url).json()
    issue_lists = resp['t']['issueList']
    results = list(map(lambda issue_list: format_issue_list(issue_list), issue_lists)) 
    return results

def format_issue_list(issue_list):
    dataset = {'Giải': ['Giải tám', 'Giải bảy', 'Giải sáu', 'Giải năm', 'Giải tư', 'Giải ba', 'Giải nhì', 'Giải nhất', 'Giải Đặc Biệt'], 
               'Giải Thưởng': ['100.000đ', '200.000đ', '400.000đ', '1.0000.000đ', '3.0000.000đ', '10.0000.000đ', '15.0000.000đ', '30.0000.000đ', '2.000.0000.000đ']}
    detail = issue_list['detail']
    result = literal_eval(detail)[::-1]
    turn_num = issue_list['turnNum']
    result[2] = result[2].replace(',', '     ')
    result[4] = br_array(result[4].split(','))
    result[5] = result[5].replace(',', '     ')
    ket_qua_header = f'Kết Quả  <br>{turn_num}'
    dataset[f'{ket_qua_header}'] = result

    df = pd.DataFrame(dataset)
    table = ff.create_table(df, height_constant=20)
    table.update_layout(
        width=700,
        height=300,
        font=dict(family='Tahoma'),
        font_size=12
    )
    return table

def br_array(arr):
    arr[4] = f'<br>{arr[4]}'
    return ",".join(arr).replace(',', '     ')
