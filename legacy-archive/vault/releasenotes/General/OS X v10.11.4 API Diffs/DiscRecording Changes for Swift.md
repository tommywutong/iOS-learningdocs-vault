---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/DiscRecording.html
archived_at: '2026-07-18T02:53:51.158092Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# DiscRecording Changes for Swift

### DiscRecording

Modified DRBurnRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DRBurnRef = DRBurn ``` |
| To | ``` class DRBurnRef { } ``` |

Modified DRCDTextBlockRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DRCDTextBlockRef = DRCDTextBlock ``` |
| To | ``` class DRCDTextBlockRef { } ``` |

Modified DRDeviceRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DRDeviceRef = DRDevice ``` |
| To | ``` class DRDeviceRef { } ``` |

Modified DREraseRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DREraseRef = DRErase ``` |
| To | ``` class DREraseRef { } ``` |

Modified DRFileRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DRFileRef = DRFile ``` |
| To | ``` class DRFileRef { } ``` |

Modified DRFolderRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DRFolderRef = DRFolder ``` |
| To | ``` class DRFolderRef { } ``` |

Modified DRNotificationCenterRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DRNotificationCenterRef = DRNotificationCenter ``` |
| To | ``` class DRNotificationCenterRef { } ``` |

Modified DRTrackRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DRTrackRef = DRTrack ``` |
| To | ``` class DRTrackRef { } ``` |

Modified DRBurnAbort(_: DRBurnRef!)

|  | Declaration |
| --- | --- |
| From | ``` func DRBurnAbort(_ burn: DRBurn!) ``` |
| To | ``` func DRBurnAbort(_ burn: DRBurnRef!) ``` |

Modified DRBurnCopyStatus(_: DRBurnRef!) -> Unmanaged<CFDictionary>!

|  | Declaration |
| --- | --- |
| From | ``` func DRBurnCopyStatus(_ burn: DRBurn!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func DRBurnCopyStatus(_ burn: DRBurnRef!) -> Unmanaged<CFDictionary>! ``` |

Modified DRBurnCreate(_: DRDeviceRef!) -> Unmanaged<DRBurnRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRBurnCreate(_ device: DRDevice!) -> Unmanaged<DRBurn>! ``` |
| To | ``` func DRBurnCreate(_ device: DRDeviceRef!) -> Unmanaged<DRBurnRef>! ``` |

Modified DRBurnGetDevice(_: DRBurnRef!) -> Unmanaged<DRDeviceRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRBurnGetDevice(_ burn: DRBurn!) -> Unmanaged<DRDevice>! ``` |
| To | ``` func DRBurnGetDevice(_ burn: DRBurnRef!) -> Unmanaged<DRDeviceRef>! ``` |

Modified DRBurnGetProperties(_: DRBurnRef!) -> Unmanaged<CFDictionary>!

|  | Declaration |
| --- | --- |
| From | ``` func DRBurnGetProperties(_ burn: DRBurn!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func DRBurnGetProperties(_ burn: DRBurnRef!) -> Unmanaged<CFDictionary>! ``` |

Modified DRBurnSetProperties(_: DRBurnRef!, _: CFDictionary!)

|  | Declaration |
| --- | --- |
| From | ``` func DRBurnSetProperties(_ burn: DRBurn!, _ properties: CFDictionary!) ``` |
| To | ``` func DRBurnSetProperties(_ burn: DRBurnRef!, _ properties: CFDictionary!) ``` |

Modified DRBurnWriteLayout(_: DRBurnRef!, _: AnyObject!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DRBurnWriteLayout(_ burn: DRBurn!, _ layout: AnyObject!) -> OSStatus ``` |
| To | ``` func DRBurnWriteLayout(_ burn: DRBurnRef!, _ layout: AnyObject!) -> OSStatus ``` |

Modified DRCDTextBlockCreate(_: CFString!, _: CFStringEncoding) -> Unmanaged<DRCDTextBlockRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRCDTextBlockCreate(_ language: CFString!, _ encoding: CFStringEncoding) -> Unmanaged<DRCDTextBlock>! ``` |
| To | ``` func DRCDTextBlockCreate(_ language: CFString!, _ encoding: CFStringEncoding) -> Unmanaged<DRCDTextBlockRef>! ``` |

Modified DRCDTextBlockFlatten(_: DRCDTextBlockRef!) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func DRCDTextBlockFlatten(_ block: DRCDTextBlock!) -> UInt32 ``` |
| To | ``` func DRCDTextBlockFlatten(_ block: DRCDTextBlockRef!) -> UInt32 ``` |

Modified DRCDTextBlockGetProperties(_: DRCDTextBlockRef!) -> Unmanaged<CFDictionary>!

|  | Declaration |
| --- | --- |
| From | ``` func DRCDTextBlockGetProperties(_ block: DRCDTextBlock!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func DRCDTextBlockGetProperties(_ block: DRCDTextBlockRef!) -> Unmanaged<CFDictionary>! ``` |

Modified DRCDTextBlockGetTrackDictionaries(_: DRCDTextBlockRef!) -> Unmanaged<CFArray>!

|  | Declaration |
| --- | --- |
| From | ``` func DRCDTextBlockGetTrackDictionaries(_ block: DRCDTextBlock!) -> Unmanaged<CFArray>! ``` |
| To | ``` func DRCDTextBlockGetTrackDictionaries(_ block: DRCDTextBlockRef!) -> Unmanaged<CFArray>! ``` |

Modified DRCDTextBlockGetValue(_: DRCDTextBlockRef!, _: CFIndex, _: CFString!) -> Unmanaged<AnyObject>!

|  | Declaration |
| --- | --- |
| From | ``` func DRCDTextBlockGetValue(_ block: DRCDTextBlock!, _ trackIndex: CFIndex, _ key: CFString!) -> Unmanaged<AnyObject>! ``` |
| To | ``` func DRCDTextBlockGetValue(_ block: DRCDTextBlockRef!, _ trackIndex: CFIndex, _ key: CFString!) -> Unmanaged<AnyObject>! ``` |

Modified DRCDTextBlockSetProperties(_: DRCDTextBlockRef!, _: CFDictionary!)

|  | Declaration |
| --- | --- |
| From | ``` func DRCDTextBlockSetProperties(_ block: DRCDTextBlock!, _ properties: CFDictionary!) ``` |
| To | ``` func DRCDTextBlockSetProperties(_ block: DRCDTextBlockRef!, _ properties: CFDictionary!) ``` |

Modified DRCDTextBlockSetTrackDictionaries(_: DRCDTextBlockRef!, _: CFArray!)

|  | Declaration |
| --- | --- |
| From | ``` func DRCDTextBlockSetTrackDictionaries(_ block: DRCDTextBlock!, _ array: CFArray!) ``` |
| To | ``` func DRCDTextBlockSetTrackDictionaries(_ block: DRCDTextBlockRef!, _ array: CFArray!) ``` |

Modified DRCDTextBlockSetValue(_: DRCDTextBlockRef!, _: CFIndex, _: CFString!, _: AnyObject!)

|  | Declaration |
| --- | --- |
| From | ``` func DRCDTextBlockSetValue(_ block: DRCDTextBlock!, _ trackIndex: CFIndex, _ key: CFString!, _ value: AnyObject!) ``` |
| To | ``` func DRCDTextBlockSetValue(_ block: DRCDTextBlockRef!, _ trackIndex: CFIndex, _ key: CFString!, _ value: AnyObject!) ``` |

Modified DRDeviceAcquireExclusiveAccess(_: DRDeviceRef!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DRDeviceAcquireExclusiveAccess(_ device: DRDevice!) -> OSStatus ``` |
| To | ``` func DRDeviceAcquireExclusiveAccess(_ device: DRDeviceRef!) -> OSStatus ``` |

Modified DRDeviceAcquireMediaReservation(_: DRDeviceRef!)

|  | Declaration |
| --- | --- |
| From | ``` func DRDeviceAcquireMediaReservation(_ device: DRDevice!) ``` |
| To | ``` func DRDeviceAcquireMediaReservation(_ device: DRDeviceRef!) ``` |

Modified DRDeviceCloseTray(_: DRDeviceRef!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DRDeviceCloseTray(_ device: DRDevice!) -> OSStatus ``` |
| To | ``` func DRDeviceCloseTray(_ device: DRDeviceRef!) -> OSStatus ``` |

Modified DRDeviceCopyDeviceForBSDName(_: CFString!) -> Unmanaged<DRDeviceRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRDeviceCopyDeviceForBSDName(_ name: CFString!) -> Unmanaged<DRDevice>! ``` |
| To | ``` func DRDeviceCopyDeviceForBSDName(_ name: CFString!) -> Unmanaged<DRDeviceRef>! ``` |

Modified DRDeviceCopyDeviceForIORegistryEntryPath(_: CFString!) -> Unmanaged<DRDeviceRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRDeviceCopyDeviceForIORegistryEntryPath(_ path: CFString!) -> Unmanaged<DRDevice>! ``` |
| To | ``` func DRDeviceCopyDeviceForIORegistryEntryPath(_ path: CFString!) -> Unmanaged<DRDeviceRef>! ``` |

Modified DRDeviceCopyInfo(_: DRDeviceRef!) -> Unmanaged<CFDictionary>!

|  | Declaration |
| --- | --- |
| From | ``` func DRDeviceCopyInfo(_ device: DRDevice!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func DRDeviceCopyInfo(_ device: DRDeviceRef!) -> Unmanaged<CFDictionary>! ``` |

Modified DRDeviceCopyStatus(_: DRDeviceRef!) -> Unmanaged<CFDictionary>!

|  | Declaration |
| --- | --- |
| From | ``` func DRDeviceCopyStatus(_ device: DRDevice!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func DRDeviceCopyStatus(_ device: DRDeviceRef!) -> Unmanaged<CFDictionary>! ``` |

Modified DRDeviceEjectMedia(_: DRDeviceRef!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DRDeviceEjectMedia(_ device: DRDevice!) -> OSStatus ``` |
| To | ``` func DRDeviceEjectMedia(_ device: DRDeviceRef!) -> OSStatus ``` |

Modified DRDeviceIsValid(_: DRDeviceRef!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func DRDeviceIsValid(_ device: DRDevice!) -> Bool ``` |
| To | ``` func DRDeviceIsValid(_ device: DRDeviceRef!) -> Bool ``` |

Modified DRDeviceOpenTray(_: DRDeviceRef!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DRDeviceOpenTray(_ device: DRDevice!) -> OSStatus ``` |
| To | ``` func DRDeviceOpenTray(_ device: DRDeviceRef!) -> OSStatus ``` |

Modified DRDeviceReleaseExclusiveAccess(_: DRDeviceRef!)

|  | Declaration |
| --- | --- |
| From | ``` func DRDeviceReleaseExclusiveAccess(_ device: DRDevice!) ``` |
| To | ``` func DRDeviceReleaseExclusiveAccess(_ device: DRDeviceRef!) ``` |

Modified DRDeviceReleaseMediaReservation(_: DRDeviceRef!)

|  | Declaration |
| --- | --- |
| From | ``` func DRDeviceReleaseMediaReservation(_ device: DRDevice!) ``` |
| To | ``` func DRDeviceReleaseMediaReservation(_ device: DRDeviceRef!) ``` |

Modified DREraseCopyStatus(_: DREraseRef!) -> Unmanaged<CFDictionary>!

|  | Declaration |
| --- | --- |
| From | ``` func DREraseCopyStatus(_ erase: DRErase!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func DREraseCopyStatus(_ erase: DREraseRef!) -> Unmanaged<CFDictionary>! ``` |

Modified DREraseCreate(_: DRDeviceRef!) -> Unmanaged<DREraseRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DREraseCreate(_ device: DRDevice!) -> Unmanaged<DRErase>! ``` |
| To | ``` func DREraseCreate(_ device: DRDeviceRef!) -> Unmanaged<DREraseRef>! ``` |

Modified DREraseGetDevice(_: DREraseRef!) -> Unmanaged<DRDeviceRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DREraseGetDevice(_ erase: DRErase!) -> Unmanaged<DRDevice>! ``` |
| To | ``` func DREraseGetDevice(_ erase: DREraseRef!) -> Unmanaged<DRDeviceRef>! ``` |

Modified DREraseGetProperties(_: DREraseRef!) -> Unmanaged<CFDictionary>!

|  | Declaration |
| --- | --- |
| From | ``` func DREraseGetProperties(_ erase: DRErase!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func DREraseGetProperties(_ erase: DREraseRef!) -> Unmanaged<CFDictionary>! ``` |

Modified DREraseSetProperties(_: DREraseRef!, _: CFDictionary!)

|  | Declaration |
| --- | --- |
| From | ``` func DREraseSetProperties(_ erase: DRErase!, _ properties: CFDictionary!) ``` |
| To | ``` func DREraseSetProperties(_ erase: DREraseRef!, _ properties: CFDictionary!) ``` |

Modified DREraseStart(_: DREraseRef!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DREraseStart(_ erase: DRErase!) -> OSStatus ``` |
| To | ``` func DREraseStart(_ erase: DREraseRef!) -> OSStatus ``` |

Modified DRFileCreateReal(_: UnsafePointer<FSRef>) -> Unmanaged<DRFileRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFileCreateReal(_ fsRef: UnsafePointer<FSRef>) -> Unmanaged<DRFile>! ``` |
| To | ``` func DRFileCreateReal(_ fsRef: UnsafePointer<FSRef>) -> Unmanaged<DRFileRef>! ``` |

Modified DRFileCreateRealWithURL(_: CFURL!) -> Unmanaged<DRFileRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFileCreateRealWithURL(_ urlRef: CFURL!) -> Unmanaged<DRFile>! ``` |
| To | ``` func DRFileCreateRealWithURL(_ urlRef: CFURL!) -> Unmanaged<DRFileRef>! ``` |

Modified DRFileCreateVirtualLink(_: DRFSObjectRef!, _: DRLinkType, _: CFString!) -> Unmanaged<DRFileRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFileCreateVirtualLink(_ original: DRFSObject!, _ linkType: DRLinkType, _ fsKey: CFString!) -> Unmanaged<DRFile>! ``` |
| To | ``` func DRFileCreateVirtualLink(_ original: DRFSObjectRef!, _ linkType: DRLinkType, _ fsKey: CFString!) -> Unmanaged<DRFileRef>! ``` |

Modified DRFileCreateVirtualWithCallback(_: CFString!, _: DRFileProc!, _: UnsafeMutablePointer<Void>) -> Unmanaged<DRFileRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFileCreateVirtualWithCallback(_ baseName: CFString!, _ fileProc: DRFileProc!, _ fileProcRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<DRFile>! ``` |
| To | ``` func DRFileCreateVirtualWithCallback(_ baseName: CFString!, _ fileProc: DRFileProc!, _ fileProcRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<DRFileRef>! ``` |

Modified DRFileCreateVirtualWithData(_: CFString!, _: UnsafeMutablePointer<Void>, _: UInt32) -> Unmanaged<DRFileRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFileCreateVirtualWithData(_ baseName: CFString!, _ fileData: UnsafeMutablePointer<Void>, _ fileDataLength: UInt32) -> Unmanaged<DRFile>! ``` |
| To | ``` func DRFileCreateVirtualWithData(_ baseName: CFString!, _ fileData: UnsafeMutablePointer<Void>, _ fileDataLength: UInt32) -> Unmanaged<DRFileRef>! ``` |

Modified DRFileProc

|  | Declaration |
| --- | --- |
| From | ``` typealias DRFileProc = (UnsafeMutablePointer<Void>, DRFile!, DRFileMessage, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias DRFileProc = (UnsafeMutablePointer<Void>, DRFileRef!, DRFileMessage, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified DRFilesystemTrack

|  | Declaration |
| --- | --- |
| From | ``` typealias DRFilesystemTrackRef = DRFilesystemTrack ``` |
| To | ``` typealias DRFilesystemTrack = DRTrackRef ``` |

Modified DRFilesystemTrackCreate(_: DRFolderRef!) -> Unmanaged<DRFilesystemTrack>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFilesystemTrackCreate(_ rootFolder: DRFolder!) -> Unmanaged<DRFilesystemTrack>! ``` |
| To | ``` func DRFilesystemTrackCreate(_ rootFolder: DRFolderRef!) -> Unmanaged<DRFilesystemTrack>! ``` |

Modified DRFolderAddChild(_: DRFolderRef!, _: DRFSObjectRef!)

|  | Declaration |
| --- | --- |
| From | ``` func DRFolderAddChild(_ parent: DRFolder!, _ newChild: DRFSObject!) ``` |
| To | ``` func DRFolderAddChild(_ parent: DRFolderRef!, _ newChild: DRFSObjectRef!) ``` |

Modified DRFolderConvertRealToVirtual(_: DRFolderRef!)

|  | Declaration |
| --- | --- |
| From | ``` func DRFolderConvertRealToVirtual(_ realFolder: DRFolder!) ``` |
| To | ``` func DRFolderConvertRealToVirtual(_ realFolder: DRFolderRef!) ``` |

Modified DRFolderCopyChildren(_: DRFolderRef!) -> Unmanaged<CFArray>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFolderCopyChildren(_ folder: DRFolder!) -> Unmanaged<CFArray>! ``` |
| To | ``` func DRFolderCopyChildren(_ folder: DRFolderRef!) -> Unmanaged<CFArray>! ``` |

Modified DRFolderCountChildren(_: DRFolderRef!) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func DRFolderCountChildren(_ folder: DRFolder!) -> UInt32 ``` |
| To | ``` func DRFolderCountChildren(_ folder: DRFolderRef!) -> UInt32 ``` |

Modified DRFolderCreateReal(_: UnsafePointer<FSRef>) -> Unmanaged<DRFolderRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFolderCreateReal(_ fsRef: UnsafePointer<FSRef>) -> Unmanaged<DRFolder>! ``` |
| To | ``` func DRFolderCreateReal(_ fsRef: UnsafePointer<FSRef>) -> Unmanaged<DRFolderRef>! ``` |

Modified DRFolderCreateRealWithURL(_: CFURL!) -> Unmanaged<DRFolderRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFolderCreateRealWithURL(_ urlRef: CFURL!) -> Unmanaged<DRFolder>! ``` |
| To | ``` func DRFolderCreateRealWithURL(_ urlRef: CFURL!) -> Unmanaged<DRFolderRef>! ``` |

Modified DRFolderCreateVirtual(_: CFString!) -> Unmanaged<DRFolderRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFolderCreateVirtual(_ baseName: CFString!) -> Unmanaged<DRFolder>! ``` |
| To | ``` func DRFolderCreateVirtual(_ baseName: CFString!) -> Unmanaged<DRFolderRef>! ``` |

Modified DRFolderRemoveChild(_: DRFolderRef!, _: DRFSObjectRef!)

|  | Declaration |
| --- | --- |
| From | ``` func DRFolderRemoveChild(_ parent: DRFolder!, _ child: DRFSObject!) ``` |
| To | ``` func DRFolderRemoveChild(_ parent: DRFolderRef!, _ child: DRFSObjectRef!) ``` |

Modified DRFSObjectCopyBaseName(_: DRFSObjectRef!) -> Unmanaged<CFString>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectCopyBaseName(_ object: DRFSObject!) -> Unmanaged<CFString>! ``` |
| To | ``` func DRFSObjectCopyBaseName(_ object: DRFSObjectRef!) -> Unmanaged<CFString>! ``` |

Modified DRFSObjectCopyFilesystemProperties(_: DRFSObjectRef!, _: CFString!, _: Bool) -> Unmanaged<CFDictionary>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectCopyFilesystemProperties(_ object: DRFSObject!, _ fsKey: CFString!, _ coalesce: Bool) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func DRFSObjectCopyFilesystemProperties(_ object: DRFSObjectRef!, _ fsKey: CFString!, _ coalesce: Bool) -> Unmanaged<CFDictionary>! ``` |

Modified DRFSObjectCopyFilesystemProperty(_: DRFSObjectRef!, _: CFString!, _: CFString!, _: Bool) -> Unmanaged<AnyObject>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectCopyFilesystemProperty(_ object: DRFSObject!, _ fsKey: CFString!, _ propertyKey: CFString!, _ coalesce: Bool) -> Unmanaged<AnyObject>! ``` |
| To | ``` func DRFSObjectCopyFilesystemProperty(_ object: DRFSObjectRef!, _ fsKey: CFString!, _ propertyKey: CFString!, _ coalesce: Bool) -> Unmanaged<AnyObject>! ``` |

Modified DRFSObjectCopyMangledName(_: DRFSObjectRef!, _: CFString!) -> Unmanaged<CFString>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectCopyMangledName(_ object: DRFSObject!, _ fsKey: CFString!) -> Unmanaged<CFString>! ``` |
| To | ``` func DRFSObjectCopyMangledName(_ object: DRFSObjectRef!, _ fsKey: CFString!) -> Unmanaged<CFString>! ``` |

Modified DRFSObjectCopyMangledNames(_: DRFSObjectRef!) -> Unmanaged<CFDictionary>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectCopyMangledNames(_ object: DRFSObject!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func DRFSObjectCopyMangledNames(_ object: DRFSObjectRef!) -> Unmanaged<CFDictionary>! ``` |

Modified DRFSObjectCopyRealURL(_: DRFSObjectRef!) -> Unmanaged<CFURL>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectCopyRealURL(_ object: DRFSObject!) -> Unmanaged<CFURL>! ``` |
| To | ``` func DRFSObjectCopyRealURL(_ object: DRFSObjectRef!) -> Unmanaged<CFURL>! ``` |

Modified DRFSObjectCopySpecificName(_: DRFSObjectRef!, _: CFString!) -> Unmanaged<CFString>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectCopySpecificName(_ object: DRFSObject!, _ fsKey: CFString!) -> Unmanaged<CFString>! ``` |
| To | ``` func DRFSObjectCopySpecificName(_ object: DRFSObjectRef!, _ fsKey: CFString!) -> Unmanaged<CFString>! ``` |

Modified DRFSObjectCopySpecificNames(_: DRFSObjectRef!) -> Unmanaged<CFDictionary>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectCopySpecificNames(_ object: DRFSObject!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func DRFSObjectCopySpecificNames(_ object: DRFSObjectRef!) -> Unmanaged<CFDictionary>! ``` |

Modified DRFSObjectGetFilesystemMask(_: DRFSObjectRef!, _: UnsafeMutablePointer<DRFilesystemMask>, _: UnsafeMutablePointer<DRFilesystemMask>) -> DRFilesystemMask

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectGetFilesystemMask(_ object: DRFSObject!, _ explicitMask: UnsafeMutablePointer<DRFilesystemMask>, _ effectiveMask: UnsafeMutablePointer<DRFilesystemMask>) -> DRFilesystemMask ``` |
| To | ``` func DRFSObjectGetFilesystemMask(_ object: DRFSObjectRef!, _ explicitMask: UnsafeMutablePointer<DRFilesystemMask>, _ effectiveMask: UnsafeMutablePointer<DRFilesystemMask>) -> DRFilesystemMask ``` |

Modified DRFSObjectGetParent(_: DRFSObjectRef!) -> Unmanaged<DRFolderRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectGetParent(_ object: DRFSObject!) -> Unmanaged<DRFolder>! ``` |
| To | ``` func DRFSObjectGetParent(_ object: DRFSObjectRef!) -> Unmanaged<DRFolderRef>! ``` |

Modified DRFSObjectGetRealFSRef(_: DRFSObjectRef!, _: UnsafeMutablePointer<FSRef>)

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectGetRealFSRef(_ object: DRFSObject!, _ fsRef: UnsafeMutablePointer<FSRef>) ``` |
| To | ``` func DRFSObjectGetRealFSRef(_ object: DRFSObjectRef!, _ fsRef: UnsafeMutablePointer<FSRef>) ``` |

Modified DRFSObjectIsVirtual(_: DRFSObjectRef!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectIsVirtual(_ object: DRFSObject!) -> Bool ``` |
| To | ``` func DRFSObjectIsVirtual(_ object: DRFSObjectRef!) -> Bool ``` |

Modified DRFSObjectRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DRFSObjectRef = DRFSObject ``` |
| To | ``` typealias DRFSObjectRef = DRType ``` |

Modified DRFSObjectSetBaseName(_: DRFSObjectRef!, _: CFString!)

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectSetBaseName(_ object: DRFSObject!, _ baseName: CFString!) ``` |
| To | ``` func DRFSObjectSetBaseName(_ object: DRFSObjectRef!, _ baseName: CFString!) ``` |

Modified DRFSObjectSetFilesystemMask(_: DRFSObjectRef!, _: DRFilesystemMask)

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectSetFilesystemMask(_ object: DRFSObject!, _ newMask: DRFilesystemMask) ``` |
| To | ``` func DRFSObjectSetFilesystemMask(_ object: DRFSObjectRef!, _ newMask: DRFilesystemMask) ``` |

Modified DRFSObjectSetFilesystemProperties(_: DRFSObjectRef!, _: CFString!, _: CFDictionary!)

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectSetFilesystemProperties(_ object: DRFSObject!, _ fsKey: CFString!, _ properties: CFDictionary!) ``` |
| To | ``` func DRFSObjectSetFilesystemProperties(_ object: DRFSObjectRef!, _ fsKey: CFString!, _ properties: CFDictionary!) ``` |

Modified DRFSObjectSetFilesystemProperty(_: DRFSObjectRef!, _: CFString!, _: CFString!, _: AnyObject!)

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectSetFilesystemProperty(_ object: DRFSObject!, _ fsKey: CFString!, _ propertyKey: CFString!, _ value: AnyObject!) ``` |
| To | ``` func DRFSObjectSetFilesystemProperty(_ object: DRFSObjectRef!, _ fsKey: CFString!, _ propertyKey: CFString!, _ value: AnyObject!) ``` |

Modified DRFSObjectSetSpecificName(_: DRFSObjectRef!, _: CFString!, _: CFString!)

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectSetSpecificName(_ object: DRFSObject!, _ fsKey: CFString!, _ specificName: CFString!) ``` |
| To | ``` func DRFSObjectSetSpecificName(_ object: DRFSObjectRef!, _ fsKey: CFString!, _ specificName: CFString!) ``` |

Modified DRFSObjectSetSpecificNames(_: DRFSObjectRef!, _: CFDictionary!)

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectSetSpecificNames(_ object: DRFSObject!, _ specificNames: CFDictionary!) ``` |
| To | ``` func DRFSObjectSetSpecificNames(_ object: DRFSObjectRef!, _ specificNames: CFDictionary!) ``` |

Modified DRNotificationCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DRNotificationCallback = (DRNotificationCenter!, UnsafeMutablePointer<Void>, CFString!, DRType!, CFDictionary!) -> Void ``` |
| To | ``` typealias DRNotificationCallback = (DRNotificationCenterRef!, UnsafeMutablePointer<Void>, CFString!, DRType!, CFDictionary!) -> Void ``` |

Modified DRNotificationCenterAddObserver(_: DRNotificationCenterRef!, _: UnsafePointer<Void>, _: DRNotificationCallback!, _: CFString!, _: DRType!)

|  | Declaration |
| --- | --- |
| From | ``` func DRNotificationCenterAddObserver(_ center: DRNotificationCenter!, _ observer: UnsafePointer<Void>, _ callback: DRNotificationCallback!, _ name: CFString!, _ object: DRType!) ``` |
| To | ``` func DRNotificationCenterAddObserver(_ center: DRNotificationCenterRef!, _ observer: UnsafePointer<Void>, _ callback: DRNotificationCallback!, _ name: CFString!, _ object: DRType!) ``` |

Modified DRNotificationCenterCreate() -> Unmanaged<DRNotificationCenterRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRNotificationCenterCreate() -> Unmanaged<DRNotificationCenter>! ``` |
| To | ``` func DRNotificationCenterCreate() -> Unmanaged<DRNotificationCenterRef>! ``` |

Modified DRNotificationCenterCreateRunLoopSource(_: DRNotificationCenterRef!) -> Unmanaged<CFRunLoopSource>!

|  | Declaration |
| --- | --- |
| From | ``` func DRNotificationCenterCreateRunLoopSource(_ center: DRNotificationCenter!) -> Unmanaged<CFRunLoopSource>! ``` |
| To | ``` func DRNotificationCenterCreateRunLoopSource(_ center: DRNotificationCenterRef!) -> Unmanaged<CFRunLoopSource>! ``` |

Modified DRNotificationCenterRemoveObserver(_: DRNotificationCenterRef!, _: UnsafePointer<Void>, _: CFString!, _: DRType!)

|  | Declaration |
| --- | --- |
| From | ``` func DRNotificationCenterRemoveObserver(_ center: DRNotificationCenter!, _ observer: UnsafePointer<Void>, _ name: CFString!, _ object: DRType!) ``` |
| To | ``` func DRNotificationCenterRemoveObserver(_ center: DRNotificationCenterRef!, _ observer: UnsafePointer<Void>, _ name: CFString!, _ object: DRType!) ``` |

Modified DRTrackCallbackProc

|  | Declaration |
| --- | --- |
| From | ``` typealias DRTrackCallbackProc = (DRTrack!, DRTrackMessage, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias DRTrackCallbackProc = (DRTrackRef!, DRTrackMessage, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified DRTrackCreate(_: CFDictionary!, _: DRTrackCallbackProc!) -> Unmanaged<DRTrackRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRTrackCreate(_ properties: CFDictionary!, _ callback: DRTrackCallbackProc!) -> Unmanaged<DRTrack>! ``` |
| To | ``` func DRTrackCreate(_ properties: CFDictionary!, _ callback: DRTrackCallbackProc!) -> Unmanaged<DRTrackRef>! ``` |

Modified DRTrackEstimateLength(_: DRTrackRef!) -> UInt64

|  | Declaration |
| --- | --- |
| From | ``` func DRTrackEstimateLength(_ track: DRTrack!) -> UInt64 ``` |
| To | ``` func DRTrackEstimateLength(_ track: DRTrackRef!) -> UInt64 ``` |

Modified DRTrackGetProperties(_: DRTrackRef!) -> Unmanaged<CFDictionary>!

|  | Declaration |
| --- | --- |
| From | ``` func DRTrackGetProperties(_ track: DRTrack!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func DRTrackGetProperties(_ track: DRTrackRef!) -> Unmanaged<CFDictionary>! ``` |

Modified DRTrackSetProperties(_: DRTrackRef!, _: CFDictionary!)

|  | Declaration |
| --- | --- |
| From | ``` func DRTrackSetProperties(_ track: DRTrack!, _ properties: CFDictionary!) ``` |
| To | ``` func DRTrackSetProperties(_ track: DRTrackRef!, _ properties: CFDictionary!) ``` |

Modified DRTrackSpeedTest(_: DRTrackRef!, _: UInt32, _: UInt32) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func DRTrackSpeedTest(_ track: DRTrack!, _ howManyMilliseconds: UInt32, _ howManyBytes: UInt32) -> Float ``` |
| To | ``` func DRTrackSpeedTest(_ track: DRTrackRef!, _ howManyMilliseconds: UInt32, _ howManyBytes: UInt32) -> Float ``` |

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
