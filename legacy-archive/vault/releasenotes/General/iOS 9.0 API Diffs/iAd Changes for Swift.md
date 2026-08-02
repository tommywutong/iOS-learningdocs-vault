---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/iAd.html
archived_at: '2026-07-18T02:57:04.160744Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# iAd Changes for Swift

### iAd

Added [ADClient.requestAttributionDetailsWithBlock(_: (([NSObject : AnyObject]!, NSError!) -> Void)!)](https://developer.apple.com/documentation/iad/adclient/1614620-requestattributiondetails)Added [ADClientError [enum]](https://developer.apple.com/documentation/iad/adclienterror/code)Added [ADClientError.LimitAdTracking](https://developer.apple.com/documentation/iad/adclienterror/code/limitadtracking)Added [ADClientError.Unknown](https://developer.apple.com/documentation/iad/adclienterror/adclienterrorunknown)Added [ADClientErrorDomain](https://developer.apple.com/documentation/iad/adclienterrordomain)Modified [ADAdType [enum]](https://developer.apple.com/documentation/iad/adadtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [ADBannerView](https://developer.apple.com/documentation/iad/adbannerview)

|  | Declaration |
| --- | --- |
| From | ``` class ADBannerView : UIView {     init!(adType type: ADAdType)     var adType: ADAdType { get }     weak var delegate: ADBannerViewDelegate!     var bannerLoaded: Bool { get }     var bannerViewActionInProgress: Bool { get }     func cancelBannerViewAction()     var advertisingSection: String! } extension ADBannerView {     var requiredContentSizeIdentifiers: Set<NSObject>!     var currentContentSizeIdentifier: String!     class func sizeFromBannerContentSizeIdentifier(_ contentSizeIdentifier: String!) -> CGSize } ``` |
| To | ``` class ADBannerView : UIView {     init!(adType type: ADAdType)     var adType: ADAdType { get }     weak var delegate: ADBannerViewDelegate?     var bannerLoaded: Bool { get }     var bannerViewActionInProgress: Bool { get }     func cancelBannerViewAction()     var advertisingSection: String! } extension ADBannerView {     var requiredContentSizeIdentifiers: Set<NSObject>!     var currentContentSizeIdentifier: String!     class func sizeFromBannerContentSizeIdentifier(_ contentSizeIdentifier: String!) -> CGSize } ``` |

Modified [ADBannerView.delegate](https://developer.apple.com/documentation/iad/adbannerview/1614649-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: ADBannerViewDelegate! ``` |
| To | ``` weak var delegate: ADBannerViewDelegate? ``` |

Modified [ADBannerViewDelegate.bannerView(_: ADBannerView!, didFailToReceiveAdWithError: NSError!)](https://developer.apple.com/documentation/iad/adbannerviewdelegate/1614619-bannerview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified [ADBannerViewDelegate.bannerViewActionDidFinish(_: ADBannerView!)](https://developer.apple.com/documentation/iad/adbannerviewdelegate/1614662-bannerviewactiondidfinish)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified [ADBannerViewDelegate.bannerViewActionShouldBegin(_: ADBannerView!, willLeaveApplication: Bool) -> Bool](https://developer.apple.com/documentation/iad/adbannerviewdelegate/1614641-bannerviewactionshouldbegin)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified [ADBannerViewDelegate.bannerViewDidLoadAd(_: ADBannerView!)](https://developer.apple.com/documentation/iad/adbannerviewdelegate/1614625-bannerviewdidloadad)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified [ADClient](https://developer.apple.com/documentation/iad/adclient)

|  | Declaration |
| --- | --- |
| From | ``` class ADClient : NSObject {     class func sharedClient() -> ADClient!     func determineAppInstallationAttributionWithCompletionHandler(_ completionHandler: ((Bool) -> Void)!)     func lookupAdConversionDetails(_ completionHandler: ((NSDate!, NSDate!) -> Void)!)     func addClientToSegments(_ segmentIdentifiers: [AnyObject]!, replaceExisting replaceExisting: Bool) } ``` |
| To | ``` class ADClient : NSObject {     class func sharedClient() -> ADClient!     func determineAppInstallationAttributionWithCompletionHandler(_ completionHandler: ((Bool) -> Void)!)     func lookupAdConversionDetails(_ completionHandler: ((NSDate!, NSDate!) -> Void)!)     func requestAttributionDetailsWithBlock(_ completionHandler: (([NSObject : AnyObject]!, NSError!) -> Void)!)     func addClientToSegments(_ segmentIdentifiers: [AnyObject]!, replaceExisting replaceExisting: Bool) } ``` |

Modified [ADClient.determineAppInstallationAttributionWithCompletionHandler(_: ((Bool) -> Void)!)](https://developer.apple.com/documentation/iad/adclient/1614672-determineappinstallationattribut)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ADClient.lookupAdConversionDetails(_: ((NSDate!, NSDate!) -> Void)!)](https://developer.apple.com/documentation/iad/adclient/1614612-lookupadconversiondetails)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ADError [enum]](https://developer.apple.com/documentation/iad/aderror/code)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [ADInterstitialAd](https://developer.apple.com/documentation/iad/adinterstitialad)

|  | Declaration |
| --- | --- |
| From | ``` class ADInterstitialAd : NSObject {     weak var delegate: ADInterstitialAdDelegate!     var loaded: Bool { get }     var actionInProgress: Bool { get }     func cancelAction()     func presentInView(_ containerView: UIView!) -> Bool     func presentFromViewController(_ viewController: UIViewController!) } ``` |
| To | ``` class ADInterstitialAd : NSObject {     weak var delegate: ADInterstitialAdDelegate?     var loaded: Bool { get }     var actionInProgress: Bool { get }     func cancelAction()     func presentInView(_ containerView: UIView!) -> Bool     func presentFromViewController(_ viewController: UIViewController!) } ``` |

Modified [ADInterstitialAd.delegate](https://developer.apple.com/documentation/iad/adinterstitialad/1614647-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: ADInterstitialAdDelegate! ``` |
| To | ``` weak var delegate: ADInterstitialAdDelegate? ``` |

Modified [ADInterstitialAdDelegate.interstitialAd(_: ADInterstitialAd!, didFailWithError: NSError!)](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614645-interstitialad)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified [ADInterstitialAdDelegate.interstitialAdActionDidFinish(_: ADInterstitialAd!)](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614637-interstitialadactiondidfinish)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified [ADInterstitialAdDelegate.interstitialAdActionShouldBegin(_: ADInterstitialAd!, willLeaveApplication: Bool) -> Bool](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614652-interstitialadactionshouldbegin)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified [ADInterstitialAdDelegate.interstitialAdDidLoad(_: ADInterstitialAd!)](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614609-interstitialaddidload)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified [ADInterstitialAdDelegate.interstitialAdDidUnload(_: ADInterstitialAd!)](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614651-interstitialaddidunload)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified [ADInterstitialPresentationPolicy [enum]](https://developer.apple.com/documentation/iad/adinterstitialpresentationpolicy)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

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
