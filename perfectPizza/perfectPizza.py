import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

def main():
    # Compute areas and colors
    N = 150
    r = 2 * np.random.rand(N)
    theta = 2 * np.pi * np.random.rand(N)
    area = 200 * r**2
    colors = theta

    fig = plt.figure()
    ax = fig.add_subplot(projection='polar')
    c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)


    #saving the graphhy locally
    plt.savefig("/home/student/mycode/perfectPizza/perfectPizza.png")

    #saving graph to static
    plt.savefig("/home/student/static/perfectPizza.png")
    print("Graph created.")

if __name__ == "__main__":
    main()
