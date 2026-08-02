---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/CoreMIDI.html
archived_at: '2026-07-18T02:52:59.873098Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreMIDI Changes for Objective-C

### CoreMIDI

#### MIDIServices.h

Removed [kMIDIObjectType_ExternalMask](https://developer.apple.com/documentation/coremidi/midiobjecttype/kmidiobjecttype_externalmask)Removed #def MIDIPacketNextAdded [kMIDIObjectType_ExternalMask](https://developer.apple.com/documentation/coremidi/kmidiobjecttype_externalmask)Added [MIDIClientCreateWithBlock()](https://developer.apple.com/documentation/coremidi/1495330-midiclientcreatewithblock)Added [MIDIDestinationCreateWithBlock()](https://developer.apple.com/documentation/coremidi/1495247-mididestinationcreatewithblock)Added [MIDIInputPortCreateWithBlock()](https://developer.apple.com/documentation/coremidi/1495333-midiinputportcreatewithblock)Added [MIDINotifyBlock](https://developer.apple.com/documentation/coremidi/midinotifyblock)Added [MIDIPacketNext()](https://developer.apple.com/documentation/coremidi/1495178-midipacketnext)Added [MIDIReadBlock](https://developer.apple.com/documentation/coremidi/midireadblock)Modified [MIDIClientCreate()](https://developer.apple.com/documentation/coremidi/1495360-midiclientcreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIClientCreate (     CFStringRef name,     MIDINotifyProc notifyProc,     void *notifyRefCon,     MIDIClientRef *outClient ); ``` |
| To | ``` OSStatus MIDIClientCreate (     CFStringRef _Nonnull name,     MIDINotifyProc _Nullable notifyProc,     void * _Nullable notifyRefCon,     MIDIClientRef * _Nonnull outClient ); ``` |

Modified [MIDIDestinationCreate()](https://developer.apple.com/documentation/coremidi/1495347-mididestinationcreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIDestinationCreate (     MIDIClientRef client,     CFStringRef name,     MIDIReadProc readProc,     void *refCon,     MIDIEndpointRef *outDest ); ``` |
| To | ``` OSStatus MIDIDestinationCreate (     MIDIClientRef client,     CFStringRef _Nonnull name,     MIDIReadProc _Nonnull readProc,     void * _Nullable refCon,     MIDIEndpointRef * _Nonnull outDest ); ``` |

Modified [MIDIEndpointGetEntity()](https://developer.apple.com/documentation/coremidi/1495196-midiendpointgetentity)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIEndpointGetEntity (     MIDIEndpointRef inEndpoint,     MIDIEntityRef *outEntity ); ``` |
| To | ``` OSStatus MIDIEndpointGetEntity (     MIDIEndpointRef inEndpoint,     MIDIEntityRef * _Nullable outEntity ); ``` |

Modified [MIDIEntityGetDevice()](https://developer.apple.com/documentation/coremidi/1495210-midientitygetdevice)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIEntityGetDevice (     MIDIEntityRef inEntity,     MIDIDeviceRef *outDevice ); ``` |
| To | ``` OSStatus MIDIEntityGetDevice (     MIDIEntityRef inEntity,     MIDIDeviceRef * _Nullable outDevice ); ``` |

Modified [MIDIInputPortCreate()](https://developer.apple.com/documentation/coremidi/1495225-midiinputportcreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIInputPortCreate (     MIDIClientRef client,     CFStringRef portName,     MIDIReadProc readProc,     void *refCon,     MIDIPortRef *outPort ); ``` |
| To | ``` OSStatus MIDIInputPortCreate (     MIDIClientRef client,     CFStringRef _Nonnull portName,     MIDIReadProc _Nonnull readProc,     void * _Nullable refCon,     MIDIPortRef * _Nonnull outPort ); ``` |

Modified [MIDIObjectFindByUniqueID()](https://developer.apple.com/documentation/coremidi/1495191-midiobjectfindbyuniqueid)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIObjectFindByUniqueID (     MIDIUniqueID inUniqueID,     MIDIObjectRef *outObject,     MIDIObjectType *outObjectType ); ``` |
| To | ``` OSStatus MIDIObjectFindByUniqueID (     MIDIUniqueID inUniqueID,     MIDIObjectRef * _Nonnull outObject,     MIDIObjectType * _Nonnull outObjectType ); ``` |

Modified [MIDIObjectGetDataProperty()](https://developer.apple.com/documentation/coremidi/1495213-midiobjectgetdataproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIObjectGetDataProperty (     MIDIObjectRef obj,     CFStringRef propertyID,     CFDataRef *outData ); ``` |
| To | ``` OSStatus MIDIObjectGetDataProperty (     MIDIObjectRef obj,     CFStringRef _Nonnull propertyID,     CFDataRef  _Nullable * _Nonnull outData ); ``` |

Modified [MIDIObjectGetDictionaryProperty()](https://developer.apple.com/documentation/coremidi/1495154-midiobjectgetdictionaryproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIObjectGetDictionaryProperty (     MIDIObjectRef obj,     CFStringRef propertyID,     CFDictionaryRef *outDict ); ``` |
| To | ``` OSStatus MIDIObjectGetDictionaryProperty (     MIDIObjectRef obj,     CFStringRef _Nonnull propertyID,     CFDictionaryRef  _Nullable * _Nonnull outDict ); ``` |

Modified [MIDIObjectGetIntegerProperty()](https://developer.apple.com/documentation/coremidi/1495364-midiobjectgetintegerproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIObjectGetIntegerProperty (     MIDIObjectRef obj,     CFStringRef propertyID,     SInt32 *outValue ); ``` |
| To | ``` OSStatus MIDIObjectGetIntegerProperty (     MIDIObjectRef obj,     CFStringRef _Nonnull propertyID,     SInt32 * _Nonnull outValue ); ``` |

Modified [MIDIObjectGetProperties()](https://developer.apple.com/documentation/coremidi/1495206-midiobjectgetproperties)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIObjectGetProperties (     MIDIObjectRef obj,     CFPropertyListRef *outProperties,     Boolean deep ); ``` |
| To | ``` OSStatus MIDIObjectGetProperties (     MIDIObjectRef obj,     CFPropertyListRef  _Nullable * _Nonnull outProperties,     Boolean deep ); ``` |

Modified [MIDIObjectGetStringProperty()](https://developer.apple.com/documentation/coremidi/1495282-midiobjectgetstringproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIObjectGetStringProperty (     MIDIObjectRef obj,     CFStringRef propertyID,     CFStringRef *str ); ``` |
| To | ``` OSStatus MIDIObjectGetStringProperty (     MIDIObjectRef obj,     CFStringRef _Nonnull propertyID,     CFStringRef  _Nullable * _Nonnull str ); ``` |

Modified [MIDIObjectRemoveProperty()](https://developer.apple.com/documentation/coremidi/1495126-midiobjectremoveproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIObjectRemoveProperty (     MIDIObjectRef obj,     CFStringRef propertyID ); ``` |
| To | ``` OSStatus MIDIObjectRemoveProperty (     MIDIObjectRef obj,     CFStringRef _Nonnull propertyID ); ``` |

Modified [MIDIObjectSetDataProperty()](https://developer.apple.com/documentation/coremidi/1495169-midiobjectsetdataproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIObjectSetDataProperty (     MIDIObjectRef obj,     CFStringRef propertyID,     CFDataRef data ); ``` |
| To | ``` OSStatus MIDIObjectSetDataProperty (     MIDIObjectRef obj,     CFStringRef _Nonnull propertyID,     CFDataRef _Nonnull data ); ``` |

Modified [MIDIObjectSetDictionaryProperty()](https://developer.apple.com/documentation/coremidi/1495160-midiobjectsetdictionaryproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIObjectSetDictionaryProperty (     MIDIObjectRef obj,     CFStringRef propertyID,     CFDictionaryRef data ); ``` |
| To | ``` OSStatus MIDIObjectSetDictionaryProperty (     MIDIObjectRef obj,     CFStringRef _Nonnull propertyID,     CFDictionaryRef _Nonnull dict ); ``` |

Modified [MIDIObjectSetIntegerProperty()](https://developer.apple.com/documentation/coremidi/1495378-midiobjectsetintegerproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIObjectSetIntegerProperty (     MIDIObjectRef obj,     CFStringRef propertyID,     SInt32 value ); ``` |
| To | ``` OSStatus MIDIObjectSetIntegerProperty (     MIDIObjectRef obj,     CFStringRef _Nonnull propertyID,     SInt32 value ); ``` |

Modified [MIDIObjectSetStringProperty()](https://developer.apple.com/documentation/coremidi/1495173-midiobjectsetstringproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIObjectSetStringProperty (     MIDIObjectRef obj,     CFStringRef propertyID,     CFStringRef str ); ``` |
| To | ``` OSStatus MIDIObjectSetStringProperty (     MIDIObjectRef obj,     CFStringRef _Nonnull propertyID,     CFStringRef _Nonnull str ); ``` |

Modified [MIDIOutputPortCreate()](https://developer.apple.com/documentation/coremidi/1495166-midioutputportcreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIOutputPortCreate (     MIDIClientRef client,     CFStringRef portName,     MIDIPortRef *outPort ); ``` |
| To | ``` OSStatus MIDIOutputPortCreate (     MIDIClientRef client,     CFStringRef _Nonnull portName,     MIDIPortRef * _Nonnull outPort ); ``` |

Modified [MIDIPacketListAdd()](https://developer.apple.com/documentation/coremidi/1495128-midipacketlistadd)

|  | Declaration |
| --- | --- |
| From | ``` MIDIPacket * MIDIPacketListAdd (     MIDIPacketList *pktlist,     ByteCount listSize,     MIDIPacket *curPacket,     MIDITimeStamp time,     ByteCount nData,     const Byte *data ); ``` |
| To | ``` MIDIPacket * _Nonnull MIDIPacketListAdd (     MIDIPacketList * _Nonnull pktlist,     ByteCount listSize,     MIDIPacket * _Nonnull curPacket,     MIDITimeStamp time,     ByteCount nData,     const Byte * _Nonnull data ); ``` |

Modified [MIDIPacketListInit()](https://developer.apple.com/documentation/coremidi/1495218-midipacketlistinit)

|  | Declaration |
| --- | --- |
| From | ``` MIDIPacket * MIDIPacketListInit (     MIDIPacketList *pktlist ); ``` |
| To | ``` MIDIPacket * _Nonnull MIDIPacketListInit (     MIDIPacketList * _Nonnull pktlist ); ``` |

Modified [MIDIPortConnectSource()](https://developer.apple.com/documentation/coremidi/1495278-midiportconnectsource)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIPortConnectSource (     MIDIPortRef port,     MIDIEndpointRef source,     void *connRefCon ); ``` |
| To | ``` OSStatus MIDIPortConnectSource (     MIDIPortRef port,     MIDIEndpointRef source,     void * _Nullable connRefCon ); ``` |

Modified [MIDIReceived()](https://developer.apple.com/documentation/coremidi/1495276-midireceived)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIReceived (     MIDIEndpointRef src,     const MIDIPacketList *pktlist ); ``` |
| To | ``` OSStatus MIDIReceived (     MIDIEndpointRef src,     const MIDIPacketList * _Nonnull pktlist ); ``` |

Modified [MIDISend()](https://developer.apple.com/documentation/coremidi/1495289-midisend)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDISend (     MIDIPortRef port,     MIDIEndpointRef dest,     const MIDIPacketList *pktlist ); ``` |
| To | ``` OSStatus MIDISend (     MIDIPortRef port,     MIDIEndpointRef dest,     const MIDIPacketList * _Nonnull pktlist ); ``` |

Modified [MIDISendSysex()](https://developer.apple.com/documentation/coremidi/1495356-midisendsysex)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDISendSysex (     MIDISysexSendRequest *request ); ``` |
| To | ``` OSStatus MIDISendSysex (     MIDISysexSendRequest * _Nonnull request ); ``` |

Modified [MIDISourceCreate()](https://developer.apple.com/documentation/coremidi/1495212-midisourcecreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDISourceCreate (     MIDIClientRef client,     CFStringRef name,     MIDIEndpointRef *outSrc ); ``` |
| To | ``` OSStatus MIDISourceCreate (     MIDIClientRef client,     CFStringRef _Nonnull name,     MIDIEndpointRef * _Nonnull outSrc ); ``` |

#### MIDISetup.h

Modified [MIDIDeviceAddEntity()](https://developer.apple.com/documentation/coremidi/1508206-midideviceaddentity)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIDeviceAddEntity (     MIDIDeviceRef device,     CFStringRef name,     Boolean embedded,     ItemCount numSourceEndpoints,     ItemCount numDestinationEndpoints,     MIDIEntityRef *newEntity ); ``` |
| To | ``` OSStatus MIDIDeviceAddEntity (     MIDIDeviceRef device,     CFStringRef _Nonnull name,     Boolean embedded,     ItemCount numSourceEndpoints,     ItemCount numDestinationEndpoints,     MIDIEntityRef * _Nonnull newEntity ); ``` |

Modified [MIDIExternalDeviceCreate()](https://developer.apple.com/documentation/coremidi/1508456-midiexternaldevicecreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIExternalDeviceCreate (     CFStringRef name,     CFStringRef manufacturer,     CFStringRef model,     MIDIDeviceRef *outDevice ); ``` |
| To | ``` OSStatus MIDIExternalDeviceCreate (     CFStringRef _Nonnull name,     CFStringRef _Nonnull manufacturer,     CFStringRef _Nonnull model,     MIDIDeviceRef * _Nonnull outDevice ); ``` |

Modified [MIDIGetSerialPortDrivers()](https://developer.apple.com/documentation/coremidi/1562903-midigetserialportdrivers)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIGetSerialPortDrivers (     CFArrayRef *outDriverNames ); ``` |
| To | ``` OSStatus MIDIGetSerialPortDrivers (     CFArrayRef  _Nullable * _Nonnull outDriverNames ); ``` |

Modified [MIDIGetSerialPortOwner()](https://developer.apple.com/documentation/coremidi/1562902-midigetserialportowner)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIGetSerialPortOwner (     CFStringRef portName,     CFStringRef *outDriverName ); ``` |
| To | ``` OSStatus MIDIGetSerialPortOwner (     CFStringRef _Nonnull portName,     CFStringRef  _Nullable * _Nonnull outDriverName ); ``` |

Modified [MIDISetSerialPortOwner()](https://developer.apple.com/documentation/coremidi/1562896-midisetserialportowner)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDISetSerialPortOwner (     CFStringRef portName,     CFStringRef driverName ); ``` |
| To | ``` OSStatus MIDISetSerialPortOwner (     CFStringRef _Nonnull portName,     CFStringRef _Nonnull driverName ); ``` |

Modified [MIDISetupCreate()](https://developer.apple.com/documentation/coremidi/1562901-midisetupcreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDISetupCreate (     MIDISetupRef *outSetup ); ``` |
| To | ``` OSStatus MIDISetupCreate (     MIDISetupRef * _Nonnull outSetup ); ``` |

Modified [MIDISetupFromData()](https://developer.apple.com/documentation/coremidi/1562898-midisetupfromdata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDISetupFromData (     CFDataRef data,     MIDISetupRef *outSetup ); ``` |
| To | ``` OSStatus MIDISetupFromData (     CFDataRef _Nonnull data,     MIDISetupRef * _Nonnull outSetup ); ``` |

Modified [MIDISetupGetCurrent()](https://developer.apple.com/documentation/coremidi/1562895-midisetupgetcurrent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDISetupGetCurrent (     MIDISetupRef *outSetup ); ``` |
| To | ``` OSStatus MIDISetupGetCurrent (     MIDISetupRef * _Nonnull outSetup ); ``` |

Modified [MIDISetupToData()](https://developer.apple.com/documentation/coremidi/1562897-midisetuptodata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDISetupToData (     MIDISetupRef setup,     CFDataRef *outData ); ``` |
| To | ``` OSStatus MIDISetupToData (     MIDISetupRef setup,     CFDataRef  _Nullable * _Nonnull outData ); ``` |

#### MIDIThruConnection.h

Removed [#def MIDIThruConnectionParamsSize](https://developer.apple.com/documentation/coremidi/midi_thru_connection/midithruconnectionparamssize)Added [MIDIThruConnectionParamsSize()](https://developer.apple.com/documentation/coremidi/1508275-midithruconnectionparamssize)Modified [MIDIThruConnectionCreate()](https://developer.apple.com/documentation/coremidi/1508523-midithruconnectioncreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIThruConnectionCreate (     CFStringRef inPersistentOwnerID,     CFDataRef inConnectionParams,     MIDIThruConnectionRef *outConnection ); ``` |
| To | ``` OSStatus MIDIThruConnectionCreate (     CFStringRef _Nullable inPersistentOwnerID,     CFDataRef _Nonnull inConnectionParams,     MIDIThruConnectionRef * _Nonnull outConnection ); ``` |

Modified [MIDIThruConnectionFind()](https://developer.apple.com/documentation/coremidi/1508377-midithruconnectionfind)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIThruConnectionFind (     CFStringRef inPersistentOwnerID,     CFDataRef *outConnectionList ); ``` |
| To | ``` OSStatus MIDIThruConnectionFind (     CFStringRef _Nonnull inPersistentOwnerID,     CFDataRef  _Nonnull * _Nonnull outConnectionList ); ``` |

Modified [MIDIThruConnectionGetParams()](https://developer.apple.com/documentation/coremidi/1508390-midithruconnectiongetparams)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIThruConnectionGetParams (     MIDIThruConnectionRef connection,     CFDataRef *outConnectionParams ); ``` |
| To | ``` OSStatus MIDIThruConnectionGetParams (     MIDIThruConnectionRef connection,     CFDataRef  _Nonnull * _Nonnull outConnectionParams ); ``` |

Modified [MIDIThruConnectionParamsInitialize()](https://developer.apple.com/documentation/coremidi/1508520-midithruconnectionparamsinitiali)

|  | Declaration |
| --- | --- |
| From | ``` void MIDIThruConnectionParamsInitialize (     MIDIThruConnectionParams *inConnectionParams ); ``` |
| To | ``` void MIDIThruConnectionParamsInitialize (     MIDIThruConnectionParams * _Nonnull inConnectionParams ); ``` |

Modified [MIDIThruConnectionSetParams()](https://developer.apple.com/documentation/coremidi/1508352-midithruconnectionsetparams)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIThruConnectionSetParams (     MIDIThruConnectionRef connection,     CFDataRef inConnectionParams ); ``` |
| To | ``` OSStatus MIDIThruConnectionSetParams (     MIDIThruConnectionRef connection,     CFDataRef _Nonnull inConnectionParams ); ``` |

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
