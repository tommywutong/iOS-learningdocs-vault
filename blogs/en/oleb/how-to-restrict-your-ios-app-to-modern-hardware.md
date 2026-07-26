---
title: How to Restrict Your iOS App to Modern Hardware
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/12/how-to-restrict-your-ios-app-to-modern-hardware/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:52535af6aee27c79'
translated: false
---

> 原文：[How to Restrict Your iOS App to Modern Hardware](https://oleb.net/blog/2011/12/how-to-restrict-your-ios-app-to-modern-hardware/)　·　Ole Begemann

# How to Restrict Your iOS App to Modern Hardware

Marco Arment posted [one of his regular iOS device and OS version stats overviews](http://www.marco.org/2011/11/30/more-ios-device-and-os-version-stats-from-instapaper) yesterday. While Marco’s stats obviously only represent Instapaper users and one has to be careful how representative the data is, these updates are nevertheless very welcome as they represent one of very few publicly available data points to estimate the adoption rate of iOS versions.

# iOS 5 Adoption Rate Only at 45%

The most striking number to me is the rate of iOS 5 adoption: across Instapaper users on all iOS devices, 45% are running iOS 5. This strikes me as quite low. I would have expected a number in the range of 70–80%, especially considering that Instapaper users are probably significantly more geeky than the average iOS device owner.[1](#fn:1)

# How to Forcefully Exclude Older Devices From Running Your App

According to Marco’s numbers, having an app that requires iOS 5 would still exclude a lot of users at this time. Most developers should probably wait a least a few more months until they cut off iOS 4 support.[2](#fn:2) For developers of apps that require a relatively high-performance device to run smoothly, that raises the question: how do I best restrict my app to only run on newer devices?

It is important to implement such a restriction in a way that enforces it not only at runtime but also at install time. Otherwise, you will (rightfully) get lots of e-mail from angry iPhone 3G owners (if your app even makes it through the review process). Here are the options you have:

## 1. Require a Certain iOS Version

We just learned that it is probably too early to require iOS 5.0 but what about iOS 4.3? iOS 4.3 does not run on anything that’s older than the iPhone 3GS and it has an adoption rate of 88% in Marco’s stats. In fact, that is what Marco recommends:

> Developers of CPU-intensive iPhone apps and games can celebrate the continued infiltration of faster hardware, with at-least-3GS-class CPUs in 94.39% of iPhones and iPod Touches. Apps that need high performance can probably start requiring iOS 4.3 (87.8%) to forcefully cut support for the much slower old CPU in the iPhone 1, iPhone 3G, and 1-2G iPod Touches.

## 2. Require Certain Device Features such as OpenGL ES 2

If your app uses OpenGL ES 2, you are done because the GPUs in devices before the iPhone 3GS do not support that version. All you need to do is specify `opengles-2` under the [`UIRequiredDeviceCapabilities`](http://developer.apple.com/library/ios/documentation/general/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW3) key in your `Info.plist` file.

This is a convenient option but you should only use it if your app really uses and requires this special feature. Don’t just arbitrarily select a convenient option from the available device capabilities.

## 3. Require the armv7 CPU Architecture

One convenient way to sort of circumvent this rule is to explicitly require a device with a fast CPU: one of the options for `UIRequiredDeviceCapabilities` is `armv7`, which tells Apple and the OS that your app only runs on the modern CPU architecture that is used by the iPhone 3GS and all newer iOS devices. That way, you can allow iOS versions 4.0-4.2 and still restrict your app to modern hardware. (Please only do this if your app is really close to unusable on an iPhone 3G. Users of older hardware are probably used to somewhat slow performance, so they won’t necessarily hold it against you if your app stutters a bit.)

![Requiring the armv7 CPU architecture in the UIRequiredDeviceCapabilities key](https://oleb.net/media/uirequireddevicecapabilities-armv7.png)

<sub>Requiring the armv7 CPU architecture in the `UIRequiredDeviceCapabilities` key.</sub>

_Note: Patrick Burleson [noted on Twitter](https://twitter.com/pbur/status/142266546767671296) that he heard of app rejections when apps added new requirements to the `UIRequiredDeviceCapabilities` in an update. I find it hard to believe that that is a general rule. It must be allowed for existing apps to switch to OpenGL ES 2.0, for example. But it’s probably good to keep in mind._

**Update December 23, 2011:** It seems indeed to be true that the required device capabilities cannot be changed in app updates. Please see [my follow-up post on the issue](https://oleb.net/blog/2011/12/uirequireddevicecapabilities-cannot-be-changed-in-app-updates/).

1. It is not totally clear to me, however, how Marco arrived at these numbers. Do they represent a snapshot of his user base at the end of November? In that case, I would have expected the iOS 5 adoption rate to be much higher. Or is it an average across a longer period of time, perhaps the entire month or since the release of Instapaper 4.0? In that case, the 45% would not surprise me as much. [↩︎](#fnref:1)
2. That said, if I were to start developing a new app now, I would definitely go iOS 5 only. [↩︎](#fnref:2)
