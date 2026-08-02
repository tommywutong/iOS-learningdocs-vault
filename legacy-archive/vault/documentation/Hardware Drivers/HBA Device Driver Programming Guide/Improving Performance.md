---
title: HBA Device Driver Programming Guide
apple_id: TP40003194
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/SCSIHBADrivers/HBATipsAndTricks/HBATipsAndTricks.html
archived_at: '2026-07-15T07:41:09.484674Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HBA Device Driver Programming Guide](Introduction%20to%20HBA%20Device%20Driver%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Developing%20an%20HBA%20Driver.md)

# Improving Performance

This chapter describes a few things you can do to enhance the performance of your custom HBA device driver in OS X. You should read this chapter if your hardware has any of the following features:

- Serialization requirements for accessing registers
- An optimum I/O transaction size or a maximum number of tasks it can handle
- Support for interrupt coalescing
- A shared interrupt line

In [The Journey of an I/O Request Through the Mass Storage Stack](HBA%20Devices%20and%20I-O%20Processing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqmznknltc), you learned how an I/O request travels down the mass storage driver stack on the client's thread and how it is completed later by your HBA driver on its work-loop thread. In this model, it's possible for one I/O request to come into your driver at the same time another I/O request is completing. When this is the case, an HBA driver may find itself sending a command out on the bus at the same time it is attempting to handle an incoming interrupt. For some hardware, this situation can cause synchronization problems.

Some HBA devices require special synchronization because, for example, they do not allow simultaneous access to their registers. If your hardware has such a requirement, be sure to synchronize the sending and completing of I/O requests on your driver's work loop.

As described in [Handle Interrupt Requests (Required)](Developing%20an%20HBA%20Driver.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnbnknltc), the `IOSCSIParallelInterfaceController` object calls your `HandleInterruptRequest` method in the secondary interrupt context, with the work-loop lock held. To synchronize the issuing of a command with your interrupt handling, therefore, you need to execute the most sensitive code with the lock held. One way to do this is to put the sensitive, register-access code in a separate method and pass it to a command-gate object to run in its `runAction` routine. (For more information on the `IOCommandGate::runAction` function, see the documentation for `IOCommandGate` in _[Device Drivers (Kernel/IOKit) Reference](https://developer.apple.com/documentation/kernel)_.) Because a command gate object takes the work-loop lock before running its action routine, no other event sources on the same work loop (such as an interrupt event source) can run at the same time. Note that you do not need to create your own command gate. Instead, you can use the `GetCommandGate` accessor method to get a pointer to the command gate created by the `IOSCSIParallelInterfaceController` object.

If you do need to synchronize these tasks, be sure to streamline all code that executes while a lock is held. In particular, you should never allocate memory or create objects while the command gate holds the lock, because these tasks may block. The gated code should do as little work as possible to reduce potential contention on the work loop and to enhance the performance of your driver.

To achieve the best performance, you should specify the maximum I/O transaction size your hardware can handle. Given this information, the system can send to your hardware I/O requests of the appropriate size and this can increase your driver's throughput.

Information about maximum I/O transaction size is static and belongs in the I/O Registry, where other I/O Kit objects, such as other entities in the mass storage driver stack, can find it. The `IOKitKeys.h` header file in the Kernel framework defines eight keys you can use to add this information to your driver's `Info.plist` file (each key requires a value of type `OSNumber`). Table 3-1 lists these keys and whether they are required.

__Table 3-1__  I/O transaction-size keys

| Key | Required | Description |
| `IOMaximumSegmentCountRead` | Yes | Maximum number of physically disjoint (non-contiguous) segments that can be processed on a per read I/O basis. |
| `IOMaximumSegmentCountWrite` | Yes | Maximum number of physically disjoint (non-contiguous) segments that can be processed on a per write I/O basis. |
| `IOMaximumSegmentByteCountRead` | Yes | Maximum size in bytes for each physically disjoint (non-contiguous) segment. |
| `IOMaximumSegmentByteCountWrite` | Yes | Maximum size in bytes for each physically disjoint (non-contiguous) segment. |
| `IOMaximumByteCountRead` | No | For most devices, this value is equal to the product of the values of the `IOMaximumSegmentByteCountRead` and `IOMaximumSegmentCountRead` keys. |
| `IOMaximumByteCountWrite` | No | For most devices, this value is equal to the product of the values of the `IOMaximumSegmentByteCountWrite` and `IOMaximumSegmentCountWrite` keys. |
| `IOMaximumBlockCountRead` | No | If your hardware does not require this value, do not use this key. |
| `IOMaximumBlockCountWrite` | No | If your hardware does not require this value, do not use this key. |

To achieve the best overall system performance while your HBA driver is running, you should report a reasonable maximum task count in the `ReportMaximumTaskCount` method. As described in [Report Device-Specific Information (Required)](Developing%20an%20HBA%20Driver.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnbnknltk), you use this method to report the maximum number of outstanding tasks your HBA device can process. Although you should never return a number greater than your device's supported maximum task count (if it defines one), you may be able to improve system performance by reporting a number that balances the performance of your driver with that of the system as a whole.

The `IOSCSIParallelInterfaceController` class uses the number you return in the `ReportMaximumTaskCount` method to allocate an appropriate number of `SCSIParallelTask` objects. It's a good idea to run I/O tests on your HBA driver to find out if this number of preallocated objects is too large (making your driver's footprint larger than necessary and degrading system performance) or too small (causing your driver to block on I/O completions too often and degrading driver performance). Because overall system performance affects your driver's users, it's recommended that you find an optimum maximum task count value that allows your driver to be a good citizen in OS X.

On other platforms, you may be accustomed to performing interrupt coalescing in your HBA driver. If, for example, your driver tends to perform numerous very small I/O transactions, it might make sense to wait for several completion interrupts instead of processing each completion as it occurs. Although batch-processing of I/O completions can increase the number of I/O operations per second, it can degrade I/O throughput. This may be a trade-off you're willing to accept, but you should be aware of the advantages and disadvantages of interrupt coalescing in OS X.

OS X is more likely to process I/O transactions synchronously than asynchronously. When the system does process I/O transactions asynchronously, it is more likely to process large transactions (for example, a megabyte in size), which are not good candidates for batch processing. Although it may seem counterintuitive, it's usually better to avoid interrupt coalescing in your OS X HBA driver and instead handle I/O transactions separately. As with all performance decisions, however, you should test this with your specific hardware and driver and design accordingly.

It's important not to assume that your device has its own, dedicated interrupt line. For example, an expansion chassis may have a shared interrupt line and sometimes two PCI card slots can share an interrupt line. Another common example is an HBA card that is a multifunction PCI card. This type of card may have only one chip on it, but that chip can have multiple functions (also called devices). When the I/O Kit discovers such hardware, it creates an independent [IOPCIDevice](https://developer.apple.com/documentation/kernel/iopcidevice) object to represent each function in the I/O Registry. Each of these `IOPCIDevice` objects is matched by a separate `IOSCSIParallelInterfaceDevice` object (and, if one exists, a separate instance of a custom HBA driver). Although each function has its own driver, these functions might share a single interrupt line on the card itself. When this is the case, more than one function can assert the shared interrupt line when it needs work to be done. This causes the interrupt controller to call each driver's interrupt-handling routine in turn to find the right one to handle the interrupt.

The I/O Kit provides the [IOFilterInterruptEventSource](https://developer.apple.com/documentation/kernel/iofilterinterrupteventsource) class (a subclass of [IOInterruptEventSource](https://developer.apple.com/documentation/kernel/iointerrupteventsource)) to allow drivers to handle shared interrupts in a safe way. In addition to the action completion routine used to handle the interrupt, the `IOFilterInterruptEventSource` class defines a callback function that gets called in each driver sharing the interrupt line. Each driver implements this function as a filter, checking to see if the interrupt is indeed for it and responding accordingly. If a driver returns `true` in its filter routine, the I/O Kit automatically starts that driver's interrupt handler on its work loop and the interrupt remains disabled in hardware until the interrupt handler returns.

When the interrupt controller disables the interrupt line after finding and scheduling the correct driver's interrupt handling routine, no other device sharing that line can get its work done until the line is re-enabled. This can cause large interrupt latencies. You may be able to reduce these latencies if your hardware allows a driver to disable interrupts at the source (in other words, on the card).

The `IOSCSIParallelInterfaceController` class defines the `FilterInterruptRequest` method to allow the drivers of such hardware to disable interrupts and schedule their own interrupt handlers. If your hardware does not allow a driver to disable interrupts at the source, you should not implement the `FilterInterruptRequest` method. Instead, you should rely on the default implementation of this method, which returns `true`. This causes the interrupt controller to schedule the appropriate interrupt handler on the work loop and disable the interrupt line, as described above.

In your implementation of the `FilterInterruptRequest` method, you must first determine if the interrupt is for you. If it is not for you, you must allow the interrupt controller to call other drivers and allow them the chance to handle the interrupt. In this case, your implementation should immediately return `false`.

If the interrupt is for you, you must do the following in your `FilterInterruptRequest` method:

1. Disable interrupts for the device.
2. Call the `SignalInterrupt` method. This method schedules your driver's `HandleInterruptRequest` method on the work loop without disabling the interrupt line.
3. Return `false`.

Then, in your `HandleInterruptRequest` method, you must:

1. Clear the hardware condition that raised the interrupt.
2. Process the interrupt and complete the I/O request.
3. Re-enable interrupts for the device.

[Next](Document%20Revision%20History.md)[Previous](Developing%20an%20HBA%20Driver.md)

