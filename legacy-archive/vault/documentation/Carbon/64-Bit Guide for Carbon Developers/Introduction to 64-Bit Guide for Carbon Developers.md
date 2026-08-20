---
title: 64-Bit Guide for Carbon Developers
apple_id: TP40004381
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Carbon64BitGuide/Introduction/Introduction.html
archived_at: '2026-07-15T05:22:31.463771Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](The%20Transition%20to%2064-Bit%20Addressing.md)

# Introduction to 64-Bit Guide for Carbon Developers

One of Apple’s goals for OS X version 10.5 (Leopard) is to make it possible for applications to use 64-bit addressing. System libraries and frameworks are now 64-bit ready, meaning they can be used in both 32-bit and 64-bit applications. With this support, you can create applications that address extremely large data sets. On Intel-based Macintosh computers, some 64-bit applications may even run faster than their 32-bit equivalents because of the availability of extra processor resources in 64-bit mode.

Most APIs in OS X v10.5 are available to both 32-bit and 64-bit applications, but some APIs commonly used by Carbon applications are not. In particular, the APIs used to implement a Carbon user interface are generally available only to 32-bit applications. If you want to create a 64-bit application for OS X, you need to use Cocoa to implement its user interface.

You may not need to develop 64-bit versions of your applications right now, but you can start to prepare your projects for this transition. As part of this process, you need to adopt standard data types and implement some application features with alternative technologies. This document discusses guidelines, issues, and procedures specific to the transition to 64-bit executables for Carbon developers.

This document is recommended reading for Carbon developers who want to learn what changes are necessary to create 64-bit executable versions of their applications.

This document contains the following chapters:

- [The Transition to 64-Bit Addressing](The%20Transition%20to%2064-Bit%20Addressing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqmrnknltc) describes the 64-bit initiative for OS X and offers general advice and guidelines for moving your projects to 64-bit addressing.
- [Modifying Your Application to Use 64-Bit Addressing](Modifying%20Your%20Application%20to%20Use%2064-Bit%20Addressing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqmznknltc) describes what kinds of modifications are necessary in Carbon applications to make them compile and run as 64-bit executables.
- [Changes in the Human Interface Toolbox](Changes%20in%20the%20Human%20Interface%20Toolbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnbnknltc) describes what’s changed in Carbon user interface APIs.
- [Changes in Other C APIs](Changes%20in%20Other%20C%20APIs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnjnknlti) describes what’s changed in other managers and system services commonly used by Carbon applications, including printing and QuickTime.

This document is a supplement to _[64-Bit Transition Guide](../../Darwin/64-Bit%20Transition%20Guide/Introduction%20to%2064-Bit%20Transition%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanru)_, the definitive guide to 64-bit computing in OS X. If you haven’t already done so, you should read _[64-Bit Transition Guide](../../Darwin/64-Bit%20Transition%20Guide/Introduction%20to%2064-Bit%20Transition%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanru)_ before reading this document.

For Cocoa-specific information, you should read _[64-Bit Transition Guide for Cocoa](../../Cocoa/64-Bit%20Transition%20Guide%20for%20Cocoa/Introduction%20to%2064-Bit%20Transition%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denbx)_.

You may also want to read _Tiger Developer Overview Series: Developing 64-bit Applications_, an ADC featured article that discusses 64-bit computing in OS X v10.4.

[Next](The%20Transition%20to%2064-Bit%20Addressing.md)

