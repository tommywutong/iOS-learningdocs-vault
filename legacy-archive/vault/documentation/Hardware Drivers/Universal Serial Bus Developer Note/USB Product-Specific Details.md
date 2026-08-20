---
title: Universal Serial Bus Developer Note
apple_id: TP40003026
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-04-28'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/HWTech_USB/Articles/usb_implementation.html
archived_at: '2026-07-15T07:41:02.748543Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Universal Serial Bus Developer Note](Introduction%20to%20Universal%20Serial%20Bus%20Developer%20Note.md)


[Next](Document%20Revision%20History.md)[Previous](USB%20Concepts.md)

# USB Product-Specific Details

This article highlights details of the USB implementation specific to particular Mac computers. Unless otherwise specified in this chapter, USB support on a Mac computer adheres to the information in [USB Concepts](USB%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsmbrfvjvomk7gezdambtgmytcnzz).

This section provides USB-specific information for Mac Pro computers introduced beginning August 2006. Refer to the specific Mac Pro developer note for additional information.

The Mac Pro computers with Quad-Core Intel Xeon 5400 Series microprocessors were introduced in January 2008. The Mac Pro has an internal USB 2.0 controller built into the South Bridge with one Enhanced Host Controller Interface (EHCI) and four Universal Host Controller Interfaces (UHCI). The controller supports five external USB ports and the optional Bluetooth module. Two ports are not used.

The eight USB ports comply with the Universal Serial Bus Specification 2.0. The USB register set complies with the EHCI and UHCI specifications.

Each external USB port supports 500 mA at 5 V for 2.5 W. Devices plugged into each port are expected to follow the USB standard for power limits and management.

A single high-powered Apple keyboard can be attached directly to the external ports, and software will enable one of its downstream ports to supply 500 mA of power. If a second high-powered Apple keyboard is attached, it will behave like a normal bus-powered hub and only provide 100 mA per downstream port.

If a device is added that exceeds the per-port current limit, the port will be disabled, but the other ports will continue to function. Unplug the device, and the disabled port will recover in a short amount of time without restarting the computer. USB port power is provided when the computer is on, or in sleep.

An EHCI controller provides USB 2.0 (up to 480 Mbps) and four UHCI controllers provide USB 1.1 (up to 12 Mbps) support to the eight ports. The Mac Pro South Bridge contains automatic port-routing logic that determines whether a USB port should be controlled by one of the UHCI controllers or by the EHCI controller.

|  |  |
| --- | --- |
| UHCI Controller 0 | front panel port: one and two (Port0, Port1) |
| UHCI Controller 1 | rear panel port: middle and lower (Port2, Port3) |
| UHCI Controller 2 | rear panel port: top and Bluetooth (Port4, Port5) |
| UHCI Controller 3 | not used |

The quad-core Mac Pro was introduced in August 2006 and the 8-core Mac Pro was introduced in April 2007 as a configure-to-order-option. The Mac Pro has an internal USB 2.0 controller built into the South Bridge with one Enhanced Host Controller Interface (EHCI) and four Universal Host Controller Interfaces (UHCI). The controller supports five external USB ports and the optional Bluetooth module. Two ports are not used.

The eight USB ports comply with the Universal Serial Bus Specification 2.0. The USB register set complies with the EHCI and UHCI specifications.

The USB ports support 500 mA at 5 V for 2.5 W power per port.

Four UHCI controllers feed the eight USB ports. Each UHCI controller runs 480 Mbps shared among two ports. The four UHCI controllers service the ports as described below. A triple-stack USB connector on the rear I/O is referenced by top, middle, and lower panel port.

|  |  |
| --- | --- |
| UHCI Controller 0 | front panel port: one and two (Port0, Port1) |
| UHCI Controller 1 | rear panel port: middle and lower (Port2, Port3) |
| UHCI Controller 2 | rear panel port: top and Bluetooth (Port4, Port5) |
| UHCI Controller 3 | not used |

This section provides information on Xserve servers introduced after September 2005. Refer to the specific Xserve developer note for additional information.

The Xserve with Quad-Core Intel Xeon 5400 Series microprocessors, introduced in January 2008, has an internal USB 2.0 controller built into the South Bridge. USB devices are internally routed to the controller. High-speed USB devices are accessed via the Enhanced Host Controller Interface (EHCI) and full-speed and low-speed devices are accessed via the Universal Host Controller Interface (UHCI). The two external USB ports located rear and the one external USB port in the front are routed to the same EHCI controller, sharing the 480 Mbps available bandwidth between them.

Each external USB port supports 500 mA at 5 V for 2.5 W. Devices attached to these ports must follow the USB standard for power consumption limits and management.

A single high-powered Apple keyboard can be attached directly to the external ports, and software will enable one of its downstream ports to supply 500 mA of power. If a second high-powered Apple keyboard is attached, it will behave like a normal bus-powered hub and only provide 100 mA per downstream port.

The USB ports comply with the Universal Serial Bus Specification 2.0. The USB register set complies with the EHCI and UHCI specifications.

The Xserve introduced in August 2006, based on the Dual-Core Intel Xeon processor, has an internal USB 2.0 controller built into the South Bridge. USB devices are internally routed to the controller. USB 2.0 devices are routed via the Enhanced Host Controller Interface (EHCI) and USB 1.1 devices are routed via the Universal Host Controller Interface (UHCI). The UHCI controller runs 480 Mbps shared between two ports.

The USB ports comply with the Universal Serial Bus Specification 2.0. The USB register set complies with the EHCI and UHCI specifications.

The USB ports support 500 mA at 5 V for 2.5 W power per port.

This section provides information on iMac computers introduced after September 2005. Refer to the specific iMac developer note for additional information.

The iMac computers introduced in April 2008, based on the Intel Core 2 Duo processor on 45 nm process technology, have multiple internal USB 2.0 controllers built into the South Bridge. The controllers support three external USB ports, the built-in iSight camera, Bluetooth +EDR, and the IR receiver. Four ports are not used.

The external USB ports comply with the Universal Serial Bus Specification 2.0. High-speed USB devices are accessed via the Enhanced Host Controller Interface (EHCI) and full-speed and low-speed devices are accessed via the Universal Host Controller Interface (UHCI).

A single high-powered device can be attached directly to the external ports, and software will enable one of its downstream ports to supply 500 mA of power. If a second high-powered device is attached, it will behave like a normal bus-powered hub and only provide 100 mA per downstream port.

The iMac Computers introduced in August 2007, based on the Intel Core 2 Duo microprocessor, has multiple internal USB 2.0 controllers built into the South Bridge. The controllers support three external USB ports, the built-in iSight camera, Bluetooth +EDR, and the IR receiver. Four ports are not used.

The external USB ports comply with the Universal Serial Bus Specification 2.0. High-speed USB devices are accessed via the Enhanced Host Controller Interface (EHCI) and full-speed and low-speed devices are accessed via the Universal Host Controller Interface (UHCI).

A single high-powered Apple keyboard can be attached directly to the external ports, and software will enable one of its downstream ports to supply 500 mA of power. If a second high-powered Apple keyboard is attached, it will behave like a normal bus-powered hub and only provide 100 mA per downstream port.

The iMac with SuperDrive computers introduced in September 2006, based on the Intel Core 2 Duo microprocessor, have an internal USB 2.0 controller built into the South Bridge with one Enhanced Host Controller Interface (EHCI) and four Universal Host Controller Interfaces (UHCI). The controller has a total of eight ports, seven of which are available to support the three external USB ports, the built-in iSight camera, Bluetooth +EDR, and the IR receiver. Two ports are not used.

The eight USB ports comply with the Universal Serial Bus Specification 2.0. The USB register set complies with the EHCI and UHCI specifications.

The iMac with Combo drive computer introduced in September 2006, based on the Intel Core 2 Duo microprocessor, has an internal USB 2.0 controller built into the South Bridge with one Enhanced Host Controller Interface (EHCI) and four Universal Host Controller Interfaces (UHCI). The controller has a total of eight ports, six of which are available to support the three external USB ports, the built-in iSight camera, and the IR receiver. Three ports are not used.

The eight USB ports comply with the Universal Serial Bus Specification 2.0. The USB register set complies with the EHCI and UHCI specifications.

The 17-inch iMac for education computer introduced in July 2006, based on the Intel Core Duo microprocessor, has an internal USB 2.0 controller built into the South Bridge with one Enhanced Host Controller Interface (EHCI) and four Universal Host Controller Interfaces (UHCI). The controller has a total of eight ports, five of which are available to support the three external USB ports, the built-in iSight camera, and the IR receiver. Three ports are not used.

The eight USB ports comply with the Universal Serial Bus Specification 2.0. The USB register set complies with the EHCI and UHCI specifications.

The iMac computers introduced in January 2006, based on the Intel Core Duo microprocessor, have an internal USB 2.0 controller built into the South Bridge with one Enhanced Host Controller Interface (EHCI) and four Universal Host Controller Interfaces (UHCI). The controller has a total of eight ports, seven of which are available to support the three external USB ports, the built-in iSight camera, the Bluetooth module, the IR receiver, and the internal communications connector. The eighth port is not used.

The eight USB ports comply with the Universal Serial Bus Specification 2.0. The USB register set complies with the EHCI and UHCI specifications.

The iMac G5 has three external USB 2.0 ports on the enclosure. An internal connection supports the Bluetooth module and a USB2 hub that supports the built-in iSight camera and the IR receiver. The external USB 2.0 ports are off of the USB controller connected to the PCI bus, bridged by the Shasta ASIC. 

The three external USB ports on the iMac G5 are fully compliant with the USB 2.0 specification, including support for high-speed (480 Mbps) devices using an Enhanced Host Controller Interface (EHCI) that complies with the EHCI specification. Ports are automatically routed to a companion OHCI controller (that complies with the OHCI specification) when a classic-speed (full-speed or low-speed) USB device is attached to a root hub port.

The two USB 1.1 ports on the keyboard comply with the Universal Serial Bus Specification 1.1 Final Draft Revision. 

The iMac G5 provides 5-volt power to the USB 2.0 ports. The maximum current available is 500 mA on each port.

The Shasta ASIC contains special circuitry that allows the computer to wake from sleep mode on connect, disconnect, and resume events. Compatible USB devices should support the USB-suspend mode defined in the USB specification.

USB devices can provide a remote wakeup function for the computer. The USB root hub in the computer is set to support remote wakeup whenever a device is attached to or disconnected from the bus. The Apple remote and keyboard that come with the computer use this method to wake the computer at the press of a button or key.

This section provides information on MacBook computers. Refer to the specific MacBook developer note for additional information.

The MacBook computer introduced in February 2008, incorporating the Intel Core 2 Duo processor on 45 nm process technology, has multiple internal USB 2.0 controllers built into the South Bridge. The controllers support two external USB ports (one available for high-powered devices), the Bluetooth module, the IR receiver, the built-in iSight camera, and the internal keyboard/trackpad. Four ports are not used.

The external USB ports comply with the Universal Serial Bus Specification 2.0. High-speed USB devices are accessed via the Enhanced Host Controller Interface (EHCI) and full-speed and low-speed devices are accessed via the Universal Host Controller Interface (UHCI).

The USB ports support 500 A at 5 V for 2.5 W power per port.

A single high-powered device can be attached directly to the external ports, and software will enable one of its downstream ports to supply 500 mA of power. If a second high-powered device is attached, it will behave like a normal bus-powered hub and only provide 100 mA per downstream port.

The MacBook computer introduced in November 2007, based on the Intel Core 2 Duo, has multiple internal USB 2.0 controllers built into the South Bridge. The controllers support two external USB ports, the Bluetooth module, the IR receiver, the built-in iSight camera, and the internal keyboard/trackpad. Four ports are not used.

The external USB ports comply with the Universal Serial Bus Specification 2.0. High-speed USB devices are accessed via the Enhanced Host Controller Interface (EHCI) and full-speed and low-speed devices are accessed via the Universal Host Controller Interface (UHCI).

The USB ports support 500 A at 5 V for 2.5 W power per port.

A single high-powered Apple keyboard can be attached directly to the external ports, and software will enable one of its downstream ports to supply 500 mA of power. If a second high-powered Apple keyboard is attached, it will behave like a normal bus-powered hub and only provide 100 mA per downstream port.

The MacBook computer introduced in May 2007, based on the Intel Core 2 Duo, has an internal USB 2.0 controller built into the South Bridge with one Enhanced Host Controller Interface (EHCI) and four Universal Host Controller Interfaces (UHCI). The controller has a total of eight ports, six of which are available to support two external USB ports, the Bluetooth module, the IR receiver, and the built-in iSight camera, and the internal keyboard/trackpad. Two ports are not used.

The eight USB ports comply with the Universal Serial Bus Specification 2.0. The USB register set complies with the EHCI and UHCI specifications.

The USB ports support 500 mA at 5 V for 2.5 W power per port.

The MacBook computer introduced in November 2006, based on the Intel Core 2 Duo, has an internal USB 2.0 controller built into the South Bridge with one Enhanced Host Controller Interface (EHCI) and four Universal Host Controller Interfaces (UHCI). The controller has a total of eight ports, six of which are available to support two external USB ports, the Bluetooth module, the IR receiver, and the built-in iSight camera, and the internal keyboard/trackpad. Two ports are not used.

The eight USB ports comply with the Universal Serial Bus Specification 2.0. The USB register set complies with the EHCI and UHCI specifications.

The MacBook computer introduced in May 2006, based on the Intel Core Duo, has an internal USB 2.0 controller built into the South Bridge with one Enhanced Host Controller Interface (EHCI) and four Universal Host Controller Interfaces (UHCI). The controller has a total of eight ports, six of which are available to support two external USB ports, the Bluetooth module, the IR receiver, and the built-in iSight camera, and the internal keyboard/trackpad. Two ports are not used.

The eight USB ports comply with the Universal Serial Bus Specification 2.0. The USB register set complies with the EHCI and UHCI specifications.

This section provides information on MacBook Pro computers. Refer to the specific MacBook Pro developer note for additional information.

The 17-inch MacBook Pro computers introduced in February 2008, incorporating the Intel Core 2 Duo processor on 45 nm process technology, have multiple internal USB 2.0 controllers built into the South Bridge. The controllers support three external USB ports (one available for high-powered devices), the Bluetooth module, the IR receiver, the built-in iSight camera, the internal keyboard/trackpad, and the ExpressCard/34 interface. Two ports are not used.

The external USB ports comply with the Universal Serial Bus Specification 2.0. High-speed USB devices are accessed via the Enhanced Host Controller Interface (EHCI) and full-speed and low-speed devices are accessed via the Universal Host Controller Interface (UHCI).

The USB ports support 1.1 A at 5 V nominal for 2.5 W power per port and are compliant with the the Voltage Drop Budget section of the Universal Serial Bus Specification 2.0.

A single high-powered device can be attached directly to an external port, and software will enable one of its downstream ports to supply 500 mA of power. If a second high-powered device is attached, it will behave like a normal bus-powered hub and only provide 100 mA per downstream port.

The 15-inch MacBook Pro computers introduced in February 2008, incorporating the Intel Core 2 Duo processor on 45 nm process technology, have multiple internal USB 2.0 controllers built into the South Bridge. The controllers support two external USB ports (one available for high-powered devices), the Bluetooth module, the IR receiver, the built-in iSight camera, the internal keyboard/trackpad, and the ExpressCard/34 interface. Three ports are not used.

The external USB ports comply with the Universal Serial Bus Specification 2.0. High-speed USB devices are accessed via the Enhanced Host Controller Interface (EHCI) and full-speed and low-speed devices are accessed via the Universal Host Controller Interface (UHCI).

The USB ports support 1.1 A at 5 V nominal for 2.5 W power per port and are compliant with the Voltage Drop Budget section of the Universal Serial Bus Specification 2.0.

A single high-powered device can be attached directly to an external port, and software will enable one of its downstream ports to supply 500 mA of power. If a second high-powered device is attached, it will behave like a normal bus-powered hub and only provide 100 mA per downstream port.

The 17-inch MacBook Pro computers introduced in June 2007 and November 2007, based on the Intel Core 2 Duo, have multiple internal USB 2.0 controllers built into the South Bridge. The controllers support three external, high-powered USB ports, the Bluetooth module, the IR receiver, the built-in iSight camera, the internal keyboard/trackpad, and the ExpressCard/34 interface. Two ports are not used.

The external USB ports comply with the Universal Serial Bus Specification 2.0. High-speed USB devices are accessed via the Enhanced Host Controller Interface (EHCI) and full-speed and low-speed devices are accessed via the Universal Host Controller Interface (UHCI).

The USB ports support 1.1 A at 5 V nominal for 2.5 W power per port and are compliant with the the Voltage Drop Budget section of the Universal Serial Bus Specification 2.0.

A single high-powered Apple keyboard can be attached directly to the external ports, and software will enable one of its downstream ports to supply 500 mA of power. If a second high-powered Apple keyboard is attached, it will behave like a normal bus-powered hub and only provide 100 mA per downstream port.

The 15-inch MacBook Pro computers introduced in June 2007 and November 2007, based on the Intel Core 2 Duo, have multiple internal USB 2.0 controllers built into the South Bridge. The controllers supports two external high-powered USB ports, the Bluetooth module, the IR receiver, the built-in iSight camera, the internal keyboard/trackpad, and the ExpressCard/34 interface. Three ports are not used.

The external USB ports comply with the Universal Serial Bus Specification 2.0. High-speed USB devices are accessed via the Enhanced Host Controller Interface (EHCI) and full-speed and low-speed devices are accessed via the Universal Host Controller Interface (UHCI).

The USB ports support 1.1 A at 5 V nominal for 2.5 W power per port and are compliant with the the Voltage Drop Budget section of the Universal Serial Bus Specification 2.0.

A single high-powered Apple keyboard can be attached directly to the external ports, and software will enable one of its downstream ports to supply 500 mA of power. If a second high-powered Apple keyboard is attached, it will behave like a normal bus-powered hub and only provide 100 mA per downstream port.

The 17-inch MacBook Pro computer introduced in October 2006, based on the Intel Core 2 Duo, has an internal USB 2.0 controller built into the South Bridge with one Enhanced Host Controller Interface (EHCI) and four Universal Host Controller Interfaces (UHCI). The controller has a total of eight ports to support three external USB ports, the Bluetooth module, the IR receiver, the built-in iSight camera, the internal keyboard/trackpad, and the ExpressCard/34 interface.

The eight USB ports comply with the Universal Serial Bus Specification 2.0. The USB register set complies with the EHCI and UHCI specifications.

The 15-inch MacBook Pro computer introduced in October 2006, based on the Intel Core 2 Duo, has an internal USB 2.0 controller built into the South Bridge with one Enhanced Host Controller Interface (EHCI) and four Universal Host Controller Interfaces (UHCI). The controller has a total of eight ports, five of which are available to support two external USB ports, the Bluetooth module, the IR receiver, and the built-in iSight camera. The other three ports are used for the internal keyboard/trackpad, the ExpressCard/34 interface, and one is not used.

The eight USB ports comply with the Universal Serial Bus Specification 2.0. The USB register set complies with the EHCI and UHCI specifications.

The 17-inch MacBook Pro computer introduced in April 2006, based on the Intel Core Duo microprocessor, has an internal USB 2.0 controller built into the South Bridge with one Enhanced Host Controller Interface (EHCI) and four Universal Host Controller Interfaces (UHCI). The controller has a total of eight ports to support three external USB ports, the Bluetooth module, the IR receiver, the built-in iSight camera, the internal keyboard/trackpad, and the ExpressCard/34 interface.

The eight USB ports comply with the Universal Serial Bus Specification 2.0. The USB register set complies with the EHCI and UHCI specifications.

The 15-inch MacBook Pro computer introduced in January 2006, based on the Intel Core Duo microprocessor, has an internal USB 2.0 controller built into the South Bridge with one Enhanced Host Controller Interface (EHCI) and four Universal Host Controller Interfaces (UHCI). The controller has a total of eight ports, five of which are available to support two external USB ports, the Bluetooth module, the IR receiver, and the built-in iSight camera. The other three ports are used for the internal keyboard/trackpad, the ExpressCard/34 interface, and the internal communication connector.

The eight USB ports comply with the Universal Serial Bus Specification 2.0. The USB register set complies with the EHCI and UHCI specifications.

This section provides USB-specific information for MacBook Air computers. Refer to the specific MacBook Air developer note for additional information. The controllers support the Bluetooth module, the IR receiver, the built-in iSight camera, the internal Keyboard/trackpad, and one external USB port.

The MacBook Air computer introduced in January 2008, based on the Intel Core 2 Duo, has multiple internal USB controllers built into the South Bridge.

The external USB port supports 500 mA at 5 V for 2.5 W.

The external USB port complies with the Universal Serial Bus Specification 2.0. High-speed USB devices are accessed via the Enhanced Host Controller Interface (EHCI) and full-speed and low-speed devices are accessed via the Universal Host Controller Interface (UHCI).

A high-powered Apple keyboard can be attached directly to the external port, and software will enable one of its downstream ports to supply 500 mA of power. The external port also supports the External MacBook Air SuperDrive when it is directly attached.

This section provides information on Mac mini computers. Refer to the specific Mac mini developer note for additional information.

The Mac mini computer introduced in February 2006, based on the Intel Core Duo microprocessor or Intel Core Solo microprocessor, has an internal USB 2.0 controller built into the South Bridge with one Enhanced Host Controller Interface (EHCI) and four Universal Host Controller Interfaces (UHCI). The controller has a total of eight ports, six of which are available to support four external USB ports, the Bluetooth module, and the IR receiver. The other two ports are used for the internal communication connector.

The eight USB ports comply with the Universal Serial Bus Specification 2.0. The USB register set complies with the EHCI and UHCI specifications.

This section provides information on Power Mac computers introduced after September 2005. Refer to the specific Power Mac developer note for additional information.

The Power Mac G5 computer has three external Universal Serial Bus (USB) 2.0 ports on the back and one on the front of the enclosure, providing support for high-speed (480 Mbps) devices using an Enhanced Host Controller Interface (EHCI). Ports are automatically routed to a companion OHCI controller (that complies with the OHCI specification) when a classic-speed (full-speed or low-speed) USB device is attached to a root hub port.

The external USB ports are off of the USB 2.0 controller connected to the PCI bus, bridged by the South Bridge IC. In addition, there are two USB 1.1 ports on the keyboard, which are used for connecting the mouse as well as additional I/O devices such as printers, scanners, and storage devices.

The Power Mac G5 computer provides 5 V power for the USB ports and up to 500 mA on each port. The power is provided in both run and sleep mode. The ports share the same power supply; a short circuit on one disables all ports until the short has been removed.

[Next](Document%20Revision%20History.md)[Previous](USB%20Concepts.md)

