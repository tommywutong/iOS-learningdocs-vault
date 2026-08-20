---
title: Core Bluetooth Programming Guide
apple_id: TP40013257
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: CoreBluetooth
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/BestPracticesForSettingUpYourIOSDeviceAsAPeripheral/BestPracticesForSettingUpYourIOSDeviceAsAPeripheral.html
archived_at: '2026-07-18T01:33:42.409793Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Bluetooth Programming Guide](About%20Core%20Bluetooth.md)


[Next](Document%20Revision%20History.md)[Previous](Best%20Practices%20for%20Interacting%20with%20a%20Remote%20Peripheral%20Device.md)

# Best Practices for Setting Up Your Local Device as a Peripheral

As with many central-side transactions, the Core Bluetooth framework give you control over implementing most aspects of the peripheral role. This chapter provides guidelines and best practices for harnessing this level of control in a responsible way.

Advertising peripheral data is an important part of setting up your local device to implement the peripheral role. The following sections assist you in doing so in an appropriate way.

You advertise your peripheral’s data by passing in a dictionary of advertising data to the [startAdvertising:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393252-startadvertising) method of the [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager) class, as described in [Advertising Your Services](Performing%20Common%20Peripheral%20Role%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjxfvbuqnbnknltk). When you create an advertising dictionary, keep in mind that there are limits to what, as well as how much, you can advertise.

Although advertising packets in general can hold a variety of information about the peripheral device, you may advertise only your device’s local name and the UUIDs of any services you want to advertise. That is, when you create your advertising dictionary, you may specify only the following two keys: [CBAdvertisementDataLocalNameKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdatalocalnamekey) and [CBAdvertisementDataServiceUUIDsKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdataserviceuuidskey). You receive an error if you specify any other keys.

There are also limits as to how much space you can use when advertising data. When your app is in the foreground, it can use up to 28 bytes of space in the initial advertisement data for any combination of the two supported advertising data keys. If this space is used up, there are an additional 10 bytes of space in the scan response that can be used only for the local name. Any service UUIDs that do not fit in the allotted space are added to a special “overflow” area; they can be discovered only by an iOS device that is explicitly scanning for them. While your app is in the background, the local name is not advertised and all service UUIDs are place in the overflow area.

To help you stay within these space constraints, limit the service UUIDs you advertise to those that identify your primary services.

Since advertising peripheral data uses your local device’s radio (and thus your device’s battery), advertise only when you want other devices to connect to you. Once connected, these devices can explore and interact the peripheral’s data directly, without the need for any advertising packets. Therefore, to minimize radio usage, increase app performance, and preserve your device’s battery, stop advertising when it is no longer necessary to facilitate any intended Bluetooth low energy transaction. To stop advertising on your local peripheral, simply call the [stopAdvertising](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393275-stopadvertising) method of the [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager) class, like this:

```
    [myPeripheralManager stopAdvertising];
```


Knowing when to advertise is often something only the user can know. For example, it doesn’t make sense to have your app advertise services on your device when you know there aren’t any other Bluetooth low energy devices nearby. Since your app is often unaware of what other devices are nearby, provide in your app’s user interface (UI) a way for the user to decide when to advertise.

When you create a mutable characteristic, you set its properties, value, and permissions. These settings determine how connected centrals access and interact with the characteristic’s value. Although you may decide to configure the properties and permissions of your characteristics differently based on the needs of your app, the following sections provide some guidance when you need to perform the following two tasks:

- Allow connected centrals to subscribe to your characteristics
- Protect sensitive characteristic values from being accessed by unpaired centrals

As described in [Subscribe to Characteristic Values That Change Often](Best%20Practices%20for%20Interacting%20with%20a%20Remote%20Peripheral%20Device.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjxfvbuqnrnknlto), it is recommended that centrals subscribe to characteristic values (of a remote peripheral’s service) that change often. When possible, encourage this practice by allowing connected centrals to subscribe to your characteristics’ values.

When you create a mutable characteristic, configure it to support subscriptions by setting the characteristic’s properties with the [CBCharacteristicPropertyNotify](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/1518976-notify) constant, like this:

```
    myCharacteristic = [[CBMutableCharacteristic alloc]
        initWithType:myCharacteristicUUID
        properties:CBCharacteristicPropertyRead | CBCharacteristicPropertyNotify
        value:nil permissions:CBAttributePermissionsReadable];
```

In this example, the characteristic’s value is readable, and it can be subscribed to by a connected central.

Depending on the use case, you may want to vend a service that has one or more characteristic whose value needs to be secure. For example, imagine that you want to vend a social media profile service. This service may have characteristics whose values represent a member’s profile information, such as first name, last name, and email address. More than likely, you want to allow only trusted devices to retrieve a member’s email address.

You can ensure that only trusted devices have access to sensitive characteristic values by setting the appropriate characteristic properties and permissions. To continue the example above, to allow only trusted devices to retrieve a member’s email address, set the appropriate characteristic’s properties and permissions, like this:

```
    emailCharacteristic = [[CBMutableCharacteristic alloc]
        initWithType:emailCharacteristicUUID
        properties:CBCharacteristicPropertyRead
        | CBCharacteristicPropertyNotifyEncryptionRequired
        value:nil permissions:CBAttributePermissionsReadEncryptionRequired];
```

In this example, the characteristic is configured to allow only trusted devices to read or subscribe to its value. When a connected, remote central tries to read or subscribe to this characteristic’s value, Core Bluetooth tries to pair your local peripheral with the central to create a secure connection.

For example, if the central and the peripheral are iOS devices, both devices receive an alert indicating that the other device would like to pair. The alert on the central device contains a code that you must enter into a text field on the peripheral device’s alert to complete the pairing process.

After the pairing process is complete, the peripheral considers the paired central a trusted device and allows the central access to its encrypted characteristic values.

[Next](Document%20Revision%20History.md)[Previous](Best%20Practices%20for%20Interacting%20with%20a%20Remote%20Peripheral%20Device.md)

