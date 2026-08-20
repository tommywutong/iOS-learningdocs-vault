---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/CoreMIDI.html
archived_at: '2026-07-18T02:52:13.191722Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


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
| From | ``` struct MIDIDriverInterface {     var _reserved: UnsafePointer<()>     var QueryInterface: CFunctionPointer<((UnsafePointer<()>, REFIID, UnsafePointer<LPVOID>) -> HRESULT)>     var AddRef: CFunctionPointer<((UnsafePointer<()>) -> ULONG)>     var Release: CFunctionPointer<((UnsafePointer<()>) -> ULONG)>     var FindDevices: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)>     var Start: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)>     var Stop: CFunctionPointer<((MIDIDriverRef) -> OSStatus)>     var Configure: CFunctionPointer<((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)>     var Send: CFunctionPointer<((MIDIDriverRef, ConstUnsafePointer<MIDIPacketList>, UnsafePointer<()>, UnsafePointer<()>) -> OSStatus)>     var EnableSource: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, Boolean) -> OSStatus)>     var Flush: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<()>, UnsafePointer<()>) -> OSStatus)>     var Monitor: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, ConstUnsafePointer<MIDIPacketList>) -> OSStatus)> } ``` |
| To | ``` struct MIDIDriverInterface {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>     var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var FindDevices: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)>     var Start: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)>     var Stop: CFunctionPointer<((MIDIDriverRef) -> OSStatus)>     var Configure: CFunctionPointer<((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)>     var Send: CFunctionPointer<((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)>     var EnableSource: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, Boolean) -> OSStatus)>     var Flush: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)>     var Monitor: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)>     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, FindDevices FindDevices: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)>, Start Start: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)>, Stop Stop: CFunctionPointer<((MIDIDriverRef) -> OSStatus)>, Configure Configure: CFunctionPointer<((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)>, Send Send: CFunctionPointer<((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)>, EnableSource EnableSource: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, Boolean) -> OSStatus)>, Flush Flush: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)>, Monitor Monitor: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)>) } ``` |

Modified MIDIDriverInterface.AddRef

|  | Declaration |
| --- | --- |
| From | ``` var AddRef: CFunctionPointer<((UnsafePointer<()>) -> ULONG)> ``` |
| To | ``` var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)> ``` |

Modified MIDIDriverInterface.Flush

|  | Declaration |
| --- | --- |
| From | ``` var Flush: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<()>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` var Flush: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified MIDIDriverInterface.Monitor

|  | Declaration |
| --- | --- |
| From | ``` var Monitor: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, ConstUnsafePointer<MIDIPacketList>) -> OSStatus)> ``` |
| To | ``` var Monitor: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)> ``` |

Modified MIDIDriverInterface.QueryInterface

|  | Declaration |
| --- | --- |
| From | ``` var QueryInterface: CFunctionPointer<((UnsafePointer<()>, REFIID, UnsafePointer<LPVOID>) -> HRESULT)> ``` |
| To | ``` var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)> ``` |

Modified MIDIDriverInterface.Release

|  | Declaration |
| --- | --- |
| From | ``` var Release: CFunctionPointer<((UnsafePointer<()>) -> ULONG)> ``` |
| To | ``` var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)> ``` |

Modified MIDIDriverInterface.Send

|  | Declaration |
| --- | --- |
| From | ``` var Send: CFunctionPointer<((MIDIDriverRef, ConstUnsafePointer<MIDIPacketList>, UnsafePointer<()>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` var Send: CFunctionPointer<((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified MIDIIOErrorNotification [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIIOErrorNotification {     var messageID: MIDINotificationMessageID     var messageSize: UInt32     var driverDevice: MIDIDeviceRef     var errorCode: OSStatus } ``` |
| To | ``` struct MIDIIOErrorNotification {     var messageID: MIDINotificationMessageID     var messageSize: UInt32     var driverDevice: MIDIDeviceRef     var errorCode: OSStatus     init()     init(messageID messageID: MIDINotificationMessageID, messageSize messageSize: UInt32, driverDevice driverDevice: MIDIDeviceRef, errorCode errorCode: OSStatus) } ``` |

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
| From | ``` struct MIDISysexSendRequest {     var destination: MIDIEndpointRef     var data: ConstUnsafePointer<Byte>     var bytesToSend: UInt32     var complete: Boolean     var reserved: (Byte, Byte, Byte)     var completionProc: MIDICompletionProc     var completionRefCon: UnsafePointer<()> } ``` |
| To | ``` struct MIDISysexSendRequest {     var destination: MIDIEndpointRef     var data: UnsafePointer<UInt8>     var bytesToSend: UInt32     var complete: Boolean     var reserved: (UInt8, UInt8, UInt8)     var completionProc: MIDICompletionProc     var completionRefCon: UnsafeMutablePointer<Void>     init()     init(destination destination: MIDIEndpointRef, data data: UnsafePointer<UInt8>, bytesToSend bytesToSend: UInt32, complete complete: Boolean, reserved reserved: (UInt8, UInt8, UInt8), completionProc completionProc: MIDICompletionProc, completionRefCon completionRefCon: UnsafeMutablePointer<Void>) } ``` |

Modified MIDISysexSendRequest.completionRefCon

|  | Declaration |
| --- | --- |
| From | ``` var completionRefCon: UnsafePointer<()> ``` |
| To | ``` var completionRefCon: UnsafeMutablePointer<Void> ``` |

Modified MIDISysexSendRequest.data

|  | Declaration |
| --- | --- |
| From | ``` var data: ConstUnsafePointer<Byte> ``` |
| To | ``` var data: UnsafePointer<UInt8> ``` |

Modified MIDISysexSendRequest.reserved

|  | Declaration |
| --- | --- |
| From | ``` var reserved: (Byte, Byte, Byte) ``` |
| To | ``` var reserved: (UInt8, UInt8, UInt8) ``` |

Modified MIDIThruConnectionEndpoint [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIThruConnectionEndpoint {     var endpointRef: MIDIEndpointRef     var uniqueID: MIDIUniqueID } ``` |
| To | ``` struct MIDIThruConnectionEndpoint {     var endpointRef: MIDIEndpointRef     var uniqueID: MIDIUniqueID     init()     init(endpointRef endpointRef: MIDIEndpointRef, uniqueID uniqueID: MIDIUniqueID) } ``` |

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

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIClientCreate(_ name: CFString!, _ notifyProc: MIDINotifyProc, _ notifyRefCon: UnsafePointer<()>, _ outClient: UnsafePointer<MIDIClientRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIClientCreate(_ name: CFString!, _ notifyProc: MIDINotifyProc, _ notifyRefCon: UnsafeMutablePointer<Void>, _ outClient: UnsafeMutablePointer<MIDIClientRef>) -> OSStatus ``` | OS X 10.0 |

Modified MIDIClientDispose(MIDIClientRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MIDICompletionProc

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDICompletionProc = CFunctionPointer<((UnsafePointer<MIDISysexSendRequest>) -> Void)> ``` |
| To | ``` typealias MIDICompletionProc = CFunctionPointer<((UnsafeMutablePointer<MIDISysexSendRequest>) -> Void)> ``` |

Modified MIDIDestinationCreate(MIDIClientRef, CFString!, MIDIReadProc, UnsafeMutablePointer<Void>, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIDestinationCreate(_ client: MIDIClientRef, _ name: CFString!, _ readProc: MIDIReadProc, _ refCon: UnsafePointer<()>, _ outDest: UnsafePointer<MIDIEndpointRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIDestinationCreate(_ client: MIDIClientRef, _ name: CFString!, _ readProc: MIDIReadProc, _ refCon: UnsafeMutablePointer<Void>, _ outDest: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus ``` | OS X 10.0 |

Modified MIDIDeviceAddEntity(MIDIDeviceRef, CFString!, Boolean, Int, Int, UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIDeviceAddEntity(_ device: MIDIDeviceRef, _ name: CFString!, _ embedded: Boolean, _ numSourceEndpoints: ItemCount, _ numDestinationEndpoints: ItemCount, _ newEntity: UnsafePointer<MIDIEntityRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIDeviceAddEntity(_ device: MIDIDeviceRef, _ name: CFString!, _ embedded: Boolean, _ numSourceEndpoints: Int, _ numDestinationEndpoints: Int, _ newEntity: UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus ``` | OS X 10.0 |

Modified MIDIDeviceCreate(MIDIDriverRef, CFString!, CFString!, CFString!, UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIDeviceCreate(_ owner: MIDIDriverRef, _ name: CFString!, _ manufacturer: CFString!, _ model: CFString!, _ outDevice: UnsafePointer<MIDIDeviceRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIDeviceCreate(_ owner: MIDIDriverRef, _ name: CFString!, _ manufacturer: CFString!, _ model: CFString!, _ outDevice: UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus ``` | OS X 10.0 |

Modified MIDIDeviceDispose(MIDIDeviceRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified MIDIDeviceGetEntity(MIDIDeviceRef, Int) -> MIDIEntityRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIDeviceGetEntity(_ device: MIDIDeviceRef, _ entityIndex0: ItemCount) -> MIDIEntityRef ``` | OS X 10.10 |
| To | ``` func MIDIDeviceGetEntity(_ device: MIDIDeviceRef, _ entityIndex0: Int) -> MIDIEntityRef ``` | OS X 10.0 |

Modified MIDIDeviceGetNumberOfEntities(MIDIDeviceRef) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIDeviceGetNumberOfEntities(_ device: MIDIDeviceRef) -> ItemCount ``` | OS X 10.10 |
| To | ``` func MIDIDeviceGetNumberOfEntities(_ device: MIDIDeviceRef) -> Int ``` | OS X 10.0 |

Modified MIDIDeviceListAddDevice(MIDIDeviceListRef, MIDIDeviceRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MIDIDeviceListDispose(MIDIDeviceListRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified MIDIDeviceListGetDevice(MIDIDeviceListRef, Int) -> MIDIDeviceRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIDeviceListGetDevice(_ devList: MIDIDeviceListRef, _ index0: ItemCount) -> MIDIDeviceRef ``` | OS X 10.10 |
| To | ``` func MIDIDeviceListGetDevice(_ devList: MIDIDeviceListRef, _ index0: Int) -> MIDIDeviceRef ``` | OS X 10.0 |

Modified MIDIDeviceListGetNumberOfDevices(MIDIDeviceListRef) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIDeviceListGetNumberOfDevices(_ devList: MIDIDeviceListRef) -> ItemCount ``` | OS X 10.10 |
| To | ``` func MIDIDeviceListGetNumberOfDevices(_ devList: MIDIDeviceListRef) -> Int ``` | OS X 10.0 |

Modified MIDIDeviceRemoveEntity(MIDIDeviceRef, MIDIEntityRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified MIDIDriverEnableMonitoring(MIDIDriverRef, Boolean) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified MIDIDriverRef

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIDriverRef = UnsafePointer<UnsafePointer<MIDIDriverInterface>> ``` |
| To | ``` typealias MIDIDriverRef = UnsafeMutablePointer<UnsafeMutablePointer<MIDIDriverInterface>> ``` |

Modified MIDIEndpointDispose(MIDIEndpointRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MIDIEndpointGetEntity(MIDIEndpointRef, UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIEndpointGetEntity(_ inEndpoint: MIDIEndpointRef, _ outEntity: UnsafePointer<MIDIEntityRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIEndpointGetEntity(_ inEndpoint: MIDIEndpointRef, _ outEntity: UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus ``` | OS X 10.2 |

Modified MIDIEndpointGetRefCons(MIDIEndpointRef, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIEndpointGetRefCons(_ endpt: MIDIEndpointRef, _ ref1: UnsafePointer<UnsafePointer<()>>, _ ref2: UnsafePointer<UnsafePointer<()>>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIEndpointGetRefCons(_ endpt: MIDIEndpointRef, _ ref1: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ ref2: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus ``` | OS X 10.0 |

Modified MIDIEndpointSetRefCons(MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIEndpointSetRefCons(_ endpt: MIDIEndpointRef, _ ref1: UnsafePointer<()>, _ ref2: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIEndpointSetRefCons(_ endpt: MIDIEndpointRef, _ ref1: UnsafeMutablePointer<Void>, _ ref2: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.0 |

Modified MIDIEntityAddOrRemoveEndpoints(MIDIEntityRef, Int, Int) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIEntityAddOrRemoveEndpoints(_ entity: MIDIEntityRef, _ numSourceEndpoints: ItemCount, _ numDestinationEndpoints: ItemCount) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIEntityAddOrRemoveEndpoints(_ entity: MIDIEntityRef, _ numSourceEndpoints: Int, _ numDestinationEndpoints: Int) -> OSStatus ``` | OS X 10.2 |

Modified MIDIEntityGetDestination(MIDIEntityRef, Int) -> MIDIEndpointRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIEntityGetDestination(_ entity: MIDIEntityRef, _ destIndex0: ItemCount) -> MIDIEndpointRef ``` | OS X 10.10 |
| To | ``` func MIDIEntityGetDestination(_ entity: MIDIEntityRef, _ destIndex0: Int) -> MIDIEndpointRef ``` | OS X 10.0 |

Modified MIDIEntityGetDevice(MIDIEntityRef, UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIEntityGetDevice(_ inEntity: MIDIEntityRef, _ outDevice: UnsafePointer<MIDIDeviceRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIEntityGetDevice(_ inEntity: MIDIEntityRef, _ outDevice: UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus ``` | OS X 10.2 |

Modified MIDIEntityGetNumberOfDestinations(MIDIEntityRef) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIEntityGetNumberOfDestinations(_ entity: MIDIEntityRef) -> ItemCount ``` | OS X 10.10 |
| To | ``` func MIDIEntityGetNumberOfDestinations(_ entity: MIDIEntityRef) -> Int ``` | OS X 10.0 |

Modified MIDIEntityGetNumberOfSources(MIDIEntityRef) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIEntityGetNumberOfSources(_ entity: MIDIEntityRef) -> ItemCount ``` | OS X 10.10 |
| To | ``` func MIDIEntityGetNumberOfSources(_ entity: MIDIEntityRef) -> Int ``` | OS X 10.0 |

Modified MIDIEntityGetSource(MIDIEntityRef, Int) -> MIDIEndpointRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIEntityGetSource(_ entity: MIDIEntityRef, _ sourceIndex0: ItemCount) -> MIDIEndpointRef ``` | OS X 10.10 |
| To | ``` func MIDIEntityGetSource(_ entity: MIDIEntityRef, _ sourceIndex0: Int) -> MIDIEndpointRef ``` | OS X 10.0 |

Modified MIDIExternalDeviceCreate(CFString!, CFString!, CFString!, UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIExternalDeviceCreate(_ name: CFString!, _ manufacturer: CFString!, _ model: CFString!, _ outDevice: UnsafePointer<MIDIDeviceRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIExternalDeviceCreate(_ name: CFString!, _ manufacturer: CFString!, _ model: CFString!, _ outDevice: UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus ``` | OS X 10.1 |

Modified MIDIFlushOutput(MIDIEndpointRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified MIDIGetDestination(Int) -> MIDIEndpointRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIGetDestination(_ destIndex0: ItemCount) -> MIDIEndpointRef ``` | OS X 10.10 |
| To | ``` func MIDIGetDestination(_ destIndex0: Int) -> MIDIEndpointRef ``` | OS X 10.0 |

Modified MIDIGetDevice(Int) -> MIDIDeviceRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIGetDevice(_ deviceIndex0: ItemCount) -> MIDIDeviceRef ``` | OS X 10.10 |
| To | ``` func MIDIGetDevice(_ deviceIndex0: Int) -> MIDIDeviceRef ``` | OS X 10.0 |

Modified MIDIGetDriverDeviceList(MIDIDriverRef) -> MIDIDeviceListRef

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified MIDIGetDriverIORunLoop() -> Unmanaged<CFRunLoop>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MIDIGetExternalDevice(Int) -> MIDIDeviceRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIGetExternalDevice(_ deviceIndex0: ItemCount) -> MIDIDeviceRef ``` | OS X 10.10 |
| To | ``` func MIDIGetExternalDevice(_ deviceIndex0: Int) -> MIDIDeviceRef ``` | OS X 10.1 |

Modified MIDIGetNumberOfDestinations() -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIGetNumberOfDestinations() -> ItemCount ``` | OS X 10.10 |
| To | ``` func MIDIGetNumberOfDestinations() -> Int ``` | OS X 10.0 |

Modified MIDIGetNumberOfDevices() -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIGetNumberOfDevices() -> ItemCount ``` | OS X 10.10 |
| To | ``` func MIDIGetNumberOfDevices() -> Int ``` | OS X 10.0 |

Modified MIDIGetNumberOfExternalDevices() -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIGetNumberOfExternalDevices() -> ItemCount ``` | OS X 10.10 |
| To | ``` func MIDIGetNumberOfExternalDevices() -> Int ``` | OS X 10.1 |

Modified MIDIGetNumberOfSources() -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIGetNumberOfSources() -> ItemCount ``` | OS X 10.10 |
| To | ``` func MIDIGetNumberOfSources() -> Int ``` | OS X 10.0 |

Modified MIDIGetSource(Int) -> MIDIEndpointRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIGetSource(_ sourceIndex0: ItemCount) -> MIDIEndpointRef ``` | OS X 10.10 |
| To | ``` func MIDIGetSource(_ sourceIndex0: Int) -> MIDIEndpointRef ``` | OS X 10.0 |

Modified MIDIInputPortCreate(MIDIClientRef, CFString!, MIDIReadProc, UnsafeMutablePointer<Void>, UnsafeMutablePointer<MIDIPortRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIInputPortCreate(_ client: MIDIClientRef, _ portName: CFString!, _ readProc: MIDIReadProc, _ refCon: UnsafePointer<()>, _ outPort: UnsafePointer<MIDIPortRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIInputPortCreate(_ client: MIDIClientRef, _ portName: CFString!, _ readProc: MIDIReadProc, _ refCon: UnsafeMutablePointer<Void>, _ outPort: UnsafeMutablePointer<MIDIPortRef>) -> OSStatus ``` | OS X 10.0 |

Modified MIDINotifyProc

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDINotifyProc = CFunctionPointer<((ConstUnsafePointer<MIDINotification>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias MIDINotifyProc = CFunctionPointer<((UnsafePointer<MIDINotification>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified MIDIObjectFindByUniqueID(MIDIUniqueID, UnsafeMutablePointer<MIDIObjectRef>, UnsafeMutablePointer<MIDIObjectType>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIObjectFindByUniqueID(_ inUniqueID: MIDIUniqueID, _ outObject: UnsafePointer<MIDIObjectRef>, _ outObjectType: UnsafePointer<MIDIObjectType>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIObjectFindByUniqueID(_ inUniqueID: MIDIUniqueID, _ outObject: UnsafeMutablePointer<MIDIObjectRef>, _ outObjectType: UnsafeMutablePointer<MIDIObjectType>) -> OSStatus ``` | OS X 10.2 |

Modified MIDIObjectGetDataProperty(MIDIObjectRef, CFString!, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIObjectGetDataProperty(_ obj: MIDIObjectRef, _ propertyID: CFString!, _ outData: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIObjectGetDataProperty(_ obj: MIDIObjectRef, _ propertyID: CFString!, _ outData: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.0 |

Modified MIDIObjectGetDictionaryProperty(MIDIObjectRef, CFString!, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIObjectGetDictionaryProperty(_ obj: MIDIObjectRef, _ propertyID: CFString!, _ outDict: UnsafePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIObjectGetDictionaryProperty(_ obj: MIDIObjectRef, _ propertyID: CFString!, _ outDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` | OS X 10.2 |

Modified MIDIObjectGetIntegerProperty(MIDIObjectRef, CFString!, UnsafeMutablePointer<Int32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIObjectGetIntegerProperty(_ obj: MIDIObjectRef, _ propertyID: CFString!, _ outValue: UnsafePointer<Int32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIObjectGetIntegerProperty(_ obj: MIDIObjectRef, _ propertyID: CFString!, _ outValue: UnsafeMutablePointer<Int32>) -> OSStatus ``` | OS X 10.0 |

Modified MIDIObjectGetProperties(MIDIObjectRef, UnsafeMutablePointer<Unmanaged<CFPropertyList>?>, Boolean) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIObjectGetProperties(_ obj: MIDIObjectRef, _ outProperties: UnsafePointer<Unmanaged<CFPropertyListRef>?>, _ deep: Boolean) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIObjectGetProperties(_ obj: MIDIObjectRef, _ outProperties: UnsafeMutablePointer<Unmanaged<CFPropertyList>?>, _ deep: Boolean) -> OSStatus ``` | OS X 10.1 |

Modified MIDIObjectGetStringProperty(MIDIObjectRef, CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIObjectGetStringProperty(_ obj: MIDIObjectRef, _ propertyID: CFString!, _ str: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIObjectGetStringProperty(_ obj: MIDIObjectRef, _ propertyID: CFString!, _ str: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.0 |

Modified MIDIObjectRemoveProperty(MIDIObjectRef, CFString!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified MIDIObjectSetDataProperty(MIDIObjectRef, CFString!, CFData!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MIDIObjectSetDictionaryProperty(MIDIObjectRef, CFString!, CFDictionary!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified MIDIObjectSetIntegerProperty(MIDIObjectRef, CFString!, Int32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MIDIObjectSetStringProperty(MIDIObjectRef, CFString!, CFString!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MIDIOutputPortCreate(MIDIClientRef, CFString!, UnsafeMutablePointer<MIDIPortRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIOutputPortCreate(_ client: MIDIClientRef, _ portName: CFString!, _ outPort: UnsafePointer<MIDIPortRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIOutputPortCreate(_ client: MIDIClientRef, _ portName: CFString!, _ outPort: UnsafeMutablePointer<MIDIPortRef>) -> OSStatus ``` | OS X 10.0 |

Modified MIDIPacketListAdd(UnsafeMutablePointer<MIDIPacketList>, Int, UnsafeMutablePointer<MIDIPacket>, MIDITimeStamp, Int, UnsafePointer<UInt8>) -> UnsafeMutablePointer<MIDIPacket>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIPacketListAdd(_ pktlist: UnsafePointer<MIDIPacketList>, _ listSize: ByteCount, _ curPacket: UnsafePointer<MIDIPacket>, _ time: MIDITimeStamp, _ nData: ByteCount, _ data: ConstUnsafePointer<Byte>) -> UnsafePointer<MIDIPacket> ``` | OS X 10.10 |
| To | ``` func MIDIPacketListAdd(_ pktlist: UnsafeMutablePointer<MIDIPacketList>, _ listSize: Int, _ curPacket: UnsafeMutablePointer<MIDIPacket>, _ time: MIDITimeStamp, _ nData: Int, _ data: UnsafePointer<UInt8>) -> UnsafeMutablePointer<MIDIPacket> ``` | OS X 10.0 |

Modified MIDIPacketListInit(UnsafeMutablePointer<MIDIPacketList>) -> UnsafeMutablePointer<MIDIPacket>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIPacketListInit(_ pktlist: UnsafePointer<MIDIPacketList>) -> UnsafePointer<MIDIPacket> ``` | OS X 10.10 |
| To | ``` func MIDIPacketListInit(_ pktlist: UnsafeMutablePointer<MIDIPacketList>) -> UnsafeMutablePointer<MIDIPacket> ``` | OS X 10.0 |

Modified MIDIPortConnectSource(MIDIPortRef, MIDIEndpointRef, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIPortConnectSource(_ port: MIDIPortRef, _ source: MIDIEndpointRef, _ connRefCon: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIPortConnectSource(_ port: MIDIPortRef, _ source: MIDIEndpointRef, _ connRefCon: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.0 |

Modified MIDIPortDisconnectSource(MIDIPortRef, MIDIEndpointRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MIDIPortDispose(MIDIPortRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MIDIReadProc

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIReadProc = CFunctionPointer<((ConstUnsafePointer<MIDIPacketList>, UnsafePointer<()>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias MIDIReadProc = CFunctionPointer<((UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified MIDIReceived(MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIReceived(_ src: MIDIEndpointRef, _ pktlist: ConstUnsafePointer<MIDIPacketList>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIReceived(_ src: MIDIEndpointRef, _ pktlist: UnsafePointer<MIDIPacketList>) -> OSStatus ``` | OS X 10.0 |

Modified MIDIRestart() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified MIDISend(MIDIPortRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDISend(_ port: MIDIPortRef, _ dest: MIDIEndpointRef, _ pktlist: ConstUnsafePointer<MIDIPacketList>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDISend(_ port: MIDIPortRef, _ dest: MIDIEndpointRef, _ pktlist: UnsafePointer<MIDIPacketList>) -> OSStatus ``` | OS X 10.0 |

Modified MIDISendSysex(UnsafeMutablePointer<MIDISysexSendRequest>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDISendSysex(_ request: UnsafePointer<MIDISysexSendRequest>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDISendSysex(_ request: UnsafeMutablePointer<MIDISysexSendRequest>) -> OSStatus ``` | OS X 10.0 |

Modified MIDISetupAddDevice(MIDIDeviceRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified MIDISetupAddExternalDevice(MIDIDeviceRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified MIDISetupRemoveDevice(MIDIDeviceRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified MIDISetupRemoveExternalDevice(MIDIDeviceRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified MIDISourceCreate(MIDIClientRef, CFString!, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDISourceCreate(_ client: MIDIClientRef, _ name: CFString!, _ outSrc: UnsafePointer<MIDIEndpointRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDISourceCreate(_ client: MIDIClientRef, _ name: CFString!, _ outSrc: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus ``` | OS X 10.0 |

Modified MIDIThruConnectionCreate(CFString!, CFData!, UnsafeMutablePointer<MIDIThruConnectionRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIThruConnectionCreate(_ inPersistentOwnerID: CFString!, _ inConnectionParams: CFData!, _ outConnection: UnsafePointer<MIDIThruConnectionRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIThruConnectionCreate(_ inPersistentOwnerID: CFString!, _ inConnectionParams: CFData!, _ outConnection: UnsafeMutablePointer<MIDIThruConnectionRef>) -> OSStatus ``` | OS X 10.2 |

Modified MIDIThruConnectionDispose(MIDIThruConnectionRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified MIDIThruConnectionFind(CFString!, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIThruConnectionFind(_ inPersistentOwnerID: CFString!, _ outConnectionList: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIThruConnectionFind(_ inPersistentOwnerID: CFString!, _ outConnectionList: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.2 |

Modified MIDIThruConnectionGetParams(MIDIThruConnectionRef, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIThruConnectionGetParams(_ connection: MIDIThruConnectionRef, _ outConnectionParams: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MIDIThruConnectionGetParams(_ connection: MIDIThruConnectionRef, _ outConnectionParams: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.2 |

Modified MIDIThruConnectionParamsInitialize(UnsafeMutablePointer<MIDIThruConnectionParams>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MIDIThruConnectionParamsInitialize(_ inConnectionParams: UnsafePointer<MIDIThruConnectionParams>) ``` | OS X 10.10 |
| To | ``` func MIDIThruConnectionParamsInitialize(_ inConnectionParams: UnsafeMutablePointer<MIDIThruConnectionParams>) ``` | OS X 10.2 |

Modified MIDIThruConnectionSetParams(MIDIThruConnectionRef, CFData!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIDriverPropertyUsesSerial

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kMIDIPropertyAdvanceScheduleTimeMuSec

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified kMIDIPropertyCanRoute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified kMIDIPropertyConnectionUniqueID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kMIDIPropertyDeviceID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified kMIDIPropertyDisplayName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kMIDIPropertyDriverDeviceEditorApp

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kMIDIPropertyDriverOwner

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kMIDIPropertyDriverVersion

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyImage

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyIsBroadcast

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyIsDrumMachine

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyIsEffectUnit

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyIsEmbeddedEntity

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kMIDIPropertyIsMixer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyIsSampler

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyManufacturer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified kMIDIPropertyMaxReceiveChannels

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyMaxSysExSpeed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified kMIDIPropertyMaxTransmitChannels

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyModel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified kMIDIPropertyName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified kMIDIPropertyNameConfiguration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyOffline

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kMIDIPropertyPanDisruptsStereo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyPrivate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyReceiveChannels

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified kMIDIPropertyReceivesBankSelectLSB

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyReceivesBankSelectMSB

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyReceivesClock

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyReceivesMTC

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyReceivesNotes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyReceivesProgramChanges

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertySingleRealtimeEntity

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertySupportsGeneralMIDI

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertySupportsMMC

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertySupportsShowControl

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kMIDIPropertyTransmitChannels

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyTransmitsBankSelectLSB

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyTransmitsBankSelectMSB

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyTransmitsClock

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyTransmitsMTC

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyTransmitsNotes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyTransmitsProgramChanges

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kMIDIPropertyUniqueID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

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
