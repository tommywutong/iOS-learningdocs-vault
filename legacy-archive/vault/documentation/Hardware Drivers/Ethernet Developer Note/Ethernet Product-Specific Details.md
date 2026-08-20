---
title: Ethernet Developer Note
apple_id: TP40003029
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-04-28'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/HWTech_Ethernet/Articles/ENet_implementation.html
archived_at: '2026-07-15T07:40:58.732155Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Ethernet Developer Note](Introduction%20to%20Ethernet%20Developer%20Note.md)


[Next](Document%20Revision%20History.md)[Previous](Ethernet%20Concepts.md)

# Ethernet Product-Specific Details

This article highlights details of the Ethernet implementation specific to particular Mac computers. Unless otherwise specified in this article, Ethernet support a Mac computer adheres to the information in [Ethernet Concepts](Ethernet%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsmbwfvjvomk7gezdambtgmytcnzr).

This section provides Ethernet-specific information for Mac Pro computers introduced beginning August 2006. Refer to the specific Mac Pro developer note for additional information.

The Mac Pro computers with Quad-Core Intel Xeon 5400 Series microprocessors were introduced in January 2008. The Mac Pro provides support for dual, gigabit Ethernet with jumbo frame support for 10BASE-T/UTP, 100BASE-TX, and 1000BASE-T operation. The Ethernet MAC is internal to the South Bridge and interfaces to the dual gigabit Ethernet PHY. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Mac computer or PC to which the Ethernet port is connected.

The quad-core Mac Pro was introduced in August 2006 and the 8-core Mac Pro was introduced in April 2007 as a configure-to-order-option. The Mac Pro provides support for dual, gigabit Ethernet with jumbo frame support for 10BASE-T/UTP, 100BASE-TX, and 1000BASE-T operation. The Ethernet MAC is internal to the South Bridge and interfaces to the dual gigabit Ethernet PHY. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Mac computer or PC to which the Ethernet port is connected.

The Ethernet MAC is connected to the South Bridge IC via the I/O Acceleration Technology (IOAT) bus.

This section provides information on Xserve servers introduced after September 2005. Refer to the specific Xserve developer note for additional information.

The Xserve with Quad-Core Intel Xeon 5400 Series microprocessors, introduced in January 2008, provides supports for dual, gigabit Ethernet with jumbo frame support for 10BASE-T/UTP, 100BASE-TX, and 1000BASE-T operation. The Ethernet MAC is internal to the South Bridge and interfaces to the dual gigabit Ethernet PHY. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Mac computer or PC to which the Ethernet port is connected.

The Ethernet MAC is connected to the South Bridge via the I/O Acceleration Technology (IOAT) bus.

The Xserve announced in August 2006, based on the Dual-cCore Intel Xeon processor, provides supports for dual, gigabit Ethernet with jumbo frame support for 10BASE-T/UTP, 100BASE-TX, and 1000BASE-T operation. The Ethernet MAC is internal to the South Bridge and interfaces to the dual gigabit Ethernet PHY. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Mac computer or PC to which the Ethernet port is connected.

The Ethernet MAC is connected to the South Bridge via the I/O Acceleration Technology (IOAT) bus.

This section provides information on iMac computers introduced after September 2005. Refer to the specific iMac developer note for additional information.

The iMac Computers introduced in April 2008 use the Intel Core 2 Duo microprocessor. Ethernet support in these computers is provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Macintosh computer or PC to which the Ethernet port is connected.

The Ethernet controller is connected to the South Bridge IC via a 1-lane PCI Express link.

The iMac Computers introduced in August 2007 use the Intel Core 2 Duo microprocessor. Ethernet support in these computers is provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Macintosh computer or PC to which the Ethernet port is connected.

The Ethernet controller is connected to the South Bridge IC via a 1-lane PCI Express link.

The iMac with SuperDrive computers introduced in September 2006 use the Intel Core 2 Duo microprocessor. Ethernet support in these computers is provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Macintosh computer or PC to which the Ethernet port is connected.

The Ethernet controller is connected to the South Bridge IC via a 1-lane PCI Express link.

The iMac with Combo drive computer introduced in September 2006 uses the Intel Core 2 Duo microprocessor. Ethernet support is a provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Mac computer or PC to which the Ethernet port is connected.

The Ethernet controller is connected to the South Bridge IC via a 1-lane PCI Express link.

The 17-inch iMac for education computer introduced in July 2006 uses the Intel Core Duo microprocessor. Ethernet support in these computers is a provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Macintosh computer or PC to which the Ethernet port is connected.

The Ethernet controller is connected to the South Bridge IC via a 1-lane PCI Express link.

The iMac computers introduced in January 2006 are the first to incorporate the Intel Core Duo microprocessor. Ethernet support in these models is a provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Macintosh computer or PC to which the Ethernet port is connected.

The Ethernet controller is connected to the South Bridge IC via a 1-lane PCI Express link.

The iMac G5 Ethernet port supports 10/100/1000 Mbps transfer rates. The port is connected to the Vesta PHY ASIC.

This section provides information on MacBook computers. Refer to the specific MacBook developer note for additional information.

The MacBook computer introduced in February 2008 incorporates the Intel Core 2 Duo processor on 45 nm process technology. Ethernet support is a provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Mac computer or PC to which the Ethernet port is connected.

The Ethernet port is auto-sensing and self-configuring to allow connection via either a cross-over or straight-through cable.

The Ethernet controller is connected to the South Bridge IC via a 1-lane PCI Express link.

The MacBook employs power management to the Ethernet controller. When no cable is present the Ethernet controller periodically goes into a low power state. When an active link cable is attached it may take up to 2 seconds to recognize the connection.

The MacBook computer introduced in November 2007 incorporates the Intel Core 2 Duo microprocessor. Ethernet support is a provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Mac computer or PC to which the Ethernet port is connected.

The Ethernet port is auto-sensing and self-configuring to allow connection via either a cross-over or straight-through cable.

The Ethernet controller is connected to the South Bridge IC via a 1-lane PCI Express link.

The MacBook employs power management to the Ethernet controller. When no cable is present the Ethernet controller periodically goes into a low power state. When an active link cable is attached it may take up to 2 seconds to recognize the connection.

The MacBook computer introduced in May 2007 incorporates the Intel Core 2 Duo microprocessor. Ethernet support is a provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Mac computer or PC to which the Ethernet port is connected.

The Ethernet port is auto-sensing and self-configuring to allow connection via either a cross-over or straight-through cable.

The Ethernet controller is connected to the South Bridge IC via a 1-lane PCI Express link.

The MacBook employs power management to the Ethernet controller. When no cable is present the Ethernet controller periodically goes into a low power state. When an active link cable is attached it may take up to 2 seconds to recognize the connection.

The MacBook models introduced in November 2006 incorporate the Intel Core 2 Duo microprocessor. Ethernet support in these models is a provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Macintosh computer or PC to which the Ethernet port is connected.

The Ethernet port is auto-sensing and self-configuring to allow connection via either a cross-over or straight-through cable.

The Ethernet controller is connected to the South Bridge IC via a 1-lane PCI Express link.

The MacBook employs power management to the Ethernet controller. When no cable is present the Ethernet controller periodically goes into a low power state. When an active link cable is attached it may take up to 2 seconds to recognize the connection.

The MacBook models introduced in May 2006 incorporate the Intel Core Duo microprocessor. Ethernet support in these models is a provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Macintosh computer or PC to which the Ethernet port is connected.

The Ethernet port is auto-sensing and self-configuring to allow connection via either a cross-over or straight-through cable.

The Ethernet controller is connected to the South Bridge IC via a 1-lane PCI Express link.

The MacBook employs power management to the Ethernet controller. When no cable is present the Ethernet controller periodically goes into a low power state. When an active link cable is attached it may take up to 2 seconds to recognize the connection.

This section provides information on MacBook Pro computers. Refer to the specific MacBook Pro developer note for additional information.

The 17-inch MacBook Pro computers introduced in February 2008 incorporate the Intel Core 2 Duo processor on 45 nm process technology. Ethernet support in these models is provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Mac computer or PC to which the Ethernet port is connected.

The Ethernet port is auto-sensing and self-configuring to allow connection via either a cross-over or straight-through cable.

The Ethernet controller is connected to the South Bridge via a 1-lane PCI Express link.

The 17-inch MacBook Pro employs power management to the Ethernet controller. When no cable is present the Ethernet controller periodically goes into a low power state. When an active link cable is attached it may take up to 5 seconds to recognize the connection.

The 15-inch MacBook Pro models introduced in February 2008 incorporate the Intel Core 2 Duo processor on 45 nm process technology. Ethernet support in these models is a provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Mac computer or PC to which the Ethernet port is connected.

The Ethernet port is auto-sensing and self-configuring to allow connection via either a cross-over or straight-through cable.

The Ethernet controller is connected to the South Bridge via a 1-lane PCI Express link.

The 15-inch MacBook Pro employs power management to the Ethernet controller. When no cable is present the Ethernet controller periodically goes into a low power state. When an active link cable is attached it may take up to 5 seconds to recognize the connection.

The 17-inch MacBook Pro computers introduced in June 2007 and November 2007 incorporate the Intel Core 2 Duo microprocessor. Ethernet support in these models is a provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Mac computer or PC to which the Ethernet port is connected.

The Ethernet port is auto-sensing and self-configuring to allow connection via either a cross-over or straight-through cable.

The Ethernet controller is connected to the South Bridge via a 1-lane PCI Express link.

The 17-inch MacBook Pro employs power management to the Ethernet controller. When no cable is present the Ethernet controller periodically goes into a low power state. When an active link cable is attached it may take up to 5 seconds to recognize the connection.

The 15-inch MacBook Pro computers introduced in June 2007 and November 2007 incorporate the Intel Core 2 Duo microprocessor. Ethernet support in these models is a provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Mac computer or PC to which the Ethernet port is connected.

The Ethernet port is auto-sensing and self-configuring to allow connection via either a cross-over or straight-through cable.

The Ethernet controller is connected to the South Bridge via a 1-lane PCI Express link.

The 15-inch MacBook Pro employs power management to the Ethernet controller. When no cable is present the Ethernet controller periodically goes into a low power state. When an active link cable is attached it may take up to 5 seconds to recognize the connection.

The 17-inch MacBook Pro computer introduced in October 2006 incorporates the Intel Core 2 Duo microprocessor. Ethernet support in these models is provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Mac computer or PC to which the Ethernet port is connected.

The Ethernet port is auto-sensing and self-configuring to allow connection via either a cross-over or straight-through cable.

The Ethernet controller is connected to the South Bridge IC via a 1-lane PCI Express link.

The 17-inch MacBook Pro employs power management to the Ethernet controller. When no cable is present the Ethernet controller periodically goes into a low power state. When an active link cable is attached it may take up to 5 seconds to recognize the connection.

The 15-inch MacBook Pro models introduced in October 2006 incorporate the Intel Core 2 Duo microprocessor. Ethernet support in these models is a provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Mac computer or PC to which the Ethernet port is connected.

The Ethernet port is auto-sensing and self-configuring to allow connection via either a cross-over or straight-through cable.

The Ethernet controller is connected to the South Bridge IC via a 1-lane PCI Express link.

The 15-inch MacBook Pro employs power management to the Ethernet controller. When no cable is present the Ethernet controller periodically goes into a low power state. When an active link cable is attached it may take up to 5 seconds to recognize the connection.

The 17-inch MacBook Pro models introduced in April 2006 incorporate the Intel Core Duo microprocessor. Ethernet support in these models is a provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Macintosh computer or PC to which the Ethernet port is connected.

The Ethernet port is auto-sensing and self-configuring to allow connection via either a cross-over or straight-through cable.

The Ethernet controller is connected to the South Bridge IC via a 1-lane PCI Express link.

The 17-inch MacBook Pro employs power management to the Ethernet controller. When no cable is present the Ethernet controller periodically goes into a low power state. When an active link cable is attached it may take up to 2 seconds to recognize the connection.

The 15-inch MacBook Pro models introduced in January 2006 incorporate the Intel Core Duo microprocessor. Ethernet support in these models is a provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Macintosh computer or PC to which the Ethernet port is connected.

The Ethernet port is auto-sensing and self-configuring to allow connection via either a cross-over or straight-through cable.

The Ethernet controller is connected to the South Bridge IC via a 1-lane PCI Express link.

The MacBook Pro employs power management to the Ethernet controller. When no cable is present the Ethernet controller periodically goes into a low power state. When an active link cable is attached it may take up to 2 seconds to recognize the connection.

This section provides Ethernet-specific information for MacBook Air computers. Refer to the specific MacBook Air developer note for additional information.

The MacBook Air computer introduced in January 2008, based on the Intel Core 2 Duo processor, does not have built-in Ethernet. The Apple USB to Ethernet adapter can be connected to the external USB port for 10BASE-T/UTP or 100BASE-TX Ethernet operation.

This section provides information on Mac mini computers. Refer to the specific Mac mini developer note for additional information.

The Mac mini models introduced in February 2006 incorporate the Intel Core Duo microprocessor or Intel Core Solo microprocessor. Ethernet support in these models is a provided by a single-chip, integrated MAC/PHY LOM (LAN-On-Motherboard) solution. The Ethernet controller has an internal Ethernet PHY that provides 10BASE-T/UTP, 100BASE-TX, or 1000BASE-T operation over a standard twisted-pair interface. The operating speed of a link is automatically negotiated by the PHY and the bridge, router, hub, switch, or other Macintosh computer or PC to which the Ethernet port is connected.

The Ethernet port is auto-sensing and self-configuring to allow connection via either a cross-over or straight-through cable.

The Ethernet controller is connected to the South Bridge IC via a 1-lane PCI Express link.

The Mac mini employs power management to the Ethernet controller. When no cable is present the Ethernet controller periodically goes into a low power state. When an active link cable is attached it may take up to 2 seconds to recognize the connection.

This section provides information on Power Mac computers introduced after September 2005. Refer to the specific Power Mac developer note for additional information.

The Power Mac G5 computer has two built-in Ethernet ports that support 10/100/1000 Mbps transfer rates. In operation, the actual speed of each link is auto-negotiated between the Ethernet PHY device that is internal to the Mid Bridge and the bridge, router, hub, switch, or other Mac or PC to which it is connected. The Ethernet port is auto-sensing and self-configuring to allow connection via either a cross-over or straight-through cable.

Both CAT 5 unshielded twisted pair (UTP) and shielded twisted pair (STP) cables work with the Ethernet port. An STP cable is recommended for noisy environments or runs of greater than 100 meters.

[Next](Document%20Revision%20History.md)[Previous](Ethernet%20Concepts.md)

