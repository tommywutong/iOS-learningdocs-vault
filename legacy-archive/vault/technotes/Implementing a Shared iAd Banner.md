---
title: Implementing a Shared iAd Banner
apple_id: DTS40011212
resource_type: Technical Note
platform: iOS
topic: User Experience
technology: null
published: '2014-07-18'
source_url: https://developer.apple.com/library/archive/technotes/tn2286/_index.html
archived_at: '2026-07-26T19:54:10.077158Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2286

# Implementing a Shared iAd Banner

Why you should use a single shared iAd banner, and how to implement it in your application.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrgiwugsbrfvke4vcbi4yq)[Show and hide your iAd banner](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrgiwugsbrfvke4vcbi4za)[Use a single shared iAd banner](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrgiwugsbrfvke4vcbi4zq)[Why use a shared banner](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrgiwugsbrfvke4vcbi4zs2v2ilfpvku2fl5av6u2iifjekrc7ijau4tsfki)[How to implement a shared banner](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrgiwugsbrfvke4vcbi4zs2scpk5pvit27jfgvatcfjvcu4vc7ifpvgscbkjcuix2cifhe4rks)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrgiwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

There are two best practices you'll want to implement when integrating iAd into your iOS application. First, show and hide your iAd banner based on inventory availability; second, use a single shared iAd banner across multiple views. See the TabbedBanner sample code from [iAdSuite](https://developer.apple.com/library/ios/samplecode/iAdSuite/Introduction/Intro.html#//apple_ref/doc/uid/DTS40010198) and [iAdSuite with Storyboards](https://developer.apple.com/library/ios/samplecode/iAdSuite_Storyboard/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013458) that demonstrates how to implement a shared iAd banner.

[Back to Top](#)

## Show and hide your iAd banner

You should hide your iAd banner when ad inventory is unavailable. [QA1641: Hiding iAd banners when ads are not available](https://developer.apple.com/library/ios/#qa/qa1641/_index.html) explains when and how you should hide the iAd banner.

[Back to Top](#)

## Use a single shared iAd banner

### Why use a shared banner

If your application has multiple tabs or views displaying an iAd banner, you should share a single instance of `ADBannerView` across each view.

Using a shared banner allows maximum efficiency in retrieving ad inventory for your app. The longest wait for iAd inventory is when the `ADBannerView` is instantiated. After that, ad inventory refreshes on a periodic basis. If you delete and recreate the `ADBannerView` every time the view switches, your wait for inventory is reset and induces a delay in waiting for another ad to become available.

### How to implement a shared banner

- Create an `ADBannerView` instance belonging to your app delegate soon after your application launches, for example, in `-application:didFinishLaunchingWithOptions:` of your app delegate.
- Use your application delegate as the banner's delegate. Have your application delegate tell the current view controller if it should show or hide the banner. You can use `UINavigationControllerDelegate` or `UITabBarControllerDelegate` protocol to push the banner to show it.

  __Note:__ This is important for cases where you do not want to have an ad (such as a modal view controller) – if you get a message while that controller is up, you may not be able to respond correctly if you have no delegate.
- Because the banner is owned by your app delegate, there is never a need to either release the banner, nor set its delegate to `nil`.
[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-07-18 | Fixed typo and added links to the iAdSuite and iAdSuite with Storyboard sample codes. |
| 2011-09-07 | New document that describes best practices for implementing a shared iAd banner across multiple views. |

