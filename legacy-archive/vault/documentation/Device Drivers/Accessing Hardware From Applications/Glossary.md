---
title: Accessing Hardware From Applications
apple_id: TP30000376
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2007-02-08'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/AccessingHardware/AH_Glossary/AH_Glossary.html
archived_at: '2026-07-15T07:31:08.590120Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Accessing Hardware From Applications](Introduction%20to%20Accessing%20Hardware%20From%20Applications.md)


[Next](Index.md)[Previous](Document%20Revision%20History.md)

# Glossary

- __device__

  Computer hardware, typically excluding the CPU and system memory, that can be controlled and can send or receive data. Examples of devices include monitors, drives, bus controllers, and keyboards.

- __device file__

  A special file the I/O Kit creates in the `/dev` directory for each serial and storage device it discovers.

- __device interface__

  A plug-in interface, provided by an I/O Kit family, that conforms to the CFPlugIn architecture. Code running on OS X can call the functions in a device interface to access the in-kernel object representing a device. A device interface transmits an application’s commands to the device object via a user client. See also [user client](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobtfvbecqshineessi).

- __device matching__

  The I/O Kit process of searching the I/O Registry for objects representing one or more specific kinds of device.

- __driver__

  A unit of software that manages a specific piece of hardware. A driver written with the I/O Kit is an object that implements the appropriate I/O Kit abstractions for controlling that hardware.

  A driver can serve as a nub, but this is rare. See also [nub](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobtfvbueqkgizbeesa).

- __driver matching__

  The I/O Kit process of locating a suitable driver for a device.

- __driver personality__

  A dictionary of key/value pairs that specify device property values, such as family type, vendor name, or product name. A driver is suitable for any device whose properties match one of the driver’s personalities.

- __family__

  A collection of software abstractions that are common to all devices of a particular category. Families provide functionality and services to drivers. The I/O Kit defines families for bus protocols (such as SCSI, USB, and FireWire), storage devices, human interface devices, and many others.

- __framework__

  A type of bundle that packages a dynamic shared library with the resources the library requires, including header files and reference documentation.

- __I/O Kit__

  An object-oriented framework for developing device drivers on OS X. The I/O Kit provides many features, from a set of object classes that model system software and streamline the task of writing device drivers, to a dynamic model for identifying, loading, and unloading drivers and other services in a running system.

- __I/O Kit framework__

  The framework that includes `IOKitLib.h` and makes the I/O Registry, user client plug-ins, and other I/O Kit services available to applications and other code. Stored on disk as `IOKit.framework`.

- __I/O Registry__

  A dynamic database that describes a collection of ”live” objects, each of which represents an I/O Kit entity, such as a family, driver, or nub. As hardware is added to or removed from the system, the I/O Registry is modified to reflect the changes.

- __kernel space__

  The protected memory partition in which the kernel resides. See also [user space](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobtfvbueqkgizaucry).

- __matching dictionary__

  A dictionary of key/value pairs that describe the properties of a device or other service. The values in a matching dictionary are compared against those in a driver personality during device matching.

- __nub__

  An I/O Kit object that represents a detected, controllable entity, such as a device or logical service. A nub may represent a bus controller, a disk, a graphics adaptor, or any number of similar entities. When it supports a specific piece of hardware, a nub is also a driver (although this is rare).

  A nub supports dynamic configuration by providing a connection match point between two drivers (and, by extension, between two families). A nub can also provide services to code running in user space through a device interface. See also [driver](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobtfvbueqkgijeegsi).

- __plug-in__

  An object module that can be dynamically added to a running system or application.

  Core Foundation Plug-in Services uses the basic code-loading facility of Core Foundation Bundle Services to provide a standard plug-in architecture, known as the Core Foundation plug-in model, for Mac apps.

- __SCSI__

  See [Small Computer System Interface (SCSI)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobtfvbueqkhincuksq).

- __SCSI Architecture Model__

  A specification, approved as ANSI standard X3.270-1996, that defines a common interface standard between computers and devices such as disk drives, printers, and scanners.

- __Small Computer System Interface (SCSI)__

  An industry standard parallel data bus that provides a consistent method of connecting computers and peripheral devices.

- __service__

  A service is an I/O Kit entity, based on a subclass of IOService, that has been published with the `registerService` method and provides certain capabilities to other I/O Kit objects. In the I/O Kit’s layered architecture, each layer is a client of the layer below it and a provider of services to the layer above it.

- __user client__

  An in-kernel object that inherits from the IOService class and provides a connection between an in-kernel device driver or device nub and an application or process in user space. See also [device interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobtfvbecqsfireegqq).

- __user space__

  Memory outside the protected partition in which the kernel resides. Applications, plug-ins, and other types of modules typically run in user space. See also [kernel space](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobtfvbueqkkineuuqq).

[Next](Index.md)[Previous](Document%20Revision%20History.md)

