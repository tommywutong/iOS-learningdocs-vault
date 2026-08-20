---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/AudioVideoBridging.html
archived_at: '2026-07-18T02:53:21.087103Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# AudioVideoBridging Changes for Swift

### AudioVideoBridging

Removed AVB17221ACMPFlags.init(_: UInt16)Removed AVB17221ACMPInterface.init(interface: AVBInterface!) -> AVB17221ACMPInterfaceRemoved AVB17221ADPControllerCapabilities.init(_: UInt32)Removed AVB17221ADPListenerCapabilities.init(_: UInt16)Removed AVB17221ADPTalkerCapabilities.init(_: UInt16)Removed AVB17221AECPInterface.init(interface: AVBInterface!) -> AVB17221AECPInterfaceRemoved AVB17221EntityPropertyChanged.init(_: UInt)Added AVB17221ADPEntityCapabilities.EFUModeAdded AVB17221ADPEntityCapabilities.GPTPSupportedAdded AVB17221AECPInterface.removeCommandHandlerForEntityID(_: UInt64)Added AVB17221AECPInterface.removeResponseHandlerForControllerEntityID(_: UInt64)Added AVB17221AECPInterface.setCommandHandler(_: AVB17221AECPClient, forEntityID: UInt64) -> BoolAdded AVB17221AECPInterface.setResponseHandler(_: AVB17221AECPClient, forControllerEntityID: UInt64) -> BoolAdded AVB17221AECPStatusCode.AddressAccessAddressInvalidAdded AVB17221AECPStatusCode.AddressAccessAddressTooHighAdded AVB17221AECPStatusCode.AddressAccessAddressTooLowAdded AVB17221AECPStatusCode.AddressAccessDataInvalidAdded AVB17221AECPStatusCode.AddressAccessTLVInvalidAdded AVB17221AECPStatusCode.AddressAccessUnsupportedAdded AVB17221AECPStatusCode.AVCFailureAdded AVB17221AECPStatusCode.StreamIsRunningAdded AVB1722ControlInterface.init(interface: AVBInterface)Added AVB_LEGACY_OBJC_RUNTIMEAdded AVB_MODERN_OBJC_RUNTIMEModified AVB17221ACMPClient

|  | Declaration |
| --- | --- |
| From | ``` protocol AVB17221ACMPClient {     func ACMPDidReceiveCommand(_ message: AVB17221ACMPMessage!, onInterface anInterface: AVB17221ACMPInterface!) -> Bool     func ACMPDidReceiveResponse(_ message: AVB17221ACMPMessage!, onInterface anInterface: AVB17221ACMPInterface!) -> Bool } ``` |
| To | ``` protocol AVB17221ACMPClient {     func ACMPDidReceiveCommand(_ message: AVB17221ACMPMessage, onInterface anInterface: AVB17221ACMPInterface) -> Bool     func ACMPDidReceiveResponse(_ message: AVB17221ACMPMessage, onInterface anInterface: AVB17221ACMPInterface) -> Bool } ``` |

Modified AVB17221ACMPClient.ACMPDidReceiveCommand(_: AVB17221ACMPMessage, onInterface: AVB17221ACMPInterface) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ACMPDidReceiveCommand(_ message: AVB17221ACMPMessage!, onInterface anInterface: AVB17221ACMPInterface!) -> Bool ``` | OS X 10.10 |
| To | ``` func ACMPDidReceiveCommand(_ message: AVB17221ACMPMessage, onInterface anInterface: AVB17221ACMPInterface) -> Bool ``` | OS X 10.8 |

Modified AVB17221ACMPClient.ACMPDidReceiveResponse(_: AVB17221ACMPMessage, onInterface: AVB17221ACMPInterface) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ACMPDidReceiveResponse(_ message: AVB17221ACMPMessage!, onInterface anInterface: AVB17221ACMPInterface!) -> Bool ``` | OS X 10.10 |
| To | ``` func ACMPDidReceiveResponse(_ message: AVB17221ACMPMessage, onInterface anInterface: AVB17221ACMPInterface) -> Bool ``` | OS X 10.8 |

Modified AVB17221ACMPFlags [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVB17221ACMPFlags : RawOptionSetType {     init(_ rawValue: UInt16)     init(rawValue rawValue: UInt16)     static var None: AVB17221ACMPFlags { get }     static var ClassB: AVB17221ACMPFlags { get }     static var FastConnect: AVB17221ACMPFlags { get }     static var SavedState: AVB17221ACMPFlags { get }     static var StreamingWait: AVB17221ACMPFlags { get }     static var SupportsEncrypted: AVB17221ACMPFlags { get }     static var EncryptedPDU: AVB17221ACMPFlags { get }     static var StreamingTalkerFailed: AVB17221ACMPFlags { get } } ``` | RawOptionSetType |
| To | ``` struct AVB17221ACMPFlags : OptionSetType {     init(rawValue rawValue: UInt16)     static var None: AVB17221ACMPFlags { get }     static var ClassB: AVB17221ACMPFlags { get }     static var FastConnect: AVB17221ACMPFlags { get }     static var SavedState: AVB17221ACMPFlags { get }     static var StreamingWait: AVB17221ACMPFlags { get }     static var SupportsEncrypted: AVB17221ACMPFlags { get }     static var EncryptedPDU: AVB17221ACMPFlags { get }     static var StreamingTalkerFailed: AVB17221ACMPFlags { get } } ``` | OptionSetType |

Modified AVB17221ACMPInterface

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221ACMPInterface : AVB1722ControlInterface {     @NSCopying var multicastDestinationAddress: AVBMACAddress!     init!(interface anInterface: AVBInterface!) -> AVB17221ACMPInterface     class func ACMPInterfaceWithInterface(_ anInterface: AVBInterface!) -> AVB17221ACMPInterface!     init!(interfaceNamed anInterfaceName: String!) -> AVB17221ACMPInterface     class func ACMPInterfaceWithInterfaceNamed(_ anInterfaceName: String!) -> AVB17221ACMPInterface!     func setHandler(_ handler: AVB17221ACMPClient!, forGUID targetGUID: UInt64) -> Bool     func setHandler(_ handler: AVB17221ACMPClient!, forEntityID targetEntityID: UInt64) -> Bool     func removeHandlerForGUID(_ targetGUID: UInt64)     func removeHandlerForEntityID(_ targetEntityID: UInt64)     func sendACMPResponseMessage(_ message: AVB17221ACMPMessage!, error error: NSErrorPointer) -> Bool     func sendACMPCommandMessage(_ message: AVB17221ACMPMessage!, completionHandler completionHandler: AVB17221ACMPInterfaceCompletion!) -> Bool } ``` |
| To | ``` class AVB17221ACMPInterface : AVB1722ControlInterface {     @NSCopying var multicastDestinationAddress: AVBMACAddress { get }      init(interface anInterface: AVBInterface)     class func ACMPInterfaceWithInterface(_ anInterface: AVBInterface) -> AVB17221ACMPInterface      init(interfaceNamed anInterfaceName: String)     class func ACMPInterfaceWithInterfaceNamed(_ anInterfaceName: String) -> AVB17221ACMPInterface     func setHandler(_ handler: AVB17221ACMPClient, forGUID targetGUID: UInt64) -> Bool     func setHandler(_ handler: AVB17221ACMPClient, forEntityID targetEntityID: UInt64) -> Bool     func removeHandlerForGUID(_ targetGUID: UInt64)     func removeHandlerForEntityID(_ targetEntityID: UInt64)     func sendACMPResponseMessage(_ message: AVB17221ACMPMessage) throws     func sendACMPCommandMessage(_ message: AVB17221ACMPMessage, completionHandler completionHandler: AVB17221ACMPInterfaceCompletion) -> Bool } ``` |

Modified AVB17221ACMPInterface.init(interfaceNamed: String)

|  | Declaration |
| --- | --- |
| From | ``` init!(interfaceNamed anInterfaceName: String!) -> AVB17221ACMPInterface ``` |
| To | ``` init(interfaceNamed anInterfaceName: String) ``` |

Modified AVB17221ACMPInterface.multicastDestinationAddress

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var multicastDestinationAddress: AVBMACAddress! ``` |
| To | ``` @NSCopying var multicastDestinationAddress: AVBMACAddress { get } ``` |

Modified AVB17221ACMPInterface.sendACMPCommandMessage(_: AVB17221ACMPMessage, completionHandler: AVB17221ACMPInterfaceCompletion) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func sendACMPCommandMessage(_ message: AVB17221ACMPMessage!, completionHandler completionHandler: AVB17221ACMPInterfaceCompletion!) -> Bool ``` |
| To | ``` func sendACMPCommandMessage(_ message: AVB17221ACMPMessage, completionHandler completionHandler: AVB17221ACMPInterfaceCompletion) -> Bool ``` |

Modified AVB17221ACMPInterface.sendACMPResponseMessage(_: AVB17221ACMPMessage) throws

|  | Declaration |
| --- | --- |
| From | ``` func sendACMPResponseMessage(_ message: AVB17221ACMPMessage!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func sendACMPResponseMessage(_ message: AVB17221ACMPMessage) throws ``` |

Modified AVB17221ACMPInterface.setHandler(_: AVB17221ACMPClient, forEntityID: UInt64) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func setHandler(_ handler: AVB17221ACMPClient!, forEntityID targetEntityID: UInt64) -> Bool ``` |
| To | ``` func setHandler(_ handler: AVB17221ACMPClient, forEntityID targetEntityID: UInt64) -> Bool ``` |

Modified AVB17221ACMPMessage

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221ACMPMessage : NSObject, NSCopying {     var messageType: AVB17221ACMPMessageType     var status: AVB17221ACMPStatusCode     var streamID: UInt64     var controllerGUID: UInt64     var controllerEntityID: UInt64     var talkerGUID: UInt64     var talkerEntityID: UInt64     var listenerGUID: UInt64     var listenerEntityID: UInt64     var talkerUniqueID: UInt16     var listenerUniqueID: UInt16     @NSCopying var destinationMAC: AVBMACAddress!     var connectionCount: UInt16     var sequenceID: UInt16     var flags: AVB17221ACMPFlags     var vlanID: UInt16     @NSCopying var sourceMAC: AVBMACAddress! } ``` |
| To | ``` class AVB17221ACMPMessage : NSObject, NSCopying {     var messageType: AVB17221ACMPMessageType     var status: AVB17221ACMPStatusCode     var streamID: UInt64     var controllerGUID: UInt64     var controllerEntityID: UInt64     var talkerGUID: UInt64     var talkerEntityID: UInt64     var listenerGUID: UInt64     var listenerEntityID: UInt64     var talkerUniqueID: UInt16     var listenerUniqueID: UInt16     @NSCopying var destinationMAC: AVBMACAddress?     var connectionCount: UInt16     var sequenceID: UInt16     var flags: AVB17221ACMPFlags     var vlanID: UInt16     @NSCopying var sourceMAC: AVBMACAddress? } ``` |

Modified AVB17221ACMPMessage.destinationMAC

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var destinationMAC: AVBMACAddress! ``` |
| To | ``` @NSCopying var destinationMAC: AVBMACAddress? ``` |

Modified AVB17221ACMPMessage.sourceMAC

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var sourceMAC: AVBMACAddress! ``` |
| To | ``` @NSCopying var sourceMAC: AVBMACAddress? ``` |

Modified AVB17221ACMPMessageType [enum]

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt8 |

Modified AVB17221ACMPStatusCode [enum]

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt8 |

Modified AVB17221ADPControllerCapabilities [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVB17221ADPControllerCapabilities : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var Implemented: AVB17221ADPControllerCapabilities { get }     static var HasLayer3Proxy: AVB17221ADPControllerCapabilities { get } } ``` | RawOptionSetType |
| To | ``` struct AVB17221ADPControllerCapabilities : OptionSetType {     init(rawValue rawValue: UInt32)     static var Implemented: AVB17221ADPControllerCapabilities { get }     static var HasLayer3Proxy: AVB17221ADPControllerCapabilities { get } } ``` | OptionSetType |

Modified AVB17221ADPEntityCapabilities [enum]

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum AVB17221ADPEntityCapabilities : UInt32 {     case DFUMode     case AddressAccessSupported     case GatewayEntity     case AEMSupported     case LegacyAVC     case AssociationIDSupported     case AssociationIDValid     case VendorUniqueSupported     case ClassASupported     case ClassBSupported     case ASSupported     case AEMAuthenticationSupported     case AEMAuthenticationRequired     case AEMPersistentAcquireSupported     case AEMIdenitifyControlIndexValid     case AEMInterfaceIndexValid     case GeneralControllerIgnore     case EntityNotReady } ``` | -- |
| To | ``` enum AVB17221ADPEntityCapabilities : UInt32 {     case DFUMode     static var EFUMode: AVB17221ADPEntityCapabilities { get }     case AddressAccessSupported     case GatewayEntity     case AEMSupported     case LegacyAVC     case AssociationIDSupported     case AssociationIDValid     case VendorUniqueSupported     case ClassASupported     case ClassBSupported     case ASSupported     static var GPTPSupported: AVB17221ADPEntityCapabilities { get }     case AEMAuthenticationSupported     case AEMAuthenticationRequired     case AEMPersistentAcquireSupported     case AEMIdenitifyControlIndexValid     case AEMInterfaceIndexValid     case GeneralControllerIgnore     case EntityNotReady } ``` | UInt32 |

Modified AVB17221ADPListenerCapabilities [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVB17221ADPListenerCapabilities : RawOptionSetType {     init(_ rawValue: UInt16)     init(rawValue rawValue: UInt16)     static var Implemented: AVB17221ADPListenerCapabilities { get }     static var HasOtherSink: AVB17221ADPListenerCapabilities { get }     static var HasControlSink: AVB17221ADPListenerCapabilities { get }     static var HasMediaClockSink: AVB17221ADPListenerCapabilities { get }     static var HasSMPTESink: AVB17221ADPListenerCapabilities { get }     static var HasMIDISink: AVB17221ADPListenerCapabilities { get }     static var HasAudioSink: AVB17221ADPListenerCapabilities { get }     static var HasVideoSink: AVB17221ADPListenerCapabilities { get } } ``` | RawOptionSetType |
| To | ``` struct AVB17221ADPListenerCapabilities : OptionSetType {     init(rawValue rawValue: UInt16)     static var Implemented: AVB17221ADPListenerCapabilities { get }     static var HasOtherSink: AVB17221ADPListenerCapabilities { get }     static var HasControlSink: AVB17221ADPListenerCapabilities { get }     static var HasMediaClockSink: AVB17221ADPListenerCapabilities { get }     static var HasSMPTESink: AVB17221ADPListenerCapabilities { get }     static var HasMIDISink: AVB17221ADPListenerCapabilities { get }     static var HasAudioSink: AVB17221ADPListenerCapabilities { get }     static var HasVideoSink: AVB17221ADPListenerCapabilities { get } } ``` | OptionSetType |

Modified AVB17221ADPTalkerCapabilities [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVB17221ADPTalkerCapabilities : RawOptionSetType {     init(_ rawValue: UInt16)     init(rawValue rawValue: UInt16)     static var Implemented: AVB17221ADPTalkerCapabilities { get }     static var HasOtherSource: AVB17221ADPTalkerCapabilities { get }     static var HasControlSource: AVB17221ADPTalkerCapabilities { get }     static var HasMediaClockSource: AVB17221ADPTalkerCapabilities { get }     static var HasSMPTESource: AVB17221ADPTalkerCapabilities { get }     static var HasMIDISource: AVB17221ADPTalkerCapabilities { get }     static var HasAudioSource: AVB17221ADPTalkerCapabilities { get }     static var HasVideoSource: AVB17221ADPTalkerCapabilities { get } } ``` | RawOptionSetType |
| To | ``` struct AVB17221ADPTalkerCapabilities : OptionSetType {     init(rawValue rawValue: UInt16)     static var Implemented: AVB17221ADPTalkerCapabilities { get }     static var HasOtherSource: AVB17221ADPTalkerCapabilities { get }     static var HasControlSource: AVB17221ADPTalkerCapabilities { get }     static var HasMediaClockSource: AVB17221ADPTalkerCapabilities { get }     static var HasSMPTESource: AVB17221ADPTalkerCapabilities { get }     static var HasMIDISource: AVB17221ADPTalkerCapabilities { get }     static var HasAudioSource: AVB17221ADPTalkerCapabilities { get }     static var HasVideoSource: AVB17221ADPTalkerCapabilities { get } } ``` | OptionSetType |

Modified AVB17221AECPAddressAccessMessage

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221AECPAddressAccessMessage : AVB17221AECPMessage {     var tlvs: [AnyObject]!     class func commandMessage() -> AVB17221AECPAddressAccessMessage!     class func responseMessage() -> AVB17221AECPAddressAccessMessage! } ``` |
| To | ``` class AVB17221AECPAddressAccessMessage : AVB17221AECPMessage {     var tlvs: [AVB17221AECPAddressAccessTLV]?     class func commandMessage() -> AVB17221AECPAddressAccessMessage     class func responseMessage() -> AVB17221AECPAddressAccessMessage } ``` |

Modified AVB17221AECPAddressAccessMessage.commandMessage() -> AVB17221AECPAddressAccessMessage [class]

|  | Declaration |
| --- | --- |
| From | ``` class func commandMessage() -> AVB17221AECPAddressAccessMessage! ``` |
| To | ``` class func commandMessage() -> AVB17221AECPAddressAccessMessage ``` |

Modified AVB17221AECPAddressAccessMessage.responseMessage() -> AVB17221AECPAddressAccessMessage [class]

|  | Declaration |
| --- | --- |
| From | ``` class func responseMessage() -> AVB17221AECPAddressAccessMessage! ``` |
| To | ``` class func responseMessage() -> AVB17221AECPAddressAccessMessage ``` |

Modified AVB17221AECPAddressAccessMessage.tlvs

|  | Declaration |
| --- | --- |
| From | ``` var tlvs: [AnyObject]! ``` |
| To | ``` var tlvs: [AVB17221AECPAddressAccessTLV]? ``` |

Modified AVB17221AECPAddressAccessTLV

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221AECPAddressAccessTLV : NSObject {     var mode: AVB17221AECPAddressAccessTLVMode     var address: UInt64     @NSCopying var memoryData: NSData! } ``` |
| To | ``` class AVB17221AECPAddressAccessTLV : NSObject {     var mode: AVB17221AECPAddressAccessTLVMode     var address: UInt64     @NSCopying var memoryData: NSData? } ``` |

Modified AVB17221AECPAddressAccessTLV.memoryData

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var memoryData: NSData! ``` |
| To | ``` @NSCopying var memoryData: NSData? ``` |

Modified AVB17221AECPAddressAccessTLVMode [enum]

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt8 |

Modified AVB17221AECPAEMMessage

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221AECPAEMMessage : AVB17221AECPMessage {     var commandType: AVB17221AEMCommandType     var unsolicited: Bool     var controllerRequest: Bool     @NSCopying var commandSpecificData: NSData!     class func commandMessage() -> AVB17221AECPAEMMessage!     class func responseMessage() -> AVB17221AECPAEMMessage! } ``` |
| To | ``` class AVB17221AECPAEMMessage : AVB17221AECPMessage {     var commandType: AVB17221AEMCommandType     var unsolicited: Bool     var controllerRequest: Bool     @NSCopying var commandSpecificData: NSData?     class func commandMessage() -> AVB17221AECPAEMMessage     class func responseMessage() -> AVB17221AECPAEMMessage } ``` |

Modified AVB17221AECPAEMMessage.commandMessage() -> AVB17221AECPAEMMessage [class]

|  | Declaration |
| --- | --- |
| From | ``` class func commandMessage() -> AVB17221AECPAEMMessage! ``` |
| To | ``` class func commandMessage() -> AVB17221AECPAEMMessage ``` |

Modified AVB17221AECPAEMMessage.commandSpecificData

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var commandSpecificData: NSData! ``` |
| To | ``` @NSCopying var commandSpecificData: NSData? ``` |

Modified AVB17221AECPAEMMessage.responseMessage() -> AVB17221AECPAEMMessage [class]

|  | Declaration |
| --- | --- |
| From | ``` class func responseMessage() -> AVB17221AECPAEMMessage! ``` |
| To | ``` class func responseMessage() -> AVB17221AECPAEMMessage ``` |

Modified AVB17221AECPAVCMessage

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221AECPAVCMessage : AVB17221AECPMessage {     @NSCopying var commandResponse: NSData! } ``` |
| To | ``` class AVB17221AECPAVCMessage : AVB17221AECPMessage {     @NSCopying var commandResponse: NSData? } ``` |

Modified AVB17221AECPAVCMessage.commandResponse

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var commandResponse: NSData! ``` |
| To | ``` @NSCopying var commandResponse: NSData? ``` |

Modified AVB17221AECPClient

|  | Declaration |
| --- | --- |
| From | ``` protocol AVB17221AECPClient {     func AECPDidReceiveCommand(_ message: AVB17221AECPMessage!, onInterface anInterface: AVB17221AECPInterface!) -> Bool     func AECPDidReceiveResponse(_ message: AVB17221AECPMessage!, onInterface anInterface: AVB17221AECPInterface!) -> Bool } ``` |
| To | ``` protocol AVB17221AECPClient {     func AECPDidReceiveCommand(_ message: AVB17221AECPMessage, onInterface anInterface: AVB17221AECPInterface) -> Bool     func AECPDidReceiveResponse(_ message: AVB17221AECPMessage, onInterface anInterface: AVB17221AECPInterface) -> Bool } ``` |

Modified AVB17221AECPClient.AECPDidReceiveCommand(_: AVB17221AECPMessage, onInterface: AVB17221AECPInterface) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AECPDidReceiveCommand(_ message: AVB17221AECPMessage!, onInterface anInterface: AVB17221AECPInterface!) -> Bool ``` | OS X 10.10 |
| To | ``` func AECPDidReceiveCommand(_ message: AVB17221AECPMessage, onInterface anInterface: AVB17221AECPInterface) -> Bool ``` | OS X 10.8 |

Modified AVB17221AECPClient.AECPDidReceiveResponse(_: AVB17221AECPMessage, onInterface: AVB17221AECPInterface) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AECPDidReceiveResponse(_ message: AVB17221AECPMessage!, onInterface anInterface: AVB17221AECPInterface!) -> Bool ``` | OS X 10.10 |
| To | ``` func AECPDidReceiveResponse(_ message: AVB17221AECPMessage, onInterface anInterface: AVB17221AECPInterface) -> Bool ``` | OS X 10.8 |

Modified AVB17221AECPInterface

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221AECPInterface : AVB1722ControlInterface {     init!(interface anInterface: AVBInterface!) -> AVB17221AECPInterface     class func AECPInterfaceWithInterface(_ anInterface: AVBInterface!) -> AVB17221AECPInterface!     init!(interfaceNamed anInterfaceName: String!) -> AVB17221AECPInterface     class func AECPInterfaceWithInterfaceNamed(_ anInterfaceName: String!) -> AVB17221AECPInterface!     func setHandler(_ handler: AVB17221AECPClient!, forGUID targetGUID: UInt64) -> Bool     func setHandler(_ handler: AVB17221AECPClient!, forEntityID targetEntityID: UInt64) -> Bool     func removeHandlerForGUID(_ targetGUID: UInt64)     func removeHandlerForEntityID(_ targetEntityID: UInt64)     func sendCommand(_ message: AVB17221AECPMessage!, toMACAddress destMAC: AVBMACAddress!, completionHandler completionHandler: AVB17221AECPInterfaceCompletion!) -> Bool     func sendResponse(_ message: AVB17221AECPMessage!, toMACAddress destMAC: AVBMACAddress!, error error: NSErrorPointer) -> Bool } ``` |
| To | ``` class AVB17221AECPInterface : AVB1722ControlInterface {      init?(interface anInterface: AVBInterface)     class func AECPInterfaceWithInterface(_ anInterface: AVBInterface) -> AVB17221AECPInterface?      init?(interfaceNamed anInterfaceName: String)     class func AECPInterfaceWithInterfaceNamed(_ anInterfaceName: String) -> AVB17221AECPInterface?     func setHandler(_ handler: AVB17221AECPClient, forGUID targetGUID: UInt64) -> Bool     func setHandler(_ handler: AVB17221AECPClient, forEntityID targetEntityID: UInt64) -> Bool     func removeHandlerForGUID(_ targetGUID: UInt64)     func removeHandlerForEntityID(_ targetEntityID: UInt64)     func setCommandHandler(_ handler: AVB17221AECPClient, forEntityID targetEntityID: UInt64) -> Bool     func removeCommandHandlerForEntityID(_ targetEntityID: UInt64)     func setResponseHandler(_ handler: AVB17221AECPClient, forControllerEntityID controllerEntityID: UInt64) -> Bool     func removeResponseHandlerForControllerEntityID(_ controllerEntityID: UInt64)     func sendCommand(_ message: AVB17221AECPMessage, toMACAddress destMAC: AVBMACAddress, completionHandler completionHandler: AVB17221AECPInterfaceCompletion) -> Bool     func sendResponse(_ message: AVB17221AECPMessage, toMACAddress destMAC: AVBMACAddress) throws } ``` |

Modified AVB17221AECPInterface.init(interfaceNamed: String)

|  | Declaration |
| --- | --- |
| From | ``` init!(interfaceNamed anInterfaceName: String!) -> AVB17221AECPInterface ``` |
| To | ``` init?(interfaceNamed anInterfaceName: String) ``` |

Modified AVB17221AECPInterface.removeHandlerForEntityID(_: UInt64)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified AVB17221AECPInterface.sendCommand(_: AVB17221AECPMessage, toMACAddress: AVBMACAddress, completionHandler: AVB17221AECPInterfaceCompletion) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func sendCommand(_ message: AVB17221AECPMessage!, toMACAddress destMAC: AVBMACAddress!, completionHandler completionHandler: AVB17221AECPInterfaceCompletion!) -> Bool ``` |
| To | ``` func sendCommand(_ message: AVB17221AECPMessage, toMACAddress destMAC: AVBMACAddress, completionHandler completionHandler: AVB17221AECPInterfaceCompletion) -> Bool ``` |

Modified AVB17221AECPInterface.sendResponse(_: AVB17221AECPMessage, toMACAddress: AVBMACAddress) throws

|  | Declaration |
| --- | --- |
| From | ``` func sendResponse(_ message: AVB17221AECPMessage!, toMACAddress destMAC: AVBMACAddress!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func sendResponse(_ message: AVB17221AECPMessage, toMACAddress destMAC: AVBMACAddress) throws ``` |

Modified AVB17221AECPInterface.setHandler(_: AVB17221AECPClient, forEntityID: UInt64) -> Bool

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func setHandler(_ handler: AVB17221AECPClient!, forEntityID targetEntityID: UInt64) -> Bool ``` | -- |
| To | ``` func setHandler(_ handler: AVB17221AECPClient, forEntityID targetEntityID: UInt64) -> Bool ``` | OS X 10.11 |

Modified AVB17221AECPMessage

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221AECPMessage : NSObject, NSCopying {     var messageType: AVB17221AECPMessageType     var status: AVB17221AECPStatusCode     var targetGUID: UInt64     var targetEntityID: UInt64     var controllerGUID: UInt64     var controllerEntityID: UInt64     var sequenceID: UInt16     @NSCopying var sourceMAC: AVBMACAddress! } ``` |
| To | ``` class AVB17221AECPMessage : NSObject, NSCopying {     var messageType: AVB17221AECPMessageType     var status: AVB17221AECPStatusCode     var targetGUID: UInt64     var targetEntityID: UInt64     var controllerGUID: UInt64     var controllerEntityID: UInt64     var sequenceID: UInt16     @NSCopying var sourceMAC: AVBMACAddress } ``` |

Modified AVB17221AECPMessage.sourceMAC

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var sourceMAC: AVBMACAddress! ``` |
| To | ``` @NSCopying var sourceMAC: AVBMACAddress ``` |

Modified AVB17221AECPMessageType [enum]

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt8 |

Modified AVB17221AECPStatusCode [enum]

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum AVB17221AECPStatusCode : UInt8 {     case Success     case NotImplemented     case NoSuchDescriptor     case EntityLocked     case EntityAcquired     case NotAuthorized     case InsufficientPrivileges     case BadArguments     case NoResources     case InProgress     case EntityMisbehaving     case NotSupported } ``` | -- |
| To | ``` enum AVB17221AECPStatusCode : UInt8 {     case Success     case NotImplemented     case NoSuchDescriptor     case EntityLocked     case EntityAcquired     case NotAuthorized     case InsufficientPrivileges     case BadArguments     case NoResources     case InProgress     case EntityMisbehaving     case NotSupported     case StreamIsRunning     static var AddressAccessAddressTooLow: AVB17221AECPStatusCode { get }     static var AddressAccessAddressTooHigh: AVB17221AECPStatusCode { get }     static var AddressAccessAddressInvalid: AVB17221AECPStatusCode { get }     static var AddressAccessTLVInvalid: AVB17221AECPStatusCode { get }     static var AddressAccessDataInvalid: AVB17221AECPStatusCode { get }     static var AddressAccessUnsupported: AVB17221AECPStatusCode { get }     static var AVCFailure: AVB17221AECPStatusCode { get } } ``` | UInt8 |

Modified AVB17221AECPVendorMessage

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221AECPVendorMessage : AVB17221AECPMessage {     var protocolID: UInt64     @NSCopying var protocolSpecificData: NSData! } ``` |
| To | ``` class AVB17221AECPVendorMessage : AVB17221AECPMessage {     var protocolID: UInt64     @NSCopying var protocolSpecificData: NSData? } ``` |

Modified AVB17221AECPVendorMessage.protocolSpecificData

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var protocolSpecificData: NSData! ``` |
| To | ``` @NSCopying var protocolSpecificData: NSData? ``` |

Modified AVB17221AEMCommandType [enum]

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt16 |

Modified AVB17221Entity

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221Entity : NSObject {     var localEntity: Bool     var timeToLive: UInt8     var guid: UInt64     var entityID: UInt64     var vendorID: UInt32     var modelID: UInt32     var entityModelID: UInt64     var entityCapabilities: AVB17221ADPEntityCapabilities     var talkerStreamSources: UInt16     var talkerCapabilities: AVB17221ADPTalkerCapabilities     var listenerStreamSinks: UInt16     var listenerCapabilities: AVB17221ADPListenerCapabilities     var controllerCapabilities: AVB17221ADPControllerCapabilities     var availableIndex: UInt32     var asGrandmasterID: UInt64     var gPTPGrandmasterID: UInt64     var gPTPDomainNumber: UInt8     var identifyControlIndex: UInt16     var interfaceIndex: UInt16     var associationID: UInt64     var macAddresses: [AnyObject]!     unowned(unsafe) var entityDiscovery: AVB17221EntityDiscovery! } ``` |
| To | ``` class AVB17221Entity : NSObject {     var localEntity: Bool     var timeToLive: UInt8     var guid: UInt64     var entityID: UInt64     var vendorID: UInt32     var modelID: UInt32     var entityModelID: UInt64     var entityCapabilities: AVB17221ADPEntityCapabilities     var talkerStreamSources: UInt16     var talkerCapabilities: AVB17221ADPTalkerCapabilities     var listenerStreamSinks: UInt16     var listenerCapabilities: AVB17221ADPListenerCapabilities     var controllerCapabilities: AVB17221ADPControllerCapabilities     var availableIndex: UInt32     var asGrandmasterID: UInt64     var gPTPGrandmasterID: UInt64     var gPTPDomainNumber: UInt8     var identifyControlIndex: UInt16     var interfaceIndex: UInt16     var associationID: UInt64     var macAddresses: [AVBMACAddress]     unowned(unsafe) var entityDiscovery: AVB17221EntityDiscovery? } ``` |

Modified AVB17221Entity.entityDiscovery

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var entityDiscovery: AVB17221EntityDiscovery! ``` |
| To | ``` unowned(unsafe) var entityDiscovery: AVB17221EntityDiscovery? ``` |

Modified AVB17221Entity.macAddresses

|  | Declaration |
| --- | --- |
| From | ``` var macAddresses: [AnyObject]! ``` |
| To | ``` var macAddresses: [AVBMACAddress] ``` |

Modified AVB17221EntityDiscovery

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221EntityDiscovery : NSObject {     var interfaceName: String!     unowned(unsafe) var interface: AVBInterface! { get }     unowned(unsafe) var discoveryDelegate: AVB17221EntityDiscoveryDelegate!     init!(interfaceName anInterfaceName: String!)     func primeIterators()     func discoverEntities() -> Bool     func discoverEntity(_ entityID: UInt64) -> Bool     func addLocalEntity(_ anEntity: AVB17221Entity!, error error: NSErrorPointer) -> Bool     func removeLocalEntity(_ guid: UInt64, error error: NSErrorPointer) -> Bool     func changeEntityWithGUID(_ entityGUID: UInt64, toNewASGrandmasterID asGrandmasterID: UInt64, error error: NSErrorPointer) -> Bool     func changeEntityWithEntityID(_ entityID: UInt64, toNewGPTPGrandmasterID gPTPGrandmasterID: UInt64, error error: NSErrorPointer) -> Bool } ``` |
| To | ``` class AVB17221EntityDiscovery : NSObject {     var interfaceName: String     unowned(unsafe) var interface: AVBInterface? { get }     unowned(unsafe) var discoveryDelegate: AVB17221EntityDiscoveryDelegate?     init(interfaceName anInterfaceName: String)     func primeIterators()     func discoverEntities() -> Bool     func discoverEntity(_ entityID: UInt64) -> Bool     func addLocalEntity(_ anEntity: AVB17221Entity) throws     func removeLocalEntity(_ guid: UInt64) throws     func changeEntityWithGUID(_ entityGUID: UInt64, toNewASGrandmasterID asGrandmasterID: UInt64) throws     func changeEntityWithEntityID(_ entityID: UInt64, toNewGPTPGrandmasterID gPTPGrandmasterID: UInt64) throws } ``` |

Modified AVB17221EntityDiscovery.addLocalEntity(_: AVB17221Entity) throws

|  | Declaration |
| --- | --- |
| From | ``` func addLocalEntity(_ anEntity: AVB17221Entity!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func addLocalEntity(_ anEntity: AVB17221Entity) throws ``` |

Modified AVB17221EntityDiscovery.changeEntityWithEntityID(_: UInt64, toNewGPTPGrandmasterID: UInt64) throws

|  | Declaration |
| --- | --- |
| From | ``` func changeEntityWithEntityID(_ entityID: UInt64, toNewGPTPGrandmasterID gPTPGrandmasterID: UInt64, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func changeEntityWithEntityID(_ entityID: UInt64, toNewGPTPGrandmasterID gPTPGrandmasterID: UInt64) throws ``` |

Modified AVB17221EntityDiscovery.discoveryDelegate

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var discoveryDelegate: AVB17221EntityDiscoveryDelegate! ``` |
| To | ``` unowned(unsafe) var discoveryDelegate: AVB17221EntityDiscoveryDelegate? ``` |

Modified AVB17221EntityDiscovery.init(interfaceName: String)

|  | Declaration |
| --- | --- |
| From | ``` init!(interfaceName anInterfaceName: String!) ``` |
| To | ``` init(interfaceName anInterfaceName: String) ``` |

Modified AVB17221EntityDiscovery.interface

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var interface: AVBInterface! { get } ``` |
| To | ``` unowned(unsafe) var interface: AVBInterface? { get } ``` |

Modified AVB17221EntityDiscovery.interfaceName

|  | Declaration |
| --- | --- |
| From | ``` var interfaceName: String! ``` |
| To | ``` var interfaceName: String ``` |

Modified AVB17221EntityDiscovery.removeLocalEntity(_: UInt64) throws

|  | Declaration |
| --- | --- |
| From | ``` func removeLocalEntity(_ guid: UInt64, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func removeLocalEntity(_ guid: UInt64) throws ``` |

Modified AVB17221EntityDiscoveryDelegate

|  | Declaration |
| --- | --- |
| From | ``` protocol AVB17221EntityDiscoveryDelegate {     func didAddRemoteEntity(_ newEntity: AVB17221Entity!, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery!)     func didRemoveRemoteEntity(_ oldEntity: AVB17221Entity!, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery!)     func didRediscoverRemoteEntity(_ entity: AVB17221Entity!, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery!)     func didUpdateRemoteEntity(_ entity: AVB17221Entity!, changedProperties changedProperties: AVB17221EntityPropertyChanged, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery!)     func didAddLocalEntity(_ newEntity: AVB17221Entity!, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery!)     func didRemoveLocalEntity(_ oldEntity: AVB17221Entity!, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery!)     func didRediscoverLocalEntity(_ entity: AVB17221Entity!, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery!)     func didUpdateLocalEntity(_ entity: AVB17221Entity!, changedProperties changedProperties: AVB17221EntityPropertyChanged, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery!) } ``` |
| To | ``` protocol AVB17221EntityDiscoveryDelegate {     func didAddRemoteEntity(_ newEntity: AVB17221Entity, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery)     func didRemoveRemoteEntity(_ oldEntity: AVB17221Entity, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery)     func didRediscoverRemoteEntity(_ entity: AVB17221Entity, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery)     func didUpdateRemoteEntity(_ entity: AVB17221Entity, changedProperties changedProperties: AVB17221EntityPropertyChanged, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery)     func didAddLocalEntity(_ newEntity: AVB17221Entity, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery)     func didRemoveLocalEntity(_ oldEntity: AVB17221Entity, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery)     func didRediscoverLocalEntity(_ entity: AVB17221Entity, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery)     func didUpdateLocalEntity(_ entity: AVB17221Entity, changedProperties changedProperties: AVB17221EntityPropertyChanged, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery) } ``` |

Modified AVB17221EntityDiscoveryDelegate.didAddLocalEntity(_: AVB17221Entity, on17221EntityDiscovery: AVB17221EntityDiscovery)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func didAddLocalEntity(_ newEntity: AVB17221Entity!, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery!) ``` | OS X 10.10 |
| To | ``` func didAddLocalEntity(_ newEntity: AVB17221Entity, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery) ``` | OS X 10.8 |

Modified AVB17221EntityDiscoveryDelegate.didAddRemoteEntity(_: AVB17221Entity, on17221EntityDiscovery: AVB17221EntityDiscovery)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func didAddRemoteEntity(_ newEntity: AVB17221Entity!, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery!) ``` | OS X 10.10 |
| To | ``` func didAddRemoteEntity(_ newEntity: AVB17221Entity, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery) ``` | OS X 10.8 |

Modified AVB17221EntityDiscoveryDelegate.didRediscoverLocalEntity(_: AVB17221Entity, on17221EntityDiscovery: AVB17221EntityDiscovery)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func didRediscoverLocalEntity(_ entity: AVB17221Entity!, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery!) ``` | OS X 10.10 |
| To | ``` func didRediscoverLocalEntity(_ entity: AVB17221Entity, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery) ``` | OS X 10.8 |

Modified AVB17221EntityDiscoveryDelegate.didRediscoverRemoteEntity(_: AVB17221Entity, on17221EntityDiscovery: AVB17221EntityDiscovery)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func didRediscoverRemoteEntity(_ entity: AVB17221Entity!, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery!) ``` | OS X 10.10 |
| To | ``` func didRediscoverRemoteEntity(_ entity: AVB17221Entity, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery) ``` | OS X 10.8 |

Modified AVB17221EntityDiscoveryDelegate.didRemoveLocalEntity(_: AVB17221Entity, on17221EntityDiscovery: AVB17221EntityDiscovery)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func didRemoveLocalEntity(_ oldEntity: AVB17221Entity!, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery!) ``` | OS X 10.10 |
| To | ``` func didRemoveLocalEntity(_ oldEntity: AVB17221Entity, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery) ``` | OS X 10.8 |

Modified AVB17221EntityDiscoveryDelegate.didRemoveRemoteEntity(_: AVB17221Entity, on17221EntityDiscovery: AVB17221EntityDiscovery)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func didRemoveRemoteEntity(_ oldEntity: AVB17221Entity!, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery!) ``` | OS X 10.10 |
| To | ``` func didRemoveRemoteEntity(_ oldEntity: AVB17221Entity, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery) ``` | OS X 10.8 |

Modified AVB17221EntityDiscoveryDelegate.didUpdateLocalEntity(_: AVB17221Entity, changedProperties: AVB17221EntityPropertyChanged, on17221EntityDiscovery: AVB17221EntityDiscovery)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func didUpdateLocalEntity(_ entity: AVB17221Entity!, changedProperties changedProperties: AVB17221EntityPropertyChanged, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery!) ``` | OS X 10.10 |
| To | ``` func didUpdateLocalEntity(_ entity: AVB17221Entity, changedProperties changedProperties: AVB17221EntityPropertyChanged, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery) ``` | OS X 10.8 |

Modified AVB17221EntityDiscoveryDelegate.didUpdateRemoteEntity(_: AVB17221Entity, changedProperties: AVB17221EntityPropertyChanged, on17221EntityDiscovery: AVB17221EntityDiscovery)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func didUpdateRemoteEntity(_ entity: AVB17221Entity!, changedProperties changedProperties: AVB17221EntityPropertyChanged, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery!) ``` | OS X 10.10 |
| To | ``` func didUpdateRemoteEntity(_ entity: AVB17221Entity, changedProperties changedProperties: AVB17221EntityPropertyChanged, on17221EntityDiscovery entityDiscovery: AVB17221EntityDiscovery) ``` | OS X 10.8 |

Modified AVB17221EntityPropertyChanged [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVB17221EntityPropertyChanged : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var TimeToLive: AVB17221EntityPropertyChanged { get }     static var GUID: AVB17221EntityPropertyChanged { get }     static var EntityID: AVB17221EntityPropertyChanged { get }     static var VendorID: AVB17221EntityPropertyChanged { get }     static var ModelID: AVB17221EntityPropertyChanged { get }     static var EntityCapabilities: AVB17221EntityPropertyChanged { get }     static var TalkerStreamSources: AVB17221EntityPropertyChanged { get }     static var TalkerCapabilities: AVB17221EntityPropertyChanged { get }     static var ListenerStreamSinks: AVB17221EntityPropertyChanged { get }     static var ListenerCapabilities: AVB17221EntityPropertyChanged { get }     static var ControllerCapabilities: AVB17221EntityPropertyChanged { get }     static var AvailableIndex: AVB17221EntityPropertyChanged { get }     static var ASGrandmasterID: AVB17221EntityPropertyChanged { get }     static var GPTPGrandmasterID: AVB17221EntityPropertyChanged { get }     static var MACAddress: AVB17221EntityPropertyChanged { get }     static var AssociationID: AVB17221EntityPropertyChanged { get }     static var EntityType: AVB17221EntityPropertyChanged { get }     static var IdentifyControlIndex: AVB17221EntityPropertyChanged { get }     static var InterfaceIndex: AVB17221EntityPropertyChanged { get }     static var GPTPDomainNumber: AVB17221EntityPropertyChanged { get } } ``` | RawOptionSetType |
| To | ``` struct AVB17221EntityPropertyChanged : OptionSetType {     init(rawValue rawValue: UInt)     static var TimeToLive: AVB17221EntityPropertyChanged { get }     static var GUID: AVB17221EntityPropertyChanged { get }     static var EntityID: AVB17221EntityPropertyChanged { get }     static var VendorID: AVB17221EntityPropertyChanged { get }     static var ModelID: AVB17221EntityPropertyChanged { get }     static var EntityCapabilities: AVB17221EntityPropertyChanged { get }     static var TalkerStreamSources: AVB17221EntityPropertyChanged { get }     static var TalkerCapabilities: AVB17221EntityPropertyChanged { get }     static var ListenerStreamSinks: AVB17221EntityPropertyChanged { get }     static var ListenerCapabilities: AVB17221EntityPropertyChanged { get }     static var ControllerCapabilities: AVB17221EntityPropertyChanged { get }     static var AvailableIndex: AVB17221EntityPropertyChanged { get }     static var ASGrandmasterID: AVB17221EntityPropertyChanged { get }     static var GPTPGrandmasterID: AVB17221EntityPropertyChanged { get }     static var MACAddress: AVB17221EntityPropertyChanged { get }     static var AssociationID: AVB17221EntityPropertyChanged { get }     static var EntityType: AVB17221EntityPropertyChanged { get }     static var IdentifyControlIndex: AVB17221EntityPropertyChanged { get }     static var InterfaceIndex: AVB17221EntityPropertyChanged { get }     static var GPTPDomainNumber: AVB17221EntityPropertyChanged { get } } ``` | OptionSetType |

Modified AVB1722ControlInterface

|  | Declaration |
| --- | --- |
| From | ``` class AVB1722ControlInterface : NSObject {     var interfaceName: String!     unowned(unsafe) var interface: AVBInterface! { get }     init!(service aService: io_object_t, onInterface anInterface: AVBInterface!)     init!(service aService: io_object_t, onInterfaceNamed anInterfaceName: String!)     init!(interfaceName anInterfaceName: String!) } ``` |
| To | ``` class AVB1722ControlInterface : NSObject {     var interfaceName: String { get }     unowned(unsafe) var interface: AVBInterface? { get }     init()     init?(interfaceName anInterfaceName: String)     init?(interface anInterface: AVBInterface) } ``` |

Modified AVB1722ControlInterface.init(interfaceName: String)

|  | Declaration |
| --- | --- |
| From | ``` init!(interfaceName anInterfaceName: String!) ``` |
| To | ``` init?(interfaceName anInterfaceName: String) ``` |

Modified AVB1722ControlInterface.interface

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var interface: AVBInterface! { get } ``` |
| To | ``` unowned(unsafe) var interface: AVBInterface? { get } ``` |

Modified AVB1722ControlInterface.interfaceName

|  | Declaration |
| --- | --- |
| From | ``` var interfaceName: String! ``` |
| To | ``` var interfaceName: String { get } ``` |

Modified AVBCentralManager

|  | Declaration |
| --- | --- |
| From | ``` class AVBCentralManager : NSObject {     func startControllerMatching()     func didAddInterface(_ interface: AVBInterface!)     func didRemoveInterface(_ interface: AVBInterface!)     func streamingEnabledInterfacesOnly() -> Bool     class func nextAvailableDynamicEntityID() -> UInt64     class func releaseDynamicEntityID(_ entityID: UInt64)     class func nextAvailableDynamicEntityModelID() -> UInt64     class func releaseDynamicEntityModelID(_ entityModelID: UInt64) } ``` |
| To | ``` class AVBCentralManager : NSObject {     func startControllerMatching()     func didAddInterface(_ interface: AVBInterface)     func didRemoveInterface(_ interface: AVBInterface)     func streamingEnabledInterfacesOnly() -> Bool     class func nextAvailableDynamicEntityID() -> UInt64     class func releaseDynamicEntityID(_ entityID: UInt64)     class func nextAvailableDynamicEntityModelID() -> UInt64     class func releaseDynamicEntityModelID(_ entityModelID: UInt64) } ``` |

Modified AVBCentralManager.didAddInterface(_: AVBInterface)

|  | Declaration |
| --- | --- |
| From | ``` func didAddInterface(_ interface: AVBInterface!) ``` |
| To | ``` func didAddInterface(_ interface: AVBInterface) ``` |

Modified AVBCentralManager.didRemoveInterface(_: AVBInterface)

|  | Declaration |
| --- | --- |
| From | ``` func didRemoveInterface(_ interface: AVBInterface!) ``` |
| To | ``` func didRemoveInterface(_ interface: AVBInterface) ``` |

Modified AVBInterface

|  | Declaration |
| --- | --- |
| From | ``` class AVBInterface : NSObject {     var interfaceName: String! { get }     var entityDiscovery: AVB17221EntityDiscovery! { get }     var aecp: AVB17221AECPInterface! { get }     var acmp: AVB17221ACMPInterface! { get }     class func macAddressForInterfaceNamed(_ anInterfaceName: String!) -> AVBMACAddress!     class func supportedInterfaces() -> [AnyObject]!     class func isAVBEnabledOnInterfaceNamed(_ anInterfaceName: String!) -> Bool     class func isAVBCapableInterfaceNamed(_ anInterfaceName: String!) -> Bool     init!(interfaceName anInterfaceName: String!)     class func myGUID() -> UInt64     class func myEntityID() -> UInt64 } ``` |
| To | ``` class AVBInterface : NSObject {     var interfaceName: String { get }     var entityDiscovery: AVB17221EntityDiscovery? { get }     var aecp: AVB17221AECPInterface? { get }     var acmp: AVB17221ACMPInterface? { get }     class func macAddressForInterfaceNamed(_ anInterfaceName: String) -> AVBMACAddress?     class func supportedInterfaces() -> [String]?     class func isAVBEnabledOnInterfaceNamed(_ anInterfaceName: String) -> Bool     class func isAVBCapableInterfaceNamed(_ anInterfaceName: String) -> Bool     init?(interfaceName anInterfaceName: String)     class func myGUID() -> UInt64     class func myEntityID() -> UInt64 } ``` |

Modified AVBInterface.acmp

|  | Declaration |
| --- | --- |
| From | ``` var acmp: AVB17221ACMPInterface! { get } ``` |
| To | ``` var acmp: AVB17221ACMPInterface? { get } ``` |

Modified AVBInterface.aecp

|  | Declaration |
| --- | --- |
| From | ``` var aecp: AVB17221AECPInterface! { get } ``` |
| To | ``` var aecp: AVB17221AECPInterface? { get } ``` |

Modified AVBInterface.entityDiscovery

|  | Declaration |
| --- | --- |
| From | ``` var entityDiscovery: AVB17221EntityDiscovery! { get } ``` |
| To | ``` var entityDiscovery: AVB17221EntityDiscovery? { get } ``` |

Modified AVBInterface.init(interfaceName: String)

|  | Declaration |
| --- | --- |
| From | ``` init!(interfaceName anInterfaceName: String!) ``` |
| To | ``` init?(interfaceName anInterfaceName: String) ``` |

Modified AVBInterface.interfaceName

|  | Declaration |
| --- | --- |
| From | ``` var interfaceName: String! { get } ``` |
| To | ``` var interfaceName: String { get } ``` |

Modified AVBInterface.isAVBCapableInterfaceNamed(_: String) -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func isAVBCapableInterfaceNamed(_ anInterfaceName: String!) -> Bool ``` |
| To | ``` class func isAVBCapableInterfaceNamed(_ anInterfaceName: String) -> Bool ``` |

Modified AVBInterface.isAVBEnabledOnInterfaceNamed(_: String) -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func isAVBEnabledOnInterfaceNamed(_ anInterfaceName: String!) -> Bool ``` |
| To | ``` class func isAVBEnabledOnInterfaceNamed(_ anInterfaceName: String) -> Bool ``` |

Modified AVBInterface.macAddressForInterfaceNamed(_: String) -> AVBMACAddress? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func macAddressForInterfaceNamed(_ anInterfaceName: String!) -> AVBMACAddress! ``` |
| To | ``` class func macAddressForInterfaceNamed(_ anInterfaceName: String) -> AVBMACAddress? ``` |

Modified AVBInterface.myGUID() -> UInt64 [class]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified AVBInterface.supportedInterfaces() -> [String]? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func supportedInterfaces() -> [AnyObject]! ``` |
| To | ``` class func supportedInterfaces() -> [String]? ``` |

Modified AVBMACAddress

|  | Declaration |
| --- | --- |
| From | ``` class AVBMACAddress : NSObject, NSCopying {     init!(bytes bytes: UnsafeMutablePointer<UInt8>)     var bytes: UnsafePointer<UInt8> { get }     @NSCopying var dataRepresentation: NSData!     var stringRepresentation: String!     var multicast: Bool } ``` |
| To | ``` class AVBMACAddress : NSObject, NSCopying {     init(bytes bytes: UnsafePointer<UInt8>)     var bytes: UnsafePointer<UInt8> { get }     @NSCopying var dataRepresentation: NSData     var stringRepresentation: String     var multicast: Bool } ``` |

Modified AVBMACAddress.dataRepresentation

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var dataRepresentation: NSData! ``` |
| To | ``` @NSCopying var dataRepresentation: NSData ``` |

Modified AVBMACAddress.init(bytes: UnsafePointer<UInt8>)

|  | Declaration |
| --- | --- |
| From | ``` init!(bytes bytes: UnsafeMutablePointer<UInt8>) ``` |
| To | ``` init(bytes bytes: UnsafePointer<UInt8>) ``` |

Modified AVBMACAddress.stringRepresentation

|  | Declaration |
| --- | --- |
| From | ``` var stringRepresentation: String! ``` |
| To | ``` var stringRepresentation: String ``` |

Modified AVB17221ACMPInterfaceCompletion

|  | Declaration |
| --- | --- |
| From | ``` typealias AVB17221ACMPInterfaceCompletion = (NSError!, AVB17221ACMPMessage!) -> Void ``` |
| To | ``` typealias AVB17221ACMPInterfaceCompletion = (NSError?, AVB17221ACMPMessage) -> Void ``` |

Modified AVB17221AECPInterfaceCompletion

|  | Declaration |
| --- | --- |
| From | ``` typealias AVB17221AECPInterfaceCompletion = (NSError!, AVB17221AECPMessage!) -> Void ``` |
| To | ``` typealias AVB17221AECPInterfaceCompletion = (NSError?, AVB17221AECPMessage) -> Void ``` |

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
