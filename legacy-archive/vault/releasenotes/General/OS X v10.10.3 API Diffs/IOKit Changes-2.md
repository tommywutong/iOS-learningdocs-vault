---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/IOKit.html
archived_at: '2026-07-18T02:52:31.618688Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# IOKit Changes

## IOKit

Added IOAsyncCompletionContent.init()Added IOCFPlugInInterfaceStruct.init()Added IOCFPlugInInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, version: UInt16, revision: UInt16, Probe: CFunctionPointer<((UnsafeMutablePointer<Void>, CFDictionary!, io_service_t, UnsafeMutablePointer<Int32>) -> IOReturn)>, Start: CFunctionPointer<((UnsafeMutablePointer<Void>, CFDictionary!, io_service_t) -> IOReturn)>, Stop: CFunctionPointer<((UnsafeMutablePointer<Void>) -> IOReturn)>)Added IONamedValue.init()Added IONamedValue.init(value: Int32, name: UnsafePointer<Int8>)Added IOPhysicalRange.init()Added IOPhysicalRange.init(address: IOPhysicalAddress, length: IOByteCount)Added IOServiceInterestContent.init()Added IOServiceInterestContent.init(messageType: natural_t, messageArgument:(UnsafeMutablePointer<Void>))Added IOServiceInterestContent64.init()Added IOServiceInterestContent64.init(messageType: natural_t, messageArgument:(io_user_reference_t))Added IOVirtualRange.init()Added IOVirtualRange.init(address: IOVirtualAddress, length: IOByteCount)Added OSNotificationHeader.init()Added OSNotificationHeader64.init()Added kIOBundleDevelopmentRegionKeyAdded kIOBundleExecutableKeyAdded kIOBundleIdentifierKeyAdded kIOBundleInfoDictionaryVersionKeyAdded kIOBundleNameKeyAdded kIOBundleVersionKeyAdded kIOURLFileDirectoryContentsAdded kIOURLFileExistsAdded kIOURLFileLastModificationTimeAdded kIOURLFileLengthAdded kIOURLFileOwnerIDAdded kIOURLFilePOSIXModeModified IOAsyncCompletionContent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct IOAsyncCompletionContent {     var result: IOReturn } ``` |
| To | ``` struct IOAsyncCompletionContent {     var result: IOReturn     init() } ``` |

Modified IOCFPlugInInterfaceStruct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct IOCFPlugInInterfaceStruct {     var _reserved: UnsafePointer<()>     var QueryInterface: CFunctionPointer<((UnsafePointer<()>, REFIID, UnsafePointer<LPVOID>) -> HRESULT)>     var AddRef: CFunctionPointer<((UnsafePointer<()>) -> ULONG)>     var Release: CFunctionPointer<((UnsafePointer<()>) -> ULONG)>     var version: UInt16     var revision: UInt16     var Probe: CFunctionPointer<((UnsafePointer<()>, CFDictionary!, io_service_t, UnsafePointer<Int32>) -> IOReturn)>     var Start: CFunctionPointer<((UnsafePointer<()>, CFDictionary!, io_service_t) -> IOReturn)>     var Stop: CFunctionPointer<((UnsafePointer<()>) -> IOReturn)> } ``` |
| To | ``` struct IOCFPlugInInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>     var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var version: UInt16     var revision: UInt16     var Probe: CFunctionPointer<((UnsafeMutablePointer<Void>, CFDictionary!, io_service_t, UnsafeMutablePointer<Int32>) -> IOReturn)>     var Start: CFunctionPointer<((UnsafeMutablePointer<Void>, CFDictionary!, io_service_t) -> IOReturn)>     var Stop: CFunctionPointer<((UnsafeMutablePointer<Void>) -> IOReturn)>     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, version version: UInt16, revision revision: UInt16, Probe Probe: CFunctionPointer<((UnsafeMutablePointer<Void>, CFDictionary!, io_service_t, UnsafeMutablePointer<Int32>) -> IOReturn)>, Start Start: CFunctionPointer<((UnsafeMutablePointer<Void>, CFDictionary!, io_service_t) -> IOReturn)>, Stop Stop: CFunctionPointer<((UnsafeMutablePointer<Void>) -> IOReturn)>) } ``` |

Modified IOCFPlugInInterfaceStruct.AddRef

|  | Declaration |
| --- | --- |
| From | ``` var AddRef: CFunctionPointer<((UnsafePointer<()>) -> ULONG)> ``` |
| To | ``` var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)> ``` |

Modified IOCFPlugInInterfaceStruct.Probe

|  | Declaration |
| --- | --- |
| From | ``` var Probe: CFunctionPointer<((UnsafePointer<()>, CFDictionary!, io_service_t, UnsafePointer<Int32>) -> IOReturn)> ``` |
| To | ``` var Probe: CFunctionPointer<((UnsafeMutablePointer<Void>, CFDictionary!, io_service_t, UnsafeMutablePointer<Int32>) -> IOReturn)> ``` |

Modified IOCFPlugInInterfaceStruct.QueryInterface

|  | Declaration |
| --- | --- |
| From | ``` var QueryInterface: CFunctionPointer<((UnsafePointer<()>, REFIID, UnsafePointer<LPVOID>) -> HRESULT)> ``` |
| To | ``` var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)> ``` |

Modified IOCFPlugInInterfaceStruct.Release

|  | Declaration |
| --- | --- |
| From | ``` var Release: CFunctionPointer<((UnsafePointer<()>) -> ULONG)> ``` |
| To | ``` var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)> ``` |

Modified IOCFPlugInInterfaceStruct.Start

|  | Declaration |
| --- | --- |
| From | ``` var Start: CFunctionPointer<((UnsafePointer<()>, CFDictionary!, io_service_t) -> IOReturn)> ``` |
| To | ``` var Start: CFunctionPointer<((UnsafeMutablePointer<Void>, CFDictionary!, io_service_t) -> IOReturn)> ``` |

Modified IOCFPlugInInterfaceStruct.Stop

|  | Declaration |
| --- | --- |
| From | ``` var Stop: CFunctionPointer<((UnsafePointer<()>) -> IOReturn)> ``` |
| To | ``` var Stop: CFunctionPointer<((UnsafeMutablePointer<Void>) -> IOReturn)> ``` |

Modified IONamedValue [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct IONamedValue {     var value: Int32     var name: ConstUnsafePointer<Int8> } ``` |
| To | ``` struct IONamedValue {     var value: Int32     var name: UnsafePointer<Int8>     init()     init(value value: Int32, name name: UnsafePointer<Int8>) } ``` |

Modified IONamedValue.name

|  | Declaration |
| --- | --- |
| From | ``` var name: ConstUnsafePointer<Int8> ``` |
| To | ``` var name: UnsafePointer<Int8> ``` |

Modified IOPhysicalRange [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct IOPhysicalRange {     var address: IOPhysicalAddress     var length: IOByteCount } ``` |
| To | ``` struct IOPhysicalRange {     var address: IOPhysicalAddress     var length: IOByteCount     init()     init(address address: IOPhysicalAddress, length length: IOByteCount) } ``` |

Modified IOServiceInterestContent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct IOServiceInterestContent {     var messageType: natural_t     var messageArgument: (UnsafePointer<()>) } ``` |
| To | ``` struct IOServiceInterestContent {     var messageType: natural_t     var messageArgument: (UnsafeMutablePointer<Void>)     init()     init(messageType messageType: natural_t, messageArgument messageArgument: (UnsafeMutablePointer<Void>)) } ``` |

Modified IOServiceInterestContent.messageArgument

|  | Declaration |
| --- | --- |
| From | ``` var messageArgument: (UnsafePointer<()>) ``` |
| To | ``` var messageArgument: (UnsafeMutablePointer<Void>) ``` |

Modified IOServiceInterestContent64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct IOServiceInterestContent64 {     var messageType: natural_t     var messageArgument: (io_user_reference_t) } ``` |
| To | ``` struct IOServiceInterestContent64 {     var messageType: natural_t     var messageArgument: (io_user_reference_t)     init()     init(messageType messageType: natural_t, messageArgument messageArgument: (io_user_reference_t)) } ``` |

Modified IOVirtualRange [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct IOVirtualRange {     var address: IOVirtualAddress     var length: IOByteCount } ``` |
| To | ``` struct IOVirtualRange {     var address: IOVirtualAddress     var length: IOByteCount     init()     init(address address: IOVirtualAddress, length length: IOByteCount) } ``` |

Modified OSNotificationHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OSNotificationHeader {     var size: mach_msg_size_t     var type: natural_t     var reference: OSAsyncReference } ``` |
| To | ``` struct OSNotificationHeader {     var size: mach_msg_size_t     var type: natural_t     var reference: OSAsyncReference     init() } ``` |

Modified OSNotificationHeader64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OSNotificationHeader64 {     var size: mach_msg_size_t     var type: natural_t     var reference: OSAsyncReference64 } ``` |
| To | ``` struct OSNotificationHeader64 {     var size: mach_msg_size_t     var type: natural_t     var reference: OSAsyncReference64     init() } ``` |

Modified IOAsyncCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias IOAsyncCallback = CFunctionPointer<((UnsafePointer<()>, IOReturn, UnsafePointer<UnsafePointer<()>>, UInt32) -> Void)> ``` |
| To | ``` typealias IOAsyncCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, IOReturn, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UInt32) -> Void)> ``` |

Modified IOAsyncCallback0

|  | Declaration |
| --- | --- |
| From | ``` typealias IOAsyncCallback0 = CFunctionPointer<((UnsafePointer<()>, IOReturn) -> Void)> ``` |
| To | ``` typealias IOAsyncCallback0 = CFunctionPointer<((UnsafeMutablePointer<Void>, IOReturn) -> Void)> ``` |

Modified IOAsyncCallback1

|  | Declaration |
| --- | --- |
| From | ``` typealias IOAsyncCallback1 = CFunctionPointer<((UnsafePointer<()>, IOReturn, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias IOAsyncCallback1 = CFunctionPointer<((UnsafeMutablePointer<Void>, IOReturn, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified IOAsyncCallback2

|  | Declaration |
| --- | --- |
| From | ``` typealias IOAsyncCallback2 = CFunctionPointer<((UnsafePointer<()>, IOReturn, UnsafePointer<()>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias IOAsyncCallback2 = CFunctionPointer<((UnsafeMutablePointer<Void>, IOReturn, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified IOBSDNameMatching(mach_port_t, UInt32, UnsafePointer<Int8>) -> Unmanaged<CFMutableDictionary>!

|  | Declaration |
| --- | --- |
| From | ``` func IOBSDNameMatching(_ masterPort: mach_port_t, _ options: UInt32, _ bsdName: ConstUnsafePointer<Int8>) -> Unmanaged<CFMutableDictionary>! ``` |
| To | ``` func IOBSDNameMatching(_ masterPort: mach_port_t, _ options: UInt32, _ bsdName: UnsafePointer<Int8>) -> Unmanaged<CFMutableDictionary>! ``` |

Modified IOCFUnserialize(UnsafePointer<Int8>, CFAllocator!, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFString>?>) -> AnyObject!

|  | Declaration |
| --- | --- |
| From | ``` func IOCFUnserialize(_ buffer: ConstUnsafePointer<Int8>, _ allocator: CFAllocator!, _ options: CFOptionFlags, _ errorString: UnsafePointer<Unmanaged<CFString>?>) -> AnyObject! ``` |
| To | ``` func IOCFUnserialize(_ buffer: UnsafePointer<Int8>, _ allocator: CFAllocator!, _ options: CFOptionFlags, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>) -> AnyObject! ``` |

Modified IOCFUnserializeBinary(UnsafePointer<Int8>, Int, CFAllocator!, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFString>?>) -> AnyObject!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOCFUnserializeBinary(_ buffer: ConstUnsafePointer<Int8>, _ bufferSize: UInt, _ allocator: CFAllocator!, _ options: CFOptionFlags, _ errorString: UnsafePointer<Unmanaged<CFString>?>) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func IOCFUnserializeBinary(_ buffer: UnsafePointer<Int8>, _ bufferSize: Int, _ allocator: CFAllocator!, _ options: CFOptionFlags, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>) -> AnyObject! ``` | OS X 10.10.3 |

Modified IOCFUnserializeWithSize(UnsafePointer<Int8>, Int, CFAllocator!, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFString>?>) -> AnyObject!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOCFUnserializeWithSize(_ buffer: ConstUnsafePointer<Int8>, _ bufferSize: UInt, _ allocator: CFAllocator!, _ options: CFOptionFlags, _ errorString: UnsafePointer<Unmanaged<CFString>?>) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func IOCFUnserializeWithSize(_ buffer: UnsafePointer<Int8>, _ bufferSize: Int, _ allocator: CFAllocator!, _ options: CFOptionFlags, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>) -> AnyObject! ``` | OS X 10.10.3 |

Modified IOCatalogueGetData(mach_port_t, UInt32, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, UnsafeMutablePointer<UInt32>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IOCatalogueGetData(_ masterPort: mach_port_t, _ flag: UInt32, _ buffer: UnsafePointer<UnsafePointer<Int8>>, _ size: UnsafePointer<UInt32>) -> kern_return_t ``` |
| To | ``` func IOCatalogueGetData(_ masterPort: mach_port_t, _ flag: UInt32, _ buffer: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ size: UnsafeMutablePointer<UInt32>) -> kern_return_t ``` |

Modified IOCatalogueModuleLoaded(mach_port_t, UnsafeMutablePointer<Int8>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IOCatalogueModuleLoaded(_ masterPort: mach_port_t, _ name: UnsafePointer<Int8>) -> kern_return_t ``` |
| To | ``` func IOCatalogueModuleLoaded(_ masterPort: mach_port_t, _ name: UnsafeMutablePointer<Int8>) -> kern_return_t ``` |

Modified IOCatalogueSendData(mach_port_t, UInt32, UnsafePointer<Int8>, UInt32) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IOCatalogueSendData(_ masterPort: mach_port_t, _ flag: UInt32, _ buffer: ConstUnsafePointer<Int8>, _ size: UInt32) -> kern_return_t ``` |
| To | ``` func IOCatalogueSendData(_ masterPort: mach_port_t, _ flag: UInt32, _ buffer: UnsafePointer<Int8>, _ size: UInt32) -> kern_return_t ``` |

Modified IOCatalogueTerminate(mach_port_t, UInt32, UnsafeMutablePointer<Int8>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IOCatalogueTerminate(_ masterPort: mach_port_t, _ flag: UInt32, _ description: UnsafePointer<Int8>) -> kern_return_t ``` |
| To | ``` func IOCatalogueTerminate(_ masterPort: mach_port_t, _ flag: UInt32, _ description: UnsafeMutablePointer<Int8>) -> kern_return_t ``` |

Modified IOConnectCallAsyncMethod(mach_port_t, UInt32, mach_port_t, UnsafeMutablePointer<UInt64>, UInt32, UnsafePointer<UInt64>, UInt32, UnsafePointer<Void>, Int, UnsafeMutablePointer<UInt64>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> kern_return_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOConnectCallAsyncMethod(_ connection: mach_port_t, _ selector: UInt32, _ wake_port: mach_port_t, _ reference: UnsafePointer<UInt64>, _ referenceCnt: UInt32, _ input: ConstUnsafePointer<UInt64>, _ inputCnt: UInt32, _ inputStruct: ConstUnsafePointer<()>, _ inputStructCnt: UInt, _ output: UnsafePointer<UInt64>, _ outputCnt: UnsafePointer<UInt32>, _ outputStruct: UnsafePointer<()>, _ outputStructCnt: UnsafePointer<UInt>) -> kern_return_t ``` | OS X 10.10 |
| To | ``` func IOConnectCallAsyncMethod(_ connection: mach_port_t, _ selector: UInt32, _ wake_port: mach_port_t, _ reference: UnsafeMutablePointer<UInt64>, _ referenceCnt: UInt32, _ input: UnsafePointer<UInt64>, _ inputCnt: UInt32, _ inputStruct: UnsafePointer<Void>, _ inputStructCnt: Int, _ output: UnsafeMutablePointer<UInt64>, _ outputCnt: UnsafeMutablePointer<UInt32>, _ outputStruct: UnsafeMutablePointer<Void>, _ outputStructCnt: UnsafeMutablePointer<Int>) -> kern_return_t ``` | OS X 10.5 |

Modified IOConnectCallAsyncScalarMethod(mach_port_t, UInt32, mach_port_t, UnsafeMutablePointer<UInt64>, UInt32, UnsafePointer<UInt64>, UInt32, UnsafeMutablePointer<UInt64>, UnsafeMutablePointer<UInt32>) -> kern_return_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOConnectCallAsyncScalarMethod(_ connection: mach_port_t, _ selector: UInt32, _ wake_port: mach_port_t, _ reference: UnsafePointer<UInt64>, _ referenceCnt: UInt32, _ input: ConstUnsafePointer<UInt64>, _ inputCnt: UInt32, _ output: UnsafePointer<UInt64>, _ outputCnt: UnsafePointer<UInt32>) -> kern_return_t ``` | OS X 10.10 |
| To | ``` func IOConnectCallAsyncScalarMethod(_ connection: mach_port_t, _ selector: UInt32, _ wake_port: mach_port_t, _ reference: UnsafeMutablePointer<UInt64>, _ referenceCnt: UInt32, _ input: UnsafePointer<UInt64>, _ inputCnt: UInt32, _ output: UnsafeMutablePointer<UInt64>, _ outputCnt: UnsafeMutablePointer<UInt32>) -> kern_return_t ``` | OS X 10.5 |

Modified IOConnectCallAsyncStructMethod(mach_port_t, UInt32, mach_port_t, UnsafeMutablePointer<UInt64>, UInt32, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> kern_return_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOConnectCallAsyncStructMethod(_ connection: mach_port_t, _ selector: UInt32, _ wake_port: mach_port_t, _ reference: UnsafePointer<UInt64>, _ referenceCnt: UInt32, _ inputStruct: ConstUnsafePointer<()>, _ inputStructCnt: UInt, _ outputStruct: UnsafePointer<()>, _ outputStructCnt: UnsafePointer<UInt>) -> kern_return_t ``` | OS X 10.10 |
| To | ``` func IOConnectCallAsyncStructMethod(_ connection: mach_port_t, _ selector: UInt32, _ wake_port: mach_port_t, _ reference: UnsafeMutablePointer<UInt64>, _ referenceCnt: UInt32, _ inputStruct: UnsafePointer<Void>, _ inputStructCnt: Int, _ outputStruct: UnsafeMutablePointer<Void>, _ outputStructCnt: UnsafeMutablePointer<Int>) -> kern_return_t ``` | OS X 10.5 |

Modified IOConnectCallMethod(mach_port_t, UInt32, UnsafePointer<UInt64>, UInt32, UnsafePointer<Void>, Int, UnsafeMutablePointer<UInt64>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> kern_return_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOConnectCallMethod(_ connection: mach_port_t, _ selector: UInt32, _ input: ConstUnsafePointer<UInt64>, _ inputCnt: UInt32, _ inputStruct: ConstUnsafePointer<()>, _ inputStructCnt: UInt, _ output: UnsafePointer<UInt64>, _ outputCnt: UnsafePointer<UInt32>, _ outputStruct: UnsafePointer<()>, _ outputStructCnt: UnsafePointer<UInt>) -> kern_return_t ``` | OS X 10.10 |
| To | ``` func IOConnectCallMethod(_ connection: mach_port_t, _ selector: UInt32, _ input: UnsafePointer<UInt64>, _ inputCnt: UInt32, _ inputStruct: UnsafePointer<Void>, _ inputStructCnt: Int, _ output: UnsafeMutablePointer<UInt64>, _ outputCnt: UnsafeMutablePointer<UInt32>, _ outputStruct: UnsafeMutablePointer<Void>, _ outputStructCnt: UnsafeMutablePointer<Int>) -> kern_return_t ``` | OS X 10.5 |

Modified IOConnectCallScalarMethod(mach_port_t, UInt32, UnsafePointer<UInt64>, UInt32, UnsafeMutablePointer<UInt64>, UnsafeMutablePointer<UInt32>) -> kern_return_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOConnectCallScalarMethod(_ connection: mach_port_t, _ selector: UInt32, _ input: ConstUnsafePointer<UInt64>, _ inputCnt: UInt32, _ output: UnsafePointer<UInt64>, _ outputCnt: UnsafePointer<UInt32>) -> kern_return_t ``` | OS X 10.10 |
| To | ``` func IOConnectCallScalarMethod(_ connection: mach_port_t, _ selector: UInt32, _ input: UnsafePointer<UInt64>, _ inputCnt: UInt32, _ output: UnsafeMutablePointer<UInt64>, _ outputCnt: UnsafeMutablePointer<UInt32>) -> kern_return_t ``` | OS X 10.5 |

Modified IOConnectCallStructMethod(mach_port_t, UInt32, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> kern_return_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOConnectCallStructMethod(_ connection: mach_port_t, _ selector: UInt32, _ inputStruct: ConstUnsafePointer<()>, _ inputStructCnt: UInt, _ outputStruct: UnsafePointer<()>, _ outputStructCnt: UnsafePointer<UInt>) -> kern_return_t ``` | OS X 10.10 |
| To | ``` func IOConnectCallStructMethod(_ connection: mach_port_t, _ selector: UInt32, _ inputStruct: UnsafePointer<Void>, _ inputStructCnt: Int, _ outputStruct: UnsafeMutablePointer<Void>, _ outputStructCnt: UnsafeMutablePointer<Int>) -> kern_return_t ``` | OS X 10.5 |

Modified IOConnectGetService(io_connect_t, UnsafeMutablePointer<io_service_t>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IOConnectGetService(_ connect: io_connect_t, _ service: UnsafePointer<io_service_t>) -> kern_return_t ``` |
| To | ``` func IOConnectGetService(_ connect: io_connect_t, _ service: UnsafeMutablePointer<io_service_t>) -> kern_return_t ``` |

Modified IOConnectMapMemory(io_connect_t, UInt32, task_port_t, UnsafeMutablePointer<mach_vm_address_t>, UnsafeMutablePointer<mach_vm_size_t>, IOOptionBits) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IOConnectMapMemory(_ connect: io_connect_t, _ memoryType: UInt32, _ intoTask: task_port_t, _ atAddress: UnsafePointer<mach_vm_address_t>, _ ofSize: UnsafePointer<mach_vm_size_t>, _ options: IOOptionBits) -> kern_return_t ``` |
| To | ``` func IOConnectMapMemory(_ connect: io_connect_t, _ memoryType: UInt32, _ intoTask: task_port_t, _ atAddress: UnsafeMutablePointer<mach_vm_address_t>, _ ofSize: UnsafeMutablePointer<mach_vm_size_t>, _ options: IOOptionBits) -> kern_return_t ``` |

Modified IOConnectMapMemory64(io_connect_t, UInt32, task_port_t, UnsafeMutablePointer<mach_vm_address_t>, UnsafeMutablePointer<mach_vm_size_t>, IOOptionBits) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IOConnectMapMemory64(_ connect: io_connect_t, _ memoryType: UInt32, _ intoTask: task_port_t, _ atAddress: UnsafePointer<mach_vm_address_t>, _ ofSize: UnsafePointer<mach_vm_size_t>, _ options: IOOptionBits) -> kern_return_t ``` |
| To | ``` func IOConnectMapMemory64(_ connect: io_connect_t, _ memoryType: UInt32, _ intoTask: task_port_t, _ atAddress: UnsafeMutablePointer<mach_vm_address_t>, _ ofSize: UnsafeMutablePointer<mach_vm_size_t>, _ options: IOOptionBits) -> kern_return_t ``` |

Modified IOCreatePlugInInterfaceForService(io_service_t, CFUUID!, CFUUID!, UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<IOCFPlugInInterface>>>, UnsafeMutablePointer<Int32>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IOCreatePlugInInterfaceForService(_ service: io_service_t, _ pluginType: CFUUID!, _ interfaceType: CFUUID!, _ theInterface: UnsafePointer<UnsafePointer<UnsafePointer<IOCFPlugInInterface>>>, _ theScore: UnsafePointer<Int32>) -> kern_return_t ``` |
| To | ``` func IOCreatePlugInInterfaceForService(_ service: io_service_t, _ pluginType: CFUUID!, _ interfaceType: CFUUID!, _ theInterface: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<IOCFPlugInInterface>>>, _ theScore: UnsafeMutablePointer<Int32>) -> kern_return_t ``` |

Modified IOCreateReceivePort(UInt32, UnsafeMutablePointer<mach_port_t>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IOCreateReceivePort(_ msgType: UInt32, _ recvPort: UnsafePointer<mach_port_t>) -> kern_return_t ``` |
| To | ``` func IOCreateReceivePort(_ msgType: UInt32, _ recvPort: UnsafeMutablePointer<mach_port_t>) -> kern_return_t ``` |

Modified IODataQueueDataAvailable(UnsafeMutablePointer<IODataQueueMemory>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func IODataQueueDataAvailable(_ dataQueue: UnsafePointer<IODataQueueMemory>) -> Boolean ``` |
| To | ``` func IODataQueueDataAvailable(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>) -> Boolean ``` |

Modified IODataQueueDequeue(UnsafeMutablePointer<IODataQueueMemory>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func IODataQueueDequeue(_ dataQueue: UnsafePointer<IODataQueueMemory>, _ data: UnsafePointer<()>, _ dataSize: UnsafePointer<UInt32>) -> IOReturn ``` |
| To | ``` func IODataQueueDequeue(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>, _ data: UnsafeMutablePointer<Void>, _ dataSize: UnsafeMutablePointer<UInt32>) -> IOReturn ``` |

Modified IODataQueueEnqueue(UnsafeMutablePointer<IODataQueueMemory>, UnsafeMutablePointer<Void>, UInt32) -> IOReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IODataQueueEnqueue(_ dataQueue: UnsafePointer<IODataQueueMemory>, _ data: UnsafePointer<()>, _ dataSize: UInt32) -> IOReturn ``` | OS X 10.10 |
| To | ``` func IODataQueueEnqueue(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>, _ data: UnsafeMutablePointer<Void>, _ dataSize: UInt32) -> IOReturn ``` | OS X 10.5 |

Modified IODataQueuePeek(UnsafeMutablePointer<IODataQueueMemory>) -> UnsafeMutablePointer<IODataQueueEntry>

|  | Declaration |
| --- | --- |
| From | ``` func IODataQueuePeek(_ dataQueue: UnsafePointer<IODataQueueMemory>) -> UnsafePointer<IODataQueueEntry> ``` |
| To | ``` func IODataQueuePeek(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>) -> UnsafeMutablePointer<IODataQueueEntry> ``` |

Modified IODataQueueSetNotificationPort(UnsafeMutablePointer<IODataQueueMemory>, mach_port_t) -> IOReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IODataQueueSetNotificationPort(_ dataQueue: UnsafePointer<IODataQueueMemory>, _ notifyPort: mach_port_t) -> IOReturn ``` | OS X 10.10 |
| To | ``` func IODataQueueSetNotificationPort(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>, _ notifyPort: mach_port_t) -> IOReturn ``` | OS X 10.5 |

Modified IODataQueueWaitForAvailableData(UnsafeMutablePointer<IODataQueueMemory>, mach_port_t) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func IODataQueueWaitForAvailableData(_ dataQueue: UnsafePointer<IODataQueueMemory>, _ notificationPort: mach_port_t) -> IOReturn ``` |
| To | ``` func IODataQueueWaitForAvailableData(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>, _ notificationPort: mach_port_t) -> IOReturn ``` |

Modified IODestroyPlugInInterface(UnsafeMutablePointer<UnsafeMutablePointer<IOCFPlugInInterface>>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IODestroyPlugInInterface(_ interface: UnsafePointer<UnsafePointer<IOCFPlugInInterface>>) -> kern_return_t ``` |
| To | ``` func IODestroyPlugInInterface(_ interface: UnsafeMutablePointer<UnsafeMutablePointer<IOCFPlugInInterface>>) -> kern_return_t ``` |

Modified IODispatchCalloutFromMessage(UnsafeMutablePointer<Void>, UnsafeMutablePointer<mach_msg_header_t>, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func IODispatchCalloutFromMessage(_ unused: UnsafePointer<()>, _ msg: UnsafePointer<mach_msg_header_t>, _ reference: UnsafePointer<()>) ``` |
| To | ``` func IODispatchCalloutFromMessage(_ unused: UnsafeMutablePointer<Void>, _ msg: UnsafeMutablePointer<mach_msg_header_t>, _ reference: UnsafeMutablePointer<Void>) ``` |

Modified IOKitGetBusyState(mach_port_t, UnsafeMutablePointer<UInt32>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IOKitGetBusyState(_ masterPort: mach_port_t, _ busyState: UnsafePointer<UInt32>) -> kern_return_t ``` |
| To | ``` func IOKitGetBusyState(_ masterPort: mach_port_t, _ busyState: UnsafeMutablePointer<UInt32>) -> kern_return_t ``` |

Modified IOKitWaitQuiet(mach_port_t, UnsafeMutablePointer<mach_timespec_t>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IOKitWaitQuiet(_ masterPort: mach_port_t, _ waitTime: UnsafePointer<mach_timespec_t>) -> kern_return_t ``` |
| To | ``` func IOKitWaitQuiet(_ masterPort: mach_port_t, _ waitTime: UnsafeMutablePointer<mach_timespec_t>) -> kern_return_t ``` |

Modified IOMasterPort(mach_port_t, UnsafeMutablePointer<mach_port_t>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IOMasterPort(_ bootstrapPort: mach_port_t, _ masterPort: UnsafePointer<mach_port_t>) -> kern_return_t ``` |
| To | ``` func IOMasterPort(_ bootstrapPort: mach_port_t, _ masterPort: UnsafeMutablePointer<mach_port_t>) -> kern_return_t ``` |

Modified IONotificationPortCreate(mach_port_t) -> IONotificationPortRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IONotificationPortCreate(_ masterPort: mach_port_t) -> Unmanaged<IONotificationPort>! ``` | OS X 10.10 |
| To | ``` func IONotificationPortCreate(_ masterPort: mach_port_t) -> IONotificationPortRef ``` | OS X 10.10.3 |

Modified IONotificationPortDestroy(IONotificationPortRef)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IONotificationPortDestroy(_ notify: IONotificationPort!) ``` | OS X 10.10 |
| To | ``` func IONotificationPortDestroy(_ notify: IONotificationPortRef) ``` | OS X 10.10.3 |

Modified IONotificationPortGetMachPort(IONotificationPortRef) -> mach_port_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IONotificationPortGetMachPort(_ notify: IONotificationPort!) -> mach_port_t ``` | OS X 10.10 |
| To | ``` func IONotificationPortGetMachPort(_ notify: IONotificationPortRef) -> mach_port_t ``` | OS X 10.10.3 |

Modified IONotificationPortGetRunLoopSource(IONotificationPortRef) -> Unmanaged<CFRunLoopSource>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IONotificationPortGetRunLoopSource(_ notify: IONotificationPort!) -> Unmanaged<CFRunLoopSource>! ``` | OS X 10.10 |
| To | ``` func IONotificationPortGetRunLoopSource(_ notify: IONotificationPortRef) -> Unmanaged<CFRunLoopSource>! ``` | OS X 10.10.3 |

Modified IONotificationPortRef

|  | Declaration |
| --- | --- |
| From | ``` typealias IONotificationPortRef = IONotificationPort ``` |
| To | ``` typealias IONotificationPortRef = COpaquePointer ``` |

Modified IONotificationPortSetDispatchQueue(IONotificationPortRef, dispatch_queue_t!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IONotificationPortSetDispatchQueue(_ notify: IONotificationPort!, _ queue: dispatch_queue_t!) ``` | OS X 10.10 |
| To | ``` func IONotificationPortSetDispatchQueue(_ notify: IONotificationPortRef, _ queue: dispatch_queue_t!) ``` | OS X 10.6 |

Modified IOObjectConformsTo(io_object_t, UnsafePointer<Int8>) -> boolean_t

|  | Declaration |
| --- | --- |
| From | ``` func IOObjectConformsTo(_ object: io_object_t, _ className: ConstUnsafePointer<Int8>) -> boolean_t ``` |
| To | ``` func IOObjectConformsTo(_ object: io_object_t, _ className: UnsafePointer<Int8>) -> boolean_t ``` |

Modified IOObjectCopyBundleIdentifierForClass(CFString!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified IOObjectCopyClass(io_object_t) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified IOObjectCopySuperclassForClass(CFString!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified IOObjectGetClass(io_object_t, UnsafeMutablePointer<Int8>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IOObjectGetClass(_ object: io_object_t, _ className: UnsafePointer<Int8>) -> kern_return_t ``` |
| To | ``` func IOObjectGetClass(_ object: io_object_t, _ className: UnsafeMutablePointer<Int8>) -> kern_return_t ``` |

Modified IOObjectGetKernelRetainCount(io_object_t) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified IOObjectGetUserRetainCount(io_object_t) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified IORegistryCreateIterator(mach_port_t, UnsafePointer<Int8>, IOOptionBits, UnsafeMutablePointer<io_iterator_t>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryCreateIterator(_ masterPort: mach_port_t, _ plane: ConstUnsafePointer<Int8>, _ options: IOOptionBits, _ iterator: UnsafePointer<io_iterator_t>) -> kern_return_t ``` |
| To | ``` func IORegistryCreateIterator(_ masterPort: mach_port_t, _ plane: UnsafePointer<Int8>, _ options: IOOptionBits, _ iterator: UnsafeMutablePointer<io_iterator_t>) -> kern_return_t ``` |

Modified IORegistryEntryCreateCFProperties(io_registry_entry_t, UnsafeMutablePointer<Unmanaged<CFMutableDictionary>?>, CFAllocator!, IOOptionBits) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryCreateCFProperties(_ entry: io_registry_entry_t, _ properties: UnsafePointer<Unmanaged<CFMutableDictionary>?>, _ allocator: CFAllocator!, _ options: IOOptionBits) -> kern_return_t ``` |
| To | ``` func IORegistryEntryCreateCFProperties(_ entry: io_registry_entry_t, _ properties: UnsafeMutablePointer<Unmanaged<CFMutableDictionary>?>, _ allocator: CFAllocator!, _ options: IOOptionBits) -> kern_return_t ``` |

Modified IORegistryEntryCreateIterator(io_registry_entry_t, UnsafePointer<Int8>, IOOptionBits, UnsafeMutablePointer<io_iterator_t>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryCreateIterator(_ entry: io_registry_entry_t, _ plane: ConstUnsafePointer<Int8>, _ options: IOOptionBits, _ iterator: UnsafePointer<io_iterator_t>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryCreateIterator(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>, _ options: IOOptionBits, _ iterator: UnsafeMutablePointer<io_iterator_t>) -> kern_return_t ``` |

Modified IORegistryEntryFromPath(mach_port_t, UnsafePointer<Int8>) -> io_registry_entry_t

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryFromPath(_ masterPort: mach_port_t, _ path: ConstUnsafePointer<Int8>) -> io_registry_entry_t ``` |
| To | ``` func IORegistryEntryFromPath(_ masterPort: mach_port_t, _ path: UnsafePointer<Int8>) -> io_registry_entry_t ``` |

Modified IORegistryEntryGetChildEntry(io_registry_entry_t, UnsafePointer<Int8>, UnsafeMutablePointer<io_registry_entry_t>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetChildEntry(_ entry: io_registry_entry_t, _ plane: ConstUnsafePointer<Int8>, _ child: UnsafePointer<io_registry_entry_t>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetChildEntry(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>, _ child: UnsafeMutablePointer<io_registry_entry_t>) -> kern_return_t ``` |

Modified IORegistryEntryGetChildIterator(io_registry_entry_t, UnsafePointer<Int8>, UnsafeMutablePointer<io_iterator_t>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetChildIterator(_ entry: io_registry_entry_t, _ plane: ConstUnsafePointer<Int8>, _ iterator: UnsafePointer<io_iterator_t>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetChildIterator(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>, _ iterator: UnsafeMutablePointer<io_iterator_t>) -> kern_return_t ``` |

Modified IORegistryEntryGetLocationInPlane(io_registry_entry_t, UnsafePointer<Int8>, UnsafeMutablePointer<Int8>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetLocationInPlane(_ entry: io_registry_entry_t, _ plane: ConstUnsafePointer<Int8>, _ location: UnsafePointer<Int8>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetLocationInPlane(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>, _ location: UnsafeMutablePointer<Int8>) -> kern_return_t ``` |

Modified IORegistryEntryGetName(io_registry_entry_t, UnsafeMutablePointer<Int8>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetName(_ entry: io_registry_entry_t, _ name: UnsafePointer<Int8>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetName(_ entry: io_registry_entry_t, _ name: UnsafeMutablePointer<Int8>) -> kern_return_t ``` |

Modified IORegistryEntryGetNameInPlane(io_registry_entry_t, UnsafePointer<Int8>, UnsafeMutablePointer<Int8>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetNameInPlane(_ entry: io_registry_entry_t, _ plane: ConstUnsafePointer<Int8>, _ name: UnsafePointer<Int8>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetNameInPlane(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>, _ name: UnsafeMutablePointer<Int8>) -> kern_return_t ``` |

Modified IORegistryEntryGetParentEntry(io_registry_entry_t, UnsafePointer<Int8>, UnsafeMutablePointer<io_registry_entry_t>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetParentEntry(_ entry: io_registry_entry_t, _ plane: ConstUnsafePointer<Int8>, _ parent: UnsafePointer<io_registry_entry_t>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetParentEntry(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>, _ parent: UnsafeMutablePointer<io_registry_entry_t>) -> kern_return_t ``` |

Modified IORegistryEntryGetParentIterator(io_registry_entry_t, UnsafePointer<Int8>, UnsafeMutablePointer<io_iterator_t>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetParentIterator(_ entry: io_registry_entry_t, _ plane: ConstUnsafePointer<Int8>, _ iterator: UnsafePointer<io_iterator_t>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetParentIterator(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>, _ iterator: UnsafeMutablePointer<io_iterator_t>) -> kern_return_t ``` |

Modified IORegistryEntryGetPath(io_registry_entry_t, UnsafePointer<Int8>, UnsafeMutablePointer<Int8>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetPath(_ entry: io_registry_entry_t, _ plane: ConstUnsafePointer<Int8>, _ path: UnsafePointer<Int8>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetPath(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>, _ path: UnsafeMutablePointer<Int8>) -> kern_return_t ``` |

Modified IORegistryEntryGetProperty(io_registry_entry_t, UnsafePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UInt32>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetProperty(_ entry: io_registry_entry_t, _ propertyName: ConstUnsafePointer<Int8>, _ buffer: UnsafePointer<Int8>, _ size: UnsafePointer<UInt32>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetProperty(_ entry: io_registry_entry_t, _ propertyName: UnsafePointer<Int8>, _ buffer: UnsafeMutablePointer<Int8>, _ size: UnsafeMutablePointer<UInt32>) -> kern_return_t ``` |

Modified IORegistryEntryGetRegistryEntryID(io_registry_entry_t, UnsafeMutablePointer<UInt64>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetRegistryEntryID(_ entry: io_registry_entry_t, _ entryID: UnsafePointer<UInt64>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetRegistryEntryID(_ entry: io_registry_entry_t, _ entryID: UnsafeMutablePointer<UInt64>) -> kern_return_t ``` |

Modified IORegistryEntryInPlane(io_registry_entry_t, UnsafePointer<Int8>) -> boolean_t

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryInPlane(_ entry: io_registry_entry_t, _ plane: ConstUnsafePointer<Int8>) -> boolean_t ``` |
| To | ``` func IORegistryEntryInPlane(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>) -> boolean_t ``` |

Modified IORegistryEntrySearchCFProperty(io_registry_entry_t, UnsafePointer<Int8>, CFString!, CFAllocator!, IOOptionBits) -> AnyObject!

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntrySearchCFProperty(_ entry: io_registry_entry_t, _ plane: ConstUnsafePointer<Int8>, _ key: CFString!, _ allocator: CFAllocator!, _ options: IOOptionBits) -> AnyObject! ``` |
| To | ``` func IORegistryEntrySearchCFProperty(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>, _ key: CFString!, _ allocator: CFAllocator!, _ options: IOOptionBits) -> AnyObject! ``` |

Modified IOServiceAddInterestNotification(IONotificationPortRef, io_service_t, UnsafePointer<Int8>, IOServiceInterestCallback, UnsafeMutablePointer<Void>, UnsafeMutablePointer<io_object_t>) -> kern_return_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOServiceAddInterestNotification(_ notifyPort: IONotificationPort!, _ service: io_service_t, _ interestType: ConstUnsafePointer<Int8>, _ callback: IOServiceInterestCallback, _ refCon: UnsafePointer<()>, _ notification: UnsafePointer<io_object_t>) -> kern_return_t ``` | OS X 10.10 |
| To | ``` func IOServiceAddInterestNotification(_ notifyPort: IONotificationPortRef, _ service: io_service_t, _ interestType: UnsafePointer<Int8>, _ callback: IOServiceInterestCallback, _ refCon: UnsafeMutablePointer<Void>, _ notification: UnsafeMutablePointer<io_object_t>) -> kern_return_t ``` | OS X 10.10.3 |

Modified IOServiceAddMatchingNotification(IONotificationPortRef, UnsafePointer<Int8>, CFDictionary!, IOServiceMatchingCallback, UnsafeMutablePointer<Void>, UnsafeMutablePointer<io_iterator_t>) -> kern_return_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOServiceAddMatchingNotification(_ notifyPort: IONotificationPort!, _ notificationType: ConstUnsafePointer<Int8>, _ matching: CFDictionary!, _ callback: IOServiceMatchingCallback, _ refCon: UnsafePointer<()>, _ notification: UnsafePointer<io_iterator_t>) -> kern_return_t ``` | OS X 10.10 |
| To | ``` func IOServiceAddMatchingNotification(_ notifyPort: IONotificationPortRef, _ notificationType: UnsafePointer<Int8>, _ matching: CFDictionary!, _ callback: IOServiceMatchingCallback, _ refCon: UnsafeMutablePointer<Void>, _ notification: UnsafeMutablePointer<io_iterator_t>) -> kern_return_t ``` | OS X 10.10.3 |

Modified IOServiceGetBusyState(io_service_t, UnsafeMutablePointer<UInt32>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IOServiceGetBusyState(_ service: io_service_t, _ busyState: UnsafePointer<UInt32>) -> kern_return_t ``` |
| To | ``` func IOServiceGetBusyState(_ service: io_service_t, _ busyState: UnsafeMutablePointer<UInt32>) -> kern_return_t ``` |

Modified IOServiceGetMatchingServices(mach_port_t, CFDictionary!, UnsafeMutablePointer<io_iterator_t>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IOServiceGetMatchingServices(_ masterPort: mach_port_t, _ matching: CFDictionary!, _ existing: UnsafePointer<io_iterator_t>) -> kern_return_t ``` |
| To | ``` func IOServiceGetMatchingServices(_ masterPort: mach_port_t, _ matching: CFDictionary!, _ existing: UnsafeMutablePointer<io_iterator_t>) -> kern_return_t ``` |

Modified IOServiceInterestCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias IOServiceInterestCallback = CFunctionPointer<((UnsafePointer<()>, io_service_t, UInt32, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias IOServiceInterestCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, io_service_t, UInt32, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified IOServiceMatchPropertyTable(io_service_t, CFDictionary!, UnsafeMutablePointer<boolean_t>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IOServiceMatchPropertyTable(_ service: io_service_t, _ matching: CFDictionary!, _ matches: UnsafePointer<boolean_t>) -> kern_return_t ``` |
| To | ``` func IOServiceMatchPropertyTable(_ service: io_service_t, _ matching: CFDictionary!, _ matches: UnsafeMutablePointer<boolean_t>) -> kern_return_t ``` |

Modified IOServiceMatching(UnsafePointer<Int8>) -> Unmanaged<CFMutableDictionary>!

|  | Declaration |
| --- | --- |
| From | ``` func IOServiceMatching(_ name: ConstUnsafePointer<Int8>) -> Unmanaged<CFMutableDictionary>! ``` |
| To | ``` func IOServiceMatching(_ name: UnsafePointer<Int8>) -> Unmanaged<CFMutableDictionary>! ``` |

Modified IOServiceMatchingCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias IOServiceMatchingCallback = CFunctionPointer<((UnsafePointer<()>, io_iterator_t) -> Void)> ``` |
| To | ``` typealias IOServiceMatchingCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, io_iterator_t) -> Void)> ``` |

Modified IOServiceNameMatching(UnsafePointer<Int8>) -> Unmanaged<CFMutableDictionary>!

|  | Declaration |
| --- | --- |
| From | ``` func IOServiceNameMatching(_ name: ConstUnsafePointer<Int8>) -> Unmanaged<CFMutableDictionary>! ``` |
| To | ``` func IOServiceNameMatching(_ name: UnsafePointer<Int8>) -> Unmanaged<CFMutableDictionary>! ``` |

Modified IOServiceOpen(io_service_t, task_port_t, UInt32, UnsafeMutablePointer<io_connect_t>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IOServiceOpen(_ service: io_service_t, _ owningTask: task_port_t, _ type: UInt32, _ connect: UnsafePointer<io_connect_t>) -> kern_return_t ``` |
| To | ``` func IOServiceOpen(_ service: io_service_t, _ owningTask: task_port_t, _ type: UInt32, _ connect: UnsafeMutablePointer<io_connect_t>) -> kern_return_t ``` |

Modified IOServiceWaitQuiet(io_service_t, UnsafeMutablePointer<mach_timespec_t>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func IOServiceWaitQuiet(_ service: io_service_t, _ waitTime: UnsafePointer<mach_timespec_t>) -> kern_return_t ``` |
| To | ``` func IOServiceWaitQuiet(_ service: io_service_t, _ waitTime: UnsafeMutablePointer<mach_timespec_t>) -> kern_return_t ``` |

Modified IOURLCreateDataAndPropertiesFromResource(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFData>?>, UnsafeMutablePointer<Unmanaged<CFDictionary>?>, CFArray!, UnsafeMutablePointer<Int32>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func IOURLCreateDataAndPropertiesFromResource(_ alloc: CFAllocator!, _ url: CFURL!, _ resourceData: UnsafePointer<Unmanaged<CFData>?>, _ properties: UnsafePointer<Unmanaged<CFDictionary>?>, _ desiredProperties: CFArray!, _ errorCode: UnsafePointer<Int32>) -> Boolean ``` |
| To | ``` func IOURLCreateDataAndPropertiesFromResource(_ alloc: CFAllocator!, _ url: CFURL!, _ resourceData: UnsafeMutablePointer<Unmanaged<CFData>?>, _ properties: UnsafeMutablePointer<Unmanaged<CFDictionary>?>, _ desiredProperties: CFArray!, _ errorCode: UnsafeMutablePointer<Int32>) -> Boolean ``` |

Modified IOURLCreatePropertyFromResource(CFAllocator!, CFURL!, CFString!, UnsafeMutablePointer<Int32>) -> Unmanaged<AnyObject>!

|  | Declaration |
| --- | --- |
| From | ``` func IOURLCreatePropertyFromResource(_ alloc: CFAllocator!, _ url: CFURL!, _ property: CFString!, _ errorCode: UnsafePointer<Int32>) -> Unmanaged<AnyObject>! ``` |
| To | ``` func IOURLCreatePropertyFromResource(_ alloc: CFAllocator!, _ url: CFURL!, _ property: CFString!, _ errorCode: UnsafeMutablePointer<Int32>) -> Unmanaged<AnyObject>! ``` |

Modified IOURLWriteDataAndPropertiesToResource(CFURL!, CFData!, CFDictionary!, UnsafeMutablePointer<Int32>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func IOURLWriteDataAndPropertiesToResource(_ url: CFURL!, _ dataToWrite: CFData!, _ propertiesToWrite: CFDictionary!, _ errorCode: UnsafePointer<Int32>) -> Boolean ``` |
| To | ``` func IOURLWriteDataAndPropertiesToResource(_ url: CFURL!, _ dataToWrite: CFData!, _ propertiesToWrite: CFDictionary!, _ errorCode: UnsafeMutablePointer<Int32>) -> Boolean ``` |

Modified OSGetNotificationFromMessage(UnsafeMutablePointer<mach_msg_header_t>, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<vm_size_t>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func OSGetNotificationFromMessage(_ msg: UnsafePointer<mach_msg_header_t>, _ index: UInt32, _ type: UnsafePointer<UInt32>, _ reference: UnsafePointer<UInt>, _ content: UnsafePointer<UnsafePointer<()>>, _ size: UnsafePointer<vm_size_t>) -> kern_return_t ``` |
| To | ``` func OSGetNotificationFromMessage(_ msg: UnsafeMutablePointer<mach_msg_header_t>, _ index: UInt32, _ type: UnsafeMutablePointer<UInt32>, _ reference: UnsafeMutablePointer<UInt>, _ content: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ size: UnsafeMutablePointer<vm_size_t>) -> kern_return_t ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
