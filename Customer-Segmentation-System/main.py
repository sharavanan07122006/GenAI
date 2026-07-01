import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data={
    "Age":[25, 27, 50, 30, 55],
    "Income":[50000, 55000, 80000, 60000, 90000]
}
df = pd.DataFrame(data)

print("Customer Data:")
print(df)

model = KMeans(n_clusters=2, random_state=42)
model.fit(df)
#assign clusters
df['Cluster'] = model.labels_
print("\nCustomer Segmentation:")
print(df)
#cluster centers
print("\nCluster Centers:")
print(model.cluster_centers_)
#visualization
plt.scatter(df['Age'], df['Income'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Customer Segmentation')
plt.show()