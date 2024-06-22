import csv

# 讀取CSV文件
file_path = 'nba_standings.csv'
df = open(file_path,"r")

# (1) 找出東部聯盟中主場勝率低於客場勝率的球隊
def get_win_percentage(record):
    # 根據勝-負記錄計算勝率
    wins, losses = map(int, record.split('-'))
    return wins / (wins + losses)

# 篩選出東部聯盟的球隊
east_teams = df[df['Conference'] == 'Eastern']

# 找出主場勝率低於客場勝率的東部聯盟球隊
east_teams_with_lower_home_win_percentage = east_teams[east_teams['Home'].apply(get_win_percentage) < east_teams['Away'].apply(get_win_percentage)]

# 獲取這些球隊的名字
east_teams_with_lower_home_win_percentage_names = east_teams_with_lower_home_win_percentage['Team'].tolist()
print("(1) 東部主場勝率低於客場勝率的球隊: ", east_teams_with_lower_home_win_percentage_names)

# (2) 計算每個聯盟的“得分減去失分”的平均值
df['PF-PA'] = df['PF'] - df['PA']  # 計算每支球隊的“得分減去失分”

# 按聯盟分組計算平均值
average_diff_by_conference = df.groupby('Conference')['PF-PA'].mean()

# 找出擁有較高平均值的聯盟
higher_avg_diff_conference = average_diff_by_conference.idxmax()
print("(2) 擁有較高“平均得分減掉失分”的聯盟: ", higher_avg_diff_conference)

# (3) 生成根據與另一聯盟球隊勝率的排名列表
df['Inter-Conference Wins'] = df['W-L'].apply(lambda x: int(x.split('-')[0]))  # 提取勝場數
df['Inter-Conference Games'] = df['W-L'].apply(lambda x: int(x.split('-')[0]) + int(x.split('-')[1]))  # 計算總場數

# 計算對另一聯盟球隊的勝率
df['Inter-Conference Win Percentage'] = df['Inter-Conference Wins'] / df['Inter-Conference Games']

# 根據勝率排序並生成排名列表
ranking = df.sort_values(by='Inter-Conference Win Percentage', ascending=False)[['Team', 'Inter-Conference Win Percentage']]
print("(3) 根據與另一聯盟球隊勝率的排名列表: ")
print(ranking)
df.close()#把檔案關掉

