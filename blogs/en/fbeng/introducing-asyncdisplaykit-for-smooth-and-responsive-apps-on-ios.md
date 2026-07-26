---
title: 'Introducing AsyncDisplayKit: For smooth and responsive apps on iOS'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2014/10/15/ios/introducing-asyncdisplaykit-for-smooth-and-responsive-apps-on-ios/'
original_language: en
published: 2014-10-15
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:8862485472150534'
translated: false
---

> 原文：[Introducing AsyncDisplayKit: For smooth and responsive apps on iOS](https://engineering.fb.com/2014/10/15/ios/introducing-asyncdisplaykit-for-smooth-and-responsive-apps-on-ios/)　·　Meta Engineering — iOS

Have you ever noticed apps stuttering as you scroll and swipe around? Tapped a button and watched the entire interface freeze as it tries to react? iOS is well-known for its user experience quality bar, but meeting that bar can be difficult, especially on older iPhones and iPads. Polished apps typically use piecemeal performance optimizations to keep their interfaces fluid, treating different sources of slowness as different problems. Today we’re open-sourcing AsyncDisplayKit, a framework that offers a holistic way to keep your app smooth and responsive.

[![](https://engineering.fb.com/wp-content/uploads/2014/10/GFX_DABw2mnhocECAKOX2xgAAAAAbj0JAAAD.png)](http://asyncdisplaykit.org/)

## The case for AsyncDisplayKit

iOS user interface functionality — drawing to the screen, responding to touch events, running physics simulations for inertial scrolling, and so on — is bottlenecked by the main thread. For an app to maintain the gold standard of 60 frames per second, it can only use the main thread for milliseconds at a time. But main-thread-only UIKit views like UIImageView and UITextView can take tens to hundreds of milliseconds to size and display themselves. And while the main thread is decoding an image or rendering text, it can’t respond to user input or keep up with scrolling.

Since using stock UIKit views can cause slowdowns, performant apps tend to have workarounds for individual UIKit components. Instead of letting UIImageView do expensive work itself, they might manually use Core Graphics to decompress JPEGs and PNGs in the background; instead of using UITextView, they might work with Core Text directly. This approach is effective, but has limitations — individual workarounds tend to behave differently, making it difficult to reason about higher-level improvements and application behavior.

AsyncDisplayKit builds on UIKit and Core Animation to offer a general solution. Its image and text views can be used without blocking the main thread, offering a drop-in solution for this common task. More importantly, it supports asynchronously creating and rendering complex view hierarchies the same way.

## Introducing the node

The AsyncDisplayKit _node_ is a thread-safe abstraction over UIView, which is in turn an abstraction over CALayer:

![](https://engineering.fb.com/wp-content/uploads/2014/10/GNPXoAC5axq2pj8FAFBrjkYAAAAAbj0JAAAD.png)

If you know how to use views, you know how to use nodes. ASImageNode and the Text Kit-powered ASTextNode can be used just like their UIKit counterparts. Unlike UIKit view hierarchies, node hierarchies for entire screenfuls of content can be initialized and laid out on background threads — and nodes make it easy to take advantage of the multicore CPUs in all current iOS devices.

Nodes have many advantages over views. For example, you can often improve performance by replacing views with layers. Unfortunately, doing so requires the tedious process of porting view-based code to the different API and inevitably risks regressions. With nodes, it’s as easy as:

![](https://engineering.fb.com/wp-content/uploads/2014/10/GN-KowDO4Y3TvMICAIVKpBoAAAAAbj0JAAAD.png)

If you later need to switch from layers back to views, it’s a one-line change! This is a transformational difference. Instead of being cautious of layer-backed UI code, you can use it by default whenever you don’t need touch handling.

## Getting started

AsyncDisplayKit is robust and ready for use in your apps. We originally built it to make [Paper](https://facebook.com/paper)’s highly tactile user interface possible, and it goes hand-in-hand with the [Pop animation engine](https://engineering.fb.com/posts/234067533455773/introducing-pop-the-animation-engine-behind-paper/), but it’s just as powerful with [UIKit Dynamics](https://developer.apple.com/library/ios/documentation/Miscellaneous/Conceptual/iPhoneOSTechOverview/iPhoneOSTechnologies/iPhoneOSTechnologies.html#//apple_ref/doc/uid/TP40007898-CH3-SW14) and conventional app designs. We can’t wait to see what you’ll create with it.

Check out the [guide](http://asyncdisplaykit.org/guide/) or the [NSLondon talk](http://vimeo.com/103589245) to learn more. AsyncDisplayKit is available on [GitHub](https://github.com/facebook/AsyncDisplayKit).
