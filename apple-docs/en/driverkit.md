---
title: DriverKit
framework: DriverKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [DriverKit 19.0+, iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/driverkit
source_url: 'https://developer.apple.com/documentation/driverkit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/driverkit.json'
content_hash: 'sha256:db6fa919d528f993'
translated: false
---

> Navigation: [Technologies](technologies.md)

# DriverKit

<sub>Framework</sub>

Develop device drivers that run in user space.

## Overview

The DriverKit framework defines the fundamental behaviors for device drivers in macOS and iPadOS. The C++ classes of this framework define your driver’s basic structure, and provide support for handling events and allocating memory. This framework also supports appropriate types for examining the numbers, strings, and other types of data in your driver’s I/O registry entry. Other frameworks, such as [USBDriverKit](usbdriverkit.md), [HIDDriverKit](hiddriverkit.md), [NetworkingDriverKit](networkingdriverkit.md), [PCIDriverKit](pcidriverkit.md), [SerialDriverKit](serialdriverkit.md), and [AudioDriverKit](audiodriverkit.md), provide the specific behaviors you need to support different types of devices.

The drivers you build with DriverKit run in user space, rather than as kernel extensions, which improves system stability and security. You create your driver as an app extension and deliver it inside your existing app.

In macOS, use the [System Extensions](systemextensions.md) framework to install and upgrade your driver. In iPadOS, the system automatically discovers and upgrades drivers along with their host apps.

> [!note] Note
> The base DriverKit framework is available in macOS for Apple silicon and Intel-based Mac computers, and in iPadOS for devices with an M-series chip. The availability of family frameworks like [USBDriverKit](usbdriverkit.md) and [AudioDriverKit](audiodriverkit.md) varies by platform.

## Topics

### Essentials

- [Implementing drivers, system extensions, and kexts](kernel/implementing_drivers_system_extensions_and_kexts.md) — Create drivers and system extensions to communicate with hardware and provide low-level services, and only use kernel extensions for a few tasks. 
- [Creating drivers for iPadOS](driverkit/creating-drivers-for-ipados.md) — Bring your drivers to iPadOS by using the platform’s DriverKit support.

### Entitlements

- [Requesting Entitlements for DriverKit Development](driverkit/requesting-entitlements-for-driverkit-development.md) — Request the entitlement for DriverKit development, and request other entitlements your driver needs to interact with specific devices and interfaces.
- [com.apple.developer.driverkit](bundleresources/entitlements/com.apple.developer.driverkit.md) — A Boolean value that indicates whether your extension has permission to run as a user-space driver.
- [com.apple.developer.driverkit.userclient-access](bundleresources/entitlements/com.apple.developer.driverkit.userclient-access.md) — An array of strings that represent macOS driver extensions that may communicate with other DriverKit services.
- [com.apple.developer.driverkit.allow-any-userclient-access](bundleresources/entitlements/com.apple.developer.driverkit.allow-any-userclient-access.md) — A Boolean value that determines whether a macOS driver accepts user client connections from any application.
- [Communicates with Drivers](bundleresources/entitlements/com.apple.developer.driverkit.communicates-with-drivers.md) — A Boolean value that indicates whether an iPadOS app can communicate with drivers.
- [DriverKit Allow Third Party User Clients](bundleresources/entitlements/com.apple.developer.driverkit.allow-third-party-userclients.md) — A Boolean value that indicates whether an iPadOS driver accepts calls from third-party user clients.

### Samples

- [DriverKit sample code](driverkit/driverkit-sample-code.md) — Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.

### Services

- [Creating a Driver Using the DriverKit SDK](driverkit/creating-a-driver-using-the-driverkit-sdk.md) — Create a driver that supports proprietary features of your company’s hardware devices.
- [Debugging and testing system extensions](driverkit/debugging-and-testing-system-extensions.md) — Debug your system extensions by temporarily disabling the security checks that macOS performs during the installation process.
- [IOService](driverkit/ioservice.md) — The base class for managing the setup and registration of your driver.

### Event management

- [IODispatchQueue](driverkit/iodispatchqueue.md) — An object that manages the serial execution of blocks.
- [IOInterruptDispatchSource](driverkit/iointerruptdispatchsource.md) — A dispatch source that reports hardware-related interrupt events to your driver.
- [IOTimerDispatchSource](driverkit/iotimerdispatchsource.md) — A dispatch source that notifies your driver at a specific time.
- [IODataQueueDispatchSource](driverkit/iodataqueuedispatchsource.md) — A dispatch source that manages a shared-memory data queue.
- [IODispatchSource](driverkit/iodispatchsource.md) — The common base class for dispatch sources.
- [OSAction](driverkit/osaction.md) — An object that executes your driver’s custom behavior.

### Memory management

- [IOBufferMemoryDescriptor](driverkit/iobuffermemorydescriptor.md) — A memory buffer allocated in the caller’s address space.
- [IOMemoryDescriptor](driverkit/iomemorydescriptor.md) — The base class for describing a location in memory.
- [IOMemoryMap](driverkit/iomemorymap.md) — A reference to an existing block of memory in the current process or in a different process.
- [Memory Utilities](driverkit/memory-utilities.md) — Allocate and deallocate memory and manage memory pointers in different address spaces.

### Registry data types

- [OSArray](driverkit/osarray.md) — A container for an ordered, random-access collection of objects.
- [OSDictionary](driverkit/osdictionary.md) — A container for a collection with elements that are key-value pairs.
- [OSBoolean](driverkit/osboolean.md) — A container for a true or false value.
- [OSData](driverkit/osdata.md) — A container for untyped data.
- [OSNumber](driverkit/osnumber.md) — A container for an integer value.
- [OSString](driverkit/osstring.md) — A container for managing an array of characters.
- [OSSerialization](driverkit/osserialization.md) — A container for one or more objects, serialized in a binary data format that is suitable for messaging.
- [OSCollection](driverkit/oscollection.md) — The base class for DriverKit collection objects.
- [OSContainer](driverkit/oscontainer.md) — The base class for DriverKit data objects.
- [OSObject](driverkit/osobject.md) — The base class for DriverKit objects
- [OSSymbol](driverkit/ossymbol.md) — A container for managing an array of characters.
- [IOFixed](driverkit/iofixed.md) — A fixed-point number.

### External drivers

- [IOUserClient](driverkit/iouserclient.md) — A connection to another service that the system manages.
- [IOUserServer](driverkit/iouserserver.md) — A system-managed service.
- [com.apple.developer.driverkit.userclient-access](bundleresources/entitlements/com.apple.developer.driverkit.userclient-access.md) — An array of strings that represent macOS driver extensions that may communicate with other DriverKit services.
- [Communicating between a DriverKit extension and a client app](driverkit/communicating-between-a-driverkit-extension-and-a-client-app.md) — Send and receive different kinds of data securely by validating inputs and asynchronously by storing and using a callback.

### Runtime support

- [OSDynamicCast](driverkit/osdynamiccast.md) — Casts an object safely to the specified type, if possible.
- [OSRequiredCast](driverkit/osrequiredcast.md) — Casts the object to the specified type, stopping the process if the object isn’t of the correct type.
- [IMPL](driverkit/impl.md) — Tells the system that the superclass implementation of this method runs in the kernel.
- [TYPE](driverkit/type.md) — Annotates a method declaration to indicate that it conforms to an existing method signature.
- [QUEUENAME](driverkit/queuename.md) — Tells the system to execute a method on the dispatch queue with the specified name.
- [SUPERDISPATCH](driverkit/superdispatch.md) — Tells the system to execute the superclass’ implementation of the current method in the kernel.
- [IIG_KERNEL](driverkit/iig_kernel.md) — Tells the system that the class or method runs inside the kernel.
- [LOCAL](driverkit/local.md) — Tells the system that the method runs locally in the driver extension’s process space.
- [LOCALONLY](driverkit/localonly.md) — Tells the system that the class or method runs locally in the driver extension’s process space.
- [Error Codes](driverkit/error-codes.md) — Determine the reason an operation fails.
- [C++ Runtime Support](driverkit/c-runtime-support.md) — Examine low-level types that DriverKit uses to support kernel-level operations.

### Classes

- [IOHistogramReporter](driverkit/iohistogramreporter.md)
- [IOReportLegend](driverkit/ioreportlegend.md)
- [IOReporter](driverkit/ioreporter.md)
- [IOServiceStateNotificationDispatchSource](driverkit/ioservicestatenotificationdispatchsource.md)
- [IOSimpleReporter](driverkit/iosimplereporter.md)
- [IOStateReporter](driverkit/iostatereporter.md)
- [OSBundle](driverkit/osbundle.md)
- [OSMappedFile](driverkit/osmappedfile.md)
- [IOEventLink](driverkit/ioeventlink.md)
- [IOExtensiblePaniclog](driverkit/ioextensiblepaniclog.md)
- [IOWorkGroup](driverkit/ioworkgroup.md)

### Reference

- [DriverKit Structures](driverkit/driverkit-structures.md)
- [DriverKit Enumerations](driverkit/driverkit-enumerations.md)
- [DriverKit Constants](driverkit/driverkit-constants.md)
- [DriverKit Functions](driverkit/driverkit-functions.md)
- [DriverKit Data Types](driverkit/driverkit-data-types.md)
- [DriverKit Namespaces](driverkit/driverkit-namespaces.md)

### Macros

- [Macros](driverkit/driverkit-macros.md)
- [IOKIT](driverkit/iokit.md)
- [IOPhysSize](driverkit/iophyssize.md)
- [IOPhysical32](driverkit/iophysical32.md)
- [IO_NULL_VM_TASK](driverkit/io_null_vm_task.md)
- [IO_OBJECT_NULL](driverkit/io_object_null.md)
- [PRIIOByteCount](driverkit/priiobytecount.md)
- [SERIALIZABLE](driverkit/serializable.md)
- [kIOConfigOrderKey](driverkit/kioconfigorderkey.md)
- [kIOPropertyHashTypeKey](driverkit/kiopropertyhashtypekey.md)
- [kIOPropertySHA3256Key](driverkit/kiopropertysha3256key.md)
- [kIOPropertySHA3384Key](driverkit/kiopropertysha3384key.md)
- [kIOPropertySHA3512Key](driverkit/kiopropertysha3512key.md)
- [kIOUserPlatformFunctionHandlerGet](driverkit/kiouserplatformfunctionhandlerget.md)
- [kIOUserResourcesSetPropertyKey](driverkit/kiouserresourcessetpropertykey.md)
- [kIOUserServrMaxExitReasonLength](driverkit/kiouserservrmaxexitreasonlength.md)
- [kIOUserServrMaxModulePathLength](driverkit/kiouserservrmaxmodulepathlength.md)
- [kIOUserServrMaxPanicReasonLength](driverkit/kiouserservrmaxpanicreasonlength.md)
- [queue_extend_first](driverkit/queue_extend_first.md)
- [queue_extend_last](driverkit/queue_extend_last.md)

### Structures

- [IONamedValue](driverkit/ionamedvalue.md)
- [IOPhysicalRange](driverkit/iophysicalrange.md)
- [IOVirtualRange](driverkit/iovirtualrange.md)

### Functions

- [IOSysCtlByName](driverkit/iosysctlbyname.md)
- [getpid](driverkit/getpid.md)

### Enumeration Cases

- [kIOConnectMethodVarOutputSize](driverkit/kioconnectmethodvaroutputsize.md)
- [kIOEventLinkAssociateCurrentThread](driverkit/kioeventlinkassociatecurrentthread.md)
- [kIOEventLinkAssociateOnWait](driverkit/kioeventlinkassociateonwait.md)
- [kIOEventLinkClockMachAbsoluteTime](driverkit/kioeventlinkclockmachabsolutetime.md)
- [kIOEventLinkMaxNameLength](driverkit/kioeventlinkmaxnamelength.md)
- [kIOExtensiblePaniclogOptionsNone](driverkit/kioextensiblepaniclogoptionsnone.md)
- [kIOExtensiblePaniclogOptionsWithBuffer](driverkit/kioextensiblepaniclogoptionswithbuffer.md)
- [kIOMemoryMapCacheModePostedCombinedReordered](driverkit/kiomemorymapcachemodepostedcombinedreordered.md)
- [kIORPCMessageDeepSerialization](driverkit/kiorpcmessagedeepserialization.md)
- [kIOServicePMAssertionCPUBit](driverkit/kioservicepmassertioncpubit.md) — kIOServicePMAssertionCPUBit When set, PM kernel will prefer to leave the CPU and core hardware running in “Dark Wake” state, instead of sleeping.
- [kIOServicePMAssertionForceFullWakeupBit](driverkit/kioservicepmassertionforcefullwakeupbit.md) — kIOServicePMAssertionForceFullWakeupBit When set, the system will immediately do a full wakeup after going to sleep.
- [kIOServicePowerCapabilityLPW](driverkit/kioservicepowercapabilitylpw.md)
- [kIOWorkGroupMaxNameLength](driverkit/kioworkgroupmaxnamelength.md)
- [kSCSICmd_ATA_PASS_THROUGH](driverkit/kscsicmd_ata_pass_through.md)
- [kSCSICmd_ATA_PASS_THROUGH_EXT](driverkit/kscsicmd_ata_pass_through_ext.md)
- [kTickScale](driverkit/ktickscale.md)

### Type Aliases

- [IOAddressRange](driverkit/ioaddressrange.md)
- [IOAlignment](driverkit/ioalignment.md)
- [IODeviceNumber](driverkit/iodevicenumber.md)
- [IOLogicalAddress](driverkit/iologicaladdress.md)
- [OSSerializationPortCopyInHandler](driverkit/osserializationportcopyinhandler.md)
- [OSSerializationPortCopyOutHandler](driverkit/osserializationportcopyouthandler.md)
- [io_connect_t](driverkit/io_connect_t.md)
- [io_enumerator_t](driverkit/io_enumerator_t.md)
- [io_ident_t](driverkit/io_ident_t.md)
- [io_iterator_t](driverkit/io_iterator_t.md)
- [io_object_t](driverkit/io_object_t.md)
- [io_registry_entry_t](driverkit/io_registry_entry_t.md)
- [io_service_t](driverkit/io_service_t.md)
- [pid_t](driverkit/pid_t.md)
- [uext_object_t](driverkit/uext_object_t.md)
