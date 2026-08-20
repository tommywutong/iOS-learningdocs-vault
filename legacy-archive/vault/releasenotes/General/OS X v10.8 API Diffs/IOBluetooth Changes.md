---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/IOBluetooth.html
archived_at: '2026-07-18T02:54:01.628851Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# IOBluetooth Changes

## IOBluetooth

Bluetooth.hRemoved BluetoothHCIEventFlowSpecificationCompleteResults (no architecture available)Added [BluetoothEventFilterCondition](https://developer.apple.com/documentation/iobluetooth/bluetootheventfiltercondition) (no architecture available)Added #def BluetoothGetSecondsFromSlotsAdded [BluetoothHCIEventFlowSpecificationData](https://developer.apple.com/documentation/iobluetooth/bluetoothhcieventflowspecificationdata) (no architecture available)Added [BluetoothHCIEventLEConnectionCompleteResults](https://developer.apple.com/documentation/iobluetooth/bluetoothhcieventleconnectioncompleteresults) (no architecture available)Added [BluetoothHCIEventLELongTermKeyRequestResults](https://developer.apple.com/documentation/iobluetooth/bluetoothhcieventlelongtermkeyrequestresults) (no architecture available)Added [BluetoothHCIEventLEMetaResults](https://developer.apple.com/documentation/iobluetooth/bluetoothhcieventlemetaresults) (no architecture available)Added [BluetoothHCILEBufferSize](https://developer.apple.com/documentation/kernel/bluetoothhcilebuffersize) (no architecture available)Added [BluetoothLESecurityManagerCommandCode](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagercommandcode) (no architecture available)Added [BluetoothLESecurityManagerIOCapability](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanageriocapability) (no architecture available)Added BluetoothLESecurityManagerKeyDistributionFormat (no architecture available)Added [BluetoothLESecurityManagerOOBData](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanageroobdata) (no architecture available)Added [BluetoothLESecurityManagerPairingFailedReasonCode](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerpairingfailedreasoncode) (no architecture available)Added [BluetoothLESecurityManagerUserInputCapability](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanageruserinputcapability) (no architecture available)Added [BluetoothLESecurityManagerUserOutputCapability](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanageruseroutputcapability) (no architecture available)Added [kBluetoothHCICommandGroupLowEnergy](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandgrouplowenergy) (no architecture available)Added [kBluetoothHCICommandLEAddDeviceToWhiteList](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandleadddevicetowhitelist) (no architecture available)Added [kBluetoothHCICommandLEClearWhiteList](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandleclearwhitelist) (no architecture available)Added [kBluetoothHCICommandLEConnectionUpdate](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandleconnectionupdate) (no architecture available)Added [kBluetoothHCICommandLECreateConnection](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandlecreateconnection) (no architecture available)Added [kBluetoothHCICommandLECreateConnectionCancel](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlecreateconnectioncancel) (no architecture available)Added [kBluetoothHCICommandLEEncrypt](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandleencrypt) (no architecture available)Added [kBluetoothHCICommandLELongTermKeyRequestNegativeReply](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandlelongtermkeyrequestnegativereply) (no architecture available)Added [kBluetoothHCICommandLELongTermKeyRequestReply](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandlelongtermkeyrequestreply) (no architecture available)Added [kBluetoothHCICommandLERand](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandlerand) (no architecture available)Added [kBluetoothHCICommandLEReadAdvertisingChannelTxPower](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlereadadvertisingchanneltxpower) (no architecture available)Added [kBluetoothHCICommandLEReadBufferSize](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandlereadbuffersize) (no architecture available)Added [kBluetoothHCICommandLEReadChannelMap](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandlereadchannelmap) (no architecture available)Added [kBluetoothHCICommandLEReadLocalSupportedFeatures](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandlereadlocalsupportedfeatures) (no architecture available)Added [kBluetoothHCICommandLEReadRemoteUsedFeatures](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandlereadremoteusedfeatures) (no architecture available)Added [kBluetoothHCICommandLEReadSupportedStates](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandlereadsupportedstates) (no architecture available)Added [kBluetoothHCICommandLEReadWhiteListSize](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandlereadwhitelistsize) (no architecture available)Added [kBluetoothHCICommandLEReceiverTest](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandlereceivertest) (no architecture available)Added [kBluetoothHCICommandLERemoveDeviceFromWhiteList](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandleremovedevicefromwhitelist) (no architecture available)Added [kBluetoothHCICommandLESetAdvertiseEnable](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlesetadvertiseenable) (no architecture available)Added [kBluetoothHCICommandLESetAdvertisingData](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlesetadvertisingdata) (no architecture available)Added [kBluetoothHCICommandLESetAdvertisingParameters](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlesetadvertisingparameters) (no architecture available)Added [kBluetoothHCICommandLESetEventMask](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandleseteventmask) (no architecture available)Added [kBluetoothHCICommandLESetHostChannelClassification](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandlesethostchannelclassification) (no architecture available)Added [kBluetoothHCICommandLESetRandomAddress](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlesetrandomaddress) (no architecture available)Added [kBluetoothHCICommandLESetScanEnable](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandlesetscanenable) (no architecture available)Added [kBluetoothHCICommandLESetScanParameters](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandlesetscanparameters) (no architecture available)Added [kBluetoothHCICommandLESetScanResponseData](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandlesetscanresponsedata) (no architecture available)Added [kBluetoothHCICommandLEStartEncryption](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlestartencryption) (no architecture available)Added [kBluetoothHCICommandLETestEnd](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandletestend) (no architecture available)Added [kBluetoothHCICommandLETransmitterTest](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandletransmittertest) (no architecture available)Added [kBluetoothHCIEventLEMetaEvent](https://developer.apple.com/documentation/iobluetooth/1490041-anonymous/kbluetoothhcieventlemetaevent) (no architecture available)Added [#def kBluetoothHCIEventMaskLEMetaEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmasklemetaevent)Added [kBluetoothHCISubEventLEAdvertisingReport](https://developer.apple.com/documentation/kernel/1639977-anonymous/kbluetoothhcisubeventleadvertisingreport) (no architecture available)Added [kBluetoothHCISubEventLEConnectionComplete](https://developer.apple.com/documentation/kernel/1639977-anonymous/kbluetoothhcisubeventleconnectioncomplete) (no architecture available)Added [kBluetoothHCISubEventLEConnectionUpdateComplete](https://developer.apple.com/documentation/kernel/1639977-anonymous/kbluetoothhcisubeventleconnectionupdatecomplete) (no architecture available)Added [kBluetoothHCISubEventLELongTermKeyRequest](https://developer.apple.com/documentation/kernel/1639977-anonymous/kbluetoothhcisubeventlelongtermkeyrequest) (no architecture available)Added [kBluetoothHCISubEventLEReadRemoteUsedFeaturesComplete](https://developer.apple.com/documentation/iobluetooth/1490041-anonymous/kbluetoothhcisubeventlereadremoteusedfeaturescomplete) (no architecture available)Added [kBluetoothL2CAPCommandCodeConnectionParameterUpdateRequest](https://developer.apple.com/documentation/iobluetooth/kbluetoothl2capcommandcodeconnectionparameterupdaterequest) (no architecture available)Added [kBluetoothL2CAPCommandCodeConnectionParameterUpdateResponse](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capcommandcode/kbluetoothl2capcommandcodeconnectionparameterupdateresponse) (no architecture available)Added [kBluetoothL2CAPConfigurationEnhancedRetransmissionMode](https://developer.apple.com/documentation/kernel/bluetoothl2capconfigurationretransmissionandflowcontrolflags/kbluetoothl2capconfigurationenhancedretransmissionmode) (no architecture available)Added [kBluetoothL2CAPConfigurationOptionExtendedFlowSpecification](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capconfigurationoption/kbluetoothl2capconfigurationoptionextendedflowspecification) (no architecture available)Added [kBluetoothL2CAPConfigurationOptionExtendedWindowSize](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capconfigurationoption/kbluetoothl2capconfigurationoptionextendedwindowsize) (no architecture available)Added [kBluetoothL2CAPConfigurationOptionFrameCheckSequence](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capconfigurationoption/kbluetoothl2capconfigurationoptionframechecksequence) (no architecture available)Added [kBluetoothL2CAPConfigurationStreamingMode](https://developer.apple.com/documentation/kernel/bluetoothl2capconfigurationretransmissionandflowcontrolflags/kbluetoothl2capconfigurationstreamingmode) (no architecture available)Added [kBluetoothL2CAPMTULowEnergyDefault](https://developer.apple.com/documentation/iobluetooth/1489801-anonymous/kbluetoothl2capmtulowenergydefault) (no architecture available)Added [#def kBluetoothLESMPMaxEncryptionKeySize](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesmpmaxencryptionkeysize)Added [#def kBluetoothLESMPMinEncryptionKeySize](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesmpminencryptionkeysize)Added [#def kBluetoothLESMPTimeout](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesmptimeout)Added [kBluetoothLESecurityManagerBonding](https://developer.apple.com/documentation/iobluetooth/1489364-anonymous/kbluetoothlesecuritymanagerbonding) (no architecture available)Added [kBluetoothLESecurityManagerCommandCodeEncryptionInfo](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagercommandcode/kbluetoothlesecuritymanagercommandcodeencryptioninfo) (no architecture available)Added [kBluetoothLESecurityManagerCommandCodeIdentityAddressInfo](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagercommandcode/kbluetoothlesecuritymanagercommandcodeidentityaddressinfo) (no architecture available)Added [kBluetoothLESecurityManagerCommandCodeIdentityInfo](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagercommandcode/kbluetoothlesecuritymanagercommandcodeidentityinfo) (no architecture available)Added [kBluetoothLESecurityManagerCommandCodeMasterIdentification](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagercommandcode/kbluetoothlesecuritymanagercommandcodemasteridentification) (no architecture available)Added [kBluetoothLESecurityManagerCommandCodePairingConfirm](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagercommandcode/kbluetoothlesecuritymanagercommandcodepairingconfirm) (no architecture available)Added [kBluetoothLESecurityManagerCommandCodePairingFailed](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagercommandcode/kbluetoothlesecuritymanagercommandcodepairingfailed) (no architecture available)Added [kBluetoothLESecurityManagerCommandCodePairingRandom](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanagercommandcodepairingrandom) (no architecture available)Added [kBluetoothLESecurityManagerCommandCodePairingRequest](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagercommandcode/kbluetoothlesecuritymanagercommandcodepairingrequest) (no architecture available)Added [kBluetoothLESecurityManagerCommandCodePairingResponse](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagercommandcode/kbluetoothlesecuritymanagercommandcodepairingresponse) (no architecture available)Added [kBluetoothLESecurityManagerCommandCodeReserved](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagercommandcode/kbluetoothlesecuritymanagercommandcodereserved) (no architecture available)Added [kBluetoothLESecurityManagerCommandCodeReservedEnd](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanagercommandcodereservedend) (no architecture available)Added [kBluetoothLESecurityManagerCommandCodeReservedStart](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagercommandcode/kbluetoothlesecuritymanagercommandcodereservedstart) (no architecture available)Added [kBluetoothLESecurityManagerCommandCodeSecurityRequest](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagercommandcode/kbluetoothlesecuritymanagercommandcodesecurityrequest) (no architecture available)Added [kBluetoothLESecurityManagerCommandCodeSigningInfo](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagercommandcode/kbluetoothlesecuritymanagercommandcodesigninginfo) (no architecture available)Added [kBluetoothLESecurityManagerEncryptionKey](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerkeydistributionformat/kbluetoothlesecuritymanagerencryptionkey) (no architecture available)Added [kBluetoothLESecurityManagerIDKey](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanageridkey) (no architecture available)Added [kBluetoothLESecurityManagerIOCapabilityDisplayOnly](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanageriocapability/kbluetoothlesecuritymanageriocapabilitydisplayonly) (no architecture available)Added [kBluetoothLESecurityManagerIOCapabilityDisplayYesNo](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanageriocapability/kbluetoothlesecuritymanageriocapabilitydisplayyesno) (no architecture available)Added [kBluetoothLESecurityManagerIOCapabilityKeyboardDisplay](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanageriocapability/kbluetoothlesecuritymanageriocapabilitykeyboarddisplay) (no architecture available)Added [kBluetoothLESecurityManagerIOCapabilityKeyboardOnly](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanageriocapability/kbluetoothlesecuritymanageriocapabilitykeyboardonly) (no architecture available)Added [kBluetoothLESecurityManagerIOCapabilityNoInputNoOutput](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanageriocapability/kbluetoothlesecuritymanageriocapabilitynoinputnooutput) (no architecture available)Added [kBluetoothLESecurityManagerIOCapabilityReservedEnd](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanageriocapability/kbluetoothlesecuritymanageriocapabilityreservedend) (no architecture available)Added [kBluetoothLESecurityManagerIOCapabilityReservedStart](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanageriocapability/kbluetoothlesecuritymanageriocapabilityreservedstart) (no architecture available)Added [kBluetoothLESecurityManagerNoBonding](https://developer.apple.com/documentation/kernel/1639940-anonymous/kbluetoothlesecuritymanagernobonding) (no architecture available)Added [kBluetoothLESecurityManagerOOBAuthenticationDataNotPresent](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanageroobdata/kbluetoothlesecuritymanageroobauthenticationdatanotpresent) (no architecture available)Added [kBluetoothLESecurityManagerOOBAuthenticationDataPresent](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanageroobdata/kbluetoothlesecuritymanageroobauthenticationdatapresent) (no architecture available)Added [kBluetoothLESecurityManagerOOBDataReservedEnd](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanageroobdatareservedend) (no architecture available)Added [kBluetoothLESecurityManagerOOBDataReservedStart](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanageroobdata/kbluetoothlesecuritymanageroobdatareservedstart) (no architecture available)Added [kBluetoothLESecurityManagerReasonCodeAuthenticationRequirements](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerpairingfailedreasoncode/kbluetoothlesecuritymanagerreasoncodeauthenticationrequirements) (no architecture available)Added [kBluetoothLESecurityManagerReasonCodeCommandNotSupported](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerpairingfailedreasoncode/kbluetoothlesecuritymanagerreasoncodecommandnotsupported) (no architecture available)Added [kBluetoothLESecurityManagerReasonCodeConfirmValueFailed](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerpairingfailedreasoncode/kbluetoothlesecuritymanagerreasoncodeconfirmvaluefailed) (no architecture available)Added [kBluetoothLESecurityManagerReasonCodeEncryptionKeySize](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerpairingfailedreasoncode/kbluetoothlesecuritymanagerreasoncodeencryptionkeysize) (no architecture available)Added [kBluetoothLESecurityManagerReasonCodeInvalidParameters](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerpairingfailedreasoncode/kbluetoothlesecuritymanagerreasoncodeinvalidparameters) (no architecture available)Added [kBluetoothLESecurityManagerReasonCodeOOBNotAvailbale](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerpairingfailedreasoncode/kbluetoothlesecuritymanagerreasoncodeoobnotavailbale) (no architecture available)Added [kBluetoothLESecurityManagerReasonCodePairingNotSupported](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerpairingfailedreasoncode/kbluetoothlesecuritymanagerreasoncodepairingnotsupported) (no architecture available)Added [kBluetoothLESecurityManagerReasonCodePasskeyEntryFailed](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerpairingfailedreasoncode/kbluetoothlesecuritymanagerreasoncodepasskeyentryfailed) (no architecture available)Added [kBluetoothLESecurityManagerReasonCodeRepeatedAttempts](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerpairingfailedreasoncode/kbluetoothlesecuritymanagerreasoncoderepeatedattempts) (no architecture available)Added [kBluetoothLESecurityManagerReasonCodeReserved](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanagerreasoncodereserved) (no architecture available)Added [kBluetoothLESecurityManagerReasonCodeReservedEnd](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanagerreasoncodereservedend) (no architecture available)Added [kBluetoothLESecurityManagerReasonCodeReservedStart](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanagerreasoncodereservedstart) (no architecture available)Added [kBluetoothLESecurityManagerReasonCodeUnspecifiedReason](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerpairingfailedreasoncode/kbluetoothlesecuritymanagerreasoncodeunspecifiedreason) (no architecture available)Added [kBluetoothLESecurityManagerReservedEnd](https://developer.apple.com/documentation/kernel/1639940-anonymous/kbluetoothlesecuritymanagerreservedend) (no architecture available)Added [kBluetoothLESecurityManagerReservedStart](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanagerreservedstart) (no architecture available)Added [kBluetoothLESecurityManagerSignKey](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerkeydistributionformat/kbluetoothlesecuritymanagersignkey) (no architecture available)Added [kBluetoothLESecurityManagerUserInputCapabilityKeyboard](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanageruserinputcapabilitykeyboard) (no architecture available)Added [kBluetoothLESecurityManagerUserInputCapabilityNoInput](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanageruserinputcapabilitynoinput) (no architecture available)Added [kBluetoothLESecurityManagerUserInputCapabilityYesNo](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanageruserinputcapabilityyesno) (no architecture available)Added [kBluetoothLESecurityManagerUserOutputCapabilityNoOutput](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanageruseroutputcapability/kbluetoothlesecuritymanageruseroutputcapabilitynooutput) (no architecture available)Added [kBluetoothLESecurityManagerUserOutputCapabilityNumericOutput](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanageruseroutputcapabilitynumericoutput) (no architecture available)BluetoothAssignedNumbers.hAdded [kBluetoothDeviceClassMinorPeripheral2DigitalPen](https://developer.apple.com/documentation/kernel/1640543-anonymous/kbluetoothdeviceclassminorperipheral2digitalpen)Added [kBluetoothDeviceClassMinorPeripheral2GesturalInputDevice](https://developer.apple.com/documentation/iobluetooth/1459058-anonymous/kbluetoothdeviceclassminorperipheral2gesturalinputdevice)Added [kBluetoothDeviceClassMinorPeripheral2HandheldScanner](https://developer.apple.com/documentation/iobluetooth/1459058-anonymous/kbluetoothdeviceclassminorperipheral2handheldscanner)Added [kBluetoothL2CAPPSMATT](https://developer.apple.com/documentation/kernel/1640540-anonymous/kbluetoothl2cappsmatt)Added [kBluetoothSDPAttributeIdentifierHIDSSRHostMaxLatency](https://developer.apple.com/documentation/iobluetooth/kbluetoothsdpattributeidentifierhidssrhostmaxlatency)Added [kBluetoothSDPAttributeIdentifierHIDSSRHostMinTimeout](https://developer.apple.com/documentation/iobluetooth/kbluetoothsdpattributeidentifierhidssrhostmintimeout)CBCentralManager.hAdded [CBCentralManager](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager)Added [-[CBCentralManager cancelPeripheralConnection:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518952-cancelperipheralconnection)Added [-[CBCentralManager connectPeripheral:options:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518766-connect)Added [CBCentralManager.delegate](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518944-delegate)Added [-[CBCentralManager initWithDelegate:queue:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518695-initwithdelegate)Added -[CBCentralManager retrieveConnectedPeripherals]Added -[CBCentralManager retrievePeripherals:]Added [-[CBCentralManager scanForPeripheralsWithServices:options:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518986-scanforperipheralswithservices)Added CBCentralManager.stateAdded [-[CBCentralManager stopScan]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518984-stopscan)Added [CBCentralManagerDelegate](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate)Added [-[CBCentralManagerDelegate centralManager:didConnectPeripheral:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518969-centralmanager)Added [-[CBCentralManagerDelegate centralManager:didDisconnectPeripheral:error:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518791-centralmanager)Added [-[CBCentralManagerDelegate centralManager:didDiscoverPeripheral:advertisementData:RSSI:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518937-centralmanager)Added [-[CBCentralManagerDelegate centralManager:didFailToConnectPeripheral:error:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518988-centralmanager)Added -[CBCentralManagerDelegate centralManager:didRetrieveConnectedPeripherals:]Added -[CBCentralManagerDelegate centralManager:didRetrievePeripherals:]Added [-[CBCentralManagerDelegate centralManagerDidUpdateState:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518888-centralmanagerdidupdatestate)Added [CBAdvertisementDataLocalNameKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdatalocalnamekey)Added [CBAdvertisementDataManufacturerDataKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdatamanufacturerdatakey)Added [CBAdvertisementDataServiceDataKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdataservicedatakey)Added [CBAdvertisementDataServiceUUIDsKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdataserviceuuidskey)Added [CBAdvertisementDataTxPowerLevelKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdatatxpowerlevelkey)Added [CBCentralManagerScanOptionAllowDuplicatesKey](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerscanoptionallowduplicateskey)Added [CBCentralManagerState](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate)Added [CBCentralManagerStatePoweredOff](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/cbcentralmanagerstatepoweredoff)Added [CBCentralManagerStatePoweredOn](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/poweredon)Added [CBCentralManagerStateResetting](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/cbcentralmanagerstateresetting)Added [CBCentralManagerStateUnauthorized](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/cbcentralmanagerstateunauthorized)Added [CBCentralManagerStateUnknown](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/unknown)Added [CBCentralManagerStateUnsupported](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/unsupported)Added [CBConnectPeripheralOptionNotifyOnDisconnectionKey](https://developer.apple.com/documentation/corebluetooth/cbconnectperipheraloptionnotifyondisconnectionkey)CBCharacteristic.hAdded [CBCharacteristic](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic)Added CBCharacteristic.UUIDAdded [CBCharacteristic.descriptors](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518957-descriptors)Added [CBCharacteristic.isBroadcasted](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518920-isbroadcasted)Added [CBCharacteristic.isNotifying](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1519057-isnotifying)Added [CBCharacteristic.properties](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1519010-properties)Added [CBCharacteristic.service](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518728-service)Added [CBCharacteristic.value](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518878-value)Added [CBCharacteristicProperties](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties)Added [CBCharacteristicPropertyAuthenticatedSignedWrites](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/cbcharacteristicpropertyauthenticatedsignedwrites)Added [CBCharacteristicPropertyBroadcast](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/1518871-broadcast)Added [CBCharacteristicPropertyExtendedProperties](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/1518699-extendedproperties)Added [CBCharacteristicPropertyIndicate](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/1519085-indicate)Added [CBCharacteristicPropertyNotify](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/1518976-notify)Added [CBCharacteristicPropertyRead](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/cbcharacteristicpropertyread)Added [CBCharacteristicPropertyWrite](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/1519089-write)Added [CBCharacteristicPropertyWriteWithoutResponse](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/cbcharacteristicpropertywritewithoutresponse)CBDefines.hAdded #def CB_EXTERNAdded #def CB_EXTERN_CLASSCBDescriptor.hAdded [CBDescriptor](https://developer.apple.com/documentation/corebluetooth/cbdescriptor)Added CBDescriptor.UUIDAdded [CBDescriptor.characteristic](https://developer.apple.com/documentation/corebluetooth/cbdescriptor/1519035-characteristic)Added [CBDescriptor.value](https://developer.apple.com/documentation/corebluetooth/cbdescriptor/1518778-value)CBError.hAdded [CBATTError](https://developer.apple.com/documentation/corebluetooth/cbatterror)Added [CBATTErrorAttributeNotFound](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorattributenotfound)Added [CBATTErrorAttributeNotLong](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/attributenotlong)Added [CBATTErrorDomain](https://developer.apple.com/documentation/corebluetooth/cbatterrordomain)Added [CBATTErrorInsufficientAuthentication](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/insufficientauthentication)Added [CBATTErrorInsufficientAuthorization](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/insufficientauthorization)Added [CBATTErrorInsufficientEncryption](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/insufficientencryption)Added [CBATTErrorInsufficientEncryptionKeySize](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/insufficientencryptionkeysize)Added [CBATTErrorInsufficientResources](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorinsufficientresources)Added [CBATTErrorInvalidAttributeValueLength](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/invalidattributevaluelength)Added [CBATTErrorInvalidHandle](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorinvalidhandle)Added [CBATTErrorInvalidOffset](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorinvalidoffset)Added [CBATTErrorInvalidPdu](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/invalidpdu)Added [CBATTErrorPrepareQueueFull](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorpreparequeuefull)Added [CBATTErrorReadNotPermitted](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/readnotpermitted)Added [CBATTErrorRequestNotSupported](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/requestnotsupported)Added [CBATTErrorUnlikelyError](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/unlikelyerror)Added [CBATTErrorUnsupportedGroupType](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorunsupportedgrouptype)Added [CBATTErrorWriteNotPermitted](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorwritenotpermitted)Added [CBError](https://developer.apple.com/documentation/corebluetooth/cberror)Added [CBErrorDomain](https://developer.apple.com/documentation/corebluetooth/cberrordomain)Added [CBErrorUnknown](https://developer.apple.com/documentation/corebluetooth/cberror/code/unknown)CBPeripheral.hAdded [CBPeripheral](https://developer.apple.com/documentation/corebluetooth/cbperipheral)Added [CBPeripheral.RSSI](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518869-rssi)Added CBPeripheral.UUIDAdded [CBPeripheral.delegate](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518730-delegate)Added [-[CBPeripheral discoverCharacteristics:forService:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518797-discovercharacteristics)Added [-[CBPeripheral discoverDescriptorsForCharacteristic:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519070-discoverdescriptors)Added [-[CBPeripheral discoverIncludedServices:forService:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519014-discoverincludedservices)Added [-[CBPeripheral discoverServices:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518706-discoverservices)Added CBPeripheral.isConnectedAdded [CBPeripheral.name](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519029-name)Added [-[CBPeripheral readRSSI]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519111-readrssi)Added [-[CBPeripheral readValueForCharacteristic:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518759-readvalue)Added [-[CBPeripheral readValueForDescriptor:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518789-readvaluefordescriptor)Added -[CBPeripheral reliablyWriteValues:forCharacteristics:]Added [CBPeripheral.services](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518978-services)Added -[CBPeripheral setBroadcastValue:forCharacteristic:]Added [-[CBPeripheral setNotifyValue:forCharacteristic:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518949-setnotifyvalue)Added [-[CBPeripheral writeValue:forCharacteristic:type:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518747-writevalue)Added [-[CBPeripheral writeValue:forDescriptor:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519107-writevalue)Added [CBPeripheralDelegate](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate)Added [-[CBPeripheralDelegate peripheral:didDiscoverCharacteristicsForService:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518821-peripheral)Added [-[CBPeripheralDelegate peripheral:didDiscoverDescriptorsForCharacteristic:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518785-peripheral)Added [-[CBPeripheralDelegate peripheral:didDiscoverIncludedServicesForService:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1519124-peripheral)Added [-[CBPeripheralDelegate peripheral:didDiscoverServices:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518744-peripheral)Added -[CBPeripheralDelegate peripheral:didReliablyWriteValuesForCharacteristics:error:]Added -[CBPeripheralDelegate peripheral:didUpdateBroadcastStateForCharacteristic:error:]Added [-[CBPeripheralDelegate peripheral:didUpdateNotificationStateForCharacteristic:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518768-peripheral)Added [-[CBPeripheralDelegate peripheral:didUpdateValueForCharacteristic:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518708-peripheral)Added [-[CBPeripheralDelegate peripheral:didUpdateValueForDescriptor:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518929-peripheral)Added [-[CBPeripheralDelegate peripheral:didWriteValueForCharacteristic:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518823-peripheral)Added [-[CBPeripheralDelegate peripheral:didWriteValueForDescriptor:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1519062-peripheral)Added [-[CBPeripheralDelegate peripheralDidUpdateRSSI:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1519083-peripheraldidupdaterssi)Added [CBCharacteristicWriteType](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicwritetype)Added [CBCharacteristicWriteWithResponse](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicwritetype/cbcharacteristicwritewithresponse)Added [CBCharacteristicWriteWithoutResponse](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicwritetype/withoutresponse)CBService.hAdded [CBService](https://developer.apple.com/documentation/corebluetooth/cbservice)Added CBService.UUIDAdded [CBService.characteristics](https://developer.apple.com/documentation/corebluetooth/cbservice/1434319-characteristics)Added [CBService.includedServices](https://developer.apple.com/documentation/corebluetooth/cbservice/1434324-includedservices)Added [CBService.peripheral](https://developer.apple.com/documentation/corebluetooth/cbservice/1434334-peripheral)CBUUID.hAdded [CBUUID](https://developer.apple.com/documentation/corebluetooth/cbuuid)Added [+[CBUUID UUIDWithCFUUID:]](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518861-uuidwithcfuuid)Added [+[CBUUID UUIDWithData:]](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518799-uuidwithdata)Added [+[CBUUID UUIDWithString:]](https://developer.apple.com/documentation/corebluetooth/cbuuid/1519025-uuidwithstring)Added [CBUUID.data](https://developer.apple.com/documentation/corebluetooth/cbuuid/1519007-data)Added CBUUIDAppearanceStringAdded [CBUUIDCharacteristicAggregateFormatString](https://developer.apple.com/documentation/corebluetooth/cbuuidcharacteristicaggregateformatstring)Added [CBUUIDCharacteristicExtendedPropertiesString](https://developer.apple.com/documentation/corebluetooth/cbuuidcharacteristicextendedpropertiesstring)Added [CBUUIDCharacteristicFormatString](https://developer.apple.com/documentation/corebluetooth/cbuuidcharacteristicformatstring)Added [CBUUIDCharacteristicUserDescriptionString](https://developer.apple.com/documentation/corebluetooth/cbuuidcharacteristicuserdescriptionstring)Added [CBUUIDClientCharacteristicConfigurationString](https://developer.apple.com/documentation/corebluetooth/cbuuidclientcharacteristicconfigurationstring)Added CBUUIDDeviceNameStringAdded CBUUIDGenericAccessProfileStringAdded CBUUIDGenericAttributeProfileStringAdded CBUUIDPeripheralPreferredConnectionParametersStringAdded CBUUIDPeripheralPrivacyFlagStringAdded CBUUIDReconnectionAddressStringAdded [CBUUIDServerCharacteristicConfigurationString](https://developer.apple.com/documentation/corebluetooth/cbuuidservercharacteristicconfigurationstring)Added CBUUIDServiceChangedStringIOBluetoothDevice.hModified [-[IOBluetoothDevice openL2CAPChannel:findExisting:newChannel:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1589893-openl2capchannel)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.5 |

Modified [-[IOBluetoothDevice openRFCOMMChannel:channel:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1589899-openrfcommchannel)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.5 |

IOBluetoothDeviceInquiry.hAdded [-[IOBluetoothDeviceInquiry searchType]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquiry/1423413-searchtype)Added [-[IOBluetoothDeviceInquiry setSearchType:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquiry/1423413-searchtype)IOBluetoothHostController.hRemoved -[IOBluetoothHostController getAddress:]Removed -[IOBluetoothHostController getSupportedFeatures:]Removed -[IOBluetoothHostController name]Removed -[IOBluetoothHostController readLinkQualityForDevice:]Removed -[IOBluetoothHostController readRSSIForDevice:]Removed -[NSObject controllerClassOfDeviceReverted:]Modified [-[IOBluetoothHostController setClassOfDevice:forTimeInterval:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhostcontroller/1433813-setclassofdevice)

|  | Deprecation |
| --- | --- |
| From | OS X 10.6 |
| To | _none_ |

Modified [-[IOBluetoothHostController classOfDevice]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhostcontroller/1428536-classofdevice)

|  | Deprecation |
| --- | --- |
| From | OS X 10.6 |
| To | _none_ |

IOBluetoothL2CAPChannel.hModified [kIOBluetoothL2CAPChannelEventTypeReconfigured](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchanneleventtype/kiobluetoothl2capchanneleventtypereconfigured)

|  | Header |
| --- | --- |
| From | IOBluetoothUserLib.h |
| To | IOBluetoothL2CAPChannel.h |

Modified [IOBluetoothL2CAPChannelIncomingEventListener](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannelincomingeventlistener)

|  | Header |
| --- | --- |
| From | IOBluetoothUserLib.h |
| To | IOBluetoothL2CAPChannel.h |

Modified [-[NSObject registerIncomingDataListener:refCon:]](https://developer.apple.com/documentation/objectivec/nsobject/1473896-registerincomingdatalistener)

|  | Deprecation |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.5 |

Modified [IOBluetoothL2CAPChannelIncomingDataListener](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannelincomingdatalistener)

|  | Header |
| --- | --- |
| From | IOBluetoothUserLib.h |
| To | IOBluetoothL2CAPChannel.h |

Modified [kIOBluetoothL2CAPChannelEventTypeOpenComplete](https://developer.apple.com/documentation/iobluetooth/kiobluetoothl2capchanneleventtypeopencomplete)

|  | Header |
| --- | --- |
| From | IOBluetoothUserLib.h |
| To | IOBluetoothL2CAPChannel.h |

Modified [kIOBluetoothL2CAPChannelEventTypeClosed](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchanneleventtype/kiobluetoothl2capchanneleventtypeclosed)

|  | Header |
| --- | --- |
| From | IOBluetoothUserLib.h |
| To | IOBluetoothL2CAPChannel.h |

Modified [kIOBluetoothL2CAPChannelEventTypeQueueSpaceAvailable](https://developer.apple.com/documentation/iobluetooth/kiobluetoothl2capchanneleventtypequeuespaceavailable)

|  | Header |
| --- | --- |
| From | IOBluetoothUserLib.h |
| To | IOBluetoothL2CAPChannel.h |

Modified [IOBluetoothL2CAPChannelEvent](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannelevent)

|  | Header |
| --- | --- |
| From | IOBluetoothUserLib.h |
| To | IOBluetoothL2CAPChannel.h |

Modified [kIOBluetoothL2CAPChannelEventTypeData](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchanneleventtype/kiobluetoothl2capchanneleventtypedata)

|  | Header |
| --- | --- |
| From | IOBluetoothUserLib.h |
| To | IOBluetoothL2CAPChannel.h |

Modified [IOBluetoothL2CAPChannelEventType](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchanneleventtype)

|  | Header |
| --- | --- |
| From | IOBluetoothUserLib.h |
| To | IOBluetoothL2CAPChannel.h |

Modified [-[NSObject write:length:]](https://developer.apple.com/documentation/objectivec/nsobject/1473874-write)

|  | Deprecation |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.5 |

Modified [kIOBluetoothL2CAPChannelEventTypeWriteComplete](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchanneleventtype/kiobluetoothl2capchanneleventtypewritecomplete)

|  | Header |
| --- | --- |
| From | IOBluetoothUserLib.h |
| To | IOBluetoothL2CAPChannel.h |

Modified [IOBluetoothL2CAPChannelDataBlock](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchanneldatablock)

|  | Header |
| --- | --- |
| From | IOBluetoothUserLib.h |
| To | IOBluetoothL2CAPChannel.h |

IOBluetoothObject.hModified [IOBluetoothObject](https://developer.apple.com/documentation/iobluetooth/iobluetoothobject)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

IOBluetoothRFCOMMAudioController.hAdded -[IOBluetoothRFCOMMAudioDelegate audioDevice:disconnectedError:]Added -[IOBluetoothRFCOMMAudioDelegate audioDevice:scoAudioDeviceActive:]Added -[IOBluetoothRFCOMMAudioDelegate audioDevice:scoAudioDeviceInactive:]Added -[IOBluetoothRFCOMMAudioDelegate audioDevice:scoConnectionOpening:]Modified IOBluetoothRFCOMMAudioDelegate

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSObject |

IOBluetoothRFCOMMChannel.hRemoved -[IOBluetoothRFCOMMChannel registerIncomingDataListener:refCon:]Removed -[IOBluetoothRFCOMMChannel registerIncomingEventListener:refCon:]Modified [-[IOBluetoothRFCOMMChannel write:length:sleep:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel/1500152-write)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.5 |

Modified [-[IOBluetoothRFCOMMChannel writeSimple:length:sleep:bytesSent:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel/1500141-writesimple)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.5 |

IOBluetoothUserLib.hRemoved #def AVAILABLE_BLUETOOTH_VERSION_1_0_1_AND_LATERRemoved #def AVAILABLE_BLUETOOTH_VERSION_1_1_AND_LATERRemoved #def AVAILABLE_BLUETOOTH_VERSION_1_2_1_AND_LATERRemoved #def AVAILABLE_BLUETOOTH_VERSION_1_2_AND_LATERRemoved #def AVAILABLE_BLUETOOTH_VERSION_1_3_1_AND_LATERRemoved #def AVAILABLE_BLUETOOTH_VERSION_1_3_AND_LATERRemoved #def AVAILABLE_BLUETOOTH_VERSION_1_6_3_AND_LATERRemoved #def AVAILABLE_BLUETOOTH_VERSION_1_6_AND_LATERRemoved #def AVAILABLE_BLUETOOTH_VERSION_2_0_AND_LATERRemoved #def BLUETOOTH_VERSION_1_0Removed #def BLUETOOTH_VERSION_1_0_0Removed #def BLUETOOTH_VERSION_1_0_1Removed #def BLUETOOTH_VERSION_1_1Removed #def BLUETOOTH_VERSION_1_1_0Removed #def BLUETOOTH_VERSION_1_2Removed #def BLUETOOTH_VERSION_1_2_0Removed #def BLUETOOTH_VERSION_1_2_1Removed #def BLUETOOTH_VERSION_1_3Removed #def BLUETOOTH_VERSION_1_3_0Removed #def BLUETOOTH_VERSION_1_3_1Removed #def BLUETOOTH_VERSION_1_6Removed #def BLUETOOTH_VERSION_1_6_0Removed #def BLUETOOTH_VERSION_1_6_3Removed #def BLUETOOTH_VERSION_2_0Removed #def BLUETOOTH_VERSION_2_0_0Removed #def BLUETOOTH_VERSION_2_1Removed #def BLUETOOTH_VERSION_2_1_0Removed #def BLUETOOTH_VERSION_2_1_1Removed #def BLUETOOTH_VERSION_2_5Removed #def BLUETOOTH_VERSION_2_5_0Removed #def BLUETOOTH_VERSION_CURRENTRemoved #def BLUETOOTH_VERSION_MAX_ALLOWEDRemoved #def BLUETOOTH_VERSION_MIN_REQUIREDRemoved #def DEPRECATED_IN_BLUETOOTH_VERSION_2_0_AND_LATERRemoved #def DEPRECATED_IN_BLUETOOTH_VERSION_2_2_AND_LATERRemoved IOBluetoothCreateConnectionCallback (no architecture available)Removed IOBluetoothDeviceAddToFavorites() (no architecture available)Removed IOBluetoothDeviceCloseConnection() (no architecture available)Removed IOBluetoothDeviceCreateWithAddress() (no architecture available)Removed IOBluetoothDeviceGetAddress() (no architecture available)Removed IOBluetoothDeviceGetAddressString() (no architecture available)Removed IOBluetoothDeviceGetClassOfDevice() (no architecture available)Removed IOBluetoothDeviceGetClockOffset() (no architecture available)Removed IOBluetoothDeviceGetConnectionHandle() (no architecture available)Removed IOBluetoothDeviceGetDeviceClassMajor() (no architecture available)Removed IOBluetoothDeviceGetDeviceClassMinor() (no architecture available)Removed IOBluetoothDeviceGetEncryptionMode() (no architecture available)Removed IOBluetoothDeviceGetLastInquiryUpdate() (no architecture available)Removed IOBluetoothDeviceGetLastNameUpdate() (no architecture available)Removed IOBluetoothDeviceGetLastServicesUpdate() (no architecture available)Removed IOBluetoothDeviceGetLinkType() (no architecture available)Removed IOBluetoothDeviceGetName() (no architecture available)Removed IOBluetoothDeviceGetNameOrAddress() (no architecture available)Removed IOBluetoothDeviceGetPageScanMode() (no architecture available)Removed IOBluetoothDeviceGetPageScanPeriodMode() (no architecture available)Removed IOBluetoothDeviceGetPageScanRepetitionMode() (no architecture available)Removed IOBluetoothDeviceGetRecentAccessDate() (no architecture available)Removed IOBluetoothDeviceGetServiceClassMajor() (no architecture available)Removed IOBluetoothDeviceGetServiceRecordForUUID() (no architecture available)Removed IOBluetoothDeviceGetServices() (no architecture available)Removed IOBluetoothDeviceInquiryClearFoundDevices() (no architecture available)Removed IOBluetoothDeviceInquiryCompleteCallback (no architecture available)Removed IOBluetoothDeviceInquiryCreateWithCallbackRefCon() (no architecture available)Removed IOBluetoothDeviceInquiryDelete() (no architecture available)Removed IOBluetoothDeviceInquiryDeviceFoundCallback (no architecture available)Removed IOBluetoothDeviceInquiryDeviceNameUpdatedCallback (no architecture available)Removed IOBluetoothDeviceInquiryGetFoundDevices() (no architecture available)Removed IOBluetoothDeviceInquiryGetInquiryLength() (no architecture available)Removed IOBluetoothDeviceInquiryGetUpdateNewDeviceNames() (no architecture available)Removed IOBluetoothDeviceInquiryGetUserRefCon() (no architecture available)Removed IOBluetoothDeviceInquiryRef (no architecture available)Removed IOBluetoothDeviceInquirySetCompleteCallback() (no architecture available)Removed IOBluetoothDeviceInquirySetDeviceFoundCallback() (no architecture available)Removed IOBluetoothDeviceInquirySetDeviceNameUpdatedCallback() (no architecture available)Removed IOBluetoothDeviceInquirySetInquiryLength() (no architecture available)Removed IOBluetoothDeviceInquirySetSearchCriteria() (no architecture available)Removed IOBluetoothDeviceInquirySetStartedCallback() (no architecture available)Removed IOBluetoothDeviceInquirySetUpdateNewDeviceNames() (no architecture available)Removed IOBluetoothDeviceInquirySetUpdatingNamesStartedCallback() (no architecture available)Removed IOBluetoothDeviceInquirySetUserRefCon() (no architecture available)Removed IOBluetoothDeviceInquiryStart() (no architecture available)Removed IOBluetoothDeviceInquiryStartedCallback (no architecture available)Removed IOBluetoothDeviceInquiryStop() (no architecture available)Removed IOBluetoothDeviceInquiryUpdatingNamesStartedCallback (no architecture available)Removed IOBluetoothDeviceIsConnected() (no architecture available)Removed IOBluetoothDeviceIsFavorite() (no architecture available)Removed IOBluetoothDeviceIsPaired() (no architecture available)Removed IOBluetoothDeviceOpenConnection() (no architecture available)Removed IOBluetoothDeviceOpenConnectionWithOptions() (no architecture available)Removed IOBluetoothDeviceOpenL2CAPChannelAsync() (no architecture available)Removed IOBluetoothDeviceOpenL2CAPChannelSync() (no architecture available)Removed IOBluetoothDeviceOpenRFCOMMChannelAsync() (no architecture available)Removed IOBluetoothDeviceOpenRFCOMMChannelSync() (no architecture available)Removed IOBluetoothDevicePerformSDPQuery() (no architecture available)Removed IOBluetoothDeviceRemoteNameRequest() (no architecture available)Removed IOBluetoothDeviceRemoteNameRequestWithTimeout() (no architecture available)Removed IOBluetoothDeviceRemoveFromFavorites() (no architecture available)Removed IOBluetoothDeviceRequestAuthentication() (no architecture available)Removed IOBluetoothDeviceSendL2CAPEchoRequest() (no architecture available)Removed IOBluetoothFavoriteDevices() (no architecture available)Removed IOBluetoothGetVersion() (no architecture available)Removed IOBluetoothL2CAPChannelCloseChannel() (no architecture available)Removed IOBluetoothL2CAPChannelCreateFromObjectID() (no architecture available)Removed IOBluetoothL2CAPChannelGetDevice() (no architecture available)Removed IOBluetoothL2CAPChannelGetIncomingMTU() (no architecture available)Removed IOBluetoothL2CAPChannelGetLocalChannelID() (no architecture available)Removed IOBluetoothL2CAPChannelGetObjectID() (no architecture available)Removed IOBluetoothL2CAPChannelGetOutgoingMTU() (no architecture available)Removed IOBluetoothL2CAPChannelGetPSM() (no architecture available)Removed IOBluetoothL2CAPChannelGetRemoteChannelID() (no architecture available)Removed IOBluetoothL2CAPChannelIsIncoming() (no architecture available)Removed IOBluetoothL2CAPChannelRegisterIncomingDataListener() (no architecture available)Removed IOBluetoothL2CAPChannelRegisterIncomingEventListener() (no architecture available)Removed IOBluetoothL2CAPChannelRequestRemoteMTU() (no architecture available)Removed IOBluetoothL2CAPChannelWriteAsync() (no architecture available)Removed IOBluetoothL2CAPChannelWriteSync() (no architecture available)Removed IOBluetoothLocalDeviceAvailable() (no architecture available)Removed IOBluetoothLocalDeviceGetDiscoverable() (no architecture available)Removed IOBluetoothLocalDeviceGetPowerState() (no architecture available)Removed IOBluetoothLocalDeviceReadAddress() (no architecture available)Removed IOBluetoothLocalDeviceReadAuthenticationEnable() (no architecture available)Removed IOBluetoothLocalDeviceReadClassOfDevice() (no architecture available)Removed IOBluetoothLocalDeviceReadConnectionAcceptTimeout() (no architecture available)Removed IOBluetoothLocalDeviceReadEncryptionMode() (no architecture available)Removed IOBluetoothLocalDeviceReadName() (no architecture available)Removed IOBluetoothLocalDeviceReadPageScanMode() (no architecture available)Removed IOBluetoothLocalDeviceReadPageScanPeriodMode() (no architecture available)Removed IOBluetoothLocalDeviceReadPageTimeout() (no architecture available)Removed IOBluetoothLocalDeviceReadScanEnable() (no architecture available)Removed IOBluetoothLocalDeviceReadSupportedFeatures() (no architecture available)Removed IOBluetoothLocalDeviceReadVersionInformation() (no architecture available)Removed IOBluetoothObjectRelease() (no architecture available)Removed IOBluetoothObjectRetain() (no architecture available)Removed IOBluetoothPairedDevices() (no architecture available)Removed IOBluetoothRFCOMMChannelCloseChannel() (no architecture available)Removed IOBluetoothRFCOMMChannelCreateFromObjectID() (no architecture available)Removed IOBluetoothRFCOMMChannelEvent (no architecture available)Removed IOBluetoothRFCOMMChannelEventType (no architecture available)Removed IOBluetoothRFCOMMChannelGetChannelID() (no architecture available)Removed IOBluetoothRFCOMMChannelGetDevice() (no architecture available)Removed IOBluetoothRFCOMMChannelGetMTU() (no architecture available)Removed IOBluetoothRFCOMMChannelGetObjectID() (no architecture available)Removed IOBluetoothRFCOMMChannelIncomingDataListener (no architecture available)Removed IOBluetoothRFCOMMChannelIncomingEventListener (no architecture available)Removed IOBluetoothRFCOMMChannelIsIncoming() (no architecture available)Removed IOBluetoothRFCOMMChannelIsOpen() (no architecture available)Removed IOBluetoothRFCOMMChannelIsTransmissionPaused() (no architecture available)Removed IOBluetoothRFCOMMChannelRegisterIncomingEventListener() (no architecture available)Removed IOBluetoothRFCOMMChannelWriteAsync() (no architecture available)Removed IOBluetoothRFCOMMChannelWriteSync() (no architecture available)Removed IOBluetoothRFCOMMDataBlock (no architecture available)Removed IOBluetoothRFCOMMEvent (no architecture available)Removed IOBluetoothRFCOMMFlowControlStatus (no architecture available)Removed IOBluetoothRFCOMMSendRemoteLineStatus() (no architecture available)Removed IOBluetoothRFCOMMSetSerialParameters() (no architecture available)Removed IOBluetoothReadAddressCallback (no architecture available)Removed IOBluetoothReadAuthenticationEnableCallback (no architecture available)Removed IOBluetoothReadClassOfDeviceCallback (no architecture available)Removed IOBluetoothReadConnectionAcceptTimeoutCallback (no architecture available)Removed IOBluetoothReadEncryptionModeCallback (no architecture available)Removed IOBluetoothReadLocalSupportedFeaturesCallback (no architecture available)Removed IOBluetoothReadLocalVersionInformationCallback (no architecture available)Removed IOBluetoothReadNameCallback (no architecture available)Removed IOBluetoothReadPageScanEnableCallback (no architecture available)Removed IOBluetoothReadPageScanModeCallback (no architecture available)Removed IOBluetoothReadPageScanPeriodModeCallback (no architecture available)Removed IOBluetoothReadPageTimeoutCallback (no architecture available)Removed IOBluetoothRecentDevices() (no architecture available)Removed IOBluetoothRemoteNameRequestCallback (no architecture available)Removed IOBluetoothSDPDataElementContainsDataElement() (no architecture available)Removed IOBluetoothSDPDataElementGetArrayValue() (no architecture available)Removed IOBluetoothSDPDataElementGetDataValue() (no architecture available)Removed IOBluetoothSDPDataElementGetNumberValue() (no architecture available)Removed IOBluetoothSDPDataElementGetSize() (no architecture available)Removed IOBluetoothSDPDataElementGetSizeDescriptor() (no architecture available)Removed IOBluetoothSDPDataElementGetStringValue() (no architecture available)Removed IOBluetoothSDPDataElementGetTypeDescriptor() (no architecture available)Removed IOBluetoothSDPDataElementGetUUIDValue() (no architecture available)Removed IOBluetoothSDPDataElementIsEqualToDataElement() (no architecture available)Removed IOBluetoothSDPQueryCallback (no architecture available)Removed IOBluetoothSDPServiceRecordGetAttributeDataElement() (no architecture available)Removed IOBluetoothSDPServiceRecordGetAttributes() (no architecture available)Removed IOBluetoothSDPServiceRecordGetDevice() (no architecture available)Removed IOBluetoothSDPServiceRecordGetL2CAPPSM() (no architecture available)Removed IOBluetoothSDPServiceRecordGetRFCOMMChannelID() (no architecture available)Removed IOBluetoothSDPServiceRecordGetServiceName() (no architecture available)Removed IOBluetoothSDPServiceRecordGetServiceRecordHandle() (no architecture available)Removed IOBluetoothSDPServiceRecordHasServiceFromArray() (no architecture available)Removed IOBluetoothSDPUUIDCreateUUID16() (no architecture available)Removed IOBluetoothSDPUUIDCreateUUID32() (no architecture available)Removed IOBluetoothSDPUUIDCreateWithBytes() (no architecture available)Removed IOBluetoothSDPUUIDCreateWithData() (no architecture available)Removed IOBluetoothSDPUUIDGetBytes() (no architecture available)Removed IOBluetoothSDPUUIDGetLength() (no architecture available)Removed IOBluetoothSDPUUIDGetUUIDWithLength() (no architecture available)Removed IOBluetoothSDPUUIDIsEqualToUUID() (no architecture available)Removed IOBluetoothSetSupervisionTimeout() (no architecture available)Removed #def MAC_OS_X_VERSION_10_2_1Removed #def MAC_OS_X_VERSION_10_2_2Removed #def MAC_OS_X_VERSION_10_2_3Removed #def MAC_OS_X_VERSION_10_2_4Removed #def MAC_OS_X_VERSION_10_2_5Removed #def MAC_OS_X_VERSION_10_2_6Removed #def MAC_OS_X_VERSION_10_2_7Removed #def MAC_OS_X_VERSION_MIN_REQUIREDRemoved kIOBluetoothRFCOMMChannelEventTypeClosed (no architecture available)Removed kIOBluetoothRFCOMMChannelEventTypeControlSignalsChanged (no architecture available)Removed kIOBluetoothRFCOMMChannelEventTypeData (no architecture available)Removed kIOBluetoothRFCOMMChannelEventTypeFlowControlChanged (no architecture available)Removed kIOBluetoothRFCOMMChannelEventTypeOpenComplete (no architecture available)Removed kIOBluetoothRFCOMMChannelEventTypeQueueSpaceAvailable (no architecture available)Removed kIOBluetoothRFCOMMChannelEventTypeWriteComplete (no architecture available)Removed kIOBluetoothRFCOMMChannelFlowControlStatusIsOff (no architecture available)Removed kIOBluetoothRFCOMMChannelFlowControlStatusIsOn (no architecture available)Removed kIOBluetoothRFCOMMChannelTerminatedEvent (no architecture available)Removed kIOBluetoothRFCOMMFlowControlChangedEvent (no architecture available)Removed kIOBluetoothRFCOMMNewDataEvent (no architecture available)Added [IOBluetoothDeviceSearchTypes](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicesearchtypes) (no architecture available)Added [IOBluetoothDeviceSearchTypesBits](https://developer.apple.com/documentation/iobluetooth/iobluetoothuserlib.h/iobluetoothdevicesearchtypesbits) (no architecture available)Added [kIOBluetoothDeviceSearchClassic](https://developer.apple.com/documentation/iobluetooth/kiobluetoothdevicesearchclassic) (no architecture available)Modified [IOBluetoothGetObjectIDFromArguments()](https://developer.apple.com/documentation/iobluetooth/1550919-iobluetoothgetobjectidfromargume)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

OBEX.hModified [OBEXSessionDelete()](https://developer.apple.com/documentation/iobluetooth/1501625-obexsessiondelete)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXSessionPutResponse()](https://developer.apple.com/documentation/iobluetooth/1501534-obexsessionputresponse)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXSessionDisconnect()](https://developer.apple.com/documentation/iobluetooth/1501556-obexsessiondisconnect)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXSessionPut()](https://developer.apple.com/documentation/iobluetooth/1501513-obexsessionput)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXSessionDisconnectResponse()](https://developer.apple.com/documentation/iobluetooth/1501581-obexsessiondisconnectresponse)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXSessionGetAvailableCommandPayloadLength()](https://developer.apple.com/documentation/iobluetooth/1501495-obexsessiongetavailablecommandpa)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXSessionGet()](https://developer.apple.com/documentation/iobluetooth/1501568-obexsessionget)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXSessionAbortResponse()](https://developer.apple.com/documentation/iobluetooth/1501715-obexsessionabortresponse)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXCreateVEvent()](https://developer.apple.com/documentation/iobluetooth/1501541-obexcreatevevent)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXSessionHasOpenOBEXConnection()](https://developer.apple.com/documentation/iobluetooth/1501553-obexsessionhasopenobexconnection)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXSessionGetResponse()](https://developer.apple.com/documentation/iobluetooth/1501696-obexsessiongetresponse)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXCreateVCard()](https://developer.apple.com/documentation/iobluetooth/1501612-obexcreatevcard)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXSessionGetAvailableCommandResponsePayloadLength()](https://developer.apple.com/documentation/iobluetooth/1501571-obexsessiongetavailablecommandre)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXSessionAbort()](https://developer.apple.com/documentation/iobluetooth/1501545-obexsessionabort)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXSessionSetPathResponse()](https://developer.apple.com/documentation/iobluetooth/1501520-obexsessionsetpathresponse)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXSessionSetPath()](https://developer.apple.com/documentation/iobluetooth/1501508-obexsessionsetpath)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXSessionConnect()](https://developer.apple.com/documentation/iobluetooth/1501667-obexsessionconnect)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXSessionSetServerCallback()](https://developer.apple.com/documentation/iobluetooth/1501719-obexsessionsetservercallback)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXSessionGetMaxPacketLength()](https://developer.apple.com/documentation/iobluetooth/1501679-obexsessiongetmaxpacketlength)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [OBEXSessionConnectResponse()](https://developer.apple.com/documentation/iobluetooth/1501703-obexsessionconnectresponse)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

OBEXBluetooth.hModified [IOBluetoothOBEXSessionCreateWithIncomingIOBluetoothRFCOMMChannel()](https://developer.apple.com/documentation/iobluetooth/1577807-iobluetoothobexsessioncreatewith)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [IOBluetoothOBEXSessionOpenTransportConnection()](https://developer.apple.com/documentation/iobluetooth/1577806-iobluetoothobexsessionopentransp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [IOBluetoothOBEXSessionCreateWithIOBluetoothDeviceRefAndChannelNumber()](https://developer.apple.com/documentation/iobluetooth/1577805-iobluetoothobexsessioncreatewith)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

Modified [IOBluetoothOBEXSessionCreateWithIOBluetoothSDPServiceRecordRef()](https://developer.apple.com/documentation/iobluetooth/1577804-iobluetoothobexsessioncreatewith)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.6 |

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
