---
title: Carbon Core Deprecations
apple_id: TP40012224
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/CarbonCoreDeprecations/index.html
archived_at: '2026-07-18T02:54:23.305393Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Carbon Core Deprecations

Carbon Core, a subframework of the Core Services umbrella framework, contains the programming interfaces of many legacy Carbon managers, in addition to various utilities. In OS X v10.8, most of these interfaces are deprecated.

If your app uses APIs in the Carbon Core framework, it’s recommended that you investigate ways to update your code. This document lists the Carbon Core header files that are deprecated in OS X v10.8 and summarizes some of the alternative APIs you can use.

> [!NOTE]
> 

#### Contents:

- [AIFF](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltg)
- [Aliases](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknlti)
- [Collections](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltk)
- [Components](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltm)
- [ConditionalMacros](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknlto)
- [Debugging](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltq)
- [DriverServices](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknlts)
- [DriverSynchronization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltcma)
- [Endian](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltcmi)
- [Files](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknlte)
- [Finder](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltcmq)
- [FixMath](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltcmy)
- [Folders](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltcna)
- [fp](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltcni)
- [Gestalt](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltcnq)
- [HFSVolumes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltcny)
- [LowMem](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltcoa)
- [MacErrors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltcoi)
- [MachineExceptions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltema)
- [MacMemory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltemi)
- [MacTypes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltemq)
- [Math64](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltemy)
- [MixedMode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltena)
- [Multiprocessing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknlteni)
- [MultiprocessingInfo](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltgmq)
- [OSUtils](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltenq)
- [PEFBinaryFormat](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknlteny)
- [PLStringFuncs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltgmy)
- [Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknlteoa)
- [Threads](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknlteoi)
- [Timer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltgma)
- [ToolUtils](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdemrufvbuqmjnknltgmi)

### AIFF

The `AIFF` header file defines the AIFF file format. Beginning in OS X v10.8, `AIFF.h` will no longer be updated or maintained.

### Aliases

The `Aliases` header file defines the functions of the Alias Manager, which was designed to help you create and resolve alias records (alias records are data structures that describe file system objects, such as files, directories, and volumes). To access the same type of information in your OS X v10.8 app, you should use the bookmark APIs provided by the `NSURL` and `CFURL` classes instead.

A bookmark is an opaque data structure that describes the location of a file. Although path and file reference URLs can be fragile between launches of your app, a bookmark can usually be used to re-create a URL to a file even when the file has been moved or renamed. If you have an alias file that contains Alias Manager information, use [bookmarkDataWithContentsOfURL:error:](https://developer.apple.com/documentation/foundation/nsurl/1408344-bookmarkdatawithcontentsofurl) to synthesize bookmark data for the file. To learn more about using bookmarks, see _[NSURL Class Reference](https://developer.apple.com/documentation/foundation/nsurl)_ and _[CFURL Reference](https://developer.apple.com/documentation/corefoundation/cfurl-rd7)_.

### Collections

The `Collections` header file defines the functions of the Collection Manager, which was deprecated prior to OS X v10.8. The Collection Manager defined an abstract data type that allowed you to store a collection of information. To manage collections of objects in your app, use the collection APIs in Foundation or Core Foundation (for more information, see _[Collections Programming Topics](../../documentation/Cocoa/Collections%20Programming%20Topics/About%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazti2i)_ and _[Collections Programming Topics for Core Foundation](../../documentation/Core%20Foundation/Collections%20Programming%20Topics%20for%20Core%20Foundation/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdi2i)_).

### Components

The `Components` header file defines the functions of the Component Manager, which was designed to help you find and use components in your app or add custom components to system-provided services, such as QuickTime and Core Audio. The Component Manager is deprecated in OS X v10.8, and there is no exact replacement for it. If you use QuickTime in your app, you might need to continue using the Component Manager to browse the built-in QuickTime components or add custom components.

If you use the Component Manager to define custom components that extend your app, consider creating a custom a plug-in model to replicate the functionality you need (to start learning about plug-ins, see _[Plug-in Programming Topics](../../documentation/Core%20Foundation/Plug-in%20Programming%20Topics/Introduction%20to%20Plug-ins.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdq2i)_). If you need to find and open audio units and audio codecs in your app, use Audio Component Services instead of the Component Manager (for more information, see _[Audio Component Services Reference](https://developer.apple.com/documentation/audiounit/audio_component_services)_).

### ConditionalMacros

In OS X v10.8, the contents of the `ConditionalMacros` header file have been moved to `/usr/include/ConditionalMacros.h`.

### Debugging

The `Debugging` header file defines macros that handle assertions and exceptions. In OS X v10.8, these macros are available in `/usr/include/AssertMacros.h`.

### DriverServices

The `DriverServices` header file defines functions that help you manipulate time-based data. To perform these functions in your OS X v10.8 app, use the [CFAbsoluteTime](https://developer.apple.com/documentation/corefoundation/cfabsolutetime) or Mach time APIs instead. For a summary of timer objects in Mach, see [Time Management](../../documentation/Darwin/Kernel%20Programming%20Guide/Mach%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrqhewviucykjcummjrge); to learn more about `mach_absolute_time`, see _[Mach Absolute Time Units](https://developer.apple.com/library/archive/qa/qa1398/_index.html#//apple_ref/doc/uid/DTS10003470)_.

### DriverSynchronization

The `DriverSynchronization` header file defines functions that perform operations—such as compare and swap—in an atomic or synchronized manner. To get this functionality in your code, use the Mach `OSAtomic` APIs instead (to learn more about the `OSAtomic` APIs, see _libkern Reference_).

### Endian

The `Endian` header file defines the Core Endian API, which provides functions that help you convert data between big-endian and little-endian formats. To replace this functionality in your code, use the Core Foundation byte order functions (described in _[Byte-Order Utilities Reference](https://developer.apple.com/documentation/corefoundation/byte_order_utilities)_) instead.

### Files

The `Files` header file defines the File Manager API, which is deprecated in OS X v10.8. The File Manager provides functions that operate on files, folders, and volumes without exposing low-level implementation details, such as file system and volume formats.

There are many Foundation, Core Foundation, Disk Arbitration, and POSIX and BSD APIs you can use to replace the File Manager functions in your app. For example, if you need to get notifications when a folder changes, use the File System Events API (to learn more about this API, see _[File System Events Programming Guide](../../documentation/Darwin/File%20System%20Events%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2teobz)_). Or if you need to mount, unmount, or eject a local volume, use the Disk Arbitration API (to learn more about the Disk Arbitration API, see _[Disk Arbitration Programming Guide](../../documentation/Disk%20Arbitration%20Programming%20Guide/About%20Disk%20Arbitration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tgmjq)_).

To find out which APIs are recommended to replace specific File Manager functions, see _File Manager Reference_.

### Finder

The `Finder` header file defines data types and constants that help you use Finder metadata to access file system items. Although you should not directly manipulate Finder information, you can access the information by using properties of `CFURL` and `NSURL` objects, such as [kCFURLIsAliasFileKey](https://developer.apple.com/documentation/corefoundation/kcfurlisaliasfilekey), [kCFURLIsHiddenKey](https://developer.apple.com/documentation/corefoundation/kcfurlishiddenkey), and [kCFURLHasHiddenExtensionKey](https://developer.apple.com/documentation/corefoundation/kcfurlhashiddenextensionkey). In addition, you can use the Launch Services API to register the document types that your app supports (to learn about using Launch Services in your code, see _[Launch Services Programming Guide](../../documentation/Carbon/Launch%20Services%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojz)_).

### FixMath

The `FixMath` header file defines functions that convert between numbers represented in different formats (such as fixed-point decimal and floating point) and functions that perform calculations. In OS X v10.8, the use of fixed data types is deprecated; use standard C floating point types instead.

### Folders

The `Folders` header file defines the functions of the Folder Manager, which was deprecated prior to OS X v10.8. The Folder Manager defined functions that allowed you to find and create folders and control how files are routed between folders. In OS X v10.8 and later, use the `NSPathUtilities` API instead (for more information, see _[NSString Class Reference](https://developer.apple.com/documentation/foundation/nsstring)_, _[NSArray Class Reference](https://developer.apple.com/documentation/foundation/nsarray)_, and _[Foundation Framework Reference](https://developer.apple.com/documentation/foundation)_).

### fp

The `fp` header file defines trigonometric, hyperbolic, and other functions that help you perform numerical calculations. To perform these calculations in an app running in OS X v10.8 and later, use the API defined in `/usr/include/math.h` instead.

### Gestalt

The `Gestalt` header file defines the functions of the Gestalt Manager, which allows you to investigate the operating environment of your app. If you need to get system information in an app running in OS X v10.8 or later, use [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) instead.

### HFSVolumes

In OS X v10.8, the `HFSVolumes` header file contains only the definition of the `HFSCatalogNodeID` type, which is used to identify a file or folder in an HFS Plus file system. OS X does not supply programming interfaces defining the on-disk data structures that HFS uses.

### LowMem

The `LowMem` header file defines functions enabling access to types of data that were stored in low-memory variables in versions of Mac OS prior to OS X. In earlier versions of OS X, these functions were supported to facilitate the porting of legacy apps. No modern OS X app should use these functions to get information about a service or the system. If, for example, you need to get the position of the mouse pointer, you would use a higher-level API such as Quartz Display Services (to learn about the Quartz Display Services, see _[Quartz Display Services Programming Topics](../../documentation/Graphics%20Imaging/Quartz%20Display%20Services%20Programming%20Topics/Introduction%20to%20Quartz%20Display%20Services%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmjw)_).

### MacErrors

The `MacErrors` header file defines error codes that were used in many legacy APIs. As much as possible, migrate to APIs that return `NSError` (or `CFError`) objects instead. To learn more about using `NSError` and `CFError` objects, see _[NSError Class Reference](https://developer.apple.com/documentation/foundation/nserror)_ and _[CFError Reference](https://developer.apple.com/documentation/corefoundation/cferror)_.

### MachineExceptions

The `MachineExceptions` header file defines data structures that represent the architecture of various CPUs and exception-handler functions. In general, use Mach functions to get this information instead.

### MacMemory

The `MacMemory` header file defines many of the functions of the Memory Manager, which is available only for compatibility with legacy apps and API. Among other things, the Memory Manager helped developers set up an app’s memory partition at launch time and helped perform memory-management tasks that became unnecessary in OS X. Except for QuickTime usages, you can use other API instead of Memory Manager API. For example, if you use `NewHandle` or `NewPtr` for simple allocations, use `malloc` instead. If you use handles to contain resizable or editable data, switch to the `CFMutableData` API (for more information, see _[CFMutableData Reference](https://developer.apple.com/documentation/corefoundation/cfmutabledata-rps)_). Finally, use [memmove](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/memmove.3.html#//apple_ref/doc/man/3/memmove) instead of `BlockMove` or `BlockMoveData`, and use [bzero](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/bzero.3.html#//apple_ref/doc/man/3/bzero) or [memset](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/memset.3.html#//apple_ref/doc/man/3/memset) instead of `BlockZero`.

### MacTypes

The `MacTypes` header file defines basic data types, such as `UInt64` and `Boolean`. If you need to include this header file for compatibility with legacy code, use `/usr/include/MacTypes.h` instead.

### Math64

The `Math64` header file defines functions that perform 64-bit integer calculations. Because current compilers support 64-bit integer math by default, you should no longer use the functions in `Math64.h`.

### MixedMode

The `MixedMode` header file defines the functions of the Mixed Mode Manager, which is available only for compatibility with legacy apps. The Mixed Mode Manager provided an API to handle switching between the PowerPC and 68K architectures. In OS X v10.8, this API is obsolete.

### Multiprocessing

The `Multiprocessing` header file is part of the legacy Multiprocessing Services API, which allowed legacy apps to support multitasking. In OS X apps, you should support multitasking by using Grand Central Dispatch or POSIX threads. To learn about multiprocessing on OS X, see _[Concurrency Programming Guide](../../documentation/General/Concurrency%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojr)_; to learn about POSIX thread routines, see `pthread(3) OS X Developer Tools
Manual Page`. You can find out about timer objects in Mach in [Time Management](../../../documentation/Darwin/Conceptual/KernelProgramming/Mach/Mach.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrqhewviucykjcummjrge); to learn more about `mach_absolute_time`, see _[Mach Absolute Time Units](https://developer.apple.com/library/archive/qa/qa1398/_index.html#//apple_ref/doc/uid/DTS10003470)_.

### MultiprocessingInfo

The `MultiprocessingInfo` header file is part of the legacy Multiprocessing Services API. In OS X apps, you should support multitasking by using blocks or Grand Central Dispatch. To learn about multiprocessing on OS X, see _[Concurrency Programming Guide](../../documentation/General/Concurrency%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojr)_.

### OSUtils

The `OSUtils` header file defines the functions of the Memory Management Utilities API, which is available only for compatibility with legacy apps. Memory Management Utilities supported functionality such as OS queue management and getting the user or computer name. Here are the alternative APIs you should use instead of the functions deprecated in OS X v10.8:

| Deprecated function | Recommended alternative |
| --- | --- |
| `Delay` | `sleep`, [usleep](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/usleep.3.html#//apple_ref/doc/man/3/usleep), or [nanosleep](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/nanosleep.2.html#//apple_ref/doc/man/2/nanosleep) |
| `Enqueue` and `Dequeue` | `queue(3)` (use mutex locking) |
| `CSCopyUserName` | Use password database operations, such as [getpwuid_r](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/getpwuid_r.3.html#//apple_ref/doc/man/3/getpwuid_r), or membership functions, such as [mbr_uid_to_uuid](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/mbr_uid_to_uuid.3.html#//apple_ref/doc/man/3/mbr_uid_to_uuid) |
| `CSCopyMachineName` | [SCDynamicStoreCopyComputerName](https://developer.apple.com/documentation/systemconfiguration/1517208-scdynamicstorecopycomputername) |

### PEFBinaryFormat

The native executable format of OS X is Mach-O, so the preferred executable format defined in `PEFBinaryFormat.h` is obsolete.

### PLStringFuncs

The `PLStringFuncs` header file defines Pascal string-manipulation routines. In OS X v10.8 and later, use Core Foundation string functions instead (for more information, see _[CFString Reference](https://developer.apple.com/documentation/corefoundation/cfstring)_).

### Resources

The `Resources` header file defines many of the functions of the Resource Manager, which allows a legacy app to create and manage its resources. In OS X v10.8, the Resource Manager is deprecated. To manage your app’s resources, use bundles instead. You can learn more about bundles by reading _[Bundle Programming Guide](../../documentation/Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_.

### Threads

The `Threads` header file defines the functions of the Thread Manager, which was deprecated prior to OS X v10.8. The Thread Manager supported the cooperative scheduling of threads in an app. In OS X, you should use Grand Central Dispatch (GCD) or POSIX threads instead. To learn more about GCD, see _Grand Central Dispatch (GCD) Reference_; to learn how to take advantage of threading in your app, see _[Threading Programming Guide](../../documentation/Cocoa/Threading%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2i)_.

### Timer

The `Timer` header file defines the functions of the Time Manager, which was deprecated prior to OS X v10.8. The Time Manager allowed apps to schedule tasks to execute at a later time. To perform similar scheduling tasks in your OS X app, you can use a run loop, an `NSTimer` object, or one of the POSIX sleep functions (that is, `sleep`, [usleep](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/usleep.3.html#//apple_ref/doc/man/3/usleep), or [nanosleep](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/nanosleep.2.html#//apple_ref/doc/man/2/nanosleep)). To learn more about Core Foundation run loops, see _[CFRunLoop Reference](https://developer.apple.com/documentation/corefoundation/cfrunloop)_; to learn more about the `NSTimer` object, see _[NSTimer Class Reference](https://developer.apple.com/documentation/foundation/timer)_. In addition, Grand Central Dispatch provides a set of dispatch sources which allow you to monitor the activities of low-level system objects (such as Mach ports or Unix descriptors) and submit an event handler to a dispatch queue when a specific activity occurs. To learn more about dispatch sources, see [Dispatch Sources](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/GCDWorkQueues/GCDWorkQueues.html#//apple_ref/doc/uid/TP40008091-CH103).

If you need to know the elapsed duration since the system started up (which is a quantity provided by the deprecated `Microseconds` function), use `mach_absolute_time` instead.

### ToolUtils

The `ToolUtils` header file defines bitwise functions, such as `BitXor` and `BitShift`. If you need this functionality in your OS X v10.8 app, use the C bitwise operators (such as `^` and `>>`) instead.
