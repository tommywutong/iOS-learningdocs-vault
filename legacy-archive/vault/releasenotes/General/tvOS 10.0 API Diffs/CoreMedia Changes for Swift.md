---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/CoreMedia.html
archived_at: '2026-07-18T02:57:39.567003Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# CoreMedia Changes for Swift

### CoreMedia

Removed [CMBlockBufferCustomBlockSource.init(version: UInt32, AllocateBlock: ((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)?, FreeBlock: ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)?, refCon: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/coremedia/cmblockbuffercustomblocksource/1489216-init)Added [CMBlockBufferCustomBlockSource.init(version: UInt32, AllocateBlock: ( (UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)?, FreeBlock: ( (UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Swift.Void)?, refCon: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/coremedia/cmblockbuffercustomblocksource/1489216-init)Added [kCMFormatDescriptionTransferFunction_SMPTE_ST_428_1](https://developer.apple.com/documentation/coremedia/kcmformatdescriptiontransferfunction_smpte_st_428_1)Added [kCMMetadataFormatDescriptionKey_SetupData](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescriptionkey_setupdata)Added [kCMMetadataFormatDescriptionMetadataSpecificationKey_SetupData](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescriptionmetadataspecificationkey_setupdata)Modified [CMBlockBufferCustomBlockSource [struct]](https://developer.apple.com/documentation/coremedia/cmblockbuffercustomblocksource)

|  | Declaration |
| --- | --- |
| From | ``` struct CMBlockBufferCustomBlockSource {     var version: UInt32     var AllocateBlock: ((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)?     var FreeBlock: ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)?     var refCon: UnsafeMutablePointer<Void>     init()     init(version version: UInt32, AllocateBlock AllocateBlock: ((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)?, FreeBlock FreeBlock: ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)?, refCon refCon: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct CMBlockBufferCustomBlockSource {     var version: UInt32     var AllocateBlock: ((UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)?     var FreeBlock: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Swift.Void)?     var refCon: UnsafeMutableRawPointer?     init()     init(version version: UInt32, AllocateBlock AllocateBlock: (@escaping (UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)?, FreeBlock FreeBlock: (@escaping (UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Swift.Void)?, refCon refCon: UnsafeMutableRawPointer?) } ``` |

Modified [CMBlockBufferCustomBlockSource.AllocateBlock](https://developer.apple.com/documentation/coremedia/cmblockbuffercustomblocksource/1489804-allocateblock)

|  | Declaration |
| --- | --- |
| From | ``` var AllocateBlock: ((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)? ``` |
| To | ``` var AllocateBlock: ((UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)? ``` |

Modified [CMBlockBufferCustomBlockSource.FreeBlock](https://developer.apple.com/documentation/coremedia/cmblockbuffercustomblocksource/1489467-freeblock)

|  | Declaration |
| --- | --- |
| From | ``` var FreeBlock: ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)? ``` |
| To | ``` var FreeBlock: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Swift.Void)? ``` |

Modified [CMBlockBufferCustomBlockSource.refCon](https://developer.apple.com/documentation/coremedia/cmblockbuffercustomblocksource/1489566-refcon)

|  | Declaration |
| --- | --- |
| From | ``` var refCon: UnsafeMutablePointer<Void> ``` |
| To | ``` var refCon: UnsafeMutableRawPointer? ``` |

Modified [CMBufferCallbacks [struct]](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CMBufferCallbacks {     var version: UInt32     var refcon: UnsafeMutablePointer<Void>     var getDecodeTimeStamp: CMBufferGetTimeCallback?     var getPresentationTimeStamp: CMBufferGetTimeCallback?     var getDuration: CMBufferGetTimeCallback     var isDataReady: CMBufferGetBooleanCallback?     var compare: CMBufferCompareCallback?     var dataBecameReadyNotification: Unmanaged<CFString>?     var getSize: CMBufferGetSizeCallback? } ``` |
| To | ``` struct CMBufferCallbacks {     var version: UInt32     var refcon: UnsafeMutableRawPointer?     var getDecodeTimeStamp: CoreMedia.CMBufferGetTimeCallback?     var getPresentationTimeStamp: CoreMedia.CMBufferGetTimeCallback?     var getDuration: CoreMedia.CMBufferGetTimeCallback     var isDataReady: CoreMedia.CMBufferGetBooleanCallback?     var compare: CoreMedia.CMBufferCompareCallback?     var dataBecameReadyNotification: Unmanaged<CFString>?     var getSize: CoreMedia.CMBufferGetSizeCallback? } ``` |

Modified [CMBufferCallbacks.compare](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks/1489718-compare)

|  | Declaration |
| --- | --- |
| From | ``` var compare: CMBufferCompareCallback? ``` |
| To | ``` var compare: CoreMedia.CMBufferCompareCallback? ``` |

Modified [CMBufferCallbacks.getDecodeTimeStamp](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks/1489805-getdecodetimestamp)

|  | Declaration |
| --- | --- |
| From | ``` var getDecodeTimeStamp: CMBufferGetTimeCallback? ``` |
| To | ``` var getDecodeTimeStamp: CoreMedia.CMBufferGetTimeCallback? ``` |

Modified [CMBufferCallbacks.getDuration](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks/1489146-getduration)

|  | Declaration |
| --- | --- |
| From | ``` var getDuration: CMBufferGetTimeCallback ``` |
| To | ``` var getDuration: CoreMedia.CMBufferGetTimeCallback ``` |

Modified [CMBufferCallbacks.getPresentationTimeStamp](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks/1489600-getpresentationtimestamp)

|  | Declaration |
| --- | --- |
| From | ``` var getPresentationTimeStamp: CMBufferGetTimeCallback? ``` |
| To | ``` var getPresentationTimeStamp: CoreMedia.CMBufferGetTimeCallback? ``` |

Modified [CMBufferCallbacks.getSize](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks/1489328-getsize)

|  | Declaration |
| --- | --- |
| From | ``` var getSize: CMBufferGetSizeCallback? ``` |
| To | ``` var getSize: CoreMedia.CMBufferGetSizeCallback? ``` |

Modified [CMBufferCallbacks.isDataReady](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks/1489430-isdataready)

|  | Declaration |
| --- | --- |
| From | ``` var isDataReady: CMBufferGetBooleanCallback? ``` |
| To | ``` var isDataReady: CoreMedia.CMBufferGetBooleanCallback? ``` |

Modified [CMBufferCallbacks.refcon](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks/1489420-refcon)

|  | Declaration |
| --- | --- |
| From | ``` var refcon: UnsafeMutablePointer<Void> ``` |
| To | ``` var refcon: UnsafeMutableRawPointer? ``` |

Modified [CMTime [struct]](https://developer.apple.com/documentation/coremedia/cmtime)

|  | Declaration |
| --- | --- |
| From | ``` struct CMTime {     var value: CMTimeValue     var timescale: CMTimeScale     var flags: CMTimeFlags     var epoch: CMTimeEpoch     init()     init(value value: CMTimeValue, timescale timescale: CMTimeScale, flags flags: CMTimeFlags, epoch epoch: CMTimeEpoch) } extension CMTime {     init(seconds seconds: Double, preferredTimescale preferredTimescale: CMTimeScale)     init(value value: CMTimeValue, timescale timescale: CMTimeScale) } extension CMTime {     var isValid: Bool { get }     var isPositiveInfinity: Bool { get }     var isNegativeInfinity: Bool { get }     var isIndefinite: Bool { get }     var isNumeric: Bool { get }     var hasBeenRounded: Bool { get }     var seconds: Double { get }     func convertScale(_ newTimescale: Int32, method method: CMTimeRoundingMethod) -> CMTime } extension CMTime : Equatable, Comparable { } extension CMTime {     init(seconds seconds: Double, preferredTimescale preferredTimescale: CMTimeScale)     init(value value: CMTimeValue, timescale timescale: CMTimeScale) } extension CMTime {     var isValid: Bool { get }     var isPositiveInfinity: Bool { get }     var isNegativeInfinity: Bool { get }     var isIndefinite: Bool { get }     var isNumeric: Bool { get }     var hasBeenRounded: Bool { get }     var seconds: Double { get }     func convertScale(_ newTimescale: Int32, method method: CMTimeRoundingMethod) -> CMTime } extension CMTime : Equatable, Comparable { } ``` |
| To | ``` struct CMTime {     var value: CMTimeValue     var timescale: CMTimeScale     var flags: CMTimeFlags     var epoch: CMTimeEpoch     init()     init(value value: CMTimeValue, timescale timescale: CMTimeScale, flags flags: CMTimeFlags, epoch epoch: CMTimeEpoch)     init(seconds seconds: Double, preferredTimescale preferredTimescale: CMTimeScale)     init(value value: CMTimeValue, timescale timescale: CMTimeScale)     var isValid: Bool { get }     var isPositiveInfinity: Bool { get }     var isNegativeInfinity: Bool { get }     var isIndefinite: Bool { get }     var isNumeric: Bool { get }     var hasBeenRounded: Bool { get }     var seconds: Double { get }     func convertScale(_ newTimescale: Int32, method method: CMTimeRoundingMethod) -> CMTime } extension CMTime {     init(seconds seconds: Double, preferredTimescale preferredTimescale: CMTimeScale)     init(value value: CMTimeValue, timescale timescale: CMTimeScale) } extension CMTime {     var isValid: Bool { get }     var isPositiveInfinity: Bool { get }     var isNegativeInfinity: Bool { get }     var isIndefinite: Bool { get }     var isNumeric: Bool { get }     var hasBeenRounded: Bool { get }     var seconds: Double { get }     func convertScale(_ newTimescale: Int32, method method: CMTimeRoundingMethod) -> CMTime } extension CMTime : Equatable, Comparable { } ``` |

Modified [CMTimeFlags [struct]](https://developer.apple.com/documentation/coremedia/cmtimeflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CMTimeFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var Valid: CMTimeFlags { get }     static var HasBeenRounded: CMTimeFlags { get }     static var PositiveInfinity: CMTimeFlags { get }     static var NegativeInfinity: CMTimeFlags { get }     static var Indefinite: CMTimeFlags { get }     static var ImpliedValueFlagsMask: CMTimeFlags { get } } ``` | OptionSetType |
| To | ``` struct CMTimeFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var valid: CMTimeFlags { get }     static var hasBeenRounded: CMTimeFlags { get }     static var positiveInfinity: CMTimeFlags { get }     static var negativeInfinity: CMTimeFlags { get }     static var indefinite: CMTimeFlags { get }     static var impliedValueFlagsMask: CMTimeFlags { get }     func intersect(_ other: CMTimeFlags) -> CMTimeFlags     func exclusiveOr(_ other: CMTimeFlags) -> CMTimeFlags     mutating func unionInPlace(_ other: CMTimeFlags)     mutating func intersectInPlace(_ other: CMTimeFlags)     mutating func exclusiveOrInPlace(_ other: CMTimeFlags)     func isSubsetOf(_ other: CMTimeFlags) -> Bool     func isDisjointWith(_ other: CMTimeFlags) -> Bool     func isSupersetOf(_ other: CMTimeFlags) -> Bool     mutating func subtractInPlace(_ other: CMTimeFlags)     func isStrictSupersetOf(_ other: CMTimeFlags) -> Bool     func isStrictSubsetOf(_ other: CMTimeFlags) -> Bool } extension CMTimeFlags {     func union(_ other: CMTimeFlags) -> CMTimeFlags     func intersection(_ other: CMTimeFlags) -> CMTimeFlags     func symmetricDifference(_ other: CMTimeFlags) -> CMTimeFlags } extension CMTimeFlags {     func contains(_ member: CMTimeFlags) -> Bool     mutating func insert(_ newMember: CMTimeFlags) -> (inserted: Bool, memberAfterInsert: CMTimeFlags)     mutating func remove(_ member: CMTimeFlags) -> CMTimeFlags?     mutating func update(with newMember: CMTimeFlags) -> CMTimeFlags? } extension CMTimeFlags {     convenience init()     mutating func formUnion(_ other: CMTimeFlags)     mutating func formIntersection(_ other: CMTimeFlags)     mutating func formSymmetricDifference(_ other: CMTimeFlags) } extension CMTimeFlags {     convenience init<S : Sequence where S.Iterator.Element == CMTimeFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CMTimeFlags...)     mutating func subtract(_ other: CMTimeFlags)     func isSubset(of other: CMTimeFlags) -> Bool     func isSuperset(of other: CMTimeFlags) -> Bool     func isDisjoint(with other: CMTimeFlags) -> Bool     func subtracting(_ other: CMTimeFlags) -> CMTimeFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: CMTimeFlags) -> Bool     func isStrictSubset(of other: CMTimeFlags) -> Bool } ``` | OptionSet |

Modified [CMTimeFlags.hasBeenRounded](https://developer.apple.com/documentation/coremedia/cmtimeflags/kcmtimeflags_hasbeenrounded)

|  | Declaration |
| --- | --- |
| From | ``` static var HasBeenRounded: CMTimeFlags { get } ``` |
| To | ``` static var hasBeenRounded: CMTimeFlags { get } ``` |

Modified [CMTimeFlags.impliedValueFlagsMask](https://developer.apple.com/documentation/coremedia/cmtimeflags/kcmtimeflags_impliedvalueflagsmask)

|  | Declaration |
| --- | --- |
| From | ``` static var ImpliedValueFlagsMask: CMTimeFlags { get } ``` |
| To | ``` static var impliedValueFlagsMask: CMTimeFlags { get } ``` |

Modified [CMTimeFlags.indefinite](https://developer.apple.com/documentation/coremedia/cmtimeflags/kcmtimeflags_indefinite)

|  | Declaration |
| --- | --- |
| From | ``` static var Indefinite: CMTimeFlags { get } ``` |
| To | ``` static var indefinite: CMTimeFlags { get } ``` |

Modified [CMTimeFlags.negativeInfinity](https://developer.apple.com/documentation/coremedia/cmtimeflags/kcmtimeflags_negativeinfinity)

|  | Declaration |
| --- | --- |
| From | ``` static var NegativeInfinity: CMTimeFlags { get } ``` |
| To | ``` static var negativeInfinity: CMTimeFlags { get } ``` |

Modified [CMTimeFlags.positiveInfinity](https://developer.apple.com/documentation/coremedia/cmtimeflags/kcmtimeflags_positiveinfinity)

|  | Declaration |
| --- | --- |
| From | ``` static var PositiveInfinity: CMTimeFlags { get } ``` |
| To | ``` static var positiveInfinity: CMTimeFlags { get } ``` |

Modified [CMTimeFlags.valid](https://developer.apple.com/documentation/coremedia/cmtimeflags/1400873-valid)

|  | Declaration |
| --- | --- |
| From | ``` static var Valid: CMTimeFlags { get } ``` |
| To | ``` static var valid: CMTimeFlags { get } ``` |

Modified [CMTimeRange [struct]](https://developer.apple.com/documentation/coremedia/cmtimerange)

|  | Declaration |
| --- | --- |
| From | ``` struct CMTimeRange {     var start: CMTime     var duration: CMTime     init()     init(start start: CMTime, duration duration: CMTime) } extension CMTimeRange {     init(start start: CMTime, end end: CMTime)     var isValid: Bool { get }     var isIndefinite: Bool { get }     var isEmpty: Bool { get }     var end: CMTime { get }     @warn_unused_result     func union(_ otherRange: CMTimeRange) -> CMTimeRange     @warn_unused_result     func intersection(_ otherRange: CMTimeRange) -> CMTimeRange     @warn_unused_result     func containsTime(_ time: CMTime) -> Bool     @warn_unused_result     func containsTimeRange(_ range: CMTimeRange) -> Bool } extension CMTimeRange : Equatable { } extension CMTimeRange {     init(start start: CMTime, end end: CMTime)     var isValid: Bool { get }     var isIndefinite: Bool { get }     var isEmpty: Bool { get }     var end: CMTime { get }     @warn_unused_result     func union(_ otherRange: CMTimeRange) -> CMTimeRange     @warn_unused_result     func intersection(_ otherRange: CMTimeRange) -> CMTimeRange     @warn_unused_result     func containsTime(_ time: CMTime) -> Bool     @warn_unused_result     func containsTimeRange(_ range: CMTimeRange) -> Bool } extension CMTimeRange : Equatable { } ``` |
| To | ``` struct CMTimeRange {     var start: CMTime     var duration: CMTime     init()     init(start start: CMTime, duration duration: CMTime)     init(start start: CMTime, end end: CMTime)     var isValid: Bool { get }     var isIndefinite: Bool { get }     var isEmpty: Bool { get }     var end: CMTime { get }     func union(_ otherRange: CMTimeRange) -> CMTimeRange     func intersection(_ otherRange: CMTimeRange) -> CMTimeRange     func containsTime(_ time: CMTime) -> Bool     func containsTimeRange(_ range: CMTimeRange) -> Bool } extension CMTimeRange {     init(start start: CMTime, end end: CMTime)     var isValid: Bool { get }     var isIndefinite: Bool { get }     var isEmpty: Bool { get }     var end: CMTime { get }     func union(_ otherRange: CMTimeRange) -> CMTimeRange     func intersection(_ otherRange: CMTimeRange) -> CMTimeRange     func containsTime(_ time: CMTime) -> Bool     func containsTimeRange(_ range: CMTimeRange) -> Bool } extension CMTimeRange : Equatable { } ``` |

Modified [CMTimeRange.containsTime(_: CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/cmtimerange/1489518-containstime)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result     func containsTime(_ time: CMTime) -> Bool ``` |
| To | ``` func containsTime(_ time: CMTime) -> Bool ``` |

Modified [CMTimeRange.containsTimeRange(_: CMTimeRange) -> Bool](https://developer.apple.com/documentation/coremedia/cmtimerange/1489757-containstimerange)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result     func containsTimeRange(_ range: CMTimeRange) -> Bool ``` |
| To | ``` func containsTimeRange(_ range: CMTimeRange) -> Bool ``` |

Modified [CMTimeRange.intersection(_: CMTimeRange) -> CMTimeRange](https://developer.apple.com/documentation/coremedia/cmtimerange/1489598-intersection)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result     func intersection(_ otherRange: CMTimeRange) -> CMTimeRange ``` |
| To | ``` func intersection(_ otherRange: CMTimeRange) -> CMTimeRange ``` |

Modified [CMTimeRange.union(_: CMTimeRange) -> CMTimeRange](https://developer.apple.com/documentation/coremedia/cmtimerange/1489789-union)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result     func union(_ otherRange: CMTimeRange) -> CMTimeRange ``` |
| To | ``` func union(_ otherRange: CMTimeRange) -> CMTimeRange ``` |

Modified [CMTimeRoundingMethod [enum]](https://developer.apple.com/documentation/coremedia/cmtimeroundingmethod)

|  | Declaration |
| --- | --- |
| From | ``` enum CMTimeRoundingMethod : UInt32 {     case RoundHalfAwayFromZero     case RoundTowardZero     case RoundAwayFromZero     case QuickTime     case RoundTowardPositiveInfinity     case RoundTowardNegativeInfinity     static var Default: CMTimeRoundingMethod { get } } ``` |
| To | ``` enum CMTimeRoundingMethod : UInt32 {     case roundHalfAwayFromZero     case roundTowardZero     case roundAwayFromZero     case quickTime     case roundTowardPositiveInfinity     case roundTowardNegativeInfinity     static var `default`: CMTimeRoundingMethod { get } } ``` |

Modified [CMTimeRoundingMethod.default](https://developer.apple.com/documentation/coremedia/cmtimeroundingmethod/kcmtimeroundingmethod_default)

|  | Declaration |
| --- | --- |
| From | ``` static var Default: CMTimeRoundingMethod { get } ``` |
| To | ``` static var `default`: CMTimeRoundingMethod { get } ``` |

Modified [CMTimeRoundingMethod.quickTime](https://developer.apple.com/documentation/coremedia/cmtimeroundingmethod/kcmtimeroundingmethod_quicktime)

|  | Declaration |
| --- | --- |
| From | ``` case QuickTime ``` |
| To | ``` case quickTime ``` |

Modified [CMTimeRoundingMethod.roundAwayFromZero](https://developer.apple.com/documentation/coremedia/cmtimeroundingmethod/roundawayfromzero)

|  | Declaration |
| --- | --- |
| From | ``` case RoundAwayFromZero ``` |
| To | ``` case roundAwayFromZero ``` |

Modified [CMTimeRoundingMethod.roundHalfAwayFromZero](https://developer.apple.com/documentation/coremedia/cmtimeroundingmethod/roundhalfawayfromzero)

|  | Declaration |
| --- | --- |
| From | ``` case RoundHalfAwayFromZero ``` |
| To | ``` case roundHalfAwayFromZero ``` |

Modified [CMTimeRoundingMethod.roundTowardNegativeInfinity](https://developer.apple.com/documentation/coremedia/cmtimeroundingmethod/roundtowardnegativeinfinity)

|  | Declaration |
| --- | --- |
| From | ``` case RoundTowardNegativeInfinity ``` |
| To | ``` case roundTowardNegativeInfinity ``` |

Modified [CMTimeRoundingMethod.roundTowardPositiveInfinity](https://developer.apple.com/documentation/coremedia/cmtimeroundingmethod/roundtowardpositiveinfinity)

|  | Declaration |
| --- | --- |
| From | ``` case RoundTowardPositiveInfinity ``` |
| To | ``` case roundTowardPositiveInfinity ``` |

Modified [CMTimeRoundingMethod.roundTowardZero](https://developer.apple.com/documentation/coremedia/cmtimeroundingmethod/kcmtimeroundingmethod_roundtowardzero)

|  | Declaration |
| --- | --- |
| From | ``` case RoundTowardZero ``` |
| To | ``` case roundTowardZero ``` |

Modified !=(_: CMTimeRange, _: CMTimeRange) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func !=(_ range1: CMTimeRange, _ range2: CMTimeRange) -> Bool ``` |
| To | ``` func !=(_ range1: CMTimeRange, _ range2: CMTimeRange) -> Bool ``` |

Modified !=(_: CMTime, _: CMTime) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func !=(_ time1: CMTime, _ time2: CMTime) -> Bool ``` |
| To | ``` func !=(_ time1: CMTime, _ time2: CMTime) -> Bool ``` |

Modified +(_: CMTime, _: CMTime) -> CMTime

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ addend1: CMTime, _ addend2: CMTime) -> CMTime ``` |
| To | ``` func +(_ addend1: CMTime, _ addend2: CMTime) -> CMTime ``` |

Modified -(_: CMTime, _: CMTime) -> CMTime

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ minuend: CMTime, _ subtrahend: CMTime) -> CMTime ``` |
| To | ``` func -(_ minuend: CMTime, _ subtrahend: CMTime) -> CMTime ``` |

Modified <(_: CMTime, _: CMTime) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func <(_ time1: CMTime, _ time2: CMTime) -> Bool ``` |
| To | ``` func <(_ time1: CMTime, _ time2: CMTime) -> Bool ``` |

Modified <=(_: CMTime, _: CMTime) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func <=(_ time1: CMTime, _ time2: CMTime) -> Bool ``` |
| To | ``` func <=(_ time1: CMTime, _ time2: CMTime) -> Bool ``` |

Modified ==(_: CMTime, _: CMTime) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ==(_ time1: CMTime, _ time2: CMTime) -> Bool ``` |
| To | ``` func ==(_ time1: CMTime, _ time2: CMTime) -> Bool ``` |

Modified ==(_: CMTimeRange, _: CMTimeRange) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ==(_ range1: CMTimeRange, _ range2: CMTimeRange) -> Bool ``` |
| To | ``` func ==(_ range1: CMTimeRange, _ range2: CMTimeRange) -> Bool ``` |

Modified >(_: CMTime, _: CMTime) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func >(_ time1: CMTime, _ time2: CMTime) -> Bool ``` |
| To | ``` func >(_ time1: CMTime, _ time2: CMTime) -> Bool ``` |

Modified >=(_: CMTime, _: CMTime) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func >=(_ time1: CMTime, _ time2: CMTime) -> Bool ``` |
| To | ``` func >=(_ time1: CMTime, _ time2: CMTime) -> Bool ``` |

Modified [CMAudioFormatDescription](https://developer.apple.com/documentation/coremedia/cmaudioformatdescriptionref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMAudioFormatDescriptionRef = CMAudioFormatDescription ``` |
| To | ``` typealias CMAudioFormatDescription = CMFormatDescription ``` |

Modified [CMAudioFormatDescriptionCreate(_: CFAllocator?, _: UnsafePointer<AudioStreamBasicDescription>, _: Int, _: UnsafePointer<AudioChannelLayout>?, _: Int, _: UnsafeRawPointer?, _: CFDictionary?, _: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489522-cmaudioformatdescriptioncreate)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionCreate(_ allocator: CFAllocator?, _ asbd: UnsafePointer<AudioStreamBasicDescription>, _ layoutSize: Int, _ layout: UnsafePointer<AudioChannelLayout>, _ magicCookieSize: Int, _ magicCookie: UnsafePointer<Void>, _ extensions: CFDictionary?, _ outDesc: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus ``` |
| To | ``` func CMAudioFormatDescriptionCreate(_ allocator: CFAllocator?, _ asbd: UnsafePointer<AudioStreamBasicDescription>, _ layoutSize: Int, _ layout: UnsafePointer<AudioChannelLayout>?, _ magicCookieSize: Int, _ magicCookie: UnsafeRawPointer?, _ extensions: CFDictionary?, _ outDesc: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus ``` |

Modified [CMAudioFormatDescriptionEqual(_: CMAudioFormatDescription, _: CMAudioFormatDescription, _: CMAudioFormatDescriptionMask, _: UnsafeMutablePointer<CMAudioFormatDescriptionMask>?) -> Bool](https://developer.apple.com/documentation/coremedia/1489582-cmaudioformatdescriptionequal)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionEqual(_ desc1: CMAudioFormatDescription, _ desc2: CMAudioFormatDescription, _ equalityMask: CMAudioFormatDescriptionMask, _ equalityMaskOut: UnsafeMutablePointer<CMAudioFormatDescriptionMask>) -> Bool ``` |
| To | ``` func CMAudioFormatDescriptionEqual(_ desc1: CMAudioFormatDescription, _ desc2: CMAudioFormatDescription, _ equalityMask: CMAudioFormatDescriptionMask, _ equalityMaskOut: UnsafeMutablePointer<CMAudioFormatDescriptionMask>?) -> Bool ``` |

Modified [CMAudioFormatDescriptionGetChannelLayout(_: CMAudioFormatDescription, _: UnsafeMutablePointer<Int>?) -> UnsafePointer<AudioChannelLayout>?](https://developer.apple.com/documentation/coremedia/1489137-cmaudioformatdescriptiongetchann)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionGetChannelLayout(_ desc: CMAudioFormatDescription, _ layoutSize: UnsafeMutablePointer<Int>) -> UnsafePointer<AudioChannelLayout> ``` |
| To | ``` func CMAudioFormatDescriptionGetChannelLayout(_ desc: CMAudioFormatDescription, _ layoutSize: UnsafeMutablePointer<Int>?) -> UnsafePointer<AudioChannelLayout>? ``` |

Modified [CMAudioFormatDescriptionGetFormatList(_: CMAudioFormatDescription, _: UnsafeMutablePointer<Int>?) -> UnsafePointer<AudioFormatListItem>?](https://developer.apple.com/documentation/coremedia/1489782-cmaudioformatdescriptiongetforma)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionGetFormatList(_ desc: CMAudioFormatDescription, _ formatListSize: UnsafeMutablePointer<Int>) -> UnsafePointer<AudioFormatListItem> ``` |
| To | ``` func CMAudioFormatDescriptionGetFormatList(_ desc: CMAudioFormatDescription, _ formatListSize: UnsafeMutablePointer<Int>?) -> UnsafePointer<AudioFormatListItem>? ``` |

Modified [CMAudioFormatDescriptionGetMagicCookie(_: CMAudioFormatDescription, _: UnsafeMutablePointer<Int>?) -> UnsafeRawPointer?](https://developer.apple.com/documentation/coremedia/1489508-cmaudioformatdescriptiongetmagic)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionGetMagicCookie(_ desc: CMAudioFormatDescription, _ cookieSizeOut: UnsafeMutablePointer<Int>) -> UnsafePointer<Void> ``` |
| To | ``` func CMAudioFormatDescriptionGetMagicCookie(_ desc: CMAudioFormatDescription, _ cookieSizeOut: UnsafeMutablePointer<Int>?) -> UnsafeRawPointer? ``` |

Modified [CMAudioFormatDescriptionGetMostCompatibleFormat(_: CMAudioFormatDescription) -> UnsafePointer<AudioFormatListItem>?](https://developer.apple.com/documentation/coremedia/1489474-cmaudioformatdescriptiongetmostc)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionGetMostCompatibleFormat(_ desc: CMAudioFormatDescription) -> UnsafePointer<AudioFormatListItem> ``` |
| To | ``` func CMAudioFormatDescriptionGetMostCompatibleFormat(_ desc: CMAudioFormatDescription) -> UnsafePointer<AudioFormatListItem>? ``` |

Modified [CMAudioFormatDescriptionGetRichestDecodableFormat(_: CMAudioFormatDescription) -> UnsafePointer<AudioFormatListItem>?](https://developer.apple.com/documentation/coremedia/1489575-cmaudioformatdescriptiongetriche)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionGetRichestDecodableFormat(_ desc: CMAudioFormatDescription) -> UnsafePointer<AudioFormatListItem> ``` |
| To | ``` func CMAudioFormatDescriptionGetRichestDecodableFormat(_ desc: CMAudioFormatDescription) -> UnsafePointer<AudioFormatListItem>? ``` |

Modified [CMAudioFormatDescriptionGetStreamBasicDescription(_: CMAudioFormatDescription) -> UnsafePointer<AudioStreamBasicDescription>?](https://developer.apple.com/documentation/coremedia/1489226-cmaudioformatdescriptiongetstrea)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionGetStreamBasicDescription(_ desc: CMAudioFormatDescription) -> UnsafePointer<AudioStreamBasicDescription> ``` |
| To | ``` func CMAudioFormatDescriptionGetStreamBasicDescription(_ desc: CMAudioFormatDescription) -> UnsafePointer<AudioStreamBasicDescription>? ``` |

Modified [CMAudioSampleBufferCreateReadyWithPacketDescriptions(_: CFAllocator?, _: CMBlockBuffer?, _: CMFormatDescription, _: CMItemCount, _: CMTime, _: UnsafePointer<AudioStreamPacketDescription>?, _: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489500-cmaudiosamplebuffercreatereadywi)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioSampleBufferCreateReadyWithPacketDescriptions(_ allocator: CFAllocator?, _ dataBuffer: CMBlockBuffer?, _ formatDescription: CMFormatDescription, _ numSamples: CMItemCount, _ sbufPTS: CMTime, _ packetDescriptions: UnsafePointer<AudioStreamPacketDescription>, _ sBufOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |
| To | ``` func CMAudioSampleBufferCreateReadyWithPacketDescriptions(_ allocator: CFAllocator?, _ dataBuffer: CMBlockBuffer?, _ formatDescription: CMFormatDescription, _ numSamples: CMItemCount, _ sbufPTS: CMTime, _ packetDescriptions: UnsafePointer<AudioStreamPacketDescription>?, _ sBufOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |

Modified [CMAudioSampleBufferCreateWithPacketDescriptions(_: CFAllocator?, _: CMBlockBuffer?, _: Bool, _: CoreMedia.CMSampleBufferMakeDataReadyCallback?, _: UnsafeMutableRawPointer?, _: CMFormatDescription, _: CMItemCount, _: CMTime, _: UnsafePointer<AudioStreamPacketDescription>?, _: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489466-cmaudiosamplebuffercreatewithpac)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioSampleBufferCreateWithPacketDescriptions(_ allocator: CFAllocator?, _ dataBuffer: CMBlockBuffer?, _ dataReady: Bool, _ makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, _ makeDataReadyRefcon: UnsafeMutablePointer<Void>, _ formatDescription: CMFormatDescription, _ numSamples: CMItemCount, _ sbufPTS: CMTime, _ packetDescriptions: UnsafePointer<AudioStreamPacketDescription>, _ sBufOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |
| To | ``` func CMAudioSampleBufferCreateWithPacketDescriptions(_ allocator: CFAllocator?, _ dataBuffer: CMBlockBuffer?, _ dataReady: Bool, _ makeDataReadyCallback: CoreMedia.CMSampleBufferMakeDataReadyCallback?, _ makeDataReadyRefcon: UnsafeMutableRawPointer?, _ formatDescription: CMFormatDescription, _ numSamples: CMItemCount, _ sbufPTS: CMTime, _ packetDescriptions: UnsafePointer<AudioStreamPacketDescription>?, _ sBufOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |

Modified [CMBlockBufferAccessDataBytes(_: CMBlockBuffer, _: Int, _: Int, _: UnsafeMutableRawPointer, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489228-cmblockbufferaccessdatabytes)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferAccessDataBytes(_ theBuffer: CMBlockBuffer, _ offset: Int, _ length: Int, _ temporaryBlock: UnsafeMutablePointer<Void>, _ returnedPointer: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus ``` |
| To | ``` func CMBlockBufferAccessDataBytes(_ theBuffer: CMBlockBuffer, _ offset: Int, _ length: Int, _ temporaryBlock: UnsafeMutableRawPointer, _ returnedPointer: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>) -> OSStatus ``` |

Modified [CMBlockBufferAppendMemoryBlock(_: CMBlockBuffer, _: UnsafeMutableRawPointer?, _: Int, _: CFAllocator?, _: UnsafePointer<CMBlockBufferCustomBlockSource>?, _: Int, _: Int, _: CMBlockBufferFlags) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489394-cmblockbufferappendmemoryblock)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferAppendMemoryBlock(_ theBuffer: CMBlockBuffer, _ memoryBlock: UnsafeMutablePointer<Void>, _ blockLength: Int, _ blockAllocator: CFAllocator?, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags) -> OSStatus ``` |
| To | ``` func CMBlockBufferAppendMemoryBlock(_ theBuffer: CMBlockBuffer, _ memoryBlock: UnsafeMutableRawPointer?, _ blockLength: Int, _ blockAllocator: CFAllocator?, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags) -> OSStatus ``` |

Modified [CMBlockBufferCopyDataBytes(_: CMBlockBuffer, _: Int, _: Int, _: UnsafeMutableRawPointer) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489155-cmblockbuffercopydatabytes)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferCopyDataBytes(_ theSourceBuffer: CMBlockBuffer, _ offsetToData: Int, _ dataLength: Int, _ destination: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func CMBlockBufferCopyDataBytes(_ theSourceBuffer: CMBlockBuffer, _ offsetToData: Int, _ dataLength: Int, _ destination: UnsafeMutableRawPointer) -> OSStatus ``` |

Modified [CMBlockBufferCreateContiguous(_: CFAllocator?, _: CMBlockBuffer, _: CFAllocator?, _: UnsafePointer<CMBlockBufferCustomBlockSource>?, _: Int, _: Int, _: CMBlockBufferFlags, _: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489220-cmblockbuffercreatecontiguous)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferCreateContiguous(_ structureAllocator: CFAllocator?, _ sourceBuffer: CMBlockBuffer, _ blockAllocator: CFAllocator?, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus ``` |
| To | ``` func CMBlockBufferCreateContiguous(_ structureAllocator: CFAllocator?, _ sourceBuffer: CMBlockBuffer, _ blockAllocator: CFAllocator?, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus ``` |

Modified [CMBlockBufferCreateWithMemoryBlock(_: CFAllocator?, _: UnsafeMutableRawPointer?, _: Int, _: CFAllocator?, _: UnsafePointer<CMBlockBufferCustomBlockSource>?, _: Int, _: Int, _: CMBlockBufferFlags, _: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489501-cmblockbuffercreatewithmemoryblo)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferCreateWithMemoryBlock(_ structureAllocator: CFAllocator?, _ memoryBlock: UnsafeMutablePointer<Void>, _ blockLength: Int, _ blockAllocator: CFAllocator?, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus ``` |
| To | ``` func CMBlockBufferCreateWithMemoryBlock(_ structureAllocator: CFAllocator?, _ memoryBlock: UnsafeMutableRawPointer?, _ blockLength: Int, _ blockAllocator: CFAllocator?, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus ``` |

Modified [CMBlockBufferGetDataPointer(_: CMBlockBuffer, _: Int, _: UnsafeMutablePointer<Int>?, _: UnsafeMutablePointer<Int>?, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>?) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489264-cmblockbuffergetdatapointer)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferGetDataPointer(_ theBuffer: CMBlockBuffer, _ offset: Int, _ lengthAtOffset: UnsafeMutablePointer<Int>, _ totalLength: UnsafeMutablePointer<Int>, _ dataPointer: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus ``` |
| To | ``` func CMBlockBufferGetDataPointer(_ theBuffer: CMBlockBuffer, _ offset: Int, _ lengthAtOffset: UnsafeMutablePointer<Int>?, _ totalLength: UnsafeMutablePointer<Int>?, _ dataPointer: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>?) -> OSStatus ``` |

Modified [CMBlockBufferReplaceDataBytes(_: UnsafeRawPointer, _: CMBlockBuffer, _: Int, _: Int) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489222-cmblockbufferreplacedatabytes)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferReplaceDataBytes(_ sourceBytes: UnsafePointer<Void>, _ destinationBuffer: CMBlockBuffer, _ offsetIntoDestination: Int, _ dataLength: Int) -> OSStatus ``` |
| To | ``` func CMBlockBufferReplaceDataBytes(_ sourceBytes: UnsafeRawPointer, _ destinationBuffer: CMBlockBuffer, _ offsetIntoDestination: Int, _ dataLength: Int) -> OSStatus ``` |

Modified [CMBufferCompareCallback](https://developer.apple.com/documentation/coremedia/cmbuffercomparecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferCompareCallback = (CMBuffer, CMBuffer, UnsafeMutablePointer<Void>) -> CFComparisonResult ``` |
| To | ``` typealias CMBufferCompareCallback = (CMBuffer, CMBuffer, UnsafeMutableRawPointer?) -> CFComparisonResult ``` |

Modified [CMBufferGetBooleanCallback](https://developer.apple.com/documentation/coremedia/cmbuffergetbooleancallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferGetBooleanCallback = (CMBuffer, UnsafeMutablePointer<Void>) -> DarwinBoolean ``` |
| To | ``` typealias CMBufferGetBooleanCallback = (CMBuffer, UnsafeMutableRawPointer?) -> DarwinBoolean ``` |

Modified [CMBufferGetSizeCallback](https://developer.apple.com/documentation/coremedia/cmbuffergetsizecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferGetSizeCallback = (CMBuffer, UnsafeMutablePointer<Void>) -> Int ``` |
| To | ``` typealias CMBufferGetSizeCallback = (CMBuffer, UnsafeMutableRawPointer?) -> Int ``` |

Modified [CMBufferGetTimeCallback](https://developer.apple.com/documentation/coremedia/cmbuffergettimecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferGetTimeCallback = (CMBuffer, UnsafeMutablePointer<Void>) -> CMTime ``` |
| To | ``` typealias CMBufferGetTimeCallback = (CMBuffer, UnsafeMutableRawPointer?) -> CMTime ``` |

Modified [CMBufferQueueCallForEachBuffer(_: CMBufferQueue, _: (CMBuffer, UnsafeMutableRawPointer?) -> OSStatus, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489798-cmbufferqueuecallforeachbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueCallForEachBuffer(_ queue: CMBufferQueue, _ callback: (CMBuffer, UnsafeMutablePointer<Void>) -> OSStatus, _ refcon: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func CMBufferQueueCallForEachBuffer(_ queue: CMBufferQueue, _ callback: @escaping (CMBuffer, UnsafeMutableRawPointer?) -> OSStatus, _ refcon: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [CMBufferQueueInstallTrigger(_: CMBufferQueue, _: CoreMedia.CMBufferQueueTriggerCallback?, _: UnsafeMutableRawPointer?, _: CMBufferQueueTriggerCondition, _: CMTime, _: UnsafeMutablePointer<CMBufferQueueTriggerToken?>?) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489822-cmbufferqueueinstalltrigger)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueInstallTrigger(_ queue: CMBufferQueue, _ triggerCallback: CMBufferQueueTriggerCallback?, _ triggerRefcon: UnsafeMutablePointer<Void>, _ triggerCondition: CMBufferQueueTriggerCondition, _ triggerTime: CMTime, _ triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken>) -> OSStatus ``` |
| To | ``` func CMBufferQueueInstallTrigger(_ queue: CMBufferQueue, _ triggerCallback: CoreMedia.CMBufferQueueTriggerCallback?, _ triggerRefcon: UnsafeMutableRawPointer?, _ triggerCondition: CMBufferQueueTriggerCondition, _ triggerTime: CMTime, _ triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken?>?) -> OSStatus ``` |

Modified [CMBufferQueueInstallTriggerWithIntegerThreshold(_: CMBufferQueue, _: CoreMedia.CMBufferQueueTriggerCallback?, _: UnsafeMutableRawPointer?, _: CMBufferQueueTriggerCondition, _: CMItemCount, _: UnsafeMutablePointer<CMBufferQueueTriggerToken?>?) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489140-cmbufferqueueinstalltriggerwithi)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueInstallTriggerWithIntegerThreshold(_ queue: CMBufferQueue, _ triggerCallback: CMBufferQueueTriggerCallback?, _ triggerRefcon: UnsafeMutablePointer<Void>, _ triggerCondition: CMBufferQueueTriggerCondition, _ triggerThreshold: CMItemCount, _ triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken>) -> OSStatus ``` |
| To | ``` func CMBufferQueueInstallTriggerWithIntegerThreshold(_ queue: CMBufferQueue, _ triggerCallback: CoreMedia.CMBufferQueueTriggerCallback?, _ triggerRefcon: UnsafeMutableRawPointer?, _ triggerCondition: CMBufferQueueTriggerCondition, _ triggerThreshold: CMItemCount, _ triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken?>?) -> OSStatus ``` |

Modified [CMBufferQueueResetWithCallback(_: CMBufferQueue, _: (CMBuffer, UnsafeMutableRawPointer?) -> Swift.Void, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489361-cmbufferqueueresetwithcallback)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueResetWithCallback(_ queue: CMBufferQueue, _ callback: (CMBuffer, UnsafeMutablePointer<Void>) -> Void, _ refcon: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func CMBufferQueueResetWithCallback(_ queue: CMBufferQueue, _ callback: @escaping (CMBuffer, UnsafeMutableRawPointer?) -> Swift.Void, _ refcon: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [CMBufferQueueSetValidationCallback(_: CMBufferQueue, _: CoreMedia.CMBufferValidationCallback, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489350-cmbufferqueuesetvalidationcallba)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueSetValidationCallback(_ queue: CMBufferQueue, _ validationCallback: CMBufferValidationCallback, _ validationRefCon: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func CMBufferQueueSetValidationCallback(_ queue: CMBufferQueue, _ validationCallback: CoreMedia.CMBufferValidationCallback, _ validationRefCon: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [CMBufferQueueTriggerCallback](https://developer.apple.com/documentation/coremedia/cmbufferqueuetriggercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferQueueTriggerCallback = (UnsafeMutablePointer<Void>, CMBufferQueueTriggerToken) -> Void ``` |
| To | ``` typealias CMBufferQueueTriggerCallback = (UnsafeMutableRawPointer?, CMBufferQueueTriggerToken) -> Swift.Void ``` |

Modified [CMBufferQueueTriggerToken](https://developer.apple.com/documentation/coremedia/cmbufferqueuetriggertoken)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferQueueTriggerToken = COpaquePointer ``` |
| To | ``` typealias CMBufferQueueTriggerToken = OpaquePointer ``` |

Modified [CMBufferValidationCallback](https://developer.apple.com/documentation/coremedia/cmbuffervalidationcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferValidationCallback = (CMBufferQueue, CMBuffer, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias CMBufferValidationCallback = (CMBufferQueue, CMBuffer, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [CMClockOrTimebase](https://developer.apple.com/documentation/coremedia/cmclockortimebaseref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMClockOrTimebaseRef = CMClockOrTimebase ``` |
| To | ``` typealias CMClockOrTimebase = CFTypeRef ``` |

Modified [CMClosedCaptionFormatDescription](https://developer.apple.com/documentation/coremedia/cmclosedcaptionformatdescriptionref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMClosedCaptionFormatDescription = CMFormatDescriptionRef ``` |
| To | ``` typealias CMClosedCaptionFormatDescription = CMFormatDescription ``` |

Modified [CMFormatDescriptionEqualIgnoringExtensionKeys(_: CMFormatDescription?, _: CMFormatDescription?, _: CFTypeRef?, _: CFTypeRef?) -> Bool](https://developer.apple.com/documentation/coremedia/1489465-cmformatdescriptionequalignoring)

|  | Declaration |
| --- | --- |
| From | ``` func CMFormatDescriptionEqualIgnoringExtensionKeys(_ desc1: CMFormatDescription?, _ desc2: CMFormatDescription?, _ formatDescriptionExtensionKeysToIgnore: AnyObject?, _ sampleDescriptionExtensionAtomKeysToIgnore: AnyObject?) -> Bool ``` |
| To | ``` func CMFormatDescriptionEqualIgnoringExtensionKeys(_ desc1: CMFormatDescription?, _ desc2: CMFormatDescription?, _ formatDescriptionExtensionKeysToIgnore: CFTypeRef?, _ sampleDescriptionExtensionAtomKeysToIgnore: CFTypeRef?) -> Bool ``` |

Modified [CMGetAttachment(_: CMAttachmentBearer, _: CFString, _: UnsafeMutablePointer<CMAttachmentMode>?) -> CFTypeRef?](https://developer.apple.com/documentation/coremedia/1470707-cmgetattachment)

|  | Declaration |
| --- | --- |
| From | ``` func CMGetAttachment(_ target: CMAttachmentBearer, _ key: CFString, _ attachmentModeOut: UnsafeMutablePointer<CMAttachmentMode>) -> AnyObject? ``` |
| To | ``` func CMGetAttachment(_ target: CMAttachmentBearer, _ key: CFString, _ attachmentModeOut: UnsafeMutablePointer<CMAttachmentMode>?) -> CFTypeRef? ``` |

Modified [CMMetadataCreateIdentifierForKeyAndKeySpace(_: CFAllocator?, _: CFTypeRef, _: CFString, _: UnsafeMutablePointer<CFString?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1474037-cmmetadatacreateidentifierforkey)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataCreateIdentifierForKeyAndKeySpace(_ allocator: CFAllocator?, _ key: AnyObject, _ keySpace: CFString, _ identifierOut: UnsafeMutablePointer<CFString?>) -> OSStatus ``` |
| To | ``` func CMMetadataCreateIdentifierForKeyAndKeySpace(_ allocator: CFAllocator?, _ key: CFTypeRef, _ keySpace: CFString, _ identifierOut: UnsafeMutablePointer<CFString?>) -> OSStatus ``` |

Modified [CMMetadataCreateKeyFromIdentifier(_: CFAllocator?, _: CFString, _: UnsafeMutablePointer<CFTypeRef?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1474086-cmmetadatacreatekeyfromidentifie)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataCreateKeyFromIdentifier(_ allocator: CFAllocator?, _ identifier: CFString, _ keyOut: UnsafeMutablePointer<AnyObject?>) -> OSStatus ``` |
| To | ``` func CMMetadataCreateKeyFromIdentifier(_ allocator: CFAllocator?, _ identifier: CFString, _ keyOut: UnsafeMutablePointer<CFTypeRef?>) -> OSStatus ``` |

Modified [CMMetadataFormatDescription](https://developer.apple.com/documentation/coremedia/cmmetadataformatdescriptionref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMMetadataFormatDescriptionRef = CMMetadataFormatDescription ``` |
| To | ``` typealias CMMetadataFormatDescription = CMFormatDescription ``` |

Modified [CMMuxedFormatDescription](https://developer.apple.com/documentation/coremedia/cmmuxedformatdescription)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMMuxedFormatDescriptionRef = CMMuxedFormatDescription ``` |
| To | ``` typealias CMMuxedFormatDescription = CMFormatDescription ``` |

Modified [CMSampleBufferCallBlockForEachSample(_: CMSampleBuffer, _: (CMSampleBuffer, CMItemCount) -> OSStatus) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489374-cmsamplebuffercallblockforeachsa)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferCallBlockForEachSample(_ sbuf: CMSampleBuffer, _ handler: (CMSampleBuffer, CMItemCount) -> OSStatus) -> OSStatus ``` |
| To | ``` func CMSampleBufferCallBlockForEachSample(_ sbuf: CMSampleBuffer, _ handler: @escaping (CMSampleBuffer, CMItemCount) -> OSStatus) -> OSStatus ``` |

Modified [CMSampleBufferCallForEachSample(_: CMSampleBuffer, _: (CMSampleBuffer, CMItemCount, UnsafeMutableRawPointer?) -> OSStatus, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489563-cmsamplebuffercallforeachsample)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferCallForEachSample(_ sbuf: CMSampleBuffer, _ callback: (CMSampleBuffer, CMItemCount, UnsafeMutablePointer<Void>) -> OSStatus, _ refcon: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func CMSampleBufferCallForEachSample(_ sbuf: CMSampleBuffer, _ callback: @escaping (CMSampleBuffer, CMItemCount, UnsafeMutableRawPointer?) -> OSStatus, _ refcon: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [CMSampleBufferCreate(_: CFAllocator?, _: CMBlockBuffer?, _: Bool, _: CoreMedia.CMSampleBufferMakeDataReadyCallback?, _: UnsafeMutableRawPointer?, _: CMFormatDescription?, _: CMItemCount, _: CMItemCount, _: UnsafePointer<CMSampleTimingInfo>?, _: CMItemCount, _: UnsafePointer<Int>?, _: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489723-cmsamplebuffercreate)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferCreate(_ allocator: CFAllocator?, _ dataBuffer: CMBlockBuffer?, _ dataReady: Bool, _ makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, _ makeDataReadyRefcon: UnsafeMutablePointer<Void>, _ formatDescription: CMFormatDescription?, _ numSamples: CMItemCount, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: UnsafePointer<CMSampleTimingInfo>, _ numSampleSizeEntries: CMItemCount, _ sampleSizeArray: UnsafePointer<Int>, _ sBufOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |
| To | ``` func CMSampleBufferCreate(_ allocator: CFAllocator?, _ dataBuffer: CMBlockBuffer?, _ dataReady: Bool, _ makeDataReadyCallback: CoreMedia.CMSampleBufferMakeDataReadyCallback?, _ makeDataReadyRefcon: UnsafeMutableRawPointer?, _ formatDescription: CMFormatDescription?, _ numSamples: CMItemCount, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: UnsafePointer<CMSampleTimingInfo>?, _ numSampleSizeEntries: CMItemCount, _ sampleSizeArray: UnsafePointer<Int>?, _ sBufOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |

Modified [CMSampleBufferCreateCopyWithNewTiming(_: CFAllocator?, _: CMSampleBuffer, _: CMItemCount, _: UnsafePointer<CMSampleTimingInfo>?, _: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489645-cmsamplebuffercreatecopywithnewt)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferCreateCopyWithNewTiming(_ allocator: CFAllocator?, _ originalSBuf: CMSampleBuffer, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: UnsafePointer<CMSampleTimingInfo>, _ sBufCopyOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |
| To | ``` func CMSampleBufferCreateCopyWithNewTiming(_ allocator: CFAllocator?, _ originalSBuf: CMSampleBuffer, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: UnsafePointer<CMSampleTimingInfo>?, _ sBufCopyOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |

Modified [CMSampleBufferCreateForImageBuffer(_: CFAllocator?, _: CVImageBuffer, _: Bool, _: CoreMedia.CMSampleBufferMakeDataReadyCallback?, _: UnsafeMutableRawPointer?, _: CMVideoFormatDescription, _: UnsafePointer<CMSampleTimingInfo>, _: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489414-cmsamplebuffercreateforimagebuff)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferCreateForImageBuffer(_ allocator: CFAllocator?, _ imageBuffer: CVImageBuffer, _ dataReady: Bool, _ makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, _ makeDataReadyRefcon: UnsafeMutablePointer<Void>, _ formatDescription: CMVideoFormatDescription, _ sampleTiming: UnsafePointer<CMSampleTimingInfo>, _ sBufOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |
| To | ``` func CMSampleBufferCreateForImageBuffer(_ allocator: CFAllocator?, _ imageBuffer: CVImageBuffer, _ dataReady: Bool, _ makeDataReadyCallback: CoreMedia.CMSampleBufferMakeDataReadyCallback?, _ makeDataReadyRefcon: UnsafeMutableRawPointer?, _ formatDescription: CMVideoFormatDescription, _ sampleTiming: UnsafePointer<CMSampleTimingInfo>, _ sBufOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |

Modified [CMSampleBufferCreateReady(_: CFAllocator?, _: CMBlockBuffer?, _: CMFormatDescription?, _: CMItemCount, _: CMItemCount, _: UnsafePointer<CMSampleTimingInfo>?, _: CMItemCount, _: UnsafePointer<Int>?, _: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489513-cmsamplebuffercreateready)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferCreateReady(_ allocator: CFAllocator?, _ dataBuffer: CMBlockBuffer?, _ formatDescription: CMFormatDescription?, _ numSamples: CMItemCount, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: UnsafePointer<CMSampleTimingInfo>, _ numSampleSizeEntries: CMItemCount, _ sampleSizeArray: UnsafePointer<Int>, _ sBufOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |
| To | ``` func CMSampleBufferCreateReady(_ allocator: CFAllocator?, _ dataBuffer: CMBlockBuffer?, _ formatDescription: CMFormatDescription?, _ numSamples: CMItemCount, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: UnsafePointer<CMSampleTimingInfo>?, _ numSampleSizeEntries: CMItemCount, _ sampleSizeArray: UnsafePointer<Int>?, _ sBufOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |

Modified [CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(_: CMSampleBuffer, _: UnsafeMutablePointer<Int>?, _: UnsafeMutablePointer<AudioBufferList>?, _: Int, _: CFAllocator?, _: CFAllocator?, _: UInt32, _: UnsafeMutablePointer<CMBlockBuffer?>?) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489191-cmsamplebuffergetaudiobufferlist)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(_ sbuf: CMSampleBuffer, _ bufferListSizeNeededOut: UnsafeMutablePointer<Int>, _ bufferListOut: UnsafeMutablePointer<AudioBufferList>, _ bufferListSize: Int, _ bbufStructAllocator: CFAllocator?, _ bbufMemoryAllocator: CFAllocator?, _ flags: UInt32, _ blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus ``` |
| To | ``` func CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(_ sbuf: CMSampleBuffer, _ bufferListSizeNeededOut: UnsafeMutablePointer<Int>?, _ bufferListOut: UnsafeMutablePointer<AudioBufferList>?, _ bufferListSize: Int, _ bbufStructAllocator: CFAllocator?, _ bbufMemoryAllocator: CFAllocator?, _ flags: UInt32, _ blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>?) -> OSStatus ``` |

Modified [CMSampleBufferGetAudioStreamPacketDescriptions(_: CMSampleBuffer, _: Int, _: UnsafeMutablePointer<AudioStreamPacketDescription>?, _: UnsafeMutablePointer<Int>?) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489190-cmsamplebuffergetaudiostreampack)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetAudioStreamPacketDescriptions(_ sbuf: CMSampleBuffer, _ packetDescriptionsSize: Int, _ packetDescriptionsOut: UnsafeMutablePointer<AudioStreamPacketDescription>, _ packetDescriptionsSizeNeededOut: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func CMSampleBufferGetAudioStreamPacketDescriptions(_ sbuf: CMSampleBuffer, _ packetDescriptionsSize: Int, _ packetDescriptionsOut: UnsafeMutablePointer<AudioStreamPacketDescription>?, _ packetDescriptionsSizeNeededOut: UnsafeMutablePointer<Int>?) -> OSStatus ``` |

Modified [CMSampleBufferGetAudioStreamPacketDescriptionsPtr(_: CMSampleBuffer, _: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>?>?, _: UnsafeMutablePointer<Int>?) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489564-cmsamplebuffergetaudiostreampack)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetAudioStreamPacketDescriptionsPtr(_ sbuf: CMSampleBuffer, _ packetDescriptionsPtrOut: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>>, _ packetDescriptionsSizeOut: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func CMSampleBufferGetAudioStreamPacketDescriptionsPtr(_ sbuf: CMSampleBuffer, _ packetDescriptionsPtrOut: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>?>?, _ packetDescriptionsSizeOut: UnsafeMutablePointer<Int>?) -> OSStatus ``` |

Modified [CMSampleBufferGetOutputSampleTimingInfoArray(_: CMSampleBuffer, _: CMItemCount, _: UnsafeMutablePointer<CMSampleTimingInfo>?, _: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489380-cmsamplebuffergetoutputsampletim)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetOutputSampleTimingInfoArray(_ sbuf: CMSampleBuffer, _ timingArrayEntries: CMItemCount, _ timingArrayOut: UnsafeMutablePointer<CMSampleTimingInfo>, _ timingArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>) -> OSStatus ``` |
| To | ``` func CMSampleBufferGetOutputSampleTimingInfoArray(_ sbuf: CMSampleBuffer, _ timingArrayEntries: CMItemCount, _ timingArrayOut: UnsafeMutablePointer<CMSampleTimingInfo>?, _ timingArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus ``` |

Modified [CMSampleBufferGetSampleSizeArray(_: CMSampleBuffer, _: CMItemCount, _: UnsafeMutablePointer<Int>?, _: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489295-cmsamplebuffergetsamplesizearray)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetSampleSizeArray(_ sbuf: CMSampleBuffer, _ sizeArrayEntries: CMItemCount, _ sizeArrayOut: UnsafeMutablePointer<Int>, _ sizeArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>) -> OSStatus ``` |
| To | ``` func CMSampleBufferGetSampleSizeArray(_ sbuf: CMSampleBuffer, _ sizeArrayEntries: CMItemCount, _ sizeArrayOut: UnsafeMutablePointer<Int>?, _ sizeArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus ``` |

Modified [CMSampleBufferGetSampleTimingInfoArray(_: CMSampleBuffer, _: CMItemCount, _: UnsafeMutablePointer<CMSampleTimingInfo>?, _: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489652-cmsamplebuffergetsampletiminginf)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetSampleTimingInfoArray(_ sbuf: CMSampleBuffer, _ timingArrayEntries: CMItemCount, _ timingArrayOut: UnsafeMutablePointer<CMSampleTimingInfo>, _ timingArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>) -> OSStatus ``` |
| To | ``` func CMSampleBufferGetSampleTimingInfoArray(_ sbuf: CMSampleBuffer, _ timingArrayEntries: CMItemCount, _ timingArrayOut: UnsafeMutablePointer<CMSampleTimingInfo>?, _ timingArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus ``` |

Modified [CMSampleBufferInvalidateCallback](https://developer.apple.com/documentation/coremedia/cmsamplebufferinvalidatecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMSampleBufferInvalidateCallback = (CMSampleBuffer, UInt64) -> Void ``` |
| To | ``` typealias CMSampleBufferInvalidateCallback = (CMSampleBuffer, UInt64) -> Swift.Void ``` |

Modified [CMSampleBufferInvalidateHandler](https://developer.apple.com/documentation/coremedia/cmsamplebufferinvalidatehandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMSampleBufferInvalidateHandler = (CMSampleBuffer) -> Void ``` |
| To | ``` typealias CMSampleBufferInvalidateHandler = (CMSampleBuffer) -> Swift.Void ``` |

Modified [CMSampleBufferMakeDataReadyCallback](https://developer.apple.com/documentation/coremedia/cmsamplebuffermakedatareadycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMSampleBufferMakeDataReadyCallback = (CMSampleBuffer, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias CMSampleBufferMakeDataReadyCallback = (CMSampleBuffer, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [CMSampleBufferSetInvalidateCallback(_: CMSampleBuffer, _: CoreMedia.CMSampleBufferInvalidateCallback, _: UInt64) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489773-cmsamplebuffersetinvalidatecallb)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferSetInvalidateCallback(_ sbuf: CMSampleBuffer, _ invalidateCallback: CMSampleBufferInvalidateCallback, _ invalidateRefCon: UInt64) -> OSStatus ``` |
| To | ``` func CMSampleBufferSetInvalidateCallback(_ sbuf: CMSampleBuffer, _ invalidateCallback: CoreMedia.CMSampleBufferInvalidateCallback, _ invalidateRefCon: UInt64) -> OSStatus ``` |

Modified [CMSampleBufferSetInvalidateHandler(_: CMSampleBuffer, _: CoreMedia.CMSampleBufferInvalidateHandler) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489256-cmsamplebuffersetinvalidatehandl)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferSetInvalidateHandler(_ sbuf: CMSampleBuffer, _ invalidateHandler: CMSampleBufferInvalidateHandler) -> OSStatus ``` |
| To | ``` func CMSampleBufferSetInvalidateHandler(_ sbuf: CMSampleBuffer, _ invalidateHandler: CoreMedia.CMSampleBufferInvalidateHandler) -> OSStatus ``` |

Modified [CMSetAttachment(_: CMAttachmentBearer, _: CFString, _: CFTypeRef?, _: CMAttachmentMode)](https://developer.apple.com/documentation/coremedia/1470696-cmsetattachment)

|  | Declaration |
| --- | --- |
| From | ``` func CMSetAttachment(_ target: CMAttachmentBearer, _ key: CFString, _ value: AnyObject?, _ attachmentMode: CMAttachmentMode) ``` |
| To | ``` func CMSetAttachment(_ target: CMAttachmentBearer, _ key: CFString, _ value: CFTypeRef?, _ attachmentMode: CMAttachmentMode) ``` |

Modified [CMSimpleQueueDequeue(_: CMSimpleQueue) -> UnsafeRawPointer?](https://developer.apple.com/documentation/coremedia/1489820-cmsimplequeuedequeue)

|  | Declaration |
| --- | --- |
| From | ``` func CMSimpleQueueDequeue(_ queue: CMSimpleQueue) -> UnsafePointer<Void> ``` |
| To | ``` func CMSimpleQueueDequeue(_ queue: CMSimpleQueue) -> UnsafeRawPointer? ``` |

Modified [CMSimpleQueueEnqueue(_: CMSimpleQueue, _: UnsafeRawPointer) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489315-cmsimplequeueenqueue)

|  | Declaration |
| --- | --- |
| From | ``` func CMSimpleQueueEnqueue(_ queue: CMSimpleQueue, _ element: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func CMSimpleQueueEnqueue(_ queue: CMSimpleQueue, _ element: UnsafeRawPointer) -> OSStatus ``` |

Modified [CMSimpleQueueGetHead(_: CMSimpleQueue) -> UnsafeRawPointer?](https://developer.apple.com/documentation/coremedia/1489410-cmsimplequeuegethead)

|  | Declaration |
| --- | --- |
| From | ``` func CMSimpleQueueGetHead(_ queue: CMSimpleQueue) -> UnsafePointer<Void> ``` |
| To | ``` func CMSimpleQueueGetHead(_ queue: CMSimpleQueue) -> UnsafeRawPointer? ``` |

Modified [CMTextFormatDescription](https://developer.apple.com/documentation/coremedia/cmtextformatdescription)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMTextFormatDescription = CMFormatDescriptionRef ``` |
| To | ``` typealias CMTextFormatDescription = CMFormatDescription ``` |

Modified [CMTextFormatDescriptionGetDefaultStyle(_: CMFormatDescription, _: UnsafeMutablePointer<UInt16>?, _: UnsafeMutablePointer<DarwinBoolean>?, _: UnsafeMutablePointer<DarwinBoolean>?, _: UnsafeMutablePointer<DarwinBoolean>?, _: UnsafeMutablePointer<CGFloat>?, _: UnsafeMutablePointer<CGFloat>!) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489145-cmtextformatdescriptiongetdefaul)

|  | Declaration |
| --- | --- |
| From | ``` func CMTextFormatDescriptionGetDefaultStyle(_ desc: CMFormatDescription, _ outLocalFontID: UnsafeMutablePointer<UInt16>, _ outBold: UnsafeMutablePointer<DarwinBoolean>, _ outItalic: UnsafeMutablePointer<DarwinBoolean>, _ outUnderline: UnsafeMutablePointer<DarwinBoolean>, _ outFontSize: UnsafeMutablePointer<CGFloat>, _ outColorComponents: UnsafeMutablePointer<CGFloat>) -> OSStatus ``` |
| To | ``` func CMTextFormatDescriptionGetDefaultStyle(_ desc: CMFormatDescription, _ outLocalFontID: UnsafeMutablePointer<UInt16>?, _ outBold: UnsafeMutablePointer<DarwinBoolean>?, _ outItalic: UnsafeMutablePointer<DarwinBoolean>?, _ outUnderline: UnsafeMutablePointer<DarwinBoolean>?, _ outFontSize: UnsafeMutablePointer<CGFloat>?, _ outColorComponents: UnsafeMutablePointer<CGFloat>!) -> OSStatus ``` |

Modified [CMTextFormatDescriptionGetJustification(_: CMFormatDescription, _: UnsafeMutablePointer<CMTextJustificationValue>?, _: UnsafeMutablePointer<CMTextJustificationValue>?) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489232-cmtextformatdescriptiongetjustif)

|  | Declaration |
| --- | --- |
| From | ``` func CMTextFormatDescriptionGetJustification(_ desc: CMFormatDescription, _ outHorizontalJust: UnsafeMutablePointer<CMTextJustificationValue>, _ outVerticalJust: UnsafeMutablePointer<CMTextJustificationValue>) -> OSStatus ``` |
| To | ``` func CMTextFormatDescriptionGetJustification(_ desc: CMFormatDescription, _ outHorizontalJust: UnsafeMutablePointer<CMTextJustificationValue>?, _ outVerticalJust: UnsafeMutablePointer<CMTextJustificationValue>?) -> OSStatus ``` |

Modified [CMTIME_HAS_BEEN_ROUNDED(_: CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/1489530-cmtime_has_been_rounded)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func CMTIME_HAS_BEEN_ROUNDED(_ time: CMTime) -> Bool ``` |
| To | ``` func CMTIME_HAS_BEEN_ROUNDED(_ time: CMTime) -> Bool ``` |

Modified [CMTIME_IS_INDEFINITE(_: CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/1489754-cmtime_is_indefinite)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func CMTIME_IS_INDEFINITE(_ time: CMTime) -> Bool ``` |
| To | ``` func CMTIME_IS_INDEFINITE(_ time: CMTime) -> Bool ``` |

Modified [CMTIME_IS_INVALID(_: CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/1489272-cmtime_is_invalid)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func CMTIME_IS_INVALID(_ time: CMTime) -> Bool ``` |
| To | ``` func CMTIME_IS_INVALID(_ time: CMTime) -> Bool ``` |

Modified [CMTIME_IS_NEGATIVEINFINITY(_: CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/1489459-cmtime_is_negativeinfinity)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func CMTIME_IS_NEGATIVEINFINITY(_ time: CMTime) -> Bool ``` |
| To | ``` func CMTIME_IS_NEGATIVEINFINITY(_ time: CMTime) -> Bool ``` |

Modified [CMTIME_IS_NUMERIC(_: CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/1489401-cmtime_is_numeric)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func CMTIME_IS_NUMERIC(_ time: CMTime) -> Bool ``` |
| To | ``` func CMTIME_IS_NUMERIC(_ time: CMTime) -> Bool ``` |

Modified [CMTIME_IS_POSITIVEINFINITY(_: CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/1489320-cmtime_is_positiveinfinity)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func CMTIME_IS_POSITIVEINFINITY(_ time: CMTime) -> Bool ``` |
| To | ``` func CMTIME_IS_POSITIVEINFINITY(_ time: CMTime) -> Bool ``` |

Modified [CMTIME_IS_VALID(_: CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/1489280-cmtime_is_valid)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func CMTIME_IS_VALID(_ time: CMTime) -> Bool ``` |
| To | ``` func CMTIME_IS_VALID(_ time: CMTime) -> Bool ``` |

Modified [CMTimebaseAddTimerDispatchSource(_: CMTimebase, _: DispatchSource) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489429-cmtimebaseaddtimerdispatchsource)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseAddTimerDispatchSource(_ timebase: CMTimebase, _ timerSource: dispatch_source_t) -> OSStatus ``` |
| To | ``` func CMTimebaseAddTimerDispatchSource(_ timebase: CMTimebase, _ timerSource: DispatchSource) -> OSStatus ``` |

Modified [CMTimebaseRemoveTimerDispatchSource(_: CMTimebase, _: DispatchSource) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489198-cmtimebaseremovetimerdispatchsou)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseRemoveTimerDispatchSource(_ timebase: CMTimebase, _ timerSource: dispatch_source_t) -> OSStatus ``` |
| To | ``` func CMTimebaseRemoveTimerDispatchSource(_ timebase: CMTimebase, _ timerSource: DispatchSource) -> OSStatus ``` |

Modified [CMTimebaseSetTimerDispatchSourceNextFireTime(_: CMTimebase, _: DispatchSource, _: CMTime, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489489-cmtimebasesettimerdispatchsource)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseSetTimerDispatchSourceNextFireTime(_ timebase: CMTimebase, _ timerSource: dispatch_source_t, _ fireTime: CMTime, _ flags: UInt32) -> OSStatus ``` |
| To | ``` func CMTimebaseSetTimerDispatchSourceNextFireTime(_ timebase: CMTimebase, _ timerSource: DispatchSource, _ fireTime: CMTime, _ flags: UInt32) -> OSStatus ``` |

Modified [CMTimebaseSetTimerDispatchSourceToFireImmediately(_: CMTimebase, _: DispatchSource) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489552-cmtimebasesettimerdispatchsource)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseSetTimerDispatchSourceToFireImmediately(_ timebase: CMTimebase, _ timerSource: dispatch_source_t) -> OSStatus ``` |
| To | ``` func CMTimebaseSetTimerDispatchSourceToFireImmediately(_ timebase: CMTimebase, _ timerSource: DispatchSource) -> OSStatus ``` |

Modified [CMTimeCodeFormatDescription](https://developer.apple.com/documentation/coremedia/cmtimecodeformatdescriptionref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMTimeCodeFormatDescriptionRef = CMTimeCodeFormatDescription ``` |
| To | ``` typealias CMTimeCodeFormatDescription = CMFormatDescription ``` |

Modified [CMTIMERANGE_IS_EMPTY(_: CMTimeRange) -> Bool](https://developer.apple.com/documentation/coremedia/1489251-cmtimerange_is_empty)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func CMTIMERANGE_IS_EMPTY(_ range: CMTimeRange) -> Bool ``` |
| To | ``` func CMTIMERANGE_IS_EMPTY(_ range: CMTimeRange) -> Bool ``` |

Modified [CMTIMERANGE_IS_INDEFINITE(_: CMTimeRange) -> Bool](https://developer.apple.com/documentation/coremedia/1489261-cmtimerange_is_indefinite)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func CMTIMERANGE_IS_INDEFINITE(_ range: CMTimeRange) -> Bool ``` |
| To | ``` func CMTIMERANGE_IS_INDEFINITE(_ range: CMTimeRange) -> Bool ``` |

Modified [CMTIMERANGE_IS_INVALID(_: CMTimeRange) -> Bool](https://developer.apple.com/documentation/coremedia/1489472-cmtimerange_is_invalid)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func CMTIMERANGE_IS_INVALID(_ range: CMTimeRange) -> Bool ``` |
| To | ``` func CMTIMERANGE_IS_INVALID(_ range: CMTimeRange) -> Bool ``` |

Modified [CMTIMERANGE_IS_VALID(_: CMTimeRange) -> Bool](https://developer.apple.com/documentation/coremedia/1489373-cmtimerange_is_valid)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func CMTIMERANGE_IS_VALID(_ range: CMTimeRange) -> Bool ``` |
| To | ``` func CMTIMERANGE_IS_VALID(_ range: CMTimeRange) -> Bool ``` |

Modified [CMVideoFormatDescription](https://developer.apple.com/documentation/coremedia/cmvideoformatdescriptionref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMVideoFormatDescriptionRef = CMVideoFormatDescription ``` |
| To | ``` typealias CMVideoFormatDescription = CMFormatDescription ``` |

Modified [CMVideoFormatDescriptionGetH264ParameterSetAtIndex(_: CMFormatDescription, _: Int, _: UnsafeMutablePointer<UnsafePointer<UInt8>?>?, _: UnsafeMutablePointer<Int>?, _: UnsafeMutablePointer<Int>?, _: UnsafeMutablePointer<Int32>?) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489529-cmvideoformatdescriptiongeth264p)

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionGetH264ParameterSetAtIndex(_ videoDesc: CMFormatDescription, _ parameterSetIndex: Int, _ parameterSetPointerOut: UnsafeMutablePointer<UnsafePointer<UInt8>>, _ parameterSetSizeOut: UnsafeMutablePointer<Int>, _ parameterSetCountOut: UnsafeMutablePointer<Int>, _ NALUnitHeaderLengthOut: UnsafeMutablePointer<Int32>) -> OSStatus ``` |
| To | ``` func CMVideoFormatDescriptionGetH264ParameterSetAtIndex(_ videoDesc: CMFormatDescription, _ parameterSetIndex: Int, _ parameterSetPointerOut: UnsafeMutablePointer<UnsafePointer<UInt8>?>?, _ parameterSetSizeOut: UnsafeMutablePointer<Int>?, _ parameterSetCountOut: UnsafeMutablePointer<Int>?, _ NALUnitHeaderLengthOut: UnsafeMutablePointer<Int32>?) -> OSStatus ``` |

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
