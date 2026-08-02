---
title: HBA Device Driver Programming Guide
apple_id: TP40003194
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/SCSIHBADrivers/HBAOverview/HBAOverview.html
archived_at: '2026-07-15T07:41:08.321135Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HBA Device Driver Programming Guide](Introduction%20to%20HBA%20Device%20Driver%20Programming%20Guide.md)


[Next](Developing%20an%20HBA%20Driver.md)[Previous](Introduction%20to%20HBA%20Device%20Driver%20Programming%20Guide.md)

# HBA Devices and I/O Processing

A host bus adapter (HBA) is a device that provides a connection between a set of peripheral storage devices and a computer or between nodes on a network. In addition, an HBA device may provide some I/O processing—such as segmentation and reassembly, flow control, error detection, and interrupt handling—that improves I/O throughput.

This chapter describes how HBA devices are represented and managed in OS X and it introduces the SCSI Parallel family, which provides support for HBA drivers. This chapter also describes the path of an I/O request and how an HBA device driver participates in that journey.

If you need to develop a custom driver for an HBA device, you should read this chapter to learn how your driver fits into the system and how to take advantage of the services provided by the SCSI Parallel family. When you're ready to begin development, read [Developing an HBA Driver](Developing%20an%20HBA%20Driver.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnbnknltm) for specific guidelines on how to implement your driver and [Improving Performance](Improving%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnjnknltc) for ways to improve its performance.

Storage HBA devices provide an interface to sets of parallel SCSI, Fibre Channel, Serial ATA (SATA), or Serial Attached SCSI (SAS) devices. Some HBAs have firmware that allows them to communicate with more than one type of attached device. For example, some HBAs can handle both SAS and SATA drives.

You can develop an HBA driver to run in OS X for any type of HBA that understands the SCSI commands defined in the command sets SPC-3 (SCSI Primary Commands-3), SBC-2 (SCSI Block Commands-2), MMC-3 (Multimedia Command Set-3), and RBC (Reduced Block Command Set). This includes most Fibre Channel HBA devices, in addition to parallel SCSI and SAS HBAs. For more information about the SCSI Parallel Interconnect standards, visit the SCSI Trade Association website at [www.scsita.org](http://www.scsita.org/).

In OS X, HBA drivers participate in the mass storage driver stack as part of the physical interconnect layer (for more information about the objects in other layers of this stack, see _[Mass Storage Device Driver Programming Guide](../../Device%20Drivers/Mass%20Storage%20Device%20Driver%20Programming%20Guide/Introduction%20to%20Mass%20Storage%20Device%20Driver%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzu)_). The mass storage driver stack groups device communication into logical layers, each of which contains drivers and other objects that implement the appropriate protocols. In general, Apple-provided drivers and other objects implement system services, such as hot-plugging support and event handling, allowing third-party drivers to focus on supporting features unique to specific devices. A custom HBA driver's primary task is to transmit commands to the hardware, but it might also implement hardware-specific interrupt handling or device-management tasks.

Figure 1-1 shows the objects and layers in an example mass storage driver stack built up from a custom HBA driver.

__Figure 1-1__  A custom HBA driver participates in the mass storage driver stack

!

When the I/O Kit performs device matching on the object representing the HBA device, it instantiates a SCSI parallel interface controller object (an `IOSCSIParallelInterfaceController` instance). Depending on the individual HBA device, either the custom HBA driver or the SCSI parallel interface controller object then instantiates some number of SCSI parallel interface device objects (`IOSCSIParallelInterfaceDevice` instances). Although Figure 1-1 shows only one SCSI parallel interface device object, a real stack would contain a number of these objects equal to the number of devices the HBA device can support.

Each SCSI parallel interface device object then tries to create a SCSI target device object (an `IOSCSITargetDevice` instance). The SCSI target device object scans the device it represents for logical units and creates a SCSI logical unit nub (an `IOSCSILogicalUnitNub` instance) for each one it finds. Figure 1-1 shows the SCSI target device object straddling the logical boundary between the transport driver and physical interconnect layers. This is because it represents a link between the SCSI Architecture Model family (in which it is defined) and the SCSI parallel family (with which it communicates).

It is important to emphasize that neither the SCSI parallel interface controller object nor a custom HBA driver object creates SCSI target device objects. This allows a controller driver (Apple-provided or custom) to avoid having to rescan the entire bus for target devices. Instead, a rescan focuses on only those SCSI parallel interface device objects that do not have a SCSI target device object attached to them. Such a rescan does not interrupt I/O transfers in progress on SCSI parallel interface device objects that do have a SCSI target device object attached to them.

The appearance of a SCSI logical unit nub causes the I/O Kit to find and match to it either an in-kernel logical unit driver (for peripheral device types $00, $05, $07, and $0E) or a SCSI task user client (for other peripheral device types). The logical unit driver creates a SCSI task object (an instance of `SCSITask`) to contain the I/O request it receives from the objects above it in the stack. A SCSI task object contains the command descriptor block (or CDB) and is the fundamental unit of I/O transactions in the transport driver layer.

Objects in the device services layer of the mass storage driver stack view devices as abstract storage spaces and have no knowledge of command sets or physical interconnect protocols. Media objects can represent a subset of a storage device (such as a disk partition) or a set of devices (such as the set controlled by an HBA device). Optional filter drivers can implement encryption or validation on the content the media objects represent. The generic block storage driver implements the open and close semantics for the device and handles tasks such as deblocking for unaligned transfers and polling for ejectable media.

The SCSI Parallel family, introduced in OS X v10.2, was designed to replace the SCSI family (which was deprecated in OS X v.10.3). In spite of its rather specific name, the SCSI Parallel family supports any HBA device that can present itself as a parallel SCSI HBA. Naturally, this includes serial-attached SCSI (SAS) HBA devices, but it also includes Fibre Channel and SATA HBAs, many of which use high-level SCSI APIs to handle I/O.

The SCSI Parallel family offers many advantages over the SCSI family, such as the elimination of the locking and synchronization problems that often plagued the older family. The SCSI Parallel family also emphasizes correct implementation of the SCSI parallel interface standards SPI-3 and SPI-4, which means that it handles the vast majority of conforming devices.

Of most interest to HBA driver developers, however, is the fact that the SCSI Parallel family implements most of the operating system–dependent and SPI-defined tasks required for an HBA driver to communicate with other objects in the mass storage driver stack. For example, the SCSI Parallel family handles bus scanning, device recovery, discovery of logical units, creation of target device objects, and construction of SCSI commands, among other things. This high level of support confers three significant advantages:

- It allows developers to focus on the HBA device driver's primary task of shuttling I/O to and from the hardware.
- It provides a consistent experience across physical interconnects.
- It insulates developers from potential changes in underlying implementations.

The SCSI Parallel family defines the `IOSCSIParallelInterfaceController` class, which is the base class for all custom HBA drivers that can communicate using SCSI commands. The `IOSCSIParallelInterfaceController` class handles most of the I/O Kit driver life-cycle functions, various memory-allocation tasks, and optional target-device management, among other things. As a subclass of this class, a custom HBA driver implements a few required methods to report information about itself, initialize itself, and process I/O requests. If necessary, a custom HBA driver can also implement methods to perform device-management tasks and device-specific interrupt handling.

The `IOSCSIParallelInterfaceController` class also provides a large number of methods that allow you to get information about other objects without needing to know anything about the structure of those objects. For example, there are methods to retrieve information about the SCSI parallel task objects that represent I/O requests and SCSI commands and methods to get information about SCSI target device objects. Using these methods is both convenient and safe; accessing such objects directly can lead to problems if their implementations change.

One of the most important features of OS X is that it is a multithreaded operating system. The advantages of multithreadedness are especially apparent in the performance of I/O. This section focuses on the roles of different threads in the processing of an I/O request. An in-depth description of multithreadedness and other ways it might affect your driver is beyond the scope of this document; if you'd like to learn more about it, see _[Kernel Programming Guide](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_.

Figure 1-2 shows a simplified view of an I/O path. Refer to this figure as you read the description below it.

__Figure 1-2__  The journey of an I/O request

!

Imagine that an application makes a standard BSD `read` request and that the request (unbeknownst to the application) ultimately targets a SCSI storage device. The BSD command calls into the kernel, which performs a translation of the command's file descriptor to ensure that it targets the correct file system. After some additional handling, the read request transitions from the file system layer to the I/O Kit layer, where it enters the IOMedia object that represents the targeted content.

The request travels down the mass storage driver stack, each driver wrapping the request in the appropriate, protocol-defined format, and passing it to the driver below. Finally, the request reaches the HBA driver, which sends a command out on the peripheral bus to the appropriate target device. At this point, the application thread blocks, waiting for the completion of its request. The exact location of the waiting thread depends on specific circumstances and is not crucial to this description. The important thing is that the read request travels on the application's thread, all the way to the HBA driver.

When the target device completes the request, it causes a hardware (direct) interrupt. The interrupt controller (running in the primary interrupt context) dispatches the interrupt to the HBA driver and signals its work loop to run. With this, the primary interrupt context goes away and the secondary interrupt context (in which the controller driver now runs) begins, with the lock held. The controller driver's read completion routine executes, which triggers a cascade of completion routines as the completed request travels back up the stack. Finally, an object in the block services layer, still on the work-loop thread with the lock held, calls a file-system completion routine that signals the application thread to wake up. The application thread returns to the application with the completed read request and the application resumes running.

The distinction between the two threads involved in the journey of an I/O request is an important one because it affects the way your HBA driver processes I/O requests and handles interrupts.

[Next](Developing%20an%20HBA%20Driver.md)[Previous](Introduction%20to%20HBA%20Device%20Driver%20Programming%20Guide.md)

