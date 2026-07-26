---
title: Introducing Pop, the animation engine behind Paper
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2014/04/28/ios/introducing-pop-the-animation-engine-behind-paper/'
original_language: en
published: 2014-04-28
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:963815db989dced0'
translated: false
---

> 原文：[Introducing Pop, the animation engine behind Paper](https://engineering.fb.com/2014/04/28/ios/introducing-pop-the-animation-engine-behind-paper/)　·　Meta Engineering — iOS

A couple of months ago we launched [Paper](https://engineering.fb.com/posts/656530327776932/building-paper/), a fluid and beautiful way to explore and share stories. Today we’re open-sourcing Pop, the animation engine behind the application’s smooth animations and transitions. Using dynamic instead of traditional static animations, Pop drives the scrolling, bouncing, and unfolding effects that bring Paper to life.

## Need for Pop

Since the original iPhone, iOS has excelled at supporting static animations. The Apple-provided Core Animation framework makes linear, ease-in, ease-out, and ease-in-ease-out animations simple to leverage.

![](https://engineering.fb.com/wp-content/uploads/2014/04/GIX_DABmrNCA_0AFALUo9hAAAAAAbj0JAAAD.png)

The innovation of touch interfaces has ushered in a new wave of software design. Direct manipulation of on-screen elements has removed one level of indirection, which in turn has raised our expectations for the screen as a medium. If objects respond to our touches, they should also respond to the velocity of our flick.

When I co-founded Push Pop Press in 2010, our goal was to create a realistic, physics-everywhere experience. We wanted a solution that would allow us to evoke the same delightful experience of UIScrollView throughout the whole application. Pop is the latest manifestation of that vision, allowing us to keep the familiar and powerful programming model of Core Animation while also capturing a gesture’s velocity and better reflecting user intent. Paper has given us the opportunity to further refine both the vision and the animation engine behind it.

## The goals

Pop aims to offer utility on three different axes. First, we wanted to make commonly needed animations extremely convenient. In addition to the four established static animations, Pop introduces three new primitive animation types: spring, decay, and custom.

![](https://engineering.fb.com/wp-content/uploads/2014/04/GFT_DADPI77z5Y0BALSZ5jUAAAAAbj0JAAAD.png)

“Spring” and “decay” are dynamic animations that help bring Paper to life. “Spring” gives Paper elements their attractive bounce. “Decay” brings movement to an eventual slow halt. Both take velocity as an input and are good candidates for realistically responding to user gestures.

Second, Pop was designed to be an extensible framework. Custom animation allows developers to plug in their own animation code, making it easier to create unique effects. By decoupling animation from display, we created a framework of wide scope. Pop can animate any property of any Objective-C object.

Third, we aimed to construct a developer-friendly yet powerful programming model. For example, Core Animation developers should recognize this API:

![](https://engineering.fb.com/wp-content/uploads/2014/04/GEM8mwCXPxyVQgsBACAASzcAAAAAbj0JAAAD.png)

This is the Core Animation interface for starting and stopping animations. Most notably, it also supports querying running animations – which is key for interrupting animations and building fluid interfaces. Here is the Pop API for the same function:

![](https://engineering.fb.com/wp-content/uploads/2014/04/GIX_DACVk72oRUUCAIPLajoAAAAAbj0JAAAD.png)

The fundamental animation type is a POPAnimation. The choice of category addition on NSObject allows any object to be animated. The API otherwise remains unchanged.

The following code snippet showcases how to animate the bounds of a layer using a spring:

![](https://engineering.fb.com/wp-content/uploads/2014/04/GEM8mwAttZnaIk8CAHbQ4TIAAAAAbj0JAAAD.png)

If you know how to use Core Animation explicit animations, you know how to use Pop.

## Open source

Pop is our latest iOS open source release, joining KVOController, Shimmer, and Tweaks. We’re excited to incorporate your feedback and look forward to your creations.

You can access Pop [here](https://github.com/facebook/pop).

![](https://engineering.fb.com/wp-content/uploads/2014/04/GEM8mwDWRF_3pDsCAJHaCw0AAAAAbj0JAAAD.png)
