---
title: Starting With Bluetooth Low Energy Development on iOS
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/04/starting-bluetooth-low-energy-development-ios/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:05af8162b4f39545'
translated: false
---

> 原文：[Starting With Bluetooth Low Energy Development on iOS](https://oleb.net/blog/2013/04/starting-bluetooth-low-energy-development-ios/)　·　Ole Begemann

# Starting With Bluetooth Low Energy Development on iOS

With the iOS 5 SDK, Apple introduced the [Core Bluetooth](http://developer.apple.com/library/ios/#documentation/CoreBluetooth/Reference/CoreBluetooth_Framework/_index.html) framework. Core Bluetooth allows developers to write apps that talk directly to hardware gadgets or other iOS devices^[1](#fn:1) using the [Bluetooth Low Energy](https://en.wikipedia.org/wiki/Bluetooth_low_energy) (BLE, also called Bluetooth Smart) standard.

**Update April 30, 2013:** Things work differently for Bluetooth devices that do not use Bluetooth LE. Certain device classes such as headsets and keyboards are managed directly by the OS in a way that is fully transparent (and off limits) to third-party apps.

Other proprietary devices (connected via Bluetooth or the Dock connector) can be accessed by using the [External Accessory Framework](http://developer.apple.com/library/ios/#featuredarticles/ExternalAccessoryPT/Introduction/Introduction.html), available since the iOS 3.0 SDK. Unfortunately, this [only works for devices that have been approved](http://developer.apple.com/library/ios/#qa/qa1657/_index.html) by Apple. The device manufacturer must be a member of [Apple’s MFi program](https://developer.apple.com/programs/mfi/) about which very little public information is available.^[2](#fn:2)

The main advantage of the Core Bluetooth and Bluetooth LE way I describe in this article is that any app can communicate with any hardware device without the need to go through a lengthy and costly approval process.

# Starting Out

If you want to start with Bluetooth LE development, you need a few things:

- An iOS device with hardware support for Bluetooth 4.0. All devices Apple released since the iPhone 4S (including the 4S) do, the older ones don’t. See the [per-device feature list on Wikipedia](https://en.wikipedia.org/wiki/List_of_iOS_devices#Features) for details.
- The iOS Simulator only supports Core Bluetooth if your Mac’s Bluetooth hardware is compatible with Bluetooth 4.0. The first Macs with Bluetooth 4.0 support were the [mid-2011 MacBook Air and Mac mini](http://appleinsider.com/articles/11/07/20/apple_adds_bluetooth_4_0_support_to_new_macbook_air_mac_mini). The MacBook Pro has included Bluetooth 4.0 support since the mid-2012 models (both retina and non-retina) and the iMac since its late-2012 refresh.
- A Bluetooth LE peripheral your app can talk to. This can be a second iOS device or Mac, but it’s usually more fun to have some hardware gadget you want to communicate with. See below for a few options.

# A Bluetooth Smart Heart Rate Sensor

[![The Polar H7 Bluetooth heart rate chest strap sensor](https://oleb.net/media/polar-h7-500px.jpg)](https://www.amazon.com/Polar-Bluetooth-Smart-Heart-Sensor/dp/B007S088F4/)

<sub>The Polar H7.</sub>

Heart rate sensors that communicate over Bluetooth LE have the advantage that they use a standardized and publicly available protocol – in this case, the [Bluetooth Heart Rate Profile](http://developer.bluetooth.org/gatt/profiles/Pages/ProfileViewer.aspx?u=org.bluetooth.profile.heart_rate.xml) – that defines the services a Bluetooth device supports and the format of the transmitted data. This means that your app will be able to talk to any compatible heart rate sensor on the market. Another pro of the heart rate sensor as a testing device is that Apple built much of its sample code for Bluetooth for these gadgets.

Examples of popular models are the [Polar H7](https://www.amazon.com/Polar-Bluetooth-Smart-Heart-Sensor/dp/B007S088F4/) or the [Wahoo Blue HR](https://www.amazon.com/Wahoo-Fitness-Heart-Strap-iPhone/dp/B006NZH0TU/). They usually cost between 60 and 80 dollars/euros.

Other standardized Bluetooth profiles include [blood pressure measurement](http://developer.bluetooth.org/gatt/profiles/Pages/ProfileViewer.aspx?u=org.bluetooth.profile.blood_pressure.xml), [running](http://developer.bluetooth.org/gatt/profiles/Pages/ProfileViewer.aspx?u=org.bluetooth.profile.running_speed_and_cadence.xml) or [cycling](http://developer.bluetooth.org/gatt/profiles/Pages/ProfileViewer.aspx?u=org.bluetooth.profile.cycling_speed_and_cadence.xml) speed and cadence, and a [proximity sensor](http://developer.bluetooth.org/gatt/profiles/Pages/ProfileViewer.aspx?u=org.bluetooth.profile.proximity.xml). [See the full list](http://developer.bluetooth.org/gatt/profiles/Pages/ProfilesHome.aspx).

# Texas Instruments CC2541 SensorTag

[![The Texas Instruments CC2541 Bluetooth LE SensorTag](https://oleb.net/media/ti-cc2541-sensortag-233px.jpg)](http://www.ti.com/tool/cc2541dk-sensor)

<sub>The Texas Instruments CC2541 SensorTag.</sub>

This is another option that is both cheaper and more flexible. The [Texas Instruments CC2541 SensorTag](http://www.ti.com/tool/cc2541dk-sensor) is a small gadget (about the size of a remote car key) and includes a temperature sensor (IR), a humidity sensor, an accelerometer, a gyroscope, a magnetometer and two buttons, all of which you can query via Bluetooth LE. And the best part: it’s only $25, including worldwide shipping! (My order to Germany arrived within just a few days, from the Netherlands.)

Even though I am not sure how accurate the sensors really are, this thing is a no-brainer if you are at all interested in Bluetooth LE development and communication with hardware devices. It’s a perfect testing device. Texas Instruments even provides a bad-looking [iOS app on the App Store](https://itunes.apple.com/us/app/ti-sensortag/id552918064?mt=8) that not only lets you check out all the different sensors; it can also generate source code that you can use as a basis for writing your own app that talks to the CC2541.

[![Screenshot of Texas Instruments's SensorTag iOS app](https://oleb.net/media/ti-sensortag-app-screenshot-1024px.jpg)](https://oleb.net/media/ti-sensortag-app-screenshot-1024px.jpg)

<sub>TI's accompanying SensorTag app is universal.</sub>

# WWDC Sessions on Core Bluetooth

Apple’s written documentation on Core Bluetooth is still sparse. The framework is not very difficult to understand, though, at least once you have grasped a few basic concepts. These are best explained in the [WWDC 2012 sessions](https://developer.apple.com/videos/wwdc/2012/) 703 and 705, which I highly recommend you watch to get started. The sample code Apple presents in the sessions talks to a Bluetooth heart rate sensor.

You will find that setting up a connection with a Bluetooth LE device is quite simple and straightforward. The format of the actual data you then receive or transmit over the Bluetooth connection is either entirely up to you (if you control both ends of the connection) or must be defined in a separate protocol (such as the heart rate profile discussed above). It is not part of the Core Bluetooth APIs.

1. The ability for an iOS device to act as a Bluetooth _peripheral_ – allowing one iOS device to talk to another – was introduced with iOS 6. [↩︎](#fnref:1)
2. From what I have heard, the MFi application and approval process is very lengthy and frustrating, especially for smaller companies. [↩︎](#fnref:2)
