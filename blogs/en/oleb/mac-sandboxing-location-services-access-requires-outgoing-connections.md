---
title: 'Mac Sandboxing: Location Services Access Requires Outgoing Connections'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/01/mac-sandboxing-location-services-outgoing-connections/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a306cb0a8b0ba03e'
translated: false
---

> 原文：[Mac Sandboxing: Location Services Access Requires Outgoing Connections](https://oleb.net/blog/2013/01/mac-sandboxing-location-services-outgoing-connections/)　·　Ole Begemann

# Mac Sandboxing: Location Services Access Requires Outgoing Connections

A few weeks ago, Apple’s app review team contacted me and asked me to change the sandboxing entitlements of my app [Blue Planet](http://blueplanetapp.com).

# One Entitlement Is Not Enough

Blue Planet uses the Core Location framework to determine the user’s location. As a Mac App Store app, it must specify the corresponding [sandboxing entitlement](http://developer.apple.com/library/mac/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingAppSandbox.html#//apple_ref/doc/uid/TP40011195-CH4-SW5), “Allow Location Services Access” (`com.apple.security.personal-information.location`), for this feature to work. That’s what I did and that’s what has worked fine until now.

When the app review team called me, they asked me to submit an update to Blue Planet that included the “Allow Outgoing Connections” entitlement (`com.apple.security.network.client`) as the only change. In the future, only those sandboxed apps that requested both entitlements would be allowed to access Location Services on the Mac.

[![Screenshot of the Sandboxing Entitlements in Xcode with Allow Outgoing Connections and Allow Location Services Access activated](https://oleb.net/media/xcode-sandboxing-entitlements-blueplanet.png)](https://oleb.net/media/xcode-sandboxing-entitlements-blueplanet.png)

<sub>If your sandboxed Mac app uses Location Services, make sure to request the “Allow Location Services Access” and the “Allow Outgoing Connections” entitlements.</sub>

I quickly submitted the update and it was approved within a few hours, suggesting that Apple wanted to resolve this quickly. I have no information when this change will become effective, but I would guess rather soon (maybe with 10.8.3?).

# Access to Location Services Also Requires Outgoing Connections

If your sandboxed Mac app requires access to Location Services, make sure to also request the entitlement for outgoing internet connections, whether your app needs it for other features or not. It might save you an unnecessary rejection by the app review team.
