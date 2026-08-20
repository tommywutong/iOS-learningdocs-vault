---
title: iOS Wi-Fi Management APIs
apple_id: DTS40017579
resource_type: QA
platform: iOS
topic: Networking, Internet, & Web
technology: null
published: '2017-08-14'
source_url: https://developer.apple.com/library/archive/qa/qa1942/_index.html
archived_at: '2026-07-27T06:57:05.475760Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1942

# iOS Wi-Fi Management APIs

## Q:  On iOS, how can my app scan for nearby Wi-Fi networks?

A: iOS does not have a general-purpose API for Wi-Fi scanning and configuration. However, there are a number of special-purpose APIs, and one of these may be appropriate for your product. Specifically:

- NEHotspotHelper — If your app helps the user navigate a hotspot (a Wi-Fi network where the user must interact with the network to gain access to the wider Internet), you should look at NEHotspotHelper, part of the Network Extension framework. See the [Hotspot Network Subsystem Programming Guide](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/Hotspot_Network_Subsystem_Guide/Contents/Introduction.html#//apple_ref/doc/uid/TP40016639) for details.

  __Important:__ NEHotspotHelper requires that your app have special entitlements. The [NEHotspotHelper API Reference](https://developer.apple.com/reference/networkextension/nehotspothelper) has the details.
- NEHotspotConfigurationManager — iOS 11 adds the NEHotspotConfigurationManager API, also part of the Network Extension framework, which supports two use cases:

  - An app that interacts with a Wi-Fi based accessory and wants the iOS device to temporarily join the accessory’s Wi-Fi network
  - An app that wants to add a specific Wi-Fi network to the user’s list of known networks

  Both of these scenarios require explicit user approval.

  For more details, see [WWDC 2017 Session 707 Advances in Networking, Part 1](https://developer.apple.com/videos/play/wwdc2017/707/).
- Accessory configuration — If you want to configure an accessory to join the user’s local network (for example, you’re creating a companion app for a set of wireless speakers and the goal is to get those speakers on to the user’s home network), you have two options:

  - Wireless Accessory Configuration (WAC) — To learn more about WAC, watch [WWDC 2013 Session 700 Designing Accessories for iOS and OS X](https://developer.apple.com/videos/play/wwdc2013/700/), which introduced the technology, and [WWDC 2014 Session 701 Designing Accessories for iOS and OS X](https://developer.apple.com/videos/play/wwdc2014/701/), which describes enhancements made in iOS 8 that let you configure a WAC accessory from within your app.
  - HomeKit — You can ask the system to scan for, pair and configure any unpaired HomeKit accessories by calling the `addAndSetupAccessories(completionHandler:)` method on [HMHome](https://developer.apple.com/reference/homekit/hmhome). To learn more about this, watch [WWDC 2016 Session 710 What’s New in HomeKit](https://developer.apple.com/videos/play/wwdc2016/710/).

  __Important:__ Both WAC and HomeKit accessories must be built under the aegis of the [MFi program](https://developer.apple.com/programs/mfi/).
- Peer-to-peer networking — If your goal is to communicate with other nearby devices, you should look at:

  - NSNetService
  - Multipeer Connectivity

  Both of these support peer-to-peer networking over both Bluetooth and peer-to-peer Wi-Fi, although in the case of NSNetService you must opt in to that support by settings the `includesPeerToPeer` flag, as shown by _[WiTap](../samplecode/WiTap/WiTap.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydomzsge)_.

  __Important:__ The on-the-wire protocols used by this peer-to-peer networking are not documented for third-party use, so this technique only works between Apple devices.
- Location — If you’d like to use Wi-Fi data to determine the device’s location, we recommend you use Core Location. This locates the device using a wide variety of techniques, including Wi-Fi. For more information, see the [Maps](https://developer.apple.com/maps/) page on the developer web site.
- Current Wi-Fi network — If you’re interested in getting the name of the Wi-Fi network to which the device is currently associated, you can call [CNCopyCurrentNetworkInfo](https://developer.apple.com/reference/systemconfiguration/1614126-cncopycurrentnetworkinfo), part of the System Configuration framework.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-08-14 | Added information about NEHotspotConfigurationManager. |
| 2016-11-16 | New document that summarizes the Wi-Fi APIs available on iOS. |
