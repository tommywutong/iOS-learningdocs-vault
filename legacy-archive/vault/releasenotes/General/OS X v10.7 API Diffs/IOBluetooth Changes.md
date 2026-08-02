---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/IOBluetooth.html
archived_at: '2026-07-18T02:54:28.541784Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# IOBluetooth Changes

## IOBluetooth

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

Bluetooth.hRemoved kBluetoothFeatureAnonymityMode (no architecture available)Removed kBluetoothHCIAddHIDDevice (no architecture available)Removed kBluetoothHCICommandDeletePersistentSniffInterval (no architecture available)Removed kBluetoothHCICommandEnableHIDEmulation (no architecture available)Removed kBluetoothHCICommandEnableRadio (no architecture available)Removed kBluetoothHCICommandInvalidateFlashAndReboot (no architecture available)Removed kBluetoothHCICommandReadPersistentSniffInterval (no architecture available)Removed kBluetoothHCICommandSetMaxPower (no architecture available)Removed kBluetoothHCICommandWriteDeviceAddress (no architecture available)Removed kBluetoothHCICommandWriteHoppingChannels (no architecture available)Removed kBluetoothHCICommandWritePersistentSniffInterval (no architecture available)Removed #def kBluetoothHCIEventMaskSniffSubstrateEventRemoved kBluetoothHCIEventSniffRequest (no architecture available)Removed kBluetoothHCIEventSniffSubstrate (no architecture available)Removed kBluetoothHCIGetHIDDeviceList (no architecture available)Removed kBluetoothHCIRemoveHIDDevice (no architecture available)Added [BluetoothAFHHostChannelClassification](https://developer.apple.com/documentation/iobluetooth/bluetoothafhhostchannelclassification) (no architecture available)Added [BluetoothAirMode](https://developer.apple.com/documentation/kernel/bluetoothairmode) (no architecture available)Added #def BluetoothGetDeviceClassMajorAdded [BluetoothHCIAcceptSynchronousConnectionRequestParams](https://developer.apple.com/documentation/iobluetooth/bluetoothhciacceptsynchronousconnectionrequestparams) (no architecture available)Added [BluetoothHCIContentFormat](https://developer.apple.com/documentation/kernel/bluetoothhcicontentformat) (no architecture available)Added [BluetoothHCIErroneousDataReporting](https://developer.apple.com/documentation/kernel/bluetoothhcierroneousdatareporting) (no architecture available)Added [BluetoothHCIEventEncryptionKeyRefreshCompleteResults](https://developer.apple.com/documentation/iobluetooth/bluetoothhcieventencryptionkeyrefreshcompleteresults) (no architecture available)Added BluetoothHCIEventFlowSpecificationCompleteResults (no architecture available)Added [BluetoothHCIEventSniffSubratingResults](https://developer.apple.com/documentation/iobluetooth/bluetoothhcieventsniffsubratingresults) (no architecture available)Added [BluetoothHCIEventSynchronousConnectionChangedResults](https://developer.apple.com/documentation/kernel/bluetoothhcieventsynchronousconnectionchangedresults) (no architecture available)Added [BluetoothHCIEventSynchronousConnectionCompleteResults](https://developer.apple.com/documentation/iobluetooth/bluetoothhcieventsynchronousconnectioncompleteresults) (no architecture available)Added [BluetoothHCIInquiryScanType](https://developer.apple.com/documentation/kernel/bluetoothhciinquiryscantype) (no architecture available)Added BluetoothHCIInquiryScanTypes (no architecture available)Added [BluetoothHCIMaxLatency](https://developer.apple.com/documentation/kernel/bluetoothhcimaxlatency) (no architecture available)Added [BluetoothHCIPageScanType](https://developer.apple.com/documentation/kernel/bluetoothhcipagescantype) (no architecture available)Added BluetoothHCIPageScanTypes (no architecture available)Added [BluetoothHCIReadLMPHandleResults](https://developer.apple.com/documentation/kernel/bluetoothhcireadlmphandleresults) (no architecture available)Added [BluetoothHCIReceiveBandwidth](https://developer.apple.com/documentation/iobluetooth/bluetoothhcireceivebandwidth) (no architecture available)Added [BluetoothHCIRetransmissionEffort](https://developer.apple.com/documentation/kernel/bluetoothhciretransmissioneffort) (no architecture available)Added BluetoothHCIRetransmissionEffortTypes (no architecture available)Added [BluetoothHCISetupSynchronousConnectionParams](https://developer.apple.com/documentation/iobluetooth/bluetoothhcisetupsynchronousconnectionparams) (no architecture available)Added [BluetoothHCISupportedCommands](https://developer.apple.com/documentation/iobluetooth/bluetoothhcisupportedcommands) (no architecture available)Added [BluetoothHCITransmitBandwidth](https://developer.apple.com/documentation/iobluetooth/bluetoothhcitransmitbandwidth) (no architecture available)Added [BluetoothLMPHandle](https://developer.apple.com/documentation/iobluetooth/bluetoothlmphandle) (no architecture available)Added [BluetoothReadClockInfo](https://developer.apple.com/documentation/kernel/bluetoothreadclockinfo) (no architecture available)Added [BluetoothRemoteHostSupportedFeaturesNotification](https://developer.apple.com/documentation/kernel/bluetoothremotehostsupportedfeaturesnotification) (no architecture available)Added [BluetoothSynchronousConnectionInfo](https://developer.apple.com/documentation/kernel/bluetoothsynchronousconnectioninfo) (no architecture available)Added #def IOBLUETOOTH_EXPORTAdded [kBluetoothAirModeALawLog](https://developer.apple.com/documentation/kernel/1639975-anonymous/kbluetoothairmodealawlog) (no architecture available)Added [kBluetoothAirModeCVSD](https://developer.apple.com/documentation/iobluetooth/1489352-anonymous/kbluetoothairmodecvsd) (no architecture available)Added [kBluetoothAirModeTransparentData](https://developer.apple.com/documentation/iobluetooth/kbluetoothairmodetransparentdata) (no architecture available)Added [kBluetoothAirModeULawLog](https://developer.apple.com/documentation/iobluetooth/kbluetoothairmodeulawlog) (no architecture available)Added [kBluetoothFeatureLESupportedController](https://developer.apple.com/documentation/iobluetooth/kbluetoothfeaturelesupportedcontroller) (no architecture available)Added [kBluetoothHCICommandAMPTest](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandamptest) (no architecture available)Added [kBluetoothHCICommandAMPTestEnd](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandamptestend) (no architecture available)Added [kBluetoothHCICommandEnableAMPReceiverReports](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandenableampreceiverreports) (no architecture available)Added [kBluetoothHCICommandIOCapabilityRequestNegativeReply](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandiocapabilityrequestnegativereply) (no architecture available)Added [kBluetoothHCICommandReadBestEffortFlushTimeout](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandreadbesteffortflushtimeout) (no architecture available)Added [kBluetoothHCICommandReadEncryptionKeySize](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandreadencryptionkeysize) (no architecture available)Added [kBluetoothHCICommandReadEnhancedTransmitPowerLevel](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandreadenhancedtransmitpowerlevel) (no architecture available)Added [kBluetoothHCICommandReadFlowControlMode](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandreadflowcontrolmode) (no architecture available)Added [kBluetoothHCICommandReadLEHostSupported](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandreadlehostsupported) (no architecture available)Added [kBluetoothHCICommandReadLocalAMPASSOC](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandreadlocalampassoc) (no architecture available)Added [kBluetoothHCICommandReadLocalAMPInfo](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandreadlocalampinfo) (no architecture available)Added [kBluetoothHCICommandReadLocationData](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandreadlocationdata) (no architecture available)Added [kBluetoothHCICommandReadLogicalLinkAcceptTimeout](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandreadlogicallinkaccepttimeout) (no architecture available)Added [kBluetoothHCICommandRefreshEncryptionKey](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandrefreshencryptionkey) (no architecture available)Added [kBluetoothHCICommandSetEventMaskPageTwo](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandseteventmaskpagetwo) (no architecture available)Added [kBluetoothHCICommandShortRangeMode](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandshortrangemode) (no architecture available)Added [kBluetoothHCICommandWriteBestEffortFlushTimeout](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandwritebesteffortflushtimeout) (no architecture available)Added [kBluetoothHCICommandWriteFlowControlMode](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandwriteflowcontrolmode) (no architecture available)Added [kBluetoothHCICommandWriteLEHostSupported](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandwritelehostsupported) (no architecture available)Added [kBluetoothHCICommandWriteLocationData](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandwritelocationdata) (no architecture available)Added [kBluetoothHCICommandWriteLogicalLinkAcceptTimeout](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandwritelogicallinkaccepttimeout) (no architecture available)Added [kBluetoothHCICommandWriteRemoteAMPASSOC](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandwriteremoteampassoc) (no architecture available)Added [kBluetoothHCIErroneousDataReportingDisabled](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcierroneousdatareportingdisabled) (no architecture available)Added [kBluetoothHCIErroneousDataReportingEnabled](https://developer.apple.com/documentation/iobluetooth/1489133-anonymous/kbluetoothhcierroneousdatareportingenabled) (no architecture available)Added [kBluetoothHCIErroneousDataReportingReservedEnd](https://developer.apple.com/documentation/kernel/1640104-anonymous/kbluetoothhcierroneousdatareportingreservedend) (no architecture available)Added [kBluetoothHCIErroneousDataReportingReservedStart](https://developer.apple.com/documentation/iobluetooth/1489133-anonymous/kbluetoothhcierroneousdatareportingreservedstart) (no architecture available)Added [kBluetoothHCIErrorConnectionFailedToBeEstablished](https://developer.apple.com/documentation/iobluetooth/1490120-anonymous/kbluetoothhcierrorconnectionfailedtobeestablished) (no architecture available)Added [kBluetoothHCIErrorConnectionRejectedDueToNoSuitableChannelFound](https://developer.apple.com/documentation/kernel/1640161-anonymous/kbluetoothhcierrorconnectionrejectedduetonosuitablechannelfound) (no architecture available)Added [kBluetoothHCIErrorConnectionTerminatedDueToMICFailure](https://developer.apple.com/documentation/kernel/1640161-anonymous/kbluetoothhcierrorconnectionterminatedduetomicfailure) (no architecture available)Added [kBluetoothHCIErrorControllerBusy](https://developer.apple.com/documentation/kernel/1640161-anonymous/kbluetoothhcierrorcontrollerbusy) (no architecture available)Added [kBluetoothHCIErrorDirectedAdvertisingTimeout](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcierrordirectedadvertisingtimeout) (no architecture available)Added [kBluetoothHCIErrorHostBusyPairing](https://developer.apple.com/documentation/iobluetooth/1490120-anonymous/kbluetoothhcierrorhostbusypairing) (no architecture available)Added [kBluetoothHCIErrorMACConnectionFailed](https://developer.apple.com/documentation/iobluetooth/1490120-anonymous/kbluetoothhcierrormacconnectionfailed) (no architecture available)Added [kBluetoothHCIErrorUnacceptableConnectionInterval](https://developer.apple.com/documentation/kernel/1640161-anonymous/kbluetoothhcierrorunacceptableconnectioninterval) (no architecture available)Added [kBluetoothHCIEventAMPReceiverReport](https://developer.apple.com/documentation/kernel/1639977-anonymous/kbluetoothhcieventampreceiverreport) (no architecture available)Added [kBluetoothHCIEventAMPStartTest](https://developer.apple.com/documentation/kernel/1639977-anonymous/kbluetoothhcieventampstarttest) (no architecture available)Added [kBluetoothHCIEventAMPStatusChange](https://developer.apple.com/documentation/iobluetooth/1490041-anonymous/kbluetoothhcieventampstatuschange) (no architecture available)Added [kBluetoothHCIEventAMPTestEnd](https://developer.apple.com/documentation/iobluetooth/1490041-anonymous/kbluetoothhcieventamptestend) (no architecture available)Added [kBluetoothHCIEventChannelSelected](https://developer.apple.com/documentation/iobluetooth/1490041-anonymous/kbluetoothhcieventchannelselected) (no architecture available)Added [kBluetoothHCIEventDisconnectionLogicalLinkComplete](https://developer.apple.com/documentation/kernel/1639977-anonymous/kbluetoothhcieventdisconnectionlogicallinkcomplete) (no architecture available)Added [kBluetoothHCIEventDisconnectionPhysicalLinkComplete](https://developer.apple.com/documentation/kernel/1639977-anonymous/kbluetoothhcieventdisconnectionphysicallinkcomplete) (no architecture available)Added [kBluetoothHCIEventEncryptionKeyRefreshComplete](https://developer.apple.com/documentation/kernel/1639977-anonymous/kbluetoothhcieventencryptionkeyrefreshcomplete) (no architecture available)Added [kBluetoothHCIEventFlowSpecModifyComplete](https://developer.apple.com/documentation/kernel/1639977-anonymous/kbluetoothhcieventflowspecmodifycomplete) (no architecture available)Added [kBluetoothHCIEventLogicalLinkComplete](https://developer.apple.com/documentation/kernel/1639977-anonymous/kbluetoothhcieventlogicallinkcomplete) (no architecture available)Added [#def kBluetoothHCIEventMaskEncryptionChangeEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmaskencryptionchangeevent)Added [#def kBluetoothHCIEventMaskEncryptionKeyRefreshCompleteEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmaskencryptionkeyrefreshcompleteevent)Added [#def kBluetoothHCIEventMaskLEDefault64Bit](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmaskledefault64bit)Added [#def kBluetoothHCIEventMaskRemoteHostSupportedFeaturesNotificationEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmaskremotehostsupportedfeaturesnotificationevent)Added [#def kBluetoothHCIEventMaskSniffSubratingEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmasksniffsubratingevent)Added [kBluetoothHCIEventNumberOfCompletedDataBlocks](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventnumberofcompleteddatablocks) (no architecture available)Added [kBluetoothHCIEventPhysicalLinkComplete](https://developer.apple.com/documentation/kernel/1639977-anonymous/kbluetoothhcieventphysicallinkcomplete) (no architecture available)Added [kBluetoothHCIEventPhysicalLinkLossEarlyWarning](https://developer.apple.com/documentation/iobluetooth/1490041-anonymous/kbluetoothhcieventphysicallinklossearlywarning) (no architecture available)Added [kBluetoothHCIEventPhysicalLinkRecovery](https://developer.apple.com/documentation/iobluetooth/1490041-anonymous/kbluetoothhcieventphysicallinkrecovery) (no architecture available)Added [kBluetoothHCIEventRemoteHostSupportedFeaturesNotification](https://developer.apple.com/documentation/kernel/1639977-anonymous/kbluetoothhcieventremotehostsupportedfeaturesnotification) (no architecture available)Added [kBluetoothHCIEventShortRangeModeChangeComplete](https://developer.apple.com/documentation/kernel/1639977-anonymous/kbluetoothhcieventshortrangemodechangecomplete) (no architecture available)Added [kBluetoothHCIEventSniffSubrating](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventsniffsubrating) (no architecture available)Added [#def kBluetoothHCIEvnetMaskEnhancedFlushCompleteEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcievnetmaskenhancedflushcompleteevent)Added [#def kBluetoothHCIEvnetMaskLinkSupervisionTimeoutChangedEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcievnetmasklinksupervisiontimeoutchangedevent)Added [#def kBluetoothHCIInquiryResultsMaxResults](https://developer.apple.com/documentation/iobluetooth/kbluetoothhciinquiryresultsmaxresults)Added [kBluetoothHCIInquiryScanTypeInterlaced](https://developer.apple.com/documentation/kernel/bluetoothhciinquiryscantypes/kbluetoothhciinquiryscantypeinterlaced) (no architecture available)Added [kBluetoothHCIInquiryScanTypeReservedEnd](https://developer.apple.com/documentation/iobluetooth/bluetoothhciinquiryscantypes/kbluetoothhciinquiryscantypereservedend) (no architecture available)Added [kBluetoothHCIInquiryScanTypeReservedStart](https://developer.apple.com/documentation/kernel/bluetoothhciinquiryscantypes/kbluetoothhciinquiryscantypereservedstart) (no architecture available)Added [kBluetoothHCIInquiryScanTypeStandard](https://developer.apple.com/documentation/kernel/bluetoothhciinquiryscantypes/kbluetoothhciinquiryscantypestandard) (no architecture available)Added [kBluetoothHCIPageScanTypeInterlaced](https://developer.apple.com/documentation/kernel/bluetoothhcipagescantypes/kbluetoothhcipagescantypeinterlaced) (no architecture available)Added [kBluetoothHCIPageScanTypeReservedEnd](https://developer.apple.com/documentation/kernel/bluetoothhcipagescantypes/kbluetoothhcipagescantypereservedend) (no architecture available)Added [kBluetoothHCIPageScanTypeReservedStart](https://developer.apple.com/documentation/kernel/bluetoothhcipagescantypes/kbluetoothhcipagescantypereservedstart) (no architecture available)Added [kBluetoothHCIPageScanTypeStandard](https://developer.apple.com/documentation/kernel/bluetoothhcipagescantypes/kbluetoothhcipagescantypestandard) (no architecture available)Added [kBluetoothL2CAPChannelAttributeProtocol](https://developer.apple.com/documentation/iobluetooth/1489277-anonymous/kbluetoothl2capchannelattributeprotocol) (no architecture available)Added [kBluetoothL2CAPChannelLESignalling](https://developer.apple.com/documentation/kernel/1640028-anonymous/kbluetoothl2capchannellesignalling) (no architecture available)Added [kBluetoothL2CAPChannelSecurityManager](https://developer.apple.com/documentation/kernel/1640028-anonymous/kbluetoothl2capchannelsecuritymanager) (no architecture available)Added [kBluetoothPacketType2DH1Omit](https://developer.apple.com/documentation/iobluetooth/kbluetoothpackettype2dh1omit) (no architecture available)Added [kBluetoothPacketType2DH3Omit](https://developer.apple.com/documentation/iobluetooth/1489455-anonymous/kbluetoothpackettype2dh3omit) (no architecture available)Added [kBluetoothPacketType2DH5Omit](https://developer.apple.com/documentation/kernel/1640188-anonymous/kbluetoothpackettype2dh5omit) (no architecture available)Added [kBluetoothPacketType3DH1Omit](https://developer.apple.com/documentation/iobluetooth/1489455-anonymous/kbluetoothpackettype3dh1omit) (no architecture available)Added [kBluetoothPacketType3DH3Omit](https://developer.apple.com/documentation/kernel/1640188-anonymous/kbluetoothpackettype3dh3omit) (no architecture available)Added [kBluetoothPacketType3DM5Omit](https://developer.apple.com/documentation/iobluetooth/kbluetoothpackettype3dm5omit) (no architecture available)Added [kBluetoothPacketTypeReserved1](https://developer.apple.com/documentation/iobluetooth/1489455-anonymous/kbluetoothpackettypereserved1) (no architecture available)Added [kBluetoothSynchronousConnectionPacketType2EV3Omit](https://developer.apple.com/documentation/iobluetooth/1489721-anonymous/kbluetoothsynchronousconnectionpackettype2ev3omit) (no architecture available)Added [kBluetoothSynchronousConnectionPacketType2EV5Omit](https://developer.apple.com/documentation/iobluetooth/kbluetoothsynchronousconnectionpackettype2ev5omit) (no architecture available)Added [kBluetoothSynchronousConnectionPacketType3EV3Omit](https://developer.apple.com/documentation/kernel/1640210-anonymous/kbluetoothsynchronousconnectionpackettype3ev3omit) (no architecture available)Added [kBluetoothSynchronousConnectionPacketType3EV5Omit](https://developer.apple.com/documentation/iobluetooth/1489721-anonymous/kbluetoothsynchronousconnectionpackettype3ev5omit) (no architecture available)Added [kBluetoothSynchronousConnectionPacketTypeAll](https://developer.apple.com/documentation/kernel/1640210-anonymous/kbluetoothsynchronousconnectionpackettypeall) (no architecture available)Added [kBluetoothSynchronousConnectionPacketTypeEV3](https://developer.apple.com/documentation/kernel/1640210-anonymous/kbluetoothsynchronousconnectionpackettypeev3) (no architecture available)Added [kBluetoothSynchronousConnectionPacketTypeEV4](https://developer.apple.com/documentation/kernel/1640210-anonymous/kbluetoothsynchronousconnectionpackettypeev4) (no architecture available)Added [kBluetoothSynchronousConnectionPacketTypeEV5](https://developer.apple.com/documentation/iobluetooth/kbluetoothsynchronousconnectionpackettypeev5) (no architecture available)Added [kBluetoothSynchronousConnectionPacketTypeEnd](https://developer.apple.com/documentation/iobluetooth/1489721-anonymous/kbluetoothsynchronousconnectionpackettypeend) (no architecture available)Added [kBluetoothSynchronousConnectionPacketTypeFutureUse](https://developer.apple.com/documentation/iobluetooth/1489721-anonymous/kbluetoothsynchronousconnectionpackettypefutureuse) (no architecture available)Added [kBluetoothSynchronousConnectionPacketTypeHV1](https://developer.apple.com/documentation/kernel/1640210-anonymous/kbluetoothsynchronousconnectionpackettypehv1) (no architecture available)Added [kBluetoothSynchronousConnectionPacketTypeHV2](https://developer.apple.com/documentation/iobluetooth/1489721-anonymous/kbluetoothsynchronousconnectionpackettypehv2) (no architecture available)Added [kBluetoothSynchronousConnectionPacketTypeHV3](https://developer.apple.com/documentation/iobluetooth/kbluetoothsynchronousconnectionpackettypehv3) (no architecture available)Added [kBluetoothSynchronousConnectionPacketTypeNone](https://developer.apple.com/documentation/kernel/1640210-anonymous/kbluetoothsynchronousconnectionpackettypenone) (no architecture available)Added [kBluetoothVoiceSettingAirCodingFormatALaw](https://developer.apple.com/documentation/kernel/1640052-anonymous/kbluetoothvoicesettingaircodingformatalaw) (no architecture available)Added [kBluetoothVoiceSettingAirCodingFormatCVSD](https://developer.apple.com/documentation/iobluetooth/kbluetoothvoicesettingaircodingformatcvsd) (no architecture available)Added [kBluetoothVoiceSettingAirCodingFormatMask](https://developer.apple.com/documentation/kernel/1640052-anonymous/kbluetoothvoicesettingaircodingformatmask) (no architecture available)Added [kBluetoothVoiceSettingAirCodingFormatTransparentData](https://developer.apple.com/documentation/iobluetooth/kbluetoothvoicesettingaircodingformattransparentdata) (no architecture available)Added [kBluetoothVoiceSettingAirCodingFormatULaw](https://developer.apple.com/documentation/iobluetooth/1489230-anonymous/kbluetoothvoicesettingaircodingformatulaw) (no architecture available)Added [kBluetoothVoiceSettingInputCodingALawInputCoding](https://developer.apple.com/documentation/kernel/1640171-anonymous/kbluetoothvoicesettinginputcodingalawinputcoding) (no architecture available)Added [kBluetoothVoiceSettingInputCodingLinearInputCoding](https://developer.apple.com/documentation/kernel/1640171-anonymous/kbluetoothvoicesettinginputcodinglinearinputcoding) (no architecture available)Added [kBluetoothVoiceSettingInputCodingMask](https://developer.apple.com/documentation/iobluetooth/1489937-anonymous/kbluetoothvoicesettinginputcodingmask) (no architecture available)Added [kBluetoothVoiceSettingInputCodingULawInputCoding](https://developer.apple.com/documentation/iobluetooth/kbluetoothvoicesettinginputcodingulawinputcoding) (no architecture available)Added [kBluetoothVoiceSettingInputDataFormat1sComplement](https://developer.apple.com/documentation/iobluetooth/1489896-anonymous/kbluetoothvoicesettinginputdataformat1scomplement) (no architecture available)Added [kBluetoothVoiceSettingInputDataFormat2sComplement](https://developer.apple.com/documentation/kernel/1639916-anonymous/kbluetoothvoicesettinginputdataformat2scomplement) (no architecture available)Added [kBluetoothVoiceSettingInputDataFormatMask](https://developer.apple.com/documentation/kernel/1639916-anonymous/kbluetoothvoicesettinginputdataformatmask) (no architecture available)Added [kBluetoothVoiceSettingInputDataFormatSignMagnitude](https://developer.apple.com/documentation/kernel/1639916-anonymous/kbluetoothvoicesettinginputdataformatsignmagnitude) (no architecture available)Added [kBluetoothVoiceSettingInputDataFormatUnsigned](https://developer.apple.com/documentation/kernel/1639916-anonymous/kbluetoothvoicesettinginputdataformatunsigned) (no architecture available)Added [kBluetoothVoiceSettingInputSampleSize16Bit](https://developer.apple.com/documentation/kernel/1640005-anonymous/kbluetoothvoicesettinginputsamplesize16bit) (no architecture available)Added [kBluetoothVoiceSettingInputSampleSize8Bit](https://developer.apple.com/documentation/iobluetooth/1489541-anonymous/kbluetoothvoicesettinginputsamplesize8bit) (no architecture available)Added [kBluetoothVoiceSettingInputSampleSizeMask](https://developer.apple.com/documentation/kernel/1640005-anonymous/kbluetoothvoicesettinginputsamplesizemask) (no architecture available)Added [kBluetoothVoiceSettingPCMBitPositionMask](https://developer.apple.com/documentation/iobluetooth/kbluetoothvoicesettingpcmbitpositionmask) (no architecture available)Added [kHCIRetransmissionEffortTypeAtLeastOneAndOptimizeForPower](https://developer.apple.com/documentation/kernel/bluetoothhciretransmissionefforttypes/khciretransmissionefforttypeatleastoneandoptimizeforpower) (no architecture available)Added [kHCIRetransmissionEffortTypeAtLeastOneAndOptimizeLinkQuality](https://developer.apple.com/documentation/kernel/bluetoothhciretransmissionefforttypes/khciretransmissionefforttypeatleastoneandoptimizelinkquality) (no architecture available)Added [kHCIRetransmissionEffortTypeDontCare](https://developer.apple.com/documentation/kernel/bluetoothhciretransmissionefforttypes/khciretransmissionefforttypedontcare) (no architecture available)Added [kHCIRetransmissionEffortTypeNone](https://developer.apple.com/documentation/kernel/bluetoothhciretransmissionefforttypes/khciretransmissionefforttypenone) (no architecture available)BluetoothAssignedNumbers.hRemoved kBluetoothSDPUUID16ServiceClassHandsfreeRemoved kBluetoothSDPUUID16ServiceClassHandsfreeAudioGatewayAdded #def BluetoothCoDMinorPeripheral1Added #def BluetoothCoDMinorPeripheral2Added [BluetoothHCIVersions](https://developer.apple.com/documentation/kernel/bluetoothhciversions)Added [BluetoothLMPVersions](https://developer.apple.com/documentation/kernel/bluetoothlmpversions)Added [kBluetoothCompanyIdentifer3DiJoy](https://developer.apple.com/documentation/kernel/bluetoothcompanyidentifers/kbluetoothcompanyidentifer3dijoy)Added [kBluetoothCompanyIdentiferEMMicroElectronicMarin](https://developer.apple.com/documentation/iobluetooth/kbluetoothcompanyidentiferemmicroelectronicmarin)Added [kBluetoothCompanyIdentiferFree2Move](https://developer.apple.com/documentation/iobluetooth/kbluetoothcompanyidentiferfree2move)Added [kBluetoothCompanyIdentiferHarmonInternational](https://developer.apple.com/documentation/iobluetooth/kbluetoothcompanyidentiferharmoninternational)Added [kBluetoothCompanyIdentiferJandM](https://developer.apple.com/documentation/kernel/bluetoothcompanyidentifers/kbluetoothcompanyidentiferjandm)Added [kBluetoothCompanyIdentiferNordicSemiconductor](https://developer.apple.com/documentation/iobluetooth/kbluetoothcompanyidentifernordicsemiconductor)Added [kBluetoothCompanyIdentiferPlantronics](https://developer.apple.com/documentation/kernel/bluetoothcompanyidentifers/kbluetoothcompanyidentiferplantronics)Added [kBluetoothCompanyIdentiferSiRFTechnology](https://developer.apple.com/documentation/iobluetooth/bluetoothcompanyidentifers/kbluetoothcompanyidentifersirftechnology)Added [kBluetoothCompanyIdentiferSonyEricssonMobileCommunications](https://developer.apple.com/documentation/iobluetooth/bluetoothcompanyidentifers/kbluetoothcompanyidentifersonyericssonmobilecommunications)Added [kBluetoothCompanyIdentiferTZeroTechnologies](https://developer.apple.com/documentation/kernel/bluetoothcompanyidentifers/kbluetoothcompanyidentifertzerotechnologies)Added [kBluetoothCompanyIdentiferVisio](https://developer.apple.com/documentation/iobluetooth/kbluetoothcompanyidentifervisio)Added kBluetoothDeviceClassMajoHealthAdded kBluetoothDeviceClassMajoToyAdded [kBluetoothDeviceClassMajorWearable](https://developer.apple.com/documentation/kernel/1640534-anonymous/kbluetoothdeviceclassmajorwearable)Added [kBluetoothDeviceClassMinorHealthBloodPressureMonitor](https://developer.apple.com/documentation/iobluetooth/1459058-anonymous/kbluetoothdeviceclassminorhealthbloodpressuremonitor)Added [kBluetoothDeviceClassMinorHealthDataDisplay](https://developer.apple.com/documentation/kernel/1640543-anonymous/kbluetoothdeviceclassminorhealthdatadisplay)Added [kBluetoothDeviceClassMinorHealthGlucoseMeter](https://developer.apple.com/documentation/iobluetooth/kbluetoothdeviceclassminorhealthglucosemeter)Added [kBluetoothDeviceClassMinorHealthHeartRateMonitor](https://developer.apple.com/documentation/kernel/1640543-anonymous/kbluetoothdeviceclassminorhealthheartratemonitor)Added [kBluetoothDeviceClassMinorHealthPulseOximeter](https://developer.apple.com/documentation/iobluetooth/kbluetoothdeviceclassminorhealthpulseoximeter)Added [kBluetoothDeviceClassMinorHealthScale](https://developer.apple.com/documentation/kernel/1640543-anonymous/kbluetoothdeviceclassminorhealthscale)Added [kBluetoothDeviceClassMinorHealthThermometer](https://developer.apple.com/documentation/kernel/1640543-anonymous/kbluetoothdeviceclassminorhealththermometer)Added [kBluetoothDeviceClassMinorHealthUndefined](https://developer.apple.com/documentation/iobluetooth/kbluetoothdeviceclassminorhealthundefined)Added [kBluetoothDeviceClassMinorPeripheral2AnyPointing](https://developer.apple.com/documentation/kernel/1640543-anonymous/kbluetoothdeviceclassminorperipheral2anypointing)Added [kBluetoothDeviceClassMinorPeripheral2CardReader](https://developer.apple.com/documentation/kernel/1640543-anonymous/kbluetoothdeviceclassminorperipheral2cardreader)Added [kBluetoothDeviceClassMinorPeripheral2DigitizerTablet](https://developer.apple.com/documentation/iobluetooth/kbluetoothdeviceclassminorperipheral2digitizertablet)Added [kBluetoothDeviceClassMinorToyController](https://developer.apple.com/documentation/iobluetooth/1459058-anonymous/kbluetoothdeviceclassminortoycontroller)Added [kBluetoothDeviceClassMinorToyDollActionFigure](https://developer.apple.com/documentation/kernel/1640543-anonymous/kbluetoothdeviceclassminortoydollactionfigure)Added [kBluetoothDeviceClassMinorToyGame](https://developer.apple.com/documentation/kernel/1640543-anonymous/kbluetoothdeviceclassminortoygame)Added [kBluetoothDeviceClassMinorToyRobot](https://developer.apple.com/documentation/iobluetooth/kbluetoothdeviceclassminortoyrobot)Added [kBluetoothDeviceClassMinorToyVehicle](https://developer.apple.com/documentation/kernel/1640543-anonymous/kbluetoothdeviceclassminortoyvehicle)Added [kBluetoothDeviceClassMinorWearableGlasses](https://developer.apple.com/documentation/kernel/1640543-anonymous/kbluetoothdeviceclassminorwearableglasses)Added [kBluetoothDeviceClassMinorWearableHelmet](https://developer.apple.com/documentation/iobluetooth/1459058-anonymous/kbluetoothdeviceclassminorwearablehelmet)Added [kBluetoothDeviceClassMinorWearableJacket](https://developer.apple.com/documentation/kernel/1640543-anonymous/kbluetoothdeviceclassminorwearablejacket)Added [kBluetoothDeviceClassMinorWearablePager](https://developer.apple.com/documentation/kernel/1640543-anonymous/kbluetoothdeviceclassminorwearablepager)Added [kBluetoothDeviceClassMinorWearableWristWatch](https://developer.apple.com/documentation/iobluetooth/kbluetoothdeviceclassminorwearablewristwatch)Added [kBluetoothHCIExtendedInquiryResponseDataTypeDeviceID](https://developer.apple.com/documentation/iobluetooth/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypedeviceid)Added [kBluetoothHCIExtendedInquiryResponseDataTypeSSPOOBClassOfDevice](https://developer.apple.com/documentation/iobluetooth/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypesspoobclassofdevice)Added [kBluetoothHCIExtendedInquiryResponseDataTypeSSPOOBSimplePairingHashC](https://developer.apple.com/documentation/iobluetooth/kbluetoothhciextendedinquiryresponsedatatypesspoobsimplepairinghashc)Added [kBluetoothHCIExtendedInquiryResponseDataTypeSSPOOBSimplePairingRandomizerR](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypesspoobsimplepairingrandomizerr)Added [kBluetoothHCIExtendedInquiryResponseDataTypeSecurityManagerOOBFlags](https://developer.apple.com/documentation/iobluetooth/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypesecuritymanageroobflags)Added [kBluetoothHCIExtendedInquiryResponseDataTypeSecurityManagerTKValue](https://developer.apple.com/documentation/iobluetooth/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypesecuritymanagertkvalue)Added [kBluetoothHCIExtendedInquiryResponseDataTypeServiceData](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypeservicedata)Added [kBluetoothHCIExtendedInquiryResponseDataTypeServiceSolicitation128BitUUIDs](https://developer.apple.com/documentation/iobluetooth/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypeservicesolicitation128bituuids)Added [kBluetoothHCIExtendedInquiryResponseDataTypeServiceSolicitation16BitUUIDs](https://developer.apple.com/documentation/iobluetooth/kbluetoothhciextendedinquiryresponsedatatypeservicesolicitation16bituuids)Added [kBluetoothHCIExtendedInquiryResponseDataTypeSlaveConnectionIntervalRange](https://developer.apple.com/documentation/iobluetooth/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypeslaveconnectionintervalrange)Added [kBluetoothHCIExtendedInquiryResponseDataTypeTransmitPowerLevel](https://developer.apple.com/documentation/iobluetooth/kbluetoothhciextendedinquiryresponsedatatypetransmitpowerlevel)Added [kBluetoothHCIVersionCoreSpecification1_0b](https://developer.apple.com/documentation/kernel/bluetoothhciversions/kbluetoothhciversioncorespecification1_0b)Added [kBluetoothHCIVersionCoreSpecification1_1](https://developer.apple.com/documentation/iobluetooth/bluetoothhciversions/kbluetoothhciversioncorespecification1_1)Added [kBluetoothHCIVersionCoreSpecification1_2](https://developer.apple.com/documentation/kernel/bluetoothhciversions/kbluetoothhciversioncorespecification1_2)Added [kBluetoothHCIVersionCoreSpecification2_0EDR](https://developer.apple.com/documentation/kernel/bluetoothhciversions/kbluetoothhciversioncorespecification2_0edr)Added [kBluetoothHCIVersionCoreSpecification2_1EDR](https://developer.apple.com/documentation/kernel/bluetoothhciversions/kbluetoothhciversioncorespecification2_1edr)Added [kBluetoothHCIVersionCoreSpecification3_0HS](https://developer.apple.com/documentation/kernel/bluetoothhciversions/kbluetoothhciversioncorespecification3_0hs)Added [kBluetoothHCIVersionCoreSpecification4_0](https://developer.apple.com/documentation/iobluetooth/kbluetoothhciversioncorespecification4_0)Added [kBluetoothL2CAPPSMD2D](https://developer.apple.com/documentation/iobluetooth/1459299-anonymous/kbluetoothl2cappsmd2d)Added [kBluetoothLMPVersionCoreSpecification1_0b](https://developer.apple.com/documentation/kernel/bluetoothlmpversions/kbluetoothlmpversioncorespecification1_0b)Added [kBluetoothLMPVersionCoreSpecification1_1](https://developer.apple.com/documentation/iobluetooth/kbluetoothlmpversioncorespecification1_1)Added [kBluetoothLMPVersionCoreSpecification1_2](https://developer.apple.com/documentation/kernel/bluetoothlmpversions/kbluetoothlmpversioncorespecification1_2)Added [kBluetoothLMPVersionCoreSpecification2_0EDR](https://developer.apple.com/documentation/iobluetooth/kbluetoothlmpversioncorespecification2_0edr)Added [kBluetoothLMPVersionCoreSpecification2_1EDR](https://developer.apple.com/documentation/iobluetooth/kbluetoothlmpversioncorespecification2_1edr)Added [kBluetoothLMPVersionCoreSpecification3_0HS](https://developer.apple.com/documentation/iobluetooth/kbluetoothlmpversioncorespecification3_0hs)Added [kBluetoothLMPVersionCoreSpecification4_0](https://developer.apple.com/documentation/kernel/bluetoothlmpversions/kbluetoothlmpversioncorespecification4_0)Added [kBluetoothSDPUUID16ServiceClassHandsFree](https://developer.apple.com/documentation/iobluetooth/sdpserviceclasses/kbluetoothsdpuuid16serviceclasshandsfree)Added [kBluetoothSDPUUID16ServiceClassHandsFreeAudioGateway](https://developer.apple.com/documentation/iobluetooth/kbluetoothsdpuuid16serviceclasshandsfreeaudiogateway)IOBluetoothDevice.hRemoved -[IOBluetoothDevice description]Removed -[IOBluetoothDevice encodeWithCoder:]Removed -[IOBluetoothDevice initWithCoder:]Removed -[IOBluetoothDevice isEqual:]Added [-[IOBluetoothDevice RSSI]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1431127-rssi)Added [IOBluetoothDevice.addressString](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1431756-addressstring)Added [IOBluetoothDevice.classOfDevice](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1428484-classofdevice)Added [IOBluetoothDevice.connectionHandle](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1431263-connectionhandle)Added [IOBluetoothDevice.deviceClassMajor](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1435069-deviceclassmajor)Added [IOBluetoothDevice.deviceClassMinor](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1429321-deviceclassminor)Added [+[IOBluetoothDevice deviceWithAddress:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1434863-init)Added [+[IOBluetoothDevice deviceWithAddressString:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1434342-init)Added [IOBluetoothDevice.lastNameUpdate](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1430448-lastnameupdate)Added [-[IOBluetoothDevice performSDPQuery:uuids:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1431740-performsdpquery)Added [-[IOBluetoothDevice rawRSSI]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1434998-rawrssi)Added [IOBluetoothDevice.serviceClassMajor](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1429342-serviceclassmajor)Added [IOBluetoothDevice.services](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1432771-services)Modified [+[IOBluetoothDevice withAddress:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1589898-withaddress)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[IOBluetoothDevice getLastNameUpdate]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1589896-getlastnameupdate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[IOBluetoothDevice getDeviceClassMajor]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1589888-getdeviceclassmajor)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [IOBluetoothDevice](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCoding |

Modified [-[IOBluetoothDevice getServiceClassMajor]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1589897-getserviceclassmajor)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [+[IOBluetoothDevice withDeviceRef:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1589902-withdeviceref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[IOBluetoothDevice getServices]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1589900-getservices)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[IOBluetoothDevice getConnectionHandle]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1589895-getconnectionhandle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[IOBluetoothDevice getAddressString]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1589890-getaddressstring)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[IOBluetoothDevice getDeviceClassMinor]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1589894-getdeviceclassminor)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [IOBluetoothDevice.name](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1434669-name)

|  | Declaration |
| --- | --- |
| From | @property(readonly) NSString \*name |
| To | @property(readonly, copy) NSString \*name |

Modified [-[IOBluetoothDevice getClassOfDevice]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1589901-getclassofdevice)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[IOBluetoothDevice getDeviceRef]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1589892-getdeviceref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

IOBluetoothDeviceInquiry.hRemoved -[IOBluetoothDeviceInquiry delegate]Removed -[IOBluetoothDeviceInquiry setDelegate:]Removed -[NSObject deviceInquiryComplete:error:aborted:]Removed -[NSObject deviceInquiryDeviceFound:device:]Removed -[NSObject deviceInquiryDeviceNameUpdated:device:devicesRemaining:]Removed -[NSObject deviceInquiryStarted:]Removed -[NSObject deviceInquiryUpdatingDeviceNamesStarted:devicesRemaining:]Removed NSObject(IOBluetoothDeviceInquiryDelegate)Added [IOBluetoothDeviceInquiry.delegate](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquiry/1423403-delegate)Added [IOBluetoothDeviceInquiryDelegate](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate)Added [-[IOBluetoothDeviceInquiryDelegate deviceInquiryComplete:error:aborted:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate/1423409-deviceinquirycomplete)Added [-[IOBluetoothDeviceInquiryDelegate deviceInquiryDeviceFound:device:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate/1423415-deviceinquirydevicefound)Added [-[IOBluetoothDeviceInquiryDelegate deviceInquiryDeviceNameUpdated:device:devicesRemaining:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate/1423429-deviceinquirydevicenameupdated)Added [-[IOBluetoothDeviceInquiryDelegate deviceInquiryStarted:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate/1423405-deviceinquirystarted)Added [-[IOBluetoothDeviceInquiryDelegate deviceInquiryUpdatingDeviceNamesStarted:devicesRemaining:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate/1423425-deviceinquiryupdatingdevicenames)IOBluetoothDevicePair.hRemoved -[IOBluetoothDevicePair setDelegate:]Removed -[NSObject devicePairingConnecting:]Removed -[NSObject devicePairingFinished:error:]Removed -[NSObject devicePairingPINCodeRequest:]Removed -[NSObject devicePairingStarted:]Removed -[NSObject devicePairingUserConfirmationRequest:numericValue:]Removed -[NSObject devicePairingUserPasskeyNotification:passkey:]Removed NSObject(IOBluetoothDevicePairDelegate)Added [IOBluetoothDevicePair.delegate](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepair/1431438-delegate)Added [IOBluetoothDevicePairDelegate](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepairdelegate)Added [-[IOBluetoothDevicePairDelegate devicePairingConnecting:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepairdelegate/1432152-devicepairingconnecting)Added [-[IOBluetoothDevicePairDelegate devicePairingFinished:error:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepairdelegate/1434609-devicepairingfinished)Added [-[IOBluetoothDevicePairDelegate devicePairingPINCodeRequest:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepairdelegate/1432539-devicepairingpincoderequest)Added [-[IOBluetoothDevicePairDelegate devicePairingStarted:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepairdelegate/1431489-devicepairingstarted)Added [-[IOBluetoothDevicePairDelegate devicePairingUserConfirmationRequest:numericValue:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepairdelegate/1431902-devicepairinguserconfirmationreq)Added [-[IOBluetoothDevicePairDelegate devicePairingUserPasskeyNotification:passkey:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepairdelegate/1432500-devicepairinguserpasskeynotifica)IOBluetoothHandsFree.hAdded [-[IOBluetoothDevice handsFreeAudioGatewayDriverID]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1427922-handsfreeaudiogatewaydriverid)Added [-[IOBluetoothDevice handsFreeAudioGatewayServiceRecord]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1427826-handsfreeaudiogatewayservicereco)Added [-[IOBluetoothDevice handsFreeDeviceDriverID]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1427814-handsfreedevicedriverid)Added [-[IOBluetoothDevice handsFreeDeviceServiceRecord]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1427740-handsfreedeviceservicerecord)Added -[IOBluetoothDevice isHandsFreeAudioGateway]Added -[IOBluetoothDevice isHandsFreeDevice]Added [IOBluetoothHandsFree](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree)Added [IOBluetoothHandsFree.SMSEnabled](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427726-smsenabled)Added [IOBluetoothHandsFree.SMSMode](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427794-smsmode)Added [-[IOBluetoothHandsFree connect]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427829-connect)Added [-[IOBluetoothHandsFree connectSCO]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427914-connectsco)Added [IOBluetoothHandsFree.delegate](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427851-delegate)Added [IOBluetoothHandsFree.device](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427918-device)Added [IOBluetoothHandsFree.deviceCallHoldModes](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427864-devicecallholdmodes)Added [IOBluetoothHandsFree.deviceSupportedFeatures](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427893-devicesupportedfeatures)Added [IOBluetoothHandsFree.deviceSupportedSMSServices](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427843-devicesupportedsmsservices)Added [-[IOBluetoothHandsFree disconnect]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427804-disconnect)Added [-[IOBluetoothHandsFree disconnectSCO]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427766-disconnectsco)Added [-[IOBluetoothHandsFree indicator:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427897-indicator)Added [-[IOBluetoothHandsFree initWithDevice:delegate:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427916-initwithdevice)Added [IOBluetoothHandsFree.inputMuted](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427800-isinputmuted)Added [IOBluetoothHandsFree.inputVolume](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427816-inputvolume)Added [-[IOBluetoothHandsFree isConnected]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1811379-isconnected)Added [-[IOBluetoothHandsFree isSCOConnected]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427858-isscoconnected)Added [IOBluetoothHandsFree.outputMuted](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427756-outputmuted)Added [IOBluetoothHandsFree.outputVolume](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427874-outputvolume)Added [IOBluetoothHandsFree.scoAudioDevice](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1811492-scoaudiodevice)Added [-[IOBluetoothHandsFree setIndicator:value:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427872-setindicator)Added [IOBluetoothHandsFree.supportedFeatures](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427903-supportedfeatures)Added [IOBluetoothHandsFreeDelegate](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedelegate)Added [-[IOBluetoothHandsFreeDelegate handsFree:connected:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedelegate/1427880-handsfree)Added [-[IOBluetoothHandsFreeDelegate handsFree:disconnected:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedelegate/1427728-handsfree)Added [-[IOBluetoothHandsFreeDelegate handsFree:scoConnectionClosed:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedelegate/1427824-handsfree)Added [-[IOBluetoothHandsFreeDelegate handsFree:scoConnectionOpened:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedelegate/1427868-handsfree)Added [-[IOBluetoothSDPServiceRecord handsFreeSupportedFeatures]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/1427810-handsfreesupportedfeatures)Added IOBluetoothDevice(HandsFreeDeviceAdditions)Added [IOBluetoothHandsFreeAudioGatewayFeatureAttachedNumberToVoiceTag](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/attachednumbertovoicetag)Added [IOBluetoothHandsFreeAudioGatewayFeatureECAndOrNRFunction](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/iobluetoothhandsfreeaudiogatewayfeatureecandornrfunction)Added [IOBluetoothHandsFreeAudioGatewayFeatureEnhancedCallControl](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/iobluetoothhandsfreeaudiogatewayfeatureenhancedcallcontrol)Added [IOBluetoothHandsFreeAudioGatewayFeatureEnhancedCallStatus](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/enhancedcallstatus)Added [IOBluetoothHandsFreeAudioGatewayFeatureExtendedErrorResultCodes](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/iobluetoothhandsfreeaudiogatewayfeatureextendederrorresultcodes)Added [IOBluetoothHandsFreeAudioGatewayFeatureInBandRingTone](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/inbandringtone)Added [IOBluetoothHandsFreeAudioGatewayFeatureNone](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/none)Added [IOBluetoothHandsFreeAudioGatewayFeatureRejectCallCapability](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/iobluetoothhandsfreeaudiogatewayfeaturerejectcallcapability)Added [IOBluetoothHandsFreeAudioGatewayFeatureThreeWayCalling](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/iobluetoothhandsfreeaudiogatewayfeaturethreewaycalling)Added [IOBluetoothHandsFreeAudioGatewayFeatureVoiceRecognition](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/iobluetoothhandsfreeaudiogatewayfeaturevoicerecognition)Added [IOBluetoothHandsFreeAudioGatewayFeatures](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures)Added [IOBluetoothHandsFreeCallDirection](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecalldirection)Added [IOBluetoothHandsFreeCallHoldMode0](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallholdmodes/iobluetoothhandsfreecallholdmode0)Added [IOBluetoothHandsFreeCallHoldMode1](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallholdmodes/iobluetoothhandsfreecallholdmode1)Added [IOBluetoothHandsFreeCallHoldMode1idx](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallholdmodes/iobluetoothhandsfreecallholdmode1idx)Added [IOBluetoothHandsFreeCallHoldMode2](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallholdmodes/iobluetoothhandsfreecallholdmode2)Added [IOBluetoothHandsFreeCallHoldMode2idx](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallholdmodes/iobluetoothhandsfreecallholdmode2idx)Added [IOBluetoothHandsFreeCallHoldMode3](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallholdmodes/iobluetoothhandsfreecallholdmode3)Added [IOBluetoothHandsFreeCallHoldMode4](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallholdmodes/iobluetoothhandsfreecallholdmode4)Added [IOBluetoothHandsFreeCallHoldModes](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallholdmodes)Added [IOBluetoothHandsFreeCallIndex](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallindex)Added [IOBluetoothHandsFreeCallMode](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallmode)Added [IOBluetoothHandsFreeCallMultiparty](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallmultiparty)Added [IOBluetoothHandsFreeCallName](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallname)Added [IOBluetoothHandsFreeCallNumber](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallnumber)Added [IOBluetoothHandsFreeCallStatus](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallstatus)Added [IOBluetoothHandsFreeCallType](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecalltype)Added [IOBluetoothHandsFreeDeviceFeatureCLIPresentation](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures/clipresentation)Added [IOBluetoothHandsFreeDeviceFeatureECAndOrNRFunction](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures/iobluetoothhandsfreedevicefeatureecandornrfunction)Added [IOBluetoothHandsFreeDeviceFeatureEnhancedCallControl](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures/enhancedcallcontrol)Added [IOBluetoothHandsFreeDeviceFeatureEnhancedCallStatus](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures/enhancedcallstatus)Added [IOBluetoothHandsFreeDeviceFeatureNone](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures/iobluetoothhandsfreedevicefeaturenone)Added [IOBluetoothHandsFreeDeviceFeatureRemoteVolumeControl](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures/iobluetoothhandsfreedevicefeatureremotevolumecontrol)Added [IOBluetoothHandsFreeDeviceFeatureThreeWayCalling](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures/threewaycalling)Added [IOBluetoothHandsFreeDeviceFeatureVoiceRecognition](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures/iobluetoothhandsfreedevicefeaturevoicerecognition)Added [IOBluetoothHandsFreeDeviceFeatures](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures)Added [IOBluetoothHandsFreeIndicatorBattChg](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeindicatorbattchg)Added [IOBluetoothHandsFreeIndicatorCall](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeindicatorcall)Added [IOBluetoothHandsFreeIndicatorCallHeld](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeindicatorcallheld)Added [IOBluetoothHandsFreeIndicatorCallSetup](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeindicatorcallsetup)Added [IOBluetoothHandsFreeIndicatorRoam](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeindicatorroam)Added [IOBluetoothHandsFreeIndicatorService](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeindicatorservice)Added [IOBluetoothHandsFreeIndicatorSignal](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeindicatorsignal)Added [IOBluetoothHandsFreeManufactureSpecificSMSSupport](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreesmssupport/manufacturespecificsmssupport)Added [IOBluetoothHandsFreePDUMessageStatus](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreepdumessagestatus)Added [IOBluetoothHandsFreePDUStatusAll](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreepdumessagestatus/iobluetoothhandsfreepdustatusall)Added [IOBluetoothHandsFreePDUStatusRecRead](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreepdumessagestatus/iobluetoothhandsfreepdustatusrecread)Added [IOBluetoothHandsFreePDUStatusRecUnread](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreepdumessagestatus/iobluetoothhandsfreepdustatusrecunread)Added [IOBluetoothHandsFreePDUStatusStoSent](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreepdumessagestatus/iobluetoothhandsfreepdustatusstosent)Added [IOBluetoothHandsFreePDUStatusStoUnsent](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreepdumessagestatus/statusstounsent)Added [IOBluetoothHandsFreePhase2SMSSupport](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreesmssupport/iobluetoothhandsfreephase2smssupport)Added [IOBluetoothHandsFreePhase2pSMSSupport](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreesmssupport/phase2psmssupport)Added [IOBluetoothHandsFreeSMSSupport](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreesmssupport)Added [IOBluetoothPDUEncoding](https://developer.apple.com/documentation/iobluetooth/iobluetoothpduencoding)Added [IOBluetoothPDUOriginatingAddress](https://developer.apple.com/documentation/iobluetooth/iobluetoothpduoriginatingaddress)Added [IOBluetoothPDUOriginatingAddressType](https://developer.apple.com/documentation/iobluetooth/iobluetoothpduoriginatingaddresstype)Added [IOBluetoothPDUProtocolID](https://developer.apple.com/documentation/iobluetooth/iobluetoothpduprotocolid)Added [IOBluetoothPDUServicCenterAddress](https://developer.apple.com/documentation/iobluetooth/iobluetoothpduserviccenteraddress)Added [IOBluetoothPDUServiceCenterAddressType](https://developer.apple.com/documentation/iobluetooth/iobluetoothpduservicecenteraddresstype)Added [IOBluetoothPDUTimestamp](https://developer.apple.com/documentation/iobluetooth/iobluetoothpdutimestamp)Added [IOBluetoothPDUType](https://developer.apple.com/documentation/iobluetooth/iobluetoothpdutype)Added [IOBluetoothPDUUserData](https://developer.apple.com/documentation/iobluetooth/iobluetoothpduuserdata)Added IOBluetoothSDPServiceRecord(HandsFreeSDPServiceRecordAdditions)Added [IOBluetoothSMSMode](https://developer.apple.com/documentation/iobluetooth/iobluetoothsmsmode)Added [IOBluetoothSMSModePDU](https://developer.apple.com/documentation/iobluetooth/iobluetoothsmsmode/iobluetoothsmsmodepdu)Added [IOBluetoothSMSModeText](https://developer.apple.com/documentation/iobluetooth/iobluetoothsmsmode/text)IOBluetoothHandsFreeAudioGateway.hAdded [IOBluetoothHandsFreeAudioGateway](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogateway)Added [-[IOBluetoothHandsFreeAudioGateway createIndicator:min:max:currentValue:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogateway/1431383-createindicator)Added [-[IOBluetoothHandsFreeAudioGateway initWithDevice:delegate:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogateway/1428663-init)Added [-[IOBluetoothHandsFreeAudioGateway processATCommand:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogateway/1429231-process)Added [-[IOBluetoothHandsFreeAudioGateway sendOKResponse]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogateway/1429059-sendokresponse)Added [-[IOBluetoothHandsFreeAudioGateway sendResponse:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogateway/1434911-sendresponse)Added [-[IOBluetoothHandsFreeAudioGateway sendResponse:withOK:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogateway/1434547-sendresponse)Added [IOBluetoothHandsFreeAudioGatewayDelegate](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewaydelegate)Added [-[IOBluetoothHandsFreeAudioGatewayDelegate handsFree:hangup:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewaydelegate/1433943-handsfree)Added [-[IOBluetoothHandsFreeAudioGatewayDelegate handsFree:redial:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewaydelegate/1433563-handsfree)IOBluetoothHandsFreeDevice.hAdded [IOBluetoothHandsFreeDevice](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice)Added [-[IOBluetoothHandsFreeDevice acceptCall]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1430391-acceptcall)Added [-[IOBluetoothHandsFreeDevice acceptCallOnPhone]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1432773-acceptcallonphone)Added [-[IOBluetoothHandsFreeDevice addHeldCall]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1432732-addheldcall)Added [-[IOBluetoothHandsFreeDevice callTransfer]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1434534-calltransfer)Added [-[IOBluetoothHandsFreeDevice currentCallList]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1430837-currentcalllist)Added [-[IOBluetoothHandsFreeDevice dialNumber:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1430771-dialnumber)Added [-[IOBluetoothHandsFreeDevice endCall]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1430763-endcall)Added [-[IOBluetoothHandsFreeDevice holdCall]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1434936-holdcall)Added [-[IOBluetoothHandsFreeDevice initWithDevice:delegate:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1428834-initwithdevice)Added [-[IOBluetoothHandsFreeDevice memoryDial:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1429842-memorydial)Added [-[IOBluetoothHandsFreeDevice placeAllOthersOnHold:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1430932-placeallothersonhold)Added [-[IOBluetoothHandsFreeDevice redial]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1430476-redial)Added [-[IOBluetoothHandsFreeDevice releaseActiveCalls]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1432769-releaseactivecalls)Added [-[IOBluetoothHandsFreeDevice releaseCall:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1431536-releasecall)Added [-[IOBluetoothHandsFreeDevice releaseHeldCalls]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1433087-releaseheldcalls)Added [-[IOBluetoothHandsFreeDevice sendATCommand:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1429190-send)Added [-[IOBluetoothHandsFreeDevice sendATCommand:timeout:selector:target:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1430619-sendatcommand)Added [-[IOBluetoothHandsFreeDevice sendDTMF:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1428351-senddtmf)Added [-[IOBluetoothHandsFreeDevice sendSMS:message:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1429652-sendsms)Added [-[IOBluetoothHandsFreeDevice subscriberNumber]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1430919-subscribernumber)Added [-[IOBluetoothHandsFreeDevice transferAudioToComputer]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1429256-transferaudiotocomputer)Added [-[IOBluetoothHandsFreeDevice transferAudioToPhone]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1434079-transferaudiotophone)Added [IOBluetoothHandsFreeDeviceDelegate](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate)Added [-[IOBluetoothHandsFreeDeviceDelegate handsFree:batteryCharge:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1428496-handsfree)Added [-[IOBluetoothHandsFreeDeviceDelegate handsFree:callHoldState:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1433981-handsfree)Added [-[IOBluetoothHandsFreeDeviceDelegate handsFree:callSetupMode:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1429223-handsfree)Added [-[IOBluetoothHandsFreeDeviceDelegate handsFree:currentCall:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1432883-handsfree)Added [-[IOBluetoothHandsFreeDeviceDelegate handsFree:incomingSMS:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1430510-handsfree)Added [-[IOBluetoothHandsFreeDeviceDelegate handsFree:isCallActive:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1431339-handsfree)Added [-[IOBluetoothHandsFreeDeviceDelegate handsFree:isRoaming:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1431758-handsfree)Added [-[IOBluetoothHandsFreeDeviceDelegate handsFree:isServiceAvailable:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1433100-handsfree)Added [-[IOBluetoothHandsFreeDeviceDelegate handsFree:signalStrength:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1432799-handsfree)Added [-[IOBluetoothHandsFreeDeviceDelegate handsFree:subscriberNumber:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1430067-handsfree)Added [-[IOBluetoothHandsFreeDeviceDelegate handsFree:unhandledResultCode:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1433815-handsfree)IOBluetoothHandsFreeGateway.hModified -[IOBluetoothHandsFreeGateway getDeviceSupportedFeatures]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothHandsFreeGateway setGatewaySupportedFeatures:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified +[IOBluetoothHandsFreeGateway getRequiredSDPRFCOMMChannelIDForDevice:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothHandsFreeGateway initForConnectionToDevice:supportedFeatures:delegate:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothHandsFreeGateway initWithIncomingDevice:incomingRFCOMMChannelID:supportedFeatures:delegate:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified +[IOBluetoothHandsFreeGateway getRequiredSDPServiceRecordForDevice:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothHandsFreeGateway getGatewaySupportedFeatures]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

IOBluetoothHeadsetDevice.hAdded -[IOBluetoothDevice headsetAudioGatewayServiceRecord]Added -[IOBluetoothDevice headsetDeviceServiceRecord]Added -[IOBluetoothDevice isHeadsetAudioGateway]Added -[IOBluetoothDevice isHeadsetDevice]Added IOBluetoothDevice(HeadsetAdditions)Modified -[IOBluetoothHeadsetDevice initForConnectionToDevice:delegate:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified +[IOBluetoothHeadsetDevice getRequiredSDPRFCOMMChannelIDForDevice:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothHeadsetDevice initWithIncomingDevice:incomingRFCOMMChannelID:delegate:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified +[IOBluetoothHeadsetDevice getRequiredSDPServiceRecordForDevice:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

IOBluetoothHostController.hRemoved -[IOBluetoothHostController delegate]Removed -[IOBluetoothHostController setDelegate:]Added [IOBluetoothHostController.delegate](https://developer.apple.com/documentation/iobluetooth/iobluetoothhostcontroller/1434248-delegate)Added [-[IOBluetoothHostController nameAsString]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhostcontroller/1431310-nameasstring)Added [IOBluetoothHostController.powerState](https://developer.apple.com/documentation/iobluetooth/iobluetoothhostcontroller/1429740-powerstate)Modified [-[IOBluetoothHostController setClassOfDevice:forTimeInterval:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhostcontroller/1433813-setclassofdevice)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [-[IOBluetoothHostController classOfDevice]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhostcontroller/1428536-classofdevice)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified -[IOBluetoothHostController readRSSIForDevice:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified -[IOBluetoothHostController name]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified -[IOBluetoothHostController readLinkQualityForDevice:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified -[IOBluetoothHostController getSupportedFeatures:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified -[IOBluetoothHostController getAddress:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

IOBluetoothL2CAPChannel.hRemoved -[IOBluetoothL2CAPChannel description]Removed -[IOBluetoothL2CAPChannel getL2CAPChannelRef]Removed -[IOBluetoothL2CAPChannel registerIncomingDataListener:refCon:]Removed +[IOBluetoothL2CAPChannel withL2CAPChannelRef:]Removed -[IOBluetoothL2CAPChannel write:length:]Added [IOBluetoothL2CAPChannel.PSM](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/1432783-psm)Added [-[IOBluetoothL2CAPChannel delegate]](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/1431693-delegate)Added [IOBluetoothL2CAPChannel.device](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/1433430-device)Added [IOBluetoothL2CAPChannel.incomingMTU](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/1431269-incomingmtu)Added [IOBluetoothL2CAPChannel.localChannelID](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/1434996-localchannelid)Added [IOBluetoothL2CAPChannel.objectID](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/1428413-objectid)Added [IOBluetoothL2CAPChannel.outgoingMTU](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/1433700-outgoingmtu)Added [IOBluetoothL2CAPChannel.remoteChannelID](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/1434793-remotechannelid)Added [-[NSObject getL2CAPChannelRef]](https://developer.apple.com/documentation/objectivec/nsobject/1473892-getl2capchannelref)Added [-[NSObject registerIncomingDataListener:refCon:]](https://developer.apple.com/documentation/objectivec/nsobject/1473896-registerincomingdatalistener)Added [+[NSObject withL2CAPChannelRef:]](https://developer.apple.com/documentation/objectivec/nsobject/1473857-withl2capchannelref)Added [-[NSObject write:length:]](https://developer.apple.com/documentation/objectivec/nsobject/1473874-write)Added [IOBluetoothL2CAPChannelPublishedNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1429970-iobluetoothl2capchannelpublished)Added [IOBluetoothL2CAPChannelTerminatedNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1431835-iobluetoothl2capchannelterminate)Added NSObject(IOBluetoothL2CAPChannelDeprecated)Modified [-[IOBluetoothL2CAPChannel getPSM]](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/1473894-getpsm)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[IOBluetoothL2CAPChannel getObjectID]](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/1473902-getobjectid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[IOBluetoothL2CAPChannel getOutgoingMTU]](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/1473877-getoutgoingmtu)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[IOBluetoothL2CAPChannel getIncomingMTU]](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/1473864-getincomingmtu)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[IOBluetoothL2CAPChannel getRemoteChannelID]](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/1473912-getremotechannelid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[IOBluetoothL2CAPChannel getDevice]](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/1473859-getdevice)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[IOBluetoothL2CAPChannel getLocalChannelID]](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/1473918-getlocalchannelid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

IOBluetoothOBEXSession.hModified [IOBluetoothOBEXSession](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | IOBluetoothRFCOMMChannelDelegate |

IOBluetoothRFCOMMAudioController.hRemoved -[IOBluetoothRFCOMMAudioController dealloc]Removed -[IOBluetoothRFCOMMAudioController setDelegate:]Removed -[NSObject audioDevice:deviceConnectionClosed:]Removed -[NSObject audioDevice:deviceConnectionOpened:]Removed -[NSObject audioDevice:rfcommChannelClosed:]Removed -[NSObject audioDevice:rfcommChannelOpened:]Removed -[NSObject audioDevice:scoConnectionClosed:]Removed -[NSObject audioDevice:scoConnectionOpened:]Removed -[NSObject audioDevice:serviceLevelConnectionClosed:]Removed -[NSObject audioDevice:serviceLevelConnectionComplete:]Removed -[NSObject audioDevice:serviceLevelConnectionOpened:]Removed NSObject(IOBluetoothRFCOMMAudioDelegate)Added IOBluetoothRFCOMMAudioController.delegateAdded +[IOBluetoothRFCOMMAudioController getDriverIDForDevice:]Added IOBluetoothRFCOMMAudioDelegateAdded -[IOBluetoothRFCOMMAudioDelegate audioDevice:deviceConnectionClosed:]Added -[IOBluetoothRFCOMMAudioDelegate audioDevice:deviceConnectionOpened:]Added -[IOBluetoothRFCOMMAudioDelegate audioDevice:rfcommChannelClosed:]Added -[IOBluetoothRFCOMMAudioDelegate audioDevice:rfcommChannelOpened:]Added -[IOBluetoothRFCOMMAudioDelegate audioDevice:scoConnectionClosed:]Added -[IOBluetoothRFCOMMAudioDelegate audioDevice:scoConnectionOpened:]Added -[IOBluetoothRFCOMMAudioDelegate audioDevice:scoDone:]Added -[IOBluetoothRFCOMMAudioDelegate audioDevice:serviceLevelConnectionClosed:]Added -[IOBluetoothRFCOMMAudioDelegate audioDevice:serviceLevelConnectionOpened:]Added #def kIOBluetoothRFCOMMAudioControllerButtonPressedNotificationModified -[IOBluetoothRFCOMMAudioController closeSCOConnection]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController setRFCOMMChannel:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController isSCOConnected]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController handleIncomingRFCOMMChannelOpened:channel:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController getAudioDeviceID]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController sendRFCOMMData:length:]

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | - (IOReturn)sendRFCOMMData:(const void \*)data length:(UInt16)length |
| To | OS X v10.7 | - (IOReturn)sendRFCOMMData:(const void \*)data length:(uint16_t)length |

Modified -[IOBluetoothRFCOMMAudioController rfcommChannelData:data:length:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController closeDeviceConnection]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController initForConnectionToDevice:delegate:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController closeRFCOMMChannel]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController rfcommChannelClosed:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController getBluetoothDevice]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController openRFCOMMChannel]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController getIncomingRFCOMMChannelID]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController getOutgoingRFCOMMChannelID]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController openSCOConnection]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController rfcommChannelOpenComplete:status:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController openDeviceConnection]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController isDeviceConnected]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController initWithIncomingDevice:incomingRFCOMMChannelID:delegate:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[IOBluetoothRFCOMMAudioController isRFCOMMChannelOpen]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

IOBluetoothRFCOMMChannel.hAdded [-[IOBluetoothRFCOMMChannel delegate]](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel/1432238-delegate)IOBluetoothSDPDataElement.hRemoved -[IOBluetoothSDPDataElement encodeWithCoder:]Removed -[IOBluetoothSDPDataElement initWithCoder:]Removed -[IOBluetoothSDPDataElement isEqual:]Modified [+[IOBluetoothSDPDataElement withType:sizeDescriptor:size:value:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/1396706-withtype)

|  | Declaration |
| --- | --- |
| From | + (IOBluetoothSDPDataElement \*)withType:(BluetoothSDPDataElementTypeDescriptor)type sizeDescriptor:(BluetoothSDPDataElementSizeDescriptor)newSizeDescriptor size:(UInt32)newSize value:(NSObject \*)newValue |
| To | + (IOBluetoothSDPDataElement \*)withType:(BluetoothSDPDataElementTypeDescriptor)type sizeDescriptor:(BluetoothSDPDataElementSizeDescriptor)newSizeDescriptor size:(uint32_t)newSize value:(NSObject \*)newValue |

Modified [-[IOBluetoothSDPDataElement getSize]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/1396713-getsize)

|  | Declaration |
| --- | --- |
| From | - (UInt32)getSize |
| To | - (uint32_t)getSize |

Modified [-[IOBluetoothSDPDataElement initWithType:sizeDescriptor:size:value:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/1396719-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithType:(BluetoothSDPDataElementTypeDescriptor)newType sizeDescriptor:(BluetoothSDPDataElementSizeDescriptor)newSizeDescriptor size:(UInt32)newSize value:(NSObject \*)newValue |
| To | - (id)initWithType:(BluetoothSDPDataElementTypeDescriptor)newType sizeDescriptor:(BluetoothSDPDataElementSizeDescriptor)newSizeDescriptor size:(uint32_t)newSize value:(NSObject \*)newValue |

Modified [IOBluetoothSDPDataElement](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCoding |

IOBluetoothSDPServiceAttribute.hRemoved -[IOBluetoothSDPServiceAttribute encodeWithCoder:]Removed -[IOBluetoothSDPServiceAttribute initWithCoder:]Modified [IOBluetoothSDPServiceAttribute](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpserviceattribute)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCoding |

IOBluetoothSDPServiceRecord.hRemoved -[IOBluetoothSDPServiceRecord encodeWithCoder:]Removed -[IOBluetoothSDPServiceRecord initWithCoder:]Added [-[IOBluetoothSDPServiceRecord matchesUUID16:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/1429229-matchesuuid16)Added [IOBluetoothSDPServiceRecord.sortedAttributes](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/1434569-sortedattributes)Modified [IOBluetoothSDPServiceRecord](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCoding |

IOBluetoothSDPUUID.hRemoved -[IOBluetoothSDPUUID bytes]Removed -[IOBluetoothSDPUUID encodeWithCoder:]Removed -[IOBluetoothSDPUUID initWithBytes:length:]Removed -[IOBluetoothSDPUUID initWithCoder:]Removed -[IOBluetoothSDPUUID initWithData:]Removed -[IOBluetoothSDPUUID isEqualToData:]Removed -[IOBluetoothSDPUUID length]Modified [-[IOBluetoothSDPUUID getSDPUUIDRef]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid/1434312-getsdpuuidref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [+[IOBluetoothSDPUUID withSDPUUIDRef:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid/1434302-withsdpuuidref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

IOBluetoothUserLib.hRemoved IOBluetoothDeviceOpenL2CAPChannel() (no architecture available)Removed IOBluetoothDeviceOpenRFCOMMChannel() (no architecture available)Removed IOBluetoothL2CAPChannelWrite() (no architecture available)Removed IOBluetoothRFCOMMChannelRegisterIncomingDataListener() (no architecture available)Removed IOBluetoothRFCOMMChannelWrite() (no architecture available)Removed IOBluetoothRFCOMMChannelWriteSimple() (no architecture available)Added #def AVAILABLE_BLUETOOTH_VERSION_1_0_1_AND_LATERAdded #def BLUETOOTH_VERSION_2_5Added #def BLUETOOTH_VERSION_2_5_0Modified IOBluetoothSDPDataElementGetSize()

|  | Declaration |
| --- | --- |
| From | UInt32 IOBluetoothSDPDataElementGetSize ( IOBluetoothSDPDataElementRef dataElement); |
| To | uint32_t IOBluetoothSDPDataElementGetSize ( IOBluetoothSDPDataElementRef dataElement); |

IOBluetoothUtilities.hAdded IOBluetoothLaunchAudioAgent() (no architecture available)Added [IOBluetoothLaunchHandsFreeAgent()](https://developer.apple.com/documentation/iobluetooth/iobluetoothutilities.h/1811195-iobluetoothlaunchhandsfreeagent) (no architecture available)NSDictionaryOBEXExtensions.hModified [+[NSMutableDictionary withOBEXHeadersData:headersDataSize:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1458889-withobexheadersdata)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

OBEX.hAdded #def GET_HEADER_ID_IS_1_BYTE_QUANTITYAdded [kOBEXConflictError](https://developer.apple.com/documentation/iobluetooth/kobexconflicterror) (no architecture available)Added [kOBEXMethodNotAllowedError](https://developer.apple.com/documentation/iobluetooth/kobexmethodnotallowederror) (no architecture available)Added [kOBEXNotAcceptableError](https://developer.apple.com/documentation/iobluetooth/obexerrorcodes/kobexnotacceptableerror) (no architecture available)Added [kOBEXNotFoundError](https://developer.apple.com/documentation/iobluetooth/obexerrorcodes/kobexnotfounderror) (no architecture available)Added [kOBEXNotImplementedError](https://developer.apple.com/documentation/iobluetooth/kobexnotimplementederror) (no architecture available)Added [kOBEXPreconditionFailedError](https://developer.apple.com/documentation/iobluetooth/obexerrorcodes/kobexpreconditionfailederror) (no architecture available)Added [kOBEXUnauthorizedError](https://developer.apple.com/documentation/iobluetooth/obexerrorcodes/kobexunauthorizederror) (no architecture available)OBEXFileTransferServices.hRemoved -[OBEXFileTransferServices delegate] (no architecture available)Removed -[OBEXFileTransferServices setDelegate:] (no architecture available)Removed OBEXFileTransferServicesAbort() (no architecture available)Removed OBEXFileTransferServicesAbortComplete (no architecture available)Removed OBEXFileTransferServicesChangeCurrentFolderBackward() (no architecture available)Removed OBEXFileTransferServicesChangeCurrentFolderForward() (no architecture available)Removed OBEXFileTransferServicesChangeCurrentFolderToRoot() (no architecture available)Removed OBEXFileTransferServicesConnectToFTPService() (no architecture available)Removed OBEXFileTransferServicesConnectToObjectPushService() (no architecture available)Removed OBEXFileTransferServicesConnectionComplete (no architecture available)Removed OBEXFileTransferServicesCopyRemoteFile() (no architecture available)Removed OBEXFileTransferServicesCopyRemoteFileComplete (no architecture available)Removed OBEXFileTransferServicesCopyRemoteFileProgress (no architecture available)Removed OBEXFileTransferServicesCreateFolder() (no architecture available)Removed OBEXFileTransferServicesCreateFolderComplete (no architecture available)Removed OBEXFileTransferServicesCreateWithSession() (no architecture available)Removed OBEXFileTransferServicesCurrentPath() (no architecture available)Removed OBEXFileTransferServicesDelete() (no architecture available)Removed OBEXFileTransferServicesDisconnect() (no architecture available)Removed OBEXFileTransferServicesDisconnectionComplete (no architecture available)Removed OBEXFileTransferServicesFilePreparationComplete (no architecture available)Removed OBEXFileTransferServicesGetDefaultVCard() (no architecture available)Removed OBEXFileTransferServicesGetUserRefCon() (no architecture available)Removed OBEXFileTransferServicesIsBusy() (no architecture available)Removed OBEXFileTransferServicesIsConnected() (no architecture available)Removed OBEXFileTransferServicesPathChangeComplete (no architecture available)Removed OBEXFileTransferServicesRef (no architecture available)Removed OBEXFileTransferServicesRemoveItem() (no architecture available)Removed OBEXFileTransferServicesRemoveItemComplete (no architecture available)Removed OBEXFileTransferServicesRetrieveFolderListing() (no architecture available)Removed OBEXFileTransferServicesRetrieveFolderListingComplete (no architecture available)Removed OBEXFileTransferServicesSendData() (no architecture available)Removed OBEXFileTransferServicesSendFile() (no architecture available)Removed OBEXFileTransferServicesSendFileComplete (no architecture available)Removed OBEXFileTransferServicesSendFileProgress (no architecture available)Removed OBEXFileTransferServicesSetAbortCallback() (no architecture available)Removed OBEXFileTransferServicesSetConnectCallback() (no architecture available)Removed OBEXFileTransferServicesSetCopyRemoteFileCompleteCallback() (no architecture available)Removed OBEXFileTransferServicesSetCopyRemoteFileProgressCallback() (no architecture available)Removed OBEXFileTransferServicesSetCreateFolderCallback() (no architecture available)Removed OBEXFileTransferServicesSetDisconnectCallback() (no architecture available)Removed OBEXFileTransferServicesSetFilePreparationCompleteCallback() (no architecture available)Removed OBEXFileTransferServicesSetPathChangeCallback() (no architecture available)Removed OBEXFileTransferServicesSetRemoveItemCallback() (no architecture available)Removed OBEXFileTransferServicesSetRetrieveFolderListingCallback() (no architecture available)Removed OBEXFileTransferServicesSetSendFileCompleteCallback() (no architecture available)Removed OBEXFileTransferServicesSetSendFileProgressCallback() (no architecture available)Removed OBEXFileTransferServicesSetUserRefCon() (no architecture available)Added [OBEXFileTransferServices.delegate](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1430781-delegate)Modified [-[NSObject fileTransferServicesRemoveItemComplete:error:removedItem:]](https://developer.apple.com/documentation/objectivec/nsobject/1434702-filetransferservicesremoveitemco)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSObject fileTransferServicesSendFileComplete:error:]](https://developer.apple.com/documentation/objectivec/nsobject/1434240-filetransferservicessendfilecomp)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[OBEXFileTransferServices changeCurrentFolderForwardToPath:]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1429069-changecurrentfolderforward)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified NSObject(OBEXFileTransferServicesDelegate)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [+[OBEXFileTransferServices withOBEXSession:]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1435045-withobexsession)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[OBEXFileTransferServices retrieveFolderListing]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1433947-retrievefolderlisting)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [kFTSFileTypeFolder](https://developer.apple.com/documentation/iobluetooth/ftsfiletype/kftsfiletypefolder)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSObject fileTransferServicesRetrieveFolderListingComplete:error:listing:]](https://developer.apple.com/documentation/objectivec/nsobject/1434777-filetransferservicesretrievefold)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[OBEXFileTransferServices sendFile:]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1430911-sendfile)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[OBEXFileTransferServices sendData:type:name:]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1432819-send)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[OBEXFileTransferServices connectToFTPService]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1433641-connecttoftpservice)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[OBEXFileTransferServices changeCurrentFolderBackward]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1429850-changecurrentfolderbackward)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[OBEXFileTransferServices connectToObjectPushService]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1429786-connecttoobjectpushservice)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSObject fileTransferServicesAbortComplete:error:]](https://developer.apple.com/documentation/objectivec/nsobject/1430046-filetransferservicesabortcomplet)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSObject fileTransferServicesDisconnectionComplete:error:]](https://developer.apple.com/documentation/objectivec/nsobject/1434806-filetransferservicesdisconnectio)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified FTSFileType

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[OBEXFileTransferServices currentPath]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1434309-currentpath)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[OBEXFileTransferServices removeItem:]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1428401-removeitem)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[OBEXFileTransferServices isConnected]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1428521-isconnected)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSObject fileTransferServicesCopyRemoteFileComplete:error:]](https://developer.apple.com/documentation/objectivec/nsobject/1432094-filetransferservicescopyremotefi)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [kFTSFileTypeFile](https://developer.apple.com/documentation/iobluetooth/ftsfiletype/kftsfiletypefile)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSObject fileTransferServicesPathChangeComplete:error:finalPath:]](https://developer.apple.com/documentation/objectivec/nsobject/1432583-filetransferservicespathchangeco)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[OBEXFileTransferServices initWithOBEXSession:]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1431373-init)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[OBEXFileTransferServices changeCurrentFolderToRoot]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1428745-changecurrentfoldertoroot)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[OBEXFileTransferServices copyRemoteFile:toLocalPath:]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1434277-copyremotefile)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSObject fileTransferServicesFilePreparationComplete:error:]](https://developer.apple.com/documentation/objectivec/nsobject/1432086-filetransferservicesfilepreparat)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[OBEXFileTransferServices getDefaultVCard:]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1433891-getdefaultvcard)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[OBEXFileTransferServices disconnect]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1434667-disconnect)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[OBEXFileTransferServices abort]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1429764-abort)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSObject fileTransferServicesConnectionComplete:error:]](https://developer.apple.com/documentation/objectivec/nsobject/1428872-filetransferservicesconnectionco)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSObject fileTransferServicesSendFileProgress:transferProgress:]](https://developer.apple.com/documentation/objectivec/nsobject/1430365-filetransferservicessendfileprog)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSObject fileTransferServicesCopyRemoteFileProgress:transferProgress:]](https://developer.apple.com/documentation/objectivec/nsobject/1431422-filetransferservicescopyremotefi)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [OBEXFileTransferServices](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSObject fileTransferServicesCreateFolderComplete:error:folder:]](https://developer.apple.com/documentation/objectivec/nsobject/1430913-filetransferservicescreatefolder)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[OBEXFileTransferServices isBusy]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1434607-isbusy)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[OBEXFileTransferServices createFolder:]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1434906-createfolder)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

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
