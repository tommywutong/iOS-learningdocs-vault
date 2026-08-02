---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/DiscRecording.html
archived_at: '2026-07-18T02:53:31.371585Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# DiscRecording Changes for Swift

### DiscRecording

Removed DRRefConCallbacks.init(version: UInt, retain: DRRefConRetainCallback, release: DRRefConReleaseCallback)Added DRRefConCallbacks.init(version: UInt, retain: DRRefConRetainCallback!, release: DRRefConReleaseCallback!)Modified DRBurn

|  | Declaration |
| --- | --- |
| From | ``` class DRBurn : NSObject {     init!(forDevice device: DRDevice!) -> DRBurn     class func burnForDevice(_ device: DRDevice!) -> DRBurn!     init!(device device: DRDevice!)     func writeLayout(_ layout: AnyObject!)     func status() -> [NSObject : AnyObject]!     func abort()     func properties() -> [NSObject : AnyObject]!     func setProperties(_ properties: [NSObject : AnyObject]!)     func device() -> DRDevice! } extension DRBurn {     func requestedBurnSpeed() -> Float     func setRequestedBurnSpeed(_ speed: Float)     func appendable() -> Bool     func setAppendable(_ appendable: Bool)     func verifyDisc() -> Bool     func setVerifyDisc(_ verify: Bool)     func completionAction() -> String!     func setCompletionAction(_ action: String!) } extension DRBurn {     class func layoutForImageFile(_ path: String!) -> AnyObject! } ``` |
| To | ``` class DRBurn : NSObject {      init!(forDevice device: DRDevice!)     class func burnForDevice(_ device: DRDevice!) -> DRBurn!     init!(device device: DRDevice!)     func writeLayout(_ layout: AnyObject!)     func status() -> [NSObject : AnyObject]!     func abort()     func properties() -> [NSObject : AnyObject]!     func setProperties(_ properties: [NSObject : AnyObject]!)     func device() -> DRDevice! } extension DRBurn {     func requestedBurnSpeed() -> Float     func setRequestedBurnSpeed(_ speed: Float)     func appendable() -> Bool     func setAppendable(_ appendable: Bool)     func verifyDisc() -> Bool     func setVerifyDisc(_ verify: Bool)     func completionAction() -> String!     func setCompletionAction(_ action: String!) } extension DRBurn {     class func layoutForImageFile(_ path: String!) -> AnyObject! } ``` |

Modified DRBurn.init(forDevice: DRDevice!)

|  | Declaration |
| --- | --- |
| From | ``` init!(forDevice device: DRDevice!) -> DRBurn ``` |
| To | ``` init!(forDevice device: DRDevice!) ``` |

Modified DRDevice

|  | Declaration |
| --- | --- |
| From | ``` class DRDevice : NSObject {     class func devices() -> [AnyObject]!     init!(forBSDName bsdName: String!) -> DRDevice     class func deviceForBSDName(_ bsdName: String!) -> DRDevice!     init!(forIORegistryEntryPath path: String!) -> DRDevice     class func deviceForIORegistryEntryPath(_ path: String!) -> DRDevice!     func isValid() -> Bool     func info() -> [NSObject : AnyObject]!     func status() -> [NSObject : AnyObject]!     func openTray() -> Bool     func closeTray() -> Bool     func ejectMedia() -> Bool     func acquireExclusiveAccess() -> Bool     func releaseExclusiveAccess()     func acquireMediaReservation()     func releaseMediaReservation()     func isEqualToDevice(_ otherDevice: DRDevice!) -> Bool } extension DRDevice {     func writesCD() -> Bool     func writesDVD() -> Bool     func displayName() -> String!     func ioRegistryEntryPath() -> String! } extension DRDevice {     func mediaIsPresent() -> Bool     func mediaIsTransitioning() -> Bool     func mediaIsBusy() -> Bool     func mediaType() -> String!     func mediaIsBlank() -> Bool     func mediaIsAppendable() -> Bool     func mediaIsOverwritable() -> Bool     func mediaIsErasable() -> Bool     func mediaIsReserved() -> Bool     func mediaSpaceOverwritable() -> DRMSF!     func mediaSpaceUsed() -> DRMSF!     func mediaSpaceFree() -> DRMSF!     func trayIsOpen() -> Bool     func bsdName() -> String! } ``` |
| To | ``` class DRDevice : NSObject {     class func devices() -> [AnyObject]!      init!(forBSDName bsdName: String!)     class func deviceForBSDName(_ bsdName: String!) -> DRDevice!      init!(forIORegistryEntryPath path: String!)     class func deviceForIORegistryEntryPath(_ path: String!) -> DRDevice!     func isValid() -> Bool     func info() -> [NSObject : AnyObject]!     func status() -> [NSObject : AnyObject]!     func openTray() -> Bool     func closeTray() -> Bool     func ejectMedia() -> Bool     func acquireExclusiveAccess() -> Bool     func releaseExclusiveAccess()     func acquireMediaReservation()     func releaseMediaReservation()     func isEqualToDevice(_ otherDevice: DRDevice!) -> Bool } extension DRDevice {     func writesCD() -> Bool     func writesDVD() -> Bool     func displayName() -> String!     func ioRegistryEntryPath() -> String! } extension DRDevice {     func mediaIsPresent() -> Bool     func mediaIsTransitioning() -> Bool     func mediaIsBusy() -> Bool     func mediaType() -> String!     func mediaIsBlank() -> Bool     func mediaIsAppendable() -> Bool     func mediaIsOverwritable() -> Bool     func mediaIsErasable() -> Bool     func mediaIsReserved() -> Bool     func mediaSpaceOverwritable() -> DRMSF!     func mediaSpaceUsed() -> DRMSF!     func mediaSpaceFree() -> DRMSF!     func trayIsOpen() -> Bool     func bsdName() -> String! } ``` |

Modified DRDevice.init(forBSDName: String!)

|  | Declaration |
| --- | --- |
| From | ``` init!(forBSDName bsdName: String!) -> DRDevice ``` |
| To | ``` init!(forBSDName bsdName: String!) ``` |

Modified DRDevice.init(forIORegistryEntryPath: String!)

|  | Declaration |
| --- | --- |
| From | ``` init!(forIORegistryEntryPath path: String!) -> DRDevice ``` |
| To | ``` init!(forIORegistryEntryPath path: String!) ``` |

Modified DRErase

|  | Declaration |
| --- | --- |
| From | ``` class DRErase : NSObject {     init!(forDevice device: DRDevice!) -> DRErase     class func eraseForDevice(_ device: DRDevice!) -> DRErase!     init!(device device: DRDevice!)     func start()     func status() -> [NSObject : AnyObject]!     func properties() -> [NSObject : AnyObject]!     func setProperties(_ properties: [NSObject : AnyObject]!)     func device() -> DRDevice! } extension DRErase {     func eraseType() -> String!     func setEraseType(_ type: String!) } ``` |
| To | ``` class DRErase : NSObject {      init!(forDevice device: DRDevice!)     class func eraseForDevice(_ device: DRDevice!) -> DRErase!     init!(device device: DRDevice!)     func start()     func status() -> [NSObject : AnyObject]!     func properties() -> [NSObject : AnyObject]!     func setProperties(_ properties: [NSObject : AnyObject]!)     func device() -> DRDevice! } extension DRErase {     func eraseType() -> String!     func setEraseType(_ type: String!) } ``` |

Modified DRErase.init(forDevice: DRDevice!)

|  | Declaration |
| --- | --- |
| From | ``` init!(forDevice device: DRDevice!) -> DRErase ``` |
| To | ``` init!(forDevice device: DRDevice!) ``` |

Modified DRFile

|  | Declaration |
| --- | --- |
| From | ``` class DRFile : DRFSObject {     init!(path path: String!) -> DRFile     class func fileWithPath(_ path: String!) -> DRFile!     init!(path path: String!) } extension DRFile {     class func virtualFileWithName(_ name: String!, data data: NSData!) -> DRFile!     class func virtualFileWithName(_ name: String!, dataProducer producer: AnyObject!) -> DRFile!     init!(name name: String!, data data: NSData!)     init!(name name: String!, dataProducer producer: AnyObject!) } extension DRFile {     class func hardLinkPointingTo(_ original: DRFile!, inFilesystem filesystem: String!) -> DRFile!     class func symLinkPointingTo(_ original: DRFSObject!, inFilesystem filesystem: String!) -> DRFile!     class func finderAliasPointingTo(_ original: DRFSObject!, inFilesystem filesystem: String!) -> DRFile!     init!(linkType linkType: String!, pointingTo original: DRFSObject!, inFilesystem filesystem: String!) } ``` |
| To | ``` class DRFile : DRFSObject {      init!(path path: String!)     class func fileWithPath(_ path: String!) -> DRFile!     init!(path path: String!) } extension DRFile {     class func virtualFileWithName(_ name: String!, data data: NSData!) -> DRFile!     class func virtualFileWithName(_ name: String!, dataProducer producer: AnyObject!) -> DRFile!     init!(name name: String!, data data: NSData!)     init!(name name: String!, dataProducer producer: AnyObject!) } extension DRFile {     class func hardLinkPointingTo(_ original: DRFile!, inFilesystem filesystem: String!) -> DRFile!     class func symLinkPointingTo(_ original: DRFSObject!, inFilesystem filesystem: String!) -> DRFile!     class func finderAliasPointingTo(_ original: DRFSObject!, inFilesystem filesystem: String!) -> DRFile!     init!(linkType linkType: String!, pointingTo original: DRFSObject!, inFilesystem filesystem: String!) } ``` |

Modified DRFolder

|  | Declaration |
| --- | --- |
| From | ``` class DRFolder : DRFSObject {     init!(path path: String!) -> DRFolder     class func folderWithPath(_ path: String!) -> DRFolder!     init!(path path: String!) } extension DRFolder {     class func virtualFolderWithName(_ name: String!) -> DRFolder!     init!(name name: String!)     func makeVirtual()     func addChild(_ child: DRFSObject!)     func removeChild(_ child: DRFSObject!)     func count() -> Int     func children() -> [AnyObject]! } ``` |
| To | ``` class DRFolder : DRFSObject {      init!(path path: String!)     class func folderWithPath(_ path: String!) -> DRFolder!     init!(path path: String!) } extension DRFolder {     class func virtualFolderWithName(_ name: String!) -> DRFolder!     init!(name name: String!)     func makeVirtual()     func addChild(_ child: DRFSObject!)     func removeChild(_ child: DRFSObject!)     func count() -> Int     func children() -> [AnyObject]! } ``` |

Modified DRRefConCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DRRefConCallbacks {     var version: UInt     var retain: DRRefConRetainCallback     var release: DRRefConReleaseCallback     init()     init(version version: UInt, retain retain: DRRefConRetainCallback, release release: DRRefConReleaseCallback) } ``` |
| To | ``` struct DRRefConCallbacks {     var version: UInt     var retain: DRRefConRetainCallback!     var release: DRRefConReleaseCallback!     init()     init(version version: UInt, retain retain: DRRefConRetainCallback!, release release: DRRefConReleaseCallback!) } ``` |

Modified DRRefConCallbacks.release

|  | Declaration |
| --- | --- |
| From | ``` var release: DRRefConReleaseCallback ``` |
| To | ``` var release: DRRefConReleaseCallback! ``` |

Modified DRRefConCallbacks.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: DRRefConRetainCallback ``` |
| To | ``` var retain: DRRefConRetainCallback! ``` |

Modified DRTrack

|  | Declaration |
| --- | --- |
| From | ``` class DRTrack : NSObject {     init!(producer producer: AnyObject!)     func properties() -> [NSObject : AnyObject]!     func setProperties(_ properties: [NSObject : AnyObject]!)     func testProductionSpeedForInterval(_ interval: NSTimeInterval) -> Float     func testProductionSpeedForLength(_ length: UInt32) -> Float     func estimateLength() -> UInt64 } extension DRTrack {     func length() -> DRMSF!     func preGap() -> DRMSF!     func setPreGap(_ preGap: DRMSF!) } extension DRTrack {     init!(forAudioOfLength length: DRMSF!, producer producer: AnyObject!) -> DRTrack     class func trackForAudioOfLength(_ length: DRMSF!, producer producer: AnyObject!) -> DRTrack!     init!(forAudioFile path: String!) -> DRTrack     class func trackForAudioFile(_ path: String!) -> DRTrack! } extension DRTrack {     init!(forRootFolder rootFolder: DRFolder!) -> DRTrack     class func trackForRootFolder(_ rootFolder: DRFolder!) -> DRTrack! } ``` |
| To | ``` class DRTrack : NSObject {     init!(producer producer: AnyObject!)     func properties() -> [NSObject : AnyObject]!     func setProperties(_ properties: [NSObject : AnyObject]!)     func testProductionSpeedForInterval(_ interval: NSTimeInterval) -> Float     func testProductionSpeedForLength(_ length: UInt32) -> Float     func estimateLength() -> UInt64 } extension DRTrack {     func length() -> DRMSF!     func preGap() -> DRMSF!     func setPreGap(_ preGap: DRMSF!) } extension DRTrack {      init!(forAudioOfLength length: DRMSF!, producer producer: AnyObject!)     class func trackForAudioOfLength(_ length: DRMSF!, producer producer: AnyObject!) -> DRTrack!      init!(forAudioFile path: String!)     class func trackForAudioFile(_ path: String!) -> DRTrack! } extension DRTrack {      init!(forRootFolder rootFolder: DRFolder!)     class func trackForRootFolder(_ rootFolder: DRFolder!) -> DRTrack! } ``` |

Modified DRTrack.init(forAudioFile: String!)

|  | Declaration |
| --- | --- |
| From | ``` init!(forAudioFile path: String!) -> DRTrack ``` |
| To | ``` init!(forAudioFile path: String!) ``` |

Modified DRTrack.init(forAudioOfLength: DRMSF!, producer: AnyObject!)

|  | Declaration |
| --- | --- |
| From | ``` init!(forAudioOfLength length: DRMSF!, producer producer: AnyObject!) -> DRTrack ``` |
| To | ``` init!(forAudioOfLength length: DRMSF!, producer producer: AnyObject!) ``` |

Modified DRTrack.init(forRootFolder: DRFolder!)

|  | Declaration |
| --- | --- |
| From | ``` init!(forRootFolder rootFolder: DRFolder!) -> DRTrack ``` |
| To | ``` init!(forRootFolder rootFolder: DRFolder!) ``` |

Modified DRTrackDataProduction.prepareTrack(_: DRTrack!, forBurn: DRBurn!, toMedia: [NSObject : AnyObject]!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified DRDeviceIsValid(_: DRDevice!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func DRDeviceIsValid(_ device: DRDevice!) -> Boolean ``` |
| To | ``` func DRDeviceIsValid(_ device: DRDevice!) -> Bool ``` |

Modified DRFileCreateVirtualWithCallback(_: CFString!, _: DRFileProc!, _: UnsafeMutablePointer<Void>) -> Unmanaged<DRFile>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFileCreateVirtualWithCallback(_ baseName: CFString!, _ fileProc: DRFileProc, _ fileProcRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<DRFile>! ``` |
| To | ``` func DRFileCreateVirtualWithCallback(_ baseName: CFString!, _ fileProc: DRFileProc!, _ fileProcRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<DRFile>! ``` |

Modified DRFileProc

|  | Declaration |
| --- | --- |
| From | ``` typealias DRFileProc = CFunctionPointer<((UnsafeMutablePointer<Void>, DRFile!, DRFileMessage, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias DRFileProc = (UnsafeMutablePointer<Void>, DRFile!, DRFileMessage, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified DRFSObjectCopyFilesystemProperties(_: DRFSObject!, _: CFString!, _: Bool) -> Unmanaged<CFDictionary>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectCopyFilesystemProperties(_ object: DRFSObject!, _ fsKey: CFString!, _ coalesce: Boolean) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func DRFSObjectCopyFilesystemProperties(_ object: DRFSObject!, _ fsKey: CFString!, _ coalesce: Bool) -> Unmanaged<CFDictionary>! ``` |

Modified DRFSObjectCopyFilesystemProperty(_: DRFSObject!, _: CFString!, _: CFString!, _: Bool) -> Unmanaged<AnyObject>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectCopyFilesystemProperty(_ object: DRFSObject!, _ fsKey: CFString!, _ propertyKey: CFString!, _ coalesce: Boolean) -> Unmanaged<AnyObject>! ``` |
| To | ``` func DRFSObjectCopyFilesystemProperty(_ object: DRFSObject!, _ fsKey: CFString!, _ propertyKey: CFString!, _ coalesce: Bool) -> Unmanaged<AnyObject>! ``` |

Modified DRFSObjectIsVirtual(_: DRFSObject!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectIsVirtual(_ object: DRFSObject!) -> Boolean ``` |
| To | ``` func DRFSObjectIsVirtual(_ object: DRFSObject!) -> Bool ``` |

Modified DRNotificationCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DRNotificationCallback = CFunctionPointer<((DRNotificationCenter!, UnsafeMutablePointer<Void>, CFString!, DRType!, CFDictionary!) -> Void)> ``` |
| To | ``` typealias DRNotificationCallback = (DRNotificationCenter!, UnsafeMutablePointer<Void>, CFString!, DRType!, CFDictionary!) -> Void ``` |

Modified DRNotificationCenterAddObserver(_: DRNotificationCenter!, _: UnsafePointer<Void>, _: DRNotificationCallback!, _: CFString!, _: DRType!)

|  | Declaration |
| --- | --- |
| From | ``` func DRNotificationCenterAddObserver(_ center: DRNotificationCenter!, _ observer: UnsafePointer<Void>, _ callback: DRNotificationCallback, _ name: CFString!, _ object: DRType!) ``` |
| To | ``` func DRNotificationCenterAddObserver(_ center: DRNotificationCenter!, _ observer: UnsafePointer<Void>, _ callback: DRNotificationCallback!, _ name: CFString!, _ object: DRType!) ``` |

Modified DRRefConReleaseCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DRRefConReleaseCallback = CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |
| To | ``` typealias DRRefConReleaseCallback = (UnsafePointer<Void>) -> Void ``` |

Modified DRRefConRetainCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DRRefConRetainCallback = CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` typealias DRRefConRetainCallback = (UnsafePointer<Void>) -> UnsafePointer<Void> ``` |

Modified DRTrackCallbackProc

|  | Declaration |
| --- | --- |
| From | ``` typealias DRTrackCallbackProc = CFunctionPointer<((DRTrack!, DRTrackMessage, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias DRTrackCallbackProc = (DRTrack!, DRTrackMessage, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified DRTrackCreate(_: CFDictionary!, _: DRTrackCallbackProc!) -> Unmanaged<DRTrack>!

|  | Declaration |
| --- | --- |
| From | ``` func DRTrackCreate(_ properties: CFDictionary!, _ callback: DRTrackCallbackProc) -> Unmanaged<DRTrack>! ``` |
| To | ``` func DRTrackCreate(_ properties: CFDictionary!, _ callback: DRTrackCallbackProc!) -> Unmanaged<DRTrack>! ``` |

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
