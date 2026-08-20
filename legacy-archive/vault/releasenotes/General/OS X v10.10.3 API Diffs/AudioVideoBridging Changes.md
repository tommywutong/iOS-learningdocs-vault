---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/AudioVideoBridging.html
archived_at: '2026-07-18T02:52:06.535862Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# AudioVideoBridging Changes

## AudioVideoBridging

Removed AVB17221ACMPFlags.valueRemoved AVB17221ADPControllerCapabilities.valueRemoved AVB17221ADPEntityCapabilities.ASSupportedRemoved AVB17221ADPEntityCapabilities.DFUModeRemoved AVB17221ADPListenerCapabilities.valueRemoved AVB17221ADPTalkerCapabilities.valueRemoved AVB17221EntityPropertyChanged.ASGrandmasterIDRemoved AVB17221EntityPropertyChanged.GUIDRemoved AVB17221EntityPropertyChanged.valueAdded AVB17221ACMPFlags.init(rawValue: UInt16)Added AVB17221ADPControllerCapabilities.init(rawValue: UInt32)Added AVB17221ADPListenerCapabilities.init(rawValue: UInt16)Added AVB17221ADPTalkerCapabilities.init(rawValue: UInt16)Added AVB17221EntityPropertyChanged.init(rawValue: UInt)Modified AVB17221ACMPFlags [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct AVB17221ACMPFlags : RawOptionSet {     init(_ value: UInt16)     var value: UInt16     static var None: AVB17221ACMPFlags { get }     static var ClassB: AVB17221ACMPFlags { get }     static var FastConnect: AVB17221ACMPFlags { get }     static var SavedState: AVB17221ACMPFlags { get }     static var StreamingWait: AVB17221ACMPFlags { get }     static var SupportsEncrypted: AVB17221ACMPFlags { get }     static var EncryptedPDU: AVB17221ACMPFlags { get }     static var StreamingTalkerFailed: AVB17221ACMPFlags { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct AVB17221ACMPFlags : RawOptionSetType {     init(_ rawValue: UInt16)     init(rawValue rawValue: UInt16)     static var None: AVB17221ACMPFlags { get }     static var ClassB: AVB17221ACMPFlags { get }     static var FastConnect: AVB17221ACMPFlags { get }     static var SavedState: AVB17221ACMPFlags { get }     static var StreamingWait: AVB17221ACMPFlags { get }     static var SupportsEncrypted: AVB17221ACMPFlags { get }     static var EncryptedPDU: AVB17221ACMPFlags { get }     static var StreamingTalkerFailed: AVB17221ACMPFlags { get } } ``` | RawOptionSetType | OS X 10.8 |

Modified AVB17221ACMPFlags.init(_: UInt16)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt16) ``` |
| To | ``` init(_ rawValue: UInt16) ``` |

Modified AVB17221ACMPInterface

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVB17221ACMPInterface.init(interface: AVBInterface!)

|  | Declaration |
| --- | --- |
| From | ``` init(interface anInterface: AVBInterface!) -> AVB17221ACMPInterface ``` |
| To | ``` init!(interface anInterface: AVBInterface!) -> AVB17221ACMPInterface ``` |

Modified AVB17221ACMPInterface.init(interfaceNamed: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(interfaceNamed anInterfaceName: String!) -> AVB17221ACMPInterface ``` |
| To | ``` init!(interfaceNamed anInterfaceName: String!) -> AVB17221ACMPInterface ``` |

Modified AVB17221ACMPInterface.multicastDestinationAddress

|  | Declaration |
| --- | --- |
| From | ``` var multicastDestinationAddress: AVBMACAddress! ``` |
| To | ``` @NSCopying var multicastDestinationAddress: AVBMACAddress! ``` |

Modified AVB17221ACMPInterface.removeHandlerForEntityID(UInt64)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221ACMPInterface.setHandler(AVB17221ACMPClient!, forEntityID: UInt64) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221ACMPMessage

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVB17221ACMPMessage.controllerEntityID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221ACMPMessage.destinationMAC

|  | Declaration |
| --- | --- |
| From | ``` var destinationMAC: AVBMACAddress! ``` |
| To | ``` @NSCopying var destinationMAC: AVBMACAddress! ``` |

Modified AVB17221ACMPMessage.listenerEntityID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221ACMPMessage.sourceMAC

|  | Declaration |
| --- | --- |
| From | ``` var sourceMAC: AVBMACAddress! ``` |
| To | ``` @NSCopying var sourceMAC: AVBMACAddress! ``` |

Modified AVB17221ACMPMessage.talkerEntityID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221ACMPMessageType [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVB17221ACMPStatusCode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVB17221ADPControllerCapabilities [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct AVB17221ADPControllerCapabilities : RawOptionSet {     init(_ value: UInt32)     var value: UInt32     static var Implemented: AVB17221ADPControllerCapabilities { get }     static var HasLayer3Proxy: AVB17221ADPControllerCapabilities { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct AVB17221ADPControllerCapabilities : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var Implemented: AVB17221ADPControllerCapabilities { get }     static var HasLayer3Proxy: AVB17221ADPControllerCapabilities { get } } ``` | RawOptionSetType | OS X 10.8 |

Modified AVB17221ADPControllerCapabilities.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

Modified AVB17221ADPEntityCapabilities [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVB17221ADPEntityCapabilities.AEMAuthenticationRequired

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221ADPEntityCapabilities.AEMAuthenticationSupported

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221ADPEntityCapabilities.AEMIdenitifyControlIndexValid

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221ADPEntityCapabilities.AEMInterfaceIndexValid

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221ADPEntityCapabilities.AEMPersistentAcquireSupported

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221ADPEntityCapabilities.EntityNotReady

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221ADPEntityCapabilities.GeneralControllerIgnore

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221ADPListenerCapabilities [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct AVB17221ADPListenerCapabilities : RawOptionSet {     init(_ value: UInt16)     var value: UInt16     static var Implemented: AVB17221ADPListenerCapabilities { get }     static var HasOtherSink: AVB17221ADPListenerCapabilities { get }     static var HasControlSink: AVB17221ADPListenerCapabilities { get }     static var HasMediaClockSink: AVB17221ADPListenerCapabilities { get }     static var HasSMPTESink: AVB17221ADPListenerCapabilities { get }     static var HasMIDISink: AVB17221ADPListenerCapabilities { get }     static var HasAudioSink: AVB17221ADPListenerCapabilities { get }     static var HasVideoSink: AVB17221ADPListenerCapabilities { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct AVB17221ADPListenerCapabilities : RawOptionSetType {     init(_ rawValue: UInt16)     init(rawValue rawValue: UInt16)     static var Implemented: AVB17221ADPListenerCapabilities { get }     static var HasOtherSink: AVB17221ADPListenerCapabilities { get }     static var HasControlSink: AVB17221ADPListenerCapabilities { get }     static var HasMediaClockSink: AVB17221ADPListenerCapabilities { get }     static var HasSMPTESink: AVB17221ADPListenerCapabilities { get }     static var HasMIDISink: AVB17221ADPListenerCapabilities { get }     static var HasAudioSink: AVB17221ADPListenerCapabilities { get }     static var HasVideoSink: AVB17221ADPListenerCapabilities { get } } ``` | RawOptionSetType | OS X 10.8 |

Modified AVB17221ADPListenerCapabilities.init(_: UInt16)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt16) ``` |
| To | ``` init(_ rawValue: UInt16) ``` |

Modified AVB17221ADPTalkerCapabilities [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct AVB17221ADPTalkerCapabilities : RawOptionSet {     init(_ value: UInt16)     var value: UInt16     static var Implemented: AVB17221ADPTalkerCapabilities { get }     static var HasOtherSource: AVB17221ADPTalkerCapabilities { get }     static var HasControlSource: AVB17221ADPTalkerCapabilities { get }     static var HasMediaClockSource: AVB17221ADPTalkerCapabilities { get }     static var HasSMPTESource: AVB17221ADPTalkerCapabilities { get }     static var HasMIDISource: AVB17221ADPTalkerCapabilities { get }     static var HasAudioSource: AVB17221ADPTalkerCapabilities { get }     static var HasVideoSource: AVB17221ADPTalkerCapabilities { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct AVB17221ADPTalkerCapabilities : RawOptionSetType {     init(_ rawValue: UInt16)     init(rawValue rawValue: UInt16)     static var Implemented: AVB17221ADPTalkerCapabilities { get }     static var HasOtherSource: AVB17221ADPTalkerCapabilities { get }     static var HasControlSource: AVB17221ADPTalkerCapabilities { get }     static var HasMediaClockSource: AVB17221ADPTalkerCapabilities { get }     static var HasSMPTESource: AVB17221ADPTalkerCapabilities { get }     static var HasMIDISource: AVB17221ADPTalkerCapabilities { get }     static var HasAudioSource: AVB17221ADPTalkerCapabilities { get }     static var HasVideoSource: AVB17221ADPTalkerCapabilities { get } } ``` | RawOptionSetType | OS X 10.8 |

Modified AVB17221ADPTalkerCapabilities.init(_: UInt16)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt16) ``` |
| To | ``` init(_ rawValue: UInt16) ``` |

Modified AVB17221AECPAEMMessage

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVB17221AECPAEMMessage.commandSpecificData

|  | Declaration |
| --- | --- |
| From | ``` var commandSpecificData: NSData! ``` |
| To | ``` @NSCopying var commandSpecificData: NSData! ``` |

Modified AVB17221AECPAEMMessage.controllerRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221AECPAVCMessage

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVB17221AECPAVCMessage.commandResponse

|  | Declaration |
| --- | --- |
| From | ``` var commandResponse: NSData! ``` |
| To | ``` @NSCopying var commandResponse: NSData! ``` |

Modified AVB17221AECPAddressAccessMessage

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVB17221AECPAddressAccessTLV

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVB17221AECPAddressAccessTLV.memoryData

|  | Declaration |
| --- | --- |
| From | ``` var memoryData: NSData! ``` |
| To | ``` @NSCopying var memoryData: NSData! ``` |

Modified AVB17221AECPAddressAccessTLVMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221AECPInterface

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVB17221AECPInterface.init(interface: AVBInterface!)

|  | Declaration |
| --- | --- |
| From | ``` init(interface anInterface: AVBInterface!) -> AVB17221AECPInterface ``` |
| To | ``` init!(interface anInterface: AVBInterface!) -> AVB17221AECPInterface ``` |

Modified AVB17221AECPInterface.init(interfaceNamed: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(interfaceNamed anInterfaceName: String!) -> AVB17221AECPInterface ``` |
| To | ``` init!(interfaceNamed anInterfaceName: String!) -> AVB17221AECPInterface ``` |

Modified AVB17221AECPInterface.removeHandlerForEntityID(UInt64)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221AECPInterface.setHandler(AVB17221AECPClient!, forEntityID: UInt64) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221AECPMessage

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVB17221AECPMessage.controllerEntityID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221AECPMessage.sourceMAC

|  | Declaration |
| --- | --- |
| From | ``` var sourceMAC: AVBMACAddress! ``` |
| To | ``` @NSCopying var sourceMAC: AVBMACAddress! ``` |

Modified AVB17221AECPMessage.targetEntityID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221AECPMessageType [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVB17221AECPStatusCode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVB17221AECPVendorMessage

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVB17221AECPVendorMessage.protocolSpecificData

|  | Declaration |
| --- | --- |
| From | ``` var protocolSpecificData: NSData! ``` |
| To | ``` @NSCopying var protocolSpecificData: NSData! ``` |

Modified AVB17221AEMCommandType [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVB17221Entity

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVB17221Entity.entityDiscovery

|  | Declaration |
| --- | --- |
| From | ``` var entityDiscovery: AVB17221EntityDiscovery! ``` |
| To | ``` unowned(unsafe) var entityDiscovery: AVB17221EntityDiscovery! ``` |

Modified AVB17221Entity.entityID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221Entity.entityModelID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221Entity.gPTPDomainNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221Entity.gPTPGrandmasterID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221Entity.identifyControlIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221Entity.interfaceIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221EntityDiscovery

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVB17221EntityDiscovery.changeEntityWithEntityID(UInt64, toNewGPTPGrandmasterID: UInt64, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221EntityDiscovery.discoveryDelegate

|  | Declaration |
| --- | --- |
| From | ``` var discoveryDelegate: AVB17221EntityDiscoveryDelegate! ``` |
| To | ``` unowned(unsafe) var discoveryDelegate: AVB17221EntityDiscoveryDelegate! ``` |

Modified AVB17221EntityDiscovery.interface

|  | Declaration |
| --- | --- |
| From | ``` var interface: AVBInterface! { get } ``` |
| To | ``` unowned(unsafe) var interface: AVBInterface! { get } ``` |

Modified AVB17221EntityDiscovery.init(interfaceName: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(interfaceName anInterfaceName: String!) ``` |
| To | ``` init!(interfaceName anInterfaceName: String!) ``` |

Modified AVB17221EntityPropertyChanged [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct AVB17221EntityPropertyChanged : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var TimeToLive: AVB17221EntityPropertyChanged { get }     static var GUID: AVB17221EntityPropertyChanged { get }     static var EntityID: AVB17221EntityPropertyChanged { get }     static var VendorID: AVB17221EntityPropertyChanged { get }     static var ModelID: AVB17221EntityPropertyChanged { get }     static var EntityCapabilities: AVB17221EntityPropertyChanged { get }     static var TalkerStreamSources: AVB17221EntityPropertyChanged { get }     static var TalkerCapabilities: AVB17221EntityPropertyChanged { get }     static var ListenerStreamSinks: AVB17221EntityPropertyChanged { get }     static var ListenerCapabilities: AVB17221EntityPropertyChanged { get }     static var ControllerCapabilities: AVB17221EntityPropertyChanged { get }     static var AvailableIndex: AVB17221EntityPropertyChanged { get }     static var ASGrandmasterID: AVB17221EntityPropertyChanged { get }     static var GPTPGrandmasterID: AVB17221EntityPropertyChanged { get }     static var MACAddress: AVB17221EntityPropertyChanged { get }     static var AssociationID: AVB17221EntityPropertyChanged { get }     static var EntityType: AVB17221EntityPropertyChanged { get }     static var IdentifyControlIndex: AVB17221EntityPropertyChanged { get }     static var InterfaceIndex: AVB17221EntityPropertyChanged { get }     static var GPTPDomainNumber: AVB17221EntityPropertyChanged { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct AVB17221EntityPropertyChanged : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var TimeToLive: AVB17221EntityPropertyChanged { get }     static var GUID: AVB17221EntityPropertyChanged { get }     static var EntityID: AVB17221EntityPropertyChanged { get }     static var VendorID: AVB17221EntityPropertyChanged { get }     static var ModelID: AVB17221EntityPropertyChanged { get }     static var EntityCapabilities: AVB17221EntityPropertyChanged { get }     static var TalkerStreamSources: AVB17221EntityPropertyChanged { get }     static var TalkerCapabilities: AVB17221EntityPropertyChanged { get }     static var ListenerStreamSinks: AVB17221EntityPropertyChanged { get }     static var ListenerCapabilities: AVB17221EntityPropertyChanged { get }     static var ControllerCapabilities: AVB17221EntityPropertyChanged { get }     static var AvailableIndex: AVB17221EntityPropertyChanged { get }     static var ASGrandmasterID: AVB17221EntityPropertyChanged { get }     static var GPTPGrandmasterID: AVB17221EntityPropertyChanged { get }     static var MACAddress: AVB17221EntityPropertyChanged { get }     static var AssociationID: AVB17221EntityPropertyChanged { get }     static var EntityType: AVB17221EntityPropertyChanged { get }     static var IdentifyControlIndex: AVB17221EntityPropertyChanged { get }     static var InterfaceIndex: AVB17221EntityPropertyChanged { get }     static var GPTPDomainNumber: AVB17221EntityPropertyChanged { get } } ``` | RawOptionSetType | OS X 10.8 |

Modified AVB17221EntityPropertyChanged.EntityID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221EntityPropertyChanged.GPTPDomainNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221EntityPropertyChanged.GPTPGrandmasterID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221EntityPropertyChanged.IdentifyControlIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221EntityPropertyChanged.InterfaceIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVB17221EntityPropertyChanged.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified AVB1722ControlInterface

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVB1722ControlInterface.interface

|  | Declaration |
| --- | --- |
| From | ``` var interface: AVBInterface! { get } ``` |
| To | ``` unowned(unsafe) var interface: AVBInterface! { get } ``` |

Modified AVB1722ControlInterface.init(interfaceName: String!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(interfaceName anInterfaceName: String!) ``` | OS X 10.10 |
| To | ``` init!(interfaceName anInterfaceName: String!) ``` | OS X 10.9 |

Modified AVBEthernetInterface

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVBInterface

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVBInterface.init(interfaceName: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(interfaceName anInterfaceName: String!) ``` |
| To | ``` init!(interfaceName anInterfaceName: String!) ``` |

Modified AVBMACAddress

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVBMACAddress.bytes

|  | Declaration |
| --- | --- |
| From | ``` var bytes: ConstUnsafePointer<UInt8> { get } ``` |
| To | ``` var bytes: UnsafePointer<UInt8> { get } ``` |

Modified AVBMACAddress.init(bytes: UnsafeMutablePointer<UInt8>)

|  | Declaration |
| --- | --- |
| From | ``` init(bytes bytes: UnsafePointer<UInt8>) ``` |
| To | ``` init!(bytes bytes: UnsafeMutablePointer<UInt8>) ``` |

Modified AVBMACAddress.dataRepresentation

|  | Declaration |
| --- | --- |
| From | ``` var dataRepresentation: NSData! ``` |
| To | ``` @NSCopying var dataRepresentation: NSData! ``` |

Modified AVBErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let AVBErrorDomain: NSString! ``` |
| To | ``` let AVBErrorDomain: String ``` |

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
