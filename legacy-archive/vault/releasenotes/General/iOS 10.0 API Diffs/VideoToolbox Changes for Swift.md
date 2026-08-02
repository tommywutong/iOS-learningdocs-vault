---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/VideoToolbox.html
archived_at: '2026-07-18T02:55:45.744714Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# VideoToolbox Changes for Swift

### VideoToolbox

Removed [VTDecompressionOutputCallbackRecord.init(decompressionOutputCallback: VTDecompressionOutputCallback?, decompressionOutputRefCon: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/videotoolbox/vtdecompressionoutputcallbackrecord/1536069-init)Added [VTDecompressionOutputCallbackRecord.init(decompressionOutputCallback: VideoToolbox.VTDecompressionOutputCallback?, decompressionOutputRefCon: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/videotoolbox/vtdecompressionoutputcallbackrecord/1536069-init)Added [kVTColorCorrectionImageRotationFailedErr](https://developer.apple.com/documentation/videotoolbox/1490398-error_code_constants/kvtcolorcorrectionimagerotationfailederr)Added [kVTDownsamplingMode_Average](https://developer.apple.com/documentation/videotoolbox/kvtdownsamplingmode_average)Added [kVTDownsamplingMode_Decimate](https://developer.apple.com/documentation/videotoolbox/kvtdownsamplingmode_decimate)Added [kVTPixelTransferPropertyKey_DestinationCleanAperture](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_destinationcleanaperture)Added [kVTPixelTransferPropertyKey_DestinationColorPrimaries](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_destinationcolorprimaries)Added [kVTPixelTransferPropertyKey_DestinationICCProfile](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_destinationiccprofile)Added [kVTPixelTransferPropertyKey_DestinationPixelAspectRatio](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_destinationpixelaspectratio)Added [kVTPixelTransferPropertyKey_DestinationTransferFunction](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_destinationtransferfunction)Added [kVTPixelTransferPropertyKey_DestinationYCbCrMatrix](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_destinationycbcrmatrix)Added [kVTPixelTransferPropertyKey_DownsamplingMode](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_downsamplingmode)Added [kVTPixelTransferPropertyKey_ScalingMode](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_scalingmode)Added [kVTScalingMode_CropSourceToCleanAperture](https://developer.apple.com/documentation/videotoolbox/kvtscalingmode_cropsourcetocleanaperture)Added [kVTScalingMode_Letterbox](https://developer.apple.com/documentation/videotoolbox/kvtscalingmode_letterbox)Added [kVTScalingMode_Normal](https://developer.apple.com/documentation/videotoolbox/kvtscalingmode_normal)Added [kVTScalingMode_Trim](https://developer.apple.com/documentation/videotoolbox/kvtscalingmode_trim)Modified [VTCompressionSessionOptionFlags [struct]](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessionoptionflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct VTCompressionSessionOptionFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var BeginFinalPass: VTCompressionSessionOptionFlags { get } } ``` | OptionSetType |
| To | ``` struct VTCompressionSessionOptionFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var beginFinalPass: VTCompressionSessionOptionFlags { get }     func intersect(_ other: VTCompressionSessionOptionFlags) -> VTCompressionSessionOptionFlags     func exclusiveOr(_ other: VTCompressionSessionOptionFlags) -> VTCompressionSessionOptionFlags     mutating func unionInPlace(_ other: VTCompressionSessionOptionFlags)     mutating func intersectInPlace(_ other: VTCompressionSessionOptionFlags)     mutating func exclusiveOrInPlace(_ other: VTCompressionSessionOptionFlags)     func isSubsetOf(_ other: VTCompressionSessionOptionFlags) -> Bool     func isDisjointWith(_ other: VTCompressionSessionOptionFlags) -> Bool     func isSupersetOf(_ other: VTCompressionSessionOptionFlags) -> Bool     mutating func subtractInPlace(_ other: VTCompressionSessionOptionFlags)     func isStrictSupersetOf(_ other: VTCompressionSessionOptionFlags) -> Bool     func isStrictSubsetOf(_ other: VTCompressionSessionOptionFlags) -> Bool } extension VTCompressionSessionOptionFlags {     func union(_ other: VTCompressionSessionOptionFlags) -> VTCompressionSessionOptionFlags     func intersection(_ other: VTCompressionSessionOptionFlags) -> VTCompressionSessionOptionFlags     func symmetricDifference(_ other: VTCompressionSessionOptionFlags) -> VTCompressionSessionOptionFlags } extension VTCompressionSessionOptionFlags {     func contains(_ member: VTCompressionSessionOptionFlags) -> Bool     mutating func insert(_ newMember: VTCompressionSessionOptionFlags) -> (inserted: Bool, memberAfterInsert: VTCompressionSessionOptionFlags)     mutating func remove(_ member: VTCompressionSessionOptionFlags) -> VTCompressionSessionOptionFlags?     mutating func update(with newMember: VTCompressionSessionOptionFlags) -> VTCompressionSessionOptionFlags? } extension VTCompressionSessionOptionFlags {     convenience init()     mutating func formUnion(_ other: VTCompressionSessionOptionFlags)     mutating func formIntersection(_ other: VTCompressionSessionOptionFlags)     mutating func formSymmetricDifference(_ other: VTCompressionSessionOptionFlags) } extension VTCompressionSessionOptionFlags {     convenience init<S : Sequence where S.Iterator.Element == VTCompressionSessionOptionFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: VTCompressionSessionOptionFlags...)     mutating func subtract(_ other: VTCompressionSessionOptionFlags)     func isSubset(of other: VTCompressionSessionOptionFlags) -> Bool     func isSuperset(of other: VTCompressionSessionOptionFlags) -> Bool     func isDisjoint(with other: VTCompressionSessionOptionFlags) -> Bool     func subtracting(_ other: VTCompressionSessionOptionFlags) -> VTCompressionSessionOptionFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: VTCompressionSessionOptionFlags) -> Bool     func isStrictSubset(of other: VTCompressionSessionOptionFlags) -> Bool } ``` | OptionSet |

Modified [VTCompressionSessionOptionFlags.beginFinalPass](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessionoptionflags/1428299-beginfinalpass)

|  | Declaration |
| --- | --- |
| From | ``` static var BeginFinalPass: VTCompressionSessionOptionFlags { get } ``` |
| To | ``` static var beginFinalPass: VTCompressionSessionOptionFlags { get } ``` |

Modified [VTDecodeFrameFlags [struct]](https://developer.apple.com/documentation/videotoolbox/vtdecodeframeflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct VTDecodeFrameFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var _EnableAsynchronousDecompression: VTDecodeFrameFlags { get }     static var _DoNotOutputFrame: VTDecodeFrameFlags { get }     static var _1xRealTimePlayback: VTDecodeFrameFlags { get }     static var _EnableTemporalProcessing: VTDecodeFrameFlags { get } } ``` | OptionSetType |
| To | ``` struct VTDecodeFrameFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var _EnableAsynchronousDecompression: VTDecodeFrameFlags { get }     static var _DoNotOutputFrame: VTDecodeFrameFlags { get }     static var _1xRealTimePlayback: VTDecodeFrameFlags { get }     static var _EnableTemporalProcessing: VTDecodeFrameFlags { get }     func intersect(_ other: VTDecodeFrameFlags) -> VTDecodeFrameFlags     func exclusiveOr(_ other: VTDecodeFrameFlags) -> VTDecodeFrameFlags     mutating func unionInPlace(_ other: VTDecodeFrameFlags)     mutating func intersectInPlace(_ other: VTDecodeFrameFlags)     mutating func exclusiveOrInPlace(_ other: VTDecodeFrameFlags)     func isSubsetOf(_ other: VTDecodeFrameFlags) -> Bool     func isDisjointWith(_ other: VTDecodeFrameFlags) -> Bool     func isSupersetOf(_ other: VTDecodeFrameFlags) -> Bool     mutating func subtractInPlace(_ other: VTDecodeFrameFlags)     func isStrictSupersetOf(_ other: VTDecodeFrameFlags) -> Bool     func isStrictSubsetOf(_ other: VTDecodeFrameFlags) -> Bool } extension VTDecodeFrameFlags {     func union(_ other: VTDecodeFrameFlags) -> VTDecodeFrameFlags     func intersection(_ other: VTDecodeFrameFlags) -> VTDecodeFrameFlags     func symmetricDifference(_ other: VTDecodeFrameFlags) -> VTDecodeFrameFlags } extension VTDecodeFrameFlags {     func contains(_ member: VTDecodeFrameFlags) -> Bool     mutating func insert(_ newMember: VTDecodeFrameFlags) -> (inserted: Bool, memberAfterInsert: VTDecodeFrameFlags)     mutating func remove(_ member: VTDecodeFrameFlags) -> VTDecodeFrameFlags?     mutating func update(with newMember: VTDecodeFrameFlags) -> VTDecodeFrameFlags? } extension VTDecodeFrameFlags {     convenience init()     mutating func formUnion(_ other: VTDecodeFrameFlags)     mutating func formIntersection(_ other: VTDecodeFrameFlags)     mutating func formSymmetricDifference(_ other: VTDecodeFrameFlags) } extension VTDecodeFrameFlags {     convenience init<S : Sequence where S.Iterator.Element == VTDecodeFrameFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: VTDecodeFrameFlags...)     mutating func subtract(_ other: VTDecodeFrameFlags)     func isSubset(of other: VTDecodeFrameFlags) -> Bool     func isSuperset(of other: VTDecodeFrameFlags) -> Bool     func isDisjoint(with other: VTDecodeFrameFlags) -> Bool     func subtracting(_ other: VTDecodeFrameFlags) -> VTDecodeFrameFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: VTDecodeFrameFlags) -> Bool     func isStrictSubset(of other: VTDecodeFrameFlags) -> Bool } ``` | OptionSet |

Modified [VTDecodeInfoFlags [struct]](https://developer.apple.com/documentation/videotoolbox/vtdecodeinfoflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct VTDecodeInfoFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var Asynchronous: VTDecodeInfoFlags { get }     static var FrameDropped: VTDecodeInfoFlags { get }     static var ImageBufferModifiable: VTDecodeInfoFlags { get } } ``` | OptionSetType |
| To | ``` struct VTDecodeInfoFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var asynchronous: VTDecodeInfoFlags { get }     static var frameDropped: VTDecodeInfoFlags { get }     static var imageBufferModifiable: VTDecodeInfoFlags { get }     func intersect(_ other: VTDecodeInfoFlags) -> VTDecodeInfoFlags     func exclusiveOr(_ other: VTDecodeInfoFlags) -> VTDecodeInfoFlags     mutating func unionInPlace(_ other: VTDecodeInfoFlags)     mutating func intersectInPlace(_ other: VTDecodeInfoFlags)     mutating func exclusiveOrInPlace(_ other: VTDecodeInfoFlags)     func isSubsetOf(_ other: VTDecodeInfoFlags) -> Bool     func isDisjointWith(_ other: VTDecodeInfoFlags) -> Bool     func isSupersetOf(_ other: VTDecodeInfoFlags) -> Bool     mutating func subtractInPlace(_ other: VTDecodeInfoFlags)     func isStrictSupersetOf(_ other: VTDecodeInfoFlags) -> Bool     func isStrictSubsetOf(_ other: VTDecodeInfoFlags) -> Bool } extension VTDecodeInfoFlags {     func union(_ other: VTDecodeInfoFlags) -> VTDecodeInfoFlags     func intersection(_ other: VTDecodeInfoFlags) -> VTDecodeInfoFlags     func symmetricDifference(_ other: VTDecodeInfoFlags) -> VTDecodeInfoFlags } extension VTDecodeInfoFlags {     func contains(_ member: VTDecodeInfoFlags) -> Bool     mutating func insert(_ newMember: VTDecodeInfoFlags) -> (inserted: Bool, memberAfterInsert: VTDecodeInfoFlags)     mutating func remove(_ member: VTDecodeInfoFlags) -> VTDecodeInfoFlags?     mutating func update(with newMember: VTDecodeInfoFlags) -> VTDecodeInfoFlags? } extension VTDecodeInfoFlags {     convenience init()     mutating func formUnion(_ other: VTDecodeInfoFlags)     mutating func formIntersection(_ other: VTDecodeInfoFlags)     mutating func formSymmetricDifference(_ other: VTDecodeInfoFlags) } extension VTDecodeInfoFlags {     convenience init<S : Sequence where S.Iterator.Element == VTDecodeInfoFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: VTDecodeInfoFlags...)     mutating func subtract(_ other: VTDecodeInfoFlags)     func isSubset(of other: VTDecodeInfoFlags) -> Bool     func isSuperset(of other: VTDecodeInfoFlags) -> Bool     func isDisjoint(with other: VTDecodeInfoFlags) -> Bool     func subtracting(_ other: VTDecodeInfoFlags) -> VTDecodeInfoFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: VTDecodeInfoFlags) -> Bool     func isStrictSubset(of other: VTDecodeInfoFlags) -> Bool } ``` | OptionSet |

Modified [VTDecodeInfoFlags.asynchronous](https://developer.apple.com/documentation/videotoolbox/vtdecodeinfoflags/kvtdecodeinfo_asynchronous)

|  | Declaration |
| --- | --- |
| From | ``` static var Asynchronous: VTDecodeInfoFlags { get } ``` |
| To | ``` static var asynchronous: VTDecodeInfoFlags { get } ``` |

Modified [VTDecodeInfoFlags.frameDropped](https://developer.apple.com/documentation/videotoolbox/vtdecodeinfoflags/1490385-framedropped)

|  | Declaration |
| --- | --- |
| From | ``` static var FrameDropped: VTDecodeInfoFlags { get } ``` |
| To | ``` static var frameDropped: VTDecodeInfoFlags { get } ``` |

Modified [VTDecodeInfoFlags.imageBufferModifiable](https://developer.apple.com/documentation/videotoolbox/vtdecodeinfoflags/1490384-imagebuffermodifiable)

|  | Declaration |
| --- | --- |
| From | ``` static var ImageBufferModifiable: VTDecodeInfoFlags { get } ``` |
| To | ``` static var imageBufferModifiable: VTDecodeInfoFlags { get } ``` |

Modified [VTDecompressionOutputCallbackRecord [struct]](https://developer.apple.com/documentation/videotoolbox/vtdecompressionoutputcallbackrecord)

|  | Declaration |
| --- | --- |
| From | ``` struct VTDecompressionOutputCallbackRecord {     var decompressionOutputCallback: VTDecompressionOutputCallback?     var decompressionOutputRefCon: UnsafeMutablePointer<Void>     init()     init(decompressionOutputCallback decompressionOutputCallback: VTDecompressionOutputCallback?, decompressionOutputRefCon decompressionOutputRefCon: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct VTDecompressionOutputCallbackRecord {     var decompressionOutputCallback: VideoToolbox.VTDecompressionOutputCallback?     var decompressionOutputRefCon: UnsafeMutableRawPointer?     init()     init(decompressionOutputCallback decompressionOutputCallback: VideoToolbox.VTDecompressionOutputCallback?, decompressionOutputRefCon decompressionOutputRefCon: UnsafeMutableRawPointer?) } ``` |

Modified [VTDecompressionOutputCallbackRecord.decompressionOutputCallback](https://developer.apple.com/documentation/videotoolbox/vtdecompressionoutputcallbackrecord/1536141-decompressionoutputcallback)

|  | Declaration |
| --- | --- |
| From | ``` var decompressionOutputCallback: VTDecompressionOutputCallback? ``` |
| To | ``` var decompressionOutputCallback: VideoToolbox.VTDecompressionOutputCallback? ``` |

Modified [VTDecompressionOutputCallbackRecord.decompressionOutputRefCon](https://developer.apple.com/documentation/videotoolbox/vtdecompressionoutputcallbackrecord/1536087-decompressionoutputrefcon)

|  | Declaration |
| --- | --- |
| From | ``` var decompressionOutputRefCon: UnsafeMutablePointer<Void> ``` |
| To | ``` var decompressionOutputRefCon: UnsafeMutableRawPointer? ``` |

Modified [VTEncodeInfoFlags [struct]](https://developer.apple.com/documentation/videotoolbox/vtencodeinfoflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct VTEncodeInfoFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var Asynchronous: VTEncodeInfoFlags { get }     static var FrameDropped: VTEncodeInfoFlags { get } } ``` | OptionSetType |
| To | ``` struct VTEncodeInfoFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var asynchronous: VTEncodeInfoFlags { get }     static var frameDropped: VTEncodeInfoFlags { get }     func intersect(_ other: VTEncodeInfoFlags) -> VTEncodeInfoFlags     func exclusiveOr(_ other: VTEncodeInfoFlags) -> VTEncodeInfoFlags     mutating func unionInPlace(_ other: VTEncodeInfoFlags)     mutating func intersectInPlace(_ other: VTEncodeInfoFlags)     mutating func exclusiveOrInPlace(_ other: VTEncodeInfoFlags)     func isSubsetOf(_ other: VTEncodeInfoFlags) -> Bool     func isDisjointWith(_ other: VTEncodeInfoFlags) -> Bool     func isSupersetOf(_ other: VTEncodeInfoFlags) -> Bool     mutating func subtractInPlace(_ other: VTEncodeInfoFlags)     func isStrictSupersetOf(_ other: VTEncodeInfoFlags) -> Bool     func isStrictSubsetOf(_ other: VTEncodeInfoFlags) -> Bool } extension VTEncodeInfoFlags {     func union(_ other: VTEncodeInfoFlags) -> VTEncodeInfoFlags     func intersection(_ other: VTEncodeInfoFlags) -> VTEncodeInfoFlags     func symmetricDifference(_ other: VTEncodeInfoFlags) -> VTEncodeInfoFlags } extension VTEncodeInfoFlags {     func contains(_ member: VTEncodeInfoFlags) -> Bool     mutating func insert(_ newMember: VTEncodeInfoFlags) -> (inserted: Bool, memberAfterInsert: VTEncodeInfoFlags)     mutating func remove(_ member: VTEncodeInfoFlags) -> VTEncodeInfoFlags?     mutating func update(with newMember: VTEncodeInfoFlags) -> VTEncodeInfoFlags? } extension VTEncodeInfoFlags {     convenience init()     mutating func formUnion(_ other: VTEncodeInfoFlags)     mutating func formIntersection(_ other: VTEncodeInfoFlags)     mutating func formSymmetricDifference(_ other: VTEncodeInfoFlags) } extension VTEncodeInfoFlags {     convenience init<S : Sequence where S.Iterator.Element == VTEncodeInfoFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: VTEncodeInfoFlags...)     mutating func subtract(_ other: VTEncodeInfoFlags)     func isSubset(of other: VTEncodeInfoFlags) -> Bool     func isSuperset(of other: VTEncodeInfoFlags) -> Bool     func isDisjoint(with other: VTEncodeInfoFlags) -> Bool     func subtracting(_ other: VTEncodeInfoFlags) -> VTEncodeInfoFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: VTEncodeInfoFlags) -> Bool     func isStrictSubset(of other: VTEncodeInfoFlags) -> Bool } ``` | OptionSet |

Modified [VTEncodeInfoFlags.asynchronous](https://developer.apple.com/documentation/videotoolbox/vtencodeinfoflags/1490349-asynchronous)

|  | Declaration |
| --- | --- |
| From | ``` static var Asynchronous: VTEncodeInfoFlags { get } ``` |
| To | ``` static var asynchronous: VTEncodeInfoFlags { get } ``` |

Modified [VTEncodeInfoFlags.frameDropped](https://developer.apple.com/documentation/videotoolbox/vtencodeinfoflags/1490388-framedropped)

|  | Declaration |
| --- | --- |
| From | ``` static var FrameDropped: VTEncodeInfoFlags { get } ``` |
| To | ``` static var frameDropped: VTEncodeInfoFlags { get } ``` |

Modified [VTCompressionOutputCallback](https://developer.apple.com/documentation/videotoolbox/vtcompressionoutputcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias VTCompressionOutputCallback = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, OSStatus, VTEncodeInfoFlags, CMSampleBuffer?) -> Void ``` |
| To | ``` typealias VTCompressionOutputCallback = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, OSStatus, VTEncodeInfoFlags, CMSampleBuffer?) -> Swift.Void ``` |

Modified [VTCompressionOutputHandler](https://developer.apple.com/documentation/videotoolbox/vtcompressionoutputhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias VTCompressionOutputHandler = (OSStatus, VTEncodeInfoFlags, CMSampleBuffer?) -> Void ``` |
| To | ``` typealias VTCompressionOutputHandler = (OSStatus, VTEncodeInfoFlags, CMSampleBuffer?) -> Swift.Void ``` |

Modified [VTCompressionSessionBeginPass(_: VTCompressionSession, _: VTCompressionSessionOptionFlags, _: UnsafeMutablePointer<UInt32>?) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1428289-vtcompressionsessionbeginpass)

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionBeginPass(_ session: VTCompressionSession, _ beginPassFlags: VTCompressionSessionOptionFlags, _ reserved: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func VTCompressionSessionBeginPass(_ session: VTCompressionSession, _ beginPassFlags: VTCompressionSessionOptionFlags, _ reserved: UnsafeMutablePointer<UInt32>?) -> OSStatus ``` |

Modified [VTCompressionSessionCreate(_: CFAllocator?, _: Int32, _: Int32, _: CMVideoCodecType, _: CFDictionary?, _: CFDictionary?, _: CFAllocator?, _: VideoToolbox.VTCompressionOutputCallback?, _: UnsafeMutableRawPointer?, _: UnsafeMutablePointer<VTCompressionSession?>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1428285-vtcompressionsessioncreate)

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionCreate(_ allocator: CFAllocator?, _ width: Int32, _ height: Int32, _ codecType: CMVideoCodecType, _ encoderSpecification: CFDictionary?, _ sourceImageBufferAttributes: CFDictionary?, _ compressedDataAllocator: CFAllocator?, _ outputCallback: VTCompressionOutputCallback?, _ outputCallbackRefCon: UnsafeMutablePointer<Void>, _ compressionSessionOut: UnsafeMutablePointer<VTCompressionSession?>) -> OSStatus ``` |
| To | ``` func VTCompressionSessionCreate(_ allocator: CFAllocator?, _ width: Int32, _ height: Int32, _ codecType: CMVideoCodecType, _ encoderSpecification: CFDictionary?, _ sourceImageBufferAttributes: CFDictionary?, _ compressedDataAllocator: CFAllocator?, _ outputCallback: VideoToolbox.VTCompressionOutputCallback?, _ outputCallbackRefCon: UnsafeMutableRawPointer?, _ compressionSessionOut: UnsafeMutablePointer<VTCompressionSession?>) -> OSStatus ``` |

Modified [VTCompressionSessionEncodeFrame(_: VTCompressionSession, _: CVImageBuffer, _: CMTime, _: CMTime, _: CFDictionary?, _: UnsafeMutableRawPointer?, _: UnsafeMutablePointer<VTEncodeInfoFlags>?) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1428287-vtcompressionsessionencodeframe)

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionEncodeFrame(_ session: VTCompressionSession, _ imageBuffer: CVImageBuffer, _ presentationTimeStamp: CMTime, _ duration: CMTime, _ frameProperties: CFDictionary?, _ sourceFrameRefCon: UnsafeMutablePointer<Void>, _ infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>) -> OSStatus ``` |
| To | ``` func VTCompressionSessionEncodeFrame(_ session: VTCompressionSession, _ imageBuffer: CVImageBuffer, _ presentationTimeStamp: CMTime, _ duration: CMTime, _ frameProperties: CFDictionary?, _ sourceFrameRefCon: UnsafeMutableRawPointer?, _ infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?) -> OSStatus ``` |

Modified [VTCompressionSessionEncodeFrameWithOutputHandler(_: VTCompressionSession, _: CVImageBuffer, _: CMTime, _: CMTime, _: CFDictionary?, _: UnsafeMutablePointer<VTEncodeInfoFlags>?, _: VideoToolbox.VTCompressionOutputHandler) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1428281-vtcompressionsessionencodeframew)

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionEncodeFrameWithOutputHandler(_ session: VTCompressionSession, _ imageBuffer: CVImageBuffer, _ presentationTimeStamp: CMTime, _ duration: CMTime, _ frameProperties: CFDictionary?, _ infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>, _ outputHandler: VTCompressionOutputHandler) -> OSStatus ``` |
| To | ``` func VTCompressionSessionEncodeFrameWithOutputHandler(_ session: VTCompressionSession, _ imageBuffer: CVImageBuffer, _ presentationTimeStamp: CMTime, _ duration: CMTime, _ frameProperties: CFDictionary?, _ infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?, _ outputHandler: VideoToolbox.VTCompressionOutputHandler) -> OSStatus ``` |

Modified [VTCompressionSessionEndPass(_: VTCompressionSession, _: UnsafeMutablePointer<DarwinBoolean>?, _: UnsafeMutablePointer<UInt32>?) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1428313-vtcompressionsessionendpass)

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionEndPass(_ session: VTCompressionSession, _ furtherPassesRequestedOut: UnsafeMutablePointer<DarwinBoolean>, _ reserved: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func VTCompressionSessionEndPass(_ session: VTCompressionSession, _ furtherPassesRequestedOut: UnsafeMutablePointer<DarwinBoolean>?, _ reserved: UnsafeMutablePointer<UInt32>?) -> OSStatus ``` |

Modified [VTCompressionSessionGetTimeRangesForNextPass(_: VTCompressionSession, _: UnsafeMutablePointer<CMItemCount>, _: UnsafeMutablePointer<UnsafePointer<CMTimeRange>?>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1428311-vtcompressionsessiongettimerange)

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionGetTimeRangesForNextPass(_ session: VTCompressionSession, _ timeRangeCountOut: UnsafeMutablePointer<CMItemCount>, _ timeRangeArrayOut: UnsafeMutablePointer<UnsafePointer<CMTimeRange>>) -> OSStatus ``` |
| To | ``` func VTCompressionSessionGetTimeRangesForNextPass(_ session: VTCompressionSession, _ timeRangeCountOut: UnsafeMutablePointer<CMItemCount>, _ timeRangeArrayOut: UnsafeMutablePointer<UnsafePointer<CMTimeRange>?>) -> OSStatus ``` |

Modified [VTDecompressionOutputCallback](https://developer.apple.com/documentation/videotoolbox/vtdecompressionoutputcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias VTDecompressionOutputCallback = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, OSStatus, VTDecodeInfoFlags, CVImageBuffer?, CMTime, CMTime) -> Void ``` |
| To | ``` typealias VTDecompressionOutputCallback = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, OSStatus, VTDecodeInfoFlags, CVImageBuffer?, CMTime, CMTime) -> Swift.Void ``` |

Modified [VTDecompressionOutputHandler](https://developer.apple.com/documentation/videotoolbox/vtdecompressionoutputhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias VTDecompressionOutputHandler = (OSStatus, VTDecodeInfoFlags, CVImageBuffer?, CMTime, CMTime) -> Void ``` |
| To | ``` typealias VTDecompressionOutputHandler = (OSStatus, VTDecodeInfoFlags, CVImageBuffer?, CMTime, CMTime) -> Swift.Void ``` |

Modified [VTDecompressionSessionCreate(_: CFAllocator?, _: CMVideoFormatDescription, _: CFDictionary?, _: CFDictionary?, _: UnsafePointer<VTDecompressionOutputCallbackRecord>?, _: UnsafeMutablePointer<VTDecompressionSession?>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536134-vtdecompressionsessioncreate)

|  | Declaration |
| --- | --- |
| From | ``` func VTDecompressionSessionCreate(_ allocator: CFAllocator?, _ videoFormatDescription: CMVideoFormatDescription, _ videoDecoderSpecification: CFDictionary?, _ destinationImageBufferAttributes: CFDictionary?, _ outputCallback: UnsafePointer<VTDecompressionOutputCallbackRecord>, _ decompressionSessionOut: UnsafeMutablePointer<VTDecompressionSession?>) -> OSStatus ``` |
| To | ``` func VTDecompressionSessionCreate(_ allocator: CFAllocator?, _ videoFormatDescription: CMVideoFormatDescription, _ videoDecoderSpecification: CFDictionary?, _ destinationImageBufferAttributes: CFDictionary?, _ outputCallback: UnsafePointer<VTDecompressionOutputCallbackRecord>?, _ decompressionSessionOut: UnsafeMutablePointer<VTDecompressionSession?>) -> OSStatus ``` |

Modified [VTDecompressionSessionDecodeFrame(_: VTDecompressionSession, _: CMSampleBuffer, _: VTDecodeFrameFlags, _: UnsafeMutableRawPointer?, _: UnsafeMutablePointer<VTDecodeInfoFlags>?) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536071-vtdecompressionsessiondecodefram)

|  | Declaration |
| --- | --- |
| From | ``` func VTDecompressionSessionDecodeFrame(_ session: VTDecompressionSession, _ sampleBuffer: CMSampleBuffer, _ decodeFlags: VTDecodeFrameFlags, _ sourceFrameRefCon: UnsafeMutablePointer<Void>, _ infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>) -> OSStatus ``` |
| To | ``` func VTDecompressionSessionDecodeFrame(_ session: VTDecompressionSession, _ sampleBuffer: CMSampleBuffer, _ decodeFlags: VTDecodeFrameFlags, _ sourceFrameRefCon: UnsafeMutableRawPointer?, _ infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?) -> OSStatus ``` |

Modified [VTDecompressionSessionDecodeFrameWithOutputHandler(_: VTDecompressionSession, _: CMSampleBuffer, _: VTDecodeFrameFlags, _: UnsafeMutablePointer<VTDecodeInfoFlags>?, _: VideoToolbox.VTDecompressionOutputHandler) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536067-vtdecompressionsessiondecodefram)

|  | Declaration |
| --- | --- |
| From | ``` func VTDecompressionSessionDecodeFrameWithOutputHandler(_ session: VTDecompressionSession, _ sampleBuffer: CMSampleBuffer, _ decodeFlags: VTDecodeFrameFlags, _ infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>, _ outputHandler: VTDecompressionOutputHandler) -> OSStatus ``` |
| To | ``` func VTDecompressionSessionDecodeFrameWithOutputHandler(_ session: VTDecompressionSession, _ sampleBuffer: CMSampleBuffer, _ decodeFlags: VTDecodeFrameFlags, _ infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, _ outputHandler: VideoToolbox.VTDecompressionOutputHandler) -> OSStatus ``` |

Modified [VTFrameSiloCallBlockForEachSampleBuffer(_: VTFrameSilo, _: CMTimeRange, _: (CMSampleBuffer) -> OSStatus) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1474252-vtframesilocallblockforeachsampl)

|  | Declaration |
| --- | --- |
| From | ``` func VTFrameSiloCallBlockForEachSampleBuffer(_ silo: VTFrameSilo, _ timeRange: CMTimeRange, _ handler: (CMSampleBuffer) -> OSStatus) -> OSStatus ``` |
| To | ``` func VTFrameSiloCallBlockForEachSampleBuffer(_ silo: VTFrameSilo, _ timeRange: CMTimeRange, _ handler: @escaping (CMSampleBuffer) -> OSStatus) -> OSStatus ``` |

Modified [VTFrameSiloCallFunctionForEachSampleBuffer(_: VTFrameSilo, _: CMTimeRange, _: UnsafeMutableRawPointer?, _: (UnsafeMutableRawPointer?, CMSampleBuffer) -> OSStatus) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1474246-vtframesilocallfunctionforeachsa)

|  | Declaration |
| --- | --- |
| From | ``` func VTFrameSiloCallFunctionForEachSampleBuffer(_ silo: VTFrameSilo, _ timeRange: CMTimeRange, _ callbackInfo: UnsafeMutablePointer<Void>, _ callback: (UnsafeMutablePointer<Void>, CMSampleBuffer) -> OSStatus) -> OSStatus ``` |
| To | ``` func VTFrameSiloCallFunctionForEachSampleBuffer(_ silo: VTFrameSilo, _ timeRange: CMTimeRange, _ callbackInfo: UnsafeMutableRawPointer?, _ callback: @escaping (UnsafeMutableRawPointer?, CMSampleBuffer) -> OSStatus) -> OSStatus ``` |

Modified [VTSessionCopyProperty(_: VTSession, _: CFString, _: CFAllocator?, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536169-vtsessioncopyproperty)

|  | Declaration |
| --- | --- |
| From | ``` func VTSessionCopyProperty(_ session: VTSession, _ propertyKey: CFString, _ allocator: CFAllocator?, _ propertyValueOut: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func VTSessionCopyProperty(_ session: VTSession, _ propertyKey: CFString, _ allocator: CFAllocator?, _ propertyValueOut: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [VTSessionSetProperty(_: VTSession, _: CFString, _: CFTypeRef) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536144-vtsessionsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func VTSessionSetProperty(_ session: VTSession, _ propertyKey: CFString, _ propertyValue: AnyObject) -> OSStatus ``` |
| To | ``` func VTSessionSetProperty(_ session: VTSession, _ propertyKey: CFString, _ propertyValue: CFTypeRef) -> OSStatus ``` |

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
