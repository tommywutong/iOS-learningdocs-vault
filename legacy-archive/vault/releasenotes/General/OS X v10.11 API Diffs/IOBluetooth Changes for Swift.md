---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/IOBluetooth.html
archived_at: '2026-07-18T02:53:36.028294Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# IOBluetooth Changes for Swift

### IOBluetooth

Removed BluetoothAMPCommandRejectReason.valueRemoved BluetoothAMPCreatePhysicalLinkResponseStatus.valueRemoved BluetoothAMPDisconnectPhysicalLinkResponseStatus.valueRemoved BluetoothAMPDiscoverResponseControllerStatus.valueRemoved BluetoothAMPGetAssocResponseStatus.valueRemoved BluetoothAMPGetInfoResponseStatus.valueRemoved BluetoothAMPManagerCode.valueRemoved BluetoothAuthenticationRequirementsValues.valueRemoved BluetoothCompanyIdentifers.valueRemoved BluetoothFeatureBits.valueRemoved BluetoothHCIAFHChannelAssessmentModes.valueRemoved BluetoothHCIAuthentionEnableModes.valueRemoved BluetoothHCIConnectionModes.valueRemoved BluetoothHCIDeleteStoredLinkKeyFlags.valueRemoved BluetoothHCIEncryptionModes.valueRemoved BluetoothHCIExtendedInquiryResponseDataTypes.valueRemoved BluetoothHCIFECRequiredValues.valueRemoved BluetoothHCIGeneralFlowControlStates.valueRemoved BluetoothHCIHoldModeActivityStates.valueRemoved BluetoothHCIInquiryModes.valueRemoved BluetoothHCIInquiryScanTypes.valueRemoved BluetoothHCILinkPolicySettingsValues.valueRemoved BluetoothHCIPageScanEnableStates.valueRemoved BluetoothHCIPageScanModes.valueRemoved BluetoothHCIPageScanPeriodModes.valueRemoved BluetoothHCIPageScanTypes.valueRemoved BluetoothHCIPowerState.valueRemoved BluetoothHCIReadStoredLinkKeysFlags.valueRemoved BluetoothHCIRetransmissionEffortTypes.valueRemoved BluetoothHCIRoles.valueRemoved BluetoothHCISCOFlowControlStates.valueRemoved BluetoothHCISimplePairingModes.valueRemoved BluetoothHCITimeoutValues.valueRemoved BluetoothHCITransmitReadPowerLevelTypes.valueRemoved BluetoothHCIVersions.valueRemoved BluetoothIOCapabilities.valueRemoved BluetoothKeypressNotificationTypes.valueRemoved BluetoothL2CAPCommandCode.valueRemoved BluetoothL2CAPCommandRejectReason.valueRemoved BluetoothL2CAPConfigurationOption.valueRemoved BluetoothL2CAPConfigurationResult.valueRemoved BluetoothL2CAPConfigurationRetransmissionAndFlowControlFlags.valueRemoved BluetoothL2CAPConnectionResult.valueRemoved BluetoothL2CAPConnectionStatus.valueRemoved BluetoothL2CAPInformationExtendedFeaturesMask.valueRemoved BluetoothL2CAPInformationResult.valueRemoved BluetoothL2CAPInformationType.valueRemoved BluetoothL2CAPQoSType.valueRemoved BluetoothLEAddressType.valueRemoved BluetoothLEAdvertisingType.valueRemoved BluetoothLEConnectionInterval.valueRemoved BluetoothLEScan.valueRemoved BluetoothLEScanDuplicateFilter.valueRemoved BluetoothLEScanFilter.valueRemoved BluetoothLEScanType.valueRemoved BluetoothLESecurityManagerCommandCode.valueRemoved BluetoothLESecurityManagerIOCapability.valueRemoved BluetoothLESecurityManagerKeyDistributionFormat.valueRemoved BluetoothLESecurityManagerOOBData.valueRemoved BluetoothLESecurityManagerPairingFailedReasonCode.valueRemoved BluetoothLESecurityManagerUserInputCapability.valueRemoved BluetoothLESecurityManagerUserOutputCapability.valueRemoved BluetoothLinkTypes.valueRemoved BluetoothLMPVersions.valueRemoved BluetoothOOBDataPresenceValues.valueRemoved BluetoothRFCOMMLineStatus.valueRemoved BluetoothRFCOMMParityType.valueRemoved BluetoothSimplePairingDebugModes.valueRemoved BluetoothTransportTypes.valueRemoved FTSFileType.valueRemoved IOBluetoothDevice.isHandsFreeAudioGateway() -> BoolRemoved IOBluetoothDevice.isHandsFreeDevice() -> BoolRemoved IOBluetoothDeviceSearchOptionsBits.valueRemoved IOBluetoothDeviceSearchTypesBits.valueRemoved IOBluetoothL2CAPChannelEventType.valueRemoved IOBluetoothUserNotificationChannelDirection.valueRemoved OBEXConnectFlagValues.valueRemoved OBEXErrorCodes.valueRemoved OBEXHeaderIdentifiers.valueRemoved OBEXNonceFlagValues.valueRemoved OBEXOpCodeCommandValues.valueRemoved OBEXOpCodeResponseValues.valueRemoved OBEXOpCodeSessionValues.valueRemoved OBEXPutFlagValues.valueRemoved OBEXRealmValues.valueRemoved OBEXSessionEventTypes.valueRemoved OBEXSessionParameterTags.valueRemoved OBEXTransportEventTypes.valueRemoved OBEXVersions.valueRemoved ProtocolParameters.valueRemoved SDPAttributeDeviceIdentificationRecord.valueRemoved SDPAttributeIdentifierCodes.valueRemoved SDPServiceClasses.valueRemoved [IOBluetoothLaunchHandsFreeAgent(_: String!) -> Boolean](https://developer.apple.com/documentation/iobluetooth/iobluetoothutilities.h/1811195-iobluetoothlaunchhandsfreeagent)Added BluetoothAMPCommandRejectReason.init(rawValue: UInt32)Added BluetoothAMPCommandRejectReason.rawValueAdded BluetoothAMPCreatePhysicalLinkResponseStatus.init(rawValue: UInt32)Added BluetoothAMPCreatePhysicalLinkResponseStatus.rawValueAdded BluetoothAMPDisconnectPhysicalLinkResponseStatus.init(rawValue: UInt32)Added BluetoothAMPDisconnectPhysicalLinkResponseStatus.rawValueAdded BluetoothAMPDiscoverResponseControllerStatus.init(rawValue: UInt32)Added BluetoothAMPDiscoverResponseControllerStatus.rawValueAdded BluetoothAMPGetAssocResponseStatus.init(rawValue: UInt32)Added BluetoothAMPGetAssocResponseStatus.rawValueAdded BluetoothAMPGetInfoResponseStatus.init(rawValue: UInt32)Added BluetoothAMPGetInfoResponseStatus.rawValueAdded BluetoothAMPManagerCode.init(rawValue: UInt32)Added BluetoothAMPManagerCode.rawValueAdded BluetoothAuthenticationRequirementsValues.init(rawValue: UInt32)Added BluetoothAuthenticationRequirementsValues.rawValueAdded BluetoothCompanyIdentifers.init(rawValue: UInt32)Added BluetoothCompanyIdentifers.rawValueAdded BluetoothFeatureBits.init(rawValue: UInt32)Added BluetoothFeatureBits.rawValueAdded BluetoothHCIAFHChannelAssessmentModes.init(rawValue: UInt32)Added BluetoothHCIAFHChannelAssessmentModes.rawValueAdded BluetoothHCIAuthentionEnableModes.init(rawValue: UInt32)Added BluetoothHCIAuthentionEnableModes.rawValueAdded BluetoothHCIConnectionModes.init(rawValue: UInt32)Added BluetoothHCIConnectionModes.rawValueAdded [BluetoothHCICurrentInquiryAccessCodesForWrite [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhcicurrentinquiryaccesscodesforwrite)Added [BluetoothHCICurrentInquiryAccessCodesForWrite.codes](https://developer.apple.com/documentation/iobluetooth/bluetoothhcicurrentinquiryaccesscodesforwrite/1429848-codes)Added [BluetoothHCICurrentInquiryAccessCodesForWrite.count](https://developer.apple.com/documentation/iobluetooth/bluetoothhcicurrentinquiryaccesscodesforwrite/1433549-count)Added BluetoothHCICurrentInquiryAccessCodesForWrite.init()Added BluetoothHCICurrentInquiryAccessCodesForWrite.init(count: BluetoothHCIInquiryAccessCodeCount, codes: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added BluetoothHCIDeleteStoredLinkKeyFlags.init(rawValue: UInt32)Added BluetoothHCIDeleteStoredLinkKeyFlags.rawValueAdded BluetoothHCIEncryptionModes.init(rawValue: UInt32)Added BluetoothHCIEncryptionModes.rawValueAdded BluetoothHCIExtendedInquiryResponseDataTypes.init(rawValue: UInt32)Added BluetoothHCIExtendedInquiryResponseDataTypes.rawValueAdded BluetoothHCIFECRequiredValues.init(rawValue: UInt32)Added BluetoothHCIFECRequiredValues.rawValueAdded BluetoothHCIGeneralFlowControlStates.init(rawValue: UInt32)Added BluetoothHCIGeneralFlowControlStates.rawValueAdded BluetoothHCIHoldModeActivityStates.init(rawValue: UInt32)Added BluetoothHCIHoldModeActivityStates.rawValueAdded BluetoothHCIInquiryModes.init(rawValue: UInt32)Added BluetoothHCIInquiryModes.rawValueAdded BluetoothHCIInquiryScanTypes.init(rawValue: UInt32)Added BluetoothHCIInquiryScanTypes.rawValueAdded BluetoothHCILinkPolicySettingsValues.init(rawValue: UInt32)Added BluetoothHCILinkPolicySettingsValues.rawValueAdded BluetoothHCIPageScanEnableStates.init(rawValue: UInt32)Added BluetoothHCIPageScanEnableStates.rawValueAdded BluetoothHCIPageScanModes.init(rawValue: UInt32)Added BluetoothHCIPageScanModes.rawValueAdded BluetoothHCIPageScanPeriodModes.init(rawValue: UInt32)Added BluetoothHCIPageScanPeriodModes.rawValueAdded BluetoothHCIPageScanTypes.init(rawValue: UInt32)Added BluetoothHCIPageScanTypes.rawValueAdded BluetoothHCIPowerState.init(rawValue: UInt32)Added BluetoothHCIPowerState.rawValueAdded BluetoothHCIReadStoredLinkKeysFlags.init(rawValue: UInt32)Added BluetoothHCIReadStoredLinkKeysFlags.rawValueAdded BluetoothHCIRetransmissionEffortTypes.init(rawValue: UInt32)Added BluetoothHCIRetransmissionEffortTypes.rawValueAdded BluetoothHCIRoles.init(rawValue: UInt32)Added BluetoothHCIRoles.rawValueAdded BluetoothHCISCOFlowControlStates.init(rawValue: UInt32)Added BluetoothHCISCOFlowControlStates.rawValueAdded BluetoothHCISimplePairingModes.init(rawValue: UInt32)Added BluetoothHCISimplePairingModes.rawValueAdded BluetoothHCITimeoutValues.init(rawValue: UInt32)Added BluetoothHCITimeoutValues.rawValueAdded BluetoothHCITransmitReadPowerLevelTypes.init(rawValue: UInt32)Added BluetoothHCITransmitReadPowerLevelTypes.rawValueAdded BluetoothHCIVersions.init(rawValue: UInt32)Added BluetoothHCIVersions.rawValueAdded BluetoothIOCapabilities.init(rawValue: UInt32)Added BluetoothIOCapabilities.rawValueAdded BluetoothKeypressNotificationTypes.init(rawValue: UInt32)Added BluetoothKeypressNotificationTypes.rawValueAdded BluetoothL2CAPCommandCode.init(rawValue: UInt32)Added BluetoothL2CAPCommandCode.rawValueAdded BluetoothL2CAPCommandRejectReason.init(rawValue: UInt32)Added BluetoothL2CAPCommandRejectReason.rawValueAdded BluetoothL2CAPConfigurationOption.init(rawValue: UInt32)Added BluetoothL2CAPConfigurationOption.rawValueAdded BluetoothL2CAPConfigurationResult.init(rawValue: UInt32)Added BluetoothL2CAPConfigurationResult.rawValueAdded BluetoothL2CAPConfigurationRetransmissionAndFlowControlFlags.init(rawValue: UInt32)Added BluetoothL2CAPConfigurationRetransmissionAndFlowControlFlags.rawValueAdded BluetoothL2CAPConnectionResult.init(rawValue: UInt32)Added BluetoothL2CAPConnectionResult.rawValueAdded BluetoothL2CAPConnectionStatus.init(rawValue: UInt32)Added BluetoothL2CAPConnectionStatus.rawValueAdded BluetoothL2CAPInformationExtendedFeaturesMask.init(rawValue: UInt32)Added BluetoothL2CAPInformationExtendedFeaturesMask.rawValueAdded BluetoothL2CAPInformationResult.init(rawValue: UInt32)Added BluetoothL2CAPInformationResult.rawValueAdded BluetoothL2CAPInformationType.init(rawValue: UInt32)Added BluetoothL2CAPInformationType.rawValueAdded BluetoothL2CAPQoSType.init(rawValue: UInt32)Added BluetoothL2CAPQoSType.rawValueAdded BluetoothLEAddressType.init(rawValue: UInt32)Added BluetoothLEAddressType.rawValueAdded BluetoothLEAdvertisingType.init(rawValue: UInt32)Added BluetoothLEAdvertisingType.rawValueAdded BluetoothLEConnectionInterval.init(rawValue: UInt32)Added BluetoothLEConnectionInterval.rawValueAdded BluetoothLEScan.init(rawValue: UInt32)Added BluetoothLEScan.rawValueAdded BluetoothLEScanDuplicateFilter.init(rawValue: UInt32)Added BluetoothLEScanDuplicateFilter.rawValueAdded BluetoothLEScanFilter.init(rawValue: UInt32)Added BluetoothLEScanFilter.rawValueAdded BluetoothLEScanType.init(rawValue: UInt32)Added BluetoothLEScanType.rawValueAdded BluetoothLESecurityManagerCommandCode.init(rawValue: UInt32)Added BluetoothLESecurityManagerCommandCode.rawValueAdded BluetoothLESecurityManagerIOCapability.init(rawValue: UInt32)Added BluetoothLESecurityManagerIOCapability.rawValueAdded BluetoothLESecurityManagerKeyDistributionFormat.init(rawValue: UInt32)Added BluetoothLESecurityManagerKeyDistributionFormat.rawValueAdded [BluetoothLESecurityManagerKeypressNotificationType [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerkeypressnotificationtype)Added BluetoothLESecurityManagerKeypressNotificationType.init(_: UInt32)Added BluetoothLESecurityManagerKeypressNotificationType.init(rawValue: UInt32)Added BluetoothLESecurityManagerKeypressNotificationType.rawValueAdded BluetoothLESecurityManagerOOBData.init(rawValue: UInt32)Added BluetoothLESecurityManagerOOBData.rawValueAdded BluetoothLESecurityManagerPairingFailedReasonCode.init(rawValue: UInt32)Added BluetoothLESecurityManagerPairingFailedReasonCode.rawValueAdded BluetoothLESecurityManagerUserInputCapability.init(rawValue: UInt32)Added BluetoothLESecurityManagerUserInputCapability.rawValueAdded BluetoothLESecurityManagerUserOutputCapability.init(rawValue: UInt32)Added BluetoothLESecurityManagerUserOutputCapability.rawValueAdded BluetoothLinkTypes.init(rawValue: UInt32)Added BluetoothLinkTypes.rawValueAdded BluetoothLMPVersions.init(rawValue: UInt32)Added BluetoothLMPVersions.rawValueAdded BluetoothOOBDataPresenceValues.init(rawValue: UInt32)Added BluetoothOOBDataPresenceValues.rawValueAdded BluetoothRFCOMMLineStatus.init(rawValue: UInt32)Added BluetoothRFCOMMLineStatus.rawValueAdded BluetoothRFCOMMParityType.init(rawValue: UInt32)Added BluetoothRFCOMMParityType.rawValueAdded BluetoothSimplePairingDebugModes.init(rawValue: UInt32)Added BluetoothSimplePairingDebugModes.rawValueAdded BluetoothTransportTypes.init(rawValue: UInt32)Added BluetoothTransportTypes.rawValueAdded FTSFileType.init(rawValue: UInt32)Added FTSFileType.rawValueAdded [IOBluetoothDevice.handsFreeAudioGateway](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1427806-ishandsfreeaudiogateway)Added [IOBluetoothDevice.handsFreeDevice](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1427742-ishandsfreedevice)Added IOBluetoothDeviceSearchOptionsBits.init(rawValue: UInt32)Added IOBluetoothDeviceSearchOptionsBits.rawValueAdded IOBluetoothDeviceSearchTypesBits.init(rawValue: UInt32)Added IOBluetoothDeviceSearchTypesBits.rawValueAdded IOBluetoothL2CAPChannelEventType.init(rawValue: UInt32)Added IOBluetoothL2CAPChannelEventType.rawValueAdded IOBluetoothUserNotificationChannelDirection.init(rawValue: UInt32)Added IOBluetoothUserNotificationChannelDirection.rawValueAdded OBEXConnectFlagValues.init(rawValue: UInt32)Added OBEXConnectFlagValues.rawValueAdded OBEXErrorCodes.init(rawValue: Int32)Added OBEXErrorCodes.rawValueAdded OBEXHeaderIdentifiers.init(rawValue: UInt32)Added OBEXHeaderIdentifiers.rawValueAdded OBEXNonceFlagValues.init(rawValue: UInt32)Added OBEXNonceFlagValues.rawValueAdded OBEXOpCodeCommandValues.init(rawValue: UInt32)Added OBEXOpCodeCommandValues.rawValueAdded OBEXOpCodeResponseValues.init(rawValue: UInt32)Added OBEXOpCodeResponseValues.rawValueAdded OBEXOpCodeSessionValues.init(rawValue: UInt32)Added OBEXOpCodeSessionValues.rawValueAdded OBEXPutFlagValues.init(rawValue: UInt32)Added OBEXPutFlagValues.rawValueAdded OBEXRealmValues.init(rawValue: UInt32)Added OBEXRealmValues.rawValueAdded OBEXSessionEventTypes.init(rawValue: UInt32)Added OBEXSessionEventTypes.rawValueAdded OBEXSessionParameterTags.init(rawValue: UInt32)Added OBEXSessionParameterTags.rawValueAdded OBEXTransportEventTypes.init(rawValue: UInt32)Added OBEXTransportEventTypes.rawValueAdded OBEXVersions.init(rawValue: UInt32)Added OBEXVersions.rawValueAdded ProtocolParameters.init(rawValue: UInt32)Added ProtocolParameters.rawValueAdded SDPAttributeDeviceIdentificationRecord.init(rawValue: UInt32)Added SDPAttributeDeviceIdentificationRecord.rawValueAdded SDPAttributeIdentifierCodes.init(rawValue: UInt32)Added SDPAttributeIdentifierCodes.rawValueAdded SDPServiceClasses.init(rawValue: UInt32)Added SDPServiceClasses.rawValueAdded [kBluetoothHCICommandDeleteReservedLTADDR](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommanddeletereservedltaddr)Added [kBluetoothHCICommandEnhancedAcceptSynchronousConnectionRequest](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandenhancedacceptsynchronousconnectionrequest)Added [kBluetoothHCICommandEnhancedSetupSynchronousConnection](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandenhancedsetupsynchronousconnection)Added [kBluetoothHCICommandGetMWSTransportLayerConfiguration](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandgetmwstransportlayerconfiguration)Added [kBluetoothHCICommandLEAddDeviceToResolvingList](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandleadddevicetoresolvinglist)Added [kBluetoothHCICommandLEClearResolvingList](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandleclearresolvinglist)Added [kBluetoothHCICommandLEGenerateDHKey](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandlegeneratedhkey)Added [kBluetoothHCICommandLEReadLocalP256PublicKey](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandlereadlocalp256publickey)Added [kBluetoothHCICommandLEReadLocalResolvableAddress](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlereadlocalresolvableaddress)Added [kBluetoothHCICommandLEReadMaximumDataLength](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlereadmaximumdatalength)Added [kBluetoothHCICommandLEReadPeerResolvableAddress](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandlereadpeerresolvableaddress)Added [kBluetoothHCICommandLEReadResolvingListSize](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandlereadresolvinglistsize)Added [kBluetoothHCICommandLEReadSuggestedDefaultDataLength](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlereadsuggesteddefaultdatalength)Added [kBluetoothHCICommandLERemoteConnectionParameterRequestNegativeReply](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandleremoteconnectionparameterrequestnegativereply)Added [kBluetoothHCICommandLERemoteConnectionParameterRequestReply](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandleremoteconnectionparameterrequestreply)Added [kBluetoothHCICommandLERemoveDeviceFromResolvingList](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandleremovedevicefromresolvinglist)Added [kBluetoothHCICommandLESetAddressResolutionEnable](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandlesetaddressresolutionenable)Added [kBluetoothHCICommandLESetDataLength](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlesetdatalength)Added [kBluetoothHCICommandLESetResolvablePrivateAddressTimeout](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlesetresolvableprivateaddresstimeout)Added [kBluetoothHCICommandLEWriteSuggestedDefaultDataLength](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlewritesuggesteddefaultdatalength)Added [kBluetoothHCICommandReadAuthenticatedPayloadTimeout](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandreadauthenticatedpayloadtimeout)Added [kBluetoothHCICommandReadDataBlockSize](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandreaddatablocksize)Added [kBluetoothHCICommandReadExtendedInquiryLength](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandreadextendedinquirylength)Added [kBluetoothHCICommandReadExtendedPageTimeout](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandreadextendedpagetimeout)Added [kBluetoothHCICommandReadLocalOOBExtendedData](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandreadlocaloobextendeddata)Added [kBluetoothHCICommandReadLocalSupportedCodecs](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandreadlocalsupportedcodecs)Added [kBluetoothHCICommandReadSecureConnectionsHostSupport](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandreadsecureconnectionshostsupport)Added [kBluetoothHCICommandReadSynchronizationTrainParameters](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandreadsynchronizationtrainparameters)Added [kBluetoothHCICommandReceiveSynchronizationTrain](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandreceivesynchronizationtrain)Added [kBluetoothHCICommandRemoteOOBExtendedDataRequestReply](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandremoteoobextendeddatarequestreply)Added [kBluetoothHCICommandSetConnectionlessSlaveBroadcast](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandsetconnectionlessslavebroadcast)Added [kBluetoothHCICommandSetConnectionlessSlaveBroadcastData](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandsetconnectionlessslavebroadcastdata)Added [kBluetoothHCICommandSetConnectionlessSlaveBroadcastReceive](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandsetconnectionlessslavebroadcastreceive)Added [kBluetoothHCICommandSetExternalFrameConfiguration](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandsetexternalframeconfiguration)Added [kBluetoothHCICommandSetMWSChannelParameters](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandsetmwschannelparameters)Added [kBluetoothHCICommandSetMWSPATTERNConfiguration](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandsetmwspatternconfiguration)Added [kBluetoothHCICommandSetMWSScanFrequencyTable](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandsetmwsscanfrequencytable)Added [kBluetoothHCICommandSetMWSSignaling](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandsetmwssignaling)Added [kBluetoothHCICommandSetMWSTransportLayer](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandsetmwstransportlayer)Added [kBluetoothHCICommandSetReservedLTADDR](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandsetreservedltaddr)Added [kBluetoothHCICommandSetTriggeredClockCapture](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandsettriggeredclockcapture)Added [kBluetoothHCICommandStartSynchronizationTrain](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandstartsynchronizationtrain)Added [kBluetoothHCICommandTruncatedPage](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandtruncatedpage)Added [kBluetoothHCICommandTruncatedPageCancel](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandtruncatedpagecancel)Added [kBluetoothHCICommandWriteAuthenticatedPayloadTimeout](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandwriteauthenticatedpayloadtimeout)Added [kBluetoothHCICommandWriteExtendedInquiryLength](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandwriteextendedinquirylength)Added [kBluetoothHCICommandWriteExtendedPageTimeout](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandwriteextendedpagetimeout)Added [kBluetoothHCICommandWriteSecureConnectionsHostSupport](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandwritesecureconnectionshostsupport)Added [kBluetoothHCICommandWriteSynchronizationTrainParameters](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandwritesynchronizationtrainparameters)Added [kBluetoothL2CAPPSMAVCTP_Browsing](https://developer.apple.com/documentation/iobluetooth/1459299-anonymous/kbluetoothl2cappsmavctp_browsing)Added [kBluetoothLESecurityManagerLinkKey](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerkeydistributionformat/kbluetoothlesecuritymanagerlinkkey)Added [kBluetoothLESecurityManagerNotificationTypePasskeyCleared](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerkeypressnotificationtype/kbluetoothlesecuritymanagernotificationtypepasskeycleared)Added [kBluetoothLESecurityManagerNotificationTypePasskeyDigitEntered](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanagernotificationtypepasskeydigitentered)Added [kBluetoothLESecurityManagerNotificationTypePasskeyDigitErased](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerkeypressnotificationtype/kbluetoothlesecuritymanagernotificationtypepasskeydigiterased)Added [kBluetoothLESecurityManagerNotificationTypePasskeyEntryCompleted](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanagernotificationtypepasskeyentrycompleted)Added [kBluetoothLESecurityManagerNotificationTypePasskeyEntryStarted](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanagernotificationtypepasskeyentrystarted)Added [kBluetoothLESecurityManagerNotificationTypeReservedEnd](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerkeypressnotificationtype/kbluetoothlesecuritymanagernotificationtypereservedend)Added [kBluetoothLESecurityManagerNotificationTypeReservedStart](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanagernotificationtypereservedstart)Added [kBluetoothLESecurityManagerReasonCodeBREDRPairingInProgress](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerpairingfailedreasoncode/kbluetoothlesecuritymanagerreasoncodebredrpairinginprogress)Added [kBluetoothLESecurityManagerReasonCodeCrossTransportKeyDerivationGenerationNotAllowed](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerpairingfailedreasoncode/kbluetoothlesecuritymanagerreasoncodecrosstransportkeyderivationgenerationnotallowed)Added [kMaximumNumberOfInquiryAccessCodes](https://developer.apple.com/documentation/iobluetooth/1489444-anonymous/kmaximumnumberofinquiryaccesscodes)Modified [BluetoothAMPCommandRejectReason [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothampcommandrejectreason)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothAMPCommandRejectReason {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothAMPCommandRejectReason : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothAMPCreatePhysicalLinkResponseStatus [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothampcreatephysicallinkresponsestatus)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothAMPCreatePhysicalLinkResponseStatus {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothAMPCreatePhysicalLinkResponseStatus : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothAMPDisconnectPhysicalLinkResponseStatus [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothampdisconnectphysicallinkresponsestatus)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothAMPDisconnectPhysicalLinkResponseStatus {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothAMPDisconnectPhysicalLinkResponseStatus : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothAMPDiscoverResponseControllerStatus [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothampdiscoverresponsecontrollerstatus)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothAMPDiscoverResponseControllerStatus {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothAMPDiscoverResponseControllerStatus : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothAMPGetAssocResponseStatus [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothampgetassocresponsestatus)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothAMPGetAssocResponseStatus {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothAMPGetAssocResponseStatus : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothAMPGetInfoResponseStatus [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothampgetinforesponsestatus)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothAMPGetInfoResponseStatus {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothAMPGetInfoResponseStatus : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothAMPManagerCode [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothampmanagercode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothAMPManagerCode {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothAMPManagerCode : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothAuthenticationRequirementsValues [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothauthenticationrequirementsvalues)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothAuthenticationRequirementsValues {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothAuthenticationRequirementsValues : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothCompanyIdentifers [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothcompanyidentifers)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothCompanyIdentifers {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothCompanyIdentifers : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothFeatureBits [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothfeaturebits)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothFeatureBits {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothFeatureBits : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIAFHChannelAssessmentModes [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhciafhchannelassessmentmodes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIAFHChannelAssessmentModes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIAFHChannelAssessmentModes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIAuthentionEnableModes [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhciauthentionenablemodes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIAuthentionEnableModes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIAuthentionEnableModes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIConnectionModes [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhciconnectionmodes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIConnectionModes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIConnectionModes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIDeleteStoredLinkKeyFlags [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhcideletestoredlinkkeyflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIDeleteStoredLinkKeyFlags {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIDeleteStoredLinkKeyFlags : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIEncryptionModes [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhciencryptionmodes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIEncryptionModes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIEncryptionModes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIExtendedInquiryResponseDataTypes [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhciextendedinquiryresponsedatatypes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIExtendedInquiryResponseDataTypes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIExtendedInquiryResponseDataTypes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIFECRequiredValues [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhcifecrequiredvalues)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIFECRequiredValues {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIFECRequiredValues : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIGeneralFlowControlStates [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhcigeneralflowcontrolstates)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIGeneralFlowControlStates {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIGeneralFlowControlStates : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIHoldModeActivityStates [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhciholdmodeactivitystates)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIHoldModeActivityStates {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIHoldModeActivityStates : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIInquiryModes [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhciinquirymodes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIInquiryModes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIInquiryModes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIInquiryScanTypes [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhciinquiryscantypes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIInquiryScanTypes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIInquiryScanTypes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCILinkPolicySettingsValues [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhcilinkpolicysettingsvalues)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCILinkPolicySettingsValues {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCILinkPolicySettingsValues : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIPageScanEnableStates [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhcipagescanenablestates)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIPageScanEnableStates {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIPageScanEnableStates : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIPageScanModes [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhcipagescanmodes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIPageScanModes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIPageScanModes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIPageScanPeriodModes [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhcipagescanperiodmodes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIPageScanPeriodModes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIPageScanPeriodModes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIPageScanTypes [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhcipagescantypes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIPageScanTypes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIPageScanTypes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIPowerState [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhcipowerstate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIPowerState {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIPowerState : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIReadStoredLinkKeysFlags [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhcireadstoredlinkkeysflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIReadStoredLinkKeysFlags {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIReadStoredLinkKeysFlags : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIRetransmissionEffortTypes [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhciretransmissionefforttypes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIRetransmissionEffortTypes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIRetransmissionEffortTypes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIRoles [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhciroles)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIRoles {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIRoles : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCISCOFlowControlStates [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhciscoflowcontrolstates)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCISCOFlowControlStates {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCISCOFlowControlStates : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCISimplePairingModes [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhcisimplepairingmodes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCISimplePairingModes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCISimplePairingModes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCITimeoutValues [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhcitimeoutvalues)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCITimeoutValues {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCITimeoutValues : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCITransmitReadPowerLevelTypes [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhcitransmitreadpowerleveltypes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCITransmitReadPowerLevelTypes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCITransmitReadPowerLevelTypes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothHCIVersions [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothhciversions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothHCIVersions {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothHCIVersions : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothIOCapabilities [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothiocapabilities)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothIOCapabilities {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothIOCapabilities : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothKeypressNotificationTypes [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothkeypressnotificationtypes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothKeypressNotificationTypes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothKeypressNotificationTypes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothL2CAPCommandCode [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capcommandcode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothL2CAPCommandCode {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothL2CAPCommandCode : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothL2CAPCommandRejectReason [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capcommandrejectreason)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothL2CAPCommandRejectReason {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothL2CAPCommandRejectReason : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothL2CAPConfigurationOption [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capconfigurationoption)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothL2CAPConfigurationOption {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothL2CAPConfigurationOption : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothL2CAPConfigurationResult [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capconfigurationresult)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothL2CAPConfigurationResult {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothL2CAPConfigurationResult : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothL2CAPConfigurationRetransmissionAndFlowControlFlags [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capconfigurationretransmissionandflowcontrolflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothL2CAPConfigurationRetransmissionAndFlowControlFlags {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothL2CAPConfigurationRetransmissionAndFlowControlFlags : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothL2CAPConnectionResult [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capconnectionresult)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothL2CAPConnectionResult {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothL2CAPConnectionResult : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothL2CAPConnectionStatus [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capconnectionstatus)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothL2CAPConnectionStatus {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothL2CAPConnectionStatus : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothL2CAPInformationExtendedFeaturesMask [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capinformationextendedfeaturesmask)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothL2CAPInformationExtendedFeaturesMask {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothL2CAPInformationExtendedFeaturesMask : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothL2CAPInformationResult [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capinformationresult)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothL2CAPInformationResult {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothL2CAPInformationResult : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothL2CAPInformationType [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capinformationtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothL2CAPInformationType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothL2CAPInformationType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothL2CAPQoSType [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capqostype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothL2CAPQoSType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothL2CAPQoSType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothLEAddressType [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothleaddresstype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothLEAddressType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothLEAddressType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothLEAdvertisingType [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothleadvertisingtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothLEAdvertisingType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothLEAdvertisingType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothLEConnectionInterval [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothleconnectioninterval)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothLEConnectionInterval {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothLEConnectionInterval : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothLEScan [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothlescan)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothLEScan {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothLEScan : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothLEScanDuplicateFilter [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothlescanduplicatefilter)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothLEScanDuplicateFilter {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothLEScanDuplicateFilter : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothLEScanFilter [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothlescanfilter)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothLEScanFilter {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothLEScanFilter : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothLEScanType [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothlescantype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothLEScanType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothLEScanType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothLESecurityManagerCommandCode [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagercommandcode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothLESecurityManagerCommandCode {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothLESecurityManagerCommandCode : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothLESecurityManagerIOCapability [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanageriocapability)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothLESecurityManagerIOCapability {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothLESecurityManagerIOCapability : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothLESecurityManagerKeyDistributionFormat [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerkeydistributionformat)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothLESecurityManagerKeyDistributionFormat {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothLESecurityManagerKeyDistributionFormat : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothLESecurityManagerOOBData [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanageroobdata)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothLESecurityManagerOOBData {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothLESecurityManagerOOBData : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothLESecurityManagerPairingFailedReasonCode [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerpairingfailedreasoncode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothLESecurityManagerPairingFailedReasonCode {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothLESecurityManagerPairingFailedReasonCode : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothLESecurityManagerUserInputCapability [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanageruserinputcapability)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothLESecurityManagerUserInputCapability {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothLESecurityManagerUserInputCapability : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothLESecurityManagerUserOutputCapability [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanageruseroutputcapability)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothLESecurityManagerUserOutputCapability {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothLESecurityManagerUserOutputCapability : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothLinkTypes [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothlinktypes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothLinkTypes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothLinkTypes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothLMPVersions [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothlmpversions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothLMPVersions {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothLMPVersions : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothOOBDataPresenceValues [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothoobdatapresencevalues)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothOOBDataPresenceValues {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothOOBDataPresenceValues : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothRFCOMMLineStatus [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothrfcommlinestatus)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothRFCOMMLineStatus {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothRFCOMMLineStatus : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothRFCOMMParityType [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothrfcommparitytype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothRFCOMMParityType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothRFCOMMParityType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothSimplePairingDebugModes [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothsimplepairingdebugmodes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothSimplePairingDebugModes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothSimplePairingDebugModes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BluetoothTransportTypes [struct]](https://developer.apple.com/documentation/iobluetooth/bluetoothtransporttypes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothTransportTypes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothTransportTypes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [FTSFileType [struct]](https://developer.apple.com/documentation/iobluetooth/ftsfiletype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct FTSFileType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct FTSFileType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [IOBluetoothDevice](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice)

|  | Declaration |
| --- | --- |
| From | ``` class IOBluetoothDevice : IOBluetoothObject, NSCoding, NSSecureCoding {     class func registerForConnectNotifications(_ observer: AnyObject!, selector inSelector: Selector) -> IOBluetoothUserNotification!     func registerForDisconnectNotification(_ observer: AnyObject!, selector inSelector: Selector) -> IOBluetoothUserNotification!     convenience init!(address address: UnsafePointer<BluetoothDeviceAddress>)     class func deviceWithAddress(_ address: UnsafePointer<BluetoothDeviceAddress>) -> Self!     class func withAddress(_ address: UnsafePointer<BluetoothDeviceAddress>) -> Self!     convenience init!(addressString address: String!)     class func deviceWithAddressString(_ address: String!) -> Self!     class func withDeviceRef(_ deviceRef: IOBluetoothDevice!) -> Self!     func getDeviceRef() -> Unmanaged<IOBluetoothDevice>!     func openL2CAPChannelSync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, delegate channelDelegate: AnyObject!) -> IOReturn     func openL2CAPChannelAsync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, delegate channelDelegate: AnyObject!) -> IOReturn     func openL2CAPChannel(_ psm: BluetoothL2CAPPSM, findExisting findExisting: Bool, newChannel newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>) -> IOReturn     func sendL2CAPEchoRequest(_ data: UnsafeMutablePointer<Void>, length length: UInt16) -> IOReturn     func openRFCOMMChannel(_ channelID: BluetoothRFCOMMChannelID, channel rfcommChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>) -> IOReturn     func openRFCOMMChannelSync(_ rfcommChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>, withChannelID channelID: BluetoothRFCOMMChannelID, delegate channelDelegate: AnyObject!) -> IOReturn     func openRFCOMMChannelAsync(_ rfcommChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>, withChannelID channelID: BluetoothRFCOMMChannelID, delegate channelDelegate: AnyObject!) -> IOReturn     var classOfDevice: BluetoothClassOfDevice { get }     func getClassOfDevice() -> BluetoothClassOfDevice     var serviceClassMajor: BluetoothServiceClassMajor { get }     func getServiceClassMajor() -> BluetoothServiceClassMajor     var deviceClassMajor: BluetoothDeviceClassMajor { get }     func getDeviceClassMajor() -> BluetoothDeviceClassMajor     var deviceClassMinor: BluetoothDeviceClassMinor { get }     func getDeviceClassMinor() -> BluetoothDeviceClassMinor     var name: String! { get }     func getName() -> String!     var nameOrAddress: String! { get }     func getNameOrAddress() -> String!     var lastNameUpdate: NSDate! { get }     func getLastNameUpdate() -> NSDate!     func getAddress() -> UnsafePointer<BluetoothDeviceAddress>     var addressString: String! { get }     func getAddressString() -> String!     func getPageScanRepetitionMode() -> BluetoothPageScanRepetitionMode     func getPageScanPeriodMode() -> BluetoothPageScanPeriodMode     func getPageScanMode() -> BluetoothPageScanMode     func getClockOffset() -> BluetoothClockOffset     func getLastInquiryUpdate() -> NSDate!     func RSSI() -> BluetoothHCIRSSIValue     func rawRSSI() -> BluetoothHCIRSSIValue     func isConnected() -> Bool     func openConnection() -> IOReturn     func openConnection(_ target: AnyObject!) -> IOReturn     func openConnection(_ target: AnyObject!, withPageTimeout pageTimeoutValue: BluetoothHCIPageTimeout, authenticationRequired authenticationRequired: Bool) -> IOReturn     func closeConnection() -> IOReturn     func remoteNameRequest(_ target: AnyObject!) -> IOReturn     func remoteNameRequest(_ target: AnyObject!, withPageTimeout pageTimeoutValue: BluetoothHCIPageTimeout) -> IOReturn     func requestAuthentication() -> IOReturn     var connectionHandle: BluetoothConnectionHandle { get }     func getConnectionHandle() -> BluetoothConnectionHandle     func isIncoming() -> Bool     func getLinkType() -> BluetoothLinkType     func getEncryptionMode() -> BluetoothHCIEncryptionMode     func performSDPQuery(_ target: AnyObject!) -> IOReturn     func performSDPQuery(_ target: AnyObject!, uuids uuidArray: [AnyObject]!) -> IOReturn     var services: [AnyObject]! { get }     func getServices() -> [AnyObject]!     func getLastServicesUpdate() -> NSDate!     func getServiceRecordForUUID(_ sdpUUID: IOBluetoothSDPUUID!) -> IOBluetoothSDPServiceRecord!     class func favoriteDevices() -> [AnyObject]!     func isFavorite() -> Bool     func addToFavorites() -> IOReturn     func removeFromFavorites() -> IOReturn     class func recentDevices(_ numDevices: UInt) -> [AnyObject]!     func recentAccessDate() -> NSDate!     class func pairedDevices() -> [AnyObject]!     func isPaired() -> Bool     func setSupervisionTimeout(_ timeout: UInt16) -> IOReturn     func openL2CAPChannelSync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, withConfiguration channelConfiguration: [NSObject : AnyObject]!, delegate channelDelegate: AnyObject!) -> IOReturn     func openL2CAPChannelAsync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, withConfiguration channelConfiguration: [NSObject : AnyObject]!, delegate channelDelegate: AnyObject!) -> IOReturn     func awakeAfterUsingCoder(_ coder: NSCoder!) -> AnyObject! } extension IOBluetoothDevice {     func handsFreeAudioGatewayDriverID() -> String!     func handsFreeAudioGatewayServiceRecord() -> IOBluetoothSDPServiceRecord!     func isHandsFreeAudioGateway() -> Bool     func handsFreeDeviceDriverID() -> String!     func handsFreeDeviceServiceRecord() -> IOBluetoothSDPServiceRecord!     func isHandsFreeDevice() -> Bool } ``` |
| To | ``` class IOBluetoothDevice : IOBluetoothObject, NSCoding, NSSecureCoding {     class func registerForConnectNotifications(_ observer: AnyObject!, selector inSelector: Selector) -> IOBluetoothUserNotification!     func registerForDisconnectNotification(_ observer: AnyObject!, selector inSelector: Selector) -> IOBluetoothUserNotification!     convenience init!(address address: UnsafePointer<BluetoothDeviceAddress>)     class func deviceWithAddress(_ address: UnsafePointer<BluetoothDeviceAddress>) -> Self!     class func withAddress(_ address: UnsafePointer<BluetoothDeviceAddress>) -> Self!     convenience init!(addressString address: String!)     class func deviceWithAddressString(_ address: String!) -> Self!     class func withDeviceRef(_ deviceRef: IOBluetoothDevice!) -> Self!     func getDeviceRef() -> Unmanaged<IOBluetoothDevice>!     func openL2CAPChannelSync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, delegate channelDelegate: AnyObject!) -> IOReturn     func openL2CAPChannelAsync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, delegate channelDelegate: AnyObject!) -> IOReturn     func openL2CAPChannel(_ psm: BluetoothL2CAPPSM, findExisting findExisting: Bool, newChannel newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>) -> IOReturn     func sendL2CAPEchoRequest(_ data: UnsafeMutablePointer<Void>, length length: UInt16) -> IOReturn     func openRFCOMMChannel(_ channelID: BluetoothRFCOMMChannelID, channel rfcommChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>) -> IOReturn     func openRFCOMMChannelSync(_ rfcommChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>, withChannelID channelID: BluetoothRFCOMMChannelID, delegate channelDelegate: AnyObject!) -> IOReturn     func openRFCOMMChannelAsync(_ rfcommChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>, withChannelID channelID: BluetoothRFCOMMChannelID, delegate channelDelegate: AnyObject!) -> IOReturn     var classOfDevice: BluetoothClassOfDevice { get }     func getClassOfDevice() -> BluetoothClassOfDevice     var serviceClassMajor: BluetoothServiceClassMajor { get }     func getServiceClassMajor() -> BluetoothServiceClassMajor     var deviceClassMajor: BluetoothDeviceClassMajor { get }     func getDeviceClassMajor() -> BluetoothDeviceClassMajor     var deviceClassMinor: BluetoothDeviceClassMinor { get }     func getDeviceClassMinor() -> BluetoothDeviceClassMinor     var name: String! { get }     func getName() -> String!     var nameOrAddress: String! { get }     func getNameOrAddress() -> String!     var lastNameUpdate: NSDate! { get }     func getLastNameUpdate() -> NSDate!     func getAddress() -> UnsafePointer<BluetoothDeviceAddress>     var addressString: String! { get }     func getAddressString() -> String!     func getPageScanRepetitionMode() -> BluetoothPageScanRepetitionMode     func getPageScanPeriodMode() -> BluetoothPageScanPeriodMode     func getPageScanMode() -> BluetoothPageScanMode     func getClockOffset() -> BluetoothClockOffset     func getLastInquiryUpdate() -> NSDate!     func RSSI() -> BluetoothHCIRSSIValue     func rawRSSI() -> BluetoothHCIRSSIValue     func isConnected() -> Bool     func openConnection() -> IOReturn     func openConnection(_ target: AnyObject!) -> IOReturn     func openConnection(_ target: AnyObject!, withPageTimeout pageTimeoutValue: BluetoothHCIPageTimeout, authenticationRequired authenticationRequired: Bool) -> IOReturn     func closeConnection() -> IOReturn     func remoteNameRequest(_ target: AnyObject!) -> IOReturn     func remoteNameRequest(_ target: AnyObject!, withPageTimeout pageTimeoutValue: BluetoothHCIPageTimeout) -> IOReturn     func requestAuthentication() -> IOReturn     var connectionHandle: BluetoothConnectionHandle { get }     func getConnectionHandle() -> BluetoothConnectionHandle     func isIncoming() -> Bool     func getLinkType() -> BluetoothLinkType     func getEncryptionMode() -> BluetoothHCIEncryptionMode     func performSDPQuery(_ target: AnyObject!) -> IOReturn     func performSDPQuery(_ target: AnyObject!, uuids uuidArray: [AnyObject]!) -> IOReturn     var services: [AnyObject]! { get }     func getServices() -> [AnyObject]!     func getLastServicesUpdate() -> NSDate!     func getServiceRecordForUUID(_ sdpUUID: IOBluetoothSDPUUID!) -> IOBluetoothSDPServiceRecord!     class func favoriteDevices() -> [AnyObject]!     func isFavorite() -> Bool     func addToFavorites() -> IOReturn     func removeFromFavorites() -> IOReturn     class func recentDevices(_ numDevices: UInt) -> [AnyObject]!     func recentAccessDate() -> NSDate!     class func pairedDevices() -> [AnyObject]!     func isPaired() -> Bool     func setSupervisionTimeout(_ timeout: UInt16) -> IOReturn     func openL2CAPChannelSync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, withConfiguration channelConfiguration: [NSObject : AnyObject]!, delegate channelDelegate: AnyObject!) -> IOReturn     func openL2CAPChannelAsync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, withConfiguration channelConfiguration: [NSObject : AnyObject]!, delegate channelDelegate: AnyObject!) -> IOReturn     func awakeAfterUsingCoder(_ coder: NSCoder!) -> AnyObject! } extension IOBluetoothDevice {     func handsFreeAudioGatewayDriverID() -> String!     func handsFreeAudioGatewayServiceRecord() -> IOBluetoothSDPServiceRecord!     var handsFreeAudioGateway: Bool { get }     func handsFreeDeviceDriverID() -> String!     func handsFreeDeviceServiceRecord() -> IOBluetoothSDPServiceRecord!     var handsFreeDevice: Bool { get } } ``` |

Modified [IOBluetoothDeviceSearchOptionsBits [struct]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicesearchoptionsbits)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct IOBluetoothDeviceSearchOptionsBits {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct IOBluetoothDeviceSearchOptionsBits : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [IOBluetoothDeviceSearchTypesBits [struct]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicesearchtypesbits)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct IOBluetoothDeviceSearchTypesBits {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct IOBluetoothDeviceSearchTypesBits : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [IOBluetoothL2CAPChannel](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel)

|  | Declaration |
| --- | --- |
| From | ``` class IOBluetoothL2CAPChannel : IOBluetoothObject, NSPortDelegate, NSObjectProtocol {     class func registerForChannelOpenNotifications(_ object: AnyObject!, selector selector: Selector) -> IOBluetoothUserNotification!     class func registerForChannelOpenNotifications(_ object: AnyObject!, selector selector: Selector, withPSM psm: BluetoothL2CAPPSM, direction inDirection: IOBluetoothUserNotificationChannelDirection) -> IOBluetoothUserNotification!     class func withObjectID(_ objectID: IOBluetoothObjectID) -> Self!     func closeChannel() -> IOReturn     var outgoingMTU: BluetoothL2CAPMTU { get }     func getOutgoingMTU() -> BluetoothL2CAPMTU     var incomingMTU: BluetoothL2CAPMTU { get }     func getIncomingMTU() -> BluetoothL2CAPMTU     func requestRemoteMTU(_ remoteMTU: BluetoothL2CAPMTU) -> IOReturn     func writeAsync(_ data: UnsafeMutablePointer<Void>, length length: UInt16, refcon refcon: UnsafeMutablePointer<Void>) -> IOReturn     func writeSync(_ data: UnsafeMutablePointer<Void>, length length: UInt16) -> IOReturn     func setDelegate(_ channelDelegate: AnyObject!) -> IOReturn     func setDelegate(_ channelDelegate: AnyObject!, withConfiguration channelConfiguration: [NSObject : AnyObject]!) -> IOReturn     func delegate() -> AnyObject!     var device: IOBluetoothDevice! { get }     func getDevice() -> IOBluetoothDevice!     var objectID: IOBluetoothObjectID { get }     func getObjectID() -> IOBluetoothObjectID     var PSM: BluetoothL2CAPPSM { get }     func getPSM() -> BluetoothL2CAPPSM     var localChannelID: BluetoothL2CAPChannelID { get }     func getLocalChannelID() -> BluetoothL2CAPChannelID     var remoteChannelID: BluetoothL2CAPChannelID { get }     func getRemoteChannelID() -> BluetoothL2CAPChannelID     func isIncoming() -> Bool     func registerForChannelCloseNotification(_ observer: AnyObject!, selector inSelector: Selector) -> IOBluetoothUserNotification! } ``` |
| To | ``` class IOBluetoothL2CAPChannel : IOBluetoothObject, NSPortDelegate {     class func registerForChannelOpenNotifications(_ object: AnyObject!, selector selector: Selector) -> IOBluetoothUserNotification!     class func registerForChannelOpenNotifications(_ object: AnyObject!, selector selector: Selector, withPSM psm: BluetoothL2CAPPSM, direction inDirection: IOBluetoothUserNotificationChannelDirection) -> IOBluetoothUserNotification!     class func withObjectID(_ objectID: IOBluetoothObjectID) -> Self!     func closeChannel() -> IOReturn     var outgoingMTU: BluetoothL2CAPMTU { get }     func getOutgoingMTU() -> BluetoothL2CAPMTU     var incomingMTU: BluetoothL2CAPMTU { get }     func getIncomingMTU() -> BluetoothL2CAPMTU     func requestRemoteMTU(_ remoteMTU: BluetoothL2CAPMTU) -> IOReturn     func writeAsync(_ data: UnsafeMutablePointer<Void>, length length: UInt16, refcon refcon: UnsafeMutablePointer<Void>) -> IOReturn     func writeSync(_ data: UnsafeMutablePointer<Void>, length length: UInt16) -> IOReturn     func setDelegate(_ channelDelegate: AnyObject!) -> IOReturn     func setDelegate(_ channelDelegate: AnyObject!, withConfiguration channelConfiguration: [NSObject : AnyObject]!) -> IOReturn     func delegate() -> AnyObject!     var device: IOBluetoothDevice! { get }     func getDevice() -> IOBluetoothDevice!     var objectID: IOBluetoothObjectID { get }     func getObjectID() -> IOBluetoothObjectID     var PSM: BluetoothL2CAPPSM { get }     func getPSM() -> BluetoothL2CAPPSM     var localChannelID: BluetoothL2CAPChannelID { get }     func getLocalChannelID() -> BluetoothL2CAPChannelID     var remoteChannelID: BluetoothL2CAPChannelID { get }     func getRemoteChannelID() -> BluetoothL2CAPChannelID     func isIncoming() -> Bool     func registerForChannelCloseNotification(_ observer: AnyObject!, selector inSelector: Selector) -> IOBluetoothUserNotification! } ``` |

Modified [IOBluetoothL2CAPChannelEventType [struct]](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchanneleventtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct IOBluetoothL2CAPChannelEventType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct IOBluetoothL2CAPChannelEventType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [IOBluetoothOBEXSession](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession)

|  | Declaration |
| --- | --- |
| From | ``` class IOBluetoothOBEXSession : OBEXSession, IOBluetoothRFCOMMChannelDelegate {     class func withSDPServiceRecord(_ inSDPServiceRecord: IOBluetoothSDPServiceRecord!) -> Self!     class func withDevice(_ inDevice: IOBluetoothDevice!, channelID inRFCOMMChannelID: BluetoothRFCOMMChannelID) -> Self!     class func withIncomingRFCOMMChannel(_ inChannel: IOBluetoothRFCOMMChannel!, eventSelector inEventSelector: Selector, selectorTarget inEventSelectorTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> Self!     init!(SDPServiceRecord inSDPServiceRecord: IOBluetoothSDPServiceRecord!)     init!(device inDevice: IOBluetoothDevice!, channelID inChannelID: BluetoothRFCOMMChannelID)     init!(incomingRFCOMMChannel inChannel: IOBluetoothRFCOMMChannel!, eventSelector inEventSelector: Selector, selectorTarget inEventSelectorTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>)     func getRFCOMMChannel() -> IOBluetoothRFCOMMChannel!     func getDevice() -> IOBluetoothDevice!     func sendBufferTroughChannel() -> IOReturn     func restartTransmission()     func isSessionTargetAMac() -> Bool     func openTransportConnection(_ inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func hasOpenTransportConnection() -> Bool     func closeTransportConnection() -> OBEXError     func sendDataToTransport(_ inDataToSend: UnsafeMutablePointer<Void>, dataLength inDataLength: Int) -> OBEXError     func setOpenTransportConnectionAsyncSelector(_ inSelector: Selector, target inSelectorTarget: AnyObject!, refCon inUserRefCon: AnyObject!)     func setOBEXSessionOpenConnectionCallback(_ inCallback: IOBluetoothOBEXSessionOpenConnectionCallback, refCon inUserRefCon: UnsafeMutablePointer<Void>) } ``` |
| To | ``` class IOBluetoothOBEXSession : OBEXSession, IOBluetoothRFCOMMChannelDelegate {     class func withSDPServiceRecord(_ inSDPServiceRecord: IOBluetoothSDPServiceRecord!) -> Self!     class func withDevice(_ inDevice: IOBluetoothDevice!, channelID inRFCOMMChannelID: BluetoothRFCOMMChannelID) -> Self!     class func withIncomingRFCOMMChannel(_ inChannel: IOBluetoothRFCOMMChannel!, eventSelector inEventSelector: Selector, selectorTarget inEventSelectorTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> Self!     init!(SDPServiceRecord inSDPServiceRecord: IOBluetoothSDPServiceRecord!)     init!(device inDevice: IOBluetoothDevice!, channelID inChannelID: BluetoothRFCOMMChannelID)     init!(incomingRFCOMMChannel inChannel: IOBluetoothRFCOMMChannel!, eventSelector inEventSelector: Selector, selectorTarget inEventSelectorTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>)     func getRFCOMMChannel() -> IOBluetoothRFCOMMChannel!     func getDevice() -> IOBluetoothDevice!     func sendBufferTroughChannel() -> IOReturn     func restartTransmission()     func isSessionTargetAMac() -> Bool     func openTransportConnection(_ inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func hasOpenTransportConnection() -> Bool     func closeTransportConnection() -> OBEXError     func sendDataToTransport(_ inDataToSend: UnsafeMutablePointer<Void>, dataLength inDataLength: Int) -> OBEXError     func setOpenTransportConnectionAsyncSelector(_ inSelector: Selector, target inSelectorTarget: AnyObject!, refCon inUserRefCon: AnyObject!)     func setOBEXSessionOpenConnectionCallback(_ inCallback: IOBluetoothOBEXSessionOpenConnectionCallback!, refCon inUserRefCon: UnsafeMutablePointer<Void>) } ``` |

Modified [IOBluetoothOBEXSession.setOBEXSessionOpenConnectionCallback(_: IOBluetoothOBEXSessionOpenConnectionCallback!, refCon: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/1431213-setobexsessionopenconnectioncall)

|  | Declaration |
| --- | --- |
| From | ``` func setOBEXSessionOpenConnectionCallback(_ inCallback: IOBluetoothOBEXSessionOpenConnectionCallback, refCon inUserRefCon: UnsafeMutablePointer<Void>) ``` |
| To | ``` func setOBEXSessionOpenConnectionCallback(_ inCallback: IOBluetoothOBEXSessionOpenConnectionCallback!, refCon inUserRefCon: UnsafeMutablePointer<Void>) ``` |

Modified [IOBluetoothRFCOMMChannel](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel)

|  | Declaration |
| --- | --- |
| From | ``` class IOBluetoothRFCOMMChannel : IOBluetoothObject, NSPortDelegate, NSObjectProtocol {     class func registerForChannelOpenNotifications(_ object: AnyObject!, selector selector: Selector) -> IOBluetoothUserNotification!     class func registerForChannelOpenNotifications(_ object: AnyObject!, selector selector: Selector, withChannelID channelID: BluetoothRFCOMMChannelID, direction inDirection: IOBluetoothUserNotificationChannelDirection) -> IOBluetoothUserNotification!     class func withRFCOMMChannelRef(_ rfcommChannelRef: IOBluetoothRFCOMMChannel!) -> Self!     class func withObjectID(_ objectID: IOBluetoothObjectID) -> Self!     func getRFCOMMChannelRef() -> Unmanaged<IOBluetoothRFCOMMChannel>!     func closeChannel() -> IOReturn     func isOpen() -> Bool     func getMTU() -> BluetoothRFCOMMMTU     func isTransmissionPaused() -> Bool     func write(_ data: UnsafeMutablePointer<Void>, length length: UInt16, sleep sleep: Bool) -> IOReturn     func writeAsync(_ data: UnsafeMutablePointer<Void>, length length: UInt16, refcon refcon: UnsafeMutablePointer<Void>) -> IOReturn     func writeSync(_ data: UnsafeMutablePointer<Void>, length length: UInt16) -> IOReturn     func writeSimple(_ data: UnsafeMutablePointer<Void>, length length: UInt16, sleep sleep: Bool, bytesSent numBytesSent: UnsafeMutablePointer<UInt32>) -> IOReturn     func setSerialParameters(_ speed: UInt32, dataBits nBits: UInt8, parity parity: BluetoothRFCOMMParityType, stopBits bitStop: UInt8) -> IOReturn     func sendRemoteLineStatus(_ lineStatus: BluetoothRFCOMMLineStatus) -> IOReturn     func setDelegate(_ delegate: AnyObject!) -> IOReturn     func delegate() -> AnyObject!     func getChannelID() -> BluetoothRFCOMMChannelID     func isIncoming() -> Bool     func getDevice() -> IOBluetoothDevice!     func getObjectID() -> IOBluetoothObjectID     func registerForChannelCloseNotification(_ observer: AnyObject!, selector inSelector: Selector) -> IOBluetoothUserNotification! } ``` |
| To | ``` class IOBluetoothRFCOMMChannel : IOBluetoothObject, NSPortDelegate {     class func registerForChannelOpenNotifications(_ object: AnyObject!, selector selector: Selector) -> IOBluetoothUserNotification!     class func registerForChannelOpenNotifications(_ object: AnyObject!, selector selector: Selector, withChannelID channelID: BluetoothRFCOMMChannelID, direction inDirection: IOBluetoothUserNotificationChannelDirection) -> IOBluetoothUserNotification!     class func withRFCOMMChannelRef(_ rfcommChannelRef: IOBluetoothRFCOMMChannel!) -> Self!     class func withObjectID(_ objectID: IOBluetoothObjectID) -> Self!     func getRFCOMMChannelRef() -> Unmanaged<IOBluetoothRFCOMMChannel>!     func closeChannel() -> IOReturn     func isOpen() -> Bool     func getMTU() -> BluetoothRFCOMMMTU     func isTransmissionPaused() -> Bool     func write(_ data: UnsafeMutablePointer<Void>, length length: UInt16, sleep sleep: Bool) -> IOReturn     func writeAsync(_ data: UnsafeMutablePointer<Void>, length length: UInt16, refcon refcon: UnsafeMutablePointer<Void>) -> IOReturn     func writeSync(_ data: UnsafeMutablePointer<Void>, length length: UInt16) -> IOReturn     func writeSimple(_ data: UnsafeMutablePointer<Void>, length length: UInt16, sleep sleep: Bool, bytesSent numBytesSent: UnsafeMutablePointer<UInt32>) -> IOReturn     func setSerialParameters(_ speed: UInt32, dataBits nBits: UInt8, parity parity: BluetoothRFCOMMParityType, stopBits bitStop: UInt8) -> IOReturn     func sendRemoteLineStatus(_ lineStatus: BluetoothRFCOMMLineStatus) -> IOReturn     func setDelegate(_ delegate: AnyObject!) -> IOReturn     func delegate() -> AnyObject!     func getChannelID() -> BluetoothRFCOMMChannelID     func isIncoming() -> Bool     func getDevice() -> IOBluetoothDevice!     func getObjectID() -> IOBluetoothObjectID     func registerForChannelCloseNotification(_ observer: AnyObject!, selector inSelector: Selector) -> IOBluetoothUserNotification! } ``` |

Modified [IOBluetoothUserNotificationChannelDirection [struct]](https://developer.apple.com/documentation/iobluetooth/iobluetoothusernotificationchanneldirection)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct IOBluetoothUserNotificationChannelDirection {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct IOBluetoothUserNotificationChannelDirection : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [OBEXConnectFlagValues [struct]](https://developer.apple.com/documentation/iobluetooth/obexconnectflagvalues)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OBEXConnectFlagValues {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct OBEXConnectFlagValues : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [OBEXErrorCodes [struct]](https://developer.apple.com/documentation/iobluetooth/obexerrorcodes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OBEXErrorCodes {     init(_ value: Int32)     var value: Int32 } ``` | -- |
| To | ``` struct OBEXErrorCodes : RawRepresentable {     init(_ rawValue: Int32)     init(rawValue rawValue: Int32)     var rawValue: Int32 } ``` | RawRepresentable |

Modified [OBEXHeaderIdentifiers [struct]](https://developer.apple.com/documentation/iobluetooth/obexheaderidentifiers)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OBEXHeaderIdentifiers {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct OBEXHeaderIdentifiers : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [OBEXNonceFlagValues [struct]](https://developer.apple.com/documentation/iobluetooth/obexnonceflagvalues)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OBEXNonceFlagValues {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct OBEXNonceFlagValues : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [OBEXOpCodeCommandValues [struct]](https://developer.apple.com/documentation/iobluetooth/obexopcodecommandvalues)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OBEXOpCodeCommandValues {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct OBEXOpCodeCommandValues : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [OBEXOpCodeResponseValues [struct]](https://developer.apple.com/documentation/iobluetooth/obexopcoderesponsevalues)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OBEXOpCodeResponseValues {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct OBEXOpCodeResponseValues : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [OBEXOpCodeSessionValues [struct]](https://developer.apple.com/documentation/iobluetooth/obexopcodesessionvalues)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OBEXOpCodeSessionValues {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct OBEXOpCodeSessionValues : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [OBEXPutFlagValues [struct]](https://developer.apple.com/documentation/iobluetooth/obexputflagvalues)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OBEXPutFlagValues {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct OBEXPutFlagValues : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [OBEXRealmValues [struct]](https://developer.apple.com/documentation/iobluetooth/obexrealmvalues)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OBEXRealmValues {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct OBEXRealmValues : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [OBEXSession](https://developer.apple.com/documentation/iobluetooth/obexsession)

|  | Declaration |
| --- | --- |
| From | ``` class OBEXSession : NSObject {     func OBEXConnect(_ inFlags: OBEXFlags, maxPacketLength inMaxPacketLength: OBEXMaxPacketLength, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXDisconnect(_ inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXPut(_ isFinalChunk: Boolean, headersData inHeadersData: UnsafeMutablePointer<Void>, headersDataLength inHeadersDataLength: Int, bodyData inBodyData: UnsafeMutablePointer<Void>, bodyDataLength inBodyDataLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXGet(_ isFinalChunk: Boolean, headers inHeaders: UnsafeMutablePointer<Void>, headersLength inHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXAbort(_ inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXSetPath(_ inFlags: OBEXFlags, constants inConstants: OBEXConstants, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXConnectResponse(_ inResponseOpCode: OBEXOpCode, flags inFlags: OBEXFlags, maxPacketLength inMaxPacketLength: OBEXMaxPacketLength, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXDisconnectResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXPutResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXGetResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXAbortResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXSetPathResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func getAvailableCommandPayloadLength(_ inOpCode: OBEXOpCode) -> OBEXMaxPacketLength     func getAvailableCommandResponsePayloadLength(_ inOpCode: OBEXOpCode) -> OBEXMaxPacketLength     func getMaxPacketLength() -> OBEXMaxPacketLength     func hasOpenOBEXConnection() -> Bool     func setEventCallback(_ inEventCallback: OBEXSessionEventCallback)     func setEventRefCon(_ inRefCon: UnsafeMutablePointer<Void>)     func setEventSelector(_ inEventSelector: Selector, target inEventSelectorTarget: AnyObject!, refCon inUserRefCon: AnyObject!)     func serverHandleIncomingData(_ event: UnsafeMutablePointer<OBEXTransportEvent>)     func clientHandleIncomingData(_ event: UnsafeMutablePointer<OBEXTransportEvent>)     func sendDataToTransport(_ inDataToSend: UnsafeMutablePointer<Void>, dataLength inDataLength: Int) -> OBEXError     func openTransportConnection(_ inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func hasOpenTransportConnection() -> Boolean     func closeTransportConnection() -> OBEXError } ``` |
| To | ``` class OBEXSession : NSObject {     func OBEXConnect(_ inFlags: OBEXFlags, maxPacketLength inMaxPacketLength: OBEXMaxPacketLength, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXDisconnect(_ inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXPut(_ isFinalChunk: Bool, headersData inHeadersData: UnsafeMutablePointer<Void>, headersDataLength inHeadersDataLength: Int, bodyData inBodyData: UnsafeMutablePointer<Void>, bodyDataLength inBodyDataLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXGet(_ isFinalChunk: Bool, headers inHeaders: UnsafeMutablePointer<Void>, headersLength inHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXAbort(_ inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXSetPath(_ inFlags: OBEXFlags, constants inConstants: OBEXConstants, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXConnectResponse(_ inResponseOpCode: OBEXOpCode, flags inFlags: OBEXFlags, maxPacketLength inMaxPacketLength: OBEXMaxPacketLength, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXDisconnectResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXPutResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXGetResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXAbortResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func OBEXSetPathResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafeMutablePointer<Void>, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func getAvailableCommandPayloadLength(_ inOpCode: OBEXOpCode) -> OBEXMaxPacketLength     func getAvailableCommandResponsePayloadLength(_ inOpCode: OBEXOpCode) -> OBEXMaxPacketLength     func getMaxPacketLength() -> OBEXMaxPacketLength     func hasOpenOBEXConnection() -> Bool     func setEventCallback(_ inEventCallback: OBEXSessionEventCallback!)     func setEventRefCon(_ inRefCon: UnsafeMutablePointer<Void>)     func setEventSelector(_ inEventSelector: Selector, target inEventSelectorTarget: AnyObject!, refCon inUserRefCon: AnyObject!)     func serverHandleIncomingData(_ event: UnsafeMutablePointer<OBEXTransportEvent>)     func clientHandleIncomingData(_ event: UnsafeMutablePointer<OBEXTransportEvent>)     func sendDataToTransport(_ inDataToSend: UnsafeMutablePointer<Void>, dataLength inDataLength: Int) -> OBEXError     func openTransportConnection(_ inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError     func hasOpenTransportConnection() -> Bool     func closeTransportConnection() -> OBEXError } ``` |

Modified [OBEXSession.hasOpenTransportConnection() -> Bool](https://developer.apple.com/documentation/iobluetooth/obexsession/1430785-hasopentransportconnection)

|  | Declaration |
| --- | --- |
| From | ``` func hasOpenTransportConnection() -> Boolean ``` |
| To | ``` func hasOpenTransportConnection() -> Bool ``` |

Modified [OBEXSession.OBEXGet(_: Bool, headers: UnsafeMutablePointer<Void>, headersLength: Int, eventSelector: Selector, selectorTarget: AnyObject!, refCon: UnsafeMutablePointer<Void>) -> OBEXError](https://developer.apple.com/documentation/iobluetooth/obexsession/1434710-obexget)

|  | Declaration |
| --- | --- |
| From | ``` func OBEXGet(_ isFinalChunk: Boolean, headers inHeaders: UnsafeMutablePointer<Void>, headersLength inHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError ``` |
| To | ``` func OBEXGet(_ isFinalChunk: Bool, headers inHeaders: UnsafeMutablePointer<Void>, headersLength inHeadersLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError ``` |

Modified [OBEXSession.OBEXPut(_: Bool, headersData: UnsafeMutablePointer<Void>, headersDataLength: Int, bodyData: UnsafeMutablePointer<Void>, bodyDataLength: Int, eventSelector: Selector, selectorTarget: AnyObject!, refCon: UnsafeMutablePointer<Void>) -> OBEXError](https://developer.apple.com/documentation/iobluetooth/obexsession/1431295-obexput)

|  | Declaration |
| --- | --- |
| From | ``` func OBEXPut(_ isFinalChunk: Boolean, headersData inHeadersData: UnsafeMutablePointer<Void>, headersDataLength inHeadersDataLength: Int, bodyData inBodyData: UnsafeMutablePointer<Void>, bodyDataLength inBodyDataLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError ``` |
| To | ``` func OBEXPut(_ isFinalChunk: Bool, headersData inHeadersData: UnsafeMutablePointer<Void>, headersDataLength inHeadersDataLength: Int, bodyData inBodyData: UnsafeMutablePointer<Void>, bodyDataLength inBodyDataLength: Int, eventSelector inSelector: Selector, selectorTarget inTarget: AnyObject!, refCon inUserRefCon: UnsafeMutablePointer<Void>) -> OBEXError ``` |

Modified [OBEXSession.setEventCallback(_: OBEXSessionEventCallback!)](https://developer.apple.com/documentation/iobluetooth/obexsession/1431039-seteventcallback)

|  | Declaration |
| --- | --- |
| From | ``` func setEventCallback(_ inEventCallback: OBEXSessionEventCallback) ``` |
| To | ``` func setEventCallback(_ inEventCallback: OBEXSessionEventCallback!) ``` |

Modified [OBEXSessionEvent [struct]](https://developer.apple.com/documentation/iobluetooth/obexsessionevent)

|  | Declaration |
| --- | --- |
| From | ``` struct OBEXSessionEvent {     var type: OBEXSessionEventType     var session: OBEXSessionRef     var refCon: UnsafeMutablePointer<Void>     var isEndOfEventData: Boolean     var reserved1: UnsafeMutablePointer<Void>     var reserved2: UnsafeMutablePointer<Void>     init() } ``` |
| To | ``` struct OBEXSessionEvent {     var type: OBEXSessionEventType     var session: OBEXSessionRef     var refCon: UnsafeMutablePointer<Void>     var isEndOfEventData: DarwinBoolean     var reserved1: UnsafeMutablePointer<Void>     var reserved2: UnsafeMutablePointer<Void>     init() } ``` |

Modified [OBEXSessionEvent.isEndOfEventData](https://developer.apple.com/documentation/iobluetooth/obexsessionevent/1432887-isendofeventdata)

|  | Declaration |
| --- | --- |
| From | ``` var isEndOfEventData: Boolean ``` |
| To | ``` var isEndOfEventData: DarwinBoolean ``` |

Modified [OBEXSessionEventTypes [struct]](https://developer.apple.com/documentation/iobluetooth/obexsessioneventtypes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OBEXSessionEventTypes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct OBEXSessionEventTypes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [OBEXSessionParameterTags [struct]](https://developer.apple.com/documentation/iobluetooth/obexsessionparametertags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OBEXSessionParameterTags {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct OBEXSessionParameterTags : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [OBEXTransportEventTypes [struct]](https://developer.apple.com/documentation/iobluetooth/obextransporteventtypes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OBEXTransportEventTypes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct OBEXTransportEventTypes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [OBEXVersions [struct]](https://developer.apple.com/documentation/iobluetooth/obexversions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OBEXVersions {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct OBEXVersions : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [ProtocolParameters [struct]](https://developer.apple.com/documentation/iobluetooth/protocolparameters)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ProtocolParameters {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct ProtocolParameters : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [SDPAttributeDeviceIdentificationRecord [struct]](https://developer.apple.com/documentation/iobluetooth/sdpattributedeviceidentificationrecord)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SDPAttributeDeviceIdentificationRecord {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct SDPAttributeDeviceIdentificationRecord : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [SDPAttributeIdentifierCodes [struct]](https://developer.apple.com/documentation/iobluetooth/sdpattributeidentifiercodes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SDPAttributeIdentifierCodes {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct SDPAttributeIdentifierCodes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [SDPServiceClasses [struct]](https://developer.apple.com/documentation/iobluetooth/sdpserviceclasses)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SDPServiceClasses {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct SDPServiceClasses : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [IOBluetoothDeviceRegisterForDisconnectNotification(_: IOBluetoothDevice!, _: IOBluetoothUserNotificationCallback!, _: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>!](https://developer.apple.com/documentation/iobluetooth/1431047-iobluetoothdeviceregisterfordisc)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothDeviceRegisterForDisconnectNotification(_ inDevice: IOBluetoothDevice!, _ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothDeviceRegisterForDisconnectNotification(_ inDevice: IOBluetoothDevice!, _ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |

Modified [IOBluetoothIsFileAppleDesignatedPIMData(_: String!) -> Bool](https://developer.apple.com/documentation/iobluetooth/1431744-iobluetoothisfileappledesignated)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothIsFileAppleDesignatedPIMData(_ inFileName: String!) -> Boolean ``` |
| To | ``` func IOBluetoothIsFileAppleDesignatedPIMData(_ inFileName: String!) -> Bool ``` |

Modified [IOBluetoothL2CAPChannelIncomingDataListener](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannelincomingdatalistener)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothL2CAPChannelIncomingDataListener = CFunctionPointer<((IOBluetoothL2CAPChannel!, UnsafeMutablePointer<Void>, UInt16, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias IOBluetoothL2CAPChannelIncomingDataListener = (IOBluetoothL2CAPChannel!, UnsafeMutablePointer<Void>, UInt16, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [IOBluetoothL2CAPChannelIncomingEventListener](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannelincomingeventlistener)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothL2CAPChannelIncomingEventListener = CFunctionPointer<((IOBluetoothL2CAPChannel!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<IOBluetoothL2CAPChannelEvent>) -> Void)> ``` |
| To | ``` typealias IOBluetoothL2CAPChannelIncomingEventListener = (IOBluetoothL2CAPChannel!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<IOBluetoothL2CAPChannelEvent>) -> Void ``` |

Modified [IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(_: IOBluetoothL2CAPChannel!, _: IOBluetoothUserNotificationCallback!, _: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>!](https://developer.apple.com/documentation/iobluetooth/1430069-iobluetoothl2capchannelregisterf)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(_ channel: IOBluetoothL2CAPChannel!, _ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(_ channel: IOBluetoothL2CAPChannel!, _ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |

Modified [IOBluetoothOBEXSessionOpenConnectionCallback](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsessionopenconnectioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothOBEXSessionOpenConnectionCallback = CFunctionPointer<((OBEXSessionRef, OBEXError, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias IOBluetoothOBEXSessionOpenConnectionCallback = (OBEXSessionRef, OBEXError, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [IOBluetoothRegisterForDeviceConnectNotifications(_: IOBluetoothUserNotificationCallback!, _: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>!](https://developer.apple.com/documentation/iobluetooth/1432361-iobluetoothregisterfordeviceconn)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRegisterForDeviceConnectNotifications(_ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothRegisterForDeviceConnectNotifications(_ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |

Modified [IOBluetoothRegisterForFilteredL2CAPChannelOpenNotifications(_: IOBluetoothUserNotificationCallback!, _: UnsafeMutablePointer<Void>, _: BluetoothL2CAPPSM, _: IOBluetoothUserNotificationChannelDirection) -> Unmanaged<IOBluetoothUserNotification>!](https://developer.apple.com/documentation/iobluetooth/1431179-iobluetoothregisterforfilteredl2)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRegisterForFilteredL2CAPChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafeMutablePointer<Void>, _ inPSM: BluetoothL2CAPPSM, _ inDirection: IOBluetoothUserNotificationChannelDirection) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothRegisterForFilteredL2CAPChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>, _ inPSM: BluetoothL2CAPPSM, _ inDirection: IOBluetoothUserNotificationChannelDirection) -> Unmanaged<IOBluetoothUserNotification>! ``` |

Modified [IOBluetoothRegisterForFilteredRFCOMMChannelOpenNotifications(_: IOBluetoothUserNotificationCallback!, _: UnsafeMutablePointer<Void>, _: BluetoothRFCOMMChannelID, _: IOBluetoothUserNotificationChannelDirection) -> Unmanaged<IOBluetoothUserNotification>!](https://developer.apple.com/documentation/iobluetooth/1428798-iobluetoothregisterforfilteredrf)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRegisterForFilteredRFCOMMChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafeMutablePointer<Void>, _ channelID: BluetoothRFCOMMChannelID, _ inDirection: IOBluetoothUserNotificationChannelDirection) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothRegisterForFilteredRFCOMMChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>, _ channelID: BluetoothRFCOMMChannelID, _ inDirection: IOBluetoothUserNotificationChannelDirection) -> Unmanaged<IOBluetoothUserNotification>! ``` |

Modified [IOBluetoothRegisterForL2CAPChannelOpenNotifications(_: IOBluetoothUserNotificationCallback!, _: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>!](https://developer.apple.com/documentation/iobluetooth/1434362-iobluetoothregisterforl2capchann)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRegisterForL2CAPChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothRegisterForL2CAPChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |

Modified [IOBluetoothRegisterForRFCOMMChannelOpenNotifications(_: IOBluetoothUserNotificationCallback!, _: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>!](https://developer.apple.com/documentation/iobluetooth/1430329-iobluetoothregisterforrfcommchan)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRegisterForRFCOMMChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothRegisterForRFCOMMChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |

Modified [IOBluetoothRFCOMMChannelRegisterForChannelCloseNotification(_: IOBluetoothRFCOMMChannel!, _: IOBluetoothUserNotificationCallback!, _: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>!](https://developer.apple.com/documentation/iobluetooth/1430321-iobluetoothrfcommchannelregister)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRFCOMMChannelRegisterForChannelCloseNotification(_ inChannel: IOBluetoothRFCOMMChannel!, _ callback: IOBluetoothUserNotificationCallback, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothRFCOMMChannelRegisterForChannelCloseNotification(_ inChannel: IOBluetoothRFCOMMChannel!, _ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |

Modified [IOBluetoothUserNotificationCallback](https://developer.apple.com/documentation/iobluetooth/iobluetoothusernotificationcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothUserNotificationCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, IOBluetoothUserNotification!, IOBluetoothObject!) -> Void)> ``` |
| To | ``` typealias IOBluetoothUserNotificationCallback = (UnsafeMutablePointer<Void>, IOBluetoothUserNotification!, IOBluetoothObject!) -> Void ``` |

Modified [OBEXAddBodyHeader(_: UnsafePointer<Void>, _: UInt32, _: Bool, _: CFMutableDictionary!) -> OBEXError](https://developer.apple.com/documentation/iobluetooth/1432916-obexaddbodyheader)

|  | Declaration |
| --- | --- |
| From | ``` func OBEXAddBodyHeader(_ inHeaderData: UnsafePointer<Void>, _ inHeaderDataLength: UInt32, _ isEndOfBody: Boolean, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |
| To | ``` func OBEXAddBodyHeader(_ inHeaderData: UnsafePointer<Void>, _ inHeaderDataLength: UInt32, _ isEndOfBody: Bool, _ dictRef: CFMutableDictionary!) -> OBEXError ``` |

Modified [OBEXSessionEventCallback](https://developer.apple.com/documentation/iobluetooth/obexsessioneventcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias OBEXSessionEventCallback = CFunctionPointer<((UnsafePointer<OBEXSessionEvent>) -> Void)> ``` |
| To | ``` typealias OBEXSessionEventCallback = (UnsafePointer<OBEXSessionEvent>) -> Void ``` |

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
