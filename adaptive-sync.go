type Node struct {
	id int
	delay int
	load int
}

func createNodes(n int) []Node {
	nodes := make([]Node, n)
	for i := 0; i < n; i++ {
		nodes[i] = Node{id: i + 1, delay: 0, load: rand.Intn(50)}
	}
	return nodes
}

func adaptiveReplication(nodes []Node) {
	for i := range nodes {
		base := rand.Intn(70) + 30
		loadFactor := nodes[i].load
		delay := base + loadFactor/2
		nodes[i].delay = delay
		time.Sleep(time.Millisecond * time.Duration(delay))
		fmt.Printf("Node %d adaptive delay %d ms\n", nodes[i].id, delay)
	}
}

func evaluate(nodes []Node) {
	total := 0
	for _, n := range nodes {
		total += n.delay
	}
	avg := total / len(nodes)
	fmt.Printf("Average adaptive delay %d ms\n", avg)
}

func simulate(nodes []Node, cycle int) {
	fmt.Printf("\nAdaptive Cycle %d\n", cycle)
	adaptiveReplication(nodes)
	evaluate(nodes)
}

func main() {
	rand.Seed(time.Now().UnixNano())
	nodes := createNodes(5)

	fmt.Println("Adaptive Replication Simulation")

	for i := 1; i <= 6; i++ {
		simulate(nodes, i)
	}

	fmt.Println("\nAdaptive Synchronization Complete")
}
