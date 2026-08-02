---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/IOBluetooth.html
archived_at: '2026-07-18T02:52:30.894255Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# IOBluetooth Changes

## IOBluetooth

Removed kBluetoothSDPUUID16ServiceClassVideoConferencingAdded BluetoothAFHHostChannelClassification.init()Added BluetoothAFHHostChannelClassification.init(data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added BluetoothAFHResults.init()Added BluetoothAFHResults.init(handle: BluetoothConnectionHandle, mode: BluetoothAFHMode, afhMap:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added BluetoothDeviceAddress.init()Added BluetoothDeviceAddress.init(data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added BluetoothEventFilterCondition.init()Added BluetoothEventFilterCondition.init(data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added BluetoothHCIAcceptSynchronousConnectionRequestParams.init()Added BluetoothHCIAcceptSynchronousConnectionRequestParams.init(transmitBandwidth: UInt32, receiveBandwidth: UInt32, maxLatency: UInt16, contentFormat: UInt16, retransmissionEffort: UInt8, packetType: UInt16)Added BluetoothHCIAutomaticFlushTimeoutInfo.init()Added BluetoothHCIAutomaticFlushTimeoutInfo.init(handle: BluetoothConnectionHandle, timeout: BluetoothHCIAutomaticFlushTimeout)Added BluetoothHCIBufferSize.init()Added BluetoothHCIBufferSize.init(ACLDataPacketLength: UInt16, SCODataPacketLength: UInt8, totalNumACLDataPackets: UInt16, totalNumSCODataPackets: UInt16)Added BluetoothHCICurrentInquiryAccessCodes.init()Added BluetoothHCICurrentInquiryAccessCodes.init(count: BluetoothHCIInquiryAccessCodeCount, codes: UnsafeMutablePointer<BluetoothHCIInquiryAccessCode>)Added BluetoothHCIEventAuthenticationCompleteResults.init()Added BluetoothHCIEventAuthenticationCompleteResults.init(connectionHandle: BluetoothConnectionHandle)Added BluetoothHCIEventChangeConnectionLinkKeyCompleteResults.init()Added BluetoothHCIEventChangeConnectionLinkKeyCompleteResults.init(connectionHandle: BluetoothConnectionHandle)Added BluetoothHCIEventConnectionCompleteResults.init()Added BluetoothHCIEventConnectionCompleteResults.init(connectionHandle: BluetoothConnectionHandle, deviceAddress: BluetoothDeviceAddress, linkType: BluetoothLinkType, encryptionMode: BluetoothHCIEncryptionMode)Added BluetoothHCIEventConnectionPacketTypeResults.init()Added BluetoothHCIEventConnectionPacketTypeResults.init(connectionHandle: BluetoothConnectionHandle, packetType: BluetoothPacketType)Added BluetoothHCIEventConnectionRequestResults.init()Added BluetoothHCIEventConnectionRequestResults.init(deviceAddress: BluetoothDeviceAddress, classOfDevice: BluetoothClassOfDevice, linkType: BluetoothLinkType)Added BluetoothHCIEventDataBufferOverflowResults.init()Added BluetoothHCIEventDataBufferOverflowResults.init(linkType: BluetoothLinkType)Added BluetoothHCIEventDisconnectionCompleteResults.init()Added BluetoothHCIEventDisconnectionCompleteResults.init(connectionHandle: BluetoothConnectionHandle, reason: BluetoothReasonCode)Added BluetoothHCIEventEncryptionChangeResults.init()Added BluetoothHCIEventEncryptionChangeResults.init(connectionHandle: BluetoothConnectionHandle, enable: BluetoothEncryptionEnable)Added BluetoothHCIEventEncryptionKeyRefreshCompleteResults.init()Added BluetoothHCIEventEncryptionKeyRefreshCompleteResults.init(connectionHandle: BluetoothConnectionHandle)Added BluetoothHCIEventFlowSpecificationData.init()Added BluetoothHCIEventFlowSpecificationData.init(connectionHandle: BluetoothConnectionHandle, flags: UInt8, flowDirection: UInt8, serviceType: UInt8, tokenRate: UInt32, tokenBucketSize: UInt32, peakBandwidth: UInt32, accessLatency: UInt32)Added BluetoothHCIEventFlushOccurredResults.init()Added BluetoothHCIEventFlushOccurredResults.init(connectionHandle: BluetoothConnectionHandle)Added BluetoothHCIEventHardwareErrorResults.init()Added BluetoothHCIEventHardwareErrorResults.init(error: BluetoothHCIStatus)Added BluetoothHCIEventLEConnectionCompleteResults.init()Added BluetoothHCIEventLEConnectionCompleteResults.init(connectionHandle: BluetoothConnectionHandle, role: UInt8, peerAddressType: UInt8, peerAddress: BluetoothDeviceAddress, connInterval: UInt16, connLatency: UInt16, supervisionTimeout: UInt16, masterClockAccuracy: UInt8)Added BluetoothHCIEventLEConnectionUpdateCompleteResults.init()Added BluetoothHCIEventLEConnectionUpdateCompleteResults.init(connectionHandle: BluetoothConnectionHandle, connInterval: UInt16, connLatency: UInt16, supervisionTimeout: UInt16)Added BluetoothHCIEventLELongTermKeyRequestResults.init()Added BluetoothHCIEventLELongTermKeyRequestResults.init(connectionHandle: BluetoothConnectionHandle, randomNumber:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), ediv: UInt16)Added BluetoothHCIEventLEMetaResults.init()Added BluetoothHCIEventLEMetaResults.init(length: UInt8, data:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added BluetoothHCIEventLinkKeyNotificationResults.init()Added BluetoothHCIEventLinkKeyNotificationResults.init(deviceAddress: BluetoothDeviceAddress, linkKey: BluetoothKey, keyType: BluetoothKeyType)Added BluetoothHCIEventMasterLinkKeyCompleteResults.init()Added BluetoothHCIEventMasterLinkKeyCompleteResults.init(connectionHandle: BluetoothConnectionHandle, keyFlag: BluetoothKeyFlag)Added BluetoothHCIEventMaxSlotsChangeResults.init()Added BluetoothHCIEventMaxSlotsChangeResults.init(connectionHandle: BluetoothConnectionHandle, maxSlots: BluetoothMaxSlots)Added BluetoothHCIEventModeChangeResults.init()Added BluetoothHCIEventModeChangeResults.init(connectionHandle: BluetoothConnectionHandle, mode: BluetoothHCIConnectionMode, modeInterval: BluetoothHCIModeInterval)Added BluetoothHCIEventPageScanModeChangeResults.init()Added BluetoothHCIEventPageScanModeChangeResults.init(deviceAddress: BluetoothDeviceAddress, pageScanMode: BluetoothPageScanMode)Added BluetoothHCIEventPageScanRepetitionModeChangeResults.init()Added BluetoothHCIEventPageScanRepetitionModeChangeResults.init(deviceAddress: BluetoothDeviceAddress, pageScanRepetitionMode: BluetoothPageScanRepetitionMode)Added BluetoothHCIEventQoSSetupCompleteResults.init()Added BluetoothHCIEventQoSSetupCompleteResults.init(connectionHandle: BluetoothConnectionHandle, setupParams: BluetoothHCIQualityOfServiceSetupParams)Added BluetoothHCIEventQoSViolationResults.init()Added BluetoothHCIEventQoSViolationResults.init(connectionHandle: BluetoothConnectionHandle)Added BluetoothHCIEventReadClockOffsetResults.init()Added BluetoothHCIEventReadClockOffsetResults.init(connectionHandle: BluetoothConnectionHandle, clockOffset: BluetoothClockOffset)Added BluetoothHCIEventReadExtendedFeaturesResults.init()Added BluetoothHCIEventReadExtendedFeaturesResults.init(connectionHandle: BluetoothConnectionHandle, supportedFeaturesInfo: BluetoothHCIExtendedFeaturesInfo)Added BluetoothHCIEventReadRemoteExtendedFeaturesResults.init()Added BluetoothHCIEventReadRemoteExtendedFeaturesResults.init(error: BluetoothHCIStatus, connectionHandle: BluetoothConnectionHandle, page: BluetoothHCIPageNumber, maxPage: BluetoothHCIPageNumber, lmpFeatures: BluetoothHCISupportedFeatures)Added BluetoothHCIEventReadRemoteSupportedFeaturesResults.init()Added BluetoothHCIEventReadRemoteSupportedFeaturesResults.init(error: BluetoothHCIStatus, connectionHandle: BluetoothConnectionHandle, lmpFeatures: BluetoothHCISupportedFeatures)Added BluetoothHCIEventReadRemoteVersionInfoResults.init()Added BluetoothHCIEventReadRemoteVersionInfoResults.init(connectionHandle: BluetoothConnectionHandle, lmpVersion: BluetoothLMPVersion, manufacturerName: BluetoothManufacturerName, lmpSubversion: BluetoothLMPSubversion)Added BluetoothHCIEventReadSupportedFeaturesResults.init()Added BluetoothHCIEventReadSupportedFeaturesResults.init(connectionHandle: BluetoothConnectionHandle, supportedFeatures: BluetoothHCISupportedFeatures)Added BluetoothHCIEventRemoteNameRequestResults.init()Added BluetoothHCIEventRemoteNameRequestResults.init(deviceAddress: BluetoothDeviceAddress, deviceName: BluetoothDeviceName)Added BluetoothHCIEventReturnLinkKeysResults.init()Added BluetoothHCIEventRoleChangeResults.init()Added BluetoothHCIEventRoleChangeResults.init(connectionHandle: BluetoothConnectionHandle, deviceAddress: BluetoothDeviceAddress, role: BluetoothRole)Added BluetoothHCIEventSimplePairingCompleteResults.init()Added BluetoothHCIEventSimplePairingCompleteResults.init(deviceAddress: BluetoothDeviceAddress)Added BluetoothHCIEventSniffSubratingResults.init()Added BluetoothHCIEventSniffSubratingResults.init(connectionHandle: BluetoothConnectionHandle, maxTransmitLatency: UInt16, maxReceiveLatency: UInt16, minRemoteTimeout: UInt16, minLocalTimeout: UInt16)Added BluetoothHCIEventSynchronousConnectionChangedResults.init()Added BluetoothHCIEventSynchronousConnectionChangedResults.init(connectionHandle: BluetoothConnectionHandle, transmissionInterval: UInt8, retransmissionWindow: UInt8, receivePacketLength: UInt16, transmitPacketLength: UInt16)Added BluetoothHCIEventSynchronousConnectionCompleteResults.init()Added BluetoothHCIEventSynchronousConnectionCompleteResults.init(connectionHandle: BluetoothConnectionHandle, deviceAddress: BluetoothDeviceAddress, linkType: BluetoothLinkType, transmissionInterval: UInt8, retransmissionWindow: UInt8, receivePacketLength: UInt16, transmitPacketLength: UInt16, airMode: BluetoothAirMode)Added BluetoothHCIEventVendorSpecificResults.init()Added BluetoothHCIEventVendorSpecificResults.init(length: UInt8, data:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added BluetoothHCIExtendedFeaturesInfo.init()Added BluetoothHCIExtendedFeaturesInfo.init(page: BluetoothHCIPageNumber, maxPage: BluetoothHCIPageNumber, data:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added BluetoothHCIExtendedInquiryResponse.init()Added BluetoothHCIExtendedInquiryResponse.init(data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added BluetoothHCIExtendedInquiryResult.init()Added BluetoothHCIExtendedInquiryResult.init(numberOfReponses: UInt8, deviceAddress: BluetoothDeviceAddress, pageScanRepetitionMode: BluetoothPageScanRepetitionMode, reserved: UInt8, classOfDevice: BluetoothClassOfDevice, clockOffset: BluetoothClockOffset, RSSIValue: BluetoothHCIRSSIValue, extendedInquiryResponse: BluetoothHCIExtendedInquiryResponse)Added BluetoothHCIFailedContactInfo.init()Added BluetoothHCIFailedContactInfo.init(count: BluetoothHCIFailedContactCount, handle: BluetoothConnectionHandle)Added BluetoothHCIInquiryAccessCode.init()Added BluetoothHCIInquiryAccessCode.init(data: (UInt8, UInt8, UInt8))Added BluetoothHCIInquiryResult.init()Added BluetoothHCIInquiryResult.init(deviceAddress: BluetoothDeviceAddress, pageScanRepetitionMode: BluetoothPageScanRepetitionMode, pageScanPeriodMode: BluetoothHCIPageScanPeriodMode, pageScanMode: BluetoothHCIPageScanMode, classOfDevice: BluetoothClassOfDevice, clockOffset: BluetoothClockOffset)Added BluetoothHCIInquiryResults.init()Added BluetoothHCIInquiryResults.init(results: (BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult), count: IOItemCount)Added BluetoothHCIInquiryWithRSSIResult.init()Added BluetoothHCIInquiryWithRSSIResult.init(deviceAddress: BluetoothDeviceAddress, pageScanRepetitionMode: BluetoothPageScanRepetitionMode, reserved: UInt8, classOfDevice: BluetoothClassOfDevice, clockOffset: BluetoothClockOffset, RSSIValue: BluetoothHCIRSSIValue)Added BluetoothHCIInquiryWithRSSIResults.init()Added BluetoothHCIInquiryWithRSSIResults.init(results: (BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult), count: IOItemCount)Added BluetoothHCILEBufferSize.init()Added BluetoothHCILEBufferSize.init(ACLDataPacketLength: UInt16, totalNumACLDataPackets: UInt8)Added BluetoothHCILinkPolicySettingsInfo.init()Added BluetoothHCILinkPolicySettingsInfo.init(settings: BluetoothHCILinkPolicySettings, handle: BluetoothConnectionHandle)Added BluetoothHCILinkQualityInfo.init()Added BluetoothHCILinkQualityInfo.init(handle: BluetoothConnectionHandle, qualityValue: BluetoothHCILinkQuality)Added BluetoothHCILinkSupervisionTimeout.init()Added BluetoothHCILinkSupervisionTimeout.init(handle: BluetoothConnectionHandle, timeout: UInt16)Added BluetoothHCIQualityOfServiceSetupParams.init()Added BluetoothHCIQualityOfServiceSetupParams.init(flags: UInt8, serviceType: UInt8, tokenRate: UInt32, peakBandwidth: UInt32, latency: UInt32, delayVariation: UInt32)Added BluetoothHCIRSSIInfo.init()Added BluetoothHCIRSSIInfo.init(handle: BluetoothConnectionHandle, RSSIValue: BluetoothHCIRSSIValue)Added BluetoothHCIReadExtendedInquiryResponseResults.init()Added BluetoothHCIReadExtendedInquiryResponseResults.init(outFECRequired: BluetoothHCIFECRequired, extendedInquiryResponse: BluetoothHCIExtendedInquiryResponse)Added BluetoothHCIReadLMPHandleResults.init()Added BluetoothHCIReadLMPHandleResults.init(handle: BluetoothConnectionHandle, lmp_handle: BluetoothLMPHandle, reserved: UInt32)Added BluetoothHCIReadLocalOOBDataResults.init()Added BluetoothHCIReadLocalOOBDataResults.init(hash: BluetoothHCISimplePairingOOBData, randomizer: BluetoothHCISimplePairingOOBData)Added BluetoothHCIRequestCallbackInfo.init()Added BluetoothHCIRequestCallbackInfo.init(userCallback: mach_vm_address_t, userRefCon: mach_vm_address_t, internalRefCon: mach_vm_address_t, asyncIDRefCon: mach_vm_address_t, reserved: mach_vm_address_t)Added BluetoothHCIRoleInfo.init()Added BluetoothHCIRoleInfo.init(role: UInt8, handle: BluetoothConnectionHandle)Added BluetoothHCIScanActivity.init()Added BluetoothHCIScanActivity.init(scanInterval: UInt16, scanWindow: UInt16)Added BluetoothHCISetupSynchronousConnectionParams.init()Added BluetoothHCISetupSynchronousConnectionParams.init(transmitBandwidth: UInt32, receiveBandwidth: UInt32, maxLatency: UInt16, voiceSetting: UInt16, retransmissionEffort: UInt8, packetType: UInt16)Added BluetoothHCISimplePairingOOBData.init()Added BluetoothHCISimplePairingOOBData.init(data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added BluetoothHCIStoredLinkKeysInfo.init()Added BluetoothHCIStoredLinkKeysInfo.init(numLinkKeysRead: UInt16, maxNumLinkKeysAllowedInDevice: UInt16)Added BluetoothHCISupportedCommands.init()Added BluetoothHCISupportedCommands.init(data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added BluetoothHCISupportedFeatures.init()Added BluetoothHCISupportedFeatures.init(data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added BluetoothHCITransmitPowerLevelInfo.init()Added BluetoothHCITransmitPowerLevelInfo.init(handle: BluetoothConnectionHandle, level: BluetoothHCITransmitPowerLevel)Added BluetoothHCIVersionInfo.init()Added BluetoothHCIVersionInfo.init(manufacturerName: BluetoothManufacturerName, lmpVersion: BluetoothLMPVersion, lmpSubVersion: BluetoothLMPSubversion, hciVersion: UInt8, hciRevision: UInt16)Added BluetoothIOCapabilityResponse.init()Added BluetoothIOCapabilityResponse.init(deviceAddress: BluetoothDeviceAddress, ioCapability: BluetoothIOCapability, OOBDataPresence: BluetoothOOBDataPresence, authenticationRequirements: BluetoothAuthenticationRequirements)Added BluetoothIRK.init()Added BluetoothIRK.init(data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added BluetoothKey.init()Added BluetoothKey.init(data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added BluetoothKeypressNotification.init()Added BluetoothKeypressNotification.init(deviceAddress: BluetoothDeviceAddress, notificationType: BluetoothKeypressNotificationType)Added BluetoothL2CAPQualityOfServiceOptions.init()Added BluetoothL2CAPQualityOfServiceOptions.init(flags: UInt8, serviceType: UInt8, tokenRate: UInt32, tokenBucketSize: UInt32, peakBandwidth: UInt32, latency: UInt32, delayVariation: UInt32)Added BluetoothL2CAPRetransmissionAndFlowControlOptions.init()Added BluetoothL2CAPRetransmissionAndFlowControlOptions.init(flags: UInt8, txWindowSize: UInt8, maxTransmit: UInt8, retransmissionTimeout: UInt16, monitorTimeout: UInt16, maxPDUPayloadSize: UInt16)Added BluetoothLEConnectionInterval [struct]Added BluetoothLEConnectionInterval.init(_: UInt32)Added BluetoothLEConnectionInterval.valueAdded BluetoothPINCode.init()Added BluetoothPINCode.init(data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added BluetoothReadClockInfo.init()Added BluetoothReadClockInfo.init(handle: BluetoothConnectionHandle, clock: UInt32, accuracy: UInt16)Added BluetoothRemoteHostSupportedFeaturesNotification.init()Added BluetoothRemoteHostSupportedFeaturesNotification.init(deviceAddress: BluetoothDeviceAddress, hostSupportedFeatures: BluetoothHCISupportedFeatures)Added BluetoothSetEventMask.init()Added BluetoothSetEventMask.init(data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added BluetoothSynchronousConnectionInfo.init()Added BluetoothSynchronousConnectionInfo.init(transmitBandWidth: BluetoothHCITransmitBandwidth, receiveBandWidth: BluetoothHCIReceiveBandwidth, maxLatency: BluetoothHCIMaxLatency, voiceSetting: BluetoothHCIVoiceSetting, retransmissionEffort: BluetoothHCIRetransmissionEffort, packetType: BluetoothPacketType)Added BluetoothTransportInfo.init()Added BluetoothTransportInfo.init(productID: UInt32, vendorID: UInt32, type: UInt32, productName:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), vendorName:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), totalDataBytesSent: UInt64, totalSCOBytesSent: UInt64, totalDataBytesReceived: UInt64, totalSCOBytesReceived: UInt64)Added BluetoothUserConfirmationRequest.init()Added BluetoothUserConfirmationRequest.init(deviceAddress: BluetoothDeviceAddress, numericValue: BluetoothNumericValue)Added BluetoothUserPasskeyNotification.init()Added BluetoothUserPasskeyNotification.init(deviceAddress: BluetoothDeviceAddress, passkey: BluetoothPasskey)Added IOBluetoothDeviceSearchAttributes.init()Added IOBluetoothDeviceSearchAttributes.init(options: IOBluetoothDeviceSearchOptions, maxResults: IOItemCount, deviceAttributeCount: IOItemCount, attributeList: UnsafeMutablePointer<IOBluetoothDeviceSearchDeviceAttributes>)Added IOBluetoothDeviceSearchDeviceAttributes.init()Added IOBluetoothDeviceSearchDeviceAttributes.init(address: BluetoothDeviceAddress, name: BluetoothDeviceName, serviceClassMajor: BluetoothServiceClassMajor, deviceClassMajor: BluetoothDeviceClassMajor, deviceClassMinor: BluetoothDeviceClassMinor)Added IOBluetoothL2CAPChannelDataBlock.init()Added IOBluetoothL2CAPChannelDataBlock.init(dataPtr: UnsafeMutablePointer<Void>, dataSize: Int)Added IOBluetoothL2CAPChannelEvent.init()Added NSMutableDictionary.init(OBEXHeadersData: NSData!)Added NSMutableDictionary.init(OBEXHeadersData: UnsafePointer<Void>, headersDataSize: Int)Added NSMutableDictionary.addApplicationParameterHeader(UnsafePointer<Void>, length: UInt32) -> OBEXErrorAdded NSMutableDictionary.addAuthorizationChallengeHeader(UnsafePointer<Void>, length: UInt32) -> OBEXErrorAdded NSMutableDictionary.addAuthorizationResponseHeader(UnsafePointer<Void>, length: UInt32) -> OBEXErrorAdded NSMutableDictionary.addBodyHeader(UnsafePointer<Void>, length: UInt32, endOfBody: Bool) -> OBEXErrorAdded NSMutableDictionary.addByteSequenceHeader(UnsafePointer<Void>, length: UInt32) -> OBEXErrorAdded NSMutableDictionary.addConnectionIDHeader(UnsafePointer<Void>, length: UInt32) -> OBEXErrorAdded NSMutableDictionary.addCountHeader(UInt32) -> OBEXErrorAdded NSMutableDictionary.addDescriptionHeader(String!) -> OBEXErrorAdded NSMutableDictionary.addHTTPHeader(UnsafePointer<Void>, length: UInt32) -> OBEXErrorAdded NSMutableDictionary.addImageDescriptorHeader(UnsafePointer<Void>, length: UInt32) -> OBEXErrorAdded NSMutableDictionary.addImageHandleHeader(String!) -> OBEXErrorAdded NSMutableDictionary.addLengthHeader(UInt32) -> OBEXErrorAdded NSMutableDictionary.addNameHeader(String!) -> OBEXErrorAdded NSMutableDictionary.addObjectClassHeader(UnsafePointer<Void>, length: UInt32) -> OBEXErrorAdded NSMutableDictionary.addTargetHeader(UnsafePointer<Void>, length: UInt32) -> OBEXErrorAdded NSMutableDictionary.addTime4ByteHeader(UInt32) -> OBEXErrorAdded NSMutableDictionary.addTimeISOHeader(UnsafePointer<Void>, length: UInt32) -> OBEXErrorAdded NSMutableDictionary.addTypeHeader(String!) -> OBEXErrorAdded NSMutableDictionary.addUserDefinedHeader(UnsafePointer<Void>, length: UInt32) -> OBEXErrorAdded NSMutableDictionary.addWhoHeader(UnsafePointer<Void>, length: UInt32) -> OBEXErrorAdded NSMutableDictionary.getHeaderBytes() -> NSMutableData!Added NSObject.fileTransferServicesAbortComplete(OBEXFileTransferServices!, error: OBEXError)Added NSObject.fileTransferServicesConnectionComplete(OBEXFileTransferServices!, error: OBEXError)Added NSObject.fileTransferServicesCopyRemoteFileComplete(OBEXFileTransferServices!, error: OBEXError)Added NSObject.fileTransferServicesCopyRemoteFileProgress(OBEXFileTransferServices!, transferProgress:[NSObject: AnyObject]!)Added NSObject.fileTransferServicesCreateFolderComplete(OBEXFileTransferServices!, error: OBEXError, folder: String!)Added NSObject.fileTransferServicesDisconnectionComplete(OBEXFileTransferServices!, error: OBEXError)Added NSObject.fileTransferServicesFilePreparationComplete(OBEXFileTransferServices!, error: OBEXError)Added NSObject.fileTransferServicesPathChangeComplete(OBEXFileTransferServices!, error: OBEXError, finalPath: String!)Added NSObject.fileTransferServicesRemoveItemComplete(OBEXFileTransferServices!, error: OBEXError, removedItem: String!)Added NSObject.fileTransferServicesRetrieveFolderListingComplete(OBEXFileTransferServices!, error: OBEXError, listing:[AnyObject]!)Added NSObject.fileTransferServicesSendFileComplete(OBEXFileTransferServices!, error: OBEXError)Added NSObject.fileTransferServicesSendFileProgress(OBEXFileTransferServices!, transferProgress:[NSObject: AnyObject]!)Added NSObject.readLinkQualityForDeviceComplete(AnyObject!, device: IOBluetoothDevice!, info: UnsafeMutablePointer<BluetoothHCILinkQualityInfo>, error: IOReturn)Added NSObject.readRSSIForDeviceComplete(AnyObject!, device: IOBluetoothDevice!, info: UnsafeMutablePointer<BluetoothHCIRSSIInfo>, error: IOReturn)Added OBEXAbortCommandData.init()Added OBEXAbortCommandData.init(headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength: Int)Added OBEXAbortCommandResponseData.init()Added OBEXAbortCommandResponseData.init(serverResponseOpCode: OBEXOpCode, headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength: Int)Added OBEXConnectCommandData.init()Added OBEXConnectCommandData.init(headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength: Int, maxPacketSize: OBEXMaxPacketLength, version: OBEXVersion, flags: OBEXFlags)Added OBEXConnectCommandResponseData.init()Added OBEXConnectCommandResponseData.init(serverResponseOpCode: OBEXOpCode, headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength: Int, maxPacketSize: OBEXMaxPacketLength, version: OBEXVersion, flags: OBEXFlags)Added OBEXDisconnectCommandData.init()Added OBEXDisconnectCommandData.init(headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength: Int)Added OBEXDisconnectCommandResponseData.init()Added OBEXDisconnectCommandResponseData.init(serverResponseOpCode: OBEXOpCode, headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength: Int)Added OBEXErrorData.init()Added OBEXErrorData.init(error: OBEXError, dataPtr: UnsafeMutablePointer<Void>, dataLength: Int)Added OBEXGetCommandData.init()Added OBEXGetCommandData.init(headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength: Int)Added OBEXGetCommandResponseData.init()Added OBEXGetCommandResponseData.init(serverResponseOpCode: OBEXOpCode, headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength: Int)Added OBEXPutCommandData.init()Added OBEXPutCommandData.init(headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength: Int, bodyDataLeftToSend: Int)Added OBEXPutCommandResponseData.init()Added OBEXPutCommandResponseData.init(serverResponseOpCode: OBEXOpCode, headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength: Int)Added OBEXSessionEvent.init()Added OBEXSetPathCommandData.init()Added OBEXSetPathCommandData.init(headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength: Int, flags: OBEXFlags, constants: OBEXConstants)Added OBEXSetPathCommandResponseData.init()Added OBEXSetPathCommandResponseData.init(serverResponseOpCode: OBEXOpCode, headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength: Int, flags: OBEXFlags, constants: OBEXConstants)Added OBEXTransportEvent.init()Added OBEXTransportEvent.init(type: OBEXTransportEventType, status: OBEXError, dataPtr: UnsafeMutablePointer<Void>, dataLength: Int)Added BluetoothLEConnectionIntervalMaxAdded BluetoothLEConnectionIntervalMinAdded kBluetoothL2CAPChannelMagnetAdded kBluetoothSDPUUID16ServiceClassAVRemoteControlControllerModified BluetoothAFHHostChannelClassification [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothAFHHostChannelClassification {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct BluetoothAFHHostChannelClassification {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(data data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified BluetoothAFHResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothAFHResults {     var handle: BluetoothConnectionHandle     var mode: BluetoothAFHMode     var afhMap: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct BluetoothAFHResults {     var handle: BluetoothConnectionHandle     var mode: BluetoothAFHMode     var afhMap: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(handle handle: BluetoothConnectionHandle, mode mode: BluetoothAFHMode, afhMap afhMap: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified BluetoothDeviceAddress [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothDeviceAddress {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct BluetoothDeviceAddress {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(data data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified BluetoothEventFilterCondition [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothEventFilterCondition {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct BluetoothEventFilterCondition {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(data data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified BluetoothHCIAcceptSynchronousConnectionRequestParams [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIAcceptSynchronousConnectionRequestParams {     var transmitBandwidth: UInt32     var receiveBandwidth: UInt32     var maxLatency: UInt16     var contentFormat: UInt16     var retransmissionEffort: UInt8     var packetType: UInt16 } ``` |
| To | ``` struct BluetoothHCIAcceptSynchronousConnectionRequestParams {     var transmitBandwidth: UInt32     var receiveBandwidth: UInt32     var maxLatency: UInt16     var contentFormat: UInt16     var retransmissionEffort: UInt8     var packetType: UInt16     init()     init(transmitBandwidth transmitBandwidth: UInt32, receiveBandwidth receiveBandwidth: UInt32, maxLatency maxLatency: UInt16, contentFormat contentFormat: UInt16, retransmissionEffort retransmissionEffort: UInt8, packetType packetType: UInt16) } ``` |

Modified BluetoothHCIAutomaticFlushTimeoutInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIAutomaticFlushTimeoutInfo {     var handle: BluetoothConnectionHandle     var timeout: BluetoothHCIAutomaticFlushTimeout } ``` |
| To | ``` struct BluetoothHCIAutomaticFlushTimeoutInfo {     var handle: BluetoothConnectionHandle     var timeout: BluetoothHCIAutomaticFlushTimeout     init()     init(handle handle: BluetoothConnectionHandle, timeout timeout: BluetoothHCIAutomaticFlushTimeout) } ``` |

Modified BluetoothHCIBufferSize [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIBufferSize {     var ACLDataPacketLength: UInt16     var SCODataPacketLength: UInt8     var totalNumACLDataPackets: UInt16     var totalNumSCODataPackets: UInt16 } ``` |
| To | ``` struct BluetoothHCIBufferSize {     var ACLDataPacketLength: UInt16     var SCODataPacketLength: UInt8     var totalNumACLDataPackets: UInt16     var totalNumSCODataPackets: UInt16     init()     init(ACLDataPacketLength ACLDataPacketLength: UInt16, SCODataPacketLength SCODataPacketLength: UInt8, totalNumACLDataPackets totalNumACLDataPackets: UInt16, totalNumSCODataPackets totalNumSCODataPackets: UInt16) } ``` |

Modified BluetoothHCICurrentInquiryAccessCodes [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCICurrentInquiryAccessCodes {     var count: BluetoothHCIInquiryAccessCodeCount     var codes: UnsafePointer<BluetoothHCIInquiryAccessCode> } ``` |
| To | ``` struct BluetoothHCICurrentInquiryAccessCodes {     var count: BluetoothHCIInquiryAccessCodeCount     var codes: UnsafeMutablePointer<BluetoothHCIInquiryAccessCode>     init()     init(count count: BluetoothHCIInquiryAccessCodeCount, codes codes: UnsafeMutablePointer<BluetoothHCIInquiryAccessCode>) } ``` |

Modified BluetoothHCICurrentInquiryAccessCodes.codes

|  | Declaration |
| --- | --- |
| From | ``` var codes: UnsafePointer<BluetoothHCIInquiryAccessCode> ``` |
| To | ``` var codes: UnsafeMutablePointer<BluetoothHCIInquiryAccessCode> ``` |

Modified BluetoothHCIEventAuthenticationCompleteResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventAuthenticationCompleteResults {     var connectionHandle: BluetoothConnectionHandle } ``` |
| To | ``` struct BluetoothHCIEventAuthenticationCompleteResults {     var connectionHandle: BluetoothConnectionHandle     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle) } ``` |

Modified BluetoothHCIEventChangeConnectionLinkKeyCompleteResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventChangeConnectionLinkKeyCompleteResults {     var connectionHandle: BluetoothConnectionHandle } ``` |
| To | ``` struct BluetoothHCIEventChangeConnectionLinkKeyCompleteResults {     var connectionHandle: BluetoothConnectionHandle     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle) } ``` |

Modified BluetoothHCIEventConnectionCompleteResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventConnectionCompleteResults {     var connectionHandle: BluetoothConnectionHandle     var deviceAddress: BluetoothDeviceAddress     var linkType: BluetoothLinkType     var encryptionMode: BluetoothHCIEncryptionMode } ``` |
| To | ``` struct BluetoothHCIEventConnectionCompleteResults {     var connectionHandle: BluetoothConnectionHandle     var deviceAddress: BluetoothDeviceAddress     var linkType: BluetoothLinkType     var encryptionMode: BluetoothHCIEncryptionMode     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, deviceAddress deviceAddress: BluetoothDeviceAddress, linkType linkType: BluetoothLinkType, encryptionMode encryptionMode: BluetoothHCIEncryptionMode) } ``` |

Modified BluetoothHCIEventConnectionPacketTypeResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventConnectionPacketTypeResults {     var connectionHandle: BluetoothConnectionHandle     var packetType: BluetoothPacketType } ``` |
| To | ``` struct BluetoothHCIEventConnectionPacketTypeResults {     var connectionHandle: BluetoothConnectionHandle     var packetType: BluetoothPacketType     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, packetType packetType: BluetoothPacketType) } ``` |

Modified BluetoothHCIEventConnectionRequestResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventConnectionRequestResults {     var deviceAddress: BluetoothDeviceAddress     var classOfDevice: BluetoothClassOfDevice     var linkType: BluetoothLinkType } ``` |
| To | ``` struct BluetoothHCIEventConnectionRequestResults {     var deviceAddress: BluetoothDeviceAddress     var classOfDevice: BluetoothClassOfDevice     var linkType: BluetoothLinkType     init()     init(deviceAddress deviceAddress: BluetoothDeviceAddress, classOfDevice classOfDevice: BluetoothClassOfDevice, linkType linkType: BluetoothLinkType) } ``` |

Modified BluetoothHCIEventDataBufferOverflowResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventDataBufferOverflowResults {     var linkType: BluetoothLinkType } ``` |
| To | ``` struct BluetoothHCIEventDataBufferOverflowResults {     var linkType: BluetoothLinkType     init()     init(linkType linkType: BluetoothLinkType) } ``` |

Modified BluetoothHCIEventDisconnectionCompleteResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventDisconnectionCompleteResults {     var connectionHandle: BluetoothConnectionHandle     var reason: BluetoothReasonCode } ``` |
| To | ``` struct BluetoothHCIEventDisconnectionCompleteResults {     var connectionHandle: BluetoothConnectionHandle     var reason: BluetoothReasonCode     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, reason reason: BluetoothReasonCode) } ``` |

Modified BluetoothHCIEventEncryptionChangeResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventEncryptionChangeResults {     var connectionHandle: BluetoothConnectionHandle     var enable: BluetoothEncryptionEnable } ``` |
| To | ``` struct BluetoothHCIEventEncryptionChangeResults {     var connectionHandle: BluetoothConnectionHandle     var enable: BluetoothEncryptionEnable     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, enable enable: BluetoothEncryptionEnable) } ``` |

Modified BluetoothHCIEventEncryptionKeyRefreshCompleteResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventEncryptionKeyRefreshCompleteResults {     var connectionHandle: BluetoothConnectionHandle } ``` |
| To | ``` struct BluetoothHCIEventEncryptionKeyRefreshCompleteResults {     var connectionHandle: BluetoothConnectionHandle     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle) } ``` |

Modified BluetoothHCIEventFlowSpecificationData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventFlowSpecificationData {     var connectionHandle: BluetoothConnectionHandle     var flags: UInt8     var flowDirection: UInt8     var serviceType: UInt8     var tokenRate: UInt32     var tokenBucketSize: UInt32     var peakBandwidth: UInt32     var accessLatency: UInt32 } ``` |
| To | ``` struct BluetoothHCIEventFlowSpecificationData {     var connectionHandle: BluetoothConnectionHandle     var flags: UInt8     var flowDirection: UInt8     var serviceType: UInt8     var tokenRate: UInt32     var tokenBucketSize: UInt32     var peakBandwidth: UInt32     var accessLatency: UInt32     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, flags flags: UInt8, flowDirection flowDirection: UInt8, serviceType serviceType: UInt8, tokenRate tokenRate: UInt32, tokenBucketSize tokenBucketSize: UInt32, peakBandwidth peakBandwidth: UInt32, accessLatency accessLatency: UInt32) } ``` |

Modified BluetoothHCIEventFlushOccurredResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventFlushOccurredResults {     var connectionHandle: BluetoothConnectionHandle } ``` |
| To | ``` struct BluetoothHCIEventFlushOccurredResults {     var connectionHandle: BluetoothConnectionHandle     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle) } ``` |

Modified BluetoothHCIEventHardwareErrorResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventHardwareErrorResults {     var error: BluetoothHCIStatus } ``` |
| To | ``` struct BluetoothHCIEventHardwareErrorResults {     var error: BluetoothHCIStatus     init()     init(error error: BluetoothHCIStatus) } ``` |

Modified BluetoothHCIEventLEConnectionCompleteResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventLEConnectionCompleteResults {     var connectionHandle: BluetoothConnectionHandle     var role: UInt8     var peerAddressType: UInt8     var peerAddress: BluetoothDeviceAddress     var connInterval: UInt16     var connLatency: UInt16     var supervisionTimeout: UInt16     var masterClockAccuracy: UInt8 } ``` |
| To | ``` struct BluetoothHCIEventLEConnectionCompleteResults {     var connectionHandle: BluetoothConnectionHandle     var role: UInt8     var peerAddressType: UInt8     var peerAddress: BluetoothDeviceAddress     var connInterval: UInt16     var connLatency: UInt16     var supervisionTimeout: UInt16     var masterClockAccuracy: UInt8     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, role role: UInt8, peerAddressType peerAddressType: UInt8, peerAddress peerAddress: BluetoothDeviceAddress, connInterval connInterval: UInt16, connLatency connLatency: UInt16, supervisionTimeout supervisionTimeout: UInt16, masterClockAccuracy masterClockAccuracy: UInt8) } ``` |

Modified BluetoothHCIEventLEConnectionUpdateCompleteResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventLEConnectionUpdateCompleteResults {     var connectionHandle: BluetoothConnectionHandle     var connInterval: UInt16     var connLatency: UInt16     var supervisionTimeout: UInt16 } ``` |
| To | ``` struct BluetoothHCIEventLEConnectionUpdateCompleteResults {     var connectionHandle: BluetoothConnectionHandle     var connInterval: UInt16     var connLatency: UInt16     var supervisionTimeout: UInt16     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, connInterval connInterval: UInt16, connLatency connLatency: UInt16, supervisionTimeout supervisionTimeout: UInt16) } ``` |

Modified BluetoothHCIEventLELongTermKeyRequestResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventLELongTermKeyRequestResults {     var connectionHandle: BluetoothConnectionHandle     var randomNumber: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var ediv: UInt16 } ``` |
| To | ``` struct BluetoothHCIEventLELongTermKeyRequestResults {     var connectionHandle: BluetoothConnectionHandle     var randomNumber: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var ediv: UInt16     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, randomNumber randomNumber: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), ediv ediv: UInt16) } ``` |

Modified BluetoothHCIEventLEMetaResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventLEMetaResults {     var length: UInt8     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct BluetoothHCIEventLEMetaResults {     var length: UInt8     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(length length: UInt8, data data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified BluetoothHCIEventLinkKeyNotificationResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventLinkKeyNotificationResults {     var deviceAddress: BluetoothDeviceAddress     var linkKey: BluetoothKey     var keyType: BluetoothKeyType } ``` |
| To | ``` struct BluetoothHCIEventLinkKeyNotificationResults {     var deviceAddress: BluetoothDeviceAddress     var linkKey: BluetoothKey     var keyType: BluetoothKeyType     init()     init(deviceAddress deviceAddress: BluetoothDeviceAddress, linkKey linkKey: BluetoothKey, keyType keyType: BluetoothKeyType) } ``` |

Modified BluetoothHCIEventMasterLinkKeyCompleteResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventMasterLinkKeyCompleteResults {     var connectionHandle: BluetoothConnectionHandle     var keyFlag: BluetoothKeyFlag } ``` |
| To | ``` struct BluetoothHCIEventMasterLinkKeyCompleteResults {     var connectionHandle: BluetoothConnectionHandle     var keyFlag: BluetoothKeyFlag     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, keyFlag keyFlag: BluetoothKeyFlag) } ``` |

Modified BluetoothHCIEventMaxSlotsChangeResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventMaxSlotsChangeResults {     var connectionHandle: BluetoothConnectionHandle     var maxSlots: BluetoothMaxSlots } ``` |
| To | ``` struct BluetoothHCIEventMaxSlotsChangeResults {     var connectionHandle: BluetoothConnectionHandle     var maxSlots: BluetoothMaxSlots     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, maxSlots maxSlots: BluetoothMaxSlots) } ``` |

Modified BluetoothHCIEventModeChangeResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventModeChangeResults {     var connectionHandle: BluetoothConnectionHandle     var mode: BluetoothHCIConnectionMode     var modeInterval: BluetoothHCIModeInterval } ``` |
| To | ``` struct BluetoothHCIEventModeChangeResults {     var connectionHandle: BluetoothConnectionHandle     var mode: BluetoothHCIConnectionMode     var modeInterval: BluetoothHCIModeInterval     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, mode mode: BluetoothHCIConnectionMode, modeInterval modeInterval: BluetoothHCIModeInterval) } ``` |

Modified BluetoothHCIEventPageScanModeChangeResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventPageScanModeChangeResults {     var deviceAddress: BluetoothDeviceAddress     var pageScanMode: BluetoothPageScanMode } ``` |
| To | ``` struct BluetoothHCIEventPageScanModeChangeResults {     var deviceAddress: BluetoothDeviceAddress     var pageScanMode: BluetoothPageScanMode     init()     init(deviceAddress deviceAddress: BluetoothDeviceAddress, pageScanMode pageScanMode: BluetoothPageScanMode) } ``` |

Modified BluetoothHCIEventPageScanRepetitionModeChangeResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventPageScanRepetitionModeChangeResults {     var deviceAddress: BluetoothDeviceAddress     var pageScanRepetitionMode: BluetoothPageScanRepetitionMode } ``` |
| To | ``` struct BluetoothHCIEventPageScanRepetitionModeChangeResults {     var deviceAddress: BluetoothDeviceAddress     var pageScanRepetitionMode: BluetoothPageScanRepetitionMode     init()     init(deviceAddress deviceAddress: BluetoothDeviceAddress, pageScanRepetitionMode pageScanRepetitionMode: BluetoothPageScanRepetitionMode) } ``` |

Modified BluetoothHCIEventQoSSetupCompleteResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventQoSSetupCompleteResults {     var connectionHandle: BluetoothConnectionHandle     var setupParams: BluetoothHCIQualityOfServiceSetupParams } ``` |
| To | ``` struct BluetoothHCIEventQoSSetupCompleteResults {     var connectionHandle: BluetoothConnectionHandle     var setupParams: BluetoothHCIQualityOfServiceSetupParams     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, setupParams setupParams: BluetoothHCIQualityOfServiceSetupParams) } ``` |

Modified BluetoothHCIEventQoSViolationResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventQoSViolationResults {     var connectionHandle: BluetoothConnectionHandle } ``` |
| To | ``` struct BluetoothHCIEventQoSViolationResults {     var connectionHandle: BluetoothConnectionHandle     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle) } ``` |

Modified BluetoothHCIEventReadClockOffsetResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventReadClockOffsetResults {     var connectionHandle: BluetoothConnectionHandle     var clockOffset: BluetoothClockOffset } ``` |
| To | ``` struct BluetoothHCIEventReadClockOffsetResults {     var connectionHandle: BluetoothConnectionHandle     var clockOffset: BluetoothClockOffset     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, clockOffset clockOffset: BluetoothClockOffset) } ``` |

Modified BluetoothHCIEventReadExtendedFeaturesResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventReadExtendedFeaturesResults {     var connectionHandle: BluetoothConnectionHandle     var supportedFeaturesInfo: BluetoothHCIExtendedFeaturesInfo } ``` |
| To | ``` struct BluetoothHCIEventReadExtendedFeaturesResults {     var connectionHandle: BluetoothConnectionHandle     var supportedFeaturesInfo: BluetoothHCIExtendedFeaturesInfo     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, supportedFeaturesInfo supportedFeaturesInfo: BluetoothHCIExtendedFeaturesInfo) } ``` |

Modified BluetoothHCIEventReadRemoteExtendedFeaturesResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventReadRemoteExtendedFeaturesResults {     var error: BluetoothHCIStatus     var connectionHandle: BluetoothConnectionHandle     var page: BluetoothHCIPageNumber     var maxPage: BluetoothHCIPageNumber     var lmpFeatures: BluetoothHCISupportedFeatures } ``` |
| To | ``` struct BluetoothHCIEventReadRemoteExtendedFeaturesResults {     var error: BluetoothHCIStatus     var connectionHandle: BluetoothConnectionHandle     var page: BluetoothHCIPageNumber     var maxPage: BluetoothHCIPageNumber     var lmpFeatures: BluetoothHCISupportedFeatures     init()     init(error error: BluetoothHCIStatus, connectionHandle connectionHandle: BluetoothConnectionHandle, page page: BluetoothHCIPageNumber, maxPage maxPage: BluetoothHCIPageNumber, lmpFeatures lmpFeatures: BluetoothHCISupportedFeatures) } ``` |

Modified BluetoothHCIEventReadRemoteSupportedFeaturesResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventReadRemoteSupportedFeaturesResults {     var error: BluetoothHCIStatus     var connectionHandle: BluetoothConnectionHandle     var lmpFeatures: BluetoothHCISupportedFeatures } ``` |
| To | ``` struct BluetoothHCIEventReadRemoteSupportedFeaturesResults {     var error: BluetoothHCIStatus     var connectionHandle: BluetoothConnectionHandle     var lmpFeatures: BluetoothHCISupportedFeatures     init()     init(error error: BluetoothHCIStatus, connectionHandle connectionHandle: BluetoothConnectionHandle, lmpFeatures lmpFeatures: BluetoothHCISupportedFeatures) } ``` |

Modified BluetoothHCIEventReadRemoteVersionInfoResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventReadRemoteVersionInfoResults {     var connectionHandle: BluetoothConnectionHandle     var lmpVersion: BluetoothLMPVersion     var manufacturerName: BluetoothManufacturerName     var lmpSubversion: BluetoothLMPSubversion } ``` |
| To | ``` struct BluetoothHCIEventReadRemoteVersionInfoResults {     var connectionHandle: BluetoothConnectionHandle     var lmpVersion: BluetoothLMPVersion     var manufacturerName: BluetoothManufacturerName     var lmpSubversion: BluetoothLMPSubversion     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, lmpVersion lmpVersion: BluetoothLMPVersion, manufacturerName manufacturerName: BluetoothManufacturerName, lmpSubversion lmpSubversion: BluetoothLMPSubversion) } ``` |

Modified BluetoothHCIEventReadSupportedFeaturesResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventReadSupportedFeaturesResults {     var connectionHandle: BluetoothConnectionHandle     var supportedFeatures: BluetoothHCISupportedFeatures } ``` |
| To | ``` struct BluetoothHCIEventReadSupportedFeaturesResults {     var connectionHandle: BluetoothConnectionHandle     var supportedFeatures: BluetoothHCISupportedFeatures     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, supportedFeatures supportedFeatures: BluetoothHCISupportedFeatures) } ``` |

Modified BluetoothHCIEventRemoteNameRequestResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventRemoteNameRequestResults {     var deviceAddress: BluetoothDeviceAddress     var deviceName: BluetoothDeviceName } ``` |
| To | ``` struct BluetoothHCIEventRemoteNameRequestResults {     var deviceAddress: BluetoothDeviceAddress     var deviceName: BluetoothDeviceName     init()     init(deviceAddress deviceAddress: BluetoothDeviceAddress, deviceName deviceName: BluetoothDeviceName) } ``` |

Modified BluetoothHCIEventReturnLinkKeysResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventReturnLinkKeysResults {     var numLinkKeys: UInt8 } ``` |
| To | ``` struct BluetoothHCIEventReturnLinkKeysResults {     var numLinkKeys: UInt8     init() } ``` |

Modified BluetoothHCIEventRoleChangeResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventRoleChangeResults {     var connectionHandle: BluetoothConnectionHandle     var deviceAddress: BluetoothDeviceAddress     var role: BluetoothRole } ``` |
| To | ``` struct BluetoothHCIEventRoleChangeResults {     var connectionHandle: BluetoothConnectionHandle     var deviceAddress: BluetoothDeviceAddress     var role: BluetoothRole     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, deviceAddress deviceAddress: BluetoothDeviceAddress, role role: BluetoothRole) } ``` |

Modified BluetoothHCIEventSimplePairingCompleteResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventSimplePairingCompleteResults {     var deviceAddress: BluetoothDeviceAddress } ``` |
| To | ``` struct BluetoothHCIEventSimplePairingCompleteResults {     var deviceAddress: BluetoothDeviceAddress     init()     init(deviceAddress deviceAddress: BluetoothDeviceAddress) } ``` |

Modified BluetoothHCIEventSniffSubratingResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventSniffSubratingResults {     var connectionHandle: BluetoothConnectionHandle     var maxTransmitLatency: UInt16     var maxReceiveLatency: UInt16     var minRemoteTimeout: UInt16     var minLocalTimeout: UInt16 } ``` |
| To | ``` struct BluetoothHCIEventSniffSubratingResults {     var connectionHandle: BluetoothConnectionHandle     var maxTransmitLatency: UInt16     var maxReceiveLatency: UInt16     var minRemoteTimeout: UInt16     var minLocalTimeout: UInt16     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, maxTransmitLatency maxTransmitLatency: UInt16, maxReceiveLatency maxReceiveLatency: UInt16, minRemoteTimeout minRemoteTimeout: UInt16, minLocalTimeout minLocalTimeout: UInt16) } ``` |

Modified BluetoothHCIEventSynchronousConnectionChangedResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventSynchronousConnectionChangedResults {     var connectionHandle: BluetoothConnectionHandle     var transmissionInterval: UInt8     var retransmissionWindow: UInt8     var receivePacketLength: UInt16     var transmitPacketLength: UInt16 } ``` |
| To | ``` struct BluetoothHCIEventSynchronousConnectionChangedResults {     var connectionHandle: BluetoothConnectionHandle     var transmissionInterval: UInt8     var retransmissionWindow: UInt8     var receivePacketLength: UInt16     var transmitPacketLength: UInt16     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, transmissionInterval transmissionInterval: UInt8, retransmissionWindow retransmissionWindow: UInt8, receivePacketLength receivePacketLength: UInt16, transmitPacketLength transmitPacketLength: UInt16) } ``` |

Modified BluetoothHCIEventSynchronousConnectionCompleteResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventSynchronousConnectionCompleteResults {     var connectionHandle: BluetoothConnectionHandle     var deviceAddress: BluetoothDeviceAddress     var linkType: BluetoothLinkType     var transmissionInterval: UInt8     var retransmissionWindow: UInt8     var receivePacketLength: UInt16     var transmitPacketLength: UInt16     var airMode: BluetoothAirMode } ``` |
| To | ``` struct BluetoothHCIEventSynchronousConnectionCompleteResults {     var connectionHandle: BluetoothConnectionHandle     var deviceAddress: BluetoothDeviceAddress     var linkType: BluetoothLinkType     var transmissionInterval: UInt8     var retransmissionWindow: UInt8     var receivePacketLength: UInt16     var transmitPacketLength: UInt16     var airMode: BluetoothAirMode     init()     init(connectionHandle connectionHandle: BluetoothConnectionHandle, deviceAddress deviceAddress: BluetoothDeviceAddress, linkType linkType: BluetoothLinkType, transmissionInterval transmissionInterval: UInt8, retransmissionWindow retransmissionWindow: UInt8, receivePacketLength receivePacketLength: UInt16, transmitPacketLength transmitPacketLength: UInt16, airMode airMode: BluetoothAirMode) } ``` |

Modified BluetoothHCIEventVendorSpecificResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIEventVendorSpecificResults {     var length: UInt8     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct BluetoothHCIEventVendorSpecificResults {     var length: UInt8     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(length length: UInt8, data data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified BluetoothHCIExtendedFeaturesInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIExtendedFeaturesInfo {     var page: BluetoothHCIPageNumber     var maxPage: BluetoothHCIPageNumber     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct BluetoothHCIExtendedFeaturesInfo {     var page: BluetoothHCIPageNumber     var maxPage: BluetoothHCIPageNumber     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(page page: BluetoothHCIPageNumber, maxPage maxPage: BluetoothHCIPageNumber, data data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified BluetoothHCIExtendedInquiryResponse [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIExtendedInquiryResponse {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct BluetoothHCIExtendedInquiryResponse {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(data data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified BluetoothHCIExtendedInquiryResult [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIExtendedInquiryResult {     var numberOfReponses: UInt8     var deviceAddress: BluetoothDeviceAddress     var pageScanRepetitionMode: BluetoothPageScanRepetitionMode     var reserved: UInt8     var classOfDevice: BluetoothClassOfDevice     var clockOffset: BluetoothClockOffset     var RSSIValue: BluetoothHCIRSSIValue     var extendedInquiryResponse: BluetoothHCIExtendedInquiryResponse } ``` |
| To | ``` struct BluetoothHCIExtendedInquiryResult {     var numberOfReponses: UInt8     var deviceAddress: BluetoothDeviceAddress     var pageScanRepetitionMode: BluetoothPageScanRepetitionMode     var reserved: UInt8     var classOfDevice: BluetoothClassOfDevice     var clockOffset: BluetoothClockOffset     var RSSIValue: BluetoothHCIRSSIValue     var extendedInquiryResponse: BluetoothHCIExtendedInquiryResponse     init()     init(numberOfReponses numberOfReponses: UInt8, deviceAddress deviceAddress: BluetoothDeviceAddress, pageScanRepetitionMode pageScanRepetitionMode: BluetoothPageScanRepetitionMode, reserved reserved: UInt8, classOfDevice classOfDevice: BluetoothClassOfDevice, clockOffset clockOffset: BluetoothClockOffset, RSSIValue RSSIValue: BluetoothHCIRSSIValue, extendedInquiryResponse extendedInquiryResponse: BluetoothHCIExtendedInquiryResponse) } ``` |

Modified BluetoothHCIFailedContactInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIFailedContactInfo {     var count: BluetoothHCIFailedContactCount     var handle: BluetoothConnectionHandle } ``` |
| To | ``` struct BluetoothHCIFailedContactInfo {     var count: BluetoothHCIFailedContactCount     var handle: BluetoothConnectionHandle     init()     init(count count: BluetoothHCIFailedContactCount, handle handle: BluetoothConnectionHandle) } ``` |

Modified BluetoothHCIInquiryAccessCode [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIInquiryAccessCode {     var data: (UInt8, UInt8, UInt8) } ``` |
| To | ``` struct BluetoothHCIInquiryAccessCode {     var data: (UInt8, UInt8, UInt8)     init()     init(data data: (UInt8, UInt8, UInt8)) } ``` |

Modified BluetoothHCIInquiryResult [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIInquiryResult {     var deviceAddress: BluetoothDeviceAddress     var pageScanRepetitionMode: BluetoothPageScanRepetitionMode     var pageScanPeriodMode: BluetoothHCIPageScanPeriodMode     var pageScanMode: BluetoothHCIPageScanMode     var classOfDevice: BluetoothClassOfDevice     var clockOffset: BluetoothClockOffset } ``` |
| To | ``` struct BluetoothHCIInquiryResult {     var deviceAddress: BluetoothDeviceAddress     var pageScanRepetitionMode: BluetoothPageScanRepetitionMode     var pageScanPeriodMode: BluetoothHCIPageScanPeriodMode     var pageScanMode: BluetoothHCIPageScanMode     var classOfDevice: BluetoothClassOfDevice     var clockOffset: BluetoothClockOffset     init()     init(deviceAddress deviceAddress: BluetoothDeviceAddress, pageScanRepetitionMode pageScanRepetitionMode: BluetoothPageScanRepetitionMode, pageScanPeriodMode pageScanPeriodMode: BluetoothHCIPageScanPeriodMode, pageScanMode pageScanMode: BluetoothHCIPageScanMode, classOfDevice classOfDevice: BluetoothClassOfDevice, clockOffset clockOffset: BluetoothClockOffset) } ``` |

Modified BluetoothHCIInquiryResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIInquiryResults {     var results: (BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult)     var count: IOItemCount } ``` |
| To | ``` struct BluetoothHCIInquiryResults {     var results: (BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult)     var count: IOItemCount     init()     init(results results: (BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult, BluetoothHCIInquiryResult), count count: IOItemCount) } ``` |

Modified BluetoothHCIInquiryWithRSSIResult [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIInquiryWithRSSIResult {     var deviceAddress: BluetoothDeviceAddress     var pageScanRepetitionMode: BluetoothPageScanRepetitionMode     var reserved: UInt8     var classOfDevice: BluetoothClassOfDevice     var clockOffset: BluetoothClockOffset     var RSSIValue: BluetoothHCIRSSIValue } ``` |
| To | ``` struct BluetoothHCIInquiryWithRSSIResult {     var deviceAddress: BluetoothDeviceAddress     var pageScanRepetitionMode: BluetoothPageScanRepetitionMode     var reserved: UInt8     var classOfDevice: BluetoothClassOfDevice     var clockOffset: BluetoothClockOffset     var RSSIValue: BluetoothHCIRSSIValue     init()     init(deviceAddress deviceAddress: BluetoothDeviceAddress, pageScanRepetitionMode pageScanRepetitionMode: BluetoothPageScanRepetitionMode, reserved reserved: UInt8, classOfDevice classOfDevice: BluetoothClassOfDevice, clockOffset clockOffset: BluetoothClockOffset, RSSIValue RSSIValue: BluetoothHCIRSSIValue) } ``` |

Modified BluetoothHCIInquiryWithRSSIResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIInquiryWithRSSIResults {     var results: (BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult)     var count: IOItemCount } ``` |
| To | ``` struct BluetoothHCIInquiryWithRSSIResults {     var results: (BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult)     var count: IOItemCount     init()     init(results results: (BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult, BluetoothHCIInquiryWithRSSIResult), count count: IOItemCount) } ``` |

Modified BluetoothHCILEBufferSize [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCILEBufferSize {     var ACLDataPacketLength: UInt16     var totalNumACLDataPackets: UInt8 } ``` |
| To | ``` struct BluetoothHCILEBufferSize {     var ACLDataPacketLength: UInt16     var totalNumACLDataPackets: UInt8     init()     init(ACLDataPacketLength ACLDataPacketLength: UInt16, totalNumACLDataPackets totalNumACLDataPackets: UInt8) } ``` |

Modified BluetoothHCILinkPolicySettingsInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCILinkPolicySettingsInfo {     var settings: BluetoothHCILinkPolicySettings     var handle: BluetoothConnectionHandle } ``` |
| To | ``` struct BluetoothHCILinkPolicySettingsInfo {     var settings: BluetoothHCILinkPolicySettings     var handle: BluetoothConnectionHandle     init()     init(settings settings: BluetoothHCILinkPolicySettings, handle handle: BluetoothConnectionHandle) } ``` |

Modified BluetoothHCILinkQualityInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCILinkQualityInfo {     var handle: BluetoothConnectionHandle     var qualityValue: BluetoothHCILinkQuality } ``` |
| To | ``` struct BluetoothHCILinkQualityInfo {     var handle: BluetoothConnectionHandle     var qualityValue: BluetoothHCILinkQuality     init()     init(handle handle: BluetoothConnectionHandle, qualityValue qualityValue: BluetoothHCILinkQuality) } ``` |

Modified BluetoothHCILinkSupervisionTimeout [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCILinkSupervisionTimeout {     var handle: BluetoothConnectionHandle     var timeout: UInt16 } ``` |
| To | ``` struct BluetoothHCILinkSupervisionTimeout {     var handle: BluetoothConnectionHandle     var timeout: UInt16     init()     init(handle handle: BluetoothConnectionHandle, timeout timeout: UInt16) } ``` |

Modified BluetoothHCIQualityOfServiceSetupParams [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIQualityOfServiceSetupParams {     var flags: UInt8     var serviceType: UInt8     var tokenRate: UInt32     var peakBandwidth: UInt32     var latency: UInt32     var delayVariation: UInt32 } ``` |
| To | ``` struct BluetoothHCIQualityOfServiceSetupParams {     var flags: UInt8     var serviceType: UInt8     var tokenRate: UInt32     var peakBandwidth: UInt32     var latency: UInt32     var delayVariation: UInt32     init()     init(flags flags: UInt8, serviceType serviceType: UInt8, tokenRate tokenRate: UInt32, peakBandwidth peakBandwidth: UInt32, latency latency: UInt32, delayVariation delayVariation: UInt32) } ``` |

Modified BluetoothHCIRSSIInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIRSSIInfo {     var handle: BluetoothConnectionHandle     var RSSIValue: BluetoothHCIRSSIValue } ``` |
| To | ``` struct BluetoothHCIRSSIInfo {     var handle: BluetoothConnectionHandle     var RSSIValue: BluetoothHCIRSSIValue     init()     init(handle handle: BluetoothConnectionHandle, RSSIValue RSSIValue: BluetoothHCIRSSIValue) } ``` |

Modified BluetoothHCIReadExtendedInquiryResponseResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIReadExtendedInquiryResponseResults {     var outFECRequired: BluetoothHCIFECRequired     var extendedInquiryResponse: BluetoothHCIExtendedInquiryResponse } ``` |
| To | ``` struct BluetoothHCIReadExtendedInquiryResponseResults {     var outFECRequired: BluetoothHCIFECRequired     var extendedInquiryResponse: BluetoothHCIExtendedInquiryResponse     init()     init(outFECRequired outFECRequired: BluetoothHCIFECRequired, extendedInquiryResponse extendedInquiryResponse: BluetoothHCIExtendedInquiryResponse) } ``` |

Modified BluetoothHCIReadLMPHandleResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIReadLMPHandleResults {     var handle: BluetoothConnectionHandle     var lmp_handle: BluetoothLMPHandle     var reserved: UInt32 } ``` |
| To | ``` struct BluetoothHCIReadLMPHandleResults {     var handle: BluetoothConnectionHandle     var lmp_handle: BluetoothLMPHandle     var reserved: UInt32     init()     init(handle handle: BluetoothConnectionHandle, lmp_handle lmp_handle: BluetoothLMPHandle, reserved reserved: UInt32) } ``` |

Modified BluetoothHCIReadLocalOOBDataResults [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIReadLocalOOBDataResults {     var hash: BluetoothHCISimplePairingOOBData     var randomizer: BluetoothHCISimplePairingOOBData } ``` |
| To | ``` struct BluetoothHCIReadLocalOOBDataResults {     var hash: BluetoothHCISimplePairingOOBData     var randomizer: BluetoothHCISimplePairingOOBData     init()     init(hash hash: BluetoothHCISimplePairingOOBData, randomizer randomizer: BluetoothHCISimplePairingOOBData) } ``` |

Modified BluetoothHCIRequestCallbackInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIRequestCallbackInfo {     var userCallback: mach_vm_address_t     var userRefCon: mach_vm_address_t     var internalRefCon: mach_vm_address_t     var asyncIDRefCon: mach_vm_address_t     var reserved: mach_vm_address_t } ``` |
| To | ``` struct BluetoothHCIRequestCallbackInfo {     var userCallback: mach_vm_address_t     var userRefCon: mach_vm_address_t     var internalRefCon: mach_vm_address_t     var asyncIDRefCon: mach_vm_address_t     var reserved: mach_vm_address_t     init()     init(userCallback userCallback: mach_vm_address_t, userRefCon userRefCon: mach_vm_address_t, internalRefCon internalRefCon: mach_vm_address_t, asyncIDRefCon asyncIDRefCon: mach_vm_address_t, reserved reserved: mach_vm_address_t) } ``` |

Modified BluetoothHCIRoleInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIRoleInfo {     var role: UInt8     var handle: BluetoothConnectionHandle } ``` |
| To | ``` struct BluetoothHCIRoleInfo {     var role: UInt8     var handle: BluetoothConnectionHandle     init()     init(role role: UInt8, handle handle: BluetoothConnectionHandle) } ``` |

Modified BluetoothHCIScanActivity [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIScanActivity {     var scanInterval: UInt16     var scanWindow: UInt16 } ``` |
| To | ``` struct BluetoothHCIScanActivity {     var scanInterval: UInt16     var scanWindow: UInt16     init()     init(scanInterval scanInterval: UInt16, scanWindow scanWindow: UInt16) } ``` |

Modified BluetoothHCISetupSynchronousConnectionParams [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCISetupSynchronousConnectionParams {     var transmitBandwidth: UInt32     var receiveBandwidth: UInt32     var maxLatency: UInt16     var voiceSetting: UInt16     var retransmissionEffort: UInt8     var packetType: UInt16 } ``` |
| To | ``` struct BluetoothHCISetupSynchronousConnectionParams {     var transmitBandwidth: UInt32     var receiveBandwidth: UInt32     var maxLatency: UInt16     var voiceSetting: UInt16     var retransmissionEffort: UInt8     var packetType: UInt16     init()     init(transmitBandwidth transmitBandwidth: UInt32, receiveBandwidth receiveBandwidth: UInt32, maxLatency maxLatency: UInt16, voiceSetting voiceSetting: UInt16, retransmissionEffort retransmissionEffort: UInt8, packetType packetType: UInt16) } ``` |

Modified BluetoothHCISimplePairingOOBData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCISimplePairingOOBData {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct BluetoothHCISimplePairingOOBData {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(data data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified BluetoothHCIStoredLinkKeysInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIStoredLinkKeysInfo {     var numLinkKeysRead: UInt16     var maxNumLinkKeysAllowedInDevice: UInt16 } ``` |
| To | ``` struct BluetoothHCIStoredLinkKeysInfo {     var numLinkKeysRead: UInt16     var maxNumLinkKeysAllowedInDevice: UInt16     init()     init(numLinkKeysRead numLinkKeysRead: UInt16, maxNumLinkKeysAllowedInDevice maxNumLinkKeysAllowedInDevice: UInt16) } ``` |

Modified BluetoothHCISupportedCommands [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCISupportedCommands {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct BluetoothHCISupportedCommands {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(data data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified BluetoothHCISupportedFeatures [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCISupportedFeatures {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct BluetoothHCISupportedFeatures {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(data data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified BluetoothHCITransmitPowerLevelInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCITransmitPowerLevelInfo {     var handle: BluetoothConnectionHandle     var level: BluetoothHCITransmitPowerLevel } ``` |
| To | ``` struct BluetoothHCITransmitPowerLevelInfo {     var handle: BluetoothConnectionHandle     var level: BluetoothHCITransmitPowerLevel     init()     init(handle handle: BluetoothConnectionHandle, level level: BluetoothHCITransmitPowerLevel) } ``` |

Modified BluetoothHCIVersionInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothHCIVersionInfo {     var manufacturerName: BluetoothManufacturerName     var lmpVersion: BluetoothLMPVersion     var lmpSubVersion: BluetoothLMPSubversion     var hciVersion: UInt8     var hciRevision: UInt16 } ``` |
| To | ``` struct BluetoothHCIVersionInfo {     var manufacturerName: BluetoothManufacturerName     var lmpVersion: BluetoothLMPVersion     var lmpSubVersion: BluetoothLMPSubversion     var hciVersion: UInt8     var hciRevision: UInt16     init()     init(manufacturerName manufacturerName: BluetoothManufacturerName, lmpVersion lmpVersion: BluetoothLMPVersion, lmpSubVersion lmpSubVersion: BluetoothLMPSubversion, hciVersion hciVersion: UInt8, hciRevision hciRevision: UInt16) } ``` |

Modified BluetoothIOCapabilityResponse [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothIOCapabilityResponse {     var deviceAddress: BluetoothDeviceAddress     var ioCapability: BluetoothIOCapability     var OOBDataPresence: BluetoothOOBDataPresence     var authenticationRequirements: BluetoothAuthenticationRequirements } ``` |
| To | ``` struct BluetoothIOCapabilityResponse {     var deviceAddress: BluetoothDeviceAddress     var ioCapability: BluetoothIOCapability     var OOBDataPresence: BluetoothOOBDataPresence     var authenticationRequirements: BluetoothAuthenticationRequirements     init()     init(deviceAddress deviceAddress: BluetoothDeviceAddress, ioCapability ioCapability: BluetoothIOCapability, OOBDataPresence OOBDataPresence: BluetoothOOBDataPresence, authenticationRequirements authenticationRequirements: BluetoothAuthenticationRequirements) } ``` |

Modified BluetoothIRK [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothIRK {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct BluetoothIRK {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(data data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified BluetoothKey [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothKey {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct BluetoothKey {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(data data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified BluetoothKeypressNotification [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothKeypressNotification {     var deviceAddress: BluetoothDeviceAddress     var notificationType: BluetoothKeypressNotificationType } ``` |
| To | ``` struct BluetoothKeypressNotification {     var deviceAddress: BluetoothDeviceAddress     var notificationType: BluetoothKeypressNotificationType     init()     init(deviceAddress deviceAddress: BluetoothDeviceAddress, notificationType notificationType: BluetoothKeypressNotificationType) } ``` |

Modified BluetoothL2CAPQualityOfServiceOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothL2CAPQualityOfServiceOptions {     var flags: UInt8     var serviceType: UInt8     var tokenRate: UInt32     var tokenBucketSize: UInt32     var peakBandwidth: UInt32     var latency: UInt32     var delayVariation: UInt32 } ``` |
| To | ``` struct BluetoothL2CAPQualityOfServiceOptions {     var flags: UInt8     var serviceType: UInt8     var tokenRate: UInt32     var tokenBucketSize: UInt32     var peakBandwidth: UInt32     var latency: UInt32     var delayVariation: UInt32     init()     init(flags flags: UInt8, serviceType serviceType: UInt8, tokenRate tokenRate: UInt32, tokenBucketSize tokenBucketSize: UInt32, peakBandwidth peakBandwidth: UInt32, latency latency: UInt32, delayVariation delayVariation: UInt32) } ``` |

Modified BluetoothL2CAPRetransmissionAndFlowControlOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothL2CAPRetransmissionAndFlowControlOptions {     var flags: UInt8     var txWindowSize: UInt8     var maxTransmit: UInt8     var retransmissionTimeout: UInt16     var monitorTimeout: UInt16     var maxPDUPayloadSize: UInt16 } ``` |
| To | ``` struct BluetoothL2CAPRetransmissionAndFlowControlOptions {     var flags: UInt8     var txWindowSize: UInt8     var maxTransmit: UInt8     var retransmissionTimeout: UInt16     var monitorTimeout: UInt16     var maxPDUPayloadSize: UInt16     init()     init(flags flags: UInt8, txWindowSize txWindowSize: UInt8, maxTransmit maxTransmit: UInt8, retransmissionTimeout retransmissionTimeout: UInt16, monitorTimeout monitorTimeout: UInt16, maxPDUPayloadSize maxPDUPayloadSize: UInt16) } ``` |

Modified BluetoothPINCode [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothPINCode {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct BluetoothPINCode {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(data data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified BluetoothReadClockInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothReadClockInfo {     var handle: BluetoothConnectionHandle     var clock: UInt32     var accuracy: UInt16 } ``` |
| To | ``` struct BluetoothReadClockInfo {     var handle: BluetoothConnectionHandle     var clock: UInt32     var accuracy: UInt16     init()     init(handle handle: BluetoothConnectionHandle, clock clock: UInt32, accuracy accuracy: UInt16) } ``` |

Modified BluetoothRemoteHostSupportedFeaturesNotification [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothRemoteHostSupportedFeaturesNotification {     var deviceAddress: BluetoothDeviceAddress     var hostSupportedFeatures: BluetoothHCISupportedFeatures } ``` |
| To | ``` struct BluetoothRemoteHostSupportedFeaturesNotification {     var deviceAddress: BluetoothDeviceAddress     var hostSupportedFeatures: BluetoothHCISupportedFeatures     init()     init(deviceAddress deviceAddress: BluetoothDeviceAddress, hostSupportedFeatures hostSupportedFeatures: BluetoothHCISupportedFeatures) } ``` |

Modified BluetoothSetEventMask [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothSetEventMask {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct BluetoothSetEventMask {     var data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(data data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified BluetoothSynchronousConnectionInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothSynchronousConnectionInfo {     var transmitBandWidth: BluetoothHCITransmitBandwidth     var receiveBandWidth: BluetoothHCIReceiveBandwidth     var maxLatency: BluetoothHCIMaxLatency     var voiceSetting: BluetoothHCIVoiceSetting     var retransmissionEffort: BluetoothHCIRetransmissionEffort     var packetType: BluetoothPacketType } ``` |
| To | ``` struct BluetoothSynchronousConnectionInfo {     var transmitBandWidth: BluetoothHCITransmitBandwidth     var receiveBandWidth: BluetoothHCIReceiveBandwidth     var maxLatency: BluetoothHCIMaxLatency     var voiceSetting: BluetoothHCIVoiceSetting     var retransmissionEffort: BluetoothHCIRetransmissionEffort     var packetType: BluetoothPacketType     init()     init(transmitBandWidth transmitBandWidth: BluetoothHCITransmitBandwidth, receiveBandWidth receiveBandWidth: BluetoothHCIReceiveBandwidth, maxLatency maxLatency: BluetoothHCIMaxLatency, voiceSetting voiceSetting: BluetoothHCIVoiceSetting, retransmissionEffort retransmissionEffort: BluetoothHCIRetransmissionEffort, packetType packetType: BluetoothPacketType) } ``` |

Modified BluetoothTransportInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothTransportInfo {     var productID: UInt32     var vendorID: UInt32     var type: UInt32     var productName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var vendorName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var totalDataBytesSent: UInt64     var totalSCOBytesSent: UInt64     var totalDataBytesReceived: UInt64     var totalSCOBytesReceived: UInt64 } ``` |
| To | ``` struct BluetoothTransportInfo {     var productID: UInt32     var vendorID: UInt32     var type: UInt32     var productName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var vendorName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var totalDataBytesSent: UInt64     var totalSCOBytesSent: UInt64     var totalDataBytesReceived: UInt64     var totalSCOBytesReceived: UInt64     init()     init(productID productID: UInt32, vendorID vendorID: UInt32, type type: UInt32, productName productName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), vendorName vendorName: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), totalDataBytesSent totalDataBytesSent: UInt64, totalSCOBytesSent totalSCOBytesSent: UInt64, totalDataBytesReceived totalDataBytesReceived: UInt64, totalSCOBytesReceived totalSCOBytesReceived: UInt64) } ``` |

Modified BluetoothUserConfirmationRequest [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothUserConfirmationRequest {     var deviceAddress: BluetoothDeviceAddress     var numericValue: BluetoothNumericValue } ``` |
| To | ``` struct BluetoothUserConfirmationRequest {     var deviceAddress: BluetoothDeviceAddress     var numericValue: BluetoothNumericValue     init()     init(deviceAddress deviceAddress: BluetoothDeviceAddress, numericValue numericValue: BluetoothNumericValue) } ``` |

Modified BluetoothUserPasskeyNotification [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BluetoothUserPasskeyNotification {     var deviceAddress: BluetoothDeviceAddress     var passkey: BluetoothPasskey } ``` |
| To | ``` struct BluetoothUserPasskeyNotification {     var deviceAddress: BluetoothDeviceAddress     var passkey: BluetoothPasskey     init()     init(deviceAddress deviceAddress: BluetoothDeviceAddress, passkey passkey: BluetoothPasskey) } ``` |

Modified IOBluetoothDevice.RSSI() -> BluetoothHCIRSSIValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothDevice.init(address: UnsafePointer<BluetoothDeviceAddress>)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(address address: ConstUnsafePointer<BluetoothDeviceAddress>) ``` |
| To | ``` convenience init!(address address: UnsafePointer<BluetoothDeviceAddress>) ``` |

Modified IOBluetoothDevice.init(addressString: String!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(addressString address: String!) ``` |
| To | ``` convenience init!(addressString address: String!) ``` |

Modified IOBluetoothDevice.getAddress() -> UnsafePointer<BluetoothDeviceAddress>

|  | Declaration |
| --- | --- |
| From | ``` func getAddress() -> ConstUnsafePointer<BluetoothDeviceAddress> ``` |
| To | ``` func getAddress() -> UnsafePointer<BluetoothDeviceAddress> ``` |

Modified IOBluetoothDevice.handsFreeAudioGatewayServiceRecord() -> IOBluetoothSDPServiceRecord!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothDevice.handsFreeDeviceServiceRecord() -> IOBluetoothSDPServiceRecord!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothDevice.isHandsFreeAudioGateway() -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothDevice.isHandsFreeDevice() -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothDevice.openL2CAPChannelAsync(AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM: BluetoothL2CAPPSM, delegate: AnyObject!) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func openL2CAPChannelAsync(_ newChannel: AutoreleasingUnsafePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, delegate channelDelegate: AnyObject!) -> IOReturn ``` |
| To | ``` func openL2CAPChannelAsync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, delegate channelDelegate: AnyObject!) -> IOReturn ``` |

Modified IOBluetoothDevice.openL2CAPChannelAsync(AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM: BluetoothL2CAPPSM, withConfiguration:[NSObject: AnyObject]!, delegate: AnyObject!) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func openL2CAPChannelAsync(_ newChannel: AutoreleasingUnsafePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, withConfiguration channelConfiguration: [NSObject : AnyObject]!, delegate channelDelegate: AnyObject!) -> IOReturn ``` |
| To | ``` func openL2CAPChannelAsync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, withConfiguration channelConfiguration: [NSObject : AnyObject]!, delegate channelDelegate: AnyObject!) -> IOReturn ``` |

Modified IOBluetoothDevice.openL2CAPChannelSync(AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM: BluetoothL2CAPPSM, delegate: AnyObject!) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func openL2CAPChannelSync(_ newChannel: AutoreleasingUnsafePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, delegate channelDelegate: AnyObject!) -> IOReturn ``` |
| To | ``` func openL2CAPChannelSync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, delegate channelDelegate: AnyObject!) -> IOReturn ``` |

Modified IOBluetoothDevice.openL2CAPChannelSync(AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM: BluetoothL2CAPPSM, withConfiguration:[NSObject: AnyObject]!, delegate: AnyObject!) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func openL2CAPChannelSync(_ newChannel: AutoreleasingUnsafePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, withConfiguration channelConfiguration: [NSObject : AnyObject]!, delegate channelDelegate: AnyObject!) -> IOReturn ``` |
| To | ``` func openL2CAPChannelSync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, withConfiguration channelConfiguration: [NSObject : AnyObject]!, delegate channelDelegate: AnyObject!) -> IOReturn ``` |

Modified IOBluetoothDevice.openRFCOMMChannelAsync(AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>, withChannelID: BluetoothRFCOMMChannelID, delegate: AnyObject!) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func openRFCOMMChannelAsync(_ rfcommChannel: AutoreleasingUnsafePointer<IOBluetoothRFCOMMChannel?>, withChannelID channelID: BluetoothRFCOMMChannelID, delegate channelDelegate: AnyObject!) -> IOReturn ``` |
| To | ``` func openRFCOMMChannelAsync(_ rfcommChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>, withChannelID channelID: BluetoothRFCOMMChannelID, delegate channelDelegate: AnyObject!) -> IOReturn ``` |

Modified IOBluetoothDevice.openRFCOMMChannelSync(AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>, withChannelID: BluetoothRFCOMMChannelID, delegate: AnyObject!) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func openRFCOMMChannelSync(_ rfcommChannel: AutoreleasingUnsafePointer<IOBluetoothRFCOMMChannel?>, withChannelID channelID: BluetoothRFCOMMChannelID, delegate channelDelegate: AnyObject!) -> IOReturn ``` |
| To | ``` func openRFCOMMChannelSync(_ rfcommChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>, withChannelID channelID: BluetoothRFCOMMChannelID, delegate channelDelegate: AnyObject!) -> IOReturn ``` |

Modified IOBluetoothDevice.performSDPQuery(AnyObject!, uuids:[AnyObject]!) -> IOReturn

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothDevice.rawRSSI() -> BluetoothHCIRSSIValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothDevice.sendL2CAPEchoRequest(UnsafeMutablePointer<Void>, length: UInt16) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func sendL2CAPEchoRequest(_ data: UnsafePointer<()>, length length: UInt16) -> IOReturn ``` |
| To | ``` func sendL2CAPEchoRequest(_ data: UnsafeMutablePointer<Void>, length length: UInt16) -> IOReturn ``` |

Modified IOBluetoothDeviceInquiry.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: AnyObject! ``` |
| To | ``` unowned(unsafe) var delegate: AnyObject! ``` |

Modified IOBluetoothDeviceInquiry.init(delegate: AnyObject!)

|  | Declaration |
| --- | --- |
| From | ``` init(delegate delegate: AnyObject!) ``` |
| To | ``` init!(delegate delegate: AnyObject!) ``` |

Modified IOBluetoothDeviceInquiryDelegate.deviceInquiryComplete(IOBluetoothDeviceInquiry!, error: IOReturn, aborted: Bool)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothDeviceInquiryDelegate.deviceInquiryDeviceFound(IOBluetoothDeviceInquiry!, device: IOBluetoothDevice!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothDeviceInquiryDelegate.deviceInquiryDeviceNameUpdated(IOBluetoothDeviceInquiry!, device: IOBluetoothDevice!, devicesRemaining: UInt32)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothDeviceInquiryDelegate.deviceInquiryStarted(IOBluetoothDeviceInquiry!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothDeviceInquiryDelegate.deviceInquiryUpdatingDeviceNamesStarted(IOBluetoothDeviceInquiry!, devicesRemaining: UInt32)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothDevicePair.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: AnyObject! ``` |
| To | ``` unowned(unsafe) var delegate: AnyObject! ``` |

Modified IOBluetoothDevicePair.init(device: IOBluetoothDevice!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(device device: IOBluetoothDevice!) ``` |
| To | ``` convenience init!(device device: IOBluetoothDevice!) ``` |

Modified IOBluetoothDevicePair.replyPINCode(Int, PINCode: UnsafeMutablePointer<BluetoothPINCode>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func replyPINCode(_ PINCodeSize: ByteCount, PINCode PINCode: UnsafePointer<BluetoothPINCode>) ``` | OS X 10.10 |
| To | ``` func replyPINCode(_ PINCodeSize: Int, PINCode PINCode: UnsafeMutablePointer<BluetoothPINCode>) ``` | OS X 10.10.3 |

Modified IOBluetoothDevicePairDelegate.devicePairingConnecting(AnyObject!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothDevicePairDelegate.devicePairingFinished(AnyObject!, error: IOReturn)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothDevicePairDelegate.devicePairingPINCodeRequest(AnyObject!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothDevicePairDelegate.devicePairingStarted(AnyObject!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothDevicePairDelegate.devicePairingUserConfirmationRequest(AnyObject!, numericValue: BluetoothNumericValue)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothDevicePairDelegate.devicePairingUserPasskeyNotification(AnyObject!, passkey: BluetoothPasskey)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothDevicePairDelegate.deviceSimplePairingComplete(AnyObject!, status: BluetoothHCIEventStatus)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothDeviceSearchAttributes [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct IOBluetoothDeviceSearchAttributes {     var options: IOBluetoothDeviceSearchOptions     var maxResults: IOItemCount     var deviceAttributeCount: IOItemCount     var attributeList: UnsafePointer<IOBluetoothDeviceSearchDeviceAttributes> } ``` |
| To | ``` struct IOBluetoothDeviceSearchAttributes {     var options: IOBluetoothDeviceSearchOptions     var maxResults: IOItemCount     var deviceAttributeCount: IOItemCount     var attributeList: UnsafeMutablePointer<IOBluetoothDeviceSearchDeviceAttributes>     init()     init(options options: IOBluetoothDeviceSearchOptions, maxResults maxResults: IOItemCount, deviceAttributeCount deviceAttributeCount: IOItemCount, attributeList attributeList: UnsafeMutablePointer<IOBluetoothDeviceSearchDeviceAttributes>) } ``` |

Modified IOBluetoothDeviceSearchAttributes.attributeList

|  | Declaration |
| --- | --- |
| From | ``` var attributeList: UnsafePointer<IOBluetoothDeviceSearchDeviceAttributes> ``` |
| To | ``` var attributeList: UnsafeMutablePointer<IOBluetoothDeviceSearchDeviceAttributes> ``` |

Modified IOBluetoothDeviceSearchDeviceAttributes [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct IOBluetoothDeviceSearchDeviceAttributes {     var address: BluetoothDeviceAddress     var name: BluetoothDeviceName     var serviceClassMajor: BluetoothServiceClassMajor     var deviceClassMajor: BluetoothDeviceClassMajor     var deviceClassMinor: BluetoothDeviceClassMinor } ``` |
| To | ``` struct IOBluetoothDeviceSearchDeviceAttributes {     var address: BluetoothDeviceAddress     var name: BluetoothDeviceName     var serviceClassMajor: BluetoothServiceClassMajor     var deviceClassMajor: BluetoothDeviceClassMajor     var deviceClassMinor: BluetoothDeviceClassMinor     init()     init(address address: BluetoothDeviceAddress, name name: BluetoothDeviceName, serviceClassMajor serviceClassMajor: BluetoothServiceClassMajor, deviceClassMajor deviceClassMajor: BluetoothDeviceClassMajor, deviceClassMinor deviceClassMinor: BluetoothDeviceClassMinor) } ``` |

Modified IOBluetoothHandsFree

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.SMSEnabled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.SMSMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.connect()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.connectSCO()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.delegate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var delegate: IOBluetoothHandsFreeDelegate! ``` | OS X 10.10 |
| To | ``` unowned(unsafe) var delegate: IOBluetoothHandsFreeDelegate! ``` | OS X 10.7 |

Modified IOBluetoothHandsFree.device

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.init(device: IOBluetoothDevice!, delegate: IOBluetoothHandsFreeDelegate!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(device device: IOBluetoothDevice!, delegate inDelegate: IOBluetoothHandsFreeDelegate!) ``` | OS X 10.10 |
| To | ``` init!(device device: IOBluetoothDevice!, delegate inDelegate: IOBluetoothHandsFreeDelegate!) ``` | OS X 10.7 |

Modified IOBluetoothHandsFree.deviceCallHoldModes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.deviceSupportedFeatures

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.deviceSupportedSMSServices

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.disconnect()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.disconnectSCO()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.indicator(String!) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.inputMuted

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.inputVolume

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.isConnected() -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.isSCOConnected() -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.outputMuted

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.outputVolume

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.setIndicator(String!, value: Int32)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFree.supportedFeatures

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeAudioGateway

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeAudioGateway.createIndicator(String!, min: Int32, max: Int32, currentValue: Int32)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeAudioGateway.init(device: IOBluetoothDevice!, delegate: AnyObject!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(device device: IOBluetoothDevice!, delegate inDelegate: AnyObject!) ``` | OS X 10.10 |
| To | ``` init!(device device: IOBluetoothDevice!, delegate inDelegate: AnyObject!) ``` | OS X 10.7 |

Modified IOBluetoothHandsFreeAudioGateway.processATCommand(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeAudioGateway.sendOKResponse()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeAudioGateway.sendResponse(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeAudioGateway.sendResponse(String!, withOK: Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeAudioGatewayDelegate.handsFree(IOBluetoothHandsFreeAudioGateway!, hangup: NSNumber!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHandsFreeAudioGatewayDelegate.handsFree(IOBluetoothHandsFreeAudioGateway!, redial: NSNumber!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHandsFreeDelegate.handsFree(IOBluetoothHandsFree!, connected: NSNumber!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHandsFreeDelegate.handsFree(IOBluetoothHandsFree!, disconnected: NSNumber!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHandsFreeDelegate.handsFree(IOBluetoothHandsFree!, scoConnectionClosed: NSNumber!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHandsFreeDelegate.handsFree(IOBluetoothHandsFree!, scoConnectionOpened: NSNumber!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHandsFreeDevice

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.acceptCall()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.acceptCallOnPhone()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.addHeldCall()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.callTransfer()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.currentCallList()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.init(device: IOBluetoothDevice!, delegate: AnyObject!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(device device: IOBluetoothDevice!, delegate delegate: AnyObject!) ``` | OS X 10.10 |
| To | ``` init!(device device: IOBluetoothDevice!, delegate delegate: AnyObject!) ``` | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.dialNumber(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.endCall()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.holdCall()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.memoryDial(Int32)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.placeAllOthersOnHold(Int32)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.redial()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.releaseActiveCalls()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.releaseCall(Int32)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.releaseHeldCalls()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.sendATCommand(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.sendATCommand(String!, timeout: Float, selector: Selector, target: AnyObject!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.sendDTMF(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.sendSMS(String!, message: String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.subscriberNumber()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.transferAudioToComputer()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDevice.transferAudioToPhone()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothHandsFreeDeviceDelegate.handsFree(IOBluetoothHandsFreeDevice!, batteryCharge: NSNumber!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHandsFreeDeviceDelegate.handsFree(IOBluetoothHandsFreeDevice!, callHoldState: NSNumber!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHandsFreeDeviceDelegate.handsFree(IOBluetoothHandsFreeDevice!, callSetupMode: NSNumber!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHandsFreeDeviceDelegate.handsFree(IOBluetoothHandsFreeDevice!, currentCall:[NSObject: AnyObject]!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHandsFreeDeviceDelegate.handsFree(IOBluetoothHandsFreeDevice!, incomingCallFrom: String!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHandsFreeDeviceDelegate.handsFree(IOBluetoothHandsFreeDevice!, incomingSMS:[NSObject: AnyObject]!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHandsFreeDeviceDelegate.handsFree(IOBluetoothHandsFreeDevice!, isCallActive: NSNumber!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHandsFreeDeviceDelegate.handsFree(IOBluetoothHandsFreeDevice!, isRoaming: NSNumber!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHandsFreeDeviceDelegate.handsFree(IOBluetoothHandsFreeDevice!, isServiceAvailable: NSNumber!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHandsFreeDeviceDelegate.handsFree(IOBluetoothHandsFreeDevice!, ringAttempt: NSNumber!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHandsFreeDeviceDelegate.handsFree(IOBluetoothHandsFreeDevice!, signalStrength: NSNumber!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHandsFreeDeviceDelegate.handsFree(IOBluetoothHandsFreeDevice!, subscriberNumber: String!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHandsFreeDeviceDelegate.handsFree(IOBluetoothHandsFreeDevice!, unhandledResultCode: String!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified IOBluetoothHostController.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: AnyObject! ``` |
| To | ``` unowned(unsafe) var delegate: AnyObject! ``` |

Modified IOBluetoothL2CAPChannel.writeAsync(UnsafeMutablePointer<Void>, length: UInt16, refcon: UnsafeMutablePointer<Void>) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func writeAsync(_ data: UnsafePointer<()>, length length: UInt16, refcon refcon: UnsafePointer<()>) -> IOReturn ``` |
| To | ``` func writeAsync(_ data: UnsafeMutablePointer<Void>, length length: UInt16, refcon refcon: UnsafeMutablePointer<Void>) -> IOReturn ``` |

Modified IOBluetoothL2CAPChannel.writeSync(UnsafeMutablePointer<Void>, length: UInt16) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func writeSync(_ data: UnsafePointer<()>, length length: UInt16) -> IOReturn ``` |
| To | ``` func writeSync(_ data: UnsafeMutablePointer<Void>, length length: UInt16) -> IOReturn ``` |

Modified IOBluetoothL2CAPChannelDataBlock [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct IOBluetoothL2CAPChannelDataBlock {     var dataPtr: UnsafePointer<()>     var dataSize: UInt } ``` |
| To | ``` struct IOBluetoothL2CAPChannelDataBlock {     var dataPtr: UnsafeMutablePointer<Void>     var dataSize: Int     init()     init(dataPtr dataPtr: UnsafeMutablePointer<Void>, dataSize dataSize: Int) } ``` |

Modified IOBluetoothL2CAPChannelDataBlock.dataPtr

|  | Declaration |
| --- | --- |
| From | ``` var dataPtr: UnsafePointer<()> ``` |
| To | ``` var dataPtr: UnsafeMutablePointer<Void> ``` |

Modified IOBluetoothL2CAPChannelDataBlock.dataSize

|  | Declaration |
| --- | --- |
| From | ``` var dataSize: UInt ``` |
| To | ``` var dataSize: Int ``` |

Modified IOBluetoothL2CAPChannelDelegate.l2capChannelClosed(IOBluetoothL2CAPChannel!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothL2CAPChannelDelegate.l2capChannelData(IOBluetoothL2CAPChannel!, data: UnsafeMutablePointer<Void>, length: Int)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func l2capChannelData(_ l2capChannel: IOBluetoothL2CAPChannel!, data dataPointer: UnsafePointer<()>, length dataLength: UInt) ``` | OS X 10.10 | -- |
| To | ``` optional func l2capChannelData(_ l2capChannel: IOBluetoothL2CAPChannel!, data dataPointer: UnsafeMutablePointer<Void>, length dataLength: Int) ``` | OS X 10.10.3 | yes |

Modified IOBluetoothL2CAPChannelDelegate.l2capChannelOpenComplete(IOBluetoothL2CAPChannel!, status: IOReturn)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothL2CAPChannelDelegate.l2capChannelQueueSpaceAvailable(IOBluetoothL2CAPChannel!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothL2CAPChannelDelegate.l2capChannelReconfigured(IOBluetoothL2CAPChannel!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothL2CAPChannelDelegate.l2capChannelWriteComplete(IOBluetoothL2CAPChannel!, refcon: UnsafeMutablePointer<Void>, status: IOReturn)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func l2capChannelWriteComplete(_ l2capChannel: IOBluetoothL2CAPChannel!, refcon refcon: UnsafePointer<()>, status error: IOReturn) ``` | -- |
| To | ``` optional func l2capChannelWriteComplete(_ l2capChannel: IOBluetoothL2CAPChannel!, refcon refcon: UnsafeMutablePointer<Void>, status error: IOReturn) ``` | yes |

Modified IOBluetoothL2CAPChannelEvent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct IOBluetoothL2CAPChannelEvent {     var eventType: IOBluetoothL2CAPChannelEventType     var status: IOReturn } ``` |
| To | ``` struct IOBluetoothL2CAPChannelEvent {     var eventType: IOBluetoothL2CAPChannelEventType     var status: IOReturn     init() } ``` |

Modified IOBluetoothOBEXSession.init(SDPServiceRecord: IOBluetoothSDPServiceRecord!)

|  | Declaration |
| --- | --- |
| From | ``` init(SDPServiceRecord inSDPServiceRecord: IOBluetoothSDPServiceRecord!) ``` |
| To | ``` init!(SDPServiceRecord inSDPServiceRecord: IOBluetoothSDPServiceRecord!) ``` |

Modified IOBluetoothOBEXSession.init(device: IOBluetoothDevice!, channelID: BluetoothRFCOMMChannelID)

|  | Declaration |
| --- | --- |
| From | ``` init(device inDevice: IOBluetoothDevice!, channelID inChannelID: BluetoothRFCOMMChannelID) ``` |
| To | ``` init!(device inDevice: IOBluetoothDevice!, channelID inChannelID: BluetoothRFCOMMChannelID) ``` |

Modified IOBluetoothOBEXSession.init(incomingRFCOMMChannel: IOBluetoothRFCOMMChannel!, eventSelector: Selector, selectorTarget: AnyObject!, refCon: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` init(incomingRFCOMMChannel inChannel: IOBluetoothRFCOMMChannel!, eventSelector inEventSelector: Selector, selectorTarget inEventSelectorTarget: AnyObject!, refCon inUserRefCon: UnsafePointer<()>) ``` |
| To | ``` init!(incomingRFCOMMChannel inChannel: IOBluetoothRFCOMMChannel!, eventSelector inEventSelector: Selector, selectorTarget inEventSelectorTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) ``` |

Modified IOBluetoothOBEXSession.openTransportConnection(Selector, selectorTarget: AnyObject!, refCon: UnsafeMutablePointer<Void>) -> OBEXError

|  | Declaration |
| --- | --- |
| From | ``` func openTransportConnection(_ inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafePointer<()>) -> OBEXError ``` |
| To | ``` func openTransportConnection(_ inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError ``` |

Modified IOBluetoothOBEXSession.sendDataToTransport(UnsafeMutablePointer<Void>, dataLength: Int) -> OBEXError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sendDataToTransport(_ inDataToSend: UnsafePointer<()>, dataLength inDataLength: UInt) -> OBEXError ``` | OS X 10.10 |
| To | ``` func sendDataToTransport(_ inDataToSend: UnsafeMutablePointer<Void>, dataLength inDataLength: Int) -> OBEXError ``` | OS X 10.10.3 |

Modified IOBluetoothOBEXSession.setOBEXSessionOpenConnectionCallback(IOBluetoothOBEXSessionOpenConnectionCallback, refCon: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func setOBEXSessionOpenConnectionCallback(_ inCallback: IOBluetoothOBEXSessionOpenConnectionCallback, refCon inUserRefCon: UnsafePointer<()>) ``` |
| To | ``` func setOBEXSessionOpenConnectionCallback(_ inCallback: IOBluetoothOBEXSessionOpenConnectionCallback, refCon inUserRefCon: UnsafeMutablePointer<Void>) ``` |

Modified IOBluetoothOBEXSession.withIncomingRFCOMMChannel(IOBluetoothRFCOMMChannel!, eventSelector: Selector, selectorTarget: AnyObject!, refCon: UnsafeMutablePointer<Void>) -> Self! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func withIncomingRFCOMMChannel(_ inChannel: IOBluetoothRFCOMMChannel!, eventSelector inEventSelector: Selector, selectorTarget inEventSelectorTarget: AnyObject!, refCon inUserRefCon: UnsafePointer<()>) -> Self! ``` |
| To | ``` class func withIncomingRFCOMMChannel(_ inChannel: IOBluetoothRFCOMMChannel!, eventSelector inEventSelector: Selector, selectorTarget inEventSelectorTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> Self! ``` |

Modified IOBluetoothRFCOMMChannel.writeAsync(UnsafeMutablePointer<Void>, length: UInt16, refcon: UnsafeMutablePointer<Void>) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func writeAsync(_ data: UnsafePointer<()>, length length: UInt16, refcon refcon: UnsafePointer<()>) -> IOReturn ``` |
| To | ``` func writeAsync(_ data: UnsafeMutablePointer<Void>, length length: UInt16, refcon refcon: UnsafeMutablePointer<Void>) -> IOReturn ``` |

Modified IOBluetoothRFCOMMChannel.writeSync(UnsafeMutablePointer<Void>, length: UInt16) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func writeSync(_ data: UnsafePointer<()>, length length: UInt16) -> IOReturn ``` |
| To | ``` func writeSync(_ data: UnsafeMutablePointer<Void>, length length: UInt16) -> IOReturn ``` |

Modified IOBluetoothRFCOMMChannelDelegate.rfcommChannelClosed(IOBluetoothRFCOMMChannel!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothRFCOMMChannelDelegate.rfcommChannelControlSignalsChanged(IOBluetoothRFCOMMChannel!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothRFCOMMChannelDelegate.rfcommChannelData(IOBluetoothRFCOMMChannel!, data: UnsafeMutablePointer<Void>, length: Int)

|  | Declaration | Introduction | Optional |
| --- | --- | --- | --- |
| From | ``` optional func rfcommChannelData(_ rfcommChannel: IOBluetoothRFCOMMChannel!, data dataPointer: UnsafePointer<()>, length dataLength: UInt) ``` | OS X 10.10 | -- |
| To | ``` optional func rfcommChannelData(_ rfcommChannel: IOBluetoothRFCOMMChannel!, data dataPointer: UnsafeMutablePointer<Void>, length dataLength: Int) ``` | OS X 10.10.3 | yes |

Modified IOBluetoothRFCOMMChannelDelegate.rfcommChannelFlowControlChanged(IOBluetoothRFCOMMChannel!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothRFCOMMChannelDelegate.rfcommChannelOpenComplete(IOBluetoothRFCOMMChannel!, status: IOReturn)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothRFCOMMChannelDelegate.rfcommChannelQueueSpaceAvailable(IOBluetoothRFCOMMChannel!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IOBluetoothRFCOMMChannelDelegate.rfcommChannelWriteComplete(IOBluetoothRFCOMMChannel!, refcon: UnsafeMutablePointer<Void>, status: IOReturn)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func rfcommChannelWriteComplete(_ rfcommChannel: IOBluetoothRFCOMMChannel!, refcon refcon: UnsafePointer<()>, status error: IOReturn) ``` | -- |
| To | ``` optional func rfcommChannelWriteComplete(_ rfcommChannel: IOBluetoothRFCOMMChannel!, refcon refcon: UnsafeMutablePointer<Void>, status error: IOReturn) ``` | yes |

Modified IOBluetoothSDPDataElement.init(elementValue: NSObject!)

|  | Declaration |
| --- | --- |
| From | ``` init(elementValue element: NSObject!) ``` |
| To | ``` init!(elementValue element: NSObject!) ``` |

Modified IOBluetoothSDPDataElement.init(type: BluetoothSDPDataElementTypeDescriptor, sizeDescriptor: BluetoothSDPDataElementSizeDescriptor, size: UInt32, value: NSObject!)

|  | Declaration |
| --- | --- |
| From | ``` init(type newType: BluetoothSDPDataElementTypeDescriptor, sizeDescriptor newSizeDescriptor: BluetoothSDPDataElementSizeDescriptor, size newSize: UInt32, value newValue: NSObject!) ``` |
| To | ``` init!(type newType: BluetoothSDPDataElementTypeDescriptor, sizeDescriptor newSizeDescriptor: BluetoothSDPDataElementSizeDescriptor, size newSize: UInt32, value newValue: NSObject!) ``` |

Modified IOBluetoothSDPServiceAttribute.init(ID: BluetoothSDPServiceAttributeID, attributeElement: IOBluetoothSDPDataElement!)

|  | Declaration |
| --- | --- |
| From | ``` init(ID newAttributeID: BluetoothSDPServiceAttributeID, attributeElement attributeElement: IOBluetoothSDPDataElement!) ``` |
| To | ``` init!(ID newAttributeID: BluetoothSDPServiceAttributeID, attributeElement attributeElement: IOBluetoothSDPDataElement!) ``` |

Modified IOBluetoothSDPServiceAttribute.init(ID: BluetoothSDPServiceAttributeID, attributeElementValue: NSObject!)

|  | Declaration |
| --- | --- |
| From | ``` init(ID newAttributeID: BluetoothSDPServiceAttributeID, attributeElementValue attributeElementValue: NSObject!) ``` |
| To | ``` init!(ID newAttributeID: BluetoothSDPServiceAttributeID, attributeElementValue attributeElementValue: NSObject!) ``` |

Modified IOBluetoothSDPServiceRecord.getL2CAPPSM(UnsafeMutablePointer<BluetoothL2CAPPSM>) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func getL2CAPPSM(_ outPSM: UnsafePointer<BluetoothL2CAPPSM>) -> IOReturn ``` |
| To | ``` func getL2CAPPSM(_ outPSM: UnsafeMutablePointer<BluetoothL2CAPPSM>) -> IOReturn ``` |

Modified IOBluetoothSDPServiceRecord.getRFCOMMChannelID(UnsafeMutablePointer<BluetoothRFCOMMChannelID>) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func getRFCOMMChannelID(_ rfcommChannelID: UnsafePointer<BluetoothRFCOMMChannelID>) -> IOReturn ``` |
| To | ``` func getRFCOMMChannelID(_ rfcommChannelID: UnsafeMutablePointer<BluetoothRFCOMMChannelID>) -> IOReturn ``` |

Modified IOBluetoothSDPServiceRecord.getServiceRecordHandle(UnsafeMutablePointer<BluetoothSDPServiceRecordHandle>) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func getServiceRecordHandle(_ outServiceRecordHandle: UnsafePointer<BluetoothSDPServiceRecordHandle>) -> IOReturn ``` |
| To | ``` func getServiceRecordHandle(_ outServiceRecordHandle: UnsafeMutablePointer<BluetoothSDPServiceRecordHandle>) -> IOReturn ``` |

Modified IOBluetoothSDPServiceRecord.handsFreeSupportedFeatures() -> UInt16

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IOBluetoothSDPServiceRecord.init(serviceDictionary: [NSObject: AnyObject]!, device: IOBluetoothDevice!)

|  | Declaration |
| --- | --- |
| From | ``` init(serviceDictionary serviceDict: [NSObject : AnyObject]!, device device: IOBluetoothDevice!) ``` |
| To | ``` init!(serviceDictionary serviceDict: [NSObject : AnyObject]!, device device: IOBluetoothDevice!) ``` |

Modified IOBluetoothSDPUUID.init(UUID16: BluetoothSDPUUID16)

|  | Declaration |
| --- | --- |
| From | ``` init(UUID16 uuid16: BluetoothSDPUUID16) ``` |
| To | ``` init!(UUID16 uuid16: BluetoothSDPUUID16) ``` |

Modified IOBluetoothSDPUUID.init(UUID32: BluetoothSDPUUID32)

|  | Declaration |
| --- | --- |
| From | ``` init(UUID32 uuid32: BluetoothSDPUUID32) ``` |
| To | ``` init!(UUID32 uuid32: BluetoothSDPUUID32) ``` |

Modified IOBluetoothSDPUUID.uuidWithBytes(UnsafePointer<Void>, length: UInt32) -> Self! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func uuidWithBytes(_ bytes: ConstUnsafePointer<()>, length length: UInt32) -> Self! ``` |
| To | ``` class func uuidWithBytes(_ bytes: UnsafePointer<Void>, length length: UInt32) -> Self! ``` |

Modified OBEXAbortCommandData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OBEXAbortCommandData {     var headerDataPtr: UnsafePointer<()>     var headerDataLength: UInt } ``` |
| To | ``` struct OBEXAbortCommandData {     var headerDataPtr: UnsafeMutablePointer<Void>     var headerDataLength: Int     init()     init(headerDataPtr headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength headerDataLength: Int) } ``` |

Modified OBEXAbortCommandData.headerDataLength

|  | Declaration |
| --- | --- |
| From | ``` var headerDataLength: UInt ``` |
| To | ``` var headerDataLength: Int ``` |

Modified OBEXAbortCommandData.headerDataPtr

|  | Declaration |
| --- | --- |
| From | ``` var headerDataPtr: UnsafePointer<()> ``` |
| To | ``` var headerDataPtr: UnsafeMutablePointer<Void> ``` |

Modified OBEXAbortCommandResponseData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OBEXAbortCommandResponseData {     var serverResponseOpCode: OBEXOpCode     var headerDataPtr: UnsafePointer<()>     var headerDataLength: UInt } ``` |
| To | ``` struct OBEXAbortCommandResponseData {     var serverResponseOpCode: OBEXOpCode     var headerDataPtr: UnsafeMutablePointer<Void>     var headerDataLength: Int     init()     init(serverResponseOpCode serverResponseOpCode: OBEXOpCode, headerDataPtr headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength headerDataLength: Int) } ``` |

Modified OBEXAbortCommandResponseData.headerDataLength

|  | Declaration |
| --- | --- |
| From | ``` var headerDataLength: UInt ``` |
| To | ``` var headerDataLength: Int ``` |

Modified OBEXAbortCommandResponseData.headerDataPtr

|  | Declaration |
| --- | --- |
| From | ``` var headerDataPtr: UnsafePointer<()> ``` |
| To | ``` var headerDataPtr: UnsafeMutablePointer<Void> ``` |

Modified OBEXConnectCommandData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OBEXConnectCommandData {     var headerDataPtr: UnsafePointer<()>     var headerDataLength: UInt     var maxPacketSize: OBEXMaxPacketLength     var version: OBEXVersion     var flags: OBEXFlags } ``` |
| To | ``` struct OBEXConnectCommandData {     var headerDataPtr: UnsafeMutablePointer<Void>     var headerDataLength: Int     var maxPacketSize: OBEXMaxPacketLength     var version: OBEXVersion     var flags: OBEXFlags     init()     init(headerDataPtr headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength headerDataLength: Int, maxPacketSize maxPacketSize: OBEXMaxPacketLength, version version: OBEXVersion, flags flags: OBEXFlags) } ``` |

Modified OBEXConnectCommandData.headerDataLength

|  | Declaration |
| --- | --- |
| From | ``` var headerDataLength: UInt ``` |
| To | ``` var headerDataLength: Int ``` |

Modified OBEXConnectCommandData.headerDataPtr

|  | Declaration |
| --- | --- |
| From | ``` var headerDataPtr: UnsafePointer<()> ``` |
| To | ``` var headerDataPtr: UnsafeMutablePointer<Void> ``` |

Modified OBEXConnectCommandResponseData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OBEXConnectCommandResponseData {     var serverResponseOpCode: OBEXOpCode     var headerDataPtr: UnsafePointer<()>     var headerDataLength: UInt     var maxPacketSize: OBEXMaxPacketLength     var version: OBEXVersion     var flags: OBEXFlags } ``` |
| To | ``` struct OBEXConnectCommandResponseData {     var serverResponseOpCode: OBEXOpCode     var headerDataPtr: UnsafeMutablePointer<Void>     var headerDataLength: Int     var maxPacketSize: OBEXMaxPacketLength     var version: OBEXVersion     var flags: OBEXFlags     init()     init(serverResponseOpCode serverResponseOpCode: OBEXOpCode, headerDataPtr headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength headerDataLength: Int, maxPacketSize maxPacketSize: OBEXMaxPacketLength, version version: OBEXVersion, flags flags: OBEXFlags) } ``` |

Modified OBEXConnectCommandResponseData.headerDataLength

|  | Declaration |
| --- | --- |
| From | ``` var headerDataLength: UInt ``` |
| To | ``` var headerDataLength: Int ``` |

Modified OBEXConnectCommandResponseData.headerDataPtr

|  | Declaration |
| --- | --- |
| From | ``` var headerDataPtr: UnsafePointer<()> ``` |
| To | ``` var headerDataPtr: UnsafeMutablePointer<Void> ``` |

Modified OBEXDisconnectCommandData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OBEXDisconnectCommandData {     var headerDataPtr: UnsafePointer<()>     var headerDataLength: UInt } ``` |
| To | ``` struct OBEXDisconnectCommandData {     var headerDataPtr: UnsafeMutablePointer<Void>     var headerDataLength: Int     init()     init(headerDataPtr headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength headerDataLength: Int) } ``` |

Modified OBEXDisconnectCommandData.headerDataLength

|  | Declaration |
| --- | --- |
| From | ``` var headerDataLength: UInt ``` |
| To | ``` var headerDataLength: Int ``` |

Modified OBEXDisconnectCommandData.headerDataPtr

|  | Declaration |
| --- | --- |
| From | ``` var headerDataPtr: UnsafePointer<()> ``` |
| To | ``` var headerDataPtr: UnsafeMutablePointer<Void> ``` |

Modified OBEXDisconnectCommandResponseData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OBEXDisconnectCommandResponseData {     var serverResponseOpCode: OBEXOpCode     var headerDataPtr: UnsafePointer<()>     var headerDataLength: UInt } ``` |
| To | ``` struct OBEXDisconnectCommandResponseData {     var serverResponseOpCode: OBEXOpCode     var headerDataPtr: UnsafeMutablePointer<Void>     var headerDataLength: Int     init()     init(serverResponseOpCode serverResponseOpCode: OBEXOpCode, headerDataPtr headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength headerDataLength: Int) } ``` |

Modified OBEXDisconnectCommandResponseData.headerDataLength

|  | Declaration |
| --- | --- |
| From | ``` var headerDataLength: UInt ``` |
| To | ``` var headerDataLength: Int ``` |

Modified OBEXDisconnectCommandResponseData.headerDataPtr

|  | Declaration |
| --- | --- |
| From | ``` var headerDataPtr: UnsafePointer<()> ``` |
| To | ``` var headerDataPtr: UnsafeMutablePointer<Void> ``` |

Modified OBEXErrorData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OBEXErrorData {     var error: OBEXError     var dataPtr: UnsafePointer<()>     var dataLength: UInt } ``` |
| To | ``` struct OBEXErrorData {     var error: OBEXError     var dataPtr: UnsafeMutablePointer<Void>     var dataLength: Int     init()     init(error error: OBEXError, dataPtr dataPtr: UnsafeMutablePointer<Void>, dataLength dataLength: Int) } ``` |

Modified OBEXErrorData.dataLength

|  | Declaration |
| --- | --- |
| From | ``` var dataLength: UInt ``` |
| To | ``` var dataLength: Int ``` |

Modified OBEXErrorData.dataPtr

|  | Declaration |
| --- | --- |
| From | ``` var dataPtr: UnsafePointer<()> ``` |
| To | ``` var dataPtr: UnsafeMutablePointer<Void> ``` |

Modified OBEXFileTransferServices.init(OBEXSession: IOBluetoothOBEXSession!)

|  | Declaration |
| --- | --- |
| From | ``` init(OBEXSession inOBEXSession: IOBluetoothOBEXSession!) ``` |
| To | ``` init!(OBEXSession inOBEXSession: IOBluetoothOBEXSession!) ``` |

Modified OBEXFileTransferServices.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: AnyObject! ``` |
| To | ``` unowned(unsafe) var delegate: AnyObject! ``` |

Modified OBEXGetCommandData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OBEXGetCommandData {     var headerDataPtr: UnsafePointer<()>     var headerDataLength: UInt } ``` |
| To | ``` struct OBEXGetCommandData {     var headerDataPtr: UnsafeMutablePointer<Void>     var headerDataLength: Int     init()     init(headerDataPtr headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength headerDataLength: Int) } ``` |

Modified OBEXGetCommandData.headerDataLength

|  | Declaration |
| --- | --- |
| From | ``` var headerDataLength: UInt ``` |
| To | ``` var headerDataLength: Int ``` |

Modified OBEXGetCommandData.headerDataPtr

|  | Declaration |
| --- | --- |
| From | ``` var headerDataPtr: UnsafePointer<()> ``` |
| To | ``` var headerDataPtr: UnsafeMutablePointer<Void> ``` |

Modified OBEXGetCommandResponseData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OBEXGetCommandResponseData {     var serverResponseOpCode: OBEXOpCode     var headerDataPtr: UnsafePointer<()>     var headerDataLength: UInt } ``` |
| To | ``` struct OBEXGetCommandResponseData {     var serverResponseOpCode: OBEXOpCode     var headerDataPtr: UnsafeMutablePointer<Void>     var headerDataLength: Int     init()     init(serverResponseOpCode serverResponseOpCode: OBEXOpCode, headerDataPtr headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength headerDataLength: Int) } ``` |

Modified OBEXGetCommandResponseData.headerDataLength

|  | Declaration |
| --- | --- |
| From | ``` var headerDataLength: UInt ``` |
| To | ``` var headerDataLength: Int ``` |

Modified OBEXGetCommandResponseData.headerDataPtr

|  | Declaration |
| --- | --- |
| From | ``` var headerDataPtr: UnsafePointer<()> ``` |
| To | ``` var headerDataPtr: UnsafeMutablePointer<Void> ``` |

Modified OBEXPutCommandData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OBEXPutCommandData {     var headerDataPtr: UnsafePointer<()>     var headerDataLength: UInt     var bodyDataLeftToSend: UInt } ``` |
| To | ``` struct OBEXPutCommandData {     var headerDataPtr: UnsafeMutablePointer<Void>     var headerDataLength: Int     var bodyDataLeftToSend: Int     init()     init(headerDataPtr headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength headerDataLength: Int, bodyDataLeftToSend bodyDataLeftToSend: Int) } ``` |

Modified OBEXPutCommandData.bodyDataLeftToSend

|  | Declaration |
| --- | --- |
| From | ``` var bodyDataLeftToSend: UInt ``` |
| To | ``` var bodyDataLeftToSend: Int ``` |

Modified OBEXPutCommandData.headerDataLength

|  | Declaration |
| --- | --- |
| From | ``` var headerDataLength: UInt ``` |
| To | ``` var headerDataLength: Int ``` |

Modified OBEXPutCommandData.headerDataPtr

|  | Declaration |
| --- | --- |
| From | ``` var headerDataPtr: UnsafePointer<()> ``` |
| To | ``` var headerDataPtr: UnsafeMutablePointer<Void> ``` |

Modified OBEXPutCommandResponseData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OBEXPutCommandResponseData {     var serverResponseOpCode: OBEXOpCode     var headerDataPtr: UnsafePointer<()>     var headerDataLength: UInt } ``` |
| To | ``` struct OBEXPutCommandResponseData {     var serverResponseOpCode: OBEXOpCode     var headerDataPtr: UnsafeMutablePointer<Void>     var headerDataLength: Int     init()     init(serverResponseOpCode serverResponseOpCode: OBEXOpCode, headerDataPtr headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength headerDataLength: Int) } ``` |

Modified OBEXPutCommandResponseData.headerDataLength

|  | Declaration |
| --- | --- |
| From | ``` var headerDataLength: UInt ``` |
| To | ``` var headerDataLength: Int ``` |

Modified OBEXPutCommandResponseData.headerDataPtr

|  | Declaration |
| --- | --- |
| From | ``` var headerDataPtr: UnsafePointer<()> ``` |
| To | ``` var headerDataPtr: UnsafeMutablePointer<Void> ``` |

Modified OBEXSession.OBEXAbort(UnsafeMutablePointer<Void>, optionalHeadersLength: Int, eventSelector: Selector, selectorTarget: AnyObject!, refCon: UnsafeMutablePointer<Void>) -> OBEXError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OBEXAbort(_ inOptionalHeaders: UnsafePointer<()>, optionalHeadersLength inOptionalHeadersLength: UInt, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafePointer<()>) -> OBEXError ``` | OS X 10.10 |
| To | ``` func OBEXAbort(_ inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError ``` | OS X 10.10.3 |

Modified OBEXSession.OBEXAbortResponse(OBEXOpCode, optionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength: Int, eventSelector: Selector, selectorTarget: AnyObject!, refCon: UnsafeMutablePointer<Void>) -> OBEXError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OBEXAbortResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafePointer<()>, optionalHeadersLength inOptionalHeadersLength: UInt, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafePointer<()>) -> OBEXError ``` | OS X 10.10 |
| To | ``` func OBEXAbortResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError ``` | OS X 10.10.3 |

Modified OBEXSession.OBEXConnect(OBEXFlags, maxPacketLength: OBEXMaxPacketLength, optionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength: Int, eventSelector: Selector, selectorTarget: AnyObject!, refCon: UnsafeMutablePointer<Void>) -> OBEXError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OBEXConnect(_ inFlags: OBEXFlags, maxPacketLength inMaxPacketLength: OBEXMaxPacketLength, optionalHeaders inOptionalHeaders: UnsafePointer<()>, optionalHeadersLength inOptionalHeadersLength: UInt, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafePointer<()>) -> OBEXError ``` | OS X 10.10 |
| To | ``` func OBEXConnect(_ inFlags: OBEXFlags, maxPacketLength inMaxPacketLength: OBEXMaxPacketLength, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError ``` | OS X 10.10.3 |

Modified OBEXSession.OBEXConnectResponse(OBEXOpCode, flags: OBEXFlags, maxPacketLength: OBEXMaxPacketLength, optionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength: Int, eventSelector: Selector, selectorTarget: AnyObject!, refCon: UnsafeMutablePointer<Void>) -> OBEXError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OBEXConnectResponse(_ inResponseOpCode: OBEXOpCode, flags inFlags: OBEXFlags, maxPacketLength inMaxPacketLength: OBEXMaxPacketLength, optionalHeaders inOptionalHeaders: UnsafePointer<()>, optionalHeadersLength inOptionalHeadersLength: UInt, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafePointer<()>) -> OBEXError ``` | OS X 10.10 |
| To | ``` func OBEXConnectResponse(_ inResponseOpCode: OBEXOpCode, flags inFlags: OBEXFlags, maxPacketLength inMaxPacketLength: OBEXMaxPacketLength, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError ``` | OS X 10.10.3 |

Modified OBEXSession.OBEXDisconnect(UnsafeMutablePointer<Void>, optionalHeadersLength: Int, eventSelector: Selector, selectorTarget: AnyObject!, refCon: UnsafeMutablePointer<Void>) -> OBEXError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OBEXDisconnect(_ inOptionalHeaders: UnsafePointer<()>, optionalHeadersLength inOptionalHeadersLength: UInt, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafePointer<()>) -> OBEXError ``` | OS X 10.10 |
| To | ``` func OBEXDisconnect(_ inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError ``` | OS X 10.10.3 |

Modified OBEXSession.OBEXDisconnectResponse(OBEXOpCode, optionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength: Int, eventSelector: Selector, selectorTarget: AnyObject!, refCon: UnsafeMutablePointer<Void>) -> OBEXError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OBEXDisconnectResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafePointer<()>, optionalHeadersLength inOptionalHeadersLength: UInt, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafePointer<()>) -> OBEXError ``` | OS X 10.10 |
| To | ``` func OBEXDisconnectResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError ``` | OS X 10.10.3 |

Modified OBEXSession.OBEXGet(Boolean, headers: UnsafeMutablePointer<Void>, headersLength: Int, eventSelector: Selector, selectorTarget: AnyObject!, refCon: UnsafeMutablePointer<Void>) -> OBEXError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OBEXGet(_ isFinalChunk: Boolean, headers inHeaders: UnsafePointer<()>, headersLength inHeadersLength: UInt, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafePointer<()>) -> OBEXError ``` | OS X 10.10 |
| To | ``` func OBEXGet(_ isFinalChunk: Boolean, headers inHeaders: UnsafeMutablePointer<Void>, headersLength inHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError ``` | OS X 10.10.3 |

Modified OBEXSession.OBEXGetResponse(OBEXOpCode, optionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength: Int, eventSelector: Selector, selectorTarget: AnyObject!, refCon: UnsafeMutablePointer<Void>) -> OBEXError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OBEXGetResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafePointer<()>, optionalHeadersLength inOptionalHeadersLength: UInt, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafePointer<()>) -> OBEXError ``` | OS X 10.10 |
| To | ``` func OBEXGetResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError ``` | OS X 10.10.3 |

Modified OBEXSession.OBEXPut(Boolean, headersData: UnsafeMutablePointer<Void>, headersDataLength: Int, bodyData: UnsafeMutablePointer<Void>, bodyDataLength: Int, eventSelector: Selector, selectorTarget: AnyObject!, refCon: UnsafeMutablePointer<Void>) -> OBEXError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OBEXPut(_ isFinalChunk: Boolean, headersData inHeadersData: UnsafePointer<()>, headersDataLength inHeadersDataLength: UInt, bodyData inBodyData: UnsafePointer<()>, bodyDataLength inBodyDataLength: UInt, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafePointer<()>) -> OBEXError ``` | OS X 10.10 |
| To | ``` func OBEXPut(_ isFinalChunk: Boolean, headersData inHeadersData: UnsafeMutablePointer<Void>, headersDataLength inHeadersDataLength: Int, bodyData inBodyData: UnsafeMutablePointer<Void>, bodyDataLength inBodyDataLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError ``` | OS X 10.10.3 |

Modified OBEXSession.OBEXPutResponse(OBEXOpCode, optionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength: Int, eventSelector: Selector, selectorTarget: AnyObject!, refCon: UnsafeMutablePointer<Void>) -> OBEXError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OBEXPutResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafePointer<()>, optionalHeadersLength inOptionalHeadersLength: UInt, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafePointer<()>) -> OBEXError ``` | OS X 10.10 |
| To | ``` func OBEXPutResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError ``` | OS X 10.10.3 |

Modified OBEXSession.OBEXSetPath(OBEXFlags, constants: OBEXConstants, optionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength: Int, eventSelector: Selector, selectorTarget: AnyObject!, refCon: UnsafeMutablePointer<Void>) -> OBEXError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OBEXSetPath(_ inFlags: OBEXFlags, constants inConstants: OBEXConstants, optionalHeaders inOptionalHeaders: UnsafePointer<()>, optionalHeadersLength inOptionalHeadersLength: UInt, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafePointer<()>) -> OBEXError ``` | OS X 10.10 |
| To | ``` func OBEXSetPath(_ inFlags: OBEXFlags, constants inConstants: OBEXConstants, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError ``` | OS X 10.10.3 |

Modified OBEXSession.OBEXSetPathResponse(OBEXOpCode, optionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength: Int, eventSelector: Selector, selectorTarget: AnyObject!, refCon: UnsafeMutablePointer<Void>) -> OBEXError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OBEXSetPathResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafePointer<()>, optionalHeadersLength inOptionalHeadersLength: UInt, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafePointer<()>) -> OBEXError ``` | OS X 10.10 |
| To | ``` func OBEXSetPathResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError ``` | OS X 10.10.3 |

Modified OBEXSession.clientHandleIncomingData(UnsafeMutablePointer<OBEXTransportEvent>)

|  | Declaration |
| --- | --- |
| From | ``` func clientHandleIncomingData(_ event: UnsafePointer<OBEXTransportEvent>) ``` |
| To | ``` func clientHandleIncomingData(_ event: UnsafeMutablePointer<OBEXTransportEvent>) ``` |

Modified OBEXSession.openTransportConnection(Selector, selectorTarget: AnyObject!, refCon: UnsafeMutablePointer<Void>) -> OBEXError

|  | Declaration |
| --- | --- |
| From | ``` func openTransportConnection(_ inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafePointer<()>) -> OBEXError ``` |
| To | ``` func openTransportConnection(_ inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError ``` |

Modified OBEXSession.sendDataToTransport(UnsafeMutablePointer<Void>, dataLength: Int) -> OBEXError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sendDataToTransport(_ inDataToSend: UnsafePointer<()>, dataLength inDataLength: UInt) -> OBEXError ``` | OS X 10.10 |
| To | ``` func sendDataToTransport(_ inDataToSend: UnsafeMutablePointer<Void>, dataLength inDataLength: Int) -> OBEXError ``` | OS X 10.10.3 |

Modified OBEXSession.serverHandleIncomingData(UnsafeMutablePointer<OBEXTransportEvent>)

|  | Declaration |
| --- | --- |
| From | ``` func serverHandleIncomingData(_ event: UnsafePointer<OBEXTransportEvent>) ``` |
| To | ``` func serverHandleIncomingData(_ event: UnsafeMutablePointer<OBEXTransportEvent>) ``` |

Modified OBEXSession.setEventRefCon(UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func setEventRefCon(_ inRefCon: UnsafePointer<()>) ``` |
| To | ``` func setEventRefCon(_ inRefCon: UnsafeMutablePointer<Void>) ``` |

Modified OBEXSessionEvent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OBEXSessionEvent {     var type: OBEXSessionEventType     var session: Unmanaged<OBEXSession>!     var refCon: UnsafePointer<()>     var isEndOfEventData: Boolean     var reserved1: UnsafePointer<()>     var reserved2: UnsafePointer<()> } ``` |
| To | ``` struct OBEXSessionEvent {     var type: OBEXSessionEventType     var session: OBEXSessionRef     var refCon: UnsafeMutablePointer<Void>     var isEndOfEventData: Boolean     var reserved1: UnsafeMutablePointer<Void>     var reserved2: UnsafeMutablePointer<Void>     init() } ``` |

Modified OBEXSessionEvent.refCon

|  | Declaration |
| --- | --- |
| From | ``` var refCon: UnsafePointer<()> ``` |
| To | ``` var refCon: UnsafeMutablePointer<Void> ``` |

Modified OBEXSessionEvent.reserved1

|  | Declaration |
| --- | --- |
| From | ``` var reserved1: UnsafePointer<()> ``` |
| To | ``` var reserved1: UnsafeMutablePointer<Void> ``` |

Modified OBEXSessionEvent.reserved2

|  | Declaration |
| --- | --- |
| From | ``` var reserved2: UnsafePointer<()> ``` |
| To | ``` var reserved2: UnsafeMutablePointer<Void> ``` |

Modified OBEXSessionEvent.session

|  | Declaration |
| --- | --- |
| From | ``` var session: Unmanaged<OBEXSession>! ``` |
| To | ``` var session: OBEXSessionRef ``` |

Modified OBEXSetPathCommandData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OBEXSetPathCommandData {     var headerDataPtr: UnsafePointer<()>     var headerDataLength: UInt     var flags: OBEXFlags     var constants: OBEXConstants } ``` |
| To | ``` struct OBEXSetPathCommandData {     var headerDataPtr: UnsafeMutablePointer<Void>     var headerDataLength: Int     var flags: OBEXFlags     var constants: OBEXConstants     init()     init(headerDataPtr headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength headerDataLength: Int, flags flags: OBEXFlags, constants constants: OBEXConstants) } ``` |

Modified OBEXSetPathCommandData.headerDataLength

|  | Declaration |
| --- | --- |
| From | ``` var headerDataLength: UInt ``` |
| To | ``` var headerDataLength: Int ``` |

Modified OBEXSetPathCommandData.headerDataPtr

|  | Declaration |
| --- | --- |
| From | ``` var headerDataPtr: UnsafePointer<()> ``` |
| To | ``` var headerDataPtr: UnsafeMutablePointer<Void> ``` |

Modified OBEXSetPathCommandResponseData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OBEXSetPathCommandResponseData {     var serverResponseOpCode: OBEXOpCode     var headerDataPtr: UnsafePointer<()>     var headerDataLength: UInt     var flags: OBEXFlags     var constants: OBEXConstants } ``` |
| To | ``` struct OBEXSetPathCommandResponseData {     var serverResponseOpCode: OBEXOpCode     var headerDataPtr: UnsafeMutablePointer<Void>     var headerDataLength: Int     var flags: OBEXFlags     var constants: OBEXConstants     init()     init(serverResponseOpCode serverResponseOpCode: OBEXOpCode, headerDataPtr headerDataPtr: UnsafeMutablePointer<Void>, headerDataLength headerDataLength: Int, flags flags: OBEXFlags, constants constants: OBEXConstants) } ``` |

Modified OBEXSetPathCommandResponseData.headerDataLength

|  | Declaration |
| --- | --- |
| From | ``` var headerDataLength: UInt ``` |
| To | ``` var headerDataLength: Int ``` |

Modified OBEXSetPathCommandResponseData.headerDataPtr

|  | Declaration |
| --- | --- |
| From | ``` var headerDataPtr: UnsafePointer<()> ``` |
| To | ``` var headerDataPtr: UnsafeMutablePointer<Void> ``` |

Modified OBEXTransportEvent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OBEXTransportEvent {     var type: OBEXTransportEventType     var status: OBEXError     var dataPtr: UnsafePointer<()>     var dataLength: UInt } ``` |
| To | ``` struct OBEXTransportEvent {     var type: OBEXTransportEventType     var status: OBEXError     var dataPtr: UnsafeMutablePointer<Void>     var dataLength: Int     init()     init(type type: OBEXTransportEventType, status status: OBEXError, dataPtr dataPtr: UnsafeMutablePointer<Void>, dataLength dataLength: Int) } ``` |

Modified OBEXTransportEvent.dataLength

|  | Declaration |
| --- | --- |
| From | ``` var dataLength: UInt ``` |
| To | ``` var dataLength: Int ``` |

Modified OBEXTransportEvent.dataPtr

|  | Declaration |
| --- | --- |
| From | ``` var dataPtr: UnsafePointer<()> ``` |
| To | ``` var dataPtr: UnsafeMutablePointer<Void> ``` |

Modified BluetoothTransportInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias BluetoothTransportInfoPtr = UnsafePointer<BluetoothTransportInfo> ``` |
| To | ``` typealias BluetoothTransportInfoPtr = UnsafeMutablePointer<BluetoothTransportInfo> ``` |

Modified IOBluetoothDeviceRegisterForDisconnectNotification(IOBluetoothDevice!, IOBluetoothUserNotificationCallback, UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>!

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothDeviceRegisterForDisconnectNotification(_ inDevice: IOBluetoothDevice!, _ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafePointer<()>) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothDeviceRegisterForDisconnectNotification(_ inDevice: IOBluetoothDevice!, _ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |

Modified IOBluetoothFindNumberOfRegistryEntriesOfClassName(UnsafePointer<Int8>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothFindNumberOfRegistryEntriesOfClassName(_ deviceType: ConstUnsafePointer<Int8>) -> Int ``` |
| To | ``` func IOBluetoothFindNumberOfRegistryEntriesOfClassName(_ deviceType: UnsafePointer<Int8>) -> Int ``` |

Modified IOBluetoothHandsFreeCallDirection

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothHandsFreeCallDirection: NSString! ``` |
| To | ``` let IOBluetoothHandsFreeCallDirection: String ``` |

Modified IOBluetoothHandsFreeCallIndex

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothHandsFreeCallIndex: NSString! ``` |
| To | ``` let IOBluetoothHandsFreeCallIndex: String ``` |

Modified IOBluetoothHandsFreeCallMode

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothHandsFreeCallMode: NSString! ``` |
| To | ``` let IOBluetoothHandsFreeCallMode: String ``` |

Modified IOBluetoothHandsFreeCallMultiparty

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothHandsFreeCallMultiparty: NSString! ``` |
| To | ``` let IOBluetoothHandsFreeCallMultiparty: String ``` |

Modified IOBluetoothHandsFreeCallName

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothHandsFreeCallName: NSString! ``` |
| To | ``` let IOBluetoothHandsFreeCallName: String ``` |

Modified IOBluetoothHandsFreeCallNumber

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothHandsFreeCallNumber: NSString! ``` |
| To | ``` let IOBluetoothHandsFreeCallNumber: String ``` |

Modified IOBluetoothHandsFreeCallStatus

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothHandsFreeCallStatus: NSString! ``` |
| To | ``` let IOBluetoothHandsFreeCallStatus: String ``` |

Modified IOBluetoothHandsFreeCallType

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothHandsFreeCallType: NSString! ``` |
| To | ``` let IOBluetoothHandsFreeCallType: String ``` |

Modified IOBluetoothHandsFreeIndicatorBattChg

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothHandsFreeIndicatorBattChg: NSString! ``` |
| To | ``` let IOBluetoothHandsFreeIndicatorBattChg: String ``` |

Modified IOBluetoothHandsFreeIndicatorCall

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothHandsFreeIndicatorCall: NSString! ``` |
| To | ``` let IOBluetoothHandsFreeIndicatorCall: String ``` |

Modified IOBluetoothHandsFreeIndicatorCallHeld

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothHandsFreeIndicatorCallHeld: NSString! ``` |
| To | ``` let IOBluetoothHandsFreeIndicatorCallHeld: String ``` |

Modified IOBluetoothHandsFreeIndicatorCallSetup

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothHandsFreeIndicatorCallSetup: NSString! ``` |
| To | ``` let IOBluetoothHandsFreeIndicatorCallSetup: String ``` |

Modified IOBluetoothHandsFreeIndicatorRoam

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothHandsFreeIndicatorRoam: NSString! ``` |
| To | ``` let IOBluetoothHandsFreeIndicatorRoam: String ``` |

Modified IOBluetoothHandsFreeIndicatorService

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothHandsFreeIndicatorService: NSString! ``` |
| To | ``` let IOBluetoothHandsFreeIndicatorService: String ``` |

Modified IOBluetoothHandsFreeIndicatorSignal

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothHandsFreeIndicatorSignal: NSString! ``` |
| To | ``` let IOBluetoothHandsFreeIndicatorSignal: String ``` |

Modified IOBluetoothHostControllerPoweredOffNotification

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothHostControllerPoweredOffNotification: NSString! ``` |
| To | ``` let IOBluetoothHostControllerPoweredOffNotification: String ``` |

Modified IOBluetoothHostControllerPoweredOnNotification

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothHostControllerPoweredOnNotification: NSString! ``` |
| To | ``` let IOBluetoothHostControllerPoweredOnNotification: String ``` |

Modified IOBluetoothL2CAPChannelIncomingDataListener

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothL2CAPChannelIncomingDataListener = CFunctionPointer<((IOBluetoothL2CAPChannel!, UnsafePointer<()>, UInt16, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias IOBluetoothL2CAPChannelIncomingDataListener = CFunctionPointer<((IOBluetoothL2CAPChannel!, UnsafeMutablePointer<Void>, UInt16, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified IOBluetoothL2CAPChannelIncomingEventListener

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothL2CAPChannelIncomingEventListener = CFunctionPointer<((IOBluetoothL2CAPChannel!, UnsafePointer<()>, UnsafePointer<IOBluetoothL2CAPChannelEvent>) -> Void)> ``` |
| To | ``` typealias IOBluetoothL2CAPChannelIncomingEventListener = CFunctionPointer<((IOBluetoothL2CAPChannel!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<IOBluetoothL2CAPChannelEvent>) -> Void)> ``` |

Modified IOBluetoothL2CAPChannelPublishedNotification

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothL2CAPChannelPublishedNotification: NSString! ``` |
| To | ``` let IOBluetoothL2CAPChannelPublishedNotification: String ``` |

Modified IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(IOBluetoothL2CAPChannel!, IOBluetoothUserNotificationCallback, UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>!

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(_ channel: IOBluetoothL2CAPChannel!, _ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafePointer<()>) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(_ channel: IOBluetoothL2CAPChannel!, _ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |

Modified IOBluetoothL2CAPChannelTerminatedNotification

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothL2CAPChannelTerminatedNotification: NSString! ``` |
| To | ``` let IOBluetoothL2CAPChannelTerminatedNotification: String ``` |

Modified IOBluetoothNSStringFromDeviceAddress(UnsafePointer<BluetoothDeviceAddress>) -> String!

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothNSStringFromDeviceAddress(_ deviceAddress: ConstUnsafePointer<BluetoothDeviceAddress>) -> String! ``` |
| To | ``` func IOBluetoothNSStringFromDeviceAddress(_ deviceAddress: UnsafePointer<BluetoothDeviceAddress>) -> String! ``` |

Modified IOBluetoothNSStringFromDeviceAddressColon(UnsafePointer<BluetoothDeviceAddress>) -> String!

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothNSStringFromDeviceAddressColon(_ deviceAddress: ConstUnsafePointer<BluetoothDeviceAddress>) -> String! ``` |
| To | ``` func IOBluetoothNSStringFromDeviceAddressColon(_ deviceAddress: UnsafePointer<BluetoothDeviceAddress>) -> String! ``` |

Modified IOBluetoothNSStringToDeviceAddress(String!, UnsafeMutablePointer<BluetoothDeviceAddress>) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothNSStringToDeviceAddress(_ inNameString: String!, _ outDeviceAddress: UnsafePointer<BluetoothDeviceAddress>) -> IOReturn ``` |
| To | ``` func IOBluetoothNSStringToDeviceAddress(_ inNameString: String!, _ outDeviceAddress: UnsafeMutablePointer<BluetoothDeviceAddress>) -> IOReturn ``` |

Modified IOBluetoothOBEXSessionOpenConnectionCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothOBEXSessionOpenConnectionCallback = CFunctionPointer<((OBEXSession!, OBEXError, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias IOBluetoothOBEXSessionOpenConnectionCallback = CFunctionPointer<((OBEXSessionRef, OBEXError, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified IOBluetoothPDUEncoding

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothPDUEncoding: NSString! ``` |
| To | ``` let IOBluetoothPDUEncoding: String ``` |

Modified IOBluetoothPDUOriginatingAddress

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothPDUOriginatingAddress: NSString! ``` |
| To | ``` let IOBluetoothPDUOriginatingAddress: String ``` |

Modified IOBluetoothPDUOriginatingAddressType

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothPDUOriginatingAddressType: NSString! ``` |
| To | ``` let IOBluetoothPDUOriginatingAddressType: String ``` |

Modified IOBluetoothPDUProtocolID

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothPDUProtocolID: NSString! ``` |
| To | ``` let IOBluetoothPDUProtocolID: String ``` |

Modified IOBluetoothPDUServicCenterAddress

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothPDUServicCenterAddress: NSString! ``` |
| To | ``` let IOBluetoothPDUServicCenterAddress: String ``` |

Modified IOBluetoothPDUServiceCenterAddressType

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothPDUServiceCenterAddressType: NSString! ``` |
| To | ``` let IOBluetoothPDUServiceCenterAddressType: String ``` |

Modified IOBluetoothPDUTimestamp

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothPDUTimestamp: NSString! ``` |
| To | ``` let IOBluetoothPDUTimestamp: String ``` |

Modified IOBluetoothPDUType

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothPDUType: NSString! ``` |
| To | ``` let IOBluetoothPDUType: String ``` |

Modified IOBluetoothPDUUserData

|  | Declaration |
| --- | --- |
| From | ``` let IOBluetoothPDUUserData: NSString! ``` |
| To | ``` let IOBluetoothPDUUserData: String ``` |

Modified IOBluetoothPackDataList(UnsafeMutablePointer<Void>, UnsafePointer<Int8>, CVaListPointer) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothPackDataList(_ ioBuffer: UnsafePointer<()>, _ inFormat: ConstUnsafePointer<Int8>, _ inArgs: CVaListPointer) -> Int ``` |
| To | ``` func IOBluetoothPackDataList(_ ioBuffer: UnsafeMutablePointer<Void>, _ inFormat: UnsafePointer<Int8>, _ inArgs: CVaListPointer) -> Int ``` |

Modified IOBluetoothRFCOMMChannelRegisterForChannelCloseNotification(IOBluetoothRFCOMMChannel!, IOBluetoothUserNotificationCallback, UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>!

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRFCOMMChannelRegisterForChannelCloseNotification(_ inChannel: IOBluetoothRFCOMMChannel!, _ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafePointer<()>) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothRFCOMMChannelRegisterForChannelCloseNotification(_ inChannel: IOBluetoothRFCOMMChannel!, _ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |

Modified IOBluetoothRegisterForDeviceConnectNotifications(IOBluetoothUserNotificationCallback, UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>!

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRegisterForDeviceConnectNotifications(_ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafePointer<()>) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothRegisterForDeviceConnectNotifications(_ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |

Modified IOBluetoothRegisterForFilteredL2CAPChannelOpenNotifications(IOBluetoothUserNotificationCallback, UnsafeMutablePointer<Void>, BluetoothL2CAPPSM, IOBluetoothUserNotificationChannelDirection) -> Unmanaged<IOBluetoothUserNotification>!

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRegisterForFilteredL2CAPChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafePointer<()>, _ inPSM: BluetoothL2CAPPSM, _ inDirection: IOBluetoothUserNotificationChannelDirection) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothRegisterForFilteredL2CAPChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafeMutablePointer<Void>, _ inPSM: BluetoothL2CAPPSM, _ inDirection: IOBluetoothUserNotificationChannelDirection) -> Unmanaged<IOBluetoothUserNotification>! ``` |

Modified IOBluetoothRegisterForFilteredRFCOMMChannelOpenNotifications(IOBluetoothUserNotificationCallback, UnsafeMutablePointer<Void>, BluetoothRFCOMMChannelID, IOBluetoothUserNotificationChannelDirection) -> Unmanaged<IOBluetoothUserNotification>!

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRegisterForFilteredRFCOMMChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafePointer<()>, _ channelID: BluetoothRFCOMMChannelID, _ inDirection: IOBluetoothUserNotificationChannelDirection) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothRegisterForFilteredRFCOMMChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafeMutablePointer<Void>, _ channelID: BluetoothRFCOMMChannelID, _ inDirection: IOBluetoothUserNotificationChannelDirection) -> Unmanaged<IOBluetoothUserNotification>! ``` |

Modified IOBluetoothRegisterForL2CAPChannelOpenNotifications(IOBluetoothUserNotificationCallback, UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>!

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRegisterForL2CAPChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafePointer<()>) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothRegisterForL2CAPChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |

Modified IOBluetoothRegisterForRFCOMMChannelOpenNotifications(IOBluetoothUserNotificationCallback, UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>!

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRegisterForRFCOMMChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafePointer<()>) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothRegisterForRFCOMMChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |

Modified IOBluetoothUnpackDataList(Int, UnsafePointer<Void>, UnsafePointer<Int8>, CVaListPointer) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IOBluetoothUnpackDataList(_ inBufferSize: ByteCount, _ inBuffer: ConstUnsafePointer<()>, _ inFormat: ConstUnsafePointer<Int8>, _ inArgs: CVaListPointer) -> Int ``` | OS X 10.10 |
| To | ``` func IOBluetoothUnpackDataList(_ inBufferSize: Int, _ inBuffer: UnsafePointer<Void>, _ inFormat: UnsafePointer<Int8>, _ inArgs: CVaListPointer) -> Int ``` | OS X 10.10.3 |

Modified IOBluetoothUserNotificationCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothUserNotificationCallback = CFunctionPointer<((UnsafePointer<()>, IOBluetoothUserNotification!, IOBluetoothObject!) -> Void)> ``` |
| To | ``` typealias IOBluetoothUserNotificationCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, IOBluetoothUserNotification!, IOBluetoothObject!) -> Void)> ``` |

Modified OBEXAddApplicationParameterHeader(UnsafePointer<Void>, UInt32, CFMutableDictionary!) -> OBEXError

|  | Declaration |
| --- | --- |
| From | ``` func OBEXAddApplicationParameterHeader(_ inHeaderData: ConstUnsafePointer<()>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |
| To | ``` func OBEXAddApplicationParameterHeader(_ inHeaderData: UnsafePointer<Void>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |

Modified OBEXAddAuthorizationChallengeHeader(UnsafePointer<Void>, UInt32, CFMutableDictionary!) -> OBEXError

|  | Declaration |
| --- | --- |
| From | ``` func OBEXAddAuthorizationChallengeHeader(_ inHeaderData: ConstUnsafePointer<()>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |
| To | ``` func OBEXAddAuthorizationChallengeHeader(_ inHeaderData: UnsafePointer<Void>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |

Modified OBEXAddAuthorizationResponseHeader(UnsafePointer<Void>, UInt32, CFMutableDictionary!) -> OBEXError

|  | Declaration |
| --- | --- |
| From | ``` func OBEXAddAuthorizationResponseHeader(_ inHeaderData: ConstUnsafePointer<()>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |
| To | ``` func OBEXAddAuthorizationResponseHeader(_ inHeaderData: UnsafePointer<Void>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |

Modified OBEXAddBodyHeader(UnsafePointer<Void>, UInt32, Boolean, CFMutableDictionary!) -> OBEXError

|  | Declaration |
| --- | --- |
| From | ``` func OBEXAddBodyHeader(_ inHeaderData: ConstUnsafePointer<()>, _ inHeaderDataLength: UInt32, _ isEndOfBody: Boolean, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |
| To | ``` func OBEXAddBodyHeader(_ inHeaderData: UnsafePointer<Void>, _ inHeaderDataLength: UInt32, _ isEndOfBody: Boolean, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |

Modified OBEXAddByteSequenceHeader(UnsafePointer<Void>, UInt32, CFMutableDictionary!) -> OBEXError

|  | Declaration |
| --- | --- |
| From | ``` func OBEXAddByteSequenceHeader(_ inHeaderData: ConstUnsafePointer<()>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |
| To | ``` func OBEXAddByteSequenceHeader(_ inHeaderData: UnsafePointer<Void>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |

Modified OBEXAddConnectionIDHeader(UnsafePointer<Void>, UInt32, CFMutableDictionary!) -> OBEXError

|  | Declaration |
| --- | --- |
| From | ``` func OBEXAddConnectionIDHeader(_ inHeaderData: ConstUnsafePointer<()>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |
| To | ``` func OBEXAddConnectionIDHeader(_ inHeaderData: UnsafePointer<Void>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |

Modified OBEXAddHTTPHeader(UnsafePointer<Void>, UInt32, CFMutableDictionary!) -> OBEXError

|  | Declaration |
| --- | --- |
| From | ``` func OBEXAddHTTPHeader(_ inHeaderData: ConstUnsafePointer<()>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |
| To | ``` func OBEXAddHTTPHeader(_ inHeaderData: UnsafePointer<Void>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |

Modified OBEXAddObjectClassHeader(UnsafePointer<Void>, UInt32, CFMutableDictionary!) -> OBEXError

|  | Declaration |
| --- | --- |
| From | ``` func OBEXAddObjectClassHeader(_ inHeaderData: ConstUnsafePointer<()>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |
| To | ``` func OBEXAddObjectClassHeader(_ inHeaderData: UnsafePointer<Void>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |

Modified OBEXAddTargetHeader(UnsafePointer<Void>, UInt32, CFMutableDictionary!) -> OBEXError

|  | Declaration |
| --- | --- |
| From | ``` func OBEXAddTargetHeader(_ inHeaderData: ConstUnsafePointer<()>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |
| To | ``` func OBEXAddTargetHeader(_ inHeaderData: UnsafePointer<Void>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |

Modified OBEXAddTimeISOHeader(UnsafePointer<Void>, UInt32, CFMutableDictionary!) -> OBEXError

|  | Declaration |
| --- | --- |
| From | ``` func OBEXAddTimeISOHeader(_ inHeaderData: ConstUnsafePointer<()>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |
| To | ``` func OBEXAddTimeISOHeader(_ inHeaderData: UnsafePointer<Void>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |

Modified OBEXAddUserDefinedHeader(UnsafePointer<Void>, UInt32, CFMutableDictionary!) -> OBEXError

|  | Declaration |
| --- | --- |
| From | ``` func OBEXAddUserDefinedHeader(_ inHeaderData: ConstUnsafePointer<()>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |
| To | ``` func OBEXAddUserDefinedHeader(_ inHeaderData: UnsafePointer<Void>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |

Modified OBEXAddWhoHeader(UnsafePointer<Void>, UInt32, CFMutableDictionary!) -> OBEXError

|  | Declaration |
| --- | --- |
| From | ``` func OBEXAddWhoHeader(_ inHeaderData: ConstUnsafePointer<()>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |
| To | ``` func OBEXAddWhoHeader(_ inHeaderData: UnsafePointer<Void>, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |

Modified OBEXGetHeaders(UnsafePointer<Void>, Int) -> CFDictionary!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OBEXGetHeaders(_ inData: ConstUnsafePointer<()>, _ inDataSize: UInt) -> CFDictionary! ``` | OS X 10.10 |
| To | ``` func OBEXGetHeaders(_ inData: UnsafePointer<Void>, _ inDataSize: Int) -> CFDictionary! ``` | OS X 10.10.3 |

Modified OBEXSessionEventCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias OBEXSessionEventCallback = CFunctionPointer<((ConstUnsafePointer<OBEXSessionEvent>) -> Void)> ``` |
| To | ``` typealias OBEXSessionEventCallback = CFunctionPointer<((UnsafePointer<OBEXSessionEvent>) -> Void)> ``` |

Modified OBEXSessionRef

|  | Declaration |
| --- | --- |
| From | ``` typealias OBEXSessionRef = OBEXSession ``` |
| To | ``` typealias OBEXSessionRef = COpaquePointer ``` |

Modified PrivOBEXSessionDataRef

|  | Declaration |
| --- | --- |
| From | ``` typealias PrivOBEXSessionDataRef = PrivOBEXSessionData ``` |
| To | ``` typealias PrivOBEXSessionDataRef = COpaquePointer ``` |

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
