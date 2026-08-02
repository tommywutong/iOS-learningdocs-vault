---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/CoreServices.html
archived_at: '2026-07-18T02:54:27.271356Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# CoreServices Changes

## CoreServices

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

AEDataModel.hAdded [kAEDoNotAutomaticallyAddAnnotationsToEvent](https://developer.apple.com/documentation/coreservices/1542914-anonymous/kaedonotautomaticallyaddannotationstoevent)AERegistry.hAdded [kAEQuitPreserveState](https://developer.apple.com/documentation/coreservices/1556363-anonymous/kaequitpreservestate)AppleDiskPartitions.hRemoved [Block0](https://developer.apple.com/documentation/kernel/block0)Removed [DDMap](https://developer.apple.com/documentation/kernel/ddmap)Removed PartitionRemoved kATADriverSignatureRemoved kATAPIDriverSignatureRemoved kDriveSetupHFSSignatureRemoved kDriverTypeMacATARemoved kDriverTypeMacATAChainedRemoved kDriverTypeMacSCSIRemoved kDriverTypeMacSCSIChainedRemoved kPartitionAUXIsAllocatedRemoved kPartitionAUXIsBootCodePositionIndependentRemoved kPartitionAUXIsBootValidRemoved kPartitionAUXIsInUseRemoved kPartitionAUXIsReadableRemoved kPartitionAUXIsValidRemoved kPartitionAUXIsWriteableRemoved kPartitionCanChainToNextRemoved kPartitionIsChainCompatibleRemoved kPartitionIsMountedAtStartupRemoved kPartitionIsRealDeviceDriverRemoved kPartitionIsStartupRemoved kPartitionIsWriteableRemoved kPatchDriverSignatureRemoved kSCSICDDriverSignatureRemoved kSCSIDriverSignatureRemoved newPMSigWordRemoved oldPMSigWordRemoved pMapSIGRemoved pdSigWordRemoved sbMacRemoved sbSIGWordCFHTTPMessage.hAdded [kCFHTTPAuthenticationSchemeKerberos](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationschemekerberos)Added [kCFHTTPAuthenticationSchemeNegotiate2](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationschemenegotiate2)Added [kCFHTTPAuthenticationSchemeXMobileMeAuthToken](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationschemexmobilemeauthtoken)CFProxySupport.hAdded [kCFNetworkProxiesProxyAutoConfigJavaScript](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesproxyautoconfigjavascript)Added [kCFProxyAutoConfigurationJavaScriptKey](https://developer.apple.com/documentation/cfnetwork/kcfproxyautoconfigurationjavascriptkey)Added [kCFProxyTypeAutoConfigurationJavaScript](https://developer.apple.com/documentation/cfnetwork/kcfproxytypeautoconfigurationjavascript)CFSocketStream.hAdded [kCFStreamNetworkServiceType](https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetype)Added [kCFStreamNetworkServiceTypeBackground](https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetypebackground)Added [kCFStreamNetworkServiceTypeVideo](https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetypevideo)Added [kCFStreamNetworkServiceTypeVoIP](https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetypevoip)Added [kCFStreamNetworkServiceTypeVoice](https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetypevoice)CSIdentityBase.hAdded kCSIdentityUnknownAccountErrModified [kCSIdentityDuplicateFullNameErr](../../../documentation/Networking/Core%20Services%20Identity%20Reference/CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3fmnxw443uf5vugu2jmrsw45djor4ui5lqnruwgylumvdhk3dmjzqw2zkfojza)

|  | Header |
| --- | --- |
| From | CSIdentity.h |
| To | CSIdentityBase.h |

Modified [kCSIdentityPermissionErr](../../../documentation/Networking/Core%20Services%20Identity%20Reference/CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3fmnxw443uf5vugu2jmrsw45djor4vazlsnvuxg43jn5xek4ts)

|  | Header |
| --- | --- |
| From | CSIdentity.h |
| To | CSIdentityBase.h |

Modified [kCSIdentityDuplicatePosixNameErr](../../../documentation/Networking/Core%20Services%20Identity%20Reference/CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3fmnxw443uf5vugu2jmrsw45djor4ui5lqnruwgylumvig643jpbhgc3lfivzhe)

|  | Header |
| --- | --- |
| From | CSIdentity.h |
| To | CSIdentityBase.h |

Modified [kCSIdentityErrorDomain](https://developer.apple.com/documentation/coreservices/kcsidentityerrordomain)

|  | Header |
| --- | --- |
| From | CSIdentity.h |
| To | CSIdentityBase.h |

Modified [kCSIdentityInvalidPosixNameErr](../../../documentation/Networking/Core%20Services%20Identity%20Reference/CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3fmnxw443uf5vugu2jmrsw45djor4us3twmfwgszcqn5zws6comfwwkrlsoi)

|  | Header |
| --- | --- |
| From | CSIdentity.h |
| To | CSIdentityBase.h |

Modified [kCSIdentityAuthorityNotAccessibleErr](../../../documentation/Networking/Core%20Services%20Identity%20Reference/CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3fmnxw443uf5vugu2jmrsw45djor4uc5lunbxxe2lupfhg65cbmnrwk43tnfrgyzkfojza)

|  | Header |
| --- | --- |
| From | CSIdentity.h |
| To | CSIdentityBase.h |

Modified [kCSIdentityDeletedErr](../../../documentation/Networking/Core%20Services%20Identity%20Reference/CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3fmnxw443uf5vugu2jmrsw45djor4uizlmmv2gkzcfojza)

|  | Header |
| --- | --- |
| From | CSIdentity.h |
| To | CSIdentityBase.h |

Modified [kCSIdentityInvalidFullNameErr](../../../documentation/Networking/Core%20Services%20Identity%20Reference/CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3fmnxw443uf5vugu2jmrsw45djor4us3twmfwgszcgovwgyttbnvsuk4ts)

|  | Header |
| --- | --- |
| From | CSIdentity.h |
| To | CSIdentityBase.h |

Modified [kCSIdentityUnknownAuthorityErr](../../../documentation/Networking/Core%20Services%20Identity%20Reference/CompositePage.md#apple-f4xwc4dqnrsv64tfmyxwgl3fmnxw443uf5vugu2jmrsw45djor4vk3tlnzxxo3sbov2gq33snf2hsrlsoi)

|  | Header |
| --- | --- |
| From | CSIdentity.h |
| To | CSIdentityBase.h |

DiskSpaceRecovery.hAdded [CSDiskSpaceCancelRecovery()](https://developer.apple.com/documentation/coreservices/1448335-csdiskspacecancelrecovery)Added [CSDiskSpaceGetRecoveryEstimate()](https://developer.apple.com/documentation/coreservices/1448439-csdiskspacegetrecoveryestimate)Added [CSDiskSpaceRecoveryCallback](https://developer.apple.com/documentation/coreservices/csdiskspacerecoverycallback)Added [CSDiskSpaceRecoveryOptions](https://developer.apple.com/documentation/coreservices/csdiskspacerecoveryoptions)Added [CSDiskSpaceStartRecovery()](https://developer.apple.com/documentation/coreservices/1447968-csdiskspacestartrecovery)Added [kCSDiskSpaceRecoveryOptionNoUI](https://developer.apple.com/documentation/coreservices/kcsdiskspacerecoveryoptionnoui)FSEvents.hAdded [kFSEventStreamCreateFlagFileEvents](https://developer.apple.com/documentation/coreservices/1455376-fseventstreamcreateflags/kfseventstreamcreateflagfileevents)Added [kFSEventStreamEventFlagItemChangeOwner](https://developer.apple.com/documentation/coreservices/kfseventstreameventflagitemchangeowner)Added [kFSEventStreamEventFlagItemCreated](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflagitemcreated)Added [kFSEventStreamEventFlagItemFinderInfoMod](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflagitemfinderinfomod)Added [kFSEventStreamEventFlagItemInodeMetaMod](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflagiteminodemetamod)Added [kFSEventStreamEventFlagItemIsDir](https://developer.apple.com/documentation/coreservices/kfseventstreameventflagitemisdir)Added [kFSEventStreamEventFlagItemIsFile](https://developer.apple.com/documentation/coreservices/kfseventstreameventflagitemisfile)Added [kFSEventStreamEventFlagItemIsSymlink](https://developer.apple.com/documentation/coreservices/kfseventstreameventflagitemissymlink)Added [kFSEventStreamEventFlagItemModified](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflagitemmodified)Added [kFSEventStreamEventFlagItemRemoved](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflagitemremoved)Added [kFSEventStreamEventFlagItemRenamed](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflagitemrenamed)Added [kFSEventStreamEventFlagItemXattrMod](https://developer.apple.com/documentation/coreservices/kfseventstreameventflagitemxattrmod)Files.hAdded [kFSMountServerSuppressConnectionUI](https://developer.apple.com/documentation/coreservices/1565352-anonymous/kfsmountserversuppressconnectionui)Folders.hAdded [kDropBoxFolderType](https://developer.apple.com/documentation/coreservices/1389495-anonymous/kdropboxfoldertype)Added [kServicesFolderType](https://developer.apple.com/documentation/coreservices/1389265-anonymous/kservicesfoldertype)IconStorage.hAdded [kIconServices1024PixelDataARGB](https://developer.apple.com/documentation/coreservices/1585888-anonymous/kiconservices1024pixeldataargb)MDExternalDatastore.hRemoved MDExternalDatastoreQueryRefRemoved MDExternalDatastoreRefRemoved MDExternalDatastoreStoreInterfaceStruct (no architecture available)Removed MDOIDEnumerationHasMoreOIDs()Removed MDOIDEnumerationNextOID()Removed MDOIDEnumerationRefRemoved MDResponseChannelRefRemoved MDResponseChannelSendOID()Removed MDResponseChannelSendObject()Removed #def kMDExternalDatastoreStoreInterfaceIDRemoved #def kMDExternalDatastoreTypeIDMDItem.hAdded [MDItemsCopyAttributes()](https://developer.apple.com/documentation/coreservices/1426975-mditemscopyattributes)Added [MDItemsCreateWithURLs()](https://developer.apple.com/documentation/coreservices/1427086-mditemscreatewithurls)Added [kMDItemApplicationCategories](https://developer.apple.com/documentation/coreservices/kmditemapplicationcategories)Added [kMDItemCameraOwner](https://developer.apple.com/documentation/coreservices/kmditemcameraowner)Added [kMDItemDateAdded](https://developer.apple.com/documentation/coreservices/kmditemdateadded)Added [kMDItemDownloadedDate](https://developer.apple.com/documentation/coreservices/kmditemdownloadeddate)Added [kMDItemExecutableArchitectures](https://developer.apple.com/documentation/coreservices/kmditemexecutablearchitectures)Added [kMDItemFocalLength35mm](https://developer.apple.com/documentation/coreservices/kmditemfocallength35mm)Added [kMDItemGPSAreaInformation](https://developer.apple.com/documentation/coreservices/kmditemgpsareainformation)Added [kMDItemGPSDOP](https://developer.apple.com/documentation/coreservices/kmditemgpsdop)Added [kMDItemGPSDateStamp](https://developer.apple.com/documentation/coreservices/kmditemgpsdatestamp)Added [kMDItemGPSDestBearing](https://developer.apple.com/documentation/coreservices/kmditemgpsdestbearing)Added [kMDItemGPSDestDistance](https://developer.apple.com/documentation/coreservices/kmditemgpsdestdistance)Added [kMDItemGPSDestLatitude](https://developer.apple.com/documentation/coreservices/kmditemgpsdestlatitude)Added [kMDItemGPSDestLongitude](https://developer.apple.com/documentation/coreservices/kmditemgpsdestlongitude)Added [kMDItemGPSDifferental](https://developer.apple.com/documentation/coreservices/kmditemgpsdifferental)Added [kMDItemGPSMapDatum](https://developer.apple.com/documentation/coreservices/kmditemgpsmapdatum)Added [kMDItemGPSMeasureMode](https://developer.apple.com/documentation/coreservices/kmditemgpsmeasuremode)Added [kMDItemGPSProcessingMethod](https://developer.apple.com/documentation/coreservices/kmditemgpsprocessingmethod)Added [kMDItemGPSStatus](https://developer.apple.com/documentation/coreservices/kmditemgpsstatus)Added [kMDItemIsApplicationManaged](https://developer.apple.com/documentation/coreservices/kmditemisapplicationmanaged)Added [kMDItemIsLikelyJunk](https://developer.apple.com/documentation/coreservices/kmditemislikelyjunk)Added [kMDItemLabelID](https://developer.apple.com/documentation/coreservices/kmditemlabelid)Added [kMDItemLabelIcon](https://developer.apple.com/documentation/coreservices/kmditemlabelicon)Added [kMDItemLabelKind](https://developer.apple.com/documentation/coreservices/kmditemlabelkind)Added [kMDItemLabelUUID](https://developer.apple.com/documentation/coreservices/kmditemlabeluuid)Added [kMDItemLensModel](https://developer.apple.com/documentation/coreservices/kmditemlensmodel)MDLabel.hAdded [MDCopyLabelKinds()](https://developer.apple.com/documentation/coreservices/1442887-mdcopylabelkinds)Added [MDCopyLabelWithUUID()](https://developer.apple.com/documentation/coreservices/1447030-mdcopylabelwithuuid)Added [MDCopyLabelsMatchingExpression()](https://developer.apple.com/documentation/coreservices/1448237-mdcopylabelsmatchingexpression)Added [MDCopyLabelsWithKind()](https://developer.apple.com/documentation/coreservices/1444230-mdcopylabelswithkind)Added [MDItemCopyLabels()](https://developer.apple.com/documentation/coreservices/1442606-mditemcopylabels)Added [MDItemRemoveLabel()](https://developer.apple.com/documentation/coreservices/1446067-mditemremovelabel)Added [MDItemSetLabel()](https://developer.apple.com/documentation/coreservices/1442559-mditemsetlabel)Added #def MDLABEL_HAdded [MDLabelCopyAttribute()](https://developer.apple.com/documentation/coreservices/1445456-mdlabelcopyattribute)Added [MDLabelCopyAttributeName()](https://developer.apple.com/documentation/coreservices/1445522-mdlabelcopyattributename)Added [MDLabelCreate()](https://developer.apple.com/documentation/coreservices/1442614-mdlabelcreate)Added [MDLabelDelete()](https://developer.apple.com/documentation/coreservices/1449203-mdlabeldelete)Added [MDLabelDomain](https://developer.apple.com/documentation/coreservices/mdlabeldomain)Added [MDLabelGetTypeID()](https://developer.apple.com/documentation/coreservices/1446579-mdlabelgettypeid)Added [MDLabelRef](https://developer.apple.com/documentation/coreservices/mdlabel)Added [MDLabelSetAttributes()](https://developer.apple.com/documentation/coreservices/1449005-mdlabelsetattributes)Added [kMDLabelAddedNotification](https://developer.apple.com/documentation/coreservices/kmdlabeladdednotification)Added [kMDLabelBundleURL](https://developer.apple.com/documentation/coreservices/kmdlabelbundleurl)Added [kMDLabelChangedNotification](https://developer.apple.com/documentation/coreservices/kmdlabelchangednotification)Added [kMDLabelContentChangeDate](https://developer.apple.com/documentation/coreservices/kmdlabelcontentchangedate)Added [kMDLabelDisplayName](https://developer.apple.com/documentation/coreservices/kmdlabeldisplayname)Added [kMDLabelIconData](https://developer.apple.com/documentation/coreservices/kmdlabelicondata)Added [kMDLabelIconUUID](https://developer.apple.com/documentation/coreservices/kmdlabeliconuuid)Added [kMDLabelIsMutuallyExclusiveSetMember](https://developer.apple.com/documentation/coreservices/kmdlabelismutuallyexclusivesetmember)Added [kMDLabelKind](https://developer.apple.com/documentation/coreservices/kmdlabelkind)Added [kMDLabelKindIsMutuallyExclusiveSetKey](https://developer.apple.com/documentation/coreservices/kmdlabelkindismutuallyexclusivesetkey)Added [kMDLabelKindVisibilityKey](https://developer.apple.com/documentation/coreservices/kmdlabelkindvisibilitykey)Added [kMDLabelLocalDomain](https://developer.apple.com/documentation/coreservices/mdlabeldomain/kmdlabellocaldomain)Added [kMDLabelRemovedNotification](https://developer.apple.com/documentation/coreservices/kmdlabelremovednotification)Added [kMDLabelSetsFinderColor](https://developer.apple.com/documentation/coreservices/kmdlabelsetsfindercolor)Added [kMDLabelUUID](https://developer.apple.com/documentation/coreservices/kmdlabeluuid)Added [kMDLabelUserDomain](https://developer.apple.com/documentation/coreservices/kmdlabeluserdomain)Added [kMDLabelVisibility](https://developer.apple.com/documentation/coreservices/kmdlabelvisibility)Added [kMDPrivateVisibility](https://developer.apple.com/documentation/coreservices/kmdprivatevisibility)Added [kMDPublicVisibility](https://developer.apple.com/documentation/coreservices/kmdpublicvisibility)MDQuery.hAdded [MDQueryCreateForItems()](https://developer.apple.com/documentation/coreservices/1413031-mdquerycreateforitems)Added [MDQueryGetSortOptionFlagsForAttribute()](https://developer.apple.com/documentation/coreservices/1413013-mdquerygetsortoptionflagsforattr)Added MDQuerySetOptionSortFlagsForAttribute() (no architecture available)Added [MDQuerySetSortOptionFlagsForAttribute()](https://developer.apple.com/documentation/coreservices/1413075-mdquerysetsortoptionflagsforattr)Added [MDQuerySetSortOrder()](https://developer.apple.com/documentation/coreservices/1413096-mdquerysetsortorder)Added [MDQuerySortOptionFlags](https://developer.apple.com/documentation/coreservices/mdquerysortoptionflags)Added [kMDQueryReverseSortOrderFlag](https://developer.apple.com/documentation/coreservices/mdquerysortoptionflags/kmdqueryreversesortorderflag)MacMemory.hAdded [kMacMemoryMaximumMemoryManagerBlockSize](https://developer.apple.com/documentation/coreservices/1506343-anonymous/kmacmemorymaximummemorymanagerblocksize)Modified maxSize

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | Both | i386,ppc,x86_64 |
| To | _Unknown_ | Unknown |

Multiprocessing.hModified [MPSetTimerNotify()](https://developer.apple.com/documentation/coreservices/1585726-mpsettimernotify)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPProcessors()](https://developer.apple.com/documentation/coreservices/1585778-mpprocessors)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPSignalSemaphore()](https://developer.apple.com/documentation/coreservices/1585713-mpsignalsemaphore)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPRegisterDebugger()](https://developer.apple.com/documentation/coreservices/1585573-mpregisterdebugger)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPExit()](https://developer.apple.com/documentation/coreservices/1585705-mpexit)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPGetTaskStorageValue()](https://developer.apple.com/documentation/coreservices/1585589-mpgettaskstoragevalue)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPSetTaskState()](https://developer.apple.com/documentation/coreservices/1585601-mpsettaskstate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPCancelTimer()](https://developer.apple.com/documentation/coreservices/1585745-mpcanceltimer)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPModifyNotificationParameters()](https://developer.apple.com/documentation/coreservices/1585668-mpmodifynotificationparameters)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPCreateSemaphore()](https://developer.apple.com/documentation/coreservices/1585569-mpcreatesemaphore)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPSetExceptionHandler()](https://developer.apple.com/documentation/coreservices/1585759-mpsetexceptionhandler)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPWaitOnQueue()](https://developer.apple.com/documentation/coreservices/1585762-mpwaitonqueue)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPDeallocateTaskStorageIndex()](https://developer.apple.com/documentation/coreservices/1585649-mpdeallocatetaskstorageindex)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPDisposeTaskException()](https://developer.apple.com/documentation/coreservices/1585607-mpdisposetaskexception)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPEnterCriticalRegion()](https://developer.apple.com/documentation/coreservices/1585622-mpentercriticalregion)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPDeleteCriticalRegion()](https://developer.apple.com/documentation/coreservices/1585704-mpdeletecriticalregion)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPCauseNotification()](https://developer.apple.com/documentation/coreservices/1585754-mpcausenotification)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPBlockClear()](https://developer.apple.com/documentation/coreservices/1585642-mpblockclear)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPAllocateTaskStorageIndex()](https://developer.apple.com/documentation/coreservices/1585719-mpallocatetaskstorageindex)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPSetTaskStorageValue()](https://developer.apple.com/documentation/coreservices/1585626-mpsettaskstoragevalue)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPSetEvent()](https://developer.apple.com/documentation/coreservices/1585752-mpsetevent)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPDeleteQueue()](https://developer.apple.com/documentation/coreservices/1585571-mpdeletequeue)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPProcessorsScheduled()](https://developer.apple.com/documentation/coreservices/1585777-mpprocessorsscheduled)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPCreateTimer()](https://developer.apple.com/documentation/coreservices/1585748-mpcreatetimer)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPCurrentTaskID()](https://developer.apple.com/documentation/coreservices/1585673-mpcurrenttaskid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPCreateEvent()](https://developer.apple.com/documentation/coreservices/1585702-mpcreateevent)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPModifyNotification()](https://developer.apple.com/documentation/coreservices/1585780-mpmodifynotification)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPFree()](https://developer.apple.com/documentation/coreservices/1585676-mpfree)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPThrowException()](https://developer.apple.com/documentation/coreservices/1585743-mpthrowexception)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPTaskIsPreemptive()](https://developer.apple.com/documentation/coreservices/1585681-mptaskispreemptive)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPArmTimer()](https://developer.apple.com/documentation/coreservices/1585612-mparmtimer)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPExtractTaskState()](https://developer.apple.com/documentation/coreservices/1585718-mpextracttaskstate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPWaitOnSemaphore()](https://developer.apple.com/documentation/coreservices/1585722-mpwaitonsemaphore)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPSetQueueReserve()](https://developer.apple.com/documentation/coreservices/1585671-mpsetqueuereserve)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPCreateNotification()](https://developer.apple.com/documentation/coreservices/1585723-mpcreatenotification)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPDeleteSemaphore()](https://developer.apple.com/documentation/coreservices/1585586-mpdeletesemaphore)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPTerminateTask()](https://developer.apple.com/documentation/coreservices/1585769-mpterminatetask)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPUnregisterDebugger()](https://developer.apple.com/documentation/coreservices/1585598-mpunregisterdebugger)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPExitCriticalRegion()](https://developer.apple.com/documentation/coreservices/1585758-mpexitcriticalregion)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPRemoteCall()](https://developer.apple.com/documentation/coreservices/1585652-mpremotecall)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPAllocateAligned()](https://developer.apple.com/documentation/coreservices/1585774-mpallocatealigned)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified MPDataToCode()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPSetTaskWeight()](https://developer.apple.com/documentation/coreservices/1585665-mpsettaskweight)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPWaitForEvent()](https://developer.apple.com/documentation/coreservices/1585656-mpwaitforevent)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPDelayUntil()](https://developer.apple.com/documentation/coreservices/1585647-mpdelayuntil)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPNotifyQueue()](https://developer.apple.com/documentation/coreservices/1585699-mpnotifyqueue)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPCreateCriticalRegion()](https://developer.apple.com/documentation/coreservices/1585663-mpcreatecriticalregion)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPDeleteNotification()](https://developer.apple.com/documentation/coreservices/1585659-mpdeletenotification)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPYield()](https://developer.apple.com/documentation/coreservices/1585732-mpyield)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPDeleteEvent()](https://developer.apple.com/documentation/coreservices/1585691-mpdeleteevent)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPAllocate()](https://developer.apple.com/documentation/coreservices/1585756-mpallocate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPCreateTask()](https://developer.apple.com/documentation/coreservices/1585779-mpcreatetask)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPBlockCopy()](https://developer.apple.com/documentation/coreservices/1585707-mpblockcopy)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPCreateQueue()](https://developer.apple.com/documentation/coreservices/1585694-mpcreatequeue)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPDeleteTimer()](https://developer.apple.com/documentation/coreservices/1585761-mpdeletetimer)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPRemoteCallCFM()](https://developer.apple.com/documentation/coreservices/1585757-mpremotecallcfm)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPGetAllocatedBlockSize()](https://developer.apple.com/documentation/coreservices/1585717-mpgetallocatedblocksize)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

MultiprocessingInfo.hModified [MPGetNextTaskID()](https://developer.apple.com/documentation/coreservices/1508163-mpgetnexttaskid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [MPGetNextCpuID()](https://developer.apple.com/documentation/coreservices/1508189-mpgetnextcpuid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

NSLCore.hRemoved ClientAsyncInfo (no architecture available)Removed ClientAsyncInfoPtr (no architecture available)Removed DisposeNSLClientNotifyUPP()Removed DisposeNSLMgrNotifyUPP()Removed InvokeNSLClientNotifyUPP()Removed InvokeNSLMgrNotifyUPP()Removed [NSLAddServiceToServicesList()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngeczdeknsxe5tjmnsvi32tmvzhm2ldmvzuy2ltoq)Removed [NSLCancelRequest()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngegylomnswyutfof2wk43u)Removed [NSLClientAsyncInfo](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2okngeg3djmvxhiqltpfxggslomzxq)Removed NSLClientAsyncInfoPtrRemoved NSLClientNotifyProcPtrRemoved NSLClientNotifyUPPRemoved [NSLClientRef](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2okngeg3djmvxhiutfmy)Removed [NSLCloseNavigationAPI()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngeg3dponsu4ylwnftwc5djn5xecucj)Removed [NSLContinueLookup()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngeg33ooruw45lfjrxw623voa)Removed [NSLCopyNeighborhood()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngeg33qpfhgk2lhnbrg64tin5xwi)Removed [NSLDeleteRequest()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngeizlmmv2gkutfof2wk43u)Removed [NSLDisposeServicesList()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngei2ltobxxgzktmvzhm2ldmvzuy2ltoq)Removed NSLDisposeThread()Removed [NSLError](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2okngek4tsn5za)Removed NSLErrorPtrRemoved [NSLErrorToString()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngek4tsn5zfi32torzgs3th)Removed [NSLEventCode](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Constants.md#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2okngek5tfnz2eg33emu)Removed [NSLFreeNeighborhood()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngem4tfmvhgk2lhnbrg64tin5xwi)Removed [NSLFreeTypedDataPtr()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngem4tfmvkhs4dfmrcgc5dbkb2he)Removed NSLGetErrorStringsFromResource()Removed [NSLGetNameFromNeighborhood()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngeozlujzqw2zkgojxw2ttfnftwqytpojug633e)Removed [NSLGetNeighborhoodLength()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngeozlujzswsz3imjxxe2dpn5seyzlom52gq)Removed [NSLGetNextNeighborhood()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngeozlujzsxq5comvuwo2dcn5zgq33pmq)Removed NSLGetNextUrl()Removed [NSLGetServiceFromURL()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngeozluknsxe5tjmnsum4tpnvkveta)Removed [NSLHexDecodeText()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngeqzlyirswg33emvkgk6du)Removed [NSLHexEncodeText()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngeqzlyivxgg33emvkgk6du)Removed #def NSLLibraryPresentRemoved [NSLLibraryVersion()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngey2lcojqxe6kwmvzhg2lpny)Removed [NSLMakeNewNeighborhood()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2oknge2yllmvhgk52omvuwo2dcn5zgq33pmq)Removed [NSLMakeNewServicesList()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2oknge2yllmvhgk52tmvzhm2ldmvzuy2ltoq)Removed [NSLMakeServicesRequestPB()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2oknge2yllmvjwk4twnfrwk42smvyxkzltoriee)Removed NSLMgrNotifyProcPtrRemoved NSLMgrNotifyUPPRemoved [NSLNeighborhood](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2oknge4zljm5uge33snbxw6za)Removed NSLNewThread()Removed NSLOneBasedIndexRemoved [NSLOpenNavigationAPI()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2oknge64dfnzhgc5tjm5qxi2lpnzavasi)Removed NSLParseServiceRegistrationPB()Removed NSLParseServicesRequestPB()Removed [NSLPath](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2okngfayluna)Removed NSLPluginAsyncInfoRemoved NSLPluginAsyncInfoPtrRemoved NSLPluginDataRemoved NSLPluginDataPtrRemoved [NSLPrepareRequest()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngfa4tfobqxezksmvyxkzltoq)Removed [NSLRequestRef](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2okngfezlrovsxg5csmvta)Removed [NSLSearchState](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Constants.md#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2okngfgzlbojrwqu3umf2gk)Removed [NSLServiceIsInServiceList()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngfgzlsozuwgzkjonew4u3foj3gsy3fjruxg5a)Removed [NSLServiceType](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2okngfgzlsozuwgzkupfygk)Removed [NSLServicesList](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2okngfgzlsozuwgzltjruxg5a)Removed NSLServicesListHeaderRemoved NSLServicesListHeaderPtrRemoved [NSLStandardDeregisterURL()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngfg5dbnzsgc4teirsxezlhnfzxizlskvjey)Removed [NSLStandardRegisterURL()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngfg5dbnzsgc4tekjswo2ltorsxevksjq)Removed [NSLStartNeighborhoodLookup()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngfg5dboj2e4zljm5uge33snbxw6zcmn5xww5lq)Removed [NSLStartServicesLookup()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngfg5dboj2fgzlsozuwgzltjrxw623voa)Removed [NSLTypedData](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2okngfi6lqmvseiylume)Removed NSLTypedDataPtrRemoved NewNSLClientNotifyUPP()Removed NewNSLMgrNotifyUPP()Removed PluginAsyncInfo (no architecture available)Removed PluginAsyncInfoPtr (no architecture available)Removed PluginData (no architecture available)Removed PluginDataPtr (no architecture available)Removed TypedData (no architecture available)Removed TypedDataPtr (no architecture available)Removed #def kDNSProtocolTypeRemoved #def kLDAPProtocolTypeRemoved #def kNBPProtocolTypeRemoved [kNSLContinueLookupEvent](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Constants.md#apple-f4xwc4dqnrsv64tfmyxwgl3fmnxw443uf5vu4u2minxw45djnz2wktdpn5vxk4cfozsw45a)Removed #def kNSLDataTypeRemoved kNSLDefaultListSizeRemoved #def kNSLDirectoryServiceProtocolTypeRemoved kNSLDuplicateSearchInProgressRemoved #def kNSLErrorNoErrRemoved kNSLInvalidEnumeratorRefRemoved kNSLMinOTVersionRemoved kNSLMinSystemVersionRemoved [kNSLNeighborhoodLookupDataEvent](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Constants.md#apple-f4xwc4dqnrsv64tfmyxwgl3fmnxw443uf5vu4u2mjzswsz3imjxxe2dpn5sey33pnn2xardborquk5tfnz2a)Removed kNSLNewDataEventRemoved kNSLNoContextRemoved [kNSLSearchStateBufferFull](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Constants.md#apple-f4xwc4dqnrsv64tfmyxwgl3fmnxw443uf5vu4u2mknswc4tdnbjxiylumvbhkztgmvzem5lmnq)Removed [kNSLSearchStateComplete](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Constants.md#apple-f4xwc4dqnrsv64tfmyxwgl3fmnxw443uf5vu4u2mknswc4tdnbjxiylumvbw63lqnrsxizi)Removed [kNSLSearchStateOnGoing](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Constants.md#apple-f4xwc4dqnrsv64tfmyxwgl3fmnxw443uf5vu4u2mknswc4tdnbjxiylumvhw4r3pnfxgo)Removed [kNSLSearchStateStalled](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Constants.md#apple-f4xwc4dqnrsv64tfmyxwgl3fmnxw443uf5vu4u2mknswc4tdnbjxiylumvjxiylmnrswi)Removed [kNSLServicesLookupDataEvent](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Constants.md#apple-f4xwc4dqnrsv64tfmyxwgl3fmnxw443uf5vu4u2mknsxe5tjmnsxgtdpn5vxk4cemf2gcrlwmvxhi)Removed kNSLURLDelimiterRemoved kNSLUserCanceledRemoved [kNSLWaitingForContinue](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Constants.md#apple-f4xwc4dqnrsv64tfmyxwgl3fmnxw443uf5vu4u2mk5qws5djnztum33sinxw45djnz2wk)Removed #def kSLPProtocolTypeOSUtils.hModified [IsMetric()](https://developer.apple.com/documentation/coreservices/1533364-ismetric)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

TextCommon.hAdded [kTextEncodingUnicodeV6_0](https://developer.apple.com/documentation/coreservices/1400188-unicode_and_iso_ucs_text_encodin/ktextencodingunicodev6_0)Threads.hModified [SetThreadState()](https://developer.apple.com/documentation/coreservices/1574212-setthreadstate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [DisposeThreadSwitchUPP()](https://developer.apple.com/documentation/coreservices/1574264-disposethreadswitchupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [NewThreadSwitchUPP()](https://developer.apple.com/documentation/coreservices/1574243-newthreadswitchupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [InvokeThreadTerminationUPP()](https://developer.apple.com/documentation/coreservices/1574290-invokethreadterminationupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SetThreadReadyGivenTaskRef()](https://developer.apple.com/documentation/coreservices/1574279-setthreadreadygiventaskref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [GetThreadState()](https://developer.apple.com/documentation/coreservices/1574250-getthreadstate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [DisposeDebuggerNewThreadUPP()](https://developer.apple.com/documentation/coreservices/1574218-disposedebuggernewthreadupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SetDebuggerNotificationProcs()](https://developer.apple.com/documentation/coreservices/1574202-setdebuggernotificationprocs)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [GetCurrentThread()](https://developer.apple.com/documentation/coreservices/1574216-getcurrentthread)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [NewThreadSchedulerUPP()](https://developer.apple.com/documentation/coreservices/1574293-newthreadschedulerupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [InvokeDebuggerNewThreadUPP()](https://developer.apple.com/documentation/coreservices/1574207-invokedebuggernewthreadupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SetThreadTerminator()](https://developer.apple.com/documentation/coreservices/1574205-setthreadterminator)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [DisposeDebuggerDisposeThreadUPP()](https://developer.apple.com/documentation/coreservices/1574277-disposedebuggerdisposethreadupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [YieldToThread()](https://developer.apple.com/documentation/coreservices/1574240-yieldtothread)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [NewDebuggerDisposeThreadUPP()](https://developer.apple.com/documentation/coreservices/1574285-newdebuggerdisposethreadupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ThreadCurrentStackSpace()](https://developer.apple.com/documentation/coreservices/1574269-threadcurrentstackspace)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ThreadBeginCritical()](https://developer.apple.com/documentation/coreservices/1574258-threadbegincritical)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SetThreadSwitcher()](https://developer.apple.com/documentation/coreservices/1574270-setthreadswitcher)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [NewThread()](https://developer.apple.com/documentation/coreservices/1574248-newthread)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [InvokeThreadEntryUPP()](https://developer.apple.com/documentation/coreservices/1574226-invokethreadentryupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [DisposeThreadEntryUPP()](https://developer.apple.com/documentation/coreservices/1574275-disposethreadentryupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SetThreadStateEndCritical()](https://developer.apple.com/documentation/coreservices/1574289-setthreadstateendcritical)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [DisposeThreadSchedulerUPP()](https://developer.apple.com/documentation/coreservices/1574280-disposethreadschedulerupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [InvokeThreadSwitchUPP()](https://developer.apple.com/documentation/coreservices/1574281-invokethreadswitchupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [DisposeThreadTerminationUPP()](https://developer.apple.com/documentation/coreservices/1574233-disposethreadterminationupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [CreateThreadPool()](https://developer.apple.com/documentation/coreservices/1574200-createthreadpool)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [NewThreadTerminationUPP()](https://developer.apple.com/documentation/coreservices/1574221-newthreadterminationupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified MacGetCurrentThread()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [GetThreadStateGivenTaskRef()](https://developer.apple.com/documentation/coreservices/1574234-getthreadstategiventaskref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [YieldToAnyThread()](https://developer.apple.com/documentation/coreservices/1574238-yieldtoanythread)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [DisposeThread()](https://developer.apple.com/documentation/coreservices/1574219-disposethread)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [NewDebuggerNewThreadUPP()](https://developer.apple.com/documentation/coreservices/1574208-newdebuggernewthreadupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [GetThreadCurrentTaskRef()](https://developer.apple.com/documentation/coreservices/1574236-getthreadcurrenttaskref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [DisposeDebuggerThreadSchedulerUPP()](https://developer.apple.com/documentation/coreservices/1574286-disposedebuggerthreadschedulerup)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [InvokeDebuggerDisposeThreadUPP()](https://developer.apple.com/documentation/coreservices/1574308-invokedebuggerdisposethreadupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [InvokeDebuggerThreadSchedulerUPP()](https://developer.apple.com/documentation/coreservices/1574211-invokedebuggerthreadschedulerupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ThreadEndCritical()](https://developer.apple.com/documentation/coreservices/1574230-threadendcritical)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [GetDefaultThreadStackSize()](https://developer.apple.com/documentation/coreservices/1574231-getdefaultthreadstacksize)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [NewThreadEntryUPP()](https://developer.apple.com/documentation/coreservices/1574224-newthreadentryupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SetThreadScheduler()](https://developer.apple.com/documentation/coreservices/1574195-setthreadscheduler)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [InvokeThreadSchedulerUPP()](https://developer.apple.com/documentation/coreservices/1574302-invokethreadschedulerupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [NewDebuggerThreadSchedulerUPP()](https://developer.apple.com/documentation/coreservices/1574284-newdebuggerthreadschedulerupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

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
