---
title: FireWire Developer Note
apple_id: TP40003028
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-04-28'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/HWTech_FireWire/Articles/FireW_implementation.html
archived_at: '2026-07-15T07:40:59.589140Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [FireWire Developer Note](Introduction%20to%20FireWire%20Developer%20Note.md)


[Next](Document%20Revision%20History.md)[Previous](FireWire%20Concepts.md)

# FireWire Product-Specific Details

This article highlights details of the FireWire implementation specific to particular Mac computers. Unless otherwise specified in this article, FireWire support on a specific Mac computer adheres to the information in [FireWire Concepts](FireWire%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztqojtfvjvomk7gezdambtgmytcnzt).

This section provides FireWire-specific information for Mac Pro computers introduced beginning August 2006. Refer to the specific Mac Pro developer note for additional information.

The Mac Pro computers with Quad-Core Intel Xeon 5400 Series microprocessors were introduced in January 2008. The Mac Pro provides two FireWire 800 IEEE 1394b ports and two FireWire 400 IEEE 1394a ports. The four FireWire ports are on the same FireWire bus and share a single 12V DC-regulated power supply that can provide 18 W per port, for up to 28 W total. If a device is added that exceeds the power limit, the port will be disabled but the other ports will continue to function. Unplug the device, and the disabled port will recover in a short amount of time. FireWire port power is provided when the computer is on, in sleep, or off.

The Open Host Controller Interface (OHCI) connects to the South Bridge IC via a PCI Express 1-lane 2.5 GHz bus. The front and rear FireWire PHYs interface via the OHCI.

The Mac Pro provides front and rear port repeating when the computer is powered on or asleep. Front and rear repeating is also available when the computer is off, unless the computer was shut down from Mac OS X with no FireWire devices connected.

The quad-core Mac Pro was introduced in August 2006 and the 8-core Mac Pro was introduced in April 2007 as a configure-to-order-option. The Mac Pro provides two FireWire 800 IEEE 1394b ports and two FireWire 400 IEEE 1394a ports. The four FireWire ports are on the same FireWire bus and share a single power supply that can provide 7 W per port, up to 28 watts total. The FireWire 800 and FireWire 400 ports provide a regulated power of approximately 12 VDC.

The Open Host Controller Interface (OHCI) connects to the South Bridge IC via a 33 MHz PCI bus. The front and rear FireWire PHYs interface via the OHCI.

The Mac Pro provides front and rear port repeating when the computer is powered on or asleep. Front and rear repeating is also available when the computer is off, unless the computer was shut down from Mac OS X with no FireWire devices connected.

This section provides FireWire-specific information for Xserve servers introduced after September 2005. Refer to the specific Xserve developer note for additional information.

The Xserve with Quad-Core Intel Xeon 5400 Series microprocessors, introduced in January 2008, provides two, rear FireWire 800 IEEE 1394b ports. The two FireWire ports are on the same FireWire bus and share a single power supply that can provide 15 W per port, up to 15 W total. The FireWire 800 ports provide a regulated power of approximately 12 VDC.

The Open Host Controller Interface (OHCI) interfaces via a FireWire PHY and connects to the South Bridge with an x1 PCIe bus.

The Xserve provides rear port repeating when the server is powered on or asleep. Rear repeating is also available when the computer is off, unless the computer was shut down from Mac OS X with no FireWire devices connected.

The Xserve introduced in August 2006, based on the Dual-Core Intel Xeon processor, provides two FireWire 800 IEEE 1394b ports and one FireWire 400 IEEE 1394a ports. The three FireWire ports are on the same FireWire bus and share a single power supply that can provide 15 W per port, up to 15 watts total. The FireWire 800 and FireWire 400 ports provide a regulated power of approximately 12 VDC.

The Open Host Controller Interface (OHCI) connects to the South Bridge via a 33 MHz PCI bus. The front and rear FireWire PHYs interface via the OHCI.

The Xserve provides front and rear port repeating when the server is powered on or asleep. Front and rear repeating is also available when the computer is off, unless the computer was shut down from Mac OS X with no FireWire devices connected.

This section provides FireWire-specific information for iMac computers introduced after September 2005. Refer to the specific iMac developer note for additional information.

The iMac provides one FireWire 400 port and one FireWire 800 port supported by an Open HCI FireWire controller with a FireWire 800 PHY (Physical Layer). The FireWire 400 port supports IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The FireWire 800 port supports IEEE 1394b with a maximum data rate of 800 Mbps (100 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 1-lane PCI Express link interface on the South Bridge. The PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a and IEEE 1394b standards.

The iMac supports 7 W for each port, for a total of 14 W.

The iMac provides one FireWire 400 port and one FireWire 800 port supported by an Open HCI FireWire controller with a FireWire 800 PHY (Physical Layer). The FireWire 400 port supports IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The FireWire 800 port supports IEEE 1394b with a maximum data rate of 800 Mbps (100 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 1-lane PCI Express link interface on the South Bridge. The PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a and IEEE 1394b standards.

The iMac both support 7 W for each port, for a total of 14 W.

The iMac with SuperDrive computers introduced in September 2006 are based on the Intel Core 2 Duo microprocessor. The 17-inch and 20-inch iMacs provide two FireWire 400 ports supported by an Open HCI FireWire controller with an integrated FireWire 400 PHY (Physical Layer). Both ports support IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The integrated PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a standard.

The 24-inch iMac provides one FireWire 400 and one FireWire 800 port supported by an Open HCI FireWire controller with a FireWire 800 PHY (Physical Layer). The FireWire 400 port supports IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The FireWire 800 port supports IEEE 1394b with a maximum data rate of 800 Mbps (100 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a and IEEE 1394b standards.

The 17-inch and 20-inch iMacs support a total of 8 W shared between the two ports. The 24-inch iMac supports a total of 15 W shared between the two ports.

The iMac with Combo drive computers introduced in September 2006, based on the Intel Core 2 Duo microprocessor, provide two FireWire 400 ports supported by an Open HCI FireWire controller with an integrated FireWire 400 PHY (Physical Layer). Both ports support IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The integrated PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a standard.

The iMac supports a total of 8 W shared between the two ports.

The 17-inch iMac for education computer introduced in July 2006, based on the Intel Core Duo microprocessor, provides two FireWire 400 ports supported by an Open HCI FireWire controller with an integrated FireWire 400 PHY (Physical Layer). Both ports support IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The integrated PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a standard.

The iMac computers introduced in January 2006, based on the Intel Core Duo microprocessor, provide two FireWire 400 ports supported by an Open HCI FireWire controller with an integrated FireWire 400 PHY (Physical Layer). Both ports support IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The integrated PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a standard.

The iMac G5 has two external FireWire 400 (IEEE 1394a ports). It does not provide FireWire 800. When the computer is on, the power pins provide a regulated power of approximately 24 VDC and 8 W shared between the two ports.

This section provides FireWire-specific information for MacBook computers. Refer to the specific MacBook developer note for additional information.

The MacBook computer introduced in February 2008, incorporating the Intel Core 2 Duo processor on 45 nm process technology, provides one FireWire 400 port supported by an Open HCI FireWire controller with an integrated FireWire 400 PHY (Physical Layer). The port supports IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The integrated PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a standard.

FireWire cable power is present anytime the AC adaptor is powering the system, including shutdown. The MacBook's six-pin FireWire connector provides unregulated 9 V to 12 V power with a maximum load of 0.75 A. Developers should design to use 7 W sustained power, or less.

Output voltage depends on the system's battery charge level. Output voltage may be lower when the battery is not fully charged.

The MacBook has a single FireWire port, hence, there is no repeater function.

The MacBook computer introduced in November 2007, based on the Intel Core 2 Duo, provides one FireWire 400 port supported by an Open HCI FireWire controller with an integrated FireWire 400 PHY (Physical Layer). The port supports IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The integrated PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a standard.

FireWire cable power is present anytime the AC adaptor is powering the system, including shutdown. The MacBook's six-pin FireWire connector provides unregulated 9 V to 12 V power with a maximum load of 0.75 A. Developers should design to use 7 W sustained power, or less.

Output voltage depends on the system's battery charge level. Output voltage may be lower when the battery is not fully charged.

The MacBook has a single FireWire port, hence, there is no repeater function.

The MacBook computer introduced in May 2007, based on the Intel Core 2 Duo, provides one FireWire 400 port supported by an Open HCI FireWire controller with an integrated FireWire 400 PHY (Physical Layer). The port supports IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The integrated PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a standard.

FireWire cable power is present anytime the AC adaptor is powering the system, including shutdown. The MacBook's six-pin FireWire connector provides unregulated 9 V to 12 V power with a maximum load of 0.75 A. Developers should design to use 7 W sustained power, or less.

Output voltage depends on the system's battery charge level. Output voltage may be lower when the battery is not fully charged.

The MacBook has a single FireWire port, hence, there is no repeater function.

The MacBook computers introduced in November 2006, based on the Intel Core 2 Duo, provide one FireWire 400 port supported by an Open HCI FireWire controller with an integrated FireWire 400 PHY (Physical Layer). The port supports IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The integrated PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a standard.

FireWire cable power is present anytime the AC adaptor is powering the system, including shutdown. The MacBook's six pin FireWire connector provides unregulated 9 V to 12 V power with a maximum load of 0.75 A. Developers should design to use 7 W sustained power, or less.

Output voltage depends on the system's battery charge level. Output voltage may be lower when the battery is not fully charged.

The MacBook has a single FireWire port, hence, there is no repeater function.

The MacBook computers introduced in May 2006, based on the Intel Core Duo, provide one FireWire 400 port supported by an Open HCI FireWire controller with an integrated FireWire 400 PHY (Physical Layer). The port supports IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The integrated PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a standard.

FireWire cable power is present anytime the AC adaptor is powering the system, including shutdown. The MacBook's six pin FireWire connector provides unregulated 9 V to 12 V power with a maximum load of 0.75 A. Developers should design to use 7 W sustained power, or less.

Output voltage depends on the system's battery charge level. Output voltage may be lower when the battery is not fully charged.

The MacBook has a single FireWire port, hence, there is no repeater function.

This section provides FireWire-specific information for MacBook Pro computers. Refer to the specific MacBook Pro developer note for additional information.

The 17-inch MacBook Pro computers introduced in February 2008, incorporating the Intel Core 2 Duo processor on 45 nm process technology, provide one FireWire 400 port and one IEEE-1394b FireWire 800 port.

The FireWire 400 and 800 ports are supported by an Open HCI FireWire controller with a FireWire 800 PHY (Physical Layer). The FireWire 800 port supports IEEE 1394b with a maximum data rate of 800 Mbps (100 MBps). The FireWire 400 port supports IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a and IEEE 1394b standards.

FireWire power is present anytime the AC adaptor is powering the system, including shutdown. On battery power, FireWire power is present only during system run and is un-powered in sleep and shutdown to prevent unintentional battery drain.

Both of the FireWire connectors provide unregulated 9 to 12.6 V at 0.9 A maximum (fused). Developers should design to < 7 W maximum sustainable power.

Output voltage follows the system's battery power, such that voltage is dependent on the state of the battery's charge, as listed below.

- When the system is receiving AC power, with either a fully charged battery present or no battery present, output voltage is nominally 12.6 V. FireWire power is on in run, sleep, or shutdown.
- When the system is receiving AC power, and the battery is charging, output voltage will follow the battery voltage (unregulated 9V – 12.6 V). FireWire power is on in run, sleep, or shutdown.
- When the system is _not_ receiving AC power, the output voltage follows the battery voltage (unregulated 9 V – 12.6 V), and only when the system is running. FireWire power is turned off in system sleep or shutdown when no AC power is present.

The 15-inch MacBook Pro computers introduced in February 2008, incorporating the Intel Core 2 Duo processor on 45 nm process technology, provide one FireWire 400 port and one IEEE-1394b FireWire 800.

The FireWire 400 and 800 ports are supported by an Open HCI FireWire controller with a FireWire 800 PHY (Physical Layer). The FireWire 800 port supports IEEE 1394b with a maximum data rate of 800 Mbps (100 MBps). The FireWire 400 port supports IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a and IEEE 1394b standards.

FireWire power is present anytime the AC adaptor is powering the system, including shutdown. On battery power, FireWire power is present only during system run and is un-powered in sleep and shutdown to prevent unintentional battery drain.

Both of the FireWire connectors provide unregulated 9 to 12.6 V at 0.9 A maximum (fused). Developers should design to < 7 W maximum sustainable power.

Output voltage follows the system's battery power, such that voltage is dependent on the state of the battery's charge, as listed below.

- When the system is receiving AC power, with either a fully charged battery present or no battery present, output voltage is nominally 12.6 V. FireWire power is on in run, sleep, or shutdown.
- When the system is receiving AC power, and the battery is charging, output voltage will follow the battery voltage (unregulated 9V – 12.6 V). FireWire power is on in run, sleep, or shutdown.
- When the system is _not_ receiving AC power, the output voltage follows the battery voltage (unregulated 9 V – 12.6 V), and only when the system is running. FireWire power is turned off in system sleep or shutdown when no AC power is present.

The 17-inch MacBook Pro computers introduced in June 2007 and November 2007, based on the Intel Core 2 Duo microprocessor, provide one FireWire 400 port and one IEEE-1394b FireWire 800 port.

The FireWire 400 and 800 ports are supported by an Open HCI FireWire controller with a FireWire 800 PHY (Physical Layer). The FireWire 800 port supports IEEE 1394b with a maximum data rate of 800 Mbps (100 MBps). The FireWire 400 port supports IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a and IEEE 1394b standards.

FireWire power is present anytime the AC adaptor is powering the system, including shutdown. On battery power, FireWire power is present only during system run and is un-powered in sleep and shutdown to prevent unintentional battery drain.

Both of the FireWire connectors provide unregulated 9 to 12.6 V @ 0.9 A maximum (fused). Developers should design to < 7 W maximum sustainable power.

Output voltage follows the system's battery power, such that voltage is dependent on the state of the battery's charge, as listed below.

- When the system is receiving AC power, with either a fully charged battery present or no battery present, output voltage is nominally 12.6 V. FireWire power is on in run, sleep, or shutdown.
- When the system is receiving AC power, and the battery is charging, output voltage will follow the battery voltage (unregulated 9V – 12.6 V). FireWire power is on in run, sleep, or shutdown.
- When the system is _not_ receiving AC power, the output voltage follows the battery voltage (unregulated 9 V – 12.6 V), and only when the system is running. FireWire power is turned off in system sleep or shutdown when no AC power is present.

The 15-inch MacBook Pro computers introduced in June 2007 and November 2007, based on the Intel Core 2 Duo microprocessor, provide one FireWire 400 port and one IEEE-1394b FireWire 800.

The FireWire 400 and 800 ports are supported by an Open HCI FireWire controller with a FireWire 800 PHY (Physical Layer). The FireWire 800 port supports IEEE 1394b with a maximum data rate of 800 Mbps (100 MBps). The FireWire 400 port supports IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a and IEEE 1394b standards.

FireWire power is present anytime the AC adaptor is powering the system, including shutdown. On battery power, FireWire power is present only during system run and is un-powered in sleep and shutdown to prevent unintentional battery drain.

Both of the FireWire connectors provide unregulated 9 to 12.6 V @ 0.9 A maximum (fused). Developers should design to < 7 W maximum sustainable power.

Output voltage follows the system's battery power, such that voltage is dependent on the state of the battery's charge, as listed below.

- When the system is receiving AC power, with either a fully charged battery present or no battery present, output voltage is nominally 12.6 V. FireWire power is on in run, sleep, or shutdown.
- When the system is receiving AC power, and the battery is charging, output voltage will follow the battery voltage (unregulated 9V – 12.6 V). FireWire power is on in run, sleep, or shutdown.
- When the system is _not_ receiving AC power, the output voltage follows the battery voltage (unregulated 9 V – 12.6 V), and only when the system is running. FireWire power is turned off in system sleep or shutdown when no AC power is present.

The 17-inch MacBook Pro computer introduced in October 2006, based on the Intel Core 2 Duo microprocessor, provides one FireWire 400 port and one IEEE-1394b FireWire 800 port.

The FireWire 400 and 800 ports are supported by an Open HCI FireWire controller with a FireWire 800 PHY (Physical Layer). The FireWire 800 port supports IEEE 1394b with a maximum data rate of 800 Mbps (100 MBps). The FireWire 400 port supports IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a and IEEE 1394b standards.

FireWire power is present anytime the AC adaptor is powering the system, including shutdown. On battery power, FireWire power is present only during system run and is un-powered in sleep and shutdown to prevent unintentional battery drain.

Both of the FireWire connectors provide unregulated 9 to 12.6 V @ 0.9 A maximum (fused). Developers should design to < 7 W maximum sustainable power.

Output voltage follows the system's battery power, such that voltage is dependent on the state of the battery's charge, as listed below.

- When the system is receiving AC power, with either a fully charged battery present or no battery present, output voltage is nominally 12.6 V. FireWire power is on in run, sleep, or shutdown.
- When the system is receiving AC power, and the battery is charging, output voltage will follow the battery voltage (unregulated 9V – 12.6 V). FireWire power is on in run, sleep, or shutdown.
- When the system is _not_ receiving AC power, the output voltage follows the battery voltage (unregulated 9 V – 12.6 V), and only when the system is running. FireWire power is turned off in system sleep or shutdown when no AC power is present.

The 15-inch MacBook Pro computers introduced in October 2006, based on the Intel Core 2 Duo microprocessor, provide one FireWire 400 port and one IEEE-1394b FireWire 800.

The FireWire 400 and 800 ports are supported by an Open HCI FireWire controller with a FireWire 800 PHY (Physical Layer). The FireWire 800 port supports IEEE 1394b with a maximum data rate of 800 Mbps (100 MBps). The FireWire 400 port supports IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a and IEEE 1394b standards.

FireWire power is present anytime the AC adaptor is powering the system, including shutdown. On battery power, FireWire power is present only during system run and is un-powered in sleep and shutdown to prevent unintentional battery drain.

Both of the FireWire connectors provide unregulated 9 to 12.6 V @ 0.9 A maximum (fused). Developers should design to < 7 W maximum sustainable power.

Output voltage follows the system's battery power, such that voltage is dependent on the state of the battery's charge, as listed below.

- When the system is receiving AC power, with either a fully charged battery present or no battery present, output voltage is nominally 12.6 V. FireWire power is on in run, sleep, or shutdown.
- When the system is receiving AC power, and the battery is charging, output voltage will follow the battery voltage (unregulated 9V – 12.6 V). FireWire power is on in run, sleep, or shutdown.
- When the system is _not_ receiving AC power, the output voltage follows the battery voltage (unregulated 9 V – 12.6 V), and only when the system is running. FireWire power is turned off in system sleep or shutdown when no AC power is present.

The 17-inch MacBook Pro computers introduced in April 2006, based on the Intel Core Duo microprocessor, provide one FireWire 400 port and one FireWire 800 port, supported by a single Open HCI FireWire controller with an integrated FireWire 800 PHY (Physical Layer). The FireWire 400 port supports IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The FireWire 800 port supports IEEE 1394b with a maximum data rate of 800 Mbps (100 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The integrated PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a and IEEE 1394b standards.

FireWire cable power is present anytime the AC adaptor is powering the system, including shutdown. On battery power, FireWire power is present only during system run and is un-powered in sleep and shutdown to prevent unintentional battery drain.

Both of the FireWire connectors provide unregulated 12 V power, with a maximum combined load of 1.5 A. Developers should design to use 14 W sustained power, or less. One port may provide up to 14 W if no power is drawn from the other port, or both ports combined may provide up to a total of 14 W, such as 7 W from each port, simultaneously.

Output voltage depends on the system's battery charge level. Output voltage may be lower when the battery is not fully charged.

Because the 17-inch MacBook Pro has two FireWire ports, the PHY will repeat data between the ports whenever power is available, even if the computer is asleep or off.

The 15-inch MacBook Pro computers introduced in January 2006, based on the Intel Core Duo microprocessor, provide one FireWire 400 port supported by an Open HCI FireWire controller with an integrated FireWire 400 PHY (Physical Layer). The port supports IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The integrated PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a standard.

FireWire power is present anytime the AC adaptor is powering the system, including shutdown. On battery power, FireWire power is present only during system run and is un-powered in sleep and shutdown to prevent unintentional battery drain.

The 15-inch MacBook Pro's six pin FireWire connector provides unregulated 9 to 12.6 V @ 0.9 A maximum (fused). Developers should design to < 7 W maximum sustainable power.

Output voltage follows the system's battery power, such that voltage is dependent on the state of the battery's charge, as listed below.

- When the system is receiving AC power, with either a fully charged battery present or no battery present, output voltage is nominally 12.6 V. FireWire power is on in run, sleep, or shutdown.
- When the system is receiving AC power, and the battery is charging, output voltage will follow the battery voltage (unregulated 9V – 12.6 V). FireWire power is on in run, sleep, or shutdown.
- When the system is _not_ receiving AC power, the output voltage follows the battery voltage (unregulated 9 V – 12.6 V), and only when the system is running. FireWire power is turned off in system sleep or shutdown when no AC power is present.

The 15-inch MacBook Pro has a single FireWire port, hence, there is no repeater function.

This section provides Firewire-specific information for MacBook Air computers. Refer to the specific MacBook Air developer note for additional information.

The MacBook Air computer introduced in January 2008, based on the Intel Core 2 Duo processor, does not support FireWire.

This section provides FireWire-specific information for Mac mini computers. Refer to the specific Mac mini developer note for additional information.

The Mac mini computers introduced in February 2006, based on the Intel Core Duo microprocessor or Intel Core Solo microprocessor, provide one FireWire 400 port supported by an Open HCI FireWire controller with an integrated FireWire 400 PHY (Physical Layer). The port supports IEEE 1394a with a maximum data rate of 400 Mbps (50 MBps). The Open HCI controller provides the FireWire Link layer and DMA (Direct Memory Access) through the 32-bit 33 MHz PCI interface on the South Bridge. The integrated PHY implements the electrical signaling protocol and arbitration defined in the IEEE 1394a standard.

FireWire power is present anytime the AC adapter is connected to the system, including shutdown. The Mac mini's six pin FireWire connector provides unregulated 18 V power with a maximum load of 0.5 A. Developers should design to use 7 W sustained power, or less.

The Mac mini has a single FireWire port, hence, there is no repeater function.

This section provides FireWire-specific information for Power Mac computers introduced after September 2005. Refer to the specific Power Mac developer note for additional information.

The PowerMac G5 computer has one FireWire 800 port based on IEEE 1394b and two FireWire 400 IEEE 1394a ports. The three FireWire ports are all on the same FireWire bus. They share a single power supply that can provide up to 15 watts total. The FireWire 800 port and the FireWire 400 ports provide a regulated power of approximately 25 VDC. 

The South Bridge IC provides DMA (direct memory access) support for the FireWire interface. The controller in the South Bridge IC implements the FireWire link layer. The South Bridge IC is connected to the FireWire PHY and implements the electrical signaling protocol of the FireWire interfaces and implements the FireWire arbitration functions.

The PowerMac G5 computer provides front and rear port repeating when the computer is powered on or asleep, and rear port repeating when the system is powered off. The repeater will always appear to be an active device even though nothing is plugged into the port.

[Next](Document%20Revision%20History.md)[Previous](FireWire%20Concepts.md)

