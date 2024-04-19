# CICFlowMeter

CICFlowMeter is an open-source tool that generates Biflows from pcap files and extracts features from these flows.

## Introduction

CICFlowMeter can be used to generate bidirectional flows, where the first packet determines the forward (source to destination) and backward (destination to source) directions. This allows for the calculation of statistical time-related features separately in the forward and backward directions. Additional functionalities include selecting features from the list of existing features, adding new features, and controlling the duration of flow timeout.

**Note:** TCP flows are usually terminated upon connection teardown (by FIN packet) while UDP flows are terminated by a flow timeout. The flow timeout value can be assigned arbitrarily by the individual scheme, e.g., 600 seconds for both TCP and UDP.

For citation in your works and for a comprehensive understanding of CICFlowMeter (formerly ISCXFlowMeter), refer to the following published papers:

- Arash Habibi Lashkari, Gerard Draper-Gil, Mohammad Saiful Islam Mamun, and Ali A. Ghorbani, "Characterization of Tor Traffic Using Time Based Features", In the proceeding of the 3rd International Conference on Information System Security and Privacy, SCITEPRESS, Porto, Portugal, 2017.

- Gerard Drapper Gil, Arash Habibi Lashkari, Mohammad Mamun, Ali A. Ghorbani, "Characterization of Encrypted and VPN Traffic Using Time-Related Features", In Proceedings of the 2nd International Conference on Information Systems Security and Privacy (ICISSP 2016), pages 407-414, Rome, Italy.

## List of Extracted Features and Descriptions

| Feature Name                | Description                                                  |
|-----------------------------|--------------------------------------------------------------|
| Flow duration               | Duration of the flow in microseconds                         |
| Total Fwd Packets           | Total packets in the forward direction                       |
| Total Bwd Packets           | Total packets in the backward direction                      |
| Total Length of Fwd Packet  | Total size of packet in forward direction                    |
| Total Length of Bwd Packet  | Total size of packet in backward direction                   |
| Fwd Packet Length Min       | Minimum size of packet in forward direction                  |
| Fwd Packet Length Max       | Maximum size of packet in forward direction                  |
| ...                         | ...                                                          |
| Idle Std                    | Standard deviation time a flow was idle before becoming active|

For a more detailed explanation of each feature, refer to the original source papers.

