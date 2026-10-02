from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

class EmergencyTopo(Topo):
    "Emergency Network Topology with 3 Switches and 3 Hosts"
    def build(self):
        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Add hosts
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')

        # Connect hosts to their switches
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)

        # Connect switches together linearly
        self.addLink(s1, s2)
        self.addLink(s2, s3)

def run():
    topo = EmergencyTopo()
    net = Mininet(topo=topo, controller=RemoteController, switch=OVSSwitch)
    net.start()
    info("*** Emergency Topology loaded. Entering CLI...\n")
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
