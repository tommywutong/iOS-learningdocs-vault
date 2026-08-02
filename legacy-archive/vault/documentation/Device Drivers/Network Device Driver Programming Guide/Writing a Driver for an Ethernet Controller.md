---
title: Network Device Driver Programming Guide
apple_id: TP40000913
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/NetworkDriver/4_Writing%20the%20Driver/NetworkController.html
archived_at: '2026-07-15T07:31:34.645800Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Network Device Driver Programming Guide](Introduction%20to%20Network%20Device%20Driver%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Tips%20on%20Bringing%20Up%20a%20UNIX%20Network%20Driver.md)

# Writing a Driver for an Ethernet Controller

This chapter describes what a network driver does to set up its interface object, to handle I/O, and to perform its other tasks. Follow the CDC Ethernet driver provided at [http://www.opensource.apple.com/darwinsource/tarballs/apsl/AppleUSBCDCDriver-314.4.1.tar.gz](http://www.opensource.apple.com/darwinsource/tarballs/apsl/AppleUSBCDCDriver-314.4.1.tar.gz) for specific examples of how to implement the functionality required of a network driver. In particular this document will refer to the functions in `AppleUSBCDCEMData.cpp`.

Before diving into the specifics of what you need to be do to write a network driver, it may be helpful to see the basic functions which you need to override. These descriptions are meant to give you an idea of what is entailed in creating a very simple network driver.

**`start`**
: The `start` function should initialize the device to a working state. It also needs to create a network object and make it visible to the networking stack as an interface.

**`stop`**
: The `stop` function must free anything allocated in `start` and also release the network object created in `start`.

**`enable`**
: As mentioned in [Tips on Bringing Up a UNIX Network Driver](Tips%20on%20Bringing%20Up%20a%20UNIX%20Network%20Driver.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjtfvbuqmrqgmwviubz), the `enable` function is run when the system sets the driver’s status to `up`. This function is also responsible for starting the hardware’s transmit and receive capabilities. It should inform the system about the link status of the hardware.

**`disable`**
: The `disable` function releases anything allocated, and stops any functions started in `enable`.

**`getHardwareAddress`**
: The `getHardwareAddress` function returns the MAC address of the network device.

**`outputPacket`**
: The `outputPacket` function sends the packet to the hardware for transmission. It will be called from multiple threads, so it needs to be thread-safe.

Each of these functions are described in more depth further in this chapter.

A network driver’s `start` function is responsible for setting up the resources the driver needs all the time, whether the driver is enabled or disabled. These include the network interface object, a work loop, and an output queue, along with whatever specific resources the driver needs. In addition, the driver should retain its provider nub (that is, the nub for the bus it is attached to, such as an IOUSBDevice nub). The `stop` function reverses all this, releasing the nub and disposing of any resources created in `start`. See the example driver for samples of these two functions.

The `start` function is typically not the place for a driver to allocate its transmit and receive buffers and other such runtime resources that are needed only while the driver is enabled and handling network traffic. Creation and disposal of these resources is managed by the `enable` and `disable` functions, described in [Enabling and Disabling the Driver](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjtfvbuqmrqgqwviucykjcummjqgm).

You invoke the `start` function with a single argument, the nub of the hardware device that your ethernet controller is connected to. The driver should do three things with the nub: verify that it is of the appropriate class, retain a reference to it, and open it in order to access its services.

Your driver has two options before returning from the `start` function. If you close the nub at the end of the `start` function, then you must reopen it in the `enable` function. However, you also have the option to leave the nub open, so that it will be ready to use in the `enable` function. It is recommended that the former technique be used, but because a network driver is rarely “downed,” either technique is acceptable. The sample code uses the latter method.

IONetworkController, the superclass of all network drivers, defines the `outputPacket` function for packet transmission. This function is typically called indirectly by the network interface through the network family’s standard queuing mechanism, defined by IOOutputQueue and its subclasses. A driver can choose to have it invoked directly by the network interface, however, and implement its own internal queuing mechanism.

A driver’s output queue is created by the `createOutputQueue` function. The network driver superclass, IONetworkController, invokes this function automatically on startup. The driver should override this function to create an instance of an IOOutputQueue subclass suitable for the driver, or not override it at all if the driver performs its own queuing—in which case the network interface will pass outgoing packets directly to the driver.

The simplest IOOuputQueue subclass to use is IOGatedOutputQueue. This class queues packets using a lock and dequeues them one at a time using a command gate on the driver’s work loop. It invokes `outputPacket` once for each packet, breaking up `mbuf_t` packet chains so that the driver doesn’t have to handle them. Using the work loop means that transmit and receive operations are mutually exclusive. If your network hardware has completely distinct transmit and receive engines, using an IOGatedOutputQueue object may not be the most efficient option. Even so, it makes bringing up a driver quite simple, as you do not have to worry about locking while you establish control of the hardware itself.

If your network hardware supports multithreaded access, as it does when the transmit and receive engines are distinct, you may want to use an IOBasicOutputQueue instead. This class is the actually the superclass of IOGatedOutputQueue, and it defines the locking mechanism that IOGatedOutputQueue uses. For dequeuing, however, it negotiates multiple queuing threads so that only a single thread at a time dequeues packets and invokes the driver’s `outputPacket` function. This queue subclass also breaks up `mbuf_t` packet chains for the driver. Because dequeuing isn’t synchronized with the work loop, however, both transmission and reception can occur at the same time.

If a driver performs queuing internally, it doesn’t override `createOutputQueue`, and it implements its own queuing mechanism. If you are porting a driver that already performs its own output locking, for example, you will probably choose this option. In this case, when the network interface needs to transmit packets, it invokes the driver’s `outputPacket` function directly. The driver is then responsible for all locking of its internal queue and related data, for handling stall conditions, and further for handling `mbuf_t` packet chains. The output queue classes guarantee that a single packet at a time is passed to `outputPacket`; this is not the case when the driver forgoes using an output queue object.

Another option a driver has is to create its own subclass of IOOutputQueue. See the class reference documentation and the source code for more information.

As with any driver, a network driver is responsible for creating its nub. A network nub is an instance of a subclass of IONetworkInterface. Each type of network controller has a corresponding subclass of IONetworkInterface; an IOEthernetController, for example, uses an IOEthernetInterface. Creating the network interface is implemented by the driver’s superclass; all the driver need do is call the `attachInterface` function and implement a few auxiliary functions. If the driver includes a custom subclass of the network interface class, it can override `createInterface` to create an instance of the custom subclass rather than the default class.

The `attachInterface` function takes two parameters: a pointer to the network interface object, which is filled by the function, and an optional “register with the network stacks” flag. This flag is `true` by default, meaning that the interface object will be registered with the DLIL, that the driver’s `enable` function may be invoked during startup and that the driver may receive requests to transmit packets before `attachInterface` returns (and before `start` completes). If your driver needs to perform additional initialization, you can pass `false` to delay registering with the network stacks. If you do this, your driver must invoke the interface’s `registerService` function when it becomes ready to handle network traffic.

Because a network interface can’t be reconfigured after it registers itself with the BSD network stack, it invokes a callback on the driver from the `attachInterface` function. The callback is `configureInterface`, and the driver can implement it to set up maximum transfer sizes, filter tap modes, and other such settings as described in the IONetworkInterface reference documentation. Network drivers typically use this function to get their references to the statistics structures maintained by the network interface before any network traffic comes by. (See [Gathering Network Statistics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjtfvbuqmrqgqwviucykjcummjqgy) below for information on how to do this.)

For ethernet drivers, another function related to setting up the interface is `getHardwareAddress`, which the interface object invokes in order to register the ethernet address with the BSD network stack. Before invoking `attachInterface`, the driver should determine in the `start` function what the hardware address is, and implement `getHardwareAddress` to provide this address on request. Other networking protocols may require a similar function.

This section presents some useful functions that will be explained more fully in later versions of this book.

A network driver overrides a number of IONetworkController functions in order to advertise its capabilities and restrictions. Some of these functions, and their uses, are:

- `setMaxTransferUnit`, which allows clients to set the largest single packet size to transfer.
- `getPacketBufferConstraints`, which informs the driver’s superclass of alignment constraints for packet buffers.
- `getVendorString`, which provides the vendor name for the hardware controller that the driver is operating.
- `getModelString`, which provides the model name for the hardware controller that the driver is operating.

When a network interface is brought up—for example, using the `ifconfig` command—the driver’s `enable` function is invoked. This function is responsible for preparing the driver to transmit and receive packets. Here are a few of the operations typically performed in `enable`:

- Opening the driver’s provider nub (if the nub was closed in the `start` function).
- Creating any resources needed by the driver for operation, such as hardware-specific transmit and receive buffers, memory cursors for managing scatter/gather lists, and event sources for the work loop.
- Resetting the hardware so that it’s ready to transmit and receive packets.
- Starting I/O by enabling hardware interrupts as well as interrupt event sources and setting timer event sources, restarting the output queue (if the driver uses one), and then starting the transmit and receive engines on the hardware.

The `disable` function must reverse this process, disabling what was enabled, shutting down what was started, disposing of resources that were created, and, if necessary, closing the provider nub. The driver should also reset the hardware when disabling, to leave it in a known state.

You invoke the `enable` and `disable` functions within a synchronized context through the driver’s superclass, using an IOCommandGate on the driver’s work loop. These functions are intended to be overridden, and not directly invoked.

Both `enable` and `disable` are invoked with the provider nub the driver was originally started with. The `enable` function is responsible for invoking `open` on the nub, returning a failure result if it can’t open the nub. Similarly, `disable` must invoke `close` on the nub. Because network driver code can be running in multiple threads, however, the driver should implement a mutex. The lock should ensure that the `enable` function is allowed to run only once at a time, and that the `disable` function can run only after the `enable` function. The sample driver uses a Boolean variable, `fNetifEnabled`, as the lock.

In order to preserve kernel resources, a driver should never consume more system memory than necessary. This means that the driver should delay creating resources until they’re actually needed, as when the driver becomes active, and should dispose of those resources when it becomes inactive. Such resources typically include any hardware-specific transmit and receive buffers, the BSD `mbuf_t` structures used to pass packets up and down, memory cursor objects used to manage scatter/gather lists based on the `mbuf_t` structures, and any event sources needed for operation.

Hardware-specific resources are necessarily outside the scope of this document. Whatever the hardware-specific resources are, however, they will typically include a receive buffer that contains `mbuf_t` structures. Your driver can use its network interface object to allocate and free these structures through the `allocatePacket` and `freePacket` functions defined by IONetworkController.

Memory cursors, represented by the IOMBufMemoryCursor group of classes, manage the translation between `mbuf_t` structures and scatter/gather lists used by the hardware. Specific classes are available to handle data in big-endian, little-endian, or CPU-native byte order, and to handle data used with DBDMA engines. Your driver will typically create one or more memory cursors, depending on whether it’s single- or multithreaded and whether the transmit and receive buffers used by hardware are similar or different.

To start I/O, the `enable` function should enable the interrupt and timer event sources and then enable any hardware-specific interrupts. Following this, it should start up the output queue (if it has one) using IOOutputQueue’s `setCapacity` and `start` functions. Finally, it should start any I/O engines on the hardware.

The `disable` function stops I/O by roughly reversing this process. It should disable hardware-specific interrupts, disable the interrupt event source and cancel any pending timeout. It should then stop the I/O engines and reset the hardware if necessary. Then, it must stop and flush the output queue by invoking its `stop` function, setting its capacity to zero with `setCapacity`, and invoking `flush`.

Everything that has been covered up to now is essentially support for the real purpose of a network driver: to send and receive packets through the network controller. The network family specifies the means for a driver to get an output request from the network interface object, and to hand received packets up to it, as well as defining data structures for gathering statistics. Additional functions defined by the network interface and controller superclasses provide support for managing packet buffers, and the `mbuf_t` memory cursor classes aid in the use of scatter/gather lists based on those buffers.

A network driver’s entry point for transmission is the `outputPacket` function. This function is invoked either by an IOOutputQueue or by the network interface directly. Depending on the type of queue used (see [Setting up Output Queuing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjtfvbuqmrqgqwueqkbjbdesqsj) above), this function may or may not be invoked within the protected context of the driver’s work loop.

The sole argument to `outputPacket` is an `mbuf_t` for the packet or packets to be transmitted. A driver that uses an output queue object is guaranteed to be passed a single-packet `mbuf_t`. A driver that does its own queuing must be able to process a chain of packets in a single `mbuf_t` pointer. The `mbuf_t` passed in becomes the property of the driver.

To actually output the packet or packets, the driver must check its hardware-specific resources and prepare a buffer. Depending on the state of the resources, the driver may need to return a packet status of stalled (`kIOReturnStall`), as when the hardware transmit buffers are all full, or dropped (`kIOReturnDropped`), as when an error occurs in processing the packet. If the driver returns `kIOReturnDropped`, it should also put the `mbuf_t` back into the network stack’s common pool by invoking the superclass’s `freePacket` function.

In order to generate a scatter/gather list for the packet, the driver uses an IOMBufMemoryCursor, invoking its `getPhysicalSegmentsWithCoalesce` function to create a list of physical location/length pairs for the memory segments of the `mbuf_t`. Once it has this information the driver can insert it into the hardware buffers and issue the go-ahead to the hardware controller.

After the packet has been transmitted by the hardware, the driver should reclaim its transmit buffer and put the `mbuf_t` back into the network stack’s common pool by invoking the superclass’s `freePacket` function.

Receiving packets is typically done through an interrupt handler, or possibly a timer for a device that requires polling. In either case, reception is always handled within the protected context of the driver’s work loop

To process incoming packets, the driver must extract the `mbuf_t` structure for each from its hardware receive buffers and pass it up to the network interface object by invoking that object’s `inputPacket` function. For efficient replacement of an `mbuf_t` structure containing a received packet, IONetworkController defines the functions `copyPacket`, `replacePacket`, and `replaceOrCopyPacket`, which performs the most efficient operation based on the size of the received packet. While it is recommended that you use these functions, the example driver does not take advantage of them.

The `inputPacket` function has an optional argument to allow for queueing of multiple packets. If the driver uses input queueing, it must invoke the network interface’s `flushInputQueue` function to ensure that the packets find their way up the network stack.

The network family defines several structures for recording network statistics. If you want your driver to do this, it must get the addresses of these structures from the network interface object and then update the relevant fields during operation.

The structures are available from the network interface object through its `getNetworkData` function. This function takes the name of the relevant network data structure, for which constants are defined by the network interface classes. The constant `kIONetworkStatsKey`, for example, indicates the generic network statistics structure, which contains fields for number of input and output packets, among others.

The `getNetworkData` function returns an IONetworkData object, from which you can retrieve the data buffer address using its `getBuffer` function. Casting the returned pointer to the appropriate type gives your driver direct access to the network data structure.

To indicate what kinds of packet filtering (addressing) a driver supports, it overrides `getPacketFilters`. This function is invoked with a pointer to a bitfield indicating which addressing modes are supported, such as unicast, broadcast, and multicast. The driver’s implementation of this function should set the bits for the modes it supports and return a success code.

In order to support promiscuous and multicast modes, a network driver overrides the `setPromiscuousMode`, `setMulticastMode`, and `setMulticastList` functions defined by IONetworkController. The set-mode functions can be implemented to just set a flag in the driver; actually supporting the modes requires hardware-specific code in the I/O handling functions, of course. `setMulticastList` is invoked with a list of hardware addresses, which the driver should pass down to the hardware.

When a network controller driver starts up, it typically examines its hardware for the media supported and currently active, for example10Base-T and 100Base-T for ethernet. A driver can advertise these media by creating an instance of IONetworkMedium for each one, collecting them in an OSDictionary that it makes available to the network family by invoking the `setMediumDictionary` function defined by IONetworkController.

The driver should also invoke `setCurrentMedium` to establish the current selected medium. Similarly, when the driver notes that the network link has come up or gone down, it should invoke the `setLinkStatus` function to report the status to the network interface object.

[Next](Document%20Revision%20History.md)[Previous](Tips%20on%20Bringing%20Up%20a%20UNIX%20Network%20Driver.md)

