import matplotlib.pyplot as plt

# -------------------------------------------------------
# STEP 1: Define Data (from Table III in your paper)
# -------------------------------------------------------
cluster_nodes = [3, 5, 7, 9, 11]

static_delay = [210, 335, 472, 615, 768]
adaptive_delay = [148, 236, 318, 405, 512]

# -------------------------------------------------------
# STEP 2: Validate Data Integrity
# -------------------------------------------------------
def validate_data(x, y1, y2):
    if not (len(x) == len(y1) == len(y2)):
        raise ValueError("Data length mismatch detected!")
    print("Data validation successful.\n")

validate_data(cluster_nodes, static_delay, adaptive_delay)

# -------------------------------------------------------
# STEP 3: Compute Improvement Percentage
# -------------------------------------------------------
def compute_improvement(static, adaptive):
    improvement = []
    for s, a in zip(static, adaptive):
        percent = ((s - a) / s) * 100
        improvement.append(round(percent, 2))
    return improvement

improvement_percent = compute_improvement(static_delay, adaptive_delay)

# Print improvements
print("Improvement (%) for each cluster size:")
for n, imp in zip(cluster_nodes, improvement_percent):
    print(f"Nodes={n} -> Improvement={imp}%")

print("\n")

# -------------------------------------------------------
# STEP 4: Plot Graph (Baseline vs Adaptive)
# -------------------------------------------------------
def plot_graph(nodes, static, adaptive):
    plt.figure(figsize=(10, 6))

    # Static line
    plt.plot(nodes, static, marker='o', linewidth=2,
             label='Static Synchronization')

    # Adaptive line
    plt.plot(nodes, adaptive, marker='o', linewidth=2,
             label='Adaptive Synchronization')

    # Labels
    plt.xlabel('Cluster Nodes', fontsize=12)
    plt.ylabel('Synchronization Delay (ms)', fontsize=12)
    plt.title('Baseline vs Adaptive Replication', fontsize=14)

    # Grid
    plt.grid(True)

    # Legend
    plt.legend()

    # Annotate each point
    for i in range(len(nodes)):
        plt.text(nodes[i], static[i], f"{static[i]}",
                 fontsize=9, ha='right')
        plt.text(nodes[i], adaptive[i], f"{adaptive[i]}",
                 fontsize=9, ha='left')

    plt.tight_layout()

# -------------------------------------------------------
# STEP 5: Save Graph to File
# -------------------------------------------------------
def save_plot(filename="replication_graph.png"):
    plt.savefig(filename, dpi=300)
    print(f"Graph saved as {filename}")

# -------------------------------------------------------
# STEP 6: Execute Everything
# -------------------------------------------------------
plot_graph(cluster_nodes, static_delay, adaptive_delay)
save_plot()

plt.show()

# -------------------------------------------------------
# STEP 7: Optional Summary Output
# -------------------------------------------------------
def summary():
    print("\nSUMMARY:")
    print("--------")
    print("Static delay increases rapidly with cluster size.")
    print("Adaptive delay grows slower due to optimization.")
    print("Average improvement:",
          round(sum(improvement_percent)/len(improvement_percent), 2), "%")

summary()
