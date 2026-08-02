---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/iAd.html
archived_at: '2026-07-18T02:56:02.097033Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# iAd Changes

## iAd

ADBannerView.hModified [-[ADBannerView initWithAdType:]](https://developer.apple.com/documentation/iad/adbannerview/1614692-initwithadtype)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithAdType:(ADAdType)type ``` |
| To | ``` - (instancetype)initWithAdType:(ADAdType)type ``` |

Modified [-[ADBannerViewDelegate bannerView:didFailToReceiveAdWithError:]](https://developer.apple.com/documentation/iad/adbannerviewdelegate/1614619-bannerview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[ADBannerViewDelegate bannerViewActionDidFinish:]](https://developer.apple.com/documentation/iad/adbannerviewdelegate/1614662-bannerviewactiondidfinish)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[ADBannerViewDelegate bannerViewActionShouldBegin:willLeaveApplication:]](https://developer.apple.com/documentation/iad/adbannerviewdelegate/1614641-bannerviewactionshouldbegin)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[ADBannerViewDelegate bannerViewDidLoadAd:]](https://developer.apple.com/documentation/iad/adbannerviewdelegate/1614625-bannerviewdidloadad)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[ADBannerViewDelegate bannerViewWillLoadAd:]](https://developer.apple.com/documentation/iad/adbannerviewdelegate/1614636-bannerviewwillloadad)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [ADErrorAdUnloaded](https://developer.apple.com/documentation/iad/aderror/code/adunloaded)

|  | Introduction |
| --- | --- |
| From | iOS 6.0 |
| To | iOS 4.0 |

Modified [ADErrorApplicationInactive](https://developer.apple.com/documentation/iad/aderror/aderrorapplicationinactive)

|  | Introduction |
| --- | --- |
| From | iOS 4.3 |
| To | iOS 4.0 |

Modified [ADErrorBannerVisibleWithoutContent](https://developer.apple.com/documentation/iad/aderror/code/bannervisiblewithoutcontent)

|  | Introduction |
| --- | --- |
| From | iOS 4.1 |
| To | iOS 4.0 |

Modified [ADErrorConfigurationError](https://developer.apple.com/documentation/iad/aderror/code/configurationerror)

|  | Introduction |
| --- | --- |
| From | iOS 4.1 |
| To | iOS 4.0 |

ADClient.hAdded [-[ADClient addClientToSegments:replaceExisting:]](https://developer.apple.com/documentation/iad/adclient/1614607-add)Added [-[ADClient lookupAdConversionDetails:]](https://developer.apple.com/documentation/iad/adclient/1614612-lookupadconversiondetails)ADInterstitialAd.hModified [-[ADInterstitialAdDelegate interstitialAdActionDidFinish:]](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614637-interstitialadactiondidfinish)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[ADInterstitialAdDelegate interstitialAdActionShouldBegin:willLeaveApplication:]](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614652-interstitialadactionshouldbegin)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[ADInterstitialAdDelegate interstitialAdDidLoad:]](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614609-interstitialaddidload)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[ADInterstitialAdDelegate interstitialAdWillLoad:]](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614688-interstitialadwillload)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

AVPlayerViewController_iAdPreroll.h (Added)Added [-[AVPlayerViewController cancelPreroll]](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/1614626-cancelpreroll)Added [-[AVPlayerViewController playPrerollAdWithCompletionHandler:]](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/1614638-playprerollad)Added [+[AVPlayerViewController preparePrerollAds]](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/1614660-prepareprerollads)Added AVPlayerViewController(iAdPreroll)MPMoviePlayerController_iAdPreroll.hAdded [-[MPMoviePlayerController cancelPreroll]](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1614613-cancelpreroll)UIViewControlleriAdAdditions.hRemoved [-[UIViewController shouldPresentInterstitialAd]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1614627-shouldpresentinterstitialad)Added [UIViewController.shouldPresentInterstitialAd](https://developer.apple.com/documentation/uikit/uiviewcontroller/1614627-shouldpresentinterstitialad)

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
