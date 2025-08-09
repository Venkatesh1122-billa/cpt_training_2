import matplotlib.pyplot as plt
import pickle

fig, ax = plt.subplots()
ax.plot ([1,2,3,4],[11,22,33,44], label = "Line 1")
ax.set_title("Sample plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()
with open('pick.pkl', 'wb') as f:
    pickle.dump(fig,f)
with open('pick.pkl', 'rb') as f:
    loadedfig = pickle.load(f)
plt.show()
