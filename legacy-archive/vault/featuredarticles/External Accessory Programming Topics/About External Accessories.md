---
title: External Accessory Programming Topics
apple_id: TP40009502
resource_type: Guide
platform: iOS
topic: Data Management
technology: ExternalAccessory
published: '2012-02-24'
source_url: https://developer.apple.com/library/archive/featuredarticles/ExternalAccessoryPT/Introduction/Introduction.html
archived_at: '2026-07-18T02:28:16.197847Z'
---
> 导航：[总目录](../../README.md) · [featuredarticles](../../_indexes/featuredarticles.md)


[Next](Connecting%20to%20an%20Accessory.md)

# About External Accessories

The External Accessory [framework](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56) (`ExternalAccessory.framework`) provides a conduit for communicating with accessories attached to any iOS-based device. App developers can use this conduit to integrate accessory-level features into their apps.

Communicating with an external accessory requires you to work closely with the accessory manufacturer to understand the services provided by that accessory. Manufacturers must build explicit support into their accessory hardware for communicating with iOS. As part of this support, an accessory must support at least one command _protocol_, which is a custom scheme for sending data back and forth between the accessory and an attached app. Apple does not maintain a registry of protocols; it is up to the manufacturer to decide which protocols to support and whether to use custom protocols or standard protocols supported by other manufacturers.

As part of your communication with the accessory manufacturer, you must find out what protocols a given accessory supports. To prevent namespace conflicts, protocol names are specified as reverse-DNS strings of the form `com.apple.myProtocol`. This allows each manufacturer to define as many protocols as needed to support their line of accessories.

Communicating with accessories requires information about the accessory itself, which you must obtain from the hardware manufacturer. From there, you use the classes of the External Accessory framework to create the bridge between the hardware and your app.

### Including the External Accessory Framework in Your Project

To use the features of the External Accessory framework, you must add `ExternalAccessory.framework` to your Xcode project and link against it in any relevant targets. To access the classes and headers of the framework, include an `#import <ExternalAccessory/ExternalAccessory.h>` statement at the top of any relevant source files.

### Declaring the Protocols Your App Supports

Apps that are able to communicate with an external accessory must declare the protocols they support in their `Info.plist` file. Declaring support for specific protocols lets the system know that your app can be launched when that accessory is connected. If no app supports the connected accessory, the system may choose to launch the App Store and point out apps that do.

To declare the protocols your app supports, you must include the `UISupportedExternalAccessoryProtocols` key in your app’s `Info.plist` file. This key contains an [array](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10) of strings that identify the communications protocols that your app supports. Your app can include any number of protocols in this list and the protocols can be in any order. The system does not use this list to determine which protocol your app should choose; it uses it only to determine if your app is capable of communicating with the accessory. It is up to your code to choose an appropriate communications protocol when it begins talking to the accessory.

For more information about the keys you put into your app’s `Info.plist` file, see _[Information Property List Key Reference](../../documentation/General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_.

### Communicating with an Accessory

An app communicates with an accessory by creating an [EASession](https://developer.apple.com/documentation/externalaccessory/easession) object for managing the accessory interactions. Session objects work with the underlying system to transfer data packets to and from the accessory. Data transfer in your app occurs through [NSInputStream](https://developer.apple.com/documentation/foundation/inputstream) and [NSOutputStream](https://developer.apple.com/documentation/foundation/nsoutputstream) objects, which are vended by the session object once the connection is made. To receive data from the accessory, monitor the input stream using a custom delegate object. To send data to the accessory, write data packets to the output stream. The format of the incoming and outgoing data packets is determined by the protocol you use to communicate with the accessory.

For information about the classes of the External Accessory framework, see _[External Accessory Framework Reference](https://developer.apple.com/documentation/externalaccessory)_

[Next](Connecting%20to%20an%20Accessory.md)

