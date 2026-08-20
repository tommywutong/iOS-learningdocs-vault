---
title: Collection View Transition
apple_id: DTS40013415
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2013-10-29'
source_url: https://developer.apple.com/library/archive/samplecode/CollectionViewTransition/Introduction/Intro.html
archived_at: '2026-07-18T03:03:52.718909Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Collection View Transition

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2013-10-29 First public release. |
| __Build Requirements:__ | Xcode 5.0 or later; iOS SDK 7.0 or later. |
| __Runtime Requirements:__ | iOS 7.0 or later. |

This sample illustrates how to create a custom transition when navigating between two collection views in a navigation hierarchy managed by a navigation controller. The transition can be interrupted and reversed. It uses a subclass of UICollectionViewTransitionLayout to help in the transition of the cell positions based on gesture position.

The application has two view collection view controllers that display images. The first is a stack view, the second is a grid view. You can transition from the stack to the grid by tapping on the stack. You can also use a pinch gesture, in which case you can control the speed of, and even reverse, the transition.

This sample was part of the WWDC 2013 session 218: "Custom Transitions Using View Controllers".

[Next](ReadMe.txt.md)

