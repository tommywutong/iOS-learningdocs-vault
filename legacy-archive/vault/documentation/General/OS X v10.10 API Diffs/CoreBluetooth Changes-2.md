---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/CoreBluetooth.html
archived_at: '2026-07-15T07:34:51.269561Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# CoreBluetooth Changes

## CoreBluetooth (Added)

Added CBATTError [enum]Added CBATTError.AttributeNotFoundAdded CBATTError.AttributeNotLongAdded CBATTError.InsufficientAuthenticationAdded CBATTError.InsufficientAuthorizationAdded CBATTError.InsufficientEncryptionAdded CBATTError.InsufficientEncryptionKeySizeAdded CBATTError.InsufficientResourcesAdded CBATTError.InvalidAttributeValueLengthAdded CBATTError.InvalidHandleAdded CBATTError.InvalidOffsetAdded CBATTError.InvalidPduAdded CBATTError.PrepareQueueFullAdded CBATTError.ReadNotPermittedAdded CBATTError.RequestNotSupportedAdded CBATTError.SuccessAdded CBATTError.UnlikelyErrorAdded CBATTError.UnsupportedGroupTypeAdded CBATTError.WriteNotPermittedAdded CBATTRequestAdded CBATTRequest.centralAdded CBATTRequest.characteristicAdded CBATTRequest.offsetAdded CBATTRequest.valueAdded CBAttributePermissions [enum]Added CBAttributePermissions.ReadEncryptionRequiredAdded CBAttributePermissions.ReadableAdded CBAttributePermissions.WriteEncryptionRequiredAdded CBAttributePermissions.WriteableAdded CBCentralAdded CBCentral.identifierAdded CBCentral.maximumUpdateValueLengthAdded CBCentralManagerAdded CBCentralManager.cancelPeripheralConnection(CBPeripheral!)Added CBCentralManager.connectPeripheral(CBPeripheral!, options:[NSObject: AnyObject]!)Added CBCentralManager.delegateAdded CBCentralManager.init(delegate: CBCentralManagerDelegate!, queue: dispatch_queue_t!)Added CBCentralManager.init(delegate: CBCentralManagerDelegate!, queue: dispatch_queue_t!, options:[NSObject: AnyObject]!)Added CBCentralManager.retrieveConnectedPeripheralsWithServices([AnyObject]!) -> [AnyObject]!Added CBCentralManager.retrievePeripheralsWithIdentifiers([AnyObject]!) -> [AnyObject]!Added CBCentralManager.scanForPeripheralsWithServices([AnyObject]!, options:[NSObject: AnyObject]!)Added CBCentralManager.stateAdded CBCentralManager.stopScan()Added CBCentralManagerDelegateAdded CBCentralManagerDelegate.centralManager(CBCentralManager!, didConnectPeripheral: CBPeripheral!)Added CBCentralManagerDelegate.centralManager(CBCentralManager!, didDisconnectPeripheral: CBPeripheral!, error: NSError!)Added CBCentralManagerDelegate.centralManager(CBCentralManager!, didDiscoverPeripheral: CBPeripheral!, advertisementData:[NSObject: AnyObject]!, RSSI: NSNumber!)Added CBCentralManagerDelegate.centralManager(CBCentralManager!, didFailToConnectPeripheral: CBPeripheral!, error: NSError!)Added CBCentralManagerDelegate.centralManager(CBCentralManager!, didRetrieveConnectedPeripherals:[AnyObject]!)Added CBCentralManagerDelegate.centralManager(CBCentralManager!, didRetrievePeripherals:[AnyObject]!)Added CBCentralManagerDelegate.centralManager(CBCentralManager!, willRestoreState:[NSObject: AnyObject]!)Added CBCentralManagerDelegate.centralManagerDidUpdateState(CBCentralManager!)Added CBCentralManagerState [enum]Added CBCentralManagerState.PoweredOffAdded CBCentralManagerState.PoweredOnAdded CBCentralManagerState.ResettingAdded CBCentralManagerState.UnauthorizedAdded CBCentralManagerState.UnknownAdded CBCentralManagerState.UnsupportedAdded CBCharacteristicAdded CBCharacteristic.UUIDAdded CBCharacteristic.descriptorsAdded CBCharacteristic.isBroadcastedAdded CBCharacteristic.isNotifyingAdded CBCharacteristic.propertiesAdded CBCharacteristic.serviceAdded CBCharacteristic.valueAdded CBCharacteristicProperties [enum]Added CBCharacteristicProperties.AuthenticatedSignedWritesAdded CBCharacteristicProperties.BroadcastAdded CBCharacteristicProperties.ExtendedPropertiesAdded CBCharacteristicProperties.IndicateAdded CBCharacteristicProperties.IndicateEncryptionRequiredAdded CBCharacteristicProperties.NotifyAdded CBCharacteristicProperties.NotifyEncryptionRequiredAdded CBCharacteristicProperties.ReadAdded CBCharacteristicProperties.WriteAdded CBCharacteristicProperties.WriteWithoutResponseAdded CBCharacteristicWriteType [enum]Added CBCharacteristicWriteType.WithResponseAdded CBCharacteristicWriteType.WithoutResponseAdded CBDescriptorAdded CBDescriptor.UUIDAdded CBDescriptor.characteristicAdded CBDescriptor.valueAdded CBError [enum]Added CBError.AlreadyAdvertisingAdded CBError.ConnectionTimeoutAdded CBError.InvalidHandleAdded CBError.InvalidParametersAdded CBError.NotConnectedAdded CBError.OperationCancelledAdded CBError.OutOfSpaceAdded CBError.PeripheralDisconnectedAdded CBError.UUIDNotAllowedAdded CBError.UnknownAdded CBMutableCharacteristicAdded CBMutableCharacteristic.UUIDAdded CBMutableCharacteristic.descriptorsAdded CBMutableCharacteristic.permissionsAdded CBMutableCharacteristic.propertiesAdded CBMutableCharacteristic.subscribedCentralsAdded CBMutableCharacteristic.init(type: CBUUID!, properties: CBCharacteristicProperties, value: NSData!, permissions: CBAttributePermissions)Added CBMutableCharacteristic.valueAdded CBMutableDescriptorAdded CBMutableDescriptor.init(type: CBUUID!, value: AnyObject!)Added CBMutableServiceAdded CBMutableService.UUIDAdded CBMutableService.characteristicsAdded CBMutableService.includedServicesAdded CBMutableService.isPrimaryAdded CBMutableService.init(type: CBUUID!, primary: Bool)Added CBPeripheralAdded CBPeripheral.RSSIAdded CBPeripheral.delegateAdded CBPeripheral.discoverCharacteristics([AnyObject]!, forService: CBService!)Added CBPeripheral.discoverDescriptorsForCharacteristic(CBCharacteristic!)Added CBPeripheral.discoverIncludedServices([AnyObject]!, forService: CBService!)Added CBPeripheral.discoverServices([AnyObject]!)Added CBPeripheral.identifierAdded CBPeripheral.nameAdded CBPeripheral.readRSSI()Added CBPeripheral.readValueForCharacteristic(CBCharacteristic!)Added CBPeripheral.readValueForDescriptor(CBDescriptor!)Added CBPeripheral.servicesAdded CBPeripheral.setNotifyValue(Bool, forCharacteristic: CBCharacteristic!)Added CBPeripheral.stateAdded CBPeripheral.writeValue(NSData!, forCharacteristic: CBCharacteristic!, type: CBCharacteristicWriteType)Added CBPeripheral.writeValue(NSData!, forDescriptor: CBDescriptor!)Added CBPeripheralAuthorizationStatus [enum]Added CBPeripheralAuthorizationStatus.AuthorizedAdded CBPeripheralAuthorizationStatus.DeniedAdded CBPeripheralAuthorizationStatus.NotDeterminedAdded CBPeripheralAuthorizationStatus.RestrictedAdded CBPeripheralDelegateAdded CBPeripheralDelegate.peripheral(CBPeripheral!, didDiscoverCharacteristicsForService: CBService!, error: NSError!)Added CBPeripheralDelegate.peripheral(CBPeripheral!, didDiscoverDescriptorsForCharacteristic: CBCharacteristic!, error: NSError!)Added CBPeripheralDelegate.peripheral(CBPeripheral!, didDiscoverIncludedServicesForService: CBService!, error: NSError!)Added CBPeripheralDelegate.peripheral(CBPeripheral!, didDiscoverServices: NSError!)Added CBPeripheralDelegate.peripheral(CBPeripheral!, didModifyServices:[AnyObject]!)Added CBPeripheralDelegate.peripheral(CBPeripheral!, didUpdateNotificationStateForCharacteristic: CBCharacteristic!, error: NSError!)Added CBPeripheralDelegate.peripheral(CBPeripheral!, didUpdateValueForCharacteristic: CBCharacteristic!, error: NSError!)Added CBPeripheralDelegate.peripheral(CBPeripheral!, didUpdateValueForDescriptor: CBDescriptor!, error: NSError!)Added CBPeripheralDelegate.peripheral(CBPeripheral!, didWriteValueForCharacteristic: CBCharacteristic!, error: NSError!)Added CBPeripheralDelegate.peripheral(CBPeripheral!, didWriteValueForDescriptor: CBDescriptor!, error: NSError!)Added CBPeripheralDelegate.peripheralDidUpdateName(CBPeripheral!)Added CBPeripheralDelegate.peripheralDidUpdateRSSI(CBPeripheral!, error: NSError!)Added CBPeripheralManagerAdded CBPeripheralManager.addService(CBMutableService!)Added CBPeripheralManager.delegateAdded CBPeripheralManager.init(delegate: CBPeripheralManagerDelegate!, queue: dispatch_queue_t!)Added CBPeripheralManager.init(delegate: CBPeripheralManagerDelegate!, queue: dispatch_queue_t!, options:[NSObject: AnyObject]!)Added CBPeripheralManager.isAdvertisingAdded CBPeripheralManager.removeAllServices()Added CBPeripheralManager.removeService(CBMutableService!)Added CBPeripheralManager.respondToRequest(CBATTRequest!, withResult: CBATTError)Added CBPeripheralManager.setDesiredConnectionLatency(CBPeripheralManagerConnectionLatency, forCentral: CBCentral!)Added CBPeripheralManager.startAdvertising([NSObject: AnyObject]!)Added CBPeripheralManager.stateAdded CBPeripheralManager.stopAdvertising()Added CBPeripheralManager.updateValue(NSData!, forCharacteristic: CBMutableCharacteristic!, onSubscribedCentrals:[AnyObject]!) -> BoolAdded CBPeripheralManagerConnectionLatency [enum]Added CBPeripheralManagerConnectionLatency.HighAdded CBPeripheralManagerConnectionLatency.LowAdded CBPeripheralManagerConnectionLatency.MediumAdded CBPeripheralManagerDelegateAdded CBPeripheralManagerDelegate.peripheralManager(CBPeripheralManager!, central: CBCentral!, didSubscribeToCharacteristic: CBCharacteristic!)Added CBPeripheralManagerDelegate.peripheralManager(CBPeripheralManager!, central: CBCentral!, didUnsubscribeFromCharacteristic: CBCharacteristic!)Added CBPeripheralManagerDelegate.peripheralManager(CBPeripheralManager!, didAddService: CBService!, error: NSError!)Added CBPeripheralManagerDelegate.peripheralManager(CBPeripheralManager!, didReceiveReadRequest: CBATTRequest!)Added CBPeripheralManagerDelegate.peripheralManager(CBPeripheralManager!, didReceiveWriteRequests:[AnyObject]!)Added CBPeripheralManagerDelegate.peripheralManager(CBPeripheralManager!, willRestoreState:[NSObject: AnyObject]!)Added CBPeripheralManagerDelegate.peripheralManagerDidStartAdvertising(CBPeripheralManager!, error: NSError!)Added CBPeripheralManagerDelegate.peripheralManagerDidUpdateState(CBPeripheralManager!)Added CBPeripheralManagerDelegate.peripheralManagerIsReadyToUpdateSubscribers(CBPeripheralManager!)Added CBPeripheralManagerState [enum]Added CBPeripheralManagerState.PoweredOffAdded CBPeripheralManagerState.PoweredOnAdded CBPeripheralManagerState.ResettingAdded CBPeripheralManagerState.UnauthorizedAdded CBPeripheralManagerState.UnknownAdded CBPeripheralManagerState.UnsupportedAdded CBPeripheralState [enum]Added CBPeripheralState.ConnectedAdded CBPeripheralState.ConnectingAdded CBPeripheralState.DisconnectedAdded CBServiceAdded CBService.UUIDAdded CBService.characteristicsAdded CBService.includedServicesAdded CBService.isPrimaryAdded CBService.peripheralAdded CBUUIDAdded CBUUID.init(CFUUID: CFUUID!)Added CBUUID.init(NSUUID: NSUUID!)Added CBUUID.UUIDStringAdded CBUUID.dataAdded CBUUID.init(data: NSData!)Added CBUUID.init(string: String!)Added CBATTErrorDomainAdded CBAdvertisementDataIsConnectableAdded CBAdvertisementDataLocalNameKeyAdded CBAdvertisementDataManufacturerDataKeyAdded CBAdvertisementDataOverflowServiceUUIDsKeyAdded CBAdvertisementDataServiceDataKeyAdded CBAdvertisementDataServiceUUIDsKeyAdded CBAdvertisementDataSolicitedServiceUUIDsKeyAdded CBAdvertisementDataTxPowerLevelKeyAdded CBCentralManagerOptionShowPowerAlertKeyAdded CBCentralManagerScanOptionAllowDuplicatesKeyAdded CBCentralManagerScanOptionSolicitedServiceUUIDsKeyAdded CBConnectPeripheralOptionNotifyOnDisconnectionKeyAdded CBErrorDomainAdded CBPeripheralManagerOptionShowPowerAlertKeyAdded CBUUIDAppearanceStringAdded CBUUIDCharacteristicAggregateFormatStringAdded CBUUIDCharacteristicExtendedPropertiesStringAdded CBUUIDCharacteristicFormatStringAdded CBUUIDCharacteristicUserDescriptionStringAdded CBUUIDClientCharacteristicConfigurationStringAdded CBUUIDDeviceNameStringAdded CBUUIDGenericAccessProfileStringAdded CBUUIDGenericAttributeProfileStringAdded CBUUIDPeripheralPreferredConnectionParametersStringAdded CBUUIDPeripheralPrivacyFlagStringAdded CBUUIDReconnectionAddressStringAdded CBUUIDServerCharacteristicConfigurationStringAdded CBUUIDServiceChangedString

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
