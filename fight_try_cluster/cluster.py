import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
df = pd.read_csv('D:/deeplearning_study/ML-For-Beginners/6-NLP/5-Hotel-Reviews-2/fight_try_cluster/Hotel_Reviews_NLP.csv')
hotel_features = df.groupby('Hotel_Name').agg({
    'Positive_Sentiment': 'mean',
    'Negative_Sentiment': 'mean',
    'Reviewer_Score': 'mean',
    'Total_Number_of_Reviews': 'first',
    'Leisure_trip': 'mean',
    'Couple': 'mean',
    'Solo_traveler': 'mean',
    'Business_trip': 'mean',
    'Group': 'mean',
    'Family_with_young_children': 'mean',
    'Family_with_older_children': 'mean',
    'With_a_pet': 'mean'
}).reset_index()

# 处理缺失值（如果有）
hotel_features = hotel_features.fillna(0)

# 选择用于聚类的特征列
feature_cols = ['Positive_Sentiment', 'Negative_Sentiment', 'Reviewer_Score', 'Total_Number_of_Reviews',
                'Leisure_trip', 'Couple', 'Solo_traveler', 'Business_trip', 'Group',
                'Family_with_young_children', 'Family_with_older_children', 'With_a_pet']
X = hotel_features[feature_cols]

# 标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 肘部法确定K值
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)
#kmeans.inertia_ 是 KMeans 模型在拟合数据后自动计算并保存的一个属性。它代表了聚类模型的一个性能指标：所有样本到其所属簇中心（质心）的距离的平方和。

plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()

# 假设选 K=3
kmeans = KMeans(n_clusters=3, random_state=42)
hotel_features['Cluster'] = kmeans.fit_predict(X_scaled)

# 查看每个簇的统计特征
cluster_summary = hotel_features.groupby('Cluster')[feature_cols].mean()
print(cluster_summary)