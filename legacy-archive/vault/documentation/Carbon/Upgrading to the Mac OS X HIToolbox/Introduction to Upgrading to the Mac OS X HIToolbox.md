---
title: Upgrading to the Mac OS X HIToolbox
apple_id: TP30001140
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2004-06-28'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Upgrading_HIToolbox/upgrading_hitoolbox_intro/upgrading_hitoolbox_intro.html
archived_at: '2026-07-15T05:24:42.284892Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](The%20Modern%20Advantage.md)

# Introduction to Upgrading to the Mac OS X HIToolbox

One of the strengths of Mac OS X is its support of older Mac OS APIs, many of which were introduced before Mac OS 8, and some before System 7. This support made it easier to move older applications to Mac OS X. However, because many of these APIs were designed for a different system architecture, performance can suffer, and they often cannot take advantage of key Mac OS X features. Updating your application’s user interface code to use the windowing and event-handling models designed specifically for Mac OS X gives immediate benefits in performance, code maintainablity, and portabiity, and it enables you to adopt the latest Mac OS X technologies.

This document is for Carbon developers who have older applications that would benefit from using modern HIToolbox technologies. You should consider upgrading if your application uses any of the following older Apple technologies:

- Resource-based windows, controls, or menus
- The Dialog Manager
- Procedure pointer–based custom control definitions
- QuickDraw
- Event handling using `WaitNextEvent`, `StillDown`, `WaitMouseUp`, or `Button`.

An updated application will use nib-based windows and menus, with HIView-based controls (both standard and custom). All event handling is done through Carbon events, and all drawing in views is done using Quartz.

HIViews and compositing mode are supported in Mac OS X v10.2 and later. Carbon events (including Carbon event–based control definitions) and nib files are supported in Mac OS X v10.0 and later.

Even if you do not want to adopt all these technologies in your application right away, this document can guide you towards incremental changes that will make it easier to adopt new features.

This document is organized into the following chapters:

- [The Modern Advantage](The%20Modern%20Advantage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbqfvbuqmrqgiwugscejbeuurcf) describes the benefits of adopting the modern HIToolbox in your application.
- [Porting Steps](Porting%20Steps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbqfvbuqmrqgmwueqkcjbbusqkd) describes steps you should take to port your application to use the modern HIToolbox.
- [A Porting Example: Converting a User Item to a Custom View](A%20Porting%20Example-%20Converting%20a%20User%20Item%20to%20a%20Custom%20View.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbqfvbuqmrqgqwueqkcjbbusqkd) shows how you could convert an old dialog user item to a custom HIView.

In addition to this document, you may find the following documents useful:

- [Introducing HIView](../HIView%20Programming%20Guide/Introduction%20to%20HIView%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrt) describes the concepts behind HIViews and explains how they differ from older user interface elements. It also contains numerous programming examples.
- Technical Note TN2074, [HIView APIs Vs. Control Manager APIs](https://developer.apple.com/technotes/tn2002/tn2074.html), clarifies the differences and similarities between HIView and Control Manager functions.
- _[Carbon Event Manager Programming Guide](../Carbon%20Event%20Manager%20Programming%20Guide/Introduction%20to%20Carbon%20Event%20Manager%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobz)_ provides an overview of the Carbon Event Manager and event handling in general for Carbon applications.
- If you have not yet upgraded your application to Carbon and Mac OS X, the _[Carbon Porting Guide](../Carbon%20Porting%20Guide/Introduction%20to%20Carbon%20Porting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojr)_ guides you through the steps required. It also contains information about how to move to the Carbon Event Manager from the classic `WaitNextEvent` model.
[Next](The%20Modern%20Advantage.md)

