---
title: HBA Device Driver Programming Guide
apple_id: TP40003194
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/SCSIHBADrivers/HBADriverDevelopment/HBADriverDevelopment.html
archived_at: '2026-07-15T07:41:08.303040Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HBA Device Driver Programming Guide](Introduction%20to%20HBA%20Device%20Driver%20Programming%20Guide.md)


[Next](Improving%20Performance.md)[Previous](HBA%20Devices%20and%20I-O%20Processing.md)

# Developing an HBA Driver

This chapter describes how to develop a custom HBA driver.

If you've never developed in-kernel device driver for OS X, be sure to read the documents listed in [Introduction to HBA Device Driver Programming Guide](Introduction%20to%20HBA%20Device%20Driver%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqmjnknltc) to learn about the I/O Kit and how to use Xcode to create a device driver.

To ensure that your driver matches and loads for your device, you need to edit your driver's information property list (`Info.plist` file). The I/O Kit uses the information in this file to match a device with the driver best suited to drive it. Because HBA hardware is represented by one or more `IOPCIDevice` nubs, a custom HBA driver must include the following key-value pair in its `Info.plist` file:

```
<key>IOProviderClass</key>
<string>IOPCIDevice</string>
```

If you're developing an HBA driver to run in a PowerPC-based Macintosh computer, you can use Open Firmware matching to match on some combination of the Open Firmware device properties `name`, `compatible`, `device_type`, or `model`. To do this, use the `IONameMatch` key and supply the appropriate property or properties in a string (or array of strings) as the value, as in this example:

```
<key>IONameMatch</key>
<string>pci1000,626</string>
```

If you're developing an HBA driver to run in an Intel-based Macintosh computer, use standard PCI matching (Open Firmware matching is not available in Intel-based Macintosh computers). PCI matching is based on the values in the PCI configuration space registers listed below (note that some registers, such as revision ID and header type, are not available for matching):

- Vendor and device ID (offsets $00 and $02)
- Subsystem vendor and device ID (offsets $2C and $2E)
- Class code (offset $09)

The PCI family defines four matching keys that you can use to specify combinations of values on which to match. The table below shows these keys and their associated behavior.

| Key | Matching behavior |
| --- | --- |
| `IOPCIMatch` | Matches against the primary vendor and device ID registers or the subsystem vendor and device ID registers. The values of the primary registers are checked first; if there is no match, then the values of the subsystem registers are checked. |
| `IOPCIPrimaryMatch` | Matches against only the primary vendor and device ID registers. |
| `IOPCISecondaryMatch` | Matches against only the subsystem vendor and device ID registers. |
| `IOPCIClassMatch` | Matches against the class code register. |

For several examples of PCI matching, see the "PCI Matching" section in [Writing a Driver for a PCI Device](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingPCIDrivers/pci_device/pci_device.html#//apple_ref/doc/uid/TP30000347). For information on other matching keys, such as `kIOPropertyPhysicalInterconnectLocationKey`, see the documentation for `IOStorageProtocolCharacteristics.h` in _[Device Drivers (Kernel/IOKit) Reference](https://developer.apple.com/documentation/kernel)_.

After your driver is matched to your device and started, you have the opportunity to add to the property list other properties that contain information about the HBA device itself or about its target devices. These properties (like all properties in the `Info.plist` file) are stored in the I/O Registry during the driver's lifetime. This allows other I/O Kit entities to get information about the capabilities of your device. The `IOSCSIParallelInterfaceController` class provides methods your driver can call to add or remove properties (these methods are described in [Set and Remove HBA and Target Device Properties (Optional)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnbnknlto)). It's important to use only these methods to add or remove properties because they protect you from the synchronization issues that can arise when different entities attempt to make changes in the I/O Registry at the same time.

The SCSI Parallel family's `IOSCSIParallelInterfaceController` class contains all the methods you need to develop a custom HBA driver. It's important to emphasize that the SCSI Parallel family handles a great many lower-level details for you, such as the creation of a work loop and various event sources, basic interrupt handling, and, if necessary, the creation and destruction of target device objects.

For the most part, your job consists of subclassing the `IOSCSIParallelInterfaceController` class and implementing its pure virtual methods to process I/O and report information specific to your hardware. The `IOSCSIParallelInterfaceController` class also contains methods you can implement to perform tasks, such as managing target devices and handling interrupts, and methods you can call to get information and set various properties. The following sections describe the required and optional tasks HBA drivers perform and the `IOSCSIParallelInterfaceController` methods associated with them.

After you've succeeded in developing a driver that communicates with your device, be sure to read [Improving Performance](Improving%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnjnknltc) to learn about ways to improve your driver's performance in OS X.

Custom HBA drivers do not implement the I/O Kit `init` method. Instead, the `IOSCSIParallelInterfaceController` object does some initial setup work (such as getting a work loop and updating I/O Registry properties) and then it calls the `InitializeController` method on your subclass. In your implementation of this method, you should perform any required hardware initialization, resource allocation, and hardware interrogation.

As you design the implementation of the `InitializeController` method, be aware that you do not need to allocate memory in your subclass to hold per-command or per-target information. For example, some HBA devices keep track of the mapping between the worldwide node name and the target device or information about negotiation speeds. Instead of allocating memory to hold such information in your `InitializeController` method, you should use the report methods to tell the `IOSCSIParallelInterfaceController` superclass how much space you need. Then, when the `IOSCSIParallelInterfaceController` object creates target-device and task objects, it will also allocate enough memory to hold the information you need to keep. (For more information on the report methods, see [Report Device-Specific Information (Required)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnbnknltk).)

If there is information you need to store that is specific to the HBA device itself, however, you can allocate memory for it in the `InitializeController` method. Your driver might also need to allocate a small amount of memory to use for non-task communication with target devices. For example, some HBA drivers send to target devices auxiliary requests or negotiation requests that can't be encapsulated in I/O request objects.

In your implementation of the `InitializeController` method you should also query the hardware to get information you need, such as the highest supported device ID and the initiator ID. Your driver might need other data as well, but it will be required to report the initiator ID and the highest supported device ID and logical unit number (LUN) to its superclass (see [Report Device-Specific Information (Required)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnbnknltk) for the methods you use to supply this data).

After you've initialized your HBA device, the `IOSCSIParallelInterfaceController` object requests some information from your driver. To provide this information, your driver must implement the following methods:

- `ReportInitiatorIdentifier`

  The `IOSCSIParallelInterfaceController` object calls this method to get the SCSI identifier of the initiator (your HBA device). The initiator ID is considered reserved and no target devices can be created with that ID.
- `ReportHighestSupportedDeviceID`

  In this method, your HBA driver must return the highest device ID it supports. The `IOSCSIParallelInterfaceController` object uses the value you return to determine the last ID to process when, for example, it scans for target devices.
- `ReportMaximumTaskCount`

  In this method, return the maximum number of outstanding tasks your HBA device can process. The `IOSCSIParallelInterfaceController` object uses this value both to allocate the appropriate number of task objects and to avoid sending a new task when your driver is already processing the maximum number of tasks.
- `ReportHBASpecificTaskDataSize`

  If your HBA driver needs to keep track of some data for each task it processes, it can tell its superclass to allocate space for that data in each task object. This relieves your driver of the responsibility of creating and maintaining the memory to hold per-task data, such as a scatter-gather list.
- `ReportHBASpecificDeviceDataSize`

  If your HBA driver needs to keep track of some data for each target device attached to it, it can tell its superclass to allocate space for that data in each `IOSCSIParallelInterfaceDevice` object. Your driver might want to store data such as negotiation speeds, the worldwide port name, or a destination ID.
- `DoesHBAPerformDeviceManagement`

  Many HBAs, typically Fibre Channel and SAS HBAs, are capable of discovering and managing the devices attached to them. Other HBAs, such as generic parallel SCSI HBAs, know how many devices they can support, but do not manage those devices in any way. All HBA drivers must implement the `DoesHBAPerformDeviceManagement` method to state whether they intend to manage the target devices attached to them.

  If your HBA driver returns `true` in this method, it means that target device objects will be created (and destroyed) only by your HBA driver, not by the superclass. Your HBA driver must then call the `IOSCSIParallelInterfaceController` methods that create and destroy target device objects (described in [Create, Initialize, and Destroy Target Device Objects (Optional)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnbnknlte)).

  If your HBA does _not_ perform device management, you should return `false` in the `DoesHBAPerformDeviceManagement` method, and you do not have to call the methods described in [Create, Initialize, and Destroy Target Device Objects (Optional)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnbnknlte). For these HBAs, the `IOSCSIParallelInterfaceController` takes responsibility for discovering and probing attached devices at boot time. The superclass creates the target device objects and attaches them to the custom HBA driver object in the I/O Registry.
- `ReportHBAHighestLogicalUnitNumber`

  In this method, your driver should return the highest logical unit number your HBA device can address.
- `DoesHBASupportSCSIParallelFeature`

  The superclass calls this method to find out if your HBA device supports a specific SCSI Parallel Interface feature (as defined in the SPI-3 and SPI-4 specifications). Your implementation of this method should examine the specified feature and return `true` if you support it or `false` if you don't.

A driver for an HBA device that manages the target devices attached to it must create and destroy the I/O Kit objects that represent them in the mass storage driver stack. (If your driver manages target devices, be sure to return `true` in your implementation of the required `DoesHBAPerformDeviceManagement` method, described in [Report Device-Specific Information (Required)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnbnknltk).) If your driver does not manage target devices, you can skip the rest of this section and go on to the next section, [Set and Remove HBA and Target Device Properties (Optional)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnbnknlto).

To create target device objects, your driver must call one of the variants of the `CreateTargetForID` method. You cannot override the `CreateTargetForID` methods because the `IOSCSIParallelInterfaceController` object uses them to perform many low-level tasks, such as updating internal states and structures.

The `IOSCSIParallelInterfaceController` class allows a custom HBA driver to create a target device object by passing either the device ID of the target device and a dictionary of its properties or just the device ID. In general, Fibre Channel HBA devices need to supply a dictionary of properties that describe the target device, but most other HBA devices do not. [Table 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnbnknltg) lists the property keys and values that Fibre Channel HBA devices can provide in the `CreateTargetForID` method. For more information about these and other keys used to describe the characteristics of physical interconnect protocols, see the documentation for `IOStorageProtocolCharacteristics.h` in _[Device Drivers (Kernel/IOKit) Reference](https://developer.apple.com/documentation/kernel)_.

__Table 2-1__  Property keys and values for Fibre Channel device objects

| Property key | Required | Value | Type |
| `kIOPropertyFibreChannelNodeWorldWideNameKey` | Yes | Unique 64-bit worldwide name for the device node | `OSData` |
| `kIOPropertyFibreChannelPortWorldWideNameKey` | No | Unique 64-bit worldwide name for the port | `OSData` |
| `kIOPropertyFibreChannelAddressIdentifierKey` | No | The 24-bit address identifier as defined in the Fibre Channel FS (FC-FS) specification | `OSData` |
| `kIOPropertyFibreChannelALPAKey` | No | The 8-bit Arbitrated Loop Physical Address value | `OSData` |

When you call the `CreateTargetForID` method, the `IOSCSIParallelInterfaceController` object creates a new `IOSCSIParallelInterfaceDevice` object to represent the device. This device object performs the I/O Kit `init`, `attach`, and `start` routines. In the mass storage driver stack, the `IOSCSIParallelInterfaceDevice` object transitions between objects in the SCSI Parallel family and objects in the SCSI Architecture Model family.

Because device-specific data is stored in the target device object, the memory for this data is not allocated until the target device object is created. If your HBA driver needs to access that memory to perform set-up tasks for a target object it creates, it should implement the `InitializeTargetForID` method. This method is called by the `IOSCSIParallelInterfaceDevice` object in its `start` method (before the object is registered for matching), when the target device–specific memory is available.

If your driver calls the `CreateTargetForID` method to create target device objects, it must also call the `DestroyTargetForID` method to destroy them. As with the `CreateTargetForID` method, you cannot override the `DestroyTargetForID` method; otherwise you might interfere with the tasks the `IOSCSIParallelInterfaceDevice` object performs in its implementation of the method. When you call the `DestroyTargetForID` method, the specified `IOSCSIParallelInterfaceDevice` object terminates.

To ready your HBA device to accept I/O requests and SCSI commands, you must implement the `StartController` method. The superclass calls the `StartController` method in its own `start` method, after it has retrieved HBA-specific information from your driver and allocated a pool of SCSI parallel task objects.

In your `StartController` method, you might need to enable ports on your hardware, clear pending interrupts, and perform other tasks that put your device in a running state. If your HBA performs device management, you might also scan for target devices in the `StartController` method. If you do this, be aware that the superclass is holding a command gate while in its `start` method. You might find that this prevents you from receiving asynchronous, interrupt-based device-discovery notifications. If you experience this, you can create a separate thread on which to call `CreateTargetForID`.

The most important thing to remember about the `StartController` method is that your driver must be prepared to receive and process I/O requests and commands as soon as the method completes.

During the initialization and starting phases of your driver, you might need to set or remove I/O Registry properties associated with target devices or with the HBA device itself. Instead of using [IORegistryEntry](https://developer.apple.com/documentation/kernel/ioregistryentry) methods to do this directly, you should use the methods the `IOSCSIParallelInterfaceController` class provides. One advantage of using the family-specific methods is that they perform some data validation on the properties you pass in. A more important advantage is that these methods protect you from serialization problems that can occur when different entities attempt to manipulate properties in the I/O Registry at the same time.

Both the `SetTargetProperty` and `SetHBAProperty` methods expect a string containing the property key name and an `OSObject`-derived object containing the value. Some of the valid target property keys are listed in [Table 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnbnknltg); a list of valid HBA property keys is in `SetHBAProperty`. For more information about the values appropriate for these properties, see the header files `IOStorageProtocolCharacteristics.h` and `IOStorageDeviceCharacteristics.h`.

The primary task of a custom HBA driver is to receive SCSI parallel tasks and pass them along to the target devices. To do this your HBA subclass must implement the `ProcessParallelTask` method.

In the `ProcessParallelTask` method, your HBA driver can call `IOSCSIParallelInterfaceController` accessor methods to extract information from the `SCSIParallelTask` object that represents the task. Some of these accessor methods are listed here:

- `GetCommandDescriptorBlock`
- [GetDataBuffer](https://developer.apple.com/documentation/iokit/iostreamlib.h/1810262-getdatabuffer)
- `GetHBADataPointer`
- `GetSCSIParallelFeatureNegotiationCount`

After you've examined the information in the command and processed it as required, you need to send the command out on the bus. Some HBA devices require strict synchronization between sending commands out on the bus and processing the interrupts generated from completed commands; others do not. The `IOSCSIParallelInterfaceController` class supports both types of HBA device by providing mechanisms an HBA driver can use to ensure the level of synchronization its hardware needs. For more information on how to synchronize these events, see [Synchronize Hardware Access](Improving%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnjnknlte).

You must return a valid SCSI service response value from your implementation of the `ProcessParallelTask` method. The following is a list of the SCSI service responses (defined in the header file `SCSITask.h` in the Kernel framework) you can return:

- `kSCSIServiceResponse_Request_In_Process`

  Although this is not one of the standard service responses defined in the SCSI Architecture Model specification, it is the response you should return when an asynchronous command is not yet completed.
- `kSCSIServiceResponse_SERVICE_DELIVERY_OR_TARGET_FAILURE`
- `kSCSIServiceResponse_TASK_COMPLETE`
- `kSCSIServiceResponse_LINK_COMMAND_COMPLETE`
- `kSCSIServiceResponse_FUNCTION_COMPLETE`
- `kSCSIServiceResponse_FUNCTION_REJECTED`

To learn how to handle timeouts, see [Handle Timeouts (Optional)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnbnknlts).

Clients of your HBA driver use the SCSI task management functions (defined in the SCSI Architecture Model 2 specification) to request specific actions. The `IOSCSIParallelInterfaceController` class defines the following pure virtual methods your subclass must implement to perform these actions:

- `AbortTaskRequest`
- `AbortTaskSetRequest`
- `ClearACARequest`
- `ClearTaskSetRequest`
- `LogicalUnitResetRequest`
- `TargetResetRequest`

In your implementation of these methods, you can complete them either synchronously or asynchronously. If you choose to complete them synchronously, your implementation should return the appropriate SCSI service response. You can return any of the service responses listed at the end of [Handle Parallel Tasks (Required)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnbnknltq) _except_ `kSCSIServiceResponse_Request_In_Process`.

If you decide to complete these functions asynchronously, your implementation should return only the `kSCSIServiceResponse_Request_In_Process` service response and then call the appropriate completion method. The `IOSCSIParallelInterfaceController` class defines the following completion methods your driver should implement if it processes SCSI task management functions asynchronously:

- `CompleteAbortTask`
- `CompleteAbortTaskSet`
- `CompleteClearACA`
- `CompleteClearTaskSet`
- `CompleteLogicalUnitReset`
- `CompleteTargetReset`

Because both command completion and timeout management are serialized on the work loop thread, you should serialize the task management your driver performs on the work loop, too. One way to do this is to use a command gate object associated with the work loop to take the work-loop lock before you send the task management request to the target device (you can accomplish this using the `IOCommandGate::runAction` function). In this way, you can avoid receiving a command or task management completion at the same time you send a task management request. The `IOSCSIParallelInterfaceController` class provides the convenient accessor method `GetCommandGate` to get the command gate object associated with the work loop.

SCSI commands usually have a timeout value associated with them. Your driver does not set the command's timeout value (it is set by the object that sent you the command), but it can enable the timer by calling the `SetTimeoutForTask` method. (If you choose, you can also use the `SetTimeoutForTask` method to override the timeout value provided in the task.)

Although some HBA drivers may not need to do anything when a command times out, many drivers need to perform some cleanup and communicate with the hardware. If your driver needs to handle command timeouts in a hardware-specific way, you can implement the `HandleTimeout` method.

When a task times out, the SCSI Parallel family calls the `HandleTimeout` method. The `IOSCSIParallelInterfaceController` class's default implementation of this method merely completes the command with a SCSI task status of `kSCSITaskStatus_TaskTimeoutOccurred` and a SCSI service response of `kSCSIServiceResponse_SERVICE_DELIVERY_OR_TARGET_FAILURE`. If this does not meet your driver's needs, you can implement the `HandleTimeout` method to, for example, clean up HBA-specific data structures associated with the command and abort the command. If the command is already out on the bus, you may have to send an `AbortTaskRequest` command; if not, you may be able to simply remove it from the queue of commands waiting to be sent to the target device.

As described in [The Role of an HBA Device in the Journey of an I/O Request](HBA%20Devices%20and%20I-O%20Processing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqmznknltc), the completion of an I/O request triggers an interrupt that an HBA driver must handle. When the `IOSCSIParallelInterfaceController` object is instantiated, it creates a work loop and registers with it a filter interrupt event source (among other event sources). The interrupt event source includes an action routine that runs on the work-loop thread to handle interrupts. When an interrupt occurs, the action routine calls your HBA driver's `HandleInterruptRequest` method while in the secondary interrupt context (on the work-loop thread with the lock held). Your driver must implement the `HandleInterruptRequest` method to service the interrupt.

Your implementation of the `HandleInterruptRequest` method should be as efficient as possible and never block indefinitely. In particular, this means that you must not allocate memory or create objects in your `HandleInterruptRequest` method (or any methods it calls), because allocation can block for unrestricted periods of time. Be sure to call the `CompleteParallelTask` method when your driver completes the processing of a parallel task.

In your implementation of this required method you should stop accepting commands, but you should not release any resources you may have acquired. This is because you may be called upon to resume accepting commands (with a call to your `StartController` method) at any time.

When the `IOSCSIParallelInterfaceController` object calls your `TerminateController` method, however, it means your subclass object will be destroyed. You must implement this method to shut down all hardware services and release all resources you've acquired.

[Next](Improving%20Performance.md)[Previous](HBA%20Devices%20and%20I-O%20Processing.md)

