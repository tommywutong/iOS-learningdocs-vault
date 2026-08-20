---
title: Energy Efficiency Guide for iOS Apps
apple_id: TP40015243
resource_type: Guide
platform: watchOS|iOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/BluetoothBestPractices.html
archived_at: '2026-07-18T01:47:27.901210Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for iOS Apps](index.md)



## Bluetooth Best Practices

The Core Bluetooth framework provides classes for communicating with devices that support Bluetooth low energy wireless technology. When developing an app that interacts with a Bluetooth device, remember that Bluetooth shares the device’s radio with other forms of wireless communication, such as Wi-Fi, to transmit signals over the air. Also, interacting with a Bluetooth device doesn’t just use energy on the iOS device. It uses energy on the Bluetooth device too. If you make your iOS app energy efficient, the Bluetooth device will also benefit.

In general, minimize use of the radio whenever possible to reduce impact on other resources and the device’s battery. This can be done by buffering data instead of streaming it, and by batching transactions. The following additional guidelines will help you reduce unnecessary radio use.

> [!NOTE]
> 

### Scan for Devices Only When Needed

When you call the [scanForPeripheralsWithServices:options:](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518986-scanforperipheralswithservices) method of the [CBCentralManager](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager) class to discover remote peripherals that are advertising services, the device uses its radio to listen for advertising devices until explicitly told to stop. Unless you need to discover more devices, stop scanning for other devices once you have found one you want to connect to. Use the [stopScan](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518984-stopscan) method of the `CBCentralManager` class to stop scanning for other devices. See Listing 17-1.

__Listing 17-1__Scanning for a Bluetooth device and then stopping

Objective-C

1. `-(void)beginScanningForDevice {`
2. `// Create a Core Bluetooth Central Manager object`
3. `self.myCentralManager = [[CBCentralManager alloc] initWithDelegate:self queue:nil options:nil];`
5. `// Scan for peripherals`
6. `[self.myCentralManager scanForPeripheralsWithServices:nil options:nil];`
7. `}`

10. `- (void)centralManager:(CBCentralManager *)central didDiscoverPeripheral:(CBPeripheral *)peripheral advertisementData:(NSDictionary *)advertisementData RSSI:(NSNumber *)RSSI {`
12. `// Connect to the newly discovered device`
14. `// Stop scanning for devices`
15. `[self.myCentralManager stopScan];`
16. `}`

Swift

1. `func beginScanningForDevice() {`
2. `// Create a Core Bluetooth Central Manager object`
3. `self.myCentralManager = CBCentralManager(delegate: self, queue: nil, options: nil)`
5. `// Scan for peripherals`
6. `self.myCentralManager.scanForPeripheralsWithServices(nil, options: nil)`
7. `}`
9. `func centralManager(central: CBCentralManager, didDiscoverPeripheral peripheral: CBPeripheral, advertisementData: [NSObject: AnyObject]!, RSSI: NSNumber!) {`
10. `// Connect to the newly discovered device`
12. `// Stop scanning for devices`
13. `self.myCentralManager.stopScan()`
14. `}`

### Minimize Processing of Duplicate Device Discoveries

Remote peripheral devices may send out multiple advertising packets per second to announce their presence to listening apps. By default, these packets are combined into a single event and delivered to your app once per peripheral. You should avoid changing this behavior—don’t specify the `CBCentralManagerScanOptionAllowDuplicatesKey` constant as a scan option when calling the [scanForPeripheralsWithServices:options:](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518986-scanforperipheralswithservices) method. Doing so results in excess events that can drain battery life.

### Only Discover Services and Characteristics You Need

Peripheral devices provide services related to performing specific functions—such as a Bluetooth heart monitor that offers a service for retrieving heart rate information. Services include characteristics, or attributes. For example, the heart rate service may have characteristics that provide specific measurements or data, such as the position of the sensor when a reading was obtained.

A peripheral may have many more services and characteristics than are needed to fulfill a specific use case with your app. Therefore, look for and discover the specific services and characteristics your app needs. You can do this by providing specific UUIDs (represented by CBUUID objects) to the [discoverServices:](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518706-discoverservices) and [discoverCharacteristics:forService:](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518797-discovercharacteristics) methods of the [CBPeripheral](https://developer.apple.com/documentation/corebluetooth/cbperipheral) class, as shown in Listing 17-2 and Listing 17-3.

__Listing 17-2__Discovering specific services

Objective-C

1. `// Look for services matching a specific set of UUIDs`
2. `[peripheral discoverServices:@[firstServiceUUID, secondServiceUUID]];`

Swift

1. `// Look for services matching a specific set of UUIDs`
2. `peripheral.discoverServices([firstServiceUUID, secondServiceUUID])`

__Listing 17-3__Discovering specific service characteristics

Objective-C

1. `// Look for characterstics matching a specific set of UUIDs for a given service`
2. `[[peripheral discoverCharacteristics:@[firstCharacteristicUUID, secondCharacteristicUUID]`
3. `forService:interestingService]];`

Swift

1. `// Look for characterstics matching a specific set of UUIDs for a given service`
2. `peripheral.discoverCharacteristics([firstCharacteristicUUID, secondCharacteristicUUID], forService: interestingService)`

### Request Notifications Rather than Polling for Characteristic Value Changes

In most cases, your app has no way of knowing when a service’s characteristic value will change on a connected device. You could repeatedly query the device (polling) to detect changes, but a more efficient way is to register to receive notifications when changes occur.

Subscribe to the value of a characteristic by passing a value of `YES``true` to the [setNotifyValue:forCharacteristic:](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518949-setnotifyvalue) method of the [CBPeripheral](https://developer.apple.com/documentation/corebluetooth/cbperipheral) class, as shown in Listing 17-4. Whenever the characteristic’s value changes, the peripheral calls the [peripheral:didUpdateValueForCharacteristic:error:](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518708-peripheral) method of its delegate object.

__Listing 17-4__Subscribing and responding to characteristic value change notifications

Objective-C

1. `-(void)subscribeToCharacteristic {`
2. `// Subscribe to a characteristic value`
3. `[self.peripheral setNotifyValue:YES forCharacteristic:interestingCharacteristic];`
4. `}`
6. `- (void)peripheral:(CBPeripheral *)peripheral didUpdateNotificationStateForCharacteristic:(CBCharacteristic *)characteristic error:(NSError *)error {`
7. `// Process the characteristic value update`
8. `}`

Swift

1. `func subscribeToCharacteristic() {`
2. `// Subscribe to a characteristic value`
3. `self.peripheral.setNotifyValue(true, forCharacteristic: interestingCharacteristic)`
4. `}`
6. `func peripheral(peripheral: CBPeripheral, didUpdateNotificationStateForCharacteristic characteristic: CBCharacteristic, error: NSError! {`
7. `// Process the characteristic value update`
8. `}`

### Disconnect from a Device When You No Longer Need It

To prevent your app from needlessly using the device’s radio, disconnect from a peripheral device if a characteristic has stopped providing notifications or if additional data is no longer required. Cancel any notification subscriptions by passing a value of `NO``false` to the [setNotifyValue:forCharacteristic:](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518949-setnotifyvalue) method of the [CBPeripheral](https://developer.apple.com/documentation/corebluetooth/cbperipheral) class. Then disconnect from the device by calling the [cancelPeripheralConnection:](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518952-cancelperipheralconnection) method of the [CBCentralManager](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager) class. See Listing 17-5.

__Listing 17-5__Stopping characteristic value change notifications and disconnecting from a peripheral device

Objective-C

1. `// Unsubscribe from a characteristic value`
2. `[self.peripheral setNotifyValue:NO forCharacteristic:interestingCharacteristic];`
4. `// Disconnect from the device`
5. `[self.myCentralManager cancelPeripheralConnection:peripheral];`

Swift

1. `// Unsubscribe from a characteristic value`
2. `self.peripheral.notifyValue(false, forCharacteristic: interestingCharacteristic)`
4. `// Disconnect from the device`
5. `self.myCentralManager.cancelPeripheralConnection(peripheral)`

[Notification Best Practices](NotificationBestPractices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmrwfvjvomi)

[Apple Watch Best Practices](AppleWatchExtensionBestPractices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmzwfvjvomi)
