---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/CoreAudio.html
archived_at: '2026-07-18T02:51:04.948153Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# CoreAudio Changes for Swift

### CoreAudio

Removed [AudioBuffer.init(mNumberChannels: UInt32, mDataByteSize: UInt32, mData: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/coreaudio/audiobuffer/1421787-init)Removed [AudioChannelFlags.AllOff](https://developer.apple.com/documentation/coreaudio/audiochannelflags/kaudiochannelflags_alloff)Removed [AudioTimeStampFlags.NothingValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/kaudiotimestampnothingvalid)Removed [SMPTETimeFlags.Unknown](https://developer.apple.com/documentation/coreaudio/smptetimeflags/ksmptetimeunknown)Added [AudioBuffer.init(mNumberChannels: UInt32, mDataByteSize: UInt32, mData: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/coreaudio/audiobuffer/1421787-init)Added [UnsafeMutableAudioBufferListPointer.init(_: UnsafeMutablePointer<AudioBufferList>?)](https://developer.apple.com/documentation/coreaudio/unsafemutableaudiobufferlistpointer/1690319-init)Added UnsafeMutableAudioBufferListPointer.subscript(_: Range<Int>) -> MutableRandomAccessSlice<UnsafeMutableAudioBufferListPointer>Added [kAudioAggregateDeviceClockDeviceKey](https://developer.apple.com/documentation/coreaudio/kaudioaggregatedeviceclockdevicekey)Added [kAudioAggregateDevicePropertyClockDevice](https://developer.apple.com/documentation/coreaudio/1545875-anonymous/kaudioaggregatedevicepropertyclockdevice)Added [kAudioBoxPropertyClockDeviceList](https://developer.apple.com/documentation/coreaudio/1494522-anonymous/kaudioboxpropertyclockdevicelist)Added [kAudioClockDeviceClassID](https://developer.apple.com/documentation/coreaudio/1646515-anonymous/kaudioclockdeviceclassid)Added [kAudioClockDevicePropertyAvailableNominalSampleRates](https://developer.apple.com/documentation/coreaudio/kaudioclockdevicepropertyavailablenominalsamplerates)Added [kAudioClockDevicePropertyClockDomain](https://developer.apple.com/documentation/coreaudio/kaudioclockdevicepropertyclockdomain)Added [kAudioClockDevicePropertyControlList](https://developer.apple.com/documentation/coreaudio/kaudioclockdevicepropertycontrollist)Added [kAudioClockDevicePropertyDeviceIsAlive](https://developer.apple.com/documentation/coreaudio/1646514-anonymous/kaudioclockdevicepropertydeviceisalive)Added [kAudioClockDevicePropertyDeviceIsRunning](https://developer.apple.com/documentation/coreaudio/1646514-anonymous/kaudioclockdevicepropertydeviceisrunning)Added [kAudioClockDevicePropertyDeviceUID](https://developer.apple.com/documentation/coreaudio/kaudioclockdevicepropertydeviceuid)Added [kAudioClockDevicePropertyLatency](https://developer.apple.com/documentation/coreaudio/1646514-anonymous/kaudioclockdevicepropertylatency)Added [kAudioClockDevicePropertyNominalSampleRate](https://developer.apple.com/documentation/coreaudio/1646514-anonymous/kaudioclockdevicepropertynominalsamplerate)Added [kAudioClockDevicePropertyTransportType](https://developer.apple.com/documentation/coreaudio/kaudioclockdevicepropertytransporttype)Added [kAudioDevicePropertyClockDevice](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyclockdevice)Added [kAudioHardwarePropertyClockDeviceList](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertyclockdevicelist)Added [kAudioHardwarePropertyTranslateUIDToClockDevice](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertytranslateuidtoclockdevice)Added [kAudioPlugInPropertyClockDeviceList](https://developer.apple.com/documentation/coreaudio/kaudiopluginpropertyclockdevicelist)Added [kAudioPlugInPropertyTranslateUIDToClockDevice](https://developer.apple.com/documentation/coreaudio/kaudiopluginpropertytranslateuidtoclockdevice)Added [UnsafeMutableAudioBufferListPointer.Index](https://developer.apple.com/documentation/coreaudio/unsafemutableaudiobufferlistpointer/index)Added [UnsafeMutableAudioBufferListPointer.Indices](https://developer.apple.com/documentation/coreaudio/unsafemutableaudiobufferlistpointer/indices)Modified [AudioBuffer [struct]](https://developer.apple.com/documentation/coreaudio/audiobuffer)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioBuffer {     var mNumberChannels: UInt32     var mDataByteSize: UInt32     var mData: UnsafeMutablePointer<Void>     init()     init(mNumberChannels mNumberChannels: UInt32, mDataByteSize mDataByteSize: UInt32, mData mData: UnsafeMutablePointer<Void>) } extension AudioBuffer {     init<Element>(_ typedBuffer: UnsafeMutableBufferPointer<Element>, numberOfChannels numberOfChannels: Int) } extension AudioBuffer {     init<Element>(_ typedBuffer: UnsafeMutableBufferPointer<Element>, numberOfChannels numberOfChannels: Int) } ``` |
| To | ``` struct AudioBuffer {     var mNumberChannels: UInt32     var mDataByteSize: UInt32     var mData: UnsafeMutableRawPointer?     init()     init(mNumberChannels mNumberChannels: UInt32, mDataByteSize mDataByteSize: UInt32, mData mData: UnsafeMutableRawPointer?)     init<Element>(_ typedBuffer: UnsafeMutableBufferPointer<Element>, numberOfChannels numberOfChannels: Int) } extension AudioBuffer {     init<Element>(_ typedBuffer: UnsafeMutableBufferPointer<Element>, numberOfChannels numberOfChannels: Int) } ``` |

Modified [AudioBuffer.mData](https://developer.apple.com/documentation/coreaudio/audiobuffer/1422625-mdata)

|  | Declaration |
| --- | --- |
| From | ``` var mData: UnsafeMutablePointer<Void> ``` |
| To | ``` var mData: UnsafeMutableRawPointer? ``` |

Modified [AudioBufferList [struct]](https://developer.apple.com/documentation/coreaudio/audiobufferlist)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioBufferList {     var mNumberBuffers: UInt32     var mBuffers: (AudioBuffer)     init()     init(mNumberBuffers mNumberBuffers: UInt32, mBuffers mBuffers: (AudioBuffer)) } extension AudioBufferList {     static func sizeInBytes(maximumBuffers maximumBuffers: Int) -> Int     static func allocate(maximumBuffers maximumBuffers: Int) -> UnsafeMutableAudioBufferListPointer } extension AudioBufferList {     static func sizeInBytes(maximumBuffers maximumBuffers: Int) -> Int     static func allocate(maximumBuffers maximumBuffers: Int) -> UnsafeMutableAudioBufferListPointer } ``` |
| To | ``` struct AudioBufferList {     var mNumberBuffers: UInt32     var mBuffers: (AudioBuffer)     init()     init(mNumberBuffers mNumberBuffers: UInt32, mBuffers mBuffers: (AudioBuffer))     static func sizeInBytes(maximumBuffers maximumBuffers: Int) -> Int     static func allocate(maximumBuffers maximumBuffers: Int) -> UnsafeMutableAudioBufferListPointer } extension AudioBufferList {     static func sizeInBytes(maximumBuffers maximumBuffers: Int) -> Int     static func allocate(maximumBuffers maximumBuffers: Int) -> UnsafeMutableAudioBufferListPointer } ``` |

Modified [AudioChannelBitmap [struct]](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AudioChannelBitmap : OptionSetType {     init(rawValue rawValue: UInt32)     static var Bit_Left: AudioChannelBitmap { get }     static var Bit_Right: AudioChannelBitmap { get }     static var Bit_Center: AudioChannelBitmap { get }     static var Bit_LFEScreen: AudioChannelBitmap { get }     static var Bit_LeftSurround: AudioChannelBitmap { get }     static var Bit_RightSurround: AudioChannelBitmap { get }     static var Bit_LeftCenter: AudioChannelBitmap { get }     static var Bit_RightCenter: AudioChannelBitmap { get }     static var Bit_CenterSurround: AudioChannelBitmap { get }     static var Bit_LeftSurroundDirect: AudioChannelBitmap { get }     static var Bit_RightSurroundDirect: AudioChannelBitmap { get }     static var Bit_TopCenterSurround: AudioChannelBitmap { get }     static var Bit_VerticalHeightLeft: AudioChannelBitmap { get }     static var Bit_VerticalHeightCenter: AudioChannelBitmap { get }     static var Bit_VerticalHeightRight: AudioChannelBitmap { get }     static var Bit_TopBackLeft: AudioChannelBitmap { get }     static var Bit_TopBackCenter: AudioChannelBitmap { get }     static var Bit_TopBackRight: AudioChannelBitmap { get } } ``` | OptionSetType |
| To | ``` struct AudioChannelBitmap : OptionSet {     init(rawValue rawValue: UInt32)     static var bit_Left: AudioChannelBitmap { get }     static var bit_Right: AudioChannelBitmap { get }     static var bit_Center: AudioChannelBitmap { get }     static var bit_LFEScreen: AudioChannelBitmap { get }     static var bit_LeftSurround: AudioChannelBitmap { get }     static var bit_RightSurround: AudioChannelBitmap { get }     static var bit_LeftCenter: AudioChannelBitmap { get }     static var bit_RightCenter: AudioChannelBitmap { get }     static var bit_CenterSurround: AudioChannelBitmap { get }     static var bit_LeftSurroundDirect: AudioChannelBitmap { get }     static var bit_RightSurroundDirect: AudioChannelBitmap { get }     static var bit_TopCenterSurround: AudioChannelBitmap { get }     static var bit_VerticalHeightLeft: AudioChannelBitmap { get }     static var bit_VerticalHeightCenter: AudioChannelBitmap { get }     static var bit_VerticalHeightRight: AudioChannelBitmap { get }     static var bit_TopBackLeft: AudioChannelBitmap { get }     static var bit_TopBackCenter: AudioChannelBitmap { get }     static var bit_TopBackRight: AudioChannelBitmap { get }     func intersect(_ other: AudioChannelBitmap) -> AudioChannelBitmap     func exclusiveOr(_ other: AudioChannelBitmap) -> AudioChannelBitmap     mutating func unionInPlace(_ other: AudioChannelBitmap)     mutating func intersectInPlace(_ other: AudioChannelBitmap)     mutating func exclusiveOrInPlace(_ other: AudioChannelBitmap)     func isSubsetOf(_ other: AudioChannelBitmap) -> Bool     func isDisjointWith(_ other: AudioChannelBitmap) -> Bool     func isSupersetOf(_ other: AudioChannelBitmap) -> Bool     mutating func subtractInPlace(_ other: AudioChannelBitmap)     func isStrictSupersetOf(_ other: AudioChannelBitmap) -> Bool     func isStrictSubsetOf(_ other: AudioChannelBitmap) -> Bool } extension AudioChannelBitmap {     func union(_ other: AudioChannelBitmap) -> AudioChannelBitmap     func intersection(_ other: AudioChannelBitmap) -> AudioChannelBitmap     func symmetricDifference(_ other: AudioChannelBitmap) -> AudioChannelBitmap } extension AudioChannelBitmap {     func contains(_ member: AudioChannelBitmap) -> Bool     mutating func insert(_ newMember: AudioChannelBitmap) -> (inserted: Bool, memberAfterInsert: AudioChannelBitmap)     mutating func remove(_ member: AudioChannelBitmap) -> AudioChannelBitmap?     mutating func update(with newMember: AudioChannelBitmap) -> AudioChannelBitmap? } extension AudioChannelBitmap {     convenience init()     mutating func formUnion(_ other: AudioChannelBitmap)     mutating func formIntersection(_ other: AudioChannelBitmap)     mutating func formSymmetricDifference(_ other: AudioChannelBitmap) } extension AudioChannelBitmap {     convenience init<S : Sequence where S.Iterator.Element == AudioChannelBitmap>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AudioChannelBitmap...)     mutating func subtract(_ other: AudioChannelBitmap)     func isSubset(of other: AudioChannelBitmap) -> Bool     func isSuperset(of other: AudioChannelBitmap) -> Bool     func isDisjoint(with other: AudioChannelBitmap) -> Bool     func subtracting(_ other: AudioChannelBitmap) -> AudioChannelBitmap     var isEmpty: Bool { get }     func isStrictSuperset(of other: AudioChannelBitmap) -> Bool     func isStrictSubset(of other: AudioChannelBitmap) -> Bool } ``` | OptionSet |

Modified [AudioChannelBitmap.bit_Center](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422558-bit_center)

|  | Declaration |
| --- | --- |
| From | ``` static var Bit_Center: AudioChannelBitmap { get } ``` |
| To | ``` static var bit_Center: AudioChannelBitmap { get } ``` |

Modified [AudioChannelBitmap.bit_CenterSurround](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1421862-bit_centersurround)

|  | Declaration |
| --- | --- |
| From | ``` static var Bit_CenterSurround: AudioChannelBitmap { get } ``` |
| To | ``` static var bit_CenterSurround: AudioChannelBitmap { get } ``` |

Modified [AudioChannelBitmap.bit_Left](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422633-bit_left)

|  | Declaration |
| --- | --- |
| From | ``` static var Bit_Left: AudioChannelBitmap { get } ``` |
| To | ``` static var bit_Left: AudioChannelBitmap { get } ``` |

Modified [AudioChannelBitmap.bit_LeftCenter](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1421656-bit_leftcenter)

|  | Declaration |
| --- | --- |
| From | ``` static var Bit_LeftCenter: AudioChannelBitmap { get } ``` |
| To | ``` static var bit_LeftCenter: AudioChannelBitmap { get } ``` |

Modified [AudioChannelBitmap.bit_LeftSurround](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422177-bit_leftsurround)

|  | Declaration |
| --- | --- |
| From | ``` static var Bit_LeftSurround: AudioChannelBitmap { get } ``` |
| To | ``` static var bit_LeftSurround: AudioChannelBitmap { get } ``` |

Modified [AudioChannelBitmap.bit_LeftSurroundDirect](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/kaudiochannelbit_leftsurrounddirect)

|  | Declaration |
| --- | --- |
| From | ``` static var Bit_LeftSurroundDirect: AudioChannelBitmap { get } ``` |
| To | ``` static var bit_LeftSurroundDirect: AudioChannelBitmap { get } ``` |

Modified [AudioChannelBitmap.bit_LFEScreen](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422510-bit_lfescreen)

|  | Declaration |
| --- | --- |
| From | ``` static var Bit_LFEScreen: AudioChannelBitmap { get } ``` |
| To | ``` static var bit_LFEScreen: AudioChannelBitmap { get } ``` |

Modified [AudioChannelBitmap.bit_Right](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1421518-bit_right)

|  | Declaration |
| --- | --- |
| From | ``` static var Bit_Right: AudioChannelBitmap { get } ``` |
| To | ``` static var bit_Right: AudioChannelBitmap { get } ``` |

Modified [AudioChannelBitmap.bit_RightCenter](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422165-bit_rightcenter)

|  | Declaration |
| --- | --- |
| From | ``` static var Bit_RightCenter: AudioChannelBitmap { get } ``` |
| To | ``` static var bit_RightCenter: AudioChannelBitmap { get } ``` |

Modified [AudioChannelBitmap.bit_RightSurround](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1421938-bit_rightsurround)

|  | Declaration |
| --- | --- |
| From | ``` static var Bit_RightSurround: AudioChannelBitmap { get } ``` |
| To | ``` static var bit_RightSurround: AudioChannelBitmap { get } ``` |

Modified [AudioChannelBitmap.bit_RightSurroundDirect](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/kaudiochannelbit_rightsurrounddirect)

|  | Declaration |
| --- | --- |
| From | ``` static var Bit_RightSurroundDirect: AudioChannelBitmap { get } ``` |
| To | ``` static var bit_RightSurroundDirect: AudioChannelBitmap { get } ``` |

Modified [AudioChannelBitmap.bit_TopBackCenter](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/kaudiochannelbit_topbackcenter)

|  | Declaration |
| --- | --- |
| From | ``` static var Bit_TopBackCenter: AudioChannelBitmap { get } ``` |
| To | ``` static var bit_TopBackCenter: AudioChannelBitmap { get } ``` |

Modified [AudioChannelBitmap.bit_TopBackLeft](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1423190-bit_topbackleft)

|  | Declaration |
| --- | --- |
| From | ``` static var Bit_TopBackLeft: AudioChannelBitmap { get } ``` |
| To | ``` static var bit_TopBackLeft: AudioChannelBitmap { get } ``` |

Modified [AudioChannelBitmap.bit_TopBackRight](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1423004-bit_topbackright)

|  | Declaration |
| --- | --- |
| From | ``` static var Bit_TopBackRight: AudioChannelBitmap { get } ``` |
| To | ``` static var bit_TopBackRight: AudioChannelBitmap { get } ``` |

Modified [AudioChannelBitmap.bit_TopCenterSurround](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422248-bit_topcentersurround)

|  | Declaration |
| --- | --- |
| From | ``` static var Bit_TopCenterSurround: AudioChannelBitmap { get } ``` |
| To | ``` static var bit_TopCenterSurround: AudioChannelBitmap { get } ``` |

Modified [AudioChannelBitmap.bit_VerticalHeightCenter](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422161-bit_verticalheightcenter)

|  | Declaration |
| --- | --- |
| From | ``` static var Bit_VerticalHeightCenter: AudioChannelBitmap { get } ``` |
| To | ``` static var bit_VerticalHeightCenter: AudioChannelBitmap { get } ``` |

Modified [AudioChannelBitmap.bit_VerticalHeightLeft](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/kaudiochannelbit_verticalheightleft)

|  | Declaration |
| --- | --- |
| From | ``` static var Bit_VerticalHeightLeft: AudioChannelBitmap { get } ``` |
| To | ``` static var bit_VerticalHeightLeft: AudioChannelBitmap { get } ``` |

Modified [AudioChannelBitmap.bit_VerticalHeightRight](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/kaudiochannelbit_verticalheightright)

|  | Declaration |
| --- | --- |
| From | ``` static var Bit_VerticalHeightRight: AudioChannelBitmap { get } ``` |
| To | ``` static var bit_VerticalHeightRight: AudioChannelBitmap { get } ``` |

Modified [AudioChannelCoordinateIndex [enum]](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex)

|  | Declaration |
| --- | --- |
| From | ``` enum AudioChannelCoordinateIndex : UInt32 {     case Coordinates_LeftRight     case Coordinates_BackFront     case Coordinates_DownUp     static var Coordinates_Azimuth: AudioChannelCoordinateIndex { get }     static var Coordinates_Elevation: AudioChannelCoordinateIndex { get }     static var Coordinates_Distance: AudioChannelCoordinateIndex { get } } ``` |
| To | ``` enum AudioChannelCoordinateIndex : UInt32 {     case coordinates_LeftRight     case coordinates_BackFront     case coordinates_DownUp     static var coordinates_Azimuth: AudioChannelCoordinateIndex { get }     static var coordinates_Elevation: AudioChannelCoordinateIndex { get }     static var coordinates_Distance: AudioChannelCoordinateIndex { get } } ``` |

Modified [AudioChannelCoordinateIndex.coordinates_Azimuth](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex/kaudiochannelcoordinates_azimuth)

|  | Declaration |
| --- | --- |
| From | ``` static var Coordinates_Azimuth: AudioChannelCoordinateIndex { get } ``` |
| To | ``` static var coordinates_Azimuth: AudioChannelCoordinateIndex { get } ``` |

Modified [AudioChannelCoordinateIndex.coordinates_BackFront](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex/coordinates_backfront)

|  | Declaration |
| --- | --- |
| From | ``` case Coordinates_BackFront ``` |
| To | ``` case coordinates_BackFront ``` |

Modified [AudioChannelCoordinateIndex.coordinates_Distance](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex/kaudiochannelcoordinates_distance)

|  | Declaration |
| --- | --- |
| From | ``` static var Coordinates_Distance: AudioChannelCoordinateIndex { get } ``` |
| To | ``` static var coordinates_Distance: AudioChannelCoordinateIndex { get } ``` |

Modified [AudioChannelCoordinateIndex.coordinates_DownUp](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex/coordinates_downup)

|  | Declaration |
| --- | --- |
| From | ``` case Coordinates_DownUp ``` |
| To | ``` case coordinates_DownUp ``` |

Modified [AudioChannelCoordinateIndex.coordinates_Elevation](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex/kaudiochannelcoordinates_elevation)

|  | Declaration |
| --- | --- |
| From | ``` static var Coordinates_Elevation: AudioChannelCoordinateIndex { get } ``` |
| To | ``` static var coordinates_Elevation: AudioChannelCoordinateIndex { get } ``` |

Modified [AudioChannelCoordinateIndex.coordinates_LeftRight](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex/kaudiochannelcoordinates_leftright)

|  | Declaration |
| --- | --- |
| From | ``` case Coordinates_LeftRight ``` |
| To | ``` case coordinates_LeftRight ``` |

Modified [AudioChannelFlags [struct]](https://developer.apple.com/documentation/coreaudio/audiochannelflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AudioChannelFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var AllOff: AudioChannelFlags { get }     static var RectangularCoordinates: AudioChannelFlags { get }     static var SphericalCoordinates: AudioChannelFlags { get }     static var Meters: AudioChannelFlags { get } } ``` | OptionSetType |
| To | ``` struct AudioChannelFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var allOff: AudioChannelFlags { get }     static var rectangularCoordinates: AudioChannelFlags { get }     static var sphericalCoordinates: AudioChannelFlags { get }     static var meters: AudioChannelFlags { get }     func intersect(_ other: AudioChannelFlags) -> AudioChannelFlags     func exclusiveOr(_ other: AudioChannelFlags) -> AudioChannelFlags     mutating func unionInPlace(_ other: AudioChannelFlags)     mutating func intersectInPlace(_ other: AudioChannelFlags)     mutating func exclusiveOrInPlace(_ other: AudioChannelFlags)     func isSubsetOf(_ other: AudioChannelFlags) -> Bool     func isDisjointWith(_ other: AudioChannelFlags) -> Bool     func isSupersetOf(_ other: AudioChannelFlags) -> Bool     mutating func subtractInPlace(_ other: AudioChannelFlags)     func isStrictSupersetOf(_ other: AudioChannelFlags) -> Bool     func isStrictSubsetOf(_ other: AudioChannelFlags) -> Bool } extension AudioChannelFlags {     func union(_ other: AudioChannelFlags) -> AudioChannelFlags     func intersection(_ other: AudioChannelFlags) -> AudioChannelFlags     func symmetricDifference(_ other: AudioChannelFlags) -> AudioChannelFlags } extension AudioChannelFlags {     func contains(_ member: AudioChannelFlags) -> Bool     mutating func insert(_ newMember: AudioChannelFlags) -> (inserted: Bool, memberAfterInsert: AudioChannelFlags)     mutating func remove(_ member: AudioChannelFlags) -> AudioChannelFlags?     mutating func update(with newMember: AudioChannelFlags) -> AudioChannelFlags? } extension AudioChannelFlags {     convenience init()     mutating func formUnion(_ other: AudioChannelFlags)     mutating func formIntersection(_ other: AudioChannelFlags)     mutating func formSymmetricDifference(_ other: AudioChannelFlags) } extension AudioChannelFlags {     convenience init<S : Sequence where S.Iterator.Element == AudioChannelFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AudioChannelFlags...)     mutating func subtract(_ other: AudioChannelFlags)     func isSubset(of other: AudioChannelFlags) -> Bool     func isSuperset(of other: AudioChannelFlags) -> Bool     func isDisjoint(with other: AudioChannelFlags) -> Bool     func subtracting(_ other: AudioChannelFlags) -> AudioChannelFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: AudioChannelFlags) -> Bool     func isStrictSubset(of other: AudioChannelFlags) -> Bool } ``` | OptionSet |

Modified [AudioChannelFlags.meters](https://developer.apple.com/documentation/coreaudio/audiochannelflags/1422914-meters)

|  | Declaration |
| --- | --- |
| From | ``` static var Meters: AudioChannelFlags { get } ``` |
| To | ``` static var meters: AudioChannelFlags { get } ``` |

Modified [AudioChannelFlags.rectangularCoordinates](https://developer.apple.com/documentation/coreaudio/audiochannelflags/kaudiochannelflags_rectangularcoordinates)

|  | Declaration |
| --- | --- |
| From | ``` static var RectangularCoordinates: AudioChannelFlags { get } ``` |
| To | ``` static var rectangularCoordinates: AudioChannelFlags { get } ``` |

Modified [AudioChannelFlags.sphericalCoordinates](https://developer.apple.com/documentation/coreaudio/audiochannelflags/1421586-sphericalcoordinates)

|  | Declaration |
| --- | --- |
| From | ``` static var SphericalCoordinates: AudioChannelFlags { get } ``` |
| To | ``` static var sphericalCoordinates: AudioChannelFlags { get } ``` |

Modified [AudioHardwareIOProcStreamUsage [struct]](https://developer.apple.com/documentation/coreaudio/audiohardwareioprocstreamusage)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioHardwareIOProcStreamUsage {     var mIOProc: UnsafeMutablePointer<Void>     var mNumberStreams: UInt32     var mStreamIsOn: (UInt32) } ``` |
| To | ``` struct AudioHardwareIOProcStreamUsage {     var mIOProc: UnsafeMutableRawPointer     var mNumberStreams: UInt32     var mStreamIsOn: (UInt32) } ``` |

Modified [AudioHardwareIOProcStreamUsage.mIOProc](https://developer.apple.com/documentation/coreaudio/audiohardwareioprocstreamusage/1421989-mioproc)

|  | Declaration |
| --- | --- |
| From | ``` var mIOProc: UnsafeMutablePointer<Void> ``` |
| To | ``` var mIOProc: UnsafeMutableRawPointer ``` |

Modified [AudioHardwarePowerHint [enum]](https://developer.apple.com/documentation/coreaudio/audiohardwarepowerhint)

|  | Declaration |
| --- | --- |
| From | ``` enum AudioHardwarePowerHint : UInt32 {     case None     case FavorSavingPower } ``` |
| To | ``` enum AudioHardwarePowerHint : UInt32 {     case none     case favorSavingPower } ``` |

Modified [AudioHardwarePowerHint.favorSavingPower](https://developer.apple.com/documentation/coreaudio/audiohardwarepowerhint/kaudiohardwarepowerhintfavorsavingpower)

|  | Declaration |
| --- | --- |
| From | ``` case FavorSavingPower ``` |
| To | ``` case favorSavingPower ``` |

Modified [AudioHardwarePowerHint.none](https://developer.apple.com/documentation/coreaudio/audiohardwarepowerhint/kaudiohardwarepowerhintnone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [AudioLevelControlTransferFunction [enum]](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction)

|  | Declaration |
| --- | --- |
| From | ``` enum AudioLevelControlTransferFunction : UInt32 {     case TranferFunctionLinear     case TranferFunction1Over3     case TranferFunction1Over2     case TranferFunction3Over4     case TranferFunction3Over2     case TranferFunction2Over1     case TranferFunction3Over1     case TranferFunction4Over1     case TranferFunction5Over1     case TranferFunction6Over1     case TranferFunction7Over1     case TranferFunction8Over1     case TranferFunction9Over1     case TranferFunction10Over1     case TranferFunction11Over1     case TranferFunction12Over1 } ``` |
| To | ``` enum AudioLevelControlTransferFunction : UInt32 {     case tranferFunctionLinear     case tranferFunction1Over3     case tranferFunction1Over2     case tranferFunction3Over4     case tranferFunction3Over2     case tranferFunction2Over1     case tranferFunction3Over1     case tranferFunction4Over1     case tranferFunction5Over1     case tranferFunction6Over1     case tranferFunction7Over1     case tranferFunction8Over1     case tranferFunction9Over1     case tranferFunction10Over1     case tranferFunction11Over1     case tranferFunction12Over1 } ``` |

Modified [AudioLevelControlTransferFunction.tranferFunction10Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction10over1)

|  | Declaration |
| --- | --- |
| From | ``` case TranferFunction10Over1 ``` |
| To | ``` case tranferFunction10Over1 ``` |

Modified [AudioLevelControlTransferFunction.tranferFunction11Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction11over1)

|  | Declaration |
| --- | --- |
| From | ``` case TranferFunction11Over1 ``` |
| To | ``` case tranferFunction11Over1 ``` |

Modified [AudioLevelControlTransferFunction.tranferFunction12Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction12over1)

|  | Declaration |
| --- | --- |
| From | ``` case TranferFunction12Over1 ``` |
| To | ``` case tranferFunction12Over1 ``` |

Modified [AudioLevelControlTransferFunction.tranferFunction1Over2](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction1over2)

|  | Declaration |
| --- | --- |
| From | ``` case TranferFunction1Over2 ``` |
| To | ``` case tranferFunction1Over2 ``` |

Modified [AudioLevelControlTransferFunction.tranferFunction1Over3](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction1over3)

|  | Declaration |
| --- | --- |
| From | ``` case TranferFunction1Over3 ``` |
| To | ``` case tranferFunction1Over3 ``` |

Modified [AudioLevelControlTransferFunction.tranferFunction2Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction2over1)

|  | Declaration |
| --- | --- |
| From | ``` case TranferFunction2Over1 ``` |
| To | ``` case tranferFunction2Over1 ``` |

Modified [AudioLevelControlTransferFunction.tranferFunction3Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction3over1)

|  | Declaration |
| --- | --- |
| From | ``` case TranferFunction3Over1 ``` |
| To | ``` case tranferFunction3Over1 ``` |

Modified [AudioLevelControlTransferFunction.tranferFunction3Over2](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction3over2)

|  | Declaration |
| --- | --- |
| From | ``` case TranferFunction3Over2 ``` |
| To | ``` case tranferFunction3Over2 ``` |

Modified [AudioLevelControlTransferFunction.tranferFunction3Over4](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction3over4)

|  | Declaration |
| --- | --- |
| From | ``` case TranferFunction3Over4 ``` |
| To | ``` case tranferFunction3Over4 ``` |

Modified [AudioLevelControlTransferFunction.tranferFunction4Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction4over1)

|  | Declaration |
| --- | --- |
| From | ``` case TranferFunction4Over1 ``` |
| To | ``` case tranferFunction4Over1 ``` |

Modified [AudioLevelControlTransferFunction.tranferFunction5Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction5over1)

|  | Declaration |
| --- | --- |
| From | ``` case TranferFunction5Over1 ``` |
| To | ``` case tranferFunction5Over1 ``` |

Modified [AudioLevelControlTransferFunction.tranferFunction6Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction6over1)

|  | Declaration |
| --- | --- |
| From | ``` case TranferFunction6Over1 ``` |
| To | ``` case tranferFunction6Over1 ``` |

Modified [AudioLevelControlTransferFunction.tranferFunction7Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction7over1)

|  | Declaration |
| --- | --- |
| From | ``` case TranferFunction7Over1 ``` |
| To | ``` case tranferFunction7Over1 ``` |

Modified [AudioLevelControlTransferFunction.tranferFunction8Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction8over1)

|  | Declaration |
| --- | --- |
| From | ``` case TranferFunction8Over1 ``` |
| To | ``` case tranferFunction8Over1 ``` |

Modified [AudioLevelControlTransferFunction.tranferFunction9Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction9over1)

|  | Declaration |
| --- | --- |
| From | ``` case TranferFunction9Over1 ``` |
| To | ``` case tranferFunction9Over1 ``` |

Modified [AudioLevelControlTransferFunction.tranferFunctionLinear](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunctionlinear)

|  | Declaration |
| --- | --- |
| From | ``` case TranferFunctionLinear ``` |
| To | ``` case tranferFunctionLinear ``` |

Modified [AudioTimeStampFlags [struct]](https://developer.apple.com/documentation/coreaudio/audiotimestampflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AudioTimeStampFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var NothingValid: AudioTimeStampFlags { get }     static var SampleTimeValid: AudioTimeStampFlags { get }     static var HostTimeValid: AudioTimeStampFlags { get }     static var RateScalarValid: AudioTimeStampFlags { get }     static var WordClockTimeValid: AudioTimeStampFlags { get }     static var SMPTETimeValid: AudioTimeStampFlags { get }     static var SampleHostTimeValid: AudioTimeStampFlags { get } } ``` | OptionSetType |
| To | ``` struct AudioTimeStampFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var nothingValid: AudioTimeStampFlags { get }     static var sampleTimeValid: AudioTimeStampFlags { get }     static var hostTimeValid: AudioTimeStampFlags { get }     static var rateScalarValid: AudioTimeStampFlags { get }     static var wordClockTimeValid: AudioTimeStampFlags { get }     static var smpteTimeValid: AudioTimeStampFlags { get }     static var sampleHostTimeValid: AudioTimeStampFlags { get }     func intersect(_ other: AudioTimeStampFlags) -> AudioTimeStampFlags     func exclusiveOr(_ other: AudioTimeStampFlags) -> AudioTimeStampFlags     mutating func unionInPlace(_ other: AudioTimeStampFlags)     mutating func intersectInPlace(_ other: AudioTimeStampFlags)     mutating func exclusiveOrInPlace(_ other: AudioTimeStampFlags)     func isSubsetOf(_ other: AudioTimeStampFlags) -> Bool     func isDisjointWith(_ other: AudioTimeStampFlags) -> Bool     func isSupersetOf(_ other: AudioTimeStampFlags) -> Bool     mutating func subtractInPlace(_ other: AudioTimeStampFlags)     func isStrictSupersetOf(_ other: AudioTimeStampFlags) -> Bool     func isStrictSubsetOf(_ other: AudioTimeStampFlags) -> Bool } extension AudioTimeStampFlags {     func union(_ other: AudioTimeStampFlags) -> AudioTimeStampFlags     func intersection(_ other: AudioTimeStampFlags) -> AudioTimeStampFlags     func symmetricDifference(_ other: AudioTimeStampFlags) -> AudioTimeStampFlags } extension AudioTimeStampFlags {     func contains(_ member: AudioTimeStampFlags) -> Bool     mutating func insert(_ newMember: AudioTimeStampFlags) -> (inserted: Bool, memberAfterInsert: AudioTimeStampFlags)     mutating func remove(_ member: AudioTimeStampFlags) -> AudioTimeStampFlags?     mutating func update(with newMember: AudioTimeStampFlags) -> AudioTimeStampFlags? } extension AudioTimeStampFlags {     convenience init()     mutating func formUnion(_ other: AudioTimeStampFlags)     mutating func formIntersection(_ other: AudioTimeStampFlags)     mutating func formSymmetricDifference(_ other: AudioTimeStampFlags) } extension AudioTimeStampFlags {     convenience init<S : Sequence where S.Iterator.Element == AudioTimeStampFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AudioTimeStampFlags...)     mutating func subtract(_ other: AudioTimeStampFlags)     func isSubset(of other: AudioTimeStampFlags) -> Bool     func isSuperset(of other: AudioTimeStampFlags) -> Bool     func isDisjoint(with other: AudioTimeStampFlags) -> Bool     func subtracting(_ other: AudioTimeStampFlags) -> AudioTimeStampFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: AudioTimeStampFlags) -> Bool     func isStrictSubset(of other: AudioTimeStampFlags) -> Bool } ``` | OptionSet |

Modified [AudioTimeStampFlags.hostTimeValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/1423064-hosttimevalid)

|  | Declaration |
| --- | --- |
| From | ``` static var HostTimeValid: AudioTimeStampFlags { get } ``` |
| To | ``` static var hostTimeValid: AudioTimeStampFlags { get } ``` |

Modified [AudioTimeStampFlags.rateScalarValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/1422238-ratescalarvalid)

|  | Declaration |
| --- | --- |
| From | ``` static var RateScalarValid: AudioTimeStampFlags { get } ``` |
| To | ``` static var rateScalarValid: AudioTimeStampFlags { get } ``` |

Modified [AudioTimeStampFlags.sampleHostTimeValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/1422143-samplehosttimevalid)

|  | Declaration |
| --- | --- |
| From | ``` static var SampleHostTimeValid: AudioTimeStampFlags { get } ``` |
| To | ``` static var sampleHostTimeValid: AudioTimeStampFlags { get } ``` |

Modified [AudioTimeStampFlags.sampleTimeValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/1423034-sampletimevalid)

|  | Declaration |
| --- | --- |
| From | ``` static var SampleTimeValid: AudioTimeStampFlags { get } ``` |
| To | ``` static var sampleTimeValid: AudioTimeStampFlags { get } ``` |

Modified [AudioTimeStampFlags.smpteTimeValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/kaudiotimestampsmptetimevalid)

|  | Declaration |
| --- | --- |
| From | ``` static var SMPTETimeValid: AudioTimeStampFlags { get } ``` |
| To | ``` static var smpteTimeValid: AudioTimeStampFlags { get } ``` |

Modified [AudioTimeStampFlags.wordClockTimeValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/1422676-wordclocktimevalid)

|  | Declaration |
| --- | --- |
| From | ``` static var WordClockTimeValid: AudioTimeStampFlags { get } ``` |
| To | ``` static var wordClockTimeValid: AudioTimeStampFlags { get } ``` |

Modified [AudioValueTranslation [struct]](https://developer.apple.com/documentation/coreaudio/audiovaluetranslation)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioValueTranslation {     var mInputData: UnsafeMutablePointer<Void>     var mInputDataSize: UInt32     var mOutputData: UnsafeMutablePointer<Void>     var mOutputDataSize: UInt32 } ``` |
| To | ``` struct AudioValueTranslation {     var mInputData: UnsafeMutableRawPointer     var mInputDataSize: UInt32     var mOutputData: UnsafeMutableRawPointer     var mOutputDataSize: UInt32 } ``` |

Modified [AudioValueTranslation.mInputData](https://developer.apple.com/documentation/coreaudio/audiovaluetranslation/1421725-minputdata)

|  | Declaration |
| --- | --- |
| From | ``` var mInputData: UnsafeMutablePointer<Void> ``` |
| To | ``` var mInputData: UnsafeMutableRawPointer ``` |

Modified [AudioValueTranslation.mOutputData](https://developer.apple.com/documentation/coreaudio/audiovaluetranslation/1422730-moutputdata)

|  | Declaration |
| --- | --- |
| From | ``` var mOutputData: UnsafeMutablePointer<Void> ``` |
| To | ``` var mOutputData: UnsafeMutableRawPointer ``` |

Modified [MPEG4ObjectID [enum]](https://developer.apple.com/documentation/coreaudio/mpeg4objectid)

|  | Declaration |
| --- | --- |
| From | ``` enum MPEG4ObjectID : Int {     case AAC_Main     case AAC_LC     case AAC_SSR     case AAC_LTP     case AAC_SBR     case AAC_Scalable     case TwinVQ     case CELP     case HVXC } ``` |
| To | ``` enum MPEG4ObjectID : Int {     case aac_Main     case AAC_LC     case AAC_SSR     case AAC_LTP     case AAC_SBR     case aac_Scalable     case twinVQ     case CELP     case HVXC } ``` |

Modified [MPEG4ObjectID.aac_Main](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/kmpeg4object_aac_main)

|  | Declaration |
| --- | --- |
| From | ``` case AAC_Main ``` |
| To | ``` case aac_Main ``` |

Modified [MPEG4ObjectID.aac_Scalable](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/aac_scalable)

|  | Declaration |
| --- | --- |
| From | ``` case AAC_Scalable ``` |
| To | ``` case aac_Scalable ``` |

Modified [MPEG4ObjectID.twinVQ](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/twinvq)

|  | Declaration |
| --- | --- |
| From | ``` case TwinVQ ``` |
| To | ``` case twinVQ ``` |

Modified [SMPTETimeFlags [struct]](https://developer.apple.com/documentation/coreaudio/smptetimeflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SMPTETimeFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var Unknown: SMPTETimeFlags { get }     static var Valid: SMPTETimeFlags { get }     static var Running: SMPTETimeFlags { get } } ``` | OptionSetType |
| To | ``` struct SMPTETimeFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var unknown: SMPTETimeFlags { get }     static var valid: SMPTETimeFlags { get }     static var running: SMPTETimeFlags { get }     func intersect(_ other: SMPTETimeFlags) -> SMPTETimeFlags     func exclusiveOr(_ other: SMPTETimeFlags) -> SMPTETimeFlags     mutating func unionInPlace(_ other: SMPTETimeFlags)     mutating func intersectInPlace(_ other: SMPTETimeFlags)     mutating func exclusiveOrInPlace(_ other: SMPTETimeFlags)     func isSubsetOf(_ other: SMPTETimeFlags) -> Bool     func isDisjointWith(_ other: SMPTETimeFlags) -> Bool     func isSupersetOf(_ other: SMPTETimeFlags) -> Bool     mutating func subtractInPlace(_ other: SMPTETimeFlags)     func isStrictSupersetOf(_ other: SMPTETimeFlags) -> Bool     func isStrictSubsetOf(_ other: SMPTETimeFlags) -> Bool } extension SMPTETimeFlags {     func union(_ other: SMPTETimeFlags) -> SMPTETimeFlags     func intersection(_ other: SMPTETimeFlags) -> SMPTETimeFlags     func symmetricDifference(_ other: SMPTETimeFlags) -> SMPTETimeFlags } extension SMPTETimeFlags {     func contains(_ member: SMPTETimeFlags) -> Bool     mutating func insert(_ newMember: SMPTETimeFlags) -> (inserted: Bool, memberAfterInsert: SMPTETimeFlags)     mutating func remove(_ member: SMPTETimeFlags) -> SMPTETimeFlags?     mutating func update(with newMember: SMPTETimeFlags) -> SMPTETimeFlags? } extension SMPTETimeFlags {     convenience init()     mutating func formUnion(_ other: SMPTETimeFlags)     mutating func formIntersection(_ other: SMPTETimeFlags)     mutating func formSymmetricDifference(_ other: SMPTETimeFlags) } extension SMPTETimeFlags {     convenience init<S : Sequence where S.Iterator.Element == SMPTETimeFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: SMPTETimeFlags...)     mutating func subtract(_ other: SMPTETimeFlags)     func isSubset(of other: SMPTETimeFlags) -> Bool     func isSuperset(of other: SMPTETimeFlags) -> Bool     func isDisjoint(with other: SMPTETimeFlags) -> Bool     func subtracting(_ other: SMPTETimeFlags) -> SMPTETimeFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: SMPTETimeFlags) -> Bool     func isStrictSubset(of other: SMPTETimeFlags) -> Bool } ``` | OptionSet |

Modified [SMPTETimeFlags.running](https://developer.apple.com/documentation/coreaudio/smptetimeflags/ksmptetimerunning)

|  | Declaration |
| --- | --- |
| From | ``` static var Running: SMPTETimeFlags { get } ``` |
| To | ``` static var running: SMPTETimeFlags { get } ``` |

Modified [SMPTETimeFlags.valid](https://developer.apple.com/documentation/coreaudio/smptetimeflags/ksmptetimevalid)

|  | Declaration |
| --- | --- |
| From | ``` static var Valid: SMPTETimeFlags { get } ``` |
| To | ``` static var valid: SMPTETimeFlags { get } ``` |

Modified [SMPTETimeType [enum]](https://developer.apple.com/documentation/coreaudio/smptetimetype)

|  | Declaration |
| --- | --- |
| From | ``` enum SMPTETimeType : UInt32 {     case Type24     case Type25     case Type30Drop     case Type30     case Type2997     case Type2997Drop     case Type60     case Type5994     case Type60Drop     case Type5994Drop     case Type50     case Type2398 } ``` |
| To | ``` enum SMPTETimeType : UInt32 {     case type24     case type25     case type30Drop     case type30     case type2997     case type2997Drop     case type60     case type5994     case type60Drop     case type5994Drop     case type50     case type2398 } ``` |

Modified [SMPTETimeType.type2398](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype2398)

|  | Declaration |
| --- | --- |
| From | ``` case Type2398 ``` |
| To | ``` case type2398 ``` |

Modified [SMPTETimeType.type24](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype24)

|  | Declaration |
| --- | --- |
| From | ``` case Type24 ``` |
| To | ``` case type24 ``` |

Modified [SMPTETimeType.type25](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype25)

|  | Declaration |
| --- | --- |
| From | ``` case Type25 ``` |
| To | ``` case type25 ``` |

Modified [SMPTETimeType.type2997](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype2997)

|  | Declaration |
| --- | --- |
| From | ``` case Type2997 ``` |
| To | ``` case type2997 ``` |

Modified [SMPTETimeType.type2997Drop](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype2997drop)

|  | Declaration |
| --- | --- |
| From | ``` case Type2997Drop ``` |
| To | ``` case type2997Drop ``` |

Modified [SMPTETimeType.type30](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype30)

|  | Declaration |
| --- | --- |
| From | ``` case Type30 ``` |
| To | ``` case type30 ``` |

Modified [SMPTETimeType.type30Drop](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype30drop)

|  | Declaration |
| --- | --- |
| From | ``` case Type30Drop ``` |
| To | ``` case type30Drop ``` |

Modified [SMPTETimeType.type50](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype50)

|  | Declaration |
| --- | --- |
| From | ``` case Type50 ``` |
| To | ``` case type50 ``` |

Modified [SMPTETimeType.type5994](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype5994)

|  | Declaration |
| --- | --- |
| From | ``` case Type5994 ``` |
| To | ``` case type5994 ``` |

Modified [SMPTETimeType.type5994Drop](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype5994drop)

|  | Declaration |
| --- | --- |
| From | ``` case Type5994Drop ``` |
| To | ``` case type5994Drop ``` |

Modified [SMPTETimeType.type60](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype60)

|  | Declaration |
| --- | --- |
| From | ``` case Type60 ``` |
| To | ``` case type60 ``` |

Modified [SMPTETimeType.type60Drop](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype60drop)

|  | Declaration |
| --- | --- |
| From | ``` case Type60Drop ``` |
| To | ``` case type60Drop ``` |

Modified [UnsafeMutableAudioBufferListPointer [struct]](https://developer.apple.com/documentation/coreaudio/unsafemutableaudiobufferlistpointer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UnsafeMutableAudioBufferListPointer {     init(_ p: UnsafeMutablePointer<AudioBufferList>)     var count: Int { get nonmutating set }     var unsafePointer: UnsafePointer<AudioBufferList> { get }     var unsafeMutablePointer: UnsafeMutablePointer<AudioBufferList> } extension UnsafeMutableAudioBufferListPointer : MutableCollectionType {     var startIndex: Int { get }     var endIndex: Int { get }     subscript (_ index: Int) -> AudioBuffer { get nonmutating set } } ``` | MutableCollectionType |
| To | ``` struct UnsafeMutableAudioBufferListPointer {     init(_ p: UnsafeMutablePointer<AudioBufferList>)     init?(_ p: UnsafeMutablePointer<AudioBufferList>?)     var count: Int { get nonmutating set }     var unsafePointer: UnsafePointer<AudioBufferList> { get }     var unsafeMutablePointer: UnsafeMutablePointer<AudioBufferList> } extension UnsafeMutableAudioBufferListPointer : MutableCollection, RandomAccessCollection {     typealias Index = Int     var startIndex: Int { get }     var endIndex: Int { get }     subscript(_ index: Int) -> AudioBuffer { get nonmutating set }     subscript(_ bounds: Range<Int>) -> MutableRandomAccessSlice<UnsafeMutableAudioBufferListPointer>     typealias Indices = CountableRange<Int> } ``` | MutableCollection, RandomAccessCollection |

Modified [UnsafeMutableAudioBufferListPointer.subscript(_: Int) -> AudioBuffer](https://developer.apple.com/documentation/coreaudio/unsafemutableaudiobufferlistpointer/1422107-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ index: Int) -> AudioBuffer { get nonmutating set } ``` |
| To | ``` subscript(_ index: Int) -> AudioBuffer { get nonmutating set } ``` |

Modified [AudioDeviceCreateIOProcID(_: AudioObjectID, _: CoreAudio.AudioDeviceIOProc, _: UnsafeMutableRawPointer?, _: UnsafeMutablePointer<CoreAudio.AudioDeviceIOProcID?>) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1423215-audiodevicecreateioprocid)

|  | Declaration |
| --- | --- |
| From | ``` func AudioDeviceCreateIOProcID(_ inDevice: AudioObjectID, _ inProc: AudioDeviceIOProc, _ inClientData: UnsafeMutablePointer<Void>, _ outIOProcID: UnsafeMutablePointer<AudioDeviceIOProcID?>) -> OSStatus ``` |
| To | ``` func AudioDeviceCreateIOProcID(_ inDevice: AudioObjectID, _ inProc: CoreAudio.AudioDeviceIOProc, _ inClientData: UnsafeMutableRawPointer?, _ outIOProcID: UnsafeMutablePointer<CoreAudio.AudioDeviceIOProcID?>) -> OSStatus ``` |

Modified [AudioDeviceCreateIOProcIDWithBlock(_: UnsafeMutablePointer<CoreAudio.AudioDeviceIOProcID?>, _: AudioObjectID, _: DispatchQueue?, _: CoreAudio.AudioDeviceIOBlock) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422986-audiodevicecreateioprocidwithblo)

|  | Declaration |
| --- | --- |
| From | ``` func AudioDeviceCreateIOProcIDWithBlock(_ outIOProcID: UnsafeMutablePointer<AudioDeviceIOProcID?>, _ inDevice: AudioObjectID, _ inDispatchQueue: dispatch_queue_t?, _ inIOBlock: AudioDeviceIOBlock) -> OSStatus ``` |
| To | ``` func AudioDeviceCreateIOProcIDWithBlock(_ outIOProcID: UnsafeMutablePointer<CoreAudio.AudioDeviceIOProcID?>, _ inDevice: AudioObjectID, _ inDispatchQueue: DispatchQueue?, _ inIOBlock: CoreAudio.AudioDeviceIOBlock) -> OSStatus ``` |

Modified [AudioDeviceDestroyIOProcID(_: AudioObjectID, _: CoreAudio.AudioDeviceIOProcID) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422982-audiodevicedestroyioprocid)

|  | Declaration |
| --- | --- |
| From | ``` func AudioDeviceDestroyIOProcID(_ inDevice: AudioObjectID, _ inIOProcID: AudioDeviceIOProcID) -> OSStatus ``` |
| To | ``` func AudioDeviceDestroyIOProcID(_ inDevice: AudioObjectID, _ inIOProcID: CoreAudio.AudioDeviceIOProcID) -> OSStatus ``` |

Modified [AudioDeviceIOBlock](https://developer.apple.com/documentation/coreaudio/audiodeviceioblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioDeviceIOBlock = (UnsafePointer<AudioTimeStamp>, UnsafePointer<AudioBufferList>, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioBufferList>, UnsafePointer<AudioTimeStamp>) -> Void ``` |
| To | ``` typealias AudioDeviceIOBlock = (UnsafePointer<AudioTimeStamp>, UnsafePointer<AudioBufferList>, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioBufferList>, UnsafePointer<AudioTimeStamp>) -> Swift.Void ``` |

Modified [AudioDeviceIOProc](https://developer.apple.com/documentation/coreaudio/audiodeviceioproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioDeviceIOProc = (AudioObjectID, UnsafePointer<AudioTimeStamp>, UnsafePointer<AudioBufferList>, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioBufferList>, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias AudioDeviceIOProc = (AudioObjectID, UnsafePointer<AudioTimeStamp>, UnsafePointer<AudioBufferList>, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioBufferList>, UnsafePointer<AudioTimeStamp>, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AudioDeviceIOProcID](https://developer.apple.com/documentation/coreaudio/audiodeviceioprocid)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioDeviceIOProcID = AudioDeviceIOProc ``` |
| To | ``` typealias AudioDeviceIOProcID = CoreAudio.AudioDeviceIOProc ``` |

Modified [AudioDevicePropertyListenerProc](https://developer.apple.com/documentation/coreaudio/audiodevicepropertylistenerproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioDevicePropertyListenerProc = (AudioDeviceID, UInt32, DarwinBoolean, AudioDevicePropertyID, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias AudioDevicePropertyListenerProc = (AudioDeviceID, UInt32, DarwinBoolean, AudioDevicePropertyID, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AudioDeviceStart(_: AudioObjectID, _: CoreAudio.AudioDeviceIOProcID?) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422884-audiodevicestart)

|  | Declaration |
| --- | --- |
| From | ``` func AudioDeviceStart(_ inDevice: AudioObjectID, _ inProcID: AudioDeviceIOProcID?) -> OSStatus ``` |
| To | ``` func AudioDeviceStart(_ inDevice: AudioObjectID, _ inProcID: CoreAudio.AudioDeviceIOProcID?) -> OSStatus ``` |

Modified [AudioDeviceStartAtTime(_: AudioObjectID, _: CoreAudio.AudioDeviceIOProcID?, _: UnsafeMutablePointer<AudioTimeStamp>, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422331-audiodevicestartattime)

|  | Declaration |
| --- | --- |
| From | ``` func AudioDeviceStartAtTime(_ inDevice: AudioObjectID, _ inProcID: AudioDeviceIOProcID?, _ ioRequestedStartTime: UnsafeMutablePointer<AudioTimeStamp>, _ inFlags: UInt32) -> OSStatus ``` |
| To | ``` func AudioDeviceStartAtTime(_ inDevice: AudioObjectID, _ inProcID: CoreAudio.AudioDeviceIOProcID?, _ ioRequestedStartTime: UnsafeMutablePointer<AudioTimeStamp>, _ inFlags: UInt32) -> OSStatus ``` |

Modified [AudioDeviceStop(_: AudioObjectID, _: CoreAudio.AudioDeviceIOProcID?) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1421761-audiodevicestop)

|  | Declaration |
| --- | --- |
| From | ``` func AudioDeviceStop(_ inDevice: AudioObjectID, _ inProcID: AudioDeviceIOProcID?) -> OSStatus ``` |
| To | ``` func AudioDeviceStop(_ inDevice: AudioObjectID, _ inProcID: CoreAudio.AudioDeviceIOProcID?) -> OSStatus ``` |

Modified [AudioHardwarePropertyListenerProc](https://developer.apple.com/documentation/coreaudio/audiohardwarepropertylistenerproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioHardwarePropertyListenerProc = (AudioHardwarePropertyID, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias AudioHardwarePropertyListenerProc = (AudioHardwarePropertyID, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AudioObjectAddPropertyListener(_: AudioObjectID, _: UnsafePointer<AudioObjectPropertyAddress>, _: CoreAudio.AudioObjectPropertyListenerProc, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422472-audioobjectaddpropertylistener)

|  | Declaration |
| --- | --- |
| From | ``` func AudioObjectAddPropertyListener(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inListener: AudioObjectPropertyListenerProc, _ inClientData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioObjectAddPropertyListener(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inListener: CoreAudio.AudioObjectPropertyListenerProc, _ inClientData: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AudioObjectAddPropertyListenerBlock(_: AudioObjectID, _: UnsafePointer<AudioObjectPropertyAddress>, _: DispatchQueue?, _: CoreAudio.AudioObjectPropertyListenerBlock) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422686-audioobjectaddpropertylistenerbl)

|  | Declaration |
| --- | --- |
| From | ``` func AudioObjectAddPropertyListenerBlock(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inDispatchQueue: dispatch_queue_t?, _ inListener: AudioObjectPropertyListenerBlock) -> OSStatus ``` |
| To | ``` func AudioObjectAddPropertyListenerBlock(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inDispatchQueue: DispatchQueue?, _ inListener: CoreAudio.AudioObjectPropertyListenerBlock) -> OSStatus ``` |

Modified [AudioObjectGetPropertyData(_: AudioObjectID, _: UnsafePointer<AudioObjectPropertyAddress>, _: UInt32, _: UnsafeRawPointer?, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutableRawPointer) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422524-audioobjectgetpropertydata)

|  | Declaration |
| --- | --- |
| From | ``` func AudioObjectGetPropertyData(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inQualifierDataSize: UInt32, _ inQualifierData: UnsafePointer<Void>, _ ioDataSize: UnsafeMutablePointer<UInt32>, _ outData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioObjectGetPropertyData(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inQualifierDataSize: UInt32, _ inQualifierData: UnsafeRawPointer?, _ ioDataSize: UnsafeMutablePointer<UInt32>, _ outData: UnsafeMutableRawPointer) -> OSStatus ``` |

Modified [AudioObjectGetPropertyDataSize(_: AudioObjectID, _: UnsafePointer<AudioObjectPropertyAddress>, _: UInt32, _: UnsafeRawPointer?, _: UnsafeMutablePointer<UInt32>) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422305-audioobjectgetpropertydatasize)

|  | Declaration |
| --- | --- |
| From | ``` func AudioObjectGetPropertyDataSize(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inQualifierDataSize: UInt32, _ inQualifierData: UnsafePointer<Void>, _ outDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func AudioObjectGetPropertyDataSize(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inQualifierDataSize: UInt32, _ inQualifierData: UnsafeRawPointer?, _ outDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified [AudioObjectPropertyListenerBlock](https://developer.apple.com/documentation/coreaudio/audioobjectpropertylistenerblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioObjectPropertyListenerBlock = (UInt32, UnsafePointer<AudioObjectPropertyAddress>) -> Void ``` |
| To | ``` typealias AudioObjectPropertyListenerBlock = (UInt32, UnsafePointer<AudioObjectPropertyAddress>) -> Swift.Void ``` |

Modified [AudioObjectPropertyListenerProc](https://developer.apple.com/documentation/coreaudio/audioobjectpropertylistenerproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioObjectPropertyListenerProc = (AudioObjectID, UInt32, UnsafePointer<AudioObjectPropertyAddress>, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias AudioObjectPropertyListenerProc = (AudioObjectID, UInt32, UnsafePointer<AudioObjectPropertyAddress>, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AudioObjectRemovePropertyListener(_: AudioObjectID, _: UnsafePointer<AudioObjectPropertyAddress>, _: CoreAudio.AudioObjectPropertyListenerProc, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422593-audioobjectremovepropertylistene)

|  | Declaration |
| --- | --- |
| From | ``` func AudioObjectRemovePropertyListener(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inListener: AudioObjectPropertyListenerProc, _ inClientData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioObjectRemovePropertyListener(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inListener: CoreAudio.AudioObjectPropertyListenerProc, _ inClientData: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AudioObjectRemovePropertyListenerBlock(_: AudioObjectID, _: UnsafePointer<AudioObjectPropertyAddress>, _: DispatchQueue?, _: CoreAudio.AudioObjectPropertyListenerBlock) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1421640-audioobjectremovepropertylistene)

|  | Declaration |
| --- | --- |
| From | ``` func AudioObjectRemovePropertyListenerBlock(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inDispatchQueue: dispatch_queue_t?, _ inListener: AudioObjectPropertyListenerBlock) -> OSStatus ``` |
| To | ``` func AudioObjectRemovePropertyListenerBlock(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inDispatchQueue: DispatchQueue?, _ inListener: CoreAudio.AudioObjectPropertyListenerBlock) -> OSStatus ``` |

Modified [AudioObjectSetPropertyData(_: AudioObjectID, _: UnsafePointer<AudioObjectPropertyAddress>, _: UInt32, _: UnsafeRawPointer?, _: UInt32, _: UnsafeRawPointer) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422920-audioobjectsetpropertydata)

|  | Declaration |
| --- | --- |
| From | ``` func AudioObjectSetPropertyData(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inQualifierDataSize: UInt32, _ inQualifierData: UnsafePointer<Void>, _ inDataSize: UInt32, _ inData: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioObjectSetPropertyData(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inQualifierDataSize: UInt32, _ inQualifierData: UnsafeRawPointer?, _ inDataSize: UInt32, _ inData: UnsafeRawPointer) -> OSStatus ``` |

Modified [AudioStreamPropertyListenerProc](https://developer.apple.com/documentation/coreaudio/audiostreampropertylistenerproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioStreamPropertyListenerProc = (AudioStreamID, UInt32, AudioDevicePropertyID, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias AudioStreamPropertyListenerProc = (AudioStreamID, UInt32, AudioDevicePropertyID, UnsafeMutableRawPointer?) -> OSStatus ``` |

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
