---
title: Cellular Best Practices Guide
apple_id: TP40013998
resource_type: Guide
platform: iOS
topic: Performance
technology: null
published: '2014-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CellularBestPractices/CellularProcessors/CellularProcessors.html
archived_at: '2026-07-18T01:46:23.145930Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cellular Best Practices Guide](About%20Creating%20Efficient%20Cellular%20Apps.md)


[Next](Best%20Practices%20for%20Developing%20Cellular%20Apps.md)[Previous](About%20Creating%20Efficient%20Cellular%20Apps.md)

# Cellular Processors: Interface to the Cellular Network

Wi-Fi and Ethernet technologies are similar, and apps can run on either interchangeably. This is not true for cellular networks, where data transfer has different requirements. Whereas Wi-Fi connectivity is relatively inexpensive, the cost per byte of the same data transmitted over a cellular connection can be quite costly—for the carrier as well as the user. Cellular networks are quite complex in how they acquire and use radio (airwave/spectrum) resources. That complexity is expensive for the carrier and they pass those expenses on to the user.

On most mobile devices, apps can use multiple forms of connectivity, each carrying different expenses. Yet the transition from one to the other is often outside of the users’ awareness. In addition, to manage cellular connections, the device itself usually has multiple cellular data modes with different data rates and different power usage, also invisible to the user.

When a mobile device user out of Wi-Fi range opens an Internet app, it typically takes the exchange of eight to ten cellular network messages (depending on the protocol) before a single byte of data is transmitted. This is far more overhead than in a typical Ethernet/Wi-Fi LAN exchange and it is the principal reason that apps designed for Ethernet and Wi-Fi are often not as efficient when used over a cellular interface.

Typically, a device has both an application processor and a cellular processor, which each operate in different power states and data states, as shown in Figure 2-1.

__Figure 2-1__  Power and data states of a cellular device’s processors

!

The cellular processor typically has three different “on” states, as shown here; some protocols have four. The states are defined by the power consumed and the data rates. There may be a “zero state” for an established but idle connection with no data being transmitted. Processors use higher power states to send larger amounts of data. The choice of state and the decision to change state is automatically negotiated with the cellular network.

The cellular processor communicates with the cellular network in two different planes: the _control plane_, which manages the communication protocol, and the _data plane_, which carries the actual data packets.

To provide good user performance, cellular network providers attempt to deploy a network that will never have its capacity exceeded while keeping costs reasonable. Yet they can be vulnerable to the behavior of apps over which they have no control. Many apps are designed with features that, intentionally or not, push the boundaries of the networks. As a result, carriers often need to restrict app behavior to keep them within the limitations of the networks. For example, a carrier could limit the number of connections that an app triggers, especially in the control plane.

Apps may also be restricted by the device manufacturers. For example, devices can restrict an app’s use of memory, processing, or battery resources.

[Next](Best%20Practices%20for%20Developing%20Cellular%20Apps.md)[Previous](About%20Creating%20Efficient%20Cellular%20Apps.md)

