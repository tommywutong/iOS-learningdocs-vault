---
title: USB Device Interface Guide
apple_id: TP40000973
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/USBBook/USBOverview/USBOverview.html
archived_at: '2026-07-15T07:31:34.714725Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [USB Device Interface Guide](Introduction%20to%20USB%20Device%20Interface%20Guide.md)


[Next](Working%20With%20USB%20Device%20Interfaces.md)[Previous](Introduction%20to%20USB%20Device%20Interface%20Guide.md)

# USB Device Overview

This chapter provides a summary of USB device architecture and describes how USB devices are represented in OS X. It also presents a few specific guidelines for working with USB devices in an application.For details on the USB specification, see [http://www.usb.org](http://www.usb.org/).

The USB specification supports a wide selection of devices that range from lower-speed devices such as keyboards, mice, and joysticks to higher-speed devices such as scanners and digital cameras. The specification lists a number of device classes that each define a set of expected device behaviors. [Table 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeskhjfcuisa) lists some examples of USB devices, categorized by class.

__Table 1-1__  Examples of USB devices

| USB device class | USB devices in class |
| Audio class | Speakers, microphones |
| Chip Card Interface Device Class | Smart cards, chip cards |
| Communication class | Speakerphone, modem |
| Composite class | A device in which all class-specific information is embedded in its interfaces |
| HID class | Keyboards, mice, joysticks, drawing tablets |
| Hub class | Hubs provide additional attachment points for USB devices |
| Mass storage class | Hard drives, flash memory readers, CD Read/Write drives, digital cameras, and high-end media players |
| Printing class | Printers |
| Vendor specific | A device that doesn’t fit into any other predefined class or one that doesn’t use the standard protocols for an existing class |
| Video class | Digital camcorders, webcams, digital still cameras that support video streaming |

Version 1.1 of the USB specification supports two bus speeds:

- Low speed (1.5 Mbps)
- Full speed (12 Mbps)

Version 2.0 of the specification adds another bus speed to this list:

- High speed (480 Mbps)

The USB 2.0 specification is fully compatible with low-speed and full-speed USB devices and even supports the use of cables and connectors made to meet earlier versions of the specification. Apple provides USB 2.0 ports on all new Macintosh computers and fully supports the new specification with Enhanced Host Controller Interface (EHCI) controllers and built-in, low-level USB drivers.

For the most part, you do not have to change existing applications to support the faster data rate because the speed increase and other enhancements are implemented at such a low level. The exceptions to this are some differences in isochronous transfers. For information on how the USB 2.0 specification affects isochronous transfers, see [USB 2.0 and Isochronous Transfers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeq2di5ducsq).

The architecture of a generic USB device is multi-layered. A device consists of one or more configurations, each of which describes a possible setting the device can be programmed into. Such settings can include the power characteristics of the configuration (for example, the maximum power consumed by the configuration and whether it is self-powered or not) and whether the configuration supports remote wake-up.

Each configuration contains one or more interfaces that are accessible after the configuration is set. An interface provides the definitions of the functions available within the device and may even contain alternate settings within a single interface. For example, an interface for an audio device may have different settings you can select for different bandwidths.

Each interface contains zero or more endpoints. An endpoint is a uniquely identifiable portion of a USB device that is the source or sink of information in a communication flow between the host and the device. Each endpoint has characteristics that describe the communication it supports, such as transfer type (control, isochronous, interrupt, or bulk, described in [USB Transfer Types](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeskiifeucry)), maximum packet size, and transfer direction (input or output).

Communication with a USB device is accomplished through a pipe, a logical association between an endpoint and software running on the host. Endpoint and pipe are often used synonymously although an endpoint is a component of a USB device and a pipe is a logical abstraction of the communications link between endpoint and host.

Each layer of a USB device provides information about its attributes and resource requirements in its descriptor, a data structure accessible through device interface functions. By examining the descriptors at each layer, you can determine exactly which endpoint you need to communicate successfully with a particular device.

At the top layer is the device descriptor, which has fields associated with information such as the device’s class and subclass, vendor and product numbers, and number of configurations. Each configuration in turn has a configuration descriptor containing fields that describe the number of interfaces it supports and the power characteristics of the device when it is in that configuration, along with other information. Each interface supported by a configuration has its own descriptor with fields for information such as the interface class, subclass, and protocol, and the number of endpoints in that interface. At the bottom layer are the endpoint descriptors that specify attributes such as transfer type and maximum packet size.

The USB specification defines a name for each descriptor field, such as the `bDeviceClass` field in the device descriptor and the `bNumInterfaces` field in the configuration descriptor, and each field is associated with a value. For a complete listing of all descriptor fields, see the USB specification at [www.usb.org](http://www.usb.org/). The USB family defines structures that represent the descriptors defined by the USB specification. For the definitions of these structures, see `USB` in _[Kernel Framework Reference](https://developer.apple.com/documentation/kernel)_.

The USB specification defines a composite class device as a device whose device-descriptor fields for device class (`bDeviceClass`) and device subclass (`bDeviceSubClass`) both have the value `0`. A composite class device appears to the system as a USB device using a single bus address that may present multiple interfaces, each of which represents a separate function. A good example of a composite class device is a multifunction device, such as a device that performs printing, scanning, and faxing. In such a device, each function is represented by a separate interface. In OS X, the I/O Kit loads the `AppleUSBComposite` device driver for composite class devices that do not already have vendor-specific device drivers to drive them. The `AppleUSBComposite` driver configures the device and causes drivers to be loaded for each USB interface.

Although most multifunction USB devices are composite class devices, not all composite class devices are multifunction devices. The manufacturer of a single-function USB device is at liberty to classify the device as a composite class device as long as the device meets the USB specifications. For more information on how OS X represents USB devices and interfaces, see [USB Devices on OS X](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeskkizdeiqy).

The USB specification defines four types of pipe transfer:

- _Control_—intended to support configuration, command, and status communication between the host software and the device. Control transfers support error detection and retry.
- _Interrupt_—used to support small, limited-latency transfers to or from a device such as coordinates from a pointing device or status changes from a modem. Interrupt transfers support error detection and retry.
- _Isochronous_—used for periodic, continuous communication between the host and the device, usually involving time-relevant information such as audio or video data streams. Isochronous transfers do not support error detection or retry.
- _Bulk_—intended for non-periodic, large-packet communication with relaxed timing constraints such as between the host software and a printer or scanner. Bulk transfers support error detection and retry.

Pipes also have a transfer direction associated with them. A control pipe can support bidirectional communication but all other pipes are strictly uni-directional. Therefore, two-way communication requires two pipes, one for input and one for output.

Every USB device is required to implement a default control pipe that provides access to the device’s configuration, status, and control information. This pipe, implemented in the `IOUSBDevice` nub object (described in [USB Devices on OS X](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeskkizdeiqy)), is used when a driver such as the `AppleUSBComposite` driver configures the device or when device-specific control and status information is needed. For example, your application would use the default control pipe if it needs to set or choose a configuration for the device. The default control pipe is connected to the default endpoint (endpoint 0). Note that endpoint 0 does not provide an endpoint descriptor and it is never counted in the total number of endpoints in an interface.

The interfaces associated with a configuration can contain any combination of the three remaining pipe types (interrupt, isochronous, and bulk), implemented in the `IOUSBInterface` nub objects (described in [USB Devices on OS X](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeskkizdeiqy)). Your application can query the interface descriptors of a device to select the pipe most suited to its needs.

Although a stall and a halt are different, they are closely related in their effect on data transmission. Halt is a feature of an endpoint and it can be set by either the host or the device itself in response to an error. A stall is a type of handshake packet an endpoint returns when it is unable to transmit or receive data or when its halt feature is set (the host never sends a stall packet). When an endpoint sends a stall packet, the host can halt the endpoint.

Depending on the precise circumstances and on how compliant the device is, the halt feature must be cleared in the host, the endpoint, or both before data transmission can resume. When the halt is cleared the data toggle bit, used to synchronize data transmission, is also reset (see [Data Synchronization in Non-Isochronous Transfers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeq2ijjeesrq) for more information about the data toggle). For information on how to handle these conditions in your application, see [Handling Stalls, Halts, and Data Toggle Resynchronization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeq2gijbumqq).

The USB specification defines a simple protocol to provide data synchronization across multiple packets for non-isochronous transfers (recall that isochronous transfers do not support error recovery or retry). The protocol is implemented by means of a data toggle bit in both the host and the endpoint which is synchronized at the start of a transaction (or when a reset occurs). The precise synchronization mechanism varies with the type of transfer; see the USB specification for details.

Both the host and the endpoint begin a transaction with their data toggle bits set to zero. In general, the entity receiving data toggles its data toggle bit when it is able to accept the data and it receives an error-free data packet with the correct identification. The entity sending the data toggles its data toggle bit when it receives a positive acknowledgement from the receiver. In this way, the data toggle bits stay synchronized until, for example, a packet with an incorrect identification is received. When this happens, the receiver ignores the packet and does not increment its data toggle bit. When the data toggle bits get out of synchronization (for this or any other reason), you will probably notice that alternate transactions are not getting through in your application. The solution to this is to resynchronize the data toggle bits. For information on how to do this, see [Handling Stalls, Halts, and Data Toggle Resynchronization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeq2gijbumqq).

The USB 2.0 specification supports the same four transfer types as earlier versions of the specification. In addition to supporting a higher transfer rate, the new specification defines an improved protocol for high-speed transfers and new ways of handling transactions for low-speed and full-speed devices. For details on the protocols and transaction-handling methods, see the specification at [http://www.usb.org](http://www.usb.org/).

For the most part, these enhancements are implemented at the host software level and do not require changes to your code. For isochronous transfers, however, you should be aware of the following differences:

- Earlier versions of the specification divide bus time into 1-millisecond frames, each of which can carry multiple transactions to multiple destinations. (A transaction contains two or more packets: a token packet and one or more data packets, a handshake packet, or both.) The USB 2.0 specification divides the 1-millisecond frame into eight, 125-microsecond microframes, each of which can carry multiple transactions to multiple destinations.
- The maximum amount of data allowed in a transaction is increased to 3 KB.
- Any isochronous endpoints in a device’s default interface must have a maximum packet size of zero. (This means that the default setting for an interface containing isochronous pipes is alternate setting zero and the maximum packet size for that interface’s isochronous endpoints must be zero.) This ensures that the host can configure the device no matter how busy the bus is.

For a summary of how these differences affect the OS X USB API, see [Changes in Isochronous Functions to Support USB 2.0](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeq2cjfcemra).

When a USB device is plugged in, the OS X USB family abstracts the contents of the device descriptor into an I/O Kit nub object called an `IOUSBDevice`. This nub object is attached to the `IOService` plane of the I/O Registry as a child of the driver for the USB controller. The `IOUSBDevice` nub object is then registered for matching with the I/O Kit.

If the device is a composite class device with no vendor-specific driver to match against it, the `AppleUSBComposite` driver matches against it and starts as its provider. The `AppleUSBComposite` driver then configures the device by setting the configuration in the device’s list of configuration descriptors with the maximum power usage that can be satisfied by the port to which the device is attached. This allows a device with a low power and a high power configuration to be configured differently depending on whether it’s attached to a bus-powered hub or a self-powered hub. In addition, if the `IOUSBDevice` nub object has the “Preferred Configuration” property, the `AppleUSBComposite` driver will always use that value when it attempts to configure the device.

The configuration of the device causes the USB family to abstract each interface descriptor in the chosen configuration into an `IOUSBInterface` nub object. These nub objects are attached to the I/O Registry as children of the original `IOUSBDevice` nub object and are registered for matching with the I/O Kit.

For non-composite class devices or composite class devices with vendor-specific drivers that match against them, there is no guarantee that any configuration will be set and you may have to perform this task within your application.

It's important to be mindful of the difference between a USB device (represented in the I/O Registry by an `IOUSBDevice` nub object) and its interfaces (each represented by an `IOUSBInterface` nub object). A multifunction USB device, for example, is represented in the I/O Registry by one `IOUSBDevice` object and one `IOUSBInterface` object for each interface.

The distinction between interface and device is important because it determines which object your application must find in the I/O Registry and which type of device interface to get. For example, if your application needs to communicate with a specific interface in a multifunction USB device, it must find that interface and get an `IOUSBInterfaceInterface` to communicate with it. An application that needs to communicate with the USB device as a whole, on the other hand, would need to find the device in the I/O Registry and get an `IOUSBDeviceInterface` to communicate with it. For more information on finding devices and interfaces in the I/O Registry, see [Finding USB Devices and Interfaces](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeskei5buqqq); for more information on how to get the proper device interface to communicate with a device or interface, see [Using USB Device Interfaces](Working%20With%20USB%20Device%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskiineuqqq).

To find a USB device or interface, use the keys defined in the _Universal Serial Bus Common Class Specification, Revision 1.0_ (available for download from [http://www.usb.org/developers/devclass_docs/usbccs10.pdf](http://www.usb.org/developers/devclass_docs/usbccs10.pdf)) to create a matching dictionary that defines a particular search. If you are unfamiliar with the concept of device matching, see the section “Finding Devices in the I/O Registry” in _[Accessing Hardware From Applications](../Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw)_.

The keys defined in the specification are listed in the tables below. Each key consists of a specific combination of elements in a device or interface descriptor. In the tables below, the elements in a key are separated by the ‘+’ character to emphasize the requirement that all a key’s elements must appear together in your matching dictionary. Both tables present the keys in order of specificity: the first key in each table defines the most specific search and the last key defines the broadest search.

Before you build a matching dictionary, be sure you know whether your application needs to communicate with a device or a specific interface in a device. It’s especially important to be aware of this distinction when working with multifunction devices. A multifunction device is often a composite class device that defines a separate interface for each function. If, for example, your application needs to communicate with the scanning function of a device that does scanning, faxing, and printing, you need to build a dictionary to match on only the scanning interface (an IOUSBInterface object), not the device as a whole (an IOUSBDevice object). In this situation, you would use the keys defined for interface matching (those shown in [Table 1-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeq2fifbucsq)), not the keys for device matching.

[Table 1-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeq2di5cukrq) lists the keys you can use to find devices (not interfaces). Each key element is a piece of information contained in the device descriptor for a USB device.

__Table 1-2__  Keys for finding a USB device

| Key | Notes |
| `idVendor` + `idProduct` + `bcdDevice` | `bcdDevice` contains the release number of the device |
| `idVendor` + `idProduct` |  |
| `idVendor` + `bDeviceSubClass` + `bDeviceProtocol` | Use this key only if the device’s `bDeviceClass` is $FF |
| `idVendor` + `bDeviceSubClass` | Use this key only if the device’s `bDeviceClass` is $FF |
| `bDeviceClass` + `bDeviceSubClass` + `bDeviceProtocol` | Use this key only if the device’s `bDeviceClass` is _not_ $FF |
| `bDeviceClass` + `bDeviceSubClass` | Use this key only if the device’s `bDeviceClass` is _not_ $FF |

[Table 1-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeq2fifbucsq) lists the keys you can use to find interfaces (not devices). Each key element is a piece of information contained in an interface descriptor for a USB device.

__Table 1-3__  Keys for finding a USB interface

| Key | Notes |
| `idVendor` + `idProduct` + `bcdDevice` + `bConfigurationValue` + `bInterfaceNumber` |  |
| `idVendor` + `idProduct` + `bConfigurationValue` + `bInterfaceNumber` |  |
| `idVendor` + `bInterfaceSubClass` + `bInterfaceProtocol` | Use this key only if `bInterfaceClass` is $FF |
| `idVendor` + `bInterfaceSubClass` | Use this key only if `bInterfaceSubClass` is $FF |
| `bInterfaceClass` + `bInterfaceSubClass` + `bInterfaceProtocol` | Use this key only if `bInterfaceSubClass` is _not_ $FF |
| `bInterfaceClass` + `bInterfaceSubClass` | Use this key only if `bInterfaceSubClass` is _not_ $FF |

For a successful search, you must add the elements of exactly one key to your matching dictionary. If your matching dictionary contains a combination of elements not defined by any key, the search will be unsuccessful. For example, if you create a matching dictionary containing values representing a device’s vendor, product, and protocol, the search will be unsuccessful even if a device with those precise values in its device descriptor is currently represented by an `IOUSBDevice` nub in the I/O Registry. This is because there is no key in [Table 1-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeq2di5cukrq) that combines the `idVendor`, `idProduct`, and `bDeviceProtocol` elements.

As you develop an application to access a USB device or interface, you will probably encounter error codes specific to the OS X USB family. If you are using Xcode, you can search for information about these error codes in the Xcode documentation window.

To find error code documentation, select Documentation from the Xcode Help menu. Select Full-Text Search from the pull-down menu associated with the search field (click the magnifying glass icon to reveal the menu). Select Reference Library in the Search Groups pane at the left of the window. Type an error code number in the search field, such as 0xe0004057, and press Return. Select the most relevant entry in the search results to display the document in the lower portion of the window. Use the Find command (press Command-F) to find the error code in this document. Using the example of error code 0xe0004057, you’ll see that this error is returned when the endpoint has not been found.

For help with deciphering I/O Kit error codes in general, see Technical Q&A QA1075, “[Making sense of I/O Kit error codes](https://developer.apple.com/qa/qa2001/qa1075.html).”

As described in [USB Devices on OS X](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeskkizdeiqy), the OS X USB family provides an `IOUSBDeviceInterface` object you use to communicate with a USB device as a whole and an `IOUSBInterfaceInterface` object you use to communicate with an interface in a USB device. There are a number of different versions of the USB family, however, some of which provide new versions of these interface objects. (One way to find the version of the USB family installed in your computer is to view the Finder preview information for the `IOUSBFamily.kext` located in `/System/Library/Extensions`.) This section describes how to make sure you use the correct interface object and how to view the documentation for the interface objects.

The first version of the USB family was introduced in OS X v10.0 and contains the first versions of the interface objects `IOUSBDeviceInterface` and `IOUSBInterfaceInterface`. When new versions of the USB family introduce new functions for an interface object, a new version of the interface object is created, which gives access to both the new functions and all functions defined in all previous versions of that interface object. For example, the `IOUSBDeviceInterface197` object provides two new functions you can use with version 1.9.7 of the USB family (available in OS X v10.2.3 and later), in addition to all functions available in the previous device interface objects `IOUSBDeviceInterface187`, `IOUSBDeviceInterface182`, and `IOUSBDeviceInterface`.

As you develop an application that accesses a USB device or interface, you should use the latest version of the interface object that is available in the earliest version of OS X that you want to support. For example, if your application must run in OS X v10.0, you must use the `IOUSBDeviceInterface` and `IOUSBInterfaceInterface` objects. If, however, you develop an application to run in OS X v10.4 and later, you use the `IOUSBDeviceInterface197` object to access the device as a whole and the `IOUSBInterfaceInterface220` object to access an interface in it. This is because `IOUSBDeviceInterface197` is available in OS X version 10.2.3 and later and `IOUSBInterfaceInterface220` is available in OS X v10.4 and later.

This section presents some specific tasks your application might need to perform, along with some caveats related to USB 2.0 support of which you should be aware.

As described in [Stalls and Halts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeq2fi5cekri), stalls and halts are closely related in their effect on data transmission. To simplify the API, the USB family uses the pipe stall terminology in the names of the functions that handle these conditions:

- `ClearPipeStall`
- `ClearPipeStallBothEnds`

The `ClearPipeStall` function operates exclusively on the host controller side, clearing the halt feature and resetting the data toggle bit to zero. If the endpoint’s halt feature and data toggle bit must be reset as well, your application must do so explicitly, using one of the `ControlRequest` functions to send the appropriate device request. See the documentation for the `USB.h` header file in _[I/O Kit Framework Reference](https://developer.apple.com/documentation/iokit)_ for more information about standard device requests.

In OS X version 10.2 and later, you can use the `ClearPipeStallBothEnds` function which, as its name suggests, clears the halt and resets the data toggle bit on both sides at the same time.

In OS X, the time between when an isochronous transaction completes on the USB bus and when you receive your callback can stretch to tens of milliseconds. This is because the callback happens on the USB family work loop, which runs at a lower priority than some other threads in the system. In most cases, you can work around this delay by queuing read and write requests so that the next transaction is scheduled and ready to start before you receive the callback from the current transaction. In fact, this scheme is a good way to achieve higher performance whether or not low latency is a requirement of your application.

In a few cases, however, queuing isochronous transactions to keep the pipe busy is not enough to prevent a latency problem that a user might notice. Consider an application that performs audio processing on some USB input (from a musical instrument, for example) before sending the processed data out to USB speakers. In this scenario, a user hears both the raw, unprocessed output of the instrument and the processed output of the speakers. Of course, some small delay between the time the instrument creates the raw sound waves and the time the speaker emits the processed sound waves is unavoidable. If this delay is greater than about 8 milliseconds, however, the user will notice.

In OS X version 10.2.3 (version 1.9.2 of the USB family) the USB family solves this problem by taking advantage of the predictability of isochronous data transfers. By definition, isochronous mode guarantees the delivery of some amount of data every frame or microframe. In earlier versions of OS X, however, it was not possible to find out the exact amount of data that was transferred by a given time. This meant that an application could not begin processing the data until it received the callback associated with the transaction, telling it the transfer status and the actual amount of data that was transferred.

Version 1.9.2 of the USB family introduced the `LowLatencyReadIsochPipeAsync` and `LowLatencyWriteIsochPipeAsync` functions. These functions update the frame list information (including the transfer status and the number of bytes actually transferred) at primary interrupt time. Using these functions, an application can request that the frame list information be updated as frequently as every millisecond. This means an application can retrieve and begin processing the number of bytes actually transferred once a millisecond, without waiting for the entire transaction to complete.

To support the low latency isochronous read and write functions, the USB family also introduced functions to create and destroy the buffers that hold the frame list information and the data. Although you can choose to create a single data buffer and a single frame list buffer or multiple buffers of each type, you must use the `LowLatencyCreateBuffer` function to create them. Similarly, you must use the `LowLatencyDestroyBuffer` function to destroy the buffers after you are finished with them. This restricts all necessary communication with kernel entities to the USB family.

For reference documentation on the low latency isochronous functions, see the `IOUSBLib.h` documentation in _[I/O Kit Framework Reference](https://developer.apple.com/documentation/iokit)_.

The EHCI hub that supports high-speed devices (as well as low-speed and full-speed devices) provides coarser-grained error reporting than the OHCI hub does. For example, with an OHCI hub, you might receive an “endpoint timed out” error if you unplug the device while it is active. If you perform the same action with an EHCI hub, you might receive a “pipe stalled” error instead.

The Apple EHCI hub driver cannot get more detailed error information from the hub, so it alternates between reporting “device not responding” and “pipe stalled” regardless of the actual error reported by the device. To avoid problems with your code, be sure your application does not rely on other, more specific errors to make important decisions.

Recall that the USB 2.0 specification divides the 1-millisecond frame into eight, 125-microsecond microframes. The USB family handles this by reinterpreting some function parameters (where appropriate) and adding a couple of new functions. This section summarizes these changes; for reference documentation, see documentation for `IOUSBLib.h` in _[I/O Kit Framework Reference](https://developer.apple.com/documentation/iokit)_.

The functions you use to read from and write to isochronous endpoints are `ReadIsochPipeAsync` and `WriteIsochPipeAsync`. Both functions include the following two parameters:

- _numFrames_—The number of frames for which to transfer data
- _frameList_—A pointer to an array of structures that describe the frames

If you need to handle high-speed isochronous transfers, you can think of these parameters as referring to “transfer opportunities” instead of frames. In other words, _numFrames_ can refer to a number of frames for full-speed devices or to a number of microframes for high-speed devices. Similarly, _frameList_ specifies the list of transfers you want to occur, whether they are in terms of frames or microframes.

To help you determine whether a device is functioning in full-speed or high-speed mode, the USB family added the `GetFrameListTime` function, which returns the number of microseconds in a frame. By examining the result (`kUSBFullSpeedMicrosecondsInFrame` or `kUSBHighSpeedMicrosecondsInFrame`) you can tell in which mode the device is operating.

The USB family also added the `GetBusMicroFrameNumber` function which is similar to the `GetBusFrameNumber` function, except that it returns both the current frame and microframe number and includes the time at which that information was retrieved.

To handle the new specification’s requirement that isochronous endpoints in a device’s default interface have a maximum packet size of zero, the USB family added functions that allow you to balance bandwidth allocations among isochronous endpoints. A typical scenario is this:

1. Call `GetBandwidthAvailable` (available in OS X version 10.2 and later) to determine how much bandwidth is currently available for allocation to isochronous endpoints.
2. Call `GetEndpointProperties` (available in OS X version 10.2 and later) to examine the alternate settings of an interface and find one that uses an appropriate amount of bandwidth.
3. Call `SetAlternateInterface` (available in OS X version 10.0 and later) to create the desired interface and allocate the pipe objects.
4. Call `GetPipeProperties` (available in OS X version 10.0 and later) on the chosen isochronous endpoint. This is a very important step because `SetAlternateInterface` will succeed, even if there is not enough bandwidth for the endpoints. Also, another device might have claimed the bandwidth that was available at the time the `GetBandwidthAvailable` function returned. If this happens, the maximum packet size for your chosen endpoint (contained in the `maxPacketSize` field) is now zero, which means that the bandwidth is no longer available.

In addition, in OS X version 10.2, the USB family added the `SetPipePolicy` function, which allows you to relinquish bandwidth that might have been specified in an alternate setting.

This section provides an overview of some of the issues related to developing a universal binary version of an application that accesses a USB device. Before you read this section, be sure to read _[Universal Binary Programming Guidelines, Second Edition](../../Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_. That document covers architectural differences and byte-ordering formats and provides comprehensive guidelines for code modification and building universal binaries. The guidelines in that document apply to all types of applications, including those that access hardware.

Before you build your application as a universal binary, make sure that:

- You port your project to GCC 4 (Xcode uses GCC 4 to target Intel-based Macintosh computers)
- You install the OS X v10.4 universal SDK
- You develop your project in Xcode 2.1 or later

The USB bus is a little-endian bus. Structured data appears on the bus in the little-endian format regardless of the native endian format of the computer an application is running in. If you've developed a USB device-access application to run in a PowerPC-based Macintosh, you probably perform some byte swapping on data you read from the USB bus because the PowerPC processor uses the big-endian format. For example, the USB configuration descriptor structure contains a two-byte field that holds the descriptor length. If your PowerPC application reads this structure from the USB bus (instead of receiving it from a USB device interface function), you need to swap the value from the USB bus format (little endian) to the PowerPC format (big endian).

The USB family provides several swapping macros that swap from USB to host and from host to USB (for more information on these macros, see `USB.h`). The Kernel framework also provides byte-swapping macros and functions you can use in high-level applications (see the `OSByteOrder.h` header file in `libkern`). If you use these macros in your application, you shouldn't have any trouble developing a universal binary version of your application. This is because these macros determine at compile time if a swap is necessary. If, however, your application uses hard-coded swaps from little endian to big endian, your application will not run correctly in an Intel-based Macintosh. As you develop a universal binary version of your application, therefore, be sure to use the USB family swapping macros or the macros in `libkern/OSByteOrder.h` for all byte swapping.

Although you may need to perform byte swapping on values your application reads from the USB bus, you do not need to perform any byte swapping on values you pass in arguments to functions in the USB family API. You should pass argument values in the computer's host format. Likewise, any values you receive from the USB family functions will be in the computer's host format.

[Next](Working%20With%20USB%20Device%20Interfaces.md)[Previous](Introduction%20to%20USB%20Device%20Interface%20Guide.md)

