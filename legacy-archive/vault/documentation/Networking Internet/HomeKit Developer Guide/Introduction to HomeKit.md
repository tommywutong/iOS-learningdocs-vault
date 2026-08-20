---
title: HomeKit Developer Guide
apple_id: TP40015050
resource_type: Guide
platform: watchOS|iOS
topic: null
technology: HomeKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/HomeKitDeveloperGuide/Introduction/Introduction.html
archived_at: '2026-07-27T06:57:09.394002Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Enabling%20HomeKit.md)

# Introduction to HomeKit

This document helps you write a HomeKit app. HomeKit is a framework for communicating with and controlling connected home automation accessories that support Apple's HomeKit Accessory Protocol. HomeKit apps enable users to discover compatible accessories and configure them. Users can also create actions to control accessories (such as a thermostat or light), group them together, and trigger them by using Siri. HomeKit objects are stored in a database residing on the user’s iOS device, which is synchronized over iCloud to other iOS devices. HomeKit supports remote access to accessories, multiple user devices, and multiple users. HomeKit also handles security and privacy for you.

（原归档配图获取待重试：`into_diagram_2x.png`）

__Note:__ If you’re a vendor who is creating a HomeKit-enabled hardware accessory, go to the [HomeKit](https://developer.apple.com/homekit) page under Hardware Developers, for information about the MFi Program. Also read _[External Accessory Programming Topics](../../../featuredarticles/External%20Accessory%20Programming%20Topics/About%20External%20Accessories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbs)_.

## See Also

The following resources provide more information about creating a HomeKit app:

- HomeKit provides guidelines for designing the user interface for your app.
- [App Store Review Guidelines: HomeKit](https://developer.apple.com/app-store/review/guidelines/#homekit) gives you tips for accelerating the approval process when you submit your app.
- _[HomeKit Framework Reference](https://developer.apple.com/documentation/homekit)_ describes the classes and methods in the HomeKit framework.
- _[External Accessory Framework Reference](https://developer.apple.com/documentation/externalaccessory)_ documents the system-provided UI for discovering and configuring wireless accessories without requiring the user to leave your app.
- _[HomeKit Catalog: Creating Homes, Pairing and Controlling Accessories, and Setting Up Triggers](https://developer.apple.com/library/archive/samplecode/HomeKitCatalog/Introduction/Intro.html#//apple_ref/doc/uid/TP40015048)_ sample code demonstrates HomeKit features.
- _WWDC 2014: Introducing HomeKit_ is a high-level look at HomeKit.
- [iOS Security](https://www.apple.com/business/docs/iOS_Security_Guide_Oct_2014.pdf) describes how HomeKit handles security and privacy on iOS.

[Next](Enabling%20HomeKit.md)
