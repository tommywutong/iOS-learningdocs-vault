---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/IOBluetooth.html
archived_at: '2026-07-15T07:34:46.196464Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# IOBluetooth Changes

## IOBluetooth

Bluetooth.hAdded [BluetoothHCIEventLEConnectionUpdateCompleteResults](https://developer.apple.com/documentation/kernel/bluetoothhcieventleconnectionupdatecompleteresults)Added [BluetoothLEAddressType](https://developer.apple.com/documentation/kernel/bluetoothleaddresstype)Added [BluetoothLEAddressTypePublic](https://developer.apple.com/documentation/iobluetooth/bluetoothleaddresstype/bluetoothleaddresstypepublic)Added [BluetoothLEAddressTypeRandom](https://developer.apple.com/documentation/kernel/bluetoothleaddresstype/bluetoothleaddresstyperandom)Added [BluetoothLEAdvertisingType](https://developer.apple.com/documentation/kernel/bluetoothleadvertisingtype)Added [BluetoothLEAdvertisingTypeConnectableDirected](https://developer.apple.com/documentation/kernel/bluetoothleadvertisingtype/bluetoothleadvertisingtypeconnectabledirected)Added [BluetoothLEAdvertisingTypeConnectableUndirected](https://developer.apple.com/documentation/iobluetooth/bluetoothleadvertisingtype/bluetoothleadvertisingtypeconnectableundirected)Added [BluetoothLEAdvertisingTypeDiscoverableUndirected](https://developer.apple.com/documentation/kernel/bluetoothleadvertisingtype/bluetoothleadvertisingtypediscoverableundirected)Added [BluetoothLEAdvertisingTypeNonConnectableUndirected](https://developer.apple.com/documentation/kernel/bluetoothleadvertisingtype/bluetoothleadvertisingtypenonconnectableundirected)Added [BluetoothLEAdvertisingTypeScanResponse](https://developer.apple.com/documentation/kernel/bluetoothleadvertisingtype/bluetoothleadvertisingtypescanresponse)Added [BluetoothLEScan](https://developer.apple.com/documentation/kernel/bluetoothlescan)Added [BluetoothLEScanDisable](https://developer.apple.com/documentation/iobluetooth/bluetoothlescan/bluetoothlescandisable)Added [BluetoothLEScanDuplicateFilter](https://developer.apple.com/documentation/iobluetooth/bluetoothlescanduplicatefilter)Added [BluetoothLEScanDuplicateFilterDisable](https://developer.apple.com/documentation/kernel/bluetoothlescanduplicatefilter/bluetoothlescanduplicatefilterdisable)Added [BluetoothLEScanDuplicateFilterEnable](https://developer.apple.com/documentation/kernel/bluetoothlescanduplicatefilter/bluetoothlescanduplicatefilterenable)Added [BluetoothLEScanEnable](https://developer.apple.com/documentation/kernel/bluetoothlescan/bluetoothlescanenable)Added [BluetoothLEScanFilter](https://developer.apple.com/documentation/iobluetooth/bluetoothlescanfilter)Added [BluetoothLEScanFilterNone](https://developer.apple.com/documentation/iobluetooth/bluetoothlescanfilter/bluetoothlescanfilternone)Added [BluetoothLEScanFilterWhitelist](https://developer.apple.com/documentation/kernel/bluetoothlescanfilter/bluetoothlescanfilterwhitelist)Added [BluetoothLEScanType](https://developer.apple.com/documentation/iobluetooth/bluetoothlescantype)Added [BluetoothLEScanTypeActive](https://developer.apple.com/documentation/kernel/bluetoothlescantype/bluetoothlescantypeactive)Added [BluetoothLEScanTypePassive](https://developer.apple.com/documentation/iobluetooth/bluetoothlescantype/bluetoothlescantypepassive)Added [kBluetoothEncryptionEnableBREDRAESCCM](https://developer.apple.com/documentation/iobluetooth/kbluetoothencryptionenablebredraesccm)Added [kBluetoothEncryptionEnableBREDRE0](https://developer.apple.com/documentation/kernel/1640012-anonymous/kbluetoothencryptionenablebredre0)Added [kBluetoothEncryptionEnableLEAESCCM](https://developer.apple.com/documentation/iobluetooth/1489342-anonymous/kbluetoothencryptionenableleaesccm)Added [kBluetoothL2CAPChannelLEAP](https://developer.apple.com/documentation/kernel/1640028-anonymous/kbluetoothl2capchannelleap)Added [kBluetoothL2CAPChannelLEAS](https://developer.apple.com/documentation/kernel/1640028-anonymous/kbluetoothl2capchannelleas)Added [kBluetoothL2CAPChannelMagnet](https://developer.apple.com/documentation/kernel/1640028-anonymous/kbluetoothl2capchannelmagnet)Added [kBluetoothL2CAPCommandCodeLECreditBasedConnectionRequest](https://developer.apple.com/documentation/kernel/bluetoothl2capcommandcode/kbluetoothl2capcommandcodelecreditbasedconnectionrequest)Added [kBluetoothL2CAPCommandCodeLECreditBasedConnectionResponse](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capcommandcode/kbluetoothl2capcommandcodelecreditbasedconnectionresponse)Added [kBluetoothL2CAPCommandCodeLEFlowControlCredit](https://developer.apple.com/documentation/iobluetooth/kbluetoothl2capcommandcodeleflowcontrolcredit)Added [kBluetoothLESecurityManagerCommandCodePairingDHKeyCheck](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanagercommandcodepairingdhkeycheck)Added [kBluetoothLESecurityManagerCommandCodePairingKeypressNotification](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagercommandcode/kbluetoothlesecuritymanagercommandcodepairingkeypressnotification)Added [kBluetoothLESecurityManagerCommandCodePairingPublicKey](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanagercommandcodepairingpublickey)Added [kBluetoothLESecurityManagerReasonCodeDHKeyCheckFailed](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerpairingfailedreasoncode/kbluetoothlesecuritymanagerreasoncodedhkeycheckfailed)Added [kBluetoothLESecurityManagerReasonCodeNumericComparisonFailed](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerpairingfailedreasoncode/kbluetoothlesecuritymanagerreasoncodenumericcomparisonfailed)Added [kBluetoothTransportTypeUART](https://developer.apple.com/documentation/iobluetooth/kbluetoothtransporttypeuart)CBATTRequest.h (Removed)CBAdvertisementData.h (Removed)CBCentral.h (Removed)CBCentralManager.h (Removed)CBCentralManagerConstants.h (Removed)CBCharacteristic.h (Removed)CBDefines.h (Removed)CBDescriptor.h (Removed)CBError.h (Removed)CBPeripheral.h (Removed)CBPeripheralManager.h (Removed)CBPeripheralManagerConstants.h (Removed)CBService.h (Removed)CBUUID.h (Removed)CoreBluetooth.h (Removed)objc/IOBluetoothDevice.hModified [+[IOBluetoothDevice deviceWithAddress:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1434863-init)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothDevice *)deviceWithAddress:(const BluetoothDeviceAddress *)address ``` |
| To | ``` + (instancetype)deviceWithAddress:(const BluetoothDeviceAddress *)address ``` |

Modified [+[IOBluetoothDevice deviceWithAddressString:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1434342-init)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothDevice *)deviceWithAddressString:(NSString *)address ``` |
| To | ``` + (instancetype)deviceWithAddressString:(NSString *)address ``` |

Modified [+[IOBluetoothDevice withAddress:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1589898-withaddress)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothDevice *)withAddress:(const BluetoothDeviceAddress *)address ``` |
| To | ``` + (instancetype)withAddress:(const BluetoothDeviceAddress *)address ``` |

Modified [+[IOBluetoothDevice withDeviceRef:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1589902-withdeviceref)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothDevice *)withDeviceRef:(IOBluetoothDeviceRef)deviceRef ``` |
| To | ``` + (instancetype)withDeviceRef:(IOBluetoothDeviceRef)deviceRef ``` |

objc/IOBluetoothDeviceInquiry.hModified [-[IOBluetoothDeviceInquiry initWithDelegate:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquiry/1423401-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDelegate:(id)delegate ``` |
| To | ``` - (instancetype)initWithDelegate:(id)delegate ``` |

Modified [+[IOBluetoothDeviceInquiry inquiryWithDelegate:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquiry/1423421-inquirywithdelegate)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothDeviceInquiry *)inquiryWithDelegate:(id)delegate ``` |
| To | ``` + (instancetype)inquiryWithDelegate:(id)delegate ``` |

Modified [-[IOBluetoothDeviceInquiryDelegate deviceInquiryComplete:error:aborted:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate/1423409-deviceinquirycomplete)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothDeviceInquiryDelegate deviceInquiryDeviceFound:device:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate/1423415-deviceinquirydevicefound)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothDeviceInquiryDelegate deviceInquiryDeviceNameUpdated:device:devicesRemaining:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate/1423429-deviceinquirydevicenameupdated)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothDeviceInquiryDelegate deviceInquiryStarted:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate/1423405-deviceinquirystarted)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothDeviceInquiryDelegate deviceInquiryUpdatingDeviceNamesStarted:devicesRemaining:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate/1423425-deviceinquiryupdatingdevicenames)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

objc/IOBluetoothDevicePair.hModified [+[IOBluetoothDevicePair pairWithDevice:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepair/1429730-pairwithdevice)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothDevicePair *)pairWithDevice:(IOBluetoothDevice *)device ``` |
| To | ``` + (instancetype)pairWithDevice:(IOBluetoothDevice *)device ``` |

Modified [-[IOBluetoothDevicePairDelegate devicePairingConnecting:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepairdelegate/1432152-devicepairingconnecting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothDevicePairDelegate devicePairingFinished:error:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepairdelegate/1434609-devicepairingfinished)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothDevicePairDelegate devicePairingPINCodeRequest:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepairdelegate/1432539-devicepairingpincoderequest)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothDevicePairDelegate devicePairingStarted:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepairdelegate/1431489-devicepairingstarted)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothDevicePairDelegate devicePairingUserConfirmationRequest:numericValue:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepairdelegate/1431902-devicepairinguserconfirmationreq)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothDevicePairDelegate devicePairingUserPasskeyNotification:passkey:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepairdelegate/1432500-devicepairinguserpasskeynotifica)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothDevicePairDelegate deviceSimplePairingComplete:status:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepairdelegate/1429233-devicesimplepairingcomplete)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

objc/IOBluetoothHandsFree.hModified [-[IOBluetoothHandsFree initWithDevice:delegate:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427916-initwithdevice)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDevice:(IOBluetoothDevice *)device delegate:(id<IOBluetoothHandsFreeDelegate>)inDelegate ``` |
| To | ``` - (instancetype)initWithDevice:(IOBluetoothDevice *)device delegate:(id<IOBluetoothHandsFreeDelegate>)inDelegate ``` |

Modified [-[IOBluetoothHandsFreeDelegate handsFree:connected:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedelegate/1427880-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothHandsFreeDelegate handsFree:disconnected:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedelegate/1427728-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothHandsFreeDelegate handsFree:scoConnectionClosed:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedelegate/1427824-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothHandsFreeDelegate handsFree:scoConnectionOpened:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedelegate/1427868-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

objc/IOBluetoothHandsFreeAudioGateway.hModified [-[IOBluetoothHandsFreeAudioGateway initWithDevice:delegate:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogateway/1428663-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDevice:(IOBluetoothDevice *)device delegate:(id)inDelegate ``` |
| To | ``` - (instancetype)initWithDevice:(IOBluetoothDevice *)device delegate:(id)inDelegate ``` |

Modified [-[IOBluetoothHandsFreeAudioGatewayDelegate handsFree:hangup:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewaydelegate/1433943-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothHandsFreeAudioGatewayDelegate handsFree:redial:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewaydelegate/1433563-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

objc/IOBluetoothHandsFreeDevice.hModified [-[IOBluetoothHandsFreeDevice initWithDevice:delegate:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/1428834-initwithdevice)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDevice:(IOBluetoothDevice *)device delegate:(id)delegate ``` |
| To | ``` - (instancetype)initWithDevice:(IOBluetoothDevice *)device delegate:(id)delegate ``` |

Modified [-[IOBluetoothHandsFreeDeviceDelegate handsFree:batteryCharge:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1428496-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothHandsFreeDeviceDelegate handsFree:callHoldState:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1433981-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothHandsFreeDeviceDelegate handsFree:callSetupMode:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1429223-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothHandsFreeDeviceDelegate handsFree:currentCall:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1432883-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothHandsFreeDeviceDelegate handsFree:incomingCallFrom:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1429210-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothHandsFreeDeviceDelegate handsFree:incomingSMS:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1430510-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothHandsFreeDeviceDelegate handsFree:isCallActive:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1431339-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothHandsFreeDeviceDelegate handsFree:isRoaming:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1431758-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothHandsFreeDeviceDelegate handsFree:isServiceAvailable:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1433100-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothHandsFreeDeviceDelegate handsFree:ringAttempt:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1431746-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothHandsFreeDeviceDelegate handsFree:signalStrength:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1432799-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothHandsFreeDeviceDelegate handsFree:subscriberNumber:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1430067-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothHandsFreeDeviceDelegate handsFree:unhandledResultCode:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/1433815-handsfree)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

objc/IOBluetoothHostController.hModified [+[IOBluetoothHostController defaultController]](https://developer.apple.com/documentation/iobluetooth/iobluetoothhostcontroller/1433496-default)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothHostController *)defaultController ``` |
| To | ``` + (instancetype)defaultController ``` |

objc/IOBluetoothL2CAPChannel.hModified [+[IOBluetoothL2CAPChannel withObjectID:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/1433768-withobjectid)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothL2CAPChannel *)withObjectID:(IOBluetoothObjectID)objectID ``` |
| To | ``` + (instancetype)withObjectID:(IOBluetoothObjectID)objectID ``` |

Modified [-[IOBluetoothL2CAPChannelDelegate l2capChannelClosed:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchanneldelegate/1433766-l2capchannelclosed)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothL2CAPChannelDelegate l2capChannelData:data:length:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchanneldelegate/1431868-l2capchanneldata)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothL2CAPChannelDelegate l2capChannelOpenComplete:status:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchanneldelegate/1430363-l2capchannelopencomplete)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothL2CAPChannelDelegate l2capChannelQueueSpaceAvailable:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchanneldelegate/1431728-l2capchannelqueuespaceavailable)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothL2CAPChannelDelegate l2capChannelReconfigured:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchanneldelegate/1428740-l2capchannelreconfigured)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothL2CAPChannelDelegate l2capChannelWriteComplete:refcon:status:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchanneldelegate/1431099-l2capchannelwritecomplete)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

objc/IOBluetoothOBEXSession.hModified [-[IOBluetoothOBEXSession initWithDevice:channelID:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/1429922-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDevice:(IOBluetoothDevice *)inDevice channelID:(BluetoothRFCOMMChannelID)inChannelID ``` |
| To | ``` - (instancetype)initWithDevice:(IOBluetoothDevice *)inDevice channelID:(BluetoothRFCOMMChannelID)inChannelID ``` |

Modified [-[IOBluetoothOBEXSession initWithIncomingRFCOMMChannel:eventSelector:selectorTarget:refCon:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/1431317-initwithincomingrfcommchannel)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithIncomingRFCOMMChannel:(IOBluetoothRFCOMMChannel *)inChannel eventSelector:(SEL)inEventSelector selectorTarget:(id)inEventSelectorTarget refCon:(void *)inUserRefCon ``` |
| To | ``` - (instancetype)initWithIncomingRFCOMMChannel:(IOBluetoothRFCOMMChannel *)inChannel eventSelector:(SEL)inEventSelector selectorTarget:(id)inEventSelectorTarget refCon:(void *)inUserRefCon ``` |

Modified [-[IOBluetoothOBEXSession initWithSDPServiceRecord:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/1429196-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithSDPServiceRecord:(IOBluetoothSDPServiceRecord *)inSDPServiceRecord ``` |
| To | ``` - (instancetype)initWithSDPServiceRecord:(IOBluetoothSDPServiceRecord *)inSDPServiceRecord ``` |

Modified [+[IOBluetoothOBEXSession withDevice:channelID:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/1432953-withdevice)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothOBEXSession *)withDevice:(IOBluetoothDevice *)inDevice channelID:(BluetoothRFCOMMChannelID)inRFCOMMChannelID ``` |
| To | ``` + (instancetype)withDevice:(IOBluetoothDevice *)inDevice channelID:(BluetoothRFCOMMChannelID)inRFCOMMChannelID ``` |

Modified [+[IOBluetoothOBEXSession withIncomingRFCOMMChannel:eventSelector:selectorTarget:refCon:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/1431248-withincomingrfcommchannel)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothOBEXSession *)withIncomingRFCOMMChannel:(IOBluetoothRFCOMMChannel *)inChannel eventSelector:(SEL)inEventSelector selectorTarget:(id)inEventSelectorTarget refCon:(void *)inUserRefCon ``` |
| To | ``` + (instancetype)withIncomingRFCOMMChannel:(IOBluetoothRFCOMMChannel *)inChannel eventSelector:(SEL)inEventSelector selectorTarget:(id)inEventSelectorTarget refCon:(void *)inUserRefCon ``` |

Modified [+[IOBluetoothOBEXSession withSDPServiceRecord:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/1431979-withsdpservicerecord)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothOBEXSession *)withSDPServiceRecord:(IOBluetoothSDPServiceRecord *)inSDPServiceRecord ``` |
| To | ``` + (instancetype)withSDPServiceRecord:(IOBluetoothSDPServiceRecord *)inSDPServiceRecord ``` |

objc/IOBluetoothRFCOMMChannel.hModified [+[IOBluetoothRFCOMMChannel withObjectID:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel/1430561-withobjectid)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothRFCOMMChannel *)withObjectID:(IOBluetoothObjectID)objectID ``` |
| To | ``` + (instancetype)withObjectID:(IOBluetoothObjectID)objectID ``` |

Modified [+[IOBluetoothRFCOMMChannel withRFCOMMChannelRef:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel/1433571-withrfcommchannelref)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothRFCOMMChannel *)withRFCOMMChannelRef:(IOBluetoothRFCOMMChannelRef)rfcommChannelRef ``` |
| To | ``` + (instancetype)withRFCOMMChannelRef:(IOBluetoothRFCOMMChannelRef)rfcommChannelRef ``` |

Modified [-[IOBluetoothRFCOMMChannelDelegate rfcommChannelClosed:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchanneldelegate/1434518-rfcommchannelclosed)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothRFCOMMChannelDelegate rfcommChannelControlSignalsChanged:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchanneldelegate/1429160-rfcommchannelcontrolsignalschang)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothRFCOMMChannelDelegate rfcommChannelData:data:length:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchanneldelegate/1431822-rfcommchanneldata)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothRFCOMMChannelDelegate rfcommChannelFlowControlChanged:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchanneldelegate/1430179-rfcommchannelflowcontrolchanged)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothRFCOMMChannelDelegate rfcommChannelOpenComplete:status:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchanneldelegate/1429633-rfcommchannelopencomplete)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothRFCOMMChannelDelegate rfcommChannelQueueSpaceAvailable:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchanneldelegate/1429752-rfcommchannelqueuespaceavailable)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[IOBluetoothRFCOMMChannelDelegate rfcommChannelWriteComplete:refcon:status:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchanneldelegate/1434978-rfcommchannelwritecomplete)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

objc/IOBluetoothSDPDataElement.hModified [-[IOBluetoothSDPDataElement initWithElementValue:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/1396701-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithElementValue:(NSObject *)element ``` |
| To | ``` - (instancetype)initWithElementValue:(NSObject *)element ``` |

Modified [-[IOBluetoothSDPDataElement initWithType:sizeDescriptor:size:value:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/1396719-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithType:(BluetoothSDPDataElementTypeDescriptor)newType sizeDescriptor:(BluetoothSDPDataElementSizeDescriptor)newSizeDescriptor size:(uint32_t)newSize value:(NSObject *)newValue ``` |
| To | ``` - (instancetype)initWithType:(BluetoothSDPDataElementTypeDescriptor)newType sizeDescriptor:(BluetoothSDPDataElementSizeDescriptor)newSizeDescriptor size:(uint32_t)newSize value:(NSObject *)newValue ``` |

Modified [+[IOBluetoothSDPDataElement withElementValue:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/1396721-withelementvalue)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothSDPDataElement *)withElementValue:(NSObject *)element ``` |
| To | ``` + (instancetype)withElementValue:(NSObject *)element ``` |

Modified [+[IOBluetoothSDPDataElement withSDPDataElementRef:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/1396687-withsdpdataelementref)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothSDPDataElement *)withSDPDataElementRef:(IOBluetoothSDPDataElementRef)sdpDataElementRef ``` |
| To | ``` + (instancetype)withSDPDataElementRef:(IOBluetoothSDPDataElementRef)sdpDataElementRef ``` |

Modified [+[IOBluetoothSDPDataElement withType:sizeDescriptor:size:value:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/1396706-withtype)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothSDPDataElement *)withType:(BluetoothSDPDataElementTypeDescriptor)type sizeDescriptor:(BluetoothSDPDataElementSizeDescriptor)newSizeDescriptor size:(uint32_t)newSize value:(NSObject *)newValue ``` |
| To | ``` + (instancetype)withType:(BluetoothSDPDataElementTypeDescriptor)type sizeDescriptor:(BluetoothSDPDataElementSizeDescriptor)newSizeDescriptor size:(uint32_t)newSize value:(NSObject *)newValue ``` |

objc/IOBluetoothSDPServiceAttribute.hModified [-[IOBluetoothSDPServiceAttribute initWithID:attributeElement:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpserviceattribute/1434496-initwithid)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithID:(BluetoothSDPServiceAttributeID)newAttributeID attributeElement:(IOBluetoothSDPDataElement *)attributeElement ``` |
| To | ``` - (instancetype)initWithID:(BluetoothSDPServiceAttributeID)newAttributeID attributeElement:(IOBluetoothSDPDataElement *)attributeElement ``` |

Modified [-[IOBluetoothSDPServiceAttribute initWithID:attributeElementValue:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpserviceattribute/1434660-initwithid)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithID:(BluetoothSDPServiceAttributeID)newAttributeID attributeElementValue:(NSObject *)attributeElementValue ``` |
| To | ``` - (instancetype)initWithID:(BluetoothSDPServiceAttributeID)newAttributeID attributeElementValue:(NSObject *)attributeElementValue ``` |

Modified [+[IOBluetoothSDPServiceAttribute withID:attributeElement:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpserviceattribute/1431154-withid)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothSDPServiceAttribute *)withID:(BluetoothSDPServiceAttributeID)newAttributeID attributeElement:(IOBluetoothSDPDataElement *)attributeElement ``` |
| To | ``` + (instancetype)withID:(BluetoothSDPServiceAttributeID)newAttributeID attributeElement:(IOBluetoothSDPDataElement *)attributeElement ``` |

Modified [+[IOBluetoothSDPServiceAttribute withID:attributeElementValue:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpserviceattribute/1430305-withid)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothSDPServiceAttribute *)withID:(BluetoothSDPServiceAttributeID)newAttributeID attributeElementValue:(NSObject *)attributeElementValue ``` |
| To | ``` + (instancetype)withID:(BluetoothSDPServiceAttributeID)newAttributeID attributeElementValue:(NSObject *)attributeElementValue ``` |

objc/IOBluetoothSDPServiceRecord.hModified [-[IOBluetoothSDPServiceRecord initWithServiceDictionary:device:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/1431493-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithServiceDictionary:(NSDictionary *)serviceDict device:(IOBluetoothDevice *)device ``` |
| To | ``` - (instancetype)initWithServiceDictionary:(NSDictionary *)serviceDict device:(IOBluetoothDevice *)device ``` |

Modified [+[IOBluetoothSDPServiceRecord publishedServiceRecordWithDictionary:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/1430450-publishedservicerecord)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothSDPServiceRecord *)publishedServiceRecordWithDictionary:(NSDictionary *)serviceDict ``` |
| To | ``` + (instancetype)publishedServiceRecordWithDictionary:(NSDictionary *)serviceDict ``` |

Modified [+[IOBluetoothSDPServiceRecord withSDPServiceRecordRef:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/1434716-withsdpservicerecordref)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothSDPServiceRecord *)withSDPServiceRecordRef:(IOBluetoothSDPServiceRecordRef)sdpServiceRecordRef ``` |
| To | ``` + (instancetype)withSDPServiceRecordRef:(IOBluetoothSDPServiceRecordRef)sdpServiceRecordRef ``` |

Modified [+[IOBluetoothSDPServiceRecord withServiceDictionary:device:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/1435073-withservicedictionary)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothSDPServiceRecord *)withServiceDictionary:(NSDictionary *)serviceDict device:(IOBluetoothDevice *)device ``` |
| To | ``` + (instancetype)withServiceDictionary:(NSDictionary *)serviceDict device:(IOBluetoothDevice *)device ``` |

objc/IOBluetoothSDPUUID.hModified [-[IOBluetoothSDPUUID getUUIDWithLength:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid/1434307-getwithlength)

|  | Declaration |
| --- | --- |
| From | ``` - (IOBluetoothSDPUUID *)getUUIDWithLength:(unsigned int)newLength ``` |
| To | ``` - (instancetype)getUUIDWithLength:(unsigned int)newLength ``` |

Modified [-[IOBluetoothSDPUUID initWithUUID16:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid/1431398-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithUUID16:(BluetoothSDPUUID16)uuid16 ``` |
| To | ``` - (instancetype)initWithUUID16:(BluetoothSDPUUID16)uuid16 ``` |

Modified [-[IOBluetoothSDPUUID initWithUUID32:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid/1430416-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithUUID32:(BluetoothSDPUUID32)uuid32 ``` |
| To | ``` - (instancetype)initWithUUID32:(BluetoothSDPUUID32)uuid32 ``` |

Modified [+[IOBluetoothSDPUUID uuid16:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid/1433610-uuid16)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothSDPUUID *)uuid16:(BluetoothSDPUUID16)uuid16 ``` |
| To | ``` + (instancetype)uuid16:(BluetoothSDPUUID16)uuid16 ``` |

Modified [+[IOBluetoothSDPUUID uuid32:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid/1429154-uuid32)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothSDPUUID *)uuid32:(BluetoothSDPUUID32)uuid32 ``` |
| To | ``` + (instancetype)uuid32:(BluetoothSDPUUID32)uuid32 ``` |

Modified [+[IOBluetoothSDPUUID uuidWithBytes:length:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid/1428320-uuidwithbytes)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothSDPUUID *)uuidWithBytes:(const void *)bytes length:(unsigned int)length ``` |
| To | ``` + (instancetype)uuidWithBytes:(const void *)bytes length:(unsigned int)length ``` |

Modified [+[IOBluetoothSDPUUID uuidWithData:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid/1433987-init)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothSDPUUID *)uuidWithData:(NSData *)data ``` |
| To | ``` + (instancetype)uuidWithData:(NSData *)data ``` |

Modified [+[IOBluetoothSDPUUID withSDPUUIDRef:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid/1434302-withsdpuuidref)

|  | Declaration |
| --- | --- |
| From | ``` + (IOBluetoothSDPUUID *)withSDPUUIDRef:(IOBluetoothSDPUUIDRef)sdpUUIDRef ``` |
| To | ``` + (instancetype)withSDPUUIDRef:(IOBluetoothSDPUUIDRef)sdpUUIDRef ``` |

IOBluetoothUtilities.hAdded [IOBluetoothNSStringFromDeviceAddressColon()](https://developer.apple.com/documentation/iobluetooth/1428569-iobluetoothnsstringfromdeviceadd)objc/NSDictionaryOBEXExtensions.hModified [+[NSMutableDictionary dictionaryWithOBEXHeadersData:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1428433-dictionarywithobexheadersdata)

|  | Declaration |
| --- | --- |
| From | ``` + (NSMutableDictionary *)dictionaryWithOBEXHeadersData:(NSData *)inHeadersData ``` |
| To | ``` + (instancetype)dictionaryWithOBEXHeadersData:(NSData *)inHeadersData ``` |

Modified [+[NSMutableDictionary dictionaryWithOBEXHeadersData:headersDataSize:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1429768-dictionarywithobexheadersdata)

|  | Declaration |
| --- | --- |
| From | ``` + (NSMutableDictionary *)dictionaryWithOBEXHeadersData:(const void *)inHeadersData headersDataSize:(size_t)inDataSize ``` |
| To | ``` + (instancetype)dictionaryWithOBEXHeadersData:(const void *)inHeadersData headersDataSize:(size_t)inDataSize ``` |

Modified [+[NSMutableDictionary withOBEXHeadersData:headersDataSize:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1458889-withobexheadersdata)

|  | Declaration |
| --- | --- |
| From | ``` + (NSMutableDictionary *)withOBEXHeadersData:(const void *)inHeadersData headersDataSize:(size_t)inDataSize ``` |
| To | ``` + (instancetype)withOBEXHeadersData:(const void *)inHeadersData headersDataSize:(size_t)inDataSize ``` |

OBEX.hModified [OBEXSessionAbort()](https://developer.apple.com/documentation/iobluetooth/1501545-obexsessionabort)

|  | Declaration |
| --- | --- |
| From | ``` OBEXError OBEXSessionAbort (	OBEXSessionRef inSessionRef,	void *inOptionalHeaders,	size_t inOptionalHeadersLength,	OBEXSessionEventCallback inCallback,	void *inUserRefcon); ``` |
| To | ``` OBEXError OBEXSessionAbort (	OBEXSessionRef inSessionRef,	void *inOptionalHeaders,	size_t inOptionalHeadersLength,	OBEXSessionEventCallback inCallback,	void *inUserRefCon); ``` |

Modified [OBEXSessionSetPath()](https://developer.apple.com/documentation/iobluetooth/1501508-obexsessionsetpath)

|  | Declaration |
| --- | --- |
| From | ``` OBEXError OBEXSessionSetPath (	OBEXSessionRef inSessionRef,	OBEXFlags inFlags,	OBEXConstants inConstants,	void *inOptionalHeaders,	size_t inOptionalHeadersLength,	OBEXSessionEventCallback inCallback,	void *inUserRefcon); ``` |
| To | ``` OBEXError OBEXSessionSetPath (	OBEXSessionRef inSessionRef,	OBEXFlags inFlags,	OBEXConstants inConstants,	void *inOptionalHeaders,	size_t inOptionalHeadersLength,	OBEXSessionEventCallback inCallback,	void *inUserRefCon); ``` |

objc/OBEXFileTransferServices.hModified [-[OBEXFileTransferServices initWithOBEXSession:]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1431373-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithOBEXSession:(IOBluetoothOBEXSession *)inOBEXSession ``` |
| To | ``` - (instancetype)initWithOBEXSession:(IOBluetoothOBEXSession *)inOBEXSession ``` |

Modified [+[OBEXFileTransferServices withOBEXSession:]](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/1435045-withobexsession)

|  | Declaration |
| --- | --- |
| From | ``` + (OBEXFileTransferServices *)withOBEXSession:(IOBluetoothOBEXSession *)inOBEXSession ``` |
| To | ``` + (instancetype)withOBEXSession:(IOBluetoothOBEXSession *)inOBEXSession ``` |

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
