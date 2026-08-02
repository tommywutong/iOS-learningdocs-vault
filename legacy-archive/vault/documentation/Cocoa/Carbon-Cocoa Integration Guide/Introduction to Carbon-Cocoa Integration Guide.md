---
title: Carbon-Cocoa Integration Guide
apple_id: TP30000893
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CarbonCocoaDoc/CarbonCocoaDoc.html
archived_at: '2026-07-15T07:11:57.998228Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Carbon%20and%20Cocoa%20User%20Interface%20Communication.md)

# Introduction to Carbon-Cocoa Integration Guide

No matter which development environment you choose for developing applications—Cocoa or Carbon—you may find that the other development environment offers functionality you’d like to use in your application. Choosing the Cocoa or Carbon development environment to create new applications doesn’t restrict you to using the API defined for that environment. You can use the Carbon API from a Cocoa application or the Cocoa API from a Carbon application. This document shows you how.

There are a number of reasons you might want to integrate Cocoa and Carbon in an application, including the following:

- You want to use existing code while getting the benefits of technologies offered by another framework.
- You’re developing a common service that you want to make available to both Carbon and Cocoa.
- It’s easier for you to do some tasks in Cocoa than in Carbon, or vice versa.
- You’ve already created a terrific user interface in one environment and you want to access it from the other environment.
- Your programming team consists of engineers with different skill sets—Cocoa and Carbon.

This document assumes you are programming for Cocoa in Objective-C and does not discuss Java integration issues. To get the full benefit of this document, you should have experience programming in either the Cocoa or Carbon environment and you should also have some basic knowledge of the other environment. The [See Also](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4tgljxhe4tsmbr) section contains a list of documents to help you gain this knowledge.

You should be familiar with a few fundamental concepts before you begin to integrate Cocoa and Carbon in the same application. These concepts are covered in the following articles:

- [Carbon and Cocoa User Interface Communication](Carbon%20and%20Cocoa%20User%20Interface%20Communication.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm4tslkukayq) discusses how Mac OS X communicates user events between Carbon and Cocoa application environments.
- [Preprocessing Mixed-Language Code](Preprocessing%20Mixed-Language%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgqydalkukayq) lists filename extensions you can use when you mix programming languages in a project.
- [Interchangeable Data Types](Interchangeable%20Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgqydclkukayq) provides information on Foundation (Cocoa) and Core Foundation (Carbon) data types you can use interchangeably.
- [Using Carbon and Cocoa in the Same Application](Using%20Carbon%20and%20Cocoa%20in%20the%20Same%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm4tqlkukayq) provides a brief overview of how to combine Carbon and Cocoa code in an application. Includes a discussion of C-callable wrapper functions.

The concepts discussed in the preceding articles are put into practice in the sample code provided in these articles:

- [Using Cocoa Functionality in a Carbon Application](Using%20Cocoa%20Functionality%20in%20a%20Carbon%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgqydelkukayq) describes how to use Cocoa functionality unrelated to the user interface in a Carbon application.
- [Using Carbon Functionality in a Cocoa Application](Using%20Carbon%20Functionality%20in%20a%20Cocoa%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgqydglkukayq) describes how to use Carbon functionality unrelated to the user interface in a Cocoa application.
- [Using a Cocoa User Interface in a Carbon Application](Using%20a%20Cocoa%20User%20Interface%20in%20a%20Carbon%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgqydilkukayq) describes tasks you must perform to enable a Cocoa user interface to work properly in Carbon.
- [Using a Carbon User Interface in a Cocoa Application](Using%20a%20Carbon%20User%20Interface%20in%20a%20Cocoa%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgqydklkukayq) describes tasks you must perform to enable a Carbon user interface to work properly in Cocoa.
- [HICocoaView: Using Cocoa Views in Carbon Windows](HICocoaView-%20Using%20Cocoa%20Views%20in%20Carbon%20Windows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2domrufvjvomi) describes how HICocoaView, introduced in Mac OS X v10.5, makes it possible to use Cocoa views in a Carbon window.
- [Using Cocoa in a Navigation Services Dialog](Using%20Cocoa%20in%20a%20Navigation%20Services%20Dialog.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsnbufvjvomi) describes how Carbon applications using Navigation Services in Mac OS X v10.5 can directly access features in the Cocoa classes `NSOpenPanel` and `NSSavePanel`.

For additional information on developing for Mac OS X, especially in Cocoa and Carbon, see the following documents:

- _Getting Started with Cocoa_ and _[Getting Started with Carbon](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Carbon/_index.html#//apple_ref/doc/uid/TP30001086)_ provide a guided introduction and learning path for developers new to Cocoa and Carbon, respectively.
- _[Tools & Languages Starting Point](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Tools/index.html#//apple_ref/doc/uid/TP30001102)_ provides a guided introduction and learning path for developers new to Apple’s integrated development environment (IDE).
- _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_ provides an orientation to the technologies available in Mac OS X, with links to relevant documentation. Appendix A, “Mac OS X Frameworks,” lists the frameworks available to Mac OS X developers.
- _[Advanced Memory Management Programming Guide](../Advanced%20Memory%20Management%20Programming%20Guide/About%20Memory%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytc2i)_ addresses the object-ownership policy and related techniques for creating, copying, retaining, and disposing of objects.
[Next](Carbon%20and%20Cocoa%20User%20Interface%20Communication.md)

