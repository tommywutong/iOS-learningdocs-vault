---
title: Ethernet Developer Note
apple_id: TP40003029
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-04-28'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/HWTech_Ethernet/Articles/ENet_concepts.html
archived_at: '2026-07-15T07:40:58.718069Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Ethernet Developer Note](Introduction%20to%20Ethernet%20Developer%20Note.md)


[Next](Ethernet%20Product-Specific%20Details.md)[Previous](Introduction%20to%20Ethernet%20Developer%20Note.md)

# Ethernet Concepts

This article describes Apple's implementation of the common Ethernet standards and provides details of the hardware Ethernet ports on Macintosh computers. A detailed description of Ethernet is beyond the scope of this note.

Ethernet is the most widely accepted and adopted LAN architecture, and is available for all but the earliest models of Macintosh computers. Originally defined by an independent specification in 1980, Ethernet was first officially standardized by the IEEE 802.3 specification in 1985. Three main versions, often identified by their data rates, are in common use today with currently available cable technologies:

- Ethernet (10 Mbps)
- Fast Ethernet (100 Mbps)
- Gigabit Ethernet (1000 Mbps)

An Ethernet LAN consists of network nodes—data terminal equipment (DTE) or data communication equipment (DCE) devices—and the cables that connect them. DTEs are endpoint devices such as computers and printers, and DCEs are transmission devices such as routers, hubs, and switches. The simplest Ethernet LAN consists of two Ethernet-capable computers connected by a cable. However, aside from a few such exceptions, Ethernet LANs use a star topology, with multiple DTEs connected to a central DCE. Two or more central LAN hubs or switches connected via uplink to another hub or switch or to a router form what is often called an intranet, especially if the LANs in question are behind the same firewall. If the LANs are geographically distant, they combine to form a wide area network (WAN). The Internet is a WAN with which most of us familiar.

Ethernet implements the lowest two layers of the seven-layer Open System Interconnection (OSI) protocol stack model from the International Organization for Standardization (ISO).

Ethernet conforms to the IEEE specification 802.3 for the OSI Physical layer (layer 1), covering the following elements:

- The physical transmission medium, or cable
- The medium-dependent interface, or cable connector
- The medium attachment function, for signal transmission and reception
- The physical coding function, for handling data stream processes such as synchronization, encoding/decoding, and multiplexing/demultiplexing
- The auto-negotiation function, for establishing the optimal communication mode for the link, as required for 100BASE-T2 and 1000BASE-T

The names associated with specific physical layer implementations indicate the theoretical maximum data transmission rate and the cable characteristics, as shown in Table 1.

__Table 1__  Common Ethernet physical layer implementations

| Name | Nominal transmission rate | Cable characteristics |
| 10BASE-T | 10 Mbps | 2 pairs, UTP Cat 3 or higher |
| 100BASE-T2 | 100 Mbps | 2 pairs, UTP Cat 3 or higher) |
| 100BASE-T4 | 100 Mbps | 4 pairs, UTP Cat 3 or higher |
| 1000BASE-T | 1000 Mbps | 4 pairs, UTP Cat 5 or higher |
| 1000BASE-X | 1000 Mbps | 2 pairs, STP copper or  2 strands optical fiber |

Ethernet conforms to the IEEE specifications 802.1 and 802.2 for the OSI data link layer (layer 2), covering the following elements:

- Logical link control (LLC) in a DTE device, providing the interface between the media access controller (MAC) and the higher OSI protocol layers
- Bridging in a DCE device, providing the interface to another DCE device
- Data frame assembly and parsing
- Data frame transmission
- Error detection
- Error recovery

A standard frame format is specified for data representation at the LLC layer, with the following fields in descending order transmitted in bit-serial fashion from left to right:

- Preamble (7 bytes): alternating 1-bits and 0-bits to allow synchronization at the destination
- Start frame delimiter (1 byte): the bit sequence 10101011, indicating that the frame follows immediately
- Destination address (6 bytes): the MAC address of a single DTE device (a _unicast_ address), or a _multicast_ address specifying a group of DTE devices
- Source address (6 bytes): the MAC address of the DTE device from which the frame originates
- Length (or type) value (2 bytes): if 1500 or less, the number of bytes in the data field; if l536 or greater, the optional frame format type identifier
- Data/padding: (46 to 1500 bytes): if 45 or fewer bytes of data, the actual data padded to 46 bytes; otherwise up to 1500 bytes of data
- Frame check sequence: (4 bytes): a cyclic redundancy check (CRC) value based on the frame content (exclusive of the preamble, the start frame delimiter, and the frame check sequence field itself)

For 10BASE-T and 100BASE-T, transmission is half-duplex, using the Carrier Sense Multiple Access/Collision Detection (CSMA/CD) contention protocol to manage data transmission and to detect and respond to transmission collisions. In this model, each node monitors the traffic on its link. Any time any node determines there is no traffic, it can transmit a frame. Simultaneous transmissions will collide, rendering the signals garbled. When a transmitting node detects the collision, it waits for a period determined by a backoff algorithm, then restarts the frame transmission.

For 1000BASE-T, the speed limitations of CSMA/CD have been overcome by using:

- A PHY modeled after that of Fibre Channel
- 8B/10B block coding
- Full-duplex signal transmission
- Data flow control

Apple started offering built-in 10BASE-T Ethernet support on 68040 Macintosh computers, and 100BASE-T support on Power Macintosh G3 computers.

In July of 2000, Apple introduced its first products with Gigabit Ethernet built-in on the motherboard. Gigabit Ethernet is now available on computers in Apple's iMac, Power Mac, Xserve, PowerBook, and MacBook Pro product lines.

The Ethernet interface in Ethernet-capable Macintosh computers conforms to the ISO/IEC 802.3 specification, where applicable, and complies with IEEE specifications 802.3i (10BASE-T/UTP), 802.3u-1995 (100BASE-T), and 802.3ab (1000BASE-T).

The Ethernet port on all current Macintosh computers uses an RJ-45 connector. Connections using 1000BASE-T operation require 4-pair cable (Category 5 or 6).

Table 2 shows the signals and pin assignments for 10Base-T and 100BASE-T operation. Table 3 shows the signals and pin assignments for 1000BASE-T operation.

__Table 2__  Signals for 10BASE-T and 100BASE-T operation

| Pin | Signal name | Signal definition |
| 1 | TXP | Transmit (positive lead) |
| 2 | TXN | Transmit (negative lead) |
| 3 | RXP | Receive (positive lead) |
| 4 | – | Not used |
| 5 | – | Not used |
| 6 | RXN | Receive (negative lead) |
| 7 | – | Not used |
| 8 | – | Not used |

__Table 3__  Signals for 1000BASE-T Gigabit operation

| Pin | Signal name | Signal definition |
| 1 | TRD+(0) | Transmit and receive data 0 (positive lead) |
| 2 | TRD–(0) | Transmit and receive data 0 (negative lead) |
| 3 | TRD+(1) | Transmit and receive data 1 (positive lead) |
| 4 | TRD+(2) | Transmit and receive data 2 (positive lead) |
| 5 | TRD–(2) | Transmit and receive data 2 (negative lead) |
| 6 | TRD–(1) | Transmit and receive data 1 (negative lead) |
| 7 | TRD+(3) | Transmit and receive data 3 (positive lead) |
| 8 | TRD–(3) | Transmit and receive data 3 (negative lead) |

[Next](Ethernet%20Product-Specific%20Details.md)[Previous](Introduction%20to%20Ethernet%20Developer%20Note.md)

