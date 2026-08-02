---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/Kernel.html
archived_at: '2026-07-15T07:34:46.359065Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# Kernel Changes

## Kernel

Availability.h (Removed)AvailabilityInternal.h (Removed)AvailabilityMacros.h (Removed)Removed #def AVAILABLE_MAC_OS_X_VERSION_10_0_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_8Removed #def AVAILABLE_MAC_OS_X_VERSION_10_0_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_9Removed #def AVAILABLE_MAC_OS_X_VERSION_10_1_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_8Removed #def AVAILABLE_MAC_OS_X_VERSION_10_1_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_9Removed #def AVAILABLE_MAC_OS_X_VERSION_10_2_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_8Removed #def AVAILABLE_MAC_OS_X_VERSION_10_2_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_9Removed #def AVAILABLE_MAC_OS_X_VERSION_10_3_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_8Removed #def AVAILABLE_MAC_OS_X_VERSION_10_3_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_9Removed #def AVAILABLE_MAC_OS_X_VERSION_10_4_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_8Removed #def AVAILABLE_MAC_OS_X_VERSION_10_4_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_9Removed #def AVAILABLE_MAC_OS_X_VERSION_10_5_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_8Removed #def AVAILABLE_MAC_OS_X_VERSION_10_5_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_9Removed #def AVAILABLE_MAC_OS_X_VERSION_10_6_AND_LATERRemoved #def AVAILABLE_MAC_OS_X_VERSION_10_6_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_8Removed #def AVAILABLE_MAC_OS_X_VERSION_10_6_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_9Removed #def AVAILABLE_MAC_OS_X_VERSION_10_7_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_8Removed #def AVAILABLE_MAC_OS_X_VERSION_10_7_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_9Removed #def AVAILABLE_MAC_OS_X_VERSION_10_8_AND_LATERRemoved #def AVAILABLE_MAC_OS_X_VERSION_10_8_AND_LATER_BUT_DEPRECATEDRemoved #def AVAILABLE_MAC_OS_X_VERSION_10_8_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_9Removed #def AVAILABLE_MAC_OS_X_VERSION_10_9_AND_LATERRemoved #def AVAILABLE_MAC_OS_X_VERSION_10_9_AND_LATER_BUT_DEPRECATEDRemoved #def DEPRECATED_IN_MAC_OS_X_VERSION_10_6_AND_LATERRemoved #def DEPRECATED_IN_MAC_OS_X_VERSION_10_8_AND_LATERRemoved #def DEPRECATED_IN_MAC_OS_X_VERSION_10_9_AND_LATERRemoved #def DEPRECATED_MSG_ATTRIBUTERemoved #def MAC_OS_X_VERSION_10_0Removed #def MAC_OS_X_VERSION_10_1Removed #def MAC_OS_X_VERSION_10_2Removed #def MAC_OS_X_VERSION_10_3Removed #def MAC_OS_X_VERSION_10_8Removed #def MAC_OS_X_VERSION_10_9Removed #def MAC_OS_X_VERSION_MAX_ALLOWEDRemoved #def UNAVAILABLE_ATTRIBUTERemoved #def WEAK_IMPORT_ATTRIBUTEIOKit/audio/BigNum128.hAdded U128::operator+()Added U128::operator++()Added U128::operator+=()Added U128::operator--()Added U128::operator<()Added U128::operator=()Added U128::operator==()Added U128::operator>()IOKit/bluetooth/Bluetooth.hAdded [BluetoothHCIEventLEConnectionUpdateCompleteResults](https://developer.apple.com/documentation/kernel/bluetoothhcieventleconnectionupdatecompleteresults)Added [BluetoothLEAddressType](https://developer.apple.com/documentation/kernel/bluetoothleaddresstype)Added [BluetoothLEAddressTypePublic](https://developer.apple.com/documentation/iobluetooth/bluetoothleaddresstype/bluetoothleaddresstypepublic)Added [BluetoothLEAddressTypeRandom](https://developer.apple.com/documentation/kernel/bluetoothleaddresstype/bluetoothleaddresstyperandom)Added [BluetoothLEAdvertisingType](https://developer.apple.com/documentation/kernel/bluetoothleadvertisingtype)Added [BluetoothLEAdvertisingTypeConnectableDirected](https://developer.apple.com/documentation/kernel/bluetoothleadvertisingtype/bluetoothleadvertisingtypeconnectabledirected)Added [BluetoothLEAdvertisingTypeConnectableUndirected](https://developer.apple.com/documentation/iobluetooth/bluetoothleadvertisingtype/bluetoothleadvertisingtypeconnectableundirected)Added [BluetoothLEAdvertisingTypeDiscoverableUndirected](https://developer.apple.com/documentation/kernel/bluetoothleadvertisingtype/bluetoothleadvertisingtypediscoverableundirected)Added [BluetoothLEAdvertisingTypeNonConnectableUndirected](https://developer.apple.com/documentation/kernel/bluetoothleadvertisingtype/bluetoothleadvertisingtypenonconnectableundirected)Added [BluetoothLEAdvertisingTypeScanResponse](https://developer.apple.com/documentation/kernel/bluetoothleadvertisingtype/bluetoothleadvertisingtypescanresponse)Added [BluetoothLEScan](https://developer.apple.com/documentation/kernel/bluetoothlescan)Added [BluetoothLEScanDisable](https://developer.apple.com/documentation/iobluetooth/bluetoothlescan/bluetoothlescandisable)Added [BluetoothLEScanDuplicateFilter](https://developer.apple.com/documentation/iobluetooth/bluetoothlescanduplicatefilter)Added [BluetoothLEScanDuplicateFilterDisable](https://developer.apple.com/documentation/kernel/bluetoothlescanduplicatefilter/bluetoothlescanduplicatefilterdisable)Added [BluetoothLEScanDuplicateFilterEnable](https://developer.apple.com/documentation/kernel/bluetoothlescanduplicatefilter/bluetoothlescanduplicatefilterenable)Added [BluetoothLEScanEnable](https://developer.apple.com/documentation/kernel/bluetoothlescan/bluetoothlescanenable)Added [BluetoothLEScanFilter](https://developer.apple.com/documentation/iobluetooth/bluetoothlescanfilter)Added [BluetoothLEScanFilterNone](https://developer.apple.com/documentation/iobluetooth/bluetoothlescanfilter/bluetoothlescanfilternone)Added [BluetoothLEScanFilterWhitelist](https://developer.apple.com/documentation/kernel/bluetoothlescanfilter/bluetoothlescanfilterwhitelist)Added [BluetoothLEScanType](https://developer.apple.com/documentation/iobluetooth/bluetoothlescantype)Added [BluetoothLEScanTypeActive](https://developer.apple.com/documentation/kernel/bluetoothlescantype/bluetoothlescantypeactive)Added [BluetoothLEScanTypePassive](https://developer.apple.com/documentation/iobluetooth/bluetoothlescantype/bluetoothlescantypepassive)Added [kBluetoothEncryptionEnableBREDRAESCCM](https://developer.apple.com/documentation/iobluetooth/kbluetoothencryptionenablebredraesccm)Added [kBluetoothEncryptionEnableBREDRE0](https://developer.apple.com/documentation/kernel/1640012-anonymous/kbluetoothencryptionenablebredre0)Added [kBluetoothEncryptionEnableLEAESCCM](https://developer.apple.com/documentation/iobluetooth/1489342-anonymous/kbluetoothencryptionenableleaesccm)Added [kBluetoothL2CAPChannelLEAP](https://developer.apple.com/documentation/kernel/1640028-anonymous/kbluetoothl2capchannelleap)Added [kBluetoothL2CAPChannelLEAS](https://developer.apple.com/documentation/kernel/1640028-anonymous/kbluetoothl2capchannelleas)Added [kBluetoothL2CAPChannelMagnet](https://developer.apple.com/documentation/kernel/1640028-anonymous/kbluetoothl2capchannelmagnet)Added [kBluetoothL2CAPCommandCodeLECreditBasedConnectionRequest](https://developer.apple.com/documentation/kernel/bluetoothl2capcommandcode/kbluetoothl2capcommandcodelecreditbasedconnectionrequest)Added [kBluetoothL2CAPCommandCodeLECreditBasedConnectionResponse](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capcommandcode/kbluetoothl2capcommandcodelecreditbasedconnectionresponse)Added [kBluetoothL2CAPCommandCodeLEFlowControlCredit](https://developer.apple.com/documentation/iobluetooth/kbluetoothl2capcommandcodeleflowcontrolcredit)Added [kBluetoothLESecurityManagerCommandCodePairingDHKeyCheck](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanagercommandcodepairingdhkeycheck)Added [kBluetoothLESecurityManagerCommandCodePairingKeypressNotification](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagercommandcode/kbluetoothlesecuritymanagercommandcodepairingkeypressnotification)Added [kBluetoothLESecurityManagerCommandCodePairingPublicKey](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanagercommandcodepairingpublickey)Added [kBluetoothLESecurityManagerReasonCodeDHKeyCheckFailed](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerpairingfailedreasoncode/kbluetoothlesecuritymanagerreasoncodedhkeycheckfailed)Added [kBluetoothLESecurityManagerReasonCodeNumericComparisonFailed](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerpairingfailedreasoncode/kbluetoothlesecuritymanagerreasoncodenumericcomparisonfailed)Added [kBluetoothTransportTypeUART](https://developer.apple.com/documentation/iobluetooth/kbluetoothtransporttypeuart)IOKit/ata/IOATARegI386.hAdded IOATAIOReg16::operator=()Added IOATAIOReg32::operator=()Added IOATAIOReg8::operator=()Added IOATAReg16::operator=()Added IOATAReg32::operator=()Added IOATAReg8::operator=()IOKit/audio/IOAudioControl.hModified IOAudioControl::addUserClient()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::addUserClientAction()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::attachAndStart()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::clientClosed()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::createUserClient()

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` virtual IOReturn createUserClient (	task_t task,	void *securityID,	UInt32 type,	IOAudioControlUserClient **newUserClient,	OSDictionary *properties); ``` | OS X 10.1 | -- |
| To | ``` virtual IOReturn createUserClient (	task_t task,	void *securityID,	UInt32 taskType,	IOAudioControlUserClient **newUserClient,	OSDictionary *properties); ``` | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::detachUserClients()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::detachUserClientsAction()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::flushValue()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::free()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::getChannelID()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::getCommandGate()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::getControlID()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::getDataBytes()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::getDataLength()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::getIntValue()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::getIsStarted()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::getSubType()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::getType()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::getUsage()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::getValue()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::getWorkLoop()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::hardwareValueChanged()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::init()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::newUserClient()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::performValueChange()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::removeUserClient()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::removeUserClientAction()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::sendChangeNotification()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::sendQueuedNotifications()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::sendValueChangeNotification()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::setChannelID()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::setChannelName()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::setChannelNumber()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::setCommandGateUsage()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.7 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::setControlID()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::setCoreAudioPropertyID()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::setProperties()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::setReadOnlyFlag()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::setSubType()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::setType()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::setUsage()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::setValue()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::setValueAction()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::setValueChangeHandler()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::setValueChangeTarget()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::setWorkLoop()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::start()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::stop()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::updateValue()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::validateValue()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControl::withAttributes()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

IOKit/audio/IOAudioControlUserClient.hModified IOAudioControlUserClient::clientClose()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControlUserClient::clientDied()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControlUserClient::free()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControlUserClient::initWithAudioControl()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControlUserClient::registerNotificationPort()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControlUserClient::sendChangeNotification()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControlUserClient::sendValueChangeNotification()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioControlUserClient::withAudioControl()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

IOKit/audio/IOAudioDevice.hModified IOAudioDevice::activateAudioEngine()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::addTimerEvent()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::attachAudioPort()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::audioEngineStarting()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::audioEngineStopped()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::completePowerStateChange()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::completePowerStateChangeAction()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::deactivateAllAudioEngines()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::detachAllAudioPorts()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::dispatchTimerEvents()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::flushAudioControls()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::free()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::getCommandGate()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::getPendingPowerState()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::getPowerState()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::getWorkLoop()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::idleAudioSleepHandlerTimer()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::init()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::initHardware()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::initiatePowerStateChange()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::performPowerStateChange()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::protectedCompletePowerStateChange()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::protectedSetPowerState()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::removeAllTimerEvents()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::removeTimerEvent()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::scheduleIdleAudioSleep()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::setAggressiveness()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::setConfigurationApplicationBundle()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::setDeviceCanBeDefault()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::setDeviceModelName()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::setDeviceName()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::setDeviceShortName()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::setDeviceTransportType()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::setFamilyManagePower()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::setIdleAudioSleepTime()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::setManufacturerName()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::setPowerState()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::setPowerStateAction()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::start()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::stop()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::timerFired()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::waitForPendingPowerStateChange()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioDevice::willTerminate()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

IOKit/audio/IOAudioEngine.hAdded IOAudioEngine::waitForEngineResume()Modified IOAudioEngine::addAudioStream()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::addDefaultAudioControl()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::addTimer()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::addUserClient()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::addUserClientAction()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::beginConfigurationChange()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::calculateSampleTimeout()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::cancelConfigurationChange()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::clearAllSampleBuffers()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::clientClosed()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::clipOutputSamples()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::completeConfigurationChange()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::convertInputSamples()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::convertInputSamplesVBR()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified IOAudioEngine::createDictionaryFromSampleRate()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::createSampleRateFromDictionary()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::createUserClient()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::decrementActiveUserClients()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::detachAudioStreams()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::detachUserClients()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::detachUserClientsAction()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::eraseOutputSamples()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::free()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::getAttributeForConnection()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.7 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::getAudioStream()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::getBytesInInputBufferArrayDescriptor()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::getBytesInOutputBufferArrayDescriptor()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::getGlobalUniqueID()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::getLocalUniqueID()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::getLoopCountAndTimeStamp()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::getNearestStartTime()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::getNextStreamID()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::getNumSampleFramesPerBuffer()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::getRunEraseHead()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::getSampleRate()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::getState()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::getStatus()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::getStatusDescriptor()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::getStreamForID()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::getTimerInterval()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::hardwareSampleRateChanged()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::incrementActiveUserClients()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::init()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::initHardware()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::initKeys()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::lockAllStreams()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::lockStreamForIO()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::mixOutputSamples()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::newUserClient()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::pauseAudioEngine()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::performAudioEngineStart()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::performAudioEngineStop()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::performErase()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::performFlush()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::performFormatChange()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::registerService()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::removeAllDefaultAudioControls()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::removeDefaultAudioControl()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::removeTimer()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::removeUserClient()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::removeUserClientAction()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::resetClipPosition()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::resetStatusBuffer()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::resumeAudioEngine()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::sendFormatChangeNotification()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::sendNotification()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::setAttributeForConnection()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.7 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::setAudioDevice()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::setClockDomain()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::setClockIsStable()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::setCommandGateUsage()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.7 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::setDescription()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::setIndex()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::setInputSampleLatency()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::setInputSampleOffset()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified IOAudioEngine::setMixClipOverhead()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::setNumSampleFramesPerBuffer()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::setOutputSampleLatency()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::setOutputSampleOffset()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified IOAudioEngine::setRunEraseHead()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::setSampleLatency()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::setSampleOffset()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::setSampleRate()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::setState()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::setWorkLoopOnAllAudioControls()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::start()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::startAudioEngine()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::startClient()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::stop()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::stopAudioEngine()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::stopClient()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::stopEngineAtPosition()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::takeTimeStamp()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::timerCallback()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::timerFired()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::unlockAllStreams()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::unlockStreamForIO()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngine::updateChannelNumbers()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

IOKit/audio/IOAudioEngineUserClient.hModified IOAudioEngineUserClient::clientClose()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::clientDied()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::clientMemoryForType()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::clientStart()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::clientStop()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::closeClient()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::closeClientAction()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::externalMethod()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.5 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::findBufferSet()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::findExtendedInfo()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::findExtendedInfo64()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.5 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::free()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::freeClientBuffer()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::freeClientBufferSetList()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::getClientNearestStartTime()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::getConnectionID()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::getExternalMethodForIndex()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::getExternalTrapForIndex()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::getNearestStartTime()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::getNearestStartTimeAction()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::initWithAudioEngine()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::isOnline()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::lockBuffers()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::performClientIO()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::performClientInput()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::performClientOutput()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::performWatchdogOutput()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::registerBuffer()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::registerBuffer64()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.5 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::registerBufferAction()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::registerClientBuffer()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::registerClientBuffer64()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.5 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::registerClientParameterBuffer()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::registerNotification()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::registerNotificationAction()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::registerNotificationPort()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::removeBufferSet()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::safeRegisterClientBuffer()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::safeRegisterClientBuffer64()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.5 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::sendFormatChangeNotification()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::sendNotification()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::setCommandGateUsage()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.7 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::setOnline()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::startClient()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::startClientAction()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::stop()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::stopClient()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::stopClientAction()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::unlockBuffers()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::unregisterBuffer()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::unregisterBuffer64()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.5 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::unregisterBufferAction()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::unregisterClientBuffer()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::unregisterClientBuffer64()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.5 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioEngineUserClient::withAudioEngine()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

IOKit/audio/IOAudioLevelControl.hModified IOAudioLevelControl::addNegativeInfinity()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioLevelControl::addRange()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioLevelControl::create()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioLevelControl::createPassThruVolumeControl()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioLevelControl::createVolumeControl()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioLevelControl::free()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioLevelControl::getMaxDB()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioLevelControl::getMaxValue()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioLevelControl::getMinDB()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioLevelControl::getMinValue()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioLevelControl::init()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioLevelControl::setLinearScale()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioLevelControl::setMaxDB()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioLevelControl::setMaxValue()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioLevelControl::setMinDB()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioLevelControl::setMinValue()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioLevelControl::validateValue()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

IOKit/audio/IOAudioPort.hModified IOAudioPort::addAudioControl()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioPort::deactivateAudioControls()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioPort::free()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioPort::getAudioDevice()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioPort::initWithAttributes()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioPort::registerService()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioPort::setName()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioPort::setSubType()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioPort::setType()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioPort::start()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioPort::stop()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioPort::withAttributes()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

IOKit/audio/IOAudioSelectorControl.hModified IOAudioSelectorControl::addAvailableSelection()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioSelectorControl::create()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioSelectorControl::createInputClockSelector()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioSelectorControl::createInputSelector()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioSelectorControl::createOutputClockSelector()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioSelectorControl::createOutputSelector()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioSelectorControl::free()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioSelectorControl::init()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioSelectorControl::removeAvailableSelection()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioSelectorControl::replaceAvailableSelection()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioSelectorControl::validateValue()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioSelectorControl::valueExists()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

IOKit/audio/IOAudioStream.hAdded IOAudioStream::safeLogError()Modified IOAudioStream::addAvailableFormat()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::addClient()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::addDefaultAudioControl()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::clearAvailableFormats()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::clearSampleBuffer()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::clipIfNecessary()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::clipOutputSamples()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::createDictionaryFromFormat()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::createFormatFromDictionary()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::free()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::getDirection()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::getFormat()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::getFormatExtension()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::getMaxNumChannels()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::getMixBuffer()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::getMixBufferSize()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::getNumClients()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::getNumSampleFramesRead()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified IOAudioStream::getSampleBuffer()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::getSampleBufferSize()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::getStartingChannelID()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::getStreamAvailable()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::hardwareFormatChanged()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::initKeys()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::initWithAudioEngine()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::lockStreamForIO()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::mixOutputSamples()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::numSampleFramesPerBufferChanged()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::processOutputSamples()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::readInputSamples()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::removeClient()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::removeDefaultAudioControls()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::resetClipInfo()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::setDefaultNumSampleFramesRead()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified IOAudioStream::setDirection()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::setFormat()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::setFormatAction()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::setIOFunction()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::setIOFunctionList()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::setMixBuffer()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::setProperties()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::setSampleBuffer()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::setSampleLatency()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::setStartingChannelNumber()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::setStreamAvailable()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::setTerminalType()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::stop()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::unlockStreamForIO()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::updateNumClients()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioStream::validateFormat()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

IOKit/audio/IOAudioToggleControl.hModified IOAudioToggleControl::create()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioToggleControl::createMuteControl()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioToggleControl::createPassThruMuteControl()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified IOAudioToggleControl::init()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.1 | -- |
| To | OS X 10.4 | OS X 10.10 |

IOKit/audio/IOAudioTypes.hAdded [kIOAudioSMPTETimeType2398](https://developer.apple.com/documentation/iokit/1584674-anonymous/kioaudiosmptetimetype2398)Added [kIOAudioSMPTETimeType50](https://developer.apple.com/documentation/kernel/1646422-anonymous/kioaudiosmptetimetype50)Added [kIOAudioSMPTETimeType5994](https://developer.apple.com/documentation/iokit/1584674-anonymous/kioaudiosmptetimetype5994)Added [kIOAudioSMPTETimeType5994Drop](https://developer.apple.com/documentation/iokit/1584674-anonymous/kioaudiosmptetimetype5994drop)Added [kIOAudioSMPTETimeType60](https://developer.apple.com/documentation/kernel/1646422-anonymous/kioaudiosmptetimetype60)Added [kIOAudioSMPTETimeType60Drop](https://developer.apple.com/documentation/kernel/1646422-anonymous/kioaudiosmptetimetype60drop)IOKit/storage/IOBlockStorageDevice.hAdded IOBlockStorageDevice::doSetPriority()IOKit/storage/IOBlockStorageDriver.hAdded IOBlockStorageDriver::setPriority()IOKit/bluetooth/IOBluetoothHIDDriver.hAdded IOBluetoothHIDDriver::HIDCommandSleep()IOKit/IODataQueue.hModified [IODataQueue](https://developer.apple.com/documentation/kernel/iodataqueue)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

IOKit/graphics/IODisplay.hAdded [gIODisplayBrightnessFadeKey](https://developer.apple.com/documentation/kernel/giodisplaybrightnessfadekey)Added [gIODisplayFadeStyle](https://developer.apple.com/documentation/kernel/giodisplayfadestyle)Added [gIODisplayFadeStyleKey](https://developer.apple.com/documentation/kernel/giodisplayfadestylekey)Added [gIODisplayFadeTime1](https://developer.apple.com/documentation/kernel/giodisplayfadetime1)Added [gIODisplayFadeTime1Key](https://developer.apple.com/documentation/kernel/giodisplayfadetime1key)Added [gIODisplayFadeTime2](https://developer.apple.com/documentation/kernel/giodisplayfadetime2)Added [gIODisplayFadeTime2Key](https://developer.apple.com/documentation/kernel/giodisplayfadetime2key)Added [gIODisplayFadeTime3](https://developer.apple.com/documentation/kernel/giodisplayfadetime3)Added [gIODisplayFadeTime3Key](https://developer.apple.com/documentation/kernel/giodisplayfadetime3key)Added [gIODisplayGammaScaleKey](https://developer.apple.com/documentation/kernel/giodisplaygammascalekey)IOKit/storage/IOFilterScheme.hAdded IOFilterScheme::setPriority()IOKit/graphics/IOFramebuffer.hAdded [IOFramebufferNotificationNotify](https://developer.apple.com/documentation/kernel/ioframebuffernotificationnotify)Added [kIOFBNotifyDidNotify](https://developer.apple.com/documentation/kernel/1638125-anonymous/kiofbnotifydidnotify)Added [kIOFBNotifyWillNotify](https://developer.apple.com/documentation/kernel/1638125-anonymous/kiofbnotifywillnotify)IOKit/graphics/IOGraphicsTypes.hAdded [kConnectionFlushParameters](https://developer.apple.com/documentation/kernel/1645147-anonymous/kconnectionflushparameters)Added [kConnectionGammaScale](https://developer.apple.com/documentation/iokit/1505380-anonymous/kconnectiongammascale)Added [kDisplayModeNativeFlag](https://developer.apple.com/documentation/kernel/1645087-anonymous/kdisplaymodenativeflag)Added #def kIODisplayBrightnessFadeKeyAdded #def kIODisplayGammaScaleKeyAdded #def kIOFBDisplayPortConfigurationDataKeyAdded [kIOTimingIDVESA_1152x864_75hz](https://developer.apple.com/documentation/kernel/1645122-anonymous/kiotimingidvesa_1152x864_75hz)Added [kIOWindowServerActiveAttribute](https://developer.apple.com/documentation/kernel/1645144-anonymous/kiowindowserveractiveattribute)IOKit/hidevent/IOHIDEventDriver.hRemoved IOHIDEventDriver::calibrateAxisToButtonElement()Removed IOHIDEventDriver::findElements()Removed IOHIDEventDriver::processMultiAxisElement()Removed IOHIDEventDriver::storeReportElement()Added [DigitizerTransducer](https://developer.apple.com/documentation/kernel/digitizertransducer)Added [EventElementCollection](https://developer.apple.com/documentation/kernel/eventelementcollection)Added [IOHIDEvent](https://developer.apple.com/documentation/kernel/iohidevent)Added IOHIDEventDriver::checkMultiAxisElement()Added IOHIDEventDriver::handleDigitizerReport()Added IOHIDEventDriver::handleDigitizerTransducerReport()Added IOHIDEventDriver::handleKeboardReport()Added IOHIDEventDriver::handleMultiAxisPointerReport()Added IOHIDEventDriver::handleRelativeReport()Added IOHIDEventDriver::handleScrollReport()Added IOHIDEventDriver::handleUnicodeGestureCandidateReport()Added IOHIDEventDriver::handleUnicodeGestureReport()Added IOHIDEventDriver::handleUnicodeLegacyReport()Added IOHIDEventDriver::handleUnicodeReport()Added IOHIDEventDriver::parseDigitizerElement()Added IOHIDEventDriver::parseDigitizerTransducerElement()Added IOHIDEventDriver::parseElements()Added IOHIDEventDriver::parseGestureUnicodeElement()Added IOHIDEventDriver::parseKeyboardElement()Added IOHIDEventDriver::parseLegacyUnicodeElement()Added IOHIDEventDriver::parseMultiAxisElement()Added IOHIDEventDriver::parseRelativeElement()Added IOHIDEventDriver::parseScrollElement()Added IOHIDEventDriver::parseUnicodeElement()Added IOHIDEventDriver::processDigitizerElements()Added IOHIDEventDriver::processMultiAxisElements()Added IOHIDEventDriver::processUnicodeElements()Added IOHIDEventDriver::serializeCharacterGestureState()Added IOHIDEventDriver::setDigitizerProperties()Added IOHIDEventDriver::setKeyboardProperties()Added IOHIDEventDriver::setMultiAxisProperties()Added IOHIDEventDriver::setProperties()Added IOHIDEventDriver::setRelativeProperties()Added IOHIDEventDriver::setScrollProperties()Added IOHIDEventDriver::setUnicodeProperties()Modified IOHIDEventDriver::handleBootPointingReport()

|  | Declaration |
| --- | --- |
| From | ``` void handleBootPointingReport (	IOMemoryDescriptor *report,	SInt32 *dX,	SInt32 *dY,	UInt32 *buttonState); ``` |
| To | ``` void handleBootPointingReport (	AbsoluteTime timeStamp,	IOMemoryDescriptor *report,	UInt32 reportID); ``` |

IOKit/hidevent/IOHIDEventService.hRemoved IOHIDEventService::createTransducerData()Removed IOHIDEventService::getTransducerData()Removed IOHIDEventService::processTransducerData()Added IOHIDEventService::dispatchUnicodeEvent()Added [kHIDDispatchOptionDeliveryNotificationForce](https://developer.apple.com/documentation/kernel/2765584-anonymous/khiddispatchoptiondeliverynotificationforce)Added [kHIDDispatchOptionDeliveryNotificationSuppress](https://developer.apple.com/documentation/kernel/2765584-anonymous/khiddispatchoptiondeliverynotificationsuppress)Added [kHIDDispatchOptionPointerDisplayIntegrated](https://developer.apple.com/documentation/kernel/2765607-anonymous/khiddispatchoptionpointerdisplayintegrated)IOKit/hid/IOHIDInterface.hAdded IOHIDInterface::message()IOKit/hid/IOHIDKeys.hAdded #def kIOHIDCategoryAutomotiveValueAdded #def kIOHIDCategoryKeyAdded #def kIOHIDDigitizerGestureCharacterStateKeyAdded #def kIOHIDMaxResponseLatencyKeyAdded #def kIOHIDRequestTimeoutKeyAdded #def kIOHIDTransportAIDBValueAdded #def kIOHIDTransportAirPlayValueAdded #def kIOHIDTransportBluetoothLowEnergyValueAdded #def kIOHIDTransportBluetoothValueAdded #def kIOHIDTransportI2CValueAdded #def kIOHIDTransportIAPValueAdded #def kIOHIDTransportSPIValueAdded #def kIOHIDTransportSPUValueAdded #def kIOHIDTransportSerialValueAdded #def kIOHIDTransportUSBValueAdded [kIOHIDValueOptionsFlagPrevious](https://developer.apple.com/documentation/iokit/1556610-anonymous/kiohidvalueoptionsflagprevious)IOKit/hidsystem/IOHIDSystem.hAdded IOHIDSystem::disableContinuousCursor()Added IOHIDSystem::doSetContinuousCursorEnable()Added IOHIDSystem::enableContinuousCursor()Added IOHIDSystem::setContinuousCursorEnable()Added IOHIDSystem::setContinuousCursorEnableGated()IOKit/hid/IOHIDUsageTables.hAdded [kHIDPage_GenericDeviceControls](https://developer.apple.com/documentation/iokit/1591932-anonymous/khidpage_genericdevicecontrols)Added [kHIDPage_Monitor](https://developer.apple.com/documentation/iokit/1591932-anonymous/khidpage_monitor)Added [kHIDPage_MonitorEnumerated](https://developer.apple.com/documentation/kernel/1641368-anonymous/khidpage_monitorenumerated)Added [kHIDPage_MonitorReserved](https://developer.apple.com/documentation/iokit/1591932-anonymous/khidpage_monitorreserved)Added [kHIDPage_MonitorVirtual](https://developer.apple.com/documentation/iokit/1591932-anonymous/khidpage_monitorvirtual)Added [kHIDPage_PowerReserved](https://developer.apple.com/documentation/iokit/1591932-anonymous/khidpage_powerreserved)Added [kHIDPage_PowerReserved2](https://developer.apple.com/documentation/iokit/1591932-anonymous/khidpage_powerreserved2)Added [kHIDUsage_Csmr_3DModeSelect](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_3dmodeselect)Added [kHIDUsage_Csmr_Aspect](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_aspect)Added [kHIDUsage_Csmr_BlueMenuButton](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_bluemenubutton)Added [kHIDUsage_Csmr_DisplayBacklightToggle](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_displaybacklighttoggle)Added [kHIDUsage_Csmr_DisplayBrightness](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_displaybrightness)Added [kHIDUsage_Csmr_DisplayBrightnessDecrement](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_displaybrightnessdecrement)Added [kHIDUsage_Csmr_DisplayBrightnessIncrement](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_displaybrightnessincrement)Added [kHIDUsage_Csmr_DisplayBrightnessMaximum](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_displaybrightnessmaximum)Added [kHIDUsage_Csmr_DisplayBrightnessMinimum](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_displaybrightnessminimum)Added [kHIDUsage_Csmr_DisplayBrightnessSetAutoBrightness](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_displaybrightnesssetautobrightness)Added [kHIDUsage_Csmr_GreenMenuButton](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_greenmenubutton)Added [kHIDUsage_Csmr_PictureInPictureSwap](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_pictureinpictureswap)Added [kHIDUsage_Csmr_PictureInPictureToggle](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_pictureinpicturetoggle)Added [kHIDUsage_Csmr_RedMenuButton](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_redmenubutton)Added [kHIDUsage_Csmr_VoiceCommand](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_voicecommand)Added [kHIDUsage_Csmr_YellowMenuButton](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_yellowmenubutton)Added [kHIDUsage_Dig_ContactCount](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_contactcount)Added [kHIDUsage_Dig_ContactCountMaximum](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_contactcountmaximum)Added [kHIDUsage_Dig_ContactIdentifier](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_contactidentifier)Added [kHIDUsage_Dig_DeviceConfiguration](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_deviceconfiguration)Added [kHIDUsage_Dig_DeviceIdentifier](https://developer.apple.com/documentation/iokit/1591715-anonymous/khidusage_dig_deviceidentifier)Added [kHIDUsage_Dig_DeviceMode](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_devicemode)Added [kHIDUsage_Dig_DeviceSettings](https://developer.apple.com/documentation/iokit/1591715-anonymous/khidusage_dig_devicesettings)Added [kHIDUsage_Dig_GestureCharacter](https://developer.apple.com/documentation/iokit/1591715-anonymous/khidusage_dig_gesturecharacter)Added [kHIDUsage_Dig_GestureCharacterData](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_gesturecharacterdata)Added [kHIDUsage_Dig_GestureCharacterDataLength](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_gesturecharacterdatalength)Added [kHIDUsage_Dig_GestureCharacterEnable](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_gesturecharacterenable)Added [kHIDUsage_Dig_GestureCharacterEncoding](https://developer.apple.com/documentation/iokit/1591715-anonymous/khidusage_dig_gesturecharacterencoding)Added [kHIDUsage_Dig_GestureCharacterEncodingUTF16BE](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_gesturecharacterencodingutf16be)Added [kHIDUsage_Dig_GestureCharacterEncodingUTF16LE](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_gesturecharacterencodingutf16le)Added [kHIDUsage_Dig_GestureCharacterEncodingUTF32BE](https://developer.apple.com/documentation/iokit/1591715-anonymous/khidusage_dig_gesturecharacterencodingutf32be)Added [kHIDUsage_Dig_GestureCharacterEncodingUTF32LE](https://developer.apple.com/documentation/iokit/1591715-anonymous/khidusage_dig_gesturecharacterencodingutf32le)Added [kHIDUsage_Dig_GestureCharacterEncodingUTF8](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_gesturecharacterencodingutf8)Added [kHIDUsage_Dig_GestureCharacterQuality](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_gesturecharacterquality)Added [kHIDUsage_Dig_Height](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_height)Added [kHIDUsage_Dig_TouchValid](https://developer.apple.com/documentation/iokit/1591715-anonymous/khidusage_dig_touchvalid)Added [kHIDUsage_Dig_Width](https://developer.apple.com/documentation/iokit/1591715-anonymous/khidusage_dig_width)Added [kHIDUsage_GD_SystemMenuSelect](https://developer.apple.com/documentation/kernel/1641458-anonymous/khidusage_gd_systemmenuselect)Added [kHIDUsage_GenDevControls_BackgroundControls](https://developer.apple.com/documentation/iokit/1592575-anonymous/khidusage_gendevcontrols_backgroundcontrols)IOKit/hidsystem/IOHIDUsageTables.hAdded [kHIDPage_GenericDeviceControls](https://developer.apple.com/documentation/iokit/1591932-anonymous/khidpage_genericdevicecontrols)Added [kHIDPage_Monitor](https://developer.apple.com/documentation/iokit/1591932-anonymous/khidpage_monitor)Added [kHIDPage_MonitorEnumerated](https://developer.apple.com/documentation/kernel/1641368-anonymous/khidpage_monitorenumerated)Added [kHIDPage_MonitorReserved](https://developer.apple.com/documentation/iokit/1591932-anonymous/khidpage_monitorreserved)Added [kHIDPage_MonitorVirtual](https://developer.apple.com/documentation/iokit/1591932-anonymous/khidpage_monitorvirtual)Added [kHIDPage_PowerReserved](https://developer.apple.com/documentation/iokit/1591932-anonymous/khidpage_powerreserved)Added [kHIDPage_PowerReserved2](https://developer.apple.com/documentation/iokit/1591932-anonymous/khidpage_powerreserved2)Added [kHIDUsage_Csmr_3DModeSelect](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_3dmodeselect)Added [kHIDUsage_Csmr_Aspect](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_aspect)Added [kHIDUsage_Csmr_BlueMenuButton](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_bluemenubutton)Added [kHIDUsage_Csmr_DisplayBacklightToggle](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_displaybacklighttoggle)Added [kHIDUsage_Csmr_DisplayBrightness](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_displaybrightness)Added [kHIDUsage_Csmr_DisplayBrightnessDecrement](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_displaybrightnessdecrement)Added [kHIDUsage_Csmr_DisplayBrightnessIncrement](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_displaybrightnessincrement)Added [kHIDUsage_Csmr_DisplayBrightnessMaximum](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_displaybrightnessmaximum)Added [kHIDUsage_Csmr_DisplayBrightnessMinimum](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_displaybrightnessminimum)Added [kHIDUsage_Csmr_DisplayBrightnessSetAutoBrightness](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_displaybrightnesssetautobrightness)Added [kHIDUsage_Csmr_GreenMenuButton](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_greenmenubutton)Added [kHIDUsage_Csmr_PictureInPictureSwap](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_pictureinpictureswap)Added [kHIDUsage_Csmr_PictureInPictureToggle](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_pictureinpicturetoggle)Added [kHIDUsage_Csmr_RedMenuButton](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_redmenubutton)Added [kHIDUsage_Csmr_VoiceCommand](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_voicecommand)Added [kHIDUsage_Csmr_YellowMenuButton](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_yellowmenubutton)Added [kHIDUsage_Dig_ContactCount](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_contactcount)Added [kHIDUsage_Dig_ContactCountMaximum](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_contactcountmaximum)Added [kHIDUsage_Dig_ContactIdentifier](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_contactidentifier)Added [kHIDUsage_Dig_DeviceConfiguration](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_deviceconfiguration)Added [kHIDUsage_Dig_DeviceIdentifier](https://developer.apple.com/documentation/iokit/1591715-anonymous/khidusage_dig_deviceidentifier)Added [kHIDUsage_Dig_DeviceMode](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_devicemode)Added [kHIDUsage_Dig_DeviceSettings](https://developer.apple.com/documentation/iokit/1591715-anonymous/khidusage_dig_devicesettings)Added [kHIDUsage_Dig_GestureCharacter](https://developer.apple.com/documentation/iokit/1591715-anonymous/khidusage_dig_gesturecharacter)Added [kHIDUsage_Dig_GestureCharacterData](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_gesturecharacterdata)Added [kHIDUsage_Dig_GestureCharacterDataLength](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_gesturecharacterdatalength)Added [kHIDUsage_Dig_GestureCharacterEnable](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_gesturecharacterenable)Added [kHIDUsage_Dig_GestureCharacterEncoding](https://developer.apple.com/documentation/iokit/1591715-anonymous/khidusage_dig_gesturecharacterencoding)Added [kHIDUsage_Dig_GestureCharacterEncodingUTF16BE](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_gesturecharacterencodingutf16be)Added [kHIDUsage_Dig_GestureCharacterEncodingUTF16LE](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_gesturecharacterencodingutf16le)Added [kHIDUsage_Dig_GestureCharacterEncodingUTF32BE](https://developer.apple.com/documentation/iokit/1591715-anonymous/khidusage_dig_gesturecharacterencodingutf32be)Added [kHIDUsage_Dig_GestureCharacterEncodingUTF32LE](https://developer.apple.com/documentation/iokit/1591715-anonymous/khidusage_dig_gesturecharacterencodingutf32le)Added [kHIDUsage_Dig_GestureCharacterEncodingUTF8](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_gesturecharacterencodingutf8)Added [kHIDUsage_Dig_GestureCharacterQuality](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_gesturecharacterquality)Added [kHIDUsage_Dig_Height](https://developer.apple.com/documentation/kernel/1641337-anonymous/khidusage_dig_height)Added [kHIDUsage_Dig_TouchValid](https://developer.apple.com/documentation/iokit/1591715-anonymous/khidusage_dig_touchvalid)Added [kHIDUsage_Dig_Width](https://developer.apple.com/documentation/iokit/1591715-anonymous/khidusage_dig_width)Added [kHIDUsage_GD_SystemMenuSelect](https://developer.apple.com/documentation/kernel/1641458-anonymous/khidusage_gd_systemmenuselect)Added [kHIDUsage_GenDevControls_BackgroundControls](https://developer.apple.com/documentation/iokit/1592575-anonymous/khidusage_gendevcontrols_backgroundcontrols)IOKit/IOInterruptAccounting.h (Added)Added #def IA_BASE_CHANNEL_IDAdded #def IA_GET_CHANNEL_IDAdded #def IA_GET_INTERRUPT_INDEXAdded #def IA_GET_STATISTIC_INDEXAdded #def IA_INDEX_MASKAdded #def IA_INDEX_MAXAdded #def IA_INTERRUPT_INDEX_SHIFTAdded #def IA_MAX_CHANNEL_IDAdded #def IA_NUM_INTERRUPT_ACCOUNTING_STATISTICSAdded #def IA_STATISTIC_INDEX_SHIFTAdded kInterruptAccountingCPUWakeupsIndexAdded kInterruptAccountingFirstLevelCountIndexAdded kInterruptAccountingFirstLevelTimeIndexAdded kInterruptAccountingIdleExitsIndexAdded kInterruptAccountingInvalidStatisticIndexAdded kInterruptAccountingNoThreadWakeupsIndexAdded kInterruptAccountingPackageWakeupsIndexAdded kInterruptAccountingSecondLevelCPUTimeIndexAdded kInterruptAccountingSecondLevelCountIndexAdded kInterruptAccountingSecondLevelSystemTimeIndexAdded kInterruptAccountingTotalThreadWakeupsIndexIOKit/IOInterruptEventSource.hAdded IOInterruptEventSource::unregisterInterruptHandler()IOKit/IOKernelReportStructs.h (Added)Added [IOHistogramSegmentConfig](https://developer.apple.com/documentation/kernel/iohistogramsegmentconfig)Added [IONormDistReportValues](https://developer.apple.com/documentation/kernel/ionormdistreportvalues)Added #def IOREPORT_GETUNIT_QUANTITYAdded #def IOREPORT_GETUNIT_SCALEAdded [IOReportQuantity](https://developer.apple.com/documentation/kernel/ioreportquantity)Added [IOReportScaleFactor](https://developer.apple.com/documentation/kernel/ioreportscalefactor)Added [IOReportUnits](https://developer.apple.com/documentation/kernel/ioreportunits)Added #def kIOHistogramScaleExponentialAdded #def kIOHistogramScaleLinearAdded #def kIOReportAPIVersionAdded #def kIOReportCardinalMaskAdded #def kIOReportCardinalShiftAdded #def kIOReportChannelIDIdxAdded #def kIOReportChannelNameIdxAdded #def kIOReportChannelTypeIdxAdded #def kIOReportExpBaseAdded #def kIOReportExpZeroOffsetAdded #def kIOReportLegendChannelsKeyAdded #def kIOReportLegendConfigKeyAdded #def kIOReportLegendGroupNameKeyAdded #def kIOReportLegendInfoKeyAdded #def kIOReportLegendKeyAdded #def kIOReportLegendPublicKeyAdded #def kIOReportLegendStateNamesKeyAdded #def kIOReportLegendSubGroupNameKeyAdded #def kIOReportLegendUnitKeyAdded [kIOReportQuantityCapacitance](https://developer.apple.com/documentation/kernel/1643665-anonymous/kioreportquantitycapacitance)Added [kIOReportQuantityCurrent](https://developer.apple.com/documentation/kernel/1643665-anonymous/kioreportquantitycurrent)Added [kIOReportQuantityData](https://developer.apple.com/documentation/kernel/1643665-anonymous/kioreportquantitydata)Added [kIOReportQuantityEnergy](https://developer.apple.com/documentation/kernel/1643665-anonymous/kioreportquantityenergy)Added [kIOReportQuantityEventCount](https://developer.apple.com/documentation/kernel/1643665-anonymous/kioreportquantityeventcount)Added [kIOReportQuantityFrequency](https://developer.apple.com/documentation/kernel/1643665-anonymous/kioreportquantityfrequency)Added [kIOReportQuantityInductance](https://developer.apple.com/documentation/kernel/1643665-anonymous/kioreportquantityinductance)Added [kIOReportQuantityPacketCount](https://developer.apple.com/documentation/kernel/1643665-anonymous/kioreportquantitypacketcount)Added [kIOReportQuantityPower](https://developer.apple.com/documentation/kernel/1643665-anonymous/kioreportquantitypower)Added [kIOReportQuantityTemperature](https://developer.apple.com/documentation/kernel/1643665-anonymous/kioreportquantitytemperature)Added [kIOReportQuantityTime](https://developer.apple.com/documentation/kernel/1643665-anonymous/kioreportquantitytime)Added [kIOReportQuantityUndefined](https://developer.apple.com/documentation/kernel/1643665-anonymous/kioreportquantityundefined)Added [kIOReportQuantityVoltage](https://developer.apple.com/documentation/kernel/1643665-anonymous/kioreportquantityvoltage)Added #def kIOReportScale1GHzAdded #def kIOReportScale24MHzAdded #def kIOReportScale4KiBAdded #def kIOReportScale8KiBAdded #def kIOReportScaleBitsAdded #def kIOReportScaleBytesAdded #def kIOReportScaleConstMaskAdded #def kIOReportScaleGiBytesAdded #def kIOReportScaleGibiAdded #def kIOReportScaleGigaAdded #def kIOReportScaleHWPageSizeAdded #def kIOReportScaleIECMaskAdded #def kIOReportScaleIECShiftAdded #def kIOReportScaleKiBytesAdded #def kIOReportScaleKibiAdded #def kIOReportScaleKiloAdded #def kIOReportScaleMachHWTicksAdded #def kIOReportScaleMebiAdded #def kIOReportScaleMegaAdded #def kIOReportScaleMiBytesAdded #def kIOReportScaleMicroAdded #def kIOReportScaleMilliAdded #def kIOReportScaleNanoAdded #def kIOReportScaleOneOverAdded #def kIOReportScalePicoAdded #def kIOReportScaleSIMaskAdded #def kIOReportScaleSIShiftAdded #def kIOReportScaleTebiAdded #def kIOReportScaleTeraAdded #def kIOReportScaleTiBytesAdded #def kIOReportScaleUnityAdded #def kIOReportUnit1GHzTicksAdded #def kIOReportUnit24MHzTicksAdded #def kIOReportUnitBitsAdded #def kIOReportUnitBytesAdded #def kIOReportUnitEventsAdded #def kIOReportUnitHWTicksAdded #def kIOReportUnitNoneAdded #def kIOReportUnitPacketsAdded #def kIOReportUnit_JAdded #def kIOReportUnit_KiBAdded #def kIOReportUnit_mJAdded #def kIOReportUnit_msAdded #def kIOReportUnit_nJAdded #def kIOReportUnit_nsAdded #def kIOReportUnit_pJAdded #def kIOReportUnit_sAdded #def kIOReportUnit_uJAdded #def kIOReportUnit_usIOKit/IOKitDebug.hRemoved kIOAppRespStacksOnRemoved kIOLogDriverPower1Removed kIOLogDriverPower2Removed kIOPersistentLogAdded [kIOWaitQuietBeforeRoot](https://developer.apple.com/documentation/kernel/1644087-anonymous/kiowaitquietbeforeroot)IOKit/IOKitKeys.hAdded [#def kIONVRAMActivateCSRConfigPropertyKey](https://developer.apple.com/documentation/iokit/kionvramactivatecsrconfigpropertykey)IOKit/storage/IOMedia.hAdded IOMedia::setPriority()IOKit/IOMemoryDescriptor.hRemoved IOGeneralMemoryDescriptor::createNamedEntry()Added IOMemoryDescriptor::populateDevicePager()Added #def IODIRECTIONCOMPLETEWITHDATAVALIDDEFINEDAdded #def IODIRECTIONCOMPLETEWITHERRORDEFINEDAdded #def IODIRECTIONPREPARENONCOHERENTDEFINEDAdded [kIODirectionCompleteWithDataValid](https://developer.apple.com/documentation/kernel/1643339-anonymous/kiodirectioncompletewithdatavalid)Added [kIODirectionCompleteWithError](https://developer.apple.com/documentation/kernel/1643339-anonymous/kiodirectioncompletewitherror)Added [kIODirectionPrepareNonCoherent](https://developer.apple.com/documentation/kernel/1643339-anonymous/kiodirectionpreparenoncoherent)Modified IOMemoryDescriptor::handleFault()

|  | Declaration |
| --- | --- |
| From | ``` IOReturn handleFault (	void *pager,	vm_map_t addressMap,	mach_vm_address_t address,	mach_vm_size_t sourceOffset,	mach_vm_size_t length,	IOOptionBits options); ``` |
| To | ``` IOReturn handleFault (	void *_pager,	mach_vm_size_t sourceOffset,	mach_vm_size_t length); ``` |

IOKit/IONVRAM.hAdded IODTNVRAM::copyProperty()IOKit/pci/IOPCIBridge.hRemoved IOPCI2PCIBridge::startHotPlug()Removed #def kIOPCIBridgeRegsAdded IOPCI2PCIBridge::allocateBridgeInterrupts()Added IOPCI2PCIBridge::createEventSource()Added IOPCI2PCIBridge::disableBridgeInterrupts()Added IOPCI2PCIBridge::enableBridgeInterrupts()Added IOPCI2PCIBridge::enableLTR()Added IOPCI2PCIBridge::setTunnelL1Enable()Added IOPCI2PCIBridge::startBridgeInterrupts()Added IOPCIBridge::createEventSource()Added IOPCIBridge::enableLTR()Added IOPCIBridge::getConfiguratorWorkLoop()Added IOPCIBridge::newUserClient()Added IOPCIBridge::restoreQEnter()Added IOPCIBridge::restoreQRemove()Added IOPCIBridge::restoreTunnelState()Added IOPCIBridge::setDeviceL1PMBits()Added IOPCIBridge::tunnelsWait()Added #def kIOPCI2PCIBridgeNameModified IOPCIBridge::configOp()

|  | Declaration |
| --- | --- |
| From | ``` IOReturn configOp (	IOService *device,	uintptr_t op,	void *result); ``` |
| To | ``` IOReturn configOp (	IOService *device,	uintptr_t op,	void *result,	void *arg); ``` |

Modified IOPCIBridge::setDeviceASPMBits()

|  | Declaration |
| --- | --- |
| From | ``` IOReturn setDeviceASPMBits (	IOPCIDevice *device,	IOOptionBits state); ``` |
| To | ``` IOReturn setDeviceASPMBits (	IOPCIDevice *device,	uint32_t bits); ``` |

IOKit/pci/IOPCIDevice.hRemoved IOPCIAddressSpaceAdded IOPCIDevice::createEventSource()Added IOPCIDevice::enableLTR()Added IOPCIDevice::getDeviceMemoryWithIndex()Added IOPCIDevice::setASPMState()Added IOPCIDevice::setTunnelL1Enable()Added IOPCIDevice::updateWakeReason()Added [IOPCIEventSource](https://developer.apple.com/documentation/kernel/iopcieventsource)Added IOPCIEventSource::checkForWork()Added IOPCIEventSource::disable()Added IOPCIEventSource::enable()Added IOPCIEventSource::free()Added IOPCIEventSource::getMetaClass()Added IOPCIAddressSpaceAdded [IOPCIEvent](https://developer.apple.com/documentation/kernel/iopcievent)Added #def IOPCIEventActionAdded #def kIOPCIBridgeInterruptESKeyAdded [kIOPCIEventCorrectableError](https://developer.apple.com/documentation/kernel/1640345-anonymous/kiopcieventcorrectableerror)Added [kIOPCIEventFatalError](https://developer.apple.com/documentation/kernel/1640345-anonymous/kiopcieventfatalerror)Added [kIOPCIEventLinkEnableChange](https://developer.apple.com/documentation/kernel/1640345-anonymous/kiopcieventlinkenablechange)Added [kIOPCIEventNonFatalError](https://developer.apple.com/documentation/kernel/1640345-anonymous/kiopcieventnonfatalerror)Added [kIOPCIExpressL1PMSubstatesCapability](https://developer.apple.com/documentation/kernel/1640344-anonymous/kiopciexpressl1pmsubstatescapability)Added [kIOPCIExpressLatencyTolerenceReportingCapability](https://developer.apple.com/documentation/kernel/1640344-anonymous/kiopciexpresslatencytolerencereportingcapability)Added #def kIOPCITunnelL1EnableKeyAdded [kPCI2PCIBridgeControl](https://developer.apple.com/documentation/kernel/1640341-anonymous/kpci2pcibridgecontrol)Added [kPCI2PCIIORange](https://developer.apple.com/documentation/kernel/1640341-anonymous/kpci2pciiorange)Added [kPCI2PCIMemoryRange](https://developer.apple.com/documentation/kernel/1640341-anonymous/kpci2pcimemoryrange)Added [kPCI2PCIPrefetchMemoryRange](https://developer.apple.com/documentation/kernel/1640341-anonymous/kpci2pciprefetchmemoryrange)Added [kPCI2PCIPrefetchUpperBase](https://developer.apple.com/documentation/kernel/1640341-anonymous/kpci2pciprefetchupperbase)Added [kPCI2PCIPrefetchUpperLimit](https://developer.apple.com/documentation/kernel/1640341-anonymous/kpci2pciprefetchupperlimit)Added [kPCI2PCIPrimaryBus](https://developer.apple.com/documentation/kernel/1640341-anonymous/kpci2pciprimarybus)Added [kPCI2PCISecondaryBus](https://developer.apple.com/documentation/kernel/1640341-anonymous/kpci2pcisecondarybus)Added [kPCI2PCISecondaryLT](https://developer.apple.com/documentation/kernel/1640341-anonymous/kpci2pcisecondarylt)Added [kPCI2PCISubordinateBus](https://developer.apple.com/documentation/kernel/1640341-anonymous/kpci2pcisubordinatebus)Added [kPCI2PCIUpperIORange](https://developer.apple.com/documentation/kernel/1640341-anonymous/kpci2pciupperiorange)IOKit/storage/IOPartitionScheme.hAdded IOPartitionScheme::setPriority()Added #def kIOMediaBaseKeyIOKit/IOPlatformExpert.hAdded IOPlatformExpert::deregisterInterruptController()Added IOPlatformExpert::getUTCTimeOfDay()Added IOPlatformExpert::setUTCTimeOfDay()Added [PEGetUTCTimeOfDay()](https://developer.apple.com/documentation/kernel/1451638-pegetutctimeofday)Added [PESetUTCTimeOfDay()](https://developer.apple.com/documentation/kernel/1451543-pesetutctimeofday)Added [gIOPlatformHaltRestartActionKey](https://developer.apple.com/documentation/kernel/gioplatformhaltrestartactionkey)IOKit/IOReportMacros.h (Added)Added #def IOREPORT_ABORTAdded [IOStateReportInfo](https://developer.apple.com/documentation/kernel/iostatereportinfo)Added #def SIMPLEARRAY_BUFSIZEAdded #def SIMPLEARRAY_GETCHIDAdded #def SIMPLEARRAY_GETCHTYPEAdded #def SIMPLEARRAY_GETVALUEAdded #def SIMPLEARRAY_INCREMENTVALUEAdded #def SIMPLEARRAY_INITAdded #def SIMPLEARRAY_SETVALUEAdded #def SIMPLEARRAY_UPDATEPREPAdded #def SIMPLEARRAY_UPDATERESAdded #def SIMPLEREPORT_BUFSIZEAdded #def SIMPLEREPORT_GETCHIDAdded #def SIMPLEREPORT_GETCHTYPEAdded #def SIMPLEREPORT_GETVALUEAdded #def SIMPLEREPORT_INCREMENTVALUEAdded #def SIMPLEREPORT_INITAdded #def SIMPLEREPORT_SETVALUEAdded #def SIMPLEREPORT_UPDATEPREPAdded #def SIMPLEREPORT_UPDATERESAdded #def STATEREPORT_BUFSIZEAdded #def STATEREPORT_GETCHIDAdded #def STATEREPORT_GETCHTYPEAdded #def STATEREPORT_GETTICKSAdded #def STATEREPORT_GETTRANSITIONSAdded #def STATEREPORT_INITAdded #def STATEREPORT_SETSTATEAdded #def STATEREPORT_SETSTATEIDAdded #def STATEREPORT_UPDATEPREPAdded #def STATEREPORT_UPDATERESIOKit/IOReportTypes.hAdded #def IOR_VALUES_PER_ELEMENTAdded [IOSimpleArrayReportValues](https://developer.apple.com/documentation/kernel/iosimplearrayreportvalues)Added #def kIOReportCategoryFieldAdded #def kIOReportCategoryInterruptAdded [kIOReportFormatSimpleArray](https://developer.apple.com/documentation/kernel/1645976-anonymous/kioreportformatsimplearray)IOKit/scsi/IOSCSIProtocolInterface.hAdded #def kIOPropertyRequiresRestartEjectKeyIOKit/IOService.hAdded IOService::actionDidStop()Added IOService::actionWillStop()Added IOService::addInterruptStatistics()Added IOService::init()Added IOService::removeInterruptStatistics()IOKit/IOSharedDataQueue.hAdded IOSharedDataQueue::enqueue()Added IOSharedDataQueue::getQueueSize()Added IOSharedDataQueue::setQueueSize()Added #def DISABLE_DATAQUEUE_WARNINGIOKit/storage/IOStorage.hAdded IOStorage::setPriority()Added [IOStoragePriority](https://developer.apple.com/documentation/kernel/iostoragepriority)Added #def kIOStorageFeaturePriorityAdded [kIOStoragePriorityBackground](https://developer.apple.com/documentation/kernel/1644757-anonymous/kiostorageprioritybackground)Added [kIOStoragePriorityDefault](https://developer.apple.com/documentation/kernel/1644757-anonymous/kiostorageprioritydefault)Added [kIOStoragePriorityHigh](https://developer.apple.com/documentation/kernel/1644757-anonymous/kiostoragepriorityhigh)Added [kIOStoragePriorityLow](https://developer.apple.com/documentation/kernel/1644757-anonymous/kiostorageprioritylow)IOKit/storage/IOStorageControllerCharacteristics.h (Added)Added #def kIOPropertyAESCBCKeyAdded #def kIOPropertyAESXEXKeyAdded #def kIOPropertyAESXTSKeyAdded #def kIOPropertyControllerCharacteristicsKeyAdded #def kIOPropertyEncryptionTypeKeyAdded [#def kIOPropertyFibreChannelALPAKey](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelalpakey)Added [#def kIOPropertyFibreChannelAddressIdentifierKey](https://developer.apple.com/documentation/kernel/kiopropertyfibrechanneladdressidentifierkey)Added [#def kIOPropertyFibreChannelCableDescriptionCopperKey](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelcabledescriptioncopperkey)Added [#def kIOPropertyFibreChannelCableDescriptionFiberOpticKey](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelcabledescriptionfiberoptickey)Added [#def kIOPropertyFibreChannelCableDescriptionKey](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelcabledescriptionkey)Added [#def kIOPropertyFibreChannelNodeWorldWideNameKey](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelnodeworldwidenamekey)Added [#def kIOPropertyFibreChannelPortWorldWideNameKey](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelportworldwidenamekey)Added #def kIOPropertyLowPowerModeKeyAdded [#def kIOPropertyPortDescriptionKey](https://developer.apple.com/documentation/kernel/kiopropertyportdescriptionkey)Added [#def kIOPropertyPortSpeed10GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed10gigabitkey)Added [#def kIOPropertyPortSpeed12GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed12gigabitkey)Added [#def kIOPropertyPortSpeed16GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed16gigabitkey)Added [#def kIOPropertyPortSpeed1GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed1gigabitkey)Added [#def kIOPropertyPortSpeed1_5GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed1_5gigabitkey)Added [#def kIOPropertyPortSpeed2GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed2gigabitkey)Added [#def kIOPropertyPortSpeed3GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed3gigabitkey)Added [#def kIOPropertyPortSpeed40GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed40gigabitkey)Added [#def kIOPropertyPortSpeed4GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed4gigabitkey)Added [#def kIOPropertyPortSpeed6GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed6gigabitkey)Added [#def kIOPropertyPortSpeed8GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed8gigabitkey)Added [#def kIOPropertyPortSpeedAutomatic10GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatic10gigabitkey)Added [#def kIOPropertyPortSpeedAutomatic1GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatic1gigabitkey)Added [#def kIOPropertyPortSpeedAutomatic1_5GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatic1_5gigabitkey)Added [#def kIOPropertyPortSpeedAutomatic2GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatic2gigabitkey)Added [#def kIOPropertyPortSpeedAutomatic3GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatic3gigabitkey)Added [#def kIOPropertyPortSpeedAutomatic4GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatic4gigabitkey)Added [#def kIOPropertyPortSpeedAutomatic6GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatic6gigabitkey)Added [#def kIOPropertyPortSpeedAutomatic8GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatic8gigabitkey)Added [#def kIOPropertyPortSpeedAutomaticKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatickey)Added [#def kIOPropertyPortSpeedKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedkey)Added [#def kIOPropertyPortStatusKey](https://developer.apple.com/documentation/kernel/kiopropertyportstatuskey)Added [#def kIOPropertyPortStatusLinkEstablishedKey](https://developer.apple.com/documentation/kernel/kiopropertyportstatuslinkestablishedkey)Added [#def kIOPropertyPortStatusLinkFailedKey](https://developer.apple.com/documentation/kernel/kiopropertyportstatuslinkfailedkey)Added [#def kIOPropertyPortStatusNoLinkEstablishedKey](https://developer.apple.com/documentation/kernel/kiopropertyportstatusnolinkestablishedkey)Added [#def kIOPropertyPortTopologyAutomaticKey](https://developer.apple.com/documentation/kernel/kiopropertyporttopologyautomatickey)Added [#def kIOPropertyPortTopologyAutomaticNLPortKey](https://developer.apple.com/documentation/kernel/kiopropertyporttopologyautomaticnlportkey)Added [#def kIOPropertyPortTopologyAutomaticNPortKey](https://developer.apple.com/documentation/kernel/kiopropertyporttopologyautomaticnportkey)Added [#def kIOPropertyPortTopologyKey](https://developer.apple.com/documentation/kernel/kiopropertyporttopologykey)Added [#def kIOPropertyPortTopologyNLPortKey](https://developer.apple.com/documentation/kernel/kiopropertyporttopologynlportkey)Added [#def kIOPropertyPortTopologyNPortKey](https://developer.apple.com/documentation/kernel/kiopropertyporttopologynportkey)Added [#def kIOPropertySASAddressKey](https://developer.apple.com/documentation/kernel/kiopropertysasaddresskey)Added [#def kIOPropertySCSIParallelSignalingTypeHVDKey](https://developer.apple.com/documentation/kernel/kiopropertyscsiparallelsignalingtypehvdkey)Added [#def kIOPropertySCSIParallelSignalingTypeKey](https://developer.apple.com/documentation/kernel/kiopropertyscsiparallelsignalingtypekey)Added [#def kIOPropertySCSIParallelSignalingTypeLVDKey](https://developer.apple.com/documentation/kernel/kiopropertyscsiparallelsignalingtypelvdkey)Added [#def kIOPropertySCSIParallelSignalingTypeSEKey](https://developer.apple.com/documentation/kernel/kiopropertyscsiparallelsignalingtypesekey)Added [#def kIOPropertySCSIPortIdentifierKey](https://developer.apple.com/documentation/kernel/kiopropertyscsiportidentifierkey)IOKit/storage/IOStorageProtocolCharacteristics.hRemoved [#def kIOPropertyFibreChannelALPAKey](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelalpakey)Removed [#def kIOPropertyFibreChannelAddressIdentifierKey](https://developer.apple.com/documentation/kernel/kiopropertyfibrechanneladdressidentifierkey)Removed [#def kIOPropertyFibreChannelCableDescriptionCopperKey](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelcabledescriptioncopperkey)Removed [#def kIOPropertyFibreChannelCableDescriptionFiberOpticKey](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelcabledescriptionfiberoptickey)Removed [#def kIOPropertyFibreChannelCableDescriptionKey](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelcabledescriptionkey)Removed [#def kIOPropertyFibreChannelNodeWorldWideNameKey](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelnodeworldwidenamekey)Removed [#def kIOPropertyFibreChannelPortWorldWideNameKey](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelportworldwidenamekey)Removed [#def kIOPropertyPortDescriptionKey](https://developer.apple.com/documentation/kernel/kiopropertyportdescriptionkey)Removed [#def kIOPropertyPortSpeed10GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed10gigabitkey)Removed [#def kIOPropertyPortSpeed12GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed12gigabitkey)Removed [#def kIOPropertyPortSpeed16GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed16gigabitkey)Removed [#def kIOPropertyPortSpeed1GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed1gigabitkey)Removed [#def kIOPropertyPortSpeed1_5GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed1_5gigabitkey)Removed [#def kIOPropertyPortSpeed2GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed2gigabitkey)Removed [#def kIOPropertyPortSpeed3GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed3gigabitkey)Removed [#def kIOPropertyPortSpeed40GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed40gigabitkey)Removed [#def kIOPropertyPortSpeed4GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed4gigabitkey)Removed [#def kIOPropertyPortSpeed6GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed6gigabitkey)Removed [#def kIOPropertyPortSpeed8GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeed8gigabitkey)Removed [#def kIOPropertyPortSpeedAutomatic10GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatic10gigabitkey)Removed [#def kIOPropertyPortSpeedAutomatic1GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatic1gigabitkey)Removed [#def kIOPropertyPortSpeedAutomatic1_5GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatic1_5gigabitkey)Removed [#def kIOPropertyPortSpeedAutomatic2GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatic2gigabitkey)Removed [#def kIOPropertyPortSpeedAutomatic3GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatic3gigabitkey)Removed [#def kIOPropertyPortSpeedAutomatic4GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatic4gigabitkey)Removed [#def kIOPropertyPortSpeedAutomatic6GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatic6gigabitkey)Removed [#def kIOPropertyPortSpeedAutomatic8GigabitKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatic8gigabitkey)Removed [#def kIOPropertyPortSpeedAutomaticKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatickey)Removed [#def kIOPropertyPortSpeedKey](https://developer.apple.com/documentation/kernel/kiopropertyportspeedkey)Removed [#def kIOPropertyPortStatusKey](https://developer.apple.com/documentation/kernel/kiopropertyportstatuskey)Removed [#def kIOPropertyPortStatusLinkEstablishedKey](https://developer.apple.com/documentation/kernel/kiopropertyportstatuslinkestablishedkey)Removed [#def kIOPropertyPortStatusLinkFailedKey](https://developer.apple.com/documentation/kernel/kiopropertyportstatuslinkfailedkey)Removed [#def kIOPropertyPortStatusNoLinkEstablishedKey](https://developer.apple.com/documentation/kernel/kiopropertyportstatusnolinkestablishedkey)Removed [#def kIOPropertyPortTopologyAutomaticKey](https://developer.apple.com/documentation/kernel/kiopropertyporttopologyautomatickey)Removed [#def kIOPropertyPortTopologyAutomaticNLPortKey](https://developer.apple.com/documentation/kernel/kiopropertyporttopologyautomaticnlportkey)Removed [#def kIOPropertyPortTopologyAutomaticNPortKey](https://developer.apple.com/documentation/kernel/kiopropertyporttopologyautomaticnportkey)Removed [#def kIOPropertyPortTopologyKey](https://developer.apple.com/documentation/kernel/kiopropertyporttopologykey)Removed [#def kIOPropertyPortTopologyNLPortKey](https://developer.apple.com/documentation/kernel/kiopropertyporttopologynlportkey)Removed [#def kIOPropertyPortTopologyNPortKey](https://developer.apple.com/documentation/kernel/kiopropertyporttopologynportkey)Removed [#def kIOPropertySASAddressKey](https://developer.apple.com/documentation/kernel/kiopropertysasaddresskey)Removed [#def kIOPropertySCSIParallelSignalingTypeHVDKey](https://developer.apple.com/documentation/kernel/kiopropertyscsiparallelsignalingtypehvdkey)Removed [#def kIOPropertySCSIParallelSignalingTypeKey](https://developer.apple.com/documentation/kernel/kiopropertyscsiparallelsignalingtypekey)Removed [#def kIOPropertySCSIParallelSignalingTypeLVDKey](https://developer.apple.com/documentation/kernel/kiopropertyscsiparallelsignalingtypelvdkey)Removed [#def kIOPropertySCSIParallelSignalingTypeSEKey](https://developer.apple.com/documentation/kernel/kiopropertyscsiparallelsignalingtypesekey)Removed [#def kIOPropertySCSIPortIdentifierKey](https://developer.apple.com/documentation/kernel/kiopropertyscsiportidentifierkey)IOKit/IOTypes.hAdded [kIOMapPrefault](https://developer.apple.com/documentation/kernel/1646291-anonymous/kiomapprefault)IOKit/usb/IOUSBCommand.hAdded IOUSBCommand::GetMasterUSBCommand()Added IOUSBCommand::GetUIMScratch64()Added IOUSBCommand::SetUIMScratch64()Added #def kUSBCommandScratch64BuffersIOKit/usb/IOUSBCompositeDriver.hAdded IOUSBCompositeDriver::FindConfigIndexFromPowerRequirements()Added IOUSBCompositeDriver::FindConfigIndexFromPreferredConfiguration()Added IOUSBCompositeDriver::FindConfigIndexFromPreferredInterface()Added IOUSBCompositeDriver::FindPreferredConfiguration()Added IOUSBCompositeDriver::GetConfigDescriptor()IOKit/usb/IOUSBControllerV2.hAdded #def kLowLatencyUSB32bitPhysicalMaskAdded #def kLowLatencyUSB64bitPhysicalMaskAdded #def kLowLatencyUSBDefaultOptionBitsIOKit/usb/IOUSBControllerV3.hAdded IOUSBControllerV3::DoNotPowerOffPortsOnStop()Added IOUSBControllerV3::GetPMCSR()Added IOUSBControllerV3::GetRootHubPowerExitLatencies()Added IOUSBControllerV3::UpdateThunderboltExtraCurrentiVars()Added IOUSBControllerV3::WaitForPCIPauseToFinish()Added IOUSBControllerV3::WakeUpCheckPowerModeThreadsGated()Added kCheckPowerModeOptionsUserSpaceRequestMaskAdded kMaxTransactionsDuringPCIPauseIOKit/usb/IOUSBDevice.hAdded [IOUSBControllerV3](https://developer.apple.com/documentation/kernel/iousbcontrollerv3)Added IOUSBDevice::GetDevicePowerParent()Added IOUSBDevice::GetInterfacePowerParent()Added IOUSBDevice::GetIsochDelay()Added IOUSBDevice::IsDeviceInternal()Added IOUSBDevice::SetIsochDelay()Added IOUSBDevice::TrimStringDescriptor()Added IOUSBDevice::joinPMtree()IOKit/usb/IOUSBHubPolicyMaker.hAdded IOUSBHubPolicyMaker::GetMinimumIdlePowerState()Added IOUSBHubPolicyMaker::GetPowerExitLatencies()Added IOUSBHubExitLatenciesAdded IOUSBHubExitLatencyStatesAdded #def kIOUSBHubExitLatenciesVersionAdded #def kIOUSBHubExitLatencyMaxIOKit/usb/IOUSBInterface.hAdded IOUSBInterface::joinPMtree()IOKit/usb/IOUSBLog.hAdded #def require_nonzeroAdded #def require_nonzero_actionAdded #def require_nonzero_stringAdded #def require_successAdded #def require_success_actionAdded #def require_success_action_quietAdded #def require_success_action_stringAdded #def require_success_quietAdded #def require_success_stringIOKit/usb/IOUSBMassStorageClass.hAdded #def fResetStatusModified IOUSBMassStorageClass::ResetDeviceNow()

|  | Declaration |
| --- | --- |
| From | ``` void ResetDeviceNow (	bool waitForReset); ``` |
| To | ``` IOReturn ResetDeviceNow (	bool waitForReset); ``` |

IOKit/usb/IOUSBNub.hRemoved IOUSBNub::joinPMtree()IOKit/usb/IOUSBUserClient.hAdded IOUSBNotification::GetToken()Added IOUSBNotification::SetToken()Added #def kIOUSBDeviceUserClientClassNameStrAdded #def kIOUSBDeviceUserClientTypeIDKeyAdded #def kIOUSBInterfaceUserClientClassNameStrAdded #def kIOUSBInterfaceUserClientTypeIDKeyAdded #def kIOUSBLibBundleNameAdded #def kNeedsDeviceAccessEntitlementAdded [kUSBInterfaceUserClientRegisterDriver](https://developer.apple.com/documentation/kernel/1646287-anonymous/kusbinterfaceuserclientregisterdriver)IOKit/IOUserClient.hAdded IOUserClient::clientHasAuthorization()Added IOUserClient::copyClientEntitlement()libkern/c++/OSEndianTypes.hAdded BigSInt16::operator=()Added BigSInt32::operator=()Added BigSInt64::operator=()Added BigUInt16::operator=()Added BigUInt32::operator=()Added BigUInt64::operator=()Added LittleSInt16::operator=()Added LittleSInt32::operator=()Added LittleSInt64::operator=()Added LittleUInt16::operator=()Added LittleUInt32::operator=()Added LittleUInt64::operator=()IOKit/OSMessageNotification.hRemoved [IOAsyncCompletionContent](https://developer.apple.com/documentation/kernel/ioasynccompletioncontent)Removed [IOServiceInterestContent](https://developer.apple.com/documentation/kernel/ioserviceinterestcontent)Removed [OSNotificationHeader](https://developer.apple.com/documentation/kernel/osnotificationheader)Added [kIOKitNoticationMsgSizeMask](https://developer.apple.com/documentation/iokit/kiokitnoticationmsgsizemask)Added [kIOKitNoticationTypeMask](https://developer.apple.com/documentation/kernel/1645646-anonymous/kiokitnoticationtypemask)Added [kIOKitNoticationTypeSizeAdjShift](https://developer.apple.com/documentation/iokit/kiokitnoticationtypesizeadjshift)libkern/c++/OSMetaClass.hAdded OSMetaClassBase::operator=()libkern/c++/OSSerialize.hAdded [OSCollection](https://developer.apple.com/documentation/kernel/oscollection)Added OSSerialize::addBinary()Added OSSerialize::addBinaryObject()Added OSSerialize::binarySerialize()Added OSSerialize::binaryWithCapacity()Added [OSUnserializeBinary()](https://developer.apple.com/documentation/kernel/1575008-osunserializebinary)libkern/c++/OSString.hAdded OSString::initWithStringOfLength()Added OSString::withStringOfLength()libkern/c++/OSUnserialize.hAdded [OSUnserializeBinary()](https://developer.apple.com/documentation/kernel/1575008-osunserializebinary)AppleDSP/OSvKernDSPLib.hAdded [cosf()](https://developer.apple.com/documentation/kernel/1532192-cosf)Added [sinf()](https://developer.apple.com/documentation/kernel/1532196-sinf)IOKit/pwr_mgt/RootDomain.hAdded IOPMrootDomain::claimSystemWakeEvent()Added IOPMrootDomain::restartWithStackshot()IOKit/usb/USB.hRemoved #def kThunderboltMaxBusStallAdded #def kAppleAcpiRootHubDepthAdded #def kAppleExternalConnectorBitmapAdded #def kIOUSBMessageHubCountExceededAdded #def kMaxBusStall10uSAdded #def kMaxBusStall25uSAdded [kSuperSpeedBusBitMask](https://developer.apple.com/documentation/iokit/1426312-anonymous/ksuperspeedbusbitmask)Added [kUSBDeviceCountExceededNotificationType](https://developer.apple.com/documentation/iokit/1426344-anonymous/kusbdevicecountexceedednotificationtype)Added [kUSBEndpointCountExceededNotificationType](https://developer.apple.com/documentation/iokit/1426344-anonymous/kusbendpointcountexceedednotificationtype)Added [kUSBEndpointTransferTypeUCMask](https://developer.apple.com/documentation/iokit/1426201-miscellaneous_constants/kusbendpointtransfertypeucmask)Added [kUSBHubCountExceededNotificationType](https://developer.apple.com/documentation/kernel/1646362-anonymous/kusbhubcountexceedednotificationtype)Added #def kUSBPreferredInterfaceAdded #def kUSBPreferredInterfacePriorityAdded [kUSBReEnumerateCaptureDeviceBit](https://developer.apple.com/documentation/kernel/usbreenumerateoptions/kusbreenumeratecapturedevicebit)Added [kUSBReEnumerateCaptureDeviceMask](https://developer.apple.com/documentation/iokit/usbreenumerateoptions/kusbreenumeratecapturedevicemask)Added [kUSBReEnumerateReleaseDeviceBit](https://developer.apple.com/documentation/kernel/usbreenumerateoptions/kusbreenumeratereleasedevicebit)Added [kUSBReEnumerateReleaseDeviceMask](https://developer.apple.com/documentation/iokit/usbreenumerateoptions/kusbreenumeratereleasedevicemask)Added [kUSBStreamIDAllStreamsMask](https://developer.apple.com/documentation/kernel/1646366-anonymous/kusbstreamidallstreamsmask)Added [kUSBStreamIDMask](https://developer.apple.com/documentation/kernel/1646366-anonymous/kusbstreamidmask)Added [kUSBTooManyDevicesAddress](https://developer.apple.com/documentation/iokit/1426201-miscellaneous_constants/kusbtoomanydevicesaddress)Added [kUSBUCRequestWithoutUSBNotificationMask](https://developer.apple.com/documentation/kernel/1646366-anonymous/kusbucrequestwithoutusbnotificationmask)IOKit/usb/USBSpec.hAdded #def kUSBSpecReleaseNumbervm/WKdm_new.hRemoved #def ALL_ONES_MASKRemoved #def BITS_PER_BYTERemoved #def BITS_PER_WORDRemoved #def BYTES_PER_WORDRemoved #def DEBUG_PRINT_1Removed #def DEBUG_PRINT_2Removed #def DICTIONARY_SIZERemoved DictionaryElementRemoved #def EMIT_BYTERemoved #def EMIT_WORDRemoved #def EXACT_TAGRemoved #def FOUR_BITS_PACKING_MASKRemoved #def FULL_WORD_AREA_STARTRemoved #def HASH_LOOKUP_TABLE_CONTENTSRemoved #def HASH_TO_DICT_BYTE_OFFSETRemoved #def HEADER_SIZE_IN_WORDSRemoved #def HIGH_BITSRemoved #def LOW_BITSRemoved #def LOW_BITS_AREA_ENDRemoved #def LOW_BITS_AREA_STARTRemoved #def LOW_BITS_MASKRemoved #def MISS_TAGRemoved #def NUM_LOW_BITSRemoved #def PAGE_SIZE_IN_BYTESRemoved #def PAGE_SIZE_IN_WORDSRemoved #def PARTIAL_TAGRemoved #def PRELOAD_DICTIONARYRemoved #def QPOS_AREA_ENDRemoved #def QPOS_AREA_STARTRemoved #def RECORD_EXACTRemoved #def RECORD_MISSRemoved #def RECORD_PARTIALRemoved #def RECORD_ZERORemoved #def SET_LOW_BITS_AREA_ENDRemoved #def SET_LOW_BITS_AREA_STARTRemoved #def SET_QPOS_AREA_STARTRemoved #def TAGS_AREA_ENDRemoved #def TAGS_AREA_OFFSETRemoved #def TAGS_AREA_SIZERemoved #def TAGS_AREA_STARTRemoved #def TEN_LOW_BITS_MASKRemoved #def TWENTY_TWO_HIGH_BITS_MASKRemoved #def TWO_BITS_PACKING_MASKRemoved #def ZERO_TAGRemoved hashLookupTablesys/_types/___offsetof.h (Removed)sys/_endian.hAdded #def HTONLLAdded #def NTOHLLAdded #def htonllAdded #def ntohllsys/_types/_fsid_t.h (Added)Modified [fsid_t](https://developer.apple.com/documentation/kernel/fsid_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/mount.h |
| To | Kernel/sys/_types/_fsid_t.h |

i386/_mcontext.hRemoved #def I386_MCONTEXT_SIZEsys/_types/_offsetof.h (Added)Modified #def offsetof

|  | Header |
| --- | --- |
| From | Kernel/sys/_types.h |
| To | Kernel/sys/_types/_offsetof.h |

sys/_types/_pthread_attr_t.h (Removed)Removed pthread_attr_tsys/_types/_pthread_cond_t.h (Removed)Removed pthread_cond_tsys/_types/_pthread_condattr_t.h (Removed)Removed pthread_condattr_tsys/_types/_pthread_key_t.h (Removed)Removed pthread_key_tsys/_types/_pthread_mutex_t.h (Removed)Removed pthread_mutex_tsys/_types/_pthread_mutexattr_t.h (Removed)Removed pthread_mutexattr_tsys/_types/_pthread_once_t.h (Removed)Removed pthread_once_tsys/_types/_pthread_rwlock_t.h (Removed)Removed pthread_rwlock_tsys/_types/_pthread_rwlockattr_t.h (Removed)Removed pthread_rwlockattr_tsys/_types/_pthread_t.h (Removed)Removed pthread_ti386/_structs.h (Removed)machine/_structs.h (Removed)atm/atm_types.h (Added)Added #def ATM_ACTION_COLLECTAdded #def ATM_ACTION_DISCARDAdded #def ATM_ACTION_LOGFAILAdded #def ATM_ACTION_UNREGISTERAdded #def ATM_FIND_MIN_SUB_AIDAdded #def ATM_SUBAID32_MAXAdded #def MACH_VOUCHER_ATTR_ATM_CREATEAdded #def MACH_VOUCHER_ATTR_ATM_NULLAdded #def MACH_VOUCHER_ATTR_ATM_REGISTERAdded #def SUB_AID_MAXAdded [aid_t](https://developer.apple.com/documentation/kernel/aid_t)Added [atm_action_t](https://developer.apple.com/documentation/kernel/atm_action_t)Added [atm_aid_t](https://developer.apple.com/documentation/kernel/atm_aid_t)Added [atm_mailbox_offset_t](https://developer.apple.com/documentation/kernel/atm_mailbox_offset_t)Added [atm_memory_descriptor_array_t](https://developer.apple.com/documentation/kernel/atm_memory_descriptor_array_t)Added [atm_memory_descriptor_t](https://developer.apple.com/documentation/kernel/atm_memory_descriptor_t)Added [atm_memory_size_array_t](https://developer.apple.com/documentation/kernel/atm_memory_size_array_t)Added [atm_subaid32_t](https://developer.apple.com/documentation/kernel/atm_subaid32_t)Added [mach_atm_subaid_t](https://developer.apple.com/documentation/kernel/mach_atm_subaid_t)Added [mailbox_offset_t](https://developer.apple.com/documentation/kernel/mailbox_offset_t)Added [subaid_t](https://developer.apple.com/documentation/kernel/subaid_t)sys/attr.hAdded #def ATTR_BULK_REQUIREDAdded #def ATTR_CMN_DATA_PROTECT_FLAGSAdded #def ATTR_CMN_DOCUMENT_IDAdded #def ATTR_CMN_ERRORAdded #def ATTR_CMN_GEN_COUNTAdded #def FSOPT_ATTR_CMN_EXTENDEDbank/bank_types.h (Added)Added #def BANK_ORIGINATOR_PIDAdded #def MACH_VOUCHER_ATTR_BANK_CREATEAdded #def MACH_VOUCHER_ATTR_BANK_NULLAdded #def MACH_VOUCHER_BANK_CONTENT_SIZEAdded [bank_action_t](https://developer.apple.com/documentation/kernel/bank_action_t)pexpert/i386/boot.hAdded #def kBootArgsFlagBlackBgAdded #def kBootArgsFlagCSRActiveConfigAdded #def kBootArgsFlagCSRBootAdded #def kBootArgsFlagCSRPendingConfigAdded #def kBootArgsFlagLoginUIkern/coalition.h (Added)mach/coalition_notification_server.h (Added)Added [coalition_notification()](https://developer.apple.com/documentation/kernel/1543358-coalition_notification)Added #def coalition_notification_MSG_COUNTAdded [coalition_notification_server()](https://developer.apple.com/documentation/kernel/1543361-coalition_notification_server)Added [coalition_notification_server_routine()](https://developer.apple.com/documentation/kernel/1543352-coalition_notification_server_ro)Added [coalition_notification_subsystem](https://developer.apple.com/documentation/kernel/coalition_notification_subsystem)Added [coalition_notification_subsystem](https://developer.apple.com/documentation/kernel/coalition_notification_subsystem-36b)Added #def subsystem_to_name_map_coalition_notificationi386/cpuid.hRemoved #def CPUID_LEAF7_FEATURE_ENFSTRGAdded #def CPUID_EXTFEATURE_LZCNTAdded #def CPUID_EXTFEATURE_PREFETCHWAdded #def CPUID_LEAF7_FEATURE_ERMSAdded #def CPUID_MODEL_CRYSTALWELLAdded #def CPUID_MODEL_IVYBRIDGE_EPAdded #def CPUID_VMM_FAMILY_PARALLELSAdded #def CPUID_VMM_ID_PARALLELSAdded #def CPUID_X86_64_H_EXTFEATURE_SUBSETAdded #def CPUID_X86_64_H_FEATURE_SUBSETAdded #def CPUID_X86_64_H_LEAF7_FEATURE_SUBSETkern/debug.hRemoved panic_active()Removed populate_model_name()Added STACKSHOT_GET_WINDOWED_MICROSTACKSHOTSAdded #def STACKSHOT_IO_NUM_PRIORITIESAdded #def STACKSHOT_MAX_THREAD_NAME_SIZEAdded [STACKSHOT_SAVE_IMP_DONATION_PIDS](https://developer.apple.com/documentation/kernel/1644204-anonymous/stackshot_save_imp_donation_pids)Added STACKSHOT_WINDOWED_MICROSTACKSHOTS_DISABLEAdded STACKSHOT_WINDOWED_MICROSTACKSHOTS_ENABLEAdded [kTaskIsImpDonor](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskisimpdonor)Added [kTaskIsLiveImpDonor](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskisliveimpdonor)Added [kThreadIOPassive](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kthreadiopassive)Added [kThreadSuspended](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kthreadsuspended)sys/disk.hRemoved #def DKIOCGETMAXPRIORITYCOUNTAdded #def DKIOCGETENCRYPTIONTYPEAdded #def DKIOCISLOWPOWERMODEAdded #def DKIOCSETTIERAdded #def DK_ENCRYPTION_TYPE_AES_CBCAdded #def DK_ENCRYPTION_TYPE_AES_XEXAdded #def DK_ENCRYPTION_TYPE_AES_XTSAdded #def DK_FEATURE_PRIORITYAdded #def DK_PRIORITY_TO_TIERAdded #def DK_TIER_MASKAdded #def DK_TIER_SHIFTAdded #def DK_TIER_TO_PRIORITYAdded [dk_set_tier_t](https://developer.apple.com/documentation/kernel/dk_set_tier_t)kern/ecc.h (Added)Added #def ECC_EVENT_INFO_DATA_ENTRIESAdded [ecc_event](https://developer.apple.com/documentation/kernel/ecc_event)kern/energy_perf.h (Added)Added #def GPU_SCOPE_CURRENT_THREADAdded #def GPU_SCOPE_MISCAdded #def IO_MEDIUM_ROTATINGAdded #def IO_MEDIUM_SOLID_STATEAdded #def IO_PRIORITY_LOWAdded #def IO_PRIORITY_PREDICTIVEAdded [gpu_accumulate_time()](https://developer.apple.com/documentation/kernel/1478468-gpu_accumulate_time)Added [gpu_describe()](https://developer.apple.com/documentation/kernel/1478509-gpu_describe)Added [gpu_descriptor](https://developer.apple.com/documentation/kernel/gpu_descriptor)Added [gpu_descriptor_t](https://developer.apple.com/documentation/kernel/gpu_descriptor_t)Added [io_rate_update()](https://developer.apple.com/documentation/kernel/1478470-io_rate_update)Added [io_rate_update_callback_t](https://developer.apple.com/documentation/kernel/io_rate_update_callback_t)Added [io_rate_update_register()](https://developer.apple.com/documentation/kernel/1478504-io_rate_update_register)kern/exc_resource.h (Added)Added #def EXC_RESOURCE_CPUMONITOR_DECODE_INTERVALAdded #def EXC_RESOURCE_CPUMONITOR_DECODE_OBSERVATION_INTERVALAdded #def EXC_RESOURCE_CPUMONITOR_DECODE_PERCENTAGEAdded #def EXC_RESOURCE_CPUMONITOR_DECODE_PERCENTAGE_OBSERVEDAdded #def EXC_RESOURCE_CPUMONITOR_DECODE_WAKEUPS_OBSERVEDAdded #def EXC_RESOURCE_CPUMONITOR_DECODE_WAKEUPS_PERMITTEDAdded #def EXC_RESOURCE_CPUMONITOR_ENCODE_INTERVALAdded #def EXC_RESOURCE_CPUMONITOR_ENCODE_OBSERVATION_INTERVALAdded #def EXC_RESOURCE_CPUMONITOR_ENCODE_PERCENTAGEAdded #def EXC_RESOURCE_CPUMONITOR_ENCODE_WAKEUPS_OBSERVEDAdded #def EXC_RESOURCE_CPUMONITOR_ENCODE_WAKEUPS_PERMITTEDAdded #def EXC_RESOURCE_DECODE_FLAVORAdded #def EXC_RESOURCE_DECODE_RESOURCE_TYPEAdded #def EXC_RESOURCE_ENCODE_FLAVORAdded #def EXC_RESOURCE_ENCODE_TYPEAdded #def EXC_RESOURCE_HWM_DECODE_LIMITAdded #def EXC_RESOURCE_HWM_ENCODE_LIMITAdded #def FLAVOR_CPU_MONITORAdded #def FLAVOR_CPU_MONITOR_FATALAdded #def FLAVOR_HIGH_WATERMARKAdded #def FLAVOR_WAKEUPS_MONITORAdded #def RESOURCE_TYPE_CPUAdded #def RESOURCE_TYPE_MEMORYAdded #def RESOURCE_TYPE_WAKEUPSsys/fcntl.hAdded #def AT_EACCESSAdded #def AT_FDCWDAdded #def AT_REMOVEDIRAdded #def AT_SYMLINK_FOLLOWAdded #def AT_SYMLINK_NOFOLLOWAdded #def F_GETCODEDIRAdded [user32_fcodeblobs_t](https://developer.apple.com/documentation/kernel/user32_fcodeblobs_t)Added [user64_fcodeblobs_t](https://developer.apple.com/documentation/kernel/user64_fcodeblobs_t)Added [user_fcodeblobs_t](https://developer.apple.com/documentation/kernel/user_fcodeblobs_t)mach/host_special_ports.hAdded #def HOST_ATM_NOTIFICATION_PORTAdded #def HOST_COALITION_PORTAdded #def host_get_atm_notification_portAdded #def host_get_coalition_portAdded #def host_set_atm_notification_portAdded #def host_set_coalition_portkern/hv_support.h (Added)Added [HV_DEBUG_STATE](https://developer.apple.com/documentation/kernel/hv_volatile_state_t/hv_debug_state)Added [HV_TASK_TRAP](https://developer.apple.com/documentation/kernel/hv_trap_type_t/hv_task_trap)Added [HV_THREAD_TRAP](https://developer.apple.com/documentation/kernel/hv_trap_type_t/hv_thread_trap)Added hv_callback_0_tAdded hv_callback_1_tAdded [hv_callbacks](https://developer.apple.com/documentation/kernel/hv_callbacks)Added [hv_callbacks_t](https://developer.apple.com/documentation/kernel/hv_callbacks_t)Added [hv_get_support()](https://developer.apple.com/documentation/kernel/1507081-hv_get_support)Added [hv_get_task_target()](https://developer.apple.com/documentation/kernel/1507096-hv_get_task_target)Added [hv_get_thread_target()](https://developer.apple.com/documentation/kernel/1507076-hv_get_thread_target)Added [hv_get_volatile_state()](https://developer.apple.com/documentation/kernel/1507077-hv_get_volatile_state)Added [hv_release_callbacks()](https://developer.apple.com/documentation/kernel/1507094-hv_release_callbacks)Added hv_release_mp_notify()Added [hv_release_traps()](https://developer.apple.com/documentation/kernel/1507113-hv_release_traps)Added [hv_set_callbacks()](https://developer.apple.com/documentation/kernel/1507074-hv_set_callbacks)Added hv_set_mp_notify()Added [hv_set_task_target()](https://developer.apple.com/documentation/kernel/1507070-hv_set_task_target)Added [hv_set_thread_target()](https://developer.apple.com/documentation/kernel/1507095-hv_set_thread_target)Added [hv_set_traps()](https://developer.apple.com/documentation/kernel/1507088-hv_set_traps)Added [hv_support_available](https://developer.apple.com/documentation/kernel/hv_support_available)Added [hv_support_init()](https://developer.apple.com/documentation/kernel/1507083-hv_support_init)Added [hv_task_trap()](https://developer.apple.com/documentation/kernel/1507105-hv_task_trap)Added [hv_thread_trap()](https://developer.apple.com/documentation/kernel/1507079-hv_thread_trap)Added [hv_trap_t](https://developer.apple.com/documentation/kernel/hv_trap_t)Added [hv_trap_table_t](https://developer.apple.com/documentation/kernel/hv_trap_table_t)Added [hv_trap_type_t](https://developer.apple.com/documentation/kernel/hv_trap_type_t)Added [hv_volatile_state_t](https://developer.apple.com/documentation/kernel/hv_volatile_state_t)net/if.hRemoved #def IFLR_PREFIXRemoved if_laddrreqAdded #def IFQ_TARGET_DELAYAdded #def IFQ_UPDATE_INTERVALAdded #def KEV_DL_AWDL_RESTRICTEDAdded #def KEV_DL_AWDL_UNRESTRICTEDnet/if_utun.hAdded #def UTUN_OPT_MAX_PENDING_PACKETSsys/imgact.hAdded #def IMGPF_VFORK_EXECnetinet6/ip6_mroute.h (Removed)netinet/ip_mroute.h (Removed)mach_debug/ipc_info.hAdded [ipc_info_space_basic_t](https://developer.apple.com/documentation/kernel/ipc_info_space_basic_t)sys/kdebug.hAdded #def ATM_CODEAdded #def ATM_GETVALUE_INFOAdded #def ATM_MIN_CALLEDAdded #def ATM_MIN_LINK_LISTAdded #def ATM_SUBAID_INFOAdded #def ATM_UNREGISTER_INFOAdded #def ATM_VALUE_ADDEDAdded #def ATM_VALUE_DIFF_MAILBOXAdded #def ATM_VALUE_REPLACEDAdded #def ATM_VALUE_UNREGISTEREDAdded #def BANK_ACCOUNT_INFOAdded #def BANK_CODEAdded #def BANK_SETTLE_CPU_TIMEAdded #def BANK_TASK_INFOAdded #def BSD_MEMSTAT_DIRTY_CLEARAdded #def BSD_MEMSTAT_DIRTY_SETAdded #def BSD_MEMSTAT_DIRTY_TRACKAdded #def DBG_ATMAdded #def DBG_BANKAdded #def DBG_CONTENT_PROTAdded #def DBG_MACH_ENERGY_PERFAdded #def DBG_MACH_SFIAdded #def DBG_NETVMNETAdded #def DBG_SEC_KERNELAdded #def DBG_WORKQUEUEAdded #def DBG_XPCAdded #def IMP_DONOR_CHANGEAdded #def IMP_DONOR_INIT_DONOR_STATEAdded #def IMP_DONOR_UPDATE_LIVE_DONOR_STATEAdded #def IMP_MAIN_THREAD_QOSAdded #def IMP_USYNCH_ADD_OVERRIDEAdded #def IMP_USYNCH_QOS_OVERRIDEAdded #def IMP_USYNCH_REMOVE_OVERRIDEAdded #def KERNEL_DEBUG_EARLYAdded #def MACH_DISPATCHAdded #def MACH_IPC_KMSG_FREEAdded #def MACH_IPC_MSG_RECVAdded #def MACH_IPC_MSG_RECV_VOUCHER_REFUSEDAdded #def MACH_IPC_MSG_SENDAdded #def MACH_IPC_VOUCHER_CREATEAdded #def MACH_IPC_VOUCHER_CREATE_ATTR_DATAAdded #def MACH_IPC_VOUCHER_DESTROYAdded #def MACH_MULTIQ_BOUNDAdded #def MACH_MULTIQ_DEQUEUEAdded #def MACH_MULTIQ_GLOBALAdded #def MACH_MULTIQ_GROUPAdded #def MACH_QUANTUM_HANDOFFAdded #def MACH_SCHED_MAINTENANCEAdded #def MACH_SCHED_SMT_BALANCEAdded #def MACH_SCHED_THREAD_SWITCHAdded #def MACH_THREAD_SET_VOUCHERAdded #def PMAP__FLUSH_TLBS_TOAdded #def SFI_CANCEL_CLASS_OFFTIMEAdded #def SFI_CANCEL_WINDOWAdded #def SFI_OFF_TIMERAdded #def SFI_ON_TIMERAdded #def SFI_PID_CLEAR_MANAGEDAdded #def SFI_PID_SET_MANAGEDAdded #def SFI_SET_CLASS_OFFTIMEAdded #def SFI_SET_WINDOWAdded #def SFI_THREAD_DEFERAdded #def SFI_WAIT_CANCELEDAdded #def TRACE_DATA_THREAD_TERMINATEAdded [kernel_debug_early()](https://developer.apple.com/documentation/kernel/1568942-kernel_debug_early)Added kernel_debug_string()sys/kern_memorystatus.h (Removed)Removed #def DEFAULT_JETSAM_PRIORITYRemoved #def DEFERRED_IDLE_EXIT_TIME_SECSRemoved #def JETSAM_PRIORITY_AUDIO_AND_ACCESSORYRemoved #def JETSAM_PRIORITY_BACKGROUNDRemoved #def JETSAM_PRIORITY_BACKGROUND_OPPORTUNISTICRemoved #def JETSAM_PRIORITY_CONDUCTORRemoved #def JETSAM_PRIORITY_CRITICALRemoved #def JETSAM_PRIORITY_DEFAULTRemoved #def JETSAM_PRIORITY_EXECUTIVERemoved #def JETSAM_PRIORITY_FOREGROUNDRemoved #def JETSAM_PRIORITY_FOREGROUND_SUPPORTRemoved #def JETSAM_PRIORITY_HOMERemoved #def JETSAM_PRIORITY_IDLERemoved #def JETSAM_PRIORITY_IDLE_DEFERREDRemoved #def JETSAM_PRIORITY_IMPORTANTRemoved #def JETSAM_PRIORITY_MAILRemoved #def JETSAM_PRIORITY_MAXRemoved #def JETSAM_PRIORITY_PHONERemoved #def JETSAM_PRIORITY_REVISIONRemoved #def JETSAM_PRIORITY_TELEPHONYRemoved #def JETSAM_PRIORITY_UI_SUPPORTRemoved #def KEV_MEMORYSTATUS_SUBCLASSRemoved #def MEMORYSTATUS_BUFFERSIZE_MAXRemoved #def MEMORYSTATUS_CMD_GET_JETSAM_SNAPSHOTRemoved #def MEMORYSTATUS_CMD_GET_PRESSURE_STATUSRemoved #def MEMORYSTATUS_CMD_GET_PRIORITY_LISTRemoved #def MEMORYSTATUS_CMD_SET_JETSAM_HIGH_WATER_MARKRemoved #def MEMORYSTATUS_CMD_SET_PRIORITY_PROPERTIESRemoved #def SYS_MEMORYSTATUS_HRemoved #def kMaxSnapshotEntriesRemoved #def kMemorystatusDirtyRemoved kMemorystatusFreezeNoteRemoved #def kMemorystatusFrozenRemoved kMemorystatusKilledRemoved kMemorystatusKilledDiagnosticRemoved kMemorystatusKilledHiwatRemoved kMemorystatusKilledIdleExitRemoved kMemorystatusKilledPerProcessLimitRemoved kMemorystatusKilledVMRemoved kMemorystatusKilledVMPageShortageRemoved kMemorystatusKilledVMThrashingRemoved kMemorystatusKilledVnodesRemoved kMemorystatusLevelAnyRemoved kMemorystatusLevelCriticalRemoved kMemorystatusLevelNormalRemoved kMemorystatusLevelNoteRemoved kMemorystatusLevelUrgentRemoved kMemorystatusLevelWarningRemoved kMemorystatusPressureNoteRemoved kMemorystatusSnapshotNoteRemoved #def kMemorystatusSupportsIdleExitRemoved #def kMemorystatusSuspendedRemoved #def kMemorystatusTrackedRemoved #def kMemorystatusWasThawedRemoved memorystatus_freeze_entry_tRemoved memorystatus_jetsam_snapshot_entry_tRemoved memorystatus_jetsam_snapshot_tRemoved memorystatus_kernel_stats_tRemoved memorystatus_priority_entry_tRemoved memorystatus_priority_properties_tmach/kern_return.hAdded #def KERN_POLICY_STATICkern/kern_types.hAdded #def TIMEOUT_URGENCY_RATELIMITEDkern/locks.hAdded #def LCK_SLEEP_PROMOTED_PRIsecurity/mac_mach_internal.hRemoved mac_port_check_method()Removed mac_port_label_compute()Removed mac_task_check_service()Removed mac_task_label_update_internal()mach/mach_host.hAdded [host_create_mach_voucher()](https://developer.apple.com/documentation/kernel/1502476-host_create_mach_voucher)Added [host_register_mach_voucher_attr_manager()](https://developer.apple.com/documentation/kernel/1502592-host_register_mach_voucher_attr_)Added [host_register_well_known_mach_voucher_attr_manager()](https://developer.apple.com/documentation/kernel/1502856-host_register_well_known_mach_vo)mach/mach_port.hAdded [mach_port_space_basic_info()](https://developer.apple.com/documentation/kernel/1578841-mach_port_space_basic_info)mach/mach_time.hAdded [mach_approximate_time()](https://developer.apple.com/documentation/kernel/1462443-mach_approximate_time)mach/mach_types.hAdded #def COALITION_NULLAdded [coalition_t](https://developer.apple.com/documentation/kernel/coalition_t)mach/mach_voucher.h (Added)Added #def mach_voucher_MSG_COUNTAdded [mach_voucher_attr_command()](https://developer.apple.com/documentation/kernel/1410145-mach_voucher_attr_command)Added [mach_voucher_debug_info()](https://developer.apple.com/documentation/kernel/1410149-mach_voucher_debug_info)Added [mach_voucher_extract_all_attr_recipes()](https://developer.apple.com/documentation/kernel/1410119-mach_voucher_extract_all_attr_re)Added [mach_voucher_extract_attr_content()](https://developer.apple.com/documentation/kernel/1410080-mach_voucher_extract_attr_conten)Added [mach_voucher_extract_attr_recipe()](https://developer.apple.com/documentation/kernel/1410137-mach_voucher_extract_attr_recipe)Added #def subsystem_to_name_map_mach_vouchermach/mach_voucher_attr_control.h (Added)Added #def mach_voucher_attr_control_MSG_COUNTAdded [mach_voucher_attr_control_create_mach_voucher()](https://developer.apple.com/documentation/kernel/1477870-mach_voucher_attr_control_create)Added [mach_voucher_attr_control_get_values()](https://developer.apple.com/documentation/kernel/1477865-mach_voucher_attr_control_get_va)Added #def subsystem_to_name_map_mach_voucher_attr_controlmach/mach_voucher_types.h (Added)Added #def IPC_VOUCHER_ATTR_CONTROL_NULLAdded #def IPC_VOUCHER_ATTR_MANAGER_NULLAdded #def IPC_VOUCHER_NULLAdded #def MACH_VOUCHER_ATTR_BITS_STOREAdded #def MACH_VOUCHER_ATTR_CONTROL_FLAGS_NONEAdded #def MACH_VOUCHER_ATTR_CONTROL_NULLAdded #def MACH_VOUCHER_ATTR_COPYAdded #def MACH_VOUCHER_ATTR_IMPORTANCE_SELFAdded #def MACH_VOUCHER_ATTR_KEY_ALLAdded #def MACH_VOUCHER_ATTR_KEY_ATMAdded #def MACH_VOUCHER_ATTR_KEY_BANKAdded #def MACH_VOUCHER_ATTR_KEY_BITSAdded #def MACH_VOUCHER_ATTR_KEY_IMPORTANCEAdded #def MACH_VOUCHER_ATTR_KEY_NONEAdded #def MACH_VOUCHER_ATTR_KEY_NUM_WELL_KNOWNAdded #def MACH_VOUCHER_ATTR_KEY_TESTAdded #def MACH_VOUCHER_ATTR_KEY_USER_DATAAdded #def MACH_VOUCHER_ATTR_MANAGER_NULLAdded #def MACH_VOUCHER_ATTR_NOOPAdded #def MACH_VOUCHER_ATTR_REDEEMAdded #def MACH_VOUCHER_ATTR_REMOVEAdded #def MACH_VOUCHER_ATTR_SET_VALUE_HANDLEAdded #def MACH_VOUCHER_ATTR_TEST_STOREAdded #def MACH_VOUCHER_ATTR_USER_DATA_STOREAdded #def MACH_VOUCHER_ATTR_VALUE_MAX_NESTEDAdded #def MACH_VOUCHER_IMPORTANCE_ATTR_ADD_EXTERNALAdded #def MACH_VOUCHER_IMPORTANCE_ATTR_DROP_EXTERNALAdded #def MACH_VOUCHER_NAME_ARRAY_NULLAdded #def MACH_VOUCHER_NAME_NULLAdded #def MACH_VOUCHER_NULLAdded #def MACH_VOUCHER_SELECTOR_CURRENTAdded #def MACH_VOUCHER_SELECTOR_EFFECTIVEAdded [ipc_voucher_attr_control_t](https://developer.apple.com/documentation/kernel/ipc_voucher_attr_control_t)Added [ipc_voucher_attr_manager_t](https://developer.apple.com/documentation/kernel/ipc_voucher_attr_manager_t)Added [ipc_voucher_t](https://developer.apple.com/documentation/kernel/ipc_voucher_t)Added [mach_voucher_attr_command_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_command_t)Added [mach_voucher_attr_content_size_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_content_size_t)Added [mach_voucher_attr_content_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_content_t)Added [mach_voucher_attr_control_flags_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_control_flags_t)Added [mach_voucher_attr_control_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_control_t)Added [mach_voucher_attr_importance_refs](https://developer.apple.com/documentation/kernel/mach_voucher_attr_importance_refs)Added [mach_voucher_attr_key_array_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_key_array_t)Added [mach_voucher_attr_key_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_key_t)Added [mach_voucher_attr_manager_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_manager_t)Added [mach_voucher_attr_raw_recipe_array_size_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_raw_recipe_array_size_t)Added [mach_voucher_attr_raw_recipe_array_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_raw_recipe_array_t)Added [mach_voucher_attr_raw_recipe_size_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_raw_recipe_size_t)Added [mach_voucher_attr_raw_recipe_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_raw_recipe_t)Added [mach_voucher_attr_recipe_command_array_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_recipe_command_array_t)Added [mach_voucher_attr_recipe_command_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_recipe_command_t)Added [mach_voucher_attr_recipe_data_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_recipe_data_t)Added [mach_voucher_attr_recipe_size_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_recipe_size_t)Added [mach_voucher_attr_recipe_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_recipe_t)Added [mach_voucher_attr_value_handle_array_size_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_value_handle_array_size_t)Added [mach_voucher_attr_value_handle_array_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_value_handle_array_t)Added [mach_voucher_attr_value_handle_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_value_handle_t)Added [mach_voucher_attr_value_reference_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_value_reference_t)Added [mach_voucher_name_array_t](https://developer.apple.com/documentation/kernel/mach_voucher_name_array_t)Added [mach_voucher_name_t](https://developer.apple.com/documentation/kernel/mach_voucher_name_t)Added [mach_voucher_selector_t](https://developer.apple.com/documentation/kernel/mach_voucher_selector_t)Added [mach_voucher_t](https://developer.apple.com/documentation/kernel/mach_voucher_t)mach/machine.hAdded #def CPUFAMILY_ARM_15Added #def CPUFAMILY_ARM_CYCLONEAdded #def CPU_SUBTYPE_ARM64_ALLAdded #def CPU_SUBTYPE_ARM64_V8Added #def CPU_SUBTYPE_ARM_V8Added #def CPU_SUBTYPE_X86_64_HAdded #def CPU_TYPE_ARM64math.h (Added)Added #def DOMAINAdded #def FP_ILOGB0Added #def FP_ILOGBNANAdded #def FP_INFINITEAdded #def FP_NANAdded #def FP_NORMALAdded #def FP_QNANAdded #def FP_SNANAdded #def FP_SUBNORMALAdded #def FP_SUPERNORMALAdded #def FP_ZEROAdded #def HUGEAdded #def HUGE_VALAdded #def HUGE_VALFAdded #def HUGE_VALLAdded #def INFINITYAdded #def MATH_ERREXCEPTAdded #def MATH_ERRNOAdded #def MAXFLOATAdded #def M_1_PIAdded #def M_2_PIAdded #def M_2_SQRTPIAdded #def M_EAdded #def M_LN10Added #def M_LN2Added #def M_LOG10EAdded #def M_LOG2EAdded #def M_PIAdded #def M_PI_2Added #def M_PI_4Added #def M_SQRT1_2Added #def M_SQRT2Added #def NANAdded #def OVERFLOWAdded #def PLOSSAdded #def SINGAdded #def TLOSSAdded #def UNDERFLOWAdded #def X_TLOSSAdded [acos()](https://developer.apple.com/documentation/kernel/1557251-acos)Added [acosf()](https://developer.apple.com/documentation/kernel/1557163-acosf)Added [acosh()](https://developer.apple.com/documentation/kernel/1557170-acosh)Added [acoshf()](https://developer.apple.com/documentation/kernel/1557276-acoshf)Added [acoshl()](https://developer.apple.com/documentation/kernel/1557266-acoshl)Added [acosl()](https://developer.apple.com/documentation/kernel/1557197-acosl)Added [asin()](https://developer.apple.com/documentation/kernel/1557225-asin)Added [asinf()](https://developer.apple.com/documentation/kernel/1557356-asinf)Added [asinh()](https://developer.apple.com/documentation/kernel/1557211-asinh)Added [asinhf()](https://developer.apple.com/documentation/kernel/1557278-asinhf)Added [asinhl()](https://developer.apple.com/documentation/kernel/1557157-asinhl)Added [asinl()](https://developer.apple.com/documentation/kernel/1557222-asinl)Added [atan()](https://developer.apple.com/documentation/kernel/1557165-atan)Added [atan2()](https://developer.apple.com/documentation/kernel/1557368-atan2)Added [atan2f()](https://developer.apple.com/documentation/kernel/1557144-atan2f)Added [atan2l()](https://developer.apple.com/documentation/kernel/1557326-atan2l)Added [atanf()](https://developer.apple.com/documentation/kernel/1557247-atanf)Added [atanh()](https://developer.apple.com/documentation/kernel/1557372-atanh)Added [atanhf()](https://developer.apple.com/documentation/kernel/1557262-atanhf)Added [atanhl()](https://developer.apple.com/documentation/kernel/1557230-atanhl)Added [atanl()](https://developer.apple.com/documentation/kernel/1557198-atanl)Added [cbrt()](https://developer.apple.com/documentation/kernel/1557257-cbrt)Added [cbrtf()](https://developer.apple.com/documentation/kernel/1557327-cbrtf)Added [cbrtl()](https://developer.apple.com/documentation/kernel/1557373-cbrtl)Added [ceil()](https://developer.apple.com/documentation/kernel/1557272-ceil)Added [ceilf()](https://developer.apple.com/documentation/kernel/1557263-ceilf)Added [ceill()](https://developer.apple.com/documentation/kernel/1557207-ceill)Added [copysign()](https://developer.apple.com/documentation/kernel/1557306-copysign)Added [copysignf()](https://developer.apple.com/documentation/kernel/1557234-copysignf)Added [copysignl()](https://developer.apple.com/documentation/kernel/1557294-copysignl)Added [cos()](https://developer.apple.com/documentation/kernel/1557361-cos)Added [cosf()](https://developer.apple.com/documentation/kernel/1532192-cosf)Added [cosh()](https://developer.apple.com/documentation/kernel/1557145-cosh)Added [coshf()](https://developer.apple.com/documentation/kernel/1557149-coshf)Added [coshl()](https://developer.apple.com/documentation/kernel/1557214-coshl)Added [cosl()](https://developer.apple.com/documentation/kernel/1557255-cosl)Added [double_t](https://developer.apple.com/documentation/kernel/double_t)Added [drem()](https://developer.apple.com/documentation/kernel/1557204-drem)Added [erf()](https://developer.apple.com/documentation/kernel/1557352-erf)Added [erfc()](https://developer.apple.com/documentation/kernel/1557322-erfc)Added [erfcf()](https://developer.apple.com/documentation/kernel/1557244-erfcf)Added [erfcl()](https://developer.apple.com/documentation/kernel/1557164-erfcl)Added [erff()](https://developer.apple.com/documentation/kernel/1557366-erff)Added [erfl()](https://developer.apple.com/documentation/kernel/1557285-erfl)Added [exp()](https://developer.apple.com/documentation/kernel/1557217-exp)Added [exp2()](https://developer.apple.com/documentation/kernel/1557304-exp2)Added [exp2f()](https://developer.apple.com/documentation/kernel/1557192-exp2f)Added [exp2l()](https://developer.apple.com/documentation/kernel/1557194-exp2l)Added [expf()](https://developer.apple.com/documentation/kernel/1532210-expf)Added [expl()](https://developer.apple.com/documentation/kernel/1557224-expl)Added [expm1()](https://developer.apple.com/documentation/kernel/1557227-expm1)Added [expm1f()](https://developer.apple.com/documentation/kernel/1557179-expm1f)Added [expm1l()](https://developer.apple.com/documentation/kernel/1557178-expm1l)Added [fabs()](https://developer.apple.com/documentation/kernel/1557277-fabs)Added [fabsf()](https://developer.apple.com/documentation/kernel/1557291-fabsf)Added [fabsl()](https://developer.apple.com/documentation/kernel/1557341-fabsl)Added [fdim()](https://developer.apple.com/documentation/kernel/1557355-fdim)Added [fdimf()](https://developer.apple.com/documentation/kernel/1557210-fdimf)Added [fdiml()](https://developer.apple.com/documentation/kernel/1557241-fdiml)Added [finite()](https://developer.apple.com/documentation/kernel/1557318-finite)Added [float_t](https://developer.apple.com/documentation/kernel/float_t)Added [floor()](https://developer.apple.com/documentation/kernel/1557338-floor)Added [floorf()](https://developer.apple.com/documentation/kernel/1557176-floorf)Added [floorl()](https://developer.apple.com/documentation/kernel/1557330-floorl)Added [fma()](https://developer.apple.com/documentation/kernel/1557233-fma)Added [fmaf()](https://developer.apple.com/documentation/kernel/1557358-fmaf)Added [fmal()](https://developer.apple.com/documentation/kernel/1557206-fmal)Added [fmax()](https://developer.apple.com/documentation/kernel/1557201-fmax)Added [fmaxf()](https://developer.apple.com/documentation/kernel/1557268-fmaxf)Added [fmaxl()](https://developer.apple.com/documentation/kernel/1557200-fmaxl)Added [fmin()](https://developer.apple.com/documentation/kernel/1557189-fmin)Added [fminf()](https://developer.apple.com/documentation/kernel/1557340-fminf)Added [fminl()](https://developer.apple.com/documentation/kernel/1557215-fminl)Added [fmod()](https://developer.apple.com/documentation/kernel/1557253-fmod)Added [fmodf()](https://developer.apple.com/documentation/kernel/1557354-fmodf)Added [fmodl()](https://developer.apple.com/documentation/kernel/1557237-fmodl)Added #def fpclassifyAdded [frexp()](https://developer.apple.com/documentation/kernel/1557221-frexp)Added [frexpf()](https://developer.apple.com/documentation/kernel/1557321-frexpf)Added [frexpl()](https://developer.apple.com/documentation/kernel/1557175-frexpl)Added [gamma()](https://developer.apple.com/documentation/kernel/1557256-gamma)Added [hypot()](https://developer.apple.com/documentation/kernel/1557147-hypot)Added [hypotf()](https://developer.apple.com/documentation/kernel/1557254-hypotf)Added [hypotl()](https://developer.apple.com/documentation/kernel/1557299-hypotl)Added [ilogb()](https://developer.apple.com/documentation/kernel/1557252-ilogb)Added [ilogbf()](https://developer.apple.com/documentation/kernel/1557293-ilogbf)Added [ilogbl()](https://developer.apple.com/documentation/kernel/1557245-ilogbl)Added #def isfiniteAdded #def isgreaterAdded #def isgreaterequalAdded #def isinfAdded #def islessAdded #def islessequalAdded #def islessgreaterAdded #def isnanAdded #def isnormalAdded #def isunorderedAdded [j0()](https://developer.apple.com/documentation/kernel/1557261-j0)Added [j1()](https://developer.apple.com/documentation/kernel/1557280-j1)Added [jn()](https://developer.apple.com/documentation/kernel/1557154-jn)Added [ldexp()](https://developer.apple.com/documentation/kernel/1557152-ldexp)Added [ldexpf()](https://developer.apple.com/documentation/kernel/1557190-ldexpf)Added [ldexpl()](https://developer.apple.com/documentation/kernel/1557365-ldexpl)Added [lgamma()](https://developer.apple.com/documentation/kernel/1557344-lgamma)Added [lgammaf()](https://developer.apple.com/documentation/kernel/1557160-lgammaf)Added [lgammal()](https://developer.apple.com/documentation/kernel/1557282-lgammal)Added [llrint()](https://developer.apple.com/documentation/kernel/1557360-llrint)Added [llrintf()](https://developer.apple.com/documentation/kernel/1557166-llrintf)Added [llrintl()](https://developer.apple.com/documentation/kernel/1557320-llrintl)Added [llround()](https://developer.apple.com/documentation/kernel/1557265-llround)Added [llroundf()](https://developer.apple.com/documentation/kernel/1557367-llroundf)Added [llroundl()](https://developer.apple.com/documentation/kernel/1557335-llroundl)Added [log()](https://developer.apple.com/documentation/kernel/1516025-log)Added [log10()](https://developer.apple.com/documentation/kernel/1557202-log10)Added [log10f()](https://developer.apple.com/documentation/kernel/1532188-log10f)Added [log10l()](https://developer.apple.com/documentation/kernel/1557363-log10l)Added [log1p()](https://developer.apple.com/documentation/kernel/1557187-log1p)Added [log1pf()](https://developer.apple.com/documentation/kernel/1557337-log1pf)Added [log1pl()](https://developer.apple.com/documentation/kernel/1557274-log1pl)Added [log2()](https://developer.apple.com/documentation/kernel/1557246-log2)Added [log2f()](https://developer.apple.com/documentation/kernel/1557332-log2f)Added [log2l()](https://developer.apple.com/documentation/kernel/1557169-log2l)Added [logb()](https://developer.apple.com/documentation/kernel/1557235-logb)Added [logbf()](https://developer.apple.com/documentation/kernel/1557288-logbf)Added [logbl()](https://developer.apple.com/documentation/kernel/1557168-logbl)Added [logf()](https://developer.apple.com/documentation/kernel/1532186-logf)Added [logl()](https://developer.apple.com/documentation/kernel/1557184-logl)Added [lrint()](https://developer.apple.com/documentation/kernel/1557305-lrint)Added [lrintf()](https://developer.apple.com/documentation/kernel/1557142-lrintf)Added [lrintl()](https://developer.apple.com/documentation/kernel/1557180-lrintl)Added [lround()](https://developer.apple.com/documentation/kernel/1557329-lround)Added [lroundf()](https://developer.apple.com/documentation/kernel/1557186-lroundf)Added [lroundl()](https://developer.apple.com/documentation/kernel/1557342-lroundl)Added #def math_errhandlingAdded [modf()](https://developer.apple.com/documentation/kernel/1557173-modf)Added [modff()](https://developer.apple.com/documentation/kernel/1557317-modff)Added [modfl()](https://developer.apple.com/documentation/kernel/1557161-modfl)Added [nan()](https://developer.apple.com/documentation/kernel/1557310-nan)Added [nanf()](https://developer.apple.com/documentation/kernel/1557309-nanf)Added [nanl()](https://developer.apple.com/documentation/kernel/1557311-nanl)Added [nearbyint()](https://developer.apple.com/documentation/kernel/1557212-nearbyint)Added [nearbyintf()](https://developer.apple.com/documentation/kernel/1557346-nearbyintf)Added [nearbyintl()](https://developer.apple.com/documentation/kernel/1557159-nearbyintl)Added [nextafter()](https://developer.apple.com/documentation/kernel/1557351-nextafter)Added [nextafterf()](https://developer.apple.com/documentation/kernel/1557315-nextafterf)Added [nextafterl()](https://developer.apple.com/documentation/kernel/1557308-nextafterl)Added [nexttoward()](https://developer.apple.com/documentation/kernel/1557273-nexttoward)Added [nexttowardf()](https://developer.apple.com/documentation/kernel/1557290-nexttowardf)Added [nexttowardl()](https://developer.apple.com/documentation/kernel/1557238-nexttowardl)Added [pow()](https://developer.apple.com/documentation/kernel/1557302-pow)Added [powf()](https://developer.apple.com/documentation/kernel/1557297-powf)Added [powl()](https://developer.apple.com/documentation/kernel/1557343-powl)Added [remainder()](https://developer.apple.com/documentation/kernel/1557314-remainder)Added [remainderf()](https://developer.apple.com/documentation/kernel/1557334-remainderf)Added [remainderl()](https://developer.apple.com/documentation/kernel/1557193-remainderl)Added [remquo()](https://developer.apple.com/documentation/kernel/1557171-remquo)Added [remquof()](https://developer.apple.com/documentation/kernel/1557226-remquof)Added [remquol()](https://developer.apple.com/documentation/kernel/1557307-remquol)Added [rint()](https://developer.apple.com/documentation/kernel/1557284-rint)Added [rintf()](https://developer.apple.com/documentation/kernel/1557348-rintf)Added [rintl()](https://developer.apple.com/documentation/kernel/1557349-rintl)Added [rinttol()](https://developer.apple.com/documentation/kernel/1557213-rinttol)Added [round()](https://developer.apple.com/documentation/kernel/1557369-round)Added [roundf()](https://developer.apple.com/documentation/kernel/1557316-roundf)Added [roundl()](https://developer.apple.com/documentation/kernel/1557143-roundl)Added [roundtol()](https://developer.apple.com/documentation/kernel/1557345-roundtol)Added [scalb()](https://developer.apple.com/documentation/kernel/1557195-scalb)Added [scalbln()](https://developer.apple.com/documentation/kernel/1557236-scalbln)Added [scalblnf()](https://developer.apple.com/documentation/kernel/1557182-scalblnf)Added [scalblnl()](https://developer.apple.com/documentation/kernel/1557371-scalblnl)Added [scalbn()](https://developer.apple.com/documentation/kernel/1557301-scalbn)Added [scalbnf()](https://developer.apple.com/documentation/kernel/1557209-scalbnf)Added [scalbnl()](https://developer.apple.com/documentation/kernel/1557350-scalbnl)Added #def signbitAdded [signgam](https://developer.apple.com/documentation/kernel/signgam)Added [significand()](https://developer.apple.com/documentation/kernel/1557303-significand)Added [sin()](https://developer.apple.com/documentation/kernel/1557267-sin)Added [sinf()](https://developer.apple.com/documentation/kernel/1532196-sinf)Added [sinh()](https://developer.apple.com/documentation/kernel/1557279-sinh)Added [sinhf()](https://developer.apple.com/documentation/kernel/1557250-sinhf)Added [sinhl()](https://developer.apple.com/documentation/kernel/1557240-sinhl)Added [sinl()](https://developer.apple.com/documentation/kernel/1557325-sinl)Added [sqrt()](https://developer.apple.com/documentation/kernel/1557357-sqrt)Added [sqrtf()](https://developer.apple.com/documentation/kernel/1532170-sqrtf)Added [sqrtl()](https://developer.apple.com/documentation/kernel/1557199-sqrtl)Added [tan()](https://developer.apple.com/documentation/kernel/1557150-tan)Added [tanf()](https://developer.apple.com/documentation/kernel/1557258-tanf)Added [tanh()](https://developer.apple.com/documentation/kernel/1557370-tanh)Added [tanhf()](https://developer.apple.com/documentation/kernel/1557286-tanhf)Added [tanhl()](https://developer.apple.com/documentation/kernel/1557188-tanhl)Added [tanl()](https://developer.apple.com/documentation/kernel/1557239-tanl)Added [tgamma()](https://developer.apple.com/documentation/kernel/1557229-tgamma)Added [tgammaf()](https://developer.apple.com/documentation/kernel/1557191-tgammaf)Added [tgammal()](https://developer.apple.com/documentation/kernel/1557205-tgammal)Added [trunc()](https://developer.apple.com/documentation/kernel/1557333-trunc)Added [truncf()](https://developer.apple.com/documentation/kernel/1557223-truncf)Added [truncl()](https://developer.apple.com/documentation/kernel/1557153-truncl)Added [y0()](https://developer.apple.com/documentation/kernel/1557220-y0)Added [y1()](https://developer.apple.com/documentation/kernel/1557331-y1)Added [yn()](https://developer.apple.com/documentation/kernel/1557339-yn)mach/memory_object_name.h (Removed)Removed #def memory_object_name_MSG_COUNTRemoved #def subsystem_to_name_map_memory_object_namemach/memory_object_types.hAdded #def UPL_COMMIT_WRITTEN_BY_KERNELAdded #def UPL_REQUEST_FORCE_COHERENCYAdded [upl_mark_decmp()](https://developer.apple.com/documentation/kernel/1562520-upl_mark_decmp)Added [upl_unmark_decmp()](https://developer.apple.com/documentation/kernel/1562507-upl_unmark_decmp)mach/message.hAdded #def MACH_MSGH_BITS_DENAPAdded #def MACH_MSGH_BITS_DENAPHOLDASRTAdded #def MACH_MSGH_BITS_HAS_LOCALAdded #def MACH_MSGH_BITS_HAS_REMOTEAdded #def MACH_MSGH_BITS_HAS_VOUCHERAdded #def MACH_MSGH_BITS_HOLDS_IMPORTANCE_ASSERTIONAdded #def MACH_MSGH_BITS_IS_COMPLEXAdded #def MACH_MSGH_BITS_RAISED_IMPORTANCEAdded #def MACH_MSGH_BITS_SETAdded #def MACH_MSGH_BITS_SET_PORTSAdded #def MACH_MSGH_BITS_VOUCHERAdded #def MACH_MSGH_BITS_VOUCHER_MASKAdded #def MACH_MSG_TYPE_DISPOSE_RECEIVEAdded #def MACH_MSG_TYPE_DISPOSE_SENDAdded #def MACH_MSG_TYPE_DISPOSE_SEND_ONCEAdded #def MACH_RCV_VOUCHERAdded #def MACH_SEND_INVALID_VOUCHERAdded #def MACH_SEND_NODENAPAdded #def msgh_reservedmach/mig_voucher_support.h (Added)sys/mount.hRemoved #def VFS_SET_PACKAGE_EXTSAdded #def VFS_CTL_NSTATUSAdded [netfs_status](https://developer.apple.com/documentation/kernel/netfs_status)pexpert/pexpert.hAdded [PE_get_random_seed()](https://developer.apple.com/documentation/kernel/1553647-pe_get_random_seed)Added #def kPERefreshBootGraphicsnetinet6/pim6.h (Removed)mach/port.hAdded #def MACH_PORT_DENAP_RECEIVERAdded #def MPO_DENAP_RECEIVERi386/proc_reg.hRemoved #def MSR_IA32_PROCBASED_CTLSRemoved #def MSR_IA32_VMXPINBASED_CTLSRemoved #def RDRAND_RAXAdded #def MSR_IA32_VMX_EPT_VPID_CAPAdded #def MSR_IA32_VMX_PINBASED_CTLSAdded #def MSR_IA32_VMX_PROCBASED_CTLSAdded #def MSR_IA32_VMX_PROCBASED_CTLS2Added #def MSR_IA32_VMX_TRUE_PINBASED_CTLSAdded #def MSR_IA32_VMX_TRUE_PROCBASED_CTLSAdded #def MSR_IA32_VMX_TRUE_VMENTRY_CTLSAdded #def MSR_IA32_VMX_TRUE_VMEXIT_CTLSAdded #def MSR_IA32_VMX_VMCS_ENUMAdded #def MSR_IA32_VMX_VMFUNCAdded #def rdtsc_nofencesys/resource.hRemoved rusage_info_diskiobytesAdded #def RLIMIT_THREAD_CPULIMITSAdded #def RUSAGE_INFO_V3Added [rusage_info_current](https://developer.apple.com/documentation/kernel/rusage_info_current)mach/security.h (Removed)Removed [mac_check_service()](https://developer.apple.com/documentation/kernel/security.defs/1808290-mac_check_service)Removed [mac_label_new()](https://developer.apple.com/documentation/kernel/security.defs/1808296-mac_label_new)Removed [mac_port_check_access()](https://developer.apple.com/documentation/kernel/security.defs/1808299-mac_port_check_access)Removed [mac_port_check_service_obj()](https://developer.apple.com/documentation/kernel/security.defs/1808303-mac_port_check_service_obj)Removed [mac_request_label()](https://developer.apple.com/documentation/kernel/security.defs/1808307-mac_request_label)Removed [mach_get_label()](https://developer.apple.com/documentation/kernel/security.defs/1808308-mach_get_label)Removed [mach_get_label_text()](https://developer.apple.com/documentation/kernel/security.defs/1808309-mach_get_label_text)Removed [mach_get_task_label()](https://developer.apple.com/documentation/kernel/security.defs/1808312-mach_get_task_label)Removed [mach_get_task_label_text()](https://developer.apple.com/documentation/kernel/security.defs/1808314-mach_get_task_label_text)Removed [mach_set_port_label()](https://developer.apple.com/documentation/kernel/security.defs/1808317-mach_set_port_label)Removed #def security_MSG_COUNTRemoved #def subsystem_to_name_map_securityi386/setjmp.h (Removed)Removed jmp_bufRemoved longjmp()Removed longjmperror()Removed setjmp()Removed sigjmp_bufRemoved siglongjmp()Removed sigsetjmp()kern/sfi.h (Added)mach/shared_region.hAdded #def SHARED_REGION_BASE_ARM64Added #def SHARED_REGION_NESTING_BASE_ARM64Added #def SHARED_REGION_NESTING_MAX_ARM64Added #def SHARED_REGION_NESTING_MIN_ARM64Added #def SHARED_REGION_NESTING_SIZE_ARM64Added #def SHARED_REGION_SIZE_ARM64sys/signal.hRemoved sigeventsys/socket.hRemoved user32_msghdrRemoved user64_msghdrRemoved user_msghdrAdded #def SO_NUMRCVPKTsys/sockio.hRemoved #def SIOCALIFADDRRemoved #def SIOCDLIFADDRRemoved #def SIOCGETSGCNTRemoved #def SIOCGETVIFCNTRemoved #def SIOCGLIFADDRRemoved #def SIOCGLIFPHYADDRRemoved #def SIOCSLIFPHYADDRsys/stat.hAdded #def SF_RESTRICTEDstdint.hRemoved #def RSIZE_MAXsys/stdio.h (Added)sys/syscall.hRemoved #def SYS___sysctlRemoved #def SYS_sem_destroyRemoved #def SYS_sem_getvalueRemoved #def SYS_sem_initAdded #def SYS_bsdthread_ctlAdded #def SYS_coalitionAdded #def SYS_coalition_infoAdded #def SYS_csrctlAdded #def SYS_faccessatAdded #def SYS_fchmodatAdded #def SYS_fchownatAdded #def SYS_fstatatAdded #def SYS_fstatat64Added #def SYS_getattrlistatAdded #def SYS_getattrlistbulkAdded #def SYS_guarded_open_dprotected_npAdded #def SYS_guarded_pwrite_npAdded #def SYS_guarded_write_npAdded #def SYS_guarded_writev_npAdded #def SYS_linkatAdded #def SYS_mkdiratAdded #def SYS_mremap_encryptedAdded #def SYS_necp_match_policyAdded #def SYS_openatAdded #def SYS_openat_nocancelAdded #def SYS_openbyid_npAdded #def SYS_pid_hibernateAdded #def SYS_pid_shutdown_socketsAdded #def SYS_proc_trace_logAdded #def SYS_readlinkatAdded #def SYS_recvmsg_xAdded #def SYS_rename_extAdded #def SYS_renameatAdded #def SYS_sendmsg_xAdded #def SYS_sfi_ctlAdded #def SYS_sfi_pidctlAdded #def SYS_symlinkatAdded #def SYS_sysctlAdded #def SYS_sysctlbynameAdded #def SYS_thread_selfusageAdded #def SYS_unlinkatsys/sysctl.hAdded #def SYSCTL_STRUCT_INITsys/systm.hAdded [throttle_info_disable_throttle()](https://developer.apple.com/documentation/kernel/1519606-throttle_info_disable_throttle)mach/task.hAdded [task_get_mach_voucher()](https://developer.apple.com/documentation/kernel/1537867-task_get_mach_voucher)Added [task_set_mach_voucher()](https://developer.apple.com/documentation/kernel/1538121-task_set_mach_voucher)Added [task_swap_mach_voucher()](https://developer.apple.com/documentation/kernel/1537722-task_swap_mach_voucher)mach/task_info.hAdded #def TASK_POWER_INFO_V2Added #def TASK_POWER_INFO_V2_COUNTAdded #def TASK_TRACE_MEMORY_INFOAdded #def TASK_TRACE_MEMORY_INFO_COUNTAdded #def TASK_WAIT_STATE_INFOAdded #def TASK_WAIT_STATE_INFO_COUNTAdded [gpu_energy_data](https://developer.apple.com/documentation/kernel/gpu_energy_data)Added [gpu_energy_data_t](https://developer.apple.com/documentation/kernel/gpu_energy_data_t)Added [task_power_info_v2_data_t](https://developer.apple.com/documentation/kernel/task_power_info_v2_data_t)Added [task_power_info_v2_t](https://developer.apple.com/documentation/kernel/task_power_info_v2_t)Added [task_trace_memory_info_data_t](https://developer.apple.com/documentation/kernel/task_trace_memory_info_data_t)Added [task_trace_memory_info_t](https://developer.apple.com/documentation/kernel/task_trace_memory_info_t)Added [task_wait_state_info_data_t](https://developer.apple.com/documentation/kernel/task_wait_state_info_data_t)Added [task_wait_state_info_t](https://developer.apple.com/documentation/kernel/task_wait_state_info_t)mach/task_policy.hAdded #def PROC_FLAG_APPLICATIONAdded #def TASK_BASE_LATENCY_QOS_POLICYAdded #def TASK_BASE_THROUGHPUT_QOS_POLICYmach/task_special_ports.hAdded #def TASK_DEBUG_CONTROL_PORTAdded #def task_get_debug_control_portAdded #def task_set_task_debug_control_portnetinet/tcp.hAdded #def TCP_ENABLE_ECNAdded #def TCP_NOTSENT_LOWATkern/telemetry.hAdded #def TELEMETRY_CMD_VOUCHER_NAMEAdded #def TELEMETRY_CMD_VOUCHER_STAINAdded bootprofile_wake_from_sleep()Added compute_telemetry_windowed()Added telemetry_disable_window()Added telemetry_enable_window()Added telemetry_gather_windowed()Added telemetry_window_enabledModified telemetry_ast()

|  | Declaration |
| --- | --- |
| From | ``` void telemetry_ast (	thread_t,	boolean_t interrupted_userspace); ``` |
| To | ``` void telemetry_ast (	thread_t,	boolean_t interrupted_userspace,	boolean_t is_windowed); ``` |

kern/thread.hAdded [thread_tid()](https://developer.apple.com/documentation/kernel/1429091-thread_tid)mach/thread_act.hAdded [thread_get_mach_voucher()](https://developer.apple.com/documentation/kernel/1418540-thread_get_mach_voucher)Added [thread_set_mach_voucher()](https://developer.apple.com/documentation/kernel/1418834-thread_set_mach_voucher)Added [thread_swap_mach_voucher()](https://developer.apple.com/documentation/kernel/1418678-thread_swap_mach_voucher)mach/thread_info.hAdded #def IO_NUM_PRIORITIESAdded [io_stat_entry](https://developer.apple.com/documentation/kernel/io_stat_entry)Added [io_stat_info_t](https://developer.apple.com/documentation/kernel/io_stat_info_t)mach/thread_policy.hAdded #def THREAD_LATENCY_QOS_POLICYAdded #def THREAD_LATENCY_QOS_POLICY_COUNTAdded #def THREAD_THROUGHPUT_QOS_POLICYAdded #def THREAD_THROUGHPUT_QOS_POLICY_COUNTAdded [thread_latency_qos_policy_data_t](https://developer.apple.com/documentation/kernel/thread_latency_qos_policy_data_t)Added [thread_latency_qos_policy_t](https://developer.apple.com/documentation/kernel/thread_latency_qos_policy_t)Added [thread_latency_qos_t](https://developer.apple.com/documentation/kernel/thread_latency_qos_t)Added [thread_throughput_qos_policy_data_t](https://developer.apple.com/documentation/kernel/thread_throughput_qos_policy_data_t)Added [thread_throughput_qos_policy_t](https://developer.apple.com/documentation/kernel/thread_throughput_qos_policy_t)Added [thread_throughput_qos_t](https://developer.apple.com/documentation/kernel/thread_throughput_qos_t)sys/ubc.hRemoved ubc_sync_range()vecLib/vBasicOps.h (Added)Added [vA128Shift()](https://developer.apple.com/documentation/accelerate/1442963-va128shift)Added [vLL128Shift()](https://developer.apple.com/documentation/kernel/1411104-vll128shift)Added [vLR128Shift()](https://developer.apple.com/documentation/kernel/1411111-vlr128shift)Added [vS128Add()](https://developer.apple.com/documentation/accelerate/1442956-vs128add)Added [vS128AddS()](https://developer.apple.com/documentation/accelerate/1442977-vs128adds)Added [vS128Sub()](https://developer.apple.com/documentation/kernel/1411118-vs128sub)Added [vS128SubS()](https://developer.apple.com/documentation/accelerate/1442914-vs128subs)Added [vS64FullMulOdd()](https://developer.apple.com/documentation/kernel/1411122-vs64fullmulodd)Added [vS64SubS()](https://developer.apple.com/documentation/kernel/1411100-vs64subs)Added [vU128Add()](https://developer.apple.com/documentation/kernel/1411106-vu128add)Added [vU128AddS()](https://developer.apple.com/documentation/kernel/1411102-vu128adds)Added [vU128Sub()](https://developer.apple.com/documentation/accelerate/1442884-vu128sub)Added [vU128SubS()](https://developer.apple.com/documentation/accelerate/1442931-vu128subs)Added [vU64FullMulOdd()](https://developer.apple.com/documentation/kernel/1411109-vu64fullmulodd)vecLib/vDSP.hAdded [vDSP_biquadm()](https://developer.apple.com/documentation/accelerate/1450603-vdsp_biquadm)Added [vDSP_biquadmD()](https://developer.apple.com/documentation/accelerate/1450102-vdsp_biquadmd)Added [vDSP_biquadm_CopyState()](https://developer.apple.com/documentation/kernel/1579980-vdsp_biquadm_copystate)Added [vDSP_biquadm_CopyStateD()](https://developer.apple.com/documentation/kernel/1580000-vdsp_biquadm_copystated)Added [vDSP_biquadm_CreateSetup()](https://developer.apple.com/documentation/kernel/1579945-vdsp_biquadm_createsetup)Added [vDSP_biquadm_CreateSetupD()](https://developer.apple.com/documentation/accelerate/1449719-vdsp_biquadm_createsetupd)Added [vDSP_biquadm_DestroySetup()](https://developer.apple.com/documentation/kernel/1579970-vdsp_biquadm_destroysetup)Added [vDSP_biquadm_DestroySetupD()](https://developer.apple.com/documentation/accelerate/1450779-vdsp_biquadm_destroysetupd)Added [vDSP_biquadm_ResetState()](https://developer.apple.com/documentation/accelerate/1449898-vdsp_biquadm_resetstate)Added [vDSP_biquadm_ResetStateD()](https://developer.apple.com/documentation/kernel/1579935-vdsp_biquadm_resetstated)Added [vDSP_biquadm_SetupD](https://developer.apple.com/documentation/kernel/vdsp_biquadm_setupd)Added [vDSP_conv()](https://developer.apple.com/documentation/kernel/1532184-vdsp_conv)Added [vDSP_deq22()](https://developer.apple.com/documentation/kernel/1532225-vdsp_deq22)Added [vDSP_maxmgv()](https://developer.apple.com/documentation/kernel/1532187-vdsp_maxmgv)Added [vDSP_maxv()](https://developer.apple.com/documentation/kernel/1580003-vdsp_maxv)Added [vDSP_minv()](https://developer.apple.com/documentation/accelerate/1450267-vdsp_minv)Added [vDSP_rmsqv()](https://developer.apple.com/documentation/accelerate/1450655-vdsp_rmsqv)Added [vDSP_svdiv()](https://developer.apple.com/documentation/accelerate/1450412-vdsp_svdiv)Added [vDSP_sve_svesq()](https://developer.apple.com/documentation/kernel/1579989-vdsp_sve_svesq)Added [vDSP_svesq()](https://developer.apple.com/documentation/accelerate/1450392-vdsp_svesq)Added [vDSP_svs()](https://developer.apple.com/documentation/kernel/1532174-vdsp_svs)Added [vDSP_vabs()](https://developer.apple.com/documentation/kernel/1532216-vdsp_vabs)Added [vDSP_vdiv()](https://developer.apple.com/documentation/accelerate/1450243-vdsp_vdiv)Added [vDSP_vfill()](https://developer.apple.com/documentation/kernel/1579967-vdsp_vfill)Added [vDSP_vma()](https://developer.apple.com/documentation/kernel/1532193-vdsp_vma)Added [vDSP_vmaxmg()](https://developer.apple.com/documentation/accelerate/1450295-vdsp_vmaxmg)Added [vDSP_vmul()](https://developer.apple.com/documentation/accelerate/1450344-vdsp_vmul)Added [vDSP_vsadd()](https://developer.apple.com/documentation/kernel/1579993-vdsp_vsadd)Added [vDSP_vsmul()](https://developer.apple.com/documentation/kernel/1532223-vdsp_vsmul)Added [vDSP_vsub()](https://developer.apple.com/documentation/accelerate/1449900-vdsp_vsub)Added [vDSP_vswmax()](https://developer.apple.com/documentation/kernel/1579990-vdsp_vswmax)Added [vDSP_zmmul()](https://developer.apple.com/documentation/accelerate/1449712-vdsp_zmmul)Added [vDSP_zvdiv()](https://developer.apple.com/documentation/accelerate/1449769-vdsp_zvdiv)Added [vDSP_zvmov()](https://developer.apple.com/documentation/kernel/1579979-vdsp_zvmov)Added [vDSP_zvmul()](https://developer.apple.com/documentation/kernel/1579954-vdsp_zvmul)vecLib/vForce.h (Added)Added [vvexpf()](https://developer.apple.com/documentation/kernel/1532176-vvexpf)vecLib/vecLibTypes.h (Added)Added [vBool32](https://developer.apple.com/documentation/kernel/vbool32)Added [vDouble](https://developer.apple.com/documentation/kernel/vdouble)Added [vFloat](https://developer.apple.com/documentation/kernel/vfloat)Added [vSInt16](https://developer.apple.com/documentation/kernel/vsint16)Added [vSInt32](https://developer.apple.com/documentation/kernel/vsint32)Added [vSInt64](https://developer.apple.com/documentation/kernel/vsint64)Added [vSInt8](https://developer.apple.com/documentation/kernel/vsint8)Added [vUInt16](https://developer.apple.com/documentation/kernel/vuint16)Added [vUInt32](https://developer.apple.com/documentation/kernel/vuint32)Added [vUInt64](https://developer.apple.com/documentation/kernel/vuint64)Added [vUInt8](https://developer.apple.com/documentation/kernel/vuint8)vm/vm_options.hAdded #def VM_OBJECT_TRACKINGAdded #def VM_PAGE_BUCKETS_CHECKAdded #def VM_SCAN_FOR_SHADOW_CHAINmach/i386/vm_param.hAdded #def PAGE_MAX_MASKAdded #def PAGE_MAX_SHIFTAdded #def PAGE_MAX_SIZEAdded #def PAGE_MIN_MASKAdded #def PAGE_MIN_SHIFTAdded #def PAGE_MIN_SIZEmach/vm_statistics.hAdded #def VM_MEMORY_COREUIFILEAdded #def VM_MEMORY_GENEALOGYsys/vnode.hRemoved #def DOWHITEOUTRemoved #def ISWHITEOUTRemoved #def NOTRIGGERRemoved #def VNODE_LOOKUP_DOWHITEOUTRemoved VT_UNIONAdded #def IO_SKIP_ENCRYPTIONAdded #def VATTR_CLEAR_SUPPORTED_ALLAdded #def VNODE_ATTR_va_devidAdded #def VNODE_ATTR_va_document_idAdded #def VNODE_ATTR_va_finderinfoAdded #def VNODE_ATTR_va_fsid64Added #def VNODE_ATTR_va_objtagAdded #def VNODE_ATTR_va_objtypeAdded #def VNODE_ATTR_va_rsrc_allocAdded #def VNODE_ATTR_va_rsrc_lengthAdded #def VNODE_ATTR_va_user_accessAdded #def VNODE_ATTR_va_write_gencountAdded [VT_MOCKFS](https://developer.apple.com/documentation/kernel/vtagtype/vt_mockfs)Added [vfs_attr_pack()](https://developer.apple.com/documentation/kernel/1562242-vfs_attr_pack)Added [vfs_setup_vattr_from_attrlist()](https://developer.apple.com/documentation/kernel/1562135-vfs_setup_vattr_from_attrlist)Added [vnode_cleardirty()](https://developer.apple.com/documentation/kernel/1562294-vnode_cleardirty)Added [vnode_isdirty()](https://developer.apple.com/documentation/kernel/1562357-vnode_isdirty)Added [vnode_setdirty()](https://developer.apple.com/documentation/kernel/1562289-vnode_setdirty)sys/vnode_if.hAdded [vnop_getattrlistbulk_args](https://developer.apple.com/documentation/kernel/vnop_getattrlistbulk_args)Added [vnop_getattrlistbulk_desc](https://developer.apple.com/documentation/kernel/vnop_getattrlistbulk_desc)

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
