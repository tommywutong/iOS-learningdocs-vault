---
title: API Changes in Snow Leopard
apple_id: TP40007673
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/SnowLeopard_API_ReleaseNote/Kernel.html
archived_at: '2026-07-18T02:58:43.821325Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [API Changes in Snow Leopard](API%20Changes%20in%20Snow%20Leopard.md)


[ADC Home](https://developer.apple.com/) >
[Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) >
Release Notes >
OS X >
[API Changes in Snow Leopard Developer Preview](API%20Changes%20in%20Snow%20Leopard.md) >

# Kernel Changes

## Kernel

Bluetooth.hRemoved BluetoothHCIRequestNotificationInfo (no architecture available)Removed kBluetoothHCICommandIOCapabilityResponse (no architecture available)Added [BluetoothHCIEventReadExtendedFeaturesResults](https://developer.apple.com/documentation/kernel/bluetoothhcieventreadextendedfeaturesresults) (no architecture available)Added [BluetoothHCIEventReadRemoteExtendedFeaturesResults](https://developer.apple.com/documentation/kernel/bluetoothhcieventreadremoteextendedfeaturesresults) (no architecture available)Added [BluetoothHCIEventSimplePairingCompleteResults](https://developer.apple.com/documentation/kernel/bluetoothhcieventsimplepairingcompleteresults) (no architecture available)Added [BluetoothHCIExtendedFeaturesInfo](https://developer.apple.com/documentation/kernel/bluetoothhciextendedfeaturesinfo) (no architecture available)Added [BluetoothHCIPageNumber](https://developer.apple.com/documentation/iobluetooth/bluetoothhcipagenumber) (no architecture available)Added [BluetoothNumericValue](https://developer.apple.com/documentation/iobluetooth/bluetoothnumericvalue) (no architecture available)Added [BluetoothUserConfirmationRequest](https://developer.apple.com/documentation/iobluetooth/bluetoothuserconfirmationrequest) (no architecture available)Added [kBluetoothFeature3SlotEnhancedDataRateeSCOPackets](https://developer.apple.com/documentation/iobluetooth/kbluetoothfeature3slotenhanceddatarateescopackets) (no architecture available)Added [kBluetoothFeaturePowerControlRequests](https://developer.apple.com/documentation/kernel/bluetoothfeaturebits/kbluetoothfeaturepowercontrolrequests) (no architecture available)Added [kBluetoothFeatureSimpleSecurePairingHostMode](https://developer.apple.com/documentation/iobluetooth/bluetoothfeaturebits/kbluetoothfeaturesimplesecurepairinghostmode) (no architecture available)Added [kBluetoothFeatureSniffSubrating](https://developer.apple.com/documentation/kernel/bluetoothfeaturebits/kbluetoothfeaturesniffsubrating) (no architecture available)Added [kBluetoothHCICommandIOCapabilityRequestReply](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandiocapabilityrequestreply) (no architecture available)Added [kBluetoothHCICommandReadRemoteExtendedFeatures](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandreadremoteextendedfeatures) (no architecture available)Added [#def kBluetoothHCIEventMaskIOCapabilityRequestEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmaskiocapabilityrequestevent)Added [#def kBluetoothHCIEventMaskIOCapabilityRequestReplyEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmaskiocapabilityrequestreplyevent)Added [#def kBluetoothHCIEventMaskKeypressNotificationEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmaskkeypressnotificationevent)Added [#def kBluetoothHCIEventMaskRemoteOOBDataRequestEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmaskremoteoobdatarequestevent)Added [#def kBluetoothHCIEventMaskSimplePairingCompleteEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmasksimplepairingcompleteevent)Added [#def kBluetoothHCIEventMaskUserConfirmationRequestEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmaskuserconfirmationrequestevent)Added [#def kBluetoothHCIEventMaskUserPasskeyNotificationEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmaskuserpasskeynotificationevent)Added [#def kBluetoothHCIEventMaskUserPasskeyRequestEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmaskuserpasskeyrequestevent)BluetoothAssignedNumbers.hAdded [kBluetoothSDPAttributeIdentifierHIDVirtualCable](https://developer.apple.com/documentation/kernel/sdpattributeidentifiercodes/kbluetoothsdpattributeidentifierhidvirtualcable)IO80211Controller.hRemoved IO80211Controller::monitorDLT() (no architecture available)Removed IO80211Controller::monitorPacketHeaderLength() (no architecture available)Removed IO80211SystemPowerState (no architecture available)Removed kIO80211SystemPowerStateAwake (no architecture available)Removed kIO80211SystemPowerStateSleeping (no architecture available)Removed kIO80211SystemPowerStateUnknown (no architecture available)Added IO80211Controller::join4NetBoot() (no architecture available)IO80211Interface.hRemoved IO80211Interface::createStatusDevice() (no architecture available)Removed IO80211Interface::inputEAPOLFrame() (no architecture available)Removed IO80211Interface::performCountryCodeOpGated() (no architecture available)Added IO80211Interface::free() (no architecture available)IOATAStorageDefines.hModified [kATAOperationTypeSMART](https://developer.apple.com/documentation/iokit/1556750-anonymous/kataoperationtypesmart)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,ppc64,i386,x86_64 |

Modified [kATAOperationTypeSMS](https://developer.apple.com/documentation/iokit/1556750-anonymous/kataoperationtypesms)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,ppc64,i386,x86_64 |

Modified [kATAOperationTypeRead](https://developer.apple.com/documentation/kernel/1646149-anonymous/kataoperationtyperead)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,ppc64,i386,x86_64 |

Modified [kATAOperationTypeConfiguration](https://developer.apple.com/documentation/iokit/1556750-anonymous/kataoperationtypeconfiguration)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,ppc64,i386,x86_64 |

Modified [kATAOperationTypeFlushCache](https://developer.apple.com/documentation/kernel/1646149-anonymous/kataoperationtypeflushcache)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,ppc64,i386,x86_64 |

Modified [kATAOperationTypePowerManagement](https://developer.apple.com/documentation/iokit/1556750-anonymous/kataoperationtypepowermanagement)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,ppc64,i386,x86_64 |

Modified [ATAOperationType](https://developer.apple.com/documentation/kernel/ataoperationtype)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,ppc64,i386,x86_64 |

Modified [kATAOperationTypeWrite](https://developer.apple.com/documentation/iokit/1556750-anonymous/kataoperationtypewrite)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,ppc64,i386,x86_64 |

IOBDMediaBSDClient.hModified IOBDMediaBSDClient::ioctl()

|  | Declaration |
| --- | --- |
| Old | virtual int ioctl ( dev_t, u_long cmd, caddr_t data, int, proc_t); |
| New | virtual int ioctl ( dev_t dev, u_long cmd, caddr_t data, int flags, proc_t proc); |

IOBDServices.hAdded IOBDServices::getWriteCacheState() (no architecture available)Added IOBDServices::setWriteCacheState() (no architecture available)IOBlockStorageDevice.hModified IOBlockStorageDevice::OSMetaClassDeclareReservedUnused()

|  | Declaration |
| --- | --- |
| Old | OSMetaClassDeclareReservedUnused ( IOBlockStorageDevice, 4); |
| New | OSMetaClassDeclareReservedUnused ( IOBlockStorageDevice, 0); |

IOBlockStorageDriver.hAdded IOBlockStorageDriver::isMediaRemovable() (no architecture available)IOBluetoothHCIController.hRemoved IOBluetoothHCIController::BluetoothHCIIOCapabilityResponse()Added IOBluetoothHCIController::BluetoothHCIIOCapabilityRequestReply()Added IOBluetoothHCIController::BluetoothHCIReadLocalExtendedFeatures()Added IOBluetoothHCIController::BluetoothHCIReadRemoteExtendedFeatures()Modified IOBluetoothHCIController::SendRawHCICommand()

|  | Declaration |
| --- | --- |
| Old | virtual IOReturn SendRawHCICommand ( BluetoothHCIRequestID inID, char \*buffer, IOByteCount bufferSize); |
| New | virtual IOReturn SendRawHCICommand ( BluetoothHCIRequestID inID, char \*buffer, UInt32 bufferSize); |

IOBluetoothHCIRequest.hAdded IOBluetoothHCIRequest::StartTimer()Modified IOBluetoothHCIRequest::GetNotificationRefCon()

|  | Declaration |
| --- | --- |
| Old | void \* GetNotificationRefCon ( void); |
| New | mach_vm_address_t GetNotificationRefCon ( void); |

IOBluetoothInternal.hAdded [kBluetoothCompanyIdentiferContinentialAutomotiveSystems](https://developer.apple.com/documentation/kernel/bluetoothcompanyidentifers/kbluetoothcompanyidentifercontinentialautomotivesystems)IOCDBlockStorageDevice.hModified IOCDBlockStorageDevice::OSMetaClassDeclareReservedUnused()

|  | Declaration |
| --- | --- |
| Old | OSMetaClassDeclareReservedUnused ( IOCDBlockStorageDevice, 5); |
| New | OSMetaClassDeclareReservedUnused ( IOCDBlockStorageDevice, 0); |

IOCDBlockStorageDriver.hAdded completion (no architecture available)Modified IOCDBlockStorageDriver::OSMetaClassDeclareReservedUnused()

|  | Declaration |
| --- | --- |
| Old | OSMetaClassDeclareReservedUnused ( IOCDBlockStorageDriver, 6); |
| New | OSMetaClassDeclareReservedUnused ( IOCDBlockStorageDriver, 0); |

IOCDMedia.hModified IOCDMedia::write()

|  | Declaration |
| --- | --- |
| Old | virtual void write ( IOService \*client, UInt64 byteStart, IOMemoryDescriptor \*buffer, IOStorageCompletion completion); |
| New | virtual void write ( IOService \*client, UInt64 byteStart, IOMemoryDescriptor \*buffer, IOStorageAttributes \*attributes, IOStorageCompletion \*completion); |

Modified IOCDMedia::OSMetaClassDeclareReservedUnused()

|  | Declaration |
| --- | --- |
| Old | OSMetaClassDeclareReservedUnused ( IOCDMedia, 7); |
| New | OSMetaClassDeclareReservedUnused ( IOCDMedia, 0); |

Modified IOCDMedia::readCD()

|  | Declaration |
| --- | --- |
| Old | virtual void readCD ( IOService \*client, UInt64 byteStart, IOMemoryDescriptor \*buffer, CDSectorArea sectorArea, CDSectorType sectorType, IOStorageCompletion completion); |
| New | virtual void readCD ( IOService \*client, UInt64 byteStart, IOMemoryDescriptor \*buffer, CDSectorArea sectorArea, CDSectorType sectorType, IOStorageAttributes \*attributes, IOStorageCompletion \*completion); |

Modified IOCDMedia::writeCD()

|  | Declaration |
| --- | --- |
| Old | virtual void writeCD ( IOService \*client, UInt64 byteStart, IOMemoryDescriptor \*buffer, CDSectorArea sectorArea, CDSectorType sectorType, IOStorageCompletion completion); |
| New | virtual void writeCD ( IOService \*client, UInt64 byteStart, IOMemoryDescriptor \*buffer, CDSectorArea sectorArea, CDSectorType sectorType, IOStorageAttributes \*attributes, IOStorageCompletion \*completion); |

Modified IOCDMedia::read()

|  | Declaration |
| --- | --- |
| Old | virtual void read ( IOService \*client, UInt64 byteStart, IOMemoryDescriptor \*buffer, IOStorageCompletion completion); |
| New | virtual void read ( IOService \*client, UInt64 byteStart, IOMemoryDescriptor \*buffer, IOStorageAttributes \*attributes, IOStorageCompletion \*completion); |

IOCDMediaBSDClient.hModified IOCDMediaBSDClient::ioctl()

|  | Declaration |
| --- | --- |
| Old | virtual int ioctl ( dev_t, u_long cmd, caddr_t data, int, proc_t); |
| New | virtual int ioctl ( dev_t dev, u_long cmd, caddr_t data, int flags, proc_t proc); |

IOCDPartitionScheme.hModified IOCDPartitionScheme::write()

|  | Declaration |
| --- | --- |
| Old | virtual void write ( IOService \*client, UInt64 byteStart, IOMemoryDescriptor \*buffer, IOStorageCompletion completion); |
| New | virtual void write ( IOService \*client, UInt64 byteStart, IOMemoryDescriptor \*buffer, IOStorageAttributes \*attributes, IOStorageCompletion \*completion); |

Modified IOCDPartitionScheme::read()

|  | Declaration |
| --- | --- |
| Old | virtual void read ( IOService \*client, UInt64 byteStart, IOMemoryDescriptor \*buffer, IOStorageCompletion completion); |
| New | virtual void read ( IOService \*client, UInt64 byteStart, IOMemoryDescriptor \*buffer, IOStorageAttributes \*attributes, IOStorageCompletion \*completion); |

IOCatalogue.hRemoved IOKitRelocStartRemoved IOKitRelocStopIOCompactDiscServices.hAdded IOCompactDiscServices::getWriteCacheState() (no architecture available)Added IOCompactDiscServices::setWriteCacheState() (no architecture available)IODMAEventSource.hModified IODMAEventSource::stopDMACommand()

|  | Declaration |
| --- | --- |
| Old | virtual IOReturn stopDMACommand ( bool flush=false, mach_timespec_t \*timeout=0); |
| New | virtual IOReturn stopDMACommand ( bool flush=false, uint64_t timeout=18446744073709551615ULL); |

IODVDBlockStorageDevice.hModified IODVDBlockStorageDevice::OSMetaClassDeclareReservedUnused()

|  | Declaration |
| --- | --- |
| Old | OSMetaClassDeclareReservedUnused ( IODVDBlockStorageDevice, 1); |
| New | OSMetaClassDeclareReservedUnused ( IODVDBlockStorageDevice, 0); |

IODVDBlockStorageDriver.hModified IODVDBlockStorageDriver::OSMetaClassDeclareReservedUnused()

|  | Declaration |
| --- | --- |
| Old | OSMetaClassDeclareReservedUnused ( IODVDBlockStorageDriver, 1); |
| New | OSMetaClassDeclareReservedUnused ( IODVDBlockStorageDriver, 0); |

IODVDMedia.hModified IODVDMedia::OSMetaClassDeclareReservedUnused()

|  | Declaration |
| --- | --- |
| Old | OSMetaClassDeclareReservedUnused ( IODVDMedia, 7); |
| New | OSMetaClassDeclareReservedUnused ( IODVDMedia, 0); |

IODVDMediaBSDClient.hModified IODVDMediaBSDClient::ioctl()

|  | Declaration |
| --- | --- |
| Old | virtual int ioctl ( dev_t, u_long cmd, caddr_t data, int, proc_t); |
| New | virtual int ioctl ( dev_t dev, u_long cmd, caddr_t data, int flags, proc_t proc); |

IODVDServices.hAdded IODVDServices::getWriteCacheState() (no architecture available)Added IODVDServices::setWriteCacheState() (no architecture available)IODVDTypes.hAdded kDVDKeyClassCSS_CPPM_CPRM (no architecture available)Added kDVDKeyFormatAGID_CPRM (no architecture available)Added kDVDKeyFormatAGID_CSS (no architecture available)Added kDVDKeyFormatAGID_CSS2 (no architecture available)Added kDVDKeyFormatASF (no architecture available)Added kDVDKeyFormatChallengeKey (no architecture available)Added kDVDKeyFormatKey1 (no architecture available)Added kDVDKeyFormatKey2 (no architecture available)Added kDVDKeyFormatRegionState (no architecture available)Added kDVDKeyFormatSetRegion (no architecture available)Added kDVDKeyFormatTitleKey (no architecture available)IODisplay.hRemoved IOBacklightDisplay::getAggressiveness()Removed IOBacklightDisplay::setAggressiveness()Modified IODisplayConnect::getAttributeForConnection()

|  | Declaration |
| --- | --- |
| Old | virtual IOReturn getAttributeForConnection ( IOSelect selector, UInt32 \*value); |
| New | virtual IOReturn getAttributeForConnection ( IOSelect selector, uintptr_t \*value); |

Modified IODisplayConnect::setAttributeForConnection()

|  | Declaration |
| --- | --- |
| Old | virtual IOReturn setAttributeForConnection ( IOSelect selector, UInt32 value); |
| New | virtual IOReturn setAttributeForConnection ( IOSelect selector, uintptr_t value); |

IOFDiskPartitionScheme.hAdded IOFDiskPartitionScheme::OSMetaClassDeclareReservedUsed() (no architecture available)Modified IOFDiskPartitionScheme::OSMetaClassDeclareReservedUnused()

|  | Declaration |
| --- | --- |
| Old | OSMetaClassDeclareReservedUnused ( IOFDiskPartitionScheme, 2); |
| New | OSMetaClassDeclareReservedUnused ( IOFDiskPartitionScheme, 0); |

IOFWUserObjectExporter.hAdded [IOFWUserObjectExporter](https://developer.apple.com/documentation/kernel/iofwuserobjectexporter) (no architecture available)Added IOFWUserObjectExporter::addObject() (no architecture available)Added IOFWUserObjectExporter::createWithOwner() (no architecture available)Added IOFWUserObjectExporter::free() (no architecture available)Added IOFWUserObjectExporter::getOwner() (no architecture available)Added IOFWUserObjectExporter::init() (no architecture available)Added IOFWUserObjectExporter::initWithOwner() (no architecture available)Added IOFWUserObjectExporter::lock() (no architecture available)Added IOFWUserObjectExporter::lookupHandle() (no architecture available)Added IOFWUserObjectExporter::lookupObject() (no architecture available)Added IOFWUserObjectExporter::lookupObjectForType() (no architecture available)Added IOFWUserObjectExporter::removeAllObjects() (no architecture available)Added IOFWUserObjectExporter::removeObject() (no architecture available)Added IOFWUserObjectExporter::serialize() (no architecture available)Added IOFWUserObjectExporter::unlock() (no architecture available)Added CleanupFunction (no architecture available)Added CleanupFunctionWithExporter (no architecture available)Added UserObjectHandleIOFWUtils.hAdded [IOFWGetAbsoluteTime()](https://developer.apple.com/documentation/kernel/1589086-iofwgetabsolutetime)IOFireWireBus.hRemoved IOFireWireBus::createBufferFillIsochPort()Removed IOFireWireBusAux::createBufferFillIsochPort()Added IOFireWireBus::getSessionRefExporter()Added IOFireWireBusAux::OSMetaClassDeclareReservedUnused() (no architecture available)Added IOFireWireBusAux::getSessionRefExporter() (no architecture available)Modified IOFireWireBusAux::getMaxRec()

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified IOFireWireBusAux::getFireWirePhysicalAddressMask()

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified IOFireWireBusAux::getFireWirePhysicalBufferMask()

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified IOFireWireBusAux::getFireWirePhysicalAddressBits()

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified IOFireWireBusAux::getFireWirePhysicalBufferBits()

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified IOFireWireBusAux::createSimplePhysicalAddressSpace()

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified IOFireWireBusAux::createSimpleContiguousPhysicalAddressSpace()

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

IOFireWireController.hAdded IOFireWireController::activateMultiIsochReceiveListener()Added IOFireWireController::clientDoneWithMultiIsochReceivePacket()Added IOFireWireController::createMultiIsochReceiveListener()Added IOFireWireController::deactivateMultiIsochReceiveListener()IOFireWireFamilyCommon.hAdded [DCLCompilerDataType](https://developer.apple.com/documentation/iokit/dclcompilerdatatype)Added [kFWIsochRequireLastContext](https://developer.apple.com/documentation/iokit/iofwisochportoptions/kfwisochrequirelastcontext)IOFireWireMultiIsochReceive.hAdded [IOFireWireMultiIsochReceiveListener](https://developer.apple.com/documentation/kernel/iofirewiremultiisochreceivelistener)Added IOFireWireMultiIsochReceiveListener::Activate()Added IOFireWireMultiIsochReceiveListener::Deactivate()Added IOFireWireMultiIsochReceiveListener::IOFireWireMultiIsochReceiveListener()Added IOFireWireMultiIsochReceiveListener::SetCallback()Added IOFireWireMultiIsochReceiveListener::create()Added IOFireWireMultiIsochReceiveListener::getActivatedState()Added IOFireWireMultiIsochReceiveListener::getCallback()Added IOFireWireMultiIsochReceiveListener::getMetaClass()Added IOFireWireMultiIsochReceiveListener::getReceiveChannel()Added IOFireWireMultiIsochReceiveListener::getRefCon()Added IOFireWireMultiIsochReceiveListener::MetaClassAdded IOFireWireMultiIsochReceiveListener::MetaClass::MetaClass()Added IOFireWireMultiIsochReceiveListener::MetaClass::alloc()Added [IOFireWireMultiIsochReceivePacket](https://developer.apple.com/documentation/kernel/iofirewiremultiisochreceivepacket)Added IOFireWireMultiIsochReceivePacket::IOFireWireMultiIsochReceivePacket()Added IOFireWireMultiIsochReceivePacket::clientDone()Added IOFireWireMultiIsochReceivePacket::create()Added IOFireWireMultiIsochReceivePacket::createMemoryDescriptorForRanges()Added IOFireWireMultiIsochReceivePacket::getMetaClass()Added IOFireWireMultiIsochReceivePacket::isochChannel()Added IOFireWireMultiIsochReceivePacket::isochPacketSize()Added IOFireWireMultiIsochReceivePacket::isochPayloadSize()Added IOFireWireMultiIsochReceivePacket::packetReceiveTime()Added IOFireWireMultiIsochReceivePacket::MetaClassAdded IOFireWireMultiIsochReceivePacket::MetaClass::MetaClass()Added IOFireWireMultiIsochReceivePacket::MetaClass::alloc()Added [FWMultiIsochReceiveListenerCallback](https://developer.apple.com/documentation/kernel/fwmultiisochreceivelistenercallback)Added [FWMultiIsochReceiveListenerParams](https://developer.apple.com/documentation/kernel/fwmultiisochreceivelistenerparams)Added IOFireWireLinkAdded IOFireWireMultiIsochReceiveListener::MetaClassAdded IOFireWireMultiIsochReceivePacket::MetaClassAdded elementsAdded #def kMaxRangesPerMultiIsochReceivePacketAdded numClientReferencesAdded numRangesAdded rangesIOFireWireSBP2UserClient.hAdded IOFireWireSBP2UserClient::free()IOFireWireSerialBusProtocolTransport.hRemoved IOFireWireSerialBusProtocolTransport::close() (no architecture available)IOFramebuffer.hAdded IOFramebuffer::getWorkLoop()Modified IOFramebuffer::setAttribute()

|  | Declaration |
| --- | --- |
| Old | virtual IOReturn setAttribute ( IOSelect attribute, UInt32 value); |
| New | virtual IOReturn setAttribute ( IOSelect attribute, uintptr_t value); |

Modified IOFramebuffer::getAttributeForConnection()

|  | Declaration |
| --- | --- |
| Old | virtual IOReturn getAttributeForConnection ( IOIndex connectIndex, IOSelect attribute, UInt32 \*value); |
| New | virtual IOReturn getAttributeForConnection ( IOIndex connectIndex, IOSelect attribute, uintptr_t \*value); |

Modified IOFramebuffer::getAttribute()

|  | Declaration |
| --- | --- |
| Old | virtual IOReturn getAttribute ( IOSelect attribute, UInt32 \*value); |
| New | virtual IOReturn getAttribute ( IOSelect attribute, uintptr_t \*value); |

Modified IOFramebuffer::setAttributeForConnection()

|  | Declaration |
| --- | --- |
| Old | virtual IOReturn setAttributeForConnection ( IOIndex connectIndex, IOSelect attribute, UInt32 value); |
| New | virtual IOReturn setAttributeForConnection ( IOIndex connectIndex, IOSelect attribute, uintptr_t value); |

IOHIDEventService.hAdded IOHIDEventService::OSMetaClassDeclareReservedUsed() (no architecture available)Added IOHIDEventService::copyEvent() (no architecture available)Added IOHIDEventService::open() (no architecture available)IOI2CInterface.hAdded [kIOI2CBusTypeDisplayPort](https://developer.apple.com/documentation/iokit/1410382-anonymous/kioi2cbustypedisplayport)Added [kIOI2CDisplayPortNativeTransactionType](https://developer.apple.com/documentation/iokit/1410366-anonymous/kioi2cdisplayportnativetransactiontype)IOInterleavedMemoryDescriptor.hRemoved IOInterleavedMemoryDescriptor::getPhysicalSegment64()Removed IOInterleavedMemoryDescriptor::getSourceSegment()Modified IOInterleavedMemoryDescriptor::initWithCapacity()

|  | Declaration |
| --- | --- |
| Old | virtual bool initWithCapacity ( UInt32 capacity, IODirection direction); |
| New | virtual bool initWithCapacity ( IOByteCount capacity, IODirection direction); |

Modified IOInterleavedMemoryDescriptor::getPhysicalSegment()

|  | Declaration |
| --- | --- |
| Old | virtual IOPhysicalAddress getPhysicalSegment ( IOByteCount offset, IOByteCount \*length); |
| New | virtual addr64_t getPhysicalSegment ( IOByteCount offset, IOByteCount \*length, IOOptionBits options=0); |

Modified IOInterleavedMemoryDescriptor::withCapacity()

|  | Declaration |
| --- | --- |
| Old | IOInterleavedMemoryDescriptor \* withCapacity ( UInt32 capacity, IODirection direction); |
| New | IOInterleavedMemoryDescriptor \* withCapacity ( IOByteCount capacity, IODirection direction); |

IOInterruptController.hAdded [IOInterruptVectorNumber](https://developer.apple.com/documentation/kernel/iointerruptvectornumber)Modified IOInterruptController::getVectorType()

|  | Declaration |
| --- | --- |
| Old | virtual int getVectorType ( long vectorNumber, IOInterruptVector \*vector); |
| New | virtual int getVectorType ( IOInterruptVectorNumber vectorNumber, IOInterruptVector \*vector); |

Modified IOInterruptController::initVector()

|  | Declaration |
| --- | --- |
| Old | virtual void initVector ( long vectorNumber, IOInterruptVector \*vector); |
| New | virtual void initVector ( IOInterruptVectorNumber vectorNumber, IOInterruptVector \*vector); |

Modified IOInterruptController::vectorCanBeShared()

|  | Declaration |
| --- | --- |
| Old | virtual bool vectorCanBeShared ( long vectorNumber, IOInterruptVector \*vector); |
| New | virtual bool vectorCanBeShared ( IOInterruptVectorNumber vectorNumber, IOInterruptVector \*vector); |

Modified IOInterruptController::disableVectorHard()

|  | Declaration |
| --- | --- |
| Old | virtual void disableVectorHard ( long vectorNumber, IOInterruptVector \*vector); |
| New | virtual void disableVectorHard ( IOInterruptVectorNumber vectorNumber, IOInterruptVector \*vector); |

Modified IOInterruptController::enableVector()

|  | Declaration |
| --- | --- |
| Old | virtual void enableVector ( long vectorNumber, IOInterruptVector \*vector); |
| New | virtual void enableVector ( IOInterruptVectorNumber vectorNumber, IOInterruptVector \*vector); |

Modified IOInterruptController::causeVector()

|  | Declaration |
| --- | --- |
| Old | virtual void causeVector ( long vectorNumber, IOInterruptVector \*vector); |
| New | virtual void causeVector ( IOInterruptVectorNumber vectorNumber, IOInterruptVector \*vector); |

IOKitKeys.hAdded [#def kIOUserClientCreatorKey](https://developer.apple.com/documentation/iokit/kiouserclientcreatorkey)IOLib.hAdded [IOLogv()](https://developer.apple.com/documentation/kernel/1575323-iologv)IOLocks.hAdded [IORecursiveLockSleepDeadline()](https://developer.apple.com/documentation/kernel/1552986-iorecursivelocksleepdeadline)IOMacOSVideo.hAdded #def FOUR_CHAR_CODEAdded #def PRAGMA_STRUCT_ALIGNAdded [kVideoBusTypeDisplayPort](https://developer.apple.com/documentation/kernel/1644552-anonymous/kvideobustypedisplayport)Added [kVideoDisplayPortNativeType](https://developer.apple.com/documentation/iokit/1567416-anonymous/kvideodisplayportnativetype)Added [kVideoDisplayPortNativeTypeMask](https://developer.apple.com/documentation/iokit/1567416-anonymous/kvideodisplayportnativetypemask)IOMedia.hModified IOMedia::OSMetaClassDeclareReservedUnused()

|  | Declaration |
| --- | --- |
| Old | OSMetaClassDeclareReservedUnused ( IOMedia, 2); |
| New | OSMetaClassDeclareReservedUnused ( IOMedia, 0); |

IOMediaBSDClient.hModified IOMediaBSDClient::ioctl()

|  | Declaration |
| --- | --- |
| Old | virtual int ioctl ( dev_t, u_long cmd, caddr_t data, int, proc_t); |
| New | virtual int ioctl ( dev_t dev, u_long cmd, caddr_t data, int flags, proc_t proc); |

Modified IOMediaBSDClient::OSMetaClassDeclareReservedUnused()

|  | Declaration |
| --- | --- |
| Old | OSMetaClassDeclareReservedUnused ( IOMediaBSDClient, 1); |
| New | OSMetaClassDeclareReservedUnused ( IOMediaBSDClient, 0); |

IOMemoryDescriptor.hRemoved IOMemoryDescriptor::OSMetaClassDeclareReservedUsed() (no architecture available)Removed IOSubMemoryDescriptor::getPhysicalSegment64()Removed IOSubMemoryDescriptor::getSourceSegment()Removed IOSubMemoryDescriptor::getVirtualSegment()Removed IOSubMemoryDescriptor::performOperation()Removed IOSubMemoryDescriptor::readBytes()Removed IOSubMemoryDescriptor::redirect()Removed IOSubMemoryDescriptor::serialize()Removed IOSubMemoryDescriptor::writeBytes()Removed IOMemoryDescriptorRemoved IOSubMemoryDescriptorRemoved #def kIOMapperNoneRemoved kIOMemoryDontMapRemoved kIOMemoryPreparedReadOnlyAdded IOMemoryDescriptor::makeMapping()Added IOMemoryMap::IOMemoryMap()Added IOMemoryMap::OSMetaClassDeclareReservedUnused() (no architecture available)Added IODirection (no architecture available)Added IOMemoryMapAdded kIODirectionIn (no architecture available)Added kIODirectionNone (no architecture available)Added kIODirectionOut (no architecture available)Added kIODirectionOutIn (no architecture available)Added [kIOMemoryMapperNone](https://developer.apple.com/documentation/kernel/1643338-anonymous/kiomemorymappernone)Added options (no architecture available)Modified IOMemoryDescriptor::getPhysicalSegment()

|  | Declaration |
| --- | --- |
| Old | virtual IOPhysicalAddress getPhysicalSegment ( IOByteCount offset, IOByteCount \*length); |
| New | virtual addr64_t getPhysicalSegment ( IOByteCount offset, IOByteCount \*length, IOOptionBits options); |

Modified IOMemoryDescriptor::withAddressRanges()

|  | Declaration |
| --- | --- |
| Old | IOMemoryDescriptor \* withAddressRanges ( IOAddressRange \*ranges, UInt32 rangeCount, IOOptionBits options, task_t withTask); |
| New | IOMemoryDescriptor \* withAddressRanges ( IOAddressRange \*ranges, UInt32 rangeCount, IOOptionBits options, task_t task); |

IOMultiMemoryDescriptor.hRemoved IOMultiMemoryDescriptor::getPhysicalSegment64()Removed IOMultiMemoryDescriptor::getSourceSegment()Removed IOMultiMemoryDescriptor::readBytes()Removed IOMultiMemoryDescriptor::writeBytes()Modified IOMultiMemoryDescriptor::getPhysicalSegment()

|  | Declaration |
| --- | --- |
| Old | virtual IOPhysicalAddress getPhysicalSegment ( IOByteCount offset, IOByteCount \*length); |
| New | virtual addr64_t getPhysicalSegment ( IOByteCount offset, IOByteCount \*length, IOOptionBits options=0); |

IONDRVFramebuffer.hModified IONDRVFramebuffer::getAttributeForConnection()

|  | Declaration |
| --- | --- |
| Old | virtual IOReturn getAttributeForConnection ( IOIndex connectIndex, IOSelect attribute, UInt32 \*value); |
| New | virtual IOReturn getAttributeForConnection ( IOIndex connectIndex, IOSelect attribute, uintptr_t \*value); |

Modified IONDRVFramebuffer::getAttribute()

|  | Declaration |
| --- | --- |
| Old | virtual IOReturn getAttribute ( IOSelect attribute, UInt32 \*value); |
| New | virtual IOReturn getAttribute ( IOSelect attribute, uintptr_t \*value); |

Modified IONDRVFramebuffer::setAttribute()

|  | Declaration |
| --- | --- |
| Old | virtual IOReturn setAttribute ( IOSelect attribute, UInt32 value); |
| New | virtual IOReturn setAttribute ( IOSelect attribute, uintptr_t value); |

Modified IONDRVFramebuffer::setAttributeForConnection()

|  | Declaration |
| --- | --- |
| Old | virtual IOReturn setAttributeForConnection ( IOIndex connectIndex, IOSelect attribute, UInt32 info); |
| New | virtual IOReturn setAttributeForConnection ( IOIndex connectIndex, IOSelect attribute, uintptr_t info); |

IONVRAM.hAdded [kOFVariablePermKernelOnly](https://developer.apple.com/documentation/kernel/1645772-anonymous/kofvariablepermkernelonly)IONetworkController.hAdded IONetworkController::systemWillShutdown() (no architecture available)Added [kIONetworkFeatureTSOIPv4](https://developer.apple.com/documentation/kernel/1646638-anonymous/kionetworkfeaturetsoipv4)Added [kIONetworkFeatureTSOIPv6](https://developer.apple.com/documentation/kernel/1646638-anonymous/kionetworkfeaturetsoipv6)IONetworkInterface.hAdded IONetworkInterface::getIfnet() (no architecture available)Added IONetworkInterface::message() (no architecture available)IONetworkMedium.hAdded [kIOMediumEthernet10GBaseCX4](https://developer.apple.com/documentation/iokit/1562954-anonymous/kiomediumethernet10gbasecx4)Added [kIOMediumEthernet10GBaseT](https://developer.apple.com/documentation/iokit/1562954-anonymous/kiomediumethernet10gbaset)IOPCIDevice.hAdded [kIOPCICommandInterruptDisable](https://developer.apple.com/documentation/kernel/1640334-anonymous/kiopcicommandinterruptdisable)IOPM.hRemoved IOPMRegisterDevice() (no architecture available)Added #def kIOPMBatteryChargeStatusGradientAdded #def kIOPMBatteryChargeStatusTooColdAdded #def kIOPMBatteryChargeStatusTooHotAdded #def kIOPMCPUPowerLimitProcessorCountKeyAdded #def kIOPMCPUPowerLimitProcessorSpeedKeyAdded #def kIOPMCPUPowerLimitSchedulerTimeKeyAdded #def kIOPMCPUPowerLimitsKeyAdded #def kIOPMGraphicsPowerLimitPerformanceKeyAdded #def kIOPMGraphicsPowerLimitsKeyAdded #def kIOPMMessageSystemPowerEventOccurredAdded #def kIOPMPSBatteryChargeStatusKeyAdded #def kIOPMSettingGraphicsSwitchKeyAdded #def kIOPMThermalLevelWarningKeyAdded kIOPMThermalWarningLevelCrisisAdded kIOPMThermalWarningLevelDangerAdded kIOPMThermalWarningLevelNormalIOPartitionScheme.hAdded IOPartitionScheme::OSMetaClassDeclareReservedUsed() (no architecture available)Modified IOPartitionScheme::OSMetaClassDeclareReservedUnused()

|  | Declaration |
| --- | --- |
| Old | OSMetaClassDeclareReservedUnused ( IOPartitionScheme, 3); |
| New | OSMetaClassDeclareReservedUnused ( IOPartitionScheme, 0); |

IOPlatformExpert.hModified [PESavePanicInfo()](https://developer.apple.com/documentation/kernel/1451658-pesavepanicinfo)

|  | Declaration |
| --- | --- |
| Old | unsigned long PESavePanicInfo ( unsigned char \*buffer, unsigned long length); |
| New | UInt32 PESavePanicInfo ( UInt8 \*buffer, UInt32 length); |

IOReducedBlockServices.hAdded IOReducedBlockServices::getWriteCacheState() (no architecture available)Added IOReducedBlockServices::setWriteCacheState() (no architecture available)IORegistryEntry.hRemoved IORegistryEntry::OSMetaClassDeclareReservedUsed() (no architecture available)Removed IORegistryEntry::initialize()IOSCSIMultimediaCommandsDevice.hAdded IOSCSIMultimediaCommandsDevice::setAggressiveness() (no architecture available)IOSCSIPrimaryCommandsDevice.hModified IOSCSIPrimaryCommandsDevice::setAggressiveness()

|  | Declaration |
| --- | --- |
| Old | virtual IOReturn setAggressiveness ( UInt32 type, UInt32 minutes); |
| New | virtual IOReturn setAggressiveness ( unsigned long type, unsigned long minutes); |

IOSCSIProtocolInterface.hAdded [SCSIProtocolPowerState](https://developer.apple.com/documentation/kernel/scsiprotocolpowerstate) (no architecture available)Added [kSCSIProtocolFeature_ProtocolSpecificAsyncNotification](https://developer.apple.com/documentation/kernel/1638592-anonymous/kscsiprotocolfeature_protocolspecificasyncnotification) (no architecture available)Added [kSCSIProtocolFeature_ProtocolSpecificPowerControl](https://developer.apple.com/documentation/kernel/1638592-anonymous/kscsiprotocolfeature_protocolspecificpowercontrol) (no architecture available)Added [kSCSIProtocolPowerStateOff](https://developer.apple.com/documentation/kernel/1638586-anonymous/kscsiprotocolpowerstateoff) (no architecture available)Added [kSCSIProtocolPowerStateOn](https://developer.apple.com/documentation/kernel/1638586-anonymous/kscsiprotocolpowerstateon) (no architecture available)Modified IOSCSIProtocolInterface::initialPowerStateForDomainState()

|  | Declaration |
| --- | --- |
| Old | virtual UInt32 initialPowerStateForDomainState ( IOPMPowerFlags flags); |
| New | virtual unsigned long initialPowerStateForDomainState ( IOPMPowerFlags flags); |

Modified IOSCSIProtocolInterface::setPowerState()

|  | Declaration |
| --- | --- |
| Old | virtual IOReturn setPowerState ( UInt32 powerStateOrdinal, IOService \*whichDevice); |
| New | virtual IOReturn setPowerState ( unsigned long powerStateOrdinal, IOService \*whichDevice); |

IOService.hRemoved IOService::PMfree()Removed IOService::ack_timer_ticked()Removed IOService::actionDidTerminate()Removed IOService::actionFinalize()Removed IOService::actionStop()Removed IOService::actionWillTerminate()Removed IOService::catalogNewDrivers()Removed IOService::checkResource()Removed IOService::checkResources()Removed IOService::deliverNotification()Removed IOService::doInstallNotification()Removed IOService::doServiceMatch()Removed IOService::doServiceTerminate()Removed IOService::getCPUSnoopDelay()Removed IOService::getExistingServices()Removed IOService::initialize()Removed IOService::installNotification()Removed IOService::invokeNotifer()Removed IOService::lookupInterrupt()Removed IOService::passiveMatch()Removed IOService::powerDomainDidChangeTo()Removed IOService::powerDomainWillChangeTo()Removed IOService::probeCandidates()Removed IOService::requireMaxBusStall()Removed IOService::resolveInterrupt()Removed IOService::resources()Removed IOService::scheduleFinalize()Removed IOService::scheduleStop()Removed IOService::scheduleTerminatePhase2()Removed IOService::serializedAllowPowerChange2()Removed IOService::serializedCancelPowerChange2()Removed IOService::setCPUSnoopDelay()Removed IOService::setNotification()Removed IOService::setPMRootDomain()Removed IOService::setPlatform()Removed IOService::settleTimerExpired()Removed IOService::startCandidate()Removed IOService::startMatching()Removed IOService::syncNotificationHandler()Removed IOService::tellChangeDown1()Removed IOService::tellChangeDown2()Removed IOService::terminatePhase1()Removed IOService::terminateThread()Removed IOService::terminateWorker()Removed IOService::unregisterAllInterest()Removed IOService::waitForState()Removed IOService::waitMatchIdle()Added IOService::addMatchingNotification()Added IOService::copyClientWithCategory()Added IOService::waitForMatchingService()Added APPLE_KEXT_DEPRECATED (no architecture available)Added [IOServiceMatchingNotificationHandler](https://developer.apple.com/documentation/kernel/ioservicematchingnotificationhandler)Added #def UINT64_MAXModified IOService::waitQuiet()

|  | Declaration |
| --- | --- |
| Old | virtual IOReturn waitQuiet ( mach_timespec_t \*timeout=0); |
| New | virtual IOReturn waitQuiet ( mach_timespec_t \*timeout); |

Modified IOService::setPowerParent()

|  | Declaration |
| --- | --- |
| Old | virtual IOReturn setPowerParent ( IOPowerConnection \*theParent, bool stateKnown, IOPMPowerFlags currentState); |
| New | virtual IOReturn setPowerParent ( IOPowerConnection \*parent, bool stateKnown, IOPMPowerFlags currentState); |

IOServicePM.hRemoved IOPMprotRemoved IOPMprot::IOPMprot()Removed IOPMprot::getMetaClass()Removed IOPMprot::MetaClassRemoved IOPMprot::MetaClass::MetaClass()Removed IOPMprot::MetaClass::alloc()Removed IOPMprot::MetaClassRemoved IOServiceRemoved aggressivenessRemoved current_aggressiveness_validRemoved current_aggressiveness_valuesRemoved myCurrentStateRemoved ourNameRemoved theControllingDriverRemoved theNumberOfPowerStatesRemoved thePlatformRemoved thePowerStatesIOStorage.hModified IOStorage::OSMetaClassDeclareReservedUnused()

|  | Declaration |
| --- | --- |
| Old | OSMetaClassDeclareReservedUnused ( IOStorage, 2); |
| New | OSMetaClassDeclareReservedUnused ( IOStorage, 0); |

IOSubMemoryDescriptor.hAdded IOSubMemoryDescriptor::withSubRange()Modified IOSubMemoryDescriptor::getMetaClass()

|  | Header |
| --- | --- |
| Old | IOMemoryDescriptor.h |
| New | IOSubMemoryDescriptor.h |

Modified IOSubMemoryDescriptor::IOSubMemoryDescriptor()

|  | Header |
| --- | --- |
| Old | IOMemoryDescriptor.h |
| New | IOSubMemoryDescriptor.h |

Modified IOSubMemoryDescriptor::setPurgeable()

|  | Header |
| --- | --- |
| Old | IOMemoryDescriptor.h |
| New | IOSubMemoryDescriptor.h |

Modified IOSubMemoryDescriptor::complete()

|  | Header |
| --- | --- |
| Old | IOMemoryDescriptor.h |
| New | IOSubMemoryDescriptor.h |

Modified IOSubMemoryDescriptor::prepare()

|  | Header |
| --- | --- |
| Old | IOMemoryDescriptor.h |
| New | IOSubMemoryDescriptor.h |

Modified [IOSubMemoryDescriptor](https://developer.apple.com/documentation/kernel/iosubmemorydescriptor)

|  | Header |
| --- | --- |
| Old | IOMemoryDescriptor.h |
| New | IOSubMemoryDescriptor.h |

Modified IOSubMemoryDescriptor::getPhysicalSegment()

|  | Header | Declaration |
| --- | --- | --- |
| Old | IOMemoryDescriptor.h | virtual IOPhysicalAddress getPhysicalSegment ( IOByteCount offset, IOByteCount \*length); |
| New | IOSubMemoryDescriptor.h | virtual addr64_t getPhysicalSegment ( IOByteCount offset, IOByteCount \*length, IOOptionBits options=0); |

Modified IOSubMemoryDescriptor::MetaClass

|  | Header |
| --- | --- |
| Old | IOMemoryDescriptor.h |
| New | IOSubMemoryDescriptor.h |

Modified IOSubMemoryDescriptor::initSubRange()

|  | Header |
| --- | --- |
| Old | IOMemoryDescriptor.h |
| New | IOSubMemoryDescriptor.h |

Modified IOSubMemoryDescriptor::MetaClass::MetaClass()

|  | Header |
| --- | --- |
| Old | IOMemoryDescriptor.h |
| New | IOSubMemoryDescriptor.h |

Modified IOSubMemoryDescriptor::MetaClass::alloc()

|  | Header |
| --- | --- |
| Old | IOMemoryDescriptor.h |
| New | IOSubMemoryDescriptor.h |

Modified IOSubMemoryDescriptor::MetaClass

|  | Header |
| --- | --- |
| Old | IOMemoryDescriptor.h |
| New | IOSubMemoryDescriptor.h |

IOSyncer.hRemoved #def DEPRECATEDIOTimeStamp.hModified [IOTimeStampStartConstant()](https://developer.apple.com/documentation/kernel/1535234-iotimestampstartconstant)

|  | Declaration |
| --- | --- |
| Old | void IOTimeStampStartConstant ( unsigned int csc, unsigned int a=0, unsigned int b=0, unsigned int c=0, unsigned int d=0); |
| New | void IOTimeStampStartConstant ( unsigned int csc, uintptr_t a=0, uintptr_t b=0, uintptr_t c=0, uintptr_t d=0); |

Modified IOTimeStamp()

|  | Declaration |
| --- | --- |
| Old | void IOTimeStamp ( unsigned int csc, unsigned int a=0, unsigned int b=0, unsigned int c=0, unsigned int d=0); |
| New | void IOTimeStamp ( uintptr_t csc, uintptr_t a=0, uintptr_t b=0, uintptr_t c=0, uintptr_t d=0); |

Modified IOTimeStampEnd()

|  | Declaration |
| --- | --- |
| Old | void IOTimeStampEnd ( unsigned int csc, unsigned int a=0, unsigned int b=0, unsigned int c=0, unsigned int d=0); |
| New | void IOTimeStampEnd ( uintptr_t csc, uintptr_t a=0, uintptr_t b=0, uintptr_t c=0, uintptr_t d=0); |

Modified IOTimeStampStart()

|  | Declaration |
| --- | --- |
| Old | void IOTimeStampStart ( unsigned int csc, unsigned int a=0, unsigned int b=0, unsigned int c=0, unsigned int d=0); |
| New | void IOTimeStampStart ( uintptr_t csc, uintptr_t a=0, uintptr_t b=0, uintptr_t c=0, uintptr_t d=0); |

Modified [IOTimeStampConstant()](https://developer.apple.com/documentation/kernel/1535203-iotimestampconstant)

|  | Declaration |
| --- | --- |
| Old | void IOTimeStampConstant ( unsigned int csc, unsigned int a=0, unsigned int b=0, unsigned int c=0, unsigned int d=0); |
| New | void IOTimeStampConstant ( uintptr_t csc, uintptr_t a=0, uintptr_t b=0, uintptr_t c=0, uintptr_t d=0); |

Modified [IOTimeStampEndConstant()](https://developer.apple.com/documentation/kernel/1535232-iotimestampendconstant)

|  | Declaration |
| --- | --- |
| Old | void IOTimeStampEndConstant ( unsigned int csc, unsigned int a=0, unsigned int b=0, unsigned int c=0, unsigned int d=0); |
| New | void IOTimeStampEndConstant ( uintptr_t csc, uintptr_t a=0, uintptr_t b=0, uintptr_t c=0, uintptr_t d=0); |

IOTypes.hRemoved kIOMap64BitAdded [IOByteCount32](https://developer.apple.com/documentation/iokit/iobytecount32)Added [IOByteCount64](https://developer.apple.com/documentation/iokit/iobytecount64)Added [IOPhysicalAddress32](https://developer.apple.com/documentation/kernel/iophysicaladdress32)Added [IOPhysicalAddress64](https://developer.apple.com/documentation/kernel/iophysicaladdress64)Added [IOPhysicalLength32](https://developer.apple.com/documentation/iokit/iophysicallength32)Added [IOPhysicalLength64](https://developer.apple.com/documentation/iokit/iophysicallength64)Modified [IOPhysicalRange](https://developer.apple.com/documentation/kernel/iophysicalrange)

|  | Header |
| --- | --- |
| Old | IOMemoryDescriptor.h |
| New | IOTypes.h |

IOUFIStorageServices.hAdded IOUFIStorageServices::getWriteCacheState() (no architecture available)Added IOUFIStorageServices::setWriteCacheState() (no architecture available)IOUSBController.hAdded IOUSBController::didTerminate()IOUSBDevice.hAdded IOUSBDevice::GetDeviceInformation()Added IOUSBDevice::GetExtraPowerAllocated()Added IOUSBDevice::GetPolicyMaker()Added IOUSBDevice::RequestExtraPower()Added IOUSBDevice::ReturnExtraPower()Added IOUSBDevice::SetPolicyMaker()Modified IOUSBDevice::OSMetaClassDeclareReservedUnused()

|  | Declaration |
| --- | --- |
| Old | OSMetaClassDeclareReservedUnused ( IOUSBDevice, 6); |
| New | OSMetaClassDeclareReservedUnused ( IOUSBDevice, 12); |

IOUSBHIDDriver.hRemoved IOUSBHIDDriver::newReportIntervalNumber()IOUSBHubDevice.hAdded IOUSBHubDevice::GetTotalSleepCurrent()Added IOUSBHubDevice::InitializeExtraPower()Added IOUSBHubDevice::OSMetaClassDeclareReservedUsed() (no architecture available)Added IOUSBHubDevice::RequestSleepPower()Added IOUSBHubDevice::ReturnSleepPower()Added IOUSBHubDevice::SetTotalSleepCurrent()Modified IOUSBHubDevice::OSMetaClassDeclareReservedUnused()

|  | Declaration |
| --- | --- |
| Old | OSMetaClassDeclareReservedUnused ( IOUSBHubDevice, 0); |
| New | OSMetaClassDeclareReservedUnused ( IOUSBHubDevice, 3); |

IOUSBHubPolicyMaker.hAdded IOUSBHubPolicyMaker::GetPortInformation()Added IOUSBHubPolicyMaker::OSMetaClassDeclareReservedUsed() (no architecture available)Added IOUSBHubPolicyMaker::ReEnumeratePort()Added IOUSBHubPolicyMaker::RequestExtraPower()Added IOUSBHubPolicyMaker::ResetPort()Added IOUSBHubPolicyMaker::ReturnExtraPower()Added IOUSBHubPolicyMaker::SuspendPort()Modified IOUSBHubPolicyMaker::OSMetaClassDeclareReservedUnused()

|  | Declaration |
| --- | --- |
| Old | OSMetaClassDeclareReservedUnused ( IOUSBHubPolicyMaker, 0); |
| New | OSMetaClassDeclareReservedUnused ( IOUSBHubPolicyMaker, 6); |

IOUSBMassStorageClass.hAdded kUSBDAddressLengthIOUSBUserClient.hAdded [kUSBDeviceUserClientGetDeviceInformation](https://developer.apple.com/documentation/iokit/1575954-anonymous/kusbdeviceuserclientgetdeviceinformation)Added [kUSBDeviceUserClientGetExtraPowerAllocated](https://developer.apple.com/documentation/kernel/1646283-anonymous/kusbdeviceuserclientgetextrapowerallocated)Added [kUSBDeviceUserClientRequestExtraPower](https://developer.apple.com/documentation/iokit/1575954-anonymous/kusbdeviceuserclientrequestextrapower)Added [kUSBDeviceUserClientReturnExtraPower](https://developer.apple.com/documentation/iokit/1575954-anonymous/kusbdeviceuserclientreturnextrapower)IOUserClient.hRemoved IOUserClient::OSMetaClassDeclareReservedUsed() (no architecture available)Removed IOUserClient::destroyUserReferences()Removed IOUserClient::initialize()Removed IOUserClient::mapClientMemory()Removed IOUserClient::mapClientMemory64()Removed mappingsRemoved sharedInstanceModified IOUserClient::registerNotificationPort()

|  | Declaration |
| --- | --- |
| Old | virtual IOReturn registerNotificationPort ( mach_port_t port, UInt32 type, UInt32 refCon); |
| New | virtual IOReturn registerNotificationPort ( mach_port_t port, UInt32 type, io_user_reference_t refCon); |

IOVideoDevice.hRemoved [IOVideoDevice](https://developer.apple.com/documentation/kernel/iovideodevice)Removed IOVideoDevice::IOVideoDevice()Removed IOVideoDevice::addStream()Removed IOVideoDevice::createStreams()Removed IOVideoDevice::free()Removed IOVideoDevice::getMetaClass()Removed IOVideoDevice::getStream()Removed IOVideoDevice::getStreamCount()Removed IOVideoDevice::releaseStreams()Removed IOVideoDevice::removeStream()Removed IOVideoDevice::setStreamMode()Removed IOVideoDevice::startStream()Removed IOVideoDevice::stopStream()Removed IOVideoDevice::suspendStream()Removed IOVideoDevice::MetaClassRemoved IOVideoDevice::MetaClass::MetaClass()Removed IOVideoDevice::MetaClass::alloc()Removed IOVideoDevice::MetaClassIOVideoDeviceUserClient.hRemoved [IOVideoDeviceUserClient](https://developer.apple.com/documentation/kernel/iovideodeviceuserclient)Removed IOVideoDeviceUserClient::IOVideoDeviceUserClient()Removed IOVideoDeviceUserClient::clientClose()Removed IOVideoDeviceUserClient::clientDied()Removed IOVideoDeviceUserClient::clientMemoryForType() (no architecture available)Removed IOVideoDeviceUserClient::connectClient()Removed IOVideoDeviceUserClient::getMetaClass()Removed IOVideoDeviceUserClient::getService()Removed IOVideoDeviceUserClient::getTargetAndMethodForIndex()Removed IOVideoDeviceUserClient::getTargetAndTrapForIndex() (no architecture available)Removed IOVideoDeviceUserClient::initWithTask()Removed IOVideoDeviceUserClient::registerNotificationPort() (no architecture available)Removed IOVideoDeviceUserClient::setProperties()Removed IOVideoDeviceUserClient::start()Removed IOVideoDeviceUserClient::MetaClassRemoved IOVideoDeviceUserClient::MetaClass::MetaClass()Removed IOVideoDeviceUserClient::MetaClass::alloc()Removed IOVideoDeviceUserClient::MetaClassIOVideoStream.hRemoved [IOVideoStream](https://developer.apple.com/documentation/kernel/iovideostream)Removed IOVideoStream::IOVideoStream()Removed IOVideoStream::getDevice()Removed IOVideoStream::getMetaClass()Removed IOVideoStream::getStreamMode()Removed IOVideoStream::initWithBuffers()Removed IOVideoStream::setStreamMode()Removed IOVideoStream::startStream()Removed IOVideoStream::stopStream()Removed IOVideoStream::suspendStream()Removed IOVideoStream::withBuffers()Removed IOVideoStream::MetaClassRemoved IOVideoStream::MetaClass::MetaClass()Removed IOVideoStream::MetaClass::alloc()Removed IOVideoStream::MetaClassIOWorkLoop.hRemoved IOWorkLoop::OSMetaClassDeclareReservedUsed() (no architecture available)OSAtomic.hAdded [OSCompareAndSwapPtr()](https://developer.apple.com/documentation/kernel/1576461-oscompareandswapptr)OSDebug.hModified [trace_backtrace()](https://developer.apple.com/documentation/kernel/1593369-trace_backtrace)

|  | Declaration |
| --- | --- |
| Old | void trace_backtrace ( unsigned int debugid, unsigned int debugid2, int size, int data); |
| New | void trace_backtrace ( unsigned int debugid, unsigned int debugid2, unsigned long size, unsigned long data); |

OSKext.hAdded OSKextAdded OSKext::OSKext()Added OSKext::clientRelease()Added OSKext::clientRetain()Added OSKext::considerUnloads()Added OSKext::copyPersonalitiesArray()Added OSKext::copyResourceNamed()Added OSKext::copyUUID()Added OSKext::copyUUIDOfKextWithBundleID()Added OSKext::cutoverUnload()Added OSKext::declaresExecutable()Added OSKext::getAutounloadEnabled()Added OSKext::getBundleID()Added OSKext::getCompatibleVersion()Added OSKext::getKernelRequestsEnabled()Added OSKext::getLoadEnabled()Added OSKext::getLoadTag()Added OSKext::getMetaClass()Added OSKext::getMetaClasses()Added OSKext::getPropertyForHostArch()Added OSKext::getUnloadEnabled()Added OSKext::getVersion()Added OSKext::handleRequest()Added OSKext::isCompatibleWithVersion()Added OSKext::isInterface()Added OSKext::isKernelComponent()Added OSKext::isLoadableInSafeBoot()Added OSKext::isLoaded()Added OSKext::isStarted()Added OSKext::kmodDestroyNotify()Added OSKext::kmodStartNotify()Added OSKext::kmodStopNotify()Added OSKext::loadFromMkext()Added OSKext::loadKextWithBundleID()Added OSKext::lookupKextWithAddress()Added OSKext::lookupKextWithBundleID()Added OSKext::lookupKextWithLoadTag()Added OSKext::removeKext()Added OSKext::removeKextWithBundleID()Added OSKext::removePersonalitiesFromCatalog()Added OSKext::removePropertyForHostArch()Added OSKext::reportOSMetaClassInstances()Added OSKext::setAutounloadEnabled()Added OSKext::setKernelRequestsEnabled()Added OSKext::setLinkedExecutable()Added OSKext::setLoadEnabled()Added OSKext::setUnloadEnabled()Added OSKext::MetaClassAdded OSKext::MetaClass::MetaClass()Added OSKext::MetaClass::alloc()Added DebugFlagBasicAdded DebugFlagDetailAdded DebugFlagKextBasicAdded DebugFlagKextDetailAdded DebugFlagLoadBasicAdded DebugFlagLoadDetailAdded IOCatalogue (no architecture available)Added IOPMrootDomain (no architecture available)Added KLDBootstrap (no architecture available)Added OSKext::MetaClassAdded OSKextExcludeLevelAdded OSMetaClass (no architecture available)Added #def kOSKextExcludeAllAdded #def kOSKextExcludeKextAdded #def kOSKextExcludeNoneAdded osdata_kmem_free()Added osdata_phys_free()Added osdata_vm_deallocate()OSMetaClass.hAdded OSMetaClassBase::initialize()Added #def APPLE_KEXT_COMPATIBILITY_VIRTUALAdded #def APPLE_KEXT_DEPRECATEDAdded #def APPLE_KEXT_LEGACY_ABIAdded OSKextModified OSMetaClass::preModLoad()

|  | Declaration |
| --- | --- |
| Old | void \* preModLoad ( const char \*kmodName); |
| New | void \* preModLoad ( const char \*kextID); |

Modified OSMetaClass::modHasInstance()

|  | Declaration |
| --- | --- |
| Old | bool modHasInstance ( const char \*kmodName); |
| New | bool modHasInstance ( const char \*kextID); |

Modified OSMetaClass::reportModInstances()

|  | Declaration |
| --- | --- |
| Old | void reportModInstances ( const char \*kmodName); |
| New | void reportModInstances ( const char \*kextID); |

OSReturn.hAdded [#def kOSMetaClassNoKext](https://developer.apple.com/documentation/kernel/kosmetaclassnokext)OSTypes.hAdded #def OSTYPES_K64_REVRootDomain.hRemoved IOPMrootDomain::unIdleDevice()Removed IOPMrootDomain::youAreRoot()Added IOPMrootDomain::systemPowerEventOccurred()Added #def kIOPMRootDomainPowerStatusKeySCSICmds_MODE_Definitions.hAdded [kModeSenseSBCDeviceSpecific_DPOFUABit](https://developer.apple.com/documentation/iokit/1555554-device_specific_parameter_bitfie/kmodesensesbcdevicespecific_dpofuabit)Added [kModeSenseSBCDeviceSpecific_DPOFUAMask](https://developer.apple.com/documentation/kernel/1645305-anonymous/kmodesensesbcdevicespecific_dpofuamask)USB.hAdded [LowLatencyUserBufferInfoV3](https://developer.apple.com/documentation/iokit/lowlatencyuserbufferinfov3)Added [USBDeviceInformationBits](https://developer.apple.com/documentation/kernel/usbdeviceinformationbits)Added [USBPhysicalAddress32](https://developer.apple.com/documentation/kernel/usbphysicaladdress32)Added [USBPowerRequestTypes](https://developer.apple.com/documentation/kernel/usbpowerrequesttypes)Added #def kAppleCurrentAvailableAdded #def kAppleCurrentExtraAdded #def kAppleCurrentInSleepAdded #def kAppleExtraPowerAggregateAdded #def kAppleExtraPowerPerPortAdded #def kAppleInternalUSBDeviceAdded #def kUSBBusIDAdded [kUSBInformationDeviceIsAttachedToRootHubBit](https://developer.apple.com/documentation/kernel/usbdeviceinformationbits/kusbinformationdeviceisattachedtoroothubbit)Added [kUSBInformationDeviceIsCaptiveBit](https://developer.apple.com/documentation/iokit/usbdeviceinformationbits/kusbinformationdeviceiscaptivebit)Added [kUSBInformationDeviceIsConnectedBit](https://developer.apple.com/documentation/kernel/usbdeviceinformationbits/kusbinformationdeviceisconnectedbit)Added [kUSBInformationDeviceIsEnabledBit](https://developer.apple.com/documentation/kernel/usbdeviceinformationbits/kusbinformationdeviceisenabledbit)Added [kUSBInformationDeviceIsInResetBit](https://developer.apple.com/documentation/kernel/usbdeviceinformationbits/kusbinformationdeviceisinresetbit)Added [kUSBInformationDeviceIsInternalBit](https://developer.apple.com/documentation/iokit/usbdeviceinformationbits/kusbinformationdeviceisinternalbit)Added [kUSBInformationDeviceIsSuspendedBit](https://developer.apple.com/documentation/kernel/usbdeviceinformationbits/kusbinformationdeviceissuspendedbit)Added [kUSBInformationDeviceOvercurrentBit](https://developer.apple.com/documentation/kernel/usbdeviceinformationbits/kusbinformationdeviceovercurrentbit)Added [kUSBInformationDevicePortIsInTestModeBit](https://developer.apple.com/documentation/kernel/usbdeviceinformationbits/kusbinformationdeviceportisintestmodebit)Added [kUSBPowerDuringSleep](https://developer.apple.com/documentation/iokit/usbpowerrequesttypes/kusbpowerduringsleep)Added [kUSBPowerDuringWake](https://developer.apple.com/documentation/iokit/usbpowerrequesttypes/kusbpowerduringwake)Modified #def kAppleExtraPowerInSleep

|  | Header |
| --- | --- |
| Old | IOUSBHubDevice.h |
| New | USB.h |

USBSpec.hAdded [kAppleVendorID](https://developer.apple.com/documentation/iokit/1424851-apple_usb_vendor_id/kapplevendorid)Added [kUSBPersonalHealthcareClass](https://developer.apple.com/documentation/iokit/1424988-device_class_codes/kusbpersonalhealthcareclass)Added [kUSBPersonalHealthcareInterfaceClass](https://developer.apple.com/documentation/iokit/1424756-interface_class/kusbpersonalhealthcareinterfaceclass)_structs.hAdded fp_controlAdded fp_statusAdded i386_exception_stateAdded i386_float_stateAdded i386_thread_stateAdded mcontextAdded mcontext32Added mcontext64Added mmst_regAdded ppc_exception_stateAdded ppc_exception_state64Added ppc_float_stateAdded ppc_thread_stateAdded ppc_thread_state64Added ppc_vector_stateAdded sigcontextAdded sigcontext32Added sigcontext64Added x86_debug_state32Added x86_debug_state64Added x86_exception_state64Added x86_float_state64Added x86_thread_state64Added xmm_regModified [fp_control_t](https://developer.apple.com/documentation/kernel/fp_control_t)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,ppc64,i386,x86_64 |

Modified [fp_status_t](https://developer.apple.com/documentation/kernel/fp_status_t)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,ppc64,i386,x86_64 |

affinity.hRemoved affinity_setRemoved task_affinity_create()Removed task_affinity_deallocate()Removed task_affinity_info()Removed thread_affinity_dup()Removed thread_affinity_get()Removed thread_affinity_is_supported()Removed thread_affinity_set()Removed thread_affinity_terminate()apple80211_ioctl.hAdded #def APPLE80211_IOC_ASSOCIATE_INTERNALattr.hRemoved user_fssearchblockAdded #def ATTR_CMN_RETURNED_ATTRSAdded #def ATTR_VOL_UUIDAdded #def FSOPT_PACK_INVAL_ATTRSAdded user32_fssearchblockAdded user64_fssearchblockboot.hRemoved #def VGA_TEXT_MODERemoved boot_videoAdded #def kBootArgsRevision1_4Added #def kBootArgsRevision1_5buf.hAdded buf_rcred (no architecture available)Added buf_wcred (no architecture available)Modified [buf_bread()](https://developer.apple.com/documentation/kernel/1561851-buf_bread)

|  | Declaration |
| --- | --- |
| Old | errno_t buf_bread ( vnode_t, daddr64_t, int, ucred_t, buf_t \*); |
| New | errno_t buf_bread ( vnode_t, daddr64_t, int, kauth_cred_t, buf_t \*); |

Modified [buf_rcred()](https://developer.apple.com/documentation/kernel/1561836-buf_rcred)

|  | Declaration |
| --- | --- |
| Old | ucred_t buf_rcred ( buf_t); |
| New | kauth_cred_t buf_rcred ( buf_t); |

Modified [buf_wcred()](https://developer.apple.com/documentation/kernel/1561896-buf_wcred)

|  | Declaration |
| --- | --- |
| Old | ucred_t buf_wcred ( buf_t); |
| New | kauth_cred_t buf_wcred ( buf_t); |

Modified [buf_breadn()](https://developer.apple.com/documentation/kernel/1561873-buf_breadn)

|  | Declaration |
| --- | --- |
| Old | errno_t buf_breadn ( vnode_t, daddr64_t, int, daddr64_t \*, int \*, int, ucred_t, buf_t \*); |
| New | errno_t buf_breadn ( vnode_t, daddr64_t, int, daddr64_t \*, int \*, int, kauth_cred_t, buf_t \*); |

Modified [buf_meta_breadn()](https://developer.apple.com/documentation/kernel/1561821-buf_meta_breadn)

|  | Declaration |
| --- | --- |
| Old | errno_t buf_meta_breadn ( vnode_t, daddr64_t, int, daddr64_t \*, int \*, int, ucred_t, buf_t \*); |
| New | errno_t buf_meta_breadn ( vnode_t, daddr64_t, int, daddr64_t \*, int \*, int, kauth_cred_t, buf_t \*); |

Modified [buf_meta_bread()](https://developer.apple.com/documentation/kernel/1561871-buf_meta_bread)

|  | Declaration |
| --- | --- |
| Old | errno_t buf_meta_bread ( vnode_t, daddr64_t, int, ucred_t, buf_t \*); |
| New | errno_t buf_meta_bread ( vnode_t, daddr64_t, int, kauth_cred_t, buf_t \*); |

clock.hRemoved clock_get_calendar_nanotime_nowait() (no architecture available)Added [clock_nsec_t](https://developer.apple.com/documentation/kernel/clock_nsec_t)Added [clock_sec_t](https://developer.apple.com/documentation/kernel/clock_sec_t)Added [clock_usec_t](https://developer.apple.com/documentation/kernel/clock_usec_t)Modified [clock_get_calendar_microtime()](https://developer.apple.com/documentation/kernel/1416691-clock_get_calendar_microtime)

|  | Declaration |
| --- | --- |
| Old | void clock_get_calendar_microtime ( uint32_t \*secs, uint32_t \*microsecs); |
| New | void clock_get_calendar_microtime ( clock_sec_t \*secs, clock_usec_t \*microsecs); |

Modified [clock_get_system_nanotime()](https://developer.apple.com/documentation/kernel/1416671-clock_get_system_nanotime)

|  | Declaration |
| --- | --- |
| Old | void clock_get_system_nanotime ( uint32_t \*secs, uint32_t \*nanosecs); |
| New | void clock_get_system_nanotime ( clock_sec_t \*secs, clock_nsec_t \*nanosecs); |

Modified [clock_get_calendar_nanotime()](https://developer.apple.com/documentation/kernel/1416685-clock_get_calendar_nanotime)

|  | Declaration |
| --- | --- |
| Old | void clock_get_calendar_nanotime ( uint32_t \*secs, uint32_t \*nanosecs); |
| New | void clock_get_calendar_nanotime ( clock_sec_t \*secs, clock_nsec_t \*nanosecs); |

Modified [clock_get_system_microtime()](https://developer.apple.com/documentation/kernel/1416677-clock_get_system_microtime)

|  | Declaration |
| --- | --- |
| Old | void clock_get_system_microtime ( uint32_t \*secs, uint32_t \*microsecs); |
| New | void clock_get_system_microtime ( clock_sec_t \*secs, clock_usec_t \*microsecs); |

conf.hAdded [isdisk()](https://developer.apple.com/documentation/kernel/1457981-isdisk)cpu_data.hModified rtclock_timer_t

|  | Header |
| --- | --- |
| Old | etimer.h |
| New | cpu_data.h |

cpuid.hAdded #def CPUID_EXTFEATURE_RDTSCPAdded #def CPUID_FEATURE_DCAAdded #def CPUID_FEATURE_xAPICdefault_pager_types.hAdded #def SWAP_COMPACT_DISABLEAdded #def SWAP_COMPACT_ENABLEdevfs_proto.hRemoved dev_add_entry()Removed dev_add_name()Removed dev_add_node()Removed dev_dup_plane()Removed dev_findname()Removed dev_free_name()Removed devfs_dntovn()Removed devfs_free_plane()Removed devfs_kernel_mount()Removed devfs_mount()Removed devfs_sinit()Removed devnode_free()devfsdefs.hRemoved DEVFS_DECR_ENTRIES()Removed DEVFS_DECR_MOUNTS()Removed DEVFS_DECR_NODES()Removed DEVFS_DECR_STRINGSPACE()Removed DEVFS_INCR_ENTRIES()Removed DEVFS_INCR_MOUNTS()Removed DEVFS_INCR_NODES()Removed DEVFS_INCR_STRINGSPACE()Removed #def DEVFS_LOCKRemoved #def DEVFS_UNLOCKRemoved #def DEVMAXNAMESIZERemoved #def DEVMAXPATHSIZERemoved DEV_BDEVRemoved DEV_CDEVRemoved DEV_DIRRemoved DEV_SLNKRemoved #def DN_BUSYRemoved #def DN_CREATERemoved #def DN_CREATEWAITRemoved #def DN_DELETERemoved #def M_DEVFSMNTRemoved #def M_DEVFSNAMERemoved #def M_DEVFSNODERemoved #def VTODNRemoved dev_rootRemoved devdirentRemoved devdirent_tRemoved devfs_mutexRemoved devfs_spec_vnodeop_pRemoved devfs_statsRemoved devfs_statsRemoved devfs_vfsopsRemoved devfs_vnodeop_pRemoved devfsmountRemoved devfstype_tRemoved devnodeRemoved devnode_tRemoved devnode_type_tRemoved dn_copy_times()Removed dn_times()disk.hAdded #def DKIOCGETPHYSICALBLOCKSIZEefi.hRemoved EFI_CONFIGURATION_TABLERemoved EFI_HANDLERemoved EFI_RUNTIME_SERVICESRemoved EFI_SYSTEM_TABLEAdded [EFI_CONFIGURATION_TABLE_32](https://developer.apple.com/documentation/kernel/efi_configuration_table_32)Added [EFI_HANDLE32](https://developer.apple.com/documentation/kernel/efi_handle32)Added [EFI_PTR32](https://developer.apple.com/documentation/kernel/efi_ptr32)Added [EFI_RUNTIME_SERVICES_32](https://developer.apple.com/documentation/kernel/efi_runtime_services_32)Added [EFI_SYSTEM_TABLE_32](https://developer.apple.com/documentation/kernel/efi_system_table_32)etimer.hRemoved #def EndOfAllTimeRemoved etimer_intr()Removed etimer_intr_tRemoved etimer_resync_deadlines()Removed etimer_set_deadline()Removed rtclock_tick_intervalRemoved setPop()Removed setTimerReq()event.hAdded #def EVFILT_USERAdded #def EV_DISPATCHAdded #def EV_SET64Added #def EV_TRIGGERAdded #def NOTE_FFANDAdded #def NOTE_FFCOPYAdded #def NOTE_FFCTRLMASKAdded #def NOTE_FFLAGSMASKAdded #def NOTE_FFNOPAdded #def NOTE_FFORAdded #def NOTE_NONEAdded kevent64_sfb_entries.hRemoved fb_init()Removed fb_present()Removed fb_reset()fcntl.hRemoved #def S_IFXATTRAdded #def FFDSYNCAdded #def O_DSYNCAdded [user32_fbootstraptransfer_t](https://developer.apple.com/documentation/kernel/user32_fbootstraptransfer_t)Added [user32_fsignatures_t](https://developer.apple.com/documentation/kernel/user32_fsignatures_t)Modified #def SEEK_CUR

|  | Header |
| --- | --- |
| Old | unistd.h |
| New | fcntl.h |

Modified #def SEEK_SET

|  | Header |
| --- | --- |
| Old | unistd.h |
| New | fcntl.h |

Modified #def SEEK_END

|  | Header |
| --- | --- |
| Old | unistd.h |
| New | fcntl.h |

fdesc.hRemoved fdescnode::LIST_ENTRY()Removed #def FD_DESCRemoved #def FD_DEVFDRemoved #def FD_MAXRemoved #def FD_ROOTRemoved #def FD_STDERRRemoved #def FD_STDINRemoved #def FD_STDOUTRemoved FdescRemoved FdevfdRemoved FlinkRemoved FrootRemoved #def VFSTOFDESCRemoved #def VTOFDESCRemoved fdesc_allocvp()Removed fdesc_badop()Removed fdesc_getattr()Removed fdesc_inactive()Removed fdesc_init()Removed fdesc_ioctl()Removed fdesc_lookup()Removed fdesc_open()Removed fdesc_pathconf()Removed fdesc_read()Removed fdesc_readdir()Removed fdesc_readlink()Removed fdesc_reclaim()Removed fdesc_root()Removed fdesc_select()Removed fdesc_setattr()Removed fdesc_vfsopsRemoved fdesc_vnodeop_pRemoved fdesc_write()Removed fdescmountRemoved fdescnodeRemoved fdntypefifo.hAdded #def fifo_accessAdded [fifo_advlock()](https://developer.apple.com/documentation/kernel/1527464-fifo_advlock)Added #def fifo_blktooffAdded #def fifo_bwriteAdded [fifo_close()](https://developer.apple.com/documentation/kernel/1527475-fifo_close)Added #def fifo_createAdded [fifo_ebadf()](https://developer.apple.com/documentation/kernel/1527462-fifo_ebadf)Added #def fifo_fsyncAdded #def fifo_getattrAdded [fifo_inactive()](https://developer.apple.com/documentation/kernel/1527453-fifo_inactive)Added [fifo_ioctl()](https://developer.apple.com/documentation/kernel/1527448-fifo_ioctl)Added #def fifo_linkAdded [fifo_lookup()](https://developer.apple.com/documentation/kernel/1527441-fifo_lookup)Added #def fifo_mkdirAdded #def fifo_mknodAdded #def fifo_mmapAdded [fifo_open()](https://developer.apple.com/documentation/kernel/1527466-fifo_open)Added [fifo_pathconf()](https://developer.apple.com/documentation/kernel/1527439-fifo_pathconf)Added [fifo_read()](https://developer.apple.com/documentation/kernel/1527437-fifo_read)Added #def fifo_readdirAdded #def fifo_readlinkAdded #def fifo_reclaimAdded #def fifo_removeAdded #def fifo_renameAdded #def fifo_revokeAdded #def fifo_rmdirAdded [fifo_select()](https://developer.apple.com/documentation/kernel/1527454-fifo_select)Added #def fifo_setattrAdded #def fifo_strategyAdded #def fifo_symlinkAdded #def fifo_vallocAdded #def fifo_vfreeAdded [fifo_write()](https://developer.apple.com/documentation/kernel/1527467-fifo_write)file.hAdded [file_vnode_withvid()](https://developer.apple.com/documentation/kernel/1434973-file_vnode_withvid)filedesc.hRemoved #def FD_CHROOTRemoved #def NDEXTENTRemoved #def NDFILERemoved #def OFILESIZERemoved #def UF_CLOSINGRemoved #def UF_EXCLOSERemoved #def UF_RESERVEDRemoved #def UF_RESVWAITRemoved #def UF_VALID_FLAGSRemoved dupfdopen()Removed falloc()Removed fdalloc()Removed fdavail()Removed fdcopy()Removed fdexec()Removed #def fdfileRemoved #def fdflagsRemoved fdfree()Removed fdrelse()Removed ffree()Removed filedeschost_priv.hAdded [kext_request()](https://developer.apple.com/documentation/kernel/1588829-kext_request)Modified [vm_allocate_cpm()](https://developer.apple.com/documentation/kernel/1588863-vm_allocate_cpm)

|  | Declaration |
| --- | --- |
| Old | kern_return_t vm_allocate_cpm ( host_priv_t host_priv, vm_map_t task, vm_address_t \*address, vm_size_t size, boolean_t anywhere); |
| New | kern_return_t vm_allocate_cpm ( host_priv_t host_priv, vm_map_t task, vm_address_t \*address, vm_size_t size, int flags); |

Modified [host_default_memory_manager()](https://developer.apple.com/documentation/kernel/1588899-host_default_memory_manager)

|  | Declaration |
| --- | --- |
| Old | kern_return_t host_default_memory_manager ( host_priv_t host_priv, memory_object_default_t \*default_manager, vm_size_t cluster_size); |
| New | kern_return_t host_default_memory_manager ( host_priv_t host_priv, memory_object_default_t \*default_manager, memory_object_cluster_size_t cluster_size); |

host_special_ports.hAdded #def HOST_AUTOMOUNTD_PORTAdded #def HOST_KEXTD_PORTAdded #def host_get_automountd_portAdded #def host_get_kextd_portAdded #def host_set_automountd_portAdded #def host_set_kextd_portif.hRemoved #def ifc_bufRemoved #def ifc_reqRemoved ifconfRemoved ifmediareqif_media.hAdded #def IFM_10G_CX4Added #def IFM_10G_Tin.hAdded #def IP_BOUND_IFin6.hAdded #def IPV6CTL_MAXDYNROUTESAdded #def IPV6CTL_MAXIFDEFROUTERSAdded #def IPV6CTL_MAXIFPREFIXESAdded #def IPV6CTL_NEIGHBORGCTHRESHin6_var.hAdded kev_in6_addrlifetimein_pcb.hAdded #def INP_BOUND_IFip_fw2.hRemoved #def IPFW_LOADEDRemoved #def IP_FW_PORT_DENY_FLAGRemoved #def IP_FW_PORT_DYNT_FLAGRemoved #def IP_FW_PORT_TEE_FLAGModified ipfw_init()

|  | Architectures |
| --- | --- |
| Old | ppc,i386 |
| New | none? |

Modified ip_fw_chk_t

|  | Architectures |
| --- | --- |
| Old | ppc,i386 |
| New | none? |

Modified ip_fw_args

|  | Architectures |
| --- | --- |
| Old | ppc,i386 |
| New | none? |

Modified fw_one_pass

|  | Architectures |
| --- | --- |
| Old | ppc,i386 |
| New | none? |

Modified fw_enable

|  | Architectures |
| --- | --- |
| Old | ppc,i386 |
| New | none? |

Modified flush_pipe_ptrs()

|  | Architectures |
| --- | --- |
| Old | ppc,i386 |
| New | none? |

Modified ip_fw_ctl_ptr

|  | Architectures |
| --- | --- |
| Old | ppc,i386 |
| New | none? |

Modified ip_fw_ctl_t

|  | Architectures |
| --- | --- |
| Old | ppc,i386 |
| New | none? |

Modified ip_fw_chk_ptr

|  | Architectures |
| --- | --- |
| Old | ppc,i386 |
| New | none? |

ipc.hAdded #def ipc_permModified ipc_perm

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

kauth.hRemoved #def KAUTH_WKG_EVERYBODYRemoved #def KAUTH_WKG_GROUPRemoved #def KAUTH_WKG_NOBODYRemoved #def KAUTH_WKG_NOTRemoved #def KAUTH_WKG_OWNERRemoved cantrace()Removed kauth_acl_evaluate()Removed kauth_acl_inherit()Removed kauth_authorize_fileop_has_listeners()Removed kauth_authorize_generic()Removed kauth_copyinfilesec()Removed kauth_cred_alloc()Removed kauth_cred_assume()Removed kauth_cred_copy_real()Removed kauth_cred_dup()Removed kauth_cred_getgroups()Removed kauth_cred_gid_subset()Removed kauth_cred_init()Removed kauth_cred_setauditinfo()Removed kauth_cred_setgroups()Removed kauth_cred_setresgid()Removed kauth_cred_setresuid()Removed kauth_cred_setsvuidgid()Removed kauth_cred_setuidgid()Removed kauth_cred_supplementary_add()Removed kauth_cred_supplementary_register()Removed kauth_cred_supplementary_remove()Removed kauth_cred_uthread_update()Removed kauth_filesec_acl_setendian()Removed kauth_getrgid()Removed kauth_groups_init()Removed kauth_identity_init()Removed kauth_init()Removed kauth_ntsid_equal()Removed kauth_proc_label_update_execve() (no architecture available)Removed kauth_resolver_init()Removed kauth_wellknown_guid()Added groupmember()kdebug.hRemoved kdbg_trace_data()Removed kdbg_trace_string()Removed start_kern_tracing()Added #def BSD_PROC_EXITAdded #def BSD_PROC_FRCEXITAdded #def DBG_BSD_PROCAdded #def DBG_DRVGRAPHICSAdded #def DBG_IOCTLAdded #def DBG_IOGRAPHICSAdded #def DBG_LAUNCHDAdded #def DBG_PAGEIND_FAULTAdded #def DBG_PAGEINV_FAULTAdded #def DBG_TRACE_INFOModified [kernel_debug1()](https://developer.apple.com/documentation/kernel/1568762-kernel_debug1)

|  | Declaration |
| --- | --- |
| Old | void kernel_debug1 ( unsigned int debugid, unsigned int arg1, unsigned int arg2, unsigned int arg3, unsigned int arg4, unsigned int arg5); |
| New | void kernel_debug1 ( uint32_t debugid, uintptr_t arg1, uintptr_t arg2, uintptr_t arg3, uintptr_t arg4, uintptr_t arg5); |

Modified [kernel_debug()](https://developer.apple.com/documentation/kernel/1568810-kernel_debug)

|  | Declaration |
| --- | --- |
| Old | void kernel_debug ( unsigned int debugid, unsigned int arg1, unsigned int arg2, unsigned int arg3, unsigned int arg4, unsigned int arg5); |
| New | void kernel_debug ( uint32_t debugid, uintptr_t arg1, uintptr_t arg2, uintptr_t arg3, uintptr_t arg4, uintptr_t arg5); |

kern_event.hAdded [#def KEV_IEEE80211_CLASS](https://developer.apple.com/documentation/kernel/kev_ieee80211_class)kern_types.hAdded #def THREAD_NOT_WAITINGkext_alloc.hAdded [kext_alloc()](https://developer.apple.com/documentation/kernel/1577598-kext_alloc)Added [kext_alloc_init()](https://developer.apple.com/documentation/kernel/1577599-kext_alloc_init)Added [kext_free()](https://developer.apple.com/documentation/kernel/1577600-kext_free)kextd_mach.hAdded #def kextd_kernel_request_MSG_COUNTAdded [kextd_ping()](https://developer.apple.com/documentation/kernel/1520989-kextd_ping)Added #def subsystem_to_name_map_kextd_kernel_requestkmod.hAdded #def KMOD_CNTL_CUTOVER_SEND_LINKSTATEAdded #def KMOD_CNTL_CUTOVER_SEND_PLISTAdded [kmod_info_32_v1_t](https://developer.apple.com/documentation/kernel/kmod_info_32_v1_t)Added [kmod_info_64_v1_t](https://developer.apple.com/documentation/kernel/kmod_info_64_v1_t)kpi_interface.hAdded [IFNET_TSO_IPV4](https://developer.apple.com/documentation/kernel/1644631-anonymous/ifnet_tso_ipv4)Added [IFNET_TSO_IPV6](https://developer.apple.com/documentation/kernel/1644631-anonymous/ifnet_tso_ipv6)Added [ifnet_get_tso_mtu()](https://developer.apple.com/documentation/kernel/1524965-ifnet_get_tso_mtu)Added [ifnet_set_tso_mtu()](https://developer.apple.com/documentation/kernel/1525098-ifnet_set_tso_mtu)Modified [ifnet_ioctl()](https://developer.apple.com/documentation/kernel/1525082-ifnet_ioctl)

|  | Declaration |
| --- | --- |
| Old | errno_t ifnet_ioctl ( ifnet_t interface, protocol_family_t protocol, u_int32_t ioctl_code, void \*ioctl_arg); |
| New | errno_t ifnet_ioctl ( ifnet_t interface, protocol_family_t protocol, unsigned long ioctl_code, void \*ioctl_arg); |

kpi_mbuf.hAdded [MBUF_TSO_IPV4](https://developer.apple.com/documentation/kernel/1644521-anonymous/mbuf_tso_ipv4)Added [MBUF_TSO_IPV6](https://developer.apple.com/documentation/kernel/1644521-anonymous/mbuf_tso_ipv6)Added [mbuf_concatenate()](https://developer.apple.com/documentation/kernel/1535716-mbuf_concatenate)Added [mbuf_get_tso_requested()](https://developer.apple.com/documentation/kernel/1535781-mbuf_get_tso_requested)Added [mbuf_tso_request_flags_t](https://developer.apple.com/documentation/kernel/mbuf_tso_request_flags_t)Modified [mbuf_outbound_finalize()](https://developer.apple.com/documentation/kernel/1535731-mbuf_outbound_finalize)

|  | Declaration |
| --- | --- |
| Old | void mbuf_outbound_finalize ( mbuf_t mbuf, u_long protocol_family, size_t protocol_offset); |
| New | void mbuf_outbound_finalize ( mbuf_t mbuf, u_int32_t protocol_family, size_t protocol_offset); |

lapic.hAdded #def CPU_NUMBERAdded #def CPU_NUMBER_FROM_LAPICAdded #def LAPIC_CMCI_INTERRUPTAdded #def LAPIC_CPU_MAP_DUMPAdded #def LAPIC_DEFAULT_INTERRUPT_BASEAdded #def LAPIC_DUMPAdded #def LAPIC_ERROR_INTERRUPTAdded #def LAPIC_FUNC_TABLE_SIZEAdded #def LAPIC_ID_MAXAdded #def LAPIC_INTERPROCESSOR_INTERRUPTAdded #def LAPIC_ISR_IS_SETAdded #def LAPIC_NMI_INTERRUPTAdded #def LAPIC_PERFCNT_INTERRUPTAdded #def LAPIC_READAdded #def LAPIC_READ_OFFSETAdded #def LAPIC_REDUCED_INTERRUPT_BASEAdded #def LAPIC_SPURIOUS_INTERRUPTAdded #def LAPIC_THERMAL_INTERRUPTAdded #def LAPIC_TIMER_INTERRUPTAdded #def LAPIC_VECTORAdded #def LAPIC_WRITEAdded cpu_to_lapicAdded i386_intr_func_tAdded lapic_configure()Added lapic_cpu_map()Added lapic_dump()Added lapic_end_of_interrupt()Added lapic_get_timer()Added lapic_init()Added lapic_interrupt()Added lapic_interrupt_baseAdded lapic_probe()Added lapic_set_intr_func()Added lapic_set_pmi_func()Added lapic_set_thermal_func()Added lapic_set_timer()Added lapic_set_timer_func()Added lapic_shutdown()Added lapic_smm_restore()Added lapic_startAdded lapic_to_cpuAdded ml_get_apicid()Added ml_get_cpuid()Modified divide_by_64

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_DM_SMI

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_TIMER_DIVIDE_4

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_REMOTE_READ

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ID_MASK

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_TIMER_INITIAL_COUNT

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LVT_DS_PENDING

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified lapic_timer_divide_t

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_TIMER_DIVIDE_CONFIG

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_APR_MASK

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_DSS_SELF

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LVT_LINT1

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_TIMER_DIVIDE_1

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_APR

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_SIZE

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_SVR_MASK

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_DFR

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_DS_PENDING

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_DM_FIXED

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ISR_BASE

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_TIMER_CURRENT_COUNT

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified divide_by_2

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LVT_IP_PLRITY_LOW

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LVT_DM_FIXED

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_TIMER_DIVIDE_64

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LDR_SHIFT

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ID_SHIFT

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_TPR

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified divide_by_32

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_SVR_FOCUS_OFF

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_TIMER_DIVIDE_16

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_RR_VALID

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LVT_ERROR

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ERROR_STATUS

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_SVR

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_DM_INIT

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified one_shot

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_DSS_MASK

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ID

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICRD_DEST_SHIFT

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LVT_DM_MASK

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_TIMER_DIVIDE_MASK

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_DM_NMI

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_PPR

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_LEVEL_ASSERT

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LVT_TIMER

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_RR_MASK

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified lapic_timer_count_t

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_PPR_MASK

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICRD

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_DSS_DEST

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LVT_TM_LEVEL

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_TIMER_DIVIDE_32

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_DM_REMOTE

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_TIMER_DIVIDE_8

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_DFR_SHIFT

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_DM_LOGICAL

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LVT_DM_SHIFT

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_VECTOR_MASK

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_DM_LOWEST

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified periodic

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_TPR_MASK

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LVT_THERMAL

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified divide_by_16

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_DFR_FLAT

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LVT_VECTOR_MASK

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LVT_DM_NMI

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_TRIGGER_LEVEL

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LVT_PERFCNT

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_EOI

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LVT_REMOTE_IRR

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_IRR_BASE

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified lapic_timer_mode_t

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_TIMER_DIVIDE_2

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_VERSION

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_DSS_OTHERS

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_VERSION_MASK

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_RR_INVALID

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LVT_LINT0

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_DM_MASK

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_DM_STARTUP

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified divide_by_8

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_DFR_CLUSTER

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LVT_MASKED

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified divide_by_1

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LDR

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_START

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_TIMER_DIVIDE_128

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LVT_PERIODIC

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_DSS_ALL

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_TMR_BASE

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_SVR_ENABLE

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_LVT_DM_EXTINT

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified divide_by_4

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified #def LAPIC_ICR_RR_INPROGRESS

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

Modified divide_by_128

|  | Header |
| --- | --- |
| Old | apic.h |
| New | lapic.h |

libkern.hModified [ulmax()](https://developer.apple.com/documentation/kernel/1441039-ulmax)

|  | Declaration |
| --- | --- |
| Old | u_long ulmax ( u_long a, u_long b); |
| New | u_int32_t ulmax ( u_int32_t a, u_int32_t b); |

Modified [ulmin()](https://developer.apple.com/documentation/kernel/1441043-ulmin)

|  | Declaration |
| --- | --- |
| Old | u_long ulmin ( u_long a, u_long b); |
| New | u_int32_t ulmin ( u_int32_t a, u_int32_t b); |

Modified [random()](https://developer.apple.com/documentation/kernel/1441069-random)

|  | Declaration |
| --- | --- |
| Old | u_long random ( void); |
| New | u_int32_t random ( void); |

loader.hAdded #def MH_PIEAdded #def S_DTRACE_DOFlockf.hRemoved lf_advlock()Removed lf_assert()Removed lf_commit()Removed lf_print() (no architecture available)Removed lf_printlist() (no architecture available)locks.hAdded #def LCK_SLEEP_SPINAdded [lck_mtx_ext_t](https://developer.apple.com/documentation/kernel/lck_mtx_ext_t)mac_framework.hAdded mac_vnode_check_signature() (no architecture available)mac_policy.hAdded mpo_vnode_check_signature_tmach.hRemoved mach_error_string()Removed mach_task_self()mach_port.hAdded [mach_port_get_context()](https://developer.apple.com/documentation/kernel/1578930-mach_port_get_context)Added [mach_port_set_context()](https://developer.apple.com/documentation/kernel/1578733-mach_port_set_context)mach_vm.hAdded [mach_vm_page_info()](https://developer.apple.com/documentation/kernel/1402504-mach_vm_page_info)machine.hAdded #def CPUFAMILY_ARM_XSCALEAdded #def CPU_SUBTYPE_ARM_V5TEJAdded #def CPU_SUBTYPE_ARM_XSCALEmachine_cpu.hRemoved cpu_signal_handler()machine_routines.hRemoved ml_hpet_cfg()Added ml_get_maxintdelay()Added ml_set_maxintdelay()Modified ml_processor_register()

|  | Declaration |
| --- | --- |
| Old | kern_return_t ml_processor_register ( cpu_id_t cpu_id, uint32_t lapic_id, processor_t \*processor, ipi_handler_t \*ipi_handler, boolean_t boot_cpu); |
| New | kern_return_t ml_processor_register ( cpu_id_t cpu_id, uint32_t lapic_id, processor_t \*processor_out, boolean_t boot_cpu, boolean_t start); |

memory_object_control.hModified [memory_object_super_upl_request()](https://developer.apple.com/documentation/kernel/1542245-memory_object_super_upl_request)

|  | Declaration |
| --- | --- |
| Old | kern_return_t memory_object_super_upl_request ( memory_object_control_t memory_control, memory_object_offset_t offset, vm_size_t size, vm_size_t super_size, upl_t \*upl, upl_page_info_array_t page_list, mach_msg_type_number_t \*page_listCnt, integer_t cntrl_flags); |
| New | kern_return_t memory_object_super_upl_request ( memory_object_control_t memory_control, memory_object_offset_t offset, upl_size_t size, upl_size_t super_size, upl_t \*upl, upl_page_info_array_t page_list, mach_msg_type_number_t \*page_listCnt, integer_t cntrl_flags); |

Modified [memory_object_upl_request()](https://developer.apple.com/documentation/kernel/1542352-memory_object_upl_request)

|  | Declaration |
| --- | --- |
| Old | kern_return_t memory_object_upl_request ( memory_object_control_t memory_control, memory_object_offset_t offset, vm_size_t size, upl_t \*upl, upl_page_info_array_t page_list, mach_msg_type_number_t \*page_listCnt, integer_t cntrl_flags); |
| New | kern_return_t memory_object_upl_request ( memory_object_control_t memory_control, memory_object_offset_t offset, upl_size_t size, upl_t \*upl, upl_page_info_array_t page_list, mach_msg_type_number_t \*page_listCnt, integer_t cntrl_flags); |

memory_object_server.hRemoved memory_object_unmap()Added memory_object_last_unmap()Added memory_object_map()Modified memory_object_data_unlock()

|  | Declaration |
| --- | --- |
| Old | kern_return_t memory_object_data_unlock ( memory_object_t memory_object, memory_object_offset_t offset, memory_object_cluster_size_t size, vm_prot_t desired_access); |
| New | kern_return_t memory_object_data_unlock ( memory_object_t memory_object, memory_object_offset_t offset, memory_object_size_t size, vm_prot_t desired_access); |

memory_object_types.hAdded #def MEMORY_OBJECT_DATA_FLUSH_ALLAdded [vm_object_id_t](https://developer.apple.com/documentation/kernel/vm_object_id_t)message.hAdded #def MACH_RCV_TRAILER_CTXAdded [mach_msg_context_trailer_t](https://developer.apple.com/documentation/kernel/mach_msg_context_trailer_t)mkext.hRemoved #def MKEXT_EXTNRemoved #def MKEXT_MAGICRemoved #def MKEXT_SIGNRemoved compress_lzss()Removed decompress_lzss()Removed mkext_fileRemoved mkext_headerRemoved mkext_kextmman.hRemoved pshm_cache_init()Removed pshm_lock_init()Removed pshm_mmap()Removed pshm_stat()Removed pshm_truncate()mount.hRemoved VFS_FHTOVP()Removed VFS_GETATTR()Removed VFS_MOUNT()Removed VFS_QUOTACTL()Removed VFS_ROOT()Removed VFS_SETATTR()Removed VFS_START()Removed VFS_SYNC()Removed VFS_UNMOUNT()Removed VFS_VGET()Removed VFS_VPTOFH()Removed user_vfsconfRemoved vfs_extendedsecurity()Removed [vfs_getattr()](https://developer.apple.com/documentation/kernel/mount.h/1809041-vfs_getattr)Removed vfs_getvfs_by_mntonname()Removed vfs_markdependency()Removed [vfs_setattr()](https://developer.apple.com/documentation/kernel/mount.h/1809073-vfs_setattr)Added #def MNT_DWAITAdded #def VFSATTR_f_uuidAdded user32_vfsidctlAdded [vfs_init_io_attributes()](https://developer.apple.com/documentation/kernel/1523109-vfs_init_io_attributes)mp_desc.hRemoved cpu_desc_init64()Removed cpu_desc_load64()Added cpu_desc_load()Modified cpu_desc_init()

|  | Declaration |
| --- | --- |
| Old | void cpu_desc_init ( cpu_data_t \*cdp, boolean_t is_boot_cpu); |
| New | void cpu_desc_init ( cpu_data_t \*cdp, boolean_t is_boot_cpu, boolean_t use64bit); |

msg.hAdded [user32_msglen_t](https://developer.apple.com/documentation/kernel/user32_msglen_t)Added [user32_msgqnum_t](https://developer.apple.com/documentation/kernel/user32_msgqnum_t)Added user32_msqid_dsAdded [user64_msglen_t](https://developer.apple.com/documentation/kernel/user64_msglen_t)Added [user64_msgqnum_t](https://developer.apple.com/documentation/kernel/user64_msgqnum_t)Added user64_msqid_dsnd6.hRemoved #def ND6_IS_LLINFO_PROBREACHAdded #def ND6_LLINFO_PURGEpage_decrypt.hRemoved dsmos_page_transform()Removed dsmos_page_transform_hook()Removed dsmos_page_transform_hook_tpexpert.hAdded PE_get_security_epoch() (no architecture available)Added [PE_i_can_has_debugger()](https://developer.apple.com/documentation/kernel/1553651-pe_i_can_has_debugger) (no architecture available)pio.hModified [outl()](https://developer.apple.com/documentation/kernel/1537078-outl)

|  | Declaration |
| --- | --- |
| Old | void outl ( i386_ioport_t port, unsigned long datum); |
| New | void outl ( i386_ioport_t port, unsigned int datum); |

Modified [inl()](https://developer.apple.com/documentation/kernel/1537081-inl)

|  | Declaration |
| --- | --- |
| Old | unsigned long inl ( i386_ioport_t port); |
| New | unsigned int inl ( i386_ioport_t port); |

pipe.hRemoved pipe::TAILQ_HEAD() (no architecture available)Removed #def BIG_PIPE_SIZERemoved #def PIPENPAGESRemoved #def PIPE_ASYNCRemoved #def PIPE_DIRECTOKRemoved #def PIPE_DIRECTWRemoved #def PIPE_EOFRemoved #def PIPE_KNOTERemoved #def PIPE_LOCKRemoved #def PIPE_LOCKFLRemoved #def PIPE_LOCK_ASSERTRemoved #def PIPE_LWANTRemoved #def PIPE_MINDIRECTRemoved #def PIPE_MTXRemoved #def PIPE_SELRemoved #def PIPE_SIZERemoved #def PIPE_UNLOCKRemoved #def PIPE_WANTRemoved #def PIPE_WANTRRemoved #def PIPE_WANTWRemoved #def SMALL_PIPE_SIZERemoved pipeRemoved pipe_stat()Removed pipebufRemoved pipeinit()Removed pipemapping (no architecture available)port.hAdded #def CAST_MACH_NAME_TO_PORTAdded #def CAST_MACH_PORT_TO_NAMEAdded #def MACH_PORT_QLIMIT_KERNELAdded #def PORT_DEADAdded #def PORT_NULLAdded #def PORT_VALIDModified [port_name_t](https://developer.apple.com/documentation/kernel/port_name_t)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,ppc64,i386,x86_64 |

Modified [port_t](https://developer.apple.com/documentation/kernel/port_t)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,ppc64,i386,x86_64 |

Modified [port_name_array_t](https://developer.apple.com/documentation/kernel/port_name_array_t)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,ppc64,i386,x86_64 |

proc.hRemoved bsd_set_dependency_capable()Removed extern_proc (no architecture available)Removed proc_pendingsignals()Removed proc_thread()Removed unsleep()proc_reg.hAdded #def MSR_IA32_BIOS_SIGN_IDAdded [lgdt()](https://developer.apple.com/documentation/kernel/1571393-lgdt)Added [lidt()](https://developer.apple.com/documentation/kernel/1571272-lidt)Added [rdtscp64()](https://developer.apple.com/documentation/kernel/1571355-rdtscp64)Added [swapgs()](https://developer.apple.com/documentation/kernel/1571202-swapgs)Modified [set_cr4()](https://developer.apple.com/documentation/kernel/1571345-set_cr4)

|  | Declaration |
| --- | --- |
| Old | void set_cr4 ( uint32_t value); |
| New | void set_cr4 ( uintptr_t value); |

Modified set_cr3()

|  | Declaration |
| --- | --- |
| Old | void set_cr3 ( unsigned int value); |
| New | void set_cr3 ( uintptr_t value); |

Modified get_cr3()

|  | Declaration |
| --- | --- |
| Old | unsigned int get_cr3 ( void); |
| New | uintptr_t get_cr3 ( void); |

Modified [set_cr0()](https://developer.apple.com/documentation/kernel/1571254-set_cr0)

|  | Declaration |
| --- | --- |
| Old | void set_cr0 ( unsigned int value); |
| New | void set_cr0 ( uintptr_t value); |

Modified [get_cr2()](https://developer.apple.com/documentation/kernel/1571176-get_cr2)

|  | Declaration |
| --- | --- |
| Old | unsigned int get_cr2 ( void); |
| New | uintptr_t get_cr2 ( void); |

Modified [invlpg()](https://developer.apple.com/documentation/kernel/1571259-invlpg)

|  | Declaration |
| --- | --- |
| Old | void invlpg ( unsigned long addr); |
| New | void invlpg ( uintptr_t addr); |

Modified [get_cr0()](https://developer.apple.com/documentation/kernel/1571251-get_cr0)

|  | Declaration |
| --- | --- |
| Old | unsigned int get_cr0 ( void); |
| New | uintptr_t get_cr0 ( void); |

Modified [get_cr4()](https://developer.apple.com/documentation/kernel/1571378-get_cr4)

|  | Declaration |
| --- | --- |
| Old | uint32_t get_cr4 ( void); |
| New | uintptr_t get_cr4 ( void); |

queue.hModified [remque()](https://developer.apple.com/documentation/kernel/1567112-remque)

|  | Declaration |
| --- | --- |
| Old | integer_t remque ( register queue_entry_t elt); |
| New | void remque ( register queue_entry_t elt); |

quota.hRemoved #def GRPQUOTARemoved #def INITQFNAMESRemoved #def INITQMAGICSRemoved #def MAXQUOTASRemoved #def MAX_DQ_TIMERemoved #def MAX_IQ_TIMERemoved #def QCMDRemoved #def QF_GROUPS_PER_GBRemoved #def QF_MAX_GROUPSRemoved #def QF_MAX_USERSRemoved #def QF_MIN_GROUPSRemoved #def QF_MIN_USERSRemoved #def QF_STRING_TAGRemoved #def QF_USERS_PER_GBRemoved #def QF_VERSIONRemoved #def QUOTAFILENAMERemoved #def QUOTAGROUPRemoved #def QUOTAOPSNAMERemoved #def Q_GETQUOTARemoved #def Q_QUOTAOFFRemoved #def Q_QUOTAONRemoved #def Q_QUOTASTATRemoved #def Q_SETQUOTARemoved #def Q_SETUSERemoved #def Q_SYNCRemoved #def SUBCMDMASKRemoved #def SUBCMDSHIFTRemoved #def USRQUOTARemoved dqblkRemoved dqfilehdrRemoved #def dqhash1Removed #def dqhash2Removed dqhashshift()Removed #def dqoffsetraw_ip6.hRemoved rip6statresource.hRemoved user_rusageRemoved user_rusage_timevalAdded user32_rusageAdded user64_rusageresourcevar.hRemoved #def ADDUPROFRemoved addupc_intr()Removed addupc_task()Removed calcru()Removed plimitRemoved proc_limitblock()Removed proc_limitdrop()Removed proc_limitfork()Removed proc_limitget()Removed proc_limitreplace()Removed proc_limitunblock()Removed #def pstat_endzeroRemoved #def pstat_startzeroRemoved pstatsRemoved pstats::uprofRemoved pstats::user_uprofRemoved ruadd()route.hRemoved #def RTF_TRACKREFSRemoved ortentryAdded #def RTF_CONDEMNEDAdded #def RTF_IFSCOPErtclock.hAdded #def RTC_NANOTIME_READ_FASTAdded rtc_nanotime_infoAdded tsc_rebase_abs_timeModified #def SLOW_TSC_THRESHOLD

|  | Header |
| --- | --- |
| Old | cpu_data.h |
| New | rtclock.h |

Modified rtc_nanotime_t

|  | Header |
| --- | --- |
| Old | cpu_data.h |
| New | rtclock.h |

seg.hRemoved #def KERNEL_CSRemoved kernel_ldt_desc64Removed kernel_tss_desc64Added #def KERNEL32_CSAdded #def MAKE_REAL_DESCRIPTORAdded #def PROT_MODE_GDT_SIZEselect.hAdded [selwait](https://developer.apple.com/documentation/kernel/selwait)semaphore.hRemoved #def SEM_FAILEDRemoved #def SEM_VALUE_MAXRemoved psem_cache_init()Removed psem_lock_init()Removed sem_tsha1.hAdded SHA1UpdateUsePhysicalAddress()shared_region.hAdded #def SHARED_REGION_BASEAdded #def SHARED_REGION_NESTING_BASEAdded #def SHARED_REGION_NESTING_MAXAdded #def SHARED_REGION_NESTING_MINAdded #def SHARED_REGION_NESTING_SIZEAdded #def SHARED_REGION_SIZEsocket.hAdded #def SO_UPCALLCLOSEWAITAdded user32_msghdrAdded user32_sf_hdtrAdded user64_msghdrAdded user64_sf_hdtrsockio.hRemoved #def SIOCGIFCONFstat.hRemoved #def S_ISXATTRRemoved munge_stat()Removed munge_stat64()Removed user_statRemoved user_stat64stdlib.hRemoved bsearch()Removed free()Removed free_all()Removed kld_basefile_nameRemoved malloc()Removed malloc_reset()Removed qsort()Removed realloc()Removed strrchr()Removed strstr()syscall.hAdded #def SYS_ATPgetreqAdded #def SYS_ATPgetrspAdded #def SYS_ATPsndreqAdded #def SYS_ATPsndrspAdded #def SYS_ATgetmsgAdded #def SYS_ATputmsgAdded #def SYS_ATsocketAdded #def SYS_MAXSYSCALLAdded #def SYS___disable_threadsignalAdded #def SYS___mac_execveAdded #def SYS___mac_get_fdAdded #def SYS___mac_get_fileAdded #def SYS___mac_get_lcidAdded #def SYS___mac_get_lctxAdded #def SYS___mac_get_linkAdded #def SYS___mac_get_mountAdded #def SYS___mac_get_pidAdded #def SYS___mac_get_procAdded #def SYS___mac_getfsstatAdded #def SYS___mac_mountAdded #def SYS___mac_set_fdAdded #def SYS___mac_set_fileAdded #def SYS___mac_set_lctxAdded #def SYS___mac_set_linkAdded #def SYS___mac_set_procAdded #def SYS___mac_syscallAdded #def SYS___pthread_canceledAdded #def SYS___pthread_chdirAdded #def SYS___pthread_cond_broadcastAdded #def SYS___pthread_cond_destroyAdded #def SYS___pthread_cond_initAdded #def SYS___pthread_cond_signalAdded #def SYS___pthread_cond_timedwaitAdded #def SYS___pthread_cond_waitAdded #def SYS___pthread_fchdirAdded #def SYS___pthread_killAdded #def SYS___pthread_markcancelAdded #def SYS___pthread_mutex_destroyAdded #def SYS___pthread_mutex_initAdded #def SYS___pthread_mutex_lockAdded #def SYS___pthread_mutex_trylockAdded #def SYS___pthread_mutex_unlockAdded #def SYS___pthread_sigmaskAdded #def SYS___semwait_signalAdded #def SYS___semwait_signal_nocancelAdded #def SYS___sigwaitAdded #def SYS___sigwait_nocancelAdded #def SYS___sysctlAdded #def SYS_acceptAdded #def SYS_accept_nocancelAdded #def SYS_accessAdded #def SYS_access_extendedAdded #def SYS_acctAdded #def SYS_add_profilAdded #def SYS_adjtimeAdded #def SYS_aio_cancelAdded #def SYS_aio_errorAdded #def SYS_aio_fsyncAdded #def SYS_aio_readAdded #def SYS_aio_returnAdded #def SYS_aio_suspendAdded #def SYS_aio_suspend_nocancelAdded #def SYS_aio_writeAdded #def SYS_auditAdded #def SYS_auditctlAdded #def SYS_auditonAdded #def SYS_bindAdded #def SYS_bsdthread_createAdded #def SYS_bsdthread_registerAdded #def SYS_bsdthread_terminateAdded #def SYS_chdirAdded #def SYS_chflagsAdded #def SYS_chmodAdded #def SYS_chmod_extendedAdded #def SYS_chownAdded #def SYS_chrootAdded #def SYS_chudAdded #def SYS_closeAdded #def SYS_close_nocancelAdded #def SYS_connectAdded #def SYS_connect_nocancelAdded #def SYS_copyfileAdded #def SYS_csopsAdded #def SYS_deleteAdded #def SYS_dupAdded #def SYS_dup2Added #def SYS_exchangedataAdded #def SYS_execveAdded #def SYS_exitAdded #def SYS_fchdirAdded #def SYS_fchflagsAdded #def SYS_fchmodAdded #def SYS_fchmod_extendedAdded #def SYS_fchownAdded #def SYS_fcntlAdded #def SYS_fcntl_nocancelAdded #def SYS_fdatasyncAdded #def SYS_ffsctlAdded #def SYS_fgetattrlistAdded #def SYS_fgetxattrAdded #def SYS_fhopenAdded #def SYS_flistxattrAdded #def SYS_flockAdded #def SYS_forkAdded #def SYS_fpathconfAdded #def SYS_fremovexattrAdded #def SYS_fsctlAdded #def SYS_fsetattrlistAdded #def SYS_fsetxattrAdded #def SYS_fsgetpathAdded #def SYS_fstatAdded #def SYS_fstat64Added #def SYS_fstat64_extendedAdded #def SYS_fstat_extendedAdded #def SYS_fstatfsAdded #def SYS_fstatfs64Added #def SYS_fstatvAdded #def SYS_fsyncAdded #def SYS_fsync_nocancelAdded #def SYS_ftruncateAdded #def SYS_futimesAdded #def SYS_getattrlistAdded #def SYS_getauditAdded #def SYS_getaudit_addrAdded #def SYS_getauidAdded #def SYS_getdirentriesAdded #def SYS_getdirentries64Added #def SYS_getdirentriesattrAdded #def SYS_getdtablesizeAdded #def SYS_getegidAdded #def SYS_geteuidAdded #def SYS_getfhAdded #def SYS_getfsstatAdded #def SYS_getfsstat64Added #def SYS_getgidAdded #def SYS_getgroupsAdded #def SYS_gethostuuidAdded #def SYS_getitimerAdded #def SYS_getlcidAdded #def SYS_getloginAdded #def SYS_getpeernameAdded #def SYS_getpgidAdded #def SYS_getpgrpAdded #def SYS_getpidAdded #def SYS_getppidAdded #def SYS_getpriorityAdded #def SYS_getrlimitAdded #def SYS_getrusageAdded #def SYS_getsgroupsAdded #def SYS_getsidAdded #def SYS_getsocknameAdded #def SYS_getsockoptAdded #def SYS_gettidAdded #def SYS_gettimeofdayAdded #def SYS_getuidAdded #def SYS_getwgroupsAdded #def SYS_getxattrAdded #def SYS_identitysvcAdded #def SYS_initgroupsAdded #def SYS_ioctlAdded #def SYS_iopolicysysAdded #def SYS_issetugidAdded #def SYS_kdebug_traceAdded #def SYS_keventAdded #def SYS_kevent64Added #def SYS_killAdded #def SYS_kqueueAdded #def SYS_kqueue_from_portset_npAdded #def SYS_kqueue_portset_npAdded #def SYS_lchownAdded #def SYS_linkAdded #def SYS_lio_listioAdded #def SYS_listenAdded #def SYS_listxattrAdded #def SYS_lseekAdded #def SYS_lstatAdded #def SYS_lstat64Added #def SYS_lstat64_extendedAdded #def SYS_lstat_extendedAdded #def SYS_lstatvAdded #def SYS_madviseAdded #def SYS_mincoreAdded #def SYS_minheritAdded #def SYS_mkcomplexAdded #def SYS_mkdirAdded #def SYS_mkdir_extendedAdded #def SYS_mkfifoAdded #def SYS_mkfifo_extendedAdded #def SYS_mknodAdded #def SYS_mlockAdded #def SYS_mlockallAdded #def SYS_mmapAdded #def SYS_modwatchAdded #def SYS_mountAdded #def SYS_mprotectAdded #def SYS_msgctlAdded #def SYS_msggetAdded #def SYS_msgrcvAdded #def SYS_msgrcv_nocancelAdded #def SYS_msgsndAdded #def SYS_msgsnd_nocancelAdded #def SYS_msgsysAdded #def SYS_msyncAdded #def SYS_msync_nocancelAdded #def SYS_munlockAdded #def SYS_munlockallAdded #def SYS_munmapAdded #def SYS_nfsclntAdded #def SYS_nfssvcAdded #def SYS_openAdded #def SYS_open_extendedAdded #def SYS_open_nocancelAdded #def SYS_pathconfAdded #def SYS_pipeAdded #def SYS_pollAdded #def SYS_poll_nocancelAdded #def SYS_posix_spawnAdded #def SYS_preadAdded #def SYS_pread_nocancelAdded #def SYS_proc_infoAdded #def SYS_profilAdded #def SYS_ptraceAdded #def SYS_pwriteAdded #def SYS_pwrite_nocancelAdded #def SYS_quotactlAdded #def SYS_readAdded #def SYS_read_nocancelAdded #def SYS_readlinkAdded #def SYS_readvAdded #def SYS_readv_nocancelAdded #def SYS_rebootAdded #def SYS_recvfromAdded #def SYS_recvfrom_nocancelAdded #def SYS_recvmsgAdded #def SYS_recvmsg_nocancelAdded #def SYS_removexattrAdded #def SYS_renameAdded #def SYS_revokeAdded #def SYS_rmdirAdded #def SYS_searchfsAdded #def SYS_selectAdded #def SYS_select_nocancelAdded #def SYS_sem_closeAdded #def SYS_sem_destroyAdded #def SYS_sem_getvalueAdded #def SYS_sem_initAdded #def SYS_sem_openAdded #def SYS_sem_postAdded #def SYS_sem_trywaitAdded #def SYS_sem_unlinkAdded #def SYS_sem_waitAdded #def SYS_sem_wait_nocancelAdded #def SYS_semctlAdded #def SYS_semgetAdded #def SYS_semopAdded #def SYS_semsysAdded #def SYS_sendfileAdded #def SYS_sendmsgAdded #def SYS_sendmsg_nocancelAdded #def SYS_sendtoAdded #def SYS_sendto_nocancelAdded #def SYS_setattrlistAdded #def SYS_setauditAdded #def SYS_setaudit_addrAdded #def SYS_setauidAdded #def SYS_setegidAdded #def SYS_seteuidAdded #def SYS_setgidAdded #def SYS_setgroupsAdded #def SYS_setitimerAdded #def SYS_setlcidAdded #def SYS_setloginAdded #def SYS_setpgidAdded #def SYS_setpriorityAdded #def SYS_setprivexecAdded #def SYS_setregidAdded #def SYS_setreuidAdded #def SYS_setrlimitAdded #def SYS_setsgroupsAdded #def SYS_setsidAdded #def SYS_setsockoptAdded #def SYS_settidAdded #def SYS_settid_with_pidAdded #def SYS_settimeofdayAdded #def SYS_setuidAdded #def SYS_setwgroupsAdded #def SYS_setxattrAdded #def SYS_shared_region_check_npAdded #def SYS_shared_region_map_npAdded #def SYS_shm_openAdded #def SYS_shm_unlinkAdded #def SYS_shmatAdded #def SYS_shmctlAdded #def SYS_shmdtAdded #def SYS_shmgetAdded #def SYS_shmsysAdded #def SYS_shutdownAdded #def SYS_sigactionAdded #def SYS_sigaltstackAdded #def SYS_sigpendingAdded #def SYS_sigprocmaskAdded #def SYS_sigreturnAdded #def SYS_sigsuspendAdded #def SYS_sigsuspend_nocancelAdded #def SYS_socketAdded #def SYS_socketpairAdded #def SYS_stack_snapshotAdded #def SYS_statAdded #def SYS_stat64Added #def SYS_stat64_extendedAdded #def SYS_stat_extendedAdded #def SYS_statfsAdded #def SYS_statfs64Added #def SYS_statvAdded #def SYS_swaponAdded #def SYS_symlinkAdded #def SYS_syncAdded #def SYS_syscallAdded #def SYS_truncateAdded #def SYS_umaskAdded #def SYS_umask_extendedAdded #def SYS_undeleteAdded #def SYS_unlinkAdded #def SYS_unmountAdded #def SYS_utimesAdded #def SYS_vforkAdded #def SYS_vm_pressure_monitorAdded #def SYS_wait4Added #def SYS_wait4_nocancelAdded #def SYS_waiteventAdded #def SYS_waitidAdded #def SYS_waitid_nocancelAdded #def SYS_watcheventAdded #def SYS_workq_openAdded #def SYS_workq_opsAdded #def SYS_writeAdded #def SYS_write_nocancelAdded #def SYS_writevAdded #def SYS_writev_nocancelsysctl.hRemoved kinfo_lctx (no architecture available)Removed kinfo_proc (no architecture available)Removed kinfo_proc::eproc (no architecture available)syslog.hRemoved logpri()Removed logtime()Removed vaddlog()sysproto.hRemoved obreak()Removed obreak_argsRemoved ogetfsstat() (no architecture available)Removed ogetfsstat_args (no architecture available)Removed ovadvise()Removed ovadvise_argsRemoved sbrk()Removed sbrk_argsRemoved sstk()Removed sstk_argsAdded fdatasync()Added fdatasync_argsAdded ffsctl()Added ffsctl_argsAdded fgetattrlist()Added fgetattrlist_argsAdded fsetattrlist()Added fsetattrlist_argsAdded fsgetpath()Added fsgetpath_argsAdded kevent64()Added kevent64_argsAdded munge_llllll()Added vm_pressure_monitor()Added vm_pressure_monitor_argsModified exit()

|  | Declaration |
| --- | --- |
| Old | void exit ( struct proc \*, struct exit_args \*, int \*); |
| New | void exit ( struct proc \*, struct exit_args \*, int32_t \*); |

systm.hRemoved copywithin()Removed einval()Removed errsys()Removed fulong()Removed fuulong()Removed kvprintf()Removed nullsys()Removed sulong()Removed suulong()Removed tablefull()Removed uprintf()Added [tvtoabstime()](https://developer.apple.com/documentation/kernel/1519632-tvtoabstime)tcp.hAdded #def TCP_CONNECTIONTIMEOUTtermios.hAdded termios32time.hRemoved user_itimervalRemoved user_timevalttycom.hAdded #def TIOCDCDTIMESTAMP_32Added #def TIOCGETA_32Added #def TIOCSETAF_32Added #def TIOCSETAW_32Added #def TIOCSETA_32Added #def TIOCTIMESTAMP_32types.hAdded [user32_addr_t](https://developer.apple.com/documentation/kernel/user32_addr_t)Added [user32_long_t](https://developer.apple.com/documentation/kernel/user32_long_t)Added [user32_off_t](https://developer.apple.com/documentation/kernel/user32_off_t)Added [user32_size_t](https://developer.apple.com/documentation/kernel/user32_size_t)Added [user32_ssize_t](https://developer.apple.com/documentation/kernel/user32_ssize_t)Added [user32_time_t](https://developer.apple.com/documentation/kernel/user32_time_t)Added [user32_ulong_t](https://developer.apple.com/documentation/kernel/user32_ulong_t)Added [user64_addr_t](https://developer.apple.com/documentation/kernel/user64_addr_t)Added [user64_long_t](https://developer.apple.com/documentation/kernel/user64_long_t)Added [user64_off_t](https://developer.apple.com/documentation/kernel/user64_off_t)Added [user64_size_t](https://developer.apple.com/documentation/kernel/user64_size_t)Added [user64_ssize_t](https://developer.apple.com/documentation/kernel/user64_ssize_t)Added [user64_time_t](https://developer.apple.com/documentation/kernel/user64_time_t)Added [user64_ulong_t](https://developer.apple.com/documentation/kernel/user64_ulong_t)Added [user_off_t](https://developer.apple.com/documentation/kernel/user_off_t)ubc.hRemoved ubc_cs_blob_add()Removed ubc_cs_blob_get()Removed ubc_cs_getcdhash()Removed ubc_get_cs_blobs()Removed ubc_setcred()Added [is_file_clean()](https://developer.apple.com/documentation/kernel/1463775-is_file_clean)Added [ubc_page_op()](https://developer.apple.com/documentation/kernel/1463700-ubc_page_op)Added [ubc_range_op()](https://developer.apple.com/documentation/kernel/1463728-ubc_range_op)Modified [ubc_create_upl()](https://developer.apple.com/documentation/kernel/1463758-ubc_create_upl)

|  | Declaration |
| --- | --- |
| Old | int ubc_create_upl ( vnode_t, off_t, long, upl_t \*, upl_page_info_t \*\*, int); |
| New | int ubc_create_upl ( vnode_t, off_t, int, upl_t \*, upl_page_info_t \*\*, int); |

Modified [cluster_pagein_ext()](https://developer.apple.com/documentation/kernel/1463709-cluster_pagein_ext)

|  | Declaration |
| --- | --- |
| Old | int cluster_pagein_ext ( vnode_t, upl_t, vm_offset_t, off_t, int, off_t, int, int (\*)(buf_t, void \*), void \*); |
| New | int cluster_pagein_ext ( vnode_t, upl_t, upl_offset_t, off_t, int, off_t, int, int (\*)(buf_t, void \*), void \*); |

Modified [cluster_zero()](https://developer.apple.com/documentation/kernel/1463752-cluster_zero)

|  | Declaration |
| --- | --- |
| Old | void cluster_zero ( upl_t, vm_offset_t, int, buf_t); |
| New | void cluster_zero ( upl_t, upl_offset_t, int, buf_t); |

Modified [ubc_upl_map()](https://developer.apple.com/documentation/kernel/1463744-ubc_upl_map)

|  | Declaration |
| --- | --- |
| Old | int ubc_upl_map ( upl_t, upl_offset_t \*); |
| New | int ubc_upl_map ( upl_t, vm_offset_t \*); |

Modified [cluster_pagein()](https://developer.apple.com/documentation/kernel/1463765-cluster_pagein)

|  | Declaration |
| --- | --- |
| Old | int cluster_pagein ( vnode_t, upl_t, vm_offset_t, off_t, int, off_t, int); |
| New | int cluster_pagein ( vnode_t, upl_t, upl_offset_t, off_t, int, off_t, int); |

Modified [cluster_pageout_ext()](https://developer.apple.com/documentation/kernel/1463750-cluster_pageout_ext)

|  | Declaration |
| --- | --- |
| Old | int cluster_pageout_ext ( vnode_t, upl_t, vm_offset_t, off_t, int, off_t, int, int (\*)(buf_t, void \*), void \*); |
| New | int cluster_pageout_ext ( vnode_t, upl_t, upl_offset_t, off_t, int, off_t, int, int (\*)(buf_t, void \*), void \*); |

Modified [cluster_pageout()](https://developer.apple.com/documentation/kernel/1463710-cluster_pageout)

|  | Declaration |
| --- | --- |
| Old | int cluster_pageout ( vnode_t, upl_t, vm_offset_t, off_t, int, off_t, int); |
| New | int cluster_pageout ( vnode_t, upl_t, upl_offset_t, off_t, int, off_t, int); |

uio.hRemoved ureadc()Removed uwritec()Modified [uiomove64()](https://developer.apple.com/documentation/kernel/1442209-uiomove64)

|  | Declaration |
| --- | --- |
| Old | int uiomove64 ( const unsigned long long cp, int n, struct uio \*uio); |
| New | int uiomove64 ( const __uint64_t cp, int n, struct uio \*uio); |

unistd.hRemoved #def getpagesizeuuid.hAdded [uuid_string_t](https://developer.apple.com/documentation/kernel/uuid_string_t)Modified [uuid_parse()](https://developer.apple.com/documentation/kernel/1470624-uuid_parse)

|  | Declaration |
| --- | --- |
| Old | int uuid_parse ( const char \*in, uuid_t uu); |
| New | int uuid_parse ( const uuid_string_t in, uuid_t uu); |

Modified [uuid_unparse_upper()](https://developer.apple.com/documentation/kernel/1470618-uuid_unparse_upper)

|  | Declaration |
| --- | --- |
| Old | void uuid_unparse_upper ( const uuid_t uu, char \*out); |
| New | void uuid_unparse_upper ( const uuid_t uu, uuid_string_t out); |

Modified [uuid_unparse_lower()](https://developer.apple.com/documentation/kernel/1470622-uuid_unparse_lower)

|  | Declaration |
| --- | --- |
| Old | void uuid_unparse_lower ( const uuid_t uu, char \*out); |
| New | void uuid_unparse_lower ( const uuid_t uu, uuid_string_t out); |

Modified [uuid_unparse()](https://developer.apple.com/documentation/kernel/1470620-uuid_unparse)

|  | Declaration |
| --- | --- |
| Old | void uuid_unparse ( const uuid_t uu, char \*out); |
| New | void uuid_unparse ( const uuid_t uu, uuid_string_t out); |

vfs_journal.hRemoved #def BLHDR_CHECK_CHECKSUMSRemoved #def BLHDR_FIRST_HEADERRemoved #def ENDIAN_MAGICRemoved #def JOURNAL_CLOSE_PENDINGRemoved #def JOURNAL_DO_FUA_WRITESRemoved #def JOURNAL_FLUSHCACHE_ERRRemoved #def JOURNAL_HEADER_CKSUM_SIZERemoved #def JOURNAL_HEADER_MAGICRemoved #def JOURNAL_INVALIDRemoved #def JOURNAL_NEED_SWAPRemoved #def JOURNAL_NO_GROUP_COMMITRemoved #def JOURNAL_OPTION_FLAGS_MASKRemoved #def JOURNAL_RESETRemoved #def OLD_JOURNAL_HEADER_MAGICRemoved block_infoRemoved block_list_headerRemoved journalRemoved journal_active()Removed journal_close()Removed journal_create()Removed journal_end_transaction()Removed journal_flush()Removed journal_headerRemoved journal_init()Removed journal_is_clean()Removed journal_kill_block()Removed journal_modify_block_abort()Removed journal_modify_block_end()Removed journal_modify_block_start()Removed journal_open()Removed journal_owner()Removed journal_relocate()Removed journal_start_transaction()Removed journal_uses_fua()Removed transactionvm_behavior.hAdded #def VM_BEHAVIOR_FREEvm_param.hAdded #def ANON_MAX_SIZEAdded #def CAST_DOWN_EXPLICITvm_purgable.hAdded #def VM_PURGABLE_ALL_MASKSAdded #def VM_PURGABLE_DEBUG_EMPTYAdded #def VM_PURGABLE_DEBUG_FAULTAdded #def VM_PURGABLE_DEBUG_MASKAdded #def VM_PURGABLE_DEBUG_SHIFTAdded #def VM_PURGABLE_PURGE_ALLvm_region.hAdded #def VM_PAGE_INFO_BASICAdded #def VM_PAGE_INFO_BASIC_COUNTAdded #def VM_PAGE_INFO_MAXAdded [vm32_object_id_t](https://developer.apple.com/documentation/kernel/vm32_object_id_t)Added vm32_read_entry (no architecture available)Added vm32_read_entry_t (no architecture available)Added vm_page_info_basicAdded [vm_page_info_basic_data_t](https://developer.apple.com/documentation/kernel/vm_page_info_basic_data_t)Added [vm_page_info_basic_t](https://developer.apple.com/documentation/kernel/vm_page_info_basic_t)Added [vm_page_info_data_t](https://developer.apple.com/documentation/kernel/vm_page_info_data_t)Added [vm_page_info_flavor_t](https://developer.apple.com/documentation/kernel/vm_page_info_flavor_t)Added [vm_page_info_t](https://developer.apple.com/documentation/kernel/vm_page_info_t)vm_statistics.hAdded #def VM_MEMORY_OBJC_DISPATCHERSAdded #def VM_PAGE_QUERY_PAGE_EXTERNALvnode.hRemoved #def LEASE_READRemoved #def LEASE_WRITERemoved check_mountedon()Removed current_rootdir()Removed current_workingdir()Removed vfs_context_cwd()Removed vfs_context_issuser()Removed vfs_context_kernel()Removed vfs_mountref()Removed vfs_mountrele()Removed vn_getcdhash()Removed vnode_clear_openevt()Removed vnode_iftovt()Removed vnode_is_openevt()Removed vnode_isstandard()Removed vnode_lock()Removed vnode_makeimode()Removed vnode_reclaim()Removed vnode_set_openevt()Removed vnode_unlock()Removed vnode_vfscmdflags()Removed vnode_vfsfsprivate()Removed vnode_vfsstatfs()Removed vnode_vfsvisflags()Removed vnode_vttoif()Added #def VNODE_UPDATE_PURGEAdded [vn_path_package_check()](https://developer.apple.com/documentation/kernel/1562172-vn_path_package_check)Added [vn_rdwr()](https://developer.apple.com/documentation/kernel/1562098-vn_rdwr)Added [vnode_getname()](https://developer.apple.com/documentation/kernel/1562283-vnode_getname)Added [vnode_getparent()](https://developer.apple.com/documentation/kernel/1562185-vnode_getparent)Added [vnode_getwithref()](https://developer.apple.com/documentation/kernel/1562306-vnode_getwithref)Added [vnode_putname()](https://developer.apple.com/documentation/kernel/1562445-vnode_putname)Modified [vnode_getwithvid()](https://developer.apple.com/documentation/kernel/1562409-vnode_getwithvid)

|  | Declaration |
| --- | --- |
| Old | int vnode_getwithvid ( vnode_t, int); |
| New | int vnode_getwithvid ( vnode_t, uint32_t); |

Modified [vnode_update_identity()](https://developer.apple.com/documentation/kernel/1562361-vnode_update_identity)

|  | Declaration |
| --- | --- |
| Old | void vnode_update_identity ( vnode_t vp, vnode_t dvp, const char \*name, int name_len, int name_hashval, int flags); |
| New | void vnode_update_identity ( vnode_t vp, vnode_t dvp, const char \*name, int name_len, uint32_t name_hashval, int flags); |

Modified [vfs_addname()](https://developer.apple.com/documentation/kernel/1562422-vfs_addname)

|  | Declaration |
| --- | --- |
| Old | const char \* vfs_addname ( const char \*name, size_t len, u_int nc_hash, u_int flags); |
| New | const char \* vfs_addname ( const char \*name, uint32_t len, uint32_t nc_hash, uint32_t flags); |

Modified [vnode_create()](https://developer.apple.com/documentation/kernel/1562117-vnode_create)

|  | Declaration |
| --- | --- |
| Old | errno_t vnode_create ( int, size_t, void \*, vnode_t \*); |
| New | errno_t vnode_create ( uint32_t, uint32_t, void \*, vnode_t \*); |

vnode_if.hRemoved VNOP_ACCESS()Removed VNOP_ADVLOCK()Removed VNOP_ALLOCATE()Removed VNOP_BLKTOOFF()Removed VNOP_BLOCKMAP()Removed VNOP_CLOSE()Removed VNOP_COPYFILE()Removed VNOP_CREATE()Removed VNOP_EXCHANGE()Removed VNOP_GETATTR()Removed VNOP_GETNAMEDSTREAM() (no architecture available)Removed VNOP_INACTIVE()Removed VNOP_KQFILT_ADD()Removed VNOP_KQFILT_REMOVE()Removed VNOP_LINK()Removed VNOP_LISTXATTR()Removed VNOP_LOOKUP()Removed VNOP_MAKENAMEDSTREAM() (no architecture available)Removed VNOP_MKDIR()Removed VNOP_MKNOD()Removed VNOP_MMAP()Removed VNOP_MNOMAP()Removed VNOP_OFFTOBLK()Removed VNOP_OPEN()Removed VNOP_PAGEIN()Removed VNOP_PAGEOUT()Removed VNOP_PATHCONF()Removed VNOP_READDIR()Removed VNOP_READDIRATTR()Removed VNOP_READLINK()Removed VNOP_RECLAIM()Removed VNOP_REMOVE()Removed VNOP_REMOVENAMEDSTREAM() (no architecture available)Removed VNOP_REMOVEXATTR()Removed VNOP_RENAME()Removed VNOP_REVOKE()Removed VNOP_RMDIR()Removed VNOP_SEARCHFS()Removed VNOP_SELECT()Removed VNOP_SETATTR()Removed VNOP_SETLABEL()Removed VNOP_SYMLINK()Removed VNOP_WHITEOUT()zlib.hModified [adler32()](https://developer.apple.com/documentation/kernel/1546941-adler32)

|  | Header |
| --- | --- |
| Old | mkext.h |
| New | zlib.h |

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
