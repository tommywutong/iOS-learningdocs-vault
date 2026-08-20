---
title: Getting Started with Games
apple_id: TP30001091
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Games/_index.html
archived_at: '2026-07-18T02:39:22.162227Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)



## Introduction

### Learning About Apple Development Tools

Mac OS X provides a suite of developer tools, including design tools, analysis tools, packaging tools, compilers, and debuggers. For an overview of these available tools, along with examples of how to use them, read [Mac Technology Overview](../../documentation/Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx).

- __If you want to find out what the development cycle is like and how the tools work together,__ read [A Tour of Xcode](../../documentation/Developer%20Tools/A%20Tour%20of%20Xcode/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqojq). Xcode is Apple’s integrated development environment (IDE) and the application you can use for managing, building, and debugging projects.
- __If you want to know more about constructing user interfaces,__ read [Interface Builder](../../documentation/Developer%20Tools/Interface%20Builder/Introduction%20to%20Interface%20Builder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3ts2i). The online help for the Interface Builder application also contains helpful information.

### Adopting Mac OS X Media Technologies

Mac OS X offers games developers state-of-the-art audio, 2D and 3D graphics, networking capabilities, and human interface features. In the course of development, you may encounter these technologies and want to know more information about them.

- __If you want to use Apple’s implementation of OpenGL in your application,__ read [OpenGL Programming Guide for Mac](../../documentation/Graphics%20Imaging/OpenGL%20Programming%20Guide%20for%20Mac/About%20OpenGL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobx).
- __If you need to work with graphics and imaging in your application,__ read [Getting Started with Graphics & Animation](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_GraphicsImaging/_index.html#//apple_ref/doc/uid/TP30001000). Specifically, you may want to read Quartz 2D Reference Collection to understand the C API for native drawing in Mac OS X.
- __If you want to take advantage of audio in your application,__ read [Getting Started with Audio & Video](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_MusicAudio/_index.html#//apple_ref/doc/uid/TP30001095) to learn about Apple’s Core Audio architecture.

### Porting Your Existing Games

If you have existing code written for Windows, Carbon, UNIX, or another platform, you can often integrate much of that code base into your application. Mac OS X provides a number of cross-platform APIs such as OpenGL that may be of particular interest if you develop games or other highly graphic-intensive applications.

- __If you want to learn the basics about porting your code to Mac OS X,__ read Getting Started With Porting.
- __If you specifically want to port your Windows application to Mac OS X,__ read [Porting to Mac OS X from Windows Win32 API](../../documentation/Porting/Porting%20to%20Mac%20OS%20X%20from%20Windows%20Win32%20API/Porting%20to%20Mac%20OS%20X%20from%20Windows%20Win32%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4ta2i).
- __If you’re a UNIX developer,__ read [Porting UNIX/Linux Applications to OS X](../../documentation/Porting/Porting%20UNIX-Linux%20Applications%20to%20OS%20X/Introduction%20to%20Porting%20UNIX-Linux%20Applications%20to%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambt) to learn how to build UNIX applications on Mac OS X.

### Supporting Game Devices

Device control is fundamental to all games. In MacOSX, the Human Interface Device (HID) Manager supports access to HID-class devices, such as joysticks and non-Apple displays. For access to devices that provide tactile sensation to the user, the Force Feedback framework defines a programming interface that is functionally similar to Microsoft’s DirectInput API.

- __If you want to use a specific Mac OS X framework to control devices that are attached to the system,__ read [Force Feedback Device Access Reference](https://developer.apple.com/documentation/forcefeedback) to learn about Apple’s implementation of force feedback.
- __If you want to know more about how to develop applications that communicate with or control HID class devices,__ read [HID Class Device Interface Guide](../../documentation/Device%20Drivers/HID%20Class%20Device%20Interface%20Guide/Introduction%20to%20Working%20With%20HID%20Class%20Device%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzq).

### Adding Network Support to Your Games

Networking support for games is a universally hot topic of discussion among developers. Apple provides a wide range of networking capabilities that you can take advantage of in your code, including support for major protocols and services.

- __If you need to get up to speed with the networking services provided by Apple,__ read Getting Started with Networking to learn about the dominant media types, protocols, and services that are supported on the platform, as well as the rich set of networking APIs available to your application.
- __If you need to learn about Apple’s zero-configuration networking architecture,__ read [Bonjour Overview](../../documentation/Cocoa/Bonjour%20Overview/About%20Bonjour.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyts2i).
- __If you need to work with low-level networking functions and BSD sockets,__ read [CFNetwork Programming Guide](../../documentation/Networking/CFNetwork%20Programming%20Guide/Introduction%20to%20CFNetwork%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzs).

### Building High-Performance Games

In many cases, performance optimization of code can be the key to success in games. How efficiently your software uses resources such as the CPU, memory, and hard drive is the way that performance can be measured. Apple provides a number of tools for measuring software efficiency.

- __If you need to learn about ways to improve the performance of both hardware and software,__ read [Performance Starting Point for OS X](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Performance/index.html#//apple_ref/doc/uid/TP30001082).
- __If you need to understand the fundamentals of performance and the tools that are used to measure it,__ read [Performance Overview](../../documentation/Performance/Performance%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimjq).
- __If you want to take advantage of Apple’s Velocity Engine,__ read the material cited in the [Performance Velocity Engine Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000430-TP30000587), which explains how you can tune your software to get tremendous speed and performance advantages in your games using this new Apple technology.

### Next Steps

The [Games Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000467) includes the following high-level resource pages, which can be bookmarked for easy access:

- [Guides](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000440-TP30000467)

  Conceptual and how-to information for games development.
- [Reference](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000467)

  Focused, detailed descriptions in reference format for APIs related to games development.
- [Release Notes](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000872-TP30000467)

  Late-breaking news and highlights of new or changed features in the latest release.
- [Sample Code](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP30000467)

  Sample applications that are useful for games development on the Macintosh platform.
- [Technical Notes](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000924-TP30000467)

  Late-breaking documents on issues related to games.
- [Technical Q&As](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000926-TP30000467)

  Programming tips, code snippets, and FAQs by Apple’s support engineers.
- Mailing Lists

  You can use the games mailing list ([mac-games-dev](http://lists.apple.com/mailman/listinfo/mac-games-dev)) to discuss any issues you encounter writing code.

