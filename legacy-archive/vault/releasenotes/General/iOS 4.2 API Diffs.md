---
title: iOS 4.2 API Diffs
apple_id: TP40010312
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2010-11-01'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS42APIDiffs/index.html
archived_at: '2026-07-18T02:55:46.478840Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)


# iOS 4.1 to iOS 4.2 API Differences

## Added frameworks:

- CoreMIDI

## Accelerate

No changes

## AddressBook

No changes

## AddressBookUI

No changes

## AssetsLibrary

No changes

## AudioToolbox

AudioFile.hAdded [kAudioFileNotOpenError](https://developer.apple.com/documentation/audiotoolbox/1576500-anonymous/kaudiofilenotopenerror)AudioFormat.hAdded [kAudioFormatProperty_ChannelLayoutSimpleName](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_channellayoutsimplename)

## AudioUnit

AudioUnitProperties.hAdded VoiceIOFarEndVersionInfoAdded kAUVoiceIOProperty_FarEndVersionInfoAdded kVoiceIOFarEndAUVersion_RequiresBackwardCompatibilityAdded kVoiceIOFarEndAUVersion_ThirdParty

## AVFoundation

AVAsset.hAdded [AVAsset.hasProtectedContent](https://developer.apple.com/documentation/avfoundation/avasset/1389223-hasprotectedcontent)Added AVAsset(AVAssetProtectedContent)AVMetadataItem.hAdded [AVMetadataItem.duration](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1386610-duration)Added [AVMutableMetadataItem.duration](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1389980-duration)Modified [AVMetadataItem](https://developer.apple.com/documentation/avfoundation/avmetadataitem)

|  | Protocols |
| --- | --- |
| From | NSCopying, NSMutableCopying |
| To | AVAsynchronousKeyValueLoading, NSCopying, NSMutableCopying |

## CFNetwork

No changes

## CoreAudio

No changes

## CoreData

No changes

## CoreFoundation

CFBase.hAdded [#def kCFCoreFoundationVersionNumber_iOS_4_0](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_4_0)CFString.hAdded [CFStringGetHyphenationLocationBeforeIndex()](https://developer.apple.com/documentation/corefoundation/1542693-cfstringgethyphenationlocationbe)

## CoreGraphics

No changes

## CoreLocation

CLLocation.hAdded [-[CLLocation initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:course:speed:timestamp:]](https://developer.apple.com/documentation/corelocation/cllocation/1423718-init)CLLocationManager.hAdded [+[CLLocationManager authorizationStatus]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423523-authorizationstatus)Added [CLAuthorizationStatus](https://developer.apple.com/documentation/corelocation/clauthorizationstatus)Added [kCLAuthorizationStatusAuthorized](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/kclauthorizationstatusauthorized)Added [kCLAuthorizationStatusDenied](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/kclauthorizationstatusdenied)Added [kCLAuthorizationStatusNotDetermined](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/kclauthorizationstatusnotdetermined)Added [kCLAuthorizationStatusRestricted](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/restricted)CLLocationManagerDelegate.hAdded [-[CLLocationManagerDelegate locationManager:didChangeAuthorizationStatus:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423701-locationmanager)

## CoreMedia

CMFormatDescription.hAdded [kCMClosedCaptionFormatType_ATSC](https://developer.apple.com/documentation/coremedia/kcmclosedcaptionformattype_atsc)Added [kCMMPEG2VideoProfile_XDCAM_HD422_720p24_CBR50](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_hd422_720p24_cbr50)Added [kCMMPEG2VideoProfile_XDCAM_HD422_720p25_CBR50](https://developer.apple.com/documentation/coremedia/1564241-video_profile_constants/kcmmpeg2videoprofile_xdcam_hd422_720p25_cbr50)Added [kCMMPEG2VideoProfile_XDCAM_HD422_720p30_CBR50](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_hd422_720p30_cbr50)CMSimpleQueue.hAdded #def CMSIMPLEQUEUE_HAdded [CMSimpleQueueCreate()](https://developer.apple.com/documentation/coremedia/1489641-cmsimplequeuecreate)Added [CMSimpleQueueDequeue()](https://developer.apple.com/documentation/coremedia/1489820-cmsimplequeuedequeue)Added [CMSimpleQueueEnqueue()](https://developer.apple.com/documentation/coremedia/1489315-cmsimplequeueenqueue)Added [CMSimpleQueueGetCapacity()](https://developer.apple.com/documentation/coremedia/1489168-cmsimplequeuegetcapacity)Added [CMSimpleQueueGetCount()](https://developer.apple.com/documentation/coremedia/1489223-cmsimplequeuegetcount)Added [#def CMSimpleQueueGetFullness](https://developer.apple.com/documentation/coremedia/cmsimplequeuegetfullness)Added [CMSimpleQueueGetHead()](https://developer.apple.com/documentation/coremedia/1489410-cmsimplequeuegethead)Added [CMSimpleQueueGetTypeID()](https://developer.apple.com/documentation/coremedia/1489165-cmsimplequeuegettypeid)Added [CMSimpleQueueRef](https://developer.apple.com/documentation/coremedia/cmsimplequeueref)Added [CMSimpleQueueReset()](https://developer.apple.com/documentation/coremedia/1489224-cmsimplequeuereset)Added [kCMSimpleQueueError_AllocationFailed](https://developer.apple.com/documentation/coremedia/1584369-simple_queue_error_codes/kcmsimplequeueerror_allocationfailed)Added [kCMSimpleQueueError_ParameterOutOfRange](https://developer.apple.com/documentation/coremedia/1584369-simple_queue_error_codes/kcmsimplequeueerror_parameteroutofrange)Added [kCMSimpleQueueError_QueueIsFull](https://developer.apple.com/documentation/coremedia/1584369-simple_queue_error_codes/kcmsimplequeueerror_queueisfull)Added [kCMSimpleQueueError_RequiredParameterMissing](https://developer.apple.com/documentation/coremedia/1584369-simple_queue_error_codes/kcmsimplequeueerror_requiredparametermissing)

## CoreMIDI

MIDIDriver.hAdded [MIDIDeviceCreate()](https://developer.apple.com/documentation/coremidi/1508421-mididevicecreate)Added [MIDIDeviceDispose()](https://developer.apple.com/documentation/coremidi/1508423-mididevicedispose)Added [MIDIDeviceListAddDevice()](https://developer.apple.com/documentation/coremidi/1508395-mididevicelistadddevice)Added [MIDIDeviceListDispose()](https://developer.apple.com/documentation/coremidi/1508497-mididevicelistdispose)Added [MIDIDeviceListGetDevice()](https://developer.apple.com/documentation/coremidi/1508251-mididevicelistgetdevice)Added [MIDIDeviceListGetNumberOfDevices()](https://developer.apple.com/documentation/coremidi/1508535-mididevicelistgetnumberofdevices)Added [MIDIDeviceListRef](https://developer.apple.com/documentation/coremidi/mididevicelistref)Added [MIDIDriverInterface](https://developer.apple.com/documentation/coremidi/mididriverinterface)Added [MIDIDriverRef](https://developer.apple.com/documentation/coremidi/mididriverref)Added [MIDIEndpointGetRefCons()](https://developer.apple.com/documentation/coremidi/1508417-midiendpointgetrefcons)Added [MIDIEndpointSetRefCons()](https://developer.apple.com/documentation/coremidi/1508268-midiendpointsetrefcons)Added [MIDIGetDriverDeviceList()](https://developer.apple.com/documentation/coremidi/1508306-midigetdriverdevicelist)Added [MIDIGetDriverIORunLoop()](https://developer.apple.com/documentation/coremidi/1508500-midigetdriveriorunloop)Added #def kMIDIDriverInterface2IDAdded #def kMIDIDriverInterfaceIDAdded #def kMIDIDriverTypeIDMIDINetworkSession.hAdded [MIDINetworkConnection](https://developer.apple.com/documentation/coremidi/midinetworkconnection)Added [+[MIDINetworkConnection connectionWithHost:]](https://developer.apple.com/documentation/coremidi/midinetworkconnection/1619340-init)Added [MIDINetworkConnection.host](https://developer.apple.com/documentation/coremidi/midinetworkconnection/1619334-host)Added [MIDINetworkHost](https://developer.apple.com/documentation/coremidi/midinetworkhost)Added [MIDINetworkHost.address](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619353-address)Added [-[MIDINetworkHost hasSameAddressAs:]](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619372-hassameaddressas)Added [+[MIDINetworkHost hostWithName:address:port:]](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619365-hostwithname)Added [+[MIDINetworkHost hostWithName:netService:]](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619371-hostwithname)Added [+[MIDINetworkHost hostWithName:netServiceName:netServiceDomain:]](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619338-init)Added [MIDINetworkHost.name](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619339-name)Added [MIDINetworkHost.netServiceDomain](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619344-netservicedomain)Added [MIDINetworkHost.netServiceName](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619362-netservicename)Added [MIDINetworkHost.port](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619333-port)Added [MIDINetworkSession](https://developer.apple.com/documentation/coremidi/midinetworksession)Added [-[MIDINetworkSession addConnection:]](https://developer.apple.com/documentation/coremidi/midinetworksession/1619369-addconnection)Added [-[MIDINetworkSession addContact:]](https://developer.apple.com/documentation/coremidi/midinetworksession/1619361-addcontact)Added [MIDINetworkSession.connectionPolicy](https://developer.apple.com/documentation/coremidi/midinetworksession/1619360-connectionpolicy)Added [-[MIDINetworkSession connections]](https://developer.apple.com/documentation/coremidi/midinetworksession/1619366-connections)Added [-[MIDINetworkSession contacts]](https://developer.apple.com/documentation/coremidi/midinetworksession/1619335-contacts)Added [+[MIDINetworkSession defaultSession]](https://developer.apple.com/documentation/coremidi/midinetworksession/1619363-default)Added [-[MIDINetworkSession destinationEndpoint]](https://developer.apple.com/documentation/coremidi/midinetworksession/1619367-destinationendpoint)Added [MIDINetworkSession.enabled](https://developer.apple.com/documentation/coremidi/midinetworksession/1619368-enabled)Added [MIDINetworkSession.localName](https://developer.apple.com/documentation/coremidi/midinetworksession/1619358-localname)Added [MIDINetworkSession.networkName](https://developer.apple.com/documentation/coremidi/midinetworksession/1619336-networkname)Added [MIDINetworkSession.networkPort](https://developer.apple.com/documentation/coremidi/midinetworksession/1619373-networkport)Added [-[MIDINetworkSession removeConnection:]](https://developer.apple.com/documentation/coremidi/midinetworksession/1619346-removeconnection)Added [-[MIDINetworkSession removeContact:]](https://developer.apple.com/documentation/coremidi/midinetworksession/1619332-removecontact)Added [-[MIDINetworkSession sourceEndpoint]](https://developer.apple.com/documentation/coremidi/midinetworksession/1619359-sourceendpoint)Added [MIDINetworkBonjourServiceType](https://developer.apple.com/documentation/coremidi/midinetworkbonjourservicetype)Added [MIDINetworkConnectionPolicy](https://developer.apple.com/documentation/coremidi/midinetworkconnectionpolicy)Added [MIDINetworkConnectionPolicy_Anyone](https://developer.apple.com/documentation/coremidi/midinetworkconnectionpolicy/midinetworkconnectionpolicy_anyone)Added [MIDINetworkConnectionPolicy_HostsInContactList](https://developer.apple.com/documentation/coremidi/midinetworkconnectionpolicy/midinetworkconnectionpolicy_hostsincontactlist)Added [MIDINetworkConnectionPolicy_NoOne](https://developer.apple.com/documentation/coremidi/midinetworkconnectionpolicy/midinetworkconnectionpolicy_noone)Added [MIDINetworkNotificationContactsDidChange](https://developer.apple.com/documentation/coremidi/midinetworknotificationcontactsdidchange)Added [MIDINetworkNotificationSessionDidChange](https://developer.apple.com/documentation/coremidi/midinetworknotificationsessiondidchange)Added #def MIDI_EXPORTMIDIServices.hAdded [MIDIClientCreate()](https://developer.apple.com/documentation/coremidi/1495360-midiclientcreate)Added [MIDIClientDispose()](https://developer.apple.com/documentation/coremidi/1495335-midiclientdispose)Added [MIDIClientRef](https://developer.apple.com/documentation/coremidi/midiclientref)Added [MIDICompletionProc](https://developer.apple.com/documentation/coremidi/midicompletionproc)Added [MIDIDestinationCreate()](https://developer.apple.com/documentation/coremidi/1495347-mididestinationcreate)Added [MIDIDeviceGetEntity()](https://developer.apple.com/documentation/coremidi/1495261-mididevicegetentity)Added [MIDIDeviceGetNumberOfEntities()](https://developer.apple.com/documentation/coremidi/1495354-mididevicegetnumberofentities)Added [MIDIDeviceRef](https://developer.apple.com/documentation/coremidi/midideviceref)Added [MIDIEndpointDispose()](https://developer.apple.com/documentation/coremidi/1495148-midiendpointdispose)Added [MIDIEndpointGetEntity()](https://developer.apple.com/documentation/coremidi/1495196-midiendpointgetentity)Added [MIDIEndpointRef](https://developer.apple.com/documentation/audiotoolbox/midiendpointref)Added [MIDIEntityGetDestination()](https://developer.apple.com/documentation/coremidi/1495223-midientitygetdestination)Added [MIDIEntityGetDevice()](https://developer.apple.com/documentation/coremidi/1495210-midientitygetdevice)Added [MIDIEntityGetNumberOfDestinations()](https://developer.apple.com/documentation/coremidi/1495188-midientitygetnumberofdestination)Added [MIDIEntityGetNumberOfSources()](https://developer.apple.com/documentation/coremidi/1495284-midientitygetnumberofsources)Added [MIDIEntityGetSource()](https://developer.apple.com/documentation/coremidi/1495236-midientitygetsource)Added [MIDIEntityRef](https://developer.apple.com/documentation/coremidi/midientityref)Added [MIDIFlushOutput()](https://developer.apple.com/documentation/coremidi/1495312-midiflushoutput)Added [MIDIGetDestination()](https://developer.apple.com/documentation/coremidi/1495108-midigetdestination)Added [MIDIGetDevice()](https://developer.apple.com/documentation/coremidi/1495368-midigetdevice)Added [MIDIGetExternalDevice()](https://developer.apple.com/documentation/coremidi/1495149-midigetexternaldevice)Added [MIDIGetNumberOfDestinations()](https://developer.apple.com/documentation/coremidi/1495309-midigetnumberofdestinations)Added [MIDIGetNumberOfDevices()](https://developer.apple.com/documentation/coremidi/1495164-midigetnumberofdevices)Added [MIDIGetNumberOfExternalDevices()](https://developer.apple.com/documentation/coremidi/1495171-midigetnumberofexternaldevices)Added [MIDIGetNumberOfSources()](https://developer.apple.com/documentation/coremidi/1495116-midigetnumberofsources)Added [MIDIGetSource()](https://developer.apple.com/documentation/coremidi/1495168-midigetsource)Added [MIDIIOErrorNotification](https://developer.apple.com/documentation/coremidi/midiioerrornotification)Added [MIDIInputPortCreate()](https://developer.apple.com/documentation/coremidi/1495225-midiinputportcreate)Added [MIDINotification](https://developer.apple.com/documentation/coremidi/midinotification)Added [MIDINotificationMessageID](https://developer.apple.com/documentation/coremidi/midinotificationmessageid)Added [MIDINotifyProc](https://developer.apple.com/documentation/coremidi/midinotifyproc)Added [MIDIObjectAddRemoveNotification](https://developer.apple.com/documentation/coremidi/midiobjectaddremovenotification)Added [MIDIObjectFindByUniqueID()](https://developer.apple.com/documentation/coremidi/1495191-midiobjectfindbyuniqueid)Added [MIDIObjectGetDataProperty()](https://developer.apple.com/documentation/coremidi/1495213-midiobjectgetdataproperty)Added [MIDIObjectGetDictionaryProperty()](https://developer.apple.com/documentation/coremidi/1495154-midiobjectgetdictionaryproperty)Added [MIDIObjectGetIntegerProperty()](https://developer.apple.com/documentation/coremidi/1495364-midiobjectgetintegerproperty)Added [MIDIObjectGetProperties()](https://developer.apple.com/documentation/coremidi/1495206-midiobjectgetproperties)Added [MIDIObjectGetStringProperty()](https://developer.apple.com/documentation/coremidi/1495282-midiobjectgetstringproperty)Added [MIDIObjectPropertyChangeNotification](https://developer.apple.com/documentation/coremidi/midiobjectpropertychangenotification)Added [MIDIObjectRef](https://developer.apple.com/documentation/coremidi/midiobjectref)Added [MIDIObjectRemoveProperty()](https://developer.apple.com/documentation/coremidi/1495126-midiobjectremoveproperty)Added [MIDIObjectSetDataProperty()](https://developer.apple.com/documentation/coremidi/1495169-midiobjectsetdataproperty)Added [MIDIObjectSetDictionaryProperty()](https://developer.apple.com/documentation/coremidi/1495160-midiobjectsetdictionaryproperty)Added [MIDIObjectSetIntegerProperty()](https://developer.apple.com/documentation/coremidi/1495378-midiobjectsetintegerproperty)Added [MIDIObjectSetStringProperty()](https://developer.apple.com/documentation/coremidi/1495173-midiobjectsetstringproperty)Added [MIDIObjectType](https://developer.apple.com/documentation/coremidi/midiobjecttype)Added [MIDIOutputPortCreate()](https://developer.apple.com/documentation/coremidi/1495166-midioutputportcreate)Added [MIDIPacket](https://developer.apple.com/documentation/coremidi/midipacket)Added [MIDIPacketList](https://developer.apple.com/documentation/coremidi/midipacketlist)Added [MIDIPacketListAdd()](https://developer.apple.com/documentation/coremidi/1495128-midipacketlistadd)Added [MIDIPacketListInit()](https://developer.apple.com/documentation/coremidi/1495218-midipacketlistinit)Added #def MIDIPacketNextAdded [MIDIPacketNext()](https://developer.apple.com/documentation/coremidi/1495178-midipacketnext) (no architecture available)Added [MIDIPortConnectSource()](https://developer.apple.com/documentation/coremidi/1495278-midiportconnectsource)Added [MIDIPortDisconnectSource()](https://developer.apple.com/documentation/coremidi/1495342-midiportdisconnectsource)Added [MIDIPortDispose()](https://developer.apple.com/documentation/coremidi/1495345-midiportdispose)Added [MIDIPortRef](https://developer.apple.com/documentation/coremidi/midiportref)Added [MIDIReadProc](https://developer.apple.com/documentation/coremidi/midireadproc)Added [MIDIReceived()](https://developer.apple.com/documentation/coremidi/1495276-midireceived)Added [MIDIRestart()](https://developer.apple.com/documentation/coremidi/1495146-midirestart)Added [MIDISend()](https://developer.apple.com/documentation/coremidi/1495289-midisend)Added [MIDISendSysex()](https://developer.apple.com/documentation/coremidi/1495356-midisendsysex)Added [MIDISourceCreate()](https://developer.apple.com/documentation/coremidi/1495212-midisourcecreate)Added [MIDISysexSendRequest](https://developer.apple.com/documentation/coremidi/midisysexsendrequest)Added [MIDITimeStamp](https://developer.apple.com/documentation/coremidi/miditimestamp)Added [MIDIUniqueID](https://developer.apple.com/documentation/coremidi/midiuniqueid)Added [kMIDIIDNotUnique](https://developer.apple.com/documentation/coremidi/1495156-error_constants/kmidiidnotunique)Added [kMIDIInvalidClient](https://developer.apple.com/documentation/coremidi/1495156-error_constants/kmidiinvalidclient)Added [kMIDIInvalidPort](https://developer.apple.com/documentation/coremidi/kmidiinvalidport)Added [kMIDIInvalidUniqueID](https://developer.apple.com/documentation/coremidi/1495307-kmidiinvaliduniqueid/kmidiinvaliduniqueid)Added [kMIDIMessageSendErr](https://developer.apple.com/documentation/coremidi/kmidimessagesenderr)Added [kMIDIMsgIOError](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/kmidimsgioerror)Added [kMIDIMsgObjectAdded](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/msgobjectadded)Added [kMIDIMsgObjectRemoved](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/msgobjectremoved)Added [kMIDIMsgPropertyChanged](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/kmidimsgpropertychanged)Added [kMIDIMsgSerialPortOwnerChanged](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/msgserialportownerchanged)Added [kMIDIMsgSetupChanged](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/msgsetupchanged)Added [kMIDIMsgThruConnectionsChanged](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/msgthruconnectionschanged)Added [kMIDINoConnection](https://developer.apple.com/documentation/coremidi/1495156-error_constants/kmidinoconnection)Added [kMIDINoCurrentSetup](https://developer.apple.com/documentation/coremidi/1495156-error_constants/kmidinocurrentsetup)Added [kMIDIObjectNotFound](https://developer.apple.com/documentation/coremidi/kmidiobjectnotfound)Added [kMIDIObjectType_Destination](https://developer.apple.com/documentation/coremidi/midiobjecttype/destination)Added [kMIDIObjectType_Device](https://developer.apple.com/documentation/coremidi/midiobjecttype/device)Added [kMIDIObjectType_Entity](https://developer.apple.com/documentation/coremidi/midiobjecttype/entity)Added [kMIDIObjectType_ExternalDestination](https://developer.apple.com/documentation/coremidi/midiobjecttype/externaldestination)Added [kMIDIObjectType_ExternalDevice](https://developer.apple.com/documentation/coremidi/midiobjecttype/externaldevice)Added [kMIDIObjectType_ExternalEntity](https://developer.apple.com/documentation/coremidi/midiobjecttype/kmidiobjecttype_externalentity)Added [kMIDIObjectType_ExternalMask](https://developer.apple.com/documentation/coremidi/midiobjecttype/kmidiobjecttype_externalmask)Added [kMIDIObjectType_ExternalSource](https://developer.apple.com/documentation/coremidi/midiobjecttype/kmidiobjecttype_externalsource)Added [kMIDIObjectType_Other](https://developer.apple.com/documentation/coremidi/midiobjecttype/kmidiobjecttype_other)Added [kMIDIObjectType_Source](https://developer.apple.com/documentation/coremidi/midiobjecttype/source)Added [kMIDIPropertyAdvanceScheduleTimeMuSec](https://developer.apple.com/documentation/coremidi/kmidipropertyadvancescheduletimemusec)Added [kMIDIPropertyCanRoute](https://developer.apple.com/documentation/coremidi/kmidipropertycanroute)Added [kMIDIPropertyConnectionUniqueID](https://developer.apple.com/documentation/coremidi/kmidipropertyconnectionuniqueid)Added [kMIDIPropertyDeviceID](https://developer.apple.com/documentation/coremidi/kmidipropertydeviceid)Added [kMIDIPropertyDisplayName](https://developer.apple.com/documentation/coremidi/kmidipropertydisplayname)Added [kMIDIPropertyDriverDeviceEditorApp](https://developer.apple.com/documentation/coremidi/kmidipropertydriverdeviceeditorapp)Added [kMIDIPropertyDriverOwner](https://developer.apple.com/documentation/coremidi/kmidipropertydriverowner)Added [kMIDIPropertyDriverVersion](https://developer.apple.com/documentation/coremidi/kmidipropertydriverversion)Added [kMIDIPropertyImage](https://developer.apple.com/documentation/coremidi/kmidipropertyimage)Added [kMIDIPropertyIsBroadcast](https://developer.apple.com/documentation/coremidi/kmidipropertyisbroadcast)Added [kMIDIPropertyIsDrumMachine](https://developer.apple.com/documentation/coremidi/kmidipropertyisdrummachine)Added [kMIDIPropertyIsEffectUnit](https://developer.apple.com/documentation/coremidi/kmidipropertyiseffectunit)Added [kMIDIPropertyIsEmbeddedEntity](https://developer.apple.com/documentation/coremidi/kmidipropertyisembeddedentity)Added [kMIDIPropertyIsMixer](https://developer.apple.com/documentation/coremidi/kmidipropertyismixer)Added [kMIDIPropertyIsSampler](https://developer.apple.com/documentation/coremidi/kmidipropertyissampler)Added [kMIDIPropertyManufacturer](https://developer.apple.com/documentation/coremidi/kmidipropertymanufacturer)Added [kMIDIPropertyMaxReceiveChannels](https://developer.apple.com/documentation/coremidi/kmidipropertymaxreceivechannels)Added [kMIDIPropertyMaxSysExSpeed](https://developer.apple.com/documentation/coremidi/kmidipropertymaxsysexspeed)Added [kMIDIPropertyMaxTransmitChannels](https://developer.apple.com/documentation/coremidi/kmidipropertymaxtransmitchannels)Added [kMIDIPropertyModel](https://developer.apple.com/documentation/coremidi/kmidipropertymodel)Added [kMIDIPropertyName](https://developer.apple.com/documentation/coremidi/kmidipropertyname)Added [kMIDIPropertyNameConfiguration](https://developer.apple.com/documentation/coremidi/kmidipropertynameconfiguration)Added [kMIDIPropertyOffline](https://developer.apple.com/documentation/coremidi/kmidipropertyoffline)Added [kMIDIPropertyPanDisruptsStereo](https://developer.apple.com/documentation/coremidi/kmidipropertypandisruptsstereo)Added [kMIDIPropertyPrivate](https://developer.apple.com/documentation/coremidi/kmidipropertyprivate)Added [kMIDIPropertyReceiveChannels](https://developer.apple.com/documentation/coremidi/kmidipropertyreceivechannels)Added [kMIDIPropertyReceivesBankSelectLSB](https://developer.apple.com/documentation/coremidi/kmidipropertyreceivesbankselectlsb)Added [kMIDIPropertyReceivesBankSelectMSB](https://developer.apple.com/documentation/coremidi/kmidipropertyreceivesbankselectmsb)Added [kMIDIPropertyReceivesClock](https://developer.apple.com/documentation/coremidi/kmidipropertyreceivesclock)Added [kMIDIPropertyReceivesMTC](https://developer.apple.com/documentation/coremidi/kmidipropertyreceivesmtc)Added [kMIDIPropertyReceivesNotes](https://developer.apple.com/documentation/coremidi/kmidipropertyreceivesnotes)Added [kMIDIPropertyReceivesProgramChanges](https://developer.apple.com/documentation/coremidi/kmidipropertyreceivesprogramchanges)Added [kMIDIPropertySingleRealtimeEntity](https://developer.apple.com/documentation/coremidi/kmidipropertysinglerealtimeentity)Added [kMIDIPropertySupportsGeneralMIDI](https://developer.apple.com/documentation/coremidi/kmidipropertysupportsgeneralmidi)Added [kMIDIPropertySupportsMMC](https://developer.apple.com/documentation/coremidi/kmidipropertysupportsmmc)Added [kMIDIPropertySupportsShowControl](https://developer.apple.com/documentation/coremidi/kmidipropertysupportsshowcontrol)Added [kMIDIPropertyTransmitChannels](https://developer.apple.com/documentation/coremidi/kmidipropertytransmitchannels)Added [kMIDIPropertyTransmitsBankSelectLSB](https://developer.apple.com/documentation/coremidi/kmidipropertytransmitsbankselectlsb)Added [kMIDIPropertyTransmitsBankSelectMSB](https://developer.apple.com/documentation/coremidi/kmidipropertytransmitsbankselectmsb)Added [kMIDIPropertyTransmitsClock](https://developer.apple.com/documentation/coremidi/kmidipropertytransmitsclock)Added [kMIDIPropertyTransmitsMTC](https://developer.apple.com/documentation/coremidi/kmidipropertytransmitsmtc)Added [kMIDIPropertyTransmitsNotes](https://developer.apple.com/documentation/coremidi/kmidipropertytransmitsnotes)Added [kMIDIPropertyTransmitsProgramChanges](https://developer.apple.com/documentation/coremidi/kmidipropertytransmitsprogramchanges)Added [kMIDIPropertyUniqueID](https://developer.apple.com/documentation/coremidi/kmidipropertyuniqueid)Added [kMIDIServerStartErr](https://developer.apple.com/documentation/coremidi/1495156-error_constants/kmidiserverstarterr)Added [kMIDISetupFormatErr](https://developer.apple.com/documentation/coremidi/1495156-error_constants/kmidisetupformaterr)Added [kMIDIUnknownEndpoint](https://developer.apple.com/documentation/coremidi/1495156-error_constants/kmidiunknownendpoint)Added [kMIDIUnknownProperty](https://developer.apple.com/documentation/coremidi/kmidiunknownproperty)Added [kMIDIWrongEndpointType](https://developer.apple.com/documentation/coremidi/1495156-error_constants/kmidiwrongendpointtype)Added [kMIDIWrongPropertyType](https://developer.apple.com/documentation/coremidi/1495156-error_constants/kmidiwrongpropertytype)Added [kMIDIWrongThread](https://developer.apple.com/documentation/coremidi/kmidiwrongthread)MIDISetup.hAdded [MIDIDeviceAddEntity()](https://developer.apple.com/documentation/coremidi/1508206-midideviceaddentity)Added [MIDIDeviceRemoveEntity()](https://developer.apple.com/documentation/coremidi/1508180-midideviceremoveentity)Added [MIDIEntityAddOrRemoveEndpoints()](https://developer.apple.com/documentation/coremidi/1508340-midientityaddorremoveendpoints)Added [MIDIExternalDeviceCreate()](https://developer.apple.com/documentation/coremidi/1508456-midiexternaldevicecreate)Added [MIDISetupAddDevice()](https://developer.apple.com/documentation/coremidi/1508299-midisetupadddevice)Added [MIDISetupAddExternalDevice()](https://developer.apple.com/documentation/coremidi/1508222-midisetupaddexternaldevice)Added [MIDISetupRef](https://developer.apple.com/documentation/coremidi/midisetupref)Added [MIDISetupRemoveDevice()](https://developer.apple.com/documentation/coremidi/1508237-midisetupremovedevice)Added [MIDISetupRemoveExternalDevice()](https://developer.apple.com/documentation/coremidi/1508370-midisetupremoveexternaldevice)MIDIThruConnection.hAdded [MIDIControlTransform](https://developer.apple.com/documentation/coremidi/midicontroltransform)Added [MIDIThruConnectionCreate()](https://developer.apple.com/documentation/coremidi/1508523-midithruconnectioncreate)Added [MIDIThruConnectionDispose()](https://developer.apple.com/documentation/coremidi/1508256-midithruconnectiondispose)Added [MIDIThruConnectionEndpoint](https://developer.apple.com/documentation/coremidi/midithruconnectionendpoint)Added [MIDIThruConnectionFind()](https://developer.apple.com/documentation/coremidi/1508377-midithruconnectionfind)Added [MIDIThruConnectionGetParams()](https://developer.apple.com/documentation/coremidi/1508390-midithruconnectiongetparams)Added [MIDIThruConnectionParams](https://developer.apple.com/documentation/coremidi/midithruconnectionparams)Added [MIDIThruConnectionParamsInitialize()](https://developer.apple.com/documentation/coremidi/1508520-midithruconnectionparamsinitiali)Added [#def MIDIThruConnectionParamsSize](https://developer.apple.com/documentation/coremidi/midi_thru_connection/midithruconnectionparamssize)Added [MIDIThruConnectionRef](https://developer.apple.com/documentation/coremidi/midithruconnectionref)Added [MIDIThruConnectionSetParams()](https://developer.apple.com/documentation/coremidi/1508352-midithruconnectionsetparams)Added [MIDITransform](https://developer.apple.com/documentation/coremidi/miditransform)Added [MIDITransformControlType](https://developer.apple.com/documentation/coremidi/miditransformcontroltype)Added [MIDITransformType](https://developer.apple.com/documentation/coremidi/miditransformtype)Added [MIDIValueMap](https://developer.apple.com/documentation/coremidi/midivaluemap)Added [kMIDIControlType_14Bit](https://developer.apple.com/documentation/coremidi/miditransformcontroltype/kmidicontroltype_14bit)Added [kMIDIControlType_14BitNRPN](https://developer.apple.com/documentation/coremidi/miditransformcontroltype/kmidicontroltype_14bitnrpn)Added [kMIDIControlType_14BitRPN](https://developer.apple.com/documentation/coremidi/miditransformcontroltype/controltype_14bitrpn)Added [kMIDIControlType_7Bit](https://developer.apple.com/documentation/coremidi/miditransformcontroltype/controltype_7bit)Added [kMIDIControlType_7BitNRPN](https://developer.apple.com/documentation/coremidi/miditransformcontroltype/controltype_7bitnrpn)Added [kMIDIControlType_7BitRPN](https://developer.apple.com/documentation/coremidi/miditransformcontroltype/controltype_7bitrpn)Added [kMIDIThruConnection_MaxEndpoints](https://developer.apple.com/documentation/coremidi/kmidithruconnection_maxendpoints)Added [kMIDITransform_Add](https://developer.apple.com/documentation/coremidi/miditransformtype/add)Added [kMIDITransform_FilterOut](https://developer.apple.com/documentation/coremidi/miditransformtype/kmiditransform_filterout)Added [kMIDITransform_MapControl](https://developer.apple.com/documentation/coremidi/miditransformtype/kmiditransform_mapcontrol)Added [kMIDITransform_MapValue](https://developer.apple.com/documentation/coremidi/miditransformtype/mapvalue)Added [kMIDITransform_MaxValue](https://developer.apple.com/documentation/coremidi/miditransformtype/maxvalue)Added [kMIDITransform_MinValue](https://developer.apple.com/documentation/coremidi/miditransformtype/minvalue)Added [kMIDITransform_None](https://developer.apple.com/documentation/coremidi/miditransformtype/none)Added [kMIDITransform_Scale](https://developer.apple.com/documentation/coremidi/miditransformtype/scale)

## CoreMotion

No changes

## CoreTelephony

CoreTelephonyDefines.hAdded #def CORETELEPHONY_EXTERNAdded #def CORETELEPHONY_EXTERN_CLASS

## CoreText

CTFont.hAdded [CTFontDrawGlyphs()](https://developer.apple.com/documentation/coretext/1509850-ctfontdrawglyphs)Added [CTFontGetLigatureCaretPositions()](https://developer.apple.com/documentation/coretext/1508820-ctfontgetligaturecaretpositions)Added [kCTFontTableSbit](https://developer.apple.com/documentation/coretext/1524658-anonymous/kctfonttablesbit)Added [kCTFontTableSbix](https://developer.apple.com/documentation/coretext/kctfonttablesbix)CTFontCollection.hAdded [CTFontCollectionCopyOptions](https://developer.apple.com/documentation/coretext/ctfontcollectioncopyoptions)Added [kCTFontCollectionCopyDefaultOptions](https://developer.apple.com/documentation/coretext/ctfontcollectioncopyoptions/kctfontcollectioncopydefaultoptions)Added [kCTFontCollectionCopyStandardSort](https://developer.apple.com/documentation/coretext/ctfontcollectioncopyoptions/1509424-standardsort)Added [kCTFontCollectionCopyUnique](https://developer.apple.com/documentation/coretext/ctfontcollectioncopyoptions/kctfontcollectioncopyunique)CTFontTraits.hRemoved [kCTFontColorGlyphsTrait](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1508808-colorglyphstrait)CTFrame.hAdded [CTFramePathFillRule](https://developer.apple.com/documentation/coretext/ctframepathfillrule)Added [kCTFramePathFillEvenOdd](https://developer.apple.com/documentation/coretext/ctframepathfillrule/evenodd)Added [kCTFramePathFillRuleAttributeName](https://developer.apple.com/documentation/coretext/kctframepathfillruleattributename)Added [kCTFramePathFillWindingNumber](https://developer.apple.com/documentation/coretext/ctframepathfillrule/windingnumber)Added [kCTFramePathWidthAttributeName](https://developer.apple.com/documentation/coretext/kctframepathwidthattributename)

## CoreVideo

No changes

## EventKit

EKError.hAdded [EKErrorInvalidSpan](https://developer.apple.com/documentation/eventkit/ekerror/code/invalidspan)

## EventKitUI

EKEventViewController.hAdded [EKEventViewController.delegate](https://developer.apple.com/documentation/eventkitui/ekeventviewcontroller/1613939-delegate)Added [EKEventViewDelegate](https://developer.apple.com/documentation/eventkitui/ekeventviewdelegate)Added [-[EKEventViewDelegate eventViewController:didCompleteWithAction:]](https://developer.apple.com/documentation/eventkitui/ekeventviewdelegate/1613925-eventviewcontroller)Added [EKEventViewAction](https://developer.apple.com/documentation/eventkitui/ekeventviewaction)Added [EKEventViewActionDeleted](https://developer.apple.com/documentation/eventkitui/ekeventviewaction/deleted)Added [EKEventViewActionDone](https://developer.apple.com/documentation/eventkitui/ekeventviewaction/ekeventviewactiondone)Added [EKEventViewActionResponded](https://developer.apple.com/documentation/eventkitui/ekeventviewaction/ekeventviewactionresponded)Modified [EKEventViewController](https://developer.apple.com/documentation/eventkitui/ekeventviewcontroller)

|  | Protocols |
| --- | --- |
| From | UIActionSheetDelegate |
| To | _none_ |

## ExternalAccessory

ExternalAccessoryDefines.hAdded #def EA_EXTERN_CLASS_AVAILABLE

## Foundation

NSObjCRuntime.hAdded [#def NSFoundationVersionNumber_iOS_4_0](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber_ios_4_0)Added [#def NSFoundationVersionNumber_iPhoneOS_3_2](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber_iphoneos_3_2)Added #def NS_CLASS_AVAILABLE

## GameKit

GKAchievement.hModified [GKAchievement.hidden](https://developer.apple.com/documentation/gamekit/gkachievement/1521136-ishidden)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign, getter=isHidden) BOOL hidden |
| To | @property(nonatomic, assign, getter=isHidden, readonly) BOOL hidden |

GKAchievementDescription.hModified [GKAchievementDescription.unachievedDescription](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416584-unachieveddescription)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain) NSString \*unachievedDescription |
| To | @property(nonatomic, retain, readonly) NSString \*unachievedDescription |

Modified [GKAchievementDescription.achievedDescription](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416598-achieveddescription)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain) NSString \*achievedDescription |
| To | @property(nonatomic, retain, readonly) NSString \*achievedDescription |

Modified [GKAchievementDescription.maximumPoints](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416589-maximumpoints)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign) NSInteger maximumPoints |
| To | @property(nonatomic, assign, readonly) NSInteger maximumPoints |

Modified [GKAchievementDescription.identifier](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416586-identifier)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain) NSString \*identifier |
| To | @property(nonatomic, retain, readonly) NSString \*identifier |

Modified [GKAchievementDescription.title](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416602-title)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain) NSString \*title |
| To | @property(nonatomic, retain, readonly) NSString \*title |

Modified [GKAchievementDescription.hidden](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416582-hidden)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, getter=isHidden, assign) BOOL hidden |
| To | @property(nonatomic, getter=isHidden, assign, readonly) BOOL hidden |

Modified [GKAchievementDescription.image](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416591-image)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain) UIImage \*image |
| To | @property(nonatomic, retain, readonly) UIImage \*image |

GKError.hAdded [GKErrorInvalidParameter](https://developer.apple.com/documentation/gamekit/gkerror/code/invalidparameter)GKFriendRequestComposeViewController.hAdded [GKFriendRequestComposeViewController](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller)Added [-[GKFriendRequestComposeViewController addRecipientsWithEmailAddresses:]](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437190-addrecipients)Added [-[GKFriendRequestComposeViewController addRecipientsWithPlayerIDs:]](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437188-addrecipientswithplayerids)Added [GKFriendRequestComposeViewController.composeViewDelegate](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437192-composeviewdelegate)Added [+[GKFriendRequestComposeViewController maxNumberOfRecipients]](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437194-maxnumberofrecipients)Added [-[GKFriendRequestComposeViewController setMessage:]](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437201-setmessage)Added [GKFriendRequestComposeViewControllerDelegate](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontrollerdelegate)Added [-[GKFriendRequestComposeViewControllerDelegate friendRequestComposeViewControllerDidFinish:]](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontrollerdelegate/1437186-friendrequestcomposeviewcontroll)

## iAd

ADBannerView.hAdded [ADBannerContentSizeIdentifierLandscape](https://developer.apple.com/documentation/iad/adbannercontentsizeidentifierlandscape)Added [ADBannerContentSizeIdentifierPortrait](https://developer.apple.com/documentation/iad/adbannercontentsizeidentifierportrait)Modified [ADBannerContentSizeIdentifier480x32](https://developer.apple.com/documentation/iad/adbannercontentsizeidentifier480x32)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 4.2 |

Modified [ADBannerContentSizeIdentifier320x50](https://developer.apple.com/documentation/iad/adbannercontentsizeidentifier320x50)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 4.2 |

## ImageIO

No changes

## MapKit

MKAnnotationView.hAdded [-[MKAnnotationView setDragState:animated:]](https://developer.apple.com/documentation/mapkit/mkannotationview/1452639-setdragstate)MKMapView.hAdded [-[MKMapView annotationsInMapRect:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452279-annotations)

## MediaPlayer

MPMediaEntity.hAdded [MPMediaEntity](https://developer.apple.com/documentation/mediaplayer/mpmediaentity)Added [+[MPMediaEntity canFilterByProperty:]](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/1620123-canfilter)Added [-[MPMediaEntity enumerateValuesForProperties:usingBlock:]](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/1620122-enumeratevaluesforproperties)Added [-[MPMediaEntity valueForProperty:]](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/1620128-valueforproperty)Added [MPMediaEntityPropertyPersistentID](https://developer.apple.com/documentation/mediaplayer/mpmediaentitypropertypersistentid)MPMediaItem.hRemoved +[MPMediaItem canFilterByProperty:]Removed -[MPMediaItem enumerateValuesForProperties:usingBlock:]Removed -[MPMediaItem valueForProperty:]Added [MPMediaItemPropertyAlbumArtistPersistentID](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertyalbumartistpersistentid)Added [MPMediaItemPropertyAlbumPersistentID](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertyalbumpersistentid)Added [MPMediaItemPropertyArtistPersistentID](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertyartistpersistentid)Added [MPMediaItemPropertyComposerPersistentID](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertycomposerpersistentid)Added [MPMediaItemPropertyGenrePersistentID](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertygenrepersistentid)Added [MPMediaItemPropertyPodcastPersistentID](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertypodcastpersistentid)Modified [MPMediaItem](https://developer.apple.com/documentation/mediaplayer/mpmediaitem)

|  | Superclass | Protocols |
| --- | --- | --- |
| From | NSObject | NSCoding |
| To | MPMediaEntity | _none_ |

MPMediaItemCollection.hModified [MPMediaItemCollection](https://developer.apple.com/documentation/mediaplayer/mpmediaitemcollection)

|  | Superclass | Protocols |
| --- | --- | --- |
| From | NSObject | NSCoding |
| To | MPMediaEntity | _none_ |

MPMediaLibrary.hModified [MPMediaLibrary](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCoding |

MPMediaPlaylist.hRemoved +[MPMediaPlaylist canFilterByProperty:]Removed -[MPMediaPlaylist valueForProperty:]MPMediaQuery.hAdded [+[MPMediaItem persistentIDPropertyForGroupingType:]](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621805-persistentidproperty)Added [+[MPMediaItem titlePropertyForGroupingType:]](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621775-titlepropertyforgroupingtype)Added [MPMediaQuery.collectionSections](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621779-collectionsections)Added [MPMediaQuery.itemSections](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621797-itemsections)Added MPMediaItem(MPMediaQueryAdditions)MPMediaQuerySection.hAdded [MPMediaQuerySection](https://developer.apple.com/documentation/mediaplayer/mpmediaquerysection)Added [MPMediaQuerySection.range](https://developer.apple.com/documentation/mediaplayer/mpmediaquerysection/1624166-range)Added [MPMediaQuerySection.title](https://developer.apple.com/documentation/mediaplayer/mpmediaquerysection/1624170-title)MPMoviePlayerController.hRemoved -[MPMoviePlayerController play] (no architecture available)Removed [-[MPMoviePlayerController setInitialPlaybackTime:]](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620796-initialplaybacktime) (no architecture available)Removed -[MPMoviePlayerController stop] (no architecture available)Removed MPMoviePlayerController()Removed MPMoviePlayerController(MPMediaPlayback) (no architecture available)Modified [MPMoviePlayerController](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | MPMediaPlayback |

MPVolumeView.hAdded [MPVolumeView.showsRouteButton](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620075-showsroutebutton)Added [MPVolumeView.showsVolumeSlider](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620079-showsvolumeslider)MediaPlayerDefines.hAdded #def MP_EXTERN_CLASS_AVAILABLE

## MessageUI

No changes

## MobileCoreServices

No changes

## OpenAL

No changes

## OpenGLES

No changes

## QuartzCore

CAShapeLayer.hAdded [CAShapeLayer.strokeEnd](https://developer.apple.com/documentation/quartzcore/cashapelayer/1522252-strokeend)Added [CAShapeLayer.strokeStart](https://developer.apple.com/documentation/quartzcore/cashapelayer/1521929-strokestart)

## QuickLook

QLBase.hRemoved #def QUICKLOOK_VERSIONQLPreviewController.hAdded [-[QLPreviewControllerDelegate previewController:frameForPreviewItem:inSourceView:]](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate/1617007-previewcontroller)Added [-[QLPreviewControllerDelegate previewController:transitionImageForPreviewItem:contentRect:]](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate/1617021-previewcontroller)Modified [QLPreviewController](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller)

|  | Protocols |
| --- | --- |
| From | UIDocumentInteractionControllerDelegate |
| To | _none_ |

## Security

SecBase.hAdded [errSecAuthFailed](https://developer.apple.com/documentation/security/errsecauthfailed)

## StoreKit

StoreKitDefines.hAdded #def SK_EXTERN_CLASS_AVAILABLE

## SystemConfiguration

No changes

## UIKit

UIAccessibility.hAdded [-[NSObject accessibilityScroll:]](https://developer.apple.com/documentation/objectivec/nsobject/1615161-accessibilityscroll)Added [UIAccessibilityScrollDirection](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilityscrolldirection)Added [UIAccessibilityScrollDirectionDown](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilityscrolldirection/down)Added [UIAccessibilityScrollDirectionLeft](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilityscrolldirection/left)Added [UIAccessibilityScrollDirectionRight](https://developer.apple.com/documentation/uikit/uiaccessibilityscrolldirection/uiaccessibilityscrolldirectionright)Added [UIAccessibilityScrollDirectionUp](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilityscrolldirection/up)UIAccessibilityConstants.hAdded [UIAccessibilityPageScrolledNotification](https://developer.apple.com/documentation/uikit/uiaccessibility/notification/1620190-pagescrolled)UIApplication.hRemoved [-[UIApplication scheduledLocalNotifications]](https://developer.apple.com/documentation/uikit/uiapplication/1622993-scheduledlocalnotifications)Added [UIApplication.scheduledLocalNotifications](https://developer.apple.com/documentation/uikit/uiapplication/1622993-scheduledlocalnotifications)Added [-[UIApplicationDelegate application:openURL:sourceApplication:annotation:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623073-application)UIDevice.hAdded [-[UIDevice playInputClick]](https://developer.apple.com/documentation/uikit/uidevice/1620050-playinputclick)Added [UIInputViewAudioFeedback](https://developer.apple.com/documentation/uikit/uiinputviewaudiofeedback)Added [UIInputViewAudioFeedback.enableInputClicksWhenVisible](https://developer.apple.com/documentation/uikit/uiinputviewaudiofeedback/1620038-enableinputclickswhenvisible)UIKitDefines.hRemoved #def UIKIT_EXTERN_CLASSAdded #def UIKIT_CLASS_AVAILABLEUIPrintError.hAdded [UIPrintErrorDomain](https://developer.apple.com/documentation/uikit/uiprinterrordomain)Added [UIPrintJobFailedError](https://developer.apple.com/documentation/uikit/uiprinterrorcode/uiprintjobfailederror)Added [UIPrintNoContentError](https://developer.apple.com/documentation/uikit/uiprinterror/code/nocontent)Added [UIPrintUnknownImageFormatError](https://developer.apple.com/documentation/uikit/uiprinterror/code/unknownimageformat)Added [UIPrintingNotAvailableError](https://developer.apple.com/documentation/uikit/uiprinterrorcode/uiprintingnotavailableerror)UIPrintFormatter.hAdded [UIMarkupTextPrintFormatter](https://developer.apple.com/documentation/uikit/uimarkuptextprintformatter)Added [-[UIMarkupTextPrintFormatter initWithMarkupText:]](https://developer.apple.com/documentation/uikit/uimarkuptextprintformatter/1621845-init)Added [UIMarkupTextPrintFormatter.markupText](https://developer.apple.com/documentation/uikit/uimarkuptextprintformatter/1621842-markuptext)Added [UIPrintFormatter](https://developer.apple.com/documentation/uikit/uiprintformatter)Added [UIPrintFormatter.contentInsets](https://developer.apple.com/documentation/uikit/uiprintformatter/1621823-contentinsets)Added [-[UIPrintFormatter drawInRect:forPageAtIndex:]](https://developer.apple.com/documentation/uikit/uiprintformatter/1621841-draw)Added [UIPrintFormatter.maximumContentHeight](https://developer.apple.com/documentation/uikit/uiprintformatter/1621826-maximumcontentheight)Added [UIPrintFormatter.maximumContentWidth](https://developer.apple.com/documentation/uikit/uiprintformatter/1621840-maximumcontentwidth)Added [UIPrintFormatter.pageCount](https://developer.apple.com/documentation/uikit/uiprintformatter/1621843-pagecount)Added [UIPrintFormatter.printPageRenderer](https://developer.apple.com/documentation/uikit/uiprintformatter/1621821-printpagerenderer)Added [-[UIPrintFormatter rectForPageAtIndex:]](https://developer.apple.com/documentation/uikit/uiprintformatter/1621829-rectforpageatindex)Added [-[UIPrintFormatter removeFromPrintPageRenderer]](https://developer.apple.com/documentation/uikit/uiprintformatter/1621834-removefromprintpagerenderer)Added [UIPrintFormatter.startPage](https://developer.apple.com/documentation/uikit/uiprintformatter/1621827-startpage)Added [UISimpleTextPrintFormatter](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter)Added [UISimpleTextPrintFormatter.color](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/1621830-color)Added [UISimpleTextPrintFormatter.font](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/1621837-font)Added [-[UISimpleTextPrintFormatter initWithText:]](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/1621822-initwithtext)Added [UISimpleTextPrintFormatter.text](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/1621833-text)Added [UISimpleTextPrintFormatter.textAlignment](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/1621832-textalignment)Added [-[UIView drawRect:forViewPrintFormatter:]](https://developer.apple.com/documentation/uikit/uiview/1621844-drawrect)Added [-[UIView viewPrintFormatter]](https://developer.apple.com/documentation/uikit/uiview/1621835-viewprintformatter)Added [UIViewPrintFormatter](https://developer.apple.com/documentation/uikit/uiviewprintformatter)Added [UIViewPrintFormatter.view](https://developer.apple.com/documentation/uikit/uiviewprintformatter/1621824-view)Added UIView(UIPrintFormatter)UIPrintInfo.hAdded [UIPrintInfo](https://developer.apple.com/documentation/uikit/uiprintinfo)Added [-[UIPrintInfo dictionaryRepresentation]](https://developer.apple.com/documentation/uikit/uiprintinfo/1623539-dictionaryrepresentation)Added [UIPrintInfo.duplex](https://developer.apple.com/documentation/uikit/uiprintinfo/1623549-duplex)Added [UIPrintInfo.jobName](https://developer.apple.com/documentation/uikit/uiprintinfo/1623543-jobname)Added [UIPrintInfo.orientation](https://developer.apple.com/documentation/uikit/uiprintinfo/1623550-orientation)Added [UIPrintInfo.outputType](https://developer.apple.com/documentation/uikit/uiprintinfo/1623552-outputtype)Added [+[UIPrintInfo printInfo]](https://developer.apple.com/documentation/uikit/uiprintinfo/1623545-printinfo)Added [+[UIPrintInfo printInfoWithDictionary:]](https://developer.apple.com/documentation/uikit/uiprintinfo/1623553-printinfowithdictionary)Added [UIPrintInfo.printerID](https://developer.apple.com/documentation/uikit/uiprintinfo/1623535-printerid)Added [UIPrintInfoDuplex](https://developer.apple.com/documentation/uikit/uiprintinfo/duplex)Added [UIPrintInfoDuplexLongEdge](https://developer.apple.com/documentation/uikit/uiprintinfo/duplex/longedge)Added [UIPrintInfoDuplexNone](https://developer.apple.com/documentation/uikit/uiprintinfoduplex/uiprintinfoduplexnone)Added [UIPrintInfoDuplexShortEdge](https://developer.apple.com/documentation/uikit/uiprintinfo/duplex/shortedge)Added [UIPrintInfoOrientation](https://developer.apple.com/documentation/uikit/uiprintinfo/orientation)Added [UIPrintInfoOrientationLandscape](https://developer.apple.com/documentation/uikit/uiprintinfoorientation/uiprintinfoorientationlandscape)Added [UIPrintInfoOrientationPortrait](https://developer.apple.com/documentation/uikit/uiprintinfoorientation/uiprintinfoorientationportrait)Added [UIPrintInfoOutputGeneral](https://developer.apple.com/documentation/uikit/uiprintinfo/outputtype/general)Added [UIPrintInfoOutputGrayscale](https://developer.apple.com/documentation/uikit/uiprintinfo/outputtype/grayscale)Added [UIPrintInfoOutputPhoto](https://developer.apple.com/documentation/uikit/uiprintinfooutputtype/uiprintinfooutputphoto)Added [UIPrintInfoOutputType](https://developer.apple.com/documentation/uikit/uiprintinfo/outputtype)UIPrintInteractionController.hAdded [UIPrintInteractionController](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller)Added [+[UIPrintInteractionController canPrintData:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618184-canprint)Added [+[UIPrintInteractionController canPrintURL:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618155-canprinturl)Added [UIPrintInteractionController.delegate](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618153-delegate)Added [-[UIPrintInteractionController dismissAnimated:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618166-dismiss)Added [+[UIPrintInteractionController isPrintingAvailable]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618183-isprintingavailable)Added [-[UIPrintInteractionController presentAnimated:completionHandler:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618149-present)Added [-[UIPrintInteractionController presentFromBarButtonItem:animated:completionHandler:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618169-presentfrombarbuttonitem)Added [-[UIPrintInteractionController presentFromRect:inView:animated:completionHandler:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618176-present)Added [UIPrintInteractionController.printFormatter](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618152-printformatter)Added [UIPrintInteractionController.printInfo](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618171-printinfo)Added [UIPrintInteractionController.printPageRenderer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618148-printpagerenderer)Added [UIPrintInteractionController.printPaper](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618165-printpaper)Added [+[UIPrintInteractionController printableUTIs]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618150-printableutis)Added [UIPrintInteractionController.printingItem](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618157-printingitem)Added [UIPrintInteractionController.printingItems](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618156-printingitems)Added [+[UIPrintInteractionController sharedPrintController]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618159-shared)Added [UIPrintInteractionController.showsPageRange](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618180-showspagerange)Added [UIPrintInteractionControllerDelegate](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate)Added [-[UIPrintInteractionControllerDelegate printInteractionController:choosePaper:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618160-printinteractioncontroller)Added [-[UIPrintInteractionControllerDelegate printInteractionControllerDidDismissPrinterOptions:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618175-printinteractioncontrollerdiddis)Added [-[UIPrintInteractionControllerDelegate printInteractionControllerDidFinishJob:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618154-printinteractioncontrollerdidfin)Added [-[UIPrintInteractionControllerDelegate printInteractionControllerDidPresentPrinterOptions:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618158-printinteractioncontrollerdidpre)Added [-[UIPrintInteractionControllerDelegate printInteractionControllerParentViewController:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618162-printinteractioncontrollerparent)Added [-[UIPrintInteractionControllerDelegate printInteractionControllerWillDismissPrinterOptions:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618151-printinteractioncontrollerwilldi)Added [-[UIPrintInteractionControllerDelegate printInteractionControllerWillPresentPrinterOptions:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618168-printinteractioncontrollerwillpr)Added [-[UIPrintInteractionControllerDelegate printInteractionControllerWillStartJob:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618185-printinteractioncontrollerwillst)Added [UIPrintInteractionCompletionHandler](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/completionhandler)UIPrintPageRenderer.hAdded [UIPrintPageRenderer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer)Added [-[UIPrintPageRenderer addPrintFormatter:startingAtPageAtIndex:]](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621632-addprintformatter)Added [-[UIPrintPageRenderer drawContentForPageAtIndex:inRect:]](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621641-drawcontentforpageatindex)Added [-[UIPrintPageRenderer drawFooterForPageAtIndex:inRect:]](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621638-drawfooterforpage)Added [-[UIPrintPageRenderer drawHeaderForPageAtIndex:inRect:]](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621639-drawheaderforpageatindex)Added [-[UIPrintPageRenderer drawPageAtIndex:inRect:]](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621636-drawpageatindex)Added [-[UIPrintPageRenderer drawPrintFormatter:forPageAtIndex:]](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621644-drawprintformatter)Added [UIPrintPageRenderer.footerHeight](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621634-footerheight)Added [UIPrintPageRenderer.headerHeight](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621630-headerheight)Added [-[UIPrintPageRenderer numberOfPages]](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621631-numberofpages)Added [UIPrintPageRenderer.paperRect](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621633-paperrect)Added [-[UIPrintPageRenderer prepareForDrawingPages:]](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621643-prepare)Added [UIPrintPageRenderer.printFormatters](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621640-printformatters)Added [-[UIPrintPageRenderer printFormattersForPageAtIndex:]](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621635-printformattersforpage)Added [UIPrintPageRenderer.printableRect](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621628-printablerect)UIPrintPaper.hAdded [UIPrintPaper](https://developer.apple.com/documentation/uikit/uiprintpaper)Added [+[UIPrintPaper bestPaperForPageSize:withPapersFromArray:]](https://developer.apple.com/documentation/uikit/uiprintpaper/1623527-bestpaperforpagesize)Added [UIPrintPaper.paperSize](https://developer.apple.com/documentation/uikit/uiprintpaper/1623529-papersize)Added [-[UIPrintPaper printRect]](https://developer.apple.com/documentation/uikit/uiprintpaper/1623528-printrect)Added [UIPrintPaper.printableRect](https://developer.apple.com/documentation/uikit/uiprintpaper/1623530-printablerect)Added UIPrintPaper(Deprecated_Nonfunctional)UITableView.hModified [-[UITableViewDataSource tableView:numberOfRowsInSection:]](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614931-tableview)

|  | Declaration |
| --- | --- |
| From | - (NSInteger)tableView:(UITableView \*)table numberOfRowsInSection:(NSInteger)section |
| To | - (NSInteger)tableView:(UITableView \*)tableView numberOfRowsInSection:(NSInteger)section |

UITextInput.hAdded [UITextInputMode](https://developer.apple.com/documentation/uikit/uitextinputmode)Added [+[UITextInputMode currentInputMode]](https://developer.apple.com/documentation/uikit/uitextinputmode/1614538-currentinputmode)Added [UITextInputMode.primaryLanguage](https://developer.apple.com/documentation/uikit/uitextinputmode/1614535-primarylanguage)Added [UITextInputCurrentInputModeDidChangeNotification](https://developer.apple.com/documentation/uikit/uitextinputcurrentinputmodedidchangenotification)

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
