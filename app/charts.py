import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
    fix, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'images/{name}.png')
    plt.close()

def generate_pie_chart(name, labels, values):
    fix, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig(f'images/{name}.png')
    plt.close()

if __name__ == "__main__":
    labels = ['a', 'b', 'c', 'd']
    values = [100, 200, 300, 400]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)