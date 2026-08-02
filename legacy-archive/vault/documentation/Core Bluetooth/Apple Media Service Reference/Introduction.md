---
title: Apple Media Service Reference
apple_id: TP40014716
resource_type: Guide
platform: iOS
topic: Audio, Video, & Visual Effects
technology: CoreBluetooth
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/CoreBluetooth/Reference/AppleMediaService_Reference/Introduction/Introduction.html
archived_at: '2026-07-15T07:22:04.125095Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](The%20Apple%20Media%20Service.md)

# Introduction

The Apple Media Service (AMS) is used with Bluetooth accessories that connect to iOS devices through Bluetooth low-energy links. It gives them a simple and convenient way to control media apps and access information about the media states of the connected iOS devices.

The AMS has no dependencies, apart from the standard set of Generic Attribute Profile (GATT) sub-procedures. An accessory acting as a GATT client is free to access and use other services provided by the iOS device while using the AMS.

Unless specified otherwise, all numerical values transmitted through the AMS must be little endian.
Unless specified otherwise, all string values transmitted through the AMS must be composed of unicode characters encoded with UTF-8.

In this document the Apple Media Service is referred to as the _AMS_.

The publisher of the AMS service (the iOS device) is referred to as the _Media Source (MS)_.

Any client of the AMS service (an accessory) is referred to as a _Media Remote (MR)_.

[Next](The%20Apple%20Media%20Service.md)

