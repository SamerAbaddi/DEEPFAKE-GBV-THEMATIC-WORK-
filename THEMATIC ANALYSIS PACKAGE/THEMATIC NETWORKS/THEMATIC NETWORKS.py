import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import textwrap

G = nx.DiGraph()


themes = {
    'Digital Vulnerability and Exposure': {'color': 'lightblue', 'size': 40000},
    'Impact on Professional Life': {'color': 'lightgreen', 'size': 25000},
    'Psychological and Emotional Effects': {'color': 'salmon', 'size': 30000},
    'Awareness and Prevention Measures': {'color': 'gold', 'size': 15000}
}

sub_themes = {}
for i, theme in enumerate(themes):
    for j in range(1, 80):
        sub_theme_name = f"Sub_{j}_{theme[:3]}"
        sub_themes[sub_theme_name] = theme

for theme, attrs in themes.items():
    G.add_node(theme, size=attrs['size'], color=attrs['color'])

for sub_theme, theme in sub_themes.items():
    G.add_node(sub_theme, size=200, color=themes[theme]['color'])
    connections = np.random.choice(list(themes.keys()), np.random.randint(1, 2), replace=False)
    for conn in connections:
        G.add_edge(conn, sub_theme)

pos = nx.spring_layout(G, seed=42)

theme_positions = np.array([
    [-0.3, 0.3],
    [0.32, 0.35],
    [-0.35, -0.35],
    [0.31, -0.4]
])

for i, theme in enumerate(themes):
    pos[theme] = theme_positions[i]

wrapped_labels = {node: textwrap.fill(node, width=20) for node in themes}

plt.figure(figsize=(12, 12))
nx.draw_networkx_nodes(G, pos, node_size=[G.nodes[n]['size'] for n in G], node_color=[G.nodes[n]['color'] for n in G])
nx.draw_networkx_edges(G, pos, edge_color='gray', alpha=0.4)


nx.draw_networkx_labels(G, pos, labels=wrapped_labels, font_size=10)

plt.title('Thematic Network Diagram for the 4 Main Themes', fontsize=15)
plt.axis('off')
plt.show()

