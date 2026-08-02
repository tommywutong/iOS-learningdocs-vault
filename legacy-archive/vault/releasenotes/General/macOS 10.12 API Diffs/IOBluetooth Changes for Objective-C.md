---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/IOBluetooth.html
archived_at: '2026-07-18T02:50:39.553955Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# IOBluetooth Changes for Objective-C

### IOBluetooth

#### Bluetooth.h

Added [BluetoothEnhancedSynchronousConnectionInfo](https://developer.apple.com/documentation/iobluetooth/bluetoothenhancedsynchronousconnectioninfo)Added [BluetoothHCIEnhancedAcceptSynchronousConnectionRequestParams](https://developer.apple.com/documentation/iobluetooth/bluetoothhcienhancedacceptsynchronousconnectionrequestparams)Added [BluetoothHCIEnhancedSetupSynchronousConnectionParams](https://developer.apple.com/documentation/kernel/bluetoothhcienhancedsetupsynchronousconnectionparams)Added [BluetoothHCIEventLEReadRemoteUsedFeaturesCompleteResults](https://developer.apple.com/documentation/iobluetooth/bluetoothhcieventlereadremoteusedfeaturescompleteresults)Added [BluetoothHCIInputBandwidth](https://developer.apple.com/documentation/kernel/bluetoothhciinputbandwidth)Added [BluetoothHCIInputCodedDataSize](https://developer.apple.com/documentation/iobluetooth/bluetoothhciinputcodeddatasize)Added [BluetoothHCIInputCodingFormat](https://developer.apple.com/documentation/iobluetooth/bluetoothhciinputcodingformat)Added [BluetoothHCIInputDataPath](https://developer.apple.com/documentation/kernel/bluetoothhciinputdatapath)Added [BluetoothHCIInputPCMDataFormat](https://developer.apple.com/documentation/iobluetooth/bluetoothhciinputpcmdataformat)Added [BluetoothHCIInputPCMSamplePayloadMSBPosition](https://developer.apple.com/documentation/iobluetooth/bluetoothhciinputpcmsamplepayloadmsbposition)Added [BluetoothHCIInputTransportUnitSize](https://developer.apple.com/documentation/iobluetooth/bluetoothhciinputtransportunitsize)Added [BluetoothHCILESupportedFeatures](https://developer.apple.com/documentation/iobluetooth/bluetoothhcilesupportedfeatures)Added [BluetoothHCILEUsedFeatures](https://developer.apple.com/documentation/iobluetooth/bluetoothhcileusedfeatures)Added [BluetoothHCIOutputBandwidth](https://developer.apple.com/documentation/iobluetooth/bluetoothhcioutputbandwidth)Added [BluetoothHCIOutputCodedDataSize](https://developer.apple.com/documentation/kernel/bluetoothhcioutputcodeddatasize)Added [BluetoothHCIOutputCodingFormat](https://developer.apple.com/documentation/kernel/bluetoothhcioutputcodingformat)Added [BluetoothHCIOutputDataPath](https://developer.apple.com/documentation/kernel/bluetoothhcioutputdatapath)Added [BluetoothHCIOutputPCMDataFormat](https://developer.apple.com/documentation/iobluetooth/bluetoothhcioutputpcmdataformat)Added [BluetoothHCIOutputPCMSamplePayloadMSBPosition](https://developer.apple.com/documentation/iobluetooth/bluetoothhcioutputpcmsamplepayloadmsbposition)Added [BluetoothHCIOutputTransportUnitSize](https://developer.apple.com/documentation/kernel/bluetoothhcioutputtransportunitsize)Added [BluetoothHCIReceiveCodecFrameSize](https://developer.apple.com/documentation/kernel/bluetoothhcireceivecodecframesize)Added [BluetoothHCIReceiveCodingFormat](https://developer.apple.com/documentation/iobluetooth/bluetoothhcireceivecodingformat)Added [BluetoothHCITransmitCodecFrameSize](https://developer.apple.com/documentation/iobluetooth/bluetoothhcitransmitcodecframesize)Added [BluetoothHCITransmitCodingFormat](https://developer.apple.com/documentation/kernel/bluetoothhcitransmitcodingformat)Added [BluetoothL2CAPSegmentationAndReassembly](https://developer.apple.com/documentation/kernel/bluetoothl2capsegmentationandreassembly)Added [BluetoothL2CAPSupervisoryFuctionType](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capsupervisoryfuctiontype)Added [BluetoothLEFeatureBits](https://developer.apple.com/documentation/kernel/bluetoothlefeaturebits)Added [kBluetoothHCIErrorCoarseClockAdjustmentRejected](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcierrorcoarseclockadjustmentrejected)Added [kBluetoothHCISubEventLEDataLengthChange](https://developer.apple.com/documentation/iobluetooth/1490041-anonymous/kbluetoothhcisubeventledatalengthchange)Added [kBluetoothHCISubEventLEDirectAdvertisingReport](https://developer.apple.com/documentation/kernel/1639977-anonymous/kbluetoothhcisubeventledirectadvertisingreport)Added [kBluetoothHCISubEventLEEnhancedConnectionComplete](https://developer.apple.com/documentation/iobluetooth/1490041-anonymous/kbluetoothhcisubeventleenhancedconnectioncomplete)Added [kBluetoothHCISubEventLEGenerateDHKeyComplete](https://developer.apple.com/documentation/kernel/1639977-anonymous/kbluetoothhcisubeventlegeneratedhkeycomplete)Added [kBluetoothHCISubEventLEReadLocalP256PublicKeyComplete](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcisubeventlereadlocalp256publickeycomplete)Added [kBluetoothHCISubEventLERemoteConnectionParameterRequest](https://developer.apple.com/documentation/iobluetooth/1490041-anonymous/kbluetoothhcisubeventleremoteconnectionparameterrequest)Added [kBluetoothL2CAPConnectionResultRefusedInvalidSourceCID](https://developer.apple.com/documentation/kernel/bluetoothl2capconnectionresult/kbluetoothl2capconnectionresultrefusedinvalidsourcecid)Added [kBluetoothL2CAPConnectionResultRefusedReserved](https://developer.apple.com/documentation/kernel/bluetoothl2capconnectionresult/kbluetoothl2capconnectionresultrefusedreserved)Added [kBluetoothL2CAPConnectionResultRefusedSourceCIDAlreadyAllocated](https://developer.apple.com/documentation/kernel/bluetoothl2capconnectionresult/kbluetoothl2capconnectionresultrefusedsourcecidalreadyallocated)Added [kBluetoothL2CAPMTULowEnergyMax](https://developer.apple.com/documentation/iobluetooth/1489801-anonymous/kbluetoothl2capmtulowenergymax)Added [kBluetoothL2CAPSegmentationAndReassemblyContinuationOfSDU](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capsegmentationandreassembly/kbluetoothl2capsegmentationandreassemblycontinuationofsdu)Added [kBluetoothL2CAPSegmentationAndReassemblyEndOfSDU](https://developer.apple.com/documentation/kernel/bluetoothl2capsegmentationandreassembly/kbluetoothl2capsegmentationandreassemblyendofsdu)Added [kBluetoothL2CAPSegmentationAndReassemblyStartOfSDU](https://developer.apple.com/documentation/iobluetooth/kbluetoothl2capsegmentationandreassemblystartofsdu)Added [kBluetoothL2CAPSegmentationAndReassemblyUnsegmentedSDU](https://developer.apple.com/documentation/iobluetooth/kbluetoothl2capsegmentationandreassemblyunsegmentedsdu)Added [kBluetoothL2CAPSupervisoryFuctionTypeReceiverNotReady](https://developer.apple.com/documentation/iobluetooth/kbluetoothl2capsupervisoryfuctiontypereceivernotready)Added [kBluetoothL2CAPSupervisoryFuctionTypeReceiverReady](https://developer.apple.com/documentation/iobluetooth/kbluetoothl2capsupervisoryfuctiontypereceiverready)Added [kBluetoothL2CAPSupervisoryFuctionTypeReject](https://developer.apple.com/documentation/iobluetooth/kbluetoothl2capsupervisoryfuctiontypereject)Added [kBluetoothL2CAPSupervisoryFuctionTypeSelectiveReject](https://developer.apple.com/documentation/iobluetooth/kbluetoothl2capsupervisoryfuctiontypeselectivereject)Added [kBluetoothLEFeatureConnectionParamsRequestProcedure](https://developer.apple.com/documentation/iobluetooth/bluetoothlefeaturebits/kbluetoothlefeatureconnectionparamsrequestprocedure)Added [kBluetoothLEFeatureExtendedRejectIndication](https://developer.apple.com/documentation/kernel/bluetoothlefeaturebits/kbluetoothlefeatureextendedrejectindication)Added [kBluetoothLEFeatureExtendedScannerFilterPolicies](https://developer.apple.com/documentation/kernel/bluetoothlefeaturebits/kbluetoothlefeatureextendedscannerfilterpolicies)Added [kBluetoothLEFeatureLEDataPacketLengthExtension](https://developer.apple.com/documentation/kernel/bluetoothlefeaturebits/kbluetoothlefeatureledatapacketlengthextension)Added [kBluetoothLEFeatureLEEncryption](https://developer.apple.com/documentation/iobluetooth/bluetoothlefeaturebits/kbluetoothlefeatureleencryption)Added [kBluetoothLEFeatureLEPing](https://developer.apple.com/documentation/kernel/bluetoothlefeaturebits/kbluetoothlefeatureleping)Added [kBluetoothLEFeatureLLPrivacy](https://developer.apple.com/documentation/kernel/bluetoothlefeaturebits/kbluetoothlefeaturellprivacy)Added [kBluetoothLEFeatureSlaveInitiatedFeaturesExchange](https://developer.apple.com/documentation/iobluetooth/bluetoothlefeaturebits/kbluetoothlefeatureslaveinitiatedfeaturesexchange)Added [kBluetoothLEMaxTXOctetsDefault](https://developer.apple.com/documentation/iobluetooth/kbluetoothlemaxtxoctetsdefault)Added [kBluetoothLEMaxTXOctetsMax](https://developer.apple.com/documentation/iobluetooth/1643068-anonymous/kbluetoothlemaxtxoctetsmax)Added [kBluetoothLEMaxTXOctetsMin](https://developer.apple.com/documentation/iobluetooth/kbluetoothlemaxtxoctetsmin)Added [kBluetoothLEMaxTXTimeDefault](https://developer.apple.com/documentation/iobluetooth/1643068-anonymous/kbluetoothlemaxtxtimedefault)Added [kBluetoothLEMaxTXTimeMax](https://developer.apple.com/documentation/iobluetooth/1643068-anonymous/kbluetoothlemaxtxtimemax)Added [kBluetoothLEMaxTXTimeMin](https://developer.apple.com/documentation/iobluetooth/1643068-anonymous/kbluetoothlemaxtxtimemin)Added [kBluetoothLETXOctetsDefault](https://developer.apple.com/documentation/iobluetooth/kbluetoothletxoctetsdefault)Added [kBluetoothLETXOctetsMax](https://developer.apple.com/documentation/kernel/1639933-anonymous/kbluetoothletxoctetsmax)Added [kBluetoothLETXOctetsMin](https://developer.apple.com/documentation/iobluetooth/kbluetoothletxoctetsmin)Added [kBluetoothLETXTimeDefault](https://developer.apple.com/documentation/kernel/1639933-anonymous/kbluetoothletxtimedefault)Added [kBluetoothLETXTimeMax](https://developer.apple.com/documentation/iobluetooth/kbluetoothletxtimemax)Added [kBluetoothLETXTimeMin](https://developer.apple.com/documentation/iobluetooth/1642841-anonymous/kbluetoothletxtimemin)

#### BluetoothAssignedNumbers.h

Added [kBluetoothHCIExtendedInquiryResponseDataType3DInformationData](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatype3dinformationdata)Added [kBluetoothHCIExtendedInquiryResponseDataTypeAdvertisingInterval](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypeadvertisinginterval)Added [kBluetoothHCIExtendedInquiryResponseDataTypeLEBluetoothDeviceAddress](https://developer.apple.com/documentation/iobluetooth/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypelebluetoothdeviceaddress)Added [kBluetoothHCIExtendedInquiryResponseDataTypeLERole](https://developer.apple.com/documentation/iobluetooth/kbluetoothhciextendedinquiryresponsedatatypelerole)Added [kBluetoothHCIExtendedInquiryResponseDataTypeSecureConnectionsConfirmationValue](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypesecureconnectionsconfirmationvalue)Added [kBluetoothHCIExtendedInquiryResponseDataTypeSecureConnectionsRandomValue](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypesecureconnectionsrandomvalue)Added [kBluetoothHCIExtendedInquiryResponseDataTypeServiceData128BitUUID](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypeservicedata128bituuid)Added [kBluetoothHCIExtendedInquiryResponseDataTypeServiceData32BitUUID](https://developer.apple.com/documentation/iobluetooth/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypeservicedata32bituuid)Added [kBluetoothHCIExtendedInquiryResponseDataTypeServiceSolicitation32BitUUIDs](https://developer.apple.com/documentation/iobluetooth/kbluetoothhciextendedinquiryresponsedatatypeservicesolicitation32bituuids)Added [kBluetoothHCIExtendedInquiryResponseDataTypeSimplePairingHash](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypesimplepairinghash)Added [kBluetoothHCIExtendedInquiryResponseDataTypeSimplePairingRandomizer](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypesimplepairingrandomizer)Added [kBluetoothL2CAPPSMAACP](https://developer.apple.com/documentation/kernel/1640540-anonymous/kbluetoothl2cappsmaacp)

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
