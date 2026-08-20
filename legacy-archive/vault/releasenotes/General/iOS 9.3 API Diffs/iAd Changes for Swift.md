---
title: iOS 9.3 API Diffs
apple_id: TP40016662
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS93APIDiffs/Swift/iAd.html
archived_at: '2026-07-18T02:57:17.216937Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.3 API Diffs](iOS%209.2%20to%20iOS%209.3%20API%20Differences.md)


# iAd Changes for Swift

### iAd

Added [ADError.AssetLoadFailure](https://developer.apple.com/documentation/iad/aderror/code/assetloadfailure)Modified [ADBannerView](https://developer.apple.com/documentation/iad/adbannerview)

|  | Declaration |
| --- | --- |
| From | ``` class ADBannerView : UIView {     init!(adType type: ADAdType)     var adType: ADAdType { get }     weak var delegate: ADBannerViewDelegate?     var bannerLoaded: Bool { get }     var bannerViewActionInProgress: Bool { get }     func cancelBannerViewAction()     var advertisingSection: String! } extension ADBannerView {     var requiredContentSizeIdentifiers: Set<NSObject>!     var currentContentSizeIdentifier: String!     class func sizeFromBannerContentSizeIdentifier(_ contentSizeIdentifier: String!) -> CGSize } ``` |
| To | ``` class ADBannerView : UIView {     init!(adType type: ADAdType)     var adType: ADAdType { get }     weak var delegate: ADBannerViewDelegate!     var bannerLoaded: Bool { get }     var bannerViewActionInProgress: Bool { get }     func cancelBannerViewAction()     var advertisingSection: String! } extension ADBannerView {     var requiredContentSizeIdentifiers: Set<NSObject>!     var currentContentSizeIdentifier: String!     class func sizeFromBannerContentSizeIdentifier(_ contentSizeIdentifier: String!) -> CGSize } ``` |

Modified [ADBannerView.delegate](https://developer.apple.com/documentation/iad/adbannerview/1614649-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: ADBannerViewDelegate? ``` |
| To | ``` weak var delegate: ADBannerViewDelegate! ``` |

Modified [ADError [enum]](https://developer.apple.com/documentation/iad/aderror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum ADError : Int {     case Unknown     case ServerFailure     case LoadingThrottled     case InventoryUnavailable     case ConfigurationError     case BannerVisibleWithoutContent     case ApplicationInactive     case AdUnloaded } ``` |
| To | ``` enum ADError : Int {     case Unknown     case ServerFailure     case LoadingThrottled     case InventoryUnavailable     case ConfigurationError     case BannerVisibleWithoutContent     case ApplicationInactive     case AdUnloaded     case AssetLoadFailure } ``` |

Modified [ADInterstitialAd](https://developer.apple.com/documentation/iad/adinterstitialad)

|  | Declaration |
| --- | --- |
| From | ``` class ADInterstitialAd : NSObject {     weak var delegate: ADInterstitialAdDelegate?     var loaded: Bool { get }     var actionInProgress: Bool { get }     func cancelAction()     func presentInView(_ containerView: UIView!) -> Bool     func presentFromViewController(_ viewController: UIViewController!) } ``` |
| To | ``` class ADInterstitialAd : NSObject {     weak var delegate: ADInterstitialAdDelegate!     var loaded: Bool { get }     var actionInProgress: Bool { get }     func cancelAction()     func presentInView(_ containerView: UIView!) -> Bool     func presentFromViewController(_ viewController: UIViewController!) } ``` |

Modified [ADInterstitialAd.delegate](https://developer.apple.com/documentation/iad/adinterstitialad/1614647-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: ADInterstitialAdDelegate? ``` |
| To | ``` weak var delegate: ADInterstitialAdDelegate! ``` |

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
