---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/CoreMIDI.html
archived_at: '2026-07-18T02:56:22.966409Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# CoreMIDI Changes

## CoreMIDI

Added MIDIControlTransform.init()Added MIDIControlTransform.init(controlType: MIDITransformControlType, remappedControlType: MIDITransformControlType, controlNumber: UInt16, transform: MIDITransformType, param: Int16)Added MIDIDriverInterface.init()Added MIDIDriverInterface.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, FindDevices: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)>, Start: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)>, Stop: CFunctionPointer<((MIDIDriverRef) -> OSStatus)>, Configure: CFunctionPointer<((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)>, Send: CFunctionPointer<((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)>, EnableSource: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, Boolean) -> OSStatus)>, Flush: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)>, Monitor: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)>)Added MIDIIOErrorNotification.init()Added MIDIIOErrorNotification.init(messageID: MIDINotificationMessageID, messageSize: UInt32, driverDevice: MIDIDeviceRef, errorCode: OSStatus)Added MIDINotification.init()Added MIDINotification.init(messageID: MIDINotificationMessageID, messageSize: UInt32)Added MIDIObjectAddRemoveNotification.init()Added MIDIObjectAddRemoveNotification.init(messageID: MIDINotificationMessageID, messageSize: UInt32, parent: MIDIObjectRef, parentType: MIDIObjectType, child: MIDIObjectRef, childType: MIDIObjectType)Added MIDIObjectPropertyChangeNotification.init()Added MIDIObjectPropertyChangeNotification.init(messageID: MIDINotificationMessageID, messageSize: UInt32, object: MIDIObjectRef, objectType: MIDIObjectType, propertyName: Unmanaged<CFString>!)Added MIDIPacket.init()Added MIDIPacket.init(timeStamp: MIDITimeStamp, length: UInt16, data:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added MIDIPacketList.init()Added MIDIPacketList.init(numPackets: UInt32, packet:(MIDIPacket))Added MIDISysexSendRequest.init()Added MIDISysexSendRequest.init(destination: MIDIEndpointRef, data: UnsafePointer<UInt8>, bytesToSend: UInt32, complete: Boolean, reserved:(UInt8, UInt8, UInt8), completionProc: MIDICompletionProc, completionRefCon: UnsafeMutablePointer<Void>)Added MIDIThruConnectionEndpoint.init()Added MIDIThruConnectionEndpoint.init(endpointRef: MIDIEndpointRef, uniqueID: MIDIUniqueID)Added MIDIThruConnectionParams.init()Added MIDIThruConnectionParams.init(version: UInt32, numSources: UInt32, sources:(MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint), numDestinations: UInt32, destinations:(MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint), channelMap:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), lowVelocity: UInt8, highVelocity: UInt8, lowNote: UInt8, highNote: UInt8, noteNumber: MIDITransform, velocity: MIDITransform, keyPressure: MIDITransform, channelPressure: MIDITransform, programChange: MIDITransform, pitchBend: MIDITransform, filterOutSysEx: UInt8, filterOutMTC: UInt8, filterOutBeatClock: UInt8, filterOutTuneRequest: UInt8, reserved2:(UInt8, UInt8, UInt8), filterOutAllControls: UInt8, numControlTransforms: UInt16, numMaps: UInt16, reserved3:(UInt16, UInt16, UInt16, UInt16))Added MIDITransform.init()Added MIDITransform.init(transform: MIDITransformType, param: Int16)Added MIDIValueMap.init()Added MIDIValueMap.init(value: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Modified MIDIControlTransform [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIControlTransform {     var controlType: MIDITransformControlType     var remappedControlType: MIDITransformControlType     var controlNumber: UInt16     var transform: MIDITransformType     var param: Int16 } ``` |
| To | ``` struct MIDIControlTransform {     var controlType: MIDITransformControlType     var remappedControlType: MIDITransformControlType     var controlNumber: UInt16     var transform: MIDITransformType     var param: Int16     init()     init(controlType controlType: MIDITransformControlType, remappedControlType remappedControlType: MIDITransformControlType, controlNumber controlNumber: UInt16, transform transform: MIDITransformType, param param: Int16) } ``` |

Modified MIDIDriverInterface [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIDriverInterface {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>     var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var FindDevices: CFunctionPointer<((MIDIDriverRef, MIDIDeviceList!) -> OSStatus)>     var Start: CFunctionPointer<((MIDIDriverRef, MIDIDeviceList!) -> OSStatus)>     var Stop: CFunctionPointer<((MIDIDriverRef) -> OSStatus)>     var Configure: CFunctionPointer<((MIDIDriverRef, MIDIDevice!) -> OSStatus)>     var Send: CFunctionPointer<((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)>     var EnableSource: CFunctionPointer<((MIDIDriverRef, MIDIEndpoint!, Boolean) -> OSStatus)>     var Flush: CFunctionPointer<((MIDIDriverRef, MIDIEndpoint!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)>     var Monitor: CFunctionPointer<((MIDIDriverRef, MIDIEndpoint!, UnsafePointer<MIDIPacketList>) -> OSStatus)> } ``` |
| To | ``` struct MIDIDriverInterface {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>     var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var FindDevices: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)>     var Start: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)>     var Stop: CFunctionPointer<((MIDIDriverRef) -> OSStatus)>     var Configure: CFunctionPointer<((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)>     var Send: CFunctionPointer<((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)>     var EnableSource: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, Boolean) -> OSStatus)>     var Flush: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)>     var Monitor: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)>     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, FindDevices FindDevices: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)>, Start Start: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)>, Stop Stop: CFunctionPointer<((MIDIDriverRef) -> OSStatus)>, Configure Configure: CFunctionPointer<((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)>, Send Send: CFunctionPointer<((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)>, EnableSource EnableSource: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, Boolean) -> OSStatus)>, Flush Flush: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)>, Monitor Monitor: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)>) } ``` |

Modified MIDIDriverInterface.Configure

|  | Declaration |
| --- | --- |
| From | ``` var Configure: CFunctionPointer<((MIDIDriverRef, MIDIDevice!) -> OSStatus)> ``` |
| To | ``` var Configure: CFunctionPointer<((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)> ``` |

Modified MIDIDriverInterface.EnableSource

|  | Declaration |
| --- | --- |
| From | ``` var EnableSource: CFunctionPointer<((MIDIDriverRef, MIDIEndpoint!, Boolean) -> OSStatus)> ``` |
| To | ``` var EnableSource: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, Boolean) -> OSStatus)> ``` |

Modified MIDIDriverInterface.FindDevices

|  | Declaration |
| --- | --- |
| From | ``` var FindDevices: CFunctionPointer<((MIDIDriverRef, MIDIDeviceList!) -> OSStatus)> ``` |
| To | ``` var FindDevices: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)> ``` |

Modified MIDIDriverInterface.Flush

|  | Declaration |
| --- | --- |
| From | ``` var Flush: CFunctionPointer<((MIDIDriverRef, MIDIEndpoint!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` var Flush: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified MIDIDriverInterface.Monitor

|  | Declaration |
| --- | --- |
| From | ``` var Monitor: CFunctionPointer<((MIDIDriverRef, MIDIEndpoint!, UnsafePointer<MIDIPacketList>) -> OSStatus)> ``` |
| To | ``` var Monitor: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)> ``` |

Modified MIDIDriverInterface.Start

|  | Declaration |
| --- | --- |
| From | ``` var Start: CFunctionPointer<((MIDIDriverRef, MIDIDeviceList!) -> OSStatus)> ``` |
| To | ``` var Start: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)> ``` |

Modified MIDIIOErrorNotification [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIIOErrorNotification {     var messageID: MIDINotificationMessageID     var messageSize: UInt32     var driverDevice: Unmanaged<MIDIDevice>!     var errorCode: OSStatus } ``` |
| To | ``` struct MIDIIOErrorNotification {     var messageID: MIDINotificationMessageID     var messageSize: UInt32     var driverDevice: MIDIDeviceRef     var errorCode: OSStatus     init()     init(messageID messageID: MIDINotificationMessageID, messageSize messageSize: UInt32, driverDevice driverDevice: MIDIDeviceRef, errorCode errorCode: OSStatus) } ``` |

Modified MIDIIOErrorNotification.driverDevice

|  | Declaration |
| --- | --- |
| From | ``` var driverDevice: Unmanaged<MIDIDevice>! ``` |
| To | ``` var driverDevice: MIDIDeviceRef ``` |

Modified MIDINetworkSession.connections() -> Set<NSObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func connections() -> NSSet! ``` | iOS 8.0 |
| To | ``` func connections() -> Set<NSObject>! ``` | iOS 8.3 |

Modified MIDINetworkSession.contacts() -> Set<NSObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func contacts() -> NSSet! ``` | iOS 8.0 |
| To | ``` func contacts() -> Set<NSObject>! ``` | iOS 8.3 |

Modified MIDINetworkSession.destinationEndpoint() -> MIDIEndpointRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func destinationEndpoint() -> Unmanaged<MIDIEndpoint>! ``` | iOS 8.0 |
| To | ``` func destinationEndpoint() -> MIDIEndpointRef ``` | iOS 8.3 |

Modified MIDINetworkSession.sourceEndpoint() -> MIDIEndpointRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sourceEndpoint() -> Unmanaged<MIDIEndpoint>! ``` | iOS 8.0 |
| To | ``` func sourceEndpoint() -> MIDIEndpointRef ``` | iOS 8.3 |

Modified MIDINotification [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDINotification {     var messageID: MIDINotificationMessageID     var messageSize: UInt32 } ``` |
| To | ``` struct MIDINotification {     var messageID: MIDINotificationMessageID     var messageSize: UInt32     init()     init(messageID messageID: MIDINotificationMessageID, messageSize messageSize: UInt32) } ``` |

Modified MIDIObjectAddRemoveNotification [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIObjectAddRemoveNotification {     var messageID: MIDINotificationMessageID     var messageSize: UInt32     var parent: MIDIObjectRef     var parentType: MIDIObjectType     var child: MIDIObjectRef     var childType: MIDIObjectType } ``` |
| To | ``` struct MIDIObjectAddRemoveNotification {     var messageID: MIDINotificationMessageID     var messageSize: UInt32     var parent: MIDIObjectRef     var parentType: MIDIObjectType     var child: MIDIObjectRef     var childType: MIDIObjectType     init()     init(messageID messageID: MIDINotificationMessageID, messageSize messageSize: UInt32, parent parent: MIDIObjectRef, parentType parentType: MIDIObjectType, child child: MIDIObjectRef, childType childType: MIDIObjectType) } ``` |

Modified MIDIObjectPropertyChangeNotification [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIObjectPropertyChangeNotification {     var messageID: MIDINotificationMessageID     var messageSize: UInt32     var object: MIDIObjectRef     var objectType: MIDIObjectType     var propertyName: Unmanaged<CFString>! } ``` |
| To | ``` struct MIDIObjectPropertyChangeNotification {     var messageID: MIDINotificationMessageID     var messageSize: UInt32     var object: MIDIObjectRef     var objectType: MIDIObjectType     var propertyName: Unmanaged<CFString>!     init()     init(messageID messageID: MIDINotificationMessageID, messageSize messageSize: UInt32, object object: MIDIObjectRef, objectType objectType: MIDIObjectType, propertyName propertyName: Unmanaged<CFString>!) } ``` |

Modified MIDIPacket [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIPacket {     var timeStamp: MIDITimeStamp     var length: UInt16     var data: (Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte) } ``` |
| To | ``` struct MIDIPacket {     var timeStamp: MIDITimeStamp     var length: UInt16     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(timeStamp timeStamp: MIDITimeStamp, length length: UInt16, data data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified MIDIPacket.data

|  | Declaration |
| --- | --- |
| From | ``` var data: (Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte, Byte) ``` |
| To | ``` var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) ``` |

Modified MIDIPacketList [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIPacketList {     var numPackets: UInt32     var packet: (MIDIPacket) } ``` |
| To | ``` struct MIDIPacketList {     var numPackets: UInt32     var packet: (MIDIPacket)     init()     init(numPackets numPackets: UInt32, packet packet: (MIDIPacket)) } ``` |

Modified MIDISysexSendRequest [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDISysexSendRequest {     var destination: Unmanaged<MIDIEndpoint>!     var data: UnsafePointer<Byte>     var bytesToSend: UInt32     var complete: Boolean     var reserved: (Byte, Byte, Byte)     var completionProc: MIDICompletionProc     var completionRefCon: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct MIDISysexSendRequest {     var destination: MIDIEndpointRef     var data: UnsafePointer<UInt8>     var bytesToSend: UInt32     var complete: Boolean     var reserved: (UInt8, UInt8, UInt8)     var completionProc: MIDICompletionProc     var completionRefCon: UnsafeMutablePointer<Void>     init()     init(destination destination: MIDIEndpointRef, data data: UnsafePointer<UInt8>, bytesToSend bytesToSend: UInt32, complete complete: Boolean, reserved reserved: (UInt8, UInt8, UInt8), completionProc completionProc: MIDICompletionProc, completionRefCon completionRefCon: UnsafeMutablePointer<Void>) } ``` |

Modified MIDISysexSendRequest.data

|  | Declaration |
| --- | --- |
| From | ``` var data: UnsafePointer<Byte> ``` |
| To | ``` var data: UnsafePointer<UInt8> ``` |

Modified MIDISysexSendRequest.destination

|  | Declaration |
| --- | --- |
| From | ``` var destination: Unmanaged<MIDIEndpoint>! ``` |
| To | ``` var destination: MIDIEndpointRef ``` |

Modified MIDISysexSendRequest.reserved

|  | Declaration |
| --- | --- |
| From | ``` var reserved: (Byte, Byte, Byte) ``` |
| To | ``` var reserved: (UInt8, UInt8, UInt8) ``` |

Modified MIDIThruConnectionEndpoint [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIThruConnectionEndpoint {     var endpointRef: Unmanaged<MIDIEndpoint>!     var uniqueID: MIDIUniqueID } ``` |
| To | ``` struct MIDIThruConnectionEndpoint {     var endpointRef: MIDIEndpointRef     var uniqueID: MIDIUniqueID     init()     init(endpointRef endpointRef: MIDIEndpointRef, uniqueID uniqueID: MIDIUniqueID) } ``` |

Modified MIDIThruConnectionEndpoint.endpointRef

|  | Declaration |
| --- | --- |
| From | ``` var endpointRef: Unmanaged<MIDIEndpoint>! ``` |
| To | ``` var endpointRef: MIDIEndpointRef ``` |

Modified MIDIThruConnectionParams [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIThruConnectionParams {     var version: UInt32     var numSources: UInt32     var sources: (MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint)     var numDestinations: UInt32     var destinations: (MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint)     var channelMap: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var lowVelocity: UInt8     var highVelocity: UInt8     var lowNote: UInt8     var highNote: UInt8     var noteNumber: MIDITransform     var velocity: MIDITransform     var keyPressure: MIDITransform     var channelPressure: MIDITransform     var programChange: MIDITransform     var pitchBend: MIDITransform     var filterOutSysEx: UInt8     var filterOutMTC: UInt8     var filterOutBeatClock: UInt8     var filterOutTuneRequest: UInt8     var reserved2: (UInt8, UInt8, UInt8)     var filterOutAllControls: UInt8     var numControlTransforms: UInt16     var numMaps: UInt16     var reserved3: (UInt16, UInt16, UInt16, UInt16) } ``` |
| To | ``` struct MIDIThruConnectionParams {     var version: UInt32     var numSources: UInt32     var sources: (MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint)     var numDestinations: UInt32     var destinations: (MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint)     var channelMap: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var lowVelocity: UInt8     var highVelocity: UInt8     var lowNote: UInt8     var highNote: UInt8     var noteNumber: MIDITransform     var velocity: MIDITransform     var keyPressure: MIDITransform     var channelPressure: MIDITransform     var programChange: MIDITransform     var pitchBend: MIDITransform     var filterOutSysEx: UInt8     var filterOutMTC: UInt8     var filterOutBeatClock: UInt8     var filterOutTuneRequest: UInt8     var reserved2: (UInt8, UInt8, UInt8)     var filterOutAllControls: UInt8     var numControlTransforms: UInt16     var numMaps: UInt16     var reserved3: (UInt16, UInt16, UInt16, UInt16)     init()     init(version version: UInt32, numSources numSources: UInt32, sources sources: (MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint), numDestinations numDestinations: UInt32, destinations destinations: (MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint), channelMap channelMap: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), lowVelocity lowVelocity: UInt8, highVelocity highVelocity: UInt8, lowNote lowNote: UInt8, highNote highNote: UInt8, noteNumber noteNumber: MIDITransform, velocity velocity: MIDITransform, keyPressure keyPressure: MIDITransform, channelPressure channelPressure: MIDITransform, programChange programChange: MIDITransform, pitchBend pitchBend: MIDITransform, filterOutSysEx filterOutSysEx: UInt8, filterOutMTC filterOutMTC: UInt8, filterOutBeatClock filterOutBeatClock: UInt8, filterOutTuneRequest filterOutTuneRequest: UInt8, reserved2 reserved2: (UInt8, UInt8, UInt8), filterOutAllControls filterOutAllControls: UInt8, numControlTransforms numControlTransforms: UInt16, numMaps numMaps: UInt16, reserved3 reserved3: (UInt16, UInt16, UInt16, UInt16)) } ``` |

Modified MIDITransform [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDITransform {     var transform: MIDITransformType     var param: Int16 } ``` |
| To | ``` struct MIDITransform {     var transform: MIDITransformType     var param: Int16     init()     init(transform transform: MIDITransformType, param param: Int16) } ``` |

Modified MIDIValueMap [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIValueMap {     var value: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct MIDIValueMap {     var value: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(value value: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified MIDIClientCreate(CFString!, MIDINotifyProc, UnsafeMutablePointer<Void>, UnsafeMutablePointer<MIDIClientRef>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIClientCreate(_ name: CFString!, _ notifyProc: MIDINotifyProc, _ notifyRefCon: UnsafeMutablePointer<Void>, _ outClient: UnsafeMutablePointer<Unmanaged<MIDIClient>?>) -> OSStatus ``` |
| To | ``` func MIDIClientCreate(_ name: CFString!, _ notifyProc: MIDINotifyProc, _ notifyRefCon: UnsafeMutablePointer<Void>, _ outClient: UnsafeMutablePointer<MIDIClientRef>) -> OSStatus ``` |

Modified MIDIClientDispose(MIDIClientRef) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIClientDispose(_ client: MIDIClient!) -> OSStatus ``` |
| To | ``` func MIDIClientDispose(_ client: MIDIClientRef) -> OSStatus ``` |

Modified MIDIClientRef

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIClientRef = MIDIClient ``` |
| To | ``` typealias MIDIClientRef = COpaquePointer ``` |

Modified MIDIDestinationCreate(MIDIClientRef, CFString!, MIDIReadProc, UnsafeMutablePointer<Void>, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIDestinationCreate(_ client: MIDIClient!, _ name: CFString!, _ readProc: MIDIReadProc, _ refCon: UnsafeMutablePointer<Void>, _ outDest: UnsafeMutablePointer<Unmanaged<MIDIEndpoint>?>) -> OSStatus ``` |
| To | ``` func MIDIDestinationCreate(_ client: MIDIClientRef, _ name: CFString!, _ readProc: MIDIReadProc, _ refCon: UnsafeMutablePointer<Void>, _ outDest: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus ``` |

Modified MIDIDeviceAddEntity(MIDIDeviceRef, CFString!, Boolean, Int, Int, UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIDeviceAddEntity(_ device: MIDIDevice!, _ name: CFString!, _ embedded: Boolean, _ numSourceEndpoints: ItemCount, _ numDestinationEndpoints: ItemCount, _ newEntity: UnsafeMutablePointer<Unmanaged<MIDIEntity>?>) -> OSStatus ``` |
| To | ``` func MIDIDeviceAddEntity(_ device: MIDIDeviceRef, _ name: CFString!, _ embedded: Boolean, _ numSourceEndpoints: Int, _ numDestinationEndpoints: Int, _ newEntity: UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus ``` |

Modified MIDIDeviceCreate(MIDIDriverRef, CFString!, CFString!, CFString!, UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIDeviceCreate(_ owner: MIDIDriverRef, _ name: CFString!, _ manufacturer: CFString!, _ model: CFString!, _ outDevice: UnsafeMutablePointer<Unmanaged<MIDIDevice>?>) -> OSStatus ``` |
| To | ``` func MIDIDeviceCreate(_ owner: MIDIDriverRef, _ name: CFString!, _ manufacturer: CFString!, _ model: CFString!, _ outDevice: UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus ``` |

Modified MIDIDeviceDispose(MIDIDeviceRef) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIDeviceDispose(_ device: MIDIDevice!) -> OSStatus ``` |
| To | ``` func MIDIDeviceDispose(_ device: MIDIDeviceRef) -> OSStatus ``` |

Modified MIDIDeviceGetEntity(MIDIDeviceRef, Int) -> MIDIEntityRef

|  | Declaration |
| --- | --- |
| From | ``` func MIDIDeviceGetEntity(_ device: MIDIDevice!, _ entityIndex0: ItemCount) -> Unmanaged<MIDIEntity>! ``` |
| To | ``` func MIDIDeviceGetEntity(_ device: MIDIDeviceRef, _ entityIndex0: Int) -> MIDIEntityRef ``` |

Modified MIDIDeviceGetNumberOfEntities(MIDIDeviceRef) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func MIDIDeviceGetNumberOfEntities(_ device: MIDIDevice!) -> ItemCount ``` |
| To | ``` func MIDIDeviceGetNumberOfEntities(_ device: MIDIDeviceRef) -> Int ``` |

Modified MIDIDeviceListAddDevice(MIDIDeviceListRef, MIDIDeviceRef) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIDeviceListAddDevice(_ devList: MIDIDeviceList!, _ dev: MIDIDevice!) -> OSStatus ``` |
| To | ``` func MIDIDeviceListAddDevice(_ devList: MIDIDeviceListRef, _ dev: MIDIDeviceRef) -> OSStatus ``` |

Modified MIDIDeviceListDispose(MIDIDeviceListRef) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIDeviceListDispose(_ devList: MIDIDeviceList!) -> OSStatus ``` |
| To | ``` func MIDIDeviceListDispose(_ devList: MIDIDeviceListRef) -> OSStatus ``` |

Modified MIDIDeviceListGetDevice(MIDIDeviceListRef, Int) -> MIDIDeviceRef

|  | Declaration |
| --- | --- |
| From | ``` func MIDIDeviceListGetDevice(_ devList: MIDIDeviceList!, _ index0: ItemCount) -> Unmanaged<MIDIDevice>! ``` |
| To | ``` func MIDIDeviceListGetDevice(_ devList: MIDIDeviceListRef, _ index0: Int) -> MIDIDeviceRef ``` |

Modified MIDIDeviceListGetNumberOfDevices(MIDIDeviceListRef) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func MIDIDeviceListGetNumberOfDevices(_ devList: MIDIDeviceList!) -> ItemCount ``` |
| To | ``` func MIDIDeviceListGetNumberOfDevices(_ devList: MIDIDeviceListRef) -> Int ``` |

Modified MIDIDeviceListRef

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIDeviceListRef = MIDIDeviceList ``` |
| To | ``` typealias MIDIDeviceListRef = COpaquePointer ``` |

Modified MIDIDeviceRef

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIDeviceRef = MIDIDevice ``` |
| To | ``` typealias MIDIDeviceRef = COpaquePointer ``` |

Modified MIDIDeviceRemoveEntity(MIDIDeviceRef, MIDIEntityRef) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIDeviceRemoveEntity(_ device: MIDIDevice!, _ entity: MIDIEntity!) -> OSStatus ``` |
| To | ``` func MIDIDeviceRemoveEntity(_ device: MIDIDeviceRef, _ entity: MIDIEntityRef) -> OSStatus ``` |

Modified MIDIEndpointDispose(MIDIEndpointRef) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIEndpointDispose(_ endpt: MIDIEndpoint!) -> OSStatus ``` |
| To | ``` func MIDIEndpointDispose(_ endpt: MIDIEndpointRef) -> OSStatus ``` |

Modified MIDIEndpointGetEntity(MIDIEndpointRef, UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIEndpointGetEntity(_ inEndpoint: MIDIEndpoint!, _ outEntity: UnsafeMutablePointer<Unmanaged<MIDIEntity>?>) -> OSStatus ``` |
| To | ``` func MIDIEndpointGetEntity(_ inEndpoint: MIDIEndpointRef, _ outEntity: UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus ``` |

Modified MIDIEndpointGetRefCons(MIDIEndpointRef, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIEndpointGetRefCons(_ endpt: MIDIEndpoint!, _ ref1: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ ref2: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus ``` |
| To | ``` func MIDIEndpointGetRefCons(_ endpt: MIDIEndpointRef, _ ref1: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ ref2: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus ``` |

Modified MIDIEndpointRef

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIEndpointRef = MIDIEndpoint ``` |
| To | ``` typealias MIDIEndpointRef = COpaquePointer ``` |

Modified MIDIEndpointSetRefCons(MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIEndpointSetRefCons(_ endpt: MIDIEndpoint!, _ ref1: UnsafeMutablePointer<Void>, _ ref2: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func MIDIEndpointSetRefCons(_ endpt: MIDIEndpointRef, _ ref1: UnsafeMutablePointer<Void>, _ ref2: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified MIDIEntityAddOrRemoveEndpoints(MIDIEntityRef, Int, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIEntityAddOrRemoveEndpoints(_ entity: MIDIEntity!, _ numSourceEndpoints: ItemCount, _ numDestinationEndpoints: ItemCount) -> OSStatus ``` |
| To | ``` func MIDIEntityAddOrRemoveEndpoints(_ entity: MIDIEntityRef, _ numSourceEndpoints: Int, _ numDestinationEndpoints: Int) -> OSStatus ``` |

Modified MIDIEntityGetDestination(MIDIEntityRef, Int) -> MIDIEndpointRef

|  | Declaration |
| --- | --- |
| From | ``` func MIDIEntityGetDestination(_ entity: MIDIEntity!, _ destIndex0: ItemCount) -> Unmanaged<MIDIEndpoint>! ``` |
| To | ``` func MIDIEntityGetDestination(_ entity: MIDIEntityRef, _ destIndex0: Int) -> MIDIEndpointRef ``` |

Modified MIDIEntityGetDevice(MIDIEntityRef, UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIEntityGetDevice(_ inEntity: MIDIEntity!, _ outDevice: UnsafeMutablePointer<Unmanaged<MIDIDevice>?>) -> OSStatus ``` |
| To | ``` func MIDIEntityGetDevice(_ inEntity: MIDIEntityRef, _ outDevice: UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus ``` |

Modified MIDIEntityGetNumberOfDestinations(MIDIEntityRef) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func MIDIEntityGetNumberOfDestinations(_ entity: MIDIEntity!) -> ItemCount ``` |
| To | ``` func MIDIEntityGetNumberOfDestinations(_ entity: MIDIEntityRef) -> Int ``` |

Modified MIDIEntityGetNumberOfSources(MIDIEntityRef) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func MIDIEntityGetNumberOfSources(_ entity: MIDIEntity!) -> ItemCount ``` |
| To | ``` func MIDIEntityGetNumberOfSources(_ entity: MIDIEntityRef) -> Int ``` |

Modified MIDIEntityGetSource(MIDIEntityRef, Int) -> MIDIEndpointRef

|  | Declaration |
| --- | --- |
| From | ``` func MIDIEntityGetSource(_ entity: MIDIEntity!, _ sourceIndex0: ItemCount) -> Unmanaged<MIDIEndpoint>! ``` |
| To | ``` func MIDIEntityGetSource(_ entity: MIDIEntityRef, _ sourceIndex0: Int) -> MIDIEndpointRef ``` |

Modified MIDIEntityRef

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIEntityRef = MIDIEntity ``` |
| To | ``` typealias MIDIEntityRef = COpaquePointer ``` |

Modified MIDIExternalDeviceCreate(CFString!, CFString!, CFString!, UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIExternalDeviceCreate(_ name: CFString!, _ manufacturer: CFString!, _ model: CFString!, _ outDevice: UnsafeMutablePointer<Unmanaged<MIDIDevice>?>) -> OSStatus ``` |
| To | ``` func MIDIExternalDeviceCreate(_ name: CFString!, _ manufacturer: CFString!, _ model: CFString!, _ outDevice: UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus ``` |

Modified MIDIFlushOutput(MIDIEndpointRef) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIFlushOutput(_ dest: MIDIEndpoint!) -> OSStatus ``` |
| To | ``` func MIDIFlushOutput(_ dest: MIDIEndpointRef) -> OSStatus ``` |

Modified MIDIGetDestination(Int) -> MIDIEndpointRef

|  | Declaration |
| --- | --- |
| From | ``` func MIDIGetDestination(_ destIndex0: ItemCount) -> Unmanaged<MIDIEndpoint>! ``` |
| To | ``` func MIDIGetDestination(_ destIndex0: Int) -> MIDIEndpointRef ``` |

Modified MIDIGetDevice(Int) -> MIDIDeviceRef

|  | Declaration |
| --- | --- |
| From | ``` func MIDIGetDevice(_ deviceIndex0: ItemCount) -> Unmanaged<MIDIDevice>! ``` |
| To | ``` func MIDIGetDevice(_ deviceIndex0: Int) -> MIDIDeviceRef ``` |

Modified MIDIGetDriverDeviceList(MIDIDriverRef) -> MIDIDeviceListRef

|  | Declaration |
| --- | --- |
| From | ``` func MIDIGetDriverDeviceList(_ driver: MIDIDriverRef) -> Unmanaged<MIDIDeviceList>! ``` |
| To | ``` func MIDIGetDriverDeviceList(_ driver: MIDIDriverRef) -> MIDIDeviceListRef ``` |

Modified MIDIGetExternalDevice(Int) -> MIDIDeviceRef

|  | Declaration |
| --- | --- |
| From | ``` func MIDIGetExternalDevice(_ deviceIndex0: ItemCount) -> Unmanaged<MIDIDevice>! ``` |
| To | ``` func MIDIGetExternalDevice(_ deviceIndex0: Int) -> MIDIDeviceRef ``` |

Modified MIDIGetNumberOfDestinations() -> Int

|  | Declaration |
| --- | --- |
| From | ``` func MIDIGetNumberOfDestinations() -> ItemCount ``` |
| To | ``` func MIDIGetNumberOfDestinations() -> Int ``` |

Modified MIDIGetNumberOfDevices() -> Int

|  | Declaration |
| --- | --- |
| From | ``` func MIDIGetNumberOfDevices() -> ItemCount ``` |
| To | ``` func MIDIGetNumberOfDevices() -> Int ``` |

Modified MIDIGetNumberOfExternalDevices() -> Int

|  | Declaration |
| --- | --- |
| From | ``` func MIDIGetNumberOfExternalDevices() -> ItemCount ``` |
| To | ``` func MIDIGetNumberOfExternalDevices() -> Int ``` |

Modified MIDIGetNumberOfSources() -> Int

|  | Declaration |
| --- | --- |
| From | ``` func MIDIGetNumberOfSources() -> ItemCount ``` |
| To | ``` func MIDIGetNumberOfSources() -> Int ``` |

Modified MIDIGetSource(Int) -> MIDIEndpointRef

|  | Declaration |
| --- | --- |
| From | ``` func MIDIGetSource(_ sourceIndex0: ItemCount) -> Unmanaged<MIDIEndpoint>! ``` |
| To | ``` func MIDIGetSource(_ sourceIndex0: Int) -> MIDIEndpointRef ``` |

Modified MIDIInputPortCreate(MIDIClientRef, CFString!, MIDIReadProc, UnsafeMutablePointer<Void>, UnsafeMutablePointer<MIDIPortRef>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIInputPortCreate(_ client: MIDIClient!, _ portName: CFString!, _ readProc: MIDIReadProc, _ refCon: UnsafeMutablePointer<Void>, _ outPort: UnsafeMutablePointer<Unmanaged<MIDIPort>?>) -> OSStatus ``` |
| To | ``` func MIDIInputPortCreate(_ client: MIDIClientRef, _ portName: CFString!, _ readProc: MIDIReadProc, _ refCon: UnsafeMutablePointer<Void>, _ outPort: UnsafeMutablePointer<MIDIPortRef>) -> OSStatus ``` |

Modified MIDINetworkBonjourServiceType

|  | Declaration |
| --- | --- |
| From | ``` let MIDINetworkBonjourServiceType: NSString! ``` |
| To | ``` let MIDINetworkBonjourServiceType: String ``` |

Modified MIDINetworkNotificationContactsDidChange

|  | Declaration |
| --- | --- |
| From | ``` let MIDINetworkNotificationContactsDidChange: NSString! ``` |
| To | ``` let MIDINetworkNotificationContactsDidChange: String ``` |

Modified MIDINetworkNotificationSessionDidChange

|  | Declaration |
| --- | --- |
| From | ``` let MIDINetworkNotificationSessionDidChange: NSString! ``` |
| To | ``` let MIDINetworkNotificationSessionDidChange: String ``` |

Modified MIDIOutputPortCreate(MIDIClientRef, CFString!, UnsafeMutablePointer<MIDIPortRef>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIOutputPortCreate(_ client: MIDIClient!, _ portName: CFString!, _ outPort: UnsafeMutablePointer<Unmanaged<MIDIPort>?>) -> OSStatus ``` |
| To | ``` func MIDIOutputPortCreate(_ client: MIDIClientRef, _ portName: CFString!, _ outPort: UnsafeMutablePointer<MIDIPortRef>) -> OSStatus ``` |

Modified MIDIPacketListAdd(UnsafeMutablePointer<MIDIPacketList>, Int, UnsafeMutablePointer<MIDIPacket>, MIDITimeStamp, Int, UnsafePointer<UInt8>) -> UnsafeMutablePointer<MIDIPacket>

|  | Declaration |
| --- | --- |
| From | ``` func MIDIPacketListAdd(_ pktlist: UnsafeMutablePointer<MIDIPacketList>, _ listSize: ByteCount, _ curPacket: UnsafeMutablePointer<MIDIPacket>, _ time: MIDITimeStamp, _ nData: ByteCount, _ data: UnsafePointer<Byte>) -> UnsafeMutablePointer<MIDIPacket> ``` |
| To | ``` func MIDIPacketListAdd(_ pktlist: UnsafeMutablePointer<MIDIPacketList>, _ listSize: Int, _ curPacket: UnsafeMutablePointer<MIDIPacket>, _ time: MIDITimeStamp, _ nData: Int, _ data: UnsafePointer<UInt8>) -> UnsafeMutablePointer<MIDIPacket> ``` |

Modified MIDIPortConnectSource(MIDIPortRef, MIDIEndpointRef, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIPortConnectSource(_ port: MIDIPort!, _ source: MIDIEndpoint!, _ connRefCon: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func MIDIPortConnectSource(_ port: MIDIPortRef, _ source: MIDIEndpointRef, _ connRefCon: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified MIDIPortDisconnectSource(MIDIPortRef, MIDIEndpointRef) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIPortDisconnectSource(_ port: MIDIPort!, _ source: MIDIEndpoint!) -> OSStatus ``` |
| To | ``` func MIDIPortDisconnectSource(_ port: MIDIPortRef, _ source: MIDIEndpointRef) -> OSStatus ``` |

Modified MIDIPortDispose(MIDIPortRef) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIPortDispose(_ port: MIDIPort!) -> OSStatus ``` |
| To | ``` func MIDIPortDispose(_ port: MIDIPortRef) -> OSStatus ``` |

Modified MIDIPortRef

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIPortRef = MIDIPort ``` |
| To | ``` typealias MIDIPortRef = COpaquePointer ``` |

Modified MIDIReceived(MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIReceived(_ src: MIDIEndpoint!, _ pktlist: UnsafePointer<MIDIPacketList>) -> OSStatus ``` |
| To | ``` func MIDIReceived(_ src: MIDIEndpointRef, _ pktlist: UnsafePointer<MIDIPacketList>) -> OSStatus ``` |

Modified MIDISend(MIDIPortRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDISend(_ port: MIDIPort!, _ dest: MIDIEndpoint!, _ pktlist: UnsafePointer<MIDIPacketList>) -> OSStatus ``` |
| To | ``` func MIDISend(_ port: MIDIPortRef, _ dest: MIDIEndpointRef, _ pktlist: UnsafePointer<MIDIPacketList>) -> OSStatus ``` |

Modified MIDISetupAddDevice(MIDIDeviceRef) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDISetupAddDevice(_ device: MIDIDevice!) -> OSStatus ``` |
| To | ``` func MIDISetupAddDevice(_ device: MIDIDeviceRef) -> OSStatus ``` |

Modified MIDISetupAddExternalDevice(MIDIDeviceRef) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDISetupAddExternalDevice(_ device: MIDIDevice!) -> OSStatus ``` |
| To | ``` func MIDISetupAddExternalDevice(_ device: MIDIDeviceRef) -> OSStatus ``` |

Modified MIDISetupRef

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDISetupRef = MIDISetup ``` |
| To | ``` typealias MIDISetupRef = COpaquePointer ``` |

Modified MIDISetupRemoveDevice(MIDIDeviceRef) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDISetupRemoveDevice(_ device: MIDIDevice!) -> OSStatus ``` |
| To | ``` func MIDISetupRemoveDevice(_ device: MIDIDeviceRef) -> OSStatus ``` |

Modified MIDISetupRemoveExternalDevice(MIDIDeviceRef) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDISetupRemoveExternalDevice(_ device: MIDIDevice!) -> OSStatus ``` |
| To | ``` func MIDISetupRemoveExternalDevice(_ device: MIDIDeviceRef) -> OSStatus ``` |

Modified MIDISourceCreate(MIDIClientRef, CFString!, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDISourceCreate(_ client: MIDIClient!, _ name: CFString!, _ outSrc: UnsafeMutablePointer<Unmanaged<MIDIEndpoint>?>) -> OSStatus ``` |
| To | ``` func MIDISourceCreate(_ client: MIDIClientRef, _ name: CFString!, _ outSrc: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus ``` |

Modified MIDIThruConnectionCreate(CFString!, CFData!, UnsafeMutablePointer<MIDIThruConnectionRef>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIThruConnectionCreate(_ inPersistentOwnerID: CFString!, _ inConnectionParams: CFData!, _ outConnection: UnsafeMutablePointer<Unmanaged<MIDIThruConnection>?>) -> OSStatus ``` |
| To | ``` func MIDIThruConnectionCreate(_ inPersistentOwnerID: CFString!, _ inConnectionParams: CFData!, _ outConnection: UnsafeMutablePointer<MIDIThruConnectionRef>) -> OSStatus ``` |

Modified MIDIThruConnectionDispose(MIDIThruConnectionRef) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIThruConnectionDispose(_ connection: MIDIThruConnection!) -> OSStatus ``` |
| To | ``` func MIDIThruConnectionDispose(_ connection: MIDIThruConnectionRef) -> OSStatus ``` |

Modified MIDIThruConnectionGetParams(MIDIThruConnectionRef, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIThruConnectionGetParams(_ connection: MIDIThruConnection!, _ outConnectionParams: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func MIDIThruConnectionGetParams(_ connection: MIDIThruConnectionRef, _ outConnectionParams: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |

Modified MIDIThruConnectionRef

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIThruConnectionRef = MIDIThruConnection ``` |
| To | ``` typealias MIDIThruConnectionRef = COpaquePointer ``` |

Modified MIDIThruConnectionSetParams(MIDIThruConnectionRef, CFData!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MIDIThruConnectionSetParams(_ connection: MIDIThruConnection!, _ inConnectionParams: CFData!) -> OSStatus ``` |
| To | ``` func MIDIThruConnectionSetParams(_ connection: MIDIThruConnectionRef, _ inConnectionParams: CFData!) -> OSStatus ``` |

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
