---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/CoreMIDI.html
archived_at: '2026-07-18T02:56:45.611200Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreMIDI Changes for Swift

### CoreMIDI

Removed MIDIDriverInterface.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, FindDevices: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)>, Start: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)>, Stop: CFunctionPointer<((MIDIDriverRef) -> OSStatus)>, Configure: CFunctionPointer<((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)>, Send: CFunctionPointer<((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)>, EnableSource: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, Boolean) -> OSStatus)>, Flush: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)>, Monitor: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)>)Removed MIDIObjectPropertyChangeNotification.init()Removed MIDIObjectPropertyChangeNotification.init(messageID: MIDINotificationMessageID, messageSize: UInt32, object: MIDIObjectRef, objectType: MIDIObjectType, propertyName: Unmanaged<CFString>!)Removed MIDISysexSendRequest.init()Removed MIDISysexSendRequest.init(destination: MIDIEndpointRef, data: UnsafePointer<UInt8>, bytesToSend: UInt32, complete: Boolean, reserved: (UInt8, UInt8, UInt8), completionProc: MIDICompletionProc, completionRefCon: UnsafeMutablePointer<Void>)Removed kMIDIControlType_14BitRemoved kMIDIControlType_14BitNRPNRemoved kMIDIControlType_14BitRPNRemoved kMIDIControlType_7BitRemoved kMIDIControlType_7BitNRPNRemoved kMIDIControlType_7BitRPNRemoved kMIDIMsgIOErrorRemoved kMIDIMsgObjectAddedRemoved kMIDIMsgObjectRemovedRemoved kMIDIMsgPropertyChangedRemoved kMIDIMsgSerialPortOwnerChangedRemoved kMIDIMsgSetupChangedRemoved kMIDIMsgThruConnectionsChangedRemoved kMIDIObjectType_DestinationRemoved kMIDIObjectType_DeviceRemoved kMIDIObjectType_EntityRemoved kMIDIObjectType_ExternalDestinationRemoved kMIDIObjectType_ExternalDeviceRemoved kMIDIObjectType_ExternalEntityRemoved kMIDIObjectType_ExternalSourceRemoved kMIDIObjectType_OtherRemoved kMIDIObjectType_SourceRemoved kMIDITransform_AddRemoved kMIDITransform_FilterOutRemoved kMIDITransform_MapControlRemoved kMIDITransform_MapValueRemoved kMIDITransform_MaxValueRemoved kMIDITransform_MinValueRemoved kMIDITransform_NoneRemoved kMIDITransform_ScaleRemoved MIDINetworkConnectionPolicyRemoved MIDINetworkConnectionPolicy_AnyoneRemoved MIDINetworkConnectionPolicy_HostsInContactListRemoved MIDINetworkConnectionPolicy_NoOneRemoved MIDINotificationMessageIDRemoved MIDIObjectTypeRemoved MIDITransformControlTypeRemoved MIDITransformTypeAdded MIDIDriverInterface.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, FindDevices: ((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)!, Start: ((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)!, Stop: ((MIDIDriverRef) -> OSStatus)!, Configure: ((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)!, Send: ((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)!, EnableSource: ((MIDIDriverRef, MIDIEndpointRef, DarwinBoolean) -> OSStatus)!, Flush: ((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)!, Monitor: ((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)!)Added [MIDINetworkConnectionPolicy [enum]](https://developer.apple.com/documentation/coremidi/midinetworkconnectionpolicy)Added [MIDINetworkConnectionPolicy.Anyone](https://developer.apple.com/documentation/coremidi/midinetworkconnectionpolicy/anyone)Added [MIDINetworkConnectionPolicy.HostsInContactList](https://developer.apple.com/documentation/coremidi/midinetworkconnectionpolicy/hostsincontactlist)Added [MIDINetworkConnectionPolicy.NoOne](https://developer.apple.com/documentation/coremidi/midinetworkconnectionpolicy/noone)Added [MIDINotificationMessageID [enum]](https://developer.apple.com/documentation/coremidi/midinotificationmessageid)Added [MIDINotificationMessageID.MsgIOError](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/msgioerror)Added [MIDINotificationMessageID.MsgObjectAdded](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/kmidimsgobjectadded)Added [MIDINotificationMessageID.MsgObjectRemoved](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/msgobjectremoved)Added [MIDINotificationMessageID.MsgPropertyChanged](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/msgpropertychanged)Added [MIDINotificationMessageID.MsgSerialPortOwnerChanged](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/kmidimsgserialportownerchanged)Added [MIDINotificationMessageID.MsgSetupChanged](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/kmidimsgsetupchanged)Added [MIDINotificationMessageID.MsgThruConnectionsChanged](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/msgthruconnectionschanged)Added [MIDIObjectType [enum]](https://developer.apple.com/documentation/coremidi/midiobjecttype)Added [MIDIObjectType.Destination](https://developer.apple.com/documentation/coremidi/midiobjecttype/kmidiobjecttype_destination)Added [MIDIObjectType.Device](https://developer.apple.com/documentation/coremidi/midiobjecttype/device)Added [MIDIObjectType.Entity](https://developer.apple.com/documentation/coremidi/midiobjecttype/kmidiobjecttype_entity)Added [MIDIObjectType.ExternalDestination](https://developer.apple.com/documentation/coremidi/midiobjecttype/externaldestination)Added [MIDIObjectType.ExternalDevice](https://developer.apple.com/documentation/coremidi/midiobjecttype/externaldevice)Added [MIDIObjectType.ExternalEntity](https://developer.apple.com/documentation/coremidi/midiobjecttype/kmidiobjecttype_externalentity)Added [MIDIObjectType.ExternalSource](https://developer.apple.com/documentation/coremidi/midiobjecttype/kmidiobjecttype_externalsource)Added [MIDIObjectType.Other](https://developer.apple.com/documentation/coremidi/midiobjecttype/other)Added [MIDIObjectType.Source](https://developer.apple.com/documentation/coremidi/midiobjecttype/kmidiobjecttype_source)Added [MIDITransformControlType [enum]](https://developer.apple.com/documentation/coremidi/miditransformcontroltype)Added [MIDITransformControlType.ControlType_14Bit](https://developer.apple.com/documentation/coremidi/miditransformcontroltype/kmidicontroltype_14bit)Added [MIDITransformControlType.ControlType_14BitNRPN](https://developer.apple.com/documentation/coremidi/miditransformcontroltype/controltype_14bitnrpn)Added [MIDITransformControlType.ControlType_14BitRPN](https://developer.apple.com/documentation/coremidi/miditransformcontroltype/kmidicontroltype_14bitrpn)Added [MIDITransformControlType.ControlType_7Bit](https://developer.apple.com/documentation/coremidi/miditransformcontroltype/controltype_7bit)Added [MIDITransformControlType.ControlType_7BitNRPN](https://developer.apple.com/documentation/coremidi/miditransformcontroltype/controltype_7bitnrpn)Added [MIDITransformControlType.ControlType_7BitRPN](https://developer.apple.com/documentation/coremidi/miditransformcontroltype/kmidicontroltype_7bitrpn)Added [MIDITransformType [enum]](https://developer.apple.com/documentation/coremidi/miditransformtype)Added [MIDITransformType.Add](https://developer.apple.com/documentation/coremidi/miditransformtype/kmiditransform_add)Added [MIDITransformType.FilterOut](https://developer.apple.com/documentation/coremidi/miditransformtype/kmiditransform_filterout)Added [MIDITransformType.MapControl](https://developer.apple.com/documentation/coremidi/miditransformtype/kmiditransform_mapcontrol)Added [MIDITransformType.MapValue](https://developer.apple.com/documentation/coremidi/miditransformtype/kmiditransform_mapvalue)Added [MIDITransformType.MaxValue](https://developer.apple.com/documentation/coremidi/miditransformtype/kmiditransform_maxvalue)Added [MIDITransformType.MinValue](https://developer.apple.com/documentation/coremidi/miditransformtype/kmiditransform_minvalue)Added [MIDITransformType.None](https://developer.apple.com/documentation/coremidi/miditransformtype/kmiditransform_none)Added [MIDITransformType.Scale](https://developer.apple.com/documentation/coremidi/miditransformtype/scale)Added [MIDIClientCreateWithBlock(_: CFString, _: UnsafeMutablePointer<MIDIClientRef>, _: MIDINotifyBlock?) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495330-midiclientcreatewithblock)Added [MIDIDestinationCreateWithBlock(_: MIDIClientRef, _: CFString, _: UnsafeMutablePointer<MIDIEndpointRef>, _: MIDIReadBlock) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495247-mididestinationcreatewithblock)Added [MIDIInputPortCreateWithBlock(_: MIDIClientRef, _: CFString, _: UnsafeMutablePointer<MIDIPortRef>, _: MIDIReadBlock) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495333-midiinputportcreatewithblock)Added [MIDINotifyBlock](https://developer.apple.com/documentation/coremidi/midinotifyblock)Added [MIDIPacketNext(_: UnsafePointer<MIDIPacket>) -> UnsafeMutablePointer<MIDIPacket>](https://developer.apple.com/documentation/coremidi/1495178-midipacketnext)Added [MIDIReadBlock](https://developer.apple.com/documentation/coremidi/midireadblock)Added [MIDIThruConnectionParamsSize(_: UnsafePointer<MIDIThruConnectionParams>) -> Int](https://developer.apple.com/documentation/coremidi/1508275-midithruconnectionparamssize)Modified MIDIControlTransform.init(controlType: MIDITransformControlType, remappedControlType: MIDITransformControlType, controlNumber: UInt16, transform: MIDITransformType, param: Int16)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified [MIDIDriverInterface [struct]](https://developer.apple.com/documentation/coremidi/mididriverinterface)

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIDriverInterface {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>     var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var FindDevices: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)>     var Start: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)>     var Stop: CFunctionPointer<((MIDIDriverRef) -> OSStatus)>     var Configure: CFunctionPointer<((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)>     var Send: CFunctionPointer<((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)>     var EnableSource: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, Boolean) -> OSStatus)>     var Flush: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)>     var Monitor: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)>     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, FindDevices FindDevices: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)>, Start Start: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)>, Stop Stop: CFunctionPointer<((MIDIDriverRef) -> OSStatus)>, Configure Configure: CFunctionPointer<((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)>, Send Send: CFunctionPointer<((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)>, EnableSource EnableSource: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, Boolean) -> OSStatus)>, Flush Flush: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)>, Monitor Monitor: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)>) } ``` |
| To | ``` struct MIDIDriverInterface {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!     var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!     var Release: ((UnsafeMutablePointer<Void>) -> ULONG)!     var FindDevices: ((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)!     var Start: ((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)!     var Stop: ((MIDIDriverRef) -> OSStatus)!     var Configure: ((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)!     var Send: ((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)!     var EnableSource: ((MIDIDriverRef, MIDIEndpointRef, DarwinBoolean) -> OSStatus)!     var Flush: ((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)!     var Monitor: ((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)!     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, FindDevices FindDevices: ((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)!, Start Start: ((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)!, Stop Stop: ((MIDIDriverRef) -> OSStatus)!, Configure Configure: ((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)!, Send Send: ((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)!, EnableSource EnableSource: ((MIDIDriverRef, MIDIEndpointRef, DarwinBoolean) -> OSStatus)!, Flush Flush: ((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)!, Monitor Monitor: ((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)!) } ``` |

Modified [MIDIDriverInterface.AddRef](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508512-addref)

|  | Declaration |
| --- | --- |
| From | ``` var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)> ``` |
| To | ``` var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |

Modified [MIDIDriverInterface.Configure](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508254-configure)

|  | Declaration |
| --- | --- |
| From | ``` var Configure: CFunctionPointer<((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)> ``` |
| To | ``` var Configure: ((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)! ``` |

Modified [MIDIDriverInterface.EnableSource](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508318-enablesource)

|  | Declaration |
| --- | --- |
| From | ``` var EnableSource: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, Boolean) -> OSStatus)> ``` |
| To | ``` var EnableSource: ((MIDIDriverRef, MIDIEndpointRef, DarwinBoolean) -> OSStatus)! ``` |

Modified [MIDIDriverInterface.FindDevices](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508437-finddevices)

|  | Declaration |
| --- | --- |
| From | ``` var FindDevices: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)> ``` |
| To | ``` var FindDevices: ((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)! ``` |

Modified [MIDIDriverInterface.Flush](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508514-flush)

|  | Declaration |
| --- | --- |
| From | ``` var Flush: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` var Flush: ((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)! ``` |

Modified [MIDIDriverInterface.Monitor](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508375-monitor)

|  | Declaration |
| --- | --- |
| From | ``` var Monitor: CFunctionPointer<((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)> ``` |
| To | ``` var Monitor: ((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)! ``` |

Modified [MIDIDriverInterface.QueryInterface](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508283-queryinterface)

|  | Declaration |
| --- | --- |
| From | ``` var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)> ``` |
| To | ``` var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)! ``` |

Modified [MIDIDriverInterface.Release](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508249-release)

|  | Declaration |
| --- | --- |
| From | ``` var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)> ``` |
| To | ``` var Release: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |

Modified [MIDIDriverInterface.Send](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508332-send)

|  | Declaration |
| --- | --- |
| From | ``` var Send: CFunctionPointer<((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` var Send: ((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)! ``` |

Modified [MIDIDriverInterface.Start](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508269-start)

|  | Declaration |
| --- | --- |
| From | ``` var Start: CFunctionPointer<((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)> ``` |
| To | ``` var Start: ((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)! ``` |

Modified [MIDIDriverInterface.Stop](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508529-stop)

|  | Declaration |
| --- | --- |
| From | ``` var Stop: CFunctionPointer<((MIDIDriverRef) -> OSStatus)> ``` |
| To | ``` var Stop: ((MIDIDriverRef) -> OSStatus)! ``` |

Modified MIDIIOErrorNotification.init(messageID: MIDINotificationMessageID, messageSize: UInt32, driverDevice: MIDIDeviceRef, errorCode: OSStatus)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified [MIDINetworkConnection](https://developer.apple.com/documentation/coremidi/midinetworkconnection)

|  | Declaration |
| --- | --- |
| From | ``` class MIDINetworkConnection : NSObject {     class func connectionWithHost(_ host: MIDINetworkHost!) -> AnyObject!     var host: MIDINetworkHost! { get } } ``` |
| To | ``` class MIDINetworkConnection : NSObject {     convenience init(host host: MIDINetworkHost)     class func connectionWithHost(_ host: MIDINetworkHost) -> Self     var host: MIDINetworkHost { get } } ``` |

Modified [MIDINetworkConnection.host](https://developer.apple.com/documentation/coremidi/midinetworkconnection/1619334-host)

|  | Declaration |
| --- | --- |
| From | ``` var host: MIDINetworkHost! { get } ``` |
| To | ``` var host: MIDINetworkHost { get } ``` |

Modified [MIDINetworkConnection.init(host: MIDINetworkHost)](https://developer.apple.com/documentation/coremidi/midinetworkconnection/1619340-init)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | connectionWithHost(_:) | ``` class func connectionWithHost(_ host: MIDINetworkHost!) -> AnyObject! ``` | iOS 8.0 |
| To | init(host:) | ``` convenience init(host host: MIDINetworkHost) ``` | iOS 9.0 |

Modified [MIDINetworkHost](https://developer.apple.com/documentation/coremidi/midinetworkhost)

|  | Declaration |
| --- | --- |
| From | ``` class MIDINetworkHost : NSObject {     class func hostWithName(_ name: String!, address address: String!, port port: Int) -> AnyObject!     class func hostWithName(_ name: String!, netService netService: NSNetService!) -> AnyObject!     class func hostWithName(_ name: String!, netServiceName netServiceName: String!, netServiceDomain netServiceDomain: String!) -> AnyObject!     func hasSameAddressAs(_ other: MIDINetworkHost!) -> Bool     var name: String! { get }     var address: String! { get }     var port: Int { get }     var netServiceName: String! { get }     var netServiceDomain: String! { get } } ``` |
| To | ``` class MIDINetworkHost : NSObject {     convenience init(name name: String, address address: String, port port: Int)     class func hostWithName(_ name: String, address address: String, port port: Int) -> Self     convenience init(name name: String, netService netService: NSNetService)     class func hostWithName(_ name: String, netService netService: NSNetService) -> Self     convenience init(name name: String, netServiceName netServiceName: String, netServiceDomain netServiceDomain: String)     class func hostWithName(_ name: String, netServiceName netServiceName: String, netServiceDomain netServiceDomain: String) -> Self     func hasSameAddressAs(_ other: MIDINetworkHost) -> Bool     var name: String { get }     var address: String { get }     var port: Int { get }     var netServiceName: String? { get }     var netServiceDomain: String? { get } } ``` |

Modified [MIDINetworkHost.address](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619353-address)

|  | Declaration |
| --- | --- |
| From | ``` var address: String! { get } ``` |
| To | ``` var address: String { get } ``` |

Modified [MIDINetworkHost.hasSameAddressAs(_: MIDINetworkHost) -> Bool](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619372-hassameaddress)

|  | Declaration |
| --- | --- |
| From | ``` func hasSameAddressAs(_ other: MIDINetworkHost!) -> Bool ``` |
| To | ``` func hasSameAddressAs(_ other: MIDINetworkHost) -> Bool ``` |

Modified [MIDINetworkHost.init(name: String, address: String, port: Int)](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619365-init)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | hostWithName(_:address:port:) | ``` class func hostWithName(_ name: String!, address address: String!, port port: Int) -> AnyObject! ``` | iOS 8.0 |
| To | init(name:address:port:) | ``` convenience init(name name: String, address address: String, port port: Int) ``` | iOS 9.0 |

Modified [MIDINetworkHost.init(name: String, netService: NSNetService)](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619371-init)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | hostWithName(_:netService:) | ``` class func hostWithName(_ name: String!, netService netService: NSNetService!) -> AnyObject! ``` | iOS 8.0 |
| To | init(name:netService:) | ``` convenience init(name name: String, netService netService: NSNetService) ``` | iOS 9.0 |

Modified [MIDINetworkHost.init(name: String, netServiceName: String, netServiceDomain: String)](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619338-init)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | hostWithName(_:netServiceName:netServiceDomain:) | ``` class func hostWithName(_ name: String!, netServiceName netServiceName: String!, netServiceDomain netServiceDomain: String!) -> AnyObject! ``` | iOS 8.0 |
| To | init(name:netServiceName:netServiceDomain:) | ``` convenience init(name name: String, netServiceName netServiceName: String, netServiceDomain netServiceDomain: String) ``` | iOS 9.0 |

Modified [MIDINetworkHost.name](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619339-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [MIDINetworkHost.netServiceDomain](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619344-netservicedomain)

|  | Declaration |
| --- | --- |
| From | ``` var netServiceDomain: String! { get } ``` |
| To | ``` var netServiceDomain: String? { get } ``` |

Modified [MIDINetworkHost.netServiceName](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619362-netservicename)

|  | Declaration |
| --- | --- |
| From | ``` var netServiceName: String! { get } ``` |
| To | ``` var netServiceName: String? { get } ``` |

Modified [MIDINetworkSession](https://developer.apple.com/documentation/coremidi/midinetworksession)

|  | Declaration |
| --- | --- |
| From | ``` class MIDINetworkSession : NSObject {     class func defaultSession() -> MIDINetworkSession!     var enabled: Bool     var networkPort: Int { get }     var networkName: String! { get }     var localName: String! { get }     var connectionPolicy: MIDINetworkConnectionPolicy     func contacts() -> Set<NSObject>!     func addContact(_ contact: MIDINetworkHost!) -> Bool     func removeContact(_ contact: MIDINetworkHost!) -> Bool     func connections() -> Set<NSObject>!     func addConnection(_ connection: MIDINetworkConnection!) -> Bool     func removeConnection(_ connection: MIDINetworkConnection!) -> Bool     func sourceEndpoint() -> MIDIEndpointRef     func destinationEndpoint() -> MIDIEndpointRef } ``` |
| To | ``` class MIDINetworkSession : NSObject {     class func defaultSession() -> MIDINetworkSession     var enabled: Bool     var networkPort: Int { get }     var networkName: String { get }     var localName: String { get }     var connectionPolicy: MIDINetworkConnectionPolicy     func contacts() -> Set<MIDINetworkHost>     func addContact(_ contact: MIDINetworkHost) -> Bool     func removeContact(_ contact: MIDINetworkHost) -> Bool     func connections() -> Set<MIDINetworkConnection>     func addConnection(_ connection: MIDINetworkConnection) -> Bool     func removeConnection(_ connection: MIDINetworkConnection) -> Bool     func sourceEndpoint() -> MIDIEndpointRef     func destinationEndpoint() -> MIDIEndpointRef } ``` |

Modified [MIDINetworkSession.addConnection(_: MIDINetworkConnection) -> Bool](https://developer.apple.com/documentation/coremidi/midinetworksession/1619369-addconnection)

|  | Declaration |
| --- | --- |
| From | ``` func addConnection(_ connection: MIDINetworkConnection!) -> Bool ``` |
| To | ``` func addConnection(_ connection: MIDINetworkConnection) -> Bool ``` |

Modified [MIDINetworkSession.addContact(_: MIDINetworkHost) -> Bool](https://developer.apple.com/documentation/coremidi/midinetworksession/1619361-addcontact)

|  | Declaration |
| --- | --- |
| From | ``` func addContact(_ contact: MIDINetworkHost!) -> Bool ``` |
| To | ``` func addContact(_ contact: MIDINetworkHost) -> Bool ``` |

Modified [MIDINetworkSession.connections() -> Set<MIDINetworkConnection>](https://developer.apple.com/documentation/coremidi/midinetworksession/1619366-connections)

|  | Declaration |
| --- | --- |
| From | ``` func connections() -> Set<NSObject>! ``` |
| To | ``` func connections() -> Set<MIDINetworkConnection> ``` |

Modified [MIDINetworkSession.contacts() -> Set<MIDINetworkHost>](https://developer.apple.com/documentation/coremidi/midinetworksession/1619335-contacts)

|  | Declaration |
| --- | --- |
| From | ``` func contacts() -> Set<NSObject>! ``` |
| To | ``` func contacts() -> Set<MIDINetworkHost> ``` |

Modified [MIDINetworkSession.defaultSession() -> MIDINetworkSession [class]](https://developer.apple.com/documentation/coremidi/midinetworksession/1619363-default)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultSession() -> MIDINetworkSession! ``` |
| To | ``` class func defaultSession() -> MIDINetworkSession ``` |

Modified [MIDINetworkSession.localName](https://developer.apple.com/documentation/coremidi/midinetworksession/1619358-localname)

|  | Declaration |
| --- | --- |
| From | ``` var localName: String! { get } ``` |
| To | ``` var localName: String { get } ``` |

Modified [MIDINetworkSession.networkName](https://developer.apple.com/documentation/coremidi/midinetworksession/1619336-networkname)

|  | Declaration |
| --- | --- |
| From | ``` var networkName: String! { get } ``` |
| To | ``` var networkName: String { get } ``` |

Modified [MIDINetworkSession.removeConnection(_: MIDINetworkConnection) -> Bool](https://developer.apple.com/documentation/coremidi/midinetworksession/1619346-removeconnection)

|  | Declaration |
| --- | --- |
| From | ``` func removeConnection(_ connection: MIDINetworkConnection!) -> Bool ``` |
| To | ``` func removeConnection(_ connection: MIDINetworkConnection) -> Bool ``` |

Modified [MIDINetworkSession.removeContact(_: MIDINetworkHost) -> Bool](https://developer.apple.com/documentation/coremidi/midinetworksession/1619332-removecontact)

|  | Declaration |
| --- | --- |
| From | ``` func removeContact(_ contact: MIDINetworkHost!) -> Bool ``` |
| To | ``` func removeContact(_ contact: MIDINetworkHost) -> Bool ``` |

Modified MIDINotification.init(messageID: MIDINotificationMessageID, messageSize: UInt32)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified MIDIObjectAddRemoveNotification.init(messageID: MIDINotificationMessageID, messageSize: UInt32, parent: MIDIObjectRef, parentType: MIDIObjectType, child: MIDIObjectRef, childType: MIDIObjectType)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified [MIDIObjectPropertyChangeNotification [struct]](https://developer.apple.com/documentation/coremidi/midiobjectpropertychangenotification)

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIObjectPropertyChangeNotification {     var messageID: MIDINotificationMessageID     var messageSize: UInt32     var object: MIDIObjectRef     var objectType: MIDIObjectType     var propertyName: Unmanaged<CFString>!     init()     init(messageID messageID: MIDINotificationMessageID, messageSize messageSize: UInt32, object object: MIDIObjectRef, objectType objectType: MIDIObjectType, propertyName propertyName: Unmanaged<CFString>!) } ``` |
| To | ``` struct MIDIObjectPropertyChangeNotification {     var messageID: MIDINotificationMessageID     var messageSize: UInt32     var object: MIDIObjectRef     var objectType: MIDIObjectType     var propertyName: Unmanaged<CFString> } ``` |

Modified [MIDIObjectPropertyChangeNotification.propertyName](https://developer.apple.com/documentation/coremidi/midiobjectpropertychangenotification/1495390-propertyname)

|  | Declaration |
| --- | --- |
| From | ``` var propertyName: Unmanaged<CFString>! ``` |
| To | ``` var propertyName: Unmanaged<CFString> ``` |

Modified [MIDISysexSendRequest [struct]](https://developer.apple.com/documentation/coremidi/midisysexsendrequest)

|  | Declaration |
| --- | --- |
| From | ``` struct MIDISysexSendRequest {     var destination: MIDIEndpointRef     var data: UnsafePointer<UInt8>     var bytesToSend: UInt32     var complete: Boolean     var reserved: (UInt8, UInt8, UInt8)     var completionProc: MIDICompletionProc     var completionRefCon: UnsafeMutablePointer<Void>     init()     init(destination destination: MIDIEndpointRef, data data: UnsafePointer<UInt8>, bytesToSend bytesToSend: UInt32, complete complete: Boolean, reserved reserved: (UInt8, UInt8, UInt8), completionProc completionProc: MIDICompletionProc, completionRefCon completionRefCon: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct MIDISysexSendRequest {     var destination: MIDIEndpointRef     var data: UnsafePointer<UInt8>     var bytesToSend: UInt32     var complete: DarwinBoolean     var reserved: (UInt8, UInt8, UInt8)     var completionProc: MIDICompletionProc     var completionRefCon: UnsafeMutablePointer<Void> } ``` |

Modified [MIDISysexSendRequest.complete](https://developer.apple.com/documentation/coremidi/midisysexsendrequest/1495214-complete)

|  | Declaration |
| --- | --- |
| From | ``` var complete: Boolean ``` |
| To | ``` var complete: DarwinBoolean ``` |

Modified MIDIThruConnectionEndpoint.init(endpointRef: MIDIEndpointRef, uniqueID: MIDIUniqueID)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified MIDITransform.init(transform: MIDITransformType, param: Int16)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified [kMIDIIDNotUnique](https://developer.apple.com/documentation/coremidi/1495156-error_constants/kmidiidnotunique)

|  | Declaration |
| --- | --- |
| From | ``` var kMIDIIDNotUnique: Int { get } ``` |
| To | ``` var kMIDIIDNotUnique: OSStatus { get } ``` |

Modified [kMIDIInvalidClient](https://developer.apple.com/documentation/coremidi/kmidiinvalidclient)

|  | Declaration |
| --- | --- |
| From | ``` var kMIDIInvalidClient: Int { get } ``` |
| To | ``` var kMIDIInvalidClient: OSStatus { get } ``` |

Modified [kMIDIInvalidPort](https://developer.apple.com/documentation/coremidi/1495156-error_constants/kmidiinvalidport)

|  | Declaration |
| --- | --- |
| From | ``` var kMIDIInvalidPort: Int { get } ``` |
| To | ``` var kMIDIInvalidPort: OSStatus { get } ``` |

Modified [kMIDIInvalidUniqueID](https://developer.apple.com/documentation/coremidi/1495307-kmidiinvaliduniqueid/kmidiinvaliduniqueid)

|  | Declaration |
| --- | --- |
| From | ``` var kMIDIInvalidUniqueID: Int { get } ``` |
| To | ``` var kMIDIInvalidUniqueID: MIDIUniqueID { get } ``` |

Modified [kMIDIMessageSendErr](https://developer.apple.com/documentation/coremidi/1495156-error_constants/kmidimessagesenderr)

|  | Declaration |
| --- | --- |
| From | ``` var kMIDIMessageSendErr: Int { get } ``` |
| To | ``` var kMIDIMessageSendErr: OSStatus { get } ``` |

Modified [kMIDINoConnection](https://developer.apple.com/documentation/coremidi/kmidinoconnection)

|  | Declaration |
| --- | --- |
| From | ``` var kMIDINoConnection: Int { get } ``` |
| To | ``` var kMIDINoConnection: OSStatus { get } ``` |

Modified [kMIDINoCurrentSetup](https://developer.apple.com/documentation/coremidi/1495156-error_constants/kmidinocurrentsetup)

|  | Declaration |
| --- | --- |
| From | ``` var kMIDINoCurrentSetup: Int { get } ``` |
| To | ``` var kMIDINoCurrentSetup: OSStatus { get } ``` |

Modified [kMIDINotPermitted](https://developer.apple.com/documentation/coremidi/1495156-error_constants/kmidinotpermitted)

|  | Declaration |
| --- | --- |
| From | ``` var kMIDINotPermitted: Int { get } ``` |
| To | ``` var kMIDINotPermitted: OSStatus { get } ``` |

Modified [kMIDIObjectNotFound](https://developer.apple.com/documentation/coremidi/1495156-error_constants/kmidiobjectnotfound)

|  | Declaration |
| --- | --- |
| From | ``` var kMIDIObjectNotFound: Int { get } ``` |
| To | ``` var kMIDIObjectNotFound: OSStatus { get } ``` |

Modified [kMIDIObjectType_ExternalMask](https://developer.apple.com/documentation/coremidi/kmidiobjecttype_externalmask)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kMIDIObjectType_ExternalMask: Int { get } ``` | iOS 8.0 |
| To | ``` let kMIDIObjectType_ExternalMask: MIDIObjectType ``` | iOS 9.0 |

Modified [kMIDIPropertyAdvanceScheduleTimeMuSec](https://developer.apple.com/documentation/coremidi/kmidipropertyadvancescheduletimemusec)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyAdvanceScheduleTimeMuSec: CFString! ``` |
| To | ``` let kMIDIPropertyAdvanceScheduleTimeMuSec: CFString ``` |

Modified [kMIDIPropertyCanRoute](https://developer.apple.com/documentation/coremidi/kmidipropertycanroute)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyCanRoute: CFString! ``` |
| To | ``` let kMIDIPropertyCanRoute: CFString ``` |

Modified [kMIDIPropertyConnectionUniqueID](https://developer.apple.com/documentation/coremidi/kmidipropertyconnectionuniqueid)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyConnectionUniqueID: CFString! ``` |
| To | ``` let kMIDIPropertyConnectionUniqueID: CFString ``` |

Modified [kMIDIPropertyDeviceID](https://developer.apple.com/documentation/coremidi/kmidipropertydeviceid)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyDeviceID: CFString! ``` |
| To | ``` let kMIDIPropertyDeviceID: CFString ``` |

Modified [kMIDIPropertyDisplayName](https://developer.apple.com/documentation/coremidi/kmidipropertydisplayname)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyDisplayName: CFString! ``` |
| To | ``` let kMIDIPropertyDisplayName: CFString ``` |

Modified [kMIDIPropertyDriverDeviceEditorApp](https://developer.apple.com/documentation/coremidi/kmidipropertydriverdeviceeditorapp)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyDriverDeviceEditorApp: CFString! ``` |
| To | ``` let kMIDIPropertyDriverDeviceEditorApp: CFString ``` |

Modified [kMIDIPropertyDriverOwner](https://developer.apple.com/documentation/coremidi/kmidipropertydriverowner)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyDriverOwner: CFString! ``` |
| To | ``` let kMIDIPropertyDriverOwner: CFString ``` |

Modified [kMIDIPropertyDriverVersion](https://developer.apple.com/documentation/coremidi/kmidipropertydriverversion)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyDriverVersion: CFString! ``` |
| To | ``` let kMIDIPropertyDriverVersion: CFString ``` |

Modified [kMIDIPropertyImage](https://developer.apple.com/documentation/coremidi/kmidipropertyimage)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyImage: CFString! ``` |
| To | ``` let kMIDIPropertyImage: CFString ``` |

Modified [kMIDIPropertyIsBroadcast](https://developer.apple.com/documentation/coremidi/kmidipropertyisbroadcast)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyIsBroadcast: CFString! ``` |
| To | ``` let kMIDIPropertyIsBroadcast: CFString ``` |

Modified [kMIDIPropertyIsDrumMachine](https://developer.apple.com/documentation/coremidi/kmidipropertyisdrummachine)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyIsDrumMachine: CFString! ``` |
| To | ``` let kMIDIPropertyIsDrumMachine: CFString ``` |

Modified [kMIDIPropertyIsEffectUnit](https://developer.apple.com/documentation/coremidi/kmidipropertyiseffectunit)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyIsEffectUnit: CFString! ``` |
| To | ``` let kMIDIPropertyIsEffectUnit: CFString ``` |

Modified [kMIDIPropertyIsEmbeddedEntity](https://developer.apple.com/documentation/coremidi/kmidipropertyisembeddedentity)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyIsEmbeddedEntity: CFString! ``` |
| To | ``` let kMIDIPropertyIsEmbeddedEntity: CFString ``` |

Modified [kMIDIPropertyIsMixer](https://developer.apple.com/documentation/coremidi/kmidipropertyismixer)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyIsMixer: CFString! ``` |
| To | ``` let kMIDIPropertyIsMixer: CFString ``` |

Modified [kMIDIPropertyIsSampler](https://developer.apple.com/documentation/coremidi/kmidipropertyissampler)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyIsSampler: CFString! ``` |
| To | ``` let kMIDIPropertyIsSampler: CFString ``` |

Modified [kMIDIPropertyManufacturer](https://developer.apple.com/documentation/coremidi/kmidipropertymanufacturer)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyManufacturer: CFString! ``` |
| To | ``` let kMIDIPropertyManufacturer: CFString ``` |

Modified [kMIDIPropertyMaxReceiveChannels](https://developer.apple.com/documentation/coremidi/kmidipropertymaxreceivechannels)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyMaxReceiveChannels: CFString! ``` |
| To | ``` let kMIDIPropertyMaxReceiveChannels: CFString ``` |

Modified [kMIDIPropertyMaxSysExSpeed](https://developer.apple.com/documentation/coremidi/kmidipropertymaxsysexspeed)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyMaxSysExSpeed: CFString! ``` |
| To | ``` let kMIDIPropertyMaxSysExSpeed: CFString ``` |

Modified [kMIDIPropertyMaxTransmitChannels](https://developer.apple.com/documentation/coremidi/kmidipropertymaxtransmitchannels)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyMaxTransmitChannels: CFString! ``` |
| To | ``` let kMIDIPropertyMaxTransmitChannels: CFString ``` |

Modified [kMIDIPropertyModel](https://developer.apple.com/documentation/coremidi/kmidipropertymodel)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyModel: CFString! ``` |
| To | ``` let kMIDIPropertyModel: CFString ``` |

Modified [kMIDIPropertyName](https://developer.apple.com/documentation/coremidi/kmidipropertyname)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyName: CFString! ``` |
| To | ``` let kMIDIPropertyName: CFString ``` |

Modified [kMIDIPropertyNameConfiguration](https://developer.apple.com/documentation/coremidi/kmidipropertynameconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyNameConfiguration: CFString! ``` |
| To | ``` let kMIDIPropertyNameConfiguration: CFString ``` |

Modified [kMIDIPropertyOffline](https://developer.apple.com/documentation/coremidi/kmidipropertyoffline)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyOffline: CFString! ``` |
| To | ``` let kMIDIPropertyOffline: CFString ``` |

Modified [kMIDIPropertyPanDisruptsStereo](https://developer.apple.com/documentation/coremidi/kmidipropertypandisruptsstereo)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyPanDisruptsStereo: CFString! ``` |
| To | ``` let kMIDIPropertyPanDisruptsStereo: CFString ``` |

Modified [kMIDIPropertyPrivate](https://developer.apple.com/documentation/coremidi/kmidipropertyprivate)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyPrivate: CFString! ``` |
| To | ``` let kMIDIPropertyPrivate: CFString ``` |

Modified [kMIDIPropertyReceiveChannels](https://developer.apple.com/documentation/coremidi/kmidipropertyreceivechannels)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyReceiveChannels: CFString! ``` |
| To | ``` let kMIDIPropertyReceiveChannels: CFString ``` |

Modified [kMIDIPropertyReceivesBankSelectLSB](https://developer.apple.com/documentation/coremidi/kmidipropertyreceivesbankselectlsb)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyReceivesBankSelectLSB: CFString! ``` |
| To | ``` let kMIDIPropertyReceivesBankSelectLSB: CFString ``` |

Modified [kMIDIPropertyReceivesBankSelectMSB](https://developer.apple.com/documentation/coremidi/kmidipropertyreceivesbankselectmsb)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyReceivesBankSelectMSB: CFString! ``` |
| To | ``` let kMIDIPropertyReceivesBankSelectMSB: CFString ``` |

Modified [kMIDIPropertyReceivesClock](https://developer.apple.com/documentation/coremidi/kmidipropertyreceivesclock)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyReceivesClock: CFString! ``` |
| To | ``` let kMIDIPropertyReceivesClock: CFString ``` |

Modified [kMIDIPropertyReceivesMTC](https://developer.apple.com/documentation/coremidi/kmidipropertyreceivesmtc)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyReceivesMTC: CFString! ``` |
| To | ``` let kMIDIPropertyReceivesMTC: CFString ``` |

Modified [kMIDIPropertyReceivesNotes](https://developer.apple.com/documentation/coremidi/kmidipropertyreceivesnotes)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyReceivesNotes: CFString! ``` |
| To | ``` let kMIDIPropertyReceivesNotes: CFString ``` |

Modified [kMIDIPropertyReceivesProgramChanges](https://developer.apple.com/documentation/coremidi/kmidipropertyreceivesprogramchanges)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyReceivesProgramChanges: CFString! ``` |
| To | ``` let kMIDIPropertyReceivesProgramChanges: CFString ``` |

Modified [kMIDIPropertySingleRealtimeEntity](https://developer.apple.com/documentation/coremidi/kmidipropertysinglerealtimeentity)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertySingleRealtimeEntity: CFString! ``` |
| To | ``` let kMIDIPropertySingleRealtimeEntity: CFString ``` |

Modified [kMIDIPropertySupportsGeneralMIDI](https://developer.apple.com/documentation/coremidi/kmidipropertysupportsgeneralmidi)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertySupportsGeneralMIDI: CFString! ``` |
| To | ``` let kMIDIPropertySupportsGeneralMIDI: CFString ``` |

Modified [kMIDIPropertySupportsMMC](https://developer.apple.com/documentation/coremidi/kmidipropertysupportsmmc)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertySupportsMMC: CFString! ``` |
| To | ``` let kMIDIPropertySupportsMMC: CFString ``` |

Modified [kMIDIPropertySupportsShowControl](https://developer.apple.com/documentation/coremidi/kmidipropertysupportsshowcontrol)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertySupportsShowControl: CFString! ``` |
| To | ``` let kMIDIPropertySupportsShowControl: CFString ``` |

Modified [kMIDIPropertyTransmitChannels](https://developer.apple.com/documentation/coremidi/kmidipropertytransmitchannels)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyTransmitChannels: CFString! ``` |
| To | ``` let kMIDIPropertyTransmitChannels: CFString ``` |

Modified [kMIDIPropertyTransmitsBankSelectLSB](https://developer.apple.com/documentation/coremidi/kmidipropertytransmitsbankselectlsb)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyTransmitsBankSelectLSB: CFString! ``` |
| To | ``` let kMIDIPropertyTransmitsBankSelectLSB: CFString ``` |

Modified [kMIDIPropertyTransmitsBankSelectMSB](https://developer.apple.com/documentation/coremidi/kmidipropertytransmitsbankselectmsb)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyTransmitsBankSelectMSB: CFString! ``` |
| To | ``` let kMIDIPropertyTransmitsBankSelectMSB: CFString ``` |

Modified [kMIDIPropertyTransmitsClock](https://developer.apple.com/documentation/coremidi/kmidipropertytransmitsclock)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyTransmitsClock: CFString! ``` |
| To | ``` let kMIDIPropertyTransmitsClock: CFString ``` |

Modified [kMIDIPropertyTransmitsMTC](https://developer.apple.com/documentation/coremidi/kmidipropertytransmitsmtc)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyTransmitsMTC: CFString! ``` |
| To | ``` let kMIDIPropertyTransmitsMTC: CFString ``` |

Modified [kMIDIPropertyTransmitsNotes](https://developer.apple.com/documentation/coremidi/kmidipropertytransmitsnotes)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyTransmitsNotes: CFString! ``` |
| To | ``` let kMIDIPropertyTransmitsNotes: CFString ``` |

Modified [kMIDIPropertyTransmitsProgramChanges](https://developer.apple.com/documentation/coremidi/kmidipropertytransmitsprogramchanges)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyTransmitsProgramChanges: CFString! ``` |
| To | ``` let kMIDIPropertyTransmitsProgramChanges: CFString ``` |

Modified [kMIDIPropertyUniqueID](https://developer.apple.com/documentation/coremidi/kmidipropertyuniqueid)

|  | Declaration |
| --- | --- |
| From | ``` let kMIDIPropertyUniqueID: CFString! ``` |
| To | ``` let kMIDIPropertyUniqueID: CFString ``` |

Modified [kMIDIServerStartErr](https://developer.apple.com/documentation/coremidi/kmidiserverstarterr)

|  | Declaration |
| --- | --- |
| From | ``` var kMIDIServerStartErr: Int { get } ``` |
| To | ``` var kMIDIServerStartErr: OSStatus { get } ``` |

Modified [kMIDISetupFormatErr](https://developer.apple.com/documentation/coremidi/kmidisetupformaterr)

|  | Declaration |
| --- | --- |
| From | ``` var kMIDISetupFormatErr: Int { get } ``` |
| To | ``` var kMIDISetupFormatErr: OSStatus { get } ``` |

Modified [kMIDIUnknownEndpoint](https://developer.apple.com/documentation/coremidi/kmidiunknownendpoint)

|  | Declaration |
| --- | --- |
| From | ``` var kMIDIUnknownEndpoint: Int { get } ``` |
| To | ``` var kMIDIUnknownEndpoint: OSStatus { get } ``` |

Modified [kMIDIUnknownProperty](https://developer.apple.com/documentation/coremidi/1495156-error_constants/kmidiunknownproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kMIDIUnknownProperty: Int { get } ``` |
| To | ``` var kMIDIUnknownProperty: OSStatus { get } ``` |

Modified [kMIDIWrongEndpointType](https://developer.apple.com/documentation/coremidi/kmidiwrongendpointtype)

|  | Declaration |
| --- | --- |
| From | ``` var kMIDIWrongEndpointType: Int { get } ``` |
| To | ``` var kMIDIWrongEndpointType: OSStatus { get } ``` |

Modified [kMIDIWrongPropertyType](https://developer.apple.com/documentation/coremidi/1495156-error_constants/kmidiwrongpropertytype)

|  | Declaration |
| --- | --- |
| From | ``` var kMIDIWrongPropertyType: Int { get } ``` |
| To | ``` var kMIDIWrongPropertyType: OSStatus { get } ``` |

Modified [kMIDIWrongThread](https://developer.apple.com/documentation/coremidi/1495156-error_constants/kmidiwrongthread)

|  | Declaration |
| --- | --- |
| From | ``` var kMIDIWrongThread: Int { get } ``` |
| To | ``` var kMIDIWrongThread: OSStatus { get } ``` |

Modified [MIDIClientCreate(_: CFString, _: MIDINotifyProc?, _: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<MIDIClientRef>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495360-midiclientcreate)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIClientCreate(_ name: CFString!, _ notifyProc: MIDINotifyProc, _ notifyRefCon: UnsafeMutablePointer<Void>, _ outClient: UnsafeMutablePointer<MIDIClientRef>) -> OSStatus ``` |
| To | ``` func MIDIClientCreate(_ name: CFString, _ notifyProc: MIDINotifyProc?, _ notifyRefCon: UnsafeMutablePointer<Void>, _ outClient: UnsafeMutablePointer<MIDIClientRef>) -> OSStatus ``` |

Modified [MIDIClientRef](https://developer.apple.com/documentation/coremidi/midiclientref)

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIClientRef = COpaquePointer ``` |
| To | ``` typealias MIDIClientRef = MIDIObjectRef ``` |

Modified [MIDICompletionProc](https://developer.apple.com/documentation/coremidi/midicompletionproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDICompletionProc = CFunctionPointer<((UnsafeMutablePointer<MIDISysexSendRequest>) -> Void)> ``` |
| To | ``` typealias MIDICompletionProc = (UnsafeMutablePointer<MIDISysexSendRequest>) -> Void ``` |

Modified [MIDIDestinationCreate(_: MIDIClientRef, _: CFString, _: MIDIReadProc, _: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495347-mididestinationcreate)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIDestinationCreate(_ client: MIDIClientRef, _ name: CFString!, _ readProc: MIDIReadProc, _ refCon: UnsafeMutablePointer<Void>, _ outDest: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus ``` |
| To | ``` func MIDIDestinationCreate(_ client: MIDIClientRef, _ name: CFString, _ readProc: MIDIReadProc, _ refCon: UnsafeMutablePointer<Void>, _ outDest: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus ``` |

Modified [MIDIDeviceAddEntity(_: MIDIDeviceRef, _: CFString, _: Bool, _: Int, _: Int, _: UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1508206-midideviceaddentity)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIDeviceAddEntity(_ device: MIDIDeviceRef, _ name: CFString!, _ embedded: Boolean, _ numSourceEndpoints: Int, _ numDestinationEndpoints: Int, _ newEntity: UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus ``` |
| To | ``` func MIDIDeviceAddEntity(_ device: MIDIDeviceRef, _ name: CFString, _ embedded: Bool, _ numSourceEndpoints: Int, _ numDestinationEndpoints: Int, _ newEntity: UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus ``` |

Modified [MIDIDeviceListRef](https://developer.apple.com/documentation/coremidi/mididevicelistref)

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIDeviceListRef = COpaquePointer ``` |
| To | ``` typealias MIDIDeviceListRef = MIDIObjectRef ``` |

Modified [MIDIDeviceRef](https://developer.apple.com/documentation/coremidi/midideviceref)

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIDeviceRef = COpaquePointer ``` |
| To | ``` typealias MIDIDeviceRef = MIDIObjectRef ``` |

Modified [MIDIEndpointRef](https://developer.apple.com/documentation/audiotoolbox/midiendpointref)

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIEndpointRef = COpaquePointer ``` |
| To | ``` typealias MIDIEndpointRef = MIDIObjectRef ``` |

Modified [MIDIEntityRef](https://developer.apple.com/documentation/coremidi/midientityref)

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIEntityRef = COpaquePointer ``` |
| To | ``` typealias MIDIEntityRef = MIDIObjectRef ``` |

Modified [MIDIExternalDeviceCreate(_: CFString, _: CFString, _: CFString, _: UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1508456-midiexternaldevicecreate)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIExternalDeviceCreate(_ name: CFString!, _ manufacturer: CFString!, _ model: CFString!, _ outDevice: UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus ``` |
| To | ``` func MIDIExternalDeviceCreate(_ name: CFString, _ manufacturer: CFString, _ model: CFString, _ outDevice: UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus ``` |

Modified [MIDIInputPortCreate(_: MIDIClientRef, _: CFString, _: MIDIReadProc, _: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<MIDIPortRef>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495225-midiinputportcreate)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIInputPortCreate(_ client: MIDIClientRef, _ portName: CFString!, _ readProc: MIDIReadProc, _ refCon: UnsafeMutablePointer<Void>, _ outPort: UnsafeMutablePointer<MIDIPortRef>) -> OSStatus ``` |
| To | ``` func MIDIInputPortCreate(_ client: MIDIClientRef, _ portName: CFString, _ readProc: MIDIReadProc, _ refCon: UnsafeMutablePointer<Void>, _ outPort: UnsafeMutablePointer<MIDIPortRef>) -> OSStatus ``` |

Modified [MIDINotifyProc](https://developer.apple.com/documentation/coremidi/midinotifyproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDINotifyProc = CFunctionPointer<((UnsafePointer<MIDINotification>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias MIDINotifyProc = (UnsafePointer<MIDINotification>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [MIDIObjectGetDataProperty(_: MIDIObjectRef, _: CFString, _: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495213-midiobjectgetdataproperty)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIObjectGetDataProperty(_ obj: MIDIObjectRef, _ propertyID: CFString!, _ outData: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func MIDIObjectGetDataProperty(_ obj: MIDIObjectRef, _ propertyID: CFString, _ outData: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |

Modified [MIDIObjectGetDictionaryProperty(_: MIDIObjectRef, _: CFString, _: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495154-midiobjectgetdictionaryproperty)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIObjectGetDictionaryProperty(_ obj: MIDIObjectRef, _ propertyID: CFString!, _ outDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` |
| To | ``` func MIDIObjectGetDictionaryProperty(_ obj: MIDIObjectRef, _ propertyID: CFString, _ outDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` |

Modified [MIDIObjectGetIntegerProperty(_: MIDIObjectRef, _: CFString, _: UnsafeMutablePointer<Int32>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495364-midiobjectgetintegerproperty)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIObjectGetIntegerProperty(_ obj: MIDIObjectRef, _ propertyID: CFString!, _ outValue: UnsafeMutablePointer<Int32>) -> OSStatus ``` |
| To | ``` func MIDIObjectGetIntegerProperty(_ obj: MIDIObjectRef, _ propertyID: CFString, _ outValue: UnsafeMutablePointer<Int32>) -> OSStatus ``` |

Modified [MIDIObjectGetProperties(_: MIDIObjectRef, _: UnsafeMutablePointer<Unmanaged<CFPropertyList>?>, _: Bool) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495206-midiobjectgetproperties)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIObjectGetProperties(_ obj: MIDIObjectRef, _ outProperties: UnsafeMutablePointer<Unmanaged<CFPropertyList>?>, _ deep: Boolean) -> OSStatus ``` |
| To | ``` func MIDIObjectGetProperties(_ obj: MIDIObjectRef, _ outProperties: UnsafeMutablePointer<Unmanaged<CFPropertyList>?>, _ deep: Bool) -> OSStatus ``` |

Modified [MIDIObjectGetStringProperty(_: MIDIObjectRef, _: CFString, _: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495282-midiobjectgetstringproperty)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIObjectGetStringProperty(_ obj: MIDIObjectRef, _ propertyID: CFString!, _ str: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func MIDIObjectGetStringProperty(_ obj: MIDIObjectRef, _ propertyID: CFString, _ str: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |

Modified [MIDIObjectRef](https://developer.apple.com/documentation/coremidi/midiobjectref)

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIObjectRef = UnsafeMutablePointer<Void> ``` |
| To | ``` typealias MIDIObjectRef = UInt32 ``` |

Modified [MIDIObjectRemoveProperty(_: MIDIObjectRef, _: CFString) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495126-midiobjectremoveproperty)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIObjectRemoveProperty(_ obj: MIDIObjectRef, _ propertyID: CFString!) -> OSStatus ``` |
| To | ``` func MIDIObjectRemoveProperty(_ obj: MIDIObjectRef, _ propertyID: CFString) -> OSStatus ``` |

Modified [MIDIObjectSetDataProperty(_: MIDIObjectRef, _: CFString, _: CFData) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495169-midiobjectsetdataproperty)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIObjectSetDataProperty(_ obj: MIDIObjectRef, _ propertyID: CFString!, _ data: CFData!) -> OSStatus ``` |
| To | ``` func MIDIObjectSetDataProperty(_ obj: MIDIObjectRef, _ propertyID: CFString, _ data: CFData) -> OSStatus ``` |

Modified [MIDIObjectSetDictionaryProperty(_: MIDIObjectRef, _: CFString, _: CFDictionary) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495160-midiobjectsetdictionaryproperty)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIObjectSetDictionaryProperty(_ obj: MIDIObjectRef, _ propertyID: CFString!, _ data: CFDictionary!) -> OSStatus ``` |
| To | ``` func MIDIObjectSetDictionaryProperty(_ obj: MIDIObjectRef, _ propertyID: CFString, _ dict: CFDictionary) -> OSStatus ``` |

Modified [MIDIObjectSetIntegerProperty(_: MIDIObjectRef, _: CFString, _: Int32) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495378-midiobjectsetintegerproperty)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIObjectSetIntegerProperty(_ obj: MIDIObjectRef, _ propertyID: CFString!, _ value: Int32) -> OSStatus ``` |
| To | ``` func MIDIObjectSetIntegerProperty(_ obj: MIDIObjectRef, _ propertyID: CFString, _ value: Int32) -> OSStatus ``` |

Modified [MIDIObjectSetStringProperty(_: MIDIObjectRef, _: CFString, _: CFString) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495173-midiobjectsetstringproperty)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIObjectSetStringProperty(_ obj: MIDIObjectRef, _ propertyID: CFString!, _ str: CFString!) -> OSStatus ``` |
| To | ``` func MIDIObjectSetStringProperty(_ obj: MIDIObjectRef, _ propertyID: CFString, _ str: CFString) -> OSStatus ``` |

Modified [MIDIOutputPortCreate(_: MIDIClientRef, _: CFString, _: UnsafeMutablePointer<MIDIPortRef>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495166-midioutputportcreate)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIOutputPortCreate(_ client: MIDIClientRef, _ portName: CFString!, _ outPort: UnsafeMutablePointer<MIDIPortRef>) -> OSStatus ``` |
| To | ``` func MIDIOutputPortCreate(_ client: MIDIClientRef, _ portName: CFString, _ outPort: UnsafeMutablePointer<MIDIPortRef>) -> OSStatus ``` |

Modified [MIDIPortRef](https://developer.apple.com/documentation/coremidi/midiportref)

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIPortRef = COpaquePointer ``` |
| To | ``` typealias MIDIPortRef = MIDIObjectRef ``` |

Modified [MIDIReadProc](https://developer.apple.com/documentation/coremidi/midireadproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIReadProc = CFunctionPointer<((UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias MIDIReadProc = (UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [MIDISetupRef](https://developer.apple.com/documentation/coremidi/midisetupref)

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDISetupRef = COpaquePointer ``` |
| To | ``` typealias MIDISetupRef = MIDIObjectRef ``` |

Modified [MIDISourceCreate(_: MIDIClientRef, _: CFString, _: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495212-midisourcecreate)

|  | Declaration |
| --- | --- |
| From | ``` func MIDISourceCreate(_ client: MIDIClientRef, _ name: CFString!, _ outSrc: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus ``` |
| To | ``` func MIDISourceCreate(_ client: MIDIClientRef, _ name: CFString, _ outSrc: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus ``` |

Modified [MIDIThruConnectionCreate(_: CFString?, _: CFData, _: UnsafeMutablePointer<MIDIThruConnectionRef>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1508523-midithruconnectioncreate)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIThruConnectionCreate(_ inPersistentOwnerID: CFString!, _ inConnectionParams: CFData!, _ outConnection: UnsafeMutablePointer<MIDIThruConnectionRef>) -> OSStatus ``` |
| To | ``` func MIDIThruConnectionCreate(_ inPersistentOwnerID: CFString?, _ inConnectionParams: CFData, _ outConnection: UnsafeMutablePointer<MIDIThruConnectionRef>) -> OSStatus ``` |

Modified [MIDIThruConnectionFind(_: CFString, _: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1508377-midithruconnectionfind)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIThruConnectionFind(_ inPersistentOwnerID: CFString!, _ outConnectionList: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func MIDIThruConnectionFind(_ inPersistentOwnerID: CFString, _ outConnectionList: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |

Modified [MIDIThruConnectionRef](https://developer.apple.com/documentation/coremidi/midithruconnectionref)

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIThruConnectionRef = COpaquePointer ``` |
| To | ``` typealias MIDIThruConnectionRef = MIDIObjectRef ``` |

Modified [MIDIThruConnectionSetParams(_: MIDIThruConnectionRef, _: CFData) -> OSStatus](https://developer.apple.com/documentation/coremidi/1508352-midithruconnectionsetparams)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIThruConnectionSetParams(_ connection: MIDIThruConnectionRef, _ inConnectionParams: CFData!) -> OSStatus ``` |
| To | ``` func MIDIThruConnectionSetParams(_ connection: MIDIThruConnectionRef, _ inConnectionParams: CFData) -> OSStatus ``` |

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
