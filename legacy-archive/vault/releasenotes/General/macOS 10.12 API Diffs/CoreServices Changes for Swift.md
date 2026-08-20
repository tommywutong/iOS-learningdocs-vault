---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/CoreServices.html
archived_at: '2026-07-18T02:51:10.198781Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# CoreServices Changes for Swift

### CoreServices

Removed [AEArrayData.init(kAEHandleArray: (Handle))](https://developer.apple.com/documentation/coreservices/aearraydata/1448794-init)Removed AEDesc.init(descriptorType: DescType, dataHandle: AEDataStorage)Removed AERemoteProcessResolverContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack!, release: CFAllocatorReleaseCallBack!, copyDescription: CFAllocatorCopyDescriptionCallBack!)Removed CSIdentityClientContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack!, release: CFAllocatorReleaseCallBack!, copyDescription: CFAllocatorCopyDescriptionCallBack!, statusUpdated: CSIdentityStatusUpdatedCallback!)Removed CSIdentityQueryClientContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retainInfo: CFAllocatorRetainCallBack!, releaseInfo: CFAllocatorReleaseCallBack!, copyInfoDescription: CFAllocatorCopyDescriptionCallBack!, receiveEvent: CSIdentityQueryReceiveEventCallback!)Removed FSEventStreamContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack?, release: CFAllocatorReleaseCallBack?, copyDescription: CFAllocatorCopyDescriptionCallBack?)Removed [LSApplicationParameters.init(version: CFIndex, flags: LSLaunchFlags, application: UnsafePointer<FSRef>, asyncLaunchRefCon: UnsafeMutablePointer<Void>, environment: Unmanaged<CFDictionary>!, argv: Unmanaged<CFArray>!, initialEvent: UnsafeMutablePointer<AppleEvent>)](https://developer.apple.com/documentation/coreservices/lsapplicationparameters/1446779-init)Removed [LSHandlerOptions.default](https://developer.apple.com/documentation/coreservices/lshandleroptions/klshandleroptionsdefault)Removed [LSLaunchFlags.HasUntrustedContents](https://developer.apple.com/documentation/coreservices/1645929-anonymous/klslaunchhasuntrustedcontents)Removed [LSLaunchFlags.InhibitBGOnly](https://developer.apple.com/documentation/coreservices/klslaunchinhibitbgonly)Removed [LSLaunchFlags.NoParams](https://developer.apple.com/documentation/coreservices/1645929-anonymous/klslaunchnoparams)Removed LSLaunchFlags.Reserved2Removed LSLaunchFlags.Reserved3Removed LSLaunchFlags.Reserved4Removed LSLaunchFlags.Reserved5Removed [LSLaunchFSRefSpec.init(appRef: UnsafePointer<FSRef>, numDocs: Int, itemRefs: UnsafePointer<FSRef>, passThruParams: UnsafePointer<AEDesc>, launchFlags: LSLaunchFlags, asyncRefCon: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/coreservices/lslaunchfsrefspec/1442457-init)Removed [LSLaunchURLSpec.init(appURL: Unmanaged<CFURL>?, itemURLs: Unmanaged<CFArray>?, passThruParams: UnsafePointer<AEDesc>, launchFlags: LSLaunchFlags, asyncRefCon: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/coreservices/lslaunchurlspec/1446360-init)Removed MDExporterInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, ImporterExportData: ((UnsafeMutablePointer<Void>, CFDictionary!, CFString!, CFString!) -> DarwinBoolean)!)Removed MDImporterBundleWrapperURLInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, ImporterImportBundleWrapperURLData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> DarwinBoolean)!)Removed MDImporterInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, ImporterImportData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFString!) -> DarwinBoolean)!)Removed MDImporterURLInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, ImporterImportURLData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> DarwinBoolean)!)Added [AEArrayData.init(kAEHandleArray: (Handle?))](https://developer.apple.com/documentation/coreservices/aearraydata/1448794-init)Added [AEDesc.init(descriptorType: DescType, dataHandle: AEDataStorage!)](https://developer.apple.com/documentation/coreservices/aedesc/1690318-init)Added [AERemoteProcessResolverContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: CoreFoundation.CFAllocatorRetainCallBack!, release: CoreFoundation.CFAllocatorReleaseCallBack!, copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack!)](https://developer.apple.com/documentation/coreservices/aeremoteprocessresolvercontext/1792092-init)Added [CSIdentityClientContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: CoreFoundation.CFAllocatorRetainCallBack!, release: CoreFoundation.CFAllocatorReleaseCallBack!, copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack!, statusUpdated: CoreServices.CSIdentityStatusUpdatedCallback!)](https://developer.apple.com/documentation/coreservices/csidentityclientcontext/1792093-init)Added [CSIdentityQueryClientContext.init(version: CFIndex, info: UnsafeMutableRawPointer!, retainInfo: CoreFoundation.CFAllocatorRetainCallBack!, releaseInfo: CoreFoundation.CFAllocatorReleaseCallBack!, copyInfoDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack!, receiveEvent: CoreServices.CSIdentityQueryReceiveEventCallback!)](https://developer.apple.com/documentation/coreservices/csidentityqueryclientcontext/1792095-init)Added [FSEventStreamContext.init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: CoreFoundation.CFAllocatorRetainCallBack?, release: CoreFoundation.CFAllocatorReleaseCallBack?, copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack?)](https://developer.apple.com/documentation/coreservices/fseventstreamcontext/1792099-init)Added [LSApplicationParameters.init(version: CFIndex, flags: LSLaunchFlags, application: UnsafePointer<FSRef>!, asyncLaunchRefCon: UnsafeMutableRawPointer!, environment: Unmanaged<CFDictionary>!, argv: Unmanaged<CFArray>!, initialEvent: UnsafeMutablePointer<AppleEvent>!)](https://developer.apple.com/documentation/coreservices/lsapplicationparameters/1446779-init)Added [LSLaunchFSRefSpec.init(appRef: UnsafePointer<FSRef>!, numDocs: Int, itemRefs: UnsafePointer<FSRef>!, passThruParams: UnsafePointer<AEDesc>!, launchFlags: LSLaunchFlags, asyncRefCon: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/coreservices/lslaunchfsrefspec/1442457-init)Added [LSLaunchURLSpec.init(appURL: Unmanaged<CFURL>?, itemURLs: Unmanaged<CFArray>?, passThruParams: UnsafePointer<AEDesc>?, launchFlags: LSLaunchFlags, asyncRefCon: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/coreservices/lslaunchurlspec/1446360-init)Added [MDExporterInterfaceStruct.init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ( (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef: ( (UnsafeMutableRawPointer?) -> ULONG)!, Release: ( (UnsafeMutableRawPointer?) -> ULONG)!, ImporterExportData: ( (UnsafeMutableRawPointer?, CFDictionary?, CFString?, CFString?) -> DarwinBoolean)!)](https://developer.apple.com/documentation/coreservices/mdexporterinterfacestruct/1792091-init)Added [MDImporterBundleWrapperURLInterfaceStruct.init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ( (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef: ( (UnsafeMutableRawPointer?) -> ULONG)!, Release: ( (UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportBundleWrapperURLData: ( (UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!)](https://developer.apple.com/documentation/coreservices/mdimporterbundlewrapperurlinterfacestruct/1792098-init)Added [MDImporterInterfaceStruct.init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ( (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef: ( (UnsafeMutableRawPointer?) -> ULONG)!, Release: ( (UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportData: ( (UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFString?) -> DarwinBoolean)!)](https://developer.apple.com/documentation/coreservices/mdimporterinterfacestruct/1792094-init)Added [MDImporterURLInterfaceStruct.init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ( (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef: ( (UnsafeMutableRawPointer?) -> ULONG)!, Release: ( (UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportURLData: ( (UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!)](https://developer.apple.com/documentation/coreservices/mdimporterurlinterfacestruct/1792096-init)Added [kLSGarbageCollectionUnsupportedErr](https://developer.apple.com/documentation/coreservices/1469236-anonymous/klsgarbagecollectionunsupportederr)Added [kLSLaunchHasUntrustedContents](https://developer.apple.com/documentation/coreservices/klslaunchhasuntrustedcontents)Added [kLSLaunchInhibitBGOnly](https://developer.apple.com/documentation/coreservices/klslaunchinhibitbgonly)Added [kLSLaunchNoParams](https://developer.apple.com/documentation/coreservices/1645929-anonymous/klslaunchnoparams)Added [kUTTypeLivePhoto](https://developer.apple.com/documentation/coreservices/kuttypelivephoto)Modified [AEArrayData [struct]](https://developer.apple.com/documentation/coreservices/aearraydata)

|  | Declaration |
| --- | --- |
| From | ``` struct AEArrayData {     var kAEDataArray: (Int16)     var kAEPackedArray: (Int8)     var kAEHandleArray: (Handle)     var kAEDescArray: (AEDesc)     var kAEKeyDescArray: (AEKeyDesc)     init(kAEDataArray kAEDataArray: (Int16))     init(kAEPackedArray kAEPackedArray: (Int8))     init(kAEHandleArray kAEHandleArray: (Handle))     init(kAEDescArray kAEDescArray: (AEDesc))     init(kAEKeyDescArray kAEKeyDescArray: (AEKeyDesc))     init() } ``` |
| To | ``` struct AEArrayData {     var kAEDataArray: (Int16)     var kAEPackedArray: (Int8)     var kAEHandleArray: (Handle?)     var kAEDescArray: (AEDesc)     var kAEKeyDescArray: (AEKeyDesc)     init(kAEDataArray kAEDataArray: (Int16))     init(kAEPackedArray kAEPackedArray: (Int8))     init(kAEHandleArray kAEHandleArray: (Handle?))     init(kAEDescArray kAEDescArray: (AEDesc))     init(kAEKeyDescArray kAEKeyDescArray: (AEKeyDesc))     init() } ``` |

Modified [AEArrayData.kAEHandleArray](https://developer.apple.com/documentation/coreservices/1443170-aearraydata/1444461-kaehandlearray)

|  | Declaration |
| --- | --- |
| From | ``` var kAEHandleArray: (Handle) ``` |
| To | ``` var kAEHandleArray: (Handle?) ``` |

Modified [AEDesc [struct]](https://developer.apple.com/documentation/coreservices/aedesc)

|  | Declaration |
| --- | --- |
| From | ``` struct AEDesc {     var descriptorType: DescType     var dataHandle: AEDataStorage     init()     init(descriptorType descriptorType: DescType, dataHandle dataHandle: AEDataStorage) } ``` |
| To | ``` struct AEDesc {     var descriptorType: DescType     var dataHandle: AEDataStorage!     init()     init(descriptorType descriptorType: DescType, dataHandle dataHandle: AEDataStorage!) } ``` |

Modified [AEDesc.dataHandle](https://developer.apple.com/documentation/coreservices/aedesc/1444550-datahandle)

|  | Declaration |
| --- | --- |
| From | ``` var dataHandle: AEDataStorage ``` |
| To | ``` var dataHandle: AEDataStorage! ``` |

Modified [AERemoteProcessResolverContext [struct]](https://developer.apple.com/documentation/coreservices/aeremoteprocessresolvercontext)

|  | Declaration |
| --- | --- |
| From | ``` struct AERemoteProcessResolverContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack!     var release: CFAllocatorReleaseCallBack!     var copyDescription: CFAllocatorCopyDescriptionCallBack!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack!, release release: CFAllocatorReleaseCallBack!, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack!) } ``` |
| To | ``` struct AERemoteProcessResolverContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: CoreFoundation.CFAllocatorRetainCallBack!     var release: CoreFoundation.CFAllocatorReleaseCallBack!     var copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: CoreFoundation.CFAllocatorRetainCallBack!, release release: CoreFoundation.CFAllocatorReleaseCallBack!, copyDescription copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack!) } ``` |

Modified [AERemoteProcessResolverContext.copyDescription](https://developer.apple.com/documentation/coreservices/aeremoteprocessresolvercontext/1442771-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFAllocatorCopyDescriptionCallBack! ``` |
| To | ``` var copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack! ``` |

Modified [AERemoteProcessResolverContext.info](https://developer.apple.com/documentation/coreservices/aeremoteprocessresolvercontext/1449518-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer! ``` |

Modified [AERemoteProcessResolverContext.release](https://developer.apple.com/documentation/coreservices/aeremoteprocessresolvercontext/1444738-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFAllocatorReleaseCallBack! ``` |
| To | ``` var release: CoreFoundation.CFAllocatorReleaseCallBack! ``` |

Modified [AERemoteProcessResolverContext.retain](https://developer.apple.com/documentation/coreservices/aeremoteprocessresolvercontext/1450097-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFAllocatorRetainCallBack! ``` |
| To | ``` var retain: CoreFoundation.CFAllocatorRetainCallBack! ``` |

Modified [CSIdentityClientContext [struct]](https://developer.apple.com/documentation/coreservices/csidentityclientcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CSIdentityClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack!     var release: CFAllocatorReleaseCallBack!     var copyDescription: CFAllocatorCopyDescriptionCallBack!     var statusUpdated: CSIdentityStatusUpdatedCallback!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack!, release release: CFAllocatorReleaseCallBack!, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack!, statusUpdated statusUpdated: CSIdentityStatusUpdatedCallback!) } ``` |
| To | ``` struct CSIdentityClientContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retain: CoreFoundation.CFAllocatorRetainCallBack!     var release: CoreFoundation.CFAllocatorReleaseCallBack!     var copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack!     var statusUpdated: CoreServices.CSIdentityStatusUpdatedCallback!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retain retain: CoreFoundation.CFAllocatorRetainCallBack!, release release: CoreFoundation.CFAllocatorReleaseCallBack!, copyDescription copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack!, statusUpdated statusUpdated: CoreServices.CSIdentityStatusUpdatedCallback!) } ``` |

Modified [CSIdentityClientContext.copyDescription](https://developer.apple.com/documentation/coreservices/csidentityclientcontext/1445249-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFAllocatorCopyDescriptionCallBack! ``` |
| To | ``` var copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack! ``` |

Modified [CSIdentityClientContext.info](https://developer.apple.com/documentation/coreservices/csidentityclientcontext/1443727-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer! ``` |

Modified [CSIdentityClientContext.release](https://developer.apple.com/documentation/coreservices/csidentityclientcontext/1448741-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFAllocatorReleaseCallBack! ``` |
| To | ``` var release: CoreFoundation.CFAllocatorReleaseCallBack! ``` |

Modified [CSIdentityClientContext.retain](https://developer.apple.com/documentation/coreservices/csidentityclientcontext/1444414-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFAllocatorRetainCallBack! ``` |
| To | ``` var retain: CoreFoundation.CFAllocatorRetainCallBack! ``` |

Modified [CSIdentityClientContext.statusUpdated](https://developer.apple.com/documentation/coreservices/csidentityclientcontext/1447852-statusupdated)

|  | Declaration |
| --- | --- |
| From | ``` var statusUpdated: CSIdentityStatusUpdatedCallback! ``` |
| To | ``` var statusUpdated: CoreServices.CSIdentityStatusUpdatedCallback! ``` |

Modified [CSIdentityQueryClientContext [struct]](https://developer.apple.com/documentation/coreservices/csidentityqueryclientcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CSIdentityQueryClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retainInfo: CFAllocatorRetainCallBack!     var releaseInfo: CFAllocatorReleaseCallBack!     var copyInfoDescription: CFAllocatorCopyDescriptionCallBack!     var receiveEvent: CSIdentityQueryReceiveEventCallback!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retainInfo retainInfo: CFAllocatorRetainCallBack!, releaseInfo releaseInfo: CFAllocatorReleaseCallBack!, copyInfoDescription copyInfoDescription: CFAllocatorCopyDescriptionCallBack!, receiveEvent receiveEvent: CSIdentityQueryReceiveEventCallback!) } ``` |
| To | ``` struct CSIdentityQueryClientContext {     var version: CFIndex     var info: UnsafeMutableRawPointer!     var retainInfo: CoreFoundation.CFAllocatorRetainCallBack!     var releaseInfo: CoreFoundation.CFAllocatorReleaseCallBack!     var copyInfoDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack!     var receiveEvent: CoreServices.CSIdentityQueryReceiveEventCallback!     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer!, retainInfo retainInfo: CoreFoundation.CFAllocatorRetainCallBack!, releaseInfo releaseInfo: CoreFoundation.CFAllocatorReleaseCallBack!, copyInfoDescription copyInfoDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack!, receiveEvent receiveEvent: CoreServices.CSIdentityQueryReceiveEventCallback!) } ``` |

Modified [CSIdentityQueryClientContext.copyInfoDescription](https://developer.apple.com/documentation/coreservices/csidentityqueryclientcontext/1428999-copyinfodescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyInfoDescription: CFAllocatorCopyDescriptionCallBack! ``` |
| To | ``` var copyInfoDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack! ``` |

Modified [CSIdentityQueryClientContext.info](https://developer.apple.com/documentation/coreservices/csidentityqueryclientcontext/1429018-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer! ``` |

Modified [CSIdentityQueryClientContext.receiveEvent](https://developer.apple.com/documentation/coreservices/csidentityqueryclientcontext/1429030-receiveevent)

|  | Declaration |
| --- | --- |
| From | ``` var receiveEvent: CSIdentityQueryReceiveEventCallback! ``` |
| To | ``` var receiveEvent: CoreServices.CSIdentityQueryReceiveEventCallback! ``` |

Modified [CSIdentityQueryClientContext.releaseInfo](https://developer.apple.com/documentation/coreservices/csidentityqueryclientcontext/1429034-releaseinfo)

|  | Declaration |
| --- | --- |
| From | ``` var releaseInfo: CFAllocatorReleaseCallBack! ``` |
| To | ``` var releaseInfo: CoreFoundation.CFAllocatorReleaseCallBack! ``` |

Modified [CSIdentityQueryClientContext.retainInfo](https://developer.apple.com/documentation/coreservices/csidentityqueryclientcontext/1429016-retaininfo)

|  | Declaration |
| --- | --- |
| From | ``` var retainInfo: CFAllocatorRetainCallBack! ``` |
| To | ``` var retainInfo: CoreFoundation.CFAllocatorRetainCallBack! ``` |

Modified [FSEventStreamContext [struct]](https://developer.apple.com/documentation/coreservices/fseventstreamcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct FSEventStreamContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack?     var release: CFAllocatorReleaseCallBack?     var copyDescription: CFAllocatorCopyDescriptionCallBack?     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack?, release release: CFAllocatorReleaseCallBack?, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack?) } ``` |
| To | ``` struct FSEventStreamContext {     var version: CFIndex     var info: UnsafeMutableRawPointer?     var retain: CoreFoundation.CFAllocatorRetainCallBack?     var release: CoreFoundation.CFAllocatorReleaseCallBack?     var copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack?     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: CoreFoundation.CFAllocatorRetainCallBack?, release release: CoreFoundation.CFAllocatorReleaseCallBack?, copyDescription copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack?) } ``` |

Modified [FSEventStreamContext.copyDescription](https://developer.apple.com/documentation/coreservices/fseventstreamcontext/1445178-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFAllocatorCopyDescriptionCallBack? ``` |
| To | ``` var copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack? ``` |

Modified [FSEventStreamContext.info](https://developer.apple.com/documentation/coreservices/fseventstreamcontext/1446169-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer? ``` |

Modified [FSEventStreamContext.release](https://developer.apple.com/documentation/coreservices/fseventstreamcontext/1450554-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFAllocatorReleaseCallBack? ``` |
| To | ``` var release: CoreFoundation.CFAllocatorReleaseCallBack? ``` |

Modified [FSEventStreamContext.retain](https://developer.apple.com/documentation/coreservices/fseventstreamcontext/1450539-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFAllocatorRetainCallBack? ``` |
| To | ``` var retain: CoreFoundation.CFAllocatorRetainCallBack? ``` |

Modified [LSAcceptanceFlags [struct]](https://developer.apple.com/documentation/coreservices/lsacceptanceflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct LSAcceptanceFlags : OptionSetType {     init(rawValue rawValue: OptionBits)     static var AcceptDefault: LSAcceptanceFlags { get }     static var AcceptAllowLoginUI: LSAcceptanceFlags { get } } ``` | OptionSetType |
| To | ``` struct LSAcceptanceFlags : OptionSet {     init(rawValue rawValue: OptionBits)     static var acceptDefault: LSAcceptanceFlags { get }     static var acceptAllowLoginUI: LSAcceptanceFlags { get }     func intersect(_ other: LSAcceptanceFlags) -> LSAcceptanceFlags     func exclusiveOr(_ other: LSAcceptanceFlags) -> LSAcceptanceFlags     mutating func unionInPlace(_ other: LSAcceptanceFlags)     mutating func intersectInPlace(_ other: LSAcceptanceFlags)     mutating func exclusiveOrInPlace(_ other: LSAcceptanceFlags)     func isSubsetOf(_ other: LSAcceptanceFlags) -> Bool     func isDisjointWith(_ other: LSAcceptanceFlags) -> Bool     func isSupersetOf(_ other: LSAcceptanceFlags) -> Bool     mutating func subtractInPlace(_ other: LSAcceptanceFlags)     func isStrictSupersetOf(_ other: LSAcceptanceFlags) -> Bool     func isStrictSubsetOf(_ other: LSAcceptanceFlags) -> Bool } extension LSAcceptanceFlags {     func union(_ other: LSAcceptanceFlags) -> LSAcceptanceFlags     func intersection(_ other: LSAcceptanceFlags) -> LSAcceptanceFlags     func symmetricDifference(_ other: LSAcceptanceFlags) -> LSAcceptanceFlags } extension LSAcceptanceFlags {     func contains(_ member: LSAcceptanceFlags) -> Bool     mutating func insert(_ newMember: LSAcceptanceFlags) -> (inserted: Bool, memberAfterInsert: LSAcceptanceFlags)     mutating func remove(_ member: LSAcceptanceFlags) -> LSAcceptanceFlags?     mutating func update(with newMember: LSAcceptanceFlags) -> LSAcceptanceFlags? } extension LSAcceptanceFlags {     convenience init()     mutating func formUnion(_ other: LSAcceptanceFlags)     mutating func formIntersection(_ other: LSAcceptanceFlags)     mutating func formSymmetricDifference(_ other: LSAcceptanceFlags) } extension LSAcceptanceFlags {     convenience init<S : Sequence where S.Iterator.Element == LSAcceptanceFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: LSAcceptanceFlags...)     mutating func subtract(_ other: LSAcceptanceFlags)     func isSubset(of other: LSAcceptanceFlags) -> Bool     func isSuperset(of other: LSAcceptanceFlags) -> Bool     func isDisjoint(with other: LSAcceptanceFlags) -> Bool     func subtracting(_ other: LSAcceptanceFlags) -> LSAcceptanceFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: LSAcceptanceFlags) -> Bool     func isStrictSubset(of other: LSAcceptanceFlags) -> Bool } ``` | OptionSet |

Modified [LSAcceptanceFlags.acceptAllowLoginUI](https://developer.apple.com/documentation/coreservices/lsacceptanceflags/klsacceptallowloginui)

|  | Declaration |
| --- | --- |
| From | ``` static var AcceptAllowLoginUI: LSAcceptanceFlags { get } ``` |
| To | ``` static var acceptAllowLoginUI: LSAcceptanceFlags { get } ``` |

Modified [LSAcceptanceFlags.acceptDefault](https://developer.apple.com/documentation/coreservices/lsacceptanceflags/klsacceptdefault)

|  | Declaration |
| --- | --- |
| From | ``` static var AcceptDefault: LSAcceptanceFlags { get } ``` |
| To | ``` static var acceptDefault: LSAcceptanceFlags { get } ``` |

Modified [LSApplicationParameters [struct]](https://developer.apple.com/documentation/coreservices/lsapplicationparameters)

|  | Declaration |
| --- | --- |
| From | ``` struct LSApplicationParameters {     var version: CFIndex     var flags: LSLaunchFlags     var application: UnsafePointer<FSRef>     var asyncLaunchRefCon: UnsafeMutablePointer<Void>     var environment: Unmanaged<CFDictionary>!     var argv: Unmanaged<CFArray>!     var initialEvent: UnsafeMutablePointer<AppleEvent>     init()     init(version version: CFIndex, flags flags: LSLaunchFlags, application application: UnsafePointer<FSRef>, asyncLaunchRefCon asyncLaunchRefCon: UnsafeMutablePointer<Void>, environment environment: Unmanaged<CFDictionary>!, argv argv: Unmanaged<CFArray>!, initialEvent initialEvent: UnsafeMutablePointer<AppleEvent>) } ``` |
| To | ``` struct LSApplicationParameters {     var version: CFIndex     var flags: LSLaunchFlags     var application: UnsafePointer<FSRef>!     var asyncLaunchRefCon: UnsafeMutableRawPointer!     var environment: Unmanaged<CFDictionary>!     var argv: Unmanaged<CFArray>!     var initialEvent: UnsafeMutablePointer<AppleEvent>!     init()     init(version version: CFIndex, flags flags: LSLaunchFlags, application application: UnsafePointer<FSRef>!, asyncLaunchRefCon asyncLaunchRefCon: UnsafeMutableRawPointer!, environment environment: Unmanaged<CFDictionary>!, argv argv: Unmanaged<CFArray>!, initialEvent initialEvent: UnsafeMutablePointer<AppleEvent>!) } ``` |

Modified [LSApplicationParameters.application](https://developer.apple.com/documentation/coreservices/lsapplicationparameters/1447460-application)

|  | Declaration |
| --- | --- |
| From | ``` var application: UnsafePointer<FSRef> ``` |
| To | ``` var application: UnsafePointer<FSRef>! ``` |

Modified [LSApplicationParameters.asyncLaunchRefCon](https://developer.apple.com/documentation/coreservices/lsapplicationparameters/1444464-asynclaunchrefcon)

|  | Declaration |
| --- | --- |
| From | ``` var asyncLaunchRefCon: UnsafeMutablePointer<Void> ``` |
| To | ``` var asyncLaunchRefCon: UnsafeMutableRawPointer! ``` |

Modified [LSApplicationParameters.initialEvent](https://developer.apple.com/documentation/coreservices/lsapplicationparameters/1446633-initialevent)

|  | Declaration |
| --- | --- |
| From | ``` var initialEvent: UnsafeMutablePointer<AppleEvent> ``` |
| To | ``` var initialEvent: UnsafeMutablePointer<AppleEvent>! ``` |

Modified [LSHandlerOptions [struct]](https://developer.apple.com/documentation/coreservices/lshandleroptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct LSHandlerOptions : OptionSetType {     init(rawValue rawValue: OptionBits)     static var Default: LSHandlerOptions { get }     static var IgnoreCreator: LSHandlerOptions { get } } ``` | OptionSetType |
| To | ``` struct LSHandlerOptions : OptionSet {     init(rawValue rawValue: OptionBits)     static var `default`: LSHandlerOptions { get }     static var ignoreCreator: LSHandlerOptions { get }     func intersect(_ other: LSHandlerOptions) -> LSHandlerOptions     func exclusiveOr(_ other: LSHandlerOptions) -> LSHandlerOptions     mutating func unionInPlace(_ other: LSHandlerOptions)     mutating func intersectInPlace(_ other: LSHandlerOptions)     mutating func exclusiveOrInPlace(_ other: LSHandlerOptions)     func isSubsetOf(_ other: LSHandlerOptions) -> Bool     func isDisjointWith(_ other: LSHandlerOptions) -> Bool     func isSupersetOf(_ other: LSHandlerOptions) -> Bool     mutating func subtractInPlace(_ other: LSHandlerOptions)     func isStrictSupersetOf(_ other: LSHandlerOptions) -> Bool     func isStrictSubsetOf(_ other: LSHandlerOptions) -> Bool } extension LSHandlerOptions {     func union(_ other: LSHandlerOptions) -> LSHandlerOptions     func intersection(_ other: LSHandlerOptions) -> LSHandlerOptions     func symmetricDifference(_ other: LSHandlerOptions) -> LSHandlerOptions } extension LSHandlerOptions {     func contains(_ member: LSHandlerOptions) -> Bool     mutating func insert(_ newMember: LSHandlerOptions) -> (inserted: Bool, memberAfterInsert: LSHandlerOptions)     mutating func remove(_ member: LSHandlerOptions) -> LSHandlerOptions?     mutating func update(with newMember: LSHandlerOptions) -> LSHandlerOptions? } extension LSHandlerOptions {     convenience init()     mutating func formUnion(_ other: LSHandlerOptions)     mutating func formIntersection(_ other: LSHandlerOptions)     mutating func formSymmetricDifference(_ other: LSHandlerOptions) } extension LSHandlerOptions {     convenience init<S : Sequence where S.Iterator.Element == LSHandlerOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: LSHandlerOptions...)     mutating func subtract(_ other: LSHandlerOptions)     func isSubset(of other: LSHandlerOptions) -> Bool     func isSuperset(of other: LSHandlerOptions) -> Bool     func isDisjoint(with other: LSHandlerOptions) -> Bool     func subtracting(_ other: LSHandlerOptions) -> LSHandlerOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: LSHandlerOptions) -> Bool     func isStrictSubset(of other: LSHandlerOptions) -> Bool } ``` | OptionSet |

Modified [LSHandlerOptions.ignoreCreator](https://developer.apple.com/documentation/coreservices/lshandleroptions/klshandleroptionsignorecreator)

|  | Declaration |
| --- | --- |
| From | ``` static var IgnoreCreator: LSHandlerOptions { get } ``` |
| To | ``` static var ignoreCreator: LSHandlerOptions { get } ``` |

Modified [LSItemInfoFlags [struct]](https://developer.apple.com/documentation/coreservices/lsiteminfoflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct LSItemInfoFlags : OptionSetType {     init(rawValue rawValue: OptionBits)     static var IsPlainFile: LSItemInfoFlags { get }     static var IsPackage: LSItemInfoFlags { get }     static var IsApplication: LSItemInfoFlags { get }     static var IsContainer: LSItemInfoFlags { get }     static var IsAliasFile: LSItemInfoFlags { get }     static var IsSymlink: LSItemInfoFlags { get }     static var IsInvisible: LSItemInfoFlags { get }     static var IsNativeApp: LSItemInfoFlags { get }     static var IsClassicApp: LSItemInfoFlags { get }     static var AppPrefersNative: LSItemInfoFlags { get }     static var AppPrefersClassic: LSItemInfoFlags { get }     static var AppIsScriptable: LSItemInfoFlags { get }     static var IsVolume: LSItemInfoFlags { get }     static var ExtensionIsHidden: LSItemInfoFlags { get } } ``` | OptionSetType |
| To | ``` struct LSItemInfoFlags : OptionSet {     init(rawValue rawValue: OptionBits)     static var isPlainFile: LSItemInfoFlags { get }     static var isPackage: LSItemInfoFlags { get }     static var isApplication: LSItemInfoFlags { get }     static var isContainer: LSItemInfoFlags { get }     static var isAliasFile: LSItemInfoFlags { get }     static var isSymlink: LSItemInfoFlags { get }     static var isInvisible: LSItemInfoFlags { get }     static var isNativeApp: LSItemInfoFlags { get }     static var isClassicApp: LSItemInfoFlags { get }     static var appPrefersNative: LSItemInfoFlags { get }     static var appPrefersClassic: LSItemInfoFlags { get }     static var appIsScriptable: LSItemInfoFlags { get }     static var isVolume: LSItemInfoFlags { get }     static var extensionIsHidden: LSItemInfoFlags { get }     func intersect(_ other: LSItemInfoFlags) -> LSItemInfoFlags     func exclusiveOr(_ other: LSItemInfoFlags) -> LSItemInfoFlags     mutating func unionInPlace(_ other: LSItemInfoFlags)     mutating func intersectInPlace(_ other: LSItemInfoFlags)     mutating func exclusiveOrInPlace(_ other: LSItemInfoFlags)     func isSubsetOf(_ other: LSItemInfoFlags) -> Bool     func isDisjointWith(_ other: LSItemInfoFlags) -> Bool     func isSupersetOf(_ other: LSItemInfoFlags) -> Bool     mutating func subtractInPlace(_ other: LSItemInfoFlags)     func isStrictSupersetOf(_ other: LSItemInfoFlags) -> Bool     func isStrictSubsetOf(_ other: LSItemInfoFlags) -> Bool } extension LSItemInfoFlags {     func union(_ other: LSItemInfoFlags) -> LSItemInfoFlags     func intersection(_ other: LSItemInfoFlags) -> LSItemInfoFlags     func symmetricDifference(_ other: LSItemInfoFlags) -> LSItemInfoFlags } extension LSItemInfoFlags {     func contains(_ member: LSItemInfoFlags) -> Bool     mutating func insert(_ newMember: LSItemInfoFlags) -> (inserted: Bool, memberAfterInsert: LSItemInfoFlags)     mutating func remove(_ member: LSItemInfoFlags) -> LSItemInfoFlags?     mutating func update(with newMember: LSItemInfoFlags) -> LSItemInfoFlags? } extension LSItemInfoFlags {     convenience init()     mutating func formUnion(_ other: LSItemInfoFlags)     mutating func formIntersection(_ other: LSItemInfoFlags)     mutating func formSymmetricDifference(_ other: LSItemInfoFlags) } extension LSItemInfoFlags {     convenience init<S : Sequence where S.Iterator.Element == LSItemInfoFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: LSItemInfoFlags...)     mutating func subtract(_ other: LSItemInfoFlags)     func isSubset(of other: LSItemInfoFlags) -> Bool     func isSuperset(of other: LSItemInfoFlags) -> Bool     func isDisjoint(with other: LSItemInfoFlags) -> Bool     func subtracting(_ other: LSItemInfoFlags) -> LSItemInfoFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: LSItemInfoFlags) -> Bool     func isStrictSubset(of other: LSItemInfoFlags) -> Bool } ``` | OptionSet |

Modified [LSItemInfoFlags.appIsScriptable](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1448463-appisscriptable)

|  | Declaration |
| --- | --- |
| From | ``` static var AppIsScriptable: LSItemInfoFlags { get } ``` |
| To | ``` static var appIsScriptable: LSItemInfoFlags { get } ``` |

Modified [LSItemInfoFlags.appPrefersClassic](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoappprefersclassic)

|  | Declaration |
| --- | --- |
| From | ``` static var AppPrefersClassic: LSItemInfoFlags { get } ``` |
| To | ``` static var appPrefersClassic: LSItemInfoFlags { get } ``` |

Modified [LSItemInfoFlags.appPrefersNative](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoappprefersnative)

|  | Declaration |
| --- | --- |
| From | ``` static var AppPrefersNative: LSItemInfoFlags { get } ``` |
| To | ``` static var appPrefersNative: LSItemInfoFlags { get } ``` |

Modified [LSItemInfoFlags.extensionIsHidden](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoextensionishidden)

|  | Declaration |
| --- | --- |
| From | ``` static var ExtensionIsHidden: LSItemInfoFlags { get } ``` |
| To | ``` static var extensionIsHidden: LSItemInfoFlags { get } ``` |

Modified [LSItemInfoFlags.isAliasFile](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoisaliasfile)

|  | Declaration |
| --- | --- |
| From | ``` static var IsAliasFile: LSItemInfoFlags { get } ``` |
| To | ``` static var isAliasFile: LSItemInfoFlags { get } ``` |

Modified [LSItemInfoFlags.isApplication](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoisapplication)

|  | Declaration |
| --- | --- |
| From | ``` static var IsApplication: LSItemInfoFlags { get } ``` |
| To | ``` static var isApplication: LSItemInfoFlags { get } ``` |

Modified [LSItemInfoFlags.isClassicApp](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoisclassicapp)

|  | Declaration |
| --- | --- |
| From | ``` static var IsClassicApp: LSItemInfoFlags { get } ``` |
| To | ``` static var isClassicApp: LSItemInfoFlags { get } ``` |

Modified [LSItemInfoFlags.isContainer](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1443420-iscontainer)

|  | Declaration |
| --- | --- |
| From | ``` static var IsContainer: LSItemInfoFlags { get } ``` |
| To | ``` static var isContainer: LSItemInfoFlags { get } ``` |

Modified [LSItemInfoFlags.isInvisible](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoisinvisible)

|  | Declaration |
| --- | --- |
| From | ``` static var IsInvisible: LSItemInfoFlags { get } ``` |
| To | ``` static var isInvisible: LSItemInfoFlags { get } ``` |

Modified [LSItemInfoFlags.isNativeApp](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoisnativeapp)

|  | Declaration |
| --- | --- |
| From | ``` static var IsNativeApp: LSItemInfoFlags { get } ``` |
| To | ``` static var isNativeApp: LSItemInfoFlags { get } ``` |

Modified [LSItemInfoFlags.isPackage](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1449324-ispackage)

|  | Declaration |
| --- | --- |
| From | ``` static var IsPackage: LSItemInfoFlags { get } ``` |
| To | ``` static var isPackage: LSItemInfoFlags { get } ``` |

Modified [LSItemInfoFlags.isPlainFile](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoisplainfile)

|  | Declaration |
| --- | --- |
| From | ``` static var IsPlainFile: LSItemInfoFlags { get } ``` |
| To | ``` static var isPlainFile: LSItemInfoFlags { get } ``` |

Modified [LSItemInfoFlags.isSymlink](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1446223-issymlink)

|  | Declaration |
| --- | --- |
| From | ``` static var IsSymlink: LSItemInfoFlags { get } ``` |
| To | ``` static var isSymlink: LSItemInfoFlags { get } ``` |

Modified [LSItemInfoFlags.isVolume](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1448330-isvolume)

|  | Declaration |
| --- | --- |
| From | ``` static var IsVolume: LSItemInfoFlags { get } ``` |
| To | ``` static var isVolume: LSItemInfoFlags { get } ``` |

Modified [LSLaunchFlags [struct]](https://developer.apple.com/documentation/coreservices/lslaunchflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct LSLaunchFlags : OptionSetType {     init(rawValue rawValue: OptionBits)     static var Defaults: LSLaunchFlags { get }     static var AndPrint: LSLaunchFlags { get }     static var Reserved2: LSLaunchFlags { get }     static var Reserved3: LSLaunchFlags { get }     static var Reserved4: LSLaunchFlags { get }     static var Reserved5: LSLaunchFlags { get }     static var AndDisplayErrors: LSLaunchFlags { get }     static var InhibitBGOnly: LSLaunchFlags { get }     static var DontAddToRecents: LSLaunchFlags { get }     static var DontSwitch: LSLaunchFlags { get }     static var NoParams: LSLaunchFlags { get }     static var Async: LSLaunchFlags { get }     static var NewInstance: LSLaunchFlags { get }     static var AndHide: LSLaunchFlags { get }     static var AndHideOthers: LSLaunchFlags { get }     static var HasUntrustedContents: LSLaunchFlags { get } } ``` | OptionSetType |
| To | ``` struct LSLaunchFlags : OptionSet {     init(rawValue rawValue: OptionBits)     static var defaults: LSLaunchFlags { get }     static var andPrint: LSLaunchFlags { get }     static var andDisplayErrors: LSLaunchFlags { get }     static var dontAddToRecents: LSLaunchFlags { get }     static var dontSwitch: LSLaunchFlags { get }     static var async: LSLaunchFlags { get }     static var newInstance: LSLaunchFlags { get }     static var andHide: LSLaunchFlags { get }     static var andHideOthers: LSLaunchFlags { get }     func intersect(_ other: LSLaunchFlags) -> LSLaunchFlags     func exclusiveOr(_ other: LSLaunchFlags) -> LSLaunchFlags     mutating func unionInPlace(_ other: LSLaunchFlags)     mutating func intersectInPlace(_ other: LSLaunchFlags)     mutating func exclusiveOrInPlace(_ other: LSLaunchFlags)     func isSubsetOf(_ other: LSLaunchFlags) -> Bool     func isDisjointWith(_ other: LSLaunchFlags) -> Bool     func isSupersetOf(_ other: LSLaunchFlags) -> Bool     mutating func subtractInPlace(_ other: LSLaunchFlags)     func isStrictSupersetOf(_ other: LSLaunchFlags) -> Bool     func isStrictSubsetOf(_ other: LSLaunchFlags) -> Bool } extension LSLaunchFlags {     func union(_ other: LSLaunchFlags) -> LSLaunchFlags     func intersection(_ other: LSLaunchFlags) -> LSLaunchFlags     func symmetricDifference(_ other: LSLaunchFlags) -> LSLaunchFlags } extension LSLaunchFlags {     func contains(_ member: LSLaunchFlags) -> Bool     mutating func insert(_ newMember: LSLaunchFlags) -> (inserted: Bool, memberAfterInsert: LSLaunchFlags)     mutating func remove(_ member: LSLaunchFlags) -> LSLaunchFlags?     mutating func update(with newMember: LSLaunchFlags) -> LSLaunchFlags? } extension LSLaunchFlags {     convenience init()     mutating func formUnion(_ other: LSLaunchFlags)     mutating func formIntersection(_ other: LSLaunchFlags)     mutating func formSymmetricDifference(_ other: LSLaunchFlags) } extension LSLaunchFlags {     convenience init<S : Sequence where S.Iterator.Element == LSLaunchFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: LSLaunchFlags...)     mutating func subtract(_ other: LSLaunchFlags)     func isSubset(of other: LSLaunchFlags) -> Bool     func isSuperset(of other: LSLaunchFlags) -> Bool     func isDisjoint(with other: LSLaunchFlags) -> Bool     func subtracting(_ other: LSLaunchFlags) -> LSLaunchFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: LSLaunchFlags) -> Bool     func isStrictSubset(of other: LSLaunchFlags) -> Bool } ``` | OptionSet |

Modified [LSLaunchFlags.andDisplayErrors](https://developer.apple.com/documentation/coreservices/lslaunchflags/klslaunchanddisplayerrors)

|  | Declaration |
| --- | --- |
| From | ``` static var AndDisplayErrors: LSLaunchFlags { get } ``` |
| To | ``` static var andDisplayErrors: LSLaunchFlags { get } ``` |

Modified [LSLaunchFlags.andHide](https://developer.apple.com/documentation/coreservices/lslaunchflags/1444620-andhide)

|  | Declaration |
| --- | --- |
| From | ``` static var AndHide: LSLaunchFlags { get } ``` |
| To | ``` static var andHide: LSLaunchFlags { get } ``` |

Modified [LSLaunchFlags.andHideOthers](https://developer.apple.com/documentation/coreservices/lslaunchflags/klslaunchandhideothers)

|  | Declaration |
| --- | --- |
| From | ``` static var AndHideOthers: LSLaunchFlags { get } ``` |
| To | ``` static var andHideOthers: LSLaunchFlags { get } ``` |

Modified [LSLaunchFlags.andPrint](https://developer.apple.com/documentation/coreservices/lslaunchflags/1442495-andprint)

|  | Declaration |
| --- | --- |
| From | ``` static var AndPrint: LSLaunchFlags { get } ``` |
| To | ``` static var andPrint: LSLaunchFlags { get } ``` |

Modified [LSLaunchFlags.async](https://developer.apple.com/documentation/coreservices/lslaunchflags/1445037-async)

|  | Declaration |
| --- | --- |
| From | ``` static var Async: LSLaunchFlags { get } ``` |
| To | ``` static var async: LSLaunchFlags { get } ``` |

Modified [LSLaunchFlags.defaults](https://developer.apple.com/documentation/coreservices/lslaunchflags/klslaunchdefaults)

|  | Declaration |
| --- | --- |
| From | ``` static var Defaults: LSLaunchFlags { get } ``` |
| To | ``` static var defaults: LSLaunchFlags { get } ``` |

Modified [LSLaunchFlags.dontAddToRecents](https://developer.apple.com/documentation/coreservices/lslaunchflags/klslaunchdontaddtorecents)

|  | Declaration |
| --- | --- |
| From | ``` static var DontAddToRecents: LSLaunchFlags { get } ``` |
| To | ``` static var dontAddToRecents: LSLaunchFlags { get } ``` |

Modified [LSLaunchFlags.dontSwitch](https://developer.apple.com/documentation/coreservices/lslaunchflags/1442057-dontswitch)

|  | Declaration |
| --- | --- |
| From | ``` static var DontSwitch: LSLaunchFlags { get } ``` |
| To | ``` static var dontSwitch: LSLaunchFlags { get } ``` |

Modified [LSLaunchFlags.newInstance](https://developer.apple.com/documentation/coreservices/lslaunchflags/1443359-newinstance)

|  | Declaration |
| --- | --- |
| From | ``` static var NewInstance: LSLaunchFlags { get } ``` |
| To | ``` static var newInstance: LSLaunchFlags { get } ``` |

Modified [LSLaunchFSRefSpec [struct]](https://developer.apple.com/documentation/coreservices/lslaunchfsrefspec)

|  | Declaration |
| --- | --- |
| From | ``` struct LSLaunchFSRefSpec {     var appRef: UnsafePointer<FSRef>     var numDocs: Int     var itemRefs: UnsafePointer<FSRef>     var passThruParams: UnsafePointer<AEDesc>     var launchFlags: LSLaunchFlags     var asyncRefCon: UnsafeMutablePointer<Void>     init()     init(appRef appRef: UnsafePointer<FSRef>, numDocs numDocs: Int, itemRefs itemRefs: UnsafePointer<FSRef>, passThruParams passThruParams: UnsafePointer<AEDesc>, launchFlags launchFlags: LSLaunchFlags, asyncRefCon asyncRefCon: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct LSLaunchFSRefSpec {     var appRef: UnsafePointer<FSRef>!     var numDocs: Int     var itemRefs: UnsafePointer<FSRef>!     var passThruParams: UnsafePointer<AEDesc>!     var launchFlags: LSLaunchFlags     var asyncRefCon: UnsafeMutableRawPointer!     init()     init(appRef appRef: UnsafePointer<FSRef>!, numDocs numDocs: Int, itemRefs itemRefs: UnsafePointer<FSRef>!, passThruParams passThruParams: UnsafePointer<AEDesc>!, launchFlags launchFlags: LSLaunchFlags, asyncRefCon asyncRefCon: UnsafeMutableRawPointer!) } ``` |

Modified [LSLaunchFSRefSpec.appRef](https://developer.apple.com/documentation/coreservices/lslaunchfsrefspec/1448321-appref)

|  | Declaration |
| --- | --- |
| From | ``` var appRef: UnsafePointer<FSRef> ``` |
| To | ``` var appRef: UnsafePointer<FSRef>! ``` |

Modified [LSLaunchFSRefSpec.asyncRefCon](https://developer.apple.com/documentation/coreservices/lslaunchfsrefspec/1450600-asyncrefcon)

|  | Declaration |
| --- | --- |
| From | ``` var asyncRefCon: UnsafeMutablePointer<Void> ``` |
| To | ``` var asyncRefCon: UnsafeMutableRawPointer! ``` |

Modified [LSLaunchFSRefSpec.itemRefs](https://developer.apple.com/documentation/coreservices/lslaunchfsrefspec/1444360-itemrefs)

|  | Declaration |
| --- | --- |
| From | ``` var itemRefs: UnsafePointer<FSRef> ``` |
| To | ``` var itemRefs: UnsafePointer<FSRef>! ``` |

Modified [LSLaunchFSRefSpec.passThruParams](https://developer.apple.com/documentation/coreservices/lslaunchfsrefspec/1445933-passthruparams)

|  | Declaration |
| --- | --- |
| From | ``` var passThruParams: UnsafePointer<AEDesc> ``` |
| To | ``` var passThruParams: UnsafePointer<AEDesc>! ``` |

Modified [LSLaunchURLSpec [struct]](https://developer.apple.com/documentation/coreservices/lslaunchurlspec)

|  | Declaration |
| --- | --- |
| From | ``` struct LSLaunchURLSpec {     var appURL: Unmanaged<CFURL>?     var itemURLs: Unmanaged<CFArray>?     var passThruParams: UnsafePointer<AEDesc>     var launchFlags: LSLaunchFlags     var asyncRefCon: UnsafeMutablePointer<Void>     init()     init(appURL appURL: Unmanaged<CFURL>?, itemURLs itemURLs: Unmanaged<CFArray>?, passThruParams passThruParams: UnsafePointer<AEDesc>, launchFlags launchFlags: LSLaunchFlags, asyncRefCon asyncRefCon: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct LSLaunchURLSpec {     var appURL: Unmanaged<CFURL>?     var itemURLs: Unmanaged<CFArray>?     var passThruParams: UnsafePointer<AEDesc>?     var launchFlags: LSLaunchFlags     var asyncRefCon: UnsafeMutableRawPointer?     init()     init(appURL appURL: Unmanaged<CFURL>?, itemURLs itemURLs: Unmanaged<CFArray>?, passThruParams passThruParams: UnsafePointer<AEDesc>?, launchFlags launchFlags: LSLaunchFlags, asyncRefCon asyncRefCon: UnsafeMutableRawPointer?) } ``` |

Modified [LSLaunchURLSpec.asyncRefCon](https://developer.apple.com/documentation/coreservices/lslaunchurlspec/1448168-asyncrefcon)

|  | Declaration |
| --- | --- |
| From | ``` var asyncRefCon: UnsafeMutablePointer<Void> ``` |
| To | ``` var asyncRefCon: UnsafeMutableRawPointer? ``` |

Modified [LSLaunchURLSpec.passThruParams](https://developer.apple.com/documentation/coreservices/lslaunchurlspec/1445136-passthruparams)

|  | Declaration |
| --- | --- |
| From | ``` var passThruParams: UnsafePointer<AEDesc> ``` |
| To | ``` var passThruParams: UnsafePointer<AEDesc>? ``` |

Modified [LSRequestedInfo [struct]](https://developer.apple.com/documentation/coreservices/lsrequestedinfo)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct LSRequestedInfo : OptionSetType {     init(rawValue rawValue: OptionBits)     static var RequestExtension: LSRequestedInfo { get }     static var RequestTypeCreator: LSRequestedInfo { get }     static var RequestBasicFlagsOnly: LSRequestedInfo { get }     static var RequestAppTypeFlags: LSRequestedInfo { get }     static var RequestAllFlags: LSRequestedInfo { get }     static var RequestIconAndKind: LSRequestedInfo { get }     static var RequestExtensionFlagsOnly: LSRequestedInfo { get }     static var RequestAllInfo: LSRequestedInfo { get } } ``` | OptionSetType |
| To | ``` struct LSRequestedInfo : OptionSet {     init(rawValue rawValue: OptionBits)     static var requestExtension: LSRequestedInfo { get }     static var requestTypeCreator: LSRequestedInfo { get }     static var requestBasicFlagsOnly: LSRequestedInfo { get }     static var requestAppTypeFlags: LSRequestedInfo { get }     static var requestAllFlags: LSRequestedInfo { get }     static var requestIconAndKind: LSRequestedInfo { get }     static var requestExtensionFlagsOnly: LSRequestedInfo { get }     static var requestAllInfo: LSRequestedInfo { get }     func intersect(_ other: LSRequestedInfo) -> LSRequestedInfo     func exclusiveOr(_ other: LSRequestedInfo) -> LSRequestedInfo     mutating func unionInPlace(_ other: LSRequestedInfo)     mutating func intersectInPlace(_ other: LSRequestedInfo)     mutating func exclusiveOrInPlace(_ other: LSRequestedInfo)     func isSubsetOf(_ other: LSRequestedInfo) -> Bool     func isDisjointWith(_ other: LSRequestedInfo) -> Bool     func isSupersetOf(_ other: LSRequestedInfo) -> Bool     mutating func subtractInPlace(_ other: LSRequestedInfo)     func isStrictSupersetOf(_ other: LSRequestedInfo) -> Bool     func isStrictSubsetOf(_ other: LSRequestedInfo) -> Bool } extension LSRequestedInfo {     func union(_ other: LSRequestedInfo) -> LSRequestedInfo     func intersection(_ other: LSRequestedInfo) -> LSRequestedInfo     func symmetricDifference(_ other: LSRequestedInfo) -> LSRequestedInfo } extension LSRequestedInfo {     func contains(_ member: LSRequestedInfo) -> Bool     mutating func insert(_ newMember: LSRequestedInfo) -> (inserted: Bool, memberAfterInsert: LSRequestedInfo)     mutating func remove(_ member: LSRequestedInfo) -> LSRequestedInfo?     mutating func update(with newMember: LSRequestedInfo) -> LSRequestedInfo? } extension LSRequestedInfo {     convenience init()     mutating func formUnion(_ other: LSRequestedInfo)     mutating func formIntersection(_ other: LSRequestedInfo)     mutating func formSymmetricDifference(_ other: LSRequestedInfo) } extension LSRequestedInfo {     convenience init<S : Sequence where S.Iterator.Element == LSRequestedInfo>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: LSRequestedInfo...)     mutating func subtract(_ other: LSRequestedInfo)     func isSubset(of other: LSRequestedInfo) -> Bool     func isSuperset(of other: LSRequestedInfo) -> Bool     func isDisjoint(with other: LSRequestedInfo) -> Bool     func subtracting(_ other: LSRequestedInfo) -> LSRequestedInfo     var isEmpty: Bool { get }     func isStrictSuperset(of other: LSRequestedInfo) -> Bool     func isStrictSubset(of other: LSRequestedInfo) -> Bool } ``` | OptionSet |

Modified [LSRequestedInfo.requestAllFlags](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/1445356-requestallflags)

|  | Declaration |
| --- | --- |
| From | ``` static var RequestAllFlags: LSRequestedInfo { get } ``` |
| To | ``` static var requestAllFlags: LSRequestedInfo { get } ``` |

Modified [LSRequestedInfo.requestAllInfo](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequestallinfo)

|  | Declaration |
| --- | --- |
| From | ``` static var RequestAllInfo: LSRequestedInfo { get } ``` |
| To | ``` static var requestAllInfo: LSRequestedInfo { get } ``` |

Modified [LSRequestedInfo.requestAppTypeFlags](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequestapptypeflags)

|  | Declaration |
| --- | --- |
| From | ``` static var RequestAppTypeFlags: LSRequestedInfo { get } ``` |
| To | ``` static var requestAppTypeFlags: LSRequestedInfo { get } ``` |

Modified [LSRequestedInfo.requestBasicFlagsOnly](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/1447145-requestbasicflagsonly)

|  | Declaration |
| --- | --- |
| From | ``` static var RequestBasicFlagsOnly: LSRequestedInfo { get } ``` |
| To | ``` static var requestBasicFlagsOnly: LSRequestedInfo { get } ``` |

Modified [LSRequestedInfo.requestExtension](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequestextension)

|  | Declaration |
| --- | --- |
| From | ``` static var RequestExtension: LSRequestedInfo { get } ``` |
| To | ``` static var requestExtension: LSRequestedInfo { get } ``` |

Modified [LSRequestedInfo.requestExtensionFlagsOnly](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequestextensionflagsonly)

|  | Declaration |
| --- | --- |
| From | ``` static var RequestExtensionFlagsOnly: LSRequestedInfo { get } ``` |
| To | ``` static var requestExtensionFlagsOnly: LSRequestedInfo { get } ``` |

Modified [LSRequestedInfo.requestIconAndKind](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/1447945-requesticonandkind)

|  | Declaration |
| --- | --- |
| From | ``` static var RequestIconAndKind: LSRequestedInfo { get } ``` |
| To | ``` static var requestIconAndKind: LSRequestedInfo { get } ``` |

Modified [LSRequestedInfo.requestTypeCreator](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequesttypecreator)

|  | Declaration |
| --- | --- |
| From | ``` static var RequestTypeCreator: LSRequestedInfo { get } ``` |
| To | ``` static var requestTypeCreator: LSRequestedInfo { get } ``` |

Modified [LSRolesMask [struct]](https://developer.apple.com/documentation/coreservices/lsrolesmask)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct LSRolesMask : OptionSetType {     init(rawValue rawValue: OptionBits)     static var None: LSRolesMask { get }     static var Viewer: LSRolesMask { get }     static var Editor: LSRolesMask { get }     static var Shell: LSRolesMask { get }     static var All: LSRolesMask { get } } ``` | OptionSetType |
| To | ``` struct LSRolesMask : OptionSet {     init(rawValue rawValue: OptionBits)     static var none: LSRolesMask { get }     static var viewer: LSRolesMask { get }     static var editor: LSRolesMask { get }     static var shell: LSRolesMask { get }     static var all: LSRolesMask { get }     func intersect(_ other: LSRolesMask) -> LSRolesMask     func exclusiveOr(_ other: LSRolesMask) -> LSRolesMask     mutating func unionInPlace(_ other: LSRolesMask)     mutating func intersectInPlace(_ other: LSRolesMask)     mutating func exclusiveOrInPlace(_ other: LSRolesMask)     func isSubsetOf(_ other: LSRolesMask) -> Bool     func isDisjointWith(_ other: LSRolesMask) -> Bool     func isSupersetOf(_ other: LSRolesMask) -> Bool     mutating func subtractInPlace(_ other: LSRolesMask)     func isStrictSupersetOf(_ other: LSRolesMask) -> Bool     func isStrictSubsetOf(_ other: LSRolesMask) -> Bool } extension LSRolesMask {     func union(_ other: LSRolesMask) -> LSRolesMask     func intersection(_ other: LSRolesMask) -> LSRolesMask     func symmetricDifference(_ other: LSRolesMask) -> LSRolesMask } extension LSRolesMask {     func contains(_ member: LSRolesMask) -> Bool     mutating func insert(_ newMember: LSRolesMask) -> (inserted: Bool, memberAfterInsert: LSRolesMask)     mutating func remove(_ member: LSRolesMask) -> LSRolesMask?     mutating func update(with newMember: LSRolesMask) -> LSRolesMask? } extension LSRolesMask {     convenience init()     mutating func formUnion(_ other: LSRolesMask)     mutating func formIntersection(_ other: LSRolesMask)     mutating func formSymmetricDifference(_ other: LSRolesMask) } extension LSRolesMask {     convenience init<S : Sequence where S.Iterator.Element == LSRolesMask>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: LSRolesMask...)     mutating func subtract(_ other: LSRolesMask)     func isSubset(of other: LSRolesMask) -> Bool     func isSuperset(of other: LSRolesMask) -> Bool     func isDisjoint(with other: LSRolesMask) -> Bool     func subtracting(_ other: LSRolesMask) -> LSRolesMask     var isEmpty: Bool { get }     func isStrictSuperset(of other: LSRolesMask) -> Bool     func isStrictSubset(of other: LSRolesMask) -> Bool } ``` | OptionSet |

Modified [LSRolesMask.all](https://developer.apple.com/documentation/coreservices/lsrolesmask/1450616-all)

|  | Declaration |
| --- | --- |
| From | ``` static var All: LSRolesMask { get } ``` |
| To | ``` static var all: LSRolesMask { get } ``` |

Modified [LSRolesMask.editor](https://developer.apple.com/documentation/coreservices/lsrolesmask/klsroleseditor)

|  | Declaration |
| --- | --- |
| From | ``` static var Editor: LSRolesMask { get } ``` |
| To | ``` static var editor: LSRolesMask { get } ``` |

Modified [LSRolesMask.none](https://developer.apple.com/documentation/coreservices/lsrolesmask/klsrolesnone)

|  | Declaration |
| --- | --- |
| From | ``` static var None: LSRolesMask { get } ``` |
| To | ``` static var none: LSRolesMask { get } ``` |

Modified [LSRolesMask.shell](https://developer.apple.com/documentation/coreservices/lsrolesmask/1442557-shell)

|  | Declaration |
| --- | --- |
| From | ``` static var Shell: LSRolesMask { get } ``` |
| To | ``` static var shell: LSRolesMask { get } ``` |

Modified [LSRolesMask.viewer](https://developer.apple.com/documentation/coreservices/lsrolesmask/1441708-viewer)

|  | Declaration |
| --- | --- |
| From | ``` static var Viewer: LSRolesMask { get } ``` |
| To | ``` static var viewer: LSRolesMask { get } ``` |

Modified [MDExporterInterfaceStruct [struct]](https://developer.apple.com/documentation/coreservices/mdexporterinterfacestruct)

|  | Declaration |
| --- | --- |
| From | ``` struct MDExporterInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!     var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!     var Release: ((UnsafeMutablePointer<Void>) -> ULONG)!     var ImporterExportData: ((UnsafeMutablePointer<Void>, CFDictionary!, CFString!, CFString!) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, ImporterExportData ImporterExportData: ((UnsafeMutablePointer<Void>, CFDictionary!, CFString!, CFString!) -> DarwinBoolean)!) } ``` |
| To | ``` struct MDExporterInterfaceStruct {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var ImporterExportData: ((UnsafeMutableRawPointer?, CFDictionary?, CFString?, CFString?) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, ImporterExportData ImporterExportData: (@escaping (UnsafeMutableRawPointer?, CFDictionary?, CFString?, CFString?) -> DarwinBoolean)!) } ``` |

Modified [MDExporterInterfaceStruct.AddRef](https://developer.apple.com/documentation/coreservices/mdexporterinterfacestruct/1449918-addref)

|  | Declaration |
| --- | --- |
| From | ``` var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |
| To | ``` var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)! ``` |

Modified [MDExporterInterfaceStruct.ImporterExportData](https://developer.apple.com/documentation/coreservices/mdexporterinterfacestruct/1446348-importerexportdata)

|  | Declaration |
| --- | --- |
| From | ``` var ImporterExportData: ((UnsafeMutablePointer<Void>, CFDictionary!, CFString!, CFString!) -> DarwinBoolean)! ``` |
| To | ``` var ImporterExportData: ((UnsafeMutableRawPointer?, CFDictionary?, CFString?, CFString?) -> DarwinBoolean)! ``` |

Modified [MDExporterInterfaceStruct.QueryInterface](https://developer.apple.com/documentation/coreservices/mdexporterinterfacestruct/1450043-queryinterface)

|  | Declaration |
| --- | --- |
| From | ``` var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)! ``` |
| To | ``` var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)! ``` |

Modified [MDExporterInterfaceStruct.Release](https://developer.apple.com/documentation/coreservices/mdexporterinterfacestruct/1448271-release)

|  | Declaration |
| --- | --- |
| From | ``` var Release: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |
| To | ``` var Release: ((UnsafeMutableRawPointer?) -> ULONG)! ``` |

Modified [MDImporterBundleWrapperURLInterfaceStruct [struct]](https://developer.apple.com/documentation/coreservices/mdimporterbundlewrapperurlinterfacestruct)

|  | Declaration |
| --- | --- |
| From | ``` struct MDImporterBundleWrapperURLInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!     var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!     var Release: ((UnsafeMutablePointer<Void>) -> ULONG)!     var ImporterImportBundleWrapperURLData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, ImporterImportBundleWrapperURLData ImporterImportBundleWrapperURLData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> DarwinBoolean)!) } ``` |
| To | ``` struct MDImporterBundleWrapperURLInterfaceStruct {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var ImporterImportBundleWrapperURLData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportBundleWrapperURLData ImporterImportBundleWrapperURLData: (@escaping (UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!) } ``` |

Modified [MDImporterBundleWrapperURLInterfaceStruct.AddRef](https://developer.apple.com/documentation/coreservices/mdimporterbundlewrapperurlinterfacestruct/1442108-addref)

|  | Declaration |
| --- | --- |
| From | ``` var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |
| To | ``` var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)! ``` |

Modified [MDImporterBundleWrapperURLInterfaceStruct.ImporterImportBundleWrapperURLData](https://developer.apple.com/documentation/coreservices/mdimporterbundlewrapperurlinterfacestruct/1443517-importerimportbundlewrapperurlda)

|  | Declaration |
| --- | --- |
| From | ``` var ImporterImportBundleWrapperURLData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> DarwinBoolean)! ``` |
| To | ``` var ImporterImportBundleWrapperURLData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)! ``` |

Modified [MDImporterBundleWrapperURLInterfaceStruct.QueryInterface](https://developer.apple.com/documentation/coreservices/mdimporterbundlewrapperurlinterfacestruct/1445643-queryinterface)

|  | Declaration |
| --- | --- |
| From | ``` var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)! ``` |
| To | ``` var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)! ``` |

Modified [MDImporterBundleWrapperURLInterfaceStruct.Release](https://developer.apple.com/documentation/coreservices/mdimporterbundlewrapperurlinterfacestruct/1450356-release)

|  | Declaration |
| --- | --- |
| From | ``` var Release: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |
| To | ``` var Release: ((UnsafeMutableRawPointer?) -> ULONG)! ``` |

Modified [MDImporterInterfaceStruct [struct]](https://developer.apple.com/documentation/coreservices/mdimporterinterfacestruct)

|  | Declaration |
| --- | --- |
| From | ``` struct MDImporterInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!     var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!     var Release: ((UnsafeMutablePointer<Void>) -> ULONG)!     var ImporterImportData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFString!) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, ImporterImportData ImporterImportData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFString!) -> DarwinBoolean)!) } ``` |
| To | ``` struct MDImporterInterfaceStruct {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var ImporterImportData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFString?) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportData ImporterImportData: (@escaping (UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFString?) -> DarwinBoolean)!) } ``` |

Modified [MDImporterInterfaceStruct.AddRef](https://developer.apple.com/documentation/coreservices/mdimporterinterfacestruct/1443912-addref)

|  | Declaration |
| --- | --- |
| From | ``` var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |
| To | ``` var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)! ``` |

Modified [MDImporterInterfaceStruct.ImporterImportData](https://developer.apple.com/documentation/coreservices/mdimporterinterfacestruct/1444710-importerimportdata)

|  | Declaration |
| --- | --- |
| From | ``` var ImporterImportData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFString!) -> DarwinBoolean)! ``` |
| To | ``` var ImporterImportData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFString?) -> DarwinBoolean)! ``` |

Modified [MDImporterInterfaceStruct.QueryInterface](https://developer.apple.com/documentation/coreservices/mdimporterinterfacestruct/1446572-queryinterface)

|  | Declaration |
| --- | --- |
| From | ``` var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)! ``` |
| To | ``` var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)! ``` |

Modified [MDImporterInterfaceStruct.Release](https://developer.apple.com/documentation/coreservices/mdimporterinterfacestruct/1441880-release)

|  | Declaration |
| --- | --- |
| From | ``` var Release: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |
| To | ``` var Release: ((UnsafeMutableRawPointer?) -> ULONG)! ``` |

Modified [MDImporterURLInterfaceStruct [struct]](https://developer.apple.com/documentation/coreservices/mdimporterurlinterfacestruct)

|  | Declaration |
| --- | --- |
| From | ``` struct MDImporterURLInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!     var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!     var Release: ((UnsafeMutablePointer<Void>) -> ULONG)!     var ImporterImportURLData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, ImporterImportURLData ImporterImportURLData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> DarwinBoolean)!) } ``` |
| To | ``` struct MDImporterURLInterfaceStruct {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var ImporterImportURLData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportURLData ImporterImportURLData: (@escaping (UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)!) } ``` |

Modified [MDImporterURLInterfaceStruct.AddRef](https://developer.apple.com/documentation/coreservices/mdimporterurlinterfacestruct/1448177-addref)

|  | Declaration |
| --- | --- |
| From | ``` var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |
| To | ``` var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)! ``` |

Modified [MDImporterURLInterfaceStruct.ImporterImportURLData](https://developer.apple.com/documentation/coreservices/mdimporterurlinterfacestruct/1447378-importerimporturldata)

|  | Declaration |
| --- | --- |
| From | ``` var ImporterImportURLData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> DarwinBoolean)! ``` |
| To | ``` var ImporterImportURLData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFURL?) -> DarwinBoolean)! ``` |

Modified [MDImporterURLInterfaceStruct.QueryInterface](https://developer.apple.com/documentation/coreservices/mdimporterurlinterfacestruct/1442296-queryinterface)

|  | Declaration |
| --- | --- |
| From | ``` var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)! ``` |
| To | ``` var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)! ``` |

Modified [MDImporterURLInterfaceStruct.Release](https://developer.apple.com/documentation/coreservices/mdimporterurlinterfacestruct/1450015-release)

|  | Declaration |
| --- | --- |
| From | ``` var Release: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |
| To | ``` var Release: ((UnsafeMutableRawPointer?) -> ULONG)! ``` |

Modified [AcquireIconRef(_: IconRef!) -> OSErr](https://developer.apple.com/documentation/coreservices/1441852-acquireiconref)

|  | Declaration |
| --- | --- |
| From | ``` func AcquireIconRef(_ theIconRef: IconRef) -> OSErr ``` |
| To | ``` func AcquireIconRef(_ theIconRef: IconRef!) -> OSErr ``` |

Modified [AECallObjectAccessor(_: DescType, _: UnsafePointer<AEDesc>!, _: DescType, _: DescType, _: UnsafePointer<AEDesc>!, _: UnsafeMutablePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1447059-aecallobjectaccessor)

|  | Declaration |
| --- | --- |
| From | ``` func AECallObjectAccessor(_ desiredClass: DescType, _ containerToken: UnsafePointer<AEDesc>, _ containerClass: DescType, _ keyForm: DescType, _ keyData: UnsafePointer<AEDesc>, _ token: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func AECallObjectAccessor(_ desiredClass: DescType, _ containerToken: UnsafePointer<AEDesc>!, _ containerClass: DescType, _ keyForm: DescType, _ keyData: UnsafePointer<AEDesc>!, _ token: UnsafeMutablePointer<AEDesc>!) -> OSErr ``` |

Modified [AECheckIsRecord(_: UnsafePointer<AEDesc>!) -> Bool](https://developer.apple.com/documentation/coreservices/1444011-aecheckisrecord)

|  | Declaration |
| --- | --- |
| From | ``` func AECheckIsRecord(_ theDesc: UnsafePointer<AEDesc>) -> Bool ``` |
| To | ``` func AECheckIsRecord(_ theDesc: UnsafePointer<AEDesc>!) -> Bool ``` |

Modified [AECoerceDesc(_: UnsafePointer<AEDesc>!, _: DescType, _: UnsafeMutablePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1446519-aecoercedesc)

|  | Declaration |
| --- | --- |
| From | ``` func AECoerceDesc(_ theAEDesc: UnsafePointer<AEDesc>, _ toType: DescType, _ result: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func AECoerceDesc(_ theAEDesc: UnsafePointer<AEDesc>!, _ toType: DescType, _ result: UnsafeMutablePointer<AEDesc>!) -> OSErr ``` |

Modified [AECoerceDescProcPtr](https://developer.apple.com/documentation/coreservices/aecoercedescprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias AECoerceDescProcPtr = (UnsafePointer<AEDesc>, DescType, SRefCon, UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` typealias AECoerceDescProcPtr = (UnsafePointer<AEDesc>?, DescType, SRefCon?, UnsafeMutablePointer<AEDesc>?) -> OSErr ``` |

Modified [AECoerceDescUPP](https://developer.apple.com/documentation/coreservices/aecoercedescupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias AECoerceDescUPP = AECoerceDescProcPtr ``` |
| To | ``` typealias AECoerceDescUPP = CoreServices.AECoerceDescProcPtr ``` |

Modified [AECoercePtr(_: DescType, _: UnsafeRawPointer!, _: Size, _: DescType, _: UnsafeMutablePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1441846-aecoerceptr)

|  | Declaration |
| --- | --- |
| From | ``` func AECoercePtr(_ typeCode: DescType, _ dataPtr: UnsafePointer<Void>, _ dataSize: Size, _ toType: DescType, _ result: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func AECoercePtr(_ typeCode: DescType, _ dataPtr: UnsafeRawPointer!, _ dataSize: Size, _ toType: DescType, _ result: UnsafeMutablePointer<AEDesc>!) -> OSErr ``` |

Modified [AECoercePtrProcPtr](https://developer.apple.com/documentation/coreservices/aecoerceptrprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias AECoercePtrProcPtr = (DescType, UnsafePointer<Void>, Size, DescType, SRefCon, UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` typealias AECoercePtrProcPtr = (DescType, UnsafeRawPointer?, Size, DescType, SRefCon?, UnsafeMutablePointer<AEDesc>?) -> OSErr ``` |

Modified [AECoercePtrUPP](https://developer.apple.com/documentation/coreservices/aecoerceptrupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias AECoercePtrUPP = AECoercePtrProcPtr ``` |
| To | ``` typealias AECoercePtrUPP = CoreServices.AECoercePtrProcPtr ``` |

Modified [AECoercionHandlerUPP](https://developer.apple.com/documentation/coreservices/aecoercionhandlerupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias AECoercionHandlerUPP = AECoerceDescUPP ``` |
| To | ``` typealias AECoercionHandlerUPP = CoreServices.AECoerceDescUPP ``` |

Modified [AECompareDesc(_: UnsafePointer<AEDesc>!, _: UnsafePointer<AEDesc>!, _: UnsafeMutablePointer<DarwinBoolean>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1448782-aecomparedesc)

|  | Declaration |
| --- | --- |
| From | ``` func AECompareDesc(_ desc1: UnsafePointer<AEDesc>, _ desc2: UnsafePointer<AEDesc>, _ resultP: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |
| To | ``` func AECompareDesc(_ desc1: UnsafePointer<AEDesc>!, _ desc2: UnsafePointer<AEDesc>!, _ resultP: UnsafeMutablePointer<DarwinBoolean>!) -> OSStatus ``` |

Modified [AECountItems(_: UnsafePointer<AEDescList>!, _: UnsafeMutablePointer<Int>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1449533-aecountitems)

|  | Declaration |
| --- | --- |
| From | ``` func AECountItems(_ theAEDescList: UnsafePointer<AEDescList>, _ theCount: UnsafeMutablePointer<Int>) -> OSErr ``` |
| To | ``` func AECountItems(_ theAEDescList: UnsafePointer<AEDescList>!, _ theCount: UnsafeMutablePointer<Int>!) -> OSErr ``` |

Modified [AECreateAppleEvent(_: AEEventClass, _: AEEventID, _: UnsafePointer<AEAddressDesc>!, _: AEReturnID, _: AETransactionID, _: UnsafeMutablePointer<AppleEvent>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1448525-aecreateappleevent)

|  | Declaration |
| --- | --- |
| From | ``` func AECreateAppleEvent(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ target: UnsafePointer<AEAddressDesc>, _ returnID: AEReturnID, _ transactionID: AETransactionID, _ result: UnsafeMutablePointer<AppleEvent>) -> OSErr ``` |
| To | ``` func AECreateAppleEvent(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ target: UnsafePointer<AEAddressDesc>!, _ returnID: AEReturnID, _ transactionID: AETransactionID, _ result: UnsafeMutablePointer<AppleEvent>!) -> OSErr ``` |

Modified [AECreateDesc(_: DescType, _: UnsafeRawPointer!, _: Size, _: UnsafeMutablePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1448535-aecreatedesc)

|  | Declaration |
| --- | --- |
| From | ``` func AECreateDesc(_ typeCode: DescType, _ dataPtr: UnsafePointer<Void>, _ dataSize: Size, _ result: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func AECreateDesc(_ typeCode: DescType, _ dataPtr: UnsafeRawPointer!, _ dataSize: Size, _ result: UnsafeMutablePointer<AEDesc>!) -> OSErr ``` |

Modified [AECreateDescFromExternalPtr(_: OSType, _: UnsafeRawPointer!, _: Size, _: CoreServices.AEDisposeExternalUPP!, _: SRefCon!, _: UnsafeMutablePointer<AEDesc>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1446239-aecreatedescfromexternalptr)

|  | Declaration |
| --- | --- |
| From | ``` func AECreateDescFromExternalPtr(_ descriptorType: OSType, _ dataPtr: UnsafePointer<Void>, _ dataLength: Size, _ disposeCallback: AEDisposeExternalUPP!, _ disposeRefcon: SRefCon, _ theDesc: UnsafeMutablePointer<AEDesc>) -> OSStatus ``` |
| To | ``` func AECreateDescFromExternalPtr(_ descriptorType: OSType, _ dataPtr: UnsafeRawPointer!, _ dataLength: Size, _ disposeCallback: CoreServices.AEDisposeExternalUPP!, _ disposeRefcon: SRefCon!, _ theDesc: UnsafeMutablePointer<AEDesc>!) -> OSStatus ``` |

Modified [AECreateList(_: UnsafeRawPointer!, _: Size, _: Bool, _: UnsafeMutablePointer<AEDescList>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1448643-aecreatelist)

|  | Declaration |
| --- | --- |
| From | ``` func AECreateList(_ factoringPtr: UnsafePointer<Void>, _ factoredSize: Size, _ isRecord: Bool, _ resultList: UnsafeMutablePointer<AEDescList>) -> OSErr ``` |
| To | ``` func AECreateList(_ factoringPtr: UnsafeRawPointer!, _ factoredSize: Size, _ isRecord: Bool, _ resultList: UnsafeMutablePointer<AEDescList>!) -> OSErr ``` |

Modified [AECreateRemoteProcessResolver(_: CFAllocator!, _: CFURL!) -> AERemoteProcessResolverRef!](https://developer.apple.com/documentation/coreservices/1445692-aecreateremoteprocessresolver)

|  | Declaration |
| --- | --- |
| From | ``` func AECreateRemoteProcessResolver(_ allocator: CFAllocator!, _ url: CFURL!) -> AERemoteProcessResolverRef ``` |
| To | ``` func AECreateRemoteProcessResolver(_ allocator: CFAllocator!, _ url: CFURL!) -> AERemoteProcessResolverRef! ``` |

Modified [AEDataStorage](https://developer.apple.com/documentation/coreservices/aedatastorage)

|  | Declaration |
| --- | --- |
| From | ``` typealias AEDataStorage = UnsafeMutablePointer<AEDataStorageType> ``` |
| To | ``` typealias AEDataStorage = UnsafeMutablePointer<AEDataStorageType?> ``` |

Modified [AEDataStorageType](https://developer.apple.com/documentation/coreservices/aedatastoragetype)

|  | Declaration |
| --- | --- |
| From | ``` typealias AEDataStorageType = COpaquePointer ``` |
| To | ``` typealias AEDataStorageType = OpaquePointer ``` |

Modified [AEDecodeMessage(_: UnsafeMutablePointer<mach_msg_header_t>!, _: UnsafeMutablePointer<AppleEvent>!, _: UnsafeMutablePointer<AppleEvent>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1447827-aedecodemessage)

|  | Declaration |
| --- | --- |
| From | ``` func AEDecodeMessage(_ header: UnsafeMutablePointer<mach_msg_header_t>, _ event: UnsafeMutablePointer<AppleEvent>, _ reply: UnsafeMutablePointer<AppleEvent>) -> OSStatus ``` |
| To | ``` func AEDecodeMessage(_ header: UnsafeMutablePointer<mach_msg_header_t>!, _ event: UnsafeMutablePointer<AppleEvent>!, _ reply: UnsafeMutablePointer<AppleEvent>!) -> OSStatus ``` |

Modified [AEDeleteItem(_: UnsafeMutablePointer<AEDescList>!, _: Int) -> OSErr](https://developer.apple.com/documentation/coreservices/1447164-aedeleteitem)

|  | Declaration |
| --- | --- |
| From | ``` func AEDeleteItem(_ theAEDescList: UnsafeMutablePointer<AEDescList>, _ index: Int) -> OSErr ``` |
| To | ``` func AEDeleteItem(_ theAEDescList: UnsafeMutablePointer<AEDescList>!, _ index: Int) -> OSErr ``` |

Modified [AEDeleteParam(_: UnsafeMutablePointer<AppleEvent>!, _: AEKeyword) -> OSErr](https://developer.apple.com/documentation/coreservices/1444338-aedeleteparam)

|  | Declaration |
| --- | --- |
| From | ``` func AEDeleteParam(_ theAppleEvent: UnsafeMutablePointer<AppleEvent>, _ theAEKeyword: AEKeyword) -> OSErr ``` |
| To | ``` func AEDeleteParam(_ theAppleEvent: UnsafeMutablePointer<AppleEvent>!, _ theAEKeyword: AEKeyword) -> OSErr ``` |

Modified [AEDisposeDesc(_: UnsafeMutablePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1444208-aedisposedesc)

|  | Declaration |
| --- | --- |
| From | ``` func AEDisposeDesc(_ theAEDesc: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func AEDisposeDesc(_ theAEDesc: UnsafeMutablePointer<AEDesc>!) -> OSErr ``` |

Modified [AEDisposeExternalProcPtr](https://developer.apple.com/documentation/coreservices/aedisposeexternalprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias AEDisposeExternalProcPtr = (UnsafePointer<Void>, Size, SRefCon) -> Void ``` |
| To | ``` typealias AEDisposeExternalProcPtr = (UnsafeRawPointer?, Size, SRefCon?) -> Swift.Void ``` |

Modified [AEDisposeExternalUPP](https://developer.apple.com/documentation/coreservices/aedisposeexternalupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias AEDisposeExternalUPP = AEDisposeExternalProcPtr ``` |
| To | ``` typealias AEDisposeExternalUPP = CoreServices.AEDisposeExternalProcPtr ``` |

Modified [AEDisposeRemoteProcessResolver(_: AERemoteProcessResolverRef!)](https://developer.apple.com/documentation/coreservices/1442572-aedisposeremoteprocessresolver)

|  | Declaration |
| --- | --- |
| From | ``` func AEDisposeRemoteProcessResolver(_ ref: AERemoteProcessResolverRef) ``` |
| To | ``` func AEDisposeRemoteProcessResolver(_ ref: AERemoteProcessResolverRef!) ``` |

Modified [AEDisposeToken(_: UnsafeMutablePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1446783-aedisposetoken)

|  | Declaration |
| --- | --- |
| From | ``` func AEDisposeToken(_ theToken: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func AEDisposeToken(_ theToken: UnsafeMutablePointer<AEDesc>!) -> OSErr ``` |

Modified [AEDuplicateDesc(_: UnsafePointer<AEDesc>!, _: UnsafeMutablePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1442661-aeduplicatedesc)

|  | Declaration |
| --- | --- |
| From | ``` func AEDuplicateDesc(_ theAEDesc: UnsafePointer<AEDesc>, _ result: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func AEDuplicateDesc(_ theAEDesc: UnsafePointer<AEDesc>!, _ result: UnsafeMutablePointer<AEDesc>!) -> OSErr ``` |

Modified [AEEventHandlerProcPtr](https://developer.apple.com/documentation/coreservices/aeeventhandlerprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias AEEventHandlerProcPtr = (UnsafePointer<AppleEvent>, UnsafeMutablePointer<AppleEvent>, SRefCon) -> OSErr ``` |
| To | ``` typealias AEEventHandlerProcPtr = (UnsafePointer<AppleEvent>?, UnsafeMutablePointer<AppleEvent>?, SRefCon?) -> OSErr ``` |

Modified [AEEventHandlerUPP](https://developer.apple.com/documentation/coreservices/aeeventhandlerupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias AEEventHandlerUPP = AEEventHandlerProcPtr ``` |
| To | ``` typealias AEEventHandlerUPP = CoreServices.AEEventHandlerProcPtr ``` |

Modified [AEFlattenDesc(_: UnsafePointer<AEDesc>!, _: Ptr!, _: Size, _: UnsafeMutablePointer<Size>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1441808-aeflattendesc)

|  | Declaration |
| --- | --- |
| From | ``` func AEFlattenDesc(_ theAEDesc: UnsafePointer<AEDesc>, _ buffer: Ptr, _ bufferSize: Size, _ actualSize: UnsafeMutablePointer<Size>) -> OSStatus ``` |
| To | ``` func AEFlattenDesc(_ theAEDesc: UnsafePointer<AEDesc>!, _ buffer: Ptr!, _ bufferSize: Size, _ actualSize: UnsafeMutablePointer<Size>!) -> OSStatus ``` |

Modified [AEGetArray(_: UnsafePointer<AEDescList>!, _: AEArrayType, _: AEArrayDataPointer!, _: Size, _: UnsafeMutablePointer<DescType>!, _: UnsafeMutablePointer<Size>!, _: UnsafeMutablePointer<Int>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1445720-aegetarray)

|  | Declaration |
| --- | --- |
| From | ``` func AEGetArray(_ theAEDescList: UnsafePointer<AEDescList>, _ arrayType: AEArrayType, _ arrayPtr: AEArrayDataPointer, _ maximumSize: Size, _ itemType: UnsafeMutablePointer<DescType>, _ itemSize: UnsafeMutablePointer<Size>, _ itemCount: UnsafeMutablePointer<Int>) -> OSErr ``` |
| To | ``` func AEGetArray(_ theAEDescList: UnsafePointer<AEDescList>!, _ arrayType: AEArrayType, _ arrayPtr: AEArrayDataPointer!, _ maximumSize: Size, _ itemType: UnsafeMutablePointer<DescType>!, _ itemSize: UnsafeMutablePointer<Size>!, _ itemCount: UnsafeMutablePointer<Int>!) -> OSErr ``` |

Modified [AEGetAttributeDesc(_: UnsafePointer<AppleEvent>!, _: AEKeyword, _: DescType, _: UnsafeMutablePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1450314-aegetattributedesc)

|  | Declaration |
| --- | --- |
| From | ``` func AEGetAttributeDesc(_ theAppleEvent: UnsafePointer<AppleEvent>, _ theAEKeyword: AEKeyword, _ desiredType: DescType, _ result: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func AEGetAttributeDesc(_ theAppleEvent: UnsafePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ desiredType: DescType, _ result: UnsafeMutablePointer<AEDesc>!) -> OSErr ``` |

Modified [AEGetAttributePtr(_: UnsafePointer<AppleEvent>!, _: AEKeyword, _: DescType, _: UnsafeMutablePointer<DescType>!, _: UnsafeMutableRawPointer!, _: Size, _: UnsafeMutablePointer<Size>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1445109-aegetattributeptr)

|  | Declaration |
| --- | --- |
| From | ``` func AEGetAttributePtr(_ theAppleEvent: UnsafePointer<AppleEvent>, _ theAEKeyword: AEKeyword, _ desiredType: DescType, _ typeCode: UnsafeMutablePointer<DescType>, _ dataPtr: UnsafeMutablePointer<Void>, _ maximumSize: Size, _ actualSize: UnsafeMutablePointer<Size>) -> OSErr ``` |
| To | ``` func AEGetAttributePtr(_ theAppleEvent: UnsafePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ desiredType: DescType, _ typeCode: UnsafeMutablePointer<DescType>!, _ dataPtr: UnsafeMutableRawPointer!, _ maximumSize: Size, _ actualSize: UnsafeMutablePointer<Size>!) -> OSErr ``` |

Modified [AEGetCoercionHandler(_: DescType, _: DescType, _: UnsafeMutablePointer<CoreServices.AECoercionHandlerUPP?>!, _: UnsafeMutablePointer<SRefCon?>!, _: UnsafeMutablePointer<DarwinBoolean>!, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1445348-aegetcoercionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func AEGetCoercionHandler(_ fromType: DescType, _ toType: DescType, _ handler: UnsafeMutablePointer<AECoercionHandlerUPP?>, _ handlerRefcon: UnsafeMutablePointer<SRefCon>, _ fromTypeIsDesc: UnsafeMutablePointer<DarwinBoolean>, _ isSysHandler: Bool) -> OSErr ``` |
| To | ``` func AEGetCoercionHandler(_ fromType: DescType, _ toType: DescType, _ handler: UnsafeMutablePointer<CoreServices.AECoercionHandlerUPP?>!, _ handlerRefcon: UnsafeMutablePointer<SRefCon?>!, _ fromTypeIsDesc: UnsafeMutablePointer<DarwinBoolean>!, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AEGetDescData(_: UnsafePointer<AEDesc>!, _: UnsafeMutableRawPointer!, _: Size) -> OSErr](https://developer.apple.com/documentation/coreservices/1444427-aegetdescdata)

|  | Declaration |
| --- | --- |
| From | ``` func AEGetDescData(_ theAEDesc: UnsafePointer<AEDesc>, _ dataPtr: UnsafeMutablePointer<Void>, _ maximumSize: Size) -> OSErr ``` |
| To | ``` func AEGetDescData(_ theAEDesc: UnsafePointer<AEDesc>!, _ dataPtr: UnsafeMutableRawPointer!, _ maximumSize: Size) -> OSErr ``` |

Modified [AEGetDescDataRange(_: UnsafePointer<AEDesc>!, _: UnsafeMutableRawPointer!, _: Size, _: Size) -> OSStatus](https://developer.apple.com/documentation/coreservices/1446560-aegetdescdatarange)

|  | Declaration |
| --- | --- |
| From | ``` func AEGetDescDataRange(_ dataDesc: UnsafePointer<AEDesc>, _ buffer: UnsafeMutablePointer<Void>, _ offset: Size, _ length: Size) -> OSStatus ``` |
| To | ``` func AEGetDescDataRange(_ dataDesc: UnsafePointer<AEDesc>!, _ buffer: UnsafeMutableRawPointer!, _ offset: Size, _ length: Size) -> OSStatus ``` |

Modified [AEGetDescDataSize(_: UnsafePointer<AEDesc>!) -> Size](https://developer.apple.com/documentation/coreservices/1450119-aegetdescdatasize)

|  | Declaration |
| --- | --- |
| From | ``` func AEGetDescDataSize(_ theAEDesc: UnsafePointer<AEDesc>) -> Size ``` |
| To | ``` func AEGetDescDataSize(_ theAEDesc: UnsafePointer<AEDesc>!) -> Size ``` |

Modified [AEGetEventHandler(_: AEEventClass, _: AEEventID, _: UnsafeMutablePointer<CoreServices.AEEventHandlerUPP?>!, _: UnsafeMutablePointer<SRefCon?>!, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1445631-aegeteventhandler)

|  | Declaration |
| --- | --- |
| From | ``` func AEGetEventHandler(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ handler: UnsafeMutablePointer<AEEventHandlerUPP?>, _ handlerRefcon: UnsafeMutablePointer<SRefCon>, _ isSysHandler: Bool) -> OSErr ``` |
| To | ``` func AEGetEventHandler(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ handler: UnsafeMutablePointer<CoreServices.AEEventHandlerUPP?>!, _ handlerRefcon: UnsafeMutablePointer<SRefCon?>!, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AEGetNthDesc(_: UnsafePointer<AEDescList>!, _: Int, _: DescType, _: UnsafeMutablePointer<AEKeyword>!, _: UnsafeMutablePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1448326-aegetnthdesc)

|  | Declaration |
| --- | --- |
| From | ``` func AEGetNthDesc(_ theAEDescList: UnsafePointer<AEDescList>, _ index: Int, _ desiredType: DescType, _ theAEKeyword: UnsafeMutablePointer<AEKeyword>, _ result: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func AEGetNthDesc(_ theAEDescList: UnsafePointer<AEDescList>!, _ index: Int, _ desiredType: DescType, _ theAEKeyword: UnsafeMutablePointer<AEKeyword>!, _ result: UnsafeMutablePointer<AEDesc>!) -> OSErr ``` |

Modified [AEGetNthPtr(_: UnsafePointer<AEDescList>!, _: Int, _: DescType, _: UnsafeMutablePointer<AEKeyword>!, _: UnsafeMutablePointer<DescType>!, _: UnsafeMutableRawPointer!, _: Size, _: UnsafeMutablePointer<Size>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1447539-aegetnthptr)

|  | Declaration |
| --- | --- |
| From | ``` func AEGetNthPtr(_ theAEDescList: UnsafePointer<AEDescList>, _ index: Int, _ desiredType: DescType, _ theAEKeyword: UnsafeMutablePointer<AEKeyword>, _ typeCode: UnsafeMutablePointer<DescType>, _ dataPtr: UnsafeMutablePointer<Void>, _ maximumSize: Size, _ actualSize: UnsafeMutablePointer<Size>) -> OSErr ``` |
| To | ``` func AEGetNthPtr(_ theAEDescList: UnsafePointer<AEDescList>!, _ index: Int, _ desiredType: DescType, _ theAEKeyword: UnsafeMutablePointer<AEKeyword>!, _ typeCode: UnsafeMutablePointer<DescType>!, _ dataPtr: UnsafeMutableRawPointer!, _ maximumSize: Size, _ actualSize: UnsafeMutablePointer<Size>!) -> OSErr ``` |

Modified [AEGetObjectAccessor(_: DescType, _: DescType, _: UnsafeMutablePointer<CoreServices.OSLAccessorUPP?>!, _: UnsafeMutablePointer<SRefCon?>!, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1449054-aegetobjectaccessor)

|  | Declaration |
| --- | --- |
| From | ``` func AEGetObjectAccessor(_ desiredClass: DescType, _ containerType: DescType, _ accessor: UnsafeMutablePointer<OSLAccessorUPP?>, _ accessorRefcon: UnsafeMutablePointer<SRefCon>, _ isSysHandler: Bool) -> OSErr ``` |
| To | ``` func AEGetObjectAccessor(_ desiredClass: DescType, _ containerType: DescType, _ accessor: UnsafeMutablePointer<CoreServices.OSLAccessorUPP?>!, _ accessorRefcon: UnsafeMutablePointer<SRefCon?>!, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AEGetParamDesc(_: UnsafePointer<AppleEvent>!, _: AEKeyword, _: DescType, _: UnsafeMutablePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1449233-aegetparamdesc)

|  | Declaration |
| --- | --- |
| From | ``` func AEGetParamDesc(_ theAppleEvent: UnsafePointer<AppleEvent>, _ theAEKeyword: AEKeyword, _ desiredType: DescType, _ result: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func AEGetParamDesc(_ theAppleEvent: UnsafePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ desiredType: DescType, _ result: UnsafeMutablePointer<AEDesc>!) -> OSErr ``` |

Modified [AEGetParamPtr(_: UnsafePointer<AppleEvent>!, _: AEKeyword, _: DescType, _: UnsafeMutablePointer<DescType>!, _: UnsafeMutableRawPointer!, _: Size, _: UnsafeMutablePointer<Size>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1444069-aegetparamptr)

|  | Declaration |
| --- | --- |
| From | ``` func AEGetParamPtr(_ theAppleEvent: UnsafePointer<AppleEvent>, _ theAEKeyword: AEKeyword, _ desiredType: DescType, _ actualType: UnsafeMutablePointer<DescType>, _ dataPtr: UnsafeMutablePointer<Void>, _ maximumSize: Size, _ actualSize: UnsafeMutablePointer<Size>) -> OSErr ``` |
| To | ``` func AEGetParamPtr(_ theAppleEvent: UnsafePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ desiredType: DescType, _ actualType: UnsafeMutablePointer<DescType>!, _ dataPtr: UnsafeMutableRawPointer!, _ maximumSize: Size, _ actualSize: UnsafeMutablePointer<Size>!) -> OSErr ``` |

Modified [AEGetSpecialHandler(_: AEKeyword, _: UnsafeMutablePointer<CoreServices.AEEventHandlerUPP?>!, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1444274-aegetspecialhandler)

|  | Declaration |
| --- | --- |
| From | ``` func AEGetSpecialHandler(_ functionClass: AEKeyword, _ handler: UnsafeMutablePointer<AEEventHandlerUPP?>, _ isSysHandler: Bool) -> OSErr ``` |
| To | ``` func AEGetSpecialHandler(_ functionClass: AEKeyword, _ handler: UnsafeMutablePointer<CoreServices.AEEventHandlerUPP?>!, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AEInitializeDesc(_: UnsafeMutablePointer<AEDesc>!)](https://developer.apple.com/documentation/coreservices/1446047-aeinitializedesc)

|  | Declaration |
| --- | --- |
| From | ``` func AEInitializeDesc(_ desc: UnsafeMutablePointer<AEDesc>) ``` |
| To | ``` func AEInitializeDesc(_ desc: UnsafeMutablePointer<AEDesc>!) ``` |

Modified [AEInstallCoercionHandler(_: DescType, _: DescType, _: CoreServices.AECoercionHandlerUPP!, _: SRefCon!, _: Bool, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1445548-aeinstallcoercionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func AEInstallCoercionHandler(_ fromType: DescType, _ toType: DescType, _ handler: AECoercionHandlerUPP!, _ handlerRefcon: SRefCon, _ fromTypeIsDesc: Bool, _ isSysHandler: Bool) -> OSErr ``` |
| To | ``` func AEInstallCoercionHandler(_ fromType: DescType, _ toType: DescType, _ handler: CoreServices.AECoercionHandlerUPP!, _ handlerRefcon: SRefCon!, _ fromTypeIsDesc: Bool, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AEInstallEventHandler(_: AEEventClass, _: AEEventID, _: CoreServices.AEEventHandlerUPP!, _: SRefCon!, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1448596-aeinstalleventhandler)

|  | Declaration |
| --- | --- |
| From | ``` func AEInstallEventHandler(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ handler: AEEventHandlerUPP!, _ handlerRefcon: SRefCon, _ isSysHandler: Bool) -> OSErr ``` |
| To | ``` func AEInstallEventHandler(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ handler: CoreServices.AEEventHandlerUPP!, _ handlerRefcon: SRefCon!, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AEInstallObjectAccessor(_: DescType, _: DescType, _: CoreServices.OSLAccessorUPP!, _: SRefCon!, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1447905-aeinstallobjectaccessor)

|  | Declaration |
| --- | --- |
| From | ``` func AEInstallObjectAccessor(_ desiredClass: DescType, _ containerType: DescType, _ theAccessor: OSLAccessorUPP!, _ accessorRefcon: SRefCon, _ isSysHandler: Bool) -> OSErr ``` |
| To | ``` func AEInstallObjectAccessor(_ desiredClass: DescType, _ containerType: DescType, _ theAccessor: CoreServices.OSLAccessorUPP!, _ accessorRefcon: SRefCon!, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AEInstallSpecialHandler(_: AEKeyword, _: CoreServices.AEEventHandlerUPP!, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1445532-aeinstallspecialhandler)

|  | Declaration |
| --- | --- |
| From | ``` func AEInstallSpecialHandler(_ functionClass: AEKeyword, _ handler: AEEventHandlerUPP!, _ isSysHandler: Bool) -> OSErr ``` |
| To | ``` func AEInstallSpecialHandler(_ functionClass: AEKeyword, _ handler: CoreServices.AEEventHandlerUPP!, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AEManagerInfo(_: AEKeyword, _: UnsafeMutablePointer<Int>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1449373-aemanagerinfo)

|  | Declaration |
| --- | --- |
| From | ``` func AEManagerInfo(_ keyWord: AEKeyword, _ result: UnsafeMutablePointer<Int>) -> OSErr ``` |
| To | ``` func AEManagerInfo(_ keyWord: AEKeyword, _ result: UnsafeMutablePointer<Int>!) -> OSErr ``` |

Modified [AEPrintDescToHandle(_: UnsafePointer<AEDesc>!, _: UnsafeMutablePointer<Handle?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1445158-aeprintdesctohandle)

|  | Declaration |
| --- | --- |
| From | ``` func AEPrintDescToHandle(_ desc: UnsafePointer<AEDesc>, _ result: UnsafeMutablePointer<Handle>) -> OSStatus ``` |
| To | ``` func AEPrintDescToHandle(_ desc: UnsafePointer<AEDesc>!, _ result: UnsafeMutablePointer<Handle?>!) -> OSStatus ``` |

Modified [AEProcessMessage(_: UnsafeMutablePointer<mach_msg_header_t>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1444387-aeprocessmessage)

|  | Declaration |
| --- | --- |
| From | ``` func AEProcessMessage(_ header: UnsafeMutablePointer<mach_msg_header_t>) -> OSStatus ``` |
| To | ``` func AEProcessMessage(_ header: UnsafeMutablePointer<mach_msg_header_t>!) -> OSStatus ``` |

Modified [AEPutArray(_: UnsafeMutablePointer<AEDescList>!, _: AEArrayType, _: UnsafePointer<AEArrayData>!, _: DescType, _: Size, _: Int) -> OSErr](https://developer.apple.com/documentation/coreservices/1442535-aeputarray)

|  | Declaration |
| --- | --- |
| From | ``` func AEPutArray(_ theAEDescList: UnsafeMutablePointer<AEDescList>, _ arrayType: AEArrayType, _ arrayPtr: UnsafePointer<AEArrayData>, _ itemType: DescType, _ itemSize: Size, _ itemCount: Int) -> OSErr ``` |
| To | ``` func AEPutArray(_ theAEDescList: UnsafeMutablePointer<AEDescList>!, _ arrayType: AEArrayType, _ arrayPtr: UnsafePointer<AEArrayData>!, _ itemType: DescType, _ itemSize: Size, _ itemCount: Int) -> OSErr ``` |

Modified [AEPutAttributeDesc(_: UnsafeMutablePointer<AppleEvent>!, _: AEKeyword, _: UnsafePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1441790-aeputattributedesc)

|  | Declaration |
| --- | --- |
| From | ``` func AEPutAttributeDesc(_ theAppleEvent: UnsafeMutablePointer<AppleEvent>, _ theAEKeyword: AEKeyword, _ theAEDesc: UnsafePointer<AEDesc>) -> OSErr ``` |
| To | ``` func AEPutAttributeDesc(_ theAppleEvent: UnsafeMutablePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ theAEDesc: UnsafePointer<AEDesc>!) -> OSErr ``` |

Modified [AEPutAttributePtr(_: UnsafeMutablePointer<AppleEvent>!, _: AEKeyword, _: DescType, _: UnsafeRawPointer!, _: Size) -> OSErr](https://developer.apple.com/documentation/coreservices/1445940-aeputattributeptr)

|  | Declaration |
| --- | --- |
| From | ``` func AEPutAttributePtr(_ theAppleEvent: UnsafeMutablePointer<AppleEvent>, _ theAEKeyword: AEKeyword, _ typeCode: DescType, _ dataPtr: UnsafePointer<Void>, _ dataSize: Size) -> OSErr ``` |
| To | ``` func AEPutAttributePtr(_ theAppleEvent: UnsafeMutablePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ typeCode: DescType, _ dataPtr: UnsafeRawPointer!, _ dataSize: Size) -> OSErr ``` |

Modified [AEPutDesc(_: UnsafeMutablePointer<AEDescList>!, _: Int, _: UnsafePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1450093-aeputdesc)

|  | Declaration |
| --- | --- |
| From | ``` func AEPutDesc(_ theAEDescList: UnsafeMutablePointer<AEDescList>, _ index: Int, _ theAEDesc: UnsafePointer<AEDesc>) -> OSErr ``` |
| To | ``` func AEPutDesc(_ theAEDescList: UnsafeMutablePointer<AEDescList>!, _ index: Int, _ theAEDesc: UnsafePointer<AEDesc>!) -> OSErr ``` |

Modified [AEPutParamDesc(_: UnsafeMutablePointer<AppleEvent>!, _: AEKeyword, _: UnsafePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1447576-aeputparamdesc)

|  | Declaration |
| --- | --- |
| From | ``` func AEPutParamDesc(_ theAppleEvent: UnsafeMutablePointer<AppleEvent>, _ theAEKeyword: AEKeyword, _ theAEDesc: UnsafePointer<AEDesc>) -> OSErr ``` |
| To | ``` func AEPutParamDesc(_ theAppleEvent: UnsafeMutablePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ theAEDesc: UnsafePointer<AEDesc>!) -> OSErr ``` |

Modified [AEPutParamPtr(_: UnsafeMutablePointer<AppleEvent>!, _: AEKeyword, _: DescType, _: UnsafeRawPointer!, _: Size) -> OSErr](https://developer.apple.com/documentation/coreservices/1449263-aeputparamptr)

|  | Declaration |
| --- | --- |
| From | ``` func AEPutParamPtr(_ theAppleEvent: UnsafeMutablePointer<AppleEvent>, _ theAEKeyword: AEKeyword, _ typeCode: DescType, _ dataPtr: UnsafePointer<Void>, _ dataSize: Size) -> OSErr ``` |
| To | ``` func AEPutParamPtr(_ theAppleEvent: UnsafeMutablePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ typeCode: DescType, _ dataPtr: UnsafeRawPointer!, _ dataSize: Size) -> OSErr ``` |

Modified [AEPutPtr(_: UnsafeMutablePointer<AEDescList>!, _: Int, _: DescType, _: UnsafeRawPointer!, _: Size) -> OSErr](https://developer.apple.com/documentation/coreservices/1445287-aeputptr)

|  | Declaration |
| --- | --- |
| From | ``` func AEPutPtr(_ theAEDescList: UnsafeMutablePointer<AEDescList>, _ index: Int, _ typeCode: DescType, _ dataPtr: UnsafePointer<Void>, _ dataSize: Size) -> OSErr ``` |
| To | ``` func AEPutPtr(_ theAEDescList: UnsafeMutablePointer<AEDescList>!, _ index: Int, _ typeCode: DescType, _ dataPtr: UnsafeRawPointer!, _ dataSize: Size) -> OSErr ``` |

Modified [AERemoteProcessResolverCallback](https://developer.apple.com/documentation/coreservices/aeremoteprocessresolvercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias AERemoteProcessResolverCallback = (AERemoteProcessResolverRef, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias AERemoteProcessResolverCallback = (AERemoteProcessResolverRef?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [AERemoteProcessResolverGetProcesses(_: AERemoteProcessResolverRef!, _: UnsafeMutablePointer<CFStreamError>!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/coreservices/1444456-aeremoteprocessresolvergetproces)

|  | Declaration |
| --- | --- |
| From | ``` func AERemoteProcessResolverGetProcesses(_ ref: AERemoteProcessResolverRef, _ outError: UnsafeMutablePointer<CFStreamError>) -> Unmanaged<CFArray>! ``` |
| To | ``` func AERemoteProcessResolverGetProcesses(_ ref: AERemoteProcessResolverRef!, _ outError: UnsafeMutablePointer<CFStreamError>!) -> Unmanaged<CFArray>! ``` |

Modified [AERemoteProcessResolverRef](https://developer.apple.com/documentation/coreservices/aeremoteprocessresolverref)

|  | Declaration |
| --- | --- |
| From | ``` typealias AERemoteProcessResolverRef = COpaquePointer ``` |
| To | ``` typealias AERemoteProcessResolverRef = OpaquePointer ``` |

Modified [AERemoteProcessResolverScheduleWithRunLoop(_: AERemoteProcessResolverRef!, _: CFRunLoop!, _: CFString!, _: CoreServices.AERemoteProcessResolverCallback!, _: UnsafePointer<AERemoteProcessResolverContext>!)](https://developer.apple.com/documentation/coreservices/1447259-aeremoteprocessresolverschedulew)

|  | Declaration |
| --- | --- |
| From | ``` func AERemoteProcessResolverScheduleWithRunLoop(_ ref: AERemoteProcessResolverRef, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!, _ callback: AERemoteProcessResolverCallback!, _ ctx: UnsafePointer<AERemoteProcessResolverContext>) ``` |
| To | ``` func AERemoteProcessResolverScheduleWithRunLoop(_ ref: AERemoteProcessResolverRef!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!, _ callback: CoreServices.AERemoteProcessResolverCallback!, _ ctx: UnsafePointer<AERemoteProcessResolverContext>!) ``` |

Modified [AERemoveCoercionHandler(_: DescType, _: DescType, _: CoreServices.AECoercionHandlerUPP!, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1441907-aeremovecoercionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func AERemoveCoercionHandler(_ fromType: DescType, _ toType: DescType, _ handler: AECoercionHandlerUPP!, _ isSysHandler: Bool) -> OSErr ``` |
| To | ``` func AERemoveCoercionHandler(_ fromType: DescType, _ toType: DescType, _ handler: CoreServices.AECoercionHandlerUPP!, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AERemoveEventHandler(_: AEEventClass, _: AEEventID, _: CoreServices.AEEventHandlerUPP!, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1445239-aeremoveeventhandler)

|  | Declaration |
| --- | --- |
| From | ``` func AERemoveEventHandler(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ handler: AEEventHandlerUPP!, _ isSysHandler: Bool) -> OSErr ``` |
| To | ``` func AERemoveEventHandler(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ handler: CoreServices.AEEventHandlerUPP!, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AERemoveObjectAccessor(_: DescType, _: DescType, _: CoreServices.OSLAccessorUPP!, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1442552-aeremoveobjectaccessor)

|  | Declaration |
| --- | --- |
| From | ``` func AERemoveObjectAccessor(_ desiredClass: DescType, _ containerType: DescType, _ theAccessor: OSLAccessorUPP!, _ isSysHandler: Bool) -> OSErr ``` |
| To | ``` func AERemoveObjectAccessor(_ desiredClass: DescType, _ containerType: DescType, _ theAccessor: CoreServices.OSLAccessorUPP!, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AERemoveSpecialHandler(_: AEKeyword, _: CoreServices.AEEventHandlerUPP!, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1447960-aeremovespecialhandler)

|  | Declaration |
| --- | --- |
| From | ``` func AERemoveSpecialHandler(_ functionClass: AEKeyword, _ handler: AEEventHandlerUPP!, _ isSysHandler: Bool) -> OSErr ``` |
| To | ``` func AERemoveSpecialHandler(_ functionClass: AEKeyword, _ handler: CoreServices.AEEventHandlerUPP!, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AEReplaceDescData(_: DescType, _: UnsafeRawPointer!, _: Size, _: UnsafeMutablePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1446695-aereplacedescdata)

|  | Declaration |
| --- | --- |
| From | ``` func AEReplaceDescData(_ typeCode: DescType, _ dataPtr: UnsafePointer<Void>, _ dataSize: Size, _ theAEDesc: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func AEReplaceDescData(_ typeCode: DescType, _ dataPtr: UnsafeRawPointer!, _ dataSize: Size, _ theAEDesc: UnsafeMutablePointer<AEDesc>!) -> OSErr ``` |

Modified [AEResolve(_: UnsafePointer<AEDesc>!, _: Int16, _: UnsafeMutablePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1449720-aeresolve)

|  | Declaration |
| --- | --- |
| From | ``` func AEResolve(_ objectSpecifier: UnsafePointer<AEDesc>, _ callbackFlags: Int16, _ theToken: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func AEResolve(_ objectSpecifier: UnsafePointer<AEDesc>!, _ callbackFlags: Int16, _ theToken: UnsafeMutablePointer<AEDesc>!) -> OSErr ``` |

Modified [AESendMessage(_: UnsafePointer<AppleEvent>!, _: UnsafeMutablePointer<AppleEvent>!, _: AESendMode, _: Int) -> OSStatus](https://developer.apple.com/documentation/coreservices/1442994-aesendmessage)

|  | Declaration |
| --- | --- |
| From | ``` func AESendMessage(_ event: UnsafePointer<AppleEvent>, _ reply: UnsafeMutablePointer<AppleEvent>, _ sendMode: AESendMode, _ timeOutInTicks: Int) -> OSStatus ``` |
| To | ``` func AESendMessage(_ event: UnsafePointer<AppleEvent>!, _ reply: UnsafeMutablePointer<AppleEvent>!, _ sendMode: AESendMode, _ timeOutInTicks: Int) -> OSStatus ``` |

Modified [AESetObjectCallbacks(_: CoreServices.OSLCompareUPP!, _: CoreServices.OSLCountUPP!, _: CoreServices.OSLDisposeTokenUPP!, _: CoreServices.OSLGetMarkTokenUPP!, _: CoreServices.OSLMarkUPP!, _: CoreServices.OSLAdjustMarksUPP!, _: CoreServices.OSLGetErrDescUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1447756-aesetobjectcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` func AESetObjectCallbacks(_ myCompareProc: OSLCompareUPP!, _ myCountProc: OSLCountUPP!, _ myDisposeTokenProc: OSLDisposeTokenUPP!, _ myGetMarkTokenProc: OSLGetMarkTokenUPP!, _ myMarkProc: OSLMarkUPP!, _ myAdjustMarksProc: OSLAdjustMarksUPP!, _ myGetErrDescProcPtr: OSLGetErrDescUPP!) -> OSErr ``` |
| To | ``` func AESetObjectCallbacks(_ myCompareProc: CoreServices.OSLCompareUPP!, _ myCountProc: CoreServices.OSLCountUPP!, _ myDisposeTokenProc: CoreServices.OSLDisposeTokenUPP!, _ myGetMarkTokenProc: CoreServices.OSLGetMarkTokenUPP!, _ myMarkProc: CoreServices.OSLMarkUPP!, _ myAdjustMarksProc: CoreServices.OSLAdjustMarksUPP!, _ myGetErrDescProcPtr: CoreServices.OSLGetErrDescUPP!) -> OSErr ``` |

Modified [AESizeOfAttribute(_: UnsafePointer<AppleEvent>!, _: AEKeyword, _: UnsafeMutablePointer<DescType>!, _: UnsafeMutablePointer<Size>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1445764-aesizeofattribute)

|  | Declaration |
| --- | --- |
| From | ``` func AESizeOfAttribute(_ theAppleEvent: UnsafePointer<AppleEvent>, _ theAEKeyword: AEKeyword, _ typeCode: UnsafeMutablePointer<DescType>, _ dataSize: UnsafeMutablePointer<Size>) -> OSErr ``` |
| To | ``` func AESizeOfAttribute(_ theAppleEvent: UnsafePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ typeCode: UnsafeMutablePointer<DescType>!, _ dataSize: UnsafeMutablePointer<Size>!) -> OSErr ``` |

Modified [AESizeOfFlattenedDesc(_: UnsafePointer<AEDesc>!) -> Size](https://developer.apple.com/documentation/coreservices/1447305-aesizeofflatteneddesc)

|  | Declaration |
| --- | --- |
| From | ``` func AESizeOfFlattenedDesc(_ theAEDesc: UnsafePointer<AEDesc>) -> Size ``` |
| To | ``` func AESizeOfFlattenedDesc(_ theAEDesc: UnsafePointer<AEDesc>!) -> Size ``` |

Modified [AESizeOfNthItem(_: UnsafePointer<AEDescList>!, _: Int, _: UnsafeMutablePointer<DescType>!, _: UnsafeMutablePointer<Size>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1447307-aesizeofnthitem)

|  | Declaration |
| --- | --- |
| From | ``` func AESizeOfNthItem(_ theAEDescList: UnsafePointer<AEDescList>, _ index: Int, _ typeCode: UnsafeMutablePointer<DescType>, _ dataSize: UnsafeMutablePointer<Size>) -> OSErr ``` |
| To | ``` func AESizeOfNthItem(_ theAEDescList: UnsafePointer<AEDescList>!, _ index: Int, _ typeCode: UnsafeMutablePointer<DescType>!, _ dataSize: UnsafeMutablePointer<Size>!) -> OSErr ``` |

Modified [AESizeOfParam(_: UnsafePointer<AppleEvent>!, _: AEKeyword, _: UnsafeMutablePointer<DescType>!, _: UnsafeMutablePointer<Size>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1449998-aesizeofparam)

|  | Declaration |
| --- | --- |
| From | ``` func AESizeOfParam(_ theAppleEvent: UnsafePointer<AppleEvent>, _ theAEKeyword: AEKeyword, _ typeCode: UnsafeMutablePointer<DescType>, _ dataSize: UnsafeMutablePointer<Size>) -> OSErr ``` |
| To | ``` func AESizeOfParam(_ theAppleEvent: UnsafePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ typeCode: UnsafeMutablePointer<DescType>!, _ dataSize: UnsafeMutablePointer<Size>!) -> OSErr ``` |

Modified [AEStreamClose(_: AEStreamRef!, _: UnsafeMutablePointer<AEDesc>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1449821-aestreamclose)

|  | Declaration |
| --- | --- |
| From | ``` func AEStreamClose(_ ref: AEStreamRef, _ desc: UnsafeMutablePointer<AEDesc>) -> OSStatus ``` |
| To | ``` func AEStreamClose(_ ref: AEStreamRef!, _ desc: UnsafeMutablePointer<AEDesc>!) -> OSStatus ``` |

Modified [AEStreamCloseDesc(_: AEStreamRef!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1449272-aestreamclosedesc)

|  | Declaration |
| --- | --- |
| From | ``` func AEStreamCloseDesc(_ ref: AEStreamRef) -> OSStatus ``` |
| To | ``` func AEStreamCloseDesc(_ ref: AEStreamRef!) -> OSStatus ``` |

Modified [AEStreamCloseList(_: AEStreamRef!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1448185-aestreamcloselist)

|  | Declaration |
| --- | --- |
| From | ``` func AEStreamCloseList(_ ref: AEStreamRef) -> OSStatus ``` |
| To | ``` func AEStreamCloseList(_ ref: AEStreamRef!) -> OSStatus ``` |

Modified [AEStreamCloseRecord(_: AEStreamRef!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1449522-aestreamcloserecord)

|  | Declaration |
| --- | --- |
| From | ``` func AEStreamCloseRecord(_ ref: AEStreamRef) -> OSStatus ``` |
| To | ``` func AEStreamCloseRecord(_ ref: AEStreamRef!) -> OSStatus ``` |

Modified [AEStreamCreateEvent(_: AEEventClass, _: AEEventID, _: DescType, _: UnsafeRawPointer!, _: Size, _: Int16, _: Int32) -> AEStreamRef!](https://developer.apple.com/documentation/coreservices/1446562-aestreamcreateevent)

|  | Declaration |
| --- | --- |
| From | ``` func AEStreamCreateEvent(_ clazz: AEEventClass, _ id: AEEventID, _ targetType: DescType, _ targetData: UnsafePointer<Void>, _ targetLength: Size, _ returnID: Int16, _ transactionID: Int32) -> AEStreamRef ``` |
| To | ``` func AEStreamCreateEvent(_ clazz: AEEventClass, _ id: AEEventID, _ targetType: DescType, _ targetData: UnsafeRawPointer!, _ targetLength: Size, _ returnID: Int16, _ transactionID: Int32) -> AEStreamRef! ``` |

Modified [AEStreamOpen() -> AEStreamRef!](https://developer.apple.com/documentation/coreservices/1447732-aestreamopen)

|  | Declaration |
| --- | --- |
| From | ``` func AEStreamOpen() -> AEStreamRef ``` |
| To | ``` func AEStreamOpen() -> AEStreamRef! ``` |

Modified [AEStreamOpenDesc(_: AEStreamRef!, _: DescType) -> OSStatus](https://developer.apple.com/documentation/coreservices/1446544-aestreamopendesc)

|  | Declaration |
| --- | --- |
| From | ``` func AEStreamOpenDesc(_ ref: AEStreamRef, _ newType: DescType) -> OSStatus ``` |
| To | ``` func AEStreamOpenDesc(_ ref: AEStreamRef!, _ newType: DescType) -> OSStatus ``` |

Modified [AEStreamOpenEvent(_: UnsafeMutablePointer<AppleEvent>!) -> AEStreamRef!](https://developer.apple.com/documentation/coreservices/1445366-aestreamopenevent)

|  | Declaration |
| --- | --- |
| From | ``` func AEStreamOpenEvent(_ event: UnsafeMutablePointer<AppleEvent>) -> AEStreamRef ``` |
| To | ``` func AEStreamOpenEvent(_ event: UnsafeMutablePointer<AppleEvent>!) -> AEStreamRef! ``` |

Modified [AEStreamOpenKeyDesc(_: AEStreamRef!, _: AEKeyword, _: DescType) -> OSStatus](https://developer.apple.com/documentation/coreservices/1442897-aestreamopenkeydesc)

|  | Declaration |
| --- | --- |
| From | ``` func AEStreamOpenKeyDesc(_ ref: AEStreamRef, _ key: AEKeyword, _ newType: DescType) -> OSStatus ``` |
| To | ``` func AEStreamOpenKeyDesc(_ ref: AEStreamRef!, _ key: AEKeyword, _ newType: DescType) -> OSStatus ``` |

Modified [AEStreamOpenList(_: AEStreamRef!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1448594-aestreamopenlist)

|  | Declaration |
| --- | --- |
| From | ``` func AEStreamOpenList(_ ref: AEStreamRef) -> OSStatus ``` |
| To | ``` func AEStreamOpenList(_ ref: AEStreamRef!) -> OSStatus ``` |

Modified [AEStreamOpenRecord(_: AEStreamRef!, _: DescType) -> OSStatus](https://developer.apple.com/documentation/coreservices/1447141-aestreamopenrecord)

|  | Declaration |
| --- | --- |
| From | ``` func AEStreamOpenRecord(_ ref: AEStreamRef, _ newType: DescType) -> OSStatus ``` |
| To | ``` func AEStreamOpenRecord(_ ref: AEStreamRef!, _ newType: DescType) -> OSStatus ``` |

Modified [AEStreamOptionalParam(_: AEStreamRef!, _: AEKeyword) -> OSStatus](https://developer.apple.com/documentation/coreservices/1444481-aestreamoptionalparam)

|  | Declaration |
| --- | --- |
| From | ``` func AEStreamOptionalParam(_ ref: AEStreamRef, _ key: AEKeyword) -> OSStatus ``` |
| To | ``` func AEStreamOptionalParam(_ ref: AEStreamRef!, _ key: AEKeyword) -> OSStatus ``` |

Modified [AEStreamRef](https://developer.apple.com/documentation/coreservices/aestreamref)

|  | Declaration |
| --- | --- |
| From | ``` typealias AEStreamRef = COpaquePointer ``` |
| To | ``` typealias AEStreamRef = OpaquePointer ``` |

Modified [AEStreamSetRecordType(_: AEStreamRef!, _: DescType) -> OSStatus](https://developer.apple.com/documentation/coreservices/1447704-aestreamsetrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` func AEStreamSetRecordType(_ ref: AEStreamRef, _ newType: DescType) -> OSStatus ``` |
| To | ``` func AEStreamSetRecordType(_ ref: AEStreamRef!, _ newType: DescType) -> OSStatus ``` |

Modified [AEStreamWriteAEDesc(_: AEStreamRef!, _: UnsafePointer<AEDesc>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1448487-aestreamwriteaedesc)

|  | Declaration |
| --- | --- |
| From | ``` func AEStreamWriteAEDesc(_ ref: AEStreamRef, _ desc: UnsafePointer<AEDesc>) -> OSStatus ``` |
| To | ``` func AEStreamWriteAEDesc(_ ref: AEStreamRef!, _ desc: UnsafePointer<AEDesc>!) -> OSStatus ``` |

Modified [AEStreamWriteData(_: AEStreamRef!, _: UnsafeRawPointer!, _: Size) -> OSStatus](https://developer.apple.com/documentation/coreservices/1442610-aestreamwritedata)

|  | Declaration |
| --- | --- |
| From | ``` func AEStreamWriteData(_ ref: AEStreamRef, _ data: UnsafePointer<Void>, _ length: Size) -> OSStatus ``` |
| To | ``` func AEStreamWriteData(_ ref: AEStreamRef!, _ data: UnsafeRawPointer!, _ length: Size) -> OSStatus ``` |

Modified [AEStreamWriteDesc(_: AEStreamRef!, _: DescType, _: UnsafeRawPointer!, _: Size) -> OSStatus](https://developer.apple.com/documentation/coreservices/1450387-aestreamwritedesc)

|  | Declaration |
| --- | --- |
| From | ``` func AEStreamWriteDesc(_ ref: AEStreamRef, _ newType: DescType, _ data: UnsafePointer<Void>, _ length: Size) -> OSStatus ``` |
| To | ``` func AEStreamWriteDesc(_ ref: AEStreamRef!, _ newType: DescType, _ data: UnsafeRawPointer!, _ length: Size) -> OSStatus ``` |

Modified [AEStreamWriteKey(_: AEStreamRef!, _: AEKeyword) -> OSStatus](https://developer.apple.com/documentation/coreservices/1448750-aestreamwritekey)

|  | Declaration |
| --- | --- |
| From | ``` func AEStreamWriteKey(_ ref: AEStreamRef, _ key: AEKeyword) -> OSStatus ``` |
| To | ``` func AEStreamWriteKey(_ ref: AEStreamRef!, _ key: AEKeyword) -> OSStatus ``` |

Modified [AEStreamWriteKeyDesc(_: AEStreamRef!, _: AEKeyword, _: DescType, _: UnsafeRawPointer!, _: Size) -> OSStatus](https://developer.apple.com/documentation/coreservices/1442568-aestreamwritekeydesc)

|  | Declaration |
| --- | --- |
| From | ``` func AEStreamWriteKeyDesc(_ ref: AEStreamRef, _ key: AEKeyword, _ newType: DescType, _ data: UnsafePointer<Void>, _ length: Size) -> OSStatus ``` |
| To | ``` func AEStreamWriteKeyDesc(_ ref: AEStreamRef!, _ key: AEKeyword, _ newType: DescType, _ data: UnsafeRawPointer!, _ length: Size) -> OSStatus ``` |

Modified [AEUnflattenDesc(_: UnsafeRawPointer!, _: UnsafeMutablePointer<AEDesc>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1448997-aeunflattendesc)

|  | Declaration |
| --- | --- |
| From | ``` func AEUnflattenDesc(_ buffer: UnsafePointer<Void>, _ result: UnsafeMutablePointer<AEDesc>) -> OSStatus ``` |
| To | ``` func AEUnflattenDesc(_ buffer: UnsafeRawPointer!, _ result: UnsafeMutablePointer<AEDesc>!) -> OSStatus ``` |

Modified [cADBAddress](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/cadbaddress)

|  | Declaration |
| --- | --- |
| From | ``` var cADBAddress: Int { get } ``` |
| To | ``` var cADBAddress: OSType { get } ``` |

Modified [cAddressSpec](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/caddressspec)

|  | Declaration |
| --- | --- |
| From | ``` var cAddressSpec: Int { get } ``` |
| To | ``` var cAddressSpec: OSType { get } ``` |

Modified [cAEList](https://developer.apple.com/documentation/coreservices/1556411-caelist/caelist)

|  | Declaration |
| --- | --- |
| From | ``` var cAEList: Int { get } ``` |
| To | ``` var cAEList: OSType { get } ``` |

Modified [cAppleTalkAddress](https://developer.apple.com/documentation/coreservices/cappletalkaddress)

|  | Declaration |
| --- | --- |
| From | ``` var cAppleTalkAddress: Int { get } ``` |
| To | ``` var cAppleTalkAddress: OSType { get } ``` |

Modified [cApplication](https://developer.apple.com/documentation/coreservices/1556411-caelist/capplication)

|  | Declaration |
| --- | --- |
| From | ``` var cApplication: Int { get } ``` |
| To | ``` var cApplication: OSType { get } ``` |

Modified [cArc](https://developer.apple.com/documentation/coreservices/carc)

|  | Declaration |
| --- | --- |
| From | ``` var cArc: Int { get } ``` |
| To | ``` var cArc: OSType { get } ``` |

Modified [cBoolean](https://developer.apple.com/documentation/coreservices/cboolean)

|  | Declaration |
| --- | --- |
| From | ``` var cBoolean: Int { get } ``` |
| To | ``` var cBoolean: OSType { get } ``` |

Modified [cBusAddress](https://developer.apple.com/documentation/coreservices/cbusaddress)

|  | Declaration |
| --- | --- |
| From | ``` var cBusAddress: Int { get } ``` |
| To | ``` var cBusAddress: OSType { get } ``` |

Modified [cCell](https://developer.apple.com/documentation/coreservices/1556411-caelist/ccell)

|  | Declaration |
| --- | --- |
| From | ``` var cCell: Int { get } ``` |
| To | ``` var cCell: OSType { get } ``` |

Modified [cChar](https://developer.apple.com/documentation/coreservices/cchar)

|  | Declaration |
| --- | --- |
| From | ``` var cChar: Int { get } ``` |
| To | ``` var cChar: OSType { get } ``` |

Modified [ccntTokenRecHandle](https://developer.apple.com/documentation/coreservices/ccnttokenrechandle)

|  | Declaration |
| --- | --- |
| From | ``` typealias ccntTokenRecHandle = UnsafeMutablePointer<ccntTokenRecPtr> ``` |
| To | ``` typealias ccntTokenRecHandle = UnsafeMutablePointer<ccntTokenRecPtr?> ``` |

Modified [cColorTable](https://developer.apple.com/documentation/coreservices/1556411-caelist/ccolortable)

|  | Declaration |
| --- | --- |
| From | ``` var cColorTable: Int { get } ``` |
| To | ``` var cColorTable: OSType { get } ``` |

Modified [cColumn](https://developer.apple.com/documentation/coreservices/1556411-caelist/ccolumn)

|  | Declaration |
| --- | --- |
| From | ``` var cColumn: Int { get } ``` |
| To | ``` var cColumn: OSType { get } ``` |

Modified [cDevSpec](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/cdevspec)

|  | Declaration |
| --- | --- |
| From | ``` var cDevSpec: Int { get } ``` |
| To | ``` var cDevSpec: OSType { get } ``` |

Modified [cDocument](https://developer.apple.com/documentation/coreservices/cdocument)

|  | Declaration |
| --- | --- |
| From | ``` var cDocument: Int { get } ``` |
| To | ``` var cDocument: OSType { get } ``` |

Modified [cDrawingArea](https://developer.apple.com/documentation/coreservices/1556411-caelist/cdrawingarea)

|  | Declaration |
| --- | --- |
| From | ``` var cDrawingArea: Int { get } ``` |
| To | ``` var cDrawingArea: OSType { get } ``` |

Modified [cEnumeration](https://developer.apple.com/documentation/coreservices/1556411-caelist/cenumeration)

|  | Declaration |
| --- | --- |
| From | ``` var cEnumeration: Int { get } ``` |
| To | ``` var cEnumeration: OSType { get } ``` |

Modified [cEthernetAddress](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/cethernetaddress)

|  | Declaration |
| --- | --- |
| From | ``` var cEthernetAddress: Int { get } ``` |
| To | ``` var cEthernetAddress: OSType { get } ``` |

Modified [cFile](https://developer.apple.com/documentation/coreservices/cfile)

|  | Declaration |
| --- | --- |
| From | ``` var cFile: Int { get } ``` |
| To | ``` var cFile: OSType { get } ``` |

Modified [cFireWireAddress](https://developer.apple.com/documentation/coreservices/cfirewireaddress)

|  | Declaration |
| --- | --- |
| From | ``` var cFireWireAddress: Int { get } ``` |
| To | ``` var cFireWireAddress: OSType { get } ``` |

Modified [cFixed](https://developer.apple.com/documentation/coreservices/cfixed)

|  | Declaration |
| --- | --- |
| From | ``` var cFixed: Int { get } ``` |
| To | ``` var cFixed: OSType { get } ``` |

Modified [cFixedPoint](https://developer.apple.com/documentation/coreservices/1556411-caelist/cfixedpoint)

|  | Declaration |
| --- | --- |
| From | ``` var cFixedPoint: Int { get } ``` |
| To | ``` var cFixedPoint: OSType { get } ``` |

Modified [cFixedRectangle](https://developer.apple.com/documentation/coreservices/1556411-caelist/cfixedrectangle)

|  | Declaration |
| --- | --- |
| From | ``` var cFixedRectangle: Int { get } ``` |
| To | ``` var cFixedRectangle: OSType { get } ``` |

Modified [cFTPItem](https://developer.apple.com/documentation/coreservices/1556375-curl/cftpitem)

|  | Declaration |
| --- | --- |
| From | ``` var cFTPItem: Int { get } ``` |
| To | ``` var cFTPItem: OSType { get } ``` |

Modified [cGraphicLine](https://developer.apple.com/documentation/coreservices/1556411-caelist/cgraphicline)

|  | Declaration |
| --- | --- |
| From | ``` var cGraphicLine: Int { get } ``` |
| To | ``` var cGraphicLine: OSType { get } ``` |

Modified [cGraphicObject](https://developer.apple.com/documentation/coreservices/cgraphicobject)

|  | Declaration |
| --- | --- |
| From | ``` var cGraphicObject: Int { get } ``` |
| To | ``` var cGraphicObject: OSType { get } ``` |

Modified [cGraphicShape](https://developer.apple.com/documentation/coreservices/1556411-caelist/cgraphicshape)

|  | Declaration |
| --- | --- |
| From | ``` var cGraphicShape: Int { get } ``` |
| To | ``` var cGraphicShape: OSType { get } ``` |

Modified [cGraphicText](https://developer.apple.com/documentation/coreservices/1556411-caelist/cgraphictext)

|  | Declaration |
| --- | --- |
| From | ``` var cGraphicText: Int { get } ``` |
| To | ``` var cGraphicText: OSType { get } ``` |

Modified [cGroupedGraphic](https://developer.apple.com/documentation/coreservices/1556411-caelist/cgroupedgraphic)

|  | Declaration |
| --- | --- |
| From | ``` var cGroupedGraphic: Int { get } ``` |
| To | ``` var cGroupedGraphic: OSType { get } ``` |

Modified [cHTML](https://developer.apple.com/documentation/coreservices/chtml)

|  | Declaration |
| --- | --- |
| From | ``` var cHTML: Int { get } ``` |
| To | ``` var cHTML: OSType { get } ``` |

Modified [cInsertionLoc](https://developer.apple.com/documentation/coreservices/1556389-cinsertionloc/cinsertionloc)

|  | Declaration |
| --- | --- |
| From | ``` var cInsertionLoc: Int { get } ``` |
| To | ``` var cInsertionLoc: OSType { get } ``` |

Modified [cInsertionPoint](https://developer.apple.com/documentation/coreservices/cinsertionpoint)

|  | Declaration |
| --- | --- |
| From | ``` var cInsertionPoint: Int { get } ``` |
| To | ``` var cInsertionPoint: OSType { get } ``` |

Modified [cInternetAddress](https://developer.apple.com/documentation/coreservices/1556375-curl/cinternetaddress)

|  | Declaration |
| --- | --- |
| From | ``` var cInternetAddress: Int { get } ``` |
| To | ``` var cInternetAddress: OSType { get } ``` |

Modified [cIntlText](https://developer.apple.com/documentation/coreservices/1556389-cinsertionloc/cintltext)

|  | Declaration |
| --- | --- |
| From | ``` var cIntlText: Int { get } ``` |
| To | ``` var cIntlText: OSType { get } ``` |

Modified [cIntlWritingCode](https://developer.apple.com/documentation/coreservices/1556389-cinsertionloc/cintlwritingcode)

|  | Declaration |
| --- | --- |
| From | ``` var cIntlWritingCode: Int { get } ``` |
| To | ``` var cIntlWritingCode: OSType { get } ``` |

Modified [cIPAddress](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/cipaddress)

|  | Declaration |
| --- | --- |
| From | ``` var cIPAddress: Int { get } ``` |
| To | ``` var cIPAddress: OSType { get } ``` |

Modified [cItem](https://developer.apple.com/documentation/coreservices/1556389-cinsertionloc/citem)

|  | Declaration |
| --- | --- |
| From | ``` var cItem: Int { get } ``` |
| To | ``` var cItem: OSType { get } ``` |

Modified [cKeystroke](https://developer.apple.com/documentation/coreservices/1556385-ckeystroke/ckeystroke)

|  | Declaration |
| --- | --- |
| From | ``` var cKeystroke: Int { get } ``` |
| To | ``` var cKeystroke: OSType { get } ``` |

Modified [cLine](https://developer.apple.com/documentation/coreservices/cline)

|  | Declaration |
| --- | --- |
| From | ``` var cLine: Int { get } ``` |
| To | ``` var cLine: OSType { get } ``` |

Modified [cLocalTalkAddress](https://developer.apple.com/documentation/coreservices/clocaltalkaddress)

|  | Declaration |
| --- | --- |
| From | ``` var cLocalTalkAddress: Int { get } ``` |
| To | ``` var cLocalTalkAddress: OSType { get } ``` |

Modified [cLongDateTime](https://developer.apple.com/documentation/coreservices/clongdatetime)

|  | Declaration |
| --- | --- |
| From | ``` var cLongDateTime: Int { get } ``` |
| To | ``` var cLongDateTime: OSType { get } ``` |

Modified [cLongFixed](https://developer.apple.com/documentation/coreservices/1556389-cinsertionloc/clongfixed)

|  | Declaration |
| --- | --- |
| From | ``` var cLongFixed: Int { get } ``` |
| To | ``` var cLongFixed: OSType { get } ``` |

Modified [cLongFixedPoint](https://developer.apple.com/documentation/coreservices/1556389-cinsertionloc/clongfixedpoint)

|  | Declaration |
| --- | --- |
| From | ``` var cLongFixedPoint: Int { get } ``` |
| To | ``` var cLongFixedPoint: OSType { get } ``` |

Modified [cLongFixedRectangle](https://developer.apple.com/documentation/coreservices/clongfixedrectangle)

|  | Declaration |
| --- | --- |
| From | ``` var cLongFixedRectangle: Int { get } ``` |
| To | ``` var cLongFixedRectangle: OSType { get } ``` |

Modified [cLongInteger](https://developer.apple.com/documentation/coreservices/1556389-cinsertionloc/clonginteger)

|  | Declaration |
| --- | --- |
| From | ``` var cLongInteger: Int { get } ``` |
| To | ``` var cLongInteger: OSType { get } ``` |

Modified [cLongPoint](https://developer.apple.com/documentation/coreservices/clongpoint)

|  | Declaration |
| --- | --- |
| From | ``` var cLongPoint: Int { get } ``` |
| To | ``` var cLongPoint: OSType { get } ``` |

Modified [cLongRectangle](https://developer.apple.com/documentation/coreservices/1556389-cinsertionloc/clongrectangle)

|  | Declaration |
| --- | --- |
| From | ``` var cLongRectangle: Int { get } ``` |
| To | ``` var cLongRectangle: OSType { get } ``` |

Modified [cMachineLoc](https://developer.apple.com/documentation/coreservices/cmachineloc)

|  | Declaration |
| --- | --- |
| From | ``` var cMachineLoc: Int { get } ``` |
| To | ``` var cMachineLoc: OSType { get } ``` |

Modified [cMenu](https://developer.apple.com/documentation/coreservices/1556389-cinsertionloc/cmenu)

|  | Declaration |
| --- | --- |
| From | ``` var cMenu: Int { get } ``` |
| To | ``` var cMenu: OSType { get } ``` |

Modified [cMenuItem](https://developer.apple.com/documentation/coreservices/1556389-cinsertionloc/cmenuitem)

|  | Declaration |
| --- | --- |
| From | ``` var cMenuItem: Int { get } ``` |
| To | ``` var cMenuItem: OSType { get } ``` |

Modified [cObject](https://developer.apple.com/documentation/coreservices/cobject)

|  | Declaration |
| --- | --- |
| From | ``` var cObject: Int { get } ``` |
| To | ``` var cObject: OSType { get } ``` |

Modified [cObjectSpecifier](https://developer.apple.com/documentation/coreservices/1556389-cinsertionloc/cobjectspecifier)

|  | Declaration |
| --- | --- |
| From | ``` var cObjectSpecifier: Int { get } ``` |
| To | ``` var cObjectSpecifier: OSType { get } ``` |

Modified [CollatorRef](https://developer.apple.com/documentation/coreservices/collatorref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CollatorRef = COpaquePointer ``` |
| To | ``` typealias CollatorRef = OpaquePointer ``` |

Modified [CompositeIconRef(_: IconRef!, _: IconRef!, _: UnsafeMutablePointer<IconRef?>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1450541-compositeiconref)

|  | Declaration |
| --- | --- |
| From | ``` func CompositeIconRef(_ backgroundIconRef: IconRef, _ foregroundIconRef: IconRef, _ compositeIconRef: UnsafeMutablePointer<IconRef>) -> OSErr ``` |
| To | ``` func CompositeIconRef(_ backgroundIconRef: IconRef!, _ foregroundIconRef: IconRef!, _ compositeIconRef: UnsafeMutablePointer<IconRef?>!) -> OSErr ``` |

Modified [ConstFSEventStreamRef](https://developer.apple.com/documentation/coreservices/constfseventstreamref)

|  | Declaration |
| --- | --- |
| From | ``` typealias ConstFSEventStreamRef = COpaquePointer ``` |
| To | ``` typealias ConstFSEventStreamRef = OpaquePointer ``` |

Modified [cOpenableObject](https://developer.apple.com/documentation/coreservices/copenableobject)

|  | Declaration |
| --- | --- |
| From | ``` var cOpenableObject: Int { get } ``` |
| To | ``` var cOpenableObject: OSType { get } ``` |

Modified [cOval](https://developer.apple.com/documentation/coreservices/1556389-cinsertionloc/coval)

|  | Declaration |
| --- | --- |
| From | ``` var cOval: Int { get } ``` |
| To | ``` var cOval: OSType { get } ``` |

Modified [cParagraph](https://developer.apple.com/documentation/coreservices/1556368-object_class_id_constants/cparagraph)

|  | Declaration |
| --- | --- |
| From | ``` var cParagraph: Int { get } ``` |
| To | ``` var cParagraph: OSType { get } ``` |

Modified [cPICT](https://developer.apple.com/documentation/coreservices/1556368-object_class_id_constants/cpict)

|  | Declaration |
| --- | --- |
| From | ``` var cPICT: Int { get } ``` |
| To | ``` var cPICT: OSType { get } ``` |

Modified [cPixel](https://developer.apple.com/documentation/coreservices/cpixel)

|  | Declaration |
| --- | --- |
| From | ``` var cPixel: Int { get } ``` |
| To | ``` var cPixel: OSType { get } ``` |

Modified [cPixelMap](https://developer.apple.com/documentation/coreservices/1556368-object_class_id_constants/cpixelmap)

|  | Declaration |
| --- | --- |
| From | ``` var cPixelMap: Int { get } ``` |
| To | ``` var cPixelMap: OSType { get } ``` |

Modified [cPolygon](https://developer.apple.com/documentation/coreservices/1556368-object_class_id_constants/cpolygon)

|  | Declaration |
| --- | --- |
| From | ``` var cPolygon: Int { get } ``` |
| To | ``` var cPolygon: OSType { get } ``` |

Modified [cProperty](https://developer.apple.com/documentation/coreservices/1556368-object_class_id_constants/cproperty)

|  | Declaration |
| --- | --- |
| From | ``` var cProperty: Int { get } ``` |
| To | ``` var cProperty: OSType { get } ``` |

Modified [cQDPoint](https://developer.apple.com/documentation/coreservices/cqdpoint)

|  | Declaration |
| --- | --- |
| From | ``` var cQDPoint: Int { get } ``` |
| To | ``` var cQDPoint: OSType { get } ``` |

Modified [cQDRectangle](https://developer.apple.com/documentation/coreservices/1556368-object_class_id_constants/cqdrectangle)

|  | Declaration |
| --- | --- |
| From | ``` var cQDRectangle: Int { get } ``` |
| To | ``` var cQDRectangle: OSType { get } ``` |

Modified [CreateCompDescriptor(_: DescType, _: UnsafeMutablePointer<AEDesc>!, _: UnsafeMutablePointer<AEDesc>!, _: Bool, _: UnsafeMutablePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1449155-createcompdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` func CreateCompDescriptor(_ comparisonOperator: DescType, _ operand1: UnsafeMutablePointer<AEDesc>, _ operand2: UnsafeMutablePointer<AEDesc>, _ disposeInputs: Bool, _ theDescriptor: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func CreateCompDescriptor(_ comparisonOperator: DescType, _ operand1: UnsafeMutablePointer<AEDesc>!, _ operand2: UnsafeMutablePointer<AEDesc>!, _ disposeInputs: Bool, _ theDescriptor: UnsafeMutablePointer<AEDesc>!) -> OSErr ``` |

Modified [CreateLogicalDescriptor(_: UnsafeMutablePointer<AEDescList>!, _: DescType, _: Bool, _: UnsafeMutablePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1445212-createlogicaldescriptor)

|  | Declaration |
| --- | --- |
| From | ``` func CreateLogicalDescriptor(_ theLogicalTerms: UnsafeMutablePointer<AEDescList>, _ theLogicOperator: DescType, _ disposeInputs: Bool, _ theDescriptor: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func CreateLogicalDescriptor(_ theLogicalTerms: UnsafeMutablePointer<AEDescList>!, _ theLogicOperator: DescType, _ disposeInputs: Bool, _ theDescriptor: UnsafeMutablePointer<AEDesc>!) -> OSErr ``` |

Modified [CreateObjSpecifier(_: DescType, _: UnsafeMutablePointer<AEDesc>!, _: DescType, _: UnsafeMutablePointer<AEDesc>!, _: Bool, _: UnsafeMutablePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1450244-createobjspecifier)

|  | Declaration |
| --- | --- |
| From | ``` func CreateObjSpecifier(_ desiredClass: DescType, _ theContainer: UnsafeMutablePointer<AEDesc>, _ keyForm: DescType, _ keyData: UnsafeMutablePointer<AEDesc>, _ disposeInputs: Bool, _ objSpecifier: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func CreateObjSpecifier(_ desiredClass: DescType, _ theContainer: UnsafeMutablePointer<AEDesc>!, _ keyForm: DescType, _ keyData: UnsafeMutablePointer<AEDesc>!, _ disposeInputs: Bool, _ objSpecifier: UnsafeMutablePointer<AEDesc>!) -> OSErr ``` |

Modified [CreateOffsetDescriptor(_: Int, _: UnsafeMutablePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1444957-createoffsetdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` func CreateOffsetDescriptor(_ theOffset: Int, _ theDescriptor: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func CreateOffsetDescriptor(_ theOffset: Int, _ theDescriptor: UnsafeMutablePointer<AEDesc>!) -> OSErr ``` |

Modified [CreateRangeDescriptor(_: UnsafeMutablePointer<AEDesc>!, _: UnsafeMutablePointer<AEDesc>!, _: Bool, _: UnsafeMutablePointer<AEDesc>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1444087-createrangedescriptor)

|  | Declaration |
| --- | --- |
| From | ``` func CreateRangeDescriptor(_ rangeStart: UnsafeMutablePointer<AEDesc>, _ rangeStop: UnsafeMutablePointer<AEDesc>, _ disposeInputs: Bool, _ theDescriptor: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func CreateRangeDescriptor(_ rangeStart: UnsafeMutablePointer<AEDesc>!, _ rangeStop: UnsafeMutablePointer<AEDesc>!, _ disposeInputs: Bool, _ theDescriptor: UnsafeMutablePointer<AEDesc>!) -> OSErr ``` |

Modified [cRectangle](https://developer.apple.com/documentation/coreservices/1556368-object_class_id_constants/crectangle)

|  | Declaration |
| --- | --- |
| From | ``` var cRectangle: Int { get } ``` |
| To | ``` var cRectangle: OSType { get } ``` |

Modified [cRGBColor](https://developer.apple.com/documentation/coreservices/crgbcolor)

|  | Declaration |
| --- | --- |
| From | ``` var cRGBColor: Int { get } ``` |
| To | ``` var cRGBColor: OSType { get } ``` |

Modified [cRotation](https://developer.apple.com/documentation/coreservices/crotation)

|  | Declaration |
| --- | --- |
| From | ``` var cRotation: Int { get } ``` |
| To | ``` var cRotation: OSType { get } ``` |

Modified [cRoundedRectangle](https://developer.apple.com/documentation/coreservices/1556368-object_class_id_constants/croundedrectangle)

|  | Declaration |
| --- | --- |
| From | ``` var cRoundedRectangle: Int { get } ``` |
| To | ``` var cRoundedRectangle: OSType { get } ``` |

Modified [cRow](https://developer.apple.com/documentation/coreservices/1556368-object_class_id_constants/crow)

|  | Declaration |
| --- | --- |
| From | ``` var cRow: Int { get } ``` |
| To | ``` var cRow: OSType { get } ``` |

Modified [CSBackupIsItemExcluded(_: CFURL!, _: UnsafeMutablePointer<DarwinBoolean>!) -> Bool](https://developer.apple.com/documentation/coreservices/1443602-csbackupisitemexcluded)

|  | Declaration |
| --- | --- |
| From | ``` func CSBackupIsItemExcluded(_ item: CFURL!, _ excludeByPath: UnsafeMutablePointer<DarwinBoolean>) -> Bool ``` |
| To | ``` func CSBackupIsItemExcluded(_ item: CFURL!, _ excludeByPath: UnsafeMutablePointer<DarwinBoolean>!) -> Bool ``` |

Modified [cSCSIAddress](https://developer.apple.com/documentation/coreservices/cscsiaddress)

|  | Declaration |
| --- | --- |
| From | ``` var cSCSIAddress: Int { get } ``` |
| To | ``` var cSCSIAddress: OSType { get } ``` |

Modified [CSDiskSpaceRecoveryCallback](https://developer.apple.com/documentation/coreservices/csdiskspacerecoverycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CSDiskSpaceRecoveryCallback = (Bool, UInt64, CFError!) -> Void ``` |
| To | ``` typealias CSDiskSpaceRecoveryCallback = (Bool, UInt64, CFError?) -> Swift.Void ``` |

Modified [CSDiskSpaceStartRecovery(_: CFURL!, _: UInt64, _: CSDiskSpaceRecoveryOptions, _: UnsafeMutablePointer<Unmanaged<CFUUID>?>!, _: DispatchQueue!, _: CoreServices.CSDiskSpaceRecoveryCallback!)](https://developer.apple.com/documentation/coreservices/1447968-csdiskspacestartrecovery)

|  | Declaration |
| --- | --- |
| From | ``` func CSDiskSpaceStartRecovery(_ volumeURL: CFURL!, _ bytesNeeded: UInt64, _ options: CSDiskSpaceRecoveryOptions, _ outOperationUUID: UnsafeMutablePointer<Unmanaged<CFUUID>?>, _ callbackQueue: dispatch_queue_t!, _ callback: CSDiskSpaceRecoveryCallback!) ``` |
| To | ``` func CSDiskSpaceStartRecovery(_ volumeURL: CFURL!, _ bytesNeeded: UInt64, _ options: CSDiskSpaceRecoveryOptions, _ outOperationUUID: UnsafeMutablePointer<Unmanaged<CFUUID>?>!, _ callbackQueue: DispatchQueue!, _ callback: CoreServices.CSDiskSpaceRecoveryCallback!) ``` |

Modified [cSelection](https://developer.apple.com/documentation/coreservices/cselection)

|  | Declaration |
| --- | --- |
| From | ``` var cSelection: Int { get } ``` |
| To | ``` var cSelection: OSType { get } ``` |

Modified [cShortInteger](https://developer.apple.com/documentation/coreservices/cshortinteger)

|  | Declaration |
| --- | --- |
| From | ``` var cShortInteger: Int { get } ``` |
| To | ``` var cShortInteger: OSType { get } ``` |

Modified [CSIdentityCommit(_: CSIdentity!, _: AuthorizationRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/coreservices/1449575-csidentitycommit)

|  | Declaration |
| --- | --- |
| From | ``` func CSIdentityCommit(_ identity: CSIdentity!, _ authorization: AuthorizationRef, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CSIdentityCommit(_ identity: CSIdentity!, _ authorization: AuthorizationRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [CSIdentityCommitAsynchronously(_: CSIdentity!, _: UnsafePointer<CSIdentityClientContext>!, _: CFRunLoop!, _: CFString!, _: AuthorizationRef!) -> Bool](https://developer.apple.com/documentation/coreservices/1447936-csidentitycommitasynchronously)

|  | Declaration |
| --- | --- |
| From | ``` func CSIdentityCommitAsynchronously(_ identity: CSIdentity!, _ clientContext: UnsafePointer<CSIdentityClientContext>, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!, _ authorization: AuthorizationRef) -> Bool ``` |
| To | ``` func CSIdentityCommitAsynchronously(_ identity: CSIdentity!, _ clientContext: UnsafePointer<CSIdentityClientContext>!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!, _ authorization: AuthorizationRef!) -> Bool ``` |

Modified [CSIdentityQueryExecute(_: CSIdentityQuery!, _: CSIdentityQueryFlags, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/coreservices/1429041-csidentityqueryexecute)

|  | Declaration |
| --- | --- |
| From | ``` func CSIdentityQueryExecute(_ query: CSIdentityQuery!, _ flags: CSIdentityQueryFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CSIdentityQueryExecute(_ query: CSIdentityQuery!, _ flags: CSIdentityQueryFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [CSIdentityQueryExecuteAsynchronously(_: CSIdentityQuery!, _: CSIdentityQueryFlags, _: UnsafePointer<CSIdentityQueryClientContext>!, _: CFRunLoop!, _: CFString!) -> Bool](https://developer.apple.com/documentation/coreservices/1429011-csidentityqueryexecuteasynchrono)

|  | Declaration |
| --- | --- |
| From | ``` func CSIdentityQueryExecuteAsynchronously(_ query: CSIdentityQuery!, _ flags: CSIdentityQueryFlags, _ clientContext: UnsafePointer<CSIdentityQueryClientContext>, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) -> Bool ``` |
| To | ``` func CSIdentityQueryExecuteAsynchronously(_ query: CSIdentityQuery!, _ flags: CSIdentityQueryFlags, _ clientContext: UnsafePointer<CSIdentityQueryClientContext>!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) -> Bool ``` |

Modified [CSIdentityQueryReceiveEventCallback](https://developer.apple.com/documentation/coreservices/csidentityqueryreceiveeventcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CSIdentityQueryReceiveEventCallback = (CSIdentityQuery!, CSIdentityQueryEvent, CFArray!, CFError!, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CSIdentityQueryReceiveEventCallback = (CSIdentityQuery?, CSIdentityQueryEvent, CFArray?, CFError?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CSIdentityStatusUpdatedCallback](https://developer.apple.com/documentation/coreservices/csidentitystatusupdatedcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CSIdentityStatusUpdatedCallback = (CSIdentity!, CFIndex, CFError!, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CSIdentityStatusUpdatedCallback = (CSIdentity?, CFIndex, CFError?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [cTable](https://developer.apple.com/documentation/coreservices/ctable)

|  | Declaration |
| --- | --- |
| From | ``` var cTable: Int { get } ``` |
| To | ``` var cTable: OSType { get } ``` |

Modified [cText](https://developer.apple.com/documentation/coreservices/1556368-object_class_id_constants/ctext)

|  | Declaration |
| --- | --- |
| From | ``` var cText: Int { get } ``` |
| To | ``` var cText: OSType { get } ``` |

Modified [cTextFlow](https://developer.apple.com/documentation/coreservices/ctextflow)

|  | Declaration |
| --- | --- |
| From | ``` var cTextFlow: Int { get } ``` |
| To | ``` var cTextFlow: OSType { get } ``` |

Modified [cTextStyles](https://developer.apple.com/documentation/coreservices/1556368-object_class_id_constants/ctextstyles)

|  | Declaration |
| --- | --- |
| From | ``` var cTextStyles: Int { get } ``` |
| To | ``` var cTextStyles: OSType { get } ``` |

Modified [cTokenRingAddress](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/ctokenringaddress)

|  | Declaration |
| --- | --- |
| From | ``` var cTokenRingAddress: Int { get } ``` |
| To | ``` var cTokenRingAddress: OSType { get } ``` |

Modified [cType](https://developer.apple.com/documentation/coreservices/1556368-object_class_id_constants/ctype)

|  | Declaration |
| --- | --- |
| From | ``` var cType: Int { get } ``` |
| To | ``` var cType: OSType { get } ``` |

Modified [cURL](https://developer.apple.com/documentation/coreservices/curl)

|  | Declaration |
| --- | --- |
| From | ``` var cURL: Int { get } ``` |
| To | ``` var cURL: OSType { get } ``` |

Modified [cUSBAddress](https://developer.apple.com/documentation/coreservices/cusbaddress)

|  | Declaration |
| --- | --- |
| From | ``` var cUSBAddress: Int { get } ``` |
| To | ``` var cUSBAddress: OSType { get } ``` |

Modified [cVersion](https://developer.apple.com/documentation/coreservices/cversion)

|  | Declaration |
| --- | --- |
| From | ``` var cVersion: Int { get } ``` |
| To | ``` var cVersion: OSType { get } ``` |

Modified [cWindow](https://developer.apple.com/documentation/coreservices/1556364-anonymous/cwindow)

|  | Declaration |
| --- | --- |
| From | ``` var cWindow: Int { get } ``` |
| To | ``` var cWindow: OSType { get } ``` |

Modified [cWord](https://developer.apple.com/documentation/coreservices/cword)

|  | Declaration |
| --- | --- |
| From | ``` var cWord: Int { get } ``` |
| To | ``` var cWord: OSType { get } ``` |

Modified [DisposeAECoerceDescUPP(_: CoreServices.AECoerceDescUPP!)](https://developer.apple.com/documentation/coreservices/1448721-disposeaecoercedescupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeAECoerceDescUPP(_ userUPP: AECoerceDescUPP!) ``` |
| To | ``` func DisposeAECoerceDescUPP(_ userUPP: CoreServices.AECoerceDescUPP!) ``` |

Modified [DisposeAECoercePtrUPP(_: CoreServices.AECoercePtrUPP!)](https://developer.apple.com/documentation/coreservices/1450664-disposeaecoerceptrupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeAECoercePtrUPP(_ userUPP: AECoercePtrUPP!) ``` |
| To | ``` func DisposeAECoercePtrUPP(_ userUPP: CoreServices.AECoercePtrUPP!) ``` |

Modified [DisposeAEDisposeExternalUPP(_: CoreServices.AEDisposeExternalUPP!)](https://developer.apple.com/documentation/coreservices/1447284-disposeaedisposeexternalupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeAEDisposeExternalUPP(_ userUPP: AEDisposeExternalUPP!) ``` |
| To | ``` func DisposeAEDisposeExternalUPP(_ userUPP: CoreServices.AEDisposeExternalUPP!) ``` |

Modified [DisposeAEEventHandlerUPP(_: CoreServices.AEEventHandlerUPP!)](https://developer.apple.com/documentation/coreservices/1442066-disposeaeeventhandlerupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeAEEventHandlerUPP(_ userUPP: AEEventHandlerUPP!) ``` |
| To | ``` func DisposeAEEventHandlerUPP(_ userUPP: CoreServices.AEEventHandlerUPP!) ``` |

Modified [DisposeIndexToUCStringUPP(_: CoreServices.IndexToUCStringUPP!)](https://developer.apple.com/documentation/coreservices/1390390-disposeindextoucstringupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeIndexToUCStringUPP(_ userUPP: IndexToUCStringUPP!) ``` |
| To | ``` func DisposeIndexToUCStringUPP(_ userUPP: CoreServices.IndexToUCStringUPP!) ``` |

Modified [DisposeOSLAccessorUPP(_: CoreServices.OSLAccessorUPP!)](https://developer.apple.com/documentation/coreservices/1444684-disposeoslaccessorupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeOSLAccessorUPP(_ userUPP: OSLAccessorUPP!) ``` |
| To | ``` func DisposeOSLAccessorUPP(_ userUPP: CoreServices.OSLAccessorUPP!) ``` |

Modified [DisposeOSLAdjustMarksUPP(_: CoreServices.OSLAdjustMarksUPP!)](https://developer.apple.com/documentation/coreservices/1443940-disposeosladjustmarksupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeOSLAdjustMarksUPP(_ userUPP: OSLAdjustMarksUPP!) ``` |
| To | ``` func DisposeOSLAdjustMarksUPP(_ userUPP: CoreServices.OSLAdjustMarksUPP!) ``` |

Modified [DisposeOSLCompareUPP(_: CoreServices.OSLCompareUPP!)](https://developer.apple.com/documentation/coreservices/1448398-disposeoslcompareupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeOSLCompareUPP(_ userUPP: OSLCompareUPP!) ``` |
| To | ``` func DisposeOSLCompareUPP(_ userUPP: CoreServices.OSLCompareUPP!) ``` |

Modified [DisposeOSLCountUPP(_: CoreServices.OSLCountUPP!)](https://developer.apple.com/documentation/coreservices/1443984-disposeoslcountupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeOSLCountUPP(_ userUPP: OSLCountUPP!) ``` |
| To | ``` func DisposeOSLCountUPP(_ userUPP: CoreServices.OSLCountUPP!) ``` |

Modified [DisposeOSLDisposeTokenUPP(_: CoreServices.OSLDisposeTokenUPP!)](https://developer.apple.com/documentation/coreservices/1442670-disposeosldisposetokenupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeOSLDisposeTokenUPP(_ userUPP: OSLDisposeTokenUPP!) ``` |
| To | ``` func DisposeOSLDisposeTokenUPP(_ userUPP: CoreServices.OSLDisposeTokenUPP!) ``` |

Modified [DisposeOSLGetErrDescUPP(_: CoreServices.OSLGetErrDescUPP!)](https://developer.apple.com/documentation/coreservices/1446061-disposeoslgeterrdescupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeOSLGetErrDescUPP(_ userUPP: OSLGetErrDescUPP!) ``` |
| To | ``` func DisposeOSLGetErrDescUPP(_ userUPP: CoreServices.OSLGetErrDescUPP!) ``` |

Modified [DisposeOSLGetMarkTokenUPP(_: CoreServices.OSLGetMarkTokenUPP!)](https://developer.apple.com/documentation/coreservices/1442377-disposeoslgetmarktokenupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeOSLGetMarkTokenUPP(_ userUPP: OSLGetMarkTokenUPP!) ``` |
| To | ``` func DisposeOSLGetMarkTokenUPP(_ userUPP: CoreServices.OSLGetMarkTokenUPP!) ``` |

Modified [DisposeOSLMarkUPP(_: CoreServices.OSLMarkUPP!)](https://developer.apple.com/documentation/coreservices/1449253-disposeoslmarkupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeOSLMarkUPP(_ userUPP: OSLMarkUPP!) ``` |
| To | ``` func DisposeOSLMarkUPP(_ userUPP: CoreServices.OSLMarkUPP!) ``` |

Modified [eADB](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/eadb)

|  | Declaration |
| --- | --- |
| From | ``` var eADB: Int { get } ``` |
| To | ``` var eADB: OSType { get } ``` |

Modified [eAddressSpec](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/eaddressspec)

|  | Declaration |
| --- | --- |
| From | ``` var eAddressSpec: Int { get } ``` |
| To | ``` var eAddressSpec: OSType { get } ``` |

Modified [eAnalogAudio](https://developer.apple.com/documentation/coreservices/eanalogaudio)

|  | Declaration |
| --- | --- |
| From | ``` var eAnalogAudio: Int { get } ``` |
| To | ``` var eAnalogAudio: OSType { get } ``` |

Modified [eAppleTalk](https://developer.apple.com/documentation/coreservices/eappletalk)

|  | Declaration |
| --- | --- |
| From | ``` var eAppleTalk: Int { get } ``` |
| To | ``` var eAppleTalk: OSType { get } ``` |

Modified [eAudioLineIn](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/eaudiolinein)

|  | Declaration |
| --- | --- |
| From | ``` var eAudioLineIn: Int { get } ``` |
| To | ``` var eAudioLineIn: OSType { get } ``` |

Modified [eAudioLineOut](https://developer.apple.com/documentation/coreservices/eaudiolineout)

|  | Declaration |
| --- | --- |
| From | ``` var eAudioLineOut: Int { get } ``` |
| To | ``` var eAudioLineOut: OSType { get } ``` |

Modified [eAudioOut](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/eaudioout)

|  | Declaration |
| --- | --- |
| From | ``` var eAudioOut: Int { get } ``` |
| To | ``` var eAudioOut: OSType { get } ``` |

Modified [eBus](https://developer.apple.com/documentation/coreservices/ebus)

|  | Declaration |
| --- | --- |
| From | ``` var eBus: Int { get } ``` |
| To | ``` var eBus: OSType { get } ``` |

Modified [eCapsLockDown](https://developer.apple.com/documentation/coreservices/1556385-ckeystroke/ecapslockdown)

|  | Declaration |
| --- | --- |
| From | ``` var eCapsLockDown: Int { get } ``` |
| To | ``` var eCapsLockDown: OSType { get } ``` |

Modified [eCDROM](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/ecdrom)

|  | Declaration |
| --- | --- |
| From | ``` var eCDROM: Int { get } ``` |
| To | ``` var eCDROM: OSType { get } ``` |

Modified [eClearKey](https://developer.apple.com/documentation/coreservices/1556385-ckeystroke/eclearkey)

|  | Declaration |
| --- | --- |
| From | ``` var eClearKey: Int { get } ``` |
| To | ``` var eClearKey: OSType { get } ``` |

Modified [eCommandDown](https://developer.apple.com/documentation/coreservices/1556385-ckeystroke/ecommanddown)

|  | Declaration |
| --- | --- |
| From | ``` var eCommandDown: Int { get } ``` |
| To | ``` var eCommandDown: OSType { get } ``` |

Modified [eCommSlot](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/ecommslot)

|  | Declaration |
| --- | --- |
| From | ``` var eCommSlot: Int { get } ``` |
| To | ``` var eCommSlot: OSType { get } ``` |

Modified [eConduit](https://developer.apple.com/documentation/coreservices/econduit)

|  | Declaration |
| --- | --- |
| From | ``` var eConduit: Int { get } ``` |
| To | ``` var eConduit: OSType { get } ``` |

Modified [eControlDown](https://developer.apple.com/documentation/coreservices/econtroldown)

|  | Declaration |
| --- | --- |
| From | ``` var eControlDown: Int { get } ``` |
| To | ``` var eControlDown: OSType { get } ``` |

Modified [eDeleteKey](https://developer.apple.com/documentation/coreservices/1556385-ckeystroke/edeletekey)

|  | Declaration |
| --- | --- |
| From | ``` var eDeleteKey: Int { get } ``` |
| To | ``` var eDeleteKey: OSType { get } ``` |

Modified [eDeviceType](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/edevicetype)

|  | Declaration |
| --- | --- |
| From | ``` var eDeviceType: Int { get } ``` |
| To | ``` var eDeviceType: OSType { get } ``` |

Modified [eDigitalAudio](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/edigitalaudio)

|  | Declaration |
| --- | --- |
| From | ``` var eDigitalAudio: Int { get } ``` |
| To | ``` var eDigitalAudio: OSType { get } ``` |

Modified [eDisplay](https://developer.apple.com/documentation/coreservices/edisplay)

|  | Declaration |
| --- | --- |
| From | ``` var eDisplay: Int { get } ``` |
| To | ``` var eDisplay: OSType { get } ``` |

Modified [eDownArrowKey](https://developer.apple.com/documentation/coreservices/1556385-ckeystroke/edownarrowkey)

|  | Declaration |
| --- | --- |
| From | ``` var eDownArrowKey: Int { get } ``` |
| To | ``` var eDownArrowKey: OSType { get } ``` |

Modified [eDVD](https://developer.apple.com/documentation/coreservices/edvd)

|  | Declaration |
| --- | --- |
| From | ``` var eDVD: Int { get } ``` |
| To | ``` var eDVD: OSType { get } ``` |

Modified [eEndKey](https://developer.apple.com/documentation/coreservices/1556385-ckeystroke/eendkey)

|  | Declaration |
| --- | --- |
| From | ``` var eEndKey: Int { get } ``` |
| To | ``` var eEndKey: OSType { get } ``` |

Modified [eEnterKey](https://developer.apple.com/documentation/coreservices/eenterkey)

|  | Declaration |
| --- | --- |
| From | ``` var eEnterKey: Int { get } ``` |
| To | ``` var eEnterKey: OSType { get } ``` |

Modified [eEscapeKey](https://developer.apple.com/documentation/coreservices/eescapekey)

|  | Declaration |
| --- | --- |
| From | ``` var eEscapeKey: Int { get } ``` |
| To | ``` var eEscapeKey: OSType { get } ``` |

Modified [eEthernet](https://developer.apple.com/documentation/coreservices/eethernet)

|  | Declaration |
| --- | --- |
| From | ``` var eEthernet: Int { get } ``` |
| To | ``` var eEthernet: OSType { get } ``` |

Modified [eF10Key](https://developer.apple.com/documentation/coreservices/ef10key)

|  | Declaration |
| --- | --- |
| From | ``` var eF10Key: Int { get } ``` |
| To | ``` var eF10Key: OSType { get } ``` |

Modified [eF11Key](https://developer.apple.com/documentation/coreservices/1556385-ckeystroke/ef11key)

|  | Declaration |
| --- | --- |
| From | ``` var eF11Key: Int { get } ``` |
| To | ``` var eF11Key: OSType { get } ``` |

Modified [eF12Key](https://developer.apple.com/documentation/coreservices/ef12key)

|  | Declaration |
| --- | --- |
| From | ``` var eF12Key: Int { get } ``` |
| To | ``` var eF12Key: OSType { get } ``` |

Modified [eF13Key](https://developer.apple.com/documentation/coreservices/ef13key)

|  | Declaration |
| --- | --- |
| From | ``` var eF13Key: Int { get } ``` |
| To | ``` var eF13Key: OSType { get } ``` |

Modified [eF14Key](https://developer.apple.com/documentation/coreservices/1556385-ckeystroke/ef14key)

|  | Declaration |
| --- | --- |
| From | ``` var eF14Key: Int { get } ``` |
| To | ``` var eF14Key: OSType { get } ``` |

Modified [eF15Key](https://developer.apple.com/documentation/coreservices/ef15key)

|  | Declaration |
| --- | --- |
| From | ``` var eF15Key: Int { get } ``` |
| To | ``` var eF15Key: OSType { get } ``` |

Modified [eF1Key](https://developer.apple.com/documentation/coreservices/1556385-ckeystroke/ef1key)

|  | Declaration |
| --- | --- |
| From | ``` var eF1Key: Int { get } ``` |
| To | ``` var eF1Key: OSType { get } ``` |

Modified [eF2Key](https://developer.apple.com/documentation/coreservices/1556385-ckeystroke/ef2key)

|  | Declaration |
| --- | --- |
| From | ``` var eF2Key: Int { get } ``` |
| To | ``` var eF2Key: OSType { get } ``` |

Modified [eF3Key](https://developer.apple.com/documentation/coreservices/ef3key)

|  | Declaration |
| --- | --- |
| From | ``` var eF3Key: Int { get } ``` |
| To | ``` var eF3Key: OSType { get } ``` |

Modified [eF4Key](https://developer.apple.com/documentation/coreservices/ef4key)

|  | Declaration |
| --- | --- |
| From | ``` var eF4Key: Int { get } ``` |
| To | ``` var eF4Key: OSType { get } ``` |

Modified [eF5Key](https://developer.apple.com/documentation/coreservices/ef5key)

|  | Declaration |
| --- | --- |
| From | ``` var eF5Key: Int { get } ``` |
| To | ``` var eF5Key: OSType { get } ``` |

Modified [eF6Key](https://developer.apple.com/documentation/coreservices/ef6key)

|  | Declaration |
| --- | --- |
| From | ``` var eF6Key: Int { get } ``` |
| To | ``` var eF6Key: OSType { get } ``` |

Modified [eF7Key](https://developer.apple.com/documentation/coreservices/ef7key)

|  | Declaration |
| --- | --- |
| From | ``` var eF7Key: Int { get } ``` |
| To | ``` var eF7Key: OSType { get } ``` |

Modified [eF8Key](https://developer.apple.com/documentation/coreservices/1556385-ckeystroke/ef8key)

|  | Declaration |
| --- | --- |
| From | ``` var eF8Key: Int { get } ``` |
| To | ``` var eF8Key: OSType { get } ``` |

Modified [eF9Key](https://developer.apple.com/documentation/coreservices/ef9key)

|  | Declaration |
| --- | --- |
| From | ``` var eF9Key: Int { get } ``` |
| To | ``` var eF9Key: OSType { get } ``` |

Modified [eFireWire](https://developer.apple.com/documentation/coreservices/efirewire)

|  | Declaration |
| --- | --- |
| From | ``` var eFireWire: Int { get } ``` |
| To | ``` var eFireWire: OSType { get } ``` |

Modified [eFloppy](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/efloppy)

|  | Declaration |
| --- | --- |
| From | ``` var eFloppy: Int { get } ``` |
| To | ``` var eFloppy: OSType { get } ``` |

Modified [eForwardDelKey](https://developer.apple.com/documentation/coreservices/eforwarddelkey)

|  | Declaration |
| --- | --- |
| From | ``` var eForwardDelKey: Int { get } ``` |
| To | ``` var eForwardDelKey: OSType { get } ``` |

Modified [eHD](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/ehd)

|  | Declaration |
| --- | --- |
| From | ``` var eHD: Int { get } ``` |
| To | ``` var eHD: OSType { get } ``` |

Modified [eHelpKey](https://developer.apple.com/documentation/coreservices/1556385-ckeystroke/ehelpkey)

|  | Declaration |
| --- | --- |
| From | ``` var eHelpKey: Int { get } ``` |
| To | ``` var eHelpKey: OSType { get } ``` |

Modified [eHomeKey](https://developer.apple.com/documentation/coreservices/ehomekey)

|  | Declaration |
| --- | --- |
| From | ``` var eHomeKey: Int { get } ``` |
| To | ``` var eHomeKey: OSType { get } ``` |

Modified [eInfrared](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/einfrared)

|  | Declaration |
| --- | --- |
| From | ``` var eInfrared: Int { get } ``` |
| To | ``` var eInfrared: OSType { get } ``` |

Modified [eIP](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/eip)

|  | Declaration |
| --- | --- |
| From | ``` var eIP: Int { get } ``` |
| To | ``` var eIP: OSType { get } ``` |

Modified [eIrDA](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/eirda)

|  | Declaration |
| --- | --- |
| From | ``` var eIrDA: Int { get } ``` |
| To | ``` var eIrDA: OSType { get } ``` |

Modified [eIRTalk](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/eirtalk)

|  | Declaration |
| --- | --- |
| From | ``` var eIRTalk: Int { get } ``` |
| To | ``` var eIRTalk: OSType { get } ``` |

Modified [eKeyboard](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/ekeyboard)

|  | Declaration |
| --- | --- |
| From | ``` var eKeyboard: Int { get } ``` |
| To | ``` var eKeyboard: OSType { get } ``` |

Modified [eKeyKind](https://developer.apple.com/documentation/coreservices/ekeykind)

|  | Declaration |
| --- | --- |
| From | ``` var eKeyKind: Int { get } ``` |
| To | ``` var eKeyKind: OSType { get } ``` |

Modified [eLCD](https://developer.apple.com/documentation/coreservices/elcd)

|  | Declaration |
| --- | --- |
| From | ``` var eLCD: Int { get } ``` |
| To | ``` var eLCD: OSType { get } ``` |

Modified [eLeftArrowKey](https://developer.apple.com/documentation/coreservices/eleftarrowkey)

|  | Declaration |
| --- | --- |
| From | ``` var eLeftArrowKey: Int { get } ``` |
| To | ``` var eLeftArrowKey: OSType { get } ``` |

Modified [eLocalTalk](https://developer.apple.com/documentation/coreservices/elocaltalk)

|  | Declaration |
| --- | --- |
| From | ``` var eLocalTalk: Int { get } ``` |
| To | ``` var eLocalTalk: OSType { get } ``` |

Modified [eMacIP](https://developer.apple.com/documentation/coreservices/emacip)

|  | Declaration |
| --- | --- |
| From | ``` var eMacIP: Int { get } ``` |
| To | ``` var eMacIP: OSType { get } ``` |

Modified [eMacVideo](https://developer.apple.com/documentation/coreservices/emacvideo)

|  | Declaration |
| --- | --- |
| From | ``` var eMacVideo: Int { get } ``` |
| To | ``` var eMacVideo: OSType { get } ``` |

Modified [eMicrophone](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/emicrophone)

|  | Declaration |
| --- | --- |
| From | ``` var eMicrophone: Int { get } ``` |
| To | ``` var eMicrophone: OSType { get } ``` |

Modified [eModem](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/emodem)

|  | Declaration |
| --- | --- |
| From | ``` var eModem: Int { get } ``` |
| To | ``` var eModem: OSType { get } ``` |

Modified [eModemPort](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/emodemport)

|  | Declaration |
| --- | --- |
| From | ``` var eModemPort: Int { get } ``` |
| To | ``` var eModemPort: OSType { get } ``` |

Modified [eModemPrinterPort](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/emodemprinterport)

|  | Declaration |
| --- | --- |
| From | ``` var eModemPrinterPort: Int { get } ``` |
| To | ``` var eModemPrinterPort: OSType { get } ``` |

Modified [eModifiers](https://developer.apple.com/documentation/coreservices/1556385-ckeystroke/emodifiers)

|  | Declaration |
| --- | --- |
| From | ``` var eModifiers: Int { get } ``` |
| To | ``` var eModifiers: OSType { get } ``` |

Modified [eMonitorOut](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/emonitorout)

|  | Declaration |
| --- | --- |
| From | ``` var eMonitorOut: Int { get } ``` |
| To | ``` var eMonitorOut: OSType { get } ``` |

Modified [eMouse](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/emouse)

|  | Declaration |
| --- | --- |
| From | ``` var eMouse: Int { get } ``` |
| To | ``` var eMouse: OSType { get } ``` |

Modified [eNuBus](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/enubus)

|  | Declaration |
| --- | --- |
| From | ``` var eNuBus: Int { get } ``` |
| To | ``` var eNuBus: OSType { get } ``` |

Modified [eNuBusCard](https://developer.apple.com/documentation/coreservices/enubuscard)

|  | Declaration |
| --- | --- |
| From | ``` var eNuBusCard: Int { get } ``` |
| To | ``` var eNuBusCard: OSType { get } ``` |

Modified [enumArrows](https://developer.apple.com/documentation/coreservices/enumarrows)

|  | Declaration |
| --- | --- |
| From | ``` var enumArrows: Int { get } ``` |
| To | ``` var enumArrows: OSType { get } ``` |

Modified [enumJustification](https://developer.apple.com/documentation/coreservices/1556364-anonymous/enumjustification)

|  | Declaration |
| --- | --- |
| From | ``` var enumJustification: Int { get } ``` |
| To | ``` var enumJustification: OSType { get } ``` |

Modified [enumKeyForm](https://developer.apple.com/documentation/coreservices/1556364-anonymous/enumkeyform)

|  | Declaration |
| --- | --- |
| From | ``` var enumKeyForm: Int { get } ``` |
| To | ``` var enumKeyForm: OSType { get } ``` |

Modified [enumPosition](https://developer.apple.com/documentation/coreservices/enumposition)

|  | Declaration |
| --- | --- |
| From | ``` var enumPosition: Int { get } ``` |
| To | ``` var enumPosition: OSType { get } ``` |

Modified [enumProtection](https://developer.apple.com/documentation/coreservices/enumprotection)

|  | Declaration |
| --- | --- |
| From | ``` var enumProtection: Int { get } ``` |
| To | ``` var enumProtection: OSType { get } ``` |

Modified [enumQuality](https://developer.apple.com/documentation/coreservices/1556364-anonymous/enumquality)

|  | Declaration |
| --- | --- |
| From | ``` var enumQuality: Int { get } ``` |
| To | ``` var enumQuality: OSType { get } ``` |

Modified [enumSaveOptions](https://developer.apple.com/documentation/coreservices/enumsaveoptions)

|  | Declaration |
| --- | --- |
| From | ``` var enumSaveOptions: Int { get } ``` |
| To | ``` var enumSaveOptions: OSType { get } ``` |

Modified [enumStyle](https://developer.apple.com/documentation/coreservices/enumstyle)

|  | Declaration |
| --- | --- |
| From | ``` var enumStyle: Int { get } ``` |
| To | ``` var enumStyle: OSType { get } ``` |

Modified [enumTransferMode](https://developer.apple.com/documentation/coreservices/enumtransfermode)

|  | Declaration |
| --- | --- |
| From | ``` var enumTransferMode: Int { get } ``` |
| To | ``` var enumTransferMode: OSType { get } ``` |

Modified [eOptionDown](https://developer.apple.com/documentation/coreservices/eoptiondown)

|  | Declaration |
| --- | --- |
| From | ``` var eOptionDown: Int { get } ``` |
| To | ``` var eOptionDown: OSType { get } ``` |

Modified [ePageDownKey](https://developer.apple.com/documentation/coreservices/1556385-ckeystroke/epagedownkey)

|  | Declaration |
| --- | --- |
| From | ``` var ePageDownKey: Int { get } ``` |
| To | ``` var ePageDownKey: OSType { get } ``` |

Modified [ePageUpKey](https://developer.apple.com/documentation/coreservices/epageupkey)

|  | Declaration |
| --- | --- |
| From | ``` var ePageUpKey: Int { get } ``` |
| To | ``` var ePageUpKey: OSType { get } ``` |

Modified [ePCcard](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/epccard)

|  | Declaration |
| --- | --- |
| From | ``` var ePCcard: Int { get } ``` |
| To | ``` var ePCcard: OSType { get } ``` |

Modified [ePCIbus](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/epcibus)

|  | Declaration |
| --- | --- |
| From | ``` var ePCIbus: Int { get } ``` |
| To | ``` var ePCIbus: OSType { get } ``` |

Modified [ePCIcard](https://developer.apple.com/documentation/coreservices/epcicard)

|  | Declaration |
| --- | --- |
| From | ``` var ePCIcard: Int { get } ``` |
| To | ``` var ePCIcard: OSType { get } ``` |

Modified [ePDScard](https://developer.apple.com/documentation/coreservices/epdscard)

|  | Declaration |
| --- | --- |
| From | ``` var ePDScard: Int { get } ``` |
| To | ``` var ePDScard: OSType { get } ``` |

Modified [ePDSslot](https://developer.apple.com/documentation/coreservices/epdsslot)

|  | Declaration |
| --- | --- |
| From | ``` var ePDSslot: Int { get } ``` |
| To | ``` var ePDSslot: OSType { get } ``` |

Modified [ePointingDevice](https://developer.apple.com/documentation/coreservices/epointingdevice)

|  | Declaration |
| --- | --- |
| From | ``` var ePointingDevice: Int { get } ``` |
| To | ``` var ePointingDevice: OSType { get } ``` |

Modified [ePostScript](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/epostscript)

|  | Declaration |
| --- | --- |
| From | ``` var ePostScript: Int { get } ``` |
| To | ``` var ePostScript: OSType { get } ``` |

Modified [ePPP](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/eppp)

|  | Declaration |
| --- | --- |
| From | ``` var ePPP: Int { get } ``` |
| To | ``` var ePPP: OSType { get } ``` |

Modified [ePrinter](https://developer.apple.com/documentation/coreservices/eprinter)

|  | Declaration |
| --- | --- |
| From | ``` var ePrinter: Int { get } ``` |
| To | ``` var ePrinter: OSType { get } ``` |

Modified [ePrinterPort](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/eprinterport)

|  | Declaration |
| --- | --- |
| From | ``` var ePrinterPort: Int { get } ``` |
| To | ``` var ePrinterPort: OSType { get } ``` |

Modified [eProtocol](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/eprotocol)

|  | Declaration |
| --- | --- |
| From | ``` var eProtocol: Int { get } ``` |
| To | ``` var eProtocol: OSType { get } ``` |

Modified [eReturnKey](https://developer.apple.com/documentation/coreservices/ereturnkey)

|  | Declaration |
| --- | --- |
| From | ``` var eReturnKey: Int { get } ``` |
| To | ``` var eReturnKey: OSType { get } ``` |

Modified [eRightArrowKey](https://developer.apple.com/documentation/coreservices/erightarrowkey)

|  | Declaration |
| --- | --- |
| From | ``` var eRightArrowKey: Int { get } ``` |
| To | ``` var eRightArrowKey: OSType { get } ``` |

Modified [eScheme](https://developer.apple.com/documentation/coreservices/escheme)

|  | Declaration |
| --- | --- |
| From | ``` var eScheme: Int { get } ``` |
| To | ``` var eScheme: OSType { get } ``` |

Modified [eSCSI](https://developer.apple.com/documentation/coreservices/escsi)

|  | Declaration |
| --- | --- |
| From | ``` var eSCSI: Int { get } ``` |
| To | ``` var eSCSI: OSType { get } ``` |

Modified [eSerial](https://developer.apple.com/documentation/coreservices/eserial)

|  | Declaration |
| --- | --- |
| From | ``` var eSerial: Int { get } ``` |
| To | ``` var eSerial: OSType { get } ``` |

Modified [eShiftDown](https://developer.apple.com/documentation/coreservices/eshiftdown)

|  | Declaration |
| --- | --- |
| From | ``` var eShiftDown: Int { get } ``` |
| To | ``` var eShiftDown: OSType { get } ``` |

Modified [eSpeakers](https://developer.apple.com/documentation/coreservices/espeakers)

|  | Declaration |
| --- | --- |
| From | ``` var eSpeakers: Int { get } ``` |
| To | ``` var eSpeakers: OSType { get } ``` |

Modified [eStorageDevice](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/estoragedevice)

|  | Declaration |
| --- | --- |
| From | ``` var eStorageDevice: Int { get } ``` |
| To | ``` var eStorageDevice: OSType { get } ``` |

Modified [eSVGA](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/esvga)

|  | Declaration |
| --- | --- |
| From | ``` var eSVGA: Int { get } ``` |
| To | ``` var eSVGA: OSType { get } ``` |

Modified [eSvideo](https://developer.apple.com/documentation/coreservices/esvideo)

|  | Declaration |
| --- | --- |
| From | ``` var eSvideo: Int { get } ``` |
| To | ``` var eSvideo: OSType { get } ``` |

Modified [eTabKey](https://developer.apple.com/documentation/coreservices/1556385-ckeystroke/etabkey)

|  | Declaration |
| --- | --- |
| From | ``` var eTabKey: Int { get } ``` |
| To | ``` var eTabKey: OSType { get } ``` |

Modified [eTokenRing](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/etokenring)

|  | Declaration |
| --- | --- |
| From | ``` var eTokenRing: Int { get } ``` |
| To | ``` var eTokenRing: OSType { get } ``` |

Modified [eTrackball](https://developer.apple.com/documentation/coreservices/etrackball)

|  | Declaration |
| --- | --- |
| From | ``` var eTrackball: Int { get } ``` |
| To | ``` var eTrackball: OSType { get } ``` |

Modified [eTrackpad](https://developer.apple.com/documentation/coreservices/etrackpad)

|  | Declaration |
| --- | --- |
| From | ``` var eTrackpad: Int { get } ``` |
| To | ``` var eTrackpad: OSType { get } ``` |

Modified [eUpArrowKey](https://developer.apple.com/documentation/coreservices/euparrowkey)

|  | Declaration |
| --- | --- |
| From | ``` var eUpArrowKey: Int { get } ``` |
| To | ``` var eUpArrowKey: OSType { get } ``` |

Modified [eurlAFP](https://developer.apple.com/documentation/coreservices/eurlafp)

|  | Declaration |
| --- | --- |
| From | ``` var eurlAFP: Int { get } ``` |
| To | ``` var eurlAFP: OSType { get } ``` |

Modified [eurlAT](https://developer.apple.com/documentation/coreservices/1556397-escheme/eurlat)

|  | Declaration |
| --- | --- |
| From | ``` var eurlAT: Int { get } ``` |
| To | ``` var eurlAT: OSType { get } ``` |

Modified [eurlEPPC](https://developer.apple.com/documentation/coreservices/eurleppc)

|  | Declaration |
| --- | --- |
| From | ``` var eurlEPPC: Int { get } ``` |
| To | ``` var eurlEPPC: OSType { get } ``` |

Modified [eurlFile](https://developer.apple.com/documentation/coreservices/1556397-escheme/eurlfile)

|  | Declaration |
| --- | --- |
| From | ``` var eurlFile: Int { get } ``` |
| To | ``` var eurlFile: OSType { get } ``` |

Modified [eurlFTP](https://developer.apple.com/documentation/coreservices/1556397-escheme/eurlftp)

|  | Declaration |
| --- | --- |
| From | ``` var eurlFTP: Int { get } ``` |
| To | ``` var eurlFTP: OSType { get } ``` |

Modified [eurlGopher](https://developer.apple.com/documentation/coreservices/eurlgopher)

|  | Declaration |
| --- | --- |
| From | ``` var eurlGopher: Int { get } ``` |
| To | ``` var eurlGopher: OSType { get } ``` |

Modified [eurlHTTP](https://developer.apple.com/documentation/coreservices/1556397-escheme/eurlhttp)

|  | Declaration |
| --- | --- |
| From | ``` var eurlHTTP: Int { get } ``` |
| To | ``` var eurlHTTP: OSType { get } ``` |

Modified [eurlHTTPS](https://developer.apple.com/documentation/coreservices/eurlhttps)

|  | Declaration |
| --- | --- |
| From | ``` var eurlHTTPS: Int { get } ``` |
| To | ``` var eurlHTTPS: OSType { get } ``` |

Modified [eurlIMAP](https://developer.apple.com/documentation/coreservices/eurlimap)

|  | Declaration |
| --- | --- |
| From | ``` var eurlIMAP: Int { get } ``` |
| To | ``` var eurlIMAP: OSType { get } ``` |

Modified [eurlLaunch](https://developer.apple.com/documentation/coreservices/1556397-escheme/eurllaunch)

|  | Declaration |
| --- | --- |
| From | ``` var eurlLaunch: Int { get } ``` |
| To | ``` var eurlLaunch: OSType { get } ``` |

Modified [eurlLDAP](https://developer.apple.com/documentation/coreservices/eurlldap)

|  | Declaration |
| --- | --- |
| From | ``` var eurlLDAP: Int { get } ``` |
| To | ``` var eurlLDAP: OSType { get } ``` |

Modified [eurlMail](https://developer.apple.com/documentation/coreservices/1556397-escheme/eurlmail)

|  | Declaration |
| --- | --- |
| From | ``` var eurlMail: Int { get } ``` |
| To | ``` var eurlMail: OSType { get } ``` |

Modified [eurlMailbox](https://developer.apple.com/documentation/coreservices/1556397-escheme/eurlmailbox)

|  | Declaration |
| --- | --- |
| From | ``` var eurlMailbox: Int { get } ``` |
| To | ``` var eurlMailbox: OSType { get } ``` |

Modified [eurlMessage](https://developer.apple.com/documentation/coreservices/1556397-escheme/eurlmessage)

|  | Declaration |
| --- | --- |
| From | ``` var eurlMessage: Int { get } ``` |
| To | ``` var eurlMessage: OSType { get } ``` |

Modified [eurlMulti](https://developer.apple.com/documentation/coreservices/eurlmulti)

|  | Declaration |
| --- | --- |
| From | ``` var eurlMulti: Int { get } ``` |
| To | ``` var eurlMulti: OSType { get } ``` |

Modified [eurlNews](https://developer.apple.com/documentation/coreservices/eurlnews)

|  | Declaration |
| --- | --- |
| From | ``` var eurlNews: Int { get } ``` |
| To | ``` var eurlNews: OSType { get } ``` |

Modified [eurlNFS](https://developer.apple.com/documentation/coreservices/eurlnfs)

|  | Declaration |
| --- | --- |
| From | ``` var eurlNFS: Int { get } ``` |
| To | ``` var eurlNFS: OSType { get } ``` |

Modified [eurlNNTP](https://developer.apple.com/documentation/coreservices/eurlnntp)

|  | Declaration |
| --- | --- |
| From | ``` var eurlNNTP: Int { get } ``` |
| To | ``` var eurlNNTP: OSType { get } ``` |

Modified [eurlPOP](https://developer.apple.com/documentation/coreservices/eurlpop)

|  | Declaration |
| --- | --- |
| From | ``` var eurlPOP: Int { get } ``` |
| To | ``` var eurlPOP: OSType { get } ``` |

Modified [eurlRTSP](https://developer.apple.com/documentation/coreservices/eurlrtsp)

|  | Declaration |
| --- | --- |
| From | ``` var eurlRTSP: Int { get } ``` |
| To | ``` var eurlRTSP: OSType { get } ``` |

Modified [eurlSNews](https://developer.apple.com/documentation/coreservices/1556397-escheme/eurlsnews)

|  | Declaration |
| --- | --- |
| From | ``` var eurlSNews: Int { get } ``` |
| To | ``` var eurlSNews: OSType { get } ``` |

Modified [eurlTelnet](https://developer.apple.com/documentation/coreservices/eurltelnet)

|  | Declaration |
| --- | --- |
| From | ``` var eurlTelnet: Int { get } ``` |
| To | ``` var eurlTelnet: OSType { get } ``` |

Modified [eurlUnknown](https://developer.apple.com/documentation/coreservices/1556397-escheme/eurlunknown)

|  | Declaration |
| --- | --- |
| From | ``` var eurlUnknown: Int { get } ``` |
| To | ``` var eurlUnknown: OSType { get } ``` |

Modified [eUSB](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/eusb)

|  | Declaration |
| --- | --- |
| From | ``` var eUSB: Int { get } ``` |
| To | ``` var eUSB: OSType { get } ``` |

Modified [eVideoIn](https://developer.apple.com/documentation/coreservices/evideoin)

|  | Declaration |
| --- | --- |
| From | ``` var eVideoIn: Int { get } ``` |
| To | ``` var eVideoIn: OSType { get } ``` |

Modified [eVideoMonitor](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/evideomonitor)

|  | Declaration |
| --- | --- |
| From | ``` var eVideoMonitor: Int { get } ``` |
| To | ``` var eVideoMonitor: OSType { get } ``` |

Modified [eVideoOut](https://developer.apple.com/documentation/coreservices/evideoout)

|  | Declaration |
| --- | --- |
| From | ``` var eVideoOut: Int { get } ``` |
| To | ``` var eVideoOut: OSType { get } ``` |

Modified [FSEventStreamCallback](https://developer.apple.com/documentation/coreservices/fseventstreamcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias FSEventStreamCallback = (ConstFSEventStreamRef, UnsafeMutablePointer<Void>, Int, UnsafeMutablePointer<Void>, UnsafePointer<FSEventStreamEventFlags>, UnsafePointer<FSEventStreamEventId>) -> Void ``` |
| To | ``` typealias FSEventStreamCallback = (ConstFSEventStreamRef, UnsafeMutableRawPointer?, Int, UnsafeMutableRawPointer, UnsafePointer<FSEventStreamEventFlags>?, UnsafePointer<FSEventStreamEventId>?) -> Swift.Void ``` |

Modified [FSEventStreamCreate(_: CFAllocator?, _: CoreServices.FSEventStreamCallback, _: UnsafeMutablePointer<FSEventStreamContext>?, _: CFArray, _: FSEventStreamEventId, _: CFTimeInterval, _: FSEventStreamCreateFlags) -> FSEventStreamRef?](https://developer.apple.com/documentation/coreservices/1443980-fseventstreamcreate)

|  | Declaration |
| --- | --- |
| From | ``` func FSEventStreamCreate(_ allocator: CFAllocator?, _ callback: FSEventStreamCallback, _ context: UnsafeMutablePointer<FSEventStreamContext>, _ pathsToWatch: CFArray, _ sinceWhen: FSEventStreamEventId, _ latency: CFTimeInterval, _ flags: FSEventStreamCreateFlags) -> FSEventStreamRef ``` |
| To | ``` func FSEventStreamCreate(_ allocator: CFAllocator?, _ callback: CoreServices.FSEventStreamCallback, _ context: UnsafeMutablePointer<FSEventStreamContext>?, _ pathsToWatch: CFArray, _ sinceWhen: FSEventStreamEventId, _ latency: CFTimeInterval, _ flags: FSEventStreamCreateFlags) -> FSEventStreamRef? ``` |

Modified [FSEventStreamCreateRelativeToDevice(_: CFAllocator?, _: CoreServices.FSEventStreamCallback, _: UnsafeMutablePointer<FSEventStreamContext>?, _: dev_t, _: CFArray, _: FSEventStreamEventId, _: CFTimeInterval, _: FSEventStreamCreateFlags) -> FSEventStreamRef?](https://developer.apple.com/documentation/coreservices/1447341-fseventstreamcreaterelativetodev)

|  | Declaration |
| --- | --- |
| From | ``` func FSEventStreamCreateRelativeToDevice(_ allocator: CFAllocator?, _ callback: FSEventStreamCallback, _ context: UnsafeMutablePointer<FSEventStreamContext>, _ deviceToWatch: dev_t, _ pathsToWatchRelativeToDevice: CFArray, _ sinceWhen: FSEventStreamEventId, _ latency: CFTimeInterval, _ flags: FSEventStreamCreateFlags) -> FSEventStreamRef ``` |
| To | ``` func FSEventStreamCreateRelativeToDevice(_ allocator: CFAllocator?, _ callback: CoreServices.FSEventStreamCallback, _ context: UnsafeMutablePointer<FSEventStreamContext>?, _ deviceToWatch: dev_t, _ pathsToWatchRelativeToDevice: CFArray, _ sinceWhen: FSEventStreamEventId, _ latency: CFTimeInterval, _ flags: FSEventStreamCreateFlags) -> FSEventStreamRef? ``` |

Modified [FSEventStreamRef](https://developer.apple.com/documentation/coreservices/fseventstreamref)

|  | Declaration |
| --- | --- |
| From | ``` typealias FSEventStreamRef = COpaquePointer ``` |
| To | ``` typealias FSEventStreamRef = OpaquePointer ``` |

Modified [FSEventStreamSetDispatchQueue(_: FSEventStreamRef, _: DispatchQueue?)](https://developer.apple.com/documentation/coreservices/1444164-fseventstreamsetdispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` func FSEventStreamSetDispatchQueue(_ streamRef: FSEventStreamRef, _ q: dispatch_queue_t?) ``` |
| To | ``` func FSEventStreamSetDispatchQueue(_ streamRef: FSEventStreamRef, _ q: DispatchQueue?) ``` |

Modified [GetCustomIconsEnabled(_: Int16, _: UnsafeMutablePointer<DarwinBoolean>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1442255-getcustomiconsenabled)

|  | Declaration |
| --- | --- |
| From | ``` func GetCustomIconsEnabled(_ vRefNum: Int16, _ customIconsEnabled: UnsafeMutablePointer<DarwinBoolean>) -> OSErr ``` |
| To | ``` func GetCustomIconsEnabled(_ vRefNum: Int16, _ customIconsEnabled: UnsafeMutablePointer<DarwinBoolean>!) -> OSErr ``` |

Modified [GetIconRef(_: Int16, _: OSType, _: OSType, _: UnsafeMutablePointer<IconRef?>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1442776-geticonref)

|  | Declaration |
| --- | --- |
| From | ``` func GetIconRef(_ vRefNum: Int16, _ creator: OSType, _ iconType: OSType, _ theIconRef: UnsafeMutablePointer<IconRef>) -> OSErr ``` |
| To | ``` func GetIconRef(_ vRefNum: Int16, _ creator: OSType, _ iconType: OSType, _ theIconRef: UnsafeMutablePointer<IconRef?>!) -> OSErr ``` |

Modified [GetIconRefFromComponent(_: Component!, _: UnsafeMutablePointer<IconRef?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1447113-geticonreffromcomponent)

|  | Declaration |
| --- | --- |
| From | ``` func GetIconRefFromComponent(_ inComponent: Component, _ outIconRef: UnsafeMutablePointer<IconRef>) -> OSStatus ``` |
| To | ``` func GetIconRefFromComponent(_ inComponent: Component!, _ outIconRef: UnsafeMutablePointer<IconRef?>!) -> OSStatus ``` |

Modified [GetIconRefFromFileInfo(_: UnsafePointer<FSRef>!, _: Int, _: UnsafePointer<UniChar>!, _: FSCatalogInfoBitmap, _: UnsafePointer<FSCatalogInfo>!, _: IconServicesUsageFlags, _: UnsafeMutablePointer<IconRef?>!, _: UnsafeMutablePointer<Int16>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1447966-geticonreffromfileinfo)

|  | Declaration |
| --- | --- |
| From | ``` func GetIconRefFromFileInfo(_ inRef: UnsafePointer<FSRef>, _ inFileNameLength: Int, _ inFileName: UnsafePointer<UniChar>, _ inWhichInfo: FSCatalogInfoBitmap, _ inCatalogInfo: UnsafePointer<FSCatalogInfo>, _ inUsageFlags: IconServicesUsageFlags, _ outIconRef: UnsafeMutablePointer<IconRef>, _ outLabel: UnsafeMutablePointer<Int16>) -> OSStatus ``` |
| To | ``` func GetIconRefFromFileInfo(_ inRef: UnsafePointer<FSRef>!, _ inFileNameLength: Int, _ inFileName: UnsafePointer<UniChar>!, _ inWhichInfo: FSCatalogInfoBitmap, _ inCatalogInfo: UnsafePointer<FSCatalogInfo>!, _ inUsageFlags: IconServicesUsageFlags, _ outIconRef: UnsafeMutablePointer<IconRef?>!, _ outLabel: UnsafeMutablePointer<Int16>!) -> OSStatus ``` |

Modified [GetIconRefFromFolder(_: Int16, _: Int32, _: Int32, _: Int8, _: Int8, _: UnsafeMutablePointer<IconRef?>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1441712-geticonreffromfolder)

|  | Declaration |
| --- | --- |
| From | ``` func GetIconRefFromFolder(_ vRefNum: Int16, _ parentFolderID: Int32, _ folderID: Int32, _ attributes: Int8, _ accessPrivileges: Int8, _ theIconRef: UnsafeMutablePointer<IconRef>) -> OSErr ``` |
| To | ``` func GetIconRefFromFolder(_ vRefNum: Int16, _ parentFolderID: Int32, _ folderID: Int32, _ attributes: Int8, _ accessPrivileges: Int8, _ theIconRef: UnsafeMutablePointer<IconRef?>!) -> OSErr ``` |

Modified [GetIconRefFromIconFamilyPtr(_: UnsafePointer<IconFamilyResource>!, _: Size, _: UnsafeMutablePointer<IconRef?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1443251-geticonreffromiconfamilyptr)

|  | Declaration |
| --- | --- |
| From | ``` func GetIconRefFromIconFamilyPtr(_ inIconFamilyPtr: UnsafePointer<IconFamilyResource>, _ inSize: Size, _ outIconRef: UnsafeMutablePointer<IconRef>) -> OSStatus ``` |
| To | ``` func GetIconRefFromIconFamilyPtr(_ inIconFamilyPtr: UnsafePointer<IconFamilyResource>!, _ inSize: Size, _ outIconRef: UnsafeMutablePointer<IconRef?>!) -> OSStatus ``` |

Modified [GetIconRefFromTypeInfo(_: OSType, _: OSType, _: CFString!, _: CFString!, _: IconServicesUsageFlags, _: UnsafeMutablePointer<IconRef?>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1445758-geticonreffromtypeinfo)

|  | Declaration |
| --- | --- |
| From | ``` func GetIconRefFromTypeInfo(_ inCreator: OSType, _ inType: OSType, _ inExtension: CFString!, _ inMIMEType: CFString!, _ inUsageFlags: IconServicesUsageFlags, _ outIconRef: UnsafeMutablePointer<IconRef>) -> OSErr ``` |
| To | ``` func GetIconRefFromTypeInfo(_ inCreator: OSType, _ inType: OSType, _ inExtension: CFString!, _ inMIMEType: CFString!, _ inUsageFlags: IconServicesUsageFlags, _ outIconRef: UnsafeMutablePointer<IconRef?>!) -> OSErr ``` |

Modified [GetIconRefOwners(_: IconRef!, _: UnsafeMutablePointer<UInt16>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1447221-geticonrefowners)

|  | Declaration |
| --- | --- |
| From | ``` func GetIconRefOwners(_ theIconRef: IconRef, _ owners: UnsafeMutablePointer<UInt16>) -> OSErr ``` |
| To | ``` func GetIconRefOwners(_ theIconRef: IconRef!, _ owners: UnsafeMutablePointer<UInt16>!) -> OSErr ``` |

Modified [IconRef](https://developer.apple.com/documentation/coreservices/iconref)

|  | Declaration |
| --- | --- |
| From | ``` typealias IconRef = COpaquePointer ``` |
| To | ``` typealias IconRef = OpaquePointer ``` |

Modified [IndexToUCStringProcPtr](https://developer.apple.com/documentation/coreservices/indextoucstringprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias IndexToUCStringProcPtr = (UInt32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Unmanaged<CFString>?>, UnsafeMutablePointer<UCTypeSelectOptions>) -> DarwinBoolean ``` |
| To | ``` typealias IndexToUCStringProcPtr = (UInt32, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutablePointer<Unmanaged<CFString>?>?, UnsafeMutablePointer<UCTypeSelectOptions>?) -> DarwinBoolean ``` |

Modified [IndexToUCStringUPP](https://developer.apple.com/documentation/coreservices/indextoucstringupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias IndexToUCStringUPP = IndexToUCStringProcPtr ``` |
| To | ``` typealias IndexToUCStringUPP = CoreServices.IndexToUCStringProcPtr ``` |

Modified [InvokeAECoerceDescUPP(_: UnsafePointer<AEDesc>!, _: DescType, _: SRefCon!, _: UnsafeMutablePointer<AEDesc>!, _: CoreServices.AECoerceDescUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1445450-invokeaecoercedescupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeAECoerceDescUPP(_ fromDesc: UnsafePointer<AEDesc>, _ toType: DescType, _ handlerRefcon: SRefCon, _ toDesc: UnsafeMutablePointer<AEDesc>, _ userUPP: AECoerceDescUPP!) -> OSErr ``` |
| To | ``` func InvokeAECoerceDescUPP(_ fromDesc: UnsafePointer<AEDesc>!, _ toType: DescType, _ handlerRefcon: SRefCon!, _ toDesc: UnsafeMutablePointer<AEDesc>!, _ userUPP: CoreServices.AECoerceDescUPP!) -> OSErr ``` |

Modified [InvokeAECoercePtrUPP(_: DescType, _: UnsafeRawPointer!, _: Size, _: DescType, _: SRefCon!, _: UnsafeMutablePointer<AEDesc>!, _: CoreServices.AECoercePtrUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1447079-invokeaecoerceptrupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeAECoercePtrUPP(_ typeCode: DescType, _ dataPtr: UnsafePointer<Void>, _ dataSize: Size, _ toType: DescType, _ handlerRefcon: SRefCon, _ result: UnsafeMutablePointer<AEDesc>, _ userUPP: AECoercePtrUPP!) -> OSErr ``` |
| To | ``` func InvokeAECoercePtrUPP(_ typeCode: DescType, _ dataPtr: UnsafeRawPointer!, _ dataSize: Size, _ toType: DescType, _ handlerRefcon: SRefCon!, _ result: UnsafeMutablePointer<AEDesc>!, _ userUPP: CoreServices.AECoercePtrUPP!) -> OSErr ``` |

Modified [InvokeAEDisposeExternalUPP(_: UnsafeRawPointer!, _: Size, _: SRefCon!, _: CoreServices.AEDisposeExternalUPP!)](https://developer.apple.com/documentation/coreservices/1441717-invokeaedisposeexternalupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeAEDisposeExternalUPP(_ dataPtr: UnsafePointer<Void>, _ dataLength: Size, _ refcon: SRefCon, _ userUPP: AEDisposeExternalUPP!) ``` |
| To | ``` func InvokeAEDisposeExternalUPP(_ dataPtr: UnsafeRawPointer!, _ dataLength: Size, _ refcon: SRefCon!, _ userUPP: CoreServices.AEDisposeExternalUPP!) ``` |

Modified [InvokeAEEventHandlerUPP(_: UnsafePointer<AppleEvent>!, _: UnsafeMutablePointer<AppleEvent>!, _: SRefCon!, _: CoreServices.AEEventHandlerUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1446585-invokeaeeventhandlerupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeAEEventHandlerUPP(_ theAppleEvent: UnsafePointer<AppleEvent>, _ reply: UnsafeMutablePointer<AppleEvent>, _ handlerRefcon: SRefCon, _ userUPP: AEEventHandlerUPP!) -> OSErr ``` |
| To | ``` func InvokeAEEventHandlerUPP(_ theAppleEvent: UnsafePointer<AppleEvent>!, _ reply: UnsafeMutablePointer<AppleEvent>!, _ handlerRefcon: SRefCon!, _ userUPP: CoreServices.AEEventHandlerUPP!) -> OSErr ``` |

Modified [InvokeIndexToUCStringUPP(_: UInt32, _: UnsafeMutableRawPointer!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Unmanaged<CFString>?>!, _: UnsafeMutablePointer<UCTypeSelectOptions>!, _: CoreServices.IndexToUCStringUPP!) -> Bool](https://developer.apple.com/documentation/coreservices/1390660-invokeindextoucstringupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeIndexToUCStringUPP(_ index: UInt32, _ listDataPtr: UnsafeMutablePointer<Void>, _ refcon: UnsafeMutablePointer<Void>, _ outString: UnsafeMutablePointer<Unmanaged<CFString>?>, _ tsOptions: UnsafeMutablePointer<UCTypeSelectOptions>, _ userUPP: IndexToUCStringUPP!) -> Bool ``` |
| To | ``` func InvokeIndexToUCStringUPP(_ index: UInt32, _ listDataPtr: UnsafeMutableRawPointer!, _ refcon: UnsafeMutableRawPointer!, _ outString: UnsafeMutablePointer<Unmanaged<CFString>?>!, _ tsOptions: UnsafeMutablePointer<UCTypeSelectOptions>!, _ userUPP: CoreServices.IndexToUCStringUPP!) -> Bool ``` |

Modified [InvokeOSLAccessorUPP(_: DescType, _: UnsafePointer<AEDesc>!, _: DescType, _: DescType, _: UnsafePointer<AEDesc>!, _: UnsafeMutablePointer<AEDesc>!, _: SRefCon!, _: CoreServices.OSLAccessorUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1448978-invokeoslaccessorupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeOSLAccessorUPP(_ desiredClass: DescType, _ container: UnsafePointer<AEDesc>, _ containerClass: DescType, _ form: DescType, _ selectionData: UnsafePointer<AEDesc>, _ value: UnsafeMutablePointer<AEDesc>, _ accessorRefcon: SRefCon, _ userUPP: OSLAccessorUPP!) -> OSErr ``` |
| To | ``` func InvokeOSLAccessorUPP(_ desiredClass: DescType, _ container: UnsafePointer<AEDesc>!, _ containerClass: DescType, _ form: DescType, _ selectionData: UnsafePointer<AEDesc>!, _ value: UnsafeMutablePointer<AEDesc>!, _ accessorRefcon: SRefCon!, _ userUPP: CoreServices.OSLAccessorUPP!) -> OSErr ``` |

Modified [InvokeOSLAdjustMarksUPP(_: Int, _: Int, _: UnsafePointer<AEDesc>!, _: CoreServices.OSLAdjustMarksUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1448506-invokeosladjustmarksupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeOSLAdjustMarksUPP(_ newStart: Int, _ newStop: Int, _ markToken: UnsafePointer<AEDesc>, _ userUPP: OSLAdjustMarksUPP!) -> OSErr ``` |
| To | ``` func InvokeOSLAdjustMarksUPP(_ newStart: Int, _ newStop: Int, _ markToken: UnsafePointer<AEDesc>!, _ userUPP: CoreServices.OSLAdjustMarksUPP!) -> OSErr ``` |

Modified [InvokeOSLCompareUPP(_: DescType, _: UnsafePointer<AEDesc>!, _: UnsafePointer<AEDesc>!, _: UnsafeMutablePointer<DarwinBoolean>!, _: CoreServices.OSLCompareUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1443110-invokeoslcompareupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeOSLCompareUPP(_ oper: DescType, _ obj1: UnsafePointer<AEDesc>, _ obj2: UnsafePointer<AEDesc>, _ result: UnsafeMutablePointer<DarwinBoolean>, _ userUPP: OSLCompareUPP!) -> OSErr ``` |
| To | ``` func InvokeOSLCompareUPP(_ oper: DescType, _ obj1: UnsafePointer<AEDesc>!, _ obj2: UnsafePointer<AEDesc>!, _ result: UnsafeMutablePointer<DarwinBoolean>!, _ userUPP: CoreServices.OSLCompareUPP!) -> OSErr ``` |

Modified [InvokeOSLCountUPP(_: DescType, _: DescType, _: UnsafePointer<AEDesc>!, _: UnsafeMutablePointer<Int>!, _: CoreServices.OSLCountUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1448030-invokeoslcountupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeOSLCountUPP(_ desiredType: DescType, _ containerClass: DescType, _ container: UnsafePointer<AEDesc>, _ result: UnsafeMutablePointer<Int>, _ userUPP: OSLCountUPP!) -> OSErr ``` |
| To | ``` func InvokeOSLCountUPP(_ desiredType: DescType, _ containerClass: DescType, _ container: UnsafePointer<AEDesc>!, _ result: UnsafeMutablePointer<Int>!, _ userUPP: CoreServices.OSLCountUPP!) -> OSErr ``` |

Modified [InvokeOSLDisposeTokenUPP(_: UnsafeMutablePointer<AEDesc>!, _: CoreServices.OSLDisposeTokenUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1443963-invokeosldisposetokenupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeOSLDisposeTokenUPP(_ unneededToken: UnsafeMutablePointer<AEDesc>, _ userUPP: OSLDisposeTokenUPP!) -> OSErr ``` |
| To | ``` func InvokeOSLDisposeTokenUPP(_ unneededToken: UnsafeMutablePointer<AEDesc>!, _ userUPP: CoreServices.OSLDisposeTokenUPP!) -> OSErr ``` |

Modified [InvokeOSLGetErrDescUPP(_: UnsafeMutablePointer<UnsafeMutablePointer<AEDesc>?>!, _: CoreServices.OSLGetErrDescUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1448420-invokeoslgeterrdescupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeOSLGetErrDescUPP(_ appDescPtr: UnsafeMutablePointer<UnsafeMutablePointer<AEDesc>>, _ userUPP: OSLGetErrDescUPP!) -> OSErr ``` |
| To | ``` func InvokeOSLGetErrDescUPP(_ appDescPtr: UnsafeMutablePointer<UnsafeMutablePointer<AEDesc>?>!, _ userUPP: CoreServices.OSLGetErrDescUPP!) -> OSErr ``` |

Modified [InvokeOSLGetMarkTokenUPP(_: UnsafePointer<AEDesc>!, _: DescType, _: UnsafeMutablePointer<AEDesc>!, _: CoreServices.OSLGetMarkTokenUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1441894-invokeoslgetmarktokenupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeOSLGetMarkTokenUPP(_ dContainerToken: UnsafePointer<AEDesc>, _ containerClass: DescType, _ result: UnsafeMutablePointer<AEDesc>, _ userUPP: OSLGetMarkTokenUPP!) -> OSErr ``` |
| To | ``` func InvokeOSLGetMarkTokenUPP(_ dContainerToken: UnsafePointer<AEDesc>!, _ containerClass: DescType, _ result: UnsafeMutablePointer<AEDesc>!, _ userUPP: CoreServices.OSLGetMarkTokenUPP!) -> OSErr ``` |

Modified [InvokeOSLMarkUPP(_: UnsafePointer<AEDesc>!, _: UnsafePointer<AEDesc>!, _: Int, _: CoreServices.OSLMarkUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1447444-invokeoslmarkupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeOSLMarkUPP(_ dToken: UnsafePointer<AEDesc>, _ markToken: UnsafePointer<AEDesc>, _ index: Int, _ userUPP: OSLMarkUPP!) -> OSErr ``` |
| To | ``` func InvokeOSLMarkUPP(_ dToken: UnsafePointer<AEDesc>!, _ markToken: UnsafePointer<AEDesc>!, _ index: Int, _ userUPP: CoreServices.OSLMarkUPP!) -> OSErr ``` |

Modified [IsDataAvailableInIconRef(_: OSType, _: IconRef!) -> Bool](https://developer.apple.com/documentation/coreservices/1446627-isdataavailableiniconref)

|  | Declaration |
| --- | --- |
| From | ``` func IsDataAvailableInIconRef(_ inIconKind: OSType, _ inIconRef: IconRef) -> Bool ``` |
| To | ``` func IsDataAvailableInIconRef(_ inIconKind: OSType, _ inIconRef: IconRef!) -> Bool ``` |

Modified [IsIconRefComposite(_: IconRef!, _: UnsafeMutablePointer<IconRef?>!, _: UnsafeMutablePointer<IconRef?>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1446300-isiconrefcomposite)

|  | Declaration |
| --- | --- |
| From | ``` func IsIconRefComposite(_ compositeIconRef: IconRef, _ backgroundIconRef: UnsafeMutablePointer<IconRef>, _ foregroundIconRef: UnsafeMutablePointer<IconRef>) -> OSErr ``` |
| To | ``` func IsIconRefComposite(_ compositeIconRef: IconRef!, _ backgroundIconRef: UnsafeMutablePointer<IconRef?>!, _ foregroundIconRef: UnsafeMutablePointer<IconRef?>!) -> OSErr ``` |

Modified [IsValidIconRef(_: IconRef!) -> Bool](https://developer.apple.com/documentation/coreservices/1450233-isvalidiconref)

|  | Declaration |
| --- | --- |
| From | ``` func IsValidIconRef(_ theIconRef: IconRef) -> Bool ``` |
| To | ``` func IsValidIconRef(_ theIconRef: IconRef!) -> Bool ``` |

Modified [kAEAbout](https://developer.apple.com/documentation/coreservices/1556364-anonymous/kaeabout)

|  | Declaration |
| --- | --- |
| From | ``` var kAEAbout: Int { get } ``` |
| To | ``` var kAEAbout: OSType { get } ``` |

Modified [kAEActivate](https://developer.apple.com/documentation/coreservices/1556409-kaemouseclass/kaeactivate)

|  | Declaration |
| --- | --- |
| From | ``` var kAEActivate: Int { get } ``` |
| To | ``` var kAEActivate: OSType { get } ``` |

Modified [kAEAfter](https://developer.apple.com/documentation/coreservices/1556364-anonymous/kaeafter)

|  | Declaration |
| --- | --- |
| From | ``` var kAEAfter: Int { get } ``` |
| To | ``` var kAEAfter: OSType { get } ``` |

Modified [kAEAliasSelection](https://developer.apple.com/documentation/coreservices/1556364-anonymous/kaealiasselection)

|  | Declaration |
| --- | --- |
| From | ``` var kAEAliasSelection: Int { get } ``` |
| To | ``` var kAEAliasSelection: OSType { get } ``` |

Modified [kAEAllCaps](https://developer.apple.com/documentation/coreservices/kaeallcaps)

|  | Declaration |
| --- | --- |
| From | ``` var kAEAllCaps: Int { get } ``` |
| To | ``` var kAEAllCaps: OSType { get } ``` |

Modified [kAEAnswer](https://developer.apple.com/documentation/coreservices/kaeanswer)

|  | Declaration |
| --- | --- |
| From | ``` var kAEAnswer: Int { get } ``` |
| To | ``` var kAEAnswer: AEEventID { get } ``` |

Modified [kAEApplicationClass](https://developer.apple.com/documentation/coreservices/1556409-kaemouseclass/kaeapplicationclass)

|  | Declaration |
| --- | --- |
| From | ``` var kAEApplicationClass: Int { get } ``` |
| To | ``` var kAEApplicationClass: OSType { get } ``` |

Modified [kAEApplicationDied](https://developer.apple.com/documentation/coreservices/1527223-event_id_constants/kaeapplicationdied)

|  | Declaration |
| --- | --- |
| From | ``` var kAEApplicationDied: Int { get } ``` |
| To | ``` var kAEApplicationDied: AEEventID { get } ``` |

Modified [kAEArrowAtEnd](https://developer.apple.com/documentation/coreservices/kaearrowatend)

|  | Declaration |
| --- | --- |
| From | ``` var kAEArrowAtEnd: Int { get } ``` |
| To | ``` var kAEArrowAtEnd: OSType { get } ``` |

Modified [kAEArrowAtStart](https://developer.apple.com/documentation/coreservices/1556364-anonymous/kaearrowatstart)

|  | Declaration |
| --- | --- |
| From | ``` var kAEArrowAtStart: Int { get } ``` |
| To | ``` var kAEArrowAtStart: OSType { get } ``` |

Modified [kAEArrowBothEnds](https://developer.apple.com/documentation/coreservices/1556364-anonymous/kaearrowbothends)

|  | Declaration |
| --- | --- |
| From | ``` var kAEArrowBothEnds: Int { get } ``` |
| To | ``` var kAEArrowBothEnds: OSType { get } ``` |

Modified [kAEAsk](https://developer.apple.com/documentation/coreservices/kaeask)

|  | Declaration |
| --- | --- |
| From | ``` var kAEAsk: Int { get } ``` |
| To | ``` var kAEAsk: OSType { get } ``` |

Modified [kAEAutoDown](https://developer.apple.com/documentation/coreservices/1556409-kaemouseclass/kaeautodown)

|  | Declaration |
| --- | --- |
| From | ``` var kAEAutoDown: Int { get } ``` |
| To | ``` var kAEAutoDown: OSType { get } ``` |

Modified [kAEBefore](https://developer.apple.com/documentation/coreservices/kaebefore)

|  | Declaration |
| --- | --- |
| From | ``` var kAEBefore: Int { get } ``` |
| To | ``` var kAEBefore: OSType { get } ``` |

Modified [kAEBeginning](https://developer.apple.com/documentation/coreservices/kaebeginning)

|  | Declaration |
| --- | --- |
| From | ``` var kAEBeginning: Int { get } ``` |
| To | ``` var kAEBeginning: OSType { get } ``` |

Modified [kAEBeginsWith](https://developer.apple.com/documentation/coreservices/1556394-anonymous/kaebeginswith)

|  | Declaration |
| --- | --- |
| From | ``` var kAEBeginsWith: Int { get } ``` |
| To | ``` var kAEBeginsWith: OSType { get } ``` |

Modified [kAEBeginTransaction](https://developer.apple.com/documentation/coreservices/1556394-anonymous/kaebegintransaction)

|  | Declaration |
| --- | --- |
| From | ``` var kAEBeginTransaction: Int { get } ``` |
| To | ``` var kAEBeginTransaction: OSType { get } ``` |

Modified [kAEBold](https://developer.apple.com/documentation/coreservices/1556394-anonymous/kaebold)

|  | Declaration |
| --- | --- |
| From | ``` var kAEBold: Int { get } ``` |
| To | ``` var kAEBold: OSType { get } ``` |

Modified [kAECaseSensEquals](https://developer.apple.com/documentation/coreservices/1556394-anonymous/kaecasesensequals)

|  | Declaration |
| --- | --- |
| From | ``` var kAECaseSensEquals: Int { get } ``` |
| To | ``` var kAECaseSensEquals: OSType { get } ``` |

Modified [kAECentered](https://developer.apple.com/documentation/coreservices/1556394-anonymous/kaecentered)

|  | Declaration |
| --- | --- |
| From | ``` var kAECentered: Int { get } ``` |
| To | ``` var kAECentered: OSType { get } ``` |

Modified [kAEChangeView](https://developer.apple.com/documentation/coreservices/kaechangeview)

|  | Declaration |
| --- | --- |
| From | ``` var kAEChangeView: Int { get } ``` |
| To | ``` var kAEChangeView: OSType { get } ``` |

Modified [kAEClone](https://developer.apple.com/documentation/coreservices/1556394-anonymous/kaeclone)

|  | Declaration |
| --- | --- |
| From | ``` var kAEClone: Int { get } ``` |
| To | ``` var kAEClone: OSType { get } ``` |

Modified [kAEClose](https://developer.apple.com/documentation/coreservices/kaeclose)

|  | Declaration |
| --- | --- |
| From | ``` var kAEClose: Int { get } ``` |
| To | ``` var kAEClose: OSType { get } ``` |

Modified [kAECommandClass](https://developer.apple.com/documentation/coreservices/kaecommandclass)

|  | Declaration |
| --- | --- |
| From | ``` var kAECommandClass: Int { get } ``` |
| To | ``` var kAECommandClass: OSType { get } ``` |

Modified [kAECondensed](https://developer.apple.com/documentation/coreservices/1556394-anonymous/kaecondensed)

|  | Declaration |
| --- | --- |
| From | ``` var kAECondensed: Int { get } ``` |
| To | ``` var kAECondensed: OSType { get } ``` |

Modified [kAEContains](https://developer.apple.com/documentation/coreservices/1556394-anonymous/kaecontains)

|  | Declaration |
| --- | --- |
| From | ``` var kAEContains: Int { get } ``` |
| To | ``` var kAEContains: OSType { get } ``` |

Modified [kAECopy](https://developer.apple.com/documentation/coreservices/kaecopy)

|  | Declaration |
| --- | --- |
| From | ``` var kAECopy: Int { get } ``` |
| To | ``` var kAECopy: OSType { get } ``` |

Modified [kAECoreSuite](https://developer.apple.com/documentation/coreservices/1556394-anonymous/kaecoresuite)

|  | Declaration |
| --- | --- |
| From | ``` var kAECoreSuite: Int { get } ``` |
| To | ``` var kAECoreSuite: OSType { get } ``` |

Modified [kAECountElements](https://developer.apple.com/documentation/coreservices/kaecountelements)

|  | Declaration |
| --- | --- |
| From | ``` var kAECountElements: Int { get } ``` |
| To | ``` var kAECountElements: OSType { get } ``` |

Modified [kAECreateElement](https://developer.apple.com/documentation/coreservices/1556394-anonymous/kaecreateelement)

|  | Declaration |
| --- | --- |
| From | ``` var kAECreateElement: Int { get } ``` |
| To | ``` var kAECreateElement: OSType { get } ``` |

Modified [kAECreatePublisher](https://developer.apple.com/documentation/coreservices/1556394-anonymous/kaecreatepublisher)

|  | Declaration |
| --- | --- |
| From | ``` var kAECreatePublisher: Int { get } ``` |
| To | ``` var kAECreatePublisher: OSType { get } ``` |

Modified [kAECut](https://developer.apple.com/documentation/coreservices/kaecut)

|  | Declaration |
| --- | --- |
| From | ``` var kAECut: Int { get } ``` |
| To | ``` var kAECut: OSType { get } ``` |

Modified [kAEDeactivate](https://developer.apple.com/documentation/coreservices/kaedeactivate)

|  | Declaration |
| --- | --- |
| From | ``` var kAEDeactivate: Int { get } ``` |
| To | ``` var kAEDeactivate: OSType { get } ``` |

Modified [kAEDelete](https://developer.apple.com/documentation/coreservices/kaedelete)

|  | Declaration |
| --- | --- |
| From | ``` var kAEDelete: Int { get } ``` |
| To | ``` var kAEDelete: OSType { get } ``` |

Modified [kAEDiskEvent](https://developer.apple.com/documentation/coreservices/1556409-kaemouseclass/kaediskevent)

|  | Declaration |
| --- | --- |
| From | ``` var kAEDiskEvent: Int { get } ``` |
| To | ``` var kAEDiskEvent: OSType { get } ``` |

Modified [kAEDoObjectsExist](https://developer.apple.com/documentation/coreservices/1556390-anonymous/kaedoobjectsexist)

|  | Declaration |
| --- | --- |
| From | ``` var kAEDoObjectsExist: Int { get } ``` |
| To | ``` var kAEDoObjectsExist: OSType { get } ``` |

Modified [kAEDoScript](https://developer.apple.com/documentation/coreservices/1556390-anonymous/kaedoscript)

|  | Declaration |
| --- | --- |
| From | ``` var kAEDoScript: Int { get } ``` |
| To | ``` var kAEDoScript: OSType { get } ``` |

Modified [kAEDown](https://developer.apple.com/documentation/coreservices/kaedown)

|  | Declaration |
| --- | --- |
| From | ``` var kAEDown: Int { get } ``` |
| To | ``` var kAEDown: OSType { get } ``` |

Modified [kAEDrag](https://developer.apple.com/documentation/coreservices/1556390-anonymous/kaedrag)

|  | Declaration |
| --- | --- |
| From | ``` var kAEDrag: Int { get } ``` |
| To | ``` var kAEDrag: OSType { get } ``` |

Modified [kAEDuplicateSelection](https://developer.apple.com/documentation/coreservices/kaeduplicateselection)

|  | Declaration |
| --- | --- |
| From | ``` var kAEDuplicateSelection: Int { get } ``` |
| To | ``` var kAEDuplicateSelection: OSType { get } ``` |

Modified [kAEEditGraphic](https://developer.apple.com/documentation/coreservices/kaeeditgraphic)

|  | Declaration |
| --- | --- |
| From | ``` var kAEEditGraphic: Int { get } ``` |
| To | ``` var kAEEditGraphic: OSType { get } ``` |

Modified [kAEEmptyTrash](https://developer.apple.com/documentation/coreservices/kaeemptytrash)

|  | Declaration |
| --- | --- |
| From | ``` var kAEEmptyTrash: Int { get } ``` |
| To | ``` var kAEEmptyTrash: OSType { get } ``` |

Modified [kAEEnd](https://developer.apple.com/documentation/coreservices/kaeend)

|  | Declaration |
| --- | --- |
| From | ``` var kAEEnd: Int { get } ``` |
| To | ``` var kAEEnd: OSType { get } ``` |

Modified [kAEEndsWith](https://developer.apple.com/documentation/coreservices/kaeendswith)

|  | Declaration |
| --- | --- |
| From | ``` var kAEEndsWith: Int { get } ``` |
| To | ``` var kAEEndsWith: OSType { get } ``` |

Modified [kAEEndTransaction](https://developer.apple.com/documentation/coreservices/kaeendtransaction)

|  | Declaration |
| --- | --- |
| From | ``` var kAEEndTransaction: Int { get } ``` |
| To | ``` var kAEEndTransaction: OSType { get } ``` |

Modified [kAEEquals](https://developer.apple.com/documentation/coreservices/1556390-anonymous/kaeequals)

|  | Declaration |
| --- | --- |
| From | ``` var kAEEquals: Int { get } ``` |
| To | ``` var kAEEquals: OSType { get } ``` |

Modified [kAEExpanded](https://developer.apple.com/documentation/coreservices/kaeexpanded)

|  | Declaration |
| --- | --- |
| From | ``` var kAEExpanded: Int { get } ``` |
| To | ``` var kAEExpanded: OSType { get } ``` |

Modified [kAEFast](https://developer.apple.com/documentation/coreservices/1556390-anonymous/kaefast)

|  | Declaration |
| --- | --- |
| From | ``` var kAEFast: Int { get } ``` |
| To | ``` var kAEFast: OSType { get } ``` |

Modified [kAEFinderEvents](https://developer.apple.com/documentation/coreservices/1556390-anonymous/kaefinderevents)

|  | Declaration |
| --- | --- |
| From | ``` var kAEFinderEvents: Int { get } ``` |
| To | ``` var kAEFinderEvents: OSType { get } ``` |

Modified [kAEFormulaProtect](https://developer.apple.com/documentation/coreservices/1556390-anonymous/kaeformulaprotect)

|  | Declaration |
| --- | --- |
| From | ``` var kAEFormulaProtect: Int { get } ``` |
| To | ``` var kAEFormulaProtect: OSType { get } ``` |

Modified [kAEFullyJustified](https://developer.apple.com/documentation/coreservices/1556390-anonymous/kaefullyjustified)

|  | Declaration |
| --- | --- |
| From | ``` var kAEFullyJustified: Int { get } ``` |
| To | ``` var kAEFullyJustified: OSType { get } ``` |

Modified [kAEGetClassInfo](https://developer.apple.com/documentation/coreservices/kaegetclassinfo)

|  | Declaration |
| --- | --- |
| From | ``` var kAEGetClassInfo: Int { get } ``` |
| To | ``` var kAEGetClassInfo: OSType { get } ``` |

Modified [kAEGetData](https://developer.apple.com/documentation/coreservices/kaegetdata)

|  | Declaration |
| --- | --- |
| From | ``` var kAEGetData: Int { get } ``` |
| To | ``` var kAEGetData: OSType { get } ``` |

Modified [kAEGetDataSize](https://developer.apple.com/documentation/coreservices/kaegetdatasize)

|  | Declaration |
| --- | --- |
| From | ``` var kAEGetDataSize: Int { get } ``` |
| To | ``` var kAEGetDataSize: OSType { get } ``` |

Modified [kAEGetEventInfo](https://developer.apple.com/documentation/coreservices/1556390-anonymous/kaegeteventinfo)

|  | Declaration |
| --- | --- |
| From | ``` var kAEGetEventInfo: Int { get } ``` |
| To | ``` var kAEGetEventInfo: OSType { get } ``` |

Modified [kAEGetInfoSelection](https://developer.apple.com/documentation/coreservices/1556390-anonymous/kaegetinfoselection)

|  | Declaration |
| --- | --- |
| From | ``` var kAEGetInfoSelection: Int { get } ``` |
| To | ``` var kAEGetInfoSelection: OSType { get } ``` |

Modified [kAEGetPrivilegeSelection](https://developer.apple.com/documentation/coreservices/1556403-anonymous/kaegetprivilegeselection)

|  | Declaration |
| --- | --- |
| From | ``` var kAEGetPrivilegeSelection: Int { get } ``` |
| To | ``` var kAEGetPrivilegeSelection: OSType { get } ``` |

Modified [kAEGetSuiteInfo](https://developer.apple.com/documentation/coreservices/kaegetsuiteinfo)

|  | Declaration |
| --- | --- |
| From | ``` var kAEGetSuiteInfo: Int { get } ``` |
| To | ``` var kAEGetSuiteInfo: OSType { get } ``` |

Modified [kAEGreaterThan](https://developer.apple.com/documentation/coreservices/1556403-anonymous/kaegreaterthan)

|  | Declaration |
| --- | --- |
| From | ``` var kAEGreaterThan: Int { get } ``` |
| To | ``` var kAEGreaterThan: OSType { get } ``` |

Modified [kAEGreaterThanEquals](https://developer.apple.com/documentation/coreservices/kaegreaterthanequals)

|  | Declaration |
| --- | --- |
| From | ``` var kAEGreaterThanEquals: Int { get } ``` |
| To | ``` var kAEGreaterThanEquals: OSType { get } ``` |

Modified [kAEGrow](https://developer.apple.com/documentation/coreservices/1556403-anonymous/kaegrow)

|  | Declaration |
| --- | --- |
| From | ``` var kAEGrow: Int { get } ``` |
| To | ``` var kAEGrow: OSType { get } ``` |

Modified [kAEHidden](https://developer.apple.com/documentation/coreservices/1556403-anonymous/kaehidden)

|  | Declaration |
| --- | --- |
| From | ``` var kAEHidden: Int { get } ``` |
| To | ``` var kAEHidden: OSType { get } ``` |

Modified [kAEHighLevel](https://developer.apple.com/documentation/coreservices/1556409-kaemouseclass/kaehighlevel)

|  | Declaration |
| --- | --- |
| From | ``` var kAEHighLevel: Int { get } ``` |
| To | ``` var kAEHighLevel: OSType { get } ``` |

Modified [kAEHiQuality](https://developer.apple.com/documentation/coreservices/1556403-anonymous/kaehiquality)

|  | Declaration |
| --- | --- |
| From | ``` var kAEHiQuality: Int { get } ``` |
| To | ``` var kAEHiQuality: OSType { get } ``` |

Modified [kAEImageGraphic](https://developer.apple.com/documentation/coreservices/kaeimagegraphic)

|  | Declaration |
| --- | --- |
| From | ``` var kAEImageGraphic: Int { get } ``` |
| To | ``` var kAEImageGraphic: OSType { get } ``` |

Modified [kAEInternetSuite](https://developer.apple.com/documentation/coreservices/kaeinternetsuite)

|  | Declaration |
| --- | --- |
| From | ``` var kAEInternetSuite: Int { get } ``` |
| To | ``` var kAEInternetSuite: OSType { get } ``` |

Modified [kAEISAction](https://developer.apple.com/documentation/coreservices/1556404-kaeishttpsearchargs/kaeisaction)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISAction: Int { get } ``` |
| To | ``` var kAEISAction: OSType { get } ``` |

Modified [kAEISActionPath](https://developer.apple.com/documentation/coreservices/kaeisactionpath)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISActionPath: Int { get } ``` |
| To | ``` var kAEISActionPath: OSType { get } ``` |

Modified [kAEISClientAddress](https://developer.apple.com/documentation/coreservices/kaeisclientaddress)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISClientAddress: Int { get } ``` |
| To | ``` var kAEISClientAddress: OSType { get } ``` |

Modified [kAEISClientIP](https://developer.apple.com/documentation/coreservices/1556404-kaeishttpsearchargs/kaeisclientip)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISClientIP: Int { get } ``` |
| To | ``` var kAEISClientIP: OSType { get } ``` |

Modified [kAEISContentType](https://developer.apple.com/documentation/coreservices/1556404-kaeishttpsearchargs/kaeiscontenttype)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISContentType: Int { get } ``` |
| To | ``` var kAEISContentType: OSType { get } ``` |

Modified [kAEISFromUser](https://developer.apple.com/documentation/coreservices/1556404-kaeishttpsearchargs/kaeisfromuser)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISFromUser: Int { get } ``` |
| To | ``` var kAEISFromUser: OSType { get } ``` |

Modified [kAEISFullRequest](https://developer.apple.com/documentation/coreservices/kaeisfullrequest)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISFullRequest: Int { get } ``` |
| To | ``` var kAEISFullRequest: OSType { get } ``` |

Modified [kAEISGetURL](https://developer.apple.com/documentation/coreservices/kaeisgeturl)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISGetURL: Int { get } ``` |
| To | ``` var kAEISGetURL: OSType { get } ``` |

Modified [KAEISHandleCGI](https://developer.apple.com/documentation/coreservices/kaeishandlecgi)

|  | Declaration |
| --- | --- |
| From | ``` var KAEISHandleCGI: Int { get } ``` |
| To | ``` var KAEISHandleCGI: OSType { get } ``` |

Modified [kAEISHTTPSearchArgs](https://developer.apple.com/documentation/coreservices/kaeishttpsearchargs)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISHTTPSearchArgs: Int { get } ``` |
| To | ``` var kAEISHTTPSearchArgs: OSType { get } ``` |

Modified [kAEISMethod](https://developer.apple.com/documentation/coreservices/kaeismethod)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISMethod: Int { get } ``` |
| To | ``` var kAEISMethod: OSType { get } ``` |

Modified [kAEISPassword](https://developer.apple.com/documentation/coreservices/kaeispassword)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISPassword: Int { get } ``` |
| To | ``` var kAEISPassword: OSType { get } ``` |

Modified [kAEISPostArgs](https://developer.apple.com/documentation/coreservices/kaeispostargs)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISPostArgs: Int { get } ``` |
| To | ``` var kAEISPostArgs: OSType { get } ``` |

Modified [kAEISReferrer](https://developer.apple.com/documentation/coreservices/kaeisreferrer)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISReferrer: Int { get } ``` |
| To | ``` var kAEISReferrer: OSType { get } ``` |

Modified [kAEISScriptName](https://developer.apple.com/documentation/coreservices/1556404-kaeishttpsearchargs/kaeisscriptname)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISScriptName: Int { get } ``` |
| To | ``` var kAEISScriptName: OSType { get } ``` |

Modified [kAEISServerName](https://developer.apple.com/documentation/coreservices/1556404-kaeishttpsearchargs/kaeisservername)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISServerName: Int { get } ``` |
| To | ``` var kAEISServerName: OSType { get } ``` |

Modified [kAEISServerPort](https://developer.apple.com/documentation/coreservices/kaeisserverport)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISServerPort: Int { get } ``` |
| To | ``` var kAEISServerPort: OSType { get } ``` |

Modified [kAEIsUniform](https://developer.apple.com/documentation/coreservices/kaeisuniform)

|  | Declaration |
| --- | --- |
| From | ``` var kAEIsUniform: Int { get } ``` |
| To | ``` var kAEIsUniform: OSType { get } ``` |

Modified [kAEISUserAgent](https://developer.apple.com/documentation/coreservices/1556404-kaeishttpsearchargs/kaeisuseragent)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISUserAgent: Int { get } ``` |
| To | ``` var kAEISUserAgent: OSType { get } ``` |

Modified [kAEISUserName](https://developer.apple.com/documentation/coreservices/1556404-kaeishttpsearchargs/kaeisusername)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISUserName: Int { get } ``` |
| To | ``` var kAEISUserName: OSType { get } ``` |

Modified [kAEISWebStarSuite](https://developer.apple.com/documentation/coreservices/1556388-kaeinternetsuite/kaeiswebstarsuite)

|  | Declaration |
| --- | --- |
| From | ``` var kAEISWebStarSuite: Int { get } ``` |
| To | ``` var kAEISWebStarSuite: OSType { get } ``` |

Modified [kAEItalic](https://developer.apple.com/documentation/coreservices/1556403-anonymous/kaeitalic)

|  | Declaration |
| --- | --- |
| From | ``` var kAEItalic: Int { get } ``` |
| To | ``` var kAEItalic: OSType { get } ``` |

Modified [kAEKeyClass](https://developer.apple.com/documentation/coreservices/1556409-kaemouseclass/kaekeyclass)

|  | Declaration |
| --- | --- |
| From | ``` var kAEKeyClass: Int { get } ``` |
| To | ``` var kAEKeyClass: OSType { get } ``` |

Modified [kAEKeyDown](https://developer.apple.com/documentation/coreservices/1556392-kaemenuclass/kaekeydown)

|  | Declaration |
| --- | --- |
| From | ``` var kAEKeyDown: Int { get } ``` |
| To | ``` var kAEKeyDown: OSType { get } ``` |

Modified [kAELeftJustified](https://developer.apple.com/documentation/coreservices/kaeleftjustified)

|  | Declaration |
| --- | --- |
| From | ``` var kAELeftJustified: Int { get } ``` |
| To | ``` var kAELeftJustified: OSType { get } ``` |

Modified [kAELessThan](https://developer.apple.com/documentation/coreservices/kaelessthan)

|  | Declaration |
| --- | --- |
| From | ``` var kAELessThan: Int { get } ``` |
| To | ``` var kAELessThan: OSType { get } ``` |

Modified [kAELessThanEquals](https://developer.apple.com/documentation/coreservices/1556403-anonymous/kaelessthanequals)

|  | Declaration |
| --- | --- |
| From | ``` var kAELessThanEquals: Int { get } ``` |
| To | ``` var kAELessThanEquals: OSType { get } ``` |

Modified [kAELogOut](https://developer.apple.com/documentation/coreservices/1556395-kaelogout/kaelogout)

|  | Declaration |
| --- | --- |
| From | ``` var kAELogOut: Int { get } ``` |
| To | ``` var kAELogOut: OSType { get } ``` |

Modified [kAELowercase](https://developer.apple.com/documentation/coreservices/1556403-anonymous/kaelowercase)

|  | Declaration |
| --- | --- |
| From | ``` var kAELowercase: Int { get } ``` |
| To | ``` var kAELowercase: OSType { get } ``` |

Modified [kAEMakeObjectsVisible](https://developer.apple.com/documentation/coreservices/1556403-anonymous/kaemakeobjectsvisible)

|  | Declaration |
| --- | --- |
| From | ``` var kAEMakeObjectsVisible: Int { get } ``` |
| To | ``` var kAEMakeObjectsVisible: OSType { get } ``` |

Modified [kAEMenuClass](https://developer.apple.com/documentation/coreservices/kaemenuclass)

|  | Declaration |
| --- | --- |
| From | ``` var kAEMenuClass: Int { get } ``` |
| To | ``` var kAEMenuClass: OSType { get } ``` |

Modified [kAEMenuSelect](https://developer.apple.com/documentation/coreservices/1556392-kaemenuclass/kaemenuselect)

|  | Declaration |
| --- | --- |
| From | ``` var kAEMenuSelect: Int { get } ``` |
| To | ``` var kAEMenuSelect: OSType { get } ``` |

Modified [kAEMiscStandards](https://developer.apple.com/documentation/coreservices/kaemiscstandards)

|  | Declaration |
| --- | --- |
| From | ``` var kAEMiscStandards: Int { get } ``` |
| To | ``` var kAEMiscStandards: OSType { get } ``` |

Modified [kAEModifiable](https://developer.apple.com/documentation/coreservices/1556403-anonymous/kaemodifiable)

|  | Declaration |
| --- | --- |
| From | ``` var kAEModifiable: Int { get } ``` |
| To | ``` var kAEModifiable: OSType { get } ``` |

Modified [kAEMouseClass](https://developer.apple.com/documentation/coreservices/kaemouseclass)

|  | Declaration |
| --- | --- |
| From | ``` var kAEMouseClass: Int { get } ``` |
| To | ``` var kAEMouseClass: OSType { get } ``` |

Modified [kAEMouseDown](https://developer.apple.com/documentation/coreservices/1556392-kaemenuclass/kaemousedown)

|  | Declaration |
| --- | --- |
| From | ``` var kAEMouseDown: Int { get } ``` |
| To | ``` var kAEMouseDown: OSType { get } ``` |

Modified [kAEMouseDownInBack](https://developer.apple.com/documentation/coreservices/1556392-kaemenuclass/kaemousedowninback)

|  | Declaration |
| --- | --- |
| From | ``` var kAEMouseDownInBack: Int { get } ``` |
| To | ``` var kAEMouseDownInBack: OSType { get } ``` |

Modified [kAEMove](https://developer.apple.com/documentation/coreservices/1556403-anonymous/kaemove)

|  | Declaration |
| --- | --- |
| From | ``` var kAEMove: Int { get } ``` |
| To | ``` var kAEMove: OSType { get } ``` |

Modified [kAEMoved](https://developer.apple.com/documentation/coreservices/kaemoved)

|  | Declaration |
| --- | --- |
| From | ``` var kAEMoved: Int { get } ``` |
| To | ``` var kAEMoved: OSType { get } ``` |

Modified [kAENavigationKey](https://developer.apple.com/documentation/coreservices/kaenavigationkey)

|  | Declaration |
| --- | --- |
| From | ``` var kAENavigationKey: Int { get } ``` |
| To | ``` var kAENavigationKey: OSType { get } ``` |

Modified [kAENo](https://developer.apple.com/documentation/coreservices/1556403-anonymous/kaeno)

|  | Declaration |
| --- | --- |
| From | ``` var kAENo: Int { get } ``` |
| To | ``` var kAENo: OSType { get } ``` |

Modified [kAENoArrow](https://developer.apple.com/documentation/coreservices/kaenoarrow)

|  | Declaration |
| --- | --- |
| From | ``` var kAENoArrow: Int { get } ``` |
| To | ``` var kAENoArrow: OSType { get } ``` |

Modified [kAENonmodifiable](https://developer.apple.com/documentation/coreservices/1556386-kaenonmodifiable/kaenonmodifiable)

|  | Declaration |
| --- | --- |
| From | ``` var kAENonmodifiable: Int { get } ``` |
| To | ``` var kAENonmodifiable: OSType { get } ``` |

Modified [kAENotifyRecording](https://developer.apple.com/documentation/coreservices/1527224-apple_event_recording_event_id_c/kaenotifyrecording)

|  | Declaration |
| --- | --- |
| From | ``` var kAENotifyRecording: Int { get } ``` |
| To | ``` var kAENotifyRecording: AEEventID { get } ``` |

Modified [kAENotifyStartRecording](https://developer.apple.com/documentation/coreservices/kaenotifystartrecording)

|  | Declaration |
| --- | --- |
| From | ``` var kAENotifyStartRecording: Int { get } ``` |
| To | ``` var kAENotifyStartRecording: AEEventID { get } ``` |

Modified [kAENotifyStopRecording](https://developer.apple.com/documentation/coreservices/1527224-apple_event_recording_event_id_c/kaenotifystoprecording)

|  | Declaration |
| --- | --- |
| From | ``` var kAENotifyStopRecording: Int { get } ``` |
| To | ``` var kAENotifyStopRecording: AEEventID { get } ``` |

Modified [kAENullEvent](https://developer.apple.com/documentation/coreservices/1556409-kaemouseclass/kaenullevent)

|  | Declaration |
| --- | --- |
| From | ``` var kAENullEvent: Int { get } ``` |
| To | ``` var kAENullEvent: OSType { get } ``` |

Modified [kAEOpen](https://developer.apple.com/documentation/coreservices/kaeopen)

|  | Declaration |
| --- | --- |
| From | ``` var kAEOpen: Int { get } ``` |
| To | ``` var kAEOpen: OSType { get } ``` |

Modified [kAEOpenApplication](https://developer.apple.com/documentation/coreservices/1527223-event_id_constants/kaeopenapplication)

|  | Declaration |
| --- | --- |
| From | ``` var kAEOpenApplication: Int { get } ``` |
| To | ``` var kAEOpenApplication: AEEventID { get } ``` |

Modified [kAEOpenContents](https://developer.apple.com/documentation/coreservices/1527223-event_id_constants/kaeopencontents)

|  | Declaration |
| --- | --- |
| From | ``` var kAEOpenContents: Int { get } ``` |
| To | ``` var kAEOpenContents: AEEventID { get } ``` |

Modified [kAEOpenDocuments](https://developer.apple.com/documentation/coreservices/kaeopendocuments)

|  | Declaration |
| --- | --- |
| From | ``` var kAEOpenDocuments: Int { get } ``` |
| To | ``` var kAEOpenDocuments: AEEventID { get } ``` |

Modified [kAEOpenSelection](https://developer.apple.com/documentation/coreservices/kaeopenselection)

|  | Declaration |
| --- | --- |
| From | ``` var kAEOpenSelection: Int { get } ``` |
| To | ``` var kAEOpenSelection: OSType { get } ``` |

Modified [kAEOSAXSizeResource](https://developer.apple.com/documentation/coreservices/1457902-kaeuserterminology/kaeosaxsizeresource)

|  | Declaration |
| --- | --- |
| From | ``` var kAEOSAXSizeResource: Int { get } ``` |
| To | ``` var kAEOSAXSizeResource: OSType { get } ``` |

Modified [kAEOutline](https://developer.apple.com/documentation/coreservices/kaeoutline)

|  | Declaration |
| --- | --- |
| From | ``` var kAEOutline: Int { get } ``` |
| To | ``` var kAEOutline: OSType { get } ``` |

Modified [kAEPageSetup](https://developer.apple.com/documentation/coreservices/kaepagesetup)

|  | Declaration |
| --- | --- |
| From | ``` var kAEPageSetup: Int { get } ``` |
| To | ``` var kAEPageSetup: OSType { get } ``` |

Modified [kAEPaste](https://developer.apple.com/documentation/coreservices/kaepaste)

|  | Declaration |
| --- | --- |
| From | ``` var kAEPaste: Int { get } ``` |
| To | ``` var kAEPaste: OSType { get } ``` |

Modified [kAEPlain](https://developer.apple.com/documentation/coreservices/1556386-kaenonmodifiable/kaeplain)

|  | Declaration |
| --- | --- |
| From | ``` var kAEPlain: Int { get } ``` |
| To | ``` var kAEPlain: OSType { get } ``` |

Modified [kAEPrint](https://developer.apple.com/documentation/coreservices/kaeprint)

|  | Declaration |
| --- | --- |
| From | ``` var kAEPrint: Int { get } ``` |
| To | ``` var kAEPrint: OSType { get } ``` |

Modified [kAEPrintDocuments](https://developer.apple.com/documentation/coreservices/1527223-event_id_constants/kaeprintdocuments)

|  | Declaration |
| --- | --- |
| From | ``` var kAEPrintDocuments: Int { get } ``` |
| To | ``` var kAEPrintDocuments: AEEventID { get } ``` |

Modified [kAEPrintSelection](https://developer.apple.com/documentation/coreservices/1556386-kaenonmodifiable/kaeprintselection)

|  | Declaration |
| --- | --- |
| From | ``` var kAEPrintSelection: Int { get } ``` |
| To | ``` var kAEPrintSelection: OSType { get } ``` |

Modified [kAEPrintWindow](https://developer.apple.com/documentation/coreservices/kaeprintwindow)

|  | Declaration |
| --- | --- |
| From | ``` var kAEPrintWindow: Int { get } ``` |
| To | ``` var kAEPrintWindow: OSType { get } ``` |

Modified [kAEPromise](https://developer.apple.com/documentation/coreservices/1556392-kaemenuclass/kaepromise)

|  | Declaration |
| --- | --- |
| From | ``` var kAEPromise: Int { get } ``` |
| To | ``` var kAEPromise: OSType { get } ``` |

Modified [kAEPutAwaySelection](https://developer.apple.com/documentation/coreservices/kaeputawayselection)

|  | Declaration |
| --- | --- |
| From | ``` var kAEPutAwaySelection: Int { get } ``` |
| To | ``` var kAEPutAwaySelection: OSType { get } ``` |

Modified [kAEQDAddOver](https://developer.apple.com/documentation/coreservices/kaeqdaddover)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQDAddOver: Int { get } ``` |
| To | ``` var kAEQDAddOver: OSType { get } ``` |

Modified [kAEQDAddPin](https://developer.apple.com/documentation/coreservices/kaeqdaddpin)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQDAddPin: Int { get } ``` |
| To | ``` var kAEQDAddPin: OSType { get } ``` |

Modified [kAEQDAdMax](https://developer.apple.com/documentation/coreservices/kaeqdadmax)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQDAdMax: Int { get } ``` |
| To | ``` var kAEQDAdMax: OSType { get } ``` |

Modified [kAEQDAdMin](https://developer.apple.com/documentation/coreservices/kaeqdadmin)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQDAdMin: Int { get } ``` |
| To | ``` var kAEQDAdMin: OSType { get } ``` |

Modified [kAEQDBic](https://developer.apple.com/documentation/coreservices/1556386-kaenonmodifiable/kaeqdbic)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQDBic: Int { get } ``` |
| To | ``` var kAEQDBic: OSType { get } ``` |

Modified [kAEQDBlend](https://developer.apple.com/documentation/coreservices/1556386-kaenonmodifiable/kaeqdblend)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQDBlend: Int { get } ``` |
| To | ``` var kAEQDBlend: OSType { get } ``` |

Modified [kAEQDCopy](https://developer.apple.com/documentation/coreservices/1556386-kaenonmodifiable/kaeqdcopy)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQDCopy: Int { get } ``` |
| To | ``` var kAEQDCopy: OSType { get } ``` |

Modified [kAEQDNotBic](https://developer.apple.com/documentation/coreservices/kaeqdnotbic)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQDNotBic: Int { get } ``` |
| To | ``` var kAEQDNotBic: OSType { get } ``` |

Modified [kAEQDNotCopy](https://developer.apple.com/documentation/coreservices/kaeqdnotcopy)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQDNotCopy: Int { get } ``` |
| To | ``` var kAEQDNotCopy: OSType { get } ``` |

Modified [kAEQDNotOr](https://developer.apple.com/documentation/coreservices/kaeqdnotor)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQDNotOr: Int { get } ``` |
| To | ``` var kAEQDNotOr: OSType { get } ``` |

Modified [kAEQDNotXor](https://developer.apple.com/documentation/coreservices/1556377-kaeqdnotor/kaeqdnotxor)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQDNotXor: Int { get } ``` |
| To | ``` var kAEQDNotXor: OSType { get } ``` |

Modified [kAEQDOr](https://developer.apple.com/documentation/coreservices/1556377-kaeqdnotor/kaeqdor)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQDOr: Int { get } ``` |
| To | ``` var kAEQDOr: OSType { get } ``` |

Modified [kAEQDSubOver](https://developer.apple.com/documentation/coreservices/kaeqdsubover)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQDSubOver: Int { get } ``` |
| To | ``` var kAEQDSubOver: OSType { get } ``` |

Modified [kAEQDSubPin](https://developer.apple.com/documentation/coreservices/1556377-kaeqdnotor/kaeqdsubpin)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQDSubPin: Int { get } ``` |
| To | ``` var kAEQDSubPin: OSType { get } ``` |

Modified [kAEQDSupplementalSuite](https://developer.apple.com/documentation/coreservices/kaeqdsupplementalsuite)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQDSupplementalSuite: Int { get } ``` |
| To | ``` var kAEQDSupplementalSuite: OSType { get } ``` |

Modified [kAEQDXor](https://developer.apple.com/documentation/coreservices/1556377-kaeqdnotor/kaeqdxor)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQDXor: Int { get } ``` |
| To | ``` var kAEQDXor: OSType { get } ``` |

Modified [kAEQuickdrawSuite](https://developer.apple.com/documentation/coreservices/1556377-kaeqdnotor/kaequickdrawsuite)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQuickdrawSuite: Int { get } ``` |
| To | ``` var kAEQuickdrawSuite: OSType { get } ``` |

Modified [kAEQuitAll](https://developer.apple.com/documentation/coreservices/1556377-kaeqdnotor/kaequitall)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQuitAll: Int { get } ``` |
| To | ``` var kAEQuitAll: OSType { get } ``` |

Modified [kAEQuitApplication](https://developer.apple.com/documentation/coreservices/1527223-event_id_constants/kaequitapplication)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQuitApplication: Int { get } ``` |
| To | ``` var kAEQuitApplication: AEEventID { get } ``` |

Modified [kAEQuitPreserveState](https://developer.apple.com/documentation/coreservices/kaequitpreservestate)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQuitPreserveState: Int { get } ``` |
| To | ``` var kAEQuitPreserveState: OSType { get } ``` |

Modified [kAEQuitReason](https://developer.apple.com/documentation/coreservices/1556363-anonymous/kaequitreason)

|  | Declaration |
| --- | --- |
| From | ``` var kAEQuitReason: Int { get } ``` |
| To | ``` var kAEQuitReason: OSType { get } ``` |

Modified [kAERawKey](https://developer.apple.com/documentation/coreservices/1556409-kaemouseclass/kaerawkey)

|  | Declaration |
| --- | --- |
| From | ``` var kAERawKey: Int { get } ``` |
| To | ``` var kAERawKey: OSType { get } ``` |

Modified [kAEReallyLogOut](https://developer.apple.com/documentation/coreservices/kaereallylogout)

|  | Declaration |
| --- | --- |
| From | ``` var kAEReallyLogOut: Int { get } ``` |
| To | ``` var kAEReallyLogOut: OSType { get } ``` |

Modified [kAERedo](https://developer.apple.com/documentation/coreservices/kaeredo)

|  | Declaration |
| --- | --- |
| From | ``` var kAERedo: Int { get } ``` |
| To | ``` var kAERedo: OSType { get } ``` |

Modified [kAERegular](https://developer.apple.com/documentation/coreservices/1556377-kaeqdnotor/kaeregular)

|  | Declaration |
| --- | --- |
| From | ``` var kAERegular: Int { get } ``` |
| To | ``` var kAERegular: OSType { get } ``` |

Modified [kAEReopenApplication](https://developer.apple.com/documentation/coreservices/kaereopenapplication)

|  | Declaration |
| --- | --- |
| From | ``` var kAEReopenApplication: Int { get } ``` |
| To | ``` var kAEReopenApplication: OSType { get } ``` |

Modified [kAEReplace](https://developer.apple.com/documentation/coreservices/1556377-kaeqdnotor/kaereplace)

|  | Declaration |
| --- | --- |
| From | ``` var kAEReplace: Int { get } ``` |
| To | ``` var kAEReplace: OSType { get } ``` |

Modified [kAERequiredSuite](https://developer.apple.com/documentation/coreservices/kaerequiredsuite)

|  | Declaration |
| --- | --- |
| From | ``` var kAERequiredSuite: Int { get } ``` |
| To | ``` var kAERequiredSuite: OSType { get } ``` |

Modified [kAEResized](https://developer.apple.com/documentation/coreservices/kaeresized)

|  | Declaration |
| --- | --- |
| From | ``` var kAEResized: Int { get } ``` |
| To | ``` var kAEResized: OSType { get } ``` |

Modified [kAERestart](https://developer.apple.com/documentation/coreservices/1556377-kaeqdnotor/kaerestart)

|  | Declaration |
| --- | --- |
| From | ``` var kAERestart: Int { get } ``` |
| To | ``` var kAERestart: OSType { get } ``` |

Modified [kAEResume](https://developer.apple.com/documentation/coreservices/1556409-kaemouseclass/kaeresume)

|  | Declaration |
| --- | --- |
| From | ``` var kAEResume: Int { get } ``` |
| To | ``` var kAEResume: OSType { get } ``` |

Modified [kAERevealSelection](https://developer.apple.com/documentation/coreservices/1556377-kaeqdnotor/kaerevealselection)

|  | Declaration |
| --- | --- |
| From | ``` var kAERevealSelection: Int { get } ``` |
| To | ``` var kAERevealSelection: OSType { get } ``` |

Modified [kAERevert](https://developer.apple.com/documentation/coreservices/1556377-kaeqdnotor/kaerevert)

|  | Declaration |
| --- | --- |
| From | ``` var kAERevert: Int { get } ``` |
| To | ``` var kAERevert: OSType { get } ``` |

Modified [kAERightJustified](https://developer.apple.com/documentation/coreservices/kaerightjustified)

|  | Declaration |
| --- | --- |
| From | ``` var kAERightJustified: Int { get } ``` |
| To | ``` var kAERightJustified: OSType { get } ``` |

Modified [kAERPCClass](https://developer.apple.com/documentation/coreservices/1542780-keyusernameattr/kaerpcclass)

|  | Declaration |
| --- | --- |
| From | ``` var kAERPCClass: Int { get } ``` |
| To | ``` var kAERPCClass: AEKeyword { get } ``` |

Modified [kAESave](https://developer.apple.com/documentation/coreservices/1556377-kaeqdnotor/kaesave)

|  | Declaration |
| --- | --- |
| From | ``` var kAESave: Int { get } ``` |
| To | ``` var kAESave: OSType { get } ``` |

Modified [kAEScrapEvent](https://developer.apple.com/documentation/coreservices/1556409-kaemouseclass/kaescrapevent)

|  | Declaration |
| --- | --- |
| From | ``` var kAEScrapEvent: Int { get } ``` |
| To | ``` var kAEScrapEvent: OSType { get } ``` |

Modified [kAEScriptingSizeResource](https://developer.apple.com/documentation/coreservices/kaescriptingsizeresource)

|  | Declaration |
| --- | --- |
| From | ``` var kAEScriptingSizeResource: Int { get } ``` |
| To | ``` var kAEScriptingSizeResource: OSType { get } ``` |

Modified [kAESelect](https://developer.apple.com/documentation/coreservices/kaeselect)

|  | Declaration |
| --- | --- |
| From | ``` var kAESelect: Int { get } ``` |
| To | ``` var kAESelect: OSType { get } ``` |

Modified [kAESetData](https://developer.apple.com/documentation/coreservices/1556377-kaeqdnotor/kaesetdata)

|  | Declaration |
| --- | --- |
| From | ``` var kAESetData: Int { get } ``` |
| To | ``` var kAESetData: OSType { get } ``` |

Modified [kAESetPosition](https://developer.apple.com/documentation/coreservices/kaesetposition)

|  | Declaration |
| --- | --- |
| From | ``` var kAESetPosition: Int { get } ``` |
| To | ``` var kAESetPosition: OSType { get } ``` |

Modified [kAEShadow](https://developer.apple.com/documentation/coreservices/kaeshadow)

|  | Declaration |
| --- | --- |
| From | ``` var kAEShadow: Int { get } ``` |
| To | ``` var kAEShadow: OSType { get } ``` |

Modified [kAESharedScriptHandler](https://developer.apple.com/documentation/coreservices/1542780-keyusernameattr/kaesharedscripthandler)

|  | Declaration |
| --- | --- |
| From | ``` var kAESharedScriptHandler: Int { get } ``` |
| To | ``` var kAESharedScriptHandler: AEKeyword { get } ``` |

Modified [kAEShowClipboard](https://developer.apple.com/documentation/coreservices/1556407-kaesetposition/kaeshowclipboard)

|  | Declaration |
| --- | --- |
| From | ``` var kAEShowClipboard: Int { get } ``` |
| To | ``` var kAEShowClipboard: OSType { get } ``` |

Modified [kAEShowPreferences](https://developer.apple.com/documentation/coreservices/kaeshowpreferences)

|  | Declaration |
| --- | --- |
| From | ``` var kAEShowPreferences: Int { get } ``` |
| To | ``` var kAEShowPreferences: AEEventID { get } ``` |

Modified [kAEShowRestartDialog](https://developer.apple.com/documentation/coreservices/1556395-kaelogout/kaeshowrestartdialog)

|  | Declaration |
| --- | --- |
| From | ``` var kAEShowRestartDialog: Int { get } ``` |
| To | ``` var kAEShowRestartDialog: OSType { get } ``` |

Modified [kAEShowShutdownDialog](https://developer.apple.com/documentation/coreservices/kaeshowshutdowndialog)

|  | Declaration |
| --- | --- |
| From | ``` var kAEShowShutdownDialog: Int { get } ``` |
| To | ``` var kAEShowShutdownDialog: OSType { get } ``` |

Modified [kAEShutDown](https://developer.apple.com/documentation/coreservices/1556407-kaesetposition/kaeshutdown)

|  | Declaration |
| --- | --- |
| From | ``` var kAEShutDown: Int { get } ``` |
| To | ``` var kAEShutDown: OSType { get } ``` |

Modified [kAESleep](https://developer.apple.com/documentation/coreservices/kaesleep)

|  | Declaration |
| --- | --- |
| From | ``` var kAESleep: Int { get } ``` |
| To | ``` var kAESleep: OSType { get } ``` |

Modified [kAESmallCaps](https://developer.apple.com/documentation/coreservices/1556407-kaesetposition/kaesmallcaps)

|  | Declaration |
| --- | --- |
| From | ``` var kAESmallCaps: Int { get } ``` |
| To | ``` var kAESmallCaps: OSType { get } ``` |

Modified [kAESOAPScheme](https://developer.apple.com/documentation/coreservices/kaesoapscheme)

|  | Declaration |
| --- | --- |
| From | ``` var kAESOAPScheme: Int { get } ``` |
| To | ``` var kAESOAPScheme: AEKeyword { get } ``` |

Modified [kAESpecialClassProperties](https://developer.apple.com/documentation/coreservices/kaespecialclassproperties)

|  | Declaration |
| --- | --- |
| From | ``` var kAESpecialClassProperties: Int { get } ``` |
| To | ``` var kAESpecialClassProperties: OSType { get } ``` |

Modified [kAEStartRecording](https://developer.apple.com/documentation/coreservices/1527224-apple_event_recording_event_id_c/kaestartrecording)

|  | Declaration |
| --- | --- |
| From | ``` var kAEStartRecording: Int { get } ``` |
| To | ``` var kAEStartRecording: AEEventID { get } ``` |

Modified [kAEStoppedMoving](https://developer.apple.com/documentation/coreservices/1556409-kaemouseclass/kaestoppedmoving)

|  | Declaration |
| --- | --- |
| From | ``` var kAEStoppedMoving: Int { get } ``` |
| To | ``` var kAEStoppedMoving: OSType { get } ``` |

Modified [kAEStopRecording](https://developer.apple.com/documentation/coreservices/kaestoprecording)

|  | Declaration |
| --- | --- |
| From | ``` var kAEStopRecording: Int { get } ``` |
| To | ``` var kAEStopRecording: AEEventID { get } ``` |

Modified [kAEStrikethrough](https://developer.apple.com/documentation/coreservices/1556407-kaesetposition/kaestrikethrough)

|  | Declaration |
| --- | --- |
| From | ``` var kAEStrikethrough: Int { get } ``` |
| To | ``` var kAEStrikethrough: OSType { get } ``` |

Modified [kAESubscript](https://developer.apple.com/documentation/coreservices/kaesubscript)

|  | Declaration |
| --- | --- |
| From | ``` var kAESubscript: Int { get } ``` |
| To | ``` var kAESubscript: OSType { get } ``` |

Modified [kAESuperscript](https://developer.apple.com/documentation/coreservices/1556407-kaesetposition/kaesuperscript)

|  | Declaration |
| --- | --- |
| From | ``` var kAESuperscript: Int { get } ``` |
| To | ``` var kAESuperscript: OSType { get } ``` |

Modified [kAESuspend](https://developer.apple.com/documentation/coreservices/kaesuspend)

|  | Declaration |
| --- | --- |
| From | ``` var kAESuspend: Int { get } ``` |
| To | ``` var kAESuspend: OSType { get } ``` |

Modified [kAETableSuite](https://developer.apple.com/documentation/coreservices/1556407-kaesetposition/kaetablesuite)

|  | Declaration |
| --- | --- |
| From | ``` var kAETableSuite: Int { get } ``` |
| To | ``` var kAETableSuite: OSType { get } ``` |

Modified [kAETerminologyExtension](https://developer.apple.com/documentation/coreservices/kaeterminologyextension)

|  | Declaration |
| --- | --- |
| From | ``` var kAETerminologyExtension: Int { get } ``` |
| To | ``` var kAETerminologyExtension: OSType { get } ``` |

Modified [kAETextSuite](https://developer.apple.com/documentation/coreservices/kaetextsuite)

|  | Declaration |
| --- | --- |
| From | ``` var kAETextSuite: Int { get } ``` |
| To | ``` var kAETextSuite: OSType { get } ``` |

Modified [kAETransactionTerminated](https://developer.apple.com/documentation/coreservices/kaetransactionterminated)

|  | Declaration |
| --- | --- |
| From | ``` var kAETransactionTerminated: Int { get } ``` |
| To | ``` var kAETransactionTerminated: OSType { get } ``` |

Modified [kAEUnderline](https://developer.apple.com/documentation/coreservices/1556407-kaesetposition/kaeunderline)

|  | Declaration |
| --- | --- |
| From | ``` var kAEUnderline: Int { get } ``` |
| To | ``` var kAEUnderline: OSType { get } ``` |

Modified [kAEUndo](https://developer.apple.com/documentation/coreservices/kaeundo)

|  | Declaration |
| --- | --- |
| From | ``` var kAEUndo: Int { get } ``` |
| To | ``` var kAEUndo: OSType { get } ``` |

Modified [kAEUp](https://developer.apple.com/documentation/coreservices/1556409-kaemouseclass/kaeup)

|  | Declaration |
| --- | --- |
| From | ``` var kAEUp: Int { get } ``` |
| To | ``` var kAEUp: OSType { get } ``` |

Modified [kAEUpdate](https://developer.apple.com/documentation/coreservices/kaeupdate)

|  | Declaration |
| --- | --- |
| From | ``` var kAEUpdate: Int { get } ``` |
| To | ``` var kAEUpdate: OSType { get } ``` |

Modified [kAEUserTerminology](https://developer.apple.com/documentation/coreservices/kaeuserterminology)

|  | Declaration |
| --- | --- |
| From | ``` var kAEUserTerminology: Int { get } ``` |
| To | ``` var kAEUserTerminology: OSType { get } ``` |

Modified [kAEVirtualKey](https://developer.apple.com/documentation/coreservices/kaevirtualkey)

|  | Declaration |
| --- | --- |
| From | ``` var kAEVirtualKey: Int { get } ``` |
| To | ``` var kAEVirtualKey: OSType { get } ``` |

Modified [kAEWakeUpEvent](https://developer.apple.com/documentation/coreservices/1556409-kaemouseclass/kaewakeupevent)

|  | Declaration |
| --- | --- |
| From | ``` var kAEWakeUpEvent: Int { get } ``` |
| To | ``` var kAEWakeUpEvent: OSType { get } ``` |

Modified [kAEWholeWordEquals](https://developer.apple.com/documentation/coreservices/kaewholewordequals)

|  | Declaration |
| --- | --- |
| From | ``` var kAEWholeWordEquals: Int { get } ``` |
| To | ``` var kAEWholeWordEquals: OSType { get } ``` |

Modified [kAEWindowClass](https://developer.apple.com/documentation/coreservices/kaewindowclass)

|  | Declaration |
| --- | --- |
| From | ``` var kAEWindowClass: Int { get } ``` |
| To | ``` var kAEWindowClass: OSType { get } ``` |

Modified [kAEXMLRPCScheme](https://developer.apple.com/documentation/coreservices/1542780-keyusernameattr/kaexmlrpcscheme)

|  | Declaration |
| --- | --- |
| From | ``` var kAEXMLRPCScheme: Int { get } ``` |
| To | ``` var kAEXMLRPCScheme: AEKeyword { get } ``` |

Modified [kAEYes](https://developer.apple.com/documentation/coreservices/kaeyes)

|  | Declaration |
| --- | --- |
| From | ``` var kAEYes: Int { get } ``` |
| To | ``` var kAEYes: OSType { get } ``` |

Modified [kAEZoom](https://developer.apple.com/documentation/coreservices/1556407-kaesetposition/kaezoom)

|  | Declaration |
| --- | --- |
| From | ``` var kAEZoom: Int { get } ``` |
| To | ``` var kAEZoom: OSType { get } ``` |

Modified [kConnSuite](https://developer.apple.com/documentation/coreservices/kconnsuite)

|  | Declaration |
| --- | --- |
| From | ``` var kConnSuite: Int { get } ``` |
| To | ``` var kConnSuite: OSType { get } ``` |

Modified [kCoreEventClass](https://developer.apple.com/documentation/coreservices/kcoreeventclass)

|  | Declaration |
| --- | --- |
| From | ``` var kCoreEventClass: Int { get } ``` |
| To | ``` var kCoreEventClass: DescType { get } ``` |

Modified [kDoFolderActionEvent](https://developer.apple.com/documentation/coreservices/1556384-kfaserverapp/kdofolderactionevent)

|  | Declaration |
| --- | --- |
| From | ``` var kDoFolderActionEvent: Int { get } ``` |
| To | ``` var kDoFolderActionEvent: OSType { get } ``` |

Modified [keyAcceptTimeoutAttr](https://developer.apple.com/documentation/coreservices/keyaccepttimeoutattr)

|  | Declaration |
| --- | --- |
| From | ``` var keyAcceptTimeoutAttr: Int { get } ``` |
| To | ``` var keyAcceptTimeoutAttr: AEKeyword { get } ``` |

Modified [keyActualSenderAuditToken](https://developer.apple.com/documentation/coreservices/keyactualsenderaudittoken)

|  | Declaration |
| --- | --- |
| From | ``` var keyActualSenderAuditToken: Int { get } ``` |
| To | ``` var keyActualSenderAuditToken: AEKeyword { get } ``` |

Modified [keyAdditionalHTTPHeaders](https://developer.apple.com/documentation/coreservices/1542780-keyusernameattr/keyadditionalhttpheaders)

|  | Declaration |
| --- | --- |
| From | ``` var keyAdditionalHTTPHeaders: Int { get } ``` |
| To | ``` var keyAdditionalHTTPHeaders: AEKeyword { get } ``` |

Modified [keyAddressAttr](https://developer.apple.com/documentation/coreservices/1542920-keyword_attribute_constants/keyaddressattr)

|  | Declaration |
| --- | --- |
| From | ``` var keyAddressAttr: Int { get } ``` |
| To | ``` var keyAddressAttr: AEKeyword { get } ``` |

Modified [keyAEAdjustMarksProc](https://developer.apple.com/documentation/coreservices/keyaeadjustmarksproc)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEAdjustMarksProc: Int { get } ``` |
| To | ``` var keyAEAdjustMarksProc: AEKeyword { get } ``` |

Modified [keyAEAngle](https://developer.apple.com/documentation/coreservices/keyaeangle)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEAngle: Int { get } ``` |
| To | ``` var keyAEAngle: AEKeyword { get } ``` |

Modified [keyAEArcAngle](https://developer.apple.com/documentation/coreservices/1556380-keyaeangle/keyaearcangle)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEArcAngle: Int { get } ``` |
| To | ``` var keyAEArcAngle: AEKeyword { get } ``` |

Modified [keyAEBaseAddr](https://developer.apple.com/documentation/coreservices/keyaebaseaddr)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEBaseAddr: Int { get } ``` |
| To | ``` var keyAEBaseAddr: AEKeyword { get } ``` |

Modified [keyAEBestType](https://developer.apple.com/documentation/coreservices/1556383-keyaebaseaddr/keyaebesttype)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEBestType: Int { get } ``` |
| To | ``` var keyAEBestType: AEKeyword { get } ``` |

Modified [keyAEBgndColor](https://developer.apple.com/documentation/coreservices/1556383-keyaebaseaddr/keyaebgndcolor)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEBgndColor: Int { get } ``` |
| To | ``` var keyAEBgndColor: AEKeyword { get } ``` |

Modified [keyAEBgndPattern](https://developer.apple.com/documentation/coreservices/keyaebgndpattern)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEBgndPattern: Int { get } ``` |
| To | ``` var keyAEBgndPattern: AEKeyword { get } ``` |

Modified [keyAEBounds](https://developer.apple.com/documentation/coreservices/1556383-keyaebaseaddr/keyaebounds)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEBounds: Int { get } ``` |
| To | ``` var keyAEBounds: AEKeyword { get } ``` |

Modified [keyAEBufferSize](https://developer.apple.com/documentation/coreservices/1556406-ktextserviceclass/keyaebuffersize)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEBufferSize: Int { get } ``` |
| To | ``` var keyAEBufferSize: OSType { get } ``` |

Modified [keyAECellList](https://developer.apple.com/documentation/coreservices/keyaecelllist)

|  | Declaration |
| --- | --- |
| From | ``` var keyAECellList: Int { get } ``` |
| To | ``` var keyAECellList: AEKeyword { get } ``` |

Modified [keyAEClassID](https://developer.apple.com/documentation/coreservices/keyaeclassid)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEClassID: Int { get } ``` |
| To | ``` var keyAEClassID: AEKeyword { get } ``` |

Modified [keyAEClauseOffsets](https://developer.apple.com/documentation/coreservices/1556379-keyaehiliterange/keyaeclauseoffsets)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEClauseOffsets: Int { get } ``` |
| To | ``` var keyAEClauseOffsets: AEKeyword { get } ``` |

Modified [keyAEColor](https://developer.apple.com/documentation/coreservices/keyaecolor)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEColor: Int { get } ``` |
| To | ``` var keyAEColor: AEKeyword { get } ``` |

Modified [keyAEColorTable](https://developer.apple.com/documentation/coreservices/1556383-keyaebaseaddr/keyaecolortable)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEColorTable: Int { get } ``` |
| To | ``` var keyAEColorTable: AEKeyword { get } ``` |

Modified [keyAECompareProc](https://developer.apple.com/documentation/coreservices/1572726-special_handler_callback_constan/keyaecompareproc)

|  | Declaration |
| --- | --- |
| From | ``` var keyAECompareProc: Int { get } ``` |
| To | ``` var keyAECompareProc: AEKeyword { get } ``` |

Modified [keyAECountProc](https://developer.apple.com/documentation/coreservices/keyaecountproc)

|  | Declaration |
| --- | --- |
| From | ``` var keyAECountProc: Int { get } ``` |
| To | ``` var keyAECountProc: AEKeyword { get } ``` |

Modified [keyAECurrentPoint](https://developer.apple.com/documentation/coreservices/1556406-ktextserviceclass/keyaecurrentpoint)

|  | Declaration |
| --- | --- |
| From | ``` var keyAECurrentPoint: Int { get } ``` |
| To | ``` var keyAECurrentPoint: OSType { get } ``` |

Modified [keyAECurveHeight](https://developer.apple.com/documentation/coreservices/keyaecurveheight)

|  | Declaration |
| --- | --- |
| From | ``` var keyAECurveHeight: Int { get } ``` |
| To | ``` var keyAECurveHeight: AEKeyword { get } ``` |

Modified [keyAECurveWidth](https://developer.apple.com/documentation/coreservices/1556383-keyaebaseaddr/keyaecurvewidth)

|  | Declaration |
| --- | --- |
| From | ``` var keyAECurveWidth: Int { get } ``` |
| To | ``` var keyAECurveWidth: AEKeyword { get } ``` |

Modified [keyAEDashStyle](https://developer.apple.com/documentation/coreservices/1556383-keyaebaseaddr/keyaedashstyle)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEDashStyle: Int { get } ``` |
| To | ``` var keyAEDashStyle: AEKeyword { get } ``` |

Modified [keyAEData](https://developer.apple.com/documentation/coreservices/1556383-keyaebaseaddr/keyaedata)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEData: Int { get } ``` |
| To | ``` var keyAEData: AEKeyword { get } ``` |

Modified [keyAEDefaultType](https://developer.apple.com/documentation/coreservices/keyaedefaulttype)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEDefaultType: Int { get } ``` |
| To | ``` var keyAEDefaultType: AEKeyword { get } ``` |

Modified [keyAEDefinitionRect](https://developer.apple.com/documentation/coreservices/keyaedefinitionrect)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEDefinitionRect: Int { get } ``` |
| To | ``` var keyAEDefinitionRect: AEKeyword { get } ``` |

Modified [keyAEDescType](https://developer.apple.com/documentation/coreservices/keyaedesctype)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEDescType: Int { get } ``` |
| To | ``` var keyAEDescType: AEKeyword { get } ``` |

Modified [keyAEDestination](https://developer.apple.com/documentation/coreservices/1556383-keyaebaseaddr/keyaedestination)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEDestination: Int { get } ``` |
| To | ``` var keyAEDestination: AEKeyword { get } ``` |

Modified [keyAEDoAntiAlias](https://developer.apple.com/documentation/coreservices/keyaedoantialias)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEDoAntiAlias: Int { get } ``` |
| To | ``` var keyAEDoAntiAlias: AEKeyword { get } ``` |

Modified [keyAEDoDithered](https://developer.apple.com/documentation/coreservices/keyaedodithered)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEDoDithered: Int { get } ``` |
| To | ``` var keyAEDoDithered: AEKeyword { get } ``` |

Modified [keyAEDoRotate](https://developer.apple.com/documentation/coreservices/1556383-keyaebaseaddr/keyaedorotate)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEDoRotate: Int { get } ``` |
| To | ``` var keyAEDoRotate: AEKeyword { get } ``` |

Modified [keyAEDoScale](https://developer.apple.com/documentation/coreservices/1556387-keyaedoscale/keyaedoscale)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEDoScale: Int { get } ``` |
| To | ``` var keyAEDoScale: AEKeyword { get } ``` |

Modified [keyAEDoTranslate](https://developer.apple.com/documentation/coreservices/1556387-keyaedoscale/keyaedotranslate)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEDoTranslate: Int { get } ``` |
| To | ``` var keyAEDoTranslate: AEKeyword { get } ``` |

Modified [keyAEDragging](https://developer.apple.com/documentation/coreservices/keyaedragging)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEDragging: Int { get } ``` |
| To | ``` var keyAEDragging: AEKeyword { get } ``` |

Modified [keyAEEditionFileLoc](https://developer.apple.com/documentation/coreservices/1556387-keyaedoscale/keyaeeditionfileloc)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEEditionFileLoc: Int { get } ``` |
| To | ``` var keyAEEditionFileLoc: AEKeyword { get } ``` |

Modified [keyAEElements](https://developer.apple.com/documentation/coreservices/1556387-keyaedoscale/keyaeelements)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEElements: Int { get } ``` |
| To | ``` var keyAEElements: AEKeyword { get } ``` |

Modified [keyAEEndPoint](https://developer.apple.com/documentation/coreservices/1556387-keyaedoscale/keyaeendpoint)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEEndPoint: Int { get } ``` |
| To | ``` var keyAEEndPoint: AEKeyword { get } ``` |

Modified [keyAEEventClass](https://developer.apple.com/documentation/coreservices/1556387-keyaedoscale/keyaeeventclass)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEEventClass: Int { get } ``` |
| To | ``` var keyAEEventClass: AEKeyword { get } ``` |

Modified [keyAEEventID](https://developer.apple.com/documentation/coreservices/1556387-keyaedoscale/keyaeeventid)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEEventID: Int { get } ``` |
| To | ``` var keyAEEventID: AEKeyword { get } ``` |

Modified [keyAEFile](https://developer.apple.com/documentation/coreservices/1556387-keyaedoscale/keyaefile)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEFile: Int { get } ``` |
| To | ``` var keyAEFile: AEKeyword { get } ``` |

Modified [keyAEFileType](https://developer.apple.com/documentation/coreservices/1556387-keyaedoscale/keyaefiletype)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEFileType: Int { get } ``` |
| To | ``` var keyAEFileType: AEKeyword { get } ``` |

Modified [keyAEFillColor](https://developer.apple.com/documentation/coreservices/keyaefillcolor)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEFillColor: Int { get } ``` |
| To | ``` var keyAEFillColor: AEKeyword { get } ``` |

Modified [keyAEFillPattern](https://developer.apple.com/documentation/coreservices/keyaefillpattern)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEFillPattern: Int { get } ``` |
| To | ``` var keyAEFillPattern: AEKeyword { get } ``` |

Modified [keyAEFixLength](https://developer.apple.com/documentation/coreservices/keyaefixlength)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEFixLength: Int { get } ``` |
| To | ``` var keyAEFixLength: OSType { get } ``` |

Modified [keyAEFlipHorizontal](https://developer.apple.com/documentation/coreservices/1556387-keyaedoscale/keyaefliphorizontal)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEFlipHorizontal: Int { get } ``` |
| To | ``` var keyAEFlipHorizontal: AEKeyword { get } ``` |

Modified [keyAEFlipVertical](https://developer.apple.com/documentation/coreservices/keyaeflipvertical)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEFlipVertical: Int { get } ``` |
| To | ``` var keyAEFlipVertical: AEKeyword { get } ``` |

Modified [keyAEFont](https://developer.apple.com/documentation/coreservices/1556387-keyaedoscale/keyaefont)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEFont: Int { get } ``` |
| To | ``` var keyAEFont: AEKeyword { get } ``` |

Modified [keyAEFormula](https://developer.apple.com/documentation/coreservices/1556387-keyaedoscale/keyaeformula)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEFormula: Int { get } ``` |
| To | ``` var keyAEFormula: AEKeyword { get } ``` |

Modified [keyAEGetErrDescProc](https://developer.apple.com/documentation/coreservices/keyaegeterrdescproc)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEGetErrDescProc: Int { get } ``` |
| To | ``` var keyAEGetErrDescProc: AEKeyword { get } ``` |

Modified [keyAEGraphicObjects](https://developer.apple.com/documentation/coreservices/keyaegraphicobjects)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEGraphicObjects: Int { get } ``` |
| To | ``` var keyAEGraphicObjects: AEKeyword { get } ``` |

Modified [keyAEHiliteRange](https://developer.apple.com/documentation/coreservices/keyaehiliterange)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEHiliteRange: Int { get } ``` |
| To | ``` var keyAEHiliteRange: AEKeyword { get } ``` |

Modified [keyAEID](https://developer.apple.com/documentation/coreservices/1556387-keyaedoscale/keyaeid)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEID: Int { get } ``` |
| To | ``` var keyAEID: AEKeyword { get } ``` |

Modified [keyAEImageQuality](https://developer.apple.com/documentation/coreservices/keyaeimagequality)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEImageQuality: Int { get } ``` |
| To | ``` var keyAEImageQuality: AEKeyword { get } ``` |

Modified [keyAEInsertHere](https://developer.apple.com/documentation/coreservices/1556387-keyaedoscale/keyaeinserthere)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEInsertHere: Int { get } ``` |
| To | ``` var keyAEInsertHere: AEKeyword { get } ``` |

Modified [keyAEKeyForms](https://developer.apple.com/documentation/coreservices/keyaekeyforms)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEKeyForms: Int { get } ``` |
| To | ``` var keyAEKeyForms: AEKeyword { get } ``` |

Modified [keyAEKeyword](https://developer.apple.com/documentation/coreservices/keyaekeyword)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEKeyword: Int { get } ``` |
| To | ``` var keyAEKeyword: AEKeyword { get } ``` |

Modified [keyAELaunchedAsLogInItem](https://developer.apple.com/documentation/coreservices/1556410-launch_apple_event_constants/keyaelaunchedasloginitem)

|  | Declaration |
| --- | --- |
| From | ``` var keyAELaunchedAsLogInItem: Int { get } ``` |
| To | ``` var keyAELaunchedAsLogInItem: AEKeyword { get } ``` |

Modified [keyAELaunchedAsServiceItem](https://developer.apple.com/documentation/coreservices/1556410-launch_apple_event_constants/keyaelaunchedasserviceitem)

|  | Declaration |
| --- | --- |
| From | ``` var keyAELaunchedAsServiceItem: Int { get } ``` |
| To | ``` var keyAELaunchedAsServiceItem: AEKeyword { get } ``` |

Modified [keyAELeftSide](https://developer.apple.com/documentation/coreservices/1556379-keyaehiliterange/keyaeleftside)

|  | Declaration |
| --- | --- |
| From | ``` var keyAELeftSide: Int { get } ``` |
| To | ``` var keyAELeftSide: AEKeyword { get } ``` |

Modified [keyAELevel](https://developer.apple.com/documentation/coreservices/keyaelevel)

|  | Declaration |
| --- | --- |
| From | ``` var keyAELevel: Int { get } ``` |
| To | ``` var keyAELevel: AEKeyword { get } ``` |

Modified [keyAELineArrow](https://developer.apple.com/documentation/coreservices/keyaelinearrow)

|  | Declaration |
| --- | --- |
| From | ``` var keyAELineArrow: Int { get } ``` |
| To | ``` var keyAELineArrow: AEKeyword { get } ``` |

Modified [keyAEMarkProc](https://developer.apple.com/documentation/coreservices/keyaemarkproc)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEMarkProc: Int { get } ``` |
| To | ``` var keyAEMarkProc: AEKeyword { get } ``` |

Modified [keyAEMarkTokenProc](https://developer.apple.com/documentation/coreservices/keyaemarktokenproc)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEMarkTokenProc: Int { get } ``` |
| To | ``` var keyAEMarkTokenProc: AEKeyword { get } ``` |

Modified [keyAEMoveView](https://developer.apple.com/documentation/coreservices/keyaemoveview)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEMoveView: Int { get } ``` |
| To | ``` var keyAEMoveView: OSType { get } ``` |

Modified [keyAEName](https://developer.apple.com/documentation/coreservices/keyaename)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEName: Int { get } ``` |
| To | ``` var keyAEName: AEKeyword { get } ``` |

Modified [keyAENewElementLoc](https://developer.apple.com/documentation/coreservices/keyaenewelementloc)

|  | Declaration |
| --- | --- |
| From | ``` var keyAENewElementLoc: Int { get } ``` |
| To | ``` var keyAENewElementLoc: AEKeyword { get } ``` |

Modified [keyAENextBody](https://developer.apple.com/documentation/coreservices/1556406-ktextserviceclass/keyaenextbody)

|  | Declaration |
| --- | --- |
| From | ``` var keyAENextBody: Int { get } ``` |
| To | ``` var keyAENextBody: OSType { get } ``` |

Modified [keyAEObject](https://developer.apple.com/documentation/coreservices/keyaeobject)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEObject: Int { get } ``` |
| To | ``` var keyAEObject: AEKeyword { get } ``` |

Modified [keyAEObjectClass](https://developer.apple.com/documentation/coreservices/1556374-keyaekeyword/keyaeobjectclass)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEObjectClass: Int { get } ``` |
| To | ``` var keyAEObjectClass: AEKeyword { get } ``` |

Modified [keyAEOffset](https://developer.apple.com/documentation/coreservices/keyaeoffset)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEOffset: Int { get } ``` |
| To | ``` var keyAEOffset: AEKeyword { get } ``` |

Modified [keyAEOffStyles](https://developer.apple.com/documentation/coreservices/1556374-keyaekeyword/keyaeoffstyles)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEOffStyles: Int { get } ``` |
| To | ``` var keyAEOffStyles: AEKeyword { get } ``` |

Modified [keyAEOnStyles](https://developer.apple.com/documentation/coreservices/1556374-keyaekeyword/keyaeonstyles)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEOnStyles: Int { get } ``` |
| To | ``` var keyAEOnStyles: AEKeyword { get } ``` |

Modified [keyAEParameters](https://developer.apple.com/documentation/coreservices/keyaeparameters)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEParameters: Int { get } ``` |
| To | ``` var keyAEParameters: AEKeyword { get } ``` |

Modified [keyAEParamFlags](https://developer.apple.com/documentation/coreservices/keyaeparamflags)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEParamFlags: Int { get } ``` |
| To | ``` var keyAEParamFlags: AEKeyword { get } ``` |

Modified [keyAEPenColor](https://developer.apple.com/documentation/coreservices/1556374-keyaekeyword/keyaepencolor)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEPenColor: Int { get } ``` |
| To | ``` var keyAEPenColor: AEKeyword { get } ``` |

Modified [keyAEPenPattern](https://developer.apple.com/documentation/coreservices/1556374-keyaekeyword/keyaepenpattern)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEPenPattern: Int { get } ``` |
| To | ``` var keyAEPenPattern: AEKeyword { get } ``` |

Modified [keyAEPenWidth](https://developer.apple.com/documentation/coreservices/keyaepenwidth)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEPenWidth: Int { get } ``` |
| To | ``` var keyAEPenWidth: AEKeyword { get } ``` |

Modified [keyAEPinRange](https://developer.apple.com/documentation/coreservices/keyaepinrange)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEPinRange: Int { get } ``` |
| To | ``` var keyAEPinRange: AEKeyword { get } ``` |

Modified [keyAEPixelDepth](https://developer.apple.com/documentation/coreservices/keyaepixeldepth)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEPixelDepth: Int { get } ``` |
| To | ``` var keyAEPixelDepth: AEKeyword { get } ``` |

Modified [keyAEPixMapMinus](https://developer.apple.com/documentation/coreservices/keyaepixmapminus)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEPixMapMinus: Int { get } ``` |
| To | ``` var keyAEPixMapMinus: AEKeyword { get } ``` |

Modified [keyAEPMTable](https://developer.apple.com/documentation/coreservices/1556374-keyaekeyword/keyaepmtable)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEPMTable: Int { get } ``` |
| To | ``` var keyAEPMTable: AEKeyword { get } ``` |

Modified [keyAEPoint](https://developer.apple.com/documentation/coreservices/1556379-keyaehiliterange/keyaepoint)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEPoint: Int { get } ``` |
| To | ``` var keyAEPoint: AEKeyword { get } ``` |

Modified [keyAEPointList](https://developer.apple.com/documentation/coreservices/1556374-keyaekeyword/keyaepointlist)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEPointList: Int { get } ``` |
| To | ``` var keyAEPointList: AEKeyword { get } ``` |

Modified [keyAEPointSize](https://developer.apple.com/documentation/coreservices/1556374-keyaekeyword/keyaepointsize)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEPointSize: Int { get } ``` |
| To | ``` var keyAEPointSize: AEKeyword { get } ``` |

Modified [keyAEPosition](https://developer.apple.com/documentation/coreservices/1556374-keyaekeyword/keyaeposition)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEPosition: Int { get } ``` |
| To | ``` var keyAEPosition: AEKeyword { get } ``` |

Modified [keyAEPOSTHeaderData](https://developer.apple.com/documentation/coreservices/keyaepostheaderdata)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEPOSTHeaderData: Int { get } ``` |
| To | ``` var keyAEPOSTHeaderData: AEKeyword { get } ``` |

Modified [keyAEPropData](https://developer.apple.com/documentation/coreservices/1556378-anonymous/keyaepropdata)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEPropData: Int { get } ``` |
| To | ``` var keyAEPropData: AEKeyword { get } ``` |

Modified [keyAEProperties](https://developer.apple.com/documentation/coreservices/keyaeproperties)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEProperties: Int { get } ``` |
| To | ``` var keyAEProperties: AEKeyword { get } ``` |

Modified [keyAEProperty](https://developer.apple.com/documentation/coreservices/keyaeproperty)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEProperty: Int { get } ``` |
| To | ``` var keyAEProperty: AEKeyword { get } ``` |

Modified [keyAEPropFlags](https://developer.apple.com/documentation/coreservices/1556378-anonymous/keyaepropflags)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEPropFlags: Int { get } ``` |
| To | ``` var keyAEPropFlags: AEKeyword { get } ``` |

Modified [keyAEPropID](https://developer.apple.com/documentation/coreservices/1556378-anonymous/keyaepropid)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEPropID: Int { get } ``` |
| To | ``` var keyAEPropID: AEKeyword { get } ``` |

Modified [keyAEProtection](https://developer.apple.com/documentation/coreservices/1556378-anonymous/keyaeprotection)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEProtection: Int { get } ``` |
| To | ``` var keyAEProtection: AEKeyword { get } ``` |

Modified [keyAERangeStart](https://developer.apple.com/documentation/coreservices/1572726-special_handler_callback_constan/keyaerangestart)

|  | Declaration |
| --- | --- |
| From | ``` var keyAERangeStart: Int { get } ``` |
| To | ``` var keyAERangeStart: AEKeyword { get } ``` |

Modified [keyAERangeStop](https://developer.apple.com/documentation/coreservices/1572726-special_handler_callback_constan/keyaerangestop)

|  | Declaration |
| --- | --- |
| From | ``` var keyAERangeStop: Int { get } ``` |
| To | ``` var keyAERangeStop: AEKeyword { get } ``` |

Modified [keyAERecorderCount](https://developer.apple.com/documentation/coreservices/keyaerecordercount)

|  | Declaration |
| --- | --- |
| From | ``` var keyAERecorderCount: Int { get } ``` |
| To | ``` var keyAERecorderCount: AEKeyword { get } ``` |

Modified [keyAERegionClass](https://developer.apple.com/documentation/coreservices/1556379-keyaehiliterange/keyaeregionclass)

|  | Declaration |
| --- | --- |
| From | ``` var keyAERegionClass: Int { get } ``` |
| To | ``` var keyAERegionClass: AEKeyword { get } ``` |

Modified [keyAERenderAs](https://developer.apple.com/documentation/coreservices/1556378-anonymous/keyaerenderas)

|  | Declaration |
| --- | --- |
| From | ``` var keyAERenderAs: Int { get } ``` |
| To | ``` var keyAERenderAs: AEKeyword { get } ``` |

Modified [keyAEReplyHeaderData](https://developer.apple.com/documentation/coreservices/keyaereplyheaderdata)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEReplyHeaderData: Int { get } ``` |
| To | ``` var keyAEReplyHeaderData: AEKeyword { get } ``` |

Modified [keyAERequestedType](https://developer.apple.com/documentation/coreservices/keyaerequestedtype)

|  | Declaration |
| --- | --- |
| From | ``` var keyAERequestedType: Int { get } ``` |
| To | ``` var keyAERequestedType: AEKeyword { get } ``` |

Modified [keyAEResult](https://developer.apple.com/documentation/coreservices/keyaeresult)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEResult: Int { get } ``` |
| To | ``` var keyAEResult: AEKeyword { get } ``` |

Modified [keyAEResultInfo](https://developer.apple.com/documentation/coreservices/1556378-anonymous/keyaeresultinfo)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEResultInfo: Int { get } ``` |
| To | ``` var keyAEResultInfo: AEKeyword { get } ``` |

Modified [keyAERotation](https://developer.apple.com/documentation/coreservices/1556378-anonymous/keyaerotation)

|  | Declaration |
| --- | --- |
| From | ``` var keyAERotation: Int { get } ``` |
| To | ``` var keyAERotation: AEKeyword { get } ``` |

Modified [keyAERotPoint](https://developer.apple.com/documentation/coreservices/1556378-anonymous/keyaerotpoint)

|  | Declaration |
| --- | --- |
| From | ``` var keyAERotPoint: Int { get } ``` |
| To | ``` var keyAERotPoint: AEKeyword { get } ``` |

Modified [keyAERowList](https://developer.apple.com/documentation/coreservices/1556378-anonymous/keyaerowlist)

|  | Declaration |
| --- | --- |
| From | ``` var keyAERowList: Int { get } ``` |
| To | ``` var keyAERowList: AEKeyword { get } ``` |

Modified [keyAESaveOptions](https://developer.apple.com/documentation/coreservices/keyaesaveoptions)

|  | Declaration |
| --- | --- |
| From | ``` var keyAESaveOptions: Int { get } ``` |
| To | ``` var keyAESaveOptions: AEKeyword { get } ``` |

Modified [keyAEScale](https://developer.apple.com/documentation/coreservices/1556378-anonymous/keyaescale)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEScale: Int { get } ``` |
| To | ``` var keyAEScale: AEKeyword { get } ``` |

Modified [keyAEScriptTag](https://developer.apple.com/documentation/coreservices/keyaescripttag)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEScriptTag: Int { get } ``` |
| To | ``` var keyAEScriptTag: AEKeyword { get } ``` |

Modified [keyAESearchText](https://developer.apple.com/documentation/coreservices/keyaesearchtext)

|  | Declaration |
| --- | --- |
| From | ``` var keyAESearchText: Int { get } ``` |
| To | ``` var keyAESearchText: AEKeyword { get } ``` |

Modified [keyAEServerInstance](https://developer.apple.com/documentation/coreservices/1556406-ktextserviceclass/keyaeserverinstance)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEServerInstance: Int { get } ``` |
| To | ``` var keyAEServerInstance: OSType { get } ``` |

Modified [keyAEShowWhere](https://developer.apple.com/documentation/coreservices/1556378-anonymous/keyaeshowwhere)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEShowWhere: Int { get } ``` |
| To | ``` var keyAEShowWhere: AEKeyword { get } ``` |

Modified [keyAEStartAngle](https://developer.apple.com/documentation/coreservices/1556378-anonymous/keyaestartangle)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEStartAngle: Int { get } ``` |
| To | ``` var keyAEStartAngle: AEKeyword { get } ``` |

Modified [keyAEStartPoint](https://developer.apple.com/documentation/coreservices/keyaestartpoint)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEStartPoint: Int { get } ``` |
| To | ``` var keyAEStartPoint: AEKeyword { get } ``` |

Modified [keyAEStyles](https://developer.apple.com/documentation/coreservices/keyaestyles)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEStyles: Int { get } ``` |
| To | ``` var keyAEStyles: AEKeyword { get } ``` |

Modified [keyAESuiteID](https://developer.apple.com/documentation/coreservices/1556370-keyaesuiteid/keyaesuiteid)

|  | Declaration |
| --- | --- |
| From | ``` var keyAESuiteID: Int { get } ``` |
| To | ``` var keyAESuiteID: AEKeyword { get } ``` |

Modified [keyAEText](https://developer.apple.com/documentation/coreservices/keyaetext)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEText: Int { get } ``` |
| To | ``` var keyAEText: AEKeyword { get } ``` |

Modified [keyAETextColor](https://developer.apple.com/documentation/coreservices/keyaetextcolor)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETextColor: Int { get } ``` |
| To | ``` var keyAETextColor: AEKeyword { get } ``` |

Modified [keyAETextFont](https://developer.apple.com/documentation/coreservices/keyaetextfont)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETextFont: Int { get } ``` |
| To | ``` var keyAETextFont: AEKeyword { get } ``` |

Modified [keyAETextLineAscent](https://developer.apple.com/documentation/coreservices/1556370-keyaesuiteid/keyaetextlineascent)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETextLineAscent: Int { get } ``` |
| To | ``` var keyAETextLineAscent: AEKeyword { get } ``` |

Modified [keyAETextLineHeight](https://developer.apple.com/documentation/coreservices/1556370-keyaesuiteid/keyaetextlineheight)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETextLineHeight: Int { get } ``` |
| To | ``` var keyAETextLineHeight: AEKeyword { get } ``` |

Modified [keyAETextPointSize](https://developer.apple.com/documentation/coreservices/keyaetextpointsize)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETextPointSize: Int { get } ``` |
| To | ``` var keyAETextPointSize: AEKeyword { get } ``` |

Modified [keyAETextServiceEncoding](https://developer.apple.com/documentation/coreservices/keyaetextserviceencoding)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETextServiceEncoding: Int { get } ``` |
| To | ``` var keyAETextServiceEncoding: OSType { get } ``` |

Modified [keyAETextServiceMacEncoding](https://developer.apple.com/documentation/coreservices/1556406-ktextserviceclass/keyaetextservicemacencoding)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETextServiceMacEncoding: Int { get } ``` |
| To | ``` var keyAETextServiceMacEncoding: OSType { get } ``` |

Modified [keyAETextStyles](https://developer.apple.com/documentation/coreservices/1556370-keyaesuiteid/keyaetextstyles)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETextStyles: Int { get } ``` |
| To | ``` var keyAETextStyles: AEKeyword { get } ``` |

Modified [keyAETheData](https://developer.apple.com/documentation/coreservices/keyaethedata)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETheData: Int { get } ``` |
| To | ``` var keyAETheData: OSType { get } ``` |

Modified [keyAETheText](https://developer.apple.com/documentation/coreservices/1556370-keyaesuiteid/keyaethetext)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETheText: Int { get } ``` |
| To | ``` var keyAETheText: AEKeyword { get } ``` |

Modified [keyAETransferMode](https://developer.apple.com/documentation/coreservices/1556370-keyaesuiteid/keyaetransfermode)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETransferMode: Int { get } ``` |
| To | ``` var keyAETransferMode: AEKeyword { get } ``` |

Modified [keyAETranslation](https://developer.apple.com/documentation/coreservices/keyaetranslation)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETranslation: Int { get } ``` |
| To | ``` var keyAETranslation: AEKeyword { get } ``` |

Modified [keyAETryAsStructGraf](https://developer.apple.com/documentation/coreservices/keyaetryasstructgraf)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETryAsStructGraf: Int { get } ``` |
| To | ``` var keyAETryAsStructGraf: AEKeyword { get } ``` |

Modified [keyAETSMDocumentRefcon](https://developer.apple.com/documentation/coreservices/keyaetsmdocumentrefcon)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETSMDocumentRefcon: Int { get } ``` |
| To | ``` var keyAETSMDocumentRefcon: OSType { get } ``` |

Modified [keyAETSMEventRecord](https://developer.apple.com/documentation/coreservices/1556406-ktextserviceclass/keyaetsmeventrecord)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETSMEventRecord: Int { get } ``` |
| To | ``` var keyAETSMEventRecord: OSType { get } ``` |

Modified [keyAETSMEventRef](https://developer.apple.com/documentation/coreservices/1556406-ktextserviceclass/keyaetsmeventref)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETSMEventRef: Int { get } ``` |
| To | ``` var keyAETSMEventRef: OSType { get } ``` |

Modified [keyAETSMGlyphInfoArray](https://developer.apple.com/documentation/coreservices/keyaetsmglyphinfoarray)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETSMGlyphInfoArray: Int { get } ``` |
| To | ``` var keyAETSMGlyphInfoArray: OSType { get } ``` |

Modified [keyAETSMScriptTag](https://developer.apple.com/documentation/coreservices/1556406-ktextserviceclass/keyaetsmscripttag)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETSMScriptTag: Int { get } ``` |
| To | ``` var keyAETSMScriptTag: OSType { get } ``` |

Modified [keyAETSMTextFMFont](https://developer.apple.com/documentation/coreservices/1556406-ktextserviceclass/keyaetsmtextfmfont)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETSMTextFMFont: Int { get } ``` |
| To | ``` var keyAETSMTextFMFont: OSType { get } ``` |

Modified [keyAETSMTextFont](https://developer.apple.com/documentation/coreservices/keyaetsmtextfont)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETSMTextFont: Int { get } ``` |
| To | ``` var keyAETSMTextFont: OSType { get } ``` |

Modified [keyAETSMTextPointSize](https://developer.apple.com/documentation/coreservices/1556406-ktextserviceclass/keyaetsmtextpointsize)

|  | Declaration |
| --- | --- |
| From | ``` var keyAETSMTextPointSize: Int { get } ``` |
| To | ``` var keyAETSMTextPointSize: OSType { get } ``` |

Modified [keyAEUniformStyles](https://developer.apple.com/documentation/coreservices/keyaeuniformstyles)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEUniformStyles: Int { get } ``` |
| To | ``` var keyAEUniformStyles: AEKeyword { get } ``` |

Modified [keyAEUpdateOn](https://developer.apple.com/documentation/coreservices/1556370-keyaesuiteid/keyaeupdateon)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEUpdateOn: Int { get } ``` |
| To | ``` var keyAEUpdateOn: AEKeyword { get } ``` |

Modified [keyAEUpdateRange](https://developer.apple.com/documentation/coreservices/1556406-ktextserviceclass/keyaeupdaterange)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEUpdateRange: Int { get } ``` |
| To | ``` var keyAEUpdateRange: OSType { get } ``` |

Modified [keyAEUserTerm](https://developer.apple.com/documentation/coreservices/keyaeuserterm)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEUserTerm: Int { get } ``` |
| To | ``` var keyAEUserTerm: AEKeyword { get } ``` |

Modified [keyAEVersion](https://developer.apple.com/documentation/coreservices/keyaeversion)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEVersion: Int { get } ``` |
| To | ``` var keyAEVersion: AEKeyword { get } ``` |

Modified [keyAEWindow](https://developer.apple.com/documentation/coreservices/1556370-keyaesuiteid/keyaewindow)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEWindow: Int { get } ``` |
| To | ``` var keyAEWindow: AEKeyword { get } ``` |

Modified [keyAEWritingCode](https://developer.apple.com/documentation/coreservices/1556370-keyaesuiteid/keyaewritingcode)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEWritingCode: Int { get } ``` |
| To | ``` var keyAEWritingCode: AEKeyword { get } ``` |

Modified [keyAEXMLReplyData](https://developer.apple.com/documentation/coreservices/keyaexmlreplydata)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEXMLReplyData: Int { get } ``` |
| To | ``` var keyAEXMLReplyData: AEKeyword { get } ``` |

Modified [keyAEXMLRequestData](https://developer.apple.com/documentation/coreservices/1542780-keyusernameattr/keyaexmlrequestdata)

|  | Declaration |
| --- | --- |
| From | ``` var keyAEXMLRequestData: Int { get } ``` |
| To | ``` var keyAEXMLRequestData: AEKeyword { get } ``` |

Modified [keyCloseAllWindows](https://developer.apple.com/documentation/coreservices/1556381-keymenuid/keycloseallwindows)

|  | Declaration |
| --- | --- |
| From | ``` var keyCloseAllWindows: Int { get } ``` |
| To | ``` var keyCloseAllWindows: AEKeyword { get } ``` |

Modified [keyDirectObject](https://developer.apple.com/documentation/coreservices/1527206-keyword_parameter_constants/keydirectobject)

|  | Declaration |
| --- | --- |
| From | ``` var keyDirectObject: Int { get } ``` |
| To | ``` var keyDirectObject: AEKeyword { get } ``` |

Modified [keyDisableAuthenticationAttr](https://developer.apple.com/documentation/coreservices/keydisableauthenticationattr)

|  | Declaration |
| --- | --- |
| From | ``` var keyDisableAuthenticationAttr: Int { get } ``` |
| To | ``` var keyDisableAuthenticationAttr: AEKeyword { get } ``` |

Modified [keyDisposeTokenProc](https://developer.apple.com/documentation/coreservices/keydisposetokenproc)

|  | Declaration |
| --- | --- |
| From | ``` var keyDisposeTokenProc: Int { get } ``` |
| To | ``` var keyDisposeTokenProc: AEKeyword { get } ``` |

Modified [keyDriveNumber](https://developer.apple.com/documentation/coreservices/1556399-keymiscellaneous/keydrivenumber)

|  | Declaration |
| --- | --- |
| From | ``` var keyDriveNumber: Int { get } ``` |
| To | ``` var keyDriveNumber: AEKeyword { get } ``` |

Modified [keyErrorCode](https://developer.apple.com/documentation/coreservices/1556399-keymiscellaneous/keyerrorcode)

|  | Declaration |
| --- | --- |
| From | ``` var keyErrorCode: Int { get } ``` |
| To | ``` var keyErrorCode: AEKeyword { get } ``` |

Modified [keyErrorNumber](https://developer.apple.com/documentation/coreservices/1527206-keyword_parameter_constants/keyerrornumber)

|  | Declaration |
| --- | --- |
| From | ``` var keyErrorNumber: Int { get } ``` |
| To | ``` var keyErrorNumber: AEKeyword { get } ``` |

Modified [keyErrorString](https://developer.apple.com/documentation/coreservices/keyerrorstring)

|  | Declaration |
| --- | --- |
| From | ``` var keyErrorString: Int { get } ``` |
| To | ``` var keyErrorString: AEKeyword { get } ``` |

Modified [keyEventClassAttr](https://developer.apple.com/documentation/coreservices/1542920-keyword_attribute_constants/keyeventclassattr)

|  | Declaration |
| --- | --- |
| From | ``` var keyEventClassAttr: Int { get } ``` |
| To | ``` var keyEventClassAttr: AEKeyword { get } ``` |

Modified [keyEventIDAttr](https://developer.apple.com/documentation/coreservices/1542920-keyword_attribute_constants/keyeventidattr)

|  | Declaration |
| --- | --- |
| From | ``` var keyEventIDAttr: Int { get } ``` |
| To | ``` var keyEventIDAttr: AEKeyword { get } ``` |

Modified [keyEventSourceAttr](https://developer.apple.com/documentation/coreservices/1542920-keyword_attribute_constants/keyeventsourceattr)

|  | Declaration |
| --- | --- |
| From | ``` var keyEventSourceAttr: Int { get } ``` |
| To | ``` var keyEventSourceAttr: AEKeyword { get } ``` |

Modified [keyHighLevelClass](https://developer.apple.com/documentation/coreservices/keyhighlevelclass)

|  | Declaration |
| --- | --- |
| From | ``` var keyHighLevelClass: Int { get } ``` |
| To | ``` var keyHighLevelClass: AEKeyword { get } ``` |

Modified [keyHighLevelID](https://developer.apple.com/documentation/coreservices/1556399-keymiscellaneous/keyhighlevelid)

|  | Declaration |
| --- | --- |
| From | ``` var keyHighLevelID: Int { get } ``` |
| To | ``` var keyHighLevelID: AEKeyword { get } ``` |

Modified [keyInteractLevelAttr](https://developer.apple.com/documentation/coreservices/1542920-keyword_attribute_constants/keyinteractlevelattr)

|  | Declaration |
| --- | --- |
| From | ``` var keyInteractLevelAttr: Int { get } ``` |
| To | ``` var keyInteractLevelAttr: AEKeyword { get } ``` |

Modified [keyKey](https://developer.apple.com/documentation/coreservices/keykey)

|  | Declaration |
| --- | --- |
| From | ``` var keyKey: Int { get } ``` |
| To | ``` var keyKey: AEKeyword { get } ``` |

Modified [keyKeyboard](https://developer.apple.com/documentation/coreservices/keykeyboard)

|  | Declaration |
| --- | --- |
| From | ``` var keyKeyboard: Int { get } ``` |
| To | ``` var keyKeyboard: AEKeyword { get } ``` |

Modified [keyKeyCode](https://developer.apple.com/documentation/coreservices/keykeycode)

|  | Declaration |
| --- | --- |
| From | ``` var keyKeyCode: Int { get } ``` |
| To | ``` var keyKeyCode: AEKeyword { get } ``` |

Modified [keyLocalWhere](https://developer.apple.com/documentation/coreservices/1556381-keymenuid/keylocalwhere)

|  | Declaration |
| --- | --- |
| From | ``` var keyLocalWhere: Int { get } ``` |
| To | ``` var keyLocalWhere: AEKeyword { get } ``` |

Modified [keyMenuID](https://developer.apple.com/documentation/coreservices/keymenuid)

|  | Declaration |
| --- | --- |
| From | ``` var keyMenuID: Int { get } ``` |
| To | ``` var keyMenuID: AEKeyword { get } ``` |

Modified [keyMenuItem](https://developer.apple.com/documentation/coreservices/keymenuitem)

|  | Declaration |
| --- | --- |
| From | ``` var keyMenuItem: Int { get } ``` |
| To | ``` var keyMenuItem: AEKeyword { get } ``` |

Modified [keyMiscellaneous](https://developer.apple.com/documentation/coreservices/1556399-keymiscellaneous/keymiscellaneous)

|  | Declaration |
| --- | --- |
| From | ``` var keyMiscellaneous: Int { get } ``` |
| To | ``` var keyMiscellaneous: AEKeyword { get } ``` |

Modified [keyMissedKeywordAttr](https://developer.apple.com/documentation/coreservices/keymissedkeywordattr)

|  | Declaration |
| --- | --- |
| From | ``` var keyMissedKeywordAttr: Int { get } ``` |
| To | ``` var keyMissedKeywordAttr: AEKeyword { get } ``` |

Modified [keyModifiers](https://developer.apple.com/documentation/coreservices/1556399-keymiscellaneous/keymodifiers)

|  | Declaration |
| --- | --- |
| From | ``` var keyModifiers: Int { get } ``` |
| To | ``` var keyModifiers: AEKeyword { get } ``` |

Modified [keyNewBounds](https://developer.apple.com/documentation/coreservices/keynewbounds)

|  | Declaration |
| --- | --- |
| From | ``` var keyNewBounds: Int { get } ``` |
| To | ``` var keyNewBounds: AEKeyword { get } ``` |

Modified [keyOptionalKeywordAttr](https://developer.apple.com/documentation/coreservices/1542920-keyword_attribute_constants/keyoptionalkeywordattr)

|  | Declaration |
| --- | --- |
| From | ``` var keyOptionalKeywordAttr: Int { get } ``` |
| To | ``` var keyOptionalKeywordAttr: AEKeyword { get } ``` |

Modified [keyOriginalAddressAttr](https://developer.apple.com/documentation/coreservices/1542920-keyword_attribute_constants/keyoriginaladdressattr)

|  | Declaration |
| --- | --- |
| From | ``` var keyOriginalAddressAttr: Int { get } ``` |
| To | ``` var keyOriginalAddressAttr: AEKeyword { get } ``` |

Modified [keyOriginalBounds](https://developer.apple.com/documentation/coreservices/1556381-keymenuid/keyoriginalbounds)

|  | Declaration |
| --- | --- |
| From | ``` var keyOriginalBounds: Int { get } ``` |
| To | ``` var keyOriginalBounds: AEKeyword { get } ``` |

Modified [keyPreDispatch](https://developer.apple.com/documentation/coreservices/1527206-keyword_parameter_constants/keypredispatch)

|  | Declaration |
| --- | --- |
| From | ``` var keyPreDispatch: Int { get } ``` |
| To | ``` var keyPreDispatch: AEKeyword { get } ``` |

Modified [keyProcessSerialNumber](https://developer.apple.com/documentation/coreservices/keyprocessserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` var keyProcessSerialNumber: Int { get } ``` |
| To | ``` var keyProcessSerialNumber: AEKeyword { get } ``` |

Modified [keyReplyPortAttr](https://developer.apple.com/documentation/coreservices/keyreplyportattr)

|  | Declaration |
| --- | --- |
| From | ``` var keyReplyPortAttr: Int { get } ``` |
| To | ``` var keyReplyPortAttr: AEKeyword { get } ``` |

Modified [keyReplyRequestedAttr](https://developer.apple.com/documentation/coreservices/1542920-keyword_attribute_constants/keyreplyrequestedattr)

|  | Declaration |
| --- | --- |
| From | ``` var keyReplyRequestedAttr: Int { get } ``` |
| To | ``` var keyReplyRequestedAttr: AEKeyword { get } ``` |

Modified [keyReturnIDAttr](https://developer.apple.com/documentation/coreservices/keyreturnidattr)

|  | Declaration |
| --- | --- |
| From | ``` var keyReturnIDAttr: Int { get } ``` |
| To | ``` var keyReturnIDAttr: AEKeyword { get } ``` |

Modified [keyRPCMethodName](https://developer.apple.com/documentation/coreservices/1542780-keyusernameattr/keyrpcmethodname)

|  | Declaration |
| --- | --- |
| From | ``` var keyRPCMethodName: Int { get } ``` |
| To | ``` var keyRPCMethodName: AEKeyword { get } ``` |

Modified [keyRPCMethodParam](https://developer.apple.com/documentation/coreservices/1542780-keyusernameattr/keyrpcmethodparam)

|  | Declaration |
| --- | --- |
| From | ``` var keyRPCMethodParam: Int { get } ``` |
| To | ``` var keyRPCMethodParam: AEKeyword { get } ``` |

Modified [keyRPCMethodParamOrder](https://developer.apple.com/documentation/coreservices/keyrpcmethodparamorder)

|  | Declaration |
| --- | --- |
| From | ``` var keyRPCMethodParamOrder: Int { get } ``` |
| To | ``` var keyRPCMethodParamOrder: AEKeyword { get } ``` |

Modified [keySelection](https://developer.apple.com/documentation/coreservices/1556399-keymiscellaneous/keyselection)

|  | Declaration |
| --- | --- |
| From | ``` var keySelection: Int { get } ``` |
| To | ``` var keySelection: AEKeyword { get } ``` |

Modified [keySelectProc](https://developer.apple.com/documentation/coreservices/1527206-keyword_parameter_constants/keyselectproc)

|  | Declaration |
| --- | --- |
| From | ``` var keySelectProc: Int { get } ``` |
| To | ``` var keySelectProc: AEKeyword { get } ``` |

Modified [keySenderApplescriptEntitlementsAttr](https://developer.apple.com/documentation/coreservices/keysenderapplescriptentitlementsattr)

|  | Declaration |
| --- | --- |
| From | ``` var keySenderApplescriptEntitlementsAttr: Int { get } ``` |
| To | ``` var keySenderApplescriptEntitlementsAttr: AEKeyword { get } ``` |

Modified [keySenderApplicationIdentifierEntitlementAttr](https://developer.apple.com/documentation/coreservices/keysenderapplicationidentifierentitlementattr)

|  | Declaration |
| --- | --- |
| From | ``` var keySenderApplicationIdentifierEntitlementAttr: Int { get } ``` |
| To | ``` var keySenderApplicationIdentifierEntitlementAttr: AEKeyword { get } ``` |

Modified [keySenderApplicationSandboxed](https://developer.apple.com/documentation/coreservices/1542920-keyword_attribute_constants/keysenderapplicationsandboxed)

|  | Declaration |
| --- | --- |
| From | ``` var keySenderApplicationSandboxed: Int { get } ``` |
| To | ``` var keySenderApplicationSandboxed: AEKeyword { get } ``` |

Modified [keySenderAuditTokenAttr](https://developer.apple.com/documentation/coreservices/keysenderaudittokenattr)

|  | Declaration |
| --- | --- |
| From | ``` var keySenderAuditTokenAttr: Int { get } ``` |
| To | ``` var keySenderAuditTokenAttr: AEKeyword { get } ``` |

Modified [keySenderEGIDAttr](https://developer.apple.com/documentation/coreservices/1542920-keyword_attribute_constants/keysenderegidattr)

|  | Declaration |
| --- | --- |
| From | ``` var keySenderEGIDAttr: Int { get } ``` |
| To | ``` var keySenderEGIDAttr: AEKeyword { get } ``` |

Modified [keySenderEUIDAttr](https://developer.apple.com/documentation/coreservices/1542920-keyword_attribute_constants/keysendereuidattr)

|  | Declaration |
| --- | --- |
| From | ``` var keySenderEUIDAttr: Int { get } ``` |
| To | ``` var keySenderEUIDAttr: AEKeyword { get } ``` |

Modified [keySenderGIDAttr](https://developer.apple.com/documentation/coreservices/keysendergidattr)

|  | Declaration |
| --- | --- |
| From | ``` var keySenderGIDAttr: Int { get } ``` |
| To | ``` var keySenderGIDAttr: AEKeyword { get } ``` |

Modified [keySenderPIDAttr](https://developer.apple.com/documentation/coreservices/keysenderpidattr)

|  | Declaration |
| --- | --- |
| From | ``` var keySenderPIDAttr: Int { get } ``` |
| To | ``` var keySenderPIDAttr: AEKeyword { get } ``` |

Modified [keySenderUIDAttr](https://developer.apple.com/documentation/coreservices/keysenderuidattr)

|  | Declaration |
| --- | --- |
| From | ``` var keySenderUIDAttr: Int { get } ``` |
| To | ``` var keySenderUIDAttr: AEKeyword { get } ``` |

Modified [keySOAPAction](https://developer.apple.com/documentation/coreservices/keysoapaction)

|  | Declaration |
| --- | --- |
| From | ``` var keySOAPAction: Int { get } ``` |
| To | ``` var keySOAPAction: AEKeyword { get } ``` |

Modified [keySOAPMethodNameSpace](https://developer.apple.com/documentation/coreservices/1542780-keyusernameattr/keysoapmethodnamespace)

|  | Declaration |
| --- | --- |
| From | ``` var keySOAPMethodNameSpace: Int { get } ``` |
| To | ``` var keySOAPMethodNameSpace: AEKeyword { get } ``` |

Modified [keySOAPMethodNameSpaceURI](https://developer.apple.com/documentation/coreservices/1542780-keyusernameattr/keysoapmethodnamespaceuri)

|  | Declaration |
| --- | --- |
| From | ``` var keySOAPMethodNameSpaceURI: Int { get } ``` |
| To | ``` var keySOAPMethodNameSpaceURI: AEKeyword { get } ``` |

Modified [keySOAPSchemaVersion](https://developer.apple.com/documentation/coreservices/keysoapschemaversion)

|  | Declaration |
| --- | --- |
| From | ``` var keySOAPSchemaVersion: Int { get } ``` |
| To | ``` var keySOAPSchemaVersion: AEKeyword { get } ``` |

Modified [keySOAPSMDNamespace](https://developer.apple.com/documentation/coreservices/keysoapsmdnamespace)

|  | Declaration |
| --- | --- |
| From | ``` var keySOAPSMDNamespace: Int { get } ``` |
| To | ``` var keySOAPSMDNamespace: AEKeyword { get } ``` |

Modified [keySOAPSMDNamespaceURI](https://developer.apple.com/documentation/coreservices/keysoapsmdnamespaceuri)

|  | Declaration |
| --- | --- |
| From | ``` var keySOAPSMDNamespaceURI: Int { get } ``` |
| To | ``` var keySOAPSMDNamespaceURI: AEKeyword { get } ``` |

Modified [keySOAPSMDType](https://developer.apple.com/documentation/coreservices/1542797-keysoapstructuremetadata/keysoapsmdtype)

|  | Declaration |
| --- | --- |
| From | ``` var keySOAPSMDType: Int { get } ``` |
| To | ``` var keySOAPSMDType: AEKeyword { get } ``` |

Modified [keySOAPStructureMetaData](https://developer.apple.com/documentation/coreservices/1542797-keysoapstructuremetadata/keysoapstructuremetadata)

|  | Declaration |
| --- | --- |
| From | ``` var keySOAPStructureMetaData: Int { get } ``` |
| To | ``` var keySOAPStructureMetaData: AEKeyword { get } ``` |

Modified [keyTimeoutAttr](https://developer.apple.com/documentation/coreservices/keytimeoutattr)

|  | Declaration |
| --- | --- |
| From | ``` var keyTimeoutAttr: Int { get } ``` |
| To | ``` var keyTimeoutAttr: AEKeyword { get } ``` |

Modified [keyTransactionIDAttr](https://developer.apple.com/documentation/coreservices/1542920-keyword_attribute_constants/keytransactionidattr)

|  | Declaration |
| --- | --- |
| From | ``` var keyTransactionIDAttr: Int { get } ``` |
| To | ``` var keyTransactionIDAttr: AEKeyword { get } ``` |

Modified [keyUserNameAttr](https://developer.apple.com/documentation/coreservices/1542780-keyusernameattr/keyusernameattr)

|  | Declaration |
| --- | --- |
| From | ``` var keyUserNameAttr: Int { get } ``` |
| To | ``` var keyUserNameAttr: AEKeyword { get } ``` |

Modified [keyUserPasswordAttr](https://developer.apple.com/documentation/coreservices/keyuserpasswordattr)

|  | Declaration |
| --- | --- |
| From | ``` var keyUserPasswordAttr: Int { get } ``` |
| To | ``` var keyUserPasswordAttr: AEKeyword { get } ``` |

Modified [keyWhen](https://developer.apple.com/documentation/coreservices/keywhen)

|  | Declaration |
| --- | --- |
| From | ``` var keyWhen: Int { get } ``` |
| To | ``` var keyWhen: AEKeyword { get } ``` |

Modified [keyWhere](https://developer.apple.com/documentation/coreservices/keywhere)

|  | Declaration |
| --- | --- |
| From | ``` var keyWhere: Int { get } ``` |
| To | ``` var keyWhere: AEKeyword { get } ``` |

Modified [keyWindow](https://developer.apple.com/documentation/coreservices/keywindow)

|  | Declaration |
| --- | --- |
| From | ``` var keyWindow: Int { get } ``` |
| To | ``` var keyWindow: AEKeyword { get } ``` |

Modified [keyXMLDebuggingAttr](https://developer.apple.com/documentation/coreservices/keyxmldebuggingattr)

|  | Declaration |
| --- | --- |
| From | ``` var keyXMLDebuggingAttr: Int { get } ``` |
| To | ``` var keyXMLDebuggingAttr: AEKeyword { get } ``` |

Modified [kFAAttachCommand](https://developer.apple.com/documentation/coreservices/kfaattachcommand)

|  | Declaration |
| --- | --- |
| From | ``` var kFAAttachCommand: Int { get } ``` |
| To | ``` var kFAAttachCommand: OSType { get } ``` |

Modified [kFAEditCommand](https://developer.apple.com/documentation/coreservices/kfaeditcommand)

|  | Declaration |
| --- | --- |
| From | ``` var kFAEditCommand: Int { get } ``` |
| To | ``` var kFAEditCommand: OSType { get } ``` |

Modified [kFAFileParam](https://developer.apple.com/documentation/coreservices/kfafileparam)

|  | Declaration |
| --- | --- |
| From | ``` var kFAFileParam: Int { get } ``` |
| To | ``` var kFAFileParam: OSType { get } ``` |

Modified [kFAIndexParam](https://developer.apple.com/documentation/coreservices/kfaindexparam)

|  | Declaration |
| --- | --- |
| From | ``` var kFAIndexParam: Int { get } ``` |
| To | ``` var kFAIndexParam: OSType { get } ``` |

Modified [kFARemoveCommand](https://developer.apple.com/documentation/coreservices/kfaremovecommand)

|  | Declaration |
| --- | --- |
| From | ``` var kFARemoveCommand: Int { get } ``` |
| To | ``` var kFARemoveCommand: OSType { get } ``` |

Modified [kFAServerApp](https://developer.apple.com/documentation/coreservices/kfaserverapp)

|  | Declaration |
| --- | --- |
| From | ``` var kFAServerApp: Int { get } ``` |
| To | ``` var kFAServerApp: OSType { get } ``` |

Modified [kFASuiteCode](https://developer.apple.com/documentation/coreservices/kfasuitecode)

|  | Declaration |
| --- | --- |
| From | ``` var kFASuiteCode: Int { get } ``` |
| To | ``` var kFASuiteCode: OSType { get } ``` |

Modified [kFolderActionCode](https://developer.apple.com/documentation/coreservices/kfolderactioncode)

|  | Declaration |
| --- | --- |
| From | ``` var kFolderActionCode: Int { get } ``` |
| To | ``` var kFolderActionCode: OSType { get } ``` |

Modified [kFolderClosedEvent](https://developer.apple.com/documentation/coreservices/1556384-kfaserverapp/kfolderclosedevent)

|  | Declaration |
| --- | --- |
| From | ``` var kFolderClosedEvent: Int { get } ``` |
| To | ``` var kFolderClosedEvent: OSType { get } ``` |

Modified [kFolderItemsAddedEvent](https://developer.apple.com/documentation/coreservices/1556384-kfaserverapp/kfolderitemsaddedevent)

|  | Declaration |
| --- | --- |
| From | ``` var kFolderItemsAddedEvent: Int { get } ``` |
| To | ``` var kFolderItemsAddedEvent: OSType { get } ``` |

Modified [kFolderItemsRemovedEvent](https://developer.apple.com/documentation/coreservices/1556384-kfaserverapp/kfolderitemsremovedevent)

|  | Declaration |
| --- | --- |
| From | ``` var kFolderItemsRemovedEvent: Int { get } ``` |
| To | ``` var kFolderItemsRemovedEvent: OSType { get } ``` |

Modified [kFolderOpenedEvent](https://developer.apple.com/documentation/coreservices/kfolderopenedevent)

|  | Declaration |
| --- | --- |
| From | ``` var kFolderOpenedEvent: Int { get } ``` |
| To | ``` var kFolderOpenedEvent: OSType { get } ``` |

Modified [kFolderWindowMovedEvent](https://developer.apple.com/documentation/coreservices/kfolderwindowmovedevent)

|  | Declaration |
| --- | --- |
| From | ``` var kFolderWindowMovedEvent: Int { get } ``` |
| To | ``` var kFolderWindowMovedEvent: OSType { get } ``` |

Modified [kGetSelectedText](https://developer.apple.com/documentation/coreservices/kgetselectedtext)

|  | Declaration |
| --- | --- |
| From | ``` var kGetSelectedText: Int { get } ``` |
| To | ``` var kGetSelectedText: OSType { get } ``` |

Modified [kItemList](https://developer.apple.com/documentation/coreservices/1556384-kfaserverapp/kitemlist)

|  | Declaration |
| --- | --- |
| From | ``` var kItemList: Int { get } ``` |
| To | ``` var kItemList: OSType { get } ``` |

Modified [kNewSizeParameter](https://developer.apple.com/documentation/coreservices/1556384-kfaserverapp/knewsizeparameter)

|  | Declaration |
| --- | --- |
| From | ``` var kNewSizeParameter: Int { get } ``` |
| To | ``` var kNewSizeParameter: OSType { get } ``` |

Modified [kOffset2Pos](https://developer.apple.com/documentation/coreservices/1556406-ktextserviceclass/koffset2pos)

|  | Declaration |
| --- | --- |
| From | ``` var kOffset2Pos: Int { get } ``` |
| To | ``` var kOffset2Pos: OSType { get } ``` |

Modified [kPos2Offset](https://developer.apple.com/documentation/coreservices/kpos2offset)

|  | Declaration |
| --- | --- |
| From | ``` var kPos2Offset: Int { get } ``` |
| To | ``` var kPos2Offset: OSType { get } ``` |

Modified [kShowHideInputWindow](https://developer.apple.com/documentation/coreservices/kshowhideinputwindow)

|  | Declaration |
| --- | --- |
| From | ``` var kShowHideInputWindow: Int { get } ``` |
| To | ``` var kShowHideInputWindow: OSType { get } ``` |

Modified [kTextServiceClass](https://developer.apple.com/documentation/coreservices/ktextserviceclass)

|  | Declaration |
| --- | --- |
| From | ``` var kTextServiceClass: Int { get } ``` |
| To | ``` var kTextServiceClass: OSType { get } ``` |

Modified [kUnicodeNotFromInputMethod](https://developer.apple.com/documentation/coreservices/kunicodenotfrominputmethod)

|  | Declaration |
| --- | --- |
| From | ``` var kUnicodeNotFromInputMethod: Int { get } ``` |
| To | ``` var kUnicodeNotFromInputMethod: OSType { get } ``` |

Modified [kUpdateActiveInputArea](https://developer.apple.com/documentation/coreservices/1556406-ktextserviceclass/kupdateactiveinputarea)

|  | Declaration |
| --- | --- |
| From | ``` var kUpdateActiveInputArea: Int { get } ``` |
| To | ``` var kUpdateActiveInputArea: OSType { get } ``` |

Modified [LSCanRefAcceptItem(_: UnsafePointer<FSRef>!, _: UnsafePointer<FSRef>!, _: LSRolesMask, _: LSAcceptanceFlags, _: UnsafeMutablePointer<DarwinBoolean>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1442183-lscanrefacceptitem)

|  | Declaration |
| --- | --- |
| From | ``` func LSCanRefAcceptItem(_ inItemFSRef: UnsafePointer<FSRef>, _ inTargetRef: UnsafePointer<FSRef>, _ inRoleMask: LSRolesMask, _ inFlags: LSAcceptanceFlags, _ outAcceptsItem: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |
| To | ``` func LSCanRefAcceptItem(_ inItemFSRef: UnsafePointer<FSRef>!, _ inTargetRef: UnsafePointer<FSRef>!, _ inRoleMask: LSRolesMask, _ inFlags: LSAcceptanceFlags, _ outAcceptsItem: UnsafeMutablePointer<DarwinBoolean>!) -> OSStatus ``` |

Modified [LSCopyApplicationForMIMEType(_: CFString!, _: LSRolesMask, _: UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1448586-lscopyapplicationformimetype)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyApplicationForMIMEType(_ inMIMEType: CFString!, _ inRoleMask: LSRolesMask, _ outAppURL: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` |
| To | ``` func LSCopyApplicationForMIMEType(_ inMIMEType: CFString!, _ inRoleMask: LSRolesMask, _ outAppURL: UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus ``` |

Modified [LSCopyApplicationURLsForBundleIdentifier(_: CFString, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFArray>?](https://developer.apple.com/documentation/coreservices/1449290-lscopyapplicationurlsforbundleid)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyApplicationURLsForBundleIdentifier(_ inBundleIdentifier: CFString, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>? ``` |
| To | ``` func LSCopyApplicationURLsForBundleIdentifier(_ inBundleIdentifier: CFString, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFArray>? ``` |

Modified [LSCopyDefaultApplicationURLForContentType(_: CFString, _: LSRolesMask, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>?](https://developer.apple.com/documentation/coreservices/1447734-lscopydefaultapplicationurlforco)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyDefaultApplicationURLForContentType(_ inContentType: CFString, _ inRoleMask: LSRolesMask, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>? ``` |
| To | ``` func LSCopyDefaultApplicationURLForContentType(_ inContentType: CFString, _ inRoleMask: LSRolesMask, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>? ``` |

Modified [LSCopyDefaultApplicationURLForURL(_: CFURL, _: LSRolesMask, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>?](https://developer.apple.com/documentation/coreservices/1448824-lscopydefaultapplicationurlforur)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyDefaultApplicationURLForURL(_ inURL: CFURL, _ inRoleMask: LSRolesMask, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>? ``` |
| To | ``` func LSCopyDefaultApplicationURLForURL(_ inURL: CFURL, _ inRoleMask: LSRolesMask, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>? ``` |

Modified [LSCopyDisplayNameForRef(_: UnsafePointer<FSRef>!, _: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1442576-lscopydisplaynameforref)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyDisplayNameForRef(_ inRef: UnsafePointer<FSRef>, _ outDisplayName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func LSCopyDisplayNameForRef(_ inRef: UnsafePointer<FSRef>!, _ outDisplayName: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus ``` |

Modified [LSCopyDisplayNameForURL(_: CFURL!, _: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1446850-lscopydisplaynameforurl)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyDisplayNameForURL(_ inURL: CFURL!, _ outDisplayName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func LSCopyDisplayNameForURL(_ inURL: CFURL!, _ outDisplayName: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus ``` |

Modified [LSCopyItemAttribute(_: UnsafePointer<FSRef>!, _: LSRolesMask, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFTypeRef>?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1445023-lscopyitemattribute)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyItemAttribute(_ inItem: UnsafePointer<FSRef>, _ inRoles: LSRolesMask, _ inAttributeName: CFString!, _ outValue: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` |
| To | ``` func LSCopyItemAttribute(_ inItem: UnsafePointer<FSRef>!, _ inRoles: LSRolesMask, _ inAttributeName: CFString!, _ outValue: UnsafeMutablePointer<Unmanaged<CFTypeRef>?>!) -> OSStatus ``` |

Modified [LSCopyItemAttributes(_: UnsafePointer<FSRef>!, _: LSRolesMask, _: CFArray!, _: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1446078-lscopyitemattributes)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyItemAttributes(_ inItem: UnsafePointer<FSRef>, _ inRoles: LSRolesMask, _ inAttributeNames: CFArray!, _ outValues: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` |
| To | ``` func LSCopyItemAttributes(_ inItem: UnsafePointer<FSRef>!, _ inRoles: LSRolesMask, _ inAttributeNames: CFArray!, _ outValues: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!) -> OSStatus ``` |

Modified [LSCopyItemInfoForRef(_: UnsafePointer<FSRef>!, _: LSRequestedInfo, _: UnsafeMutablePointer<LSItemInfoRecord>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1445227-lscopyiteminfoforref)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyItemInfoForRef(_ inItemRef: UnsafePointer<FSRef>, _ inWhichInfo: LSRequestedInfo, _ outItemInfo: UnsafeMutablePointer<LSItemInfoRecord>) -> OSStatus ``` |
| To | ``` func LSCopyItemInfoForRef(_ inItemRef: UnsafePointer<FSRef>!, _ inWhichInfo: LSRequestedInfo, _ outItemInfo: UnsafeMutablePointer<LSItemInfoRecord>!) -> OSStatus ``` |

Modified [LSCopyItemInfoForURL(_: CFURL!, _: LSRequestedInfo, _: UnsafeMutablePointer<LSItemInfoRecord>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1445685-lscopyiteminfoforurl)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyItemInfoForURL(_ inURL: CFURL!, _ inWhichInfo: LSRequestedInfo, _ outItemInfo: UnsafeMutablePointer<LSItemInfoRecord>) -> OSStatus ``` |
| To | ``` func LSCopyItemInfoForURL(_ inURL: CFURL!, _ inWhichInfo: LSRequestedInfo, _ outItemInfo: UnsafeMutablePointer<LSItemInfoRecord>!) -> OSStatus ``` |

Modified [LSCopyKindStringForMIMEType(_: CFString!, _: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1442446-lscopykindstringformimetype)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyKindStringForMIMEType(_ inMIMEType: CFString!, _ outKindString: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func LSCopyKindStringForMIMEType(_ inMIMEType: CFString!, _ outKindString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus ``` |

Modified [LSCopyKindStringForRef(_: UnsafePointer<FSRef>!, _: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1448593-lscopykindstringforref)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyKindStringForRef(_ inFSRef: UnsafePointer<FSRef>, _ outKindString: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func LSCopyKindStringForRef(_ inFSRef: UnsafePointer<FSRef>!, _ outKindString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus ``` |

Modified [LSCopyKindStringForTypeInfo(_: OSType, _: OSType, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1446207-lscopykindstringfortypeinfo)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyKindStringForTypeInfo(_ inType: OSType, _ inCreator: OSType, _ inExtension: CFString!, _ outKindString: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func LSCopyKindStringForTypeInfo(_ inType: OSType, _ inCreator: OSType, _ inExtension: CFString!, _ outKindString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus ``` |

Modified [LSCopyKindStringForURL(_: CFURL!, _: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1447481-lscopykindstringforurl)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyKindStringForURL(_ inURL: CFURL!, _ outKindString: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func LSCopyKindStringForURL(_ inURL: CFURL!, _ outKindString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus ``` |

Modified [LSFindApplicationForInfo(_: OSType, _: CFString!, _: CFString!, _: UnsafeMutablePointer<FSRef>!, _: UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1449588-lsfindapplicationforinfo)

|  | Declaration |
| --- | --- |
| From | ``` func LSFindApplicationForInfo(_ inCreator: OSType, _ inBundleID: CFString!, _ inName: CFString!, _ outAppRef: UnsafeMutablePointer<FSRef>, _ outAppURL: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` |
| To | ``` func LSFindApplicationForInfo(_ inCreator: OSType, _ inBundleID: CFString!, _ inName: CFString!, _ outAppRef: UnsafeMutablePointer<FSRef>!, _ outAppURL: UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus ``` |

Modified [LSGetApplicationForInfo(_: OSType, _: OSType, _: CFString!, _: LSRolesMask, _: UnsafeMutablePointer<FSRef>!, _: UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1449928-lsgetapplicationforinfo)

|  | Declaration |
| --- | --- |
| From | ``` func LSGetApplicationForInfo(_ inType: OSType, _ inCreator: OSType, _ inExtension: CFString!, _ inRoleMask: LSRolesMask, _ outAppRef: UnsafeMutablePointer<FSRef>, _ outAppURL: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` |
| To | ``` func LSGetApplicationForInfo(_ inType: OSType, _ inCreator: OSType, _ inExtension: CFString!, _ inRoleMask: LSRolesMask, _ outAppRef: UnsafeMutablePointer<FSRef>!, _ outAppURL: UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus ``` |

Modified [LSGetApplicationForItem(_: UnsafePointer<FSRef>!, _: LSRolesMask, _: UnsafeMutablePointer<FSRef>!, _: UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1446185-lsgetapplicationforitem)

|  | Declaration |
| --- | --- |
| From | ``` func LSGetApplicationForItem(_ inItemRef: UnsafePointer<FSRef>, _ inRoleMask: LSRolesMask, _ outAppRef: UnsafeMutablePointer<FSRef>, _ outAppURL: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` |
| To | ``` func LSGetApplicationForItem(_ inItemRef: UnsafePointer<FSRef>!, _ inRoleMask: LSRolesMask, _ outAppRef: UnsafeMutablePointer<FSRef>!, _ outAppURL: UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus ``` |

Modified [LSGetApplicationForURL(_: CFURL!, _: LSRolesMask, _: UnsafeMutablePointer<FSRef>!, _: UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1445210-lsgetapplicationforurl)

|  | Declaration |
| --- | --- |
| From | ``` func LSGetApplicationForURL(_ inURL: CFURL!, _ inRoleMask: LSRolesMask, _ outAppRef: UnsafeMutablePointer<FSRef>, _ outAppURL: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` |
| To | ``` func LSGetApplicationForURL(_ inURL: CFURL!, _ inRoleMask: LSRolesMask, _ outAppRef: UnsafeMutablePointer<FSRef>!, _ outAppURL: UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus ``` |

Modified [LSGetExtensionInfo(_: Int, _: UnsafePointer<UniChar>!, _: UnsafeMutablePointer<Int>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1446043-lsgetextensioninfo)

|  | Declaration |
| --- | --- |
| From | ``` func LSGetExtensionInfo(_ inNameLen: Int, _ inNameBuffer: UnsafePointer<UniChar>, _ outExtStartIndex: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func LSGetExtensionInfo(_ inNameLen: Int, _ inNameBuffer: UnsafePointer<UniChar>!, _ outExtStartIndex: UnsafeMutablePointer<Int>!) -> OSStatus ``` |

Modified [LSOpenApplication(_: UnsafePointer<LSApplicationParameters>!, _: UnsafeMutablePointer<ProcessSerialNumber>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1447930-lsopenapplication)

|  | Declaration |
| --- | --- |
| From | ``` func LSOpenApplication(_ appParams: UnsafePointer<LSApplicationParameters>, _ outPSN: UnsafeMutablePointer<ProcessSerialNumber>) -> OSStatus ``` |
| To | ``` func LSOpenApplication(_ appParams: UnsafePointer<LSApplicationParameters>!, _ outPSN: UnsafeMutablePointer<ProcessSerialNumber>!) -> OSStatus ``` |

Modified [LSOpenCFURLRef(_: CFURL, _: UnsafeMutablePointer<Unmanaged<CFURL>?>?) -> OSStatus](https://developer.apple.com/documentation/coreservices/1442850-lsopencfurlref)

|  | Declaration |
| --- | --- |
| From | ``` func LSOpenCFURLRef(_ inURL: CFURL, _ outLaunchedURL: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` |
| To | ``` func LSOpenCFURLRef(_ inURL: CFURL, _ outLaunchedURL: UnsafeMutablePointer<Unmanaged<CFURL>?>?) -> OSStatus ``` |

Modified [LSOpenFromRefSpec(_: UnsafePointer<LSLaunchFSRefSpec>!, _: UnsafeMutablePointer<FSRef>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1444466-lsopenfromrefspec)

|  | Declaration |
| --- | --- |
| From | ``` func LSOpenFromRefSpec(_ inLaunchSpec: UnsafePointer<LSLaunchFSRefSpec>, _ outLaunchedRef: UnsafeMutablePointer<FSRef>) -> OSStatus ``` |
| To | ``` func LSOpenFromRefSpec(_ inLaunchSpec: UnsafePointer<LSLaunchFSRefSpec>!, _ outLaunchedRef: UnsafeMutablePointer<FSRef>!) -> OSStatus ``` |

Modified [LSOpenFromURLSpec(_: UnsafePointer<LSLaunchURLSpec>, _: UnsafeMutablePointer<Unmanaged<CFURL>?>?) -> OSStatus](https://developer.apple.com/documentation/coreservices/1441986-lsopenfromurlspec)

|  | Declaration |
| --- | --- |
| From | ``` func LSOpenFromURLSpec(_ inLaunchSpec: UnsafePointer<LSLaunchURLSpec>, _ outLaunchedURL: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` |
| To | ``` func LSOpenFromURLSpec(_ inLaunchSpec: UnsafePointer<LSLaunchURLSpec>, _ outLaunchedURL: UnsafeMutablePointer<Unmanaged<CFURL>?>?) -> OSStatus ``` |

Modified [LSOpenFSRef(_: UnsafePointer<FSRef>!, _: UnsafeMutablePointer<FSRef>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1445663-lsopenfsref)

|  | Declaration |
| --- | --- |
| From | ``` func LSOpenFSRef(_ inRef: UnsafePointer<FSRef>, _ outLaunchedRef: UnsafeMutablePointer<FSRef>) -> OSStatus ``` |
| To | ``` func LSOpenFSRef(_ inRef: UnsafePointer<FSRef>!, _ outLaunchedRef: UnsafeMutablePointer<FSRef>!) -> OSStatus ``` |

Modified [LSOpenItemsWithRole(_: UnsafePointer<FSRef>!, _: CFIndex, _: LSRolesMask, _: UnsafePointer<AEKeyDesc>!, _: UnsafePointer<LSApplicationParameters>!, _: UnsafeMutablePointer<ProcessSerialNumber>!, _: CFIndex) -> OSStatus](https://developer.apple.com/documentation/coreservices/1449783-lsopenitemswithrole)

|  | Declaration |
| --- | --- |
| From | ``` func LSOpenItemsWithRole(_ inItems: UnsafePointer<FSRef>, _ inItemCount: CFIndex, _ inRole: LSRolesMask, _ inAEParam: UnsafePointer<AEKeyDesc>, _ inAppParams: UnsafePointer<LSApplicationParameters>, _ outPSNs: UnsafeMutablePointer<ProcessSerialNumber>, _ inMaxPSNCount: CFIndex) -> OSStatus ``` |
| To | ``` func LSOpenItemsWithRole(_ inItems: UnsafePointer<FSRef>!, _ inItemCount: CFIndex, _ inRole: LSRolesMask, _ inAEParam: UnsafePointer<AEKeyDesc>!, _ inAppParams: UnsafePointer<LSApplicationParameters>!, _ outPSNs: UnsafeMutablePointer<ProcessSerialNumber>!, _ inMaxPSNCount: CFIndex) -> OSStatus ``` |

Modified [LSOpenURLsWithRole(_: CFArray!, _: LSRolesMask, _: UnsafePointer<AEKeyDesc>!, _: UnsafePointer<LSApplicationParameters>!, _: UnsafeMutablePointer<ProcessSerialNumber>!, _: CFIndex) -> OSStatus](https://developer.apple.com/documentation/coreservices/1448184-lsopenurlswithrole)

|  | Declaration |
| --- | --- |
| From | ``` func LSOpenURLsWithRole(_ inURLs: CFArray!, _ inRole: LSRolesMask, _ inAEParam: UnsafePointer<AEKeyDesc>, _ inAppParams: UnsafePointer<LSApplicationParameters>, _ outPSNs: UnsafeMutablePointer<ProcessSerialNumber>, _ inMaxPSNCount: CFIndex) -> OSStatus ``` |
| To | ``` func LSOpenURLsWithRole(_ inURLs: CFArray!, _ inRole: LSRolesMask, _ inAEParam: UnsafePointer<AEKeyDesc>!, _ inAppParams: UnsafePointer<LSApplicationParameters>!, _ outPSNs: UnsafeMutablePointer<ProcessSerialNumber>!, _ inMaxPSNCount: CFIndex) -> OSStatus ``` |

Modified [LSRegisterFSRef(_: UnsafePointer<FSRef>!, _: Bool) -> OSStatus](https://developer.apple.com/documentation/coreservices/1444582-lsregisterfsref)

|  | Declaration |
| --- | --- |
| From | ``` func LSRegisterFSRef(_ inRef: UnsafePointer<FSRef>, _ inUpdate: Bool) -> OSStatus ``` |
| To | ``` func LSRegisterFSRef(_ inRef: UnsafePointer<FSRef>!, _ inUpdate: Bool) -> OSStatus ``` |

Modified [LSSetExtensionHiddenForRef(_: UnsafePointer<FSRef>!, _: Bool) -> OSStatus](https://developer.apple.com/documentation/coreservices/1442766-lssetextensionhiddenforref)

|  | Declaration |
| --- | --- |
| From | ``` func LSSetExtensionHiddenForRef(_ inRef: UnsafePointer<FSRef>, _ inHide: Bool) -> OSStatus ``` |
| To | ``` func LSSetExtensionHiddenForRef(_ inRef: UnsafePointer<FSRef>!, _ inHide: Bool) -> OSStatus ``` |

Modified [LSSetItemAttribute(_: UnsafePointer<FSRef>!, _: LSRolesMask, _: CFString!, _: CFTypeRef!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1446733-lssetitemattribute)

|  | Declaration |
| --- | --- |
| From | ``` func LSSetItemAttribute(_ inItem: UnsafePointer<FSRef>, _ inRoles: LSRolesMask, _ inAttributeName: CFString!, _ inValue: AnyObject!) -> OSStatus ``` |
| To | ``` func LSSetItemAttribute(_ inItem: UnsafePointer<FSRef>!, _ inRoles: LSRolesMask, _ inAttributeName: CFString!, _ inValue: CFTypeRef!) -> OSStatus ``` |

Modified [LSSharedFileListAddObserver(_: LSSharedFileList!, _: CFRunLoop!, _: CFString!, _: CoreServices.LSSharedFileListChangedProcPtr!, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/coreservices/1445770-lssharedfilelistaddobserver)

|  | Declaration |
| --- | --- |
| From | ``` func LSSharedFileListAddObserver(_ inList: LSSharedFileList!, _ inRunloop: CFRunLoop!, _ inRunloopMode: CFString!, _ callback: LSSharedFileListChangedProcPtr!, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func LSSharedFileListAddObserver(_ inList: LSSharedFileList!, _ inRunloop: CFRunLoop!, _ inRunloopMode: CFString!, _ callback: CoreServices.LSSharedFileListChangedProcPtr!, _ context: UnsafeMutableRawPointer!) ``` |

Modified [LSSharedFileListChangedProcPtr](https://developer.apple.com/documentation/coreservices/lssharedfilelistchangedprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias LSSharedFileListChangedProcPtr = (LSSharedFileList!, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias LSSharedFileListChangedProcPtr = (LSSharedFileList?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [LSSharedFileListCopyProperty(_: LSSharedFileList!, _: CFString!) -> Unmanaged<CFTypeRef>!](https://developer.apple.com/documentation/coreservices/1444588-lssharedfilelistcopyproperty)

|  | Declaration |
| --- | --- |
| From | ``` func LSSharedFileListCopyProperty(_ inList: LSSharedFileList!, _ inPropertyName: CFString!) -> Unmanaged<AnyObject>! ``` |
| To | ``` func LSSharedFileListCopyProperty(_ inList: LSSharedFileList!, _ inPropertyName: CFString!) -> Unmanaged<CFTypeRef>! ``` |

Modified [LSSharedFileListCopySnapshot(_: LSSharedFileList!, _: UnsafeMutablePointer<UInt32>!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/coreservices/1448112-lssharedfilelistcopysnapshot)

|  | Declaration |
| --- | --- |
| From | ``` func LSSharedFileListCopySnapshot(_ inList: LSSharedFileList!, _ outSnapshotSeed: UnsafeMutablePointer<UInt32>) -> Unmanaged<CFArray>! ``` |
| To | ``` func LSSharedFileListCopySnapshot(_ inList: LSSharedFileList!, _ outSnapshotSeed: UnsafeMutablePointer<UInt32>!) -> Unmanaged<CFArray>! ``` |

Modified [LSSharedFileListCreate(_: CFAllocator!, _: CFString!, _: CFTypeRef!) -> Unmanaged<LSSharedFileList>!](https://developer.apple.com/documentation/coreservices/1443926-lssharedfilelistcreate)

|  | Declaration |
| --- | --- |
| From | ``` func LSSharedFileListCreate(_ inAllocator: CFAllocator!, _ inListType: CFString!, _ listOptions: AnyObject!) -> Unmanaged<LSSharedFileList>! ``` |
| To | ``` func LSSharedFileListCreate(_ inAllocator: CFAllocator!, _ inListType: CFString!, _ listOptions: CFTypeRef!) -> Unmanaged<LSSharedFileList>! ``` |

Modified [LSSharedFileListInsertItemFSRef(_: LSSharedFileList!, _: LSSharedFileListItem!, _: CFString!, _: IconRef!, _: UnsafePointer<FSRef>!, _: CFDictionary!, _: CFArray!) -> Unmanaged<LSSharedFileListItem>!](https://developer.apple.com/documentation/coreservices/1449884-lssharedfilelistinsertitemfsref)

|  | Declaration |
| --- | --- |
| From | ``` func LSSharedFileListInsertItemFSRef(_ inList: LSSharedFileList!, _ insertAfterThisItem: LSSharedFileListItem!, _ inDisplayName: CFString!, _ inIconRef: IconRef, _ inFSRef: UnsafePointer<FSRef>, _ inPropertiesToSet: CFDictionary!, _ inPropertiesToClear: CFArray!) -> Unmanaged<LSSharedFileListItem>! ``` |
| To | ``` func LSSharedFileListInsertItemFSRef(_ inList: LSSharedFileList!, _ insertAfterThisItem: LSSharedFileListItem!, _ inDisplayName: CFString!, _ inIconRef: IconRef!, _ inFSRef: UnsafePointer<FSRef>!, _ inPropertiesToSet: CFDictionary!, _ inPropertiesToClear: CFArray!) -> Unmanaged<LSSharedFileListItem>! ``` |

Modified [LSSharedFileListInsertItemURL(_: LSSharedFileList!, _: LSSharedFileListItem!, _: CFString!, _: IconRef!, _: CFURL!, _: CFDictionary!, _: CFArray!) -> Unmanaged<LSSharedFileListItem>!](https://developer.apple.com/documentation/coreservices/1444471-lssharedfilelistinsertitemurl)

|  | Declaration |
| --- | --- |
| From | ``` func LSSharedFileListInsertItemURL(_ inList: LSSharedFileList!, _ insertAfterThisItem: LSSharedFileListItem!, _ inDisplayName: CFString!, _ inIconRef: IconRef, _ inURL: CFURL!, _ inPropertiesToSet: CFDictionary!, _ inPropertiesToClear: CFArray!) -> Unmanaged<LSSharedFileListItem>! ``` |
| To | ``` func LSSharedFileListInsertItemURL(_ inList: LSSharedFileList!, _ insertAfterThisItem: LSSharedFileListItem!, _ inDisplayName: CFString!, _ inIconRef: IconRef!, _ inURL: CFURL!, _ inPropertiesToSet: CFDictionary!, _ inPropertiesToClear: CFArray!) -> Unmanaged<LSSharedFileListItem>! ``` |

Modified [LSSharedFileListItemCopyIconRef(_: LSSharedFileListItem!) -> IconRef!](https://developer.apple.com/documentation/coreservices/1442889-lssharedfilelistitemcopyiconref)

|  | Declaration |
| --- | --- |
| From | ``` func LSSharedFileListItemCopyIconRef(_ inItem: LSSharedFileListItem!) -> IconRef ``` |
| To | ``` func LSSharedFileListItemCopyIconRef(_ inItem: LSSharedFileListItem!) -> IconRef! ``` |

Modified [LSSharedFileListItemCopyProperty(_: LSSharedFileListItem!, _: CFString!) -> Unmanaged<CFTypeRef>!](https://developer.apple.com/documentation/coreservices/1445074-lssharedfilelistitemcopyproperty)

|  | Declaration |
| --- | --- |
| From | ``` func LSSharedFileListItemCopyProperty(_ inItem: LSSharedFileListItem!, _ inPropertyName: CFString!) -> Unmanaged<AnyObject>! ``` |
| To | ``` func LSSharedFileListItemCopyProperty(_ inItem: LSSharedFileListItem!, _ inPropertyName: CFString!) -> Unmanaged<CFTypeRef>! ``` |

Modified [LSSharedFileListItemCopyResolvedURL(_: LSSharedFileListItem!, _: LSSharedFileListResolutionFlags, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!](https://developer.apple.com/documentation/coreservices/1449882-lssharedfilelistitemcopyresolved)

|  | Declaration |
| --- | --- |
| From | ``` func LSSharedFileListItemCopyResolvedURL(_ inItem: LSSharedFileListItem!, _ inFlags: LSSharedFileListResolutionFlags, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>! ``` |
| To | ``` func LSSharedFileListItemCopyResolvedURL(_ inItem: LSSharedFileListItem!, _ inFlags: LSSharedFileListResolutionFlags, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>! ``` |

Modified [LSSharedFileListItemResolve(_: LSSharedFileListItem!, _: LSSharedFileListResolutionFlags, _: UnsafeMutablePointer<Unmanaged<CFURL>?>!, _: UnsafeMutablePointer<FSRef>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1447347-lssharedfilelistitemresolve)

|  | Declaration |
| --- | --- |
| From | ``` func LSSharedFileListItemResolve(_ inItem: LSSharedFileListItem!, _ inFlags: LSSharedFileListResolutionFlags, _ outURL: UnsafeMutablePointer<Unmanaged<CFURL>?>, _ outRef: UnsafeMutablePointer<FSRef>) -> OSStatus ``` |
| To | ``` func LSSharedFileListItemResolve(_ inItem: LSSharedFileListItem!, _ inFlags: LSSharedFileListResolutionFlags, _ outURL: UnsafeMutablePointer<Unmanaged<CFURL>?>!, _ outRef: UnsafeMutablePointer<FSRef>!) -> OSStatus ``` |

Modified [LSSharedFileListItemSetProperty(_: LSSharedFileListItem!, _: CFString!, _: CFTypeRef!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1445766-lssharedfilelistitemsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func LSSharedFileListItemSetProperty(_ inItem: LSSharedFileListItem!, _ inPropertyName: CFString!, _ inPropertyData: AnyObject!) -> OSStatus ``` |
| To | ``` func LSSharedFileListItemSetProperty(_ inItem: LSSharedFileListItem!, _ inPropertyName: CFString!, _ inPropertyData: CFTypeRef!) -> OSStatus ``` |

Modified [LSSharedFileListRemoveObserver(_: LSSharedFileList!, _: CFRunLoop!, _: CFString!, _: CoreServices.LSSharedFileListChangedProcPtr!, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/coreservices/1443404-lssharedfilelistremoveobserver)

|  | Declaration |
| --- | --- |
| From | ``` func LSSharedFileListRemoveObserver(_ inList: LSSharedFileList!, _ inRunloop: CFRunLoop!, _ inRunloopMode: CFString!, _ callback: LSSharedFileListChangedProcPtr!, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func LSSharedFileListRemoveObserver(_ inList: LSSharedFileList!, _ inRunloop: CFRunLoop!, _ inRunloopMode: CFString!, _ callback: CoreServices.LSSharedFileListChangedProcPtr!, _ context: UnsafeMutableRawPointer!) ``` |

Modified [LSSharedFileListSetAuthorization(_: LSSharedFileList!, _: AuthorizationRef!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1446834-lssharedfilelistsetauthorization)

|  | Declaration |
| --- | --- |
| From | ``` func LSSharedFileListSetAuthorization(_ inList: LSSharedFileList!, _ inAuthorization: AuthorizationRef) -> OSStatus ``` |
| To | ``` func LSSharedFileListSetAuthorization(_ inList: LSSharedFileList!, _ inAuthorization: AuthorizationRef!) -> OSStatus ``` |

Modified [LSSharedFileListSetProperty(_: LSSharedFileList!, _: CFString!, _: CFTypeRef!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1448857-lssharedfilelistsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func LSSharedFileListSetProperty(_ inList: LSSharedFileList!, _ inPropertyName: CFString!, _ inPropertyData: AnyObject!) -> OSStatus ``` |
| To | ``` func LSSharedFileListSetProperty(_ inList: LSSharedFileList!, _ inPropertyName: CFString!, _ inPropertyData: CFTypeRef!) -> OSStatus ``` |

Modified [MDItemCopyAttribute(_: MDItem!, _: CFString!) -> CFTypeRef!](https://developer.apple.com/documentation/coreservices/1427080-mditemcopyattribute)

|  | Declaration |
| --- | --- |
| From | ``` func MDItemCopyAttribute(_ item: MDItem!, _ name: CFString!) -> AnyObject! ``` |
| To | ``` func MDItemCopyAttribute(_ item: MDItem!, _ name: CFString!) -> CFTypeRef! ``` |

Modified [MDLabelCopyAttribute(_: MDLabel!, _: CFString!) -> CFTypeRef!](https://developer.apple.com/documentation/coreservices/1445456-mdlabelcopyattribute)

|  | Declaration |
| --- | --- |
| From | ``` func MDLabelCopyAttribute(_ label: MDLabel!, _ name: CFString!) -> AnyObject! ``` |
| To | ``` func MDLabelCopyAttribute(_ label: MDLabel!, _ name: CFString!) -> CFTypeRef! ``` |

Modified [MDQueryCreateResultFunction](https://developer.apple.com/documentation/coreservices/mdquerycreateresultfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias MDQueryCreateResultFunction = (MDQuery!, MDItem!, UnsafeMutablePointer<Void>) -> UnsafePointer<Void> ``` |
| To | ``` typealias MDQueryCreateResultFunction = (MDQuery?, MDItem?, UnsafeMutableRawPointer?) -> UnsafeRawPointer? ``` |

Modified [MDQueryCreateValueFunction](https://developer.apple.com/documentation/coreservices/mdquerycreatevaluefunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias MDQueryCreateValueFunction = (MDQuery!, CFString!, AnyObject!, UnsafeMutablePointer<Void>) -> UnsafePointer<Void> ``` |
| To | ``` typealias MDQueryCreateValueFunction = (MDQuery?, CFString?, CFTypeRef?, UnsafeMutableRawPointer?) -> UnsafeRawPointer? ``` |

Modified [MDQueryGetAttributeValueOfResultAtIndex(_: MDQuery!, _: CFString!, _: CFIndex) -> UnsafeMutableRawPointer!](https://developer.apple.com/documentation/coreservices/1413046-mdquerygetattributevalueofresult)

|  | Declaration |
| --- | --- |
| From | ``` func MDQueryGetAttributeValueOfResultAtIndex(_ query: MDQuery!, _ name: CFString!, _ idx: CFIndex) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func MDQueryGetAttributeValueOfResultAtIndex(_ query: MDQuery!, _ name: CFString!, _ idx: CFIndex) -> UnsafeMutableRawPointer! ``` |

Modified [MDQueryGetCountOfResultsWithAttributeValue(_: MDQuery!, _: CFString!, _: CFTypeRef!) -> CFIndex](https://developer.apple.com/documentation/coreservices/1413009-mdquerygetcountofresultswithattr)

|  | Declaration |
| --- | --- |
| From | ``` func MDQueryGetCountOfResultsWithAttributeValue(_ query: MDQuery!, _ name: CFString!, _ value: AnyObject!) -> CFIndex ``` |
| To | ``` func MDQueryGetCountOfResultsWithAttributeValue(_ query: MDQuery!, _ name: CFString!, _ value: CFTypeRef!) -> CFIndex ``` |

Modified [MDQueryGetIndexOfResult(_: MDQuery!, _: UnsafeRawPointer!) -> CFIndex](https://developer.apple.com/documentation/coreservices/1413093-mdquerygetindexofresult)

|  | Declaration |
| --- | --- |
| From | ``` func MDQueryGetIndexOfResult(_ query: MDQuery!, _ result: UnsafePointer<Void>) -> CFIndex ``` |
| To | ``` func MDQueryGetIndexOfResult(_ query: MDQuery!, _ result: UnsafeRawPointer!) -> CFIndex ``` |

Modified [MDQueryGetResultAtIndex(_: MDQuery!, _: CFIndex) -> UnsafeRawPointer!](https://developer.apple.com/documentation/coreservices/1413055-mdquerygetresultatindex)

|  | Declaration |
| --- | --- |
| From | ``` func MDQueryGetResultAtIndex(_ query: MDQuery!, _ idx: CFIndex) -> UnsafePointer<Void> ``` |
| To | ``` func MDQueryGetResultAtIndex(_ query: MDQuery!, _ idx: CFIndex) -> UnsafeRawPointer! ``` |

Modified [MDQuerySetCreateResultFunction(_: MDQuery!, _: CoreServices.MDQueryCreateResultFunction!, _: UnsafeMutableRawPointer!, _: UnsafePointer<CFArrayCallBacks>!)](https://developer.apple.com/documentation/coreservices/1413064-mdquerysetcreateresultfunction)

|  | Declaration |
| --- | --- |
| From | ``` func MDQuerySetCreateResultFunction(_ query: MDQuery!, _ func: MDQueryCreateResultFunction!, _ context: UnsafeMutablePointer<Void>, _ cb: UnsafePointer<CFArrayCallBacks>) ``` |
| To | ``` func MDQuerySetCreateResultFunction(_ query: MDQuery!, _ func: CoreServices.MDQueryCreateResultFunction!, _ context: UnsafeMutableRawPointer!, _ cb: UnsafePointer<CFArrayCallBacks>!) ``` |

Modified [MDQuerySetCreateValueFunction(_: MDQuery!, _: CoreServices.MDQueryCreateValueFunction!, _: UnsafeMutableRawPointer!, _: UnsafePointer<CFArrayCallBacks>!)](https://developer.apple.com/documentation/coreservices/1413017-mdquerysetcreatevaluefunction)

|  | Declaration |
| --- | --- |
| From | ``` func MDQuerySetCreateValueFunction(_ query: MDQuery!, _ func: MDQueryCreateValueFunction!, _ context: UnsafeMutablePointer<Void>, _ cb: UnsafePointer<CFArrayCallBacks>) ``` |
| To | ``` func MDQuerySetCreateValueFunction(_ query: MDQuery!, _ func: CoreServices.MDQueryCreateValueFunction!, _ context: UnsafeMutableRawPointer!, _ cb: UnsafePointer<CFArrayCallBacks>!) ``` |

Modified [MDQuerySetDispatchQueue(_: MDQuery!, _: DispatchQueue!)](https://developer.apple.com/documentation/coreservices/1413019-mdquerysetdispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` func MDQuerySetDispatchQueue(_ query: MDQuery!, _ queue: dispatch_queue_t!) ``` |
| To | ``` func MDQuerySetDispatchQueue(_ query: MDQuery!, _ queue: DispatchQueue!) ``` |

Modified [MDQuerySetSortComparator(_: MDQuery!, _: CoreServices.MDQuerySortComparatorFunction!, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/coreservices/1413087-mdquerysetsortcomparator)

|  | Declaration |
| --- | --- |
| From | ``` func MDQuerySetSortComparator(_ query: MDQuery!, _ comparator: MDQuerySortComparatorFunction!, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func MDQuerySetSortComparator(_ query: MDQuery!, _ comparator: CoreServices.MDQuerySortComparatorFunction!, _ context: UnsafeMutableRawPointer!) ``` |

Modified [MDQuerySetSortComparatorBlock(_: MDQuery!, _: ( (UnsafePointer<Unmanaged<CFTypeRef>?>?, UnsafePointer<Unmanaged<CFTypeRef>?>?) -> CFComparisonResult)!)](https://developer.apple.com/documentation/coreservices/1413021-mdquerysetsortcomparatorblock)

|  | Declaration |
| --- | --- |
| From | ``` func MDQuerySetSortComparatorBlock(_ query: MDQuery!, _ comparator: ((UnsafePointer<Unmanaged<AnyObject>?>, UnsafePointer<Unmanaged<AnyObject>?>) -> CFComparisonResult)!) ``` |
| To | ``` func MDQuerySetSortComparatorBlock(_ query: MDQuery!, _ comparator: (@escaping (UnsafePointer<Unmanaged<CFTypeRef>?>?, UnsafePointer<Unmanaged<CFTypeRef>?>?) -> CFComparisonResult)!) ``` |

Modified [MDQuerySortComparatorFunction](https://developer.apple.com/documentation/coreservices/mdquerysortcomparatorfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias MDQuerySortComparatorFunction = (UnsafePointer<Unmanaged<AnyObject>?>, UnsafePointer<Unmanaged<AnyObject>?>, UnsafeMutablePointer<Void>) -> CFComparisonResult ``` |
| To | ``` typealias MDQuerySortComparatorFunction = (UnsafePointer<Unmanaged<CFTypeRef>?>?, UnsafePointer<Unmanaged<CFTypeRef>?>?, UnsafeMutableRawPointer?) -> CFComparisonResult ``` |

Modified [NewAECoerceDescUPP(_: CoreServices.AECoerceDescProcPtr!) -> CoreServices.AECoerceDescUPP!](https://developer.apple.com/documentation/coreservices/1445885-newaecoercedescupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewAECoerceDescUPP(_ userRoutine: AECoerceDescProcPtr!) -> AECoerceDescUPP! ``` |
| To | ``` func NewAECoerceDescUPP(_ userRoutine: CoreServices.AECoerceDescProcPtr!) -> CoreServices.AECoerceDescUPP! ``` |

Modified [NewAECoercePtrUPP(_: CoreServices.AECoercePtrProcPtr!) -> CoreServices.AECoercePtrUPP!](https://developer.apple.com/documentation/coreservices/1449962-newaecoerceptrupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewAECoercePtrUPP(_ userRoutine: AECoercePtrProcPtr!) -> AECoercePtrUPP! ``` |
| To | ``` func NewAECoercePtrUPP(_ userRoutine: CoreServices.AECoercePtrProcPtr!) -> CoreServices.AECoercePtrUPP! ``` |

Modified [NewAEDisposeExternalUPP(_: CoreServices.AEDisposeExternalProcPtr!) -> CoreServices.AEDisposeExternalUPP!](https://developer.apple.com/documentation/coreservices/1447774-newaedisposeexternalupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewAEDisposeExternalUPP(_ userRoutine: AEDisposeExternalProcPtr!) -> AEDisposeExternalUPP! ``` |
| To | ``` func NewAEDisposeExternalUPP(_ userRoutine: CoreServices.AEDisposeExternalProcPtr!) -> CoreServices.AEDisposeExternalUPP! ``` |

Modified [NewAEEventHandlerUPP(_: CoreServices.AEEventHandlerProcPtr!) -> CoreServices.AEEventHandlerUPP!](https://developer.apple.com/documentation/coreservices/1446862-newaeeventhandlerupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewAEEventHandlerUPP(_ userRoutine: AEEventHandlerProcPtr!) -> AEEventHandlerUPP! ``` |
| To | ``` func NewAEEventHandlerUPP(_ userRoutine: CoreServices.AEEventHandlerProcPtr!) -> CoreServices.AEEventHandlerUPP! ``` |

Modified [NewIndexToUCStringUPP(_: CoreServices.IndexToUCStringProcPtr!) -> CoreServices.IndexToUCStringUPP!](https://developer.apple.com/documentation/coreservices/1390384-newindextoucstringupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewIndexToUCStringUPP(_ userRoutine: IndexToUCStringProcPtr!) -> IndexToUCStringUPP! ``` |
| To | ``` func NewIndexToUCStringUPP(_ userRoutine: CoreServices.IndexToUCStringProcPtr!) -> CoreServices.IndexToUCStringUPP! ``` |

Modified [NewOSLAccessorUPP(_: CoreServices.OSLAccessorProcPtr!) -> CoreServices.OSLAccessorUPP!](https://developer.apple.com/documentation/coreservices/1449584-newoslaccessorupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewOSLAccessorUPP(_ userRoutine: OSLAccessorProcPtr!) -> OSLAccessorUPP! ``` |
| To | ``` func NewOSLAccessorUPP(_ userRoutine: CoreServices.OSLAccessorProcPtr!) -> CoreServices.OSLAccessorUPP! ``` |

Modified [NewOSLAdjustMarksUPP(_: CoreServices.OSLAdjustMarksProcPtr!) -> CoreServices.OSLAdjustMarksUPP!](https://developer.apple.com/documentation/coreservices/1443347-newosladjustmarksupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewOSLAdjustMarksUPP(_ userRoutine: OSLAdjustMarksProcPtr!) -> OSLAdjustMarksUPP! ``` |
| To | ``` func NewOSLAdjustMarksUPP(_ userRoutine: CoreServices.OSLAdjustMarksProcPtr!) -> CoreServices.OSLAdjustMarksUPP! ``` |

Modified [NewOSLCompareUPP(_: CoreServices.OSLCompareProcPtr!) -> CoreServices.OSLCompareUPP!](https://developer.apple.com/documentation/coreservices/1444603-newoslcompareupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewOSLCompareUPP(_ userRoutine: OSLCompareProcPtr!) -> OSLCompareUPP! ``` |
| To | ``` func NewOSLCompareUPP(_ userRoutine: CoreServices.OSLCompareProcPtr!) -> CoreServices.OSLCompareUPP! ``` |

Modified [NewOSLCountUPP(_: CoreServices.OSLCountProcPtr!) -> CoreServices.OSLCountUPP!](https://developer.apple.com/documentation/coreservices/1448156-newoslcountupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewOSLCountUPP(_ userRoutine: OSLCountProcPtr!) -> OSLCountUPP! ``` |
| To | ``` func NewOSLCountUPP(_ userRoutine: CoreServices.OSLCountProcPtr!) -> CoreServices.OSLCountUPP! ``` |

Modified [NewOSLDisposeTokenUPP(_: CoreServices.OSLDisposeTokenProcPtr!) -> CoreServices.OSLDisposeTokenUPP!](https://developer.apple.com/documentation/coreservices/1450027-newosldisposetokenupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewOSLDisposeTokenUPP(_ userRoutine: OSLDisposeTokenProcPtr!) -> OSLDisposeTokenUPP! ``` |
| To | ``` func NewOSLDisposeTokenUPP(_ userRoutine: CoreServices.OSLDisposeTokenProcPtr!) -> CoreServices.OSLDisposeTokenUPP! ``` |

Modified [NewOSLGetErrDescUPP(_: CoreServices.OSLGetErrDescProcPtr!) -> CoreServices.OSLGetErrDescUPP!](https://developer.apple.com/documentation/coreservices/1447934-newoslgeterrdescupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewOSLGetErrDescUPP(_ userRoutine: OSLGetErrDescProcPtr!) -> OSLGetErrDescUPP! ``` |
| To | ``` func NewOSLGetErrDescUPP(_ userRoutine: CoreServices.OSLGetErrDescProcPtr!) -> CoreServices.OSLGetErrDescUPP! ``` |

Modified [NewOSLGetMarkTokenUPP(_: CoreServices.OSLGetMarkTokenProcPtr!) -> CoreServices.OSLGetMarkTokenUPP!](https://developer.apple.com/documentation/coreservices/1445166-newoslgetmarktokenupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewOSLGetMarkTokenUPP(_ userRoutine: OSLGetMarkTokenProcPtr!) -> OSLGetMarkTokenUPP! ``` |
| To | ``` func NewOSLGetMarkTokenUPP(_ userRoutine: CoreServices.OSLGetMarkTokenProcPtr!) -> CoreServices.OSLGetMarkTokenUPP! ``` |

Modified [NewOSLMarkUPP(_: CoreServices.OSLMarkProcPtr!) -> CoreServices.OSLMarkUPP!](https://developer.apple.com/documentation/coreservices/1446942-newoslmarkupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewOSLMarkUPP(_ userRoutine: OSLMarkProcPtr!) -> OSLMarkUPP! ``` |
| To | ``` func NewOSLMarkUPP(_ userRoutine: CoreServices.OSLMarkProcPtr!) -> CoreServices.OSLMarkUPP! ``` |

Modified [OffsetArrayHandle](https://developer.apple.com/documentation/coreservices/offsetarrayhandle)

|  | Declaration |
| --- | --- |
| From | ``` typealias OffsetArrayHandle = UnsafeMutablePointer<OffsetArrayPtr> ``` |
| To | ``` typealias OffsetArrayHandle = UnsafeMutablePointer<OffsetArrayPtr?> ``` |

Modified [OSLAccessorProcPtr](https://developer.apple.com/documentation/coreservices/oslaccessorprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLAccessorProcPtr = (DescType, UnsafePointer<AEDesc>, DescType, DescType, UnsafePointer<AEDesc>, UnsafeMutablePointer<AEDesc>, SRefCon) -> OSErr ``` |
| To | ``` typealias OSLAccessorProcPtr = (DescType, UnsafePointer<AEDesc>?, DescType, DescType, UnsafePointer<AEDesc>?, UnsafeMutablePointer<AEDesc>?, SRefCon?) -> OSErr ``` |

Modified [OSLAccessorUPP](https://developer.apple.com/documentation/coreservices/oslaccessorupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLAccessorUPP = OSLAccessorProcPtr ``` |
| To | ``` typealias OSLAccessorUPP = CoreServices.OSLAccessorProcPtr ``` |

Modified [OSLAdjustMarksProcPtr](https://developer.apple.com/documentation/coreservices/osladjustmarksprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLAdjustMarksProcPtr = (Int, Int, UnsafePointer<AEDesc>) -> OSErr ``` |
| To | ``` typealias OSLAdjustMarksProcPtr = (Int, Int, UnsafePointer<AEDesc>?) -> OSErr ``` |

Modified [OSLAdjustMarksUPP](https://developer.apple.com/documentation/coreservices/osladjustmarksupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLAdjustMarksUPP = OSLAdjustMarksProcPtr ``` |
| To | ``` typealias OSLAdjustMarksUPP = CoreServices.OSLAdjustMarksProcPtr ``` |

Modified [OSLCompareProcPtr](https://developer.apple.com/documentation/coreservices/oslcompareprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLCompareProcPtr = (DescType, UnsafePointer<AEDesc>, UnsafePointer<AEDesc>, UnsafeMutablePointer<DarwinBoolean>) -> OSErr ``` |
| To | ``` typealias OSLCompareProcPtr = (DescType, UnsafePointer<AEDesc>?, UnsafePointer<AEDesc>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSErr ``` |

Modified [OSLCompareUPP](https://developer.apple.com/documentation/coreservices/oslcompareupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLCompareUPP = OSLCompareProcPtr ``` |
| To | ``` typealias OSLCompareUPP = CoreServices.OSLCompareProcPtr ``` |

Modified [OSLCountProcPtr](https://developer.apple.com/documentation/coreservices/oslcountprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLCountProcPtr = (DescType, DescType, UnsafePointer<AEDesc>, UnsafeMutablePointer<Int>) -> OSErr ``` |
| To | ``` typealias OSLCountProcPtr = (DescType, DescType, UnsafePointer<AEDesc>?, UnsafeMutablePointer<Int>?) -> OSErr ``` |

Modified [OSLCountUPP](https://developer.apple.com/documentation/coreservices/oslcountupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLCountUPP = OSLCountProcPtr ``` |
| To | ``` typealias OSLCountUPP = CoreServices.OSLCountProcPtr ``` |

Modified [OSLDisposeTokenProcPtr](https://developer.apple.com/documentation/coreservices/osldisposetokenprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLDisposeTokenProcPtr = (UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` typealias OSLDisposeTokenProcPtr = (UnsafeMutablePointer<AEDesc>?) -> OSErr ``` |

Modified [OSLDisposeTokenUPP](https://developer.apple.com/documentation/coreservices/osldisposetokenupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLDisposeTokenUPP = OSLDisposeTokenProcPtr ``` |
| To | ``` typealias OSLDisposeTokenUPP = CoreServices.OSLDisposeTokenProcPtr ``` |

Modified [OSLGetErrDescProcPtr](https://developer.apple.com/documentation/coreservices/oslgeterrdescprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLGetErrDescProcPtr = (UnsafeMutablePointer<UnsafeMutablePointer<AEDesc>>) -> OSErr ``` |
| To | ``` typealias OSLGetErrDescProcPtr = (UnsafeMutablePointer<UnsafeMutablePointer<AEDesc>?>?) -> OSErr ``` |

Modified [OSLGetErrDescUPP](https://developer.apple.com/documentation/coreservices/oslgeterrdescupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLGetErrDescUPP = OSLGetErrDescProcPtr ``` |
| To | ``` typealias OSLGetErrDescUPP = CoreServices.OSLGetErrDescProcPtr ``` |

Modified [OSLGetMarkTokenProcPtr](https://developer.apple.com/documentation/coreservices/oslgetmarktokenprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLGetMarkTokenProcPtr = (UnsafePointer<AEDesc>, DescType, UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` typealias OSLGetMarkTokenProcPtr = (UnsafePointer<AEDesc>?, DescType, UnsafeMutablePointer<AEDesc>?) -> OSErr ``` |

Modified [OSLGetMarkTokenUPP](https://developer.apple.com/documentation/coreservices/oslgetmarktokenupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLGetMarkTokenUPP = OSLGetMarkTokenProcPtr ``` |
| To | ``` typealias OSLGetMarkTokenUPP = CoreServices.OSLGetMarkTokenProcPtr ``` |

Modified [OSLMarkProcPtr](https://developer.apple.com/documentation/coreservices/oslmarkprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLMarkProcPtr = (UnsafePointer<AEDesc>, UnsafePointer<AEDesc>, Int) -> OSErr ``` |
| To | ``` typealias OSLMarkProcPtr = (UnsafePointer<AEDesc>?, UnsafePointer<AEDesc>?, Int) -> OSErr ``` |

Modified [OSLMarkUPP](https://developer.apple.com/documentation/coreservices/oslmarkupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLMarkUPP = OSLMarkProcPtr ``` |
| To | ``` typealias OSLMarkUPP = CoreServices.OSLMarkProcPtr ``` |

Modified [OverrideIconRef(_: IconRef!, _: IconRef!) -> OSErr](https://developer.apple.com/documentation/coreservices/1445253-overrideiconref)

|  | Declaration |
| --- | --- |
| From | ``` func OverrideIconRef(_ oldIconRef: IconRef, _ newIconRef: IconRef) -> OSErr ``` |
| To | ``` func OverrideIconRef(_ oldIconRef: IconRef!, _ newIconRef: IconRef!) -> OSErr ``` |

Modified [pArcAngle](https://developer.apple.com/documentation/coreservices/parcangle)

|  | Declaration |
| --- | --- |
| From | ``` var pArcAngle: Int { get } ``` |
| To | ``` var pArcAngle: OSType { get } ``` |

Modified [pATMachine](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/patmachine)

|  | Declaration |
| --- | --- |
| From | ``` var pATMachine: Int { get } ``` |
| To | ``` var pATMachine: OSType { get } ``` |

Modified [pATType](https://developer.apple.com/documentation/coreservices/pattype)

|  | Declaration |
| --- | --- |
| From | ``` var pATType: Int { get } ``` |
| To | ``` var pATType: OSType { get } ``` |

Modified [pATZone](https://developer.apple.com/documentation/coreservices/patzone)

|  | Declaration |
| --- | --- |
| From | ``` var pATZone: Int { get } ``` |
| To | ``` var pATZone: OSType { get } ``` |

Modified [pBackgroundColor](https://developer.apple.com/documentation/coreservices/pbackgroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` var pBackgroundColor: Int { get } ``` |
| To | ``` var pBackgroundColor: OSType { get } ``` |

Modified [pBackgroundPattern](https://developer.apple.com/documentation/coreservices/pbackgroundpattern)

|  | Declaration |
| --- | --- |
| From | ``` var pBackgroundPattern: Int { get } ``` |
| To | ``` var pBackgroundPattern: OSType { get } ``` |

Modified [pBestType](https://developer.apple.com/documentation/coreservices/pbesttype)

|  | Declaration |
| --- | --- |
| From | ``` var pBestType: Int { get } ``` |
| To | ``` var pBestType: OSType { get } ``` |

Modified [pBounds](https://developer.apple.com/documentation/coreservices/pbounds)

|  | Declaration |
| --- | --- |
| From | ``` var pBounds: Int { get } ``` |
| To | ``` var pBounds: OSType { get } ``` |

Modified [pClass](https://developer.apple.com/documentation/coreservices/pclass)

|  | Declaration |
| --- | --- |
| From | ``` var pClass: Int { get } ``` |
| To | ``` var pClass: OSType { get } ``` |

Modified [pClipboard](https://developer.apple.com/documentation/coreservices/pclipboard)

|  | Declaration |
| --- | --- |
| From | ``` var pClipboard: Int { get } ``` |
| To | ``` var pClipboard: OSType { get } ``` |

Modified [pColor](https://developer.apple.com/documentation/coreservices/pcolor)

|  | Declaration |
| --- | --- |
| From | ``` var pColor: Int { get } ``` |
| To | ``` var pColor: OSType { get } ``` |

Modified [pColorTable](https://developer.apple.com/documentation/coreservices/pcolortable)

|  | Declaration |
| --- | --- |
| From | ``` var pColorTable: Int { get } ``` |
| To | ``` var pColorTable: OSType { get } ``` |

Modified [pConduit](https://developer.apple.com/documentation/coreservices/pconduit)

|  | Declaration |
| --- | --- |
| From | ``` var pConduit: Int { get } ``` |
| To | ``` var pConduit: OSType { get } ``` |

Modified [pContents](https://developer.apple.com/documentation/coreservices/1556376-parcangle/pcontents)

|  | Declaration |
| --- | --- |
| From | ``` var pContents: Int { get } ``` |
| To | ``` var pContents: OSType { get } ``` |

Modified [pCornerCurveHeight](https://developer.apple.com/documentation/coreservices/1556376-parcangle/pcornercurveheight)

|  | Declaration |
| --- | --- |
| From | ``` var pCornerCurveHeight: Int { get } ``` |
| To | ``` var pCornerCurveHeight: OSType { get } ``` |

Modified [pCornerCurveWidth](https://developer.apple.com/documentation/coreservices/1556376-parcangle/pcornercurvewidth)

|  | Declaration |
| --- | --- |
| From | ``` var pCornerCurveWidth: Int { get } ``` |
| To | ``` var pCornerCurveWidth: OSType { get } ``` |

Modified [pDashStyle](https://developer.apple.com/documentation/coreservices/pdashstyle)

|  | Declaration |
| --- | --- |
| From | ``` var pDashStyle: Int { get } ``` |
| To | ``` var pDashStyle: OSType { get } ``` |

Modified [pDefaultType](https://developer.apple.com/documentation/coreservices/1556376-parcangle/pdefaulttype)

|  | Declaration |
| --- | --- |
| From | ``` var pDefaultType: Int { get } ``` |
| To | ``` var pDefaultType: OSType { get } ``` |

Modified [pDefinitionRect](https://developer.apple.com/documentation/coreservices/pdefinitionrect)

|  | Declaration |
| --- | --- |
| From | ``` var pDefinitionRect: Int { get } ``` |
| To | ``` var pDefinitionRect: OSType { get } ``` |

Modified [pDeviceAddress](https://developer.apple.com/documentation/coreservices/pdeviceaddress)

|  | Declaration |
| --- | --- |
| From | ``` var pDeviceAddress: Int { get } ``` |
| To | ``` var pDeviceAddress: OSType { get } ``` |

Modified [pDeviceType](https://developer.apple.com/documentation/coreservices/pdevicetype)

|  | Declaration |
| --- | --- |
| From | ``` var pDeviceType: Int { get } ``` |
| To | ``` var pDeviceType: OSType { get } ``` |

Modified [pDNS](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/pdns)

|  | Declaration |
| --- | --- |
| From | ``` var pDNS: Int { get } ``` |
| To | ``` var pDNS: OSType { get } ``` |

Modified [pDNSForm](https://developer.apple.com/documentation/coreservices/1556408-pscheme/pdnsform)

|  | Declaration |
| --- | --- |
| From | ``` var pDNSForm: Int { get } ``` |
| To | ``` var pDNSForm: OSType { get } ``` |

Modified [pDottedDecimal](https://developer.apple.com/documentation/coreservices/pdotteddecimal)

|  | Declaration |
| --- | --- |
| From | ``` var pDottedDecimal: Int { get } ``` |
| To | ``` var pDottedDecimal: OSType { get } ``` |

Modified [pEnabled](https://developer.apple.com/documentation/coreservices/penabled)

|  | Declaration |
| --- | --- |
| From | ``` var pEnabled: Int { get } ``` |
| To | ``` var pEnabled: OSType { get } ``` |

Modified [pEndPoint](https://developer.apple.com/documentation/coreservices/pendpoint)

|  | Declaration |
| --- | --- |
| From | ``` var pEndPoint: Int { get } ``` |
| To | ``` var pEndPoint: OSType { get } ``` |

Modified [pFillColor](https://developer.apple.com/documentation/coreservices/1556376-parcangle/pfillcolor)

|  | Declaration |
| --- | --- |
| From | ``` var pFillColor: Int { get } ``` |
| To | ``` var pFillColor: OSType { get } ``` |

Modified [pFillPattern](https://developer.apple.com/documentation/coreservices/pfillpattern)

|  | Declaration |
| --- | --- |
| From | ``` var pFillPattern: Int { get } ``` |
| To | ``` var pFillPattern: OSType { get } ``` |

Modified [pFont](https://developer.apple.com/documentation/coreservices/1556376-parcangle/pfont)

|  | Declaration |
| --- | --- |
| From | ``` var pFont: Int { get } ``` |
| To | ``` var pFont: OSType { get } ``` |

Modified [pFormula](https://developer.apple.com/documentation/coreservices/pformula)

|  | Declaration |
| --- | --- |
| From | ``` var pFormula: Int { get } ``` |
| To | ``` var pFormula: OSType { get } ``` |

Modified [pFTPKind](https://developer.apple.com/documentation/coreservices/pftpkind)

|  | Declaration |
| --- | --- |
| From | ``` var pFTPKind: Int { get } ``` |
| To | ``` var pFTPKind: OSType { get } ``` |

Modified [pGraphicObjects](https://developer.apple.com/documentation/coreservices/1556373-pformula/pgraphicobjects)

|  | Declaration |
| --- | --- |
| From | ``` var pGraphicObjects: Int { get } ``` |
| To | ``` var pGraphicObjects: OSType { get } ``` |

Modified [pHasCloseBox](https://developer.apple.com/documentation/coreservices/1556373-pformula/phasclosebox)

|  | Declaration |
| --- | --- |
| From | ``` var pHasCloseBox: Int { get } ``` |
| To | ``` var pHasCloseBox: OSType { get } ``` |

Modified [pHasTitleBar](https://developer.apple.com/documentation/coreservices/phastitlebar)

|  | Declaration |
| --- | --- |
| From | ``` var pHasTitleBar: Int { get } ``` |
| To | ``` var pHasTitleBar: OSType { get } ``` |

Modified [pHost](https://developer.apple.com/documentation/coreservices/phost)

|  | Declaration |
| --- | --- |
| From | ``` var pHost: Int { get } ``` |
| To | ``` var pHost: OSType { get } ``` |

Modified [pID](https://developer.apple.com/documentation/coreservices/pid)

|  | Declaration |
| --- | --- |
| From | ``` var pID: Int { get } ``` |
| To | ``` var pID: OSType { get } ``` |

Modified [pIndex](https://developer.apple.com/documentation/coreservices/1556373-pformula/pindex)

|  | Declaration |
| --- | --- |
| From | ``` var pIndex: Int { get } ``` |
| To | ``` var pIndex: OSType { get } ``` |

Modified [pInsertionLoc](https://developer.apple.com/documentation/coreservices/pinsertionloc)

|  | Declaration |
| --- | --- |
| From | ``` var pInsertionLoc: Int { get } ``` |
| To | ``` var pInsertionLoc: OSType { get } ``` |

Modified [pIsFloating](https://developer.apple.com/documentation/coreservices/1556373-pformula/pisfloating)

|  | Declaration |
| --- | --- |
| From | ``` var pIsFloating: Int { get } ``` |
| To | ``` var pIsFloating: OSType { get } ``` |

Modified [pIsFrontProcess](https://developer.apple.com/documentation/coreservices/1556373-pformula/pisfrontprocess)

|  | Declaration |
| --- | --- |
| From | ``` var pIsFrontProcess: Int { get } ``` |
| To | ``` var pIsFrontProcess: OSType { get } ``` |

Modified [pIsModal](https://developer.apple.com/documentation/coreservices/1556373-pformula/pismodal)

|  | Declaration |
| --- | --- |
| From | ``` var pIsModal: Int { get } ``` |
| To | ``` var pIsModal: OSType { get } ``` |

Modified [pIsModified](https://developer.apple.com/documentation/coreservices/1556373-pformula/pismodified)

|  | Declaration |
| --- | --- |
| From | ``` var pIsModified: Int { get } ``` |
| To | ``` var pIsModified: OSType { get } ``` |

Modified [pIsResizable](https://developer.apple.com/documentation/coreservices/pisresizable)

|  | Declaration |
| --- | --- |
| From | ``` var pIsResizable: Int { get } ``` |
| To | ``` var pIsResizable: OSType { get } ``` |

Modified [pIsStationeryPad](https://developer.apple.com/documentation/coreservices/1556373-pformula/pisstationerypad)

|  | Declaration |
| --- | --- |
| From | ``` var pIsStationeryPad: Int { get } ``` |
| To | ``` var pIsStationeryPad: OSType { get } ``` |

Modified [pIsZoomable](https://developer.apple.com/documentation/coreservices/1556373-pformula/piszoomable)

|  | Declaration |
| --- | --- |
| From | ``` var pIsZoomable: Int { get } ``` |
| To | ``` var pIsZoomable: OSType { get } ``` |

Modified [pIsZoomed](https://developer.apple.com/documentation/coreservices/1556373-pformula/piszoomed)

|  | Declaration |
| --- | --- |
| From | ``` var pIsZoomed: Int { get } ``` |
| To | ``` var pIsZoomed: OSType { get } ``` |

Modified [pItemNumber](https://developer.apple.com/documentation/coreservices/pitemnumber)

|  | Declaration |
| --- | --- |
| From | ``` var pItemNumber: Int { get } ``` |
| To | ``` var pItemNumber: OSType { get } ``` |

Modified [pJustification](https://developer.apple.com/documentation/coreservices/pjustification)

|  | Declaration |
| --- | --- |
| From | ``` var pJustification: Int { get } ``` |
| To | ``` var pJustification: OSType { get } ``` |

Modified [pKeyKind](https://developer.apple.com/documentation/coreservices/pkeykind)

|  | Declaration |
| --- | --- |
| From | ``` var pKeyKind: Int { get } ``` |
| To | ``` var pKeyKind: OSType { get } ``` |

Modified [pKeystrokeKey](https://developer.apple.com/documentation/coreservices/1556385-ckeystroke/pkeystrokekey)

|  | Declaration |
| --- | --- |
| From | ``` var pKeystrokeKey: Int { get } ``` |
| To | ``` var pKeystrokeKey: OSType { get } ``` |

Modified [pLineArrow](https://developer.apple.com/documentation/coreservices/plinearrow)

|  | Declaration |
| --- | --- |
| From | ``` var pLineArrow: Int { get } ``` |
| To | ``` var pLineArrow: OSType { get } ``` |

Modified [pMenuID](https://developer.apple.com/documentation/coreservices/pmenuid)

|  | Declaration |
| --- | --- |
| From | ``` var pMenuID: Int { get } ``` |
| To | ``` var pMenuID: OSType { get } ``` |

Modified [pModifiers](https://developer.apple.com/documentation/coreservices/pmodifiers)

|  | Declaration |
| --- | --- |
| From | ``` var pModifiers: Int { get } ``` |
| To | ``` var pModifiers: OSType { get } ``` |

Modified [pName](https://developer.apple.com/documentation/coreservices/1556373-pformula/pname)

|  | Declaration |
| --- | --- |
| From | ``` var pName: Int { get } ``` |
| To | ``` var pName: OSType { get } ``` |

Modified [pNetwork](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/pnetwork)

|  | Declaration |
| --- | --- |
| From | ``` var pNetwork: Int { get } ``` |
| To | ``` var pNetwork: OSType { get } ``` |

Modified [pNewElementLoc](https://developer.apple.com/documentation/coreservices/pnewelementloc)

|  | Declaration |
| --- | --- |
| From | ``` var pNewElementLoc: Int { get } ``` |
| To | ``` var pNewElementLoc: OSType { get } ``` |

Modified [pNode](https://developer.apple.com/documentation/coreservices/pnode)

|  | Declaration |
| --- | --- |
| From | ``` var pNode: Int { get } ``` |
| To | ``` var pNode: OSType { get } ``` |

Modified [pPath](https://developer.apple.com/documentation/coreservices/1556408-pscheme/ppath)

|  | Declaration |
| --- | --- |
| From | ``` var pPath: Int { get } ``` |
| To | ``` var pPath: OSType { get } ``` |

Modified [pPenColor](https://developer.apple.com/documentation/coreservices/ppencolor)

|  | Declaration |
| --- | --- |
| From | ``` var pPenColor: Int { get } ``` |
| To | ``` var pPenColor: OSType { get } ``` |

Modified [pPenPattern](https://developer.apple.com/documentation/coreservices/1556400-pnewelementloc/ppenpattern)

|  | Declaration |
| --- | --- |
| From | ``` var pPenPattern: Int { get } ``` |
| To | ``` var pPenPattern: OSType { get } ``` |

Modified [pPenWidth](https://developer.apple.com/documentation/coreservices/1556400-pnewelementloc/ppenwidth)

|  | Declaration |
| --- | --- |
| From | ``` var pPenWidth: Int { get } ``` |
| To | ``` var pPenWidth: OSType { get } ``` |

Modified [pPixelDepth](https://developer.apple.com/documentation/coreservices/ppixeldepth)

|  | Declaration |
| --- | --- |
| From | ``` var pPixelDepth: Int { get } ``` |
| To | ``` var pPixelDepth: OSType { get } ``` |

Modified [pPointList](https://developer.apple.com/documentation/coreservices/ppointlist)

|  | Declaration |
| --- | --- |
| From | ``` var pPointList: Int { get } ``` |
| To | ``` var pPointList: OSType { get } ``` |

Modified [pPointSize](https://developer.apple.com/documentation/coreservices/1556400-pnewelementloc/ppointsize)

|  | Declaration |
| --- | --- |
| From | ``` var pPointSize: Int { get } ``` |
| To | ``` var pPointSize: OSType { get } ``` |

Modified [pPort](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/pport)

|  | Declaration |
| --- | --- |
| From | ``` var pPort: Int { get } ``` |
| To | ``` var pPort: OSType { get } ``` |

Modified [pProtection](https://developer.apple.com/documentation/coreservices/1556400-pnewelementloc/pprotection)

|  | Declaration |
| --- | --- |
| From | ``` var pProtection: Int { get } ``` |
| To | ``` var pProtection: OSType { get } ``` |

Modified [pProtocol](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/pprotocol)

|  | Declaration |
| --- | --- |
| From | ``` var pProtocol: Int { get } ``` |
| To | ``` var pProtocol: OSType { get } ``` |

Modified [pRotation](https://developer.apple.com/documentation/coreservices/1556400-pnewelementloc/protation)

|  | Declaration |
| --- | --- |
| From | ``` var pRotation: Int { get } ``` |
| To | ``` var pRotation: OSType { get } ``` |

Modified [pScale](https://developer.apple.com/documentation/coreservices/pscale)

|  | Declaration |
| --- | --- |
| From | ``` var pScale: Int { get } ``` |
| To | ``` var pScale: OSType { get } ``` |

Modified [pScheme](https://developer.apple.com/documentation/coreservices/1556408-pscheme/pscheme)

|  | Declaration |
| --- | --- |
| From | ``` var pScheme: Int { get } ``` |
| To | ``` var pScheme: OSType { get } ``` |

Modified [pScript](https://developer.apple.com/documentation/coreservices/1556400-pnewelementloc/pscript)

|  | Declaration |
| --- | --- |
| From | ``` var pScript: Int { get } ``` |
| To | ``` var pScript: OSType { get } ``` |

Modified [pScriptTag](https://developer.apple.com/documentation/coreservices/1556400-pnewelementloc/pscripttag)

|  | Declaration |
| --- | --- |
| From | ``` var pScriptTag: Int { get } ``` |
| To | ``` var pScriptTag: OSType { get } ``` |

Modified [pSCSIBus](https://developer.apple.com/documentation/coreservices/pscsibus)

|  | Declaration |
| --- | --- |
| From | ``` var pSCSIBus: Int { get } ``` |
| To | ``` var pSCSIBus: OSType { get } ``` |

Modified [pSCSILUN](https://developer.apple.com/documentation/coreservices/pscsilun)

|  | Declaration |
| --- | --- |
| From | ``` var pSCSILUN: Int { get } ``` |
| To | ``` var pSCSILUN: OSType { get } ``` |

Modified [pSelected](https://developer.apple.com/documentation/coreservices/pselected)

|  | Declaration |
| --- | --- |
| From | ``` var pSelected: Int { get } ``` |
| To | ``` var pSelected: OSType { get } ``` |

Modified [pSelection](https://developer.apple.com/documentation/coreservices/pselection)

|  | Declaration |
| --- | --- |
| From | ``` var pSelection: Int { get } ``` |
| To | ``` var pSelection: OSType { get } ``` |

Modified [pSocket](https://developer.apple.com/documentation/coreservices/1556369-kconnsuite/psocket)

|  | Declaration |
| --- | --- |
| From | ``` var pSocket: Int { get } ``` |
| To | ``` var pSocket: OSType { get } ``` |

Modified [pStartAngle](https://developer.apple.com/documentation/coreservices/pstartangle)

|  | Declaration |
| --- | --- |
| From | ``` var pStartAngle: Int { get } ``` |
| To | ``` var pStartAngle: OSType { get } ``` |

Modified [pStartPoint](https://developer.apple.com/documentation/coreservices/pstartpoint)

|  | Declaration |
| --- | --- |
| From | ``` var pStartPoint: Int { get } ``` |
| To | ``` var pStartPoint: OSType { get } ``` |

Modified [pTextColor](https://developer.apple.com/documentation/coreservices/ptextcolor)

|  | Declaration |
| --- | --- |
| From | ``` var pTextColor: Int { get } ``` |
| To | ``` var pTextColor: OSType { get } ``` |

Modified [pTextEncoding](https://developer.apple.com/documentation/coreservices/ptextencoding)

|  | Declaration |
| --- | --- |
| From | ``` var pTextEncoding: Int { get } ``` |
| To | ``` var pTextEncoding: OSType { get } ``` |

Modified [pTextFont](https://developer.apple.com/documentation/coreservices/1556400-pnewelementloc/ptextfont)

|  | Declaration |
| --- | --- |
| From | ``` var pTextFont: Int { get } ``` |
| To | ``` var pTextFont: OSType { get } ``` |

Modified [pTextItemDelimiters](https://developer.apple.com/documentation/coreservices/1556400-pnewelementloc/ptextitemdelimiters)

|  | Declaration |
| --- | --- |
| From | ``` var pTextItemDelimiters: Int { get } ``` |
| To | ``` var pTextItemDelimiters: OSType { get } ``` |

Modified [pTextPointSize](https://developer.apple.com/documentation/coreservices/ptextpointsize)

|  | Declaration |
| --- | --- |
| From | ``` var pTextPointSize: Int { get } ``` |
| To | ``` var pTextPointSize: OSType { get } ``` |

Modified [pTextStyles](https://developer.apple.com/documentation/coreservices/1556367-ptextstyles/ptextstyles)

|  | Declaration |
| --- | --- |
| From | ``` var pTextStyles: Int { get } ``` |
| To | ``` var pTextStyles: OSType { get } ``` |

Modified [pTransferMode](https://developer.apple.com/documentation/coreservices/ptransfermode)

|  | Declaration |
| --- | --- |
| From | ``` var pTransferMode: Int { get } ``` |
| To | ``` var pTransferMode: OSType { get } ``` |

Modified [pTranslation](https://developer.apple.com/documentation/coreservices/ptranslation)

|  | Declaration |
| --- | --- |
| From | ``` var pTranslation: Int { get } ``` |
| To | ``` var pTranslation: OSType { get } ``` |

Modified [pUniformStyles](https://developer.apple.com/documentation/coreservices/1556367-ptextstyles/puniformstyles)

|  | Declaration |
| --- | --- |
| From | ``` var pUniformStyles: Int { get } ``` |
| To | ``` var pUniformStyles: OSType { get } ``` |

Modified [pUpdateOn](https://developer.apple.com/documentation/coreservices/pupdateon)

|  | Declaration |
| --- | --- |
| From | ``` var pUpdateOn: Int { get } ``` |
| To | ``` var pUpdateOn: OSType { get } ``` |

Modified [pURL](https://developer.apple.com/documentation/coreservices/purl)

|  | Declaration |
| --- | --- |
| From | ``` var pURL: Int { get } ``` |
| To | ``` var pURL: OSType { get } ``` |

Modified [pUserName](https://developer.apple.com/documentation/coreservices/pusername)

|  | Declaration |
| --- | --- |
| From | ``` var pUserName: Int { get } ``` |
| To | ``` var pUserName: OSType { get } ``` |

Modified [pUserPassword](https://developer.apple.com/documentation/coreservices/puserpassword)

|  | Declaration |
| --- | --- |
| From | ``` var pUserPassword: Int { get } ``` |
| To | ``` var pUserPassword: OSType { get } ``` |

Modified [pUserSelection](https://developer.apple.com/documentation/coreservices/puserselection)

|  | Declaration |
| --- | --- |
| From | ``` var pUserSelection: Int { get } ``` |
| To | ``` var pUserSelection: OSType { get } ``` |

Modified [pVersion](https://developer.apple.com/documentation/coreservices/1556367-ptextstyles/pversion)

|  | Declaration |
| --- | --- |
| From | ``` var pVersion: Int { get } ``` |
| To | ``` var pVersion: OSType { get } ``` |

Modified [pVisible](https://developer.apple.com/documentation/coreservices/1556367-ptextstyles/pvisible)

|  | Declaration |
| --- | --- |
| From | ``` var pVisible: Int { get } ``` |
| To | ``` var pVisible: OSType { get } ``` |

Modified [ReadIconFromFSRef(_: UnsafePointer<FSRef>!, _: UnsafeMutablePointer<IconFamilyHandle?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1444939-readiconfromfsref)

|  | Declaration |
| --- | --- |
| From | ``` func ReadIconFromFSRef(_ ref: UnsafePointer<FSRef>, _ iconFamily: UnsafeMutablePointer<IconFamilyHandle>) -> OSStatus ``` |
| To | ``` func ReadIconFromFSRef(_ ref: UnsafePointer<FSRef>!, _ iconFamily: UnsafeMutablePointer<IconFamilyHandle?>!) -> OSStatus ``` |

Modified [RegisterIconRefFromFSRef(_: OSType, _: OSType, _: UnsafePointer<FSRef>!, _: UnsafeMutablePointer<IconRef?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1446795-registericonreffromfsref)

|  | Declaration |
| --- | --- |
| From | ``` func RegisterIconRefFromFSRef(_ creator: OSType, _ iconType: OSType, _ iconFile: UnsafePointer<FSRef>, _ theIconRef: UnsafeMutablePointer<IconRef>) -> OSStatus ``` |
| To | ``` func RegisterIconRefFromFSRef(_ creator: OSType, _ iconType: OSType, _ iconFile: UnsafePointer<FSRef>!, _ theIconRef: UnsafeMutablePointer<IconRef?>!) -> OSStatus ``` |

Modified [RegisterIconRefFromIconFamily(_: OSType, _: OSType, _: IconFamilyHandle!, _: UnsafeMutablePointer<IconRef?>!) -> OSErr](https://developer.apple.com/documentation/coreservices/1443918-registericonreffromiconfamily)

|  | Declaration |
| --- | --- |
| From | ``` func RegisterIconRefFromIconFamily(_ creator: OSType, _ iconType: OSType, _ iconFamily: IconFamilyHandle, _ theIconRef: UnsafeMutablePointer<IconRef>) -> OSErr ``` |
| To | ``` func RegisterIconRefFromIconFamily(_ creator: OSType, _ iconType: OSType, _ iconFamily: IconFamilyHandle!, _ theIconRef: UnsafeMutablePointer<IconRef?>!) -> OSErr ``` |

Modified [ReleaseIconRef(_: IconRef!) -> OSErr](https://developer.apple.com/documentation/coreservices/1443504-releaseiconref)

|  | Declaration |
| --- | --- |
| From | ``` func ReleaseIconRef(_ theIconRef: IconRef) -> OSErr ``` |
| To | ``` func ReleaseIconRef(_ theIconRef: IconRef!) -> OSErr ``` |

Modified [RemoveIconRefOverride(_: IconRef!) -> OSErr](https://developer.apple.com/documentation/coreservices/1445832-removeiconrefoverride)

|  | Declaration |
| --- | --- |
| From | ``` func RemoveIconRefOverride(_ theIconRef: IconRef) -> OSErr ``` |
| To | ``` func RemoveIconRefOverride(_ theIconRef: IconRef!) -> OSErr ``` |

Modified [SKIndexCopyDocumentRefsForDocumentIDs(_: SKIndex!, _: CFIndex, _: UnsafeMutablePointer<SKDocumentID>!, _: UnsafeMutablePointer<Unmanaged<SKDocument>?>!)](https://developer.apple.com/documentation/coreservices/1445305-skindexcopydocumentrefsfordocume)

|  | Declaration |
| --- | --- |
| From | ``` func SKIndexCopyDocumentRefsForDocumentIDs(_ inIndex: SKIndex!, _ inCount: CFIndex, _ inDocumentIDsArray: UnsafeMutablePointer<SKDocumentID>, _ outDocumentRefsArray: UnsafeMutablePointer<Unmanaged<SKDocument>?>) ``` |
| To | ``` func SKIndexCopyDocumentRefsForDocumentIDs(_ inIndex: SKIndex!, _ inCount: CFIndex, _ inDocumentIDsArray: UnsafeMutablePointer<SKDocumentID>!, _ outDocumentRefsArray: UnsafeMutablePointer<Unmanaged<SKDocument>?>!) ``` |

Modified [SKIndexCopyDocumentURLsForDocumentIDs(_: SKIndex!, _: CFIndex, _: UnsafeMutablePointer<SKDocumentID>!, _: UnsafeMutablePointer<Unmanaged<CFURL>?>!)](https://developer.apple.com/documentation/coreservices/1443501-skindexcopydocumenturlsfordocume)

|  | Declaration |
| --- | --- |
| From | ``` func SKIndexCopyDocumentURLsForDocumentIDs(_ inIndex: SKIndex!, _ inCount: CFIndex, _ inDocumentIDsArray: UnsafeMutablePointer<SKDocumentID>, _ outDocumentURLsArray: UnsafeMutablePointer<Unmanaged<CFURL>?>) ``` |
| To | ``` func SKIndexCopyDocumentURLsForDocumentIDs(_ inIndex: SKIndex!, _ inCount: CFIndex, _ inDocumentIDsArray: UnsafeMutablePointer<SKDocumentID>!, _ outDocumentURLsArray: UnsafeMutablePointer<Unmanaged<CFURL>?>!) ``` |

Modified [SKIndexCopyInfoForDocumentIDs(_: SKIndex!, _: CFIndex, _: UnsafeMutablePointer<SKDocumentID>!, _: UnsafeMutablePointer<Unmanaged<CFString>?>!, _: UnsafeMutablePointer<SKDocumentID>!)](https://developer.apple.com/documentation/coreservices/1445499-skindexcopyinfofordocumentids)

|  | Declaration |
| --- | --- |
| From | ``` func SKIndexCopyInfoForDocumentIDs(_ inIndex: SKIndex!, _ inCount: CFIndex, _ inDocumentIDsArray: UnsafeMutablePointer<SKDocumentID>, _ outNamesArray: UnsafeMutablePointer<Unmanaged<CFString>?>, _ outParentIDsArray: UnsafeMutablePointer<SKDocumentID>) ``` |
| To | ``` func SKIndexCopyInfoForDocumentIDs(_ inIndex: SKIndex!, _ inCount: CFIndex, _ inDocumentIDsArray: UnsafeMutablePointer<SKDocumentID>!, _ outNamesArray: UnsafeMutablePointer<Unmanaged<CFString>?>!, _ outParentIDsArray: UnsafeMutablePointer<SKDocumentID>!) ``` |

Modified [SKSearchFindMatches(_: SKSearch!, _: CFIndex, _: UnsafeMutablePointer<SKDocumentID>!, _: UnsafeMutablePointer<Float>!, _: CFTimeInterval, _: UnsafeMutablePointer<CFIndex>!) -> Bool](https://developer.apple.com/documentation/coreservices/1448608-sksearchfindmatches)

|  | Declaration |
| --- | --- |
| From | ``` func SKSearchFindMatches(_ inSearch: SKSearch!, _ inMaximumCount: CFIndex, _ outDocumentIDsArray: UnsafeMutablePointer<SKDocumentID>, _ outScoresArray: UnsafeMutablePointer<Float>, _ maximumTime: CFTimeInterval, _ outFoundCount: UnsafeMutablePointer<CFIndex>) -> Bool ``` |
| To | ``` func SKSearchFindMatches(_ inSearch: SKSearch!, _ inMaximumCount: CFIndex, _ outDocumentIDsArray: UnsafeMutablePointer<SKDocumentID>!, _ outScoresArray: UnsafeMutablePointer<Float>!, _ maximumTime: CFTimeInterval, _ outFoundCount: UnsafeMutablePointer<CFIndex>!) -> Bool ``` |

Modified [SKSearchResultsFilterCallBack](https://developer.apple.com/documentation/coreservices/sksearchresultsfiltercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias SKSearchResultsFilterCallBack = (SKIndex!, SKDocument!, UnsafeMutablePointer<Void>) -> DarwinBoolean ``` |
| To | ``` typealias SKSearchResultsFilterCallBack = (SKIndex?, SKDocument?, UnsafeMutableRawPointer?) -> DarwinBoolean ``` |

Modified [SKSummaryGetParagraphSummaryInfo(_: SKSummary!, _: CFIndex, _: UnsafeMutablePointer<CFIndex>!, _: UnsafeMutablePointer<CFIndex>!) -> CFIndex](https://developer.apple.com/documentation/coreservices/1447517-sksummarygetparagraphsummaryinfo)

|  | Declaration |
| --- | --- |
| From | ``` func SKSummaryGetParagraphSummaryInfo(_ summary: SKSummary!, _ numParagraphsInSummary: CFIndex, _ outRankOrderOfParagraphs: UnsafeMutablePointer<CFIndex>, _ outParagraphIndexOfParagraphs: UnsafeMutablePointer<CFIndex>) -> CFIndex ``` |
| To | ``` func SKSummaryGetParagraphSummaryInfo(_ summary: SKSummary!, _ numParagraphsInSummary: CFIndex, _ outRankOrderOfParagraphs: UnsafeMutablePointer<CFIndex>!, _ outParagraphIndexOfParagraphs: UnsafeMutablePointer<CFIndex>!) -> CFIndex ``` |

Modified [SKSummaryGetSentenceSummaryInfo(_: SKSummary!, _: CFIndex, _: UnsafeMutablePointer<CFIndex>!, _: UnsafeMutablePointer<CFIndex>!, _: UnsafeMutablePointer<CFIndex>!) -> CFIndex](https://developer.apple.com/documentation/coreservices/1444767-sksummarygetsentencesummaryinfo)

|  | Declaration |
| --- | --- |
| From | ``` func SKSummaryGetSentenceSummaryInfo(_ summary: SKSummary!, _ numSentencesInSummary: CFIndex, _ outRankOrderOfSentences: UnsafeMutablePointer<CFIndex>, _ outSentenceIndexOfSentences: UnsafeMutablePointer<CFIndex>, _ outParagraphIndexOfSentences: UnsafeMutablePointer<CFIndex>) -> CFIndex ``` |
| To | ``` func SKSummaryGetSentenceSummaryInfo(_ summary: SKSummary!, _ numSentencesInSummary: CFIndex, _ outRankOrderOfSentences: UnsafeMutablePointer<CFIndex>!, _ outSentenceIndexOfSentences: UnsafeMutablePointer<CFIndex>!, _ outParagraphIndexOfSentences: UnsafeMutablePointer<CFIndex>!) -> CFIndex ``` |

Modified [TextBreakLocatorRef](https://developer.apple.com/documentation/coreservices/textbreaklocatorref)

|  | Declaration |
| --- | --- |
| From | ``` typealias TextBreakLocatorRef = COpaquePointer ``` |
| To | ``` typealias TextBreakLocatorRef = OpaquePointer ``` |

Modified [TextRangeArrayHandle](https://developer.apple.com/documentation/coreservices/textrangearrayhandle)

|  | Declaration |
| --- | --- |
| From | ``` typealias TextRangeArrayHandle = UnsafeMutablePointer<TextRangeArrayPtr> ``` |
| To | ``` typealias TextRangeArrayHandle = UnsafeMutablePointer<TextRangeArrayPtr?> ``` |

Modified [TextRangeHandle](https://developer.apple.com/documentation/coreservices/textrangehandle)

|  | Declaration |
| --- | --- |
| From | ``` typealias TextRangeHandle = UnsafeMutablePointer<TextRangePtr> ``` |
| To | ``` typealias TextRangeHandle = UnsafeMutablePointer<TextRangePtr?> ``` |

Modified [type128BitFloatingPoint](https://developer.apple.com/documentation/coreservices/1542872-numeric_descriptor_type_constant/type128bitfloatingpoint)

|  | Declaration |
| --- | --- |
| From | ``` var type128BitFloatingPoint: Int { get } ``` |
| To | ``` var type128BitFloatingPoint: DescType { get } ``` |

Modified [typeAbsoluteOrdinal](https://developer.apple.com/documentation/coreservices/1645753-anonymous/typeabsoluteordinal)

|  | Declaration |
| --- | --- |
| From | ``` var typeAbsoluteOrdinal: Int { get } ``` |
| To | ``` var typeAbsoluteOrdinal: DescType { get } ``` |

Modified [typeAEList](https://developer.apple.com/documentation/coreservices/1542788-descriptor_type_constants/typeaelist)

|  | Declaration |
| --- | --- |
| From | ``` var typeAEList: Int { get } ``` |
| To | ``` var typeAEList: DescType { get } ``` |

Modified [typeAERecord](https://developer.apple.com/documentation/coreservices/1542788-descriptor_type_constants/typeaerecord)

|  | Declaration |
| --- | --- |
| From | ``` var typeAERecord: Int { get } ``` |
| To | ``` var typeAERecord: DescType { get } ``` |

Modified [typeAEText](https://developer.apple.com/documentation/coreservices/1556366-typeaetext/typeaetext)

|  | Declaration |
| --- | --- |
| From | ``` var typeAEText: Int { get } ``` |
| To | ``` var typeAEText: DescType { get } ``` |

Modified [typeAlias](https://developer.apple.com/documentation/coreservices/typealias)

|  | Declaration |
| --- | --- |
| From | ``` var typeAlias: Int { get } ``` |
| To | ``` var typeAlias: DescType { get } ``` |

Modified [typeAppleEvent](https://developer.apple.com/documentation/coreservices/1542788-descriptor_type_constants/typeappleevent)

|  | Declaration |
| --- | --- |
| From | ``` var typeAppleEvent: Int { get } ``` |
| To | ``` var typeAppleEvent: DescType { get } ``` |

Modified [typeApplicationBundleID](https://developer.apple.com/documentation/coreservices/1542896-typeapplicationbundleid/typeapplicationbundleid)

|  | Declaration |
| --- | --- |
| From | ``` var typeApplicationBundleID: Int { get } ``` |
| To | ``` var typeApplicationBundleID: DescType { get } ``` |

Modified [typeApplicationURL](https://developer.apple.com/documentation/coreservices/1542788-descriptor_type_constants/typeapplicationurl)

|  | Declaration |
| --- | --- |
| From | ``` var typeApplicationURL: Int { get } ``` |
| To | ``` var typeApplicationURL: DescType { get } ``` |

Modified [typeApplSignature](https://developer.apple.com/documentation/coreservices/typeapplsignature)

|  | Declaration |
| --- | --- |
| From | ``` var typeApplSignature: Int { get } ``` |
| To | ``` var typeApplSignature: DescType { get } ``` |

Modified [typeAppParameters](https://developer.apple.com/documentation/coreservices/1542788-descriptor_type_constants/typeappparameters)

|  | Declaration |
| --- | --- |
| From | ``` var typeAppParameters: Int { get } ``` |
| To | ``` var typeAppParameters: DescType { get } ``` |

Modified [typeArc](https://developer.apple.com/documentation/coreservices/1556366-typeaetext/typearc)

|  | Declaration |
| --- | --- |
| From | ``` var typeArc: Int { get } ``` |
| To | ``` var typeArc: DescType { get } ``` |

Modified [typeAuditToken](https://developer.apple.com/documentation/coreservices/1542844-anonymous/typeaudittoken)

|  | Declaration |
| --- | --- |
| From | ``` var typeAuditToken: Int { get } ``` |
| To | ``` var typeAuditToken: DescType { get } ``` |

Modified [typeBest](https://developer.apple.com/documentation/coreservices/typebest)

|  | Declaration |
| --- | --- |
| From | ``` var typeBest: Int { get } ``` |
| To | ``` var typeBest: DescType { get } ``` |

Modified [typeBookmarkData](https://developer.apple.com/documentation/coreservices/typebookmarkdata)

|  | Declaration |
| --- | --- |
| From | ``` var typeBookmarkData: Int { get } ``` |
| To | ``` var typeBookmarkData: DescType { get } ``` |

Modified [typeBoolean](https://developer.apple.com/documentation/coreservices/typeboolean)

|  | Declaration |
| --- | --- |
| From | ``` var typeBoolean: Int { get } ``` |
| To | ``` var typeBoolean: DescType { get } ``` |

Modified [typeCell](https://developer.apple.com/documentation/coreservices/typecell)

|  | Declaration |
| --- | --- |
| From | ``` var typeCell: Int { get } ``` |
| To | ``` var typeCell: DescType { get } ``` |

Modified [typeCentimeters](https://developer.apple.com/documentation/coreservices/typecentimeters)

|  | Declaration |
| --- | --- |
| From | ``` var typeCentimeters: Int { get } ``` |
| To | ``` var typeCentimeters: DescType { get } ``` |

Modified [typeCFAbsoluteTime](https://developer.apple.com/documentation/coreservices/typecfabsolutetime)

|  | Declaration |
| --- | --- |
| From | ``` var typeCFAbsoluteTime: Int { get } ``` |
| To | ``` var typeCFAbsoluteTime: DescType { get } ``` |

Modified [typeCFArrayRef](https://developer.apple.com/documentation/coreservices/typecfarrayref)

|  | Declaration |
| --- | --- |
| From | ``` var typeCFArrayRef: Int { get } ``` |
| To | ``` var typeCFArrayRef: DescType { get } ``` |

Modified [typeCFAttributedStringRef](https://developer.apple.com/documentation/coreservices/typecfattributedstringref)

|  | Declaration |
| --- | --- |
| From | ``` var typeCFAttributedStringRef: Int { get } ``` |
| To | ``` var typeCFAttributedStringRef: DescType { get } ``` |

Modified [typeCFBooleanRef](https://developer.apple.com/documentation/coreservices/1542940-anonymous/typecfbooleanref)

|  | Declaration |
| --- | --- |
| From | ``` var typeCFBooleanRef: Int { get } ``` |
| To | ``` var typeCFBooleanRef: DescType { get } ``` |

Modified [typeCFDictionaryRef](https://developer.apple.com/documentation/coreservices/1542940-anonymous/typecfdictionaryref)

|  | Declaration |
| --- | --- |
| From | ``` var typeCFDictionaryRef: Int { get } ``` |
| To | ``` var typeCFDictionaryRef: DescType { get } ``` |

Modified [typeCFMutableArrayRef](https://developer.apple.com/documentation/coreservices/typecfmutablearrayref)

|  | Declaration |
| --- | --- |
| From | ``` var typeCFMutableArrayRef: Int { get } ``` |
| To | ``` var typeCFMutableArrayRef: DescType { get } ``` |

Modified [typeCFMutableAttributedStringRef](https://developer.apple.com/documentation/coreservices/typecfmutableattributedstringref)

|  | Declaration |
| --- | --- |
| From | ``` var typeCFMutableAttributedStringRef: Int { get } ``` |
| To | ``` var typeCFMutableAttributedStringRef: DescType { get } ``` |

Modified [typeCFMutableDictionaryRef](https://developer.apple.com/documentation/coreservices/1542940-anonymous/typecfmutabledictionaryref)

|  | Declaration |
| --- | --- |
| From | ``` var typeCFMutableDictionaryRef: Int { get } ``` |
| To | ``` var typeCFMutableDictionaryRef: DescType { get } ``` |

Modified [typeCFMutableStringRef](https://developer.apple.com/documentation/coreservices/1542940-anonymous/typecfmutablestringref)

|  | Declaration |
| --- | --- |
| From | ``` var typeCFMutableStringRef: Int { get } ``` |
| To | ``` var typeCFMutableStringRef: DescType { get } ``` |

Modified [typeCFNumberRef](https://developer.apple.com/documentation/coreservices/1542940-anonymous/typecfnumberref)

|  | Declaration |
| --- | --- |
| From | ``` var typeCFNumberRef: Int { get } ``` |
| To | ``` var typeCFNumberRef: DescType { get } ``` |

Modified [typeCFStringRef](https://developer.apple.com/documentation/coreservices/typecfstringref)

|  | Declaration |
| --- | --- |
| From | ``` var typeCFStringRef: Int { get } ``` |
| To | ``` var typeCFStringRef: DescType { get } ``` |

Modified [typeCFTypeRef](https://developer.apple.com/documentation/coreservices/1542940-anonymous/typecftyperef)

|  | Declaration |
| --- | --- |
| From | ``` var typeCFTypeRef: Int { get } ``` |
| To | ``` var typeCFTypeRef: DescType { get } ``` |

Modified [typeChar](https://developer.apple.com/documentation/coreservices/typechar)

|  | Declaration |
| --- | --- |
| From | ``` var typeChar: Int { get } ``` |
| To | ``` var typeChar: DescType { get } ``` |

Modified [typeClassInfo](https://developer.apple.com/documentation/coreservices/1556366-typeaetext/typeclassinfo)

|  | Declaration |
| --- | --- |
| From | ``` var typeClassInfo: Int { get } ``` |
| To | ``` var typeClassInfo: DescType { get } ``` |

Modified [typeColorTable](https://developer.apple.com/documentation/coreservices/typecolortable)

|  | Declaration |
| --- | --- |
| From | ``` var typeColorTable: Int { get } ``` |
| To | ``` var typeColorTable: DescType { get } ``` |

Modified [typeColumn](https://developer.apple.com/documentation/coreservices/1556366-typeaetext/typecolumn)

|  | Declaration |
| --- | --- |
| From | ``` var typeColumn: Int { get } ``` |
| To | ``` var typeColumn: DescType { get } ``` |

Modified [typeCompDescriptor](https://developer.apple.com/documentation/coreservices/1645753-anonymous/typecompdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` var typeCompDescriptor: Int { get } ``` |
| To | ``` var typeCompDescriptor: DescType { get } ``` |

Modified [typeComponentInstance](https://developer.apple.com/documentation/coreservices/typecomponentinstance)

|  | Declaration |
| --- | --- |
| From | ``` var typeComponentInstance: Int { get } ``` |
| To | ``` var typeComponentInstance: OSType { get } ``` |

Modified [typeCString](https://developer.apple.com/documentation/coreservices/typecstring)

|  | Declaration |
| --- | --- |
| From | ``` var typeCString: Int { get } ``` |
| To | ``` var typeCString: DescType { get } ``` |

Modified [typeCubicCentimeter](https://developer.apple.com/documentation/coreservices/1556382-typemeters/typecubiccentimeter)

|  | Declaration |
| --- | --- |
| From | ``` var typeCubicCentimeter: Int { get } ``` |
| To | ``` var typeCubicCentimeter: DescType { get } ``` |

Modified [typeCubicFeet](https://developer.apple.com/documentation/coreservices/1556382-typemeters/typecubicfeet)

|  | Declaration |
| --- | --- |
| From | ``` var typeCubicFeet: Int { get } ``` |
| To | ``` var typeCubicFeet: DescType { get } ``` |

Modified [typeCubicInches](https://developer.apple.com/documentation/coreservices/1556382-typemeters/typecubicinches)

|  | Declaration |
| --- | --- |
| From | ``` var typeCubicInches: Int { get } ``` |
| To | ``` var typeCubicInches: DescType { get } ``` |

Modified [typeCubicMeters](https://developer.apple.com/documentation/coreservices/1556382-typemeters/typecubicmeters)

|  | Declaration |
| --- | --- |
| From | ``` var typeCubicMeters: Int { get } ``` |
| To | ``` var typeCubicMeters: DescType { get } ``` |

Modified [typeCubicYards](https://developer.apple.com/documentation/coreservices/1556382-typemeters/typecubicyards)

|  | Declaration |
| --- | --- |
| From | ``` var typeCubicYards: Int { get } ``` |
| To | ``` var typeCubicYards: DescType { get } ``` |

Modified [typeCurrentContainer](https://developer.apple.com/documentation/coreservices/1645753-anonymous/typecurrentcontainer)

|  | Declaration |
| --- | --- |
| From | ``` var typeCurrentContainer: Int { get } ``` |
| To | ``` var typeCurrentContainer: DescType { get } ``` |

Modified [typeDashStyle](https://developer.apple.com/documentation/coreservices/1556366-typeaetext/typedashstyle)

|  | Declaration |
| --- | --- |
| From | ``` var typeDashStyle: Int { get } ``` |
| To | ``` var typeDashStyle: DescType { get } ``` |

Modified [typeData](https://developer.apple.com/documentation/coreservices/1556366-typeaetext/typedata)

|  | Declaration |
| --- | --- |
| From | ``` var typeData: Int { get } ``` |
| To | ``` var typeData: DescType { get } ``` |

Modified [typeDecimalStruct](https://developer.apple.com/documentation/coreservices/typedecimalstruct)

|  | Declaration |
| --- | --- |
| From | ``` var typeDecimalStruct: Int { get } ``` |
| To | ``` var typeDecimalStruct: DescType { get } ``` |

Modified [typeDegreesC](https://developer.apple.com/documentation/coreservices/typedegreesc)

|  | Declaration |
| --- | --- |
| From | ``` var typeDegreesC: Int { get } ``` |
| To | ``` var typeDegreesC: DescType { get } ``` |

Modified [typeDegreesF](https://developer.apple.com/documentation/coreservices/1556382-typemeters/typedegreesf)

|  | Declaration |
| --- | --- |
| From | ``` var typeDegreesF: Int { get } ``` |
| To | ``` var typeDegreesF: DescType { get } ``` |

Modified [typeDegreesK](https://developer.apple.com/documentation/coreservices/typedegreesk)

|  | Declaration |
| --- | --- |
| From | ``` var typeDegreesK: Int { get } ``` |
| To | ``` var typeDegreesK: DescType { get } ``` |

Modified [typeDrawingArea](https://developer.apple.com/documentation/coreservices/typedrawingarea)

|  | Declaration |
| --- | --- |
| From | ``` var typeDrawingArea: Int { get } ``` |
| To | ``` var typeDrawingArea: DescType { get } ``` |

Modified [typeElemInfo](https://developer.apple.com/documentation/coreservices/typeeleminfo)

|  | Declaration |
| --- | --- |
| From | ``` var typeElemInfo: Int { get } ``` |
| To | ``` var typeElemInfo: DescType { get } ``` |

Modified [typeEncodedString](https://developer.apple.com/documentation/coreservices/typeencodedstring)

|  | Declaration |
| --- | --- |
| From | ``` var typeEncodedString: Int { get } ``` |
| To | ``` var typeEncodedString: DescType { get } ``` |

Modified [typeEnumerated](https://developer.apple.com/documentation/coreservices/1542788-descriptor_type_constants/typeenumerated)

|  | Declaration |
| --- | --- |
| From | ``` var typeEnumerated: Int { get } ``` |
| To | ``` var typeEnumerated: DescType { get } ``` |

Modified [typeEnumeration](https://developer.apple.com/documentation/coreservices/1556366-typeaetext/typeenumeration)

|  | Declaration |
| --- | --- |
| From | ``` var typeEnumeration: Int { get } ``` |
| To | ``` var typeEnumeration: DescType { get } ``` |

Modified [typeEPS](https://developer.apple.com/documentation/coreservices/1556366-typeaetext/typeeps)

|  | Declaration |
| --- | --- |
| From | ``` var typeEPS: Int { get } ``` |
| To | ``` var typeEPS: DescType { get } ``` |

Modified [typeEventInfo](https://developer.apple.com/documentation/coreservices/1556366-typeaetext/typeeventinfo)

|  | Declaration |
| --- | --- |
| From | ``` var typeEventInfo: Int { get } ``` |
| To | ``` var typeEventInfo: DescType { get } ``` |

Modified [typeEventRecord](https://developer.apple.com/documentation/coreservices/1542788-descriptor_type_constants/typeeventrecord)

|  | Declaration |
| --- | --- |
| From | ``` var typeEventRecord: Int { get } ``` |
| To | ``` var typeEventRecord: DescType { get } ``` |

Modified [typeEventRef](https://developer.apple.com/documentation/coreservices/1556406-ktextserviceclass/typeeventref)

|  | Declaration |
| --- | --- |
| From | ``` var typeEventRef: Int { get } ``` |
| To | ``` var typeEventRef: OSType { get } ``` |

Modified [typeFalse](https://developer.apple.com/documentation/coreservices/typefalse)

|  | Declaration |
| --- | --- |
| From | ``` var typeFalse: Int { get } ``` |
| To | ``` var typeFalse: DescType { get } ``` |

Modified [typeFeet](https://developer.apple.com/documentation/coreservices/1556382-typemeters/typefeet)

|  | Declaration |
| --- | --- |
| From | ``` var typeFeet: Int { get } ``` |
| To | ``` var typeFeet: DescType { get } ``` |

Modified [typeFileURL](https://developer.apple.com/documentation/coreservices/typefileurl)

|  | Declaration |
| --- | --- |
| From | ``` var typeFileURL: Int { get } ``` |
| To | ``` var typeFileURL: DescType { get } ``` |

Modified [typeFinderWindow](https://developer.apple.com/documentation/coreservices/typefinderwindow)

|  | Declaration |
| --- | --- |
| From | ``` var typeFinderWindow: Int { get } ``` |
| To | ``` var typeFinderWindow: DescType { get } ``` |

Modified [typeFixed](https://developer.apple.com/documentation/coreservices/1542788-descriptor_type_constants/typefixed)

|  | Declaration |
| --- | --- |
| From | ``` var typeFixed: Int { get } ``` |
| To | ``` var typeFixed: DescType { get } ``` |

Modified [typeFixedPoint](https://developer.apple.com/documentation/coreservices/typefixedpoint)

|  | Declaration |
| --- | --- |
| From | ``` var typeFixedPoint: Int { get } ``` |
| To | ``` var typeFixedPoint: DescType { get } ``` |

Modified [typeFixedRectangle](https://developer.apple.com/documentation/coreservices/1556401-anonymous/typefixedrectangle)

|  | Declaration |
| --- | --- |
| From | ``` var typeFixedRectangle: Int { get } ``` |
| To | ``` var typeFixedRectangle: DescType { get } ``` |

Modified [typeFSRef](https://developer.apple.com/documentation/coreservices/1542788-descriptor_type_constants/typefsref)

|  | Declaration |
| --- | --- |
| From | ``` var typeFSRef: Int { get } ``` |
| To | ``` var typeFSRef: DescType { get } ``` |

Modified [typeGallons](https://developer.apple.com/documentation/coreservices/typegallons)

|  | Declaration |
| --- | --- |
| From | ``` var typeGallons: Int { get } ``` |
| To | ``` var typeGallons: DescType { get } ``` |

Modified [typeGIF](https://developer.apple.com/documentation/coreservices/typegif)

|  | Declaration |
| --- | --- |
| From | ``` var typeGIF: Int { get } ``` |
| To | ``` var typeGIF: DescType { get } ``` |

Modified [typeGlyphInfoArray](https://developer.apple.com/documentation/coreservices/typeglyphinfoarray)

|  | Declaration |
| --- | --- |
| From | ``` var typeGlyphInfoArray: Int { get } ``` |
| To | ``` var typeGlyphInfoArray: OSType { get } ``` |

Modified [typeGrams](https://developer.apple.com/documentation/coreservices/typegrams)

|  | Declaration |
| --- | --- |
| From | ``` var typeGrams: Int { get } ``` |
| To | ``` var typeGrams: DescType { get } ``` |

Modified [typeGraphicLine](https://developer.apple.com/documentation/coreservices/1556401-anonymous/typegraphicline)

|  | Declaration |
| --- | --- |
| From | ``` var typeGraphicLine: Int { get } ``` |
| To | ``` var typeGraphicLine: DescType { get } ``` |

Modified [typeGraphicText](https://developer.apple.com/documentation/coreservices/1556401-anonymous/typegraphictext)

|  | Declaration |
| --- | --- |
| From | ``` var typeGraphicText: Int { get } ``` |
| To | ``` var typeGraphicText: DescType { get } ``` |

Modified [typeGroupedGraphic](https://developer.apple.com/documentation/coreservices/1556401-anonymous/typegroupedgraphic)

|  | Declaration |
| --- | --- |
| From | ``` var typeGroupedGraphic: Int { get } ``` |
| To | ``` var typeGroupedGraphic: DescType { get } ``` |

Modified [typeHIMenu](https://developer.apple.com/documentation/coreservices/typehimenu)

|  | Declaration |
| --- | --- |
| From | ``` var typeHIMenu: Int { get } ``` |
| To | ``` var typeHIMenu: DescType { get } ``` |

Modified [typeHIWindow](https://developer.apple.com/documentation/coreservices/typehiwindow)

|  | Declaration |
| --- | --- |
| From | ``` var typeHIWindow: Int { get } ``` |
| To | ``` var typeHIWindow: DescType { get } ``` |

Modified [typeIEEE32BitFloatingPoint](https://developer.apple.com/documentation/coreservices/1542872-numeric_descriptor_type_constant/typeieee32bitfloatingpoint)

|  | Declaration |
| --- | --- |
| From | ``` var typeIEEE32BitFloatingPoint: Int { get } ``` |
| To | ``` var typeIEEE32BitFloatingPoint: DescType { get } ``` |

Modified [typeIEEE64BitFloatingPoint](https://developer.apple.com/documentation/coreservices/typeieee64bitfloatingpoint)

|  | Declaration |
| --- | --- |
| From | ``` var typeIEEE64BitFloatingPoint: Int { get } ``` |
| To | ``` var typeIEEE64BitFloatingPoint: DescType { get } ``` |

Modified [typeInches](https://developer.apple.com/documentation/coreservices/typeinches)

|  | Declaration |
| --- | --- |
| From | ``` var typeInches: Int { get } ``` |
| To | ``` var typeInches: DescType { get } ``` |

Modified [typeIndexDescriptor](https://developer.apple.com/documentation/coreservices/1645753-anonymous/typeindexdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` var typeIndexDescriptor: Int { get } ``` |
| To | ``` var typeIndexDescriptor: DescType { get } ``` |

Modified [typeInsertionLoc](https://developer.apple.com/documentation/coreservices/1556401-anonymous/typeinsertionloc)

|  | Declaration |
| --- | --- |
| From | ``` var typeInsertionLoc: Int { get } ``` |
| To | ``` var typeInsertionLoc: DescType { get } ``` |

Modified [typeIntlText](https://developer.apple.com/documentation/coreservices/1556401-anonymous/typeintltext)

|  | Declaration |
| --- | --- |
| From | ``` var typeIntlText: Int { get } ``` |
| To | ``` var typeIntlText: DescType { get } ``` |

Modified [typeIntlWritingCode](https://developer.apple.com/documentation/coreservices/typeintlwritingcode)

|  | Declaration |
| --- | --- |
| From | ``` var typeIntlWritingCode: Int { get } ``` |
| To | ``` var typeIntlWritingCode: DescType { get } ``` |

Modified [typeISO8601DateTime](https://developer.apple.com/documentation/coreservices/typeiso8601datetime)

|  | Declaration |
| --- | --- |
| From | ``` var typeISO8601DateTime: Int { get } ``` |
| To | ``` var typeISO8601DateTime: DescType { get } ``` |

Modified [typeJPEG](https://developer.apple.com/documentation/coreservices/1556405-typetiff/typejpeg)

|  | Declaration |
| --- | --- |
| From | ``` var typeJPEG: Int { get } ``` |
| To | ``` var typeJPEG: DescType { get } ``` |

Modified [typeKernelProcessID](https://developer.apple.com/documentation/coreservices/1542936-typekernelprocessid/typekernelprocessid)

|  | Declaration |
| --- | --- |
| From | ``` var typeKernelProcessID: Int { get } ``` |
| To | ``` var typeKernelProcessID: DescType { get } ``` |

Modified [typeKeyword](https://developer.apple.com/documentation/coreservices/typekeyword)

|  | Declaration |
| --- | --- |
| From | ``` var typeKeyword: Int { get } ``` |
| To | ``` var typeKeyword: DescType { get } ``` |

Modified [typeKilograms](https://developer.apple.com/documentation/coreservices/typekilograms)

|  | Declaration |
| --- | --- |
| From | ``` var typeKilograms: Int { get } ``` |
| To | ``` var typeKilograms: DescType { get } ``` |

Modified [typeKilometers](https://developer.apple.com/documentation/coreservices/1556382-typemeters/typekilometers)

|  | Declaration |
| --- | --- |
| From | ``` var typeKilometers: Int { get } ``` |
| To | ``` var typeKilometers: DescType { get } ``` |

Modified [typeLiters](https://developer.apple.com/documentation/coreservices/1556382-typemeters/typeliters)

|  | Declaration |
| --- | --- |
| From | ``` var typeLiters: Int { get } ``` |
| To | ``` var typeLiters: DescType { get } ``` |

Modified [typeLogicalDescriptor](https://developer.apple.com/documentation/coreservices/typelogicaldescriptor)

|  | Declaration |
| --- | --- |
| From | ``` var typeLogicalDescriptor: Int { get } ``` |
| To | ``` var typeLogicalDescriptor: DescType { get } ``` |

Modified [typeLongDateTime](https://developer.apple.com/documentation/coreservices/typelongdatetime)

|  | Declaration |
| --- | --- |
| From | ``` var typeLongDateTime: Int { get } ``` |
| To | ``` var typeLongDateTime: DescType { get } ``` |

Modified [typeLongFixed](https://developer.apple.com/documentation/coreservices/typelongfixed)

|  | Declaration |
| --- | --- |
| From | ``` var typeLongFixed: Int { get } ``` |
| To | ``` var typeLongFixed: DescType { get } ``` |

Modified [typeLongFixedPoint](https://developer.apple.com/documentation/coreservices/1556401-anonymous/typelongfixedpoint)

|  | Declaration |
| --- | --- |
| From | ``` var typeLongFixedPoint: Int { get } ``` |
| To | ``` var typeLongFixedPoint: DescType { get } ``` |

Modified [typeLongFixedRectangle](https://developer.apple.com/documentation/coreservices/1556401-anonymous/typelongfixedrectangle)

|  | Declaration |
| --- | --- |
| From | ``` var typeLongFixedRectangle: Int { get } ``` |
| To | ``` var typeLongFixedRectangle: DescType { get } ``` |

Modified [typeLongPoint](https://developer.apple.com/documentation/coreservices/typelongpoint)

|  | Declaration |
| --- | --- |
| From | ``` var typeLongPoint: Int { get } ``` |
| To | ``` var typeLongPoint: DescType { get } ``` |

Modified [typeLongRectangle](https://developer.apple.com/documentation/coreservices/1556401-anonymous/typelongrectangle)

|  | Declaration |
| --- | --- |
| From | ``` var typeLongRectangle: Int { get } ``` |
| To | ``` var typeLongRectangle: DescType { get } ``` |

Modified [typeLowLevelEventRecord](https://developer.apple.com/documentation/coreservices/typelowleveleventrecord)

|  | Declaration |
| --- | --- |
| From | ``` var typeLowLevelEventRecord: Int { get } ``` |
| To | ``` var typeLowLevelEventRecord: OSType { get } ``` |

Modified [typeMachineLoc](https://developer.apple.com/documentation/coreservices/1556401-anonymous/typemachineloc)

|  | Declaration |
| --- | --- |
| From | ``` var typeMachineLoc: Int { get } ``` |
| To | ``` var typeMachineLoc: DescType { get } ``` |

Modified [typeMachPort](https://developer.apple.com/documentation/coreservices/1542936-typekernelprocessid/typemachport)

|  | Declaration |
| --- | --- |
| From | ``` var typeMachPort: Int { get } ``` |
| To | ``` var typeMachPort: DescType { get } ``` |

Modified [typeMeters](https://developer.apple.com/documentation/coreservices/typemeters)

|  | Declaration |
| --- | --- |
| From | ``` var typeMeters: Int { get } ``` |
| To | ``` var typeMeters: DescType { get } ``` |

Modified [typeMiles](https://developer.apple.com/documentation/coreservices/1556382-typemeters/typemiles)

|  | Declaration |
| --- | --- |
| From | ``` var typeMiles: Int { get } ``` |
| To | ``` var typeMiles: DescType { get } ``` |

Modified [typeNull](https://developer.apple.com/documentation/coreservices/1542788-descriptor_type_constants/typenull)

|  | Declaration |
| --- | --- |
| From | ``` var typeNull: Int { get } ``` |
| To | ``` var typeNull: DescType { get } ``` |

Modified [typeObjectBeingExamined](https://developer.apple.com/documentation/coreservices/1645753-anonymous/typeobjectbeingexamined)

|  | Declaration |
| --- | --- |
| From | ``` var typeObjectBeingExamined: Int { get } ``` |
| To | ``` var typeObjectBeingExamined: DescType { get } ``` |

Modified [typeObjectSpecifier](https://developer.apple.com/documentation/coreservices/typeobjectspecifier)

|  | Declaration |
| --- | --- |
| From | ``` var typeObjectSpecifier: Int { get } ``` |
| To | ``` var typeObjectSpecifier: DescType { get } ``` |

Modified [typeOffsetArray](https://developer.apple.com/documentation/coreservices/1556406-ktextserviceclass/typeoffsetarray)

|  | Declaration |
| --- | --- |
| From | ``` var typeOffsetArray: Int { get } ``` |
| To | ``` var typeOffsetArray: OSType { get } ``` |

Modified [typeOSLTokenList](https://developer.apple.com/documentation/coreservices/typeosltokenlist)

|  | Declaration |
| --- | --- |
| From | ``` var typeOSLTokenList: Int { get } ``` |
| To | ``` var typeOSLTokenList: DescType { get } ``` |

Modified [typeOunces](https://developer.apple.com/documentation/coreservices/typeounces)

|  | Declaration |
| --- | --- |
| From | ``` var typeOunces: Int { get } ``` |
| To | ``` var typeOunces: DescType { get } ``` |

Modified [typeOval](https://developer.apple.com/documentation/coreservices/typeoval)

|  | Declaration |
| --- | --- |
| From | ``` var typeOval: Int { get } ``` |
| To | ``` var typeOval: DescType { get } ``` |

Modified [typeParamInfo](https://developer.apple.com/documentation/coreservices/typeparaminfo)

|  | Declaration |
| --- | --- |
| From | ``` var typeParamInfo: Int { get } ``` |
| To | ``` var typeParamInfo: DescType { get } ``` |

Modified [typePict](https://developer.apple.com/documentation/coreservices/typepict)

|  | Declaration |
| --- | --- |
| From | ``` var typePict: Int { get } ``` |
| To | ``` var typePict: DescType { get } ``` |

Modified [typePixelMap](https://developer.apple.com/documentation/coreservices/1556396-anonymous/typepixelmap)

|  | Declaration |
| --- | --- |
| From | ``` var typePixelMap: Int { get } ``` |
| To | ``` var typePixelMap: DescType { get } ``` |

Modified [typePixMapMinus](https://developer.apple.com/documentation/coreservices/typepixmapminus)

|  | Declaration |
| --- | --- |
| From | ``` var typePixMapMinus: Int { get } ``` |
| To | ``` var typePixMapMinus: DescType { get } ``` |

Modified [typePolygon](https://developer.apple.com/documentation/coreservices/1556396-anonymous/typepolygon)

|  | Declaration |
| --- | --- |
| From | ``` var typePolygon: Int { get } ``` |
| To | ``` var typePolygon: DescType { get } ``` |

Modified [typePounds](https://developer.apple.com/documentation/coreservices/1556382-typemeters/typepounds)

|  | Declaration |
| --- | --- |
| From | ``` var typePounds: Int { get } ``` |
| To | ``` var typePounds: DescType { get } ``` |

Modified [typeProcessSerialNumber](https://developer.apple.com/documentation/coreservices/typeprocessserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` var typeProcessSerialNumber: Int { get } ``` |
| To | ``` var typeProcessSerialNumber: DescType { get } ``` |

Modified [typeProperty](https://developer.apple.com/documentation/coreservices/typeproperty)

|  | Declaration |
| --- | --- |
| From | ``` var typeProperty: Int { get } ``` |
| To | ``` var typeProperty: DescType { get } ``` |

Modified [typePropInfo](https://developer.apple.com/documentation/coreservices/typepropinfo)

|  | Declaration |
| --- | --- |
| From | ``` var typePropInfo: Int { get } ``` |
| To | ``` var typePropInfo: DescType { get } ``` |

Modified [typePString](https://developer.apple.com/documentation/coreservices/typepstring)

|  | Declaration |
| --- | --- |
| From | ``` var typePString: Int { get } ``` |
| To | ``` var typePString: DescType { get } ``` |

Modified [typePtr](https://developer.apple.com/documentation/coreservices/1556396-anonymous/typeptr)

|  | Declaration |
| --- | --- |
| From | ``` var typePtr: Int { get } ``` |
| To | ``` var typePtr: DescType { get } ``` |

Modified [typeQDPoint](https://developer.apple.com/documentation/coreservices/1556396-anonymous/typeqdpoint)

|  | Declaration |
| --- | --- |
| From | ``` var typeQDPoint: Int { get } ``` |
| To | ``` var typeQDPoint: DescType { get } ``` |

Modified [typeQDRectangle](https://developer.apple.com/documentation/coreservices/1542788-descriptor_type_constants/typeqdrectangle)

|  | Declaration |
| --- | --- |
| From | ``` var typeQDRectangle: Int { get } ``` |
| To | ``` var typeQDRectangle: DescType { get } ``` |

Modified [typeQDRegion](https://developer.apple.com/documentation/coreservices/typeqdregion)

|  | Declaration |
| --- | --- |
| From | ``` var typeQDRegion: Int { get } ``` |
| To | ``` var typeQDRegion: DescType { get } ``` |

Modified [typeQuarts](https://developer.apple.com/documentation/coreservices/1556382-typemeters/typequarts)

|  | Declaration |
| --- | --- |
| From | ``` var typeQuarts: Int { get } ``` |
| To | ``` var typeQuarts: DescType { get } ``` |

Modified [typeRangeDescriptor](https://developer.apple.com/documentation/coreservices/typerangedescriptor)

|  | Declaration |
| --- | --- |
| From | ``` var typeRangeDescriptor: Int { get } ``` |
| To | ``` var typeRangeDescriptor: DescType { get } ``` |

Modified [typeRectangle](https://developer.apple.com/documentation/coreservices/typerectangle)

|  | Declaration |
| --- | --- |
| From | ``` var typeRectangle: Int { get } ``` |
| To | ``` var typeRectangle: DescType { get } ``` |

Modified [typeRelativeDescriptor](https://developer.apple.com/documentation/coreservices/1645753-anonymous/typerelativedescriptor)

|  | Declaration |
| --- | --- |
| From | ``` var typeRelativeDescriptor: Int { get } ``` |
| To | ``` var typeRelativeDescriptor: DescType { get } ``` |

Modified [typeReplyPortAttr](https://developer.apple.com/documentation/coreservices/typereplyportattr)

|  | Declaration |
| --- | --- |
| From | ``` var typeReplyPortAttr: Int { get } ``` |
| To | ``` var typeReplyPortAttr: DescType { get } ``` |

Modified [typeRGB16](https://developer.apple.com/documentation/coreservices/1556396-anonymous/typergb16)

|  | Declaration |
| --- | --- |
| From | ``` var typeRGB16: Int { get } ``` |
| To | ``` var typeRGB16: DescType { get } ``` |

Modified [typeRGB96](https://developer.apple.com/documentation/coreservices/1556396-anonymous/typergb96)

|  | Declaration |
| --- | --- |
| From | ``` var typeRGB96: Int { get } ``` |
| To | ``` var typeRGB96: DescType { get } ``` |

Modified [typeRGBColor](https://developer.apple.com/documentation/coreservices/typergbcolor)

|  | Declaration |
| --- | --- |
| From | ``` var typeRGBColor: Int { get } ``` |
| To | ``` var typeRGBColor: DescType { get } ``` |

Modified [typeRotation](https://developer.apple.com/documentation/coreservices/1556396-anonymous/typerotation)

|  | Declaration |
| --- | --- |
| From | ``` var typeRotation: Int { get } ``` |
| To | ``` var typeRotation: DescType { get } ``` |

Modified [typeRoundedRectangle](https://developer.apple.com/documentation/coreservices/1556396-anonymous/typeroundedrectangle)

|  | Declaration |
| --- | --- |
| From | ``` var typeRoundedRectangle: Int { get } ``` |
| To | ``` var typeRoundedRectangle: DescType { get } ``` |

Modified [typeRow](https://developer.apple.com/documentation/coreservices/typerow)

|  | Declaration |
| --- | --- |
| From | ``` var typeRow: Int { get } ``` |
| To | ``` var typeRow: DescType { get } ``` |

Modified [typeScrapStyles](https://developer.apple.com/documentation/coreservices/1556396-anonymous/typescrapstyles)

|  | Declaration |
| --- | --- |
| From | ``` var typeScrapStyles: Int { get } ``` |
| To | ``` var typeScrapStyles: DescType { get } ``` |

Modified [typeScript](https://developer.apple.com/documentation/coreservices/typescript)

|  | Declaration |
| --- | --- |
| From | ``` var typeScript: Int { get } ``` |
| To | ``` var typeScript: DescType { get } ``` |

Modified [typeSectionH](https://developer.apple.com/documentation/coreservices/1542788-descriptor_type_constants/typesectionh)

|  | Declaration |
| --- | --- |
| From | ``` var typeSectionH: Int { get } ``` |
| To | ``` var typeSectionH: DescType { get } ``` |

Modified [typeSInt16](https://developer.apple.com/documentation/coreservices/1542872-numeric_descriptor_type_constant/typesint16)

|  | Declaration |
| --- | --- |
| From | ``` var typeSInt16: Int { get } ``` |
| To | ``` var typeSInt16: DescType { get } ``` |

Modified [typeSInt32](https://developer.apple.com/documentation/coreservices/typesint32)

|  | Declaration |
| --- | --- |
| From | ``` var typeSInt32: Int { get } ``` |
| To | ``` var typeSInt32: DescType { get } ``` |

Modified [typeSInt64](https://developer.apple.com/documentation/coreservices/typesint64)

|  | Declaration |
| --- | --- |
| From | ``` var typeSInt64: Int { get } ``` |
| To | ``` var typeSInt64: DescType { get } ``` |

Modified [typeSquareFeet](https://developer.apple.com/documentation/coreservices/1556382-typemeters/typesquarefeet)

|  | Declaration |
| --- | --- |
| From | ``` var typeSquareFeet: Int { get } ``` |
| To | ``` var typeSquareFeet: DescType { get } ``` |

Modified [typeSquareKilometers](https://developer.apple.com/documentation/coreservices/typesquarekilometers)

|  | Declaration |
| --- | --- |
| From | ``` var typeSquareKilometers: Int { get } ``` |
| To | ``` var typeSquareKilometers: DescType { get } ``` |

Modified [typeSquareMeters](https://developer.apple.com/documentation/coreservices/1556382-typemeters/typesquaremeters)

|  | Declaration |
| --- | --- |
| From | ``` var typeSquareMeters: Int { get } ``` |
| To | ``` var typeSquareMeters: DescType { get } ``` |

Modified [typeSquareMiles](https://developer.apple.com/documentation/coreservices/typesquaremiles)

|  | Declaration |
| --- | --- |
| From | ``` var typeSquareMiles: Int { get } ``` |
| To | ``` var typeSquareMiles: DescType { get } ``` |

Modified [typeSquareYards](https://developer.apple.com/documentation/coreservices/1556382-typemeters/typesquareyards)

|  | Declaration |
| --- | --- |
| From | ``` var typeSquareYards: Int { get } ``` |
| To | ``` var typeSquareYards: DescType { get } ``` |

Modified [typeStyledText](https://developer.apple.com/documentation/coreservices/typestyledtext)

|  | Declaration |
| --- | --- |
| From | ``` var typeStyledText: Int { get } ``` |
| To | ``` var typeStyledText: DescType { get } ``` |

Modified [typeStyledUnicodeText](https://developer.apple.com/documentation/coreservices/1542749-anonymous/typestyledunicodetext)

|  | Declaration |
| --- | --- |
| From | ``` var typeStyledUnicodeText: Int { get } ``` |
| To | ``` var typeStyledUnicodeText: DescType { get } ``` |

Modified [typeSuiteInfo](https://developer.apple.com/documentation/coreservices/1556396-anonymous/typesuiteinfo)

|  | Declaration |
| --- | --- |
| From | ``` var typeSuiteInfo: Int { get } ``` |
| To | ``` var typeSuiteInfo: DescType { get } ``` |

Modified [typeTable](https://developer.apple.com/documentation/coreservices/1556396-anonymous/typetable)

|  | Declaration |
| --- | --- |
| From | ``` var typeTable: Int { get } ``` |
| To | ``` var typeTable: DescType { get } ``` |

Modified [typeText](https://developer.apple.com/documentation/coreservices/1556406-ktextserviceclass/typetext)

|  | Declaration |
| --- | --- |
| From | ``` var typeText: Int { get } ``` |
| To | ``` var typeText: OSType { get } ``` |

Modified [typeTextRange](https://developer.apple.com/documentation/coreservices/typetextrange)

|  | Declaration |
| --- | --- |
| From | ``` var typeTextRange: Int { get } ``` |
| To | ``` var typeTextRange: OSType { get } ``` |

Modified [typeTextRangeArray](https://developer.apple.com/documentation/coreservices/1556406-ktextserviceclass/typetextrangearray)

|  | Declaration |
| --- | --- |
| From | ``` var typeTextRangeArray: Int { get } ``` |
| To | ``` var typeTextRangeArray: OSType { get } ``` |

Modified [typeTextStyles](https://developer.apple.com/documentation/coreservices/1556396-anonymous/typetextstyles)

|  | Declaration |
| --- | --- |
| From | ``` var typeTextStyles: Int { get } ``` |
| To | ``` var typeTextStyles: DescType { get } ``` |

Modified [typeTIFF](https://developer.apple.com/documentation/coreservices/1556405-typetiff/typetiff)

|  | Declaration |
| --- | --- |
| From | ``` var typeTIFF: Int { get } ``` |
| To | ``` var typeTIFF: DescType { get } ``` |

Modified [typeToken](https://developer.apple.com/documentation/coreservices/typetoken)

|  | Declaration |
| --- | --- |
| From | ``` var typeToken: Int { get } ``` |
| To | ``` var typeToken: DescType { get } ``` |

Modified [typeTrue](https://developer.apple.com/documentation/coreservices/1542788-descriptor_type_constants/typetrue)

|  | Declaration |
| --- | --- |
| From | ``` var typeTrue: Int { get } ``` |
| To | ``` var typeTrue: DescType { get } ``` |

Modified [typeType](https://developer.apple.com/documentation/coreservices/1542788-descriptor_type_constants/typetype)

|  | Declaration |
| --- | --- |
| From | ``` var typeType: Int { get } ``` |
| To | ``` var typeType: DescType { get } ``` |

Modified [typeUInt16](https://developer.apple.com/documentation/coreservices/typeuint16)

|  | Declaration |
| --- | --- |
| From | ``` var typeUInt16: Int { get } ``` |
| To | ``` var typeUInt16: DescType { get } ``` |

Modified [typeUInt32](https://developer.apple.com/documentation/coreservices/typeuint32)

|  | Declaration |
| --- | --- |
| From | ``` var typeUInt32: Int { get } ``` |
| To | ``` var typeUInt32: DescType { get } ``` |

Modified [typeUInt64](https://developer.apple.com/documentation/coreservices/typeuint64)

|  | Declaration |
| --- | --- |
| From | ``` var typeUInt64: Int { get } ``` |
| To | ``` var typeUInt64: DescType { get } ``` |

Modified [typeUnicodeText](https://developer.apple.com/documentation/coreservices/1542749-anonymous/typeunicodetext)

|  | Declaration |
| --- | --- |
| From | ``` var typeUnicodeText: Int { get } ``` |
| To | ``` var typeUnicodeText: DescType { get } ``` |

Modified [typeUTF16ExternalRepresentation](https://developer.apple.com/documentation/coreservices/1542918-typeunicodetext/typeutf16externalrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` var typeUTF16ExternalRepresentation: Int { get } ``` |
| To | ``` var typeUTF16ExternalRepresentation: DescType { get } ``` |

Modified [typeUTF8Text](https://developer.apple.com/documentation/coreservices/1542918-typeunicodetext/typeutf8text)

|  | Declaration |
| --- | --- |
| From | ``` var typeUTF8Text: Int { get } ``` |
| To | ``` var typeUTF8Text: DescType { get } ``` |

Modified [typeVersion](https://developer.apple.com/documentation/coreservices/typeversion)

|  | Declaration |
| --- | --- |
| From | ``` var typeVersion: Int { get } ``` |
| To | ``` var typeVersion: DescType { get } ``` |

Modified [typeWildCard](https://developer.apple.com/documentation/coreservices/1542788-descriptor_type_constants/typewildcard)

|  | Declaration |
| --- | --- |
| From | ``` var typeWildCard: Int { get } ``` |
| To | ``` var typeWildCard: DescType { get } ``` |

Modified [typeYards](https://developer.apple.com/documentation/coreservices/typeyards)

|  | Declaration |
| --- | --- |
| From | ``` var typeYards: Int { get } ``` |
| To | ``` var typeYards: DescType { get } ``` |

Modified [UCCompareCollationKeys(_: UnsafePointer<UCCollationValue>!, _: Int, _: UnsafePointer<UCCollationValue>!, _: Int, _: UnsafeMutablePointer<DarwinBoolean>!, _: UnsafeMutablePointer<Int32>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1390378-uccomparecollationkeys)

|  | Declaration |
| --- | --- |
| From | ``` func UCCompareCollationKeys(_ key1Ptr: UnsafePointer<UCCollationValue>, _ key1Length: Int, _ key2Ptr: UnsafePointer<UCCollationValue>, _ key2Length: Int, _ equivalent: UnsafeMutablePointer<DarwinBoolean>, _ order: UnsafeMutablePointer<Int32>) -> OSStatus ``` |
| To | ``` func UCCompareCollationKeys(_ key1Ptr: UnsafePointer<UCCollationValue>!, _ key1Length: Int, _ key2Ptr: UnsafePointer<UCCollationValue>!, _ key2Length: Int, _ equivalent: UnsafeMutablePointer<DarwinBoolean>!, _ order: UnsafeMutablePointer<Int32>!) -> OSStatus ``` |

Modified [UCCompareText(_: CollatorRef!, _: UnsafePointer<UniChar>!, _: Int, _: UnsafePointer<UniChar>!, _: Int, _: UnsafeMutablePointer<DarwinBoolean>!, _: UnsafeMutablePointer<Int32>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1390642-uccomparetext)

|  | Declaration |
| --- | --- |
| From | ``` func UCCompareText(_ collatorRef: CollatorRef, _ text1Ptr: UnsafePointer<UniChar>, _ text1Length: Int, _ text2Ptr: UnsafePointer<UniChar>, _ text2Length: Int, _ equivalent: UnsafeMutablePointer<DarwinBoolean>, _ order: UnsafeMutablePointer<Int32>) -> OSStatus ``` |
| To | ``` func UCCompareText(_ collatorRef: CollatorRef!, _ text1Ptr: UnsafePointer<UniChar>!, _ text1Length: Int, _ text2Ptr: UnsafePointer<UniChar>!, _ text2Length: Int, _ equivalent: UnsafeMutablePointer<DarwinBoolean>!, _ order: UnsafeMutablePointer<Int32>!) -> OSStatus ``` |

Modified [UCCompareTextDefault(_: UCCollateOptions, _: UnsafePointer<UniChar>!, _: Int, _: UnsafePointer<UniChar>!, _: Int, _: UnsafeMutablePointer<DarwinBoolean>!, _: UnsafeMutablePointer<Int32>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1390472-uccomparetextdefault)

|  | Declaration |
| --- | --- |
| From | ``` func UCCompareTextDefault(_ options: UCCollateOptions, _ text1Ptr: UnsafePointer<UniChar>, _ text1Length: Int, _ text2Ptr: UnsafePointer<UniChar>, _ text2Length: Int, _ equivalent: UnsafeMutablePointer<DarwinBoolean>, _ order: UnsafeMutablePointer<Int32>) -> OSStatus ``` |
| To | ``` func UCCompareTextDefault(_ options: UCCollateOptions, _ text1Ptr: UnsafePointer<UniChar>!, _ text1Length: Int, _ text2Ptr: UnsafePointer<UniChar>!, _ text2Length: Int, _ equivalent: UnsafeMutablePointer<DarwinBoolean>!, _ order: UnsafeMutablePointer<Int32>!) -> OSStatus ``` |

Modified [UCCompareTextNoLocale(_: UCCollateOptions, _: UnsafePointer<UniChar>!, _: Int, _: UnsafePointer<UniChar>!, _: Int, _: UnsafeMutablePointer<DarwinBoolean>!, _: UnsafeMutablePointer<Int32>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1390513-uccomparetextnolocale)

|  | Declaration |
| --- | --- |
| From | ``` func UCCompareTextNoLocale(_ options: UCCollateOptions, _ text1Ptr: UnsafePointer<UniChar>, _ text1Length: Int, _ text2Ptr: UnsafePointer<UniChar>, _ text2Length: Int, _ equivalent: UnsafeMutablePointer<DarwinBoolean>, _ order: UnsafeMutablePointer<Int32>) -> OSStatus ``` |
| To | ``` func UCCompareTextNoLocale(_ options: UCCollateOptions, _ text1Ptr: UnsafePointer<UniChar>!, _ text1Length: Int, _ text2Ptr: UnsafePointer<UniChar>!, _ text2Length: Int, _ equivalent: UnsafeMutablePointer<DarwinBoolean>!, _ order: UnsafeMutablePointer<Int32>!) -> OSStatus ``` |

Modified [UCCreateCollator(_: LocaleRef!, _: LocaleOperationVariant, _: UCCollateOptions, _: UnsafeMutablePointer<CollatorRef?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1390403-uccreatecollator)

|  | Declaration |
| --- | --- |
| From | ``` func UCCreateCollator(_ locale: LocaleRef, _ opVariant: LocaleOperationVariant, _ options: UCCollateOptions, _ collatorRef: UnsafeMutablePointer<CollatorRef>) -> OSStatus ``` |
| To | ``` func UCCreateCollator(_ locale: LocaleRef!, _ opVariant: LocaleOperationVariant, _ options: UCCollateOptions, _ collatorRef: UnsafeMutablePointer<CollatorRef?>!) -> OSStatus ``` |

Modified [UCDisposeCollator(_: UnsafeMutablePointer<CollatorRef?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1390435-ucdisposecollator)

|  | Declaration |
| --- | --- |
| From | ``` func UCDisposeCollator(_ collatorRef: UnsafeMutablePointer<CollatorRef>) -> OSStatus ``` |
| To | ``` func UCDisposeCollator(_ collatorRef: UnsafeMutablePointer<CollatorRef?>!) -> OSStatus ``` |

Modified [UCGetCollationKey(_: CollatorRef!, _: UnsafePointer<UniChar>!, _: Int, _: Int, _: UnsafeMutablePointer<Int>!, _: UnsafeMutablePointer<UCCollationValue>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1390468-ucgetcollationkey)

|  | Declaration |
| --- | --- |
| From | ``` func UCGetCollationKey(_ collatorRef: CollatorRef, _ textPtr: UnsafePointer<UniChar>, _ textLength: Int, _ maxKeySize: Int, _ actualKeySize: UnsafeMutablePointer<Int>, _ collationKey: UnsafeMutablePointer<UCCollationValue>) -> OSStatus ``` |
| To | ``` func UCGetCollationKey(_ collatorRef: CollatorRef!, _ textPtr: UnsafePointer<UniChar>!, _ textLength: Int, _ maxKeySize: Int, _ actualKeySize: UnsafeMutablePointer<Int>!, _ collationKey: UnsafeMutablePointer<UCCollationValue>!) -> OSStatus ``` |

Modified [UCKeyTranslate(_: UnsafePointer<UCKeyboardLayout>!, _: UInt16, _: UInt16, _: UInt32, _: UInt32, _: OptionBits, _: UnsafeMutablePointer<UInt32>!, _: Int, _: UnsafeMutablePointer<Int>!, _: UnsafeMutablePointer<UniChar>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1390584-uckeytranslate)

|  | Declaration |
| --- | --- |
| From | ``` func UCKeyTranslate(_ keyLayoutPtr: UnsafePointer<UCKeyboardLayout>, _ virtualKeyCode: UInt16, _ keyAction: UInt16, _ modifierKeyState: UInt32, _ keyboardType: UInt32, _ keyTranslateOptions: OptionBits, _ deadKeyState: UnsafeMutablePointer<UInt32>, _ maxStringLength: Int, _ actualStringLength: UnsafeMutablePointer<Int>, _ unicodeString: UnsafeMutablePointer<UniChar>) -> OSStatus ``` |
| To | ``` func UCKeyTranslate(_ keyLayoutPtr: UnsafePointer<UCKeyboardLayout>!, _ virtualKeyCode: UInt16, _ keyAction: UInt16, _ modifierKeyState: UInt32, _ keyboardType: UInt32, _ keyTranslateOptions: OptionBits, _ deadKeyState: UnsafeMutablePointer<UInt32>!, _ maxStringLength: Int, _ actualStringLength: UnsafeMutablePointer<Int>!, _ unicodeString: UnsafeMutablePointer<UniChar>!) -> OSStatus ``` |

Modified [UCTypeSelectAddKeyToSelector(_: UCTypeSelectRef!, _: CFString!, _: Double, _: UnsafeMutablePointer<DarwinBoolean>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1390517-uctypeselectaddkeytoselector)

|  | Declaration |
| --- | --- |
| From | ``` func UCTypeSelectAddKeyToSelector(_ inRef: UCTypeSelectRef, _ inText: CFString!, _ inEventTime: Double, _ updateFlag: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |
| To | ``` func UCTypeSelectAddKeyToSelector(_ inRef: UCTypeSelectRef!, _ inText: CFString!, _ inEventTime: Double, _ updateFlag: UnsafeMutablePointer<DarwinBoolean>!) -> OSStatus ``` |

Modified [UCTypeSelectCompare(_: UCTypeSelectRef!, _: CFString!, _: UnsafeMutablePointer<UCTypeSelectCompareResult>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1390474-uctypeselectcompare)

|  | Declaration |
| --- | --- |
| From | ``` func UCTypeSelectCompare(_ ref: UCTypeSelectRef, _ inText: CFString!, _ result: UnsafeMutablePointer<UCTypeSelectCompareResult>) -> OSStatus ``` |
| To | ``` func UCTypeSelectCompare(_ ref: UCTypeSelectRef!, _ inText: CFString!, _ result: UnsafeMutablePointer<UCTypeSelectCompareResult>!) -> OSStatus ``` |

Modified [UCTypeSelectCreateSelector(_: LocaleRef!, _: LocaleOperationVariant, _: UCCollateOptions, _: UnsafeMutablePointer<UCTypeSelectRef?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1390445-uctypeselectcreateselector)

|  | Declaration |
| --- | --- |
| From | ``` func UCTypeSelectCreateSelector(_ locale: LocaleRef, _ opVariant: LocaleOperationVariant, _ options: UCCollateOptions, _ newSelector: UnsafeMutablePointer<UCTypeSelectRef>) -> OSStatus ``` |
| To | ``` func UCTypeSelectCreateSelector(_ locale: LocaleRef!, _ opVariant: LocaleOperationVariant, _ options: UCCollateOptions, _ newSelector: UnsafeMutablePointer<UCTypeSelectRef?>!) -> OSStatus ``` |

Modified [UCTypeSelectFindItem(_: UCTypeSelectRef!, _: UInt32, _: UnsafeMutableRawPointer!, _: UnsafeMutableRawPointer!, _: CoreServices.IndexToUCStringUPP!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1390368-uctypeselectfinditem)

|  | Declaration |
| --- | --- |
| From | ``` func UCTypeSelectFindItem(_ ref: UCTypeSelectRef, _ listSize: UInt32, _ listDataPtr: UnsafeMutablePointer<Void>, _ refcon: UnsafeMutablePointer<Void>, _ userUPP: IndexToUCStringUPP!, _ closestItem: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func UCTypeSelectFindItem(_ ref: UCTypeSelectRef!, _ listSize: UInt32, _ listDataPtr: UnsafeMutableRawPointer!, _ refcon: UnsafeMutableRawPointer!, _ userUPP: CoreServices.IndexToUCStringUPP!, _ closestItem: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` |

Modified [UCTypeSelectFlushSelectorData(_: UCTypeSelectRef!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1390367-uctypeselectflushselectordata)

|  | Declaration |
| --- | --- |
| From | ``` func UCTypeSelectFlushSelectorData(_ ref: UCTypeSelectRef) -> OSStatus ``` |
| To | ``` func UCTypeSelectFlushSelectorData(_ ref: UCTypeSelectRef!) -> OSStatus ``` |

Modified [UCTypeSelectRef](https://developer.apple.com/documentation/coreservices/uctypeselectref)

|  | Declaration |
| --- | --- |
| From | ``` typealias UCTypeSelectRef = COpaquePointer ``` |
| To | ``` typealias UCTypeSelectRef = OpaquePointer ``` |

Modified [UCTypeSelectReleaseSelector(_: UnsafeMutablePointer<UCTypeSelectRef?>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1390644-uctypeselectreleaseselector)

|  | Declaration |
| --- | --- |
| From | ``` func UCTypeSelectReleaseSelector(_ ref: UnsafeMutablePointer<UCTypeSelectRef>) -> OSStatus ``` |
| To | ``` func UCTypeSelectReleaseSelector(_ ref: UnsafeMutablePointer<UCTypeSelectRef?>!) -> OSStatus ``` |

Modified [UCTypeSelectWalkList(_: UCTypeSelectRef!, _: CFString!, _: UCTSWalkDirection, _: UInt32, _: UnsafeMutableRawPointer!, _: UnsafeMutableRawPointer!, _: CoreServices.IndexToUCStringUPP!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1390442-uctypeselectwalklist)

|  | Declaration |
| --- | --- |
| From | ``` func UCTypeSelectWalkList(_ ref: UCTypeSelectRef, _ currSelect: CFString!, _ direction: UCTSWalkDirection, _ listSize: UInt32, _ listDataPtr: UnsafeMutablePointer<Void>, _ refcon: UnsafeMutablePointer<Void>, _ userUPP: IndexToUCStringUPP!, _ closestItem: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func UCTypeSelectWalkList(_ ref: UCTypeSelectRef!, _ currSelect: CFString!, _ direction: UCTSWalkDirection, _ listSize: UInt32, _ listDataPtr: UnsafeMutableRawPointer!, _ refcon: UnsafeMutableRawPointer!, _ userUPP: CoreServices.IndexToUCStringUPP!, _ closestItem: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` |

Modified [UCTypeSelectWouldResetBuffer(_: UCTypeSelectRef!, _: CFString!, _: Double) -> Bool](https://developer.apple.com/documentation/coreservices/1390538-uctypeselectwouldresetbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func UCTypeSelectWouldResetBuffer(_ inRef: UCTypeSelectRef, _ inText: CFString!, _ inEventTime: Double) -> Bool ``` |
| To | ``` func UCTypeSelectWouldResetBuffer(_ inRef: UCTypeSelectRef!, _ inText: CFString!, _ inEventTime: Double) -> Bool ``` |

Modified [UpdateIconRef(_: IconRef!) -> OSErr](https://developer.apple.com/documentation/coreservices/1445921-updateiconref)

|  | Declaration |
| --- | --- |
| From | ``` func UpdateIconRef(_ theIconRef: IconRef) -> OSErr ``` |
| To | ``` func UpdateIconRef(_ theIconRef: IconRef!) -> OSErr ``` |

Modified [vAEBuildAppleEvent(_: AEEventClass, _: AEEventID, _: DescType, _: UnsafeRawPointer!, _: Size, _: Int16, _: Int32, _: UnsafeMutablePointer<AppleEvent>!, _: UnsafeMutablePointer<AEBuildError>!, _: UnsafePointer<Int8>!, _: CVaListPointer) -> OSStatus](https://developer.apple.com/documentation/coreservices/1441729-vaebuildappleevent)

|  | Declaration |
| --- | --- |
| From | ``` func vAEBuildAppleEvent(_ theClass: AEEventClass, _ theID: AEEventID, _ addressType: DescType, _ addressData: UnsafePointer<Void>, _ addressLength: Size, _ returnID: Int16, _ transactionID: Int32, _ resultEvt: UnsafeMutablePointer<AppleEvent>, _ error: UnsafeMutablePointer<AEBuildError>, _ paramsFmt: UnsafePointer<Int8>, _ args: CVaListPointer) -> OSStatus ``` |
| To | ``` func vAEBuildAppleEvent(_ theClass: AEEventClass, _ theID: AEEventID, _ addressType: DescType, _ addressData: UnsafeRawPointer!, _ addressLength: Size, _ returnID: Int16, _ transactionID: Int32, _ resultEvt: UnsafeMutablePointer<AppleEvent>!, _ error: UnsafeMutablePointer<AEBuildError>!, _ paramsFmt: UnsafePointer<Int8>!, _ args: CVaListPointer) -> OSStatus ``` |

Modified [vAEBuildDesc(_: UnsafeMutablePointer<AEDesc>!, _: UnsafeMutablePointer<AEBuildError>!, _: UnsafePointer<Int8>!, _: CVaListPointer) -> OSStatus](https://developer.apple.com/documentation/coreservices/1446775-vaebuilddesc)

|  | Declaration |
| --- | --- |
| From | ``` func vAEBuildDesc(_ dst: UnsafeMutablePointer<AEDesc>, _ error: UnsafeMutablePointer<AEBuildError>, _ src: UnsafePointer<Int8>, _ args: CVaListPointer) -> OSStatus ``` |
| To | ``` func vAEBuildDesc(_ dst: UnsafeMutablePointer<AEDesc>!, _ error: UnsafeMutablePointer<AEBuildError>!, _ src: UnsafePointer<Int8>!, _ args: CVaListPointer) -> OSStatus ``` |

Modified [vAEBuildParameters(_: UnsafeMutablePointer<AppleEvent>!, _: UnsafeMutablePointer<AEBuildError>!, _: UnsafePointer<Int8>!, _: CVaListPointer) -> OSStatus](https://developer.apple.com/documentation/coreservices/1448040-vaebuildparameters)

|  | Declaration |
| --- | --- |
| From | ``` func vAEBuildParameters(_ event: UnsafeMutablePointer<AppleEvent>, _ error: UnsafeMutablePointer<AEBuildError>, _ format: UnsafePointer<Int8>, _ args: CVaListPointer) -> OSStatus ``` |
| To | ``` func vAEBuildParameters(_ event: UnsafeMutablePointer<AppleEvent>!, _ error: UnsafeMutablePointer<AEBuildError>!, _ format: UnsafePointer<Int8>!, _ args: CVaListPointer) -> OSStatus ``` |

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
