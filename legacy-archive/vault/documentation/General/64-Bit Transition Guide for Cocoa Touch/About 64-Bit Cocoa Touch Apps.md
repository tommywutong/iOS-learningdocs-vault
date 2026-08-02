---
title: 64-Bit Transition Guide for Cocoa Touch
apple_id: TP40013501
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaTouch64BitGuide/Introduction/Introduction.html
archived_at: '2026-07-27T06:57:08.767670Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Major%2064-Bit%20Changes.md)

# About 64-Bit Cocoa Touch Apps

When desktop operating systems transitioned from 32-bit to 64-bit addressing, 64-bit apps were critical to the OS transition. Now, iOS is getting a similar desktop-class architecture. Starting with iOS 7 and the A7 processor, you can build iOS apps that take advantage of 64-bit processors. An app that supports 64-bit processing almost always gains improved performance when compared with a 32-bit app running on the same device.

## At a Glance

The Apple A7 processor supports two distinct instruction sets. The first is the 32-bit ARM instruction set supported by Apple’s previous processors. The second is a brand-new 64-bit ARM architecture. The 64-bit architecture includes support for a vastly larger address space, but that is not the only (or most important) architectural improvement it provides. The 64-bit architecture supports a new and streamlined instruction set that supports twice as many integer and floating-point registers. Apple’s LLVM compiler has been optimized to take full advantage of this new architecture. As a result, 64-bit apps can work with more data at once for improved performance. Apps that extensively use 64-bit integer math or custom NEON operations see even larger performance gains. So, even though 32-bit apps already run faster on the A7 processor than they did on earlier processors, converting apps to 64-bit almost always provides better performance.

When a 64-bit app is running in iOS, pointers are 64 bits. Some integer types, once 32 bits, are also now 64 bits. Many data types in system frameworks, especially UIKit and Foundation, have also changed. These changes mean that a 64-bit app uses more memory than a 32-bit app. If not managed carefully, the increased memory consumption can be detrimental to an app’s performance.

When iOS is executing on a 64-bit device, iOS includes separate 32-bit and 64-bit versions of the system frameworks. When all apps running on the device are compiled for the 64-bit runtime, iOS never loads the 32-bit versions of those libraries. As a result, the system uses less memory and launches apps more quickly. Because all of the built-in apps already support the 64-bit runtime, it’s to everyone’s benefit that all apps running on 64-bit devices be compiled for the 64-bit runtime, especially apps that support background processing. Even apps that are not performance sensitive gain from this memory efficiency.

Here’s how you convert an app to 64-bit.

### Convert Your App to a 64-Bit Binary

The default behavior for Xcode is to build your app with both 32-bit and 64-bit binaries included. This combined binary requires a minimum deployment target of iOS 5.1.1 or later. The 64-bit binary runs only on 64-bit devices running iOS 7.0.3 and later. If you have an existing app, you should first update your app to iOS 7 or later and then port it to run on 64-bit processors. By updating it first, you can remove deprecated code paths and use modern practices. If you’re creating a new app, target iOS 7 or later and compile 32-bit and 64-bit versions of your app.

The architecture for 64-bit apps on iOS is almost identical to the architecture for OS X apps, making it easy to create a common code base that runs in both operating systems. Converting a Cocoa Touch app to 64-bit follows a similar transition process as the one for Cocoa apps on OS X. Pointers and some common C types change from 32 bits to 64 bits. Code that relies on the [NSInteger](https://developer.apple.com/documentation/objectivec/nsinteger) and [CGFloat](https://developer.apple.com/documentation/coregraphics/cgfloat) types needs to be carefully examined.

Start by building the app for the 64-bit runtime, fixing any warnings that occur as well as searching your code for specific 64-bit issues. For example:

- Make sure all function calls have a proper prototype.
- Avoid truncating 64-bit values by accidentally assigning them to a 32-bit data type.
- Ensure that calculations are performed correctly in the 64-bit version of your app.
- Create data structures whose layouts are identical in the 32-bit and 64-bit versions of your app (such as when you write a data file to iCloud).

__Chapter:__ [Major 64-Bit Changes](Major%2064-Bit%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkmbrfvbuqmrnknltc), [Optimizing Memory Performance](Optimizing%20Memory%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkmbrfvbuqnbnknltc)

### Test Your App on a 64-Bit Device

iOS Simulator can be used to simulate either 32-bit or 64-bit devices. After converting your app to the 64-bit runtime, you can use Simulator to test your app. In particular, Simulator is great for testing code that uses custom data structures to ensure that your data can be read and written in both architectures. However, before you distribute your app, you must test it on actual hardware. Some of the runtime changes can be detected only when the app is running on a device.

After your app has been successfully converted, use Instruments to profile its performance and memory usage.

__Chapters:__ [Converting Your App to a 64-Bit Binary](Converting%20Your%20App%20to%20a%2064-Bit%20Binary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkmbrfvbuqmznknltc), [Optimizing Memory Performance](Optimizing%20Memory%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkmbrfvbuqnbnknltc)

## How to Use This Document

Read [Major 64-Bit Changes](Major%2064-Bit%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkmbrfvbuqmrnknltc) to understand the changes in the 64-bit runtime, and then read [Converting Your App to a 64-Bit Binary](Converting%20Your%20App%20to%20a%2064-Bit%20Binary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkmbrfvbuqmznknltc) for concrete details on how to update your app. To ensure that your app’s memory footprint remains modest, read [Optimizing Memory Performance](Optimizing%20Memory%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkmbrfvbuqnbnknltc).

## Prerequisites

You need to have some familiarity with creating apps to understand the information in this guide. For more information, see _[Start Developing iOS Apps (Swift)](../../../referencelibrary/Getting%20Started/Start%20Developing%20iOS%20Apps%20%28Swift%29/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temju)_.

In some cases, a detailed understanding of ANSI C programming is necessary to make the most of the information in this guide.

## See Also

The details of both the 32-bit and the 64-bit application binary interfaces can be found in _[iOS ABI Function Call Guide](../../Xcode/iOS%20ABI%20Function%20Call%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tamrt)_.

[Next](Major%2064-Bit%20Changes.md)
