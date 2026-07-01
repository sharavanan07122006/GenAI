import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

data={
    "Age":[25, 27, 50, 30, 55],
    "Income":[50000, 55000, 80000, 60000, 90000],
    "Spending_Score":[60, 70, 80, 65, 90]
}
df= pd.DataFrame(data)
print("Customer Data:")
print(df)

Scalar = StandardScaler()
scaled_data = Scalar.fit_transform(df)

pca = PCA(n_components=2)
compressed_data = pca.fit_transform(scaled_data)
compressed_df = pd.DataFrame(compressed_data, columns=['PC1', 'PC2'])
print("\nCompressed Customer Data:")
print(compressed_df)

print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

plt.figure(figsize=(8,6))
plt.scatter(compressed_df['PC1'], compressed_df['PC2'],s=100)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Customer Data')
plt.grid(True)
plt.show()