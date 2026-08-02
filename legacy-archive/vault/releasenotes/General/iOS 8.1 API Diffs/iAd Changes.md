---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/iAd.html
archived_at: '2026-07-18T02:56:18.401075Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# iAd Changes

## iAd

Added AVPlayerViewController.cancelPreroll()Added AVPlayerViewController.playPrerollAdWithCompletionHandler(((NSError!) -> Void)!)Added AVPlayerViewController.preparePrerollAds() [class]Added MPMoviePlayerController.cancelPreroll()Added MPMoviePlayerController.playPrerollAdWithCompletionHandler(((NSError!) -> Void)!)Added MPMoviePlayerController.preparePrerollAds() [class]Added UIViewController.canDisplayBannerAdsAdded UIViewController.displayingBannerAdAdded UIViewController.interstitialPresentationPolicyAdded UIViewController.originalContentViewAdded UIViewController.prepareInterstitialAds() [class]Added UIViewController.presentingFullScreenAdAdded UIViewController.requestInterstitialAdPresentation() -> BoolAdded UIViewController.shouldPresentInterstitialAdModified ADAdType [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified ADBannerView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ADBannerView.adType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified ADBannerView.init(adType: ADAdType)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(adType type: ADAdType) ``` | iOS 8.0 |
| To | ``` init!(adType type: ADAdType) ``` | iOS 6.0 |

Modified ADBannerViewDelegate.bannerViewWillLoadAd(ADBannerView!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified ADClient

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified ADClient.determineAppInstallationAttributionWithCompletionHandler(((Bool) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified ADClient.sharedClient() -> ADClient! [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified ADError [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ADInterstitialAd

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified ADInterstitialAdDelegate.interstitialAdWillLoad(ADInterstitialAd!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified ADInterstitialPresentationPolicy [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
