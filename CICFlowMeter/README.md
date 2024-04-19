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
| Packet Length Mean          | Mean length of a packet                                      |
| Packet Length Std           | Standard deviation length of a packet                        |
| Packet Length Variance      | Variance length of a packet                                  |
| FIN Flag Count              | Number of packets with FIN                                   |
| SYN Flag Count              | Number of packets with SYN                                   |
| RST Flag Count              | Number of packets with RST                                   |
| PSH Flag Count              | Number of packets with PUSH                                  |
| ACK Flag Count              | Number of packets with ACK                                   |
| URG Flag Count              | Number of packets with URG                                   |
| CWR Flag Count              | Number of packets with CWR                                   |
| ECE Flag Count              | Number of packets with ECE                                   |
| down/Up Ratio               | Download and upload ratio                                    |
| Average Packet Size         | Average size of packet                                       |
| Fwd Segment Size Avg        | Average size observed in the forward direction               |
| Bwd Segment Size Avg        | Average number of bytes bulk rate in the backward direction  |
| Fwd Bytes/Bulk Avg          | Average number of bytes bulk rate in the forward direction   |
| Fwd Packet/Bulk Avg         | Average number of packets bulk rate in the forward direction |
| Fwd Bulk Rate Avg           | Average number of bulk rate in the forward direction         |
| Bwd Bytes/Bulk Avg          | Average number of bytes bulk rate in the backward direction  |
| Bwd Packet/Bulk Avg         | Average number of packets bulk rate in the backward direction|
| Bwd Bulk Rate Avg           | Average number of bulk rate in the backward direction        |
| Subflow Fwd Packets         | The average number of packets in a sub flow in the forward direction|
| Subflow Fwd Bytes           | The average number of bytes in a sub flow in the forward direction|
| Subflow Bwd Packets         | The average number of packets in a sub flow in the backward direction|
| Subflow Bwd Bytes           | The average number of bytes in a sub flow in the backward direction|
| Fwd Init Win bytes          | The total number of bytes sent in initial window in the forward direction|
| Bwd Init Win bytes          | The total number of bytes sent in initial window in the backward direction|
| Fwd Act Data Pkts           | Count of packets with at least 1 byte of TCP data payload in the forward direction|
| Fwd Seg Size Min            | Minimum segment size observed in the forward direction     |
| Active Min                  | Minimum time a flow was active before becoming idle         |
| Active Mean                 | Mean time a flow was active before becoming idle            |
| Active Max                  | Maximum time a flow was active before becoming idle         |
| Active Std                  | Standard deviation time a flow was active before becoming idle|
| Idle Min                    | Minimum time a flow was idle before becoming active         |
| Idle Mean                   | Mean time a flow was idle before becoming active            |
| Idle Max                    | Maximum time a flow was idle before becoming active         |                                             
| Idle Std                    | Standard deviation time a flow was idle before becoming active|



