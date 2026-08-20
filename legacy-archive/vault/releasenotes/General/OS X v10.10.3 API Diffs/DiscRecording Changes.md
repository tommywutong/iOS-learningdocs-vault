---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/DiscRecording.html
archived_at: '2026-07-18T02:52:22.536394Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# DiscRecording Changes

## DiscRecording

Added DRFileForkSizeInfo.init()Added DRFileForkSizeInfo.init(fork: DRFileForkIndex, query: DRFileForkSizeQuery, size: UInt64)Added DRFileProductionInfo.init()Added DRFileProductionInfo.init(requestedAddress: UInt64, buffer: UnsafeMutablePointer<Void>, reqCount: UInt32, actCount: UInt32, blockSize: UInt32, fork: DRFileForkIndex)Added DRRefConCallbacks.init()Added DRRefConCallbacks.init(version: UInt, retain: DRRefConRetainCallback, release: DRRefConReleaseCallback)Added DRTrackProductionInfo.init()Added DRTrackProductionInfo.init(buffer: UnsafeMutablePointer<Void>, reqCount: UInt32, actCount: UInt32, flags: UInt32, blockSize: UInt32, requestedAddress: UInt64)Modified DRBurn.init(device: DRDevice!)

|  | Declaration |
| --- | --- |
| From | ``` init(device device: DRDevice!) ``` |
| To | ``` init!(device device: DRDevice!) ``` |

Modified DRBurn.init(forDevice: DRDevice!)

|  | Declaration |
| --- | --- |
| From | ``` init(forDevice device: DRDevice!) -> DRBurn ``` |
| To | ``` init!(forDevice device: DRDevice!) -> DRBurn ``` |

Modified DRCDTextBlock.init(language: String!, encoding: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(language lang: String!, encoding enc: UInt) ``` |
| To | ``` init!(language lang: String!, encoding enc: UInt) ``` |

Modified DRDevice.init(forBSDName: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(forBSDName bsdName: String!) -> DRDevice ``` |
| To | ``` init!(forBSDName bsdName: String!) -> DRDevice ``` |

Modified DRDevice.init(forIORegistryEntryPath: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(forIORegistryEntryPath path: String!) -> DRDevice ``` |
| To | ``` init!(forIORegistryEntryPath path: String!) -> DRDevice ``` |

Modified DRErase.init(device: DRDevice!)

|  | Declaration |
| --- | --- |
| From | ``` init(device device: DRDevice!) ``` |
| To | ``` init!(device device: DRDevice!) ``` |

Modified DRErase.init(forDevice: DRDevice!)

|  | Declaration |
| --- | --- |
| From | ``` init(forDevice device: DRDevice!) -> DRErase ``` |
| To | ``` init!(forDevice device: DRDevice!) -> DRErase ``` |

Modified DRFile.init(linkType: String!, pointingTo: DRFSObject!, inFilesystem: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(linkType linkType: String!, pointingTo original: DRFSObject!, inFilesystem filesystem: String!) ``` |
| To | ``` init!(linkType linkType: String!, pointingTo original: DRFSObject!, inFilesystem filesystem: String!) ``` |

Modified DRFile.init(name: String!, data: NSData!)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String!, data data: NSData!) ``` |
| To | ``` init!(name name: String!, data data: NSData!) ``` |

Modified DRFile.init(name: String!, dataProducer: AnyObject!)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String!, dataProducer producer: AnyObject!) ``` |
| To | ``` init!(name name: String!, dataProducer producer: AnyObject!) ``` |

Modified DRFile.init(path: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(path path: String!) ``` |
| To | ``` init!(path path: String!) ``` |

Modified DRFileDataProduction.produceFile(DRFile!, fork: DRFileFork, intoBuffer: UnsafeMutablePointer<Int8>, length: UInt32, atAddress: UInt64, blockSize: UInt32) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func produceFile(_ file: DRFile!, fork fork: DRFileFork, intoBuffer buffer: UnsafePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32) -> UInt32 ``` |
| To | ``` func produceFile(_ file: DRFile!, fork fork: DRFileFork, intoBuffer buffer: UnsafeMutablePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32) -> UInt32 ``` |

Modified DRFileForkSizeInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DRFileForkSizeInfo {     var fork: DRFileForkIndex     var query: DRFileForkSizeQuery     var size: UInt64 } ``` |
| To | ``` struct DRFileForkSizeInfo {     var fork: DRFileForkIndex     var query: DRFileForkSizeQuery     var size: UInt64     init()     init(fork fork: DRFileForkIndex, query query: DRFileForkSizeQuery, size size: UInt64) } ``` |

Modified DRFileProductionInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DRFileProductionInfo {     var requestedAddress: UInt64     var buffer: UnsafePointer<()>     var reqCount: UInt32     var actCount: UInt32     var blockSize: UInt32     var fork: DRFileForkIndex } ``` |
| To | ``` struct DRFileProductionInfo {     var requestedAddress: UInt64     var buffer: UnsafeMutablePointer<Void>     var reqCount: UInt32     var actCount: UInt32     var blockSize: UInt32     var fork: DRFileForkIndex     init()     init(requestedAddress requestedAddress: UInt64, buffer buffer: UnsafeMutablePointer<Void>, reqCount reqCount: UInt32, actCount actCount: UInt32, blockSize blockSize: UInt32, fork fork: DRFileForkIndex) } ``` |

Modified DRFileProductionInfo.buffer

|  | Declaration |
| --- | --- |
| From | ``` var buffer: UnsafePointer<()> ``` |
| To | ``` var buffer: UnsafeMutablePointer<Void> ``` |

Modified DRFolder.init(name: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String!) ``` |
| To | ``` init!(name name: String!) ``` |

Modified DRFolder.init(path: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(path path: String!) ``` |
| To | ``` init!(path path: String!) ``` |

Modified DRMSF.init(frames: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(frames frames: UInt32) ``` |
| To | ``` init!(frames frames: UInt32) ``` |

Modified DRMSF.init(string: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(string string: String!) ``` |
| To | ``` init!(string string: String!) ``` |

Modified DRMSFFormatter.init(format: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(format format: String!) ``` |
| To | ``` init!(format format: String!) ``` |

Modified DRRefConCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DRRefConCallbacks {     var version: UInt     var retain: DRRefConRetainCallback     var release: DRRefConReleaseCallback } ``` |
| To | ``` struct DRRefConCallbacks {     var version: UInt     var retain: DRRefConRetainCallback     var release: DRRefConReleaseCallback     init()     init(version version: UInt, retain retain: DRRefConRetainCallback, release release: DRRefConReleaseCallback) } ``` |

Modified DRTrack.init(forAudioFile: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(forAudioFile path: String!) -> DRTrack ``` |
| To | ``` init!(forAudioFile path: String!) -> DRTrack ``` |

Modified DRTrack.init(forAudioOfLength: DRMSF!, producer: AnyObject!)

|  | Declaration |
| --- | --- |
| From | ``` init(forAudioOfLength length: DRMSF!, producer producer: AnyObject!) -> DRTrack ``` |
| To | ``` init!(forAudioOfLength length: DRMSF!, producer producer: AnyObject!) -> DRTrack ``` |

Modified DRTrack.init(forRootFolder: DRFolder!)

|  | Declaration |
| --- | --- |
| From | ``` init(forRootFolder rootFolder: DRFolder!) -> DRTrack ``` |
| To | ``` init!(forRootFolder rootFolder: DRFolder!) -> DRTrack ``` |

Modified DRTrack.init(producer: AnyObject!)

|  | Declaration |
| --- | --- |
| From | ``` init(producer producer: AnyObject!) ``` |
| To | ``` init!(producer producer: AnyObject!) ``` |

Modified DRTrackDataProduction.produceDataForTrack(DRTrack!, intoBuffer: UnsafeMutablePointer<Int8>, length: UInt32, atAddress: UInt64, blockSize: UInt32, ioFlags: UnsafeMutablePointer<UInt32>) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func produceDataForTrack(_ track: DRTrack!, intoBuffer buffer: UnsafePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafePointer<UInt32>) -> UInt32 ``` |
| To | ``` func produceDataForTrack(_ track: DRTrack!, intoBuffer buffer: UnsafeMutablePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>) -> UInt32 ``` |

Modified DRTrackDataProduction.producePreGapForTrack(DRTrack!, intoBuffer: UnsafeMutablePointer<Int8>, length: UInt32, atAddress: UInt64, blockSize: UInt32, ioFlags: UnsafeMutablePointer<UInt32>) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func producePreGapForTrack(_ track: DRTrack!, intoBuffer buffer: UnsafePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafePointer<UInt32>) -> UInt32 ``` |
| To | ``` func producePreGapForTrack(_ track: DRTrack!, intoBuffer buffer: UnsafeMutablePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>) -> UInt32 ``` |

Modified DRTrackDataProduction.verifyDataForTrack(DRTrack!, inBuffer: UnsafePointer<Int8>, length: UInt32, atAddress: UInt64, blockSize: UInt32, ioFlags: UnsafeMutablePointer<UInt32>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func verifyDataForTrack(_ track: DRTrack!, inBuffer buffer: ConstUnsafePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafePointer<UInt32>) -> Bool ``` |
| To | ``` func verifyDataForTrack(_ track: DRTrack!, inBuffer buffer: UnsafePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>) -> Bool ``` |

Modified DRTrackDataProduction.verifyPreGapForTrack(DRTrack!, inBuffer: UnsafePointer<Int8>, length: UInt32, atAddress: UInt64, blockSize: UInt32, ioFlags: UnsafeMutablePointer<UInt32>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func verifyPreGapForTrack(_ track: DRTrack!, inBuffer buffer: ConstUnsafePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafePointer<UInt32>) -> Bool ``` |
| To | ``` func verifyPreGapForTrack(_ track: DRTrack!, inBuffer buffer: UnsafePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>) -> Bool ``` |

Modified DRTrackProductionInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DRTrackProductionInfo {     var buffer: UnsafePointer<()>     var reqCount: UInt32     var actCount: UInt32     var flags: UInt32     var blockSize: UInt32     var requestedAddress: UInt64 } ``` |
| To | ``` struct DRTrackProductionInfo {     var buffer: UnsafeMutablePointer<Void>     var reqCount: UInt32     var actCount: UInt32     var flags: UInt32     var blockSize: UInt32     var requestedAddress: UInt64     init()     init(buffer buffer: UnsafeMutablePointer<Void>, reqCount reqCount: UInt32, actCount actCount: UInt32, flags flags: UInt32, blockSize blockSize: UInt32, requestedAddress requestedAddress: UInt64) } ``` |

Modified DRTrackProductionInfo.buffer

|  | Declaration |
| --- | --- |
| From | ``` var buffer: UnsafePointer<()> ``` |
| To | ``` var buffer: UnsafeMutablePointer<Void> ``` |

Modified DRAbstractFile

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRAbstractFile: NSString! ``` | OS X 10.10 |
| To | ``` let DRAbstractFile: String ``` | OS X 10.2 |

Modified DRAccessDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRAccessDate: NSString! ``` | OS X 10.10 |
| To | ``` let DRAccessDate: String ``` | OS X 10.2 |

Modified DRAllFilesystems

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRAllFilesystems: NSString! ``` | OS X 10.10 |
| To | ``` let DRAllFilesystems: String ``` | OS X 10.2 |

Modified DRApplicationIdentifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRApplicationIdentifier: NSString! ``` | OS X 10.10 |
| To | ``` let DRApplicationIdentifier: String ``` | OS X 10.2 |

Modified DRAttributeModificationDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRAttributeModificationDate: NSString! ``` | OS X 10.10 |
| To | ``` let DRAttributeModificationDate: String ``` | OS X 10.2 |

Modified DRAudioFourChannelKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRAudioFourChannelKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRAudioFourChannelKey: String ``` | OS X 10.3 |

Modified DRAudioPreEmphasisKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRAudioPreEmphasisKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRAudioPreEmphasisKey: String ``` | OS X 10.3 |

Modified DRAudioTrackCreate(UnsafePointer<FSRef>) -> Unmanaged<DRAudioTrack>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRAudioTrackCreate(_ audioFile: ConstUnsafePointer<FSRef>) -> Unmanaged<DRAudioTrack>! ``` | OS X 10.10 |
| To | ``` func DRAudioTrackCreate(_ audioFile: UnsafePointer<FSRef>) -> Unmanaged<DRAudioTrack>! ``` | OS X 10.3 |

Modified DRAudioTrackCreateWithURL(CFURL!) -> Unmanaged<DRAudioTrack>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DRBackupDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBackupDate: NSString! ``` | OS X 10.10 |
| To | ``` let DRBackupDate: String ``` | OS X 10.2 |

Modified DRBibliographicFile

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBibliographicFile: NSString! ``` | OS X 10.10 |
| To | ``` let DRBibliographicFile: String ``` | OS X 10.2 |

Modified DRBlockSize

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBlockSize: NSString! ``` | OS X 10.10 |
| To | ``` let DRBlockSize: String ``` | OS X 10.2 |

Modified DRBlockSizeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBlockSizeKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRBlockSizeKey: String ``` | OS X 10.2 |

Modified DRBlockTypeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBlockTypeKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRBlockTypeKey: String ``` | OS X 10.2 |

Modified DRBurnAbort(DRBurn!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRBurnAppendableKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnAppendableKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnAppendableKey: String ``` | OS X 10.2 |

Modified DRBurnCompletionActionEject

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnCompletionActionEject: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnCompletionActionEject: String ``` | OS X 10.2 |

Modified DRBurnCompletionActionKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnCompletionActionKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnCompletionActionKey: String ``` | OS X 10.2 |

Modified DRBurnCompletionActionMount

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnCompletionActionMount: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnCompletionActionMount: String ``` | OS X 10.2 |

Modified DRBurnCopyStatus(DRBurn!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRBurnCreate(DRDevice!) -> Unmanaged<DRBurn>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRBurnDoubleLayerL0DataZoneBlocksKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnDoubleLayerL0DataZoneBlocksKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnDoubleLayerL0DataZoneBlocksKey: String ``` | OS X 10.4 |

Modified DRBurnFailureActionEject

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnFailureActionEject: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnFailureActionEject: String ``` | OS X 10.3 |

Modified DRBurnFailureActionKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnFailureActionKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnFailureActionKey: String ``` | OS X 10.3 |

Modified DRBurnFailureActionNone

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnFailureActionNone: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnFailureActionNone: String ``` | OS X 10.3 |

Modified DRBurnGetDevice(DRBurn!) -> Unmanaged<DRDevice>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRBurnGetProperties(DRBurn!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRBurnGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRBurnOverwriteDiscKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnOverwriteDiscKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnOverwriteDiscKey: String ``` | OS X 10.3 |

Modified DRBurnRequestedSpeedKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnRequestedSpeedKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnRequestedSpeedKey: String ``` | OS X 10.2 |

Modified DRBurnSetProperties(DRBurn!, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRBurnStatusChangedNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnStatusChangedNotification: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnStatusChangedNotification: String ``` | OS X 10.2 |

Modified DRBurnStrategyBDDAO

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnStrategyBDDAO: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnStrategyBDDAO: String ``` | OS X 10.5 |

Modified DRBurnStrategyCDSAO

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnStrategyCDSAO: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnStrategyCDSAO: String ``` | OS X 10.3 |

Modified DRBurnStrategyCDTAO

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnStrategyCDTAO: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnStrategyCDTAO: String ``` | OS X 10.3 |

Modified DRBurnStrategyDVDDAO

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnStrategyDVDDAO: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnStrategyDVDDAO: String ``` | OS X 10.3 |

Modified DRBurnStrategyIsRequiredKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnStrategyIsRequiredKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnStrategyIsRequiredKey: String ``` | OS X 10.3 |

Modified DRBurnStrategyKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnStrategyKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnStrategyKey: String ``` | OS X 10.3 |

Modified DRBurnTestingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnTestingKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnTestingKey: String ``` | OS X 10.2 |

Modified DRBurnUnderrunProtectionKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnUnderrunProtectionKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnUnderrunProtectionKey: String ``` | OS X 10.2 |

Modified DRBurnVerifyDiscKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnVerifyDiscKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnVerifyDiscKey: String ``` | OS X 10.2 |

Modified DRBurnWriteLayout(DRBurn!, AnyObject!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRCDTextArrangerKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextArrangerKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextArrangerKey: String ``` | OS X 10.4 |

Modified DRCDTextBlockCreate(CFString!, CFStringEncoding) -> Unmanaged<DRCDTextBlock>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DRCDTextBlockCreateArrayFromPackList(CFData!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DRCDTextBlockFlatten(DRCDTextBlock!) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DRCDTextBlockGetProperties(DRCDTextBlock!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DRCDTextBlockGetTrackDictionaries(DRCDTextBlock!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DRCDTextBlockGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DRCDTextBlockGetValue(DRCDTextBlock!, CFIndex, CFString!) -> Unmanaged<AnyObject>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DRCDTextBlockSetProperties(DRCDTextBlock!, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DRCDTextBlockSetTrackDictionaries(DRCDTextBlock!, CFArray!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DRCDTextBlockSetValue(DRCDTextBlock!, CFIndex, CFString!, AnyObject!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DRCDTextCharacterCodeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextCharacterCodeKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextCharacterCodeKey: String ``` | OS X 10.4 |

Modified DRCDTextClosedKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextClosedKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextClosedKey: String ``` | OS X 10.4 |

Modified DRCDTextComposerKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextComposerKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextComposerKey: String ``` | OS X 10.4 |

Modified DRCDTextCopyrightAssertedForNamesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextCopyrightAssertedForNamesKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextCopyrightAssertedForNamesKey: String ``` | OS X 10.4 |

Modified DRCDTextCopyrightAssertedForSpecialMessagesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextCopyrightAssertedForSpecialMessagesKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextCopyrightAssertedForSpecialMessagesKey: String ``` | OS X 10.4 |

Modified DRCDTextCopyrightAssertedForTitlesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextCopyrightAssertedForTitlesKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextCopyrightAssertedForTitlesKey: String ``` | OS X 10.4 |

Modified DRCDTextDiscIdentKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextDiscIdentKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextDiscIdentKey: String ``` | OS X 10.4 |

Modified DRCDTextGenreCodeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextGenreCodeKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextGenreCodeKey: String ``` | OS X 10.4 |

Modified DRCDTextGenreKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextGenreKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextGenreKey: String ``` | OS X 10.4 |

Modified DRCDTextKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextKey: String ``` | OS X 10.4 |

Modified DRCDTextLanguageKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextLanguageKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextLanguageKey: String ``` | OS X 10.4 |

Modified DRCDTextMCNISRCKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextMCNISRCKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextMCNISRCKey: String ``` | OS X 10.4 |

Modified DRCDTextNSStringEncodingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextNSStringEncodingKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextNSStringEncodingKey: String ``` | OS X 10.4 |

Modified DRCDTextPerformerKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextPerformerKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextPerformerKey: String ``` | OS X 10.4 |

Modified DRCDTextSizeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextSizeKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextSizeKey: String ``` | OS X 10.4 |

Modified DRCDTextSongwriterKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextSongwriterKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextSongwriterKey: String ``` | OS X 10.4 |

Modified DRCDTextSpecialMessageKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextSpecialMessageKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextSpecialMessageKey: String ``` | OS X 10.4 |

Modified DRCDTextTOC2Key

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextTOC2Key: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextTOC2Key: String ``` | OS X 10.4 |

Modified DRCDTextTOCKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextTOCKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextTOCKey: String ``` | OS X 10.4 |

Modified DRCDTextTitleKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCDTextTitleKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRCDTextTitleKey: String ``` | OS X 10.4 |

Modified DRContentModificationDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRContentModificationDate: NSString! ``` | OS X 10.10 |
| To | ``` let DRContentModificationDate: String ``` | OS X 10.2 |

Modified DRCopyDeviceArray() -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRCopyLocalizedStringForValue(CFString!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DRCopyrightFile

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCopyrightFile: NSString! ``` | OS X 10.10 |
| To | ``` let DRCopyrightFile: String ``` | OS X 10.2 |

Modified DRCreationDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRCreationDate: NSString! ``` | OS X 10.10 |
| To | ``` let DRCreationDate: String ``` | OS X 10.2 |

Modified DRDVDCopyrightInfoKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDVDCopyrightInfoKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDVDCopyrightInfoKey: String ``` | OS X 10.2 |

Modified DRDVDTimestampKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDVDTimestampKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDVDTimestampKey: String ``` | OS X 10.2 |

Modified DRDataFormKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDataFormKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDataFormKey: String ``` | OS X 10.2 |

Modified DRDataPreparer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDataPreparer: NSString! ``` | OS X 10.10 |
| To | ``` let DRDataPreparer: String ``` | OS X 10.2 |

Modified DRDefaultDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDefaultDate: NSString! ``` | OS X 10.10 |
| To | ``` let DRDefaultDate: String ``` | OS X 10.2 |

Modified DRDeviceAcquireExclusiveAccess(DRDevice!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRDeviceAcquireMediaReservation(DRDevice!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRDeviceAppearedNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceAppearedNotification: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceAppearedNotification: String ``` | OS X 10.2 |

Modified DRDeviceBurnSpeedBD1x

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DRDeviceBurnSpeedCD1x

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRDeviceBurnSpeedDVD1x

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRDeviceBurnSpeedHDDVD1x

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DRDeviceBurnSpeedMax

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRDeviceBurnSpeedsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceBurnSpeedsKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceBurnSpeedsKey: String ``` | OS X 10.2 |

Modified DRDeviceCanTestWriteCDKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanTestWriteCDKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanTestWriteCDKey: String ``` | OS X 10.2 |

Modified DRDeviceCanTestWriteDVDKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanTestWriteDVDKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanTestWriteDVDKey: String ``` | OS X 10.2 |

Modified DRDeviceCanUnderrunProtectCDKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanUnderrunProtectCDKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanUnderrunProtectCDKey: String ``` | OS X 10.2 |

Modified DRDeviceCanUnderrunProtectDVDKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanUnderrunProtectDVDKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanUnderrunProtectDVDKey: String ``` | OS X 10.2 |

Modified DRDeviceCanWriteBDKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteBDKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteBDKey: String ``` | OS X 10.5 |

Modified DRDeviceCanWriteBDREKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteBDREKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteBDREKey: String ``` | OS X 10.5 |

Modified DRDeviceCanWriteBDRKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteBDRKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteBDRKey: String ``` | OS X 10.5 |

Modified DRDeviceCanWriteCDKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteCDKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteCDKey: String ``` | OS X 10.2 |

Modified DRDeviceCanWriteCDRKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteCDRKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteCDRKey: String ``` | OS X 10.2 |

Modified DRDeviceCanWriteCDRWKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteCDRWKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteCDRWKey: String ``` | OS X 10.2 |

Modified DRDeviceCanWriteCDRawKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteCDRawKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteCDRawKey: String ``` | OS X 10.3 |

Modified DRDeviceCanWriteCDSAOKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteCDSAOKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteCDSAOKey: String ``` | OS X 10.3 |

Modified DRDeviceCanWriteCDTAOKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteCDTAOKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteCDTAOKey: String ``` | OS X 10.3 |

Modified DRDeviceCanWriteCDTextKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteCDTextKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteCDTextKey: String ``` | OS X 10.2 |

Modified DRDeviceCanWriteDVDDAOKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteDVDDAOKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteDVDDAOKey: String ``` | OS X 10.3 |

Modified DRDeviceCanWriteDVDKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteDVDKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteDVDKey: String ``` | OS X 10.2 |

Modified DRDeviceCanWriteDVDPlusRDoubleLayerKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteDVDPlusRDoubleLayerKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteDVDPlusRDoubleLayerKey: String ``` | OS X 10.4 |

Modified DRDeviceCanWriteDVDPlusRKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteDVDPlusRKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteDVDPlusRKey: String ``` | OS X 10.3 |

Modified DRDeviceCanWriteDVDPlusRWDoubleLayerKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteDVDPlusRWDoubleLayerKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteDVDPlusRWDoubleLayerKey: String ``` | OS X 10.5 |

Modified DRDeviceCanWriteDVDPlusRWKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteDVDPlusRWKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteDVDPlusRWKey: String ``` | OS X 10.3 |

Modified DRDeviceCanWriteDVDRAMKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteDVDRAMKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteDVDRAMKey: String ``` | OS X 10.2 |

Modified DRDeviceCanWriteDVDRDualLayerKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteDVDRDualLayerKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteDVDRDualLayerKey: String ``` | OS X 10.5 |

Modified DRDeviceCanWriteDVDRKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteDVDRKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteDVDRKey: String ``` | OS X 10.2 |

Modified DRDeviceCanWriteDVDRWDualLayerKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteDVDRWDualLayerKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteDVDRWDualLayerKey: String ``` | OS X 10.5 |

Modified DRDeviceCanWriteDVDRWKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteDVDRWKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteDVDRWKey: String ``` | OS X 10.2 |

Modified DRDeviceCanWriteHDDVDKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteHDDVDKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteHDDVDKey: String ``` | OS X 10.5 |

Modified DRDeviceCanWriteHDDVDRAMKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteHDDVDRAMKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteHDDVDRAMKey: String ``` | OS X 10.5 |

Modified DRDeviceCanWriteHDDVDRDualLayerKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteHDDVDRDualLayerKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteHDDVDRDualLayerKey: String ``` | OS X 10.5 |

Modified DRDeviceCanWriteHDDVDRKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteHDDVDRKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteHDDVDRKey: String ``` | OS X 10.5 |

Modified DRDeviceCanWriteHDDVDRWDualLayerKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteHDDVDRWDualLayerKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteHDDVDRWDualLayerKey: String ``` | OS X 10.5 |

Modified DRDeviceCanWriteHDDVDRWKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteHDDVDRWKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteHDDVDRWKey: String ``` | OS X 10.5 |

Modified DRDeviceCanWriteISRCKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteISRCKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteISRCKey: String ``` | OS X 10.3 |

Modified DRDeviceCanWriteIndexPointsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteIndexPointsKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteIndexPointsKey: String ``` | OS X 10.3 |

Modified DRDeviceCanWriteKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCanWriteKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCanWriteKey: String ``` | OS X 10.2 |

Modified DRDeviceCloseTray(DRDevice!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRDeviceCopyDeviceForBSDName(CFString!) -> Unmanaged<DRDevice>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRDeviceCopyDeviceForIORegistryEntryPath(CFString!) -> Unmanaged<DRDevice>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRDeviceCopyInfo(DRDevice!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRDeviceCopyStatus(DRDevice!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRDeviceCurrentWriteSpeedKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceCurrentWriteSpeedKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceCurrentWriteSpeedKey: String ``` | OS X 10.2 |

Modified DRDeviceDisappearedNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceDisappearedNotification: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceDisappearedNotification: String ``` | OS X 10.2 |

Modified DRDeviceEjectMedia(DRDevice!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRDeviceFirmwareRevisionKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceFirmwareRevisionKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceFirmwareRevisionKey: String ``` | OS X 10.2 |

Modified DRDeviceGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRDeviceIORegistryEntryPathKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceIORegistryEntryPathKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceIORegistryEntryPathKey: String ``` | OS X 10.2 |

Modified DRDeviceIsBusyKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceIsBusyKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceIsBusyKey: String ``` | OS X 10.2 |

Modified DRDeviceIsTrayOpenKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceIsTrayOpenKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceIsTrayOpenKey: String ``` | OS X 10.2 |

Modified DRDeviceIsValid(DRDevice!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRDeviceKPSForXFactor(DRType!, Float) -> Float

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRDeviceKPSForXFactor(_ deviceOrMediaType: DRTypeRef!, _ xfactor: Float) -> Float ``` | OS X 10.10 |
| To | ``` func DRDeviceKPSForXFactor(_ deviceOrMediaType: DRType!, _ xfactor: Float) -> Float ``` | OS X 10.5 |

Modified DRDeviceLoadingMechanismCanEjectKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceLoadingMechanismCanEjectKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceLoadingMechanismCanEjectKey: String ``` | OS X 10.3 |

Modified DRDeviceLoadingMechanismCanInjectKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceLoadingMechanismCanInjectKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceLoadingMechanismCanInjectKey: String ``` | OS X 10.3 |

Modified DRDeviceLoadingMechanismCanOpenKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceLoadingMechanismCanOpenKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceLoadingMechanismCanOpenKey: String ``` | OS X 10.3 |

Modified DRDeviceMaximumWriteSpeedKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMaximumWriteSpeedKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMaximumWriteSpeedKey: String ``` | OS X 10.2 |

Modified DRDeviceMediaBSDNameKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaBSDNameKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaBSDNameKey: String ``` | OS X 10.2 |

Modified DRDeviceMediaBlocksFreeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaBlocksFreeKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaBlocksFreeKey: String ``` | OS X 10.2 |

Modified DRDeviceMediaBlocksOverwritableKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaBlocksOverwritableKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaBlocksOverwritableKey: String ``` | OS X 10.3 |

Modified DRDeviceMediaBlocksUsedKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaBlocksUsedKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaBlocksUsedKey: String ``` | OS X 10.2 |

Modified DRDeviceMediaClassBD

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaClassBD: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaClassBD: String ``` | OS X 10.5 |

Modified DRDeviceMediaClassCD

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaClassCD: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaClassCD: String ``` | OS X 10.2 |

Modified DRDeviceMediaClassDVD

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaClassDVD: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaClassDVD: String ``` | OS X 10.2 |

Modified DRDeviceMediaClassHDDVD

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaClassHDDVD: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaClassHDDVD: String ``` | OS X 10.5 |

Modified DRDeviceMediaClassKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaClassKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaClassKey: String ``` | OS X 10.2 |

Modified DRDeviceMediaClassUnknown

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaClassUnknown: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaClassUnknown: String ``` | OS X 10.2 |

Modified DRDeviceMediaDoubleLayerL0DataZoneBlocksKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaDoubleLayerL0DataZoneBlocksKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaDoubleLayerL0DataZoneBlocksKey: String ``` | OS X 10.4 |

Modified DRDeviceMediaFreeSpaceKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaFreeSpaceKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaFreeSpaceKey: String ``` | OS X 10.2 |

Modified DRDeviceMediaInfoKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaInfoKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaInfoKey: String ``` | OS X 10.2 |

Modified DRDeviceMediaIsAppendableKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaIsAppendableKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaIsAppendableKey: String ``` | OS X 10.2 |

Modified DRDeviceMediaIsBlankKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaIsBlankKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaIsBlankKey: String ``` | OS X 10.2 |

Modified DRDeviceMediaIsErasableKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaIsErasableKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaIsErasableKey: String ``` | OS X 10.2 |

Modified DRDeviceMediaIsOverwritableKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaIsOverwritableKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaIsOverwritableKey: String ``` | OS X 10.3 |

Modified DRDeviceMediaIsReservedKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaIsReservedKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaIsReservedKey: String ``` | OS X 10.2 |

Modified DRDeviceMediaOverwritableSpaceKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaOverwritableSpaceKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaOverwritableSpaceKey: String ``` | OS X 10.3 |

Modified DRDeviceMediaSessionCountKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaSessionCountKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaSessionCountKey: String ``` | OS X 10.2 |

Modified DRDeviceMediaStateInTransition

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaStateInTransition: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaStateInTransition: String ``` | OS X 10.2 |

Modified DRDeviceMediaStateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaStateKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaStateKey: String ``` | OS X 10.2 |

Modified DRDeviceMediaStateMediaPresent

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaStateMediaPresent: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaStateMediaPresent: String ``` | OS X 10.2 |

Modified DRDeviceMediaStateNone

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaStateNone: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaStateNone: String ``` | OS X 10.2 |

Modified DRDeviceMediaTrackCountKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTrackCountKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTrackCountKey: String ``` | OS X 10.2 |

Modified DRDeviceMediaTypeBDR

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeBDR: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeBDR: String ``` | OS X 10.5 |

Modified DRDeviceMediaTypeBDRE

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeBDRE: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeBDRE: String ``` | OS X 10.5 |

Modified DRDeviceMediaTypeBDROM

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeBDROM: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeBDROM: String ``` | OS X 10.5 |

Modified DRDeviceMediaTypeCDR

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeCDR: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeCDR: String ``` | OS X 10.2 |

Modified DRDeviceMediaTypeCDROM

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeCDROM: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeCDROM: String ``` | OS X 10.2 |

Modified DRDeviceMediaTypeCDRW

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeCDRW: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeCDRW: String ``` | OS X 10.2 |

Modified DRDeviceMediaTypeDVDPlusR

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeDVDPlusR: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeDVDPlusR: String ``` | OS X 10.3 |

Modified DRDeviceMediaTypeDVDPlusRDoubleLayer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeDVDPlusRDoubleLayer: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeDVDPlusRDoubleLayer: String ``` | OS X 10.4 |

Modified DRDeviceMediaTypeDVDPlusRW

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeDVDPlusRW: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeDVDPlusRW: String ``` | OS X 10.3 |

Modified DRDeviceMediaTypeDVDPlusRWDoubleLayer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeDVDPlusRWDoubleLayer: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeDVDPlusRWDoubleLayer: String ``` | OS X 10.5 |

Modified DRDeviceMediaTypeDVDR

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeDVDR: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeDVDR: String ``` | OS X 10.2 |

Modified DRDeviceMediaTypeDVDRAM

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeDVDRAM: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeDVDRAM: String ``` | OS X 10.2 |

Modified DRDeviceMediaTypeDVDRDualLayer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeDVDRDualLayer: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeDVDRDualLayer: String ``` | OS X 10.5 |

Modified DRDeviceMediaTypeDVDROM

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeDVDROM: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeDVDROM: String ``` | OS X 10.2 |

Modified DRDeviceMediaTypeDVDRW

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeDVDRW: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeDVDRW: String ``` | OS X 10.2 |

Modified DRDeviceMediaTypeDVDRWDualLayer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeDVDRWDualLayer: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeDVDRWDualLayer: String ``` | OS X 10.5 |

Modified DRDeviceMediaTypeHDDVDR

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeHDDVDR: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeHDDVDR: String ``` | OS X 10.5 |

Modified DRDeviceMediaTypeHDDVDRAM

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeHDDVDRAM: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeHDDVDRAM: String ``` | OS X 10.5 |

Modified DRDeviceMediaTypeHDDVDRDualLayer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeHDDVDRDualLayer: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeHDDVDRDualLayer: String ``` | OS X 10.5 |

Modified DRDeviceMediaTypeHDDVDROM

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeHDDVDROM: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeHDDVDROM: String ``` | OS X 10.5 |

Modified DRDeviceMediaTypeHDDVDRW

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeHDDVDRW: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeHDDVDRW: String ``` | OS X 10.5 |

Modified DRDeviceMediaTypeHDDVDRWDualLayer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeHDDVDRWDualLayer: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeHDDVDRWDualLayer: String ``` | OS X 10.5 |

Modified DRDeviceMediaTypeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeKey: String ``` | OS X 10.2 |

Modified DRDeviceMediaTypeUnknown

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaTypeUnknown: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaTypeUnknown: String ``` | OS X 10.2 |

Modified DRDeviceMediaUsedSpaceKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceMediaUsedSpaceKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceMediaUsedSpaceKey: String ``` | OS X 10.2 |

Modified DRDeviceOpenTray(DRDevice!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRDevicePhysicalInterconnectATAPI

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDevicePhysicalInterconnectATAPI: NSString! ``` | OS X 10.10 |
| To | ``` let DRDevicePhysicalInterconnectATAPI: String ``` | OS X 10.2 |

Modified DRDevicePhysicalInterconnectFibreChannel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDevicePhysicalInterconnectFibreChannel: NSString! ``` | OS X 10.10 |
| To | ``` let DRDevicePhysicalInterconnectFibreChannel: String ``` | OS X 10.3 |

Modified DRDevicePhysicalInterconnectFireWire

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDevicePhysicalInterconnectFireWire: NSString! ``` | OS X 10.10 |
| To | ``` let DRDevicePhysicalInterconnectFireWire: String ``` | OS X 10.2 |

Modified DRDevicePhysicalInterconnectKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDevicePhysicalInterconnectKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDevicePhysicalInterconnectKey: String ``` | OS X 10.2 |

Modified DRDevicePhysicalInterconnectLocationExternal

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDevicePhysicalInterconnectLocationExternal: NSString! ``` | OS X 10.10 |
| To | ``` let DRDevicePhysicalInterconnectLocationExternal: String ``` | OS X 10.2 |

Modified DRDevicePhysicalInterconnectLocationInternal

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDevicePhysicalInterconnectLocationInternal: NSString! ``` | OS X 10.10 |
| To | ``` let DRDevicePhysicalInterconnectLocationInternal: String ``` | OS X 10.2 |

Modified DRDevicePhysicalInterconnectLocationKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDevicePhysicalInterconnectLocationKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDevicePhysicalInterconnectLocationKey: String ``` | OS X 10.2 |

Modified DRDevicePhysicalInterconnectLocationUnknown

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDevicePhysicalInterconnectLocationUnknown: NSString! ``` | OS X 10.10 |
| To | ``` let DRDevicePhysicalInterconnectLocationUnknown: String ``` | OS X 10.2 |

Modified DRDevicePhysicalInterconnectSCSI

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDevicePhysicalInterconnectSCSI: NSString! ``` | OS X 10.10 |
| To | ``` let DRDevicePhysicalInterconnectSCSI: String ``` | OS X 10.2 |

Modified DRDevicePhysicalInterconnectUSB

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDevicePhysicalInterconnectUSB: NSString! ``` | OS X 10.10 |
| To | ``` let DRDevicePhysicalInterconnectUSB: String ``` | OS X 10.2 |

Modified DRDeviceProductNameKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceProductNameKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceProductNameKey: String ``` | OS X 10.2 |

Modified DRDeviceReleaseExclusiveAccess(DRDevice!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRDeviceReleaseMediaReservation(DRDevice!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRDeviceStatusChangedNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceStatusChangedNotification: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceStatusChangedNotification: String ``` | OS X 10.2 |

Modified DRDeviceSupportLevelAppleShipping

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceSupportLevelAppleShipping: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceSupportLevelAppleShipping: String ``` | OS X 10.2 |

Modified DRDeviceSupportLevelAppleSupported

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceSupportLevelAppleSupported: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceSupportLevelAppleSupported: String ``` | OS X 10.2 |

Modified DRDeviceSupportLevelKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceSupportLevelKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceSupportLevelKey: String ``` | OS X 10.2 |

Modified DRDeviceSupportLevelNone

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceSupportLevelNone: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceSupportLevelNone: String ``` | OS X 10.2 |

Modified DRDeviceSupportLevelUnsupported

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceSupportLevelUnsupported: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceSupportLevelUnsupported: String ``` | OS X 10.3 |

Modified DRDeviceSupportLevelVendorSupported

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceSupportLevelVendorSupported: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceSupportLevelVendorSupported: String ``` | OS X 10.2 |

Modified DRDeviceTrackInfoKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceTrackInfoKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceTrackInfoKey: String ``` | OS X 10.3 |

Modified DRDeviceTrackRefsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceTrackRefsKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceTrackRefsKey: String ``` | OS X 10.3 |

Modified DRDeviceVendorNameKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceVendorNameKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceVendorNameKey: String ``` | OS X 10.2 |

Modified DRDeviceWriteBufferSizeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceWriteBufferSizeKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceWriteBufferSizeKey: String ``` | OS X 10.3 |

Modified DRDeviceWriteCapabilitiesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRDeviceWriteCapabilitiesKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRDeviceWriteCapabilitiesKey: String ``` | OS X 10.2 |

Modified DRDeviceXFactorForKPS(DRType!, Float) -> Float

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRDeviceXFactorForKPS(_ deviceOrMediaType: DRTypeRef!, _ kps: Float) -> Float ``` | OS X 10.10 |
| To | ``` func DRDeviceXFactorForKPS(_ deviceOrMediaType: DRType!, _ kps: Float) -> Float ``` | OS X 10.5 |

Modified DREffectiveDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DREffectiveDate: NSString! ``` | OS X 10.10 |
| To | ``` let DREffectiveDate: String ``` | OS X 10.2 |

Modified DREraseCopyStatus(DRErase!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DREraseCreate(DRDevice!) -> Unmanaged<DRErase>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DREraseGetDevice(DRErase!) -> Unmanaged<DRDevice>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DREraseGetProperties(DRErase!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DREraseGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DREraseSetProperties(DRErase!, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DREraseStart(DRErase!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DREraseStatusChangedNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DREraseStatusChangedNotification: NSString! ``` | OS X 10.10 |
| To | ``` let DREraseStatusChangedNotification: String ``` | OS X 10.2 |

Modified DREraseTypeComplete

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DREraseTypeComplete: NSString! ``` | OS X 10.10 |
| To | ``` let DREraseTypeComplete: String ``` | OS X 10.2 |

Modified DREraseTypeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DREraseTypeKey: NSString! ``` | OS X 10.10 |
| To | ``` let DREraseTypeKey: String ``` | OS X 10.2 |

Modified DREraseTypeQuick

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DREraseTypeQuick: NSString! ``` | OS X 10.10 |
| To | ``` let DREraseTypeQuick: String ``` | OS X 10.2 |

Modified DRErrorStatusAdditionalSenseStringKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRErrorStatusAdditionalSenseStringKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRErrorStatusAdditionalSenseStringKey: String ``` | OS X 10.2 |

Modified DRErrorStatusErrorInfoStringKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRErrorStatusErrorInfoStringKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRErrorStatusErrorInfoStringKey: String ``` | OS X 10.4 |

Modified DRErrorStatusErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRErrorStatusErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRErrorStatusErrorKey: String ``` | OS X 10.2 |

Modified DRErrorStatusErrorStringKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRErrorStatusErrorStringKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRErrorStatusErrorStringKey: String ``` | OS X 10.2 |

Modified DRErrorStatusKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRErrorStatusKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRErrorStatusKey: String ``` | OS X 10.2 |

Modified DRErrorStatusSenseCodeStringKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRErrorStatusSenseCodeStringKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRErrorStatusSenseCodeStringKey: String ``` | OS X 10.2 |

Modified DRErrorStatusSenseKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRErrorStatusSenseKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRErrorStatusSenseKey: String ``` | OS X 10.2 |

Modified DRExpirationDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRExpirationDate: NSString! ``` | OS X 10.10 |
| To | ``` let DRExpirationDate: String ``` | OS X 10.2 |

Modified DRFSObjectCopyBaseName(DRFSObject!) -> Unmanaged<CFString>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFSObjectCopyBaseName(_ object: DRFSObjectRef!) -> Unmanaged<CFString>! ``` | OS X 10.10 |
| To | ``` func DRFSObjectCopyBaseName(_ object: DRFSObject!) -> Unmanaged<CFString>! ``` | OS X 10.2 |

Modified DRFSObjectCopyFilesystemProperties(DRFSObject!, CFString!, Boolean) -> Unmanaged<CFDictionary>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFSObjectCopyFilesystemProperties(_ object: DRFSObjectRef!, _ fsKey: CFString!, _ coalesce: Boolean) -> Unmanaged<CFDictionary>! ``` | OS X 10.10 |
| To | ``` func DRFSObjectCopyFilesystemProperties(_ object: DRFSObject!, _ fsKey: CFString!, _ coalesce: Boolean) -> Unmanaged<CFDictionary>! ``` | OS X 10.2 |

Modified DRFSObjectCopyFilesystemProperty(DRFSObject!, CFString!, CFString!, Boolean) -> Unmanaged<AnyObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFSObjectCopyFilesystemProperty(_ object: DRFSObjectRef!, _ fsKey: CFString!, _ propertyKey: CFString!, _ coalesce: Boolean) -> Unmanaged<AnyObject>! ``` | OS X 10.10 |
| To | ``` func DRFSObjectCopyFilesystemProperty(_ object: DRFSObject!, _ fsKey: CFString!, _ propertyKey: CFString!, _ coalesce: Boolean) -> Unmanaged<AnyObject>! ``` | OS X 10.2 |

Modified DRFSObjectCopyMangledName(DRFSObject!, CFString!) -> Unmanaged<CFString>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFSObjectCopyMangledName(_ object: DRFSObjectRef!, _ fsKey: CFString!) -> Unmanaged<CFString>! ``` | OS X 10.10 |
| To | ``` func DRFSObjectCopyMangledName(_ object: DRFSObject!, _ fsKey: CFString!) -> Unmanaged<CFString>! ``` | OS X 10.2 |

Modified DRFSObjectCopyMangledNames(DRFSObject!) -> Unmanaged<CFDictionary>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFSObjectCopyMangledNames(_ object: DRFSObjectRef!) -> Unmanaged<CFDictionary>! ``` | OS X 10.10 |
| To | ``` func DRFSObjectCopyMangledNames(_ object: DRFSObject!) -> Unmanaged<CFDictionary>! ``` | OS X 10.2 |

Modified DRFSObjectCopyRealURL(DRFSObject!) -> Unmanaged<CFURL>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFSObjectCopyRealURL(_ object: DRFSObjectRef!) -> Unmanaged<CFURL>! ``` | OS X 10.10 |
| To | ``` func DRFSObjectCopyRealURL(_ object: DRFSObject!) -> Unmanaged<CFURL>! ``` | OS X 10.2 |

Modified DRFSObjectCopySpecificName(DRFSObject!, CFString!) -> Unmanaged<CFString>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFSObjectCopySpecificName(_ object: DRFSObjectRef!, _ fsKey: CFString!) -> Unmanaged<CFString>! ``` | OS X 10.10 |
| To | ``` func DRFSObjectCopySpecificName(_ object: DRFSObject!, _ fsKey: CFString!) -> Unmanaged<CFString>! ``` | OS X 10.2 |

Modified DRFSObjectCopySpecificNames(DRFSObject!) -> Unmanaged<CFDictionary>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFSObjectCopySpecificNames(_ object: DRFSObjectRef!) -> Unmanaged<CFDictionary>! ``` | OS X 10.10 |
| To | ``` func DRFSObjectCopySpecificNames(_ object: DRFSObject!) -> Unmanaged<CFDictionary>! ``` | OS X 10.2 |

Modified DRFSObjectGetFilesystemMask(DRFSObject!, UnsafeMutablePointer<DRFilesystemMask>, UnsafeMutablePointer<DRFilesystemMask>) -> DRFilesystemMask

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFSObjectGetFilesystemMask(_ object: DRFSObjectRef!, _ explicitMask: UnsafePointer<DRFilesystemMask>, _ effectiveMask: UnsafePointer<DRFilesystemMask>) -> DRFilesystemMask ``` | OS X 10.10 |
| To | ``` func DRFSObjectGetFilesystemMask(_ object: DRFSObject!, _ explicitMask: UnsafeMutablePointer<DRFilesystemMask>, _ effectiveMask: UnsafeMutablePointer<DRFilesystemMask>) -> DRFilesystemMask ``` | OS X 10.2 |

Modified DRFSObjectGetParent(DRFSObject!) -> Unmanaged<DRFolder>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFSObjectGetParent(_ object: DRFSObjectRef!) -> Unmanaged<DRFolder>! ``` | OS X 10.10 |
| To | ``` func DRFSObjectGetParent(_ object: DRFSObject!) -> Unmanaged<DRFolder>! ``` | OS X 10.2 |

Modified DRFSObjectGetRealFSRef(DRFSObject!, UnsafeMutablePointer<FSRef>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFSObjectGetRealFSRef(_ object: DRFSObjectRef!, _ fsRef: UnsafePointer<FSRef>) ``` | OS X 10.10 |
| To | ``` func DRFSObjectGetRealFSRef(_ object: DRFSObject!, _ fsRef: UnsafeMutablePointer<FSRef>) ``` | OS X 10.2 |

Modified DRFSObjectIsVirtual(DRFSObject!) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFSObjectIsVirtual(_ object: DRFSObjectRef!) -> Boolean ``` | OS X 10.10 |
| To | ``` func DRFSObjectIsVirtual(_ object: DRFSObject!) -> Boolean ``` | OS X 10.2 |

Modified DRFSObjectRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DRFSObjectRef = DRTypeRef ``` |
| To | ``` typealias DRFSObjectRef = DRFSObject ``` |

Modified DRFSObjectSetBaseName(DRFSObject!, CFString!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFSObjectSetBaseName(_ object: DRFSObjectRef!, _ baseName: CFString!) ``` | OS X 10.10 |
| To | ``` func DRFSObjectSetBaseName(_ object: DRFSObject!, _ baseName: CFString!) ``` | OS X 10.2 |

Modified DRFSObjectSetFilesystemMask(DRFSObject!, DRFilesystemMask)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFSObjectSetFilesystemMask(_ object: DRFSObjectRef!, _ newMask: DRFilesystemMask) ``` | OS X 10.10 |
| To | ``` func DRFSObjectSetFilesystemMask(_ object: DRFSObject!, _ newMask: DRFilesystemMask) ``` | OS X 10.2 |

Modified DRFSObjectSetFilesystemProperties(DRFSObject!, CFString!, CFDictionary!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFSObjectSetFilesystemProperties(_ object: DRFSObjectRef!, _ fsKey: CFString!, _ properties: CFDictionary!) ``` | OS X 10.10 |
| To | ``` func DRFSObjectSetFilesystemProperties(_ object: DRFSObject!, _ fsKey: CFString!, _ properties: CFDictionary!) ``` | OS X 10.2 |

Modified DRFSObjectSetFilesystemProperty(DRFSObject!, CFString!, CFString!, AnyObject!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFSObjectSetFilesystemProperty(_ object: DRFSObjectRef!, _ fsKey: CFString!, _ propertyKey: CFString!, _ value: AnyObject!) ``` | OS X 10.10 |
| To | ``` func DRFSObjectSetFilesystemProperty(_ object: DRFSObject!, _ fsKey: CFString!, _ propertyKey: CFString!, _ value: AnyObject!) ``` | OS X 10.2 |

Modified DRFSObjectSetSpecificName(DRFSObject!, CFString!, CFString!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFSObjectSetSpecificName(_ object: DRFSObjectRef!, _ fsKey: CFString!, _ specificName: CFString!) ``` | OS X 10.10 |
| To | ``` func DRFSObjectSetSpecificName(_ object: DRFSObject!, _ fsKey: CFString!, _ specificName: CFString!) ``` | OS X 10.2 |

Modified DRFSObjectSetSpecificNames(DRFSObject!, CFDictionary!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFSObjectSetSpecificNames(_ object: DRFSObjectRef!, _ specificNames: CFDictionary!) ``` | OS X 10.10 |
| To | ``` func DRFSObjectSetSpecificNames(_ object: DRFSObject!, _ specificNames: CFDictionary!) ``` | OS X 10.2 |

Modified DRFileCreateReal(UnsafePointer<FSRef>) -> Unmanaged<DRFile>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFileCreateReal(_ fsRef: ConstUnsafePointer<FSRef>) -> Unmanaged<DRFile>! ``` | OS X 10.10 |
| To | ``` func DRFileCreateReal(_ fsRef: UnsafePointer<FSRef>) -> Unmanaged<DRFile>! ``` | OS X 10.2 |

Modified DRFileCreateRealWithURL(CFURL!) -> Unmanaged<DRFile>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRFileCreateVirtualLink(DRFSObject!, DRLinkType, CFString!) -> Unmanaged<DRFile>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFileCreateVirtualLink(_ original: DRFSObjectRef!, _ linkType: DRLinkType, _ fsKey: CFString!) -> Unmanaged<DRFile>! ``` | OS X 10.10 |
| To | ``` func DRFileCreateVirtualLink(_ original: DRFSObject!, _ linkType: DRLinkType, _ fsKey: CFString!) -> Unmanaged<DRFile>! ``` | OS X 10.2 |

Modified DRFileCreateVirtualWithCallback(CFString!, DRFileProc, UnsafeMutablePointer<Void>) -> Unmanaged<DRFile>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFileCreateVirtualWithCallback(_ baseName: CFString!, _ fileProc: DRFileProc, _ fileProcRefCon: UnsafePointer<()>) -> Unmanaged<DRFile>! ``` | OS X 10.10 |
| To | ``` func DRFileCreateVirtualWithCallback(_ baseName: CFString!, _ fileProc: DRFileProc, _ fileProcRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<DRFile>! ``` | OS X 10.2 |

Modified DRFileCreateVirtualWithData(CFString!, UnsafeMutablePointer<Void>, UInt32) -> Unmanaged<DRFile>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFileCreateVirtualWithData(_ baseName: CFString!, _ fileData: UnsafePointer<()>, _ fileDataLength: UInt32) -> Unmanaged<DRFile>! ``` | OS X 10.10 |
| To | ``` func DRFileCreateVirtualWithData(_ baseName: CFString!, _ fileData: UnsafeMutablePointer<Void>, _ fileDataLength: UInt32) -> Unmanaged<DRFile>! ``` | OS X 10.2 |

Modified DRFileGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRFileProc

|  | Declaration |
| --- | --- |
| From | ``` typealias DRFileProc = CFunctionPointer<((UnsafePointer<()>, DRFile!, DRFileMessage, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias DRFileProc = CFunctionPointer<((UnsafeMutablePointer<Void>, DRFile!, DRFileMessage, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified DRFilesystemTrackCreate(DRFolder!) -> Unmanaged<DRFilesystemTrack>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRFilesystemTrackEstimateOverhead(UInt64, UInt32, DRFilesystemMask) -> UInt64

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DRFolderAddChild(DRFolder!, DRFSObject!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFolderAddChild(_ parent: DRFolder!, _ newChild: DRFSObjectRef!) ``` | OS X 10.10 |
| To | ``` func DRFolderAddChild(_ parent: DRFolder!, _ newChild: DRFSObject!) ``` | OS X 10.2 |

Modified DRFolderConvertRealToVirtual(DRFolder!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRFolderCopyChildren(DRFolder!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRFolderCountChildren(DRFolder!) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRFolderCreateReal(UnsafePointer<FSRef>) -> Unmanaged<DRFolder>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFolderCreateReal(_ fsRef: ConstUnsafePointer<FSRef>) -> Unmanaged<DRFolder>! ``` | OS X 10.10 |
| To | ``` func DRFolderCreateReal(_ fsRef: UnsafePointer<FSRef>) -> Unmanaged<DRFolder>! ``` | OS X 10.2 |

Modified DRFolderCreateRealWithURL(CFURL!) -> Unmanaged<DRFolder>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRFolderCreateVirtual(CFString!) -> Unmanaged<DRFolder>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRFolderGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRFolderRemoveChild(DRFolder!, DRFSObject!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRFolderRemoveChild(_ parent: DRFolder!, _ child: DRFSObjectRef!) ``` | OS X 10.10 |
| To | ``` func DRFolderRemoveChild(_ parent: DRFolder!, _ child: DRFSObject!) ``` | OS X 10.2 |

Modified DRFreeBlocksKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRFreeBlocksKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRFreeBlocksKey: String ``` | OS X 10.3 |

Modified DRGetRefCon(DRType!) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRGetRefCon(_ ref: DRTypeRef!) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func DRGetRefCon(_ ref: DRType!) -> UnsafeMutablePointer<Void> ``` | OS X 10.2 |

Modified DRHFSPlus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRHFSPlus: NSString! ``` | OS X 10.10 |
| To | ``` let DRHFSPlus: String ``` | OS X 10.2 |

Modified DRHFSPlusCatalogNodeID

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRHFSPlusCatalogNodeID: NSString! ``` | OS X 10.10 |
| To | ``` let DRHFSPlusCatalogNodeID: String ``` | OS X 10.2 |

Modified DRHFSPlusTextEncodingHint

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRHFSPlusTextEncodingHint: NSString! ``` | OS X 10.10 |
| To | ``` let DRHFSPlusTextEncodingHint: String ``` | OS X 10.2 |

Modified DRISO9660

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRISO9660: NSString! ``` | OS X 10.10 |
| To | ``` let DRISO9660: String ``` | OS X 10.2 |

Modified DRISO9660LevelOne

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRISO9660LevelOne: NSString! ``` | OS X 10.10 |
| To | ``` let DRISO9660LevelOne: String ``` | OS X 10.2 |

Modified DRISO9660LevelTwo

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRISO9660LevelTwo: NSString! ``` | OS X 10.10 |
| To | ``` let DRISO9660LevelTwo: String ``` | OS X 10.2 |

Modified DRISO9660VersionNumber

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRISO9660VersionNumber: NSString! ``` | OS X 10.10 |
| To | ``` let DRISO9660VersionNumber: String ``` | OS X 10.2 |

Modified DRISOLevel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRISOLevel: NSString! ``` | OS X 10.10 |
| To | ``` let DRISOLevel: String ``` | OS X 10.2 |

Modified DRISOMacExtensions

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRISOMacExtensions: NSString! ``` | OS X 10.10 |
| To | ``` let DRISOMacExtensions: String ``` | OS X 10.2 |

Modified DRISORockRidgeExtensions

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRISORockRidgeExtensions: NSString! ``` | OS X 10.10 |
| To | ``` let DRISORockRidgeExtensions: String ``` | OS X 10.2 |

Modified DRIndexPointsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRIndexPointsKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRIndexPointsKey: String ``` | OS X 10.3 |

Modified DRInvisible

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRInvisible: NSString! ``` | OS X 10.10 |
| To | ``` let DRInvisible: String ``` | OS X 10.2 |

Modified DRJoliet

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRJoliet: NSString! ``` | OS X 10.10 |
| To | ``` let DRJoliet: String ``` | OS X 10.2 |

Modified DRLinkTypeFinderAlias

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRLinkTypeFinderAlias: NSString! ``` | OS X 10.10 |
| To | ``` let DRLinkTypeFinderAlias: String ``` | OS X 10.2 |

Modified DRLinkTypeHardLink

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRLinkTypeHardLink: NSString! ``` | OS X 10.10 |
| To | ``` let DRLinkTypeHardLink: String ``` | OS X 10.2 |

Modified DRLinkTypeSymbolicLink

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRLinkTypeSymbolicLink: NSString! ``` | OS X 10.10 |
| To | ``` let DRLinkTypeSymbolicLink: String ``` | OS X 10.2 |

Modified DRMacExtendedFinderFlags

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRMacExtendedFinderFlags: NSString! ``` | OS X 10.10 |
| To | ``` let DRMacExtendedFinderFlags: String ``` | OS X 10.2 |

Modified DRMacFileCreator

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRMacFileCreator: NSString! ``` | OS X 10.10 |
| To | ``` let DRMacFileCreator: String ``` | OS X 10.2 |

Modified DRMacFileType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRMacFileType: NSString! ``` | OS X 10.10 |
| To | ``` let DRMacFileType: String ``` | OS X 10.2 |

Modified DRMacFinderFlags

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRMacFinderFlags: NSString! ``` | OS X 10.10 |
| To | ``` let DRMacFinderFlags: String ``` | OS X 10.2 |

Modified DRMacFinderHideExtension

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRMacFinderHideExtension: NSString! ``` | OS X 10.10 |
| To | ``` let DRMacFinderHideExtension: String ``` | OS X 10.5 |

Modified DRMacIconLocation

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRMacIconLocation: NSString! ``` | OS X 10.10 |
| To | ``` let DRMacIconLocation: String ``` | OS X 10.2 |

Modified DRMacScrollPosition

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRMacScrollPosition: NSString! ``` | OS X 10.10 |
| To | ``` let DRMacScrollPosition: String ``` | OS X 10.2 |

Modified DRMacWindowBounds

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRMacWindowBounds: NSString! ``` | OS X 10.10 |
| To | ``` let DRMacWindowBounds: String ``` | OS X 10.2 |

Modified DRMacWindowView

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRMacWindowView: NSString! ``` | OS X 10.10 |
| To | ``` let DRMacWindowView: String ``` | OS X 10.2 |

Modified DRMaxBurnSpeedKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRMaxBurnSpeedKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRMaxBurnSpeedKey: String ``` | OS X 10.2 |

Modified DRMediaCatalogNumberKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRMediaCatalogNumberKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRMediaCatalogNumberKey: String ``` | OS X 10.3 |

Modified DRNextWritableAddressKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRNextWritableAddressKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRNextWritableAddressKey: String ``` | OS X 10.3 |

Modified DRNotificationCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DRNotificationCallback = CFunctionPointer<((DRNotificationCenter!, UnsafePointer<()>, CFString!, DRTypeRef!, CFDictionary!) -> Void)> ``` |
| To | ``` typealias DRNotificationCallback = CFunctionPointer<((DRNotificationCenter!, UnsafeMutablePointer<Void>, CFString!, DRType!, CFDictionary!) -> Void)> ``` |

Modified DRNotificationCenterAddObserver(DRNotificationCenter!, UnsafePointer<Void>, DRNotificationCallback, CFString!, DRType!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRNotificationCenterAddObserver(_ center: DRNotificationCenter!, _ observer: ConstUnsafePointer<()>, _ callback: DRNotificationCallback, _ name: CFString!, _ object: DRTypeRef!) ``` | OS X 10.10 |
| To | ``` func DRNotificationCenterAddObserver(_ center: DRNotificationCenter!, _ observer: UnsafePointer<Void>, _ callback: DRNotificationCallback, _ name: CFString!, _ object: DRType!) ``` | OS X 10.2 |

Modified DRNotificationCenterCreate() -> Unmanaged<DRNotificationCenter>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRNotificationCenterCreateRunLoopSource(DRNotificationCenter!) -> Unmanaged<CFRunLoopSource>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRNotificationCenterGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRNotificationCenterRemoveObserver(DRNotificationCenter!, UnsafePointer<Void>, CFString!, DRType!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRNotificationCenterRemoveObserver(_ center: DRNotificationCenter!, _ observer: ConstUnsafePointer<()>, _ name: CFString!, _ object: DRTypeRef!) ``` | OS X 10.10 |
| To | ``` func DRNotificationCenterRemoveObserver(_ center: DRNotificationCenter!, _ observer: UnsafePointer<Void>, _ name: CFString!, _ object: DRType!) ``` | OS X 10.2 |

Modified DRPosixFileMode

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRPosixFileMode: NSString! ``` | OS X 10.10 |
| To | ``` let DRPosixFileMode: String ``` | OS X 10.2 |

Modified DRPosixGID

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRPosixGID: NSString! ``` | OS X 10.10 |
| To | ``` let DRPosixGID: String ``` | OS X 10.2 |

Modified DRPosixUID

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRPosixUID: NSString! ``` | OS X 10.10 |
| To | ``` let DRPosixUID: String ``` | OS X 10.2 |

Modified DRPreGapIsRequiredKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRPreGapIsRequiredKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRPreGapIsRequiredKey: String ``` | OS X 10.5 |

Modified DRPreGapLengthKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRPreGapLengthKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRPreGapLengthKey: String ``` | OS X 10.2 |

Modified DRPublisher

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRPublisher: NSString! ``` | OS X 10.10 |
| To | ``` let DRPublisher: String ``` | OS X 10.2 |

Modified DRRecordingDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRRecordingDate: NSString! ``` | OS X 10.10 |
| To | ``` let DRRecordingDate: String ``` | OS X 10.2 |

Modified DRRefConReleaseCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DRRefConReleaseCallback = CFunctionPointer<((ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias DRRefConReleaseCallback = CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |

Modified DRRefConRetainCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DRRefConRetainCallback = CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` typealias DRRefConRetainCallback = CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified DRSCMSCopyrightFree

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRSCMSCopyrightFree: NSString! ``` | OS X 10.10 |
| To | ``` let DRSCMSCopyrightFree: String ``` | OS X 10.3 |

Modified DRSCMSCopyrightProtectedCopy

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRSCMSCopyrightProtectedCopy: NSString! ``` | OS X 10.10 |
| To | ``` let DRSCMSCopyrightProtectedCopy: String ``` | OS X 10.3 |

Modified DRSCMSCopyrightProtectedOriginal

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRSCMSCopyrightProtectedOriginal: NSString! ``` | OS X 10.10 |
| To | ``` let DRSCMSCopyrightProtectedOriginal: String ``` | OS X 10.3 |

Modified DRSerialCopyManagementStateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRSerialCopyManagementStateKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRSerialCopyManagementStateKey: String ``` | OS X 10.3 |

Modified DRSessionFormatKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRSessionFormatKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRSessionFormatKey: String ``` | OS X 10.2 |

Modified DRSessionNumberKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRSessionNumberKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRSessionNumberKey: String ``` | OS X 10.3 |

Modified DRSetRefCon(DRType!, UnsafeMutablePointer<Void>, UnsafePointer<DRRefConCallbacks>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRSetRefCon(_ ref: DRTypeRef!, _ refCon: UnsafePointer<()>, _ callbacks: ConstUnsafePointer<DRRefConCallbacks>) ``` | OS X 10.10 |
| To | ``` func DRSetRefCon(_ ref: DRType!, _ refCon: UnsafeMutablePointer<Void>, _ callbacks: UnsafePointer<DRRefConCallbacks>) ``` | OS X 10.2 |

Modified DRStatusCurrentSessionKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusCurrentSessionKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusCurrentSessionKey: String ``` | OS X 10.2 |

Modified DRStatusCurrentSpeedKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusCurrentSpeedKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusCurrentSpeedKey: String ``` | OS X 10.2 |

Modified DRStatusCurrentTrackKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusCurrentTrackKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusCurrentTrackKey: String ``` | OS X 10.2 |

Modified DRStatusEraseTypeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusEraseTypeKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusEraseTypeKey: String ``` | OS X 10.2 |

Modified DRStatusPercentCompleteKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusPercentCompleteKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusPercentCompleteKey: String ``` | OS X 10.2 |

Modified DRStatusProgressCurrentKPS

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusProgressCurrentKPS: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusProgressCurrentKPS: String ``` | OS X 10.4 |

Modified DRStatusProgressCurrentXFactor

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusProgressCurrentXFactor: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusProgressCurrentXFactor: String ``` | OS X 10.4 |

Modified DRStatusProgressInfoKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusProgressInfoKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusProgressInfoKey: String ``` | OS X 10.4 |

Modified DRStatusStateDone

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusStateDone: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusStateDone: String ``` | OS X 10.2 |

Modified DRStatusStateErasing

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusStateErasing: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusStateErasing: String ``` | OS X 10.2 |

Modified DRStatusStateFailed

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusStateFailed: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusStateFailed: String ``` | OS X 10.2 |

Modified DRStatusStateFinishing

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusStateFinishing: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusStateFinishing: String ``` | OS X 10.2 |

Modified DRStatusStateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusStateKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusStateKey: String ``` | OS X 10.2 |

Modified DRStatusStateNone

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusStateNone: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusStateNone: String ``` | OS X 10.2 |

Modified DRStatusStatePreparing

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusStatePreparing: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusStatePreparing: String ``` | OS X 10.2 |

Modified DRStatusStateSessionClose

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusStateSessionClose: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusStateSessionClose: String ``` | OS X 10.2 |

Modified DRStatusStateSessionOpen

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusStateSessionOpen: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusStateSessionOpen: String ``` | OS X 10.2 |

Modified DRStatusStateTrackClose

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusStateTrackClose: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusStateTrackClose: String ``` | OS X 10.2 |

Modified DRStatusStateTrackOpen

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusStateTrackOpen: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusStateTrackOpen: String ``` | OS X 10.2 |

Modified DRStatusStateTrackWrite

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusStateTrackWrite: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusStateTrackWrite: String ``` | OS X 10.2 |

Modified DRStatusStateVerifying

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusStateVerifying: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusStateVerifying: String ``` | OS X 10.2 |

Modified DRStatusTotalSessionsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusTotalSessionsKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusTotalSessionsKey: String ``` | OS X 10.2 |

Modified DRStatusTotalTracksKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRStatusTotalTracksKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRStatusTotalTracksKey: String ``` | OS X 10.2 |

Modified DRSubchannelDataFormKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRSubchannelDataFormKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRSubchannelDataFormKey: String ``` | OS X 10.5 |

Modified DRSubchannelDataFormNone

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRSubchannelDataFormNone: NSString! ``` | OS X 10.10 |
| To | ``` let DRSubchannelDataFormNone: String ``` | OS X 10.5 |

Modified DRSubchannelDataFormPack

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRSubchannelDataFormPack: NSString! ``` | OS X 10.10 |
| To | ``` let DRSubchannelDataFormPack: String ``` | OS X 10.5 |

Modified DRSubchannelDataFormRaw

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRSubchannelDataFormRaw: NSString! ``` | OS X 10.10 |
| To | ``` let DRSubchannelDataFormRaw: String ``` | OS X 10.5 |

Modified DRSuppressMacSpecificFiles

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRSuppressMacSpecificFiles: NSString! ``` | OS X 10.10 |
| To | ``` let DRSuppressMacSpecificFiles: String ``` | OS X 10.3 |

Modified DRSynchronousBehaviorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRSynchronousBehaviorKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRSynchronousBehaviorKey: String ``` | OS X 10.2 |

Modified DRSystemIdentifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRSystemIdentifier: NSString! ``` | OS X 10.10 |
| To | ``` let DRSystemIdentifier: String ``` | OS X 10.2 |

Modified DRTrackCallbackProc

|  | Declaration |
| --- | --- |
| From | ``` typealias DRTrackCallbackProc = CFunctionPointer<((DRTrack!, DRTrackMessage, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias DRTrackCallbackProc = CFunctionPointer<((DRTrack!, DRTrackMessage, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified DRTrackCreate(CFDictionary!, DRTrackCallbackProc) -> Unmanaged<DRTrack>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRTrackEstimateLength(DRTrack!) -> UInt64

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DRTrackGetProperties(DRTrack!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRTrackGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRTrackISRCKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRTrackISRCKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRTrackISRCKey: String ``` | OS X 10.3 |

Modified DRTrackIsEmptyKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRTrackIsEmptyKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRTrackIsEmptyKey: String ``` | OS X 10.3 |

Modified DRTrackLengthKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRTrackLengthKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRTrackLengthKey: String ``` | OS X 10.2 |

Modified DRTrackModeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRTrackModeKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRTrackModeKey: String ``` | OS X 10.2 |

Modified DRTrackNumberKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRTrackNumberKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRTrackNumberKey: String ``` | OS X 10.3 |

Modified DRTrackPacketSizeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRTrackPacketSizeKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRTrackPacketSizeKey: String ``` | OS X 10.3 |

Modified DRTrackPacketTypeFixed

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRTrackPacketTypeFixed: NSString! ``` | OS X 10.10 |
| To | ``` let DRTrackPacketTypeFixed: String ``` | OS X 10.3 |

Modified DRTrackPacketTypeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRTrackPacketTypeKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRTrackPacketTypeKey: String ``` | OS X 10.3 |

Modified DRTrackPacketTypeVariable

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRTrackPacketTypeVariable: NSString! ``` | OS X 10.10 |
| To | ``` let DRTrackPacketTypeVariable: String ``` | OS X 10.3 |

Modified DRTrackSetProperties(DRTrack!, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRTrackSpeedTest(DRTrack!, UInt32, UInt32) -> Float

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DRTrackStartAddressKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRTrackStartAddressKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRTrackStartAddressKey: String ``` | OS X 10.3 |

Modified DRTrackTypeClosed

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRTrackTypeClosed: NSString! ``` | OS X 10.10 |
| To | ``` let DRTrackTypeClosed: String ``` | OS X 10.3 |

Modified DRTrackTypeIncomplete

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRTrackTypeIncomplete: NSString! ``` | OS X 10.10 |
| To | ``` let DRTrackTypeIncomplete: String ``` | OS X 10.3 |

Modified DRTrackTypeInvisible

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRTrackTypeInvisible: NSString! ``` | OS X 10.10 |
| To | ``` let DRTrackTypeInvisible: String ``` | OS X 10.3 |

Modified DRTrackTypeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRTrackTypeKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRTrackTypeKey: String ``` | OS X 10.3 |

Modified DRTrackTypeReserved

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRTrackTypeReserved: NSString! ``` | OS X 10.10 |
| To | ``` let DRTrackTypeReserved: String ``` | OS X 10.3 |

Modified DRTypeRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DRTypeRef = AnyObject ``` |
| To | ``` typealias DRTypeRef = DRType ``` |

Modified DRUDF

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRUDF: NSString! ``` | OS X 10.10 |
| To | ``` let DRUDF: String ``` | OS X 10.4 |

Modified DRUDFApplicationIdentifierSuffix

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRUDFApplicationIdentifierSuffix: NSString! ``` | OS X 10.10 |
| To | ``` let DRUDFApplicationIdentifierSuffix: String ``` | OS X 10.4 |

Modified DRUDFExtendedFilePermissions

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRUDFExtendedFilePermissions: NSString! ``` | OS X 10.10 |
| To | ``` let DRUDFExtendedFilePermissions: String ``` | OS X 10.4 |

Modified DRUDFInterchangeLevel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRUDFInterchangeLevel: NSString! ``` | OS X 10.10 |
| To | ``` let DRUDFInterchangeLevel: String ``` | OS X 10.4 |

Modified DRUDFMaxInterchangeLevel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRUDFMaxInterchangeLevel: NSString! ``` | OS X 10.10 |
| To | ``` let DRUDFMaxInterchangeLevel: String ``` | OS X 10.4 |

Modified DRUDFMaxVolumeSequenceNumber

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRUDFMaxVolumeSequenceNumber: NSString! ``` | OS X 10.10 |
| To | ``` let DRUDFMaxVolumeSequenceNumber: String ``` | OS X 10.4 |

Modified DRUDFPrimaryVolumeDescriptorNumber

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRUDFPrimaryVolumeDescriptorNumber: NSString! ``` | OS X 10.10 |
| To | ``` let DRUDFPrimaryVolumeDescriptorNumber: String ``` | OS X 10.4 |

Modified DRUDFRealTimeFile

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRUDFRealTimeFile: NSString! ``` | OS X 10.10 |
| To | ``` let DRUDFRealTimeFile: String ``` | OS X 10.4 |

Modified DRUDFVersion102

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRUDFVersion102: NSString! ``` | OS X 10.10 |
| To | ``` let DRUDFVersion102: String ``` | OS X 10.4 |

Modified DRUDFVersion150

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRUDFVersion150: NSString! ``` | OS X 10.10 |
| To | ``` let DRUDFVersion150: String ``` | OS X 10.4 |

Modified DRUDFVolumeSequenceNumber

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRUDFVolumeSequenceNumber: NSString! ``` | OS X 10.10 |
| To | ``` let DRUDFVolumeSequenceNumber: String ``` | OS X 10.4 |

Modified DRUDFVolumeSetIdentifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRUDFVolumeSetIdentifier: NSString! ``` | OS X 10.10 |
| To | ``` let DRUDFVolumeSetIdentifier: String ``` | OS X 10.4 |

Modified DRUDFVolumeSetImplementationUse

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRUDFVolumeSetImplementationUse: NSString! ``` | OS X 10.10 |
| To | ``` let DRUDFVolumeSetImplementationUse: String ``` | OS X 10.4 |

Modified DRUDFVolumeSetTimestamp

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRUDFVolumeSetTimestamp: NSString! ``` | OS X 10.10 |
| To | ``` let DRUDFVolumeSetTimestamp: String ``` | OS X 10.4 |

Modified DRUDFWriteVersion

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRUDFWriteVersion: NSString! ``` | OS X 10.10 |
| To | ``` let DRUDFWriteVersion: String ``` | OS X 10.4 |

Modified DRVerificationTypeChecksum

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRVerificationTypeChecksum: NSString! ``` | OS X 10.10 |
| To | ``` let DRVerificationTypeChecksum: String ``` | OS X 10.4 |

Modified DRVerificationTypeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRVerificationTypeKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRVerificationTypeKey: String ``` | OS X 10.2 |

Modified DRVerificationTypeNone

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRVerificationTypeNone: NSString! ``` | OS X 10.10 |
| To | ``` let DRVerificationTypeNone: String ``` | OS X 10.2 |

Modified DRVerificationTypeProduceAgain

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRVerificationTypeProduceAgain: NSString! ``` | OS X 10.10 |
| To | ``` let DRVerificationTypeProduceAgain: String ``` | OS X 10.2 |

Modified DRVerificationTypeReceiveData

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRVerificationTypeReceiveData: NSString! ``` | OS X 10.10 |
| To | ``` let DRVerificationTypeReceiveData: String ``` | OS X 10.2 |

Modified DRVolumeCheckedDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRVolumeCheckedDate: NSString! ``` | OS X 10.10 |
| To | ``` let DRVolumeCheckedDate: String ``` | OS X 10.2 |

Modified DRVolumeCreationDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRVolumeCreationDate: NSString! ``` | OS X 10.10 |
| To | ``` let DRVolumeCreationDate: String ``` | OS X 10.2 |

Modified DRVolumeEffectiveDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRVolumeEffectiveDate: NSString! ``` | OS X 10.10 |
| To | ``` let DRVolumeEffectiveDate: String ``` | OS X 10.2 |

Modified DRVolumeExpirationDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRVolumeExpirationDate: NSString! ``` | OS X 10.10 |
| To | ``` let DRVolumeExpirationDate: String ``` | OS X 10.2 |

Modified DRVolumeModificationDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRVolumeModificationDate: NSString! ``` | OS X 10.10 |
| To | ``` let DRVolumeModificationDate: String ``` | OS X 10.2 |

Modified DRVolumeSet

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRVolumeSet: NSString! ``` | OS X 10.10 |
| To | ``` let DRVolumeSet: String ``` | OS X 10.2 |

Modified kDRAbstractFile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRAccessDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRAllFilesystems

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRApplicationIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRAttributeModificationDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRAudioFourChannelKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRAudioPreEmphasisKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRBackupDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRBibliographicFile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRBlockSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRBlockSizeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRBlockTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRBufferZone1DataKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRBurnAppendableKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRBurnCompletionActionEject

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRBurnCompletionActionKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRBurnCompletionActionMount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRBurnDoubleLayerL0DataZoneBlocksKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRBurnFailureActionEject

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRBurnFailureActionKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRBurnFailureActionNone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRBurnKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRBurnOverwriteDiscKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRBurnRequestedSpeedKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRBurnStatusChangedNotification

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRBurnStrategyBDDAO

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRBurnStrategyCDSAO

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRBurnStrategyCDTAO

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRBurnStrategyDVDDAO

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRBurnStrategyIsRequiredKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRBurnStrategyKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRBurnTestingKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRBurnUnderrunProtectionKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRBurnVerifyDiscKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRCDTextArrangerKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextCFStringEncodingKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextCharacterCodeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextClosedKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextComposerKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextCopyrightAssertedForNamesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextCopyrightAssertedForSpecialMessagesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextCopyrightAssertedForTitlesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextDiscIdentKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextGenreCodeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextGenreKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextLanguageKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextMCNISRCKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextPerformerKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextSizeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextSongwriterKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextSpecialMessageKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextTOC2Key

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextTOCKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRCDTextTitleKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRContentModificationDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRCopyrightFile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRCreationDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDVDCopyrightInfoKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDVDTimestampKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDataFormKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDataPreparer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDefaultDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceAppearedNotification

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceBurnSpeedBD1x

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceBurnSpeedCD1x

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceBurnSpeedDVD1x

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceBurnSpeedHDDVD1x

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceBurnSpeedMax

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceBurnSpeedsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceCanTestWriteCDKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceCanTestWriteDVDKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceCanUnderrunProtectCDKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceCanUnderrunProtectDVDKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceCanWriteBDKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceCanWriteBDREKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceCanWriteBDRKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceCanWriteCDKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceCanWriteCDRKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceCanWriteCDRWKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceCanWriteCDRawKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDeviceCanWriteCDSAOKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDeviceCanWriteCDTAOKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDeviceCanWriteCDTextKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceCanWriteDVDDAOKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDeviceCanWriteDVDKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceCanWriteDVDPlusRDoubleLayerKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRDeviceCanWriteDVDPlusRKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDeviceCanWriteDVDPlusRWDoubleLayerKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceCanWriteDVDPlusRWKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDeviceCanWriteDVDRAMKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceCanWriteDVDRDualLayerKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceCanWriteDVDRKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceCanWriteDVDRWDualLayerKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceCanWriteDVDRWKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceCanWriteHDDVDKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceCanWriteHDDVDRAMKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceCanWriteHDDVDRDualLayerKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceCanWriteHDDVDRKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceCanWriteHDDVDRWDualLayerKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceCanWriteHDDVDRWKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceCanWriteISRCKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDeviceCanWriteIndexPointsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDeviceCanWriteKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceCurrentWriteSpeedKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceDisappearedNotification

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceFirmwareRevisionKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceIORegistryEntryPathKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceIsBusyKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceIsTrayOpenKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceLoadingMechanismCanEjectKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDeviceLoadingMechanismCanInjectKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDeviceLoadingMechanismCanOpenKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDeviceMaximumWriteSpeedKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaBSDNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaBlocksFreeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaBlocksOverwritableKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDeviceMediaBlocksUsedKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaClassBD

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceMediaClassCD

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaClassDVD

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaClassHDDVD

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceMediaClassKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaClassUnknown

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaDoubleLayerL0DataZoneBlocksKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRDeviceMediaInfoKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaIsAppendableKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaIsBlankKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaIsErasableKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaIsOverwritableKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDeviceMediaIsReservedKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaSessionCountKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaStateInTransition

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaStateKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaStateMediaPresent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaStateNone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaTrackCountKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaTypeBDR

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceMediaTypeBDRE

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceMediaTypeBDROM

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceMediaTypeCDR

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaTypeCDROM

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaTypeCDRW

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaTypeDVDPlusR

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDeviceMediaTypeDVDPlusRDoubleLayer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRDeviceMediaTypeDVDPlusRW

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaTypeDVDPlusRWDoubleLayer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceMediaTypeDVDR

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaTypeDVDRAM

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaTypeDVDRDualLayer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceMediaTypeDVDROM

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaTypeDVDRW

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaTypeDVDRWDualLayer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceMediaTypeHDDVDR

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceMediaTypeHDDVDRAM

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceMediaTypeHDDVDRDualLayer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceMediaTypeHDDVDROM

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceMediaTypeHDDVDRW

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceMediaTypeHDDVDRWDualLayer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRDeviceMediaTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceMediaTypeUnknown

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDevicePhysicalInterconnectATAPI

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDevicePhysicalInterconnectFibreChannel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDevicePhysicalInterconnectFireWire

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDevicePhysicalInterconnectKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDevicePhysicalInterconnectLocationExternal

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDevicePhysicalInterconnectLocationInternal

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDevicePhysicalInterconnectLocationKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDevicePhysicalInterconnectLocationUnknown

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDevicePhysicalInterconnectSCSI

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDevicePhysicalInterconnectUSB

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceProductNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceStatusChangedNotification

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceSupportLevelAppleShipping

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceSupportLevelAppleSupported

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceSupportLevelKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceSupportLevelNone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceSupportLevelUnsupported

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDeviceSupportLevelVendorSupported

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceTrackInfoKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDeviceTrackRefsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDeviceVendorNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRDeviceWriteBufferSizeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRDeviceWriteCapabilitiesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDREffectiveDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDREraseStatusChangedNotification

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDREraseTypeComplete

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDREraseTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDREraseTypeQuick

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRErrorStatusAdditionalSenseStringKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRErrorStatusErrorInfoStringKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRErrorStatusErrorKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRErrorStatusErrorStringKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRErrorStatusKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRErrorStatusSenseCodeStringKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRErrorStatusSenseKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRExpirationDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRFreeBlocksKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRHFSPlus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRHFSPlusCatalogNodeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRHFSPlusTextEncodingHint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRISO9660

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRISO9660LevelOne

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRISO9660LevelTwo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRISO9660VersionNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRISOLevel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRISOMacExtensions

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRISORockRidgeExtensions

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRIndexPointsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRInvisible

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRJoliet

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRMacExtendedFinderFlags

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRMacFileCreator

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRMacFileType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRMacFinderFlags

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRMacFinderHideExtension

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRMacIconLocation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRMacScrollPosition

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRMacWindowBounds

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRMacWindowView

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRMaxBurnSpeedKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRMediaCatalogNumberKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRNextWritableAddressKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRPosixFileMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRPosixGID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRPosixUID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRPreGapIsRequiredKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRPreGapLengthKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRPublisher

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRRecordingDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRSCMSCopyrightFree

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRSCMSCopyrightProtectedCopy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRSCMSCopyrightProtectedOriginal

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRSerialCopyManagementStateKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRSessionFormatKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRSessionNumberKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRStatusCurrentSessionKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusCurrentSpeedKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusCurrentTrackKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusEraseTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusPercentCompleteKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusProgressCurrentKPS

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRStatusProgressCurrentXFactor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRStatusProgressInfoKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRStatusStateDone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusStateErasing

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusStateFailed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusStateFinishing

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusStateKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusStateNone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusStatePreparing

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusStateSessionClose

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusStateSessionOpen

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusStateTrackClose

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusStateTrackOpen

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusStateTrackWrite

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusStateVerifying

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusTotalSessionsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRStatusTotalTracksKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRSubchannelDataFormKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRSubchannelDataFormNone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRSubchannelDataFormPack

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRSubchannelDataFormRaw

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kDRSuppressMacSpecificFiles

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRSynchronousBehaviorKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRSystemIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRTrackISRCKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRTrackIsEmptyKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRTrackLengthKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRTrackModeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRTrackNumberKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRTrackPacketSizeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRTrackPacketTypeFixed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRTrackPacketTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRTrackPacketTypeVariable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRTrackStartAddressKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRTrackTypeClosed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRTrackTypeIncomplete

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRTrackTypeInvisible

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRTrackTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRTrackTypeReserved

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kDRUDF

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRUDFApplicationIdentifierSuffix

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRUDFExtendedFilePermissions

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRUDFInterchangeLevel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRUDFMaxInterchangeLevel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRUDFMaxVolumeSequenceNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRUDFPrimaryVolumeDescriptorNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRUDFRealTimeFile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRUDFVersion102

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRUDFVersion150

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRUDFVolumeSequenceNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRUDFVolumeSetIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRUDFVolumeSetImplementationUse

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRUDFVolumeSetTimestamp

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRUDFWriteVersion

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRVerificationTypeChecksum

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kDRVerificationTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRVerificationTypeNone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRVerificationTypeProduceAgain

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRVerificationTypeReceiveData

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRVolumeCheckedDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRVolumeCreationDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRVolumeEffectiveDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRVolumeExpirationDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRVolumeModificationDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kDRVolumeSet

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

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
