---
title: Kernel
framework: kernel
symbol_kind: symbol
role: collection
role_heading: Framework
platforms: [macOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/kernel
source_url: 'https://developer.apple.com/documentation/kernel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/kernel.json'
content_hash: 'sha256:f86a0a62ffcb9758'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Kernel

<sub>Framework</sub>

Develop kernel-resident device drivers and kernel extensions.

## Overview

The Kernel Framework provides the APIs and support for kernel-resident device drivers and other kernel extensions. It defines the base class for I/O Kit device drivers ([IOService](kernel/ioservice-5h.md)), several helper classes, and the families that support many types of devices.

## Topics

### Kernel Extensions

- [Implementing drivers, system extensions, and kexts](kernel/implementing_drivers_system_extensions_and_kexts.md) — Create drivers and system extensions to communicate with hardware and provide low-level services, and only use kernel extensions for a few tasks. 
- [Installing a custom kernel extension](apple-silicon/installing-a-custom-kernel-extension.md) — Install kernel extensions using a custom installer package, and help users understand the installation process.
- [Debugging a custom kernel extension](apple-silicon/debugging-a-custom-kernel-extension.md) — Configure your system to enable the debugging of custom kernel extensions from a second Mac.
- [Generating a Non-Maskable Interrupt](kernel/generating_a_non-maskable_interrupt.md) — Interrupt the kernel on a target Mac and attach a remote debugger to it.

### IOKit Drivers

- [IOKit Fundamentals](kernel/iokit_fundamentals.md) — Implement a driver for your custom hardware using a third-party kernel extension. 
- [Hardware Families](kernel/hardware_families.md) — Add support for specific hardware protocols such as USB, and for standard network, serial, audio, and graphics interfaces. 
- [Driver Support](kernel/driver_support.md) — Explore the device registry and access power-management utilities and other shared driver features. 
- [libkern](kernel/libkern.md) — Access the runtime support and base classes of the kernel library.

### BSD

- [architecture](kernel/architecture.md) — Access machine-level and architectural information about the current platform.
- [bsm](kernel/bsm.md) — Audit resource usage on the system.
- [hfs](kernel/hfs.md) — Access HFS file-system data structures. 
- [kern](kernel/kern.md) — Access kernel-level interfaces including clock, task, kernel extension, lock, and compression utilities.  
- [Math](kernel/math.md) — Perform mathematical operations and manipulate integer, float, and double values.  
- [miscfs](kernel/miscfs.md) — Access device nodes and other file-system entities.
- [net](kernel/net.md) — Access network-related utilities.
- [Strings](kernel/strings.md) — Compare, convert, and catenate strings and access the resulting content of those strings.
- [sys](kernel/sys.md) — Access general system utilities for time, file systems, and system information.
- [vfs](kernel/vfs.md) — Access the virtual file-system interfaces.
- [vm](kernel/vm.md) — Interact with the virtual memory system.

### Mach

- [mach](kernel/mach.md) — Access Mach interfaces including processor, memory, thread, and semaphore support. 
- [mach-o](kernel/mach-o.md) — Access interfaces associated with the Mach-O runtime.

### Utilities

- [Debugging](kernel/debugging.md) — Debug your kernel extensions using the kernel debugger, assertions, exceptions, backtraces, and logging.
- [AppleDSP](kernel/appledsp.md) — Perform digital signal processing on data.

### Deprecated

- [Deprecated Symbols](kernel/deprecated_symbols.md) — Review unsupported symbols and their replacements.

### Additional Reference

- [Kernel Functions](kernel/kernel_functions.md)
- [Kernel Structures](kernel/kernel_structures.md)
- [Kernel Data Types](kernel/kernel_data_types.md)
- [Kernel Enumerations](kernel/kernel_enumerations.md)
- [Kernel Constants](kernel/kernel_constants.md)

### Classes

- [IOCatalogue](kernel/iocatalogue.md) — In-kernel database for IOKit driver personalities.
- [IOEventLink](kernel/ioeventlink.md)
- [IOEventLinkInterface](kernel/ioeventlinkinterface.md)
- [IOGuardPageMemoryDescriptor](kernel/ioguardpagememorydescriptor.md)
- [IOHIDTranslationService](kernel/iohidtranslationservice.md)
- [IOServiceStateNotificationDispatchSource](driverkit/ioservicestatenotificationdispatchsource.md)
- [IOServiceStateNotificationDispatchSourceInterface](kernel/ioservicestatenotificationdispatchsourceinterface.md)
- [IOWorkGroup](kernel/ioworkgroup.md)
- [IOWorkGroupInterface](kernel/ioworkgroupinterface.md)
- [OSAction_IOHIDEventService__CopyEvent](kernel/osaction_iohideventservice_copyevent.md)
- [OSAction_IOHIDEventService__CopyEventInterface](kernel/osaction_iohideventservice_copyeventinterface.md)
- [OSAction_IOHIDEventService__SetLED](kernel/osaction_iohideventservice_setled.md)
- [OSAction_IOHIDEventService__SetLEDInterface](kernel/osaction_iohideventservice_setledinterface.md)
- [OSAction_IOHIDEventService__SetUserProperties](kernel/osaction_iohideventservice_setuserproperties.md)
- [OSAction_IOHIDEventService__SetUserPropertiesInterface](kernel/osaction_iohideventservice_setuserpropertiesinterface.md)

## See Also

### Related Documentation

- [IOKit Fundamentals](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/IOKitFundamentals/Introduction/Introduction.html#//apple_ref/doc/uid/TP0000011)
- [About This Document](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/About/About.html#//apple_ref/doc/uid/TP30000905-CH204)
