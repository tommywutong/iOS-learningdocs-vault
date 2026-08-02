---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/IOKit.html
archived_at: '2026-07-18T02:51:26.533310Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# IOKit Changes for Swift

### IOKit

Removed IOCFPlugInInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, version: UInt16, revision: UInt16, Probe: ((UnsafeMutablePointer<Void>, CFDictionary!, io_service_t, UnsafeMutablePointer<Int32>) -> IOReturn)!, Start: ((UnsafeMutablePointer<Void>, CFDictionary!, io_service_t) -> IOReturn)!, Stop: ((UnsafeMutablePointer<Void>) -> IOReturn)!)Removed [IONamedValue.init(value: Int32, name: UnsafePointer<Int8>)](https://developer.apple.com/documentation/iokit/ionamedvalue/1514633-init)Removed [IOServiceInterestContent.init(messageType: natural_t, messageArgument: (UnsafeMutablePointer<Void>))](https://developer.apple.com/documentation/iokit/ioserviceinterestcontent/1514388-init)Added [IOCFPlugInInterfaceStruct.init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ( (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef: ( (UnsafeMutableRawPointer?) -> ULONG)!, Release: ( (UnsafeMutableRawPointer?) -> ULONG)!, version: UInt16, revision: UInt16, Probe: ( (UnsafeMutableRawPointer?, CFDictionary?, io_service_t, UnsafeMutablePointer<Int32>?) -> IOReturn)!, Start: ( (UnsafeMutableRawPointer?, CFDictionary?, io_service_t) -> IOReturn)!, Stop: ( (UnsafeMutableRawPointer?) -> IOReturn)!)](https://developer.apple.com/documentation/iokit/iocfplugininterfacestruct/1792000-init)Added [IONamedValue.init(value: Int32, name: UnsafePointer<Int8>!)](https://developer.apple.com/documentation/iokit/ionamedvalue/1514633-init)Added [IOServiceInterestContent.init(messageType: natural_t, messageArgument: (UnsafeMutableRawPointer?))](https://developer.apple.com/documentation/iokit/ioserviceinterestcontent/1514388-init)Added [IO_OBJECT_NULL](https://developer.apple.com/documentation/iokit/io_object_null)Added [kIOBSDKey](https://developer.apple.com/documentation/iokit/kiobsdkey)Added [kIOMinimumSaturationByteCountKey](https://developer.apple.com/documentation/iokit/kiominimumsaturationbytecountkey)Added [kIOPropertyExistsMatchKey](https://developer.apple.com/documentation/iokit/kiopropertyexistsmatchkey)Added [kIORegistryEntryPropertyKeysKey](https://developer.apple.com/documentation/iokit/kioregistryentrypropertykeyskey)Added [kIOResourceMatchedKey](https://developer.apple.com/documentation/iokit/kioresourcematchedkey)Added [kIOReturnAborted](https://developer.apple.com/documentation/iokit/kioreturnaborted)Added [kIOReturnBadArgument](https://developer.apple.com/documentation/iokit/kioreturnbadargument)Added [kIOReturnBadMedia](https://developer.apple.com/documentation/iokit/kioreturnbadmedia)Added [kIOReturnBadMessageID](https://developer.apple.com/documentation/iokit/kioreturnbadmessageid)Added [kIOReturnBusy](https://developer.apple.com/documentation/iokit/kioreturnbusy)Added [kIOReturnCannotLock](https://developer.apple.com/documentation/iokit/kioreturncannotlock)Added [kIOReturnCannotWire](https://developer.apple.com/documentation/iokit/kioreturncannotwire)Added [kIOReturnDeviceError](https://developer.apple.com/documentation/iokit/kioreturndeviceerror)Added [kIOReturnDMAError](https://developer.apple.com/documentation/iokit/kioreturndmaerror)Added [kIOReturnError](https://developer.apple.com/documentation/iokit/kioreturnerror)Added [kIOReturnExclusiveAccess](https://developer.apple.com/documentation/iokit/kioreturnexclusiveaccess)Added [kIOReturnInternalError](https://developer.apple.com/documentation/iokit/kioreturninternalerror)Added [kIOReturnInvalid](https://developer.apple.com/documentation/iokit/kioreturninvalid)Added [kIOReturnIOError](https://developer.apple.com/documentation/iokit/kioreturnioerror)Added [kIOReturnIPCError](https://developer.apple.com/documentation/iokit/kioreturnipcerror)Added [kIOReturnIsoTooNew](https://developer.apple.com/documentation/iokit/kioreturnisotoonew)Added [kIOReturnIsoTooOld](https://developer.apple.com/documentation/iokit/kioreturnisotooold)Added [kIOReturnLockedRead](https://developer.apple.com/documentation/iokit/kioreturnlockedread)Added [kIOReturnLockedWrite](https://developer.apple.com/documentation/iokit/kioreturnlockedwrite)Added [kIOReturnMessageTooLarge](https://developer.apple.com/documentation/iokit/kioreturnmessagetoolarge)Added [kIOReturnNoBandwidth](https://developer.apple.com/documentation/iokit/kioreturnnobandwidth)Added [kIOReturnNoChannels](https://developer.apple.com/documentation/iokit/kioreturnnochannels)Added [kIOReturnNoCompletion](https://developer.apple.com/documentation/iokit/kioreturnnocompletion)Added [kIOReturnNoDevice](https://developer.apple.com/documentation/iokit/kioreturnnodevice)Added [kIOReturnNoFrames](https://developer.apple.com/documentation/iokit/kioreturnnoframes)Added [kIOReturnNoInterrupt](https://developer.apple.com/documentation/iokit/kioreturnnointerrupt)Added [kIOReturnNoMedia](https://developer.apple.com/documentation/iokit/kioreturnnomedia)Added [kIOReturnNoMemory](https://developer.apple.com/documentation/iokit/kioreturnnomemory)Added [kIOReturnNoPower](https://developer.apple.com/documentation/iokit/kioreturnnopower)Added [kIOReturnNoResources](https://developer.apple.com/documentation/iokit/kioreturnnoresources)Added [kIOReturnNoSpace](https://developer.apple.com/documentation/iokit/kioreturnnospace)Added [kIOReturnNotAligned](https://developer.apple.com/documentation/iokit/kioreturnnotaligned)Added [kIOReturnNotAttached](https://developer.apple.com/documentation/iokit/kioreturnnotattached)Added [kIOReturnNotFound](https://developer.apple.com/documentation/iokit/kioreturnnotfound)Added [kIOReturnNotOpen](https://developer.apple.com/documentation/iokit/kioreturnnotopen)Added [kIOReturnNotPermitted](https://developer.apple.com/documentation/iokit/kioreturnnotpermitted)Added [kIOReturnNotPrivileged](https://developer.apple.com/documentation/iokit/kioreturnnotprivileged)Added [kIOReturnNotReadable](https://developer.apple.com/documentation/iokit/kioreturnnotreadable)Added [kIOReturnNotReady](https://developer.apple.com/documentation/iokit/kioreturnnotready)Added [kIOReturnNotResponding](https://developer.apple.com/documentation/iokit/kioreturnnotresponding)Added [kIOReturnNotWritable](https://developer.apple.com/documentation/iokit/kioreturnnotwritable)Added [kIOReturnOffline](https://developer.apple.com/documentation/iokit/kioreturnoffline)Added [kIOReturnOverrun](https://developer.apple.com/documentation/iokit/kioreturnoverrun)Added [kIOReturnPortExists](https://developer.apple.com/documentation/iokit/kioreturnportexists)Added [kIOReturnRLDError](https://developer.apple.com/documentation/iokit/kioreturnrlderror)Added [kIOReturnStillOpen](https://developer.apple.com/documentation/iokit/kioreturnstillopen)Added [kIOReturnTimeout](https://developer.apple.com/documentation/iokit/kioreturntimeout)Added [kIOReturnUnderrun](https://developer.apple.com/documentation/iokit/kioreturnunderrun)Added [kIOReturnUnformattedMedia](https://developer.apple.com/documentation/iokit/kioreturnunformattedmedia)Added [kIOReturnUnsupported](https://developer.apple.com/documentation/iokit/kioreturnunsupported)Added [kIOReturnUnsupportedMode](https://developer.apple.com/documentation/iokit/kioreturnunsupportedmode)Added [kIOReturnVMError](https://developer.apple.com/documentation/iokit/kioreturnvmerror)Modified [IOCFPlugInInterfaceStruct [struct]](https://developer.apple.com/documentation/iokit/iocfplugininterfacestruct)

|  | Declaration |
| --- | --- |
| From | ``` struct IOCFPlugInInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!     var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!     var Release: ((UnsafeMutablePointer<Void>) -> ULONG)!     var version: UInt16     var revision: UInt16     var Probe: ((UnsafeMutablePointer<Void>, CFDictionary!, io_service_t, UnsafeMutablePointer<Int32>) -> IOReturn)!     var Start: ((UnsafeMutablePointer<Void>, CFDictionary!, io_service_t) -> IOReturn)!     var Stop: ((UnsafeMutablePointer<Void>) -> IOReturn)!     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, version version: UInt16, revision revision: UInt16, Probe Probe: ((UnsafeMutablePointer<Void>, CFDictionary!, io_service_t, UnsafeMutablePointer<Int32>) -> IOReturn)!, Start Start: ((UnsafeMutablePointer<Void>, CFDictionary!, io_service_t) -> IOReturn)!, Stop Stop: ((UnsafeMutablePointer<Void>) -> IOReturn)!) } ``` |
| To | ``` struct IOCFPlugInInterfaceStruct {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var version: UInt16     var revision: UInt16     var Probe: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t, UnsafeMutablePointer<Int32>?) -> IOReturn)!     var Start: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t) -> IOReturn)!     var Stop: ((UnsafeMutableRawPointer?) -> IOReturn)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, version version: UInt16, revision revision: UInt16, Probe Probe: (@escaping (UnsafeMutableRawPointer?, CFDictionary?, io_service_t, UnsafeMutablePointer<Int32>?) -> IOReturn)!, Start Start: (@escaping (UnsafeMutableRawPointer?, CFDictionary?, io_service_t) -> IOReturn)!, Stop Stop: (@escaping (UnsafeMutableRawPointer?) -> IOReturn)!) } ``` |

Modified [IOCFPlugInInterfaceStruct.AddRef](https://developer.apple.com/documentation/iokit/iocfplugininterfacestruct/1412440-addref)

|  | Declaration |
| --- | --- |
| From | ``` var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |
| To | ``` var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)! ``` |

Modified [IOCFPlugInInterfaceStruct.Probe](https://developer.apple.com/documentation/iokit/iocfplugininterface/1412435-probe)

|  | Declaration |
| --- | --- |
| From | ``` var Probe: ((UnsafeMutablePointer<Void>, CFDictionary!, io_service_t, UnsafeMutablePointer<Int32>) -> IOReturn)! ``` |
| To | ``` var Probe: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t, UnsafeMutablePointer<Int32>?) -> IOReturn)! ``` |

Modified [IOCFPlugInInterfaceStruct.QueryInterface](https://developer.apple.com/documentation/iokit/iocfplugininterfacestruct/1412423-queryinterface)

|  | Declaration |
| --- | --- |
| From | ``` var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)! ``` |
| To | ``` var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)! ``` |

Modified [IOCFPlugInInterfaceStruct.Release](https://developer.apple.com/documentation/iokit/iocfplugininterfacestruct/1412422-release)

|  | Declaration |
| --- | --- |
| From | ``` var Release: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |
| To | ``` var Release: ((UnsafeMutableRawPointer?) -> ULONG)! ``` |

Modified [IOCFPlugInInterfaceStruct.Start](https://developer.apple.com/documentation/iokit/iocfplugininterfacestruct/1412433-start)

|  | Declaration |
| --- | --- |
| From | ``` var Start: ((UnsafeMutablePointer<Void>, CFDictionary!, io_service_t) -> IOReturn)! ``` |
| To | ``` var Start: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t) -> IOReturn)! ``` |

Modified [IOCFPlugInInterfaceStruct.Stop](https://developer.apple.com/documentation/iokit/iocfplugininterface/1412438-stop)

|  | Declaration |
| --- | --- |
| From | ``` var Stop: ((UnsafeMutablePointer<Void>) -> IOReturn)! ``` |
| To | ``` var Stop: ((UnsafeMutableRawPointer?) -> IOReturn)! ``` |

Modified [IONamedValue [struct]](https://developer.apple.com/documentation/iokit/ionamedvalue)

|  | Declaration |
| --- | --- |
| From | ``` struct IONamedValue {     var value: Int32     var name: UnsafePointer<Int8>     init()     init(value value: Int32, name name: UnsafePointer<Int8>) } ``` |
| To | ``` struct IONamedValue {     var value: Int32     var name: UnsafePointer<Int8>!     init()     init(value value: Int32, name name: UnsafePointer<Int8>!) } ``` |

Modified [IONamedValue.name](https://developer.apple.com/documentation/iokit/ionamedvalue/1514729-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: UnsafePointer<Int8> ``` |
| To | ``` var name: UnsafePointer<Int8>! ``` |

Modified [IOServiceInterestContent [struct]](https://developer.apple.com/documentation/iokit/ioserviceinterestcontent)

|  | Declaration |
| --- | --- |
| From | ``` struct IOServiceInterestContent {     var messageType: natural_t     var messageArgument: (UnsafeMutablePointer<Void>)     init()     init(messageType messageType: natural_t, messageArgument messageArgument: (UnsafeMutablePointer<Void>)) } ``` |
| To | ``` struct IOServiceInterestContent {     var messageType: natural_t     var messageArgument: (UnsafeMutableRawPointer?)     init()     init(messageType messageType: natural_t, messageArgument messageArgument: (UnsafeMutableRawPointer?)) } ``` |

Modified [IOServiceInterestContent.messageArgument](https://developer.apple.com/documentation/iokit/ioserviceinterestcontent/1455538-messageargument)

|  | Declaration |
| --- | --- |
| From | ``` var messageArgument: (UnsafeMutablePointer<Void>) ``` |
| To | ``` var messageArgument: (UnsafeMutableRawPointer?) ``` |

Modified [OSNotificationHeader [struct]](https://developer.apple.com/documentation/iokit/osnotificationheader)

|  | Declaration |
| --- | --- |
| From | ``` struct OSNotificationHeader {     var size: mach_msg_size_t     var type: natural_t     var reference: OSAsyncReference     init() } ``` |
| To | ``` struct OSNotificationHeader {     var size: mach_msg_size_t     var type: natural_t     var reference: IOKit.OSAsyncReference     init() } ``` |

Modified [OSNotificationHeader.reference](https://developer.apple.com/documentation/iokit/osnotificationheader/1455523-reference)

|  | Declaration |
| --- | --- |
| From | ``` var reference: OSAsyncReference ``` |
| To | ``` var reference: IOKit.OSAsyncReference ``` |

Modified [OSNotificationHeader64 [struct]](https://developer.apple.com/documentation/iokit/osnotificationheader64)

|  | Declaration |
| --- | --- |
| From | ``` struct OSNotificationHeader64 {     var size: mach_msg_size_t     var type: natural_t     var reference: OSAsyncReference64     init() } ``` |
| To | ``` struct OSNotificationHeader64 {     var size: mach_msg_size_t     var type: natural_t     var reference: IOKit.OSAsyncReference64     init() } ``` |

Modified [OSNotificationHeader64.reference](https://developer.apple.com/documentation/iokit/osnotificationheader64/1455547-reference)

|  | Declaration |
| --- | --- |
| From | ``` var reference: OSAsyncReference64 ``` |
| To | ``` var reference: IOKit.OSAsyncReference64 ``` |

Modified [IOAsyncCallback](https://developer.apple.com/documentation/iokit/ioasynccallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOAsyncCallback = (UnsafeMutablePointer<Void>, IOReturn, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UInt32) -> Void ``` |
| To | ``` typealias IOAsyncCallback = (UnsafeMutableRawPointer?, IOReturn, UnsafeMutablePointer<UnsafeMutableRawPointer?>?, UInt32) -> Swift.Void ``` |

Modified [IOAsyncCallback0](https://developer.apple.com/documentation/iokit/ioasynccallback0)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOAsyncCallback0 = (UnsafeMutablePointer<Void>, IOReturn) -> Void ``` |
| To | ``` typealias IOAsyncCallback0 = (UnsafeMutableRawPointer?, IOReturn) -> Swift.Void ``` |

Modified [IOAsyncCallback1](https://developer.apple.com/documentation/iokit/ioasynccallback1)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOAsyncCallback1 = (UnsafeMutablePointer<Void>, IOReturn, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias IOAsyncCallback1 = (UnsafeMutableRawPointer?, IOReturn, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [IOAsyncCallback2](https://developer.apple.com/documentation/iokit/ioasynccallback2)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOAsyncCallback2 = (UnsafeMutablePointer<Void>, IOReturn, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias IOAsyncCallback2 = (UnsafeMutableRawPointer?, IOReturn, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [IOBSDNameMatching(_: mach_port_t, _: UInt32, _: UnsafePointer<Int8>!) -> CFMutableDictionary!](https://developer.apple.com/documentation/iokit/1514486-iobsdnamematching)

|  | Declaration |
| --- | --- |
| From | ``` func IOBSDNameMatching(_ masterPort: mach_port_t, _ options: UInt32, _ bsdName: UnsafePointer<Int8>) -> CFMutableDictionary! ``` |
| To | ``` func IOBSDNameMatching(_ masterPort: mach_port_t, _ options: UInt32, _ bsdName: UnsafePointer<Int8>!) -> CFMutableDictionary! ``` |

Modified [IOCatalogueGetData(_: mach_port_t, _: UInt32, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafeMutablePointer<UInt32>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514233-iocataloguegetdata)

|  | Declaration |
| --- | --- |
| From | ``` func IOCatalogueGetData(_ masterPort: mach_port_t, _ flag: UInt32, _ buffer: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ size: UnsafeMutablePointer<UInt32>) -> kern_return_t ``` |
| To | ``` func IOCatalogueGetData(_ masterPort: mach_port_t, _ flag: UInt32, _ buffer: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ size: UnsafeMutablePointer<UInt32>!) -> kern_return_t ``` |

Modified [IOCatalogueModuleLoaded(_: mach_port_t, _: UnsafeMutablePointer<Int8>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514886-iocataloguemoduleloaded)

|  | Declaration |
| --- | --- |
| From | ``` func IOCatalogueModuleLoaded(_ masterPort: mach_port_t, _ name: UnsafeMutablePointer<Int8>) -> kern_return_t ``` |
| To | ``` func IOCatalogueModuleLoaded(_ masterPort: mach_port_t, _ name: UnsafeMutablePointer<Int8>!) -> kern_return_t ``` |

Modified [IOCatalogueSendData(_: mach_port_t, _: UInt32, _: UnsafePointer<Int8>!, _: UInt32) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514405-iocataloguesenddata)

|  | Declaration |
| --- | --- |
| From | ``` func IOCatalogueSendData(_ masterPort: mach_port_t, _ flag: UInt32, _ buffer: UnsafePointer<Int8>, _ size: UInt32) -> kern_return_t ``` |
| To | ``` func IOCatalogueSendData(_ masterPort: mach_port_t, _ flag: UInt32, _ buffer: UnsafePointer<Int8>!, _ size: UInt32) -> kern_return_t ``` |

Modified [IOCatalogueTerminate(_: mach_port_t, _: UInt32, _: UnsafeMutablePointer<Int8>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514665-iocatalogueterminate)

|  | Declaration |
| --- | --- |
| From | ``` func IOCatalogueTerminate(_ masterPort: mach_port_t, _ flag: UInt32, _ description: UnsafeMutablePointer<Int8>) -> kern_return_t ``` |
| To | ``` func IOCatalogueTerminate(_ masterPort: mach_port_t, _ flag: UInt32, _ description: UnsafeMutablePointer<Int8>!) -> kern_return_t ``` |

Modified [IOCFSerialize(_: CFTypeRef!, _: CFOptionFlags) -> CFData!](https://developer.apple.com/documentation/iokit/1403329-iocfserialize)

|  | Declaration |
| --- | --- |
| From | ``` func IOCFSerialize(_ object: AnyObject!, _ options: CFOptionFlags) -> CFData! ``` |
| To | ``` func IOCFSerialize(_ object: CFTypeRef!, _ options: CFOptionFlags) -> CFData! ``` |

Modified [IOCFUnserialize(_: UnsafePointer<Int8>!, _: CFAllocator!, _: CFOptionFlags, _: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> CFTypeRef!](https://developer.apple.com/documentation/iokit/1514265-iocfunserialize)

|  | Declaration |
| --- | --- |
| From | ``` func IOCFUnserialize(_ buffer: UnsafePointer<Int8>, _ allocator: CFAllocator!, _ options: CFOptionFlags, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>) -> AnyObject! ``` |
| To | ``` func IOCFUnserialize(_ buffer: UnsafePointer<Int8>!, _ allocator: CFAllocator!, _ options: CFOptionFlags, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> CFTypeRef! ``` |

Modified [IOCFUnserializeBinary(_: UnsafePointer<Int8>!, _: Int, _: CFAllocator!, _: CFOptionFlags, _: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> CFTypeRef!](https://developer.apple.com/documentation/iokit/1514876-iocfunserializebinary)

|  | Declaration |
| --- | --- |
| From | ``` func IOCFUnserializeBinary(_ buffer: UnsafePointer<Int8>, _ bufferSize: Int, _ allocator: CFAllocator!, _ options: CFOptionFlags, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>) -> AnyObject! ``` |
| To | ``` func IOCFUnserializeBinary(_ buffer: UnsafePointer<Int8>!, _ bufferSize: Int, _ allocator: CFAllocator!, _ options: CFOptionFlags, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> CFTypeRef! ``` |

Modified [IOCFUnserializeWithSize(_: UnsafePointer<Int8>!, _: Int, _: CFAllocator!, _: CFOptionFlags, _: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> CFTypeRef!](https://developer.apple.com/documentation/iokit/1514745-iocfunserializewithsize)

|  | Declaration |
| --- | --- |
| From | ``` func IOCFUnserializeWithSize(_ buffer: UnsafePointer<Int8>, _ bufferSize: Int, _ allocator: CFAllocator!, _ options: CFOptionFlags, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>) -> AnyObject! ``` |
| To | ``` func IOCFUnserializeWithSize(_ buffer: UnsafePointer<Int8>!, _ bufferSize: Int, _ allocator: CFAllocator!, _ options: CFOptionFlags, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> CFTypeRef! ``` |

Modified [IOConnectCallAsyncMethod(_: mach_port_t, _: UInt32, _: mach_port_t, _: UnsafeMutablePointer<UInt64>!, _: UInt32, _: UnsafePointer<UInt64>!, _: UInt32, _: UnsafeRawPointer!, _: Int, _: UnsafeMutablePointer<UInt64>!, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514418-ioconnectcallasyncmethod)

|  | Declaration |
| --- | --- |
| From | ``` func IOConnectCallAsyncMethod(_ connection: mach_port_t, _ selector: UInt32, _ wake_port: mach_port_t, _ reference: UnsafeMutablePointer<UInt64>, _ referenceCnt: UInt32, _ input: UnsafePointer<UInt64>, _ inputCnt: UInt32, _ inputStruct: UnsafePointer<Void>, _ inputStructCnt: Int, _ output: UnsafeMutablePointer<UInt64>, _ outputCnt: UnsafeMutablePointer<UInt32>, _ outputStruct: UnsafeMutablePointer<Void>, _ outputStructCnt: UnsafeMutablePointer<Int>) -> kern_return_t ``` |
| To | ``` func IOConnectCallAsyncMethod(_ connection: mach_port_t, _ selector: UInt32, _ wake_port: mach_port_t, _ reference: UnsafeMutablePointer<UInt64>!, _ referenceCnt: UInt32, _ input: UnsafePointer<UInt64>!, _ inputCnt: UInt32, _ inputStruct: UnsafeRawPointer!, _ inputStructCnt: Int, _ output: UnsafeMutablePointer<UInt64>!, _ outputCnt: UnsafeMutablePointer<UInt32>!, _ outputStruct: UnsafeMutableRawPointer!, _ outputStructCnt: UnsafeMutablePointer<Int>!) -> kern_return_t ``` |

Modified [IOConnectCallAsyncScalarMethod(_: mach_port_t, _: UInt32, _: mach_port_t, _: UnsafeMutablePointer<UInt64>!, _: UInt32, _: UnsafePointer<UInt64>!, _: UInt32, _: UnsafeMutablePointer<UInt64>!, _: UnsafeMutablePointer<UInt32>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514884-ioconnectcallasyncscalarmethod)

|  | Declaration |
| --- | --- |
| From | ``` func IOConnectCallAsyncScalarMethod(_ connection: mach_port_t, _ selector: UInt32, _ wake_port: mach_port_t, _ reference: UnsafeMutablePointer<UInt64>, _ referenceCnt: UInt32, _ input: UnsafePointer<UInt64>, _ inputCnt: UInt32, _ output: UnsafeMutablePointer<UInt64>, _ outputCnt: UnsafeMutablePointer<UInt32>) -> kern_return_t ``` |
| To | ``` func IOConnectCallAsyncScalarMethod(_ connection: mach_port_t, _ selector: UInt32, _ wake_port: mach_port_t, _ reference: UnsafeMutablePointer<UInt64>!, _ referenceCnt: UInt32, _ input: UnsafePointer<UInt64>!, _ inputCnt: UInt32, _ output: UnsafeMutablePointer<UInt64>!, _ outputCnt: UnsafeMutablePointer<UInt32>!) -> kern_return_t ``` |

Modified [IOConnectCallAsyncStructMethod(_: mach_port_t, _: UInt32, _: mach_port_t, _: UnsafeMutablePointer<UInt64>!, _: UInt32, _: UnsafeRawPointer!, _: Int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514403-ioconnectcallasyncstructmethod)

|  | Declaration |
| --- | --- |
| From | ``` func IOConnectCallAsyncStructMethod(_ connection: mach_port_t, _ selector: UInt32, _ wake_port: mach_port_t, _ reference: UnsafeMutablePointer<UInt64>, _ referenceCnt: UInt32, _ inputStruct: UnsafePointer<Void>, _ inputStructCnt: Int, _ outputStruct: UnsafeMutablePointer<Void>, _ outputStructCnt: UnsafeMutablePointer<Int>) -> kern_return_t ``` |
| To | ``` func IOConnectCallAsyncStructMethod(_ connection: mach_port_t, _ selector: UInt32, _ wake_port: mach_port_t, _ reference: UnsafeMutablePointer<UInt64>!, _ referenceCnt: UInt32, _ inputStruct: UnsafeRawPointer!, _ inputStructCnt: Int, _ outputStruct: UnsafeMutableRawPointer!, _ outputStructCnt: UnsafeMutablePointer<Int>!) -> kern_return_t ``` |

Modified [IOConnectCallMethod(_: mach_port_t, _: UInt32, _: UnsafePointer<UInt64>!, _: UInt32, _: UnsafeRawPointer!, _: Int, _: UnsafeMutablePointer<UInt64>!, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514240-ioconnectcallmethod)

|  | Declaration |
| --- | --- |
| From | ``` func IOConnectCallMethod(_ connection: mach_port_t, _ selector: UInt32, _ input: UnsafePointer<UInt64>, _ inputCnt: UInt32, _ inputStruct: UnsafePointer<Void>, _ inputStructCnt: Int, _ output: UnsafeMutablePointer<UInt64>, _ outputCnt: UnsafeMutablePointer<UInt32>, _ outputStruct: UnsafeMutablePointer<Void>, _ outputStructCnt: UnsafeMutablePointer<Int>) -> kern_return_t ``` |
| To | ``` func IOConnectCallMethod(_ connection: mach_port_t, _ selector: UInt32, _ input: UnsafePointer<UInt64>!, _ inputCnt: UInt32, _ inputStruct: UnsafeRawPointer!, _ inputStructCnt: Int, _ output: UnsafeMutablePointer<UInt64>!, _ outputCnt: UnsafeMutablePointer<UInt32>!, _ outputStruct: UnsafeMutableRawPointer!, _ outputStructCnt: UnsafeMutablePointer<Int>!) -> kern_return_t ``` |

Modified [IOConnectCallScalarMethod(_: mach_port_t, _: UInt32, _: UnsafePointer<UInt64>!, _: UInt32, _: UnsafeMutablePointer<UInt64>!, _: UnsafeMutablePointer<UInt32>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514793-ioconnectcallscalarmethod)

|  | Declaration |
| --- | --- |
| From | ``` func IOConnectCallScalarMethod(_ connection: mach_port_t, _ selector: UInt32, _ input: UnsafePointer<UInt64>, _ inputCnt: UInt32, _ output: UnsafeMutablePointer<UInt64>, _ outputCnt: UnsafeMutablePointer<UInt32>) -> kern_return_t ``` |
| To | ``` func IOConnectCallScalarMethod(_ connection: mach_port_t, _ selector: UInt32, _ input: UnsafePointer<UInt64>!, _ inputCnt: UInt32, _ output: UnsafeMutablePointer<UInt64>!, _ outputCnt: UnsafeMutablePointer<UInt32>!) -> kern_return_t ``` |

Modified [IOConnectCallStructMethod(_: mach_port_t, _: UInt32, _: UnsafeRawPointer!, _: Int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514274-ioconnectcallstructmethod)

|  | Declaration |
| --- | --- |
| From | ``` func IOConnectCallStructMethod(_ connection: mach_port_t, _ selector: UInt32, _ inputStruct: UnsafePointer<Void>, _ inputStructCnt: Int, _ outputStruct: UnsafeMutablePointer<Void>, _ outputStructCnt: UnsafeMutablePointer<Int>) -> kern_return_t ``` |
| To | ``` func IOConnectCallStructMethod(_ connection: mach_port_t, _ selector: UInt32, _ inputStruct: UnsafeRawPointer!, _ inputStructCnt: Int, _ outputStruct: UnsafeMutableRawPointer!, _ outputStructCnt: UnsafeMutablePointer<Int>!) -> kern_return_t ``` |

Modified [IOConnectGetService(_: io_connect_t, _: UnsafeMutablePointer<io_service_t>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514438-ioconnectgetservice)

|  | Declaration |
| --- | --- |
| From | ``` func IOConnectGetService(_ connect: io_connect_t, _ service: UnsafeMutablePointer<io_service_t>) -> kern_return_t ``` |
| To | ``` func IOConnectGetService(_ connect: io_connect_t, _ service: UnsafeMutablePointer<io_service_t>!) -> kern_return_t ``` |

Modified [IOConnectMapMemory(_: io_connect_t, _: UInt32, _: task_port_t, _: UnsafeMutablePointer<mach_vm_address_t>!, _: UnsafeMutablePointer<mach_vm_size_t>!, _: IOOptionBits) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514377-ioconnectmapmemory)

|  | Declaration |
| --- | --- |
| From | ``` func IOConnectMapMemory(_ connect: io_connect_t, _ memoryType: UInt32, _ intoTask: task_port_t, _ atAddress: UnsafeMutablePointer<mach_vm_address_t>, _ ofSize: UnsafeMutablePointer<mach_vm_size_t>, _ options: IOOptionBits) -> kern_return_t ``` |
| To | ``` func IOConnectMapMemory(_ connect: io_connect_t, _ memoryType: UInt32, _ intoTask: task_port_t, _ atAddress: UnsafeMutablePointer<mach_vm_address_t>!, _ ofSize: UnsafeMutablePointer<mach_vm_size_t>!, _ options: IOOptionBits) -> kern_return_t ``` |

Modified [IOConnectMapMemory64(_: io_connect_t, _: UInt32, _: task_port_t, _: UnsafeMutablePointer<mach_vm_address_t>!, _: UnsafeMutablePointer<mach_vm_size_t>!, _: IOOptionBits) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514862-ioconnectmapmemory64)

|  | Declaration |
| --- | --- |
| From | ``` func IOConnectMapMemory64(_ connect: io_connect_t, _ memoryType: UInt32, _ intoTask: task_port_t, _ atAddress: UnsafeMutablePointer<mach_vm_address_t>, _ ofSize: UnsafeMutablePointer<mach_vm_size_t>, _ options: IOOptionBits) -> kern_return_t ``` |
| To | ``` func IOConnectMapMemory64(_ connect: io_connect_t, _ memoryType: UInt32, _ intoTask: task_port_t, _ atAddress: UnsafeMutablePointer<mach_vm_address_t>!, _ ofSize: UnsafeMutablePointer<mach_vm_size_t>!, _ options: IOOptionBits) -> kern_return_t ``` |

Modified [IOConnectSetCFProperties(_: io_connect_t, _: CFTypeRef!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514713-ioconnectsetcfproperties)

|  | Declaration |
| --- | --- |
| From | ``` func IOConnectSetCFProperties(_ connect: io_connect_t, _ properties: AnyObject!) -> kern_return_t ``` |
| To | ``` func IOConnectSetCFProperties(_ connect: io_connect_t, _ properties: CFTypeRef!) -> kern_return_t ``` |

Modified [IOConnectSetCFProperty(_: io_connect_t, _: CFString!, _: CFTypeRef!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514796-ioconnectsetcfproperty)

|  | Declaration |
| --- | --- |
| From | ``` func IOConnectSetCFProperty(_ connect: io_connect_t, _ propertyName: CFString!, _ property: AnyObject!) -> kern_return_t ``` |
| To | ``` func IOConnectSetCFProperty(_ connect: io_connect_t, _ propertyName: CFString!, _ property: CFTypeRef!) -> kern_return_t ``` |

Modified [IOCreatePlugInInterfaceForService(_: io_service_t, _: CFUUID!, _: CFUUID!, _: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<IOCFPlugInInterface>?>?>!, _: UnsafeMutablePointer<Int32>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1412429-iocreateplugininterfaceforservic)

|  | Declaration |
| --- | --- |
| From | ``` func IOCreatePlugInInterfaceForService(_ service: io_service_t, _ pluginType: CFUUID!, _ interfaceType: CFUUID!, _ theInterface: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<IOCFPlugInInterface>>>, _ theScore: UnsafeMutablePointer<Int32>) -> kern_return_t ``` |
| To | ``` func IOCreatePlugInInterfaceForService(_ service: io_service_t, _ pluginType: CFUUID!, _ interfaceType: CFUUID!, _ theInterface: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<IOCFPlugInInterface>?>?>!, _ theScore: UnsafeMutablePointer<Int32>!) -> kern_return_t ``` |

Modified [IOCreateReceivePort(_: UInt32, _: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514698-iocreatereceiveport)

|  | Declaration |
| --- | --- |
| From | ``` func IOCreateReceivePort(_ msgType: UInt32, _ recvPort: UnsafeMutablePointer<mach_port_t>) -> kern_return_t ``` |
| To | ``` func IOCreateReceivePort(_ msgType: UInt32, _ recvPort: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t ``` |

Modified [IODataQueueDataAvailable(_: UnsafeMutablePointer<IODataQueueMemory>!) -> Bool](https://developer.apple.com/documentation/iokit/1514386-iodataqueuedataavailable)

|  | Declaration |
| --- | --- |
| From | ``` func IODataQueueDataAvailable(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>) -> Bool ``` |
| To | ``` func IODataQueueDataAvailable(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>!) -> Bool ``` |

Modified [IODataQueueDequeue(_: UnsafeMutablePointer<IODataQueueMemory>!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<UInt32>!) -> IOReturn](https://developer.apple.com/documentation/iokit/1514287-iodataqueuedequeue)

|  | Declaration |
| --- | --- |
| From | ``` func IODataQueueDequeue(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>, _ data: UnsafeMutablePointer<Void>, _ dataSize: UnsafeMutablePointer<UInt32>) -> IOReturn ``` |
| To | ``` func IODataQueueDequeue(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>!, _ data: UnsafeMutableRawPointer!, _ dataSize: UnsafeMutablePointer<UInt32>!) -> IOReturn ``` |

Modified [IODataQueueEnqueue(_: UnsafeMutablePointer<IODataQueueMemory>!, _: UnsafeMutableRawPointer!, _: UInt32) -> IOReturn](https://developer.apple.com/documentation/iokit/1514482-iodataqueueenqueue)

|  | Declaration |
| --- | --- |
| From | ``` func IODataQueueEnqueue(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>, _ data: UnsafeMutablePointer<Void>, _ dataSize: UInt32) -> IOReturn ``` |
| To | ``` func IODataQueueEnqueue(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>!, _ data: UnsafeMutableRawPointer!, _ dataSize: UInt32) -> IOReturn ``` |

Modified [IODataQueuePeek(_: UnsafeMutablePointer<IODataQueueMemory>!) -> UnsafeMutablePointer<IODataQueueEntry>!](https://developer.apple.com/documentation/iokit/1514649-iodataqueuepeek)

|  | Declaration |
| --- | --- |
| From | ``` func IODataQueuePeek(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>) -> UnsafeMutablePointer<IODataQueueEntry> ``` |
| To | ``` func IODataQueuePeek(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>!) -> UnsafeMutablePointer<IODataQueueEntry>! ``` |

Modified [IODataQueueSetNotificationPort(_: UnsafeMutablePointer<IODataQueueMemory>!, _: mach_port_t) -> IOReturn](https://developer.apple.com/documentation/iokit/1514301-iodataqueuesetnotificationport)

|  | Declaration |
| --- | --- |
| From | ``` func IODataQueueSetNotificationPort(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>, _ notifyPort: mach_port_t) -> IOReturn ``` |
| To | ``` func IODataQueueSetNotificationPort(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>!, _ notifyPort: mach_port_t) -> IOReturn ``` |

Modified [IODataQueueWaitForAvailableData(_: UnsafeMutablePointer<IODataQueueMemory>!, _: mach_port_t) -> IOReturn](https://developer.apple.com/documentation/iokit/1514696-iodataqueuewaitforavailabledata)

|  | Declaration |
| --- | --- |
| From | ``` func IODataQueueWaitForAvailableData(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>, _ notificationPort: mach_port_t) -> IOReturn ``` |
| To | ``` func IODataQueueWaitForAvailableData(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>!, _ notificationPort: mach_port_t) -> IOReturn ``` |

Modified [IODestroyPlugInInterface(_: UnsafeMutablePointer<UnsafeMutablePointer<IOCFPlugInInterface>?>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1412425-iodestroyplugininterface)

|  | Declaration |
| --- | --- |
| From | ``` func IODestroyPlugInInterface(_ interface: UnsafeMutablePointer<UnsafeMutablePointer<IOCFPlugInInterface>>) -> kern_return_t ``` |
| To | ``` func IODestroyPlugInInterface(_ interface: UnsafeMutablePointer<UnsafeMutablePointer<IOCFPlugInInterface>?>!) -> kern_return_t ``` |

Modified [IODispatchCalloutFromMessage(_: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<mach_msg_header_t>!, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/iokit/1514775-iodispatchcalloutfrommessage)

|  | Declaration |
| --- | --- |
| From | ``` func IODispatchCalloutFromMessage(_ unused: UnsafeMutablePointer<Void>, _ msg: UnsafeMutablePointer<mach_msg_header_t>, _ reference: UnsafeMutablePointer<Void>) ``` |
| To | ``` func IODispatchCalloutFromMessage(_ unused: UnsafeMutableRawPointer!, _ msg: UnsafeMutablePointer<mach_msg_header_t>!, _ reference: UnsafeMutableRawPointer!) ``` |

Modified [IOKitGetBusyState(_: mach_port_t, _: UnsafeMutablePointer<UInt32>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514460-iokitgetbusystate)

|  | Declaration |
| --- | --- |
| From | ``` func IOKitGetBusyState(_ masterPort: mach_port_t, _ busyState: UnsafeMutablePointer<UInt32>) -> kern_return_t ``` |
| To | ``` func IOKitGetBusyState(_ masterPort: mach_port_t, _ busyState: UnsafeMutablePointer<UInt32>!) -> kern_return_t ``` |

Modified [IOKitWaitQuiet(_: mach_port_t, _: UnsafeMutablePointer<mach_timespec_t>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514440-iokitwaitquiet)

|  | Declaration |
| --- | --- |
| From | ``` func IOKitWaitQuiet(_ masterPort: mach_port_t, _ waitTime: UnsafeMutablePointer<mach_timespec_t>) -> kern_return_t ``` |
| To | ``` func IOKitWaitQuiet(_ masterPort: mach_port_t, _ waitTime: UnsafeMutablePointer<mach_timespec_t>!) -> kern_return_t ``` |

Modified [IOMasterPort(_: mach_port_t, _: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514652-iomasterport)

|  | Declaration |
| --- | --- |
| From | ``` func IOMasterPort(_ bootstrapPort: mach_port_t, _ masterPort: UnsafeMutablePointer<mach_port_t>) -> kern_return_t ``` |
| To | ``` func IOMasterPort(_ bootstrapPort: mach_port_t, _ masterPort: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t ``` |

Modified [IONotificationPortCreate(_: mach_port_t) -> IONotificationPortRef!](https://developer.apple.com/documentation/iokit/1514480-ionotificationportcreate)

|  | Declaration |
| --- | --- |
| From | ``` func IONotificationPortCreate(_ masterPort: mach_port_t) -> IONotificationPortRef ``` |
| To | ``` func IONotificationPortCreate(_ masterPort: mach_port_t) -> IONotificationPortRef! ``` |

Modified [IONotificationPortDestroy(_: IONotificationPortRef!)](https://developer.apple.com/documentation/iokit/1514751-ionotificationportdestroy)

|  | Declaration |
| --- | --- |
| From | ``` func IONotificationPortDestroy(_ notify: IONotificationPortRef) ``` |
| To | ``` func IONotificationPortDestroy(_ notify: IONotificationPortRef!) ``` |

Modified [IONotificationPortGetMachPort(_: IONotificationPortRef!) -> mach_port_t](https://developer.apple.com/documentation/iokit/1514875-ionotificationportgetmachport)

|  | Declaration |
| --- | --- |
| From | ``` func IONotificationPortGetMachPort(_ notify: IONotificationPortRef) -> mach_port_t ``` |
| To | ``` func IONotificationPortGetMachPort(_ notify: IONotificationPortRef!) -> mach_port_t ``` |

Modified [IONotificationPortGetRunLoopSource(_: IONotificationPortRef!) -> Unmanaged<CFRunLoopSource>!](https://developer.apple.com/documentation/iokit/1514599-ionotificationportgetrunloopsour)

|  | Declaration |
| --- | --- |
| From | ``` func IONotificationPortGetRunLoopSource(_ notify: IONotificationPortRef) -> Unmanaged<CFRunLoopSource>! ``` |
| To | ``` func IONotificationPortGetRunLoopSource(_ notify: IONotificationPortRef!) -> Unmanaged<CFRunLoopSource>! ``` |

Modified [IONotificationPortRef](https://developer.apple.com/documentation/iokit/ionotificationportref)

|  | Declaration |
| --- | --- |
| From | ``` typealias IONotificationPortRef = COpaquePointer ``` |
| To | ``` typealias IONotificationPortRef = OpaquePointer ``` |

Modified [IONotificationPortSetDispatchQueue(_: IONotificationPortRef!, _: DispatchQueue!)](https://developer.apple.com/documentation/iokit/1514596-ionotificationportsetdispatchque)

|  | Declaration |
| --- | --- |
| From | ``` func IONotificationPortSetDispatchQueue(_ notify: IONotificationPortRef, _ queue: dispatch_queue_t!) ``` |
| To | ``` func IONotificationPortSetDispatchQueue(_ notify: IONotificationPortRef!, _ queue: DispatchQueue!) ``` |

Modified [IOObjectConformsTo(_: io_object_t, _: UnsafePointer<Int8>!) -> boolean_t](https://developer.apple.com/documentation/iokit/1514505-ioobjectconformsto)

|  | Declaration |
| --- | --- |
| From | ``` func IOObjectConformsTo(_ object: io_object_t, _ className: UnsafePointer<Int8>) -> boolean_t ``` |
| To | ``` func IOObjectConformsTo(_ object: io_object_t, _ className: UnsafePointer<Int8>!) -> boolean_t ``` |

Modified [IOObjectGetClass(_: io_object_t, _: UnsafeMutablePointer<Int8>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514756-ioobjectgetclass)

|  | Declaration |
| --- | --- |
| From | ``` func IOObjectGetClass(_ object: io_object_t, _ className: UnsafeMutablePointer<Int8>) -> kern_return_t ``` |
| To | ``` func IOObjectGetClass(_ object: io_object_t, _ className: UnsafeMutablePointer<Int8>!) -> kern_return_t ``` |

Modified [IOOpenFirmwarePathMatching(_: mach_port_t, _: UInt32, _: UnsafePointer<Int8>!) -> Unmanaged<CFMutableDictionary>!](https://developer.apple.com/documentation/iokit/1514715-ioopenfirmwarepathmatching)

|  | Declaration |
| --- | --- |
| From | ``` func IOOpenFirmwarePathMatching(_ masterPort: mach_port_t, _ options: UInt32, _ path: UnsafePointer<Int8>) -> Unmanaged<CFMutableDictionary>! ``` |
| To | ``` func IOOpenFirmwarePathMatching(_ masterPort: mach_port_t, _ options: UInt32, _ path: UnsafePointer<Int8>!) -> Unmanaged<CFMutableDictionary>! ``` |

Modified [IORegistryCreateIterator(_: mach_port_t, _: UnsafePointer<Int8>!, _: IOOptionBits, _: UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514238-ioregistrycreateiterator)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryCreateIterator(_ masterPort: mach_port_t, _ plane: UnsafePointer<Int8>, _ options: IOOptionBits, _ iterator: UnsafeMutablePointer<io_iterator_t>) -> kern_return_t ``` |
| To | ``` func IORegistryCreateIterator(_ masterPort: mach_port_t, _ plane: UnsafePointer<Int8>!, _ options: IOOptionBits, _ iterator: UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t ``` |

Modified [IORegistryEntryCopyPath(_: io_registry_entry_t, _: UnsafePointer<Int8>!) -> Unmanaged<CFString>!](https://developer.apple.com/documentation/iokit/1514853-ioregistryentrycopypath)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryCopyPath(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>) -> Unmanaged<CFString>! ``` |
| To | ``` func IORegistryEntryCopyPath(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>!) -> Unmanaged<CFString>! ``` |

Modified [IORegistryEntryCreateCFProperties(_: io_registry_entry_t, _: UnsafeMutablePointer<Unmanaged<CFMutableDictionary>?>!, _: CFAllocator!, _: IOOptionBits) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514310-ioregistryentrycreatecfpropertie)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryCreateCFProperties(_ entry: io_registry_entry_t, _ properties: UnsafeMutablePointer<Unmanaged<CFMutableDictionary>?>, _ allocator: CFAllocator!, _ options: IOOptionBits) -> kern_return_t ``` |
| To | ``` func IORegistryEntryCreateCFProperties(_ entry: io_registry_entry_t, _ properties: UnsafeMutablePointer<Unmanaged<CFMutableDictionary>?>!, _ allocator: CFAllocator!, _ options: IOOptionBits) -> kern_return_t ``` |

Modified [IORegistryEntryCreateCFProperty(_: io_registry_entry_t, _: CFString!, _: CFAllocator!, _: IOOptionBits) -> Unmanaged<CFTypeRef>!](https://developer.apple.com/documentation/iokit/1514293-ioregistryentrycreatecfproperty)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryCreateCFProperty(_ entry: io_registry_entry_t, _ key: CFString!, _ allocator: CFAllocator!, _ options: IOOptionBits) -> Unmanaged<AnyObject>! ``` |
| To | ``` func IORegistryEntryCreateCFProperty(_ entry: io_registry_entry_t, _ key: CFString!, _ allocator: CFAllocator!, _ options: IOOptionBits) -> Unmanaged<CFTypeRef>! ``` |

Modified [IORegistryEntryCreateIterator(_: io_registry_entry_t, _: UnsafePointer<Int8>!, _: IOOptionBits, _: UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514318-ioregistryentrycreateiterator)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryCreateIterator(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>, _ options: IOOptionBits, _ iterator: UnsafeMutablePointer<io_iterator_t>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryCreateIterator(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>!, _ options: IOOptionBits, _ iterator: UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t ``` |

Modified [IORegistryEntryFromPath(_: mach_port_t, _: UnsafePointer<Int8>!) -> io_registry_entry_t](https://developer.apple.com/documentation/iokit/1514802-ioregistryentryfrompath)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryFromPath(_ masterPort: mach_port_t, _ path: UnsafePointer<Int8>) -> io_registry_entry_t ``` |
| To | ``` func IORegistryEntryFromPath(_ masterPort: mach_port_t, _ path: UnsafePointer<Int8>!) -> io_registry_entry_t ``` |

Modified [IORegistryEntryGetChildEntry(_: io_registry_entry_t, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<io_registry_entry_t>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514496-ioregistryentrygetchildentry)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetChildEntry(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>, _ child: UnsafeMutablePointer<io_registry_entry_t>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetChildEntry(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>!, _ child: UnsafeMutablePointer<io_registry_entry_t>!) -> kern_return_t ``` |

Modified [IORegistryEntryGetChildIterator(_: io_registry_entry_t, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514703-ioregistryentrygetchilditerator)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetChildIterator(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>, _ iterator: UnsafeMutablePointer<io_iterator_t>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetChildIterator(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>!, _ iterator: UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t ``` |

Modified [IORegistryEntryGetLocationInPlane(_: io_registry_entry_t, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<Int8>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514340-ioregistryentrygetlocationinplan)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetLocationInPlane(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>, _ location: UnsafeMutablePointer<Int8>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetLocationInPlane(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>!, _ location: UnsafeMutablePointer<Int8>!) -> kern_return_t ``` |

Modified [IORegistryEntryGetName(_: io_registry_entry_t, _: UnsafeMutablePointer<Int8>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514323-ioregistryentrygetname)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetName(_ entry: io_registry_entry_t, _ name: UnsafeMutablePointer<Int8>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetName(_ entry: io_registry_entry_t, _ name: UnsafeMutablePointer<Int8>!) -> kern_return_t ``` |

Modified [IORegistryEntryGetNameInPlane(_: io_registry_entry_t, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<Int8>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514475-ioregistryentrygetnameinplane)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetNameInPlane(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>, _ name: UnsafeMutablePointer<Int8>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetNameInPlane(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>!, _ name: UnsafeMutablePointer<Int8>!) -> kern_return_t ``` |

Modified [IORegistryEntryGetParentEntry(_: io_registry_entry_t, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<io_registry_entry_t>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514454-ioregistryentrygetparententry)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetParentEntry(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>, _ parent: UnsafeMutablePointer<io_registry_entry_t>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetParentEntry(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>!, _ parent: UnsafeMutablePointer<io_registry_entry_t>!) -> kern_return_t ``` |

Modified [IORegistryEntryGetParentIterator(_: io_registry_entry_t, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514366-ioregistryentrygetparentiterator)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetParentIterator(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>, _ iterator: UnsafeMutablePointer<io_iterator_t>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetParentIterator(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>!, _ iterator: UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t ``` |

Modified [IORegistryEntryGetPath(_: io_registry_entry_t, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<Int8>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514229-ioregistryentrygetpath)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetPath(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>, _ path: UnsafeMutablePointer<Int8>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetPath(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>!, _ path: UnsafeMutablePointer<Int8>!) -> kern_return_t ``` |

Modified [IORegistryEntryGetProperty(_: io_registry_entry_t, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<Int8>!, _: UnsafeMutablePointer<UInt32>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514254-ioregistryentrygetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetProperty(_ entry: io_registry_entry_t, _ propertyName: UnsafePointer<Int8>, _ buffer: UnsafeMutablePointer<Int8>, _ size: UnsafeMutablePointer<UInt32>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetProperty(_ entry: io_registry_entry_t, _ propertyName: UnsafePointer<Int8>!, _ buffer: UnsafeMutablePointer<Int8>!, _ size: UnsafeMutablePointer<UInt32>!) -> kern_return_t ``` |

Modified [IORegistryEntryGetRegistryEntryID(_: io_registry_entry_t, _: UnsafeMutablePointer<UInt64>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514719-ioregistryentrygetregistryentryi)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryGetRegistryEntryID(_ entry: io_registry_entry_t, _ entryID: UnsafeMutablePointer<UInt64>) -> kern_return_t ``` |
| To | ``` func IORegistryEntryGetRegistryEntryID(_ entry: io_registry_entry_t, _ entryID: UnsafeMutablePointer<UInt64>!) -> kern_return_t ``` |

Modified [IORegistryEntryInPlane(_: io_registry_entry_t, _: UnsafePointer<Int8>!) -> boolean_t](https://developer.apple.com/documentation/iokit/1514668-ioregistryentryinplane)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntryInPlane(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>) -> boolean_t ``` |
| To | ``` func IORegistryEntryInPlane(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>!) -> boolean_t ``` |

Modified [IORegistryEntrySearchCFProperty(_: io_registry_entry_t, _: UnsafePointer<Int8>!, _: CFString!, _: CFAllocator!, _: IOOptionBits) -> CFTypeRef!](https://developer.apple.com/documentation/iokit/1514537-ioregistryentrysearchcfproperty)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntrySearchCFProperty(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>, _ key: CFString!, _ allocator: CFAllocator!, _ options: IOOptionBits) -> AnyObject! ``` |
| To | ``` func IORegistryEntrySearchCFProperty(_ entry: io_registry_entry_t, _ plane: UnsafePointer<Int8>!, _ key: CFString!, _ allocator: CFAllocator!, _ options: IOOptionBits) -> CFTypeRef! ``` |

Modified [IORegistryEntrySetCFProperties(_: io_registry_entry_t, _: CFTypeRef!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514414-ioregistryentrysetcfproperties)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntrySetCFProperties(_ entry: io_registry_entry_t, _ properties: AnyObject!) -> kern_return_t ``` |
| To | ``` func IORegistryEntrySetCFProperties(_ entry: io_registry_entry_t, _ properties: CFTypeRef!) -> kern_return_t ``` |

Modified [IORegistryEntrySetCFProperty(_: io_registry_entry_t, _: CFString!, _: CFTypeRef!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514882-ioregistryentrysetcfproperty)

|  | Declaration |
| --- | --- |
| From | ``` func IORegistryEntrySetCFProperty(_ entry: io_registry_entry_t, _ propertyName: CFString!, _ property: AnyObject!) -> kern_return_t ``` |
| To | ``` func IORegistryEntrySetCFProperty(_ entry: io_registry_entry_t, _ propertyName: CFString!, _ property: CFTypeRef!) -> kern_return_t ``` |

Modified [IOServiceAddInterestNotification(_: IONotificationPortRef!, _: io_service_t, _: UnsafePointer<Int8>!, _: IOKit.IOServiceInterestCallback!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<io_object_t>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514866-ioserviceaddinterestnotification)

|  | Declaration |
| --- | --- |
| From | ``` func IOServiceAddInterestNotification(_ notifyPort: IONotificationPortRef, _ service: io_service_t, _ interestType: UnsafePointer<Int8>, _ callback: IOServiceInterestCallback!, _ refCon: UnsafeMutablePointer<Void>, _ notification: UnsafeMutablePointer<io_object_t>) -> kern_return_t ``` |
| To | ``` func IOServiceAddInterestNotification(_ notifyPort: IONotificationPortRef!, _ service: io_service_t, _ interestType: UnsafePointer<Int8>!, _ callback: IOKit.IOServiceInterestCallback!, _ refCon: UnsafeMutableRawPointer!, _ notification: UnsafeMutablePointer<io_object_t>!) -> kern_return_t ``` |

Modified [IOServiceAddMatchingNotification(_: IONotificationPortRef!, _: UnsafePointer<Int8>!, _: CFDictionary!, _: IOKit.IOServiceMatchingCallback!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514362-ioserviceaddmatchingnotification)

|  | Declaration |
| --- | --- |
| From | ``` func IOServiceAddMatchingNotification(_ notifyPort: IONotificationPortRef, _ notificationType: UnsafePointer<Int8>, _ matching: CFDictionary!, _ callback: IOServiceMatchingCallback!, _ refCon: UnsafeMutablePointer<Void>, _ notification: UnsafeMutablePointer<io_iterator_t>) -> kern_return_t ``` |
| To | ``` func IOServiceAddMatchingNotification(_ notifyPort: IONotificationPortRef!, _ notificationType: UnsafePointer<Int8>!, _ matching: CFDictionary!, _ callback: IOKit.IOServiceMatchingCallback!, _ refCon: UnsafeMutableRawPointer!, _ notification: UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t ``` |

Modified [IOServiceAddNotification(_: mach_port_t, _: UnsafePointer<Int8>!, _: CFDictionary!, _: mach_port_t, _: UInt, _: UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514382-ioserviceaddnotification)

|  | Declaration |
| --- | --- |
| From | ``` func IOServiceAddNotification(_ masterPort: mach_port_t, _ notificationType: UnsafePointer<Int8>, _ matching: CFDictionary!, _ wakePort: mach_port_t, _ reference: UInt, _ notification: UnsafeMutablePointer<io_iterator_t>) -> kern_return_t ``` |
| To | ``` func IOServiceAddNotification(_ masterPort: mach_port_t, _ notificationType: UnsafePointer<Int8>!, _ matching: CFDictionary!, _ wakePort: mach_port_t, _ reference: UInt, _ notification: UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t ``` |

Modified [IOServiceGetBusyState(_: io_service_t, _: UnsafeMutablePointer<UInt32>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514607-ioservicegetbusystate)

|  | Declaration |
| --- | --- |
| From | ``` func IOServiceGetBusyState(_ service: io_service_t, _ busyState: UnsafeMutablePointer<UInt32>) -> kern_return_t ``` |
| To | ``` func IOServiceGetBusyState(_ service: io_service_t, _ busyState: UnsafeMutablePointer<UInt32>!) -> kern_return_t ``` |

Modified [IOServiceGetMatchingServices(_: mach_port_t, _: CFDictionary!, _: UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514494-ioservicegetmatchingservices)

|  | Declaration |
| --- | --- |
| From | ``` func IOServiceGetMatchingServices(_ masterPort: mach_port_t, _ matching: CFDictionary!, _ existing: UnsafeMutablePointer<io_iterator_t>) -> kern_return_t ``` |
| To | ``` func IOServiceGetMatchingServices(_ masterPort: mach_port_t, _ matching: CFDictionary!, _ existing: UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t ``` |

Modified [IOServiceInterestCallback](https://developer.apple.com/documentation/iokit/ioserviceinterestcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOServiceInterestCallback = (UnsafeMutablePointer<Void>, io_service_t, UInt32, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias IOServiceInterestCallback = (UnsafeMutableRawPointer?, io_service_t, UInt32, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [IOServiceMatching(_: UnsafePointer<Int8>!) -> CFMutableDictionary!](https://developer.apple.com/documentation/iokit/1514687-ioservicematching)

|  | Declaration |
| --- | --- |
| From | ``` func IOServiceMatching(_ name: UnsafePointer<Int8>) -> CFMutableDictionary! ``` |
| To | ``` func IOServiceMatching(_ name: UnsafePointer<Int8>!) -> CFMutableDictionary! ``` |

Modified [IOServiceMatchingCallback](https://developer.apple.com/documentation/iokit/ioservicematchingcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOServiceMatchingCallback = (UnsafeMutablePointer<Void>, io_iterator_t) -> Void ``` |
| To | ``` typealias IOServiceMatchingCallback = (UnsafeMutableRawPointer?, io_iterator_t) -> Swift.Void ``` |

Modified [IOServiceMatchPropertyTable(_: io_service_t, _: CFDictionary!, _: UnsafeMutablePointer<boolean_t>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514685-ioservicematchpropertytable)

|  | Declaration |
| --- | --- |
| From | ``` func IOServiceMatchPropertyTable(_ service: io_service_t, _ matching: CFDictionary!, _ matches: UnsafeMutablePointer<boolean_t>) -> kern_return_t ``` |
| To | ``` func IOServiceMatchPropertyTable(_ service: io_service_t, _ matching: CFDictionary!, _ matches: UnsafeMutablePointer<boolean_t>!) -> kern_return_t ``` |

Modified [IOServiceNameMatching(_: UnsafePointer<Int8>!) -> CFMutableDictionary!](https://developer.apple.com/documentation/iokit/1514416-ioservicenamematching)

|  | Declaration |
| --- | --- |
| From | ``` func IOServiceNameMatching(_ name: UnsafePointer<Int8>) -> CFMutableDictionary! ``` |
| To | ``` func IOServiceNameMatching(_ name: UnsafePointer<Int8>!) -> CFMutableDictionary! ``` |

Modified [IOServiceOFPathToBSDName(_: mach_port_t, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<Int8>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514661-ioserviceofpathtobsdname)

|  | Declaration |
| --- | --- |
| From | ``` func IOServiceOFPathToBSDName(_ masterPort: mach_port_t, _ openFirmwarePath: UnsafePointer<Int8>, _ bsdName: UnsafeMutablePointer<Int8>) -> kern_return_t ``` |
| To | ``` func IOServiceOFPathToBSDName(_ masterPort: mach_port_t, _ openFirmwarePath: UnsafePointer<Int8>!, _ bsdName: UnsafeMutablePointer<Int8>!) -> kern_return_t ``` |

Modified [IOServiceOpen(_: io_service_t, _: task_port_t, _: UInt32, _: UnsafeMutablePointer<io_connect_t>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514515-ioserviceopen)

|  | Declaration |
| --- | --- |
| From | ``` func IOServiceOpen(_ service: io_service_t, _ owningTask: task_port_t, _ type: UInt32, _ connect: UnsafeMutablePointer<io_connect_t>) -> kern_return_t ``` |
| To | ``` func IOServiceOpen(_ service: io_service_t, _ owningTask: task_port_t, _ type: UInt32, _ connect: UnsafeMutablePointer<io_connect_t>!) -> kern_return_t ``` |

Modified [IOServiceWaitQuiet(_: io_service_t, _: UnsafeMutablePointer<mach_timespec_t>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514573-ioservicewaitquiet)

|  | Declaration |
| --- | --- |
| From | ``` func IOServiceWaitQuiet(_ service: io_service_t, _ waitTime: UnsafeMutablePointer<mach_timespec_t>) -> kern_return_t ``` |
| To | ``` func IOServiceWaitQuiet(_ service: io_service_t, _ waitTime: UnsafeMutablePointer<mach_timespec_t>!) -> kern_return_t ``` |

Modified [IOURLCreateDataAndPropertiesFromResource(_: CFAllocator!, _: CFURL!, _: UnsafeMutablePointer<Unmanaged<CFData>?>!, _: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!, _: CFArray!, _: UnsafeMutablePointer<Int32>!) -> Bool](https://developer.apple.com/documentation/iokit/1514836-iourlcreatedataandpropertiesfrom)

|  | Declaration |
| --- | --- |
| From | ``` func IOURLCreateDataAndPropertiesFromResource(_ alloc: CFAllocator!, _ url: CFURL!, _ resourceData: UnsafeMutablePointer<Unmanaged<CFData>?>, _ properties: UnsafeMutablePointer<Unmanaged<CFDictionary>?>, _ desiredProperties: CFArray!, _ errorCode: UnsafeMutablePointer<Int32>) -> Bool ``` |
| To | ``` func IOURLCreateDataAndPropertiesFromResource(_ alloc: CFAllocator!, _ url: CFURL!, _ resourceData: UnsafeMutablePointer<Unmanaged<CFData>?>!, _ properties: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!, _ desiredProperties: CFArray!, _ errorCode: UnsafeMutablePointer<Int32>!) -> Bool ``` |

Modified [IOURLCreatePropertyFromResource(_: CFAllocator!, _: CFURL!, _: CFString!, _: UnsafeMutablePointer<Int32>!) -> Unmanaged<CFTypeRef>!](https://developer.apple.com/documentation/iokit/1514499-iourlcreatepropertyfromresource)

|  | Declaration |
| --- | --- |
| From | ``` func IOURLCreatePropertyFromResource(_ alloc: CFAllocator!, _ url: CFURL!, _ property: CFString!, _ errorCode: UnsafeMutablePointer<Int32>) -> Unmanaged<AnyObject>! ``` |
| To | ``` func IOURLCreatePropertyFromResource(_ alloc: CFAllocator!, _ url: CFURL!, _ property: CFString!, _ errorCode: UnsafeMutablePointer<Int32>!) -> Unmanaged<CFTypeRef>! ``` |

Modified [IOURLWriteDataAndPropertiesToResource(_: CFURL!, _: CFData!, _: CFDictionary!, _: UnsafeMutablePointer<Int32>!) -> Bool](https://developer.apple.com/documentation/iokit/1514272-iourlwritedataandpropertiestores)

|  | Declaration |
| --- | --- |
| From | ``` func IOURLWriteDataAndPropertiesToResource(_ url: CFURL!, _ dataToWrite: CFData!, _ propertiesToWrite: CFDictionary!, _ errorCode: UnsafeMutablePointer<Int32>) -> Bool ``` |
| To | ``` func IOURLWriteDataAndPropertiesToResource(_ url: CFURL!, _ dataToWrite: CFData!, _ propertiesToWrite: CFDictionary!, _ errorCode: UnsafeMutablePointer<Int32>!) -> Bool ``` |

Modified [OSGetNotificationFromMessage(_: UnsafeMutablePointer<mach_msg_header_t>!, _: UInt32, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<UInt>!, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _: UnsafeMutablePointer<vm_size_t>!) -> kern_return_t](https://developer.apple.com/documentation/iokit/1514263-osgetnotificationfrommessage)

|  | Declaration |
| --- | --- |
| From | ``` func OSGetNotificationFromMessage(_ msg: UnsafeMutablePointer<mach_msg_header_t>, _ index: UInt32, _ type: UnsafeMutablePointer<UInt32>, _ reference: UnsafeMutablePointer<UInt>, _ content: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ size: UnsafeMutablePointer<vm_size_t>) -> kern_return_t ``` |
| To | ``` func OSGetNotificationFromMessage(_ msg: UnsafeMutablePointer<mach_msg_header_t>!, _ index: UInt32, _ type: UnsafeMutablePointer<UInt32>!, _ reference: UnsafeMutablePointer<UInt>!, _ content: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _ size: UnsafeMutablePointer<vm_size_t>!) -> kern_return_t ``` |

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
