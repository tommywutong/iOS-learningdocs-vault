---
title: iOS Device Compatibility Reference
apple_id: TP40013599
resource_type: Guide
platform: iOS
topic: Data Management
technology: null
published: '2017-10-30'
source_url: https://developer.apple.com/library/archive/documentation/DeviceInformation/Reference/iOSDeviceCompatibility/Introduction/Introduction.html
archived_at: '2026-07-15T07:31:54.562879Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](Device%20Compatibility.md)

# Introduction

iOS devices support a variety of features, including sensors, graphics processors and networking options. When designing your app, you need to decide what capabilities your app needs and which devices to support, because the capabilities of each kind of iOS device are different.

This document describes the details for each device in order to help you develop your app and choose devices to test on. The information contained here is current as of iOS 11.0, but it is subject to change in future hardware or software releases.

### Device Compatibility Strings

Sometimes, your app is dependent on a specific hardware feature existing on a device. On iOS, you can declare these dependencies when you build your app. When the app is built, this compatibility information is used to prevent the app from being installed on a device it can’t run on—and it can also be used by the App Store to prevent a customer from purchasing an app that doesn’t work on their device.

### Displays

Displays on iOS devices have a variety of characteristics, including the size of the screen, which color spaces it supports, the rate at which the screen refreshes its contents, and the rate at which touch events are sampled and delivered. Understanding the characteristics of a specific device can be critical to producing the best user experience in your app.

### Graphics Processors

When working with Metal and OpenGL ES, you often need to know the exact capabilities of the underlying hardware and the software that talks to it. Metal and OpenGL ES provide many built-in mechanisms for determining this information; this document summarizes the most important information and provides other information useful when creating Metal and OpenGL ES apps that run well on iOS devices.

### Cameras

Each iPhone and iPad model has many sophisticated camera features; iOS provides multiple ways for your app to control a device’s cameras and access their output. This chapter summarizes the specific camera capabilities of each model and provides information on how to access those features in the iOS SDK.

Although this document provides important Metal and OpenGL ES hardware information, it is not definitive. If you are unfamiliar with Metal programming, consult the _[Metal Programming Guide](../Miscellaneous/Metal%20Programming%20Guide/About%20Metal%20and%20This%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrr)_ to learn how to develop Metal apps on iOS. If you are unfamiliar with OpenGL ES programming, consult the _[OpenGL ES Programming Guide](../3D%20Drawing/OpenGL%20ES%20Programming%20Guide/About%20OpenGL%20ES.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojt)_ to learn how to develop OpenGL ES apps on iOS. To ensure compatibility with future devices and iOS versions, your app must always test the capabilities of the underlying Metal and OpenGL ES implementation at runtime, disabling any features that do not have the required support from iOS.

[Next](Device%20Compatibility.md)

