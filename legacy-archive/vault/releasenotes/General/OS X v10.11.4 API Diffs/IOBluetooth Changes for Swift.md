---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/IOBluetooth.html
archived_at: '2026-07-18T02:53:52.143116Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# IOBluetooth Changes for Swift

### IOBluetooth

Removed [IOBluetoothHandsFree.isConnected() -> Bool](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1811379-isconnected)Removed IOBluetoothHandsFreeAudioGatewayFeatureAttachedNumberToVoiceTagRemoved IOBluetoothHandsFreeAudioGatewayFeatureECAndOrNRFunctionRemoved IOBluetoothHandsFreeAudioGatewayFeatureEnhancedCallControlRemoved IOBluetoothHandsFreeAudioGatewayFeatureEnhancedCallStatusRemoved IOBluetoothHandsFreeAudioGatewayFeatureExtendedErrorResultCodesRemoved IOBluetoothHandsFreeAudioGatewayFeatureInBandRingToneRemoved IOBluetoothHandsFreeAudioGatewayFeatureNoneRemoved IOBluetoothHandsFreeAudioGatewayFeatureRejectCallCapabilityRemoved IOBluetoothHandsFreeAudioGatewayFeaturesRemoved IOBluetoothHandsFreeAudioGatewayFeatureThreeWayCallingRemoved IOBluetoothHandsFreeAudioGatewayFeatureVoiceRecognitionRemoved IOBluetoothHandsFreeCallHoldMode0Removed IOBluetoothHandsFreeCallHoldMode1Removed IOBluetoothHandsFreeCallHoldMode1idxRemoved IOBluetoothHandsFreeCallHoldMode2Removed IOBluetoothHandsFreeCallHoldMode2idxRemoved IOBluetoothHandsFreeCallHoldMode3Removed IOBluetoothHandsFreeCallHoldMode4Removed IOBluetoothHandsFreeCallHoldModesRemoved IOBluetoothHandsFreeDeviceFeatureCLIPresentationRemoved IOBluetoothHandsFreeDeviceFeatureECAndOrNRFunctionRemoved IOBluetoothHandsFreeDeviceFeatureEnhancedCallControlRemoved IOBluetoothHandsFreeDeviceFeatureEnhancedCallStatusRemoved IOBluetoothHandsFreeDeviceFeatureNoneRemoved IOBluetoothHandsFreeDeviceFeatureRemoteVolumeControlRemoved IOBluetoothHandsFreeDeviceFeaturesRemoved IOBluetoothHandsFreeDeviceFeatureThreeWayCallingRemoved IOBluetoothHandsFreeDeviceFeatureVoiceRecognitionRemoved IOBluetoothHandsFreeManufactureSpecificSMSSupportRemoved IOBluetoothHandsFreePDUMessageStatusRemoved IOBluetoothHandsFreePDUStatusAllRemoved IOBluetoothHandsFreePDUStatusRecReadRemoved IOBluetoothHandsFreePDUStatusRecUnreadRemoved IOBluetoothHandsFreePDUStatusStoSentRemoved IOBluetoothHandsFreePDUStatusStoUnsentRemoved IOBluetoothHandsFreePhase2pSMSSupportRemoved IOBluetoothHandsFreePhase2SMSSupportRemoved IOBluetoothHandsFreeSMSSupportRemoved IOBluetoothSMSModeRemoved IOBluetoothSMSModePDURemoved IOBluetoothSMSModeTextAdded [IOBluetoothHandsFree.connected](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427760-connected)Added [IOBluetoothHandsFreeAudioGatewayFeatures [enum]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures)Added [IOBluetoothHandsFreeAudioGatewayFeatures.AttachedNumberToVoiceTag](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/attachednumbertovoicetag)Added [IOBluetoothHandsFreeAudioGatewayFeatures.CodecNegotiation](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/iobluetoothhandsfreeaudiogatewayfeaturecodecnegotiation)Added [IOBluetoothHandsFreeAudioGatewayFeatures.ECAndOrNRFunction](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/iobluetoothhandsfreeaudiogatewayfeatureecandornrfunction)Added [IOBluetoothHandsFreeAudioGatewayFeatures.EnhancedCallControl](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/enhancedcallcontrol)Added [IOBluetoothHandsFreeAudioGatewayFeatures.EnhancedCallStatus](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/iobluetoothhandsfreeaudiogatewayfeatureenhancedcallstatus)Added [IOBluetoothHandsFreeAudioGatewayFeatures.ExtendedErrorResultCodes](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/extendederrorresultcodes)Added [IOBluetoothHandsFreeAudioGatewayFeatures.InBandRingTone](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/iobluetoothhandsfreeaudiogatewayfeatureinbandringtone)Added [IOBluetoothHandsFreeAudioGatewayFeatures.None](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/iobluetoothhandsfreeaudiogatewayfeaturenone)Added [IOBluetoothHandsFreeAudioGatewayFeatures.RejectCallCapability](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/iobluetoothhandsfreeaudiogatewayfeaturerejectcallcapability)Added [IOBluetoothHandsFreeAudioGatewayFeatures.ThreeWayCalling](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/iobluetoothhandsfreeaudiogatewayfeaturethreewaycalling)Added [IOBluetoothHandsFreeAudioGatewayFeatures.VoiceRecognition](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/iobluetoothhandsfreeaudiogatewayfeaturevoicerecognition)Added [IOBluetoothHandsFreeCallHoldModes [enum]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallholdmodes)Added [IOBluetoothHandsFreeCallHoldModes.Mode0](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallholdmodes/iobluetoothhandsfreecallholdmode0)Added [IOBluetoothHandsFreeCallHoldModes.Mode1](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallholdmodes/mode1)Added [IOBluetoothHandsFreeCallHoldModes.Mode1idx](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallholdmodes/iobluetoothhandsfreecallholdmode1idx)Added [IOBluetoothHandsFreeCallHoldModes.Mode2](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallholdmodes/iobluetoothhandsfreecallholdmode2)Added [IOBluetoothHandsFreeCallHoldModes.Mode2idx](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallholdmodes/mode2idx)Added [IOBluetoothHandsFreeCallHoldModes.Mode3](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallholdmodes/mode3)Added [IOBluetoothHandsFreeCallHoldModes.Mode4](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallholdmodes/iobluetoothhandsfreecallholdmode4)Added [IOBluetoothHandsFreeCodecID [enum]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecodecid)Added [IOBluetoothHandsFreeCodecID.IDAACELD](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecodecid/iobluetoothhandsfreecodecidaaceld)Added [IOBluetoothHandsFreeCodecID.IDCVSD](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecodecid/iobluetoothhandsfreecodecidcvsd)Added [IOBluetoothHandsFreeCodecID.IDmSBC](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecodecid/iobluetoothhandsfreecodecidmsbc)Added [IOBluetoothHandsFreeDeviceFeatures [enum]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures)Added [IOBluetoothHandsFreeDeviceFeatures.CLIPresentation](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures/clipresentation)Added [IOBluetoothHandsFreeDeviceFeatures.CodecNegotiation](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures/iobluetoothhandsfreedevicefeaturecodecnegotiation)Added [IOBluetoothHandsFreeDeviceFeatures.ECAndOrNRFunction](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures/ecandornrfunction)Added [IOBluetoothHandsFreeDeviceFeatures.EnhancedCallControl](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures/enhancedcallcontrol)Added [IOBluetoothHandsFreeDeviceFeatures.EnhancedCallStatus](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures/iobluetoothhandsfreedevicefeatureenhancedcallstatus)Added [IOBluetoothHandsFreeDeviceFeatures.None](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures/none)Added [IOBluetoothHandsFreeDeviceFeatures.RemoteVolumeControl](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures/iobluetoothhandsfreedevicefeatureremotevolumecontrol)Added [IOBluetoothHandsFreeDeviceFeatures.ThreeWayCalling](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures/threewaycalling)Added [IOBluetoothHandsFreeDeviceFeatures.VoiceRecognition](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures/voicerecognition)Added [IOBluetoothHandsFreePDUMessageStatus [enum]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreepdumessagestatus)Added [IOBluetoothHandsFreePDUMessageStatus.StatusAll](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreepdumessagestatus/statusall)Added [IOBluetoothHandsFreePDUMessageStatus.StatusRecRead](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreepdumessagestatus/statusrecread)Added [IOBluetoothHandsFreePDUMessageStatus.StatusRecUnread](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreepdumessagestatus/iobluetoothhandsfreepdustatusrecunread)Added [IOBluetoothHandsFreePDUMessageStatus.StatusStoSent](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreepdumessagestatus/iobluetoothhandsfreepdustatusstosent)Added [IOBluetoothHandsFreePDUMessageStatus.StatusStoUnsent](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreepdumessagestatus/statusstounsent)Added [IOBluetoothHandsFreeSMSSupport [enum]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreesmssupport)Added [IOBluetoothHandsFreeSMSSupport.ManufactureSpecificSMSSupport](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreesmssupport/iobluetoothhandsfreemanufacturespecificsmssupport)Added [IOBluetoothHandsFreeSMSSupport.Phase2pSMSSupport](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreesmssupport/iobluetoothhandsfreephase2psmssupport)Added [IOBluetoothHandsFreeSMSSupport.Phase2SMSSupport](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreesmssupport/iobluetoothhandsfreephase2smssupport)Added [IOBluetoothL2CAPChannelEvent.init(eventType: IOBluetoothL2CAPChannelEventType, u: IOBluetoothL2CAPChannelEvent.__Unnamed_union_u, status: IOReturn)](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannelevent/1429414-init)Added [IOBluetoothL2CAPChannelEvent.u](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannelevent/1433594-u)Added [IOBluetoothSMSMode [enum]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsmsmode)Added [IOBluetoothSMSMode.PDU](https://developer.apple.com/documentation/iobluetooth/iobluetoothsmsmode/pdu)Added [IOBluetoothSMSMode.Text](https://developer.apple.com/documentation/iobluetooth/iobluetoothsmsmode/iobluetoothsmsmodetext)Added OBEXSessionEvent.init(type: OBEXSessionEventType, session: OBEXSessionRef, refCon: UnsafeMutablePointer<Void>, isEndOfEventData: DarwinBoolean, reserved1: UnsafeMutablePointer<Void>, reserved2: UnsafeMutablePointer<Void>, u: OBEXSessionEvent.__Unnamed_union_u)Added [OBEXSessionEvent.u](https://developer.apple.com/documentation/iobluetooth/obexsessionevent/1434734-u)Added [kBluetoothHCIVersionCoreSpecification4_2](https://developer.apple.com/documentation/iobluetooth/kbluetoothhciversioncorespecification4_2)Added [kBluetoothLMPVersionCoreSpecification4_2](https://developer.apple.com/documentation/iobluetooth/kbluetoothlmpversioncorespecification4_2)Modified [IOBluetoothDevice](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice)

|  | Declaration |
| --- | --- |
| From | ``` class IOBluetoothDevice : IOBluetoothObject, NSCoding, NSSecureCoding {     class func registerForConnectNotifications(_ observer: AnyObject!, selector inSelector: Selector) -> IOBluetoothUserNotification!     func registerForDisconnectNotification(_ observer: AnyObject!, selector inSelector: Selector) -> IOBluetoothUserNotification!     convenience init!(address address: UnsafePointer<BluetoothDeviceAddress>)     class func deviceWithAddress(_ address: UnsafePointer<BluetoothDeviceAddress>) -> Self!     class func withAddress(_ address: UnsafePointer<BluetoothDeviceAddress>) -> Self!     convenience init!(addressString address: String!)     class func deviceWithAddressString(_ address: String!) -> Self!     class func withDeviceRef(_ deviceRef: IOBluetoothDevice!) -> Self!     func getDeviceRef() -> Unmanaged<IOBluetoothDevice>!     func openL2CAPChannelSync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, delegate channelDelegate: AnyObject!) -> IOReturn     func openL2CAPChannelAsync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, delegate channelDelegate: AnyObject!) -> IOReturn     func openL2CAPChannel(_ psm: BluetoothL2CAPPSM, findExisting findExisting: Bool, newChannel newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>) -> IOReturn     func sendL2CAPEchoRequest(_ data: UnsafeMutablePointer<Void>, length length: UInt16) -> IOReturn     func openRFCOMMChannel(_ channelID: BluetoothRFCOMMChannelID, channel rfcommChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>) -> IOReturn     func openRFCOMMChannelSync(_ rfcommChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>, withChannelID channelID: BluetoothRFCOMMChannelID, delegate channelDelegate: AnyObject!) -> IOReturn     func openRFCOMMChannelAsync(_ rfcommChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>, withChannelID channelID: BluetoothRFCOMMChannelID, delegate channelDelegate: AnyObject!) -> IOReturn     var classOfDevice: BluetoothClassOfDevice { get }     func getClassOfDevice() -> BluetoothClassOfDevice     var serviceClassMajor: BluetoothServiceClassMajor { get }     func getServiceClassMajor() -> BluetoothServiceClassMajor     var deviceClassMajor: BluetoothDeviceClassMajor { get }     func getDeviceClassMajor() -> BluetoothDeviceClassMajor     var deviceClassMinor: BluetoothDeviceClassMinor { get }     func getDeviceClassMinor() -> BluetoothDeviceClassMinor     var name: String! { get }     func getName() -> String!     var nameOrAddress: String! { get }     func getNameOrAddress() -> String!     var lastNameUpdate: NSDate! { get }     func getLastNameUpdate() -> NSDate!     func getAddress() -> UnsafePointer<BluetoothDeviceAddress>     var addressString: String! { get }     func getAddressString() -> String!     func getPageScanRepetitionMode() -> BluetoothPageScanRepetitionMode     func getPageScanPeriodMode() -> BluetoothPageScanPeriodMode     func getPageScanMode() -> BluetoothPageScanMode     func getClockOffset() -> BluetoothClockOffset     func getLastInquiryUpdate() -> NSDate!     func RSSI() -> BluetoothHCIRSSIValue     func rawRSSI() -> BluetoothHCIRSSIValue     func isConnected() -> Bool     func openConnection() -> IOReturn     func openConnection(_ target: AnyObject!) -> IOReturn     func openConnection(_ target: AnyObject!, withPageTimeout pageTimeoutValue: BluetoothHCIPageTimeout, authenticationRequired authenticationRequired: Bool) -> IOReturn     func closeConnection() -> IOReturn     func remoteNameRequest(_ target: AnyObject!) -> IOReturn     func remoteNameRequest(_ target: AnyObject!, withPageTimeout pageTimeoutValue: BluetoothHCIPageTimeout) -> IOReturn     func requestAuthentication() -> IOReturn     var connectionHandle: BluetoothConnectionHandle { get }     func getConnectionHandle() -> BluetoothConnectionHandle     func isIncoming() -> Bool     func getLinkType() -> BluetoothLinkType     func getEncryptionMode() -> BluetoothHCIEncryptionMode     func performSDPQuery(_ target: AnyObject!) -> IOReturn     func performSDPQuery(_ target: AnyObject!, uuids uuidArray: [AnyObject]!) -> IOReturn     var services: [AnyObject]! { get }     func getServices() -> [AnyObject]!     func getLastServicesUpdate() -> NSDate!     func getServiceRecordForUUID(_ sdpUUID: IOBluetoothSDPUUID!) -> IOBluetoothSDPServiceRecord!     class func favoriteDevices() -> [AnyObject]!     func isFavorite() -> Bool     func addToFavorites() -> IOReturn     func removeFromFavorites() -> IOReturn     class func recentDevices(_ numDevices: UInt) -> [AnyObject]!     func recentAccessDate() -> NSDate!     class func pairedDevices() -> [AnyObject]!     func isPaired() -> Bool     func setSupervisionTimeout(_ timeout: UInt16) -> IOReturn     func openL2CAPChannelSync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, withConfiguration channelConfiguration: [NSObject : AnyObject]!, delegate channelDelegate: AnyObject!) -> IOReturn     func openL2CAPChannelAsync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, withConfiguration channelConfiguration: [NSObject : AnyObject]!, delegate channelDelegate: AnyObject!) -> IOReturn     func awakeAfterUsingCoder(_ coder: NSCoder!) -> AnyObject! } extension IOBluetoothDevice {     func handsFreeAudioGatewayDriverID() -> String!     func handsFreeAudioGatewayServiceRecord() -> IOBluetoothSDPServiceRecord!     var handsFreeAudioGateway: Bool { get }     func handsFreeDeviceDriverID() -> String!     func handsFreeDeviceServiceRecord() -> IOBluetoothSDPServiceRecord!     var handsFreeDevice: Bool { get } } ``` |
| To | ``` class IOBluetoothDevice : IOBluetoothObject, NSCoding, NSSecureCoding {     class func registerForConnectNotifications(_ observer: AnyObject!, selector inSelector: Selector) -> IOBluetoothUserNotification!     func registerForDisconnectNotification(_ observer: AnyObject!, selector inSelector: Selector) -> IOBluetoothUserNotification!     convenience init!(address address: UnsafePointer<BluetoothDeviceAddress>)     class func deviceWithAddress(_ address: UnsafePointer<BluetoothDeviceAddress>) -> Self!     class func withAddress(_ address: UnsafePointer<BluetoothDeviceAddress>) -> Self!     convenience init!(addressString address: String!)     class func deviceWithAddressString(_ address: String!) -> Self!     class func withDeviceRef(_ deviceRef: IOBluetoothDeviceRef!) -> Self!     func getDeviceRef() -> Unmanaged<IOBluetoothDeviceRef>!     func openL2CAPChannelSync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, delegate channelDelegate: AnyObject!) -> IOReturn     func openL2CAPChannelAsync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, delegate channelDelegate: AnyObject!) -> IOReturn     func openL2CAPChannel(_ psm: BluetoothL2CAPPSM, findExisting findExisting: Bool, newChannel newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>) -> IOReturn     func sendL2CAPEchoRequest(_ data: UnsafeMutablePointer<Void>, length length: UInt16) -> IOReturn     func openRFCOMMChannel(_ channelID: BluetoothRFCOMMChannelID, channel rfcommChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>) -> IOReturn     func openRFCOMMChannelSync(_ rfcommChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>, withChannelID channelID: BluetoothRFCOMMChannelID, delegate channelDelegate: AnyObject!) -> IOReturn     func openRFCOMMChannelAsync(_ rfcommChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>, withChannelID channelID: BluetoothRFCOMMChannelID, delegate channelDelegate: AnyObject!) -> IOReturn     var classOfDevice: BluetoothClassOfDevice { get }     func getClassOfDevice() -> BluetoothClassOfDevice     var serviceClassMajor: BluetoothServiceClassMajor { get }     func getServiceClassMajor() -> BluetoothServiceClassMajor     var deviceClassMajor: BluetoothDeviceClassMajor { get }     func getDeviceClassMajor() -> BluetoothDeviceClassMajor     var deviceClassMinor: BluetoothDeviceClassMinor { get }     func getDeviceClassMinor() -> BluetoothDeviceClassMinor     var name: String! { get }     func getName() -> String!     var nameOrAddress: String! { get }     func getNameOrAddress() -> String!     var lastNameUpdate: NSDate! { get }     func getLastNameUpdate() -> NSDate!     func getAddress() -> UnsafePointer<BluetoothDeviceAddress>     var addressString: String! { get }     func getAddressString() -> String!     func getPageScanRepetitionMode() -> BluetoothPageScanRepetitionMode     func getPageScanPeriodMode() -> BluetoothPageScanPeriodMode     func getPageScanMode() -> BluetoothPageScanMode     func getClockOffset() -> BluetoothClockOffset     func getLastInquiryUpdate() -> NSDate!     func RSSI() -> BluetoothHCIRSSIValue     func rawRSSI() -> BluetoothHCIRSSIValue     func isConnected() -> Bool     func openConnection() -> IOReturn     func openConnection(_ target: AnyObject!) -> IOReturn     func openConnection(_ target: AnyObject!, withPageTimeout pageTimeoutValue: BluetoothHCIPageTimeout, authenticationRequired authenticationRequired: Bool) -> IOReturn     func closeConnection() -> IOReturn     func remoteNameRequest(_ target: AnyObject!) -> IOReturn     func remoteNameRequest(_ target: AnyObject!, withPageTimeout pageTimeoutValue: BluetoothHCIPageTimeout) -> IOReturn     func requestAuthentication() -> IOReturn     var connectionHandle: BluetoothConnectionHandle { get }     func getConnectionHandle() -> BluetoothConnectionHandle     func isIncoming() -> Bool     func getLinkType() -> BluetoothLinkType     func getEncryptionMode() -> BluetoothHCIEncryptionMode     func performSDPQuery(_ target: AnyObject!) -> IOReturn     func performSDPQuery(_ target: AnyObject!, uuids uuidArray: [AnyObject]!) -> IOReturn     var services: [AnyObject]! { get }     func getServices() -> [AnyObject]!     func getLastServicesUpdate() -> NSDate!     func getServiceRecordForUUID(_ sdpUUID: IOBluetoothSDPUUID!) -> IOBluetoothSDPServiceRecord!     class func favoriteDevices() -> [AnyObject]!     func isFavorite() -> Bool     func addToFavorites() -> IOReturn     func removeFromFavorites() -> IOReturn     class func recentDevices(_ numDevices: UInt) -> [AnyObject]!     func recentAccessDate() -> NSDate!     class func pairedDevices() -> [AnyObject]!     func isPaired() -> Bool     func setSupervisionTimeout(_ timeout: UInt16) -> IOReturn     func openL2CAPChannelSync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, withConfiguration channelConfiguration: [NSObject : AnyObject]!, delegate channelDelegate: AnyObject!) -> IOReturn     func openL2CAPChannelAsync(_ newChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>, withPSM psm: BluetoothL2CAPPSM, withConfiguration channelConfiguration: [NSObject : AnyObject]!, delegate channelDelegate: AnyObject!) -> IOReturn     func awakeAfterUsingCoder(_ coder: NSCoder!) -> AnyObject! } extension IOBluetoothDevice {     func handsFreeAudioGatewayDriverID() -> String!     func handsFreeAudioGatewayServiceRecord() -> IOBluetoothSDPServiceRecord!     var handsFreeAudioGateway: Bool { get }     func handsFreeDeviceDriverID() -> String!     func handsFreeDeviceServiceRecord() -> IOBluetoothSDPServiceRecord!     var handsFreeDevice: Bool { get } } ``` |

Modified [IOBluetoothDeviceRef](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceref)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothDeviceRef = IOBluetoothDevice ``` |
| To | ``` class IOBluetoothDeviceRef { } ``` |

Modified [IOBluetoothHandsFree](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree)

|  | Declaration |
| --- | --- |
| From | ``` class IOBluetoothHandsFree : NSObject {     var supportedFeatures: UInt32     var inputVolume: Float     var inputMuted: Bool     var outputVolume: Float     var outputMuted: Bool     var device: IOBluetoothDevice! { get }     var deviceSupportedFeatures: UInt32 { get }     var deviceSupportedSMSServices: UInt32 { get }     var deviceCallHoldModes: UInt32 { get }     var SMSMode: IOBluetoothSMSMode { get }     var SMSEnabled: Bool { get }     unowned(unsafe) var delegate: IOBluetoothHandsFreeDelegate!     func indicator(_ indicatorName: String!) -> Int32     func setIndicator(_ indicatorName: String!, value indicatorValue: Int32)     init!(device device: IOBluetoothDevice!, delegate inDelegate: IOBluetoothHandsFreeDelegate!)     func connect()     func disconnect()     func isConnected() -> Bool     func connectSCO()     func disconnectSCO()     func isSCOConnected() -> Bool } ``` |
| To | ``` class IOBluetoothHandsFree : NSObject {     var supportedFeatures: UInt32     var inputVolume: Float     var inputMuted: Bool     var outputVolume: Float     var outputMuted: Bool     var device: IOBluetoothDevice! { get }     var deviceSupportedFeatures: UInt32 { get }     var deviceSupportedSMSServices: UInt32 { get }     var deviceCallHoldModes: UInt32 { get }     var SMSMode: IOBluetoothSMSMode { get }     var SMSEnabled: Bool { get }     unowned(unsafe) var delegate: IOBluetoothHandsFreeDelegate!     func indicator(_ indicatorName: String!) -> Int32     func setIndicator(_ indicatorName: String!, value indicatorValue: Int32)     init!(device device: IOBluetoothDevice!, delegate inDelegate: IOBluetoothHandsFreeDelegate!)     func connect()     func disconnect()     var connected: Bool { get }     func connectSCO()     func disconnectSCO()     func isSCOConnected() -> Bool } ``` |

Modified [IOBluetoothL2CAPChannelEvent [struct]](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannelevent)

|  | Declaration |
| --- | --- |
| From | ``` struct IOBluetoothL2CAPChannelEvent {     var eventType: IOBluetoothL2CAPChannelEventType     var status: IOReturn     init() } ``` |
| To | ``` struct IOBluetoothL2CAPChannelEvent {     struct __Unnamed_union_u {         var data: IOBluetoothL2CAPChannelDataBlock         var writeRefCon: UnsafeMutablePointer<Void>         var padding: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)         init(data data: IOBluetoothL2CAPChannelDataBlock)         init(writeRefCon writeRefCon: UnsafeMutablePointer<Void>)         init(padding padding: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))         init()     }     var eventType: IOBluetoothL2CAPChannelEventType     var u: IOBluetoothL2CAPChannelEvent.__Unnamed_union_u     var status: IOReturn     init()     init(eventType eventType: IOBluetoothL2CAPChannelEventType, u u: IOBluetoothL2CAPChannelEvent.__Unnamed_union_u, status status: IOReturn) } ``` |

Modified [IOBluetoothL2CAPChannelRef](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannelref)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothL2CAPChannelRef = IOBluetoothL2CAPChannel ``` |
| To | ``` class IOBluetoothL2CAPChannelRef { } ``` |

Modified [IOBluetoothObjectRef](https://developer.apple.com/documentation/iobluetooth/iobluetoothobjectref)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothObjectRef = IOBluetoothObject ``` |
| To | ``` class IOBluetoothObjectRef { } ``` |

Modified [IOBluetoothRFCOMMChannel](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel)

|  | Declaration |
| --- | --- |
| From | ``` class IOBluetoothRFCOMMChannel : IOBluetoothObject, NSPortDelegate {     class func registerForChannelOpenNotifications(_ object: AnyObject!, selector selector: Selector) -> IOBluetoothUserNotification!     class func registerForChannelOpenNotifications(_ object: AnyObject!, selector selector: Selector, withChannelID channelID: BluetoothRFCOMMChannelID, direction inDirection: IOBluetoothUserNotificationChannelDirection) -> IOBluetoothUserNotification!     class func withRFCOMMChannelRef(_ rfcommChannelRef: IOBluetoothRFCOMMChannel!) -> Self!     class func withObjectID(_ objectID: IOBluetoothObjectID) -> Self!     func getRFCOMMChannelRef() -> Unmanaged<IOBluetoothRFCOMMChannel>!     func closeChannel() -> IOReturn     func isOpen() -> Bool     func getMTU() -> BluetoothRFCOMMMTU     func isTransmissionPaused() -> Bool     func write(_ data: UnsafeMutablePointer<Void>, length length: UInt16, sleep sleep: Bool) -> IOReturn     func writeAsync(_ data: UnsafeMutablePointer<Void>, length length: UInt16, refcon refcon: UnsafeMutablePointer<Void>) -> IOReturn     func writeSync(_ data: UnsafeMutablePointer<Void>, length length: UInt16) -> IOReturn     func writeSimple(_ data: UnsafeMutablePointer<Void>, length length: UInt16, sleep sleep: Bool, bytesSent numBytesSent: UnsafeMutablePointer<UInt32>) -> IOReturn     func setSerialParameters(_ speed: UInt32, dataBits nBits: UInt8, parity parity: BluetoothRFCOMMParityType, stopBits bitStop: UInt8) -> IOReturn     func sendRemoteLineStatus(_ lineStatus: BluetoothRFCOMMLineStatus) -> IOReturn     func setDelegate(_ delegate: AnyObject!) -> IOReturn     func delegate() -> AnyObject!     func getChannelID() -> BluetoothRFCOMMChannelID     func isIncoming() -> Bool     func getDevice() -> IOBluetoothDevice!     func getObjectID() -> IOBluetoothObjectID     func registerForChannelCloseNotification(_ observer: AnyObject!, selector inSelector: Selector) -> IOBluetoothUserNotification! } ``` |
| To | ``` class IOBluetoothRFCOMMChannel : IOBluetoothObject, NSPortDelegate {     class func registerForChannelOpenNotifications(_ object: AnyObject!, selector selector: Selector) -> IOBluetoothUserNotification!     class func registerForChannelOpenNotifications(_ object: AnyObject!, selector selector: Selector, withChannelID channelID: BluetoothRFCOMMChannelID, direction inDirection: IOBluetoothUserNotificationChannelDirection) -> IOBluetoothUserNotification!     class func withRFCOMMChannelRef(_ rfcommChannelRef: IOBluetoothRFCOMMChannelRef!) -> Self!     class func withObjectID(_ objectID: IOBluetoothObjectID) -> Self!     func getRFCOMMChannelRef() -> Unmanaged<IOBluetoothRFCOMMChannelRef>!     func closeChannel() -> IOReturn     func isOpen() -> Bool     func getMTU() -> BluetoothRFCOMMMTU     func isTransmissionPaused() -> Bool     func write(_ data: UnsafeMutablePointer<Void>, length length: UInt16, sleep sleep: Bool) -> IOReturn     func writeAsync(_ data: UnsafeMutablePointer<Void>, length length: UInt16, refcon refcon: UnsafeMutablePointer<Void>) -> IOReturn     func writeSync(_ data: UnsafeMutablePointer<Void>, length length: UInt16) -> IOReturn     func writeSimple(_ data: UnsafeMutablePointer<Void>, length length: UInt16, sleep sleep: Bool, bytesSent numBytesSent: UnsafeMutablePointer<UInt32>) -> IOReturn     func setSerialParameters(_ speed: UInt32, dataBits nBits: UInt8, parity parity: BluetoothRFCOMMParityType, stopBits bitStop: UInt8) -> IOReturn     func sendRemoteLineStatus(_ lineStatus: BluetoothRFCOMMLineStatus) -> IOReturn     func setDelegate(_ delegate: AnyObject!) -> IOReturn     func delegate() -> AnyObject!     func getChannelID() -> BluetoothRFCOMMChannelID     func isIncoming() -> Bool     func getDevice() -> IOBluetoothDevice!     func getObjectID() -> IOBluetoothObjectID     func registerForChannelCloseNotification(_ observer: AnyObject!, selector inSelector: Selector) -> IOBluetoothUserNotification! } ``` |

Modified [IOBluetoothRFCOMMChannel.getRFCOMMChannelRef() -> Unmanaged<IOBluetoothRFCOMMChannelRef>!](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel/1434600-getref)

|  | Declaration |
| --- | --- |
| From | ``` func getRFCOMMChannelRef() -> Unmanaged<IOBluetoothRFCOMMChannel>! ``` |
| To | ``` func getRFCOMMChannelRef() -> Unmanaged<IOBluetoothRFCOMMChannelRef>! ``` |

Modified [IOBluetoothRFCOMMChannel.withRFCOMMChannelRef(_: IOBluetoothRFCOMMChannelRef!) -> Self! [class]](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel/1433571-withrfcommchannelref)

|  | Declaration |
| --- | --- |
| From | ``` class func withRFCOMMChannelRef(_ rfcommChannelRef: IOBluetoothRFCOMMChannel!) -> Self! ``` |
| To | ``` class func withRFCOMMChannelRef(_ rfcommChannelRef: IOBluetoothRFCOMMChannelRef!) -> Self! ``` |

Modified [IOBluetoothRFCOMMChannelRef](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannelref)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothRFCOMMChannelRef = IOBluetoothRFCOMMChannel ``` |
| To | ``` class IOBluetoothRFCOMMChannelRef { } ``` |

Modified [IOBluetoothSDPDataElement](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement)

|  | Declaration |
| --- | --- |
| From | ``` class IOBluetoothSDPDataElement : NSObject, NSCoding {     class func withElementValue(_ element: NSObject!) -> Self!     class func withType(_ type: BluetoothSDPDataElementTypeDescriptor, sizeDescriptor newSizeDescriptor: BluetoothSDPDataElementSizeDescriptor, size newSize: UInt32, value newValue: NSObject!) -> Self!     class func withSDPDataElementRef(_ sdpDataElementRef: IOBluetoothSDPDataElement!) -> Self!     init!(elementValue element: NSObject!)     init!(type newType: BluetoothSDPDataElementTypeDescriptor, sizeDescriptor newSizeDescriptor: BluetoothSDPDataElementSizeDescriptor, size newSize: UInt32, value newValue: NSObject!)     func getSDPDataElementRef() -> Unmanaged<IOBluetoothSDPDataElement>!     func getTypeDescriptor() -> BluetoothSDPDataElementTypeDescriptor     func getSizeDescriptor() -> BluetoothSDPDataElementSizeDescriptor     func getSize() -> UInt32     func getNumberValue() -> NSNumber!     func getDataValue() -> NSData!     func getStringValue() -> String!     func getArrayValue() -> [AnyObject]!     func getUUIDValue() -> IOBluetoothSDPUUID!     func getValue() -> NSObject!     func containsDataElement(_ dataElement: IOBluetoothSDPDataElement!) -> Bool     func containsValue(_ cmpValue: NSObject!) -> Bool } ``` |
| To | ``` class IOBluetoothSDPDataElement : NSObject, NSCoding {     class func withElementValue(_ element: NSObject!) -> Self!     class func withType(_ type: BluetoothSDPDataElementTypeDescriptor, sizeDescriptor newSizeDescriptor: BluetoothSDPDataElementSizeDescriptor, size newSize: UInt32, value newValue: NSObject!) -> Self!     class func withSDPDataElementRef(_ sdpDataElementRef: IOBluetoothSDPDataElementRef!) -> Self!     init!(elementValue element: NSObject!)     init!(type newType: BluetoothSDPDataElementTypeDescriptor, sizeDescriptor newSizeDescriptor: BluetoothSDPDataElementSizeDescriptor, size newSize: UInt32, value newValue: NSObject!)     func getSDPDataElementRef() -> Unmanaged<IOBluetoothSDPDataElementRef>!     func getTypeDescriptor() -> BluetoothSDPDataElementTypeDescriptor     func getSizeDescriptor() -> BluetoothSDPDataElementSizeDescriptor     func getSize() -> UInt32     func getNumberValue() -> NSNumber!     func getDataValue() -> NSData!     func getStringValue() -> String!     func getArrayValue() -> [AnyObject]!     func getUUIDValue() -> IOBluetoothSDPUUID!     func getValue() -> NSObject!     func containsDataElement(_ dataElement: IOBluetoothSDPDataElement!) -> Bool     func containsValue(_ cmpValue: NSObject!) -> Bool } ``` |

Modified [IOBluetoothSDPDataElement.getSDPDataElementRef() -> Unmanaged<IOBluetoothSDPDataElementRef>!](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/1396704-getref)

|  | Declaration |
| --- | --- |
| From | ``` func getSDPDataElementRef() -> Unmanaged<IOBluetoothSDPDataElement>! ``` |
| To | ``` func getSDPDataElementRef() -> Unmanaged<IOBluetoothSDPDataElementRef>! ``` |

Modified [IOBluetoothSDPDataElement.withSDPDataElementRef(_: IOBluetoothSDPDataElementRef!) -> Self! [class]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/1396687-withsdpdataelementref)

|  | Declaration |
| --- | --- |
| From | ``` class func withSDPDataElementRef(_ sdpDataElementRef: IOBluetoothSDPDataElement!) -> Self! ``` |
| To | ``` class func withSDPDataElementRef(_ sdpDataElementRef: IOBluetoothSDPDataElementRef!) -> Self! ``` |

Modified [IOBluetoothSDPDataElementRef](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelementref)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothSDPDataElementRef = IOBluetoothSDPDataElement ``` |
| To | ``` class IOBluetoothSDPDataElementRef { } ``` |

Modified [IOBluetoothSDPServiceRecord](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord)

|  | Declaration |
| --- | --- |
| From | ``` class IOBluetoothSDPServiceRecord : NSObject, NSCoding {     class func publishedServiceRecordWithDictionary(_ serviceDict: [NSObject : AnyObject]!) -> Self!     func removeServiceRecord() -> IOReturn     class func withServiceDictionary(_ serviceDict: [NSObject : AnyObject]!, device device: IOBluetoothDevice!) -> Self!     init!(serviceDictionary serviceDict: [NSObject : AnyObject]!, device device: IOBluetoothDevice!)     class func withSDPServiceRecordRef(_ sdpServiceRecordRef: IOBluetoothSDPServiceRecord!) -> Self!     func getSDPServiceRecordRef() -> Unmanaged<IOBluetoothSDPServiceRecord>!     var device: IOBluetoothDevice! { get }     func getDevice() -> IOBluetoothDevice!     var attributes: [NSObject : AnyObject]! { get }     func getAttributes() -> [NSObject : AnyObject]!     func getAttributeDataElement(_ attributeID: BluetoothSDPServiceAttributeID) -> IOBluetoothSDPDataElement!     func getServiceName() -> String!     func getRFCOMMChannelID(_ rfcommChannelID: UnsafeMutablePointer<BluetoothRFCOMMChannelID>) -> IOReturn     func getL2CAPPSM(_ outPSM: UnsafeMutablePointer<BluetoothL2CAPPSM>) -> IOReturn     func getServiceRecordHandle(_ outServiceRecordHandle: UnsafeMutablePointer<BluetoothSDPServiceRecordHandle>) -> IOReturn     func matchesUUID16(_ uuid16: BluetoothSDPUUID16) -> Bool     func matchesUUIDArray(_ uuidArray: [AnyObject]!) -> Bool     func matchesSearchArray(_ searchArray: [AnyObject]!) -> Bool     func hasServiceFromArray(_ array: [AnyObject]!) -> Bool     var sortedAttributes: [AnyObject]! { get } } extension IOBluetoothSDPServiceRecord {     func handsFreeSupportedFeatures() -> UInt16 } ``` |
| To | ``` class IOBluetoothSDPServiceRecord : NSObject, NSCoding {     class func publishedServiceRecordWithDictionary(_ serviceDict: [NSObject : AnyObject]!) -> Self!     func removeServiceRecord() -> IOReturn     class func withServiceDictionary(_ serviceDict: [NSObject : AnyObject]!, device device: IOBluetoothDevice!) -> Self!     init!(serviceDictionary serviceDict: [NSObject : AnyObject]!, device device: IOBluetoothDevice!)     class func withSDPServiceRecordRef(_ sdpServiceRecordRef: IOBluetoothSDPServiceRecordRef!) -> Self!     func getSDPServiceRecordRef() -> Unmanaged<IOBluetoothSDPServiceRecordRef>!     var device: IOBluetoothDevice! { get }     func getDevice() -> IOBluetoothDevice!     var attributes: [NSObject : AnyObject]! { get }     func getAttributes() -> [NSObject : AnyObject]!     func getAttributeDataElement(_ attributeID: BluetoothSDPServiceAttributeID) -> IOBluetoothSDPDataElement!     func getServiceName() -> String!     func getRFCOMMChannelID(_ rfcommChannelID: UnsafeMutablePointer<BluetoothRFCOMMChannelID>) -> IOReturn     func getL2CAPPSM(_ outPSM: UnsafeMutablePointer<BluetoothL2CAPPSM>) -> IOReturn     func getServiceRecordHandle(_ outServiceRecordHandle: UnsafeMutablePointer<BluetoothSDPServiceRecordHandle>) -> IOReturn     func matchesUUID16(_ uuid16: BluetoothSDPUUID16) -> Bool     func matchesUUIDArray(_ uuidArray: [AnyObject]!) -> Bool     func matchesSearchArray(_ searchArray: [AnyObject]!) -> Bool     func hasServiceFromArray(_ array: [AnyObject]!) -> Bool     var sortedAttributes: [AnyObject]! { get } } extension IOBluetoothSDPServiceRecord {     func handsFreeSupportedFeatures() -> UInt16 } ``` |

Modified [IOBluetoothSDPServiceRecord.getSDPServiceRecordRef() -> Unmanaged<IOBluetoothSDPServiceRecordRef>!](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/1429688-getref)

|  | Declaration |
| --- | --- |
| From | ``` func getSDPServiceRecordRef() -> Unmanaged<IOBluetoothSDPServiceRecord>! ``` |
| To | ``` func getSDPServiceRecordRef() -> Unmanaged<IOBluetoothSDPServiceRecordRef>! ``` |

Modified [IOBluetoothSDPServiceRecord.withSDPServiceRecordRef(_: IOBluetoothSDPServiceRecordRef!) -> Self! [class]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/1434716-withsdpservicerecordref)

|  | Declaration |
| --- | --- |
| From | ``` class func withSDPServiceRecordRef(_ sdpServiceRecordRef: IOBluetoothSDPServiceRecord!) -> Self! ``` |
| To | ``` class func withSDPServiceRecordRef(_ sdpServiceRecordRef: IOBluetoothSDPServiceRecordRef!) -> Self! ``` |

Modified [IOBluetoothSDPServiceRecordRef](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecordref)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothSDPServiceRecordRef = IOBluetoothSDPServiceRecord ``` |
| To | ``` class IOBluetoothSDPServiceRecordRef { } ``` |

Modified [IOBluetoothSDPUUID](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid)

|  | Declaration |
| --- | --- |
| From | ``` class IOBluetoothSDPUUID : NSData {     class func uuidWithBytes(_ bytes: UnsafePointer<Void>, length length: UInt32) -> Self!     class func uuidWithData(_ data: NSData!) -> Self!     class func uuid16(_ uuid16: BluetoothSDPUUID16) -> Self!     class func uuid32(_ uuid32: BluetoothSDPUUID32) -> Self!     class func withSDPUUIDRef(_ sdpUUIDRef: IOBluetoothSDPUUID!) -> Self!     init!(UUID16 uuid16: BluetoothSDPUUID16)     init!(UUID32 uuid32: BluetoothSDPUUID32)     func getSDPUUIDRef() -> Unmanaged<IOBluetoothSDPUUID>!     func getUUIDWithLength(_ newLength: UInt32) -> Self!     func isEqualToUUID(_ otherUUID: IOBluetoothSDPUUID!) -> Bool     func classForCoder() -> AnyClass!     func classForArchiver() -> AnyClass!     func classForPortCoder() -> AnyClass! } ``` |
| To | ``` class IOBluetoothSDPUUID : NSData {     class func uuidWithBytes(_ bytes: UnsafePointer<Void>, length length: UInt32) -> Self!     class func uuidWithData(_ data: NSData!) -> Self!     class func uuid16(_ uuid16: BluetoothSDPUUID16) -> Self!     class func uuid32(_ uuid32: BluetoothSDPUUID32) -> Self!     class func withSDPUUIDRef(_ sdpUUIDRef: IOBluetoothSDPUUIDRef!) -> Self!     init!(UUID16 uuid16: BluetoothSDPUUID16)     init!(UUID32 uuid32: BluetoothSDPUUID32)     func getSDPUUIDRef() -> Unmanaged<IOBluetoothSDPUUIDRef>!     func getUUIDWithLength(_ newLength: UInt32) -> Self!     func isEqualToUUID(_ otherUUID: IOBluetoothSDPUUID!) -> Bool     func classForCoder() -> AnyClass!     func classForArchiver() -> AnyClass!     func classForPortCoder() -> AnyClass! } ``` |

Modified [IOBluetoothSDPUUIDRef](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuidref)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothSDPUUIDRef = IOBluetoothSDPUUID ``` |
| To | ``` class IOBluetoothSDPUUIDRef { } ``` |

Modified [IOBluetoothUserNotificationRef](https://developer.apple.com/documentation/iobluetooth/iobluetoothusernotificationref)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothUserNotificationRef = IOBluetoothUserNotification ``` |
| To | ``` class IOBluetoothUserNotificationRef { } ``` |

Modified [OBEXSessionEvent [struct]](https://developer.apple.com/documentation/iobluetooth/obexsessionevent)

|  | Declaration |
| --- | --- |
| From | ``` struct OBEXSessionEvent {     var type: OBEXSessionEventType     var session: OBEXSessionRef     var refCon: UnsafeMutablePointer<Void>     var isEndOfEventData: DarwinBoolean     var reserved1: UnsafeMutablePointer<Void>     var reserved2: UnsafeMutablePointer<Void>     init() } ``` |
| To | ``` struct OBEXSessionEvent {     struct __Unnamed_union_u {         var connectCommandResponseData: OBEXConnectCommandResponseData         var disconnectCommandResponseData: OBEXDisconnectCommandResponseData         var putCommandResponseData: OBEXPutCommandResponseData         var getCommandResponseData: OBEXGetCommandResponseData         var setPathCommandResponseData: OBEXSetPathCommandResponseData         var abortCommandResponseData: OBEXAbortCommandResponseData         var connectCommandData: OBEXConnectCommandData         var disconnectCommandData: OBEXDisconnectCommandData         var putCommandData: OBEXPutCommandData         var getCommandData: OBEXGetCommandData         var setPathCommandData: OBEXSetPathCommandData         var abortCommandData: OBEXAbortCommandData         var errorData: OBEXErrorData         init(connectCommandResponseData connectCommandResponseData: OBEXConnectCommandResponseData)         init(disconnectCommandResponseData disconnectCommandResponseData: OBEXDisconnectCommandResponseData)         init(putCommandResponseData putCommandResponseData: OBEXPutCommandResponseData)         init(getCommandResponseData getCommandResponseData: OBEXGetCommandResponseData)         init(setPathCommandResponseData setPathCommandResponseData: OBEXSetPathCommandResponseData)         init(abortCommandResponseData abortCommandResponseData: OBEXAbortCommandResponseData)         init(connectCommandData connectCommandData: OBEXConnectCommandData)         init(disconnectCommandData disconnectCommandData: OBEXDisconnectCommandData)         init(putCommandData putCommandData: OBEXPutCommandData)         init(getCommandData getCommandData: OBEXGetCommandData)         init(setPathCommandData setPathCommandData: OBEXSetPathCommandData)         init(abortCommandData abortCommandData: OBEXAbortCommandData)         init(errorData errorData: OBEXErrorData)         init()     }     var type: OBEXSessionEventType     var session: OBEXSessionRef     var refCon: UnsafeMutablePointer<Void>     var isEndOfEventData: DarwinBoolean     var reserved1: UnsafeMutablePointer<Void>     var reserved2: UnsafeMutablePointer<Void>     var u: OBEXSessionEvent.__Unnamed_union_u     init()     init(type type: OBEXSessionEventType, session session: OBEXSessionRef, refCon refCon: UnsafeMutablePointer<Void>, isEndOfEventData isEndOfEventData: DarwinBoolean, reserved1 reserved1: UnsafeMutablePointer<Void>, reserved2 reserved2: UnsafeMutablePointer<Void>, u u: OBEXSessionEvent.__Unnamed_union_u) } ``` |

Modified [IOBluetoothDeviceRegisterForDisconnectNotification(_: IOBluetoothDeviceRef!, _: IOBluetoothUserNotificationCallback!, _: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotificationRef>!](https://developer.apple.com/documentation/iobluetooth/1431047-iobluetoothdeviceregisterfordisc)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothDeviceRegisterForDisconnectNotification(_ inDevice: IOBluetoothDevice!, _ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothDeviceRegisterForDisconnectNotification(_ inDevice: IOBluetoothDeviceRef!, _ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotificationRef>! ``` |

Modified [IOBluetoothIgnoreHIDDevice(_: IOBluetoothDeviceRef!)](https://developer.apple.com/documentation/iobluetooth/1433141-iobluetoothignorehiddevice)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothIgnoreHIDDevice(_ device: IOBluetoothDevice!) ``` |
| To | ``` func IOBluetoothIgnoreHIDDevice(_ device: IOBluetoothDeviceRef!) ``` |

Modified [IOBluetoothL2CAPChannelIncomingDataListener](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannelincomingdatalistener)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothL2CAPChannelIncomingDataListener = (IOBluetoothL2CAPChannel!, UnsafeMutablePointer<Void>, UInt16, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias IOBluetoothL2CAPChannelIncomingDataListener = (IOBluetoothL2CAPChannelRef!, UnsafeMutablePointer<Void>, UInt16, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [IOBluetoothL2CAPChannelIncomingEventListener](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannelincomingeventlistener)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothL2CAPChannelIncomingEventListener = (IOBluetoothL2CAPChannel!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<IOBluetoothL2CAPChannelEvent>) -> Void ``` |
| To | ``` typealias IOBluetoothL2CAPChannelIncomingEventListener = (IOBluetoothL2CAPChannelRef!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<IOBluetoothL2CAPChannelEvent>) -> Void ``` |

Modified [IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(_: IOBluetoothL2CAPChannelRef!, _: IOBluetoothUserNotificationCallback!, _: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotificationRef>!](https://developer.apple.com/documentation/iobluetooth/1430069-iobluetoothl2capchannelregisterf)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(_ channel: IOBluetoothL2CAPChannel!, _ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(_ channel: IOBluetoothL2CAPChannelRef!, _ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotificationRef>! ``` |

Modified [IOBluetoothRegisterForDeviceConnectNotifications(_: IOBluetoothUserNotificationCallback!, _: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotificationRef>!](https://developer.apple.com/documentation/iobluetooth/1432361-iobluetoothregisterfordeviceconn)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRegisterForDeviceConnectNotifications(_ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothRegisterForDeviceConnectNotifications(_ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotificationRef>! ``` |

Modified [IOBluetoothRegisterForFilteredL2CAPChannelOpenNotifications(_: IOBluetoothUserNotificationCallback!, _: UnsafeMutablePointer<Void>, _: BluetoothL2CAPPSM, _: IOBluetoothUserNotificationChannelDirection) -> Unmanaged<IOBluetoothUserNotificationRef>!](https://developer.apple.com/documentation/iobluetooth/1431179-iobluetoothregisterforfilteredl2)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRegisterForFilteredL2CAPChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>, _ inPSM: BluetoothL2CAPPSM, _ inDirection: IOBluetoothUserNotificationChannelDirection) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothRegisterForFilteredL2CAPChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>, _ inPSM: BluetoothL2CAPPSM, _ inDirection: IOBluetoothUserNotificationChannelDirection) -> Unmanaged<IOBluetoothUserNotificationRef>! ``` |

Modified [IOBluetoothRegisterForFilteredRFCOMMChannelOpenNotifications(_: IOBluetoothUserNotificationCallback!, _: UnsafeMutablePointer<Void>, _: BluetoothRFCOMMChannelID, _: IOBluetoothUserNotificationChannelDirection) -> Unmanaged<IOBluetoothUserNotificationRef>!](https://developer.apple.com/documentation/iobluetooth/1428798-iobluetoothregisterforfilteredrf)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRegisterForFilteredRFCOMMChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>, _ channelID: BluetoothRFCOMMChannelID, _ inDirection: IOBluetoothUserNotificationChannelDirection) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothRegisterForFilteredRFCOMMChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>, _ channelID: BluetoothRFCOMMChannelID, _ inDirection: IOBluetoothUserNotificationChannelDirection) -> Unmanaged<IOBluetoothUserNotificationRef>! ``` |

Modified [IOBluetoothRegisterForL2CAPChannelOpenNotifications(_: IOBluetoothUserNotificationCallback!, _: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotificationRef>!](https://developer.apple.com/documentation/iobluetooth/1434362-iobluetoothregisterforl2capchann)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRegisterForL2CAPChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothRegisterForL2CAPChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotificationRef>! ``` |

Modified [IOBluetoothRegisterForRFCOMMChannelOpenNotifications(_: IOBluetoothUserNotificationCallback!, _: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotificationRef>!](https://developer.apple.com/documentation/iobluetooth/1430329-iobluetoothregisterforrfcommchan)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRegisterForRFCOMMChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothRegisterForRFCOMMChannelOpenNotifications(_ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotificationRef>! ``` |

Modified [IOBluetoothRemoveIgnoredHIDDevice(_: IOBluetoothDeviceRef!)](https://developer.apple.com/documentation/iobluetooth/1429363-iobluetoothremoveignoredhiddevic)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRemoveIgnoredHIDDevice(_ device: IOBluetoothDevice!) ``` |
| To | ``` func IOBluetoothRemoveIgnoredHIDDevice(_ device: IOBluetoothDeviceRef!) ``` |

Modified [IOBluetoothRFCOMMChannelRegisterForChannelCloseNotification(_: IOBluetoothRFCOMMChannelRef!, _: IOBluetoothUserNotificationCallback!, _: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotificationRef>!](https://developer.apple.com/documentation/iobluetooth/1430321-iobluetoothrfcommchannelregister)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothRFCOMMChannelRegisterForChannelCloseNotification(_ inChannel: IOBluetoothRFCOMMChannel!, _ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotification>! ``` |
| To | ``` func IOBluetoothRFCOMMChannelRegisterForChannelCloseNotification(_ inChannel: IOBluetoothRFCOMMChannelRef!, _ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<IOBluetoothUserNotificationRef>! ``` |

Modified [IOBluetoothUserNotificationCallback](https://developer.apple.com/documentation/iobluetooth/iobluetoothusernotificationcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothUserNotificationCallback = (UnsafeMutablePointer<Void>, IOBluetoothUserNotification!, IOBluetoothObject!) -> Void ``` |
| To | ``` typealias IOBluetoothUserNotificationCallback = (UnsafeMutablePointer<Void>, IOBluetoothUserNotificationRef!, IOBluetoothObjectRef!) -> Void ``` |

Modified [IOBluetoothUserNotificationUnregister(_: IOBluetoothUserNotificationRef!)](https://developer.apple.com/documentation/iobluetooth/1431781-iobluetoothusernotificationunreg)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothUserNotificationUnregister(_ notificationRef: IOBluetoothUserNotification!) ``` |
| To | ``` func IOBluetoothUserNotificationUnregister(_ notificationRef: IOBluetoothUserNotificationRef!) ``` |

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
