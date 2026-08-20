---
title: Bluetooth Developer Note
apple_id: TP40003032
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-04-28'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/HWTech_Bluetooth/Articles/BluToo_concepts.html
archived_at: '2026-07-15T07:40:58.667770Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Bluetooth Developer Note](Introduction%20to%20Bluetooth%20Developer%20Note.md)


[Next](Bluetooth%20Product-Specific%20Details.md)[Previous](Introduction%20to%20Bluetooth%20Developer%20Note.md)

# Bluetooth Concepts

This article provides an overview of Bluetooth technology, specifically as it is implemented in Macintosh computers.

Bluetooth is the common name for the technology described by the IEEE standard 802.15 for short-range wireless connections between desktop and notebook computers, handhelds, personal digital assistants, mobile phones, camera phones, printers, digital cameras, headsets, keyboards, mice, and other devices. Bluetooth uses a globally available frequency band (2.4 GHz) for worldwide compatibility. Considered an alternative to the IrDA (Infrared Data Association) standard, it is commonly used to connect devices within a 30-foot range at transfer rates less than 1 Mbps. Its features include the following:

- __Low cost:__ Bluetooth peripherals are typically just slightly more expensive than their USB counterparts.
- __Low power:__ 1 milliwatt power output, by default.
- __Flexibility:__ RF technology frees Bluetooth peripherals from the short distance and line-of-sight constraints imposed by IrDA.

These features of Bluetooth have given rise to the concept of a personal area network (PAN), a small flexible area in which the user can move while retaining connectivity to other Bluetooth devices.

Bluetooth is designed for low-bandwidth data transfer, so it is an effective alternative to USB for low-speed, low-bandwidth peripherals. It is not intended as a replacement for high-bandwidth connection technologies, whether wireless, such as Airport (IEEE 802.11), or cabled, such as Ethernet or FireWire (IEEE 1394).

Bluetooth is designed so that devices can communicate in ad hoc fashion with other Bluetooth devices over connections called _links_ within one or more logical groups called _piconets_. Each device includes a Bluetooth _core system_, comprising three layers:

- __Radio layer:__ consists of a radio frequency transceiver that performs RF communications using a frequency-hopping spread spectrum (FHSS) pattern in the industrial, scientific, and medical (ISM) band (2.4 GHz). Bluetooth 2.0 uses a 79-hop pattern exclusively, having eliminated the 23-hop restriction formerly imposed to address band range uses in certain countries.
- __Baseband/link controller layer:__ provides facilities for device discovery, connection establishment, device synchronization, error correction, and some security enforcement.
- __Link manager layer:__ manages creation, configuration, and maintenance of links; switching of power modes; and authentication.

Beyond the core system are the Logical Link Control and Adaptation Protocol (L2CAP) and the application layer. The L2CAP manages application access to links, packet segmentation and reassembly, and quality-of-service requests. Applications can interact with the L2CAP directly or through support protocols such as the Radio Frequency Communications (RFCOMM) protocol, the Telephony Control Specification (TCS) protocol, and the Service Discovery Protocol (SDP). In the case of adapter modules, a host controller interface is required between the core system and the L2CAP layer.

The mobile nature of Bluetooth devices requires a novel approach to networking. Moving a device among different communication environments offers many possible benefits, but significantly increases network management requirements.

A piconet consists of two or more Bluetooth devices connected over a common link. There are two types of links:

- _Synchronous Connection-Oriented (SCO)_, for isochronous and voice communication using, for example, headsets
- _Asynchronous Connectionless (ACL)_, for data communication, such as keyboard input

In each piconet, one device, typically the one that initiated the connection, is considered the master of that piconet. The master manages the links in the piconet. As many as seven additional devices can be active in the piconet, but many more can be connected but inactive. Within that piconet, these additional devices each can communicate with only the master; to communicate with each other, they must form a separate piconet.

Consider the connection possibilities that might exist among multiple devices within Bluetooth networking range of each other:

- All connected in a single piconet
- Discrete groups connected in separate piconets
- One or more discrete devices connected each to multiple piconets

In this last case, each set of overlapping piconets is referred to as a _scatternet_. An example of a scatternet would be a piconet that included a shared device such as a printer used by multiple computers in piconets exclusive of each other.

Apple's Bluetooth support is based on the Bluetooth Special Interest Group (SIG) specification. In April, 2002, Apple introduced a Bluetooth USB adapter and Bluetooth functionality in Mac OS X version 10.1.3, making Bluetooth available for all Macintosh computers shipping at that time. Now, built-in Bluetooth support is available in computers in every Apple CPU product line except Xserve servers.

Apple also provides some high-level bridges between Mac OS X functionality and the Bluetooth protocol stack. This means that many Bluetooth devices work transparently with computers running Mac OS X version 10.2 and later. The Mac OS X HID Manager, for example, handles a Bluetooth mouse just as it does a cabled mouse. In many cases, such high-level bridges allow applications to communicate with Bluetooth devices without including any Bluetooth-specific code.

To improve interoperation between devices, Bluetooth defines profiles to enforce uniformity across similar devices, features, and combinations of features. Profiles are hierarchical; at the bottom of the hierarchy is the generic access profile (GAP), which mandates UI terminology, specifies the minimum set of features, and defines how a device discovers other devices and participates in establishing a link. All other profiles build on the features of the GAP. For more information on profiles supported by Mac OS X, see _[Bluetooth Device Access Guide](../../Device%20Drivers/Bluetooth%20Device%20Access%20Guide/Introduction%20to%20Bluetooth%20Device%20Access%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojx)_.

Support for Bluetooth versions 1.1 and 1.2 support is built into Mac OS X version 10.2 and later, and it is available on older computers across Apple's entire CPU product line (except Xserve servers) either built-in or as an option.

Bluetooth 2.0 + EDR (enhanced data rate) support is built into Mac OS X version 10.3 and later, and it is available on currently shipping computers across Apple's entire CPU product line (except Xserve servers) either built-in or as an option.

This version is is backward-compatible with Bluetooth versions 1.1 and 1.2 and adds enhanced data rate (EDR) capability of 3.0 Mbps, three times as fast as with version 1.2. Other improvements include lower overall power consumption (as a result of a reduced duty cycle), extended battery life in portable devices, more efficient transfers of large files, and reduced bit error rates (BERs).

[Next](Bluetooth%20Product-Specific%20Details.md)[Previous](Introduction%20to%20Bluetooth%20Developer%20Note.md)

