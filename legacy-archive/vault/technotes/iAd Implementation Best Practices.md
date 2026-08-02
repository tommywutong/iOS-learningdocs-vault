---
title: iAd Implementation Best Practices
apple_id: DTS40011827
resource_type: Technical Note
platform: iOS
topic: null
technology: iAd
published: '2014-08-25'
source_url: https://developer.apple.com/library/archive/technotes/tn2264/_index.html
archived_at: '2026-07-26T19:54:10.176696Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2264

# iAd Implementation Best Practices

Handy checklist of best practices for developers looking to successfully integrate the iAd Network with their iOS app.

Below is an overview of best practices to follow in order to optimize your participation in the iAd Network. By following these guidelines you will maximize your revenue opportunity and ensure the best customer experience in your app(s).

[Agree to the iAd Network Contract and Enable Your App for iAd Advertising in iTunes Connect](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcobsg4wugsbrfvauousfivpvit27kreekx2jifcf6tsfkrlu6usll5bu6tsukjaugvc7ifheix2fjzauetcfl5mu6vksl5avauc7izhvex2jifcf6qkekzcvevcjkneu4r27jfhf6skukvheku27inhu4tsfinka)[Create Universal Apps](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcobsg4wugsbrfvbverkbkrcv6vkojflekustifgf6qkqkbjq)[Display a Single iAd Banner Per Screen](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcobsg4wugsbrfvcesu2qjravsx2bl5justshjrcv6skbirpueqkojzcvex2qivjf6u2dkjcuktq)[Handle Banner Orientation Changes Dynamically](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcobsg4wugsbrfveectsejrcv6qsbjzhekus7j5jesrkokraviskpjzpugscbjzduku27irmu4qknjfbuctcmle)[Hide Blank or Empty Banners](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcobsg4wugsbrfveesrcfl5beyqkojnpu6us7ivgvavczl5bectsoivjfg)[Prevent Calls to Non-existent Delegates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcobsg4wugsbrfviferkwivhfix2difgeyu27krhv6tspjzpukwcjknkektsul5cektcfi5avirkt)[Share ADBannerView Instances Across Views](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcobsg4wugsbrfvjuqqksivpucrccifhe4rkskzeukv27jfhfgvcbjzbuku27ifbvet2tknpvmskfk5jq)[Display iAd Banners for at Least 30 Seconds](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcobsg4wugsbrfvcesu2qjravsx2jifcf6qsbjzhekustl5de6us7ifkf6tcfifjvixztgbpvgrkdj5heiuy)[Ensure Your Mediation Layer is Properly Configured](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcobsg4wugsbrfvcu4u2vkjcv6wkpkvjf6tkfireucvcjj5hf6tcblfcvex2jknpvauspkbcvetczl5bu6tsgjfdvkusfiq)[Test iAd Banners More Effectively](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcobsg4wugsbrfvkeku2ul5eucrc7ijau4tsfkjjv6tkpkjcv6rkgizcugvcjkzcuywi)[Log Error Messages](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcobsg4wugsbrfvge6r27ivjfet2sl5guku2tifdukuy)[Review the Examples](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcobsg4wugsbrfvjekvsjivlv6vciivpukwcbjvieyrkt)[A Final Note](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcobsg4wugsbrfvav6rsjjzauyx2oj5kek)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcobsg4wvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Agree to the iAd Network Contract and Enable Your App for iAd Advertising in iTunes Connect

1. Go to [http://itunesconnect.apple.com](http://itunesconnect.apple.com) to review and agree to the iAd Network Contract located within the “Contracts, Tax and Banking Information” module.
2. Complete the required iAd Network tax forms, and if you have not already done so, set up your banking information.

[Back to Top](#)

## Create Universal Apps

To ensure your app is capable of displaying iAd banners for all your users, make sure you’ve developed a universal app that supports all possible devices. iPhone apps running in compatibility mode on iPad will not display a test ad in development or live ads in deployed apps.

[Back to Top](#)

## Display a Single iAd Banner Per Screen

To maximize performance and user engagement, be sure to display only a single iAd banner on each screen of your app. Apps with multiple iAd banners on a screen may be rejected.

[Back to Top](#)

## Handle Banner Orientation Changes Dynamically

If your application supports iOS 5.1 or previous, when an orientation change occurs in your application, resize the banner view by setting the currentContentSizeIdentifier to ADBannerContentSizeIdentifierPortrait or ADBannerContentSizeIdentifierLandscape. If your app supports iOS 6 or later, call -sizeThatFits: on the banner view, specifying the bounds of the view that contains your banner, and use the returned size to resize the banner view. A full example of this can be found in the iAdSuite Sample Code at [http://developer.apple.com/iphone/library/samplecode/iAdSuite/Introduction/Intro.html](https://developer.apple.com/iphone/library/samplecode/iAdSuite/Introduction/Intro.html).

[Back to Top](#)

## Hide Blank or Empty Banners

To ensure an empty banner does not run in your live application, configure your banner view's frame to be offscreen, then add or resize your content to reclaim the empty banner space. Follow these steps to hide the banner view whenever ad content is not available:

1. When the banner view is initially loaded from a .xib or Storyboard: At launch, ad content may not yet be available to your app. You should hide the banner in your view controller's -viewDidLoad method.
2. When an error occurs: A banner view may fail to load an ad due to the lack of a network connection, inventory availability, or improper banner usage. You must hide the banner in the ADBannerView's bannerView:didFailToReceiveAdWithError: delegate method.
3. When ADBannerView's bannerLoaded is false: Check the ADBannerView's bannerLoaded property to determine if the banner should be hidden in the sections of code that address layout.

Be sure to review the Technical Q&A: “Hiding iAd banners when ads are not available” at [http://developer.apple.com/library/ios/#qa/qa1641/_index.html](https://developer.apple.com/library/ios/#qa/qa1641/_index.html) for more details.

[Back to Top](#)

## Prevent Calls to Non-existent Delegates

On iOS 4, to prevent delegate messages from an ADBannerView from being sent to an object that is no longer valid, always set your ADBannerView instance’s delegate property to nil before releasing it. If your application supports iOS 5 or later, the ADBannerView will nil the delegate automatically via the weak reference system.

[Back to Top](#)

## Share ADBannerView Instances Across Views

If your application has multiple tabs or views displaying an iAd banner, be sure to share a single instance of ADBannerView across each view to improve your users’ ability to interact with ads. As of iOS 6, the iAd framework takes measures to ensure ads are only served to a single banner view. We recommend you use a central object to act as the ADBannerView’s delegate. Review the “Implementing a Shared iAd Banner” technical note at [http://developer.apple.com/library/ios/#technotes/tn2286/_index.html](https://developer.apple.com/library/ios/#technotes/tn2286/_index.html) for complete details.

[Back to Top](#)

## Display iAd Banners for at Least 30 Seconds

If your application utilizes a timer for rotating advertisements, ensure the timer aligns with the iAd Network’s 30-second minimum rendering time in order to optimize ad performance in your application.

[Back to Top](#)

## Ensure Your Mediation Layer is Properly Configured

If you are integrating with a third party for ad serving, ensure that you are using the latest version of the mediation layer, and prioritize the iAd Network for ad serving. Additionally, configure your app to serve ads only in countries where the iAd Network is live and check to ensure that the framework supports dynamic banner views. If your mediation layer uses a timer for rotating banners, implement a 10-second timeout before cycling to another provider when an ad is not available. Finally, to monitor performance and track revenue, refer to the iAd Network module in iTunes Connect.

[Back to Top](#)

## Test iAd Banners More Effectively

In iOS 6, you can further test iAd banner functionality in your developer-mode app by setting Fill Rate and Ad Refresh Rate in your device’s Developer Settings. Adjusting “Fill Rate” allows you to test cases when a banner is available and when it is not. By setting “Ad Refresh Rate,” you can more efficiently test how your app handles banner loading and errors.

[Back to Top](#)

## Log Error Messages

When troubleshooting iAd errors, it is important to know what errors were returned by the iAd Network. So, be sure to log any error messages passed to bannerView: didFailToReceiveAdWithError: in all builds of your app.

[Back to Top](#)

## Review the Examples

The iAdSuite Sample Code at [http://developer.apple.com/iphone/library/samplecode/iAdSuite/Introduction/Intro.html](https://developer.apple.com/iphone/library/samplecode/iAdSuite/Introduction/Intro.html) includes several projects demonstrating iAd banner implementation best practices, including MREC banners for iPad, new in iOS 6. For those implementing full screen banners on iPad, please review the iAdInterstitialSuite at [http://developer.apple.com/library/ios/#samplecode/iAdInterstitialSuite/Introduction/Intro.html](https://developer.apple.com/library/ios/#samplecode/iAdInterstitialSuite/Introduction/Intro.html).

[Back to Top](#)

## A Final Note

Be sure to review the iAd relevant sections of the [https://developer.apple.com/appstore/resources/approval/guidelines.html](https://developer.apple.com/appstore/resources/approval/guidelines.html) and visit our iAd Network FAQ in [http://itunesconnect.apple.com](http://itunesconnect.apple.com) for further reference.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-08-25 | Editorial update. Updated the "Agree to the iAd Network Contract and Enable Your App for iAd Advertising in iTunes Connect" section. Added the "Log Error Messages" section. |
| 2013-02-28 | Typo corrections. |
| 2012-02-13 | New document that provides an overview of best practices and guidelines designed to help you maximize revenue and customer experience in your app(s). |

