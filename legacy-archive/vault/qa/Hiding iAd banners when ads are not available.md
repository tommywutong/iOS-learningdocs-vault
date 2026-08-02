---
title: Hiding iAd banners when ads are not available
apple_id: DTS40010247
resource_type: QA
platform: iOS
topic: User Experience
technology: iAd
published: '2010-09-14'
source_url: https://developer.apple.com/library/archive/qa/qa1641/_index.html
archived_at: '2026-07-18T02:33:10.033732Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1641

# Hiding iAd banners when ads are not available

## Q:  When and how should I hide iAd banners?

A: When and how should I hide iAd banners?

You should hide your banner view whenever ad content is not available; this includes:

- When the banner view is loaded from a xib file, as ad content may not yet be available to the app (you can hide the banner in your view controller's `-viewDidLoad` method)
- When an error occurs, such as the banner view failing to load a new ad (you can hide the banner in the ADBannerView's `bannerView:didFailToReceiveAdWithError:` delegate method)

You can hide the banner view by following the steps below.

First, check if your banner view has already downloaded an ad from `ADBannerView`'s `bannerLoaded` property. If it has not, you can proceed to hide the banner.

To hide the banner view, you should:

- Resize your banner view's frame to be offscreen
- Resize your content view's frame to cover the space originally hosting the banner

Specifically, if your banner is at the bottom of the screen, you should move the frame of the banner view down by the height of the banner; if your banner is at the top of the screen, you should move the frame of the banner view up by the height of the banner.

For a code example, see Sample Code "[iAdSuite](https://developer.apple.com/iphone/library/samplecode/iAdSuite/Introduction/Intro.html)". For more information on the banner view lifecycle, see the[iAd Programming Guide](https://developer.apple.com/iphone/library/documentation/UserExperience/Conceptual/iAd_Guide/Introduction/Introduction.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-09-14 | Updated for iOS 4.1. Move the frame instead of the center of the banner. |
| 2010-08-19 | New document that describes how to hide an iAd banner views when ads are not available. |

