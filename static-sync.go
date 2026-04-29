type Node struct {
	id int
	delay int
}
func createReplicas(n int) []Node {
	replicas := make([]Node, n)
	for i := 0; i < n; i++ {
		replicas[i] = Node{id: i + 1, delay: 0}
	}
	return replicas
}
func staticReplication(replicas []Node) {
	for i := range replicas {
		delay := rand.Intn(120) + 80
		replicas[i].delay = delay
		time.Sleep(time.Millisecond * time.Duration(delay))
		fmt.Printf("Replica %d replicated in %d ms\n", replicas[i].id, delay)
	}
}
func runCycle(replicas []Node, cycle int) {
	fmt.Printf("\nReplication Cycle %d\n", cycle)
	staticReplication(replicas)
}
func monitor(replicas []Node) {
	total := 0
	for _, r := range replicas {
		total += r.delay
	}
	avg := total / len(replicas)
	fmt.Printf("Average replication delay %d ms\n", avg)
}
func main() {
	rand.Seed(time.Now().UnixNano())
	replicas := createReplicas(5)

	fmt.Println("Existing Static Replication Simulation")
	for i := 1; i <= 6; i++ {
		runCycle(replicas, i)
		monitor(replicas)
	}
	fmt.Println("\nSimulation Complete")
}
