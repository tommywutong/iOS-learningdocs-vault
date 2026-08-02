---
title: Core Bluetooth Programming Guide
apple_id: TP40013257
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: CoreBluetooth
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/CoreBluetoothOverview/CoreBluetoothOverview.html
archived_at: '2026-07-18T01:33:42.506187Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Bluetooth Programming Guide](About%20Core%20Bluetooth.md)


[Next](Performing%20Common%20Central%20Role%20Tasks.md)[Previous](About%20Core%20Bluetooth.md)

# Core Bluetooth Overview

The Core Bluetooth framework lets your iOS and Mac apps communicate with Bluetooth low energy devices. For example, your app can discover, explore, and interact with low energy peripheral devices, such as heart rate monitors, digital thermostats, and even other iOS devices.

The framework is an abstraction of the Bluetooth 4.0 specification for use with low energy devices. That said, it hides many of the low-level details of the specification from you, the developer, making it much easier for you to develop apps that interact with Bluetooth low energy devices. Because the framework is based on the specification, some concepts and terminology from the specification have been adopted. This chapter introduces you to the key terms and concepts that you need to know to begin developing great apps using the Core Bluetooth framework.

There are two major players involved in all Bluetooth low energy communication: the central and the peripheral. Based on a somewhat traditional client-server architecture, a _peripheral_ typically has data that is needed by other devices. A _central_ typically uses the information served up by peripherals to accomplish some particular task. As Figure 1-1 shows, for example, a heart rate monitor may have useful information that your Mac or iOS app may need in order to display the user’s heart rate in a user-friendly way.

__Figure 1-1__  Central and peripheral devices

!

Peripherals broadcast some of the data they have in the form of advertising packets. An _advertising packet_ is a relatively small bundle of data that may contain useful information about what a peripheral has to offer, such as the peripheral’s name and primary functionality. For instance, a digital thermostat may advertise that it provides the current temperature of a room. In Bluetooth low energy, advertising is the primary way that peripherals make their presence known.

A central, on the other hand, can scan and listen for any peripheral device that is advertising information that it’s interested in, as shown in Figure 1-2. A central can ask to connect to any peripheral that it has discovered advertising.

__Figure 1-2__  Advertising and discovery

!

The purpose of connecting to a peripheral is to begin exploring and interacting with the data it has to offer. Before you can do this, however, it helps to understand how the data of a peripheral is structured.

Peripherals may contain one or more services or provide useful information about their connected signal strength. A _service_ is a collection of data and associated behaviors for accomplishing a function or feature of a device (or portions of that device). For example, one service of a heart rate monitor may be to expose heart rate data from the monitor’s heart rate sensor.

Services themselves are made up of either characteristics or included services (that is, references to other services). A _characteristic_ provides further details about a peripheral’s service. For example, the heart rate service just described may contain one characteristic that describes the intended body location of the device’s heart rate sensor and another characteristic that transmits heart rate measurement data. Figure 1-3 illustrates one possible structure of a heart rate monitor’s service and characteristics.

__Figure 1-3__  A peripheral’s service and characteristics

!

After a central has successfully established a connection to a peripheral, it can discover the full range of services and characteristics the peripheral has to offer (advertising data might contain only a fraction of the available services).

A central can also interact with a peripheral’s service by reading or writing the value of that service’s characteristic. For example, your app may request the current room temperature from a digital thermostat, or it may provide the thermostat with a value at which to set the room’s temperature.

The major players and data involved in Bluetooth low energy communication are mapped onto the Core Bluetooth framework in a simple, straightforward way.

When you are using a local central to interact with a remote peripheral, you are performing actions on the central side of Bluetooth low energy communication. Unless you are setting up a local peripheral device—and using it to respond to requests by a central—most of your Bluetooth transactions will take place on the central side.

For information about how to implement the central role in your app, see [Performing Common Central Role Tasks](Performing%20Common%20Central%20Role%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjxfvbuqmznknltc) and [Best Practices for Interacting with a Remote Peripheral Device](Best%20Practices%20for%20Interacting%20with%20a%20Remote%20Peripheral%20Device.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjxfvbuqnrnknltc)

On the central side, a local central device is represented by a [CBCentralManager](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager) object. These objects are used to manage discovered or connected remote peripheral devices (represented by [CBPeripheral](https://developer.apple.com/documentation/corebluetooth/cbperipheral) objects), including scanning for, discovering, and connecting to advertising peripherals. Figure 1-4 shows how local centrals and remote peripherals are represented in the Core Bluetooth framework.

__Figure 1-4__  Core Bluetooth objects on the central side

!

When you are interacting with the data on a remote peripheral (represented by a [CBPeripheral](https://developer.apple.com/documentation/corebluetooth/cbperipheral) object), you are dealing with its services and characteristics. In the Core Bluetooth framework, the services of a remote peripheral are represented by [CBService](https://developer.apple.com/documentation/corebluetooth/cbservice) objects. Similarly, the characteristics of a remote peripheral’s service are represented by [CBCharacteristic](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic) objects. Figure 1-5 illustrates the basic structure of a remote peripheral’s services and characteristics.

__Figure 1-5__  A remote peripheral’s tree of services and characteristics

!

As of macOS 10.9 and iOS 6, Mac and iOS devices can function as Bluetooth low energy peripherals, serving data to other devices, including other Mac, iPhone, and iPad devices. When setting up your device to implement the peripheral role, you are performing actions on the peripheral side of Bluetooth low energy communication.

On the peripheral side, a local peripheral device is represented by a [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager) object. These objects are used to manage published services within the local peripheral device’s database of services and characteristics and to advertise these services to remote central devices (represented by [CBCentral](https://developer.apple.com/documentation/corebluetooth/cbcentral) objects). Peripheral manager objects are also used to respond to read and write requests from these remote centrals. Figure 1-6 shows how local peripherals and remote centrals are represented in the Core Bluetooth framework.

__Figure 1-6__  Core Bluetooth objects on the peripheral side

!

When you are setting up and interacting with the data on a local peripheral (represented by a [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager) object), you are dealing with mutable versions of its services and characteristics. In the Core Bluetooth framework, the services of a local peripheral are represented by [CBMutableService](https://developer.apple.com/documentation/corebluetooth/cbmutableservice) objects. Similarly, the characteristics of a local peripheral’s service are represented by [CBMutableCharacteristic](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic) objects. Figure 1-7 illustrates the basic structure of a local peripheral’s services and characteristics.

__Figure 1-7__  A local peripheral’s tree of services and characteristics

!

For more information about how to set up your local device to implement the peripheral role, see [Performing Common Peripheral Role Tasks](Performing%20Common%20Peripheral%20Role%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjxfvbuqnbnknltc) and [Best Practices for Setting Up Your Local Device as a Peripheral](Best%20Practices%20for%20Setting%20Up%20Your%20Local%20Device%20as%20a%20Peripheral.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjxfvbuqnjnknltc).

[Next](Performing%20Common%20Central%20Role%20Tasks.md)[Previous](About%20Core%20Bluetooth.md)

