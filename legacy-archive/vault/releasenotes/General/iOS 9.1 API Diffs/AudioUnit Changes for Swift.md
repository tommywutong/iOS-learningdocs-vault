---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/AudioUnit.html
archived_at: '2026-07-18T02:57:06.111925Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# AudioUnit Changes for Swift

### AudioUnit

Added [AURenderEvent.head](https://developer.apple.com/documentation/audiotoolbox/1440272-aurenderevent/1440028-head)Added AURenderEvent.init(head: AURenderEventHeader)Added AURenderEvent.init(MIDI: AUMIDIEvent)Added AURenderEvent.init(parameter: AUParameterEvent)Added [AURenderEvent.MIDI](https://developer.apple.com/documentation/audiotoolbox/1440272-aurenderevent/1438519-midi)Added [AURenderEvent.parameter](https://developer.apple.com/documentation/audiotoolbox/1440272-aurenderevent/1439668-parameter)Modified [AU3DMixerAttenuationCurve [enum]](https://developer.apple.com/documentation/audiotoolbox/au3dmixerattenuationcurve)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AUAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounit)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AUAudioUnitBus](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AUAudioUnitBusArray](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSFastEnumeration |
| To | NSFastEnumeration |

Modified [AUAudioUnitBusType [enum]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbustype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AUAudioUnitFactory](https://developer.apple.com/documentation/audiotoolbox/auaudiounitfactory)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol AUAudioUnitFactory : NSExtensionRequestHandling, NSObjectProtocol {     func createAudioUnitWithComponentDescription(_ desc: AudioComponentDescription) throws -> AUAudioUnit } ``` | NSExtensionRequestHandling, NSObjectProtocol |
| To | ``` protocol AUAudioUnitFactory : NSExtensionRequestHandling {     func createAudioUnitWithComponentDescription(_ desc: AudioComponentDescription) throws -> AUAudioUnit } ``` | NSExtensionRequestHandling |

Modified [AUAudioUnitPreset](https://developer.apple.com/documentation/audiotoolbox/auaudiounitpreset)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AUAudioUnitPreset : NSObject, NSSecureCoding, NSCoding {     var number: Int     var name: String } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class AUAudioUnitPreset : NSObject, NSSecureCoding {     var number: Int     var name: String } ``` | NSSecureCoding |

Modified [AUAudioUnitV2Bridge](https://developer.apple.com/documentation/audiotoolbox/auaudiounitv2bridge)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AudioComponentValidationResult [enum]](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AudioUnitParameterUnit [enum]](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AudioUnitRemoteControlEvent [enum]](https://developer.apple.com/documentation/audiotoolbox/audiounitremotecontrolevent)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AUParameter](https://developer.apple.com/documentation/audiotoolbox/auparameter)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AUParameter : AUParameterNode, NSSecureCoding, NSCoding {     var minValue: AUValue { get }     var maxValue: AUValue { get }     var unit: AudioUnitParameterUnit { get }     var unitName: String? { get }     var flags: AudioUnitParameterOptions { get }     var address: AUParameterAddress { get }     var valueStrings: [String]? { get }     var dependentParameters: [NSNumber]? { get }     var value: AUValue     func setValue(_ value: AUValue, originator originator: AUParameterObserverToken)     func setValue(_ value: AUValue, originator originator: AUParameterObserverToken, atHostTime hostTime: UInt64)     func stringFromValue(_ value: UnsafePointer<AUValue>) -> String     func valueFromString(_ string: String) -> AUValue } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class AUParameter : AUParameterNode, NSSecureCoding {     var minValue: AUValue { get }     var maxValue: AUValue { get }     var unit: AudioUnitParameterUnit { get }     var unitName: String? { get }     var flags: AudioUnitParameterOptions { get }     var address: AUParameterAddress { get }     var valueStrings: [String]? { get }     var dependentParameters: [NSNumber]? { get }     var value: AUValue     func setValue(_ value: AUValue, originator originator: AUParameterObserverToken)     func setValue(_ value: AUValue, originator originator: AUParameterObserverToken, atHostTime hostTime: UInt64)     func stringFromValue(_ value: UnsafePointer<AUValue>) -> String     func valueFromString(_ string: String) -> AUValue } ``` | NSSecureCoding |

Modified [AUParameterEventType [enum]](https://developer.apple.com/documentation/audiotoolbox/auparametereventtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AUParameterGroup](https://developer.apple.com/documentation/audiotoolbox/auparametergroup)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AUParameterGroup : AUParameterNode, NSSecureCoding, NSCoding {     var children: [AUParameterNode] { get }     var allParameters: [AUParameter] { get } } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class AUParameterGroup : AUParameterNode, NSSecureCoding {     var children: [AUParameterNode] { get }     var allParameters: [AUParameter] { get } } ``` | NSSecureCoding |

Modified [AUParameterNode](https://developer.apple.com/documentation/audiotoolbox/auparameternode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AUParameterTree](https://developer.apple.com/documentation/audiotoolbox/auparametertree)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AUParameterTree : AUParameterGroup {     func parameterWithAddress(_ address: AUParameterAddress) -> AUParameter?     func parameterWithID(_ paramID: AudioUnitParameterID, scope scope: AudioUnitScope, element element: AudioUnitElement) -> AUParameter? } extension AUParameterTree {     class func createParameterWithIdentifier(_ identifier: String, name name: String, address address: AUParameterAddress, min min: AUValue, max max: AUValue, unit unit: AudioUnitParameterUnit, unitName unitName: String?, flags flags: AudioUnitParameterOptions, valueStrings valueStrings: [String]?, dependentParameters dependentParameters: [NSNumber]?) -> AUParameter     class func createGroupWithIdentifier(_ identifier: String, name name: String, children children: [AUParameterNode]) -> AUParameterGroup     class func createGroupTemplate(_ children: [AUParameterNode]) -> AUParameterGroup     class func createGroupFromTemplate(_ templateGroup: AUParameterGroup, identifier identifier: String, name name: String, addressOffset addressOffset: AUParameterAddress) -> AUParameterGroup     class func createTreeWithChildren(_ children: [AUParameterNode]) -> AUParameterTree } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class AUParameterTree : AUParameterGroup, NSSecureCoding {     func parameterWithAddress(_ address: AUParameterAddress) -> AUParameter?     func parameterWithID(_ paramID: AudioUnitParameterID, scope scope: AudioUnitScope, element element: AudioUnitElement) -> AUParameter? } extension AUParameterTree {     class func createParameterWithIdentifier(_ identifier: String, name name: String, address address: AUParameterAddress, min min: AUValue, max max: AUValue, unit unit: AudioUnitParameterUnit, unitName unitName: String?, flags flags: AudioUnitParameterOptions, valueStrings valueStrings: [String]?, dependentParameters dependentParameters: [NSNumber]?) -> AUParameter     class func createGroupWithIdentifier(_ identifier: String, name name: String, children children: [AUParameterNode]) -> AUParameterGroup     class func createGroupTemplate(_ children: [AUParameterNode]) -> AUParameterGroup     class func createGroupFromTemplate(_ templateGroup: AUParameterGroup, identifier identifier: String, name name: String, addressOffset addressOffset: AUParameterAddress) -> AUParameterGroup     class func createTreeWithChildren(_ children: [AUParameterNode]) -> AUParameterTree } ``` | NSSecureCoding |

Modified [AURenderEvent [struct]](https://developer.apple.com/documentation/audiotoolbox/aurenderevent)

|  | Declaration |
| --- | --- |
| From | ``` struct AURenderEvent {     init() } ``` |
| To | ``` struct AURenderEvent {     var head: AURenderEventHeader     var parameter: AUParameterEvent     var MIDI: AUMIDIEvent     init(head head: AURenderEventHeader)     init(parameter parameter: AUParameterEvent)     init(MIDI MIDI: AUMIDIEvent)     init() } ``` |

Modified [AURenderEventType [enum]](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AUReverbRoomType [enum]](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AUSpatializationAlgorithm [enum]](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AUSpatialMixerAttenuationCurve [enum]](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

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
