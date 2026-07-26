---
title: Network Link Conditioner
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/network-link-conditioner/'
original_language: en
published: 2013-09-09
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:4f9a7eda81cdea63'
translated: false
---

> 原文：[Network Link Conditioner](https://nshipster.com/network-link-conditioner/)　·　NSHipster (Mattt)

# [Network Link Conditioner](https://nshipster.com/network-link-conditioner/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  July 29^th, 2019 ([revised](https://github.com/nshipster/articles/commits/master/2013-09-09-network-link-conditioner.md))

Product design is about empathy. Knowing what a user wants, what they like, what they dislike, what causes them frustration, and learning to understand and embody those motivations — this is what it takes to make something insanely great.

And so we invest in reaching beyond our own operational model of the world. We tailor our experience to [different locales](https://nshipster.com/nslocalizedstring/). We consider the usability implications of [screen readers or other assistive technologies](https://nshipster.com/uiaccessibility/). We [continuously evaluate](https://nshipster.com/unit-testing/) our implementation against these expectations.

There is, however, one critical factor that app developers often miss: **network condition**, or more specifically, the latency and bandwidth of an Internet connection.

For something so essential to user experience, it’s unfortunate that most developers take an ad-hoc approach to field-testing their apps under different conditions (if at all).

This week on NSHipster, we’ll be talking about the [Network Link Conditioner](https://developer.apple.com/download/more/?q=Additional%20Tools), a utility that allows macOS and iOS devices to accurately and consistently simulate adverse networking environments.

## Installation

Network Link Conditioner can be found in the “Additional Tools for Xcode” package. You can download this from the [Downloads for Apple Developers](https://developer.apple.com/download/more/?q=Additional%20Tools) page.

Search for “Additional Tools” and select the appropriate release of the package.

![Additional Tools - Hardware](https://nshipster.com/assets/network-link-conditioner-dmg--light-4786c923da7defd77df5d0d1123781278d0321f4c3d645001baebe4512fb897da0202278a4769a3e9483c30e369464859e011d7703eb662688d8de09a02a4bf1.png)

Once the download has finished, open the DMG, navigate to the “Hardware” directory, and double-click “Network Link Condition.prefPane”.

![Install Network Link Conditioner](https://nshipster.com/assets/network-link-conditioner-install--light-5742743446fec494023649d0d38341ad4df3a39c81dd0a66f4c779eff597a4fe3636f6cb42aa10ea1e130c75555842bdcbdebb04858d4b08257488aa6e4dbe76.png)

Click on the Network Link Conditioner preference pane at the bottom of System Preferences.

![Network Link Conditioner](https://nshipster.com/assets/network-link-conditioner-preference-pane--light-0fdd2adf0b2df413eb5b68f2ef3210fcd95a47dac5622a057f065217e49edebd46cc03d007c7e5958720e60d8c05ce6fc696672024dca52831b870bfabc5a4e1.png)

## Controlling Bandwidth, Latency, and Packet Loss

Enabling the Network Link Conditioner changes the network environment system-wide according to the selected configuration, limiting uplink or download [bandwidth](https://en.wikipedia.org/wiki/Bandwidth_%28computing%29), [latency](https://en.wikipedia.org/wiki/Latency_%28engineering%29%23Communication_latency), and rate of [packet loss](https://en.wikipedia.org/wiki/Packet_loss).

You can choose from one of the following presets:

- 100% Loss
- 3G
- DSL
- EDGE
- High Latency DNS
- LTE
- Very Bad Network
- WiFi
- WiFi 802.11ac

…or create your own according to your particular requirements.

![Preset](https://nshipster.com/assets/network-link-conditioner-preset-90a1ad42f1dadd577eb4f5ebbeef5e76f9535b520632d3f94792d1020d8e8d1f6e2ba5aa395504e0dd7011371b20fe9eca3233e684e7a67c14409a5c040a358a.png)

---

Now try running your app with the Network Link Conditioner enabled:

How does network latency affect your app startup?   
 What effect does bandwidth have on table view scroll performance?   
 Does your app work at all with 100% packet loss?

## Enabling Network Link Conditioner on iOS Devices

Although the preference pane works well for developing on the simulator, it’s also important to test on a real device. Fortunately, the Network Link Conditioner is available for iOS as well.

To use the Network Link Conditioner on iOS, set up your device for development:

1. Connect your iOS device to your Mac
2. In Xcode, navigate to Window \> Devices & Simulators
3. Select your device in the sidebar
4. Click “Use for Development”

![iOS Devices](https://nshipster.com/assets/network-link-conditioner-ios-28f5a485b77714d22a91039b894e51708e0bce5b9a4f8ad4a7235e999519d85bed21d262ccfc53d98e541b0627bf37e65db50107152c1f5a05892662435b99ce.png)

Now you’ll have access to the Developer section of the Settings app. You can enable and configure the Network Link Conditioner on your iOS device under Settings \> Developer \> Networking. (Just remember to turn it off after you’re done testing!).
