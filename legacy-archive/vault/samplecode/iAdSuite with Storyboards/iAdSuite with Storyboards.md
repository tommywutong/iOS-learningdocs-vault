---
title: iAdSuite with Storyboards
apple_id: DTS40013458
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2015-10-29'
source_url: https://developer.apple.com/library/archive/samplecode/iAdSuite_Storyboard/Introduction/Intro.html
archived_at: '2026-07-18T03:29:31.562208Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](SplitNavigationBanner-SplitNavigationBanner-main.m.md)

# iAdSuite with Storyboards

|  |  |
| --- | --- |
| __Last Revision:__ | Version 4.1, 2015-10-29 Updated SplitNavigationBanner project to use adaptive storyboard with Auto Layout. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgnbvhawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS 8.0 SDK, Automated Reference Counting (ARC). |
| __Runtime Requirements:__ | iOS 8.0 or later |

iAdSuite is a set of samples demonstrating how to manage an ADBannerView in many common scenarios, each scenario demonstrated in a particular sample application.

In many of the samples the content is represented by a simple TextViewController view controller that displays some text in a read-only UITextView and runs a timer. The UITextView represents your application's content and the timer represents ongoing activity in your application that you will want to pause when the advertisement takes over the user interface. The MediumRectBanner sample uses a UICollectionView with image content instead, adding the banners as additional cells.

The traditional banner (represented with the ADAdTypeBanner constant) is expected to be placed at or near the bottom of the screen and placed to consume the full width of the screen. New in iOS 6 is the Medium Rect sized banner (represented with the ADAdTypeMediumRectangle constant) which is intended to be placed inline with other content from your application. It is highly recommended that you create only a single instance of each type of banner that you use (so if you use both a banner and medium rect type, you would have at most 1 instance of each) and that you share these instances among the places in your UI that they are used.

[Next](SplitNavigationBanner-SplitNavigationBanner-main.m.md)

