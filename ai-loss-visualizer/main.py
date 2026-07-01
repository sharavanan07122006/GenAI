import matplotlib.pyplot as plt

epochs = [1, 2, 3, 4, 5, 6]
loss = [100, 80, 60, 40, 25, 10]
accuracy = [40, 50, 65, 75, 85, 95]
plt.figure(figsize=(8, 5))
plt.plot(
    epochs,
    loss,
    marker="o",
    label="Loss"
)
plt.title("AI Learning Process")
plt.xlabel("Epochs")
plt.ylabel("Loss")

plt.grid()
plt.legend()
plt.show()
plt.figure(figsize=(8, 5))
plt.plot(
    epochs,
    accuracy,
    marker="o",
   label="Accuracy"
)
plt.title("Model Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy (%)")
plt.grid()
plt.legend()
plt.show()
loss_model1 = [100, 80, 60, 40, 25, 10]
loss_model2 = [100, 90, 75, 55, 35, 20]
plt.figure(figsize=(8, 5))
plt.plot(
    epochs,
    loss_model1,
    marker="o",
    label="Model 1"
)
plt.plot(
    epochs,
    loss_model2,
    marker="o",
    label="Model 2"
)
plt.title("Multiple Loss Curves")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.grid()
plt.legend()
plt.show()
lr_001 = [100, 90, 80, 70, 60, 50]
lr_01 = [100, 75, 50, 30, 15, 5]
plt.figure(figsize=(8, 5))
plt.plot(
    epochs,
    lr_001,
    marker="o",
    label="LR = 0.001"
)
plt.plot(
    epochs,
    lr_01,
    marker="o",
    label="LR = 0.01"
)
plt.title("Learning Rate Comparison")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.grid()
plt.legend()
plt.show()