---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/CoreServices.html
archived_at: '2026-07-18T02:53:28.816590Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreServices Changes for Swift

### CoreServices

Removed AERemoteProcessResolverContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack, release: CFAllocatorReleaseCallBack, copyDescription: CFAllocatorCopyDescriptionCallBack)Removed CSIdentityClientContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack, release: CFAllocatorReleaseCallBack, copyDescription: CFAllocatorCopyDescriptionCallBack, statusUpdated: CSIdentityStatusUpdatedCallback)Removed CSIdentityQueryClientContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retainInfo: CFAllocatorRetainCallBack, releaseInfo: CFAllocatorReleaseCallBack, copyInfoDescription: CFAllocatorCopyDescriptionCallBack, receiveEvent: CSIdentityQueryReceiveEventCallback)Removed FSEventStreamContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack, release: CFAllocatorReleaseCallBack, copyDescription: CFAllocatorCopyDescriptionCallBack)Removed LSApplicationParameters.init(version: CFIndex, flags: LSLaunchFlags, application: UnsafePointer<FSRef>, asyncLaunchRefCon: UnsafeMutablePointer<Void>, environment: Unmanaged<CFDictionary>!, argv: Unmanaged<CFArray>!, initialEvent: UnsafeMutablePointer<AppleEvent>)Removed LSItemInfoRecord.init(flags: LSItemInfoFlags, filetype: OSType, creator: OSType, extension: Unmanaged<CFString>!)Removed LSLaunchFSRefSpec.init(appRef: UnsafePointer<FSRef>, numDocs: Int, itemRefs: UnsafePointer<FSRef>, passThruParams: UnsafePointer<AEDesc>, launchFlags: LSLaunchFlags, asyncRefCon: UnsafeMutablePointer<Void>)Removed LSLaunchURLSpec.init(appURL: Unmanaged<CFURL>!, itemURLs: Unmanaged<CFArray>!, passThruParams: UnsafePointer<AEDesc>, launchFlags: LSLaunchFlags, asyncRefCon: UnsafeMutablePointer<Void>)Removed MDExporterInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, ImporterExportData: CFunctionPointer<((UnsafeMutablePointer<Void>, CFDictionary!, CFString!, CFString!) -> Boolean)>)Removed MDImporterBundleWrapperURLInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, ImporterImportBundleWrapperURLData: CFunctionPointer<((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> Boolean)>)Removed MDImporterInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, ImporterImportData: CFunctionPointer<((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFString!) -> Boolean)>)Removed MDImporterURLInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, ImporterImportURLData: CFunctionPointer<((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> Boolean)>)Removed MDLabelDomain.valueRemoved MDQueryOptionFlags.valueRemoved MDQuerySortOptionFlags.valueRemoved SKDocumentIndexState.valueRemoved SKIndexType.valueRemoved SKSearchType.valueRemoved kLSAcceptAllowLoginUIRemoved kLSAcceptDefaultRemoved kLSHandlerOptionsDefaultRemoved kLSHandlerOptionsIgnoreCreatorRemoved [kLSInitializeDefaults](https://developer.apple.com/documentation/coreservices/launch_services/constants_no_longer_used/klsinitializedefaults)Removed kLSItemInfoAppIsScriptableRemoved kLSItemInfoAppPrefersClassicRemoved kLSItemInfoAppPrefersNativeRemoved kLSItemInfoExtensionIsHiddenRemoved kLSItemInfoIsAliasFileRemoved kLSItemInfoIsApplicationRemoved kLSItemInfoIsClassicAppRemoved kLSItemInfoIsContainerRemoved kLSItemInfoIsInvisibleRemoved kLSItemInfoIsNativeAppRemoved kLSItemInfoIsPackageRemoved kLSItemInfoIsPlainFileRemoved kLSItemInfoIsSymlinkRemoved kLSItemInfoIsVolumeRemoved kLSLaunchAndDisplayErrorsRemoved kLSLaunchAndHideRemoved kLSLaunchAndHideOthersRemoved kLSLaunchAndPrintRemoved kLSLaunchAsyncRemoved kLSLaunchDefaultsRemoved kLSLaunchDontAddToRecentsRemoved kLSLaunchDontSwitchRemoved kLSLaunchHasUntrustedContentsRemoved kLSLaunchInhibitBGOnlyRemoved kLSLaunchNewInstanceRemoved kLSLaunchNoParamsRemoved kLSLaunchReserved2Removed kLSLaunchReserved3Removed kLSLaunchReserved4Removed kLSLaunchReserved5Removed [kLSMinCatInfoBitmap](https://developer.apple.com/documentation/coreservices/launch_services/constants_no_longer_used/klsmincatinfobitmap)Removed kLSRequestAllFlagsRemoved kLSRequestAllInfoRemoved kLSRequestAppTypeFlagsRemoved kLSRequestBasicFlagsOnlyRemoved kLSRequestExtensionRemoved kLSRequestExtensionFlagsOnlyRemoved kLSRequestIconAndKindRemoved kLSRequestTypeCreatorRemoved kLSRolesAllRemoved kLSRolesEditorRemoved kLSRolesNoneRemoved kLSRolesShellRemoved kLSRolesViewerRemoved LSAcceptanceFlagsRemoved LSHandlerOptionsRemoved [LSInitializeFlags](https://developer.apple.com/documentation/coreservices/launch_services/constants_no_longer_used)Removed LSItemInfoFlagsRemoved LSLaunchFlagsRemoved LSRequestedInfoRemoved LSRolesMaskAdded AERemoteProcessResolverContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack!, release: CFAllocatorReleaseCallBack!, copyDescription: CFAllocatorCopyDescriptionCallBack!)Added CSIdentityClientContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack!, release: CFAllocatorReleaseCallBack!, copyDescription: CFAllocatorCopyDescriptionCallBack!, statusUpdated: CSIdentityStatusUpdatedCallback!)Added CSIdentityQueryClientContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retainInfo: CFAllocatorRetainCallBack!, releaseInfo: CFAllocatorReleaseCallBack!, copyInfoDescription: CFAllocatorCopyDescriptionCallBack!, receiveEvent: CSIdentityQueryReceiveEventCallback!)Added FSEventStreamContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack?, release: CFAllocatorReleaseCallBack?, copyDescription: CFAllocatorCopyDescriptionCallBack?)Added [LSAcceptanceFlags [struct]](https://developer.apple.com/documentation/coreservices/lsacceptanceflags)Added [LSAcceptanceFlags.AcceptAllowLoginUI](https://developer.apple.com/documentation/coreservices/lsacceptanceflags/klsacceptallowloginui)Added [LSAcceptanceFlags.AcceptDefault](https://developer.apple.com/documentation/coreservices/lsacceptanceflags/klsacceptdefault)Added LSAcceptanceFlags.init(rawValue: OptionBits)Added LSApplicationParameters.init(version: CFIndex, flags: LSLaunchFlags, application: UnsafePointer<FSRef>, asyncLaunchRefCon: UnsafeMutablePointer<Void>, environment: Unmanaged<CFDictionary>!, argv: Unmanaged<CFArray>!, initialEvent: UnsafeMutablePointer<AppleEvent>)Added [LSHandlerOptions [struct]](https://developer.apple.com/documentation/coreservices/lshandleroptions)Added [LSHandlerOptions.Default](https://developer.apple.com/documentation/coreservices/lshandleroptions/klshandleroptionsdefault)Added [LSHandlerOptions.IgnoreCreator](https://developer.apple.com/documentation/coreservices/lshandleroptions/klshandleroptionsignorecreator)Added LSHandlerOptions.init(rawValue: OptionBits)Added [LSItemInfoFlags [struct]](https://developer.apple.com/documentation/coreservices/lsiteminfoflags)Added [LSItemInfoFlags.AppIsScriptable](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1448463-appisscriptable)Added [LSItemInfoFlags.AppPrefersClassic](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoappprefersclassic)Added [LSItemInfoFlags.AppPrefersNative](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoappprefersnative)Added [LSItemInfoFlags.ExtensionIsHidden](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoextensionishidden)Added LSItemInfoFlags.init(rawValue: OptionBits)Added [LSItemInfoFlags.IsAliasFile](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoisaliasfile)Added [LSItemInfoFlags.IsApplication](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoisapplication)Added [LSItemInfoFlags.IsClassicApp](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoisclassicapp)Added [LSItemInfoFlags.IsContainer](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1443420-iscontainer)Added [LSItemInfoFlags.IsInvisible](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoisinvisible)Added [LSItemInfoFlags.IsNativeApp](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoisnativeapp)Added [LSItemInfoFlags.IsPackage](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1449324-ispackage)Added [LSItemInfoFlags.IsPlainFile](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoisplainfile)Added [LSItemInfoFlags.IsSymlink](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1446223-issymlink)Added [LSItemInfoFlags.IsVolume](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1448330-isvolume)Added LSItemInfoRecord.init(flags: LSItemInfoFlags, filetype: OSType, creator: OSType, extension: Unmanaged<CFString>!)Added [LSLaunchFlags [struct]](https://developer.apple.com/documentation/coreservices/lslaunchflags)Added [LSLaunchFlags.AndDisplayErrors](https://developer.apple.com/documentation/coreservices/lslaunchflags/klslaunchanddisplayerrors)Added [LSLaunchFlags.AndHide](https://developer.apple.com/documentation/coreservices/lslaunchflags/1444620-andhide)Added [LSLaunchFlags.AndHideOthers](https://developer.apple.com/documentation/coreservices/lslaunchflags/klslaunchandhideothers)Added [LSLaunchFlags.AndPrint](https://developer.apple.com/documentation/coreservices/lslaunchflags/1442495-andprint)Added [LSLaunchFlags.Async](https://developer.apple.com/documentation/coreservices/lslaunchflags/1445037-async)Added [LSLaunchFlags.Defaults](https://developer.apple.com/documentation/coreservices/lslaunchflags/klslaunchdefaults)Added [LSLaunchFlags.DontAddToRecents](https://developer.apple.com/documentation/coreservices/lslaunchflags/klslaunchdontaddtorecents)Added [LSLaunchFlags.DontSwitch](https://developer.apple.com/documentation/coreservices/lslaunchflags/1442057-dontswitch)Added [LSLaunchFlags.HasUntrustedContents](https://developer.apple.com/documentation/coreservices/1645929-anonymous/klslaunchhasuntrustedcontents)Added [LSLaunchFlags.InhibitBGOnly](https://developer.apple.com/documentation/coreservices/klslaunchinhibitbgonly)Added LSLaunchFlags.init(rawValue: OptionBits)Added [LSLaunchFlags.NewInstance](https://developer.apple.com/documentation/coreservices/lslaunchflags/1443359-newinstance)Added [LSLaunchFlags.NoParams](https://developer.apple.com/documentation/coreservices/1645929-anonymous/klslaunchnoparams)Added LSLaunchFlags.Reserved2Added LSLaunchFlags.Reserved3Added LSLaunchFlags.Reserved4Added LSLaunchFlags.Reserved5Added LSLaunchFSRefSpec.init(appRef: UnsafePointer<FSRef>, numDocs: Int, itemRefs: UnsafePointer<FSRef>, passThruParams: UnsafePointer<AEDesc>, launchFlags: LSLaunchFlags, asyncRefCon: UnsafeMutablePointer<Void>)Added LSLaunchURLSpec.init(appURL: Unmanaged<CFURL>?, itemURLs: Unmanaged<CFArray>?, passThruParams: UnsafePointer<AEDesc>, launchFlags: LSLaunchFlags, asyncRefCon: UnsafeMutablePointer<Void>)Added [LSRequestedInfo [struct]](https://developer.apple.com/documentation/coreservices/lsrequestedinfo)Added LSRequestedInfo.init(rawValue: OptionBits)Added [LSRequestedInfo.RequestAllFlags](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/1445356-requestallflags)Added [LSRequestedInfo.RequestAllInfo](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequestallinfo)Added [LSRequestedInfo.RequestAppTypeFlags](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequestapptypeflags)Added [LSRequestedInfo.RequestBasicFlagsOnly](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/1447145-requestbasicflagsonly)Added [LSRequestedInfo.RequestExtension](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequestextension)Added [LSRequestedInfo.RequestExtensionFlagsOnly](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequestextensionflagsonly)Added [LSRequestedInfo.RequestIconAndKind](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/1447945-requesticonandkind)Added [LSRequestedInfo.RequestTypeCreator](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequesttypecreator)Added [LSRolesMask [struct]](https://developer.apple.com/documentation/coreservices/lsrolesmask)Added [LSRolesMask.All](https://developer.apple.com/documentation/coreservices/lsrolesmask/1450616-all)Added [LSRolesMask.Editor](https://developer.apple.com/documentation/coreservices/lsrolesmask/klsroleseditor)Added LSRolesMask.init(rawValue: OptionBits)Added [LSRolesMask.None](https://developer.apple.com/documentation/coreservices/lsrolesmask/klsrolesnone)Added [LSRolesMask.Shell](https://developer.apple.com/documentation/coreservices/lsrolesmask/1442557-shell)Added [LSRolesMask.Viewer](https://developer.apple.com/documentation/coreservices/lsrolesmask/1441708-viewer)Added MDExporterInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, ImporterExportData: ((UnsafeMutablePointer<Void>, CFDictionary!, CFString!, CFString!) -> DarwinBoolean)!)Added MDImporterBundleWrapperURLInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, ImporterImportBundleWrapperURLData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> DarwinBoolean)!)Added MDImporterInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, ImporterImportData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFString!) -> DarwinBoolean)!)Added MDImporterURLInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, ImporterImportURLData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> DarwinBoolean)!)Added MDLabelDomain.init(rawValue: UInt32)Added MDLabelDomain.rawValueAdded MDQueryOptionFlags.init(rawValue: UInt32)Added MDQueryOptionFlags.rawValueAdded MDQuerySortOptionFlags.init(rawValue: UInt32)Added MDQuerySortOptionFlags.rawValueAdded SKDocumentIndexState.init(rawValue: UInt32)Added SKDocumentIndexState.rawValueAdded SKIndexType.init(rawValue: UInt32)Added SKIndexType.rawValueAdded SKSearchType.init(rawValue: UInt32)Added SKSearchType.rawValueAdded [kMDItemHTMLContent](https://developer.apple.com/documentation/coreservices/kmditemhtmlcontent)Added [kUTTypeSwiftSource](https://developer.apple.com/documentation/coreservices/kuttypeswiftsource)Modified [AERemoteProcessResolverContext [struct]](https://developer.apple.com/documentation/coreservices/aeremoteprocessresolvercontext)

|  | Declaration |
| --- | --- |
| From | ``` struct AERemoteProcessResolverContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack     var release: CFAllocatorReleaseCallBack     var copyDescription: CFAllocatorCopyDescriptionCallBack     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack, release release: CFAllocatorReleaseCallBack, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack) } ``` |
| To | ``` struct AERemoteProcessResolverContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack!     var release: CFAllocatorReleaseCallBack!     var copyDescription: CFAllocatorCopyDescriptionCallBack!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack!, release release: CFAllocatorReleaseCallBack!, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack!) } ``` |

Modified [AERemoteProcessResolverContext.copyDescription](https://developer.apple.com/documentation/coreservices/aeremoteprocessresolvercontext/1442771-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFAllocatorCopyDescriptionCallBack ``` |
| To | ``` var copyDescription: CFAllocatorCopyDescriptionCallBack! ``` |

Modified [AERemoteProcessResolverContext.release](https://developer.apple.com/documentation/coreservices/aeremoteprocessresolvercontext/1444738-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFAllocatorReleaseCallBack ``` |
| To | ``` var release: CFAllocatorReleaseCallBack! ``` |

Modified [AERemoteProcessResolverContext.retain](https://developer.apple.com/documentation/coreservices/aeremoteprocessresolvercontext/1450097-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFAllocatorRetainCallBack ``` |
| To | ``` var retain: CFAllocatorRetainCallBack! ``` |

Modified [CSIdentityClientContext [struct]](https://developer.apple.com/documentation/coreservices/csidentityclientcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CSIdentityClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack     var release: CFAllocatorReleaseCallBack     var copyDescription: CFAllocatorCopyDescriptionCallBack     var statusUpdated: CSIdentityStatusUpdatedCallback     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack, release release: CFAllocatorReleaseCallBack, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack, statusUpdated statusUpdated: CSIdentityStatusUpdatedCallback) } ``` |
| To | ``` struct CSIdentityClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack!     var release: CFAllocatorReleaseCallBack!     var copyDescription: CFAllocatorCopyDescriptionCallBack!     var statusUpdated: CSIdentityStatusUpdatedCallback!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack!, release release: CFAllocatorReleaseCallBack!, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack!, statusUpdated statusUpdated: CSIdentityStatusUpdatedCallback!) } ``` |

Modified [CSIdentityClientContext.copyDescription](https://developer.apple.com/documentation/coreservices/csidentityclientcontext/1445249-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFAllocatorCopyDescriptionCallBack ``` |
| To | ``` var copyDescription: CFAllocatorCopyDescriptionCallBack! ``` |

Modified [CSIdentityClientContext.release](https://developer.apple.com/documentation/coreservices/csidentityclientcontext/1448741-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFAllocatorReleaseCallBack ``` |
| To | ``` var release: CFAllocatorReleaseCallBack! ``` |

Modified [CSIdentityClientContext.retain](https://developer.apple.com/documentation/coreservices/csidentityclientcontext/1444414-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFAllocatorRetainCallBack ``` |
| To | ``` var retain: CFAllocatorRetainCallBack! ``` |

Modified [CSIdentityClientContext.statusUpdated](https://developer.apple.com/documentation/coreservices/csidentityclientcontext/1447852-statusupdated)

|  | Declaration |
| --- | --- |
| From | ``` var statusUpdated: CSIdentityStatusUpdatedCallback ``` |
| To | ``` var statusUpdated: CSIdentityStatusUpdatedCallback! ``` |

Modified [CSIdentityQueryClientContext [struct]](https://developer.apple.com/documentation/coreservices/csidentityqueryclientcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CSIdentityQueryClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retainInfo: CFAllocatorRetainCallBack     var releaseInfo: CFAllocatorReleaseCallBack     var copyInfoDescription: CFAllocatorCopyDescriptionCallBack     var receiveEvent: CSIdentityQueryReceiveEventCallback     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retainInfo retainInfo: CFAllocatorRetainCallBack, releaseInfo releaseInfo: CFAllocatorReleaseCallBack, copyInfoDescription copyInfoDescription: CFAllocatorCopyDescriptionCallBack, receiveEvent receiveEvent: CSIdentityQueryReceiveEventCallback) } ``` |
| To | ``` struct CSIdentityQueryClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retainInfo: CFAllocatorRetainCallBack!     var releaseInfo: CFAllocatorReleaseCallBack!     var copyInfoDescription: CFAllocatorCopyDescriptionCallBack!     var receiveEvent: CSIdentityQueryReceiveEventCallback!     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retainInfo retainInfo: CFAllocatorRetainCallBack!, releaseInfo releaseInfo: CFAllocatorReleaseCallBack!, copyInfoDescription copyInfoDescription: CFAllocatorCopyDescriptionCallBack!, receiveEvent receiveEvent: CSIdentityQueryReceiveEventCallback!) } ``` |

Modified [CSIdentityQueryClientContext.copyInfoDescription](https://developer.apple.com/documentation/coreservices/csidentityqueryclientcontext/1428999-copyinfodescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyInfoDescription: CFAllocatorCopyDescriptionCallBack ``` |
| To | ``` var copyInfoDescription: CFAllocatorCopyDescriptionCallBack! ``` |

Modified [CSIdentityQueryClientContext.receiveEvent](https://developer.apple.com/documentation/coreservices/csidentityqueryclientcontext/1429030-receiveevent)

|  | Declaration |
| --- | --- |
| From | ``` var receiveEvent: CSIdentityQueryReceiveEventCallback ``` |
| To | ``` var receiveEvent: CSIdentityQueryReceiveEventCallback! ``` |

Modified [CSIdentityQueryClientContext.releaseInfo](https://developer.apple.com/documentation/coreservices/csidentityqueryclientcontext/1429034-releaseinfo)

|  | Declaration |
| --- | --- |
| From | ``` var releaseInfo: CFAllocatorReleaseCallBack ``` |
| To | ``` var releaseInfo: CFAllocatorReleaseCallBack! ``` |

Modified [CSIdentityQueryClientContext.retainInfo](https://developer.apple.com/documentation/coreservices/csidentityqueryclientcontext/1429016-retaininfo)

|  | Declaration |
| --- | --- |
| From | ``` var retainInfo: CFAllocatorRetainCallBack ``` |
| To | ``` var retainInfo: CFAllocatorRetainCallBack! ``` |

Modified [FSEventStreamContext [struct]](https://developer.apple.com/documentation/coreservices/fseventstreamcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct FSEventStreamContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack     var release: CFAllocatorReleaseCallBack     var copyDescription: CFAllocatorCopyDescriptionCallBack     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack, release release: CFAllocatorReleaseCallBack, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack) } ``` |
| To | ``` struct FSEventStreamContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack?     var release: CFAllocatorReleaseCallBack?     var copyDescription: CFAllocatorCopyDescriptionCallBack?     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack?, release release: CFAllocatorReleaseCallBack?, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack?) } ``` |

Modified [FSEventStreamContext.copyDescription](https://developer.apple.com/documentation/coreservices/fseventstreamcontext/1445178-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFAllocatorCopyDescriptionCallBack ``` |
| To | ``` var copyDescription: CFAllocatorCopyDescriptionCallBack? ``` |

Modified [FSEventStreamContext.release](https://developer.apple.com/documentation/coreservices/fseventstreamcontext/1450554-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFAllocatorReleaseCallBack ``` |
| To | ``` var release: CFAllocatorReleaseCallBack? ``` |

Modified [FSEventStreamContext.retain](https://developer.apple.com/documentation/coreservices/fseventstreamcontext/1450539-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFAllocatorRetainCallBack ``` |
| To | ``` var retain: CFAllocatorRetainCallBack? ``` |

Modified [LSItemInfoRecord [struct]](https://developer.apple.com/documentation/coreservices/lsiteminforecord)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSItemInfoRecord.creator](https://developer.apple.com/documentation/coreservices/lsiteminforecord/1441870-creator)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSItemInfoRecord.extension](https://developer.apple.com/documentation/coreservices/lsiteminforecord/1442123-extension)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSItemInfoRecord.filetype](https://developer.apple.com/documentation/coreservices/lsiteminforecord/1447384-filetype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSItemInfoRecord.flags](https://developer.apple.com/documentation/coreservices/lsiteminforecord/1446281-flags)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified LSItemInfoRecord.init()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSLaunchURLSpec [struct]](https://developer.apple.com/documentation/coreservices/lslaunchurlspec)

|  | Declaration |
| --- | --- |
| From | ``` struct LSLaunchURLSpec {     var appURL: Unmanaged<CFURL>!     var itemURLs: Unmanaged<CFArray>!     var passThruParams: UnsafePointer<AEDesc>     var launchFlags: LSLaunchFlags     var asyncRefCon: UnsafeMutablePointer<Void>     init()     init(appURL appURL: Unmanaged<CFURL>!, itemURLs itemURLs: Unmanaged<CFArray>!, passThruParams passThruParams: UnsafePointer<AEDesc>, launchFlags launchFlags: LSLaunchFlags, asyncRefCon asyncRefCon: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct LSLaunchURLSpec {     var appURL: Unmanaged<CFURL>?     var itemURLs: Unmanaged<CFArray>?     var passThruParams: UnsafePointer<AEDesc>     var launchFlags: LSLaunchFlags     var asyncRefCon: UnsafeMutablePointer<Void>     init()     init(appURL appURL: Unmanaged<CFURL>?, itemURLs itemURLs: Unmanaged<CFArray>?, passThruParams passThruParams: UnsafePointer<AEDesc>, launchFlags launchFlags: LSLaunchFlags, asyncRefCon asyncRefCon: UnsafeMutablePointer<Void>) } ``` |

Modified [LSLaunchURLSpec.appURL](https://developer.apple.com/documentation/coreservices/lslaunchurlspec/1443566-appurl)

|  | Declaration |
| --- | --- |
| From | ``` var appURL: Unmanaged<CFURL>! ``` |
| To | ``` var appURL: Unmanaged<CFURL>? ``` |

Modified [LSLaunchURLSpec.itemURLs](https://developer.apple.com/documentation/coreservices/lslaunchurlspec/1443759-itemurls)

|  | Declaration |
| --- | --- |
| From | ``` var itemURLs: Unmanaged<CFArray>! ``` |
| To | ``` var itemURLs: Unmanaged<CFArray>? ``` |

Modified [MDExporterInterfaceStruct [struct]](https://developer.apple.com/documentation/coreservices/mdexporterinterfacestruct)

|  | Declaration |
| --- | --- |
| From | ``` struct MDExporterInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>     var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var ImporterExportData: CFunctionPointer<((UnsafeMutablePointer<Void>, CFDictionary!, CFString!, CFString!) -> Boolean)>     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, ImporterExportData ImporterExportData: CFunctionPointer<((UnsafeMutablePointer<Void>, CFDictionary!, CFString!, CFString!) -> Boolean)>) } ``` |
| To | ``` struct MDExporterInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!     var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!     var Release: ((UnsafeMutablePointer<Void>) -> ULONG)!     var ImporterExportData: ((UnsafeMutablePointer<Void>, CFDictionary!, CFString!, CFString!) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, ImporterExportData ImporterExportData: ((UnsafeMutablePointer<Void>, CFDictionary!, CFString!, CFString!) -> DarwinBoolean)!) } ``` |

Modified [MDExporterInterfaceStruct.AddRef](https://developer.apple.com/documentation/coreservices/mdexporterinterfacestruct/1449918-addref)

|  | Declaration |
| --- | --- |
| From | ``` var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)> ``` |
| To | ``` var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |

Modified [MDExporterInterfaceStruct.ImporterExportData](https://developer.apple.com/documentation/coreservices/mdexporterinterfacestruct/1446348-importerexportdata)

|  | Declaration |
| --- | --- |
| From | ``` var ImporterExportData: CFunctionPointer<((UnsafeMutablePointer<Void>, CFDictionary!, CFString!, CFString!) -> Boolean)> ``` |
| To | ``` var ImporterExportData: ((UnsafeMutablePointer<Void>, CFDictionary!, CFString!, CFString!) -> DarwinBoolean)! ``` |

Modified [MDExporterInterfaceStruct.QueryInterface](https://developer.apple.com/documentation/coreservices/mdexporterinterfacestruct/1450043-queryinterface)

|  | Declaration |
| --- | --- |
| From | ``` var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)> ``` |
| To | ``` var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)! ``` |

Modified [MDExporterInterfaceStruct.Release](https://developer.apple.com/documentation/coreservices/mdexporterinterfacestruct/1448271-release)

|  | Declaration |
| --- | --- |
| From | ``` var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)> ``` |
| To | ``` var Release: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |

Modified [MDImporterBundleWrapperURLInterfaceStruct [struct]](https://developer.apple.com/documentation/coreservices/mdimporterbundlewrapperurlinterfacestruct)

|  | Declaration |
| --- | --- |
| From | ``` struct MDImporterBundleWrapperURLInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>     var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var ImporterImportBundleWrapperURLData: CFunctionPointer<((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> Boolean)>     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, ImporterImportBundleWrapperURLData ImporterImportBundleWrapperURLData: CFunctionPointer<((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> Boolean)>) } ``` |
| To | ``` struct MDImporterBundleWrapperURLInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!     var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!     var Release: ((UnsafeMutablePointer<Void>) -> ULONG)!     var ImporterImportBundleWrapperURLData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, ImporterImportBundleWrapperURLData ImporterImportBundleWrapperURLData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> DarwinBoolean)!) } ``` |

Modified [MDImporterBundleWrapperURLInterfaceStruct.AddRef](https://developer.apple.com/documentation/coreservices/mdimporterbundlewrapperurlinterfacestruct/1442108-addref)

|  | Declaration |
| --- | --- |
| From | ``` var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)> ``` |
| To | ``` var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |

Modified [MDImporterBundleWrapperURLInterfaceStruct.ImporterImportBundleWrapperURLData](https://developer.apple.com/documentation/coreservices/mdimporterbundlewrapperurlinterfacestruct/1443517-importerimportbundlewrapperurlda)

|  | Declaration |
| --- | --- |
| From | ``` var ImporterImportBundleWrapperURLData: CFunctionPointer<((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> Boolean)> ``` |
| To | ``` var ImporterImportBundleWrapperURLData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> DarwinBoolean)! ``` |

Modified [MDImporterBundleWrapperURLInterfaceStruct.QueryInterface](https://developer.apple.com/documentation/coreservices/mdimporterbundlewrapperurlinterfacestruct/1445643-queryinterface)

|  | Declaration |
| --- | --- |
| From | ``` var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)> ``` |
| To | ``` var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)! ``` |

Modified [MDImporterBundleWrapperURLInterfaceStruct.Release](https://developer.apple.com/documentation/coreservices/mdimporterbundlewrapperurlinterfacestruct/1450356-release)

|  | Declaration |
| --- | --- |
| From | ``` var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)> ``` |
| To | ``` var Release: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |

Modified [MDImporterInterfaceStruct [struct]](https://developer.apple.com/documentation/coreservices/mdimporterinterfacestruct)

|  | Declaration |
| --- | --- |
| From | ``` struct MDImporterInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>     var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var ImporterImportData: CFunctionPointer<((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFString!) -> Boolean)>     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, ImporterImportData ImporterImportData: CFunctionPointer<((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFString!) -> Boolean)>) } ``` |
| To | ``` struct MDImporterInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!     var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!     var Release: ((UnsafeMutablePointer<Void>) -> ULONG)!     var ImporterImportData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFString!) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, ImporterImportData ImporterImportData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFString!) -> DarwinBoolean)!) } ``` |

Modified [MDImporterInterfaceStruct.AddRef](https://developer.apple.com/documentation/coreservices/mdimporterinterfacestruct/1443912-addref)

|  | Declaration |
| --- | --- |
| From | ``` var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)> ``` |
| To | ``` var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |

Modified [MDImporterInterfaceStruct.ImporterImportData](https://developer.apple.com/documentation/coreservices/mdimporterinterfacestruct/1444710-importerimportdata)

|  | Declaration |
| --- | --- |
| From | ``` var ImporterImportData: CFunctionPointer<((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFString!) -> Boolean)> ``` |
| To | ``` var ImporterImportData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFString!) -> DarwinBoolean)! ``` |

Modified [MDImporterInterfaceStruct.QueryInterface](https://developer.apple.com/documentation/coreservices/mdimporterinterfacestruct/1446572-queryinterface)

|  | Declaration |
| --- | --- |
| From | ``` var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)> ``` |
| To | ``` var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)! ``` |

Modified [MDImporterInterfaceStruct.Release](https://developer.apple.com/documentation/coreservices/mdimporterinterfacestruct/1441880-release)

|  | Declaration |
| --- | --- |
| From | ``` var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)> ``` |
| To | ``` var Release: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |

Modified [MDImporterURLInterfaceStruct [struct]](https://developer.apple.com/documentation/coreservices/mdimporterurlinterfacestruct)

|  | Declaration |
| --- | --- |
| From | ``` struct MDImporterURLInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>     var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var ImporterImportURLData: CFunctionPointer<((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> Boolean)>     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, ImporterImportURLData ImporterImportURLData: CFunctionPointer<((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> Boolean)>) } ``` |
| To | ``` struct MDImporterURLInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!     var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!     var Release: ((UnsafeMutablePointer<Void>) -> ULONG)!     var ImporterImportURLData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> DarwinBoolean)!     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, ImporterImportURLData ImporterImportURLData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> DarwinBoolean)!) } ``` |

Modified [MDImporterURLInterfaceStruct.AddRef](https://developer.apple.com/documentation/coreservices/mdimporterurlinterfacestruct/1448177-addref)

|  | Declaration |
| --- | --- |
| From | ``` var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)> ``` |
| To | ``` var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |

Modified [MDImporterURLInterfaceStruct.ImporterImportURLData](https://developer.apple.com/documentation/coreservices/mdimporterurlinterfacestruct/1447378-importerimporturldata)

|  | Declaration |
| --- | --- |
| From | ``` var ImporterImportURLData: CFunctionPointer<((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> Boolean)> ``` |
| To | ``` var ImporterImportURLData: ((UnsafeMutablePointer<Void>, CFMutableDictionary!, CFString!, CFURL!) -> DarwinBoolean)! ``` |

Modified [MDImporterURLInterfaceStruct.QueryInterface](https://developer.apple.com/documentation/coreservices/mdimporterurlinterfacestruct/1442296-queryinterface)

|  | Declaration |
| --- | --- |
| From | ``` var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)> ``` |
| To | ``` var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)! ``` |

Modified [MDImporterURLInterfaceStruct.Release](https://developer.apple.com/documentation/coreservices/mdimporterurlinterfacestruct/1450015-release)

|  | Declaration |
| --- | --- |
| From | ``` var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)> ``` |
| To | ``` var Release: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |

Modified [MDLabelDomain [struct]](https://developer.apple.com/documentation/coreservices/mdlabeldomain)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MDLabelDomain {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct MDLabelDomain : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [MDQueryOptionFlags [struct]](https://developer.apple.com/documentation/coreservices/mdqueryoptionflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MDQueryOptionFlags {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct MDQueryOptionFlags : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [MDQuerySortOptionFlags [struct]](https://developer.apple.com/documentation/coreservices/mdquerysortoptionflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MDQuerySortOptionFlags {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct MDQuerySortOptionFlags : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [SKDocumentIndexState [struct]](https://developer.apple.com/documentation/coreservices/skdocumentindexstate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SKDocumentIndexState {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct SKDocumentIndexState : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [SKIndexType [struct]](https://developer.apple.com/documentation/coreservices/skindextype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SKIndexType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct SKIndexType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [SKSearchType [struct]](https://developer.apple.com/documentation/coreservices/sksearchtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SKSearchType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct SKSearchType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [AECheckIsRecord(_: UnsafePointer<AEDesc>) -> Bool](https://developer.apple.com/documentation/coreservices/1444011-aecheckisrecord)

|  | Declaration |
| --- | --- |
| From | ``` func AECheckIsRecord(_ theDesc: UnsafePointer<AEDesc>) -> Boolean ``` |
| To | ``` func AECheckIsRecord(_ theDesc: UnsafePointer<AEDesc>) -> Bool ``` |

Modified [AECoerceDescProcPtr](https://developer.apple.com/documentation/coreservices/aecoercedescprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias AECoerceDescProcPtr = CFunctionPointer<((UnsafePointer<AEDesc>, DescType, SRefCon, UnsafeMutablePointer<AEDesc>) -> OSErr)> ``` |
| To | ``` typealias AECoerceDescProcPtr = (UnsafePointer<AEDesc>, DescType, SRefCon, UnsafeMutablePointer<AEDesc>) -> OSErr ``` |

Modified [AECoercePtrProcPtr](https://developer.apple.com/documentation/coreservices/aecoerceptrprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias AECoercePtrProcPtr = CFunctionPointer<((DescType, UnsafePointer<Void>, Size, DescType, SRefCon, UnsafeMutablePointer<AEDesc>) -> OSErr)> ``` |
| To | ``` typealias AECoercePtrProcPtr = (DescType, UnsafePointer<Void>, Size, DescType, SRefCon, UnsafeMutablePointer<AEDesc>) -> OSErr ``` |

Modified [AECompareDesc(_: UnsafePointer<AEDesc>, _: UnsafePointer<AEDesc>, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/coreservices/1448782-aecomparedesc)

|  | Declaration |
| --- | --- |
| From | ``` func AECompareDesc(_ desc1: UnsafePointer<AEDesc>, _ desc2: UnsafePointer<AEDesc>, _ resultP: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func AECompareDesc(_ desc1: UnsafePointer<AEDesc>, _ desc2: UnsafePointer<AEDesc>, _ resultP: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [AECreateDescFromExternalPtr(_: OSType, _: UnsafePointer<Void>, _: Size, _: AEDisposeExternalUPP!, _: SRefCon, _: UnsafeMutablePointer<AEDesc>) -> OSStatus](https://developer.apple.com/documentation/coreservices/1446239-aecreatedescfromexternalptr)

|  | Declaration |
| --- | --- |
| From | ``` func AECreateDescFromExternalPtr(_ descriptorType: OSType, _ dataPtr: UnsafePointer<Void>, _ dataLength: Size, _ disposeCallback: AEDisposeExternalUPP, _ disposeRefcon: SRefCon, _ theDesc: UnsafeMutablePointer<AEDesc>) -> OSStatus ``` |
| To | ``` func AECreateDescFromExternalPtr(_ descriptorType: OSType, _ dataPtr: UnsafePointer<Void>, _ dataLength: Size, _ disposeCallback: AEDisposeExternalUPP!, _ disposeRefcon: SRefCon, _ theDesc: UnsafeMutablePointer<AEDesc>) -> OSStatus ``` |

Modified [AECreateList(_: UnsafePointer<Void>, _: Size, _: Bool, _: UnsafeMutablePointer<AEDescList>) -> OSErr](https://developer.apple.com/documentation/coreservices/1448643-aecreatelist)

|  | Declaration |
| --- | --- |
| From | ``` func AECreateList(_ factoringPtr: UnsafePointer<Void>, _ factoredSize: Size, _ isRecord: Boolean, _ resultList: UnsafeMutablePointer<AEDescList>) -> OSErr ``` |
| To | ``` func AECreateList(_ factoringPtr: UnsafePointer<Void>, _ factoredSize: Size, _ isRecord: Bool, _ resultList: UnsafeMutablePointer<AEDescList>) -> OSErr ``` |

Modified [AEDisposeExternalProcPtr](https://developer.apple.com/documentation/coreservices/aedisposeexternalprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias AEDisposeExternalProcPtr = CFunctionPointer<((UnsafePointer<Void>, Size, SRefCon) -> Void)> ``` |
| To | ``` typealias AEDisposeExternalProcPtr = (UnsafePointer<Void>, Size, SRefCon) -> Void ``` |

Modified [AEEventHandlerProcPtr](https://developer.apple.com/documentation/coreservices/aeeventhandlerprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias AEEventHandlerProcPtr = CFunctionPointer<((UnsafePointer<AppleEvent>, UnsafeMutablePointer<AppleEvent>, SRefCon) -> OSErr)> ``` |
| To | ``` typealias AEEventHandlerProcPtr = (UnsafePointer<AppleEvent>, UnsafeMutablePointer<AppleEvent>, SRefCon) -> OSErr ``` |

Modified [AEGetCoercionHandler(_: DescType, _: DescType, _: UnsafeMutablePointer<AECoercionHandlerUPP?>, _: UnsafeMutablePointer<SRefCon>, _: UnsafeMutablePointer<DarwinBoolean>, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1445348-aegetcoercionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func AEGetCoercionHandler(_ fromType: DescType, _ toType: DescType, _ handler: UnsafeMutablePointer<AECoercionHandlerUPP>, _ handlerRefcon: UnsafeMutablePointer<SRefCon>, _ fromTypeIsDesc: UnsafeMutablePointer<Boolean>, _ isSysHandler: Boolean) -> OSErr ``` |
| To | ``` func AEGetCoercionHandler(_ fromType: DescType, _ toType: DescType, _ handler: UnsafeMutablePointer<AECoercionHandlerUPP?>, _ handlerRefcon: UnsafeMutablePointer<SRefCon>, _ fromTypeIsDesc: UnsafeMutablePointer<DarwinBoolean>, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AEGetEventHandler(_: AEEventClass, _: AEEventID, _: UnsafeMutablePointer<AEEventHandlerUPP?>, _: UnsafeMutablePointer<SRefCon>, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1445631-aegeteventhandler)

|  | Declaration |
| --- | --- |
| From | ``` func AEGetEventHandler(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ handler: UnsafeMutablePointer<AEEventHandlerUPP>, _ handlerRefcon: UnsafeMutablePointer<SRefCon>, _ isSysHandler: Boolean) -> OSErr ``` |
| To | ``` func AEGetEventHandler(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ handler: UnsafeMutablePointer<AEEventHandlerUPP?>, _ handlerRefcon: UnsafeMutablePointer<SRefCon>, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AEGetObjectAccessor(_: DescType, _: DescType, _: UnsafeMutablePointer<OSLAccessorUPP?>, _: UnsafeMutablePointer<SRefCon>, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1449054-aegetobjectaccessor)

|  | Declaration |
| --- | --- |
| From | ``` func AEGetObjectAccessor(_ desiredClass: DescType, _ containerType: DescType, _ accessor: UnsafeMutablePointer<OSLAccessorUPP>, _ accessorRefcon: UnsafeMutablePointer<SRefCon>, _ isSysHandler: Boolean) -> OSErr ``` |
| To | ``` func AEGetObjectAccessor(_ desiredClass: DescType, _ containerType: DescType, _ accessor: UnsafeMutablePointer<OSLAccessorUPP?>, _ accessorRefcon: UnsafeMutablePointer<SRefCon>, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AEGetSpecialHandler(_: AEKeyword, _: UnsafeMutablePointer<AEEventHandlerUPP?>, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1444274-aegetspecialhandler)

|  | Declaration |
| --- | --- |
| From | ``` func AEGetSpecialHandler(_ functionClass: AEKeyword, _ handler: UnsafeMutablePointer<AEEventHandlerUPP>, _ isSysHandler: Boolean) -> OSErr ``` |
| To | ``` func AEGetSpecialHandler(_ functionClass: AEKeyword, _ handler: UnsafeMutablePointer<AEEventHandlerUPP?>, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AEInstallCoercionHandler(_: DescType, _: DescType, _: AECoercionHandlerUPP!, _: SRefCon, _: Bool, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1445548-aeinstallcoercionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func AEInstallCoercionHandler(_ fromType: DescType, _ toType: DescType, _ handler: AECoercionHandlerUPP, _ handlerRefcon: SRefCon, _ fromTypeIsDesc: Boolean, _ isSysHandler: Boolean) -> OSErr ``` |
| To | ``` func AEInstallCoercionHandler(_ fromType: DescType, _ toType: DescType, _ handler: AECoercionHandlerUPP!, _ handlerRefcon: SRefCon, _ fromTypeIsDesc: Bool, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AEInstallEventHandler(_: AEEventClass, _: AEEventID, _: AEEventHandlerUPP!, _: SRefCon, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1448596-aeinstalleventhandler)

|  | Declaration |
| --- | --- |
| From | ``` func AEInstallEventHandler(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ handler: AEEventHandlerUPP, _ handlerRefcon: SRefCon, _ isSysHandler: Boolean) -> OSErr ``` |
| To | ``` func AEInstallEventHandler(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ handler: AEEventHandlerUPP!, _ handlerRefcon: SRefCon, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AEInstallObjectAccessor(_: DescType, _: DescType, _: OSLAccessorUPP!, _: SRefCon, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1447905-aeinstallobjectaccessor)

|  | Declaration |
| --- | --- |
| From | ``` func AEInstallObjectAccessor(_ desiredClass: DescType, _ containerType: DescType, _ theAccessor: OSLAccessorUPP, _ accessorRefcon: SRefCon, _ isSysHandler: Boolean) -> OSErr ``` |
| To | ``` func AEInstallObjectAccessor(_ desiredClass: DescType, _ containerType: DescType, _ theAccessor: OSLAccessorUPP!, _ accessorRefcon: SRefCon, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AEInstallSpecialHandler(_: AEKeyword, _: AEEventHandlerUPP!, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1445532-aeinstallspecialhandler)

|  | Declaration |
| --- | --- |
| From | ``` func AEInstallSpecialHandler(_ functionClass: AEKeyword, _ handler: AEEventHandlerUPP, _ isSysHandler: Boolean) -> OSErr ``` |
| To | ``` func AEInstallSpecialHandler(_ functionClass: AEKeyword, _ handler: AEEventHandlerUPP!, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AERemoteProcessResolverCallback](https://developer.apple.com/documentation/coreservices/aeremoteprocessresolvercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias AERemoteProcessResolverCallback = CFunctionPointer<((AERemoteProcessResolverRef, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias AERemoteProcessResolverCallback = (AERemoteProcessResolverRef, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [AERemoteProcessResolverScheduleWithRunLoop(_: AERemoteProcessResolverRef, _: CFRunLoop!, _: CFString!, _: AERemoteProcessResolverCallback!, _: UnsafePointer<AERemoteProcessResolverContext>)](https://developer.apple.com/documentation/coreservices/1447259-aeremoteprocessresolverschedulew)

|  | Declaration |
| --- | --- |
| From | ``` func AERemoteProcessResolverScheduleWithRunLoop(_ ref: AERemoteProcessResolverRef, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!, _ callback: AERemoteProcessResolverCallback, _ ctx: UnsafePointer<AERemoteProcessResolverContext>) ``` |
| To | ``` func AERemoteProcessResolverScheduleWithRunLoop(_ ref: AERemoteProcessResolverRef, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!, _ callback: AERemoteProcessResolverCallback!, _ ctx: UnsafePointer<AERemoteProcessResolverContext>) ``` |

Modified [AERemoveCoercionHandler(_: DescType, _: DescType, _: AECoercionHandlerUPP!, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1441907-aeremovecoercionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func AERemoveCoercionHandler(_ fromType: DescType, _ toType: DescType, _ handler: AECoercionHandlerUPP, _ isSysHandler: Boolean) -> OSErr ``` |
| To | ``` func AERemoveCoercionHandler(_ fromType: DescType, _ toType: DescType, _ handler: AECoercionHandlerUPP!, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AERemoveEventHandler(_: AEEventClass, _: AEEventID, _: AEEventHandlerUPP!, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1445239-aeremoveeventhandler)

|  | Declaration |
| --- | --- |
| From | ``` func AERemoveEventHandler(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ handler: AEEventHandlerUPP, _ isSysHandler: Boolean) -> OSErr ``` |
| To | ``` func AERemoveEventHandler(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ handler: AEEventHandlerUPP!, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AERemoveObjectAccessor(_: DescType, _: DescType, _: OSLAccessorUPP!, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1442552-aeremoveobjectaccessor)

|  | Declaration |
| --- | --- |
| From | ``` func AERemoveObjectAccessor(_ desiredClass: DescType, _ containerType: DescType, _ theAccessor: OSLAccessorUPP, _ isSysHandler: Boolean) -> OSErr ``` |
| To | ``` func AERemoveObjectAccessor(_ desiredClass: DescType, _ containerType: DescType, _ theAccessor: OSLAccessorUPP!, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AERemoveSpecialHandler(_: AEKeyword, _: AEEventHandlerUPP!, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1447960-aeremovespecialhandler)

|  | Declaration |
| --- | --- |
| From | ``` func AERemoveSpecialHandler(_ functionClass: AEKeyword, _ handler: AEEventHandlerUPP, _ isSysHandler: Boolean) -> OSErr ``` |
| To | ``` func AERemoveSpecialHandler(_ functionClass: AEKeyword, _ handler: AEEventHandlerUPP!, _ isSysHandler: Bool) -> OSErr ``` |

Modified [AESetObjectCallbacks(_: OSLCompareUPP!, _: OSLCountUPP!, _: OSLDisposeTokenUPP!, _: OSLGetMarkTokenUPP!, _: OSLMarkUPP!, _: OSLAdjustMarksUPP!, _: OSLGetErrDescUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1447756-aesetobjectcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` func AESetObjectCallbacks(_ myCompareProc: OSLCompareUPP, _ myCountProc: OSLCountUPP, _ myDisposeTokenProc: OSLDisposeTokenUPP, _ myGetMarkTokenProc: OSLGetMarkTokenUPP, _ myMarkProc: OSLMarkUPP, _ myAdjustMarksProc: OSLAdjustMarksUPP, _ myGetErrDescProcPtr: OSLGetErrDescUPP) -> OSErr ``` |
| To | ``` func AESetObjectCallbacks(_ myCompareProc: OSLCompareUPP!, _ myCountProc: OSLCountUPP!, _ myDisposeTokenProc: OSLDisposeTokenUPP!, _ myGetMarkTokenProc: OSLGetMarkTokenUPP!, _ myMarkProc: OSLMarkUPP!, _ myAdjustMarksProc: OSLAdjustMarksUPP!, _ myGetErrDescProcPtr: OSLGetErrDescUPP!) -> OSErr ``` |

Modified [CreateCompDescriptor(_: DescType, _: UnsafeMutablePointer<AEDesc>, _: UnsafeMutablePointer<AEDesc>, _: Bool, _: UnsafeMutablePointer<AEDesc>) -> OSErr](https://developer.apple.com/documentation/coreservices/1449155-createcompdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` func CreateCompDescriptor(_ comparisonOperator: DescType, _ operand1: UnsafeMutablePointer<AEDesc>, _ operand2: UnsafeMutablePointer<AEDesc>, _ disposeInputs: Boolean, _ theDescriptor: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func CreateCompDescriptor(_ comparisonOperator: DescType, _ operand1: UnsafeMutablePointer<AEDesc>, _ operand2: UnsafeMutablePointer<AEDesc>, _ disposeInputs: Bool, _ theDescriptor: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |

Modified [CreateLogicalDescriptor(_: UnsafeMutablePointer<AEDescList>, _: DescType, _: Bool, _: UnsafeMutablePointer<AEDesc>) -> OSErr](https://developer.apple.com/documentation/coreservices/1445212-createlogicaldescriptor)

|  | Declaration |
| --- | --- |
| From | ``` func CreateLogicalDescriptor(_ theLogicalTerms: UnsafeMutablePointer<AEDescList>, _ theLogicOperator: DescType, _ disposeInputs: Boolean, _ theDescriptor: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func CreateLogicalDescriptor(_ theLogicalTerms: UnsafeMutablePointer<AEDescList>, _ theLogicOperator: DescType, _ disposeInputs: Bool, _ theDescriptor: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |

Modified [CreateObjSpecifier(_: DescType, _: UnsafeMutablePointer<AEDesc>, _: DescType, _: UnsafeMutablePointer<AEDesc>, _: Bool, _: UnsafeMutablePointer<AEDesc>) -> OSErr](https://developer.apple.com/documentation/coreservices/1450244-createobjspecifier)

|  | Declaration |
| --- | --- |
| From | ``` func CreateObjSpecifier(_ desiredClass: DescType, _ theContainer: UnsafeMutablePointer<AEDesc>, _ keyForm: DescType, _ keyData: UnsafeMutablePointer<AEDesc>, _ disposeInputs: Boolean, _ objSpecifier: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func CreateObjSpecifier(_ desiredClass: DescType, _ theContainer: UnsafeMutablePointer<AEDesc>, _ keyForm: DescType, _ keyData: UnsafeMutablePointer<AEDesc>, _ disposeInputs: Bool, _ objSpecifier: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |

Modified [CreateRangeDescriptor(_: UnsafeMutablePointer<AEDesc>, _: UnsafeMutablePointer<AEDesc>, _: Bool, _: UnsafeMutablePointer<AEDesc>) -> OSErr](https://developer.apple.com/documentation/coreservices/1444087-createrangedescriptor)

|  | Declaration |
| --- | --- |
| From | ``` func CreateRangeDescriptor(_ rangeStart: UnsafeMutablePointer<AEDesc>, _ rangeStop: UnsafeMutablePointer<AEDesc>, _ disposeInputs: Boolean, _ theDescriptor: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |
| To | ``` func CreateRangeDescriptor(_ rangeStart: UnsafeMutablePointer<AEDesc>, _ rangeStop: UnsafeMutablePointer<AEDesc>, _ disposeInputs: Bool, _ theDescriptor: UnsafeMutablePointer<AEDesc>) -> OSErr ``` |

Modified [CSBackupIsItemExcluded(_: CFURL!, _: UnsafeMutablePointer<DarwinBoolean>) -> Bool](https://developer.apple.com/documentation/coreservices/1443602-csbackupisitemexcluded)

|  | Declaration |
| --- | --- |
| From | ``` func CSBackupIsItemExcluded(_ item: CFURL!, _ excludeByPath: UnsafeMutablePointer<Boolean>) -> Boolean ``` |
| To | ``` func CSBackupIsItemExcluded(_ item: CFURL!, _ excludeByPath: UnsafeMutablePointer<DarwinBoolean>) -> Bool ``` |

Modified [CSBackupSetItemExcluded(_: CFURL!, _: Bool, _: Bool) -> OSStatus](https://developer.apple.com/documentation/coreservices/1445043-csbackupsetitemexcluded)

|  | Declaration |
| --- | --- |
| From | ``` func CSBackupSetItemExcluded(_ item: CFURL!, _ exclude: Boolean, _ excludeByPath: Boolean) -> OSStatus ``` |
| To | ``` func CSBackupSetItemExcluded(_ item: CFURL!, _ exclude: Bool, _ excludeByPath: Bool) -> OSStatus ``` |

Modified [CSDiskSpaceRecoveryCallback](https://developer.apple.com/documentation/coreservices/csdiskspacerecoverycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CSDiskSpaceRecoveryCallback = (Boolean, UInt64, CFError!) -> Void ``` |
| To | ``` typealias CSDiskSpaceRecoveryCallback = (Bool, UInt64, CFError!) -> Void ``` |

Modified [CSIdentityAuthenticateUsingPassword(_: CSIdentity!, _: CFString!) -> Bool](https://developer.apple.com/documentation/coreservices/1449855-csidentityauthenticateusingpassw)

|  | Declaration |
| --- | --- |
| From | ``` func CSIdentityAuthenticateUsingPassword(_ user: CSIdentity!, _ password: CFString!) -> Boolean ``` |
| To | ``` func CSIdentityAuthenticateUsingPassword(_ user: CSIdentity!, _ password: CFString!) -> Bool ``` |

Modified [CSIdentityCommit(_: CSIdentity!, _: AuthorizationRef, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/coreservices/1449575-csidentitycommit)

|  | Declaration |
| --- | --- |
| From | ``` func CSIdentityCommit(_ identity: CSIdentity!, _ authorization: AuthorizationRef, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` |
| To | ``` func CSIdentityCommit(_ identity: CSIdentity!, _ authorization: AuthorizationRef, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [CSIdentityCommitAsynchronously(_: CSIdentity!, _: UnsafePointer<CSIdentityClientContext>, _: CFRunLoop!, _: CFString!, _: AuthorizationRef) -> Bool](https://developer.apple.com/documentation/coreservices/1447936-csidentitycommitasynchronously)

|  | Declaration |
| --- | --- |
| From | ``` func CSIdentityCommitAsynchronously(_ identity: CSIdentity!, _ clientContext: UnsafePointer<CSIdentityClientContext>, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!, _ authorization: AuthorizationRef) -> Boolean ``` |
| To | ``` func CSIdentityCommitAsynchronously(_ identity: CSIdentity!, _ clientContext: UnsafePointer<CSIdentityClientContext>, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!, _ authorization: AuthorizationRef) -> Bool ``` |

Modified [CSIdentityIsCommitting(_: CSIdentity!) -> Bool](https://developer.apple.com/documentation/coreservices/1449734-csidentityiscommitting)

|  | Declaration |
| --- | --- |
| From | ``` func CSIdentityIsCommitting(_ identity: CSIdentity!) -> Boolean ``` |
| To | ``` func CSIdentityIsCommitting(_ identity: CSIdentity!) -> Bool ``` |

Modified [CSIdentityIsEnabled(_: CSIdentity!) -> Bool](https://developer.apple.com/documentation/coreservices/1443379-csidentityisenabled)

|  | Declaration |
| --- | --- |
| From | ``` func CSIdentityIsEnabled(_ user: CSIdentity!) -> Boolean ``` |
| To | ``` func CSIdentityIsEnabled(_ user: CSIdentity!) -> Bool ``` |

Modified [CSIdentityIsHidden(_: CSIdentity!) -> Bool](https://developer.apple.com/documentation/coreservices/1449476-csidentityishidden)

|  | Declaration |
| --- | --- |
| From | ``` func CSIdentityIsHidden(_ identity: CSIdentity!) -> Boolean ``` |
| To | ``` func CSIdentityIsHidden(_ identity: CSIdentity!) -> Bool ``` |

Modified [CSIdentityIsMemberOfGroup(_: CSIdentity!, _: CSIdentity!) -> Bool](https://developer.apple.com/documentation/coreservices/1449237-csidentityismemberofgroup)

|  | Declaration |
| --- | --- |
| From | ``` func CSIdentityIsMemberOfGroup(_ identity: CSIdentity!, _ group: CSIdentity!) -> Boolean ``` |
| To | ``` func CSIdentityIsMemberOfGroup(_ identity: CSIdentity!, _ group: CSIdentity!) -> Bool ``` |

Modified [CSIdentityQueryExecute(_: CSIdentityQuery!, _: CSIdentityQueryFlags, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/coreservices/1429041-csidentityqueryexecute)

|  | Declaration |
| --- | --- |
| From | ``` func CSIdentityQueryExecute(_ query: CSIdentityQuery!, _ flags: CSIdentityQueryFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` |
| To | ``` func CSIdentityQueryExecute(_ query: CSIdentityQuery!, _ flags: CSIdentityQueryFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [CSIdentityQueryExecuteAsynchronously(_: CSIdentityQuery!, _: CSIdentityQueryFlags, _: UnsafePointer<CSIdentityQueryClientContext>, _: CFRunLoop!, _: CFString!) -> Bool](https://developer.apple.com/documentation/coreservices/1429011-csidentityqueryexecuteasynchrono)

|  | Declaration |
| --- | --- |
| From | ``` func CSIdentityQueryExecuteAsynchronously(_ query: CSIdentityQuery!, _ flags: CSIdentityQueryFlags, _ clientContext: UnsafePointer<CSIdentityQueryClientContext>, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) -> Boolean ``` |
| To | ``` func CSIdentityQueryExecuteAsynchronously(_ query: CSIdentityQuery!, _ flags: CSIdentityQueryFlags, _ clientContext: UnsafePointer<CSIdentityQueryClientContext>, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) -> Bool ``` |

Modified [CSIdentityQueryReceiveEventCallback](https://developer.apple.com/documentation/coreservices/csidentityqueryreceiveeventcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CSIdentityQueryReceiveEventCallback = CFunctionPointer<((CSIdentityQuery!, CSIdentityQueryEvent, CFArray!, CFError!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CSIdentityQueryReceiveEventCallback = (CSIdentityQuery!, CSIdentityQueryEvent, CFArray!, CFError!, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CSIdentitySetIsEnabled(_: CSIdentity!, _: Bool)](https://developer.apple.com/documentation/coreservices/1443028-csidentitysetisenabled)

|  | Declaration |
| --- | --- |
| From | ``` func CSIdentitySetIsEnabled(_ user: CSIdentity!, _ isEnabled: Boolean) ``` |
| To | ``` func CSIdentitySetIsEnabled(_ user: CSIdentity!, _ isEnabled: Bool) ``` |

Modified [CSIdentityStatusUpdatedCallback](https://developer.apple.com/documentation/coreservices/csidentitystatusupdatedcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CSIdentityStatusUpdatedCallback = CFunctionPointer<((CSIdentity!, CFIndex, CFError!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CSIdentityStatusUpdatedCallback = (CSIdentity!, CFIndex, CFError!, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [DCSCopyTextDefinition(_: DCSDictionary?, _: CFString, _: CFRange) -> Unmanaged<CFString>?](https://developer.apple.com/documentation/coreservices/1446842-dcscopytextdefinition)

|  | Declaration |
| --- | --- |
| From | ``` func DCSCopyTextDefinition(_ dictionary: DCSDictionary!, _ textString: CFString!, _ range: CFRange) -> Unmanaged<CFString>! ``` |
| To | ``` func DCSCopyTextDefinition(_ dictionary: DCSDictionary?, _ textString: CFString, _ range: CFRange) -> Unmanaged<CFString>? ``` |

Modified [DCSGetTermRangeInString(_: DCSDictionary?, _: CFString, _: CFIndex) -> CFRange](https://developer.apple.com/documentation/coreservices/1450556-dcsgettermrangeinstring)

|  | Declaration |
| --- | --- |
| From | ``` func DCSGetTermRangeInString(_ dictionary: DCSDictionary!, _ textString: CFString!, _ offset: CFIndex) -> CFRange ``` |
| To | ``` func DCSGetTermRangeInString(_ dictionary: DCSDictionary?, _ textString: CFString, _ offset: CFIndex) -> CFRange ``` |

Modified [DisposeAECoerceDescUPP(_: AECoerceDescUPP!)](https://developer.apple.com/documentation/coreservices/1448721-disposeaecoercedescupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeAECoerceDescUPP(_ userUPP: AECoerceDescUPP) ``` |
| To | ``` func DisposeAECoerceDescUPP(_ userUPP: AECoerceDescUPP!) ``` |

Modified [DisposeAECoercePtrUPP(_: AECoercePtrUPP!)](https://developer.apple.com/documentation/coreservices/1450664-disposeaecoerceptrupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeAECoercePtrUPP(_ userUPP: AECoercePtrUPP) ``` |
| To | ``` func DisposeAECoercePtrUPP(_ userUPP: AECoercePtrUPP!) ``` |

Modified [DisposeAEDisposeExternalUPP(_: AEDisposeExternalUPP!)](https://developer.apple.com/documentation/coreservices/1447284-disposeaedisposeexternalupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeAEDisposeExternalUPP(_ userUPP: AEDisposeExternalUPP) ``` |
| To | ``` func DisposeAEDisposeExternalUPP(_ userUPP: AEDisposeExternalUPP!) ``` |

Modified [DisposeAEEventHandlerUPP(_: AEEventHandlerUPP!)](https://developer.apple.com/documentation/coreservices/1442066-disposeaeeventhandlerupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeAEEventHandlerUPP(_ userUPP: AEEventHandlerUPP) ``` |
| To | ``` func DisposeAEEventHandlerUPP(_ userUPP: AEEventHandlerUPP!) ``` |

Modified [DisposeOSLAccessorUPP(_: OSLAccessorUPP!)](https://developer.apple.com/documentation/coreservices/1444684-disposeoslaccessorupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeOSLAccessorUPP(_ userUPP: OSLAccessorUPP) ``` |
| To | ``` func DisposeOSLAccessorUPP(_ userUPP: OSLAccessorUPP!) ``` |

Modified [DisposeOSLAdjustMarksUPP(_: OSLAdjustMarksUPP!)](https://developer.apple.com/documentation/coreservices/1443940-disposeosladjustmarksupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeOSLAdjustMarksUPP(_ userUPP: OSLAdjustMarksUPP) ``` |
| To | ``` func DisposeOSLAdjustMarksUPP(_ userUPP: OSLAdjustMarksUPP!) ``` |

Modified [DisposeOSLCompareUPP(_: OSLCompareUPP!)](https://developer.apple.com/documentation/coreservices/1448398-disposeoslcompareupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeOSLCompareUPP(_ userUPP: OSLCompareUPP) ``` |
| To | ``` func DisposeOSLCompareUPP(_ userUPP: OSLCompareUPP!) ``` |

Modified [DisposeOSLCountUPP(_: OSLCountUPP!)](https://developer.apple.com/documentation/coreservices/1443984-disposeoslcountupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeOSLCountUPP(_ userUPP: OSLCountUPP) ``` |
| To | ``` func DisposeOSLCountUPP(_ userUPP: OSLCountUPP!) ``` |

Modified [DisposeOSLDisposeTokenUPP(_: OSLDisposeTokenUPP!)](https://developer.apple.com/documentation/coreservices/1442670-disposeosldisposetokenupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeOSLDisposeTokenUPP(_ userUPP: OSLDisposeTokenUPP) ``` |
| To | ``` func DisposeOSLDisposeTokenUPP(_ userUPP: OSLDisposeTokenUPP!) ``` |

Modified [DisposeOSLGetErrDescUPP(_: OSLGetErrDescUPP!)](https://developer.apple.com/documentation/coreservices/1446061-disposeoslgeterrdescupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeOSLGetErrDescUPP(_ userUPP: OSLGetErrDescUPP) ``` |
| To | ``` func DisposeOSLGetErrDescUPP(_ userUPP: OSLGetErrDescUPP!) ``` |

Modified [DisposeOSLGetMarkTokenUPP(_: OSLGetMarkTokenUPP!)](https://developer.apple.com/documentation/coreservices/1442377-disposeoslgetmarktokenupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeOSLGetMarkTokenUPP(_ userUPP: OSLGetMarkTokenUPP) ``` |
| To | ``` func DisposeOSLGetMarkTokenUPP(_ userUPP: OSLGetMarkTokenUPP!) ``` |

Modified [DisposeOSLMarkUPP(_: OSLMarkUPP!)](https://developer.apple.com/documentation/coreservices/1449253-disposeoslmarkupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeOSLMarkUPP(_ userUPP: OSLMarkUPP) ``` |
| To | ``` func DisposeOSLMarkUPP(_ userUPP: OSLMarkUPP!) ``` |

Modified [FSEventsCopyUUIDForDevice(_: dev_t) -> CFUUID?](https://developer.apple.com/documentation/coreservices/1444453-fseventscopyuuidfordevice)

|  | Declaration |
| --- | --- |
| From | ``` func FSEventsCopyUUIDForDevice(_ dev: dev_t) -> Unmanaged<CFUUID>! ``` |
| To | ``` func FSEventsCopyUUIDForDevice(_ dev: dev_t) -> CFUUID? ``` |

Modified [FSEventsPurgeEventsForDeviceUpToEventId(_: dev_t, _: FSEventStreamEventId) -> Bool](https://developer.apple.com/documentation/coreservices/1447985-fseventspurgeeventsfordeviceupto)

|  | Declaration |
| --- | --- |
| From | ``` func FSEventsPurgeEventsForDeviceUpToEventId(_ dev: dev_t, _ eventId: FSEventStreamEventId) -> Boolean ``` |
| To | ``` func FSEventsPurgeEventsForDeviceUpToEventId(_ dev: dev_t, _ eventId: FSEventStreamEventId) -> Bool ``` |

Modified [FSEventStreamCallback](https://developer.apple.com/documentation/coreservices/fseventstreamcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias FSEventStreamCallback = CFunctionPointer<((ConstFSEventStreamRef, UnsafeMutablePointer<Void>, Int, UnsafeMutablePointer<Void>, UnsafePointer<FSEventStreamEventFlags>, UnsafePointer<FSEventStreamEventId>) -> Void)> ``` |
| To | ``` typealias FSEventStreamCallback = (ConstFSEventStreamRef, UnsafeMutablePointer<Void>, Int, UnsafeMutablePointer<Void>, UnsafePointer<FSEventStreamEventFlags>, UnsafePointer<FSEventStreamEventId>) -> Void ``` |

Modified [FSEventStreamCopyDescription(_: ConstFSEventStreamRef) -> CFString](https://developer.apple.com/documentation/coreservices/1442676-fseventstreamcopydescription)

|  | Declaration |
| --- | --- |
| From | ``` func FSEventStreamCopyDescription(_ streamRef: ConstFSEventStreamRef) -> Unmanaged<CFString>! ``` |
| To | ``` func FSEventStreamCopyDescription(_ streamRef: ConstFSEventStreamRef) -> CFString ``` |

Modified [FSEventStreamCopyPathsBeingWatched(_: ConstFSEventStreamRef) -> CFArray](https://developer.apple.com/documentation/coreservices/1447917-fseventstreamcopypathsbeingwatch)

|  | Declaration |
| --- | --- |
| From | ``` func FSEventStreamCopyPathsBeingWatched(_ streamRef: ConstFSEventStreamRef) -> Unmanaged<CFArray>! ``` |
| To | ``` func FSEventStreamCopyPathsBeingWatched(_ streamRef: ConstFSEventStreamRef) -> CFArray ``` |

Modified [FSEventStreamCreate(_: CFAllocator?, _: FSEventStreamCallback, _: UnsafeMutablePointer<FSEventStreamContext>, _: CFArray, _: FSEventStreamEventId, _: CFTimeInterval, _: FSEventStreamCreateFlags) -> FSEventStreamRef](https://developer.apple.com/documentation/coreservices/1443980-fseventstreamcreate)

|  | Declaration |
| --- | --- |
| From | ``` func FSEventStreamCreate(_ allocator: CFAllocator!, _ callback: FSEventStreamCallback, _ context: UnsafeMutablePointer<FSEventStreamContext>, _ pathsToWatch: CFArray!, _ sinceWhen: FSEventStreamEventId, _ latency: CFTimeInterval, _ flags: FSEventStreamCreateFlags) -> FSEventStreamRef ``` |
| To | ``` func FSEventStreamCreate(_ allocator: CFAllocator?, _ callback: FSEventStreamCallback, _ context: UnsafeMutablePointer<FSEventStreamContext>, _ pathsToWatch: CFArray, _ sinceWhen: FSEventStreamEventId, _ latency: CFTimeInterval, _ flags: FSEventStreamCreateFlags) -> FSEventStreamRef ``` |

Modified [FSEventStreamCreateRelativeToDevice(_: CFAllocator?, _: FSEventStreamCallback, _: UnsafeMutablePointer<FSEventStreamContext>, _: dev_t, _: CFArray, _: FSEventStreamEventId, _: CFTimeInterval, _: FSEventStreamCreateFlags) -> FSEventStreamRef](https://developer.apple.com/documentation/coreservices/1447341-fseventstreamcreaterelativetodev)

|  | Declaration |
| --- | --- |
| From | ``` func FSEventStreamCreateRelativeToDevice(_ allocator: CFAllocator!, _ callback: FSEventStreamCallback, _ context: UnsafeMutablePointer<FSEventStreamContext>, _ deviceToWatch: dev_t, _ pathsToWatchRelativeToDevice: CFArray!, _ sinceWhen: FSEventStreamEventId, _ latency: CFTimeInterval, _ flags: FSEventStreamCreateFlags) -> FSEventStreamRef ``` |
| To | ``` func FSEventStreamCreateRelativeToDevice(_ allocator: CFAllocator?, _ callback: FSEventStreamCallback, _ context: UnsafeMutablePointer<FSEventStreamContext>, _ deviceToWatch: dev_t, _ pathsToWatchRelativeToDevice: CFArray, _ sinceWhen: FSEventStreamEventId, _ latency: CFTimeInterval, _ flags: FSEventStreamCreateFlags) -> FSEventStreamRef ``` |

Modified [FSEventStreamScheduleWithRunLoop(_: FSEventStreamRef, _: CFRunLoop, _: CFString)](https://developer.apple.com/documentation/coreservices/1447824-fseventstreamschedulewithrunloop)

|  | Declaration |
| --- | --- |
| From | ``` func FSEventStreamScheduleWithRunLoop(_ streamRef: FSEventStreamRef, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |
| To | ``` func FSEventStreamScheduleWithRunLoop(_ streamRef: FSEventStreamRef, _ runLoop: CFRunLoop, _ runLoopMode: CFString) ``` |

Modified [FSEventStreamSetDispatchQueue(_: FSEventStreamRef, _: dispatch_queue_t?)](https://developer.apple.com/documentation/coreservices/1444164-fseventstreamsetdispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` func FSEventStreamSetDispatchQueue(_ streamRef: FSEventStreamRef, _ q: dispatch_queue_t!) ``` |
| To | ``` func FSEventStreamSetDispatchQueue(_ streamRef: FSEventStreamRef, _ q: dispatch_queue_t?) ``` |

Modified [FSEventStreamSetExclusionPaths(_: FSEventStreamRef, _: CFArray) -> Bool](https://developer.apple.com/documentation/coreservices/1444666-fseventstreamsetexclusionpaths)

|  | Declaration |
| --- | --- |
| From | ``` func FSEventStreamSetExclusionPaths(_ streamRef: FSEventStreamRef, _ pathsToExclude: CFArray!) -> Boolean ``` |
| To | ``` func FSEventStreamSetExclusionPaths(_ streamRef: FSEventStreamRef, _ pathsToExclude: CFArray) -> Bool ``` |

Modified [FSEventStreamStart(_: FSEventStreamRef) -> Bool](https://developer.apple.com/documentation/coreservices/1448000-fseventstreamstart)

|  | Declaration |
| --- | --- |
| From | ``` func FSEventStreamStart(_ streamRef: FSEventStreamRef) -> Boolean ``` |
| To | ``` func FSEventStreamStart(_ streamRef: FSEventStreamRef) -> Bool ``` |

Modified [FSEventStreamUnscheduleFromRunLoop(_: FSEventStreamRef, _: CFRunLoop, _: CFString)](https://developer.apple.com/documentation/coreservices/1441982-fseventstreamunschedulefromrunlo)

|  | Declaration |
| --- | --- |
| From | ``` func FSEventStreamUnscheduleFromRunLoop(_ streamRef: FSEventStreamRef, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |
| To | ``` func FSEventStreamUnscheduleFromRunLoop(_ streamRef: FSEventStreamRef, _ runLoop: CFRunLoop, _ runLoopMode: CFString) ``` |

Modified [GetCustomIconsEnabled(_: Int16, _: UnsafeMutablePointer<DarwinBoolean>) -> OSErr](https://developer.apple.com/documentation/coreservices/1442255-getcustomiconsenabled)

|  | Declaration |
| --- | --- |
| From | ``` func GetCustomIconsEnabled(_ vRefNum: Int16, _ customIconsEnabled: UnsafeMutablePointer<Boolean>) -> OSErr ``` |
| To | ``` func GetCustomIconsEnabled(_ vRefNum: Int16, _ customIconsEnabled: UnsafeMutablePointer<DarwinBoolean>) -> OSErr ``` |

Modified [InvokeAECoerceDescUPP(_: UnsafePointer<AEDesc>, _: DescType, _: SRefCon, _: UnsafeMutablePointer<AEDesc>, _: AECoerceDescUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1445450-invokeaecoercedescupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeAECoerceDescUPP(_ fromDesc: UnsafePointer<AEDesc>, _ toType: DescType, _ handlerRefcon: SRefCon, _ toDesc: UnsafeMutablePointer<AEDesc>, _ userUPP: AECoerceDescUPP) -> OSErr ``` |
| To | ``` func InvokeAECoerceDescUPP(_ fromDesc: UnsafePointer<AEDesc>, _ toType: DescType, _ handlerRefcon: SRefCon, _ toDesc: UnsafeMutablePointer<AEDesc>, _ userUPP: AECoerceDescUPP!) -> OSErr ``` |

Modified [InvokeAECoercePtrUPP(_: DescType, _: UnsafePointer<Void>, _: Size, _: DescType, _: SRefCon, _: UnsafeMutablePointer<AEDesc>, _: AECoercePtrUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1447079-invokeaecoerceptrupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeAECoercePtrUPP(_ typeCode: DescType, _ dataPtr: UnsafePointer<Void>, _ dataSize: Size, _ toType: DescType, _ handlerRefcon: SRefCon, _ result: UnsafeMutablePointer<AEDesc>, _ userUPP: AECoercePtrUPP) -> OSErr ``` |
| To | ``` func InvokeAECoercePtrUPP(_ typeCode: DescType, _ dataPtr: UnsafePointer<Void>, _ dataSize: Size, _ toType: DescType, _ handlerRefcon: SRefCon, _ result: UnsafeMutablePointer<AEDesc>, _ userUPP: AECoercePtrUPP!) -> OSErr ``` |

Modified [InvokeAEDisposeExternalUPP(_: UnsafePointer<Void>, _: Size, _: SRefCon, _: AEDisposeExternalUPP!)](https://developer.apple.com/documentation/coreservices/1441717-invokeaedisposeexternalupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeAEDisposeExternalUPP(_ dataPtr: UnsafePointer<Void>, _ dataLength: Size, _ refcon: SRefCon, _ userUPP: AEDisposeExternalUPP) ``` |
| To | ``` func InvokeAEDisposeExternalUPP(_ dataPtr: UnsafePointer<Void>, _ dataLength: Size, _ refcon: SRefCon, _ userUPP: AEDisposeExternalUPP!) ``` |

Modified [InvokeAEEventHandlerUPP(_: UnsafePointer<AppleEvent>, _: UnsafeMutablePointer<AppleEvent>, _: SRefCon, _: AEEventHandlerUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1446585-invokeaeeventhandlerupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeAEEventHandlerUPP(_ theAppleEvent: UnsafePointer<AppleEvent>, _ reply: UnsafeMutablePointer<AppleEvent>, _ handlerRefcon: SRefCon, _ userUPP: AEEventHandlerUPP) -> OSErr ``` |
| To | ``` func InvokeAEEventHandlerUPP(_ theAppleEvent: UnsafePointer<AppleEvent>, _ reply: UnsafeMutablePointer<AppleEvent>, _ handlerRefcon: SRefCon, _ userUPP: AEEventHandlerUPP!) -> OSErr ``` |

Modified [InvokeOSLAccessorUPP(_: DescType, _: UnsafePointer<AEDesc>, _: DescType, _: DescType, _: UnsafePointer<AEDesc>, _: UnsafeMutablePointer<AEDesc>, _: SRefCon, _: OSLAccessorUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1448978-invokeoslaccessorupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeOSLAccessorUPP(_ desiredClass: DescType, _ container: UnsafePointer<AEDesc>, _ containerClass: DescType, _ form: DescType, _ selectionData: UnsafePointer<AEDesc>, _ value: UnsafeMutablePointer<AEDesc>, _ accessorRefcon: SRefCon, _ userUPP: OSLAccessorUPP) -> OSErr ``` |
| To | ``` func InvokeOSLAccessorUPP(_ desiredClass: DescType, _ container: UnsafePointer<AEDesc>, _ containerClass: DescType, _ form: DescType, _ selectionData: UnsafePointer<AEDesc>, _ value: UnsafeMutablePointer<AEDesc>, _ accessorRefcon: SRefCon, _ userUPP: OSLAccessorUPP!) -> OSErr ``` |

Modified [InvokeOSLAdjustMarksUPP(_: Int, _: Int, _: UnsafePointer<AEDesc>, _: OSLAdjustMarksUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1448506-invokeosladjustmarksupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeOSLAdjustMarksUPP(_ newStart: Int, _ newStop: Int, _ markToken: UnsafePointer<AEDesc>, _ userUPP: OSLAdjustMarksUPP) -> OSErr ``` |
| To | ``` func InvokeOSLAdjustMarksUPP(_ newStart: Int, _ newStop: Int, _ markToken: UnsafePointer<AEDesc>, _ userUPP: OSLAdjustMarksUPP!) -> OSErr ``` |

Modified [InvokeOSLCompareUPP(_: DescType, _: UnsafePointer<AEDesc>, _: UnsafePointer<AEDesc>, _: UnsafeMutablePointer<DarwinBoolean>, _: OSLCompareUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1443110-invokeoslcompareupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeOSLCompareUPP(_ oper: DescType, _ obj1: UnsafePointer<AEDesc>, _ obj2: UnsafePointer<AEDesc>, _ result: UnsafeMutablePointer<Boolean>, _ userUPP: OSLCompareUPP) -> OSErr ``` |
| To | ``` func InvokeOSLCompareUPP(_ oper: DescType, _ obj1: UnsafePointer<AEDesc>, _ obj2: UnsafePointer<AEDesc>, _ result: UnsafeMutablePointer<DarwinBoolean>, _ userUPP: OSLCompareUPP!) -> OSErr ``` |

Modified [InvokeOSLCountUPP(_: DescType, _: DescType, _: UnsafePointer<AEDesc>, _: UnsafeMutablePointer<Int>, _: OSLCountUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1448030-invokeoslcountupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeOSLCountUPP(_ desiredType: DescType, _ containerClass: DescType, _ container: UnsafePointer<AEDesc>, _ result: UnsafeMutablePointer<Int>, _ userUPP: OSLCountUPP) -> OSErr ``` |
| To | ``` func InvokeOSLCountUPP(_ desiredType: DescType, _ containerClass: DescType, _ container: UnsafePointer<AEDesc>, _ result: UnsafeMutablePointer<Int>, _ userUPP: OSLCountUPP!) -> OSErr ``` |

Modified [InvokeOSLDisposeTokenUPP(_: UnsafeMutablePointer<AEDesc>, _: OSLDisposeTokenUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1443963-invokeosldisposetokenupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeOSLDisposeTokenUPP(_ unneededToken: UnsafeMutablePointer<AEDesc>, _ userUPP: OSLDisposeTokenUPP) -> OSErr ``` |
| To | ``` func InvokeOSLDisposeTokenUPP(_ unneededToken: UnsafeMutablePointer<AEDesc>, _ userUPP: OSLDisposeTokenUPP!) -> OSErr ``` |

Modified [InvokeOSLGetErrDescUPP(_: UnsafeMutablePointer<UnsafeMutablePointer<AEDesc>>, _: OSLGetErrDescUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1448420-invokeoslgeterrdescupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeOSLGetErrDescUPP(_ appDescPtr: UnsafeMutablePointer<UnsafeMutablePointer<AEDesc>>, _ userUPP: OSLGetErrDescUPP) -> OSErr ``` |
| To | ``` func InvokeOSLGetErrDescUPP(_ appDescPtr: UnsafeMutablePointer<UnsafeMutablePointer<AEDesc>>, _ userUPP: OSLGetErrDescUPP!) -> OSErr ``` |

Modified [InvokeOSLGetMarkTokenUPP(_: UnsafePointer<AEDesc>, _: DescType, _: UnsafeMutablePointer<AEDesc>, _: OSLGetMarkTokenUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1441894-invokeoslgetmarktokenupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeOSLGetMarkTokenUPP(_ dContainerToken: UnsafePointer<AEDesc>, _ containerClass: DescType, _ result: UnsafeMutablePointer<AEDesc>, _ userUPP: OSLGetMarkTokenUPP) -> OSErr ``` |
| To | ``` func InvokeOSLGetMarkTokenUPP(_ dContainerToken: UnsafePointer<AEDesc>, _ containerClass: DescType, _ result: UnsafeMutablePointer<AEDesc>, _ userUPP: OSLGetMarkTokenUPP!) -> OSErr ``` |

Modified [InvokeOSLMarkUPP(_: UnsafePointer<AEDesc>, _: UnsafePointer<AEDesc>, _: Int, _: OSLMarkUPP!) -> OSErr](https://developer.apple.com/documentation/coreservices/1447444-invokeoslmarkupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeOSLMarkUPP(_ dToken: UnsafePointer<AEDesc>, _ markToken: UnsafePointer<AEDesc>, _ index: Int, _ userUPP: OSLMarkUPP) -> OSErr ``` |
| To | ``` func InvokeOSLMarkUPP(_ dToken: UnsafePointer<AEDesc>, _ markToken: UnsafePointer<AEDesc>, _ index: Int, _ userUPP: OSLMarkUPP!) -> OSErr ``` |

Modified [IsDataAvailableInIconRef(_: OSType, _: IconRef) -> Bool](https://developer.apple.com/documentation/coreservices/1446627-isdataavailableiniconref)

|  | Declaration |
| --- | --- |
| From | ``` func IsDataAvailableInIconRef(_ inIconKind: OSType, _ inIconRef: IconRef) -> Boolean ``` |
| To | ``` func IsDataAvailableInIconRef(_ inIconKind: OSType, _ inIconRef: IconRef) -> Bool ``` |

Modified [IsValidIconRef(_: IconRef) -> Bool](https://developer.apple.com/documentation/coreservices/1450233-isvalidiconref)

|  | Declaration |
| --- | --- |
| From | ``` func IsValidIconRef(_ theIconRef: IconRef) -> Boolean ``` |
| To | ``` func IsValidIconRef(_ theIconRef: IconRef) -> Bool ``` |

Modified [kLSAppDoesNotClaimTypeErr](https://developer.apple.com/documentation/coreservices/1469236-anonymous/klsappdoesnotclaimtypeerr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSAppDoesNotClaimTypeErr: Int { get } ``` |
| To | ``` var kLSAppDoesNotClaimTypeErr: OSStatus { get } ``` |

Modified [kLSAppDoesNotSupportSchemeWarning](https://developer.apple.com/documentation/coreservices/klsappdoesnotsupportschemewarning)

|  | Declaration |
| --- | --- |
| From | ``` var kLSAppDoesNotSupportSchemeWarning: Int { get } ``` |
| To | ``` var kLSAppDoesNotSupportSchemeWarning: OSStatus { get } ``` |

Modified [kLSAppInTrashErr](https://developer.apple.com/documentation/coreservices/1469236-anonymous/klsappintrasherr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSAppInTrashErr: Int { get } ``` |
| To | ``` var kLSAppInTrashErr: OSStatus { get } ``` |

Modified [kLSApplicationNotFoundErr](https://developer.apple.com/documentation/coreservices/klsapplicationnotfounderr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSApplicationNotFoundErr: Int { get } ``` |
| To | ``` var kLSApplicationNotFoundErr: OSStatus { get } ``` |

Modified [kLSAttributeNotFoundErr](https://developer.apple.com/documentation/coreservices/klsattributenotfounderr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSAttributeNotFoundErr: Int { get } ``` |
| To | ``` var kLSAttributeNotFoundErr: OSStatus { get } ``` |

Modified [kLSAttributeNotSettableErr](https://developer.apple.com/documentation/coreservices/1469236-anonymous/klsattributenotsettableerr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSAttributeNotSettableErr: Int { get } ``` |
| To | ``` var kLSAttributeNotSettableErr: OSStatus { get } ``` |

Modified [kLSCannotSetInfoErr](https://developer.apple.com/documentation/coreservices/klscannotsetinfoerr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSCannotSetInfoErr: Int { get } ``` |
| To | ``` var kLSCannotSetInfoErr: OSStatus { get } ``` |

Modified [kLSDataErr](https://developer.apple.com/documentation/coreservices/klsdataerr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSDataErr: Int { get } ``` |
| To | ``` var kLSDataErr: OSStatus { get } ``` |

Modified [kLSDataTooOldErr](https://developer.apple.com/documentation/coreservices/klsdatatooolderr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSDataTooOldErr: Int { get } ``` |
| To | ``` var kLSDataTooOldErr: OSStatus { get } ``` |

Modified [kLSDataUnavailableErr](https://developer.apple.com/documentation/coreservices/klsdataunavailableerr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSDataUnavailableErr: Int { get } ``` |
| To | ``` var kLSDataUnavailableErr: OSStatus { get } ``` |

Modified [kLSExecutableIncorrectFormat](https://developer.apple.com/documentation/coreservices/1469236-anonymous/klsexecutableincorrectformat)

|  | Declaration |
| --- | --- |
| From | ``` var kLSExecutableIncorrectFormat: Int { get } ``` |
| To | ``` var kLSExecutableIncorrectFormat: OSStatus { get } ``` |

Modified [kLSIncompatibleApplicationVersionErr](https://developer.apple.com/documentation/coreservices/1469236-anonymous/klsincompatibleapplicationversionerr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSIncompatibleApplicationVersionErr: Int { get } ``` |
| To | ``` var kLSIncompatibleApplicationVersionErr: OSStatus { get } ``` |

Modified [kLSIncompatibleSystemVersionErr](https://developer.apple.com/documentation/coreservices/1469236-anonymous/klsincompatiblesystemversionerr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSIncompatibleSystemVersionErr: Int { get } ``` |
| To | ``` var kLSIncompatibleSystemVersionErr: OSStatus { get } ``` |

Modified [kLSLaunchInClassic](https://developer.apple.com/documentation/coreservices/1645929-anonymous/klslaunchinclassic)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.0 | OS X 10.11 |

Modified [kLSLaunchInProgressErr](https://developer.apple.com/documentation/coreservices/1469236-anonymous/klslaunchinprogresserr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSLaunchInProgressErr: Int { get } ``` |
| To | ``` var kLSLaunchInProgressErr: OSStatus { get } ``` |

Modified [kLSLaunchStartClassic](https://developer.apple.com/documentation/coreservices/1645929-anonymous/klslaunchstartclassic)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.0 | OS X 10.11 |

Modified [kLSMultipleSessionsNotSupportedErr](https://developer.apple.com/documentation/coreservices/1469236-anonymous/klsmultiplesessionsnotsupportederr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSMultipleSessionsNotSupportedErr: Int { get } ``` |
| To | ``` var kLSMultipleSessionsNotSupportedErr: OSStatus { get } ``` |

Modified [kLSNoClassicEnvironmentErr](https://developer.apple.com/documentation/coreservices/1469236-anonymous/klsnoclassicenvironmenterr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSNoClassicEnvironmentErr: Int { get } ``` |
| To | ``` var kLSNoClassicEnvironmentErr: OSStatus { get } ``` |

Modified [kLSNoExecutableErr](https://developer.apple.com/documentation/coreservices/klsnoexecutableerr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSNoExecutableErr: Int { get } ``` |
| To | ``` var kLSNoExecutableErr: OSStatus { get } ``` |

Modified [kLSNoLaunchPermissionErr](https://developer.apple.com/documentation/coreservices/klsnolaunchpermissionerr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSNoLaunchPermissionErr: Int { get } ``` |
| To | ``` var kLSNoLaunchPermissionErr: OSStatus { get } ``` |

Modified [kLSNoRegistrationInfoErr](https://developer.apple.com/documentation/coreservices/1469236-anonymous/klsnoregistrationinfoerr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSNoRegistrationInfoErr: Int { get } ``` |
| To | ``` var kLSNoRegistrationInfoErr: OSStatus { get } ``` |

Modified [kLSNoRosettaEnvironmentErr](https://developer.apple.com/documentation/coreservices/1469236-anonymous/klsnorosettaenvironmenterr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSNoRosettaEnvironmentErr: Int { get } ``` |
| To | ``` var kLSNoRosettaEnvironmentErr: OSStatus { get } ``` |

Modified [kLSNotAnApplicationErr](https://developer.apple.com/documentation/coreservices/klsnotanapplicationerr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSNotAnApplicationErr: Int { get } ``` |
| To | ``` var kLSNotAnApplicationErr: OSStatus { get } ``` |

Modified [kLSNotInitializedErr](https://developer.apple.com/documentation/coreservices/klsnotinitializederr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSNotInitializedErr: Int { get } ``` |
| To | ``` var kLSNotInitializedErr: OSStatus { get } ``` |

Modified [kLSNotRegisteredErr](https://developer.apple.com/documentation/coreservices/1469236-anonymous/klsnotregisterederr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSNotRegisteredErr: Int { get } ``` |
| To | ``` var kLSNotRegisteredErr: OSStatus { get } ``` |

Modified [kLSQuarantineAgentBundleIdentifierKey](https://developer.apple.com/documentation/coreservices/klsquarantineagentbundleidentifierkey)

|  | Declaration |
| --- | --- |
| From | ``` let kLSQuarantineAgentBundleIdentifierKey: CFString! ``` |
| To | ``` let kLSQuarantineAgentBundleIdentifierKey: CFString ``` |

Modified [kLSQuarantineAgentNameKey](https://developer.apple.com/documentation/coreservices/klsquarantineagentnamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kLSQuarantineAgentNameKey: CFString! ``` |
| To | ``` let kLSQuarantineAgentNameKey: CFString ``` |

Modified [kLSQuarantineDataURLKey](https://developer.apple.com/documentation/coreservices/klsquarantinedataurlkey)

|  | Declaration |
| --- | --- |
| From | ``` let kLSQuarantineDataURLKey: CFString! ``` |
| To | ``` let kLSQuarantineDataURLKey: CFString ``` |

Modified [kLSQuarantineOriginURLKey](https://developer.apple.com/documentation/coreservices/klsquarantineoriginurlkey)

|  | Declaration |
| --- | --- |
| From | ``` let kLSQuarantineOriginURLKey: CFString! ``` |
| To | ``` let kLSQuarantineOriginURLKey: CFString ``` |

Modified [kLSQuarantineTimeStampKey](https://developer.apple.com/documentation/coreservices/klsquarantinetimestampkey)

|  | Declaration |
| --- | --- |
| From | ``` let kLSQuarantineTimeStampKey: CFString! ``` |
| To | ``` let kLSQuarantineTimeStampKey: CFString ``` |

Modified [kLSQuarantineTypeCalendarEventAttachment](https://developer.apple.com/documentation/coreservices/klsquarantinetypecalendareventattachment)

|  | Declaration |
| --- | --- |
| From | ``` let kLSQuarantineTypeCalendarEventAttachment: CFString! ``` |
| To | ``` let kLSQuarantineTypeCalendarEventAttachment: CFString ``` |

Modified [kLSQuarantineTypeEmailAttachment](https://developer.apple.com/documentation/coreservices/klsquarantinetypeemailattachment)

|  | Declaration |
| --- | --- |
| From | ``` let kLSQuarantineTypeEmailAttachment: CFString! ``` |
| To | ``` let kLSQuarantineTypeEmailAttachment: CFString ``` |

Modified [kLSQuarantineTypeInstantMessageAttachment](https://developer.apple.com/documentation/coreservices/klsquarantinetypeinstantmessageattachment)

|  | Declaration |
| --- | --- |
| From | ``` let kLSQuarantineTypeInstantMessageAttachment: CFString! ``` |
| To | ``` let kLSQuarantineTypeInstantMessageAttachment: CFString ``` |

Modified [kLSQuarantineTypeKey](https://developer.apple.com/documentation/coreservices/klsquarantinetypekey)

|  | Declaration |
| --- | --- |
| From | ``` let kLSQuarantineTypeKey: CFString! ``` |
| To | ``` let kLSQuarantineTypeKey: CFString ``` |

Modified [kLSQuarantineTypeOtherAttachment](https://developer.apple.com/documentation/coreservices/klsquarantinetypeotherattachment)

|  | Declaration |
| --- | --- |
| From | ``` let kLSQuarantineTypeOtherAttachment: CFString! ``` |
| To | ``` let kLSQuarantineTypeOtherAttachment: CFString ``` |

Modified [kLSQuarantineTypeOtherDownload](https://developer.apple.com/documentation/coreservices/klsquarantinetypeotherdownload)

|  | Declaration |
| --- | --- |
| From | ``` let kLSQuarantineTypeOtherDownload: CFString! ``` |
| To | ``` let kLSQuarantineTypeOtherDownload: CFString ``` |

Modified [kLSQuarantineTypeWebDownload](https://developer.apple.com/documentation/coreservices/klsquarantinetypewebdownload)

|  | Declaration |
| --- | --- |
| From | ``` let kLSQuarantineTypeWebDownload: CFString! ``` |
| To | ``` let kLSQuarantineTypeWebDownload: CFString ``` |

Modified [kLSServerCommunicationErr](https://developer.apple.com/documentation/coreservices/1469236-anonymous/klsservercommunicationerr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSServerCommunicationErr: Int { get } ``` |
| To | ``` var kLSServerCommunicationErr: OSStatus { get } ``` |

Modified [kLSSharedFileListFavoriteItems](https://developer.apple.com/documentation/coreservices/klssharedfilelistfavoriteitems)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kLSSharedFileListFavoriteVolumes](https://developer.apple.com/documentation/coreservices/klssharedfilelistfavoritevolumes)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kLSSharedFileListItemBeforeFirst](https://developer.apple.com/documentation/coreservices/klssharedfilelistitembeforefirst)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kLSSharedFileListItemHidden](https://developer.apple.com/documentation/coreservices/klssharedfilelistitemhidden)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kLSSharedFileListItemLast](https://developer.apple.com/documentation/coreservices/klssharedfilelistitemlast)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kLSSharedFileListLoginItemHidden](https://developer.apple.com/documentation/coreservices/klssharedfilelistloginitemhidden)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kLSSharedFileListRecentApplicationItems](https://developer.apple.com/documentation/coreservices/klssharedfilelistrecentapplicationitems)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kLSSharedFileListRecentDocumentItems](https://developer.apple.com/documentation/coreservices/klssharedfilelistrecentdocumentitems)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kLSSharedFileListRecentItemsMaxAmount](https://developer.apple.com/documentation/coreservices/klssharedfilelistrecentitemsmaxamount)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kLSSharedFileListRecentServerItems](https://developer.apple.com/documentation/coreservices/klssharedfilelistrecentserveritems)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kLSSharedFileListSessionLoginItems](https://developer.apple.com/documentation/coreservices/klssharedfilelistsessionloginitems)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kLSSharedFileListVolumesComputerVisible](https://developer.apple.com/documentation/coreservices/klssharedfilelistvolumescomputervisible)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kLSSharedFileListVolumesNetworkVisible](https://developer.apple.com/documentation/coreservices/klssharedfilelistvolumesnetworkvisible)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kLSUnknownCreator](https://developer.apple.com/documentation/coreservices/klsunknowncreator)

|  | Declaration |
| --- | --- |
| From | ``` var kLSUnknownCreator: Int { get } ``` |
| To | ``` var kLSUnknownCreator: OSType { get } ``` |

Modified [kLSUnknownErr](https://developer.apple.com/documentation/coreservices/1469236-anonymous/klsunknownerr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSUnknownErr: Int { get } ``` |
| To | ``` var kLSUnknownErr: OSStatus { get } ``` |

Modified [kLSUnknownType](https://developer.apple.com/documentation/coreservices/1469201-unknown_type_or_creator/klsunknowntype)

|  | Declaration |
| --- | --- |
| From | ``` var kLSUnknownType: Int { get } ``` |
| To | ``` var kLSUnknownType: OSType { get } ``` |

Modified [kLSUnknownTypeErr](https://developer.apple.com/documentation/coreservices/klsunknowntypeerr)

|  | Declaration |
| --- | --- |
| From | ``` var kLSUnknownTypeErr: Int { get } ``` |
| To | ``` var kLSUnknownTypeErr: OSStatus { get } ``` |

Modified [kUTExportedTypeDeclarationsKey](https://developer.apple.com/documentation/coreservices/kutexportedtypedeclarationskey)

|  | Declaration |
| --- | --- |
| From | ``` let kUTExportedTypeDeclarationsKey: CFString! ``` |
| To | ``` let kUTExportedTypeDeclarationsKey: CFString ``` |

Modified [kUTImportedTypeDeclarationsKey](https://developer.apple.com/documentation/coreservices/kutimportedtypedeclarationskey)

|  | Declaration |
| --- | --- |
| From | ``` let kUTImportedTypeDeclarationsKey: CFString! ``` |
| To | ``` let kUTImportedTypeDeclarationsKey: CFString ``` |

Modified [kUTTagClassFilenameExtension](https://developer.apple.com/documentation/coreservices/kuttagclassfilenameextension)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTagClassFilenameExtension: CFString! ``` |
| To | ``` let kUTTagClassFilenameExtension: CFString ``` |

Modified [kUTTagClassMIMEType](https://developer.apple.com/documentation/coreservices/kuttagclassmimetype)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTagClassMIMEType: CFString! ``` |
| To | ``` let kUTTagClassMIMEType: CFString ``` |

Modified [kUTTagClassNSPboardType](https://developer.apple.com/documentation/coreservices/kuttagclassnspboardtype)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTagClassNSPboardType: CFString! ``` |
| To | ``` let kUTTagClassNSPboardType: CFString ``` |

Modified [kUTTagClassOSType](https://developer.apple.com/documentation/coreservices/kuttagclassostype)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTagClassOSType: CFString! ``` |
| To | ``` let kUTTagClassOSType: CFString ``` |

Modified [kUTType3DContent](https://developer.apple.com/documentation/coreservices/kuttype3dcontent)

|  | Declaration |
| --- | --- |
| From | ``` let kUTType3DContent: CFString! ``` |
| To | ``` let kUTType3DContent: CFString ``` |

Modified [kUTTypeAliasFile](https://developer.apple.com/documentation/coreservices/kuttypealiasfile)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeAliasFile: CFString! ``` |
| To | ``` let kUTTypeAliasFile: CFString ``` |

Modified [kUTTypeAliasRecord](https://developer.apple.com/documentation/coreservices/kuttypealiasrecord)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeAliasRecord: CFString! ``` |
| To | ``` let kUTTypeAliasRecord: CFString ``` |

Modified [kUTTypeAppleICNS](https://developer.apple.com/documentation/coreservices/kuttypeappleicns)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeAppleICNS: CFString! ``` |
| To | ``` let kUTTypeAppleICNS: CFString ``` |

Modified [kUTTypeAppleProtectedMPEG4Audio](https://developer.apple.com/documentation/coreservices/kuttypeappleprotectedmpeg4audio)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeAppleProtectedMPEG4Audio: CFString! ``` |
| To | ``` let kUTTypeAppleProtectedMPEG4Audio: CFString ``` |

Modified [kUTTypeAppleProtectedMPEG4Video](https://developer.apple.com/documentation/coreservices/kuttypeappleprotectedmpeg4video)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeAppleProtectedMPEG4Video: CFString! ``` |
| To | ``` let kUTTypeAppleProtectedMPEG4Video: CFString ``` |

Modified [kUTTypeAppleScript](https://developer.apple.com/documentation/coreservices/kuttypeapplescript)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeAppleScript: CFString! ``` |
| To | ``` let kUTTypeAppleScript: CFString ``` |

Modified [kUTTypeApplication](https://developer.apple.com/documentation/coreservices/kuttypeapplication)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeApplication: CFString! ``` |
| To | ``` let kUTTypeApplication: CFString ``` |

Modified [kUTTypeApplicationBundle](https://developer.apple.com/documentation/coreservices/kuttypeapplicationbundle)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeApplicationBundle: CFString! ``` |
| To | ``` let kUTTypeApplicationBundle: CFString ``` |

Modified [kUTTypeApplicationFile](https://developer.apple.com/documentation/coreservices/kuttypeapplicationfile)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeApplicationFile: CFString! ``` |
| To | ``` let kUTTypeApplicationFile: CFString ``` |

Modified [kUTTypeArchive](https://developer.apple.com/documentation/coreservices/kuttypearchive)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeArchive: CFString! ``` |
| To | ``` let kUTTypeArchive: CFString ``` |

Modified [kUTTypeAssemblyLanguageSource](https://developer.apple.com/documentation/coreservices/kuttypeassemblylanguagesource)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeAssemblyLanguageSource: CFString! ``` |
| To | ``` let kUTTypeAssemblyLanguageSource: CFString ``` |

Modified [kUTTypeAudio](https://developer.apple.com/documentation/coreservices/kuttypeaudio)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeAudio: CFString! ``` |
| To | ``` let kUTTypeAudio: CFString ``` |

Modified [kUTTypeAudioInterchangeFileFormat](https://developer.apple.com/documentation/coreservices/kuttypeaudiointerchangefileformat)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeAudioInterchangeFileFormat: CFString! ``` |
| To | ``` let kUTTypeAudioInterchangeFileFormat: CFString ``` |

Modified [kUTTypeAudiovisualContent](https://developer.apple.com/documentation/coreservices/kuttypeaudiovisualcontent)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeAudiovisualContent: CFString! ``` |
| To | ``` let kUTTypeAudiovisualContent: CFString ``` |

Modified [kUTTypeAVIMovie](https://developer.apple.com/documentation/coreservices/kuttypeavimovie)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeAVIMovie: CFString! ``` |
| To | ``` let kUTTypeAVIMovie: CFString ``` |

Modified [kUTTypeBinaryPropertyList](https://developer.apple.com/documentation/coreservices/kuttypebinarypropertylist)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeBinaryPropertyList: CFString! ``` |
| To | ``` let kUTTypeBinaryPropertyList: CFString ``` |

Modified [kUTTypeBMP](https://developer.apple.com/documentation/coreservices/kuttypebmp)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeBMP: CFString! ``` |
| To | ``` let kUTTypeBMP: CFString ``` |

Modified [kUTTypeBookmark](https://developer.apple.com/documentation/coreservices/kuttypebookmark)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeBookmark: CFString! ``` |
| To | ``` let kUTTypeBookmark: CFString ``` |

Modified [kUTTypeBundle](https://developer.apple.com/documentation/coreservices/kuttypebundle)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeBundle: CFString! ``` |
| To | ``` let kUTTypeBundle: CFString ``` |

Modified [kUTTypeBzip2Archive](https://developer.apple.com/documentation/coreservices/kuttypebzip2archive)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeBzip2Archive: CFString! ``` |
| To | ``` let kUTTypeBzip2Archive: CFString ``` |

Modified [kUTTypeCalendarEvent](https://developer.apple.com/documentation/coreservices/kuttypecalendarevent)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeCalendarEvent: CFString! ``` |
| To | ``` let kUTTypeCalendarEvent: CFString ``` |

Modified [kUTTypeCHeader](https://developer.apple.com/documentation/coreservices/kuttypecheader)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeCHeader: CFString! ``` |
| To | ``` let kUTTypeCHeader: CFString ``` |

Modified [kUTTypeCommaSeparatedText](https://developer.apple.com/documentation/coreservices/kuttypecommaseparatedtext)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeCommaSeparatedText: CFString! ``` |
| To | ``` let kUTTypeCommaSeparatedText: CFString ``` |

Modified [kUTTypeCompositeContent](https://developer.apple.com/documentation/coreservices/kuttypecompositecontent)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeCompositeContent: CFString! ``` |
| To | ``` let kUTTypeCompositeContent: CFString ``` |

Modified [kUTTypeConformsToKey](https://developer.apple.com/documentation/coreservices/kuttypeconformstokey)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeConformsToKey: CFString! ``` |
| To | ``` let kUTTypeConformsToKey: CFString ``` |

Modified [kUTTypeContact](https://developer.apple.com/documentation/coreservices/kuttypecontact)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeContact: CFString! ``` |
| To | ``` let kUTTypeContact: CFString ``` |

Modified [kUTTypeContent](https://developer.apple.com/documentation/coreservices/kuttypecontent)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeContent: CFString! ``` |
| To | ``` let kUTTypeContent: CFString ``` |

Modified [kUTTypeCPlusPlusHeader](https://developer.apple.com/documentation/coreservices/kuttypecplusplusheader)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeCPlusPlusHeader: CFString! ``` |
| To | ``` let kUTTypeCPlusPlusHeader: CFString ``` |

Modified [kUTTypeCPlusPlusSource](https://developer.apple.com/documentation/coreservices/kuttypecplusplussource)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeCPlusPlusSource: CFString! ``` |
| To | ``` let kUTTypeCPlusPlusSource: CFString ``` |

Modified [kUTTypeCSource](https://developer.apple.com/documentation/coreservices/kuttypecsource)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeCSource: CFString! ``` |
| To | ``` let kUTTypeCSource: CFString ``` |

Modified [kUTTypeData](https://developer.apple.com/documentation/coreservices/kuttypedata)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeData: CFString! ``` |
| To | ``` let kUTTypeData: CFString ``` |

Modified [kUTTypeDatabase](https://developer.apple.com/documentation/coreservices/kuttypedatabase)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeDatabase: CFString! ``` |
| To | ``` let kUTTypeDatabase: CFString ``` |

Modified [kUTTypeDelimitedText](https://developer.apple.com/documentation/coreservices/kuttypedelimitedtext)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeDelimitedText: CFString! ``` |
| To | ``` let kUTTypeDelimitedText: CFString ``` |

Modified [kUTTypeDescriptionKey](https://developer.apple.com/documentation/coreservices/kuttypedescriptionkey)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeDescriptionKey: CFString! ``` |
| To | ``` let kUTTypeDescriptionKey: CFString ``` |

Modified [kUTTypeDirectory](https://developer.apple.com/documentation/coreservices/kuttypedirectory)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeDirectory: CFString! ``` |
| To | ``` let kUTTypeDirectory: CFString ``` |

Modified [kUTTypeDiskImage](https://developer.apple.com/documentation/coreservices/kuttypediskimage)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeDiskImage: CFString! ``` |
| To | ``` let kUTTypeDiskImage: CFString ``` |

Modified [kUTTypeElectronicPublication](https://developer.apple.com/documentation/coreservices/kuttypeelectronicpublication)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeElectronicPublication: CFString! ``` |
| To | ``` let kUTTypeElectronicPublication: CFString ``` |

Modified [kUTTypeEmailMessage](https://developer.apple.com/documentation/coreservices/kuttypeemailmessage)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeEmailMessage: CFString! ``` |
| To | ``` let kUTTypeEmailMessage: CFString ``` |

Modified [kUTTypeExecutable](https://developer.apple.com/documentation/coreservices/kuttypeexecutable)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeExecutable: CFString! ``` |
| To | ``` let kUTTypeExecutable: CFString ``` |

Modified [kUTTypeFileURL](https://developer.apple.com/documentation/coreservices/kuttypefileurl)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeFileURL: CFString! ``` |
| To | ``` let kUTTypeFileURL: CFString ``` |

Modified [kUTTypeFlatRTFD](https://developer.apple.com/documentation/coreservices/kuttypeflatrtfd)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeFlatRTFD: CFString! ``` |
| To | ``` let kUTTypeFlatRTFD: CFString ``` |

Modified [kUTTypeFolder](https://developer.apple.com/documentation/coreservices/kuttypefolder)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeFolder: CFString! ``` |
| To | ``` let kUTTypeFolder: CFString ``` |

Modified [kUTTypeFont](https://developer.apple.com/documentation/coreservices/kuttypefont)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeFont: CFString! ``` |
| To | ``` let kUTTypeFont: CFString ``` |

Modified [kUTTypeFramework](https://developer.apple.com/documentation/coreservices/kuttypeframework)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeFramework: CFString! ``` |
| To | ``` let kUTTypeFramework: CFString ``` |

Modified [kUTTypeGIF](https://developer.apple.com/documentation/coreservices/kuttypegif)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeGIF: CFString! ``` |
| To | ``` let kUTTypeGIF: CFString ``` |

Modified [kUTTypeGNUZipArchive](https://developer.apple.com/documentation/coreservices/kuttypegnuziparchive)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeGNUZipArchive: CFString! ``` |
| To | ``` let kUTTypeGNUZipArchive: CFString ``` |

Modified [kUTTypeHTML](https://developer.apple.com/documentation/coreservices/kuttypehtml)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeHTML: CFString! ``` |
| To | ``` let kUTTypeHTML: CFString ``` |

Modified [kUTTypeICO](https://developer.apple.com/documentation/coreservices/kuttypeico)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeICO: CFString! ``` |
| To | ``` let kUTTypeICO: CFString ``` |

Modified [kUTTypeIconFileKey](https://developer.apple.com/documentation/coreservices/kuttypeiconfilekey)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeIconFileKey: CFString! ``` |
| To | ``` let kUTTypeIconFileKey: CFString ``` |

Modified [kUTTypeIdentifierKey](https://developer.apple.com/documentation/coreservices/kuttypeidentifierkey)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeIdentifierKey: CFString! ``` |
| To | ``` let kUTTypeIdentifierKey: CFString ``` |

Modified [kUTTypeImage](https://developer.apple.com/documentation/coreservices/kuttypeimage)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeImage: CFString! ``` |
| To | ``` let kUTTypeImage: CFString ``` |

Modified [kUTTypeInkText](https://developer.apple.com/documentation/coreservices/kuttypeinktext)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeInkText: CFString! ``` |
| To | ``` let kUTTypeInkText: CFString ``` |

Modified [kUTTypeInternetLocation](https://developer.apple.com/documentation/coreservices/kuttypeinternetlocation)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeInternetLocation: CFString! ``` |
| To | ``` let kUTTypeInternetLocation: CFString ``` |

Modified [kUTTypeItem](https://developer.apple.com/documentation/coreservices/kuttypeitem)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeItem: CFString! ``` |
| To | ``` let kUTTypeItem: CFString ``` |

Modified [kUTTypeJavaArchive](https://developer.apple.com/documentation/coreservices/kuttypejavaarchive)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeJavaArchive: CFString! ``` |
| To | ``` let kUTTypeJavaArchive: CFString ``` |

Modified [kUTTypeJavaClass](https://developer.apple.com/documentation/coreservices/kuttypejavaclass)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeJavaClass: CFString! ``` |
| To | ``` let kUTTypeJavaClass: CFString ``` |

Modified [kUTTypeJavaScript](https://developer.apple.com/documentation/coreservices/kuttypejavascript)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeJavaScript: CFString! ``` |
| To | ``` let kUTTypeJavaScript: CFString ``` |

Modified [kUTTypeJavaSource](https://developer.apple.com/documentation/coreservices/kuttypejavasource)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeJavaSource: CFString! ``` |
| To | ``` let kUTTypeJavaSource: CFString ``` |

Modified [kUTTypeJPEG](https://developer.apple.com/documentation/coreservices/kuttypejpeg)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeJPEG: CFString! ``` |
| To | ``` let kUTTypeJPEG: CFString ``` |

Modified [kUTTypeJPEG2000](https://developer.apple.com/documentation/coreservices/kuttypejpeg2000)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeJPEG2000: CFString! ``` |
| To | ``` let kUTTypeJPEG2000: CFString ``` |

Modified [kUTTypeJSON](https://developer.apple.com/documentation/coreservices/kuttypejson)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeJSON: CFString! ``` |
| To | ``` let kUTTypeJSON: CFString ``` |

Modified [kUTTypeLog](https://developer.apple.com/documentation/coreservices/kuttypelog)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeLog: CFString! ``` |
| To | ``` let kUTTypeLog: CFString ``` |

Modified [kUTTypeM3UPlaylist](https://developer.apple.com/documentation/coreservices/kuttypem3uplaylist)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeM3UPlaylist: CFString! ``` |
| To | ``` let kUTTypeM3UPlaylist: CFString ``` |

Modified [kUTTypeMessage](https://developer.apple.com/documentation/coreservices/kuttypemessage)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeMessage: CFString! ``` |
| To | ``` let kUTTypeMessage: CFString ``` |

Modified [kUTTypeMIDIAudio](https://developer.apple.com/documentation/coreservices/kuttypemidiaudio)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeMIDIAudio: CFString! ``` |
| To | ``` let kUTTypeMIDIAudio: CFString ``` |

Modified [kUTTypeMountPoint](https://developer.apple.com/documentation/coreservices/kuttypemountpoint)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeMountPoint: CFString! ``` |
| To | ``` let kUTTypeMountPoint: CFString ``` |

Modified [kUTTypeMovie](https://developer.apple.com/documentation/coreservices/kuttypemovie)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeMovie: CFString! ``` |
| To | ``` let kUTTypeMovie: CFString ``` |

Modified [kUTTypeMP3](https://developer.apple.com/documentation/coreservices/kuttypemp3)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeMP3: CFString! ``` |
| To | ``` let kUTTypeMP3: CFString ``` |

Modified [kUTTypeMPEG](https://developer.apple.com/documentation/coreservices/kuttypempeg)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeMPEG: CFString! ``` |
| To | ``` let kUTTypeMPEG: CFString ``` |

Modified [kUTTypeMPEG2TransportStream](https://developer.apple.com/documentation/coreservices/kuttypempeg2transportstream)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeMPEG2TransportStream: CFString! ``` |
| To | ``` let kUTTypeMPEG2TransportStream: CFString ``` |

Modified [kUTTypeMPEG2Video](https://developer.apple.com/documentation/coreservices/kuttypempeg2video)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeMPEG2Video: CFString! ``` |
| To | ``` let kUTTypeMPEG2Video: CFString ``` |

Modified [kUTTypeMPEG4](https://developer.apple.com/documentation/coreservices/kuttypempeg4)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeMPEG4: CFString! ``` |
| To | ``` let kUTTypeMPEG4: CFString ``` |

Modified [kUTTypeMPEG4Audio](https://developer.apple.com/documentation/coreservices/kuttypempeg4audio)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeMPEG4Audio: CFString! ``` |
| To | ``` let kUTTypeMPEG4Audio: CFString ``` |

Modified [kUTTypeObjectiveCPlusPlusSource](https://developer.apple.com/documentation/coreservices/kuttypeobjectivecplusplussource)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeObjectiveCPlusPlusSource: CFString! ``` |
| To | ``` let kUTTypeObjectiveCPlusPlusSource: CFString ``` |

Modified [kUTTypeObjectiveCSource](https://developer.apple.com/documentation/coreservices/kuttypeobjectivecsource)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeObjectiveCSource: CFString! ``` |
| To | ``` let kUTTypeObjectiveCSource: CFString ``` |

Modified [kUTTypeOSAScript](https://developer.apple.com/documentation/coreservices/kuttypeosascript)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeOSAScript: CFString! ``` |
| To | ``` let kUTTypeOSAScript: CFString ``` |

Modified [kUTTypeOSAScriptBundle](https://developer.apple.com/documentation/coreservices/kuttypeosascriptbundle)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeOSAScriptBundle: CFString! ``` |
| To | ``` let kUTTypeOSAScriptBundle: CFString ``` |

Modified [kUTTypePackage](https://developer.apple.com/documentation/coreservices/kuttypepackage)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypePackage: CFString! ``` |
| To | ``` let kUTTypePackage: CFString ``` |

Modified [kUTTypePDF](https://developer.apple.com/documentation/coreservices/kuttypepdf)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypePDF: CFString! ``` |
| To | ``` let kUTTypePDF: CFString ``` |

Modified [kUTTypePerlScript](https://developer.apple.com/documentation/coreservices/kuttypeperlscript)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypePerlScript: CFString! ``` |
| To | ``` let kUTTypePerlScript: CFString ``` |

Modified [kUTTypePHPScript](https://developer.apple.com/documentation/coreservices/kuttypephpscript)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypePHPScript: CFString! ``` |
| To | ``` let kUTTypePHPScript: CFString ``` |

Modified [kUTTypePICT](https://developer.apple.com/documentation/coreservices/kuttypepict)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypePICT: CFString! ``` |
| To | ``` let kUTTypePICT: CFString ``` |

Modified [kUTTypePKCS12](https://developer.apple.com/documentation/coreservices/kuttypepkcs12)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypePKCS12: CFString! ``` |
| To | ``` let kUTTypePKCS12: CFString ``` |

Modified [kUTTypePlainText](https://developer.apple.com/documentation/coreservices/kuttypeplaintext)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypePlainText: CFString! ``` |
| To | ``` let kUTTypePlainText: CFString ``` |

Modified [kUTTypePlaylist](https://developer.apple.com/documentation/coreservices/kuttypeplaylist)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypePlaylist: CFString! ``` |
| To | ``` let kUTTypePlaylist: CFString ``` |

Modified [kUTTypePluginBundle](https://developer.apple.com/documentation/coreservices/kuttypepluginbundle)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypePluginBundle: CFString! ``` |
| To | ``` let kUTTypePluginBundle: CFString ``` |

Modified [kUTTypePNG](https://developer.apple.com/documentation/coreservices/kuttypepng)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypePNG: CFString! ``` |
| To | ``` let kUTTypePNG: CFString ``` |

Modified [kUTTypePresentation](https://developer.apple.com/documentation/coreservices/kuttypepresentation)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypePresentation: CFString! ``` |
| To | ``` let kUTTypePresentation: CFString ``` |

Modified [kUTTypePropertyList](https://developer.apple.com/documentation/coreservices/kuttypepropertylist)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypePropertyList: CFString! ``` |
| To | ``` let kUTTypePropertyList: CFString ``` |

Modified [kUTTypePythonScript](https://developer.apple.com/documentation/coreservices/kuttypepythonscript)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypePythonScript: CFString! ``` |
| To | ``` let kUTTypePythonScript: CFString ``` |

Modified [kUTTypeQuickLookGenerator](https://developer.apple.com/documentation/coreservices/kuttypequicklookgenerator)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeQuickLookGenerator: CFString! ``` |
| To | ``` let kUTTypeQuickLookGenerator: CFString ``` |

Modified [kUTTypeQuickTimeImage](https://developer.apple.com/documentation/coreservices/kuttypequicktimeimage)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeQuickTimeImage: CFString! ``` |
| To | ``` let kUTTypeQuickTimeImage: CFString ``` |

Modified [kUTTypeQuickTimeMovie](https://developer.apple.com/documentation/coreservices/kuttypequicktimemovie)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeQuickTimeMovie: CFString! ``` |
| To | ``` let kUTTypeQuickTimeMovie: CFString ``` |

Modified [kUTTypeRawImage](https://developer.apple.com/documentation/coreservices/kuttyperawimage)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeRawImage: CFString! ``` |
| To | ``` let kUTTypeRawImage: CFString ``` |

Modified [kUTTypeReferenceURLKey](https://developer.apple.com/documentation/coreservices/kuttypereferenceurlkey)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeReferenceURLKey: CFString! ``` |
| To | ``` let kUTTypeReferenceURLKey: CFString ``` |

Modified [kUTTypeResolvable](https://developer.apple.com/documentation/coreservices/kuttyperesolvable)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeResolvable: CFString! ``` |
| To | ``` let kUTTypeResolvable: CFString ``` |

Modified [kUTTypeRTF](https://developer.apple.com/documentation/coreservices/kuttypertf)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeRTF: CFString! ``` |
| To | ``` let kUTTypeRTF: CFString ``` |

Modified [kUTTypeRTFD](https://developer.apple.com/documentation/coreservices/kuttypertfd)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeRTFD: CFString! ``` |
| To | ``` let kUTTypeRTFD: CFString ``` |

Modified [kUTTypeRubyScript](https://developer.apple.com/documentation/coreservices/kuttyperubyscript)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeRubyScript: CFString! ``` |
| To | ``` let kUTTypeRubyScript: CFString ``` |

Modified [kUTTypeScalableVectorGraphics](https://developer.apple.com/documentation/coreservices/kuttypescalablevectorgraphics)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeScalableVectorGraphics: CFString! ``` |
| To | ``` let kUTTypeScalableVectorGraphics: CFString ``` |

Modified [kUTTypeScript](https://developer.apple.com/documentation/coreservices/kuttypescript)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeScript: CFString! ``` |
| To | ``` let kUTTypeScript: CFString ``` |

Modified [kUTTypeShellScript](https://developer.apple.com/documentation/coreservices/kuttypeshellscript)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeShellScript: CFString! ``` |
| To | ``` let kUTTypeShellScript: CFString ``` |

Modified [kUTTypeSourceCode](https://developer.apple.com/documentation/coreservices/kuttypesourcecode)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeSourceCode: CFString! ``` |
| To | ``` let kUTTypeSourceCode: CFString ``` |

Modified [kUTTypeSpotlightImporter](https://developer.apple.com/documentation/coreservices/kuttypespotlightimporter)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeSpotlightImporter: CFString! ``` |
| To | ``` let kUTTypeSpotlightImporter: CFString ``` |

Modified [kUTTypeSpreadsheet](https://developer.apple.com/documentation/coreservices/kuttypespreadsheet)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeSpreadsheet: CFString! ``` |
| To | ``` let kUTTypeSpreadsheet: CFString ``` |

Modified [kUTTypeSymLink](https://developer.apple.com/documentation/coreservices/kuttypesymlink)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeSymLink: CFString! ``` |
| To | ``` let kUTTypeSymLink: CFString ``` |

Modified [kUTTypeSystemPreferencesPane](https://developer.apple.com/documentation/coreservices/kuttypesystempreferencespane)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeSystemPreferencesPane: CFString! ``` |
| To | ``` let kUTTypeSystemPreferencesPane: CFString ``` |

Modified [kUTTypeTabSeparatedText](https://developer.apple.com/documentation/coreservices/kuttypetabseparatedtext)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeTabSeparatedText: CFString! ``` |
| To | ``` let kUTTypeTabSeparatedText: CFString ``` |

Modified [kUTTypeTagSpecificationKey](https://developer.apple.com/documentation/coreservices/kuttypetagspecificationkey)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeTagSpecificationKey: CFString! ``` |
| To | ``` let kUTTypeTagSpecificationKey: CFString ``` |

Modified [kUTTypeText](https://developer.apple.com/documentation/coreservices/kuttypetext)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeText: CFString! ``` |
| To | ``` let kUTTypeText: CFString ``` |

Modified [kUTTypeTIFF](https://developer.apple.com/documentation/coreservices/kuttypetiff)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeTIFF: CFString! ``` |
| To | ``` let kUTTypeTIFF: CFString ``` |

Modified [kUTTypeToDoItem](https://developer.apple.com/documentation/coreservices/kuttypetodoitem)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeToDoItem: CFString! ``` |
| To | ``` let kUTTypeToDoItem: CFString ``` |

Modified [kUTTypeTXNTextAndMultimediaData](https://developer.apple.com/documentation/coreservices/kuttypetxntextandmultimediadata)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeTXNTextAndMultimediaData: CFString! ``` |
| To | ``` let kUTTypeTXNTextAndMultimediaData: CFString ``` |

Modified [kUTTypeUnixExecutable](https://developer.apple.com/documentation/coreservices/kuttypeunixexecutable)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeUnixExecutable: CFString! ``` |
| To | ``` let kUTTypeUnixExecutable: CFString ``` |

Modified [kUTTypeURL](https://developer.apple.com/documentation/coreservices/kuttypeurl)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeURL: CFString! ``` |
| To | ``` let kUTTypeURL: CFString ``` |

Modified [kUTTypeURLBookmarkData](https://developer.apple.com/documentation/coreservices/kuttypeurlbookmarkdata)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeURLBookmarkData: CFString! ``` |
| To | ``` let kUTTypeURLBookmarkData: CFString ``` |

Modified [kUTTypeUTF16ExternalPlainText](https://developer.apple.com/documentation/coreservices/kuttypeutf16externalplaintext)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeUTF16ExternalPlainText: CFString! ``` |
| To | ``` let kUTTypeUTF16ExternalPlainText: CFString ``` |

Modified [kUTTypeUTF16PlainText](https://developer.apple.com/documentation/coreservices/kuttypeutf16plaintext)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeUTF16PlainText: CFString! ``` |
| To | ``` let kUTTypeUTF16PlainText: CFString ``` |

Modified [kUTTypeUTF8PlainText](https://developer.apple.com/documentation/coreservices/kuttypeutf8plaintext)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeUTF8PlainText: CFString! ``` |
| To | ``` let kUTTypeUTF8PlainText: CFString ``` |

Modified [kUTTypeUTF8TabSeparatedText](https://developer.apple.com/documentation/coreservices/kuttypeutf8tabseparatedtext)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeUTF8TabSeparatedText: CFString! ``` |
| To | ``` let kUTTypeUTF8TabSeparatedText: CFString ``` |

Modified [kUTTypeVCard](https://developer.apple.com/documentation/coreservices/kuttypevcard)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeVCard: CFString! ``` |
| To | ``` let kUTTypeVCard: CFString ``` |

Modified [kUTTypeVersionKey](https://developer.apple.com/documentation/coreservices/kuttypeversionkey)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeVersionKey: CFString! ``` |
| To | ``` let kUTTypeVersionKey: CFString ``` |

Modified [kUTTypeVideo](https://developer.apple.com/documentation/coreservices/kuttypevideo)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeVideo: CFString! ``` |
| To | ``` let kUTTypeVideo: CFString ``` |

Modified [kUTTypeVolume](https://developer.apple.com/documentation/coreservices/kuttypevolume)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeVolume: CFString! ``` |
| To | ``` let kUTTypeVolume: CFString ``` |

Modified [kUTTypeWaveformAudio](https://developer.apple.com/documentation/coreservices/kuttypewaveformaudio)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeWaveformAudio: CFString! ``` |
| To | ``` let kUTTypeWaveformAudio: CFString ``` |

Modified [kUTTypeWebArchive](https://developer.apple.com/documentation/coreservices/kuttypewebarchive)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeWebArchive: CFString! ``` |
| To | ``` let kUTTypeWebArchive: CFString ``` |

Modified [kUTTypeWindowsExecutable](https://developer.apple.com/documentation/coreservices/kuttypewindowsexecutable)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeWindowsExecutable: CFString! ``` |
| To | ``` let kUTTypeWindowsExecutable: CFString ``` |

Modified [kUTTypeX509Certificate](https://developer.apple.com/documentation/coreservices/kuttypex509certificate)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeX509Certificate: CFString! ``` |
| To | ``` let kUTTypeX509Certificate: CFString ``` |

Modified [kUTTypeXML](https://developer.apple.com/documentation/coreservices/kuttypexml)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeXML: CFString! ``` |
| To | ``` let kUTTypeXML: CFString ``` |

Modified [kUTTypeXMLPropertyList](https://developer.apple.com/documentation/coreservices/kuttypexmlpropertylist)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeXMLPropertyList: CFString! ``` |
| To | ``` let kUTTypeXMLPropertyList: CFString ``` |

Modified [kUTTypeXPCService](https://developer.apple.com/documentation/coreservices/kuttypexpcservice)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeXPCService: CFString! ``` |
| To | ``` let kUTTypeXPCService: CFString ``` |

Modified [kUTTypeZipArchive](https://developer.apple.com/documentation/coreservices/kuttypeziparchive)

|  | Declaration |
| --- | --- |
| From | ``` let kUTTypeZipArchive: CFString! ``` |
| To | ``` let kUTTypeZipArchive: CFString ``` |

Modified [LSCanRefAcceptItem(_: UnsafePointer<FSRef>, _: UnsafePointer<FSRef>, _: LSRolesMask, _: LSAcceptanceFlags, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/coreservices/1442183-lscanrefacceptitem)

|  | Declaration |
| --- | --- |
| From | ``` func LSCanRefAcceptItem(_ inItemFSRef: UnsafePointer<FSRef>, _ inTargetRef: UnsafePointer<FSRef>, _ inRoleMask: LSRolesMask, _ inFlags: LSAcceptanceFlags, _ outAcceptsItem: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func LSCanRefAcceptItem(_ inItemFSRef: UnsafePointer<FSRef>, _ inTargetRef: UnsafePointer<FSRef>, _ inRoleMask: LSRolesMask, _ inFlags: LSAcceptanceFlags, _ outAcceptsItem: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [LSCanURLAcceptURL(_: CFURL, _: CFURL, _: LSRolesMask, _: LSAcceptanceFlags, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/coreservices/1441854-lscanurlaccepturl)

|  | Declaration |
| --- | --- |
| From | ``` func LSCanURLAcceptURL(_ inItemURL: CFURL!, _ inTargetURL: CFURL!, _ inRoleMask: LSRolesMask, _ inFlags: LSAcceptanceFlags, _ outAcceptsItem: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func LSCanURLAcceptURL(_ inItemURL: CFURL, _ inTargetURL: CFURL, _ inRoleMask: LSRolesMask, _ inFlags: LSAcceptanceFlags, _ outAcceptsItem: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [LSCopyAllHandlersForURLScheme(_: CFString) -> Unmanaged<CFArray>?](https://developer.apple.com/documentation/coreservices/1443240-lscopyallhandlersforurlscheme)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyAllHandlersForURLScheme(_ inURLScheme: CFString!) -> Unmanaged<CFArray>! ``` |
| To | ``` func LSCopyAllHandlersForURLScheme(_ inURLScheme: CFString) -> Unmanaged<CFArray>? ``` |

Modified [LSCopyAllRoleHandlersForContentType(_: CFString, _: LSRolesMask) -> Unmanaged<CFArray>?](https://developer.apple.com/documentation/coreservices/1448020-lscopyallrolehandlersforcontentt)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyAllRoleHandlersForContentType(_ inContentType: CFString!, _ inRole: LSRolesMask) -> Unmanaged<CFArray>! ``` |
| To | ``` func LSCopyAllRoleHandlersForContentType(_ inContentType: CFString, _ inRole: LSRolesMask) -> Unmanaged<CFArray>? ``` |

Modified [LSCopyApplicationURLsForBundleIdentifier(_: CFString, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>?](https://developer.apple.com/documentation/coreservices/1449290-lscopyapplicationurlsforbundleid)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyApplicationURLsForBundleIdentifier(_ inBundleIdentifier: CFString!, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |
| To | ``` func LSCopyApplicationURLsForBundleIdentifier(_ inBundleIdentifier: CFString, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>? ``` |

Modified [LSCopyApplicationURLsForURL(_: CFURL, _: LSRolesMask) -> Unmanaged<CFArray>?](https://developer.apple.com/documentation/coreservices/1445148-lscopyapplicationurlsforurl)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyApplicationURLsForURL(_ inURL: CFURL!, _ inRoleMask: LSRolesMask) -> Unmanaged<CFArray>! ``` |
| To | ``` func LSCopyApplicationURLsForURL(_ inURL: CFURL, _ inRoleMask: LSRolesMask) -> Unmanaged<CFArray>? ``` |

Modified [LSCopyDefaultApplicationURLForContentType(_: CFString, _: LSRolesMask, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>?](https://developer.apple.com/documentation/coreservices/1447734-lscopydefaultapplicationurlforco)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyDefaultApplicationURLForContentType(_ inContentType: CFString!, _ inRoleMask: LSRolesMask, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>! ``` |
| To | ``` func LSCopyDefaultApplicationURLForContentType(_ inContentType: CFString, _ inRoleMask: LSRolesMask, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>? ``` |

Modified [LSCopyDefaultApplicationURLForURL(_: CFURL, _: LSRolesMask, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>?](https://developer.apple.com/documentation/coreservices/1448824-lscopydefaultapplicationurlforur)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyDefaultApplicationURLForURL(_ inURL: CFURL!, _ inRoleMask: LSRolesMask, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>! ``` |
| To | ``` func LSCopyDefaultApplicationURLForURL(_ inURL: CFURL, _ inRoleMask: LSRolesMask, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>? ``` |

Modified [LSCopyDefaultHandlerForURLScheme(_: CFString) -> Unmanaged<CFString>?](https://developer.apple.com/documentation/coreservices/1441725-lscopydefaulthandlerforurlscheme)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyDefaultHandlerForURLScheme(_ inURLScheme: CFString!) -> Unmanaged<CFString>! ``` |
| To | ``` func LSCopyDefaultHandlerForURLScheme(_ inURLScheme: CFString) -> Unmanaged<CFString>? ``` |

Modified [LSCopyDefaultRoleHandlerForContentType(_: CFString, _: LSRolesMask) -> Unmanaged<CFString>?](https://developer.apple.com/documentation/coreservices/1449868-lscopydefaultrolehandlerforconte)

|  | Declaration |
| --- | --- |
| From | ``` func LSCopyDefaultRoleHandlerForContentType(_ inContentType: CFString!, _ inRole: LSRolesMask) -> Unmanaged<CFString>! ``` |
| To | ``` func LSCopyDefaultRoleHandlerForContentType(_ inContentType: CFString, _ inRole: LSRolesMask) -> Unmanaged<CFString>? ``` |

Modified [LSCopyDisplayNameForURL(_: CFURL!, _: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](https://developer.apple.com/documentation/coreservices/1446850-lscopydisplaynameforurl)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSCopyItemInfoForURL(_: CFURL!, _: LSRequestedInfo, _: UnsafeMutablePointer<LSItemInfoRecord>) -> OSStatus](https://developer.apple.com/documentation/coreservices/1445685-lscopyiteminfoforurl)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSCopyKindStringForURL(_: CFURL!, _: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](https://developer.apple.com/documentation/coreservices/1447481-lscopykindstringforurl)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSGetExtensionInfo(_: Int, _: UnsafePointer<UniChar>, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/coreservices/1446043-lsgetextensioninfo)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSGetHandlerOptionsForContentType(_: CFString!) -> LSHandlerOptions](https://developer.apple.com/documentation/coreservices/1445296-lsgethandleroptionsforcontenttyp)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSOpenCFURLRef(_: CFURL, _: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus](https://developer.apple.com/documentation/coreservices/1442850-lsopencfurlref)

|  | Declaration |
| --- | --- |
| From | ``` func LSOpenCFURLRef(_ inURL: CFURL!, _ outLaunchedURL: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` |
| To | ``` func LSOpenCFURLRef(_ inURL: CFURL, _ outLaunchedURL: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` |

Modified [LSRegisterFSRef(_: UnsafePointer<FSRef>, _: Bool) -> OSStatus](https://developer.apple.com/documentation/coreservices/1444582-lsregisterfsref)

|  | Declaration |
| --- | --- |
| From | ``` func LSRegisterFSRef(_ inRef: UnsafePointer<FSRef>, _ inUpdate: Boolean) -> OSStatus ``` |
| To | ``` func LSRegisterFSRef(_ inRef: UnsafePointer<FSRef>, _ inUpdate: Bool) -> OSStatus ``` |

Modified [LSRegisterURL(_: CFURL, _: Bool) -> OSStatus](https://developer.apple.com/documentation/coreservices/1446350-lsregisterurl)

|  | Declaration |
| --- | --- |
| From | ``` func LSRegisterURL(_ inURL: CFURL!, _ inUpdate: Boolean) -> OSStatus ``` |
| To | ``` func LSRegisterURL(_ inURL: CFURL, _ inUpdate: Bool) -> OSStatus ``` |

Modified [LSSetDefaultHandlerForURLScheme(_: CFString, _: CFString) -> OSStatus](https://developer.apple.com/documentation/coreservices/1447760-lssetdefaulthandlerforurlscheme)

|  | Declaration |
| --- | --- |
| From | ``` func LSSetDefaultHandlerForURLScheme(_ inURLScheme: CFString!, _ inHandlerBundleID: CFString!) -> OSStatus ``` |
| To | ``` func LSSetDefaultHandlerForURLScheme(_ inURLScheme: CFString, _ inHandlerBundleID: CFString) -> OSStatus ``` |

Modified [LSSetDefaultRoleHandlerForContentType(_: CFString, _: LSRolesMask, _: CFString) -> OSStatus](https://developer.apple.com/documentation/coreservices/1444955-lssetdefaultrolehandlerforconten)

|  | Declaration |
| --- | --- |
| From | ``` func LSSetDefaultRoleHandlerForContentType(_ inContentType: CFString!, _ inRole: LSRolesMask, _ inHandlerBundleID: CFString!) -> OSStatus ``` |
| To | ``` func LSSetDefaultRoleHandlerForContentType(_ inContentType: CFString, _ inRole: LSRolesMask, _ inHandlerBundleID: CFString) -> OSStatus ``` |

Modified [LSSetExtensionHiddenForRef(_: UnsafePointer<FSRef>, _: Bool) -> OSStatus](https://developer.apple.com/documentation/coreservices/1442766-lssetextensionhiddenforref)

|  | Declaration |
| --- | --- |
| From | ``` func LSSetExtensionHiddenForRef(_ inRef: UnsafePointer<FSRef>, _ inHide: Boolean) -> OSStatus ``` |
| To | ``` func LSSetExtensionHiddenForRef(_ inRef: UnsafePointer<FSRef>, _ inHide: Bool) -> OSStatus ``` |

Modified [LSSetExtensionHiddenForURL(_: CFURL!, _: Bool) -> OSStatus](https://developer.apple.com/documentation/coreservices/1443948-lssetextensionhiddenforurl)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func LSSetExtensionHiddenForURL(_ inURL: CFURL!, _ inHide: Boolean) -> OSStatus ``` | -- |
| To | ``` func LSSetExtensionHiddenForURL(_ inURL: CFURL!, _ inHide: Bool) -> OSStatus ``` | OS X 10.11 |

Modified [LSSetHandlerOptionsForContentType(_: CFString!, _: LSHandlerOptions) -> OSStatus](https://developer.apple.com/documentation/coreservices/1447588-lssethandleroptionsforcontenttyp)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSSharedFileListAddObserver(_: LSSharedFileList!, _: CFRunLoop!, _: CFString!, _: LSSharedFileListChangedProcPtr!, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/coreservices/1445770-lssharedfilelistaddobserver)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func LSSharedFileListAddObserver(_ inList: LSSharedFileList!, _ inRunloop: CFRunLoop!, _ inRunloopMode: CFString!, _ callback: LSSharedFileListChangedProcPtr, _ context: UnsafeMutablePointer<Void>) ``` | -- |
| To | ``` func LSSharedFileListAddObserver(_ inList: LSSharedFileList!, _ inRunloop: CFRunLoop!, _ inRunloopMode: CFString!, _ callback: LSSharedFileListChangedProcPtr!, _ context: UnsafeMutablePointer<Void>) ``` | OS X 10.11 |

Modified [LSSharedFileListChangedProcPtr](https://developer.apple.com/documentation/coreservices/lssharedfilelistchangedprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias LSSharedFileListChangedProcPtr = CFunctionPointer<((LSSharedFileList!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias LSSharedFileListChangedProcPtr = (LSSharedFileList!, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [LSSharedFileListCopyProperty(_: LSSharedFileList!, _: CFString!) -> Unmanaged<AnyObject>!](https://developer.apple.com/documentation/coreservices/1444588-lssharedfilelistcopyproperty)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSSharedFileListCopySnapshot(_: LSSharedFileList!, _: UnsafeMutablePointer<UInt32>) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/coreservices/1448112-lssharedfilelistcopysnapshot)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSSharedFileListCreate(_: CFAllocator!, _: CFString!, _: AnyObject!) -> Unmanaged<LSSharedFileList>!](https://developer.apple.com/documentation/coreservices/1443926-lssharedfilelistcreate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSSharedFileListGetSeedValue(_: LSSharedFileList!) -> UInt32](https://developer.apple.com/documentation/coreservices/1444885-lssharedfilelistgetseedvalue)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSSharedFileListGetTypeID() -> CFTypeID](https://developer.apple.com/documentation/coreservices/1450618-lssharedfilelistgettypeid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSSharedFileListInsertItemURL(_: LSSharedFileList!, _: LSSharedFileListItem!, _: CFString!, _: IconRef, _: CFURL!, _: CFDictionary!, _: CFArray!) -> Unmanaged<LSSharedFileListItem>!](https://developer.apple.com/documentation/coreservices/1444471-lssharedfilelistinsertitemurl)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSSharedFileListItemCopyDisplayName(_: LSSharedFileListItem!) -> Unmanaged<CFString>!](https://developer.apple.com/documentation/coreservices/1449716-lssharedfilelistitemcopydisplayn)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSSharedFileListItemCopyIconRef(_: LSSharedFileListItem!) -> IconRef](https://developer.apple.com/documentation/coreservices/1442889-lssharedfilelistitemcopyiconref)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSSharedFileListItemCopyProperty(_: LSSharedFileListItem!, _: CFString!) -> Unmanaged<AnyObject>!](https://developer.apple.com/documentation/coreservices/1445074-lssharedfilelistitemcopyproperty)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSSharedFileListItemCopyResolvedURL(_: LSSharedFileListItem!, _: LSSharedFileListResolutionFlags, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>!](https://developer.apple.com/documentation/coreservices/1449882-lssharedfilelistitemcopyresolved)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSSharedFileListItemGetID(_: LSSharedFileListItem!) -> UInt32](https://developer.apple.com/documentation/coreservices/1443305-lssharedfilelistitemgetid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSSharedFileListItemGetTypeID() -> CFTypeID](https://developer.apple.com/documentation/coreservices/1447138-lssharedfilelistitemgettypeid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSSharedFileListItemMove(_: LSSharedFileList!, _: LSSharedFileListItem!, _: LSSharedFileListItem!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1444348-lssharedfilelistitemmove)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSSharedFileListItemRemove(_: LSSharedFileList!, _: LSSharedFileListItem!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1442025-lssharedfilelistitemremove)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSSharedFileListItemSetProperty(_: LSSharedFileListItem!, _: CFString!, _: AnyObject!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1445766-lssharedfilelistitemsetproperty)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSSharedFileListRemoveAllItems(_: LSSharedFileList!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1446389-lssharedfilelistremoveallitems)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSSharedFileListRemoveObserver(_: LSSharedFileList!, _: CFRunLoop!, _: CFString!, _: LSSharedFileListChangedProcPtr!, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/coreservices/1443404-lssharedfilelistremoveobserver)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func LSSharedFileListRemoveObserver(_ inList: LSSharedFileList!, _ inRunloop: CFRunLoop!, _ inRunloopMode: CFString!, _ callback: LSSharedFileListChangedProcPtr, _ context: UnsafeMutablePointer<Void>) ``` | -- |
| To | ``` func LSSharedFileListRemoveObserver(_ inList: LSSharedFileList!, _ inRunloop: CFRunLoop!, _ inRunloopMode: CFString!, _ callback: LSSharedFileListChangedProcPtr!, _ context: UnsafeMutablePointer<Void>) ``` | OS X 10.11 |

Modified [LSSharedFileListSetAuthorization(_: LSSharedFileList!, _: AuthorizationRef) -> OSStatus](https://developer.apple.com/documentation/coreservices/1446834-lssharedfilelistsetauthorization)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [LSSharedFileListSetProperty(_: LSSharedFileList!, _: CFString!, _: AnyObject!) -> OSStatus](https://developer.apple.com/documentation/coreservices/1448857-lssharedfilelistsetproperty)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [MDItemRemoveLabel(_: MDItem!, _: MDLabel!) -> Bool](https://developer.apple.com/documentation/coreservices/1446067-mditemremovelabel)

|  | Declaration |
| --- | --- |
| From | ``` func MDItemRemoveLabel(_ item: MDItem!, _ label: MDLabel!) -> Boolean ``` |
| To | ``` func MDItemRemoveLabel(_ item: MDItem!, _ label: MDLabel!) -> Bool ``` |

Modified [MDItemSetLabel(_: MDItem!, _: MDLabel!) -> Bool](https://developer.apple.com/documentation/coreservices/1442559-mditemsetlabel)

|  | Declaration |
| --- | --- |
| From | ``` func MDItemSetLabel(_ item: MDItem!, _ label: MDLabel!) -> Boolean ``` |
| To | ``` func MDItemSetLabel(_ item: MDItem!, _ label: MDLabel!) -> Bool ``` |

Modified [MDLabelDelete(_: MDLabel!) -> Bool](https://developer.apple.com/documentation/coreservices/1449203-mdlabeldelete)

|  | Declaration |
| --- | --- |
| From | ``` func MDLabelDelete(_ label: MDLabel!) -> Boolean ``` |
| To | ``` func MDLabelDelete(_ label: MDLabel!) -> Bool ``` |

Modified [MDLabelSetAttributes(_: MDLabel!, _: CFDictionary!) -> Bool](https://developer.apple.com/documentation/coreservices/1449005-mdlabelsetattributes)

|  | Declaration |
| --- | --- |
| From | ``` func MDLabelSetAttributes(_ label: MDLabel!, _ attrs: CFDictionary!) -> Boolean ``` |
| To | ``` func MDLabelSetAttributes(_ label: MDLabel!, _ attrs: CFDictionary!) -> Bool ``` |

Modified [MDQueryCreateResultFunction](https://developer.apple.com/documentation/coreservices/mdquerycreateresultfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias MDQueryCreateResultFunction = CFunctionPointer<((MDQuery!, MDItem!, UnsafeMutablePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` typealias MDQueryCreateResultFunction = (MDQuery!, MDItem!, UnsafeMutablePointer<Void>) -> UnsafePointer<Void> ``` |

Modified [MDQueryCreateValueFunction](https://developer.apple.com/documentation/coreservices/mdquerycreatevaluefunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias MDQueryCreateValueFunction = CFunctionPointer<((MDQuery!, CFString!, AnyObject!, UnsafeMutablePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` typealias MDQueryCreateValueFunction = (MDQuery!, CFString!, AnyObject!, UnsafeMutablePointer<Void>) -> UnsafePointer<Void> ``` |

Modified [MDQueryExecute(_: MDQuery!, _: CFOptionFlags) -> Bool](https://developer.apple.com/documentation/coreservices/1413099-mdqueryexecute)

|  | Declaration |
| --- | --- |
| From | ``` func MDQueryExecute(_ query: MDQuery!, _ optionFlags: CFOptionFlags) -> Boolean ``` |
| To | ``` func MDQueryExecute(_ query: MDQuery!, _ optionFlags: CFOptionFlags) -> Bool ``` |

Modified [MDQueryIsGatheringComplete(_: MDQuery!) -> Bool](https://developer.apple.com/documentation/coreservices/1413032-mdqueryisgatheringcomplete)

|  | Declaration |
| --- | --- |
| From | ``` func MDQueryIsGatheringComplete(_ query: MDQuery!) -> Boolean ``` |
| To | ``` func MDQueryIsGatheringComplete(_ query: MDQuery!) -> Bool ``` |

Modified [MDQuerySetCreateResultFunction(_: MDQuery!, _: MDQueryCreateResultFunction!, _: UnsafeMutablePointer<Void>, _: UnsafePointer<CFArrayCallBacks>)](https://developer.apple.com/documentation/coreservices/1413064-mdquerysetcreateresultfunction)

|  | Declaration |
| --- | --- |
| From | ``` func MDQuerySetCreateResultFunction(_ query: MDQuery!, _ `func`: MDQueryCreateResultFunction, _ context: UnsafeMutablePointer<Void>, _ cb: UnsafePointer<CFArrayCallBacks>) ``` |
| To | ``` func MDQuerySetCreateResultFunction(_ query: MDQuery!, _ `func`: MDQueryCreateResultFunction!, _ context: UnsafeMutablePointer<Void>, _ cb: UnsafePointer<CFArrayCallBacks>) ``` |

Modified [MDQuerySetCreateValueFunction(_: MDQuery!, _: MDQueryCreateValueFunction!, _: UnsafeMutablePointer<Void>, _: UnsafePointer<CFArrayCallBacks>)](https://developer.apple.com/documentation/coreservices/1413017-mdquerysetcreatevaluefunction)

|  | Declaration |
| --- | --- |
| From | ``` func MDQuerySetCreateValueFunction(_ query: MDQuery!, _ `func`: MDQueryCreateValueFunction, _ context: UnsafeMutablePointer<Void>, _ cb: UnsafePointer<CFArrayCallBacks>) ``` |
| To | ``` func MDQuerySetCreateValueFunction(_ query: MDQuery!, _ `func`: MDQueryCreateValueFunction!, _ context: UnsafeMutablePointer<Void>, _ cb: UnsafePointer<CFArrayCallBacks>) ``` |

Modified [MDQuerySetSortComparator(_: MDQuery!, _: MDQuerySortComparatorFunction!, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/coreservices/1413087-mdquerysetsortcomparator)

|  | Declaration |
| --- | --- |
| From | ``` func MDQuerySetSortComparator(_ query: MDQuery!, _ comparator: MDQuerySortComparatorFunction, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func MDQuerySetSortComparator(_ query: MDQuery!, _ comparator: MDQuerySortComparatorFunction!, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [MDQuerySetSortOptionFlagsForAttribute(_: MDQuery!, _: CFString!, _: UInt32) -> Bool](https://developer.apple.com/documentation/coreservices/1413075-mdquerysetsortoptionflagsforattr)

|  | Declaration |
| --- | --- |
| From | ``` func MDQuerySetSortOptionFlagsForAttribute(_ query: MDQuery!, _ fieldName: CFString!, _ flags: UInt32) -> Boolean ``` |
| To | ``` func MDQuerySetSortOptionFlagsForAttribute(_ query: MDQuery!, _ fieldName: CFString!, _ flags: UInt32) -> Bool ``` |

Modified [MDQuerySetSortOrder(_: MDQuery!, _: CFArray!) -> Bool](https://developer.apple.com/documentation/coreservices/1413096-mdquerysetsortorder)

|  | Declaration |
| --- | --- |
| From | ``` func MDQuerySetSortOrder(_ query: MDQuery!, _ sortingAttrs: CFArray!) -> Boolean ``` |
| To | ``` func MDQuerySetSortOrder(_ query: MDQuery!, _ sortingAttrs: CFArray!) -> Bool ``` |

Modified [MDQuerySortComparatorFunction](https://developer.apple.com/documentation/coreservices/mdquerysortcomparatorfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias MDQuerySortComparatorFunction = CFunctionPointer<((UnsafePointer<Unmanaged<AnyObject>?>, UnsafePointer<Unmanaged<AnyObject>?>, UnsafeMutablePointer<Void>) -> CFComparisonResult)> ``` |
| To | ``` typealias MDQuerySortComparatorFunction = (UnsafePointer<Unmanaged<AnyObject>?>, UnsafePointer<Unmanaged<AnyObject>?>, UnsafeMutablePointer<Void>) -> CFComparisonResult ``` |

Modified [NewAECoerceDescUPP(_: AECoerceDescProcPtr!) -> AECoerceDescUPP!](https://developer.apple.com/documentation/coreservices/1445885-newaecoercedescupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewAECoerceDescUPP(_ userRoutine: AECoerceDescProcPtr) -> AECoerceDescUPP ``` |
| To | ``` func NewAECoerceDescUPP(_ userRoutine: AECoerceDescProcPtr!) -> AECoerceDescUPP! ``` |

Modified [NewAECoercePtrUPP(_: AECoercePtrProcPtr!) -> AECoercePtrUPP!](https://developer.apple.com/documentation/coreservices/1449962-newaecoerceptrupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewAECoercePtrUPP(_ userRoutine: AECoercePtrProcPtr) -> AECoercePtrUPP ``` |
| To | ``` func NewAECoercePtrUPP(_ userRoutine: AECoercePtrProcPtr!) -> AECoercePtrUPP! ``` |

Modified [NewAEDisposeExternalUPP(_: AEDisposeExternalProcPtr!) -> AEDisposeExternalUPP!](https://developer.apple.com/documentation/coreservices/1447774-newaedisposeexternalupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewAEDisposeExternalUPP(_ userRoutine: AEDisposeExternalProcPtr) -> AEDisposeExternalUPP ``` |
| To | ``` func NewAEDisposeExternalUPP(_ userRoutine: AEDisposeExternalProcPtr!) -> AEDisposeExternalUPP! ``` |

Modified [NewAEEventHandlerUPP(_: AEEventHandlerProcPtr!) -> AEEventHandlerUPP!](https://developer.apple.com/documentation/coreservices/1446862-newaeeventhandlerupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewAEEventHandlerUPP(_ userRoutine: AEEventHandlerProcPtr) -> AEEventHandlerUPP ``` |
| To | ``` func NewAEEventHandlerUPP(_ userRoutine: AEEventHandlerProcPtr!) -> AEEventHandlerUPP! ``` |

Modified [NewOSLAccessorUPP(_: OSLAccessorProcPtr!) -> OSLAccessorUPP!](https://developer.apple.com/documentation/coreservices/1449584-newoslaccessorupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewOSLAccessorUPP(_ userRoutine: OSLAccessorProcPtr) -> OSLAccessorUPP ``` |
| To | ``` func NewOSLAccessorUPP(_ userRoutine: OSLAccessorProcPtr!) -> OSLAccessorUPP! ``` |

Modified [NewOSLAdjustMarksUPP(_: OSLAdjustMarksProcPtr!) -> OSLAdjustMarksUPP!](https://developer.apple.com/documentation/coreservices/1443347-newosladjustmarksupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewOSLAdjustMarksUPP(_ userRoutine: OSLAdjustMarksProcPtr) -> OSLAdjustMarksUPP ``` |
| To | ``` func NewOSLAdjustMarksUPP(_ userRoutine: OSLAdjustMarksProcPtr!) -> OSLAdjustMarksUPP! ``` |

Modified [NewOSLCompareUPP(_: OSLCompareProcPtr!) -> OSLCompareUPP!](https://developer.apple.com/documentation/coreservices/1444603-newoslcompareupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewOSLCompareUPP(_ userRoutine: OSLCompareProcPtr) -> OSLCompareUPP ``` |
| To | ``` func NewOSLCompareUPP(_ userRoutine: OSLCompareProcPtr!) -> OSLCompareUPP! ``` |

Modified [NewOSLCountUPP(_: OSLCountProcPtr!) -> OSLCountUPP!](https://developer.apple.com/documentation/coreservices/1448156-newoslcountupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewOSLCountUPP(_ userRoutine: OSLCountProcPtr) -> OSLCountUPP ``` |
| To | ``` func NewOSLCountUPP(_ userRoutine: OSLCountProcPtr!) -> OSLCountUPP! ``` |

Modified [NewOSLDisposeTokenUPP(_: OSLDisposeTokenProcPtr!) -> OSLDisposeTokenUPP!](https://developer.apple.com/documentation/coreservices/1450027-newosldisposetokenupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewOSLDisposeTokenUPP(_ userRoutine: OSLDisposeTokenProcPtr) -> OSLDisposeTokenUPP ``` |
| To | ``` func NewOSLDisposeTokenUPP(_ userRoutine: OSLDisposeTokenProcPtr!) -> OSLDisposeTokenUPP! ``` |

Modified [NewOSLGetErrDescUPP(_: OSLGetErrDescProcPtr!) -> OSLGetErrDescUPP!](https://developer.apple.com/documentation/coreservices/1447934-newoslgeterrdescupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewOSLGetErrDescUPP(_ userRoutine: OSLGetErrDescProcPtr) -> OSLGetErrDescUPP ``` |
| To | ``` func NewOSLGetErrDescUPP(_ userRoutine: OSLGetErrDescProcPtr!) -> OSLGetErrDescUPP! ``` |

Modified [NewOSLGetMarkTokenUPP(_: OSLGetMarkTokenProcPtr!) -> OSLGetMarkTokenUPP!](https://developer.apple.com/documentation/coreservices/1445166-newoslgetmarktokenupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewOSLGetMarkTokenUPP(_ userRoutine: OSLGetMarkTokenProcPtr) -> OSLGetMarkTokenUPP ``` |
| To | ``` func NewOSLGetMarkTokenUPP(_ userRoutine: OSLGetMarkTokenProcPtr!) -> OSLGetMarkTokenUPP! ``` |

Modified [NewOSLMarkUPP(_: OSLMarkProcPtr!) -> OSLMarkUPP!](https://developer.apple.com/documentation/coreservices/1446942-newoslmarkupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewOSLMarkUPP(_ userRoutine: OSLMarkProcPtr) -> OSLMarkUPP ``` |
| To | ``` func NewOSLMarkUPP(_ userRoutine: OSLMarkProcPtr!) -> OSLMarkUPP! ``` |

Modified [OSLAccessorProcPtr](https://developer.apple.com/documentation/coreservices/oslaccessorprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLAccessorProcPtr = CFunctionPointer<((DescType, UnsafePointer<AEDesc>, DescType, DescType, UnsafePointer<AEDesc>, UnsafeMutablePointer<AEDesc>, SRefCon) -> OSErr)> ``` |
| To | ``` typealias OSLAccessorProcPtr = (DescType, UnsafePointer<AEDesc>, DescType, DescType, UnsafePointer<AEDesc>, UnsafeMutablePointer<AEDesc>, SRefCon) -> OSErr ``` |

Modified [OSLAdjustMarksProcPtr](https://developer.apple.com/documentation/coreservices/osladjustmarksprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLAdjustMarksProcPtr = CFunctionPointer<((Int, Int, UnsafePointer<AEDesc>) -> OSErr)> ``` |
| To | ``` typealias OSLAdjustMarksProcPtr = (Int, Int, UnsafePointer<AEDesc>) -> OSErr ``` |

Modified [OSLCompareProcPtr](https://developer.apple.com/documentation/coreservices/oslcompareprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLCompareProcPtr = CFunctionPointer<((DescType, UnsafePointer<AEDesc>, UnsafePointer<AEDesc>, UnsafeMutablePointer<Boolean>) -> OSErr)> ``` |
| To | ``` typealias OSLCompareProcPtr = (DescType, UnsafePointer<AEDesc>, UnsafePointer<AEDesc>, UnsafeMutablePointer<DarwinBoolean>) -> OSErr ``` |

Modified [OSLCountProcPtr](https://developer.apple.com/documentation/coreservices/oslcountprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLCountProcPtr = CFunctionPointer<((DescType, DescType, UnsafePointer<AEDesc>, UnsafeMutablePointer<Int>) -> OSErr)> ``` |
| To | ``` typealias OSLCountProcPtr = (DescType, DescType, UnsafePointer<AEDesc>, UnsafeMutablePointer<Int>) -> OSErr ``` |

Modified [OSLDisposeTokenProcPtr](https://developer.apple.com/documentation/coreservices/osldisposetokenprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLDisposeTokenProcPtr = CFunctionPointer<((UnsafeMutablePointer<AEDesc>) -> OSErr)> ``` |
| To | ``` typealias OSLDisposeTokenProcPtr = (UnsafeMutablePointer<AEDesc>) -> OSErr ``` |

Modified [OSLGetErrDescProcPtr](https://developer.apple.com/documentation/coreservices/oslgeterrdescprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLGetErrDescProcPtr = CFunctionPointer<((UnsafeMutablePointer<UnsafeMutablePointer<AEDesc>>) -> OSErr)> ``` |
| To | ``` typealias OSLGetErrDescProcPtr = (UnsafeMutablePointer<UnsafeMutablePointer<AEDesc>>) -> OSErr ``` |

Modified [OSLGetMarkTokenProcPtr](https://developer.apple.com/documentation/coreservices/oslgetmarktokenprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLGetMarkTokenProcPtr = CFunctionPointer<((UnsafePointer<AEDesc>, DescType, UnsafeMutablePointer<AEDesc>) -> OSErr)> ``` |
| To | ``` typealias OSLGetMarkTokenProcPtr = (UnsafePointer<AEDesc>, DescType, UnsafeMutablePointer<AEDesc>) -> OSErr ``` |

Modified [OSLMarkProcPtr](https://developer.apple.com/documentation/coreservices/oslmarkprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias OSLMarkProcPtr = CFunctionPointer<((UnsafePointer<AEDesc>, UnsafePointer<AEDesc>, Int) -> OSErr)> ``` |
| To | ``` typealias OSLMarkProcPtr = (UnsafePointer<AEDesc>, UnsafePointer<AEDesc>, Int) -> OSErr ``` |

Modified [SetCustomIconsEnabled(_: Int16, _: Bool) -> OSErr](https://developer.apple.com/documentation/coreservices/1449302-setcustomiconsenabled)

|  | Declaration |
| --- | --- |
| From | ``` func SetCustomIconsEnabled(_ vRefNum: Int16, _ enableCustomIcons: Boolean) -> OSErr ``` |
| To | ``` func SetCustomIconsEnabled(_ vRefNum: Int16, _ enableCustomIcons: Bool) -> OSErr ``` |

Modified [SKIndexAddDocument(_: SKIndex!, _: SKDocument!, _: CFString!, _: Bool) -> Bool](https://developer.apple.com/documentation/coreservices/1444897-skindexadddocument)

|  | Declaration |
| --- | --- |
| From | ``` func SKIndexAddDocument(_ inIndex: SKIndex!, _ inDocument: SKDocument!, _ inMIMETypeHint: CFString!, _ inCanReplace: Boolean) -> Boolean ``` |
| To | ``` func SKIndexAddDocument(_ inIndex: SKIndex!, _ inDocument: SKDocument!, _ inMIMETypeHint: CFString!, _ inCanReplace: Bool) -> Bool ``` |

Modified [SKIndexAddDocumentWithText(_: SKIndex!, _: SKDocument!, _: CFString!, _: Bool) -> Bool](https://developer.apple.com/documentation/coreservices/1444518-skindexadddocumentwithtext)

|  | Declaration |
| --- | --- |
| From | ``` func SKIndexAddDocumentWithText(_ inIndex: SKIndex!, _ inDocument: SKDocument!, _ inDocumentText: CFString!, _ inCanReplace: Boolean) -> Boolean ``` |
| To | ``` func SKIndexAddDocumentWithText(_ inIndex: SKIndex!, _ inDocument: SKDocument!, _ inDocumentText: CFString!, _ inCanReplace: Bool) -> Bool ``` |

Modified [SKIndexCompact(_: SKIndex!) -> Bool](https://developer.apple.com/documentation/coreservices/1443628-skindexcompact)

|  | Declaration |
| --- | --- |
| From | ``` func SKIndexCompact(_ inIndex: SKIndex!) -> Boolean ``` |
| To | ``` func SKIndexCompact(_ inIndex: SKIndex!) -> Bool ``` |

Modified [SKIndexFlush(_: SKIndex!) -> Bool](https://developer.apple.com/documentation/coreservices/1450667-skindexflush)

|  | Declaration |
| --- | --- |
| From | ``` func SKIndexFlush(_ inIndex: SKIndex!) -> Boolean ``` |
| To | ``` func SKIndexFlush(_ inIndex: SKIndex!) -> Bool ``` |

Modified [SKIndexMoveDocument(_: SKIndex!, _: SKDocument!, _: SKDocument!) -> Bool](https://developer.apple.com/documentation/coreservices/1449899-skindexmovedocument)

|  | Declaration |
| --- | --- |
| From | ``` func SKIndexMoveDocument(_ inIndex: SKIndex!, _ inDocument: SKDocument!, _ inNewParent: SKDocument!) -> Boolean ``` |
| To | ``` func SKIndexMoveDocument(_ inIndex: SKIndex!, _ inDocument: SKDocument!, _ inNewParent: SKDocument!) -> Bool ``` |

Modified [SKIndexOpenWithURL(_: CFURL!, _: CFString!, _: Bool) -> Unmanaged<SKIndex>!](https://developer.apple.com/documentation/coreservices/1449017-skindexopenwithurl)

|  | Declaration |
| --- | --- |
| From | ``` func SKIndexOpenWithURL(_ inURL: CFURL!, _ inIndexName: CFString!, _ inWriteAccess: Boolean) -> Unmanaged<SKIndex>! ``` |
| To | ``` func SKIndexOpenWithURL(_ inURL: CFURL!, _ inIndexName: CFString!, _ inWriteAccess: Bool) -> Unmanaged<SKIndex>! ``` |

Modified [SKIndexRemoveDocument(_: SKIndex!, _: SKDocument!) -> Bool](https://developer.apple.com/documentation/coreservices/1444375-skindexremovedocument)

|  | Declaration |
| --- | --- |
| From | ``` func SKIndexRemoveDocument(_ inIndex: SKIndex!, _ inDocument: SKDocument!) -> Boolean ``` |
| To | ``` func SKIndexRemoveDocument(_ inIndex: SKIndex!, _ inDocument: SKDocument!) -> Bool ``` |

Modified [SKIndexRenameDocument(_: SKIndex!, _: SKDocument!, _: CFString!) -> Bool](https://developer.apple.com/documentation/coreservices/1448935-skindexrenamedocument)

|  | Declaration |
| --- | --- |
| From | ``` func SKIndexRenameDocument(_ inIndex: SKIndex!, _ inDocument: SKDocument!, _ inNewName: CFString!) -> Boolean ``` |
| To | ``` func SKIndexRenameDocument(_ inIndex: SKIndex!, _ inDocument: SKDocument!, _ inNewName: CFString!) -> Bool ``` |

Modified [SKSearchFindMatches(_: SKSearch!, _: CFIndex, _: UnsafeMutablePointer<SKDocumentID>, _: UnsafeMutablePointer<Float>, _: CFTimeInterval, _: UnsafeMutablePointer<CFIndex>) -> Bool](https://developer.apple.com/documentation/coreservices/1448608-sksearchfindmatches)

|  | Declaration |
| --- | --- |
| From | ``` func SKSearchFindMatches(_ inSearch: SKSearch!, _ inMaximumCount: CFIndex, _ outDocumentIDsArray: UnsafeMutablePointer<SKDocumentID>, _ outScoresArray: UnsafeMutablePointer<Float>, _ maximumTime: CFTimeInterval, _ outFoundCount: UnsafeMutablePointer<CFIndex>) -> Boolean ``` |
| To | ``` func SKSearchFindMatches(_ inSearch: SKSearch!, _ inMaximumCount: CFIndex, _ outDocumentIDsArray: UnsafeMutablePointer<SKDocumentID>, _ outScoresArray: UnsafeMutablePointer<Float>, _ maximumTime: CFTimeInterval, _ outFoundCount: UnsafeMutablePointer<CFIndex>) -> Bool ``` |

Modified [SKSearchResultsFilterCallBack](https://developer.apple.com/documentation/coreservices/sksearchresultsfiltercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias SKSearchResultsFilterCallBack = CFunctionPointer<((SKIndex!, SKDocument!, UnsafeMutablePointer<Void>) -> Boolean)> ``` |
| To | ``` typealias SKSearchResultsFilterCallBack = (SKIndex!, SKDocument!, UnsafeMutablePointer<Void>) -> DarwinBoolean ``` |

Modified [UTCreateStringForOSType(_: OSType) -> Unmanaged<CFString>](https://developer.apple.com/documentation/coreservices/1442804-utcreatestringforostype)

|  | Declaration |
| --- | --- |
| From | ``` func UTCreateStringForOSType(_ inOSType: OSType) -> Unmanaged<CFString>! ``` |
| To | ``` func UTCreateStringForOSType(_ inOSType: OSType) -> Unmanaged<CFString> ``` |

Modified [UTGetOSTypeFromString(_: CFString) -> OSType](https://developer.apple.com/documentation/coreservices/1450472-utgetostypefromstring)

|  | Declaration |
| --- | --- |
| From | ``` func UTGetOSTypeFromString(_ inString: CFString!) -> OSType ``` |
| To | ``` func UTGetOSTypeFromString(_ inString: CFString) -> OSType ``` |

Modified [UTTypeConformsTo(_: CFString, _: CFString) -> Bool](https://developer.apple.com/documentation/coreservices/1444079-uttypeconformsto)

|  | Declaration |
| --- | --- |
| From | ``` func UTTypeConformsTo(_ inUTI: CFString!, _ inConformsToUTI: CFString!) -> Boolean ``` |
| To | ``` func UTTypeConformsTo(_ inUTI: CFString, _ inConformsToUTI: CFString) -> Bool ``` |

Modified [UTTypeCopyAllTagsWithClass(_: CFString, _: CFString) -> Unmanaged<CFArray>?](https://developer.apple.com/documentation/coreservices/1448473-uttypecopyalltagswithclass)

|  | Declaration |
| --- | --- |
| From | ``` func UTTypeCopyAllTagsWithClass(_ inUTI: CFString!, _ inTagClass: CFString!) -> Unmanaged<CFArray>! ``` |
| To | ``` func UTTypeCopyAllTagsWithClass(_ inUTI: CFString, _ inTagClass: CFString) -> Unmanaged<CFArray>? ``` |

Modified [UTTypeCopyDeclaration(_: CFString) -> Unmanaged<CFDictionary>?](https://developer.apple.com/documentation/coreservices/1442505-uttypecopydeclaration)

|  | Declaration |
| --- | --- |
| From | ``` func UTTypeCopyDeclaration(_ inUTI: CFString!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func UTTypeCopyDeclaration(_ inUTI: CFString) -> Unmanaged<CFDictionary>? ``` |

Modified [UTTypeCopyDeclaringBundleURL(_: CFString) -> Unmanaged<CFURL>?](https://developer.apple.com/documentation/coreservices/1447781-uttypecopydeclaringbundleurl)

|  | Declaration |
| --- | --- |
| From | ``` func UTTypeCopyDeclaringBundleURL(_ inUTI: CFString!) -> Unmanaged<CFURL>! ``` |
| To | ``` func UTTypeCopyDeclaringBundleURL(_ inUTI: CFString) -> Unmanaged<CFURL>? ``` |

Modified [UTTypeCopyDescription(_: CFString) -> Unmanaged<CFString>?](https://developer.apple.com/documentation/coreservices/1448514-uttypecopydescription)

|  | Declaration |
| --- | --- |
| From | ``` func UTTypeCopyDescription(_ inUTI: CFString!) -> Unmanaged<CFString>! ``` |
| To | ``` func UTTypeCopyDescription(_ inUTI: CFString) -> Unmanaged<CFString>? ``` |

Modified [UTTypeCopyPreferredTagWithClass(_: CFString, _: CFString) -> Unmanaged<CFString>?](https://developer.apple.com/documentation/coreservices/1442744-uttypecopypreferredtagwithclass)

|  | Declaration |
| --- | --- |
| From | ``` func UTTypeCopyPreferredTagWithClass(_ inUTI: CFString!, _ inTagClass: CFString!) -> Unmanaged<CFString>! ``` |
| To | ``` func UTTypeCopyPreferredTagWithClass(_ inUTI: CFString, _ inTagClass: CFString) -> Unmanaged<CFString>? ``` |

Modified [UTTypeCreateAllIdentifiersForTag(_: CFString, _: CFString, _: CFString?) -> Unmanaged<CFArray>?](https://developer.apple.com/documentation/coreservices/1447261-uttypecreateallidentifiersfortag)

|  | Declaration |
| --- | --- |
| From | ``` func UTTypeCreateAllIdentifiersForTag(_ inTagClass: CFString!, _ inTag: CFString!, _ inConformingToUTI: CFString!) -> Unmanaged<CFArray>! ``` |
| To | ``` func UTTypeCreateAllIdentifiersForTag(_ inTagClass: CFString, _ inTag: CFString, _ inConformingToUTI: CFString?) -> Unmanaged<CFArray>? ``` |

Modified [UTTypeCreatePreferredIdentifierForTag(_: CFString, _: CFString, _: CFString?) -> Unmanaged<CFString>?](https://developer.apple.com/documentation/coreservices/1448939-uttypecreatepreferredidentifierf)

|  | Declaration |
| --- | --- |
| From | ``` func UTTypeCreatePreferredIdentifierForTag(_ inTagClass: CFString!, _ inTag: CFString!, _ inConformingToUTI: CFString!) -> Unmanaged<CFString>! ``` |
| To | ``` func UTTypeCreatePreferredIdentifierForTag(_ inTagClass: CFString, _ inTag: CFString, _ inConformingToUTI: CFString?) -> Unmanaged<CFString>? ``` |

Modified [UTTypeEqual(_: CFString, _: CFString) -> Bool](https://developer.apple.com/documentation/coreservices/1447783-uttypeequal)

|  | Declaration |
| --- | --- |
| From | ``` func UTTypeEqual(_ inUTI1: CFString!, _ inUTI2: CFString!) -> Boolean ``` |
| To | ``` func UTTypeEqual(_ inUTI1: CFString, _ inUTI2: CFString) -> Bool ``` |

Modified [UTTypeIsDeclared(_: CFString) -> Bool](https://developer.apple.com/documentation/coreservices/1450352-uttypeisdeclared)

|  | Declaration |
| --- | --- |
| From | ``` func UTTypeIsDeclared(_ inUTI: CFString!) -> Boolean ``` |
| To | ``` func UTTypeIsDeclared(_ inUTI: CFString) -> Bool ``` |

Modified [UTTypeIsDynamic(_: CFString) -> Bool](https://developer.apple.com/documentation/coreservices/1442980-uttypeisdynamic)

|  | Declaration |
| --- | --- |
| From | ``` func UTTypeIsDynamic(_ inUTI: CFString!) -> Boolean ``` |
| To | ``` func UTTypeIsDynamic(_ inUTI: CFString) -> Bool ``` |

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
