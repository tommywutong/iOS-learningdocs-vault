---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/CoreMIDI.html
archived_at: '2026-07-18T02:56:09.722977Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# CoreMIDI Changes

## CoreMIDI

Modified MIDINetworkConnection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDINetworkHost

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDINetworkSession

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIClientCreate(CFString!, MIDINotifyProc, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Unmanaged<MIDIClient>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIClientDispose(MIDIClient!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIDestinationCreate(MIDIClient!, CFString!, MIDIReadProc, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Unmanaged<MIDIEndpoint>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIDeviceAddEntity(MIDIDevice!, CFString!, Boolean, ItemCount, ItemCount, UnsafeMutablePointer<Unmanaged<MIDIEntity>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIDeviceCreate(MIDIDriverRef, CFString!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<MIDIDevice>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIDeviceDispose(MIDIDevice!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIDeviceGetEntity(MIDIDevice!, ItemCount) -> Unmanaged<MIDIEntity>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIDeviceGetNumberOfEntities(MIDIDevice!) -> ItemCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIDeviceListAddDevice(MIDIDeviceList!, MIDIDevice!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIDeviceListDispose(MIDIDeviceList!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIDeviceListGetDevice(MIDIDeviceList!, ItemCount) -> Unmanaged<MIDIDevice>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIDeviceListGetNumberOfDevices(MIDIDeviceList!) -> ItemCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIDeviceRemoveEntity(MIDIDevice!, MIDIEntity!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIEndpointDispose(MIDIEndpoint!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIEndpointGetEntity(MIDIEndpoint!, UnsafeMutablePointer<Unmanaged<MIDIEntity>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIEndpointGetRefCons(MIDIEndpoint!, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIEndpointSetRefCons(MIDIEndpoint!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIEntityAddOrRemoveEndpoints(MIDIEntity!, ItemCount, ItemCount) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIEntityGetDestination(MIDIEntity!, ItemCount) -> Unmanaged<MIDIEndpoint>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIEntityGetDevice(MIDIEntity!, UnsafeMutablePointer<Unmanaged<MIDIDevice>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIEntityGetNumberOfDestinations(MIDIEntity!) -> ItemCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIEntityGetNumberOfSources(MIDIEntity!) -> ItemCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIEntityGetSource(MIDIEntity!, ItemCount) -> Unmanaged<MIDIEndpoint>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIExternalDeviceCreate(CFString!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<MIDIDevice>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIFlushOutput(MIDIEndpoint!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIGetDestination(ItemCount) -> Unmanaged<MIDIEndpoint>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIGetDevice(ItemCount) -> Unmanaged<MIDIDevice>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIGetDriverDeviceList(MIDIDriverRef) -> Unmanaged<MIDIDeviceList>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIGetDriverIORunLoop() -> Unmanaged<CFRunLoop>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIGetExternalDevice(ItemCount) -> Unmanaged<MIDIDevice>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIGetNumberOfDestinations() -> ItemCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIGetNumberOfDevices() -> ItemCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIGetNumberOfExternalDevices() -> ItemCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIGetNumberOfSources() -> ItemCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIGetSource(ItemCount) -> Unmanaged<MIDIEndpoint>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIInputPortCreate(MIDIClient!, CFString!, MIDIReadProc, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Unmanaged<MIDIPort>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDINetworkBonjourServiceType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDINetworkNotificationContactsDidChange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDINetworkNotificationSessionDidChange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIObjectFindByUniqueID(MIDIUniqueID, UnsafeMutablePointer<MIDIObjectRef>, UnsafeMutablePointer<MIDIObjectType>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIObjectGetDataProperty(MIDIObjectRef, CFString!, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIObjectGetDictionaryProperty(MIDIObjectRef, CFString!, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIObjectGetIntegerProperty(MIDIObjectRef, CFString!, UnsafeMutablePointer<Int32>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIObjectGetProperties(MIDIObjectRef, UnsafeMutablePointer<Unmanaged<CFPropertyList>?>, Boolean) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIObjectGetStringProperty(MIDIObjectRef, CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIObjectRemoveProperty(MIDIObjectRef, CFString!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIObjectSetDataProperty(MIDIObjectRef, CFString!, CFData!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIObjectSetDictionaryProperty(MIDIObjectRef, CFString!, CFDictionary!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIObjectSetIntegerProperty(MIDIObjectRef, CFString!, Int32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIObjectSetStringProperty(MIDIObjectRef, CFString!, CFString!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIOutputPortCreate(MIDIClient!, CFString!, UnsafeMutablePointer<Unmanaged<MIDIPort>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIPacketListAdd(UnsafeMutablePointer<MIDIPacketList>, ByteCount, UnsafeMutablePointer<MIDIPacket>, MIDITimeStamp, ByteCount, UnsafePointer<Byte>) -> UnsafeMutablePointer<MIDIPacket>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIPacketListInit(UnsafeMutablePointer<MIDIPacketList>) -> UnsafeMutablePointer<MIDIPacket>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIPortConnectSource(MIDIPort!, MIDIEndpoint!, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIPortDisconnectSource(MIDIPort!, MIDIEndpoint!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIPortDispose(MIDIPort!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIReceived(MIDIEndpoint!, UnsafePointer<MIDIPacketList>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIRestart() -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDISend(MIDIPort!, MIDIEndpoint!, UnsafePointer<MIDIPacketList>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDISendSysex(UnsafeMutablePointer<MIDISysexSendRequest>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDISetupAddDevice(MIDIDevice!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDISetupAddExternalDevice(MIDIDevice!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDISetupRemoveDevice(MIDIDevice!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDISetupRemoveExternalDevice(MIDIDevice!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDISourceCreate(MIDIClient!, CFString!, UnsafeMutablePointer<Unmanaged<MIDIEndpoint>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIThruConnectionCreate(CFString!, CFData!, UnsafeMutablePointer<Unmanaged<MIDIThruConnection>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIThruConnectionDispose(MIDIThruConnection!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIThruConnectionFind(CFString!, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIThruConnectionGetParams(MIDIThruConnection!, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIThruConnectionParamsInitialize(UnsafeMutablePointer<MIDIThruConnectionParams>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MIDIThruConnectionSetParams(MIDIThruConnection!, CFData!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyAdvanceScheduleTimeMuSec

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyCanRoute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyConnectionUniqueID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyDeviceID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyDisplayName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyDriverDeviceEditorApp

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyDriverOwner

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyDriverVersion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyIsBroadcast

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyIsDrumMachine

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyIsEffectUnit

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyIsEmbeddedEntity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyIsMixer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyIsSampler

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyManufacturer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyMaxReceiveChannels

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyMaxSysExSpeed

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyMaxTransmitChannels

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyModel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyNameConfiguration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyOffline

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyPanDisruptsStereo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyPrivate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyReceiveChannels

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyReceivesBankSelectLSB

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyReceivesBankSelectMSB

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyReceivesClock

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyReceivesMTC

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyReceivesNotes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyReceivesProgramChanges

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertySingleRealtimeEntity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertySupportsGeneralMIDI

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertySupportsMMC

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertySupportsShowControl

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyTransmitChannels

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyTransmitsBankSelectLSB

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyTransmitsBankSelectMSB

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyTransmitsClock

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyTransmitsMTC

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyTransmitsNotes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyTransmitsProgramChanges

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kMIDIPropertyUniqueID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

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
