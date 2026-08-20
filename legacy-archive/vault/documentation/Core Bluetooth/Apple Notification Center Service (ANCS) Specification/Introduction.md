---
title: Apple Notification Center Service (ANCS) Specification
apple_id: TP40013460
resource_type: Guide
platform: iOS
topic: Data Management
technology: CoreBluetooth
published: '2014-10-20'
source_url: https://developer.apple.com/library/archive/documentation/CoreBluetooth/Reference/AppleNotificationCenterServiceSpecification/Introduction/Introduction.html
archived_at: '2026-07-15T07:22:05.965834Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](The%20Apple%20Notification%20Center%20Service.md)

# Introduction

The purpose of the Apple Notification Center Service (ANCS) is to give Bluetooth accessories (that connect to iOS devices through a Bluetooth low-energy link) a simple and convenient way to access many kinds of notifications that are generated on iOS devices.

The ANCS is designed around three principles: simplicity, efficiency and scalability. As a result, accessories ranging from simple LEDs to powerful “companion” devices with large displays can find the service useful.

The ANCS has no dependencies, apart from the standard set of Generic Attribute Profile (GATT) sub-procedures. An accessory acting as a GATT client is free to access and use other services provided by the iOS device while using the ANCS.

Unless specified otherwise, all numerical values transmitted through the ANCS shall be little endian.

Unless specified otherwise, all string values transmitted through the ANCS shall be composed of unicode characters encoded with UTF-8.

The Apple Notification Center Service shall be referred to as the _ANCS_.

The publisher of the ANCS service (the iOS device) shall be referred to as the _Notification Provider (NP)_.

Any client of the ANCS service (an accessory) shall be referred to as a _Notification Consumer (NC)_.

A notification displayed on an iOS device in the iOS Notification Center shall be referred to as an _iOS notification_.

A notification sent by a GATT characteristic as an asynchronous message shall be referred to as a _GATT notification_.

[Next](The%20Apple%20Notification%20Center%20Service.md)

