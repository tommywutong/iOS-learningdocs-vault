---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/CoreServices.html
archived_at: '2026-07-15T07:34:45.274922Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# CoreServices Changes

## CoreServices

AEDataModel.hRemoved AEInitializeDescInline()Added #def AEInitializeDescInlineAdded #def DisposeAECoerceDescUPPAdded #def DisposeAECoercePtrUPPAdded #def DisposeAEDisposeExternalUPPAdded #def DisposeAEEventHandlerUPPAdded #def InvokeAECoerceDescUPPAdded #def InvokeAECoercePtrUPPAdded #def InvokeAEDisposeExternalUPPAdded #def InvokeAEEventHandlerUPPAdded #def NewAECoerceDescUPPAdded #def NewAECoercePtrUPPAdded #def NewAEDisposeExternalUPPAdded #def NewAEEventHandlerUPPAEObjects.hAdded #def DisposeOSLAccessorUPPAdded #def DisposeOSLAdjustMarksUPPAdded #def DisposeOSLCompareUPPAdded #def DisposeOSLCountUPPAdded #def DisposeOSLDisposeTokenUPPAdded #def DisposeOSLGetErrDescUPPAdded #def DisposeOSLGetMarkTokenUPPAdded #def DisposeOSLMarkUPPAdded #def InvokeOSLAccessorUPPAdded #def InvokeOSLAdjustMarksUPPAdded #def InvokeOSLCompareUPPAdded #def InvokeOSLCountUPPAdded #def InvokeOSLDisposeTokenUPPAdded #def InvokeOSLGetErrDescUPPAdded #def InvokeOSLGetMarkTokenUPPAdded #def InvokeOSLMarkUPPAdded #def NewOSLAccessorUPPAdded #def NewOSLAdjustMarksUPPAdded #def NewOSLCompareUPPAdded #def NewOSLCountUPPAdded #def NewOSLDisposeTokenUPPAdded #def NewOSLGetErrDescUPPAdded #def NewOSLGetMarkTokenUPPAdded #def NewOSLMarkUPPAVLTree.hAdded #def DisposeAVLCompareItemsUPPAdded #def DisposeAVLDisposeItemUPPAdded #def DisposeAVLItemSizeUPPAdded #def DisposeAVLWalkUPPAdded #def InvokeAVLCompareItemsUPPAdded #def InvokeAVLDisposeItemUPPAdded #def InvokeAVLItemSizeUPPAdded #def InvokeAVLWalkUPPAdded #def NewAVLCompareItemsUPPAdded #def NewAVLDisposeItemUPPAdded #def NewAVLItemSizeUPPAdded #def NewAVLWalkUPPAliases.hAdded #def DisposeAliasFilterUPPAdded #def InvokeAliasFilterUPPAdded #def NewAliasFilterUPPCollections.hAdded #def DisposeCollectionExceptionUPPAdded #def DisposeCollectionFlattenUPPAdded #def InvokeCollectionExceptionUPPAdded #def InvokeCollectionFlattenUPPAdded #def NewCollectionExceptionUPPAdded #def NewCollectionFlattenUPPComponents.hAdded #def DisposeComponentMPWorkFunctionUPPAdded #def DisposeComponentRoutineUPPAdded #def DisposeGetMissingComponentResourceUPPAdded #def InvokeComponentMPWorkFunctionUPPAdded #def InvokeComponentRoutineUPPAdded #def InvokeGetMissingComponentResourceUPPAdded #def NewComponentMPWorkFunctionUPPAdded #def NewComponentRoutineUPPAdded #def NewGetMissingComponentResourceUPPDebugging.hAdded #def DisposeDebugAssertOutputHandlerUPPAdded #def DisposeDebugComponentCallbackUPPAdded #def InvokeDebugAssertOutputHandlerUPPAdded #def InvokeDebugComponentCallbackUPPAdded #def NewDebugAssertOutputHandlerUPPAdded #def NewDebugComponentCallbackUPPFSEvents.h (Removed)FSEvents.h (Added)Modified [ConstFSEventStreamRef](https://developer.apple.com/documentation/coreservices/constfseventstreamref)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamCallback](https://developer.apple.com/documentation/coreservices/fseventstreamcallback)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamContext](https://developer.apple.com/documentation/coreservices/fseventstreamcontext)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamCopyDescription()](https://developer.apple.com/documentation/coreservices/1442676-fseventstreamcopydescription)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamCopyPathsBeingWatched()](https://developer.apple.com/documentation/coreservices/1447917-fseventstreamcopypathsbeingwatch)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamCreate()](https://developer.apple.com/documentation/coreservices/1443980-fseventstreamcreate)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamCreateFlags](https://developer.apple.com/documentation/coreservices/fseventstreamcreateflags)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamCreateRelativeToDevice()](https://developer.apple.com/documentation/coreservices/1447341-fseventstreamcreaterelativetodev)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamEventFlags](https://developer.apple.com/documentation/coreservices/fseventstreameventflags)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamEventId](https://developer.apple.com/documentation/coreservices/fseventstreameventid)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamFlushAsync()](https://developer.apple.com/documentation/coreservices/1441727-fseventstreamflushasync)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamFlushSync()](https://developer.apple.com/documentation/coreservices/1445629-fseventstreamflushsync)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamGetDeviceBeingWatched()](https://developer.apple.com/documentation/coreservices/1449675-fseventstreamgetdevicebeingwatch)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamGetLatestEventId()](https://developer.apple.com/documentation/coreservices/1446030-fseventstreamgetlatesteventid)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamInvalidate()](https://developer.apple.com/documentation/coreservices/1446990-fseventstreaminvalidate)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamRef](https://developer.apple.com/documentation/coreservices/fseventstreamref)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamRelease()](https://developer.apple.com/documentation/coreservices/1445989-fseventstreamrelease)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamRetain()](https://developer.apple.com/documentation/coreservices/1444986-fseventstreamretain)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamScheduleWithRunLoop()](https://developer.apple.com/documentation/coreservices/1447824-fseventstreamschedulewithrunloop)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamSetDispatchQueue()](https://developer.apple.com/documentation/coreservices/1444164-fseventstreamsetdispatchqueue)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamSetExclusionPaths()](https://developer.apple.com/documentation/coreservices/1444666-fseventstreamsetexclusionpaths)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamShow()](https://developer.apple.com/documentation/coreservices/1444302-fseventstreamshow)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamStart()](https://developer.apple.com/documentation/coreservices/1448000-fseventstreamstart)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamStop()](https://developer.apple.com/documentation/coreservices/1447673-fseventstreamstop)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventStreamUnscheduleFromRunLoop()](https://developer.apple.com/documentation/coreservices/1441982-fseventstreamunschedulefromrunlo)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventsCopyUUIDForDevice()](https://developer.apple.com/documentation/coreservices/1444453-fseventscopyuuidfordevice)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventsGetCurrentEventId()](https://developer.apple.com/documentation/coreservices/1442917-fseventsgetcurrenteventid)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventsGetLastEventIdForDeviceBeforeTime()](https://developer.apple.com/documentation/coreservices/1449772-fseventsgetlasteventidfordeviceb)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [FSEventsPurgeEventsForDeviceUpToEventId()](https://developer.apple.com/documentation/coreservices/1447985-fseventspurgeeventsfordeviceupto)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamCreateFlagFileEvents](https://developer.apple.com/documentation/coreservices/1455376-fseventstreamcreateflags/kfseventstreamcreateflagfileevents)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamCreateFlagIgnoreSelf](https://developer.apple.com/documentation/coreservices/kfseventstreamcreateflagignoreself)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamCreateFlagMarkSelf](https://developer.apple.com/documentation/coreservices/1455376-fseventstreamcreateflags/kfseventstreamcreateflagmarkself)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamCreateFlagNoDefer](https://developer.apple.com/documentation/coreservices/1455376-fseventstreamcreateflags/kfseventstreamcreateflagnodefer)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamCreateFlagNone](https://developer.apple.com/documentation/coreservices/kfseventstreamcreateflagnone)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamCreateFlagUseCFTypes](https://developer.apple.com/documentation/coreservices/kfseventstreamcreateflagusecftypes)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamCreateFlagWatchRoot](https://developer.apple.com/documentation/coreservices/kfseventstreamcreateflagwatchroot)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagEventIdsWrapped](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflageventidswrapped)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagHistoryDone](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflaghistorydone)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagItemChangeOwner](https://developer.apple.com/documentation/coreservices/kfseventstreameventflagitemchangeowner)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagItemCreated](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflagitemcreated)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagItemFinderInfoMod](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflagitemfinderinfomod)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagItemInodeMetaMod](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflagiteminodemetamod)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagItemIsDir](https://developer.apple.com/documentation/coreservices/kfseventstreameventflagitemisdir)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagItemIsFile](https://developer.apple.com/documentation/coreservices/kfseventstreameventflagitemisfile)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagItemIsSymlink](https://developer.apple.com/documentation/coreservices/kfseventstreameventflagitemissymlink)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagItemModified](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflagitemmodified)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagItemRemoved](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflagitemremoved)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagItemRenamed](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflagitemrenamed)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagItemXattrMod](https://developer.apple.com/documentation/coreservices/kfseventstreameventflagitemxattrmod)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagKernelDropped](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflagkerneldropped)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagMount](https://developer.apple.com/documentation/coreservices/kfseventstreameventflagmount)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagMustScanSubDirs](https://developer.apple.com/documentation/coreservices/kfseventstreameventflagmustscansubdirs)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagNone](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflagnone)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagOwnEvent](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflagownevent)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagRootChanged](https://developer.apple.com/documentation/coreservices/kfseventstreameventflagrootchanged)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagUnmount](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflagunmount)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventFlagUserDropped](https://developer.apple.com/documentation/coreservices/kfseventstreameventflaguserdropped)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Modified [kFSEventStreamEventIdSinceNow](https://developer.apple.com/documentation/coreservices/kfseventstreameventidsincenow)

|  | Header |
| --- | --- |
| From | CarbonCore/FSEvents.h |
| To | FSEvents/FSEvents.h |

Files.hAdded #def DisposeFNSubscriptionUPPAdded [#def DisposeFSVolumeEjectUPP](https://developer.apple.com/documentation/coreservices/disposefsvolumeejectupp)Added [#def DisposeFSVolumeMountUPP](https://developer.apple.com/documentation/coreservices/disposefsvolumemountupp)Added [#def DisposeFSVolumeUnmountUPP](https://developer.apple.com/documentation/coreservices/disposefsvolumeunmountupp)Added #def DisposeIOCompletionUPPAdded #def InvokeFNSubscriptionUPPAdded #def InvokeFSVolumeEjectUPPAdded #def InvokeFSVolumeMountUPPAdded #def InvokeFSVolumeUnmountUPPAdded #def InvokeIOCompletionUPPAdded #def NewFNSubscriptionUPPAdded #def NewFSVolumeEjectUPPAdded #def NewFSVolumeMountUPPAdded #def NewFSVolumeUnmountUPPAdded #def NewIOCompletionUPPFolders.hAdded #def DisposeFolderManagerNotificationUPPAdded #def InvokeFolderManagerNotificationUPPAdded #def NewFolderManagerNotificationUPPGestalt.hAdded #def DisposeSelectorFunctionUPPAdded #def InvokeSelectorFunctionUPPAdded #def NewSelectorFunctionUPPModified [gestaltSystemVersion](https://developer.apple.com/documentation/coreservices/1470788-system_version_selectors/gestaltsystemversion)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.8 |

Modified [gestaltSystemVersionBugFix](https://developer.apple.com/documentation/coreservices/1470788-system_version_selectors/gestaltsystemversionbugfix)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.0 | OS X 10.8 |

Modified [gestaltSystemVersionMajor](https://developer.apple.com/documentation/coreservices/1470788-system_version_selectors/gestaltsystemversionmajor)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.0 | OS X 10.8 |

Modified [gestaltSystemVersionMinor](https://developer.apple.com/documentation/coreservices/1470788-system_version_selectors/gestaltsystemversionminor)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.0 | OS X 10.8 |

KeychainCore.hRemoved KeychainManagerAvailable()Added #def DisposeKCCallbackUPPAdded #def InvokeKCCallbackUPPAdded #def KeychainManagerAvailableAdded #def NewKCCallbackUPPLSInfo.hAdded [LSCopyApplicationURLsForBundleIdentifier()](https://developer.apple.com/documentation/coreservices/1449290-lscopyapplicationurlsforbundleid)Added [LSCopyDefaultApplicationURLForContentType()](https://developer.apple.com/documentation/coreservices/1447734-lscopydefaultapplicationurlforco)Added [LSCopyDefaultApplicationURLForURL()](https://developer.apple.com/documentation/coreservices/1448824-lscopydefaultapplicationurlforur)Modified [LSCanRefAcceptItem()](https://developer.apple.com/documentation/coreservices/1442183-lscanrefacceptitem)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSCopyApplicationForMIMEType()](https://developer.apple.com/documentation/coreservices/1448586-lscopyapplicationformimetype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSCopyDisplayNameForRef()](https://developer.apple.com/documentation/coreservices/1442576-lscopydisplaynameforref)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSCopyItemAttribute()](https://developer.apple.com/documentation/coreservices/1445023-lscopyitemattribute)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSCopyItemAttributes()](https://developer.apple.com/documentation/coreservices/1446078-lscopyitemattributes)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSCopyItemInfoForRef()](https://developer.apple.com/documentation/coreservices/1445227-lscopyiteminfoforref)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSCopyKindStringForMIMEType()](https://developer.apple.com/documentation/coreservices/1442446-lscopykindstringformimetype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSCopyKindStringForRef()](https://developer.apple.com/documentation/coreservices/1448593-lscopykindstringforref)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSCopyKindStringForTypeInfo()](https://developer.apple.com/documentation/coreservices/1446207-lscopykindstringfortypeinfo)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSFindApplicationForInfo()](https://developer.apple.com/documentation/coreservices/1449588-lsfindapplicationforinfo)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSGetApplicationForInfo()](https://developer.apple.com/documentation/coreservices/1449928-lsgetapplicationforinfo)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSGetApplicationForItem()](https://developer.apple.com/documentation/coreservices/1446185-lsgetapplicationforitem)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSGetApplicationForURL()](https://developer.apple.com/documentation/coreservices/1445210-lsgetapplicationforurl)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSRegisterFSRef()](https://developer.apple.com/documentation/coreservices/1444582-lsregisterfsref)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSSetExtensionHiddenForRef()](https://developer.apple.com/documentation/coreservices/1442766-lssetextensionhiddenforref)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSSetItemAttribute()](https://developer.apple.com/documentation/coreservices/1446733-lssetitemattribute)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [kLSItemContentType](https://developer.apple.com/documentation/coreservices/klsitemcontenttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [kLSItemDisplayKind](https://developer.apple.com/documentation/coreservices/klsitemdisplaykind)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [kLSItemDisplayName](https://developer.apple.com/documentation/coreservices/klsitemdisplayname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [kLSItemExtension](https://developer.apple.com/documentation/coreservices/klsitemextension)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [kLSItemExtensionIsHidden](https://developer.apple.com/documentation/coreservices/klsitemextensionishidden)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [kLSItemFileCreator](https://developer.apple.com/documentation/coreservices/klsitemfilecreator)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [kLSItemFileType](https://developer.apple.com/documentation/coreservices/klsitemfiletype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [kLSItemIsInvisible](https://developer.apple.com/documentation/coreservices/klsitemisinvisible)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [kLSItemQuarantineProperties](https://developer.apple.com/documentation/coreservices/klsitemquarantineproperties)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [kLSItemRoleHandlerDisplayName](https://developer.apple.com/documentation/coreservices/klsitemrolehandlerdisplayname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

LSOpen.hModified [LSApplicationParameters](https://developer.apple.com/documentation/coreservices/lsapplicationparameters)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSLaunchFSRefSpec](https://developer.apple.com/documentation/coreservices/lslaunchfsrefspec)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSOpenApplication()](https://developer.apple.com/documentation/coreservices/1447930-lsopenapplication)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSOpenFSRef()](https://developer.apple.com/documentation/coreservices/1445663-lsopenfsref)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSOpenFromRefSpec()](https://developer.apple.com/documentation/coreservices/1444466-lsopenfromrefspec)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSOpenItemsWithRole()](https://developer.apple.com/documentation/coreservices/1449783-lsopenitemswithrole)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSOpenURLsWithRole()](https://developer.apple.com/documentation/coreservices/1448184-lsopenurlswithrole)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

LSSharedFileList.hAdded [LSSharedFileListItemCopyResolvedURL()](https://developer.apple.com/documentation/coreservices/1449882-lssharedfilelistitemcopyresolved)Added [LSSharedFileListResolutionFlags](https://developer.apple.com/documentation/coreservices/lssharedfilelistresolutionflags)Modified [LSSharedFileListInsertItemFSRef()](https://developer.apple.com/documentation/coreservices/1449884-lssharedfilelistinsertitemfsref)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [LSSharedFileListItemResolve()](https://developer.apple.com/documentation/coreservices/1447347-lssharedfilelistitemresolve)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` OSStatus LSSharedFileListItemResolve (	LSSharedFileListItemRef inItem,	UInt32 inFlags,	CFURLRef *outURL,	FSRef *outRef); ``` | -- |
| To | ``` OSStatus LSSharedFileListItemResolve (	LSSharedFileListItemRef inItem,	LSSharedFileListResolutionFlags inFlags,	CFURLRef *outURL,	FSRef *outRef); ``` | OS X 10.10 |

MacErrors.hAdded [errOSACantStorePointers](https://developer.apple.com/documentation/coreservices/1559982-anonymous/errosacantstorepointers)MacMemory.hAdded #def DisposeGrowZoneUPPAdded #def DisposePurgeUPPAdded #def DisposeUserFnUPPAdded #def InvokeGrowZoneUPPAdded #def InvokePurgeUPPAdded #def InvokeUserFnUPPAdded #def NewGrowZoneUPPAdded #def NewPurgeUPPAdded #def NewUserFnUPPMachineExceptions.hAdded #def DisposeExceptionHandlerUPPAdded #def InvokeExceptionHandlerUPPAdded #def NewExceptionHandlerUPPOSUtils.hAdded #def DisposeDeferredTaskUPPAdded #def InvokeDeferredTaskUPPAdded #def NewDeferredTaskUPPModified [false32b](https://developer.apple.com/documentation/coreservices/1533306-anonymous/false32b)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.8 |

Modified [true32b](https://developer.apple.com/documentation/coreservices/1533306-anonymous/true32b)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.8 |

Power.hAdded #def DisposeSleepQUPPAdded #def InvokeSleepQUPPAdded #def NewSleepQUPPResources.hAdded #def DisposeResErrUPPAdded #def InvokeResErrUPPAdded #def NewResErrUPPSystemSound.hAdded #def DisposeSystemSoundCompletionUPPAdded #def InvokeSystemSoundCompletionUPPAdded #def NewSystemSoundCompletionUPPTextCommon.hAdded [kTextEncodingUnicodeV6_3](https://developer.apple.com/documentation/coreservices/1400188-unicode_and_iso_ucs_text_encodin/ktextencodingunicodev6_3)Added [kUCBidiCatFirstStrongIsolate](https://developer.apple.com/documentation/coreservices/1400035-bidirectional_character_values/kucbidicatfirststrongisolate)Added [kUCBidiCatLeftRightIsolate](https://developer.apple.com/documentation/coreservices/1400035-bidirectional_character_values/kucbidicatleftrightisolate)Added [kUCBidiCatPopDirectionalIsolate](https://developer.apple.com/documentation/coreservices/1400035-bidirectional_character_values/kucbidicatpopdirectionalisolate)Added [kUCBidiCatRightLeftIsolate](https://developer.apple.com/documentation/coreservices/1400035-bidirectional_character_values/kucbidicatrightleftisolate)Threads.hAdded #def DisposeDebuggerDisposeThreadUPPAdded #def DisposeDebuggerNewThreadUPPAdded #def DisposeDebuggerThreadSchedulerUPPAdded #def DisposeThreadEntryUPPAdded #def DisposeThreadSchedulerUPPAdded #def DisposeThreadSwitchUPPAdded #def DisposeThreadTerminationUPPAdded #def InvokeDebuggerDisposeThreadUPPAdded #def InvokeDebuggerNewThreadUPPAdded #def InvokeDebuggerThreadSchedulerUPPAdded #def InvokeThreadEntryUPPAdded #def InvokeThreadSchedulerUPPAdded #def InvokeThreadSwitchUPPAdded #def InvokeThreadTerminationUPPAdded #def NewDebuggerDisposeThreadUPPAdded #def NewDebuggerNewThreadUPPAdded #def NewDebuggerThreadSchedulerUPPAdded #def NewThreadEntryUPPAdded #def NewThreadSchedulerUPPAdded #def NewThreadSwitchUPPAdded #def NewThreadTerminationUPPTimer.hAdded #def DisposeTimerUPPAdded #def InvokeTimerUPPAdded #def NewTimerUPPUTCoreTypes.hAdded [kUTType3DContent](https://developer.apple.com/documentation/coreservices/kuttype3dcontent)Added [kUTTypeAVIMovie](https://developer.apple.com/documentation/coreservices/kuttypeavimovie)Added [kUTTypeAppleProtectedMPEG4Video](https://developer.apple.com/documentation/coreservices/kuttypeappleprotectedmpeg4video)Added [kUTTypeAppleScript](https://developer.apple.com/documentation/coreservices/kuttypeapplescript)Added [kUTTypeAssemblyLanguageSource](https://developer.apple.com/documentation/coreservices/kuttypeassemblylanguagesource)Added [kUTTypeAudioInterchangeFileFormat](https://developer.apple.com/documentation/coreservices/kuttypeaudiointerchangefileformat)Added [kUTTypeBinaryPropertyList](https://developer.apple.com/documentation/coreservices/kuttypebinarypropertylist)Added [kUTTypeBookmark](https://developer.apple.com/documentation/coreservices/kuttypebookmark)Added [kUTTypeBzip2Archive](https://developer.apple.com/documentation/coreservices/kuttypebzip2archive)Added [kUTTypeCalendarEvent](https://developer.apple.com/documentation/coreservices/kuttypecalendarevent)Added [kUTTypeCommaSeparatedText](https://developer.apple.com/documentation/coreservices/kuttypecommaseparatedtext)Added [kUTTypeDatabase](https://developer.apple.com/documentation/coreservices/kuttypedatabase)Added [kUTTypeDelimitedText](https://developer.apple.com/documentation/coreservices/kuttypedelimitedtext)Added [kUTTypeElectronicPublication](https://developer.apple.com/documentation/coreservices/kuttypeelectronicpublication)Added [kUTTypeEmailMessage](https://developer.apple.com/documentation/coreservices/kuttypeemailmessage)Added [kUTTypeExecutable](https://developer.apple.com/documentation/coreservices/kuttypeexecutable)Added [kUTTypeFont](https://developer.apple.com/documentation/coreservices/kuttypefont)Added [kUTTypeGNUZipArchive](https://developer.apple.com/documentation/coreservices/kuttypegnuziparchive)Added [kUTTypeInternetLocation](https://developer.apple.com/documentation/coreservices/kuttypeinternetlocation)Added [kUTTypeJSON](https://developer.apple.com/documentation/coreservices/kuttypejson)Added [kUTTypeJavaArchive](https://developer.apple.com/documentation/coreservices/kuttypejavaarchive)Added [kUTTypeJavaClass](https://developer.apple.com/documentation/coreservices/kuttypejavaclass)Added [kUTTypeJavaScript](https://developer.apple.com/documentation/coreservices/kuttypejavascript)Added [kUTTypeLog](https://developer.apple.com/documentation/coreservices/kuttypelog)Added [kUTTypeM3UPlaylist](https://developer.apple.com/documentation/coreservices/kuttypem3uplaylist)Added [kUTTypeMIDIAudio](https://developer.apple.com/documentation/coreservices/kuttypemidiaudio)Added [kUTTypeMPEG2TransportStream](https://developer.apple.com/documentation/coreservices/kuttypempeg2transportstream)Added [kUTTypeMPEG2Video](https://developer.apple.com/documentation/coreservices/kuttypempeg2video)Added [kUTTypeOSAScript](https://developer.apple.com/documentation/coreservices/kuttypeosascript)Added [kUTTypeOSAScriptBundle](https://developer.apple.com/documentation/coreservices/kuttypeosascriptbundle)Added [kUTTypePHPScript](https://developer.apple.com/documentation/coreservices/kuttypephpscript)Added [kUTTypePKCS12](https://developer.apple.com/documentation/coreservices/kuttypepkcs12)Added [kUTTypePerlScript](https://developer.apple.com/documentation/coreservices/kuttypeperlscript)Added [kUTTypePlaylist](https://developer.apple.com/documentation/coreservices/kuttypeplaylist)Added [kUTTypePluginBundle](https://developer.apple.com/documentation/coreservices/kuttypepluginbundle)Added [kUTTypePresentation](https://developer.apple.com/documentation/coreservices/kuttypepresentation)Added [kUTTypePropertyList](https://developer.apple.com/documentation/coreservices/kuttypepropertylist)Added [kUTTypePythonScript](https://developer.apple.com/documentation/coreservices/kuttypepythonscript)Added [kUTTypeQuickLookGenerator](https://developer.apple.com/documentation/coreservices/kuttypequicklookgenerator)Added [kUTTypeRawImage](https://developer.apple.com/documentation/coreservices/kuttyperawimage)Added [kUTTypeRubyScript](https://developer.apple.com/documentation/coreservices/kuttyperubyscript)Added [kUTTypeScalableVectorGraphics](https://developer.apple.com/documentation/coreservices/kuttypescalablevectorgraphics)Added [kUTTypeScript](https://developer.apple.com/documentation/coreservices/kuttypescript)Added [kUTTypeShellScript](https://developer.apple.com/documentation/coreservices/kuttypeshellscript)Added [kUTTypeSpotlightImporter](https://developer.apple.com/documentation/coreservices/kuttypespotlightimporter)Added [kUTTypeSpreadsheet](https://developer.apple.com/documentation/coreservices/kuttypespreadsheet)Added [kUTTypeSystemPreferencesPane](https://developer.apple.com/documentation/coreservices/kuttypesystempreferencespane)Added [kUTTypeTabSeparatedText](https://developer.apple.com/documentation/coreservices/kuttypetabseparatedtext)Added [kUTTypeToDoItem](https://developer.apple.com/documentation/coreservices/kuttypetodoitem)Added [kUTTypeURLBookmarkData](https://developer.apple.com/documentation/coreservices/kuttypeurlbookmarkdata)Added [kUTTypeUTF8TabSeparatedText](https://developer.apple.com/documentation/coreservices/kuttypeutf8tabseparatedtext)Added [kUTTypeUnixExecutable](https://developer.apple.com/documentation/coreservices/kuttypeunixexecutable)Added [kUTTypeWaveformAudio](https://developer.apple.com/documentation/coreservices/kuttypewaveformaudio)Added [kUTTypeWindowsExecutable](https://developer.apple.com/documentation/coreservices/kuttypewindowsexecutable)Added [kUTTypeX509Certificate](https://developer.apple.com/documentation/coreservices/kuttypex509certificate)Added [kUTTypeXMLPropertyList](https://developer.apple.com/documentation/coreservices/kuttypexmlpropertylist)Added [kUTTypeXPCService](https://developer.apple.com/documentation/coreservices/kuttypexpcservice)Added [kUTTypeZipArchive](https://developer.apple.com/documentation/coreservices/kuttypeziparchive)UTType.hAdded [UTTypeCopyAllTagsWithClass()](https://developer.apple.com/documentation/coreservices/1448473-uttypecopyalltagswithclass)Added [UTTypeIsDeclared()](https://developer.apple.com/documentation/coreservices/1450352-uttypeisdeclared)Added [UTTypeIsDynamic()](https://developer.apple.com/documentation/coreservices/1442980-uttypeisdynamic)UnicodeConverter.hAdded #def DisposeUnicodeToTextFallbackUPPAdded #def InvokeUnicodeToTextFallbackUPPAdded #def NewUnicodeToTextFallbackUPPUnicodeUtilities.hAdded #def DisposeIndexToUCStringUPPAdded #def InvokeIndexToUCStringUPPAdded #def NewIndexToUCStringUPP

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
