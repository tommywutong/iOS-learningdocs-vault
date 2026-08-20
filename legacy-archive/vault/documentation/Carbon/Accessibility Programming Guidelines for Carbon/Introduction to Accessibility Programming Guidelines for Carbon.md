---
title: Accessibility Programming Guidelines for Carbon
apple_id: TP30001127
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-02-08'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MakingAppsAccessible/AXCarbonIntro/AXCarbonIntro.html
archived_at: '2026-07-15T05:23:22.422231Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Accessibility%20and%20the%20Carbon%20Framework.md)

# Introduction to Accessibility Programming Guidelines for Carbon

All Carbon applications can and should be accessible to users with disabilities. The process of making an application accessible is called access enabling. How big a job this is depends on the extent to which your application uses custom user interface objects.

If your Carbon application relies on HIObjects for all its user interface elements (including subclasses of HIView), most of the accessibility infrastructure is provided for you. If, on the other hand, your Carbon application uses some custom subclasses of HIObject or HIView or relies on a custom application framework, you need to supply more of the accessibility infrastructure yourself.

This document outlines how to access-enable applications throughout this range. It provides steps you can follow to access-enable an application that uses only HIObjects and HIViews in its user interface. It then provides guidelines to help you access-enable an application that implements custom views or depends on a custom application framework.

All Carbon application developers should read this document to learn how to make their applications accessible to users with disabilities. If you’re new to accessibility you should read _[Accessibility Programming Guide for OS X](https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/index.html#//apple_ref/doc/uid/TP40001078)_ to get an overview of the Mac OS X accessibility architecture.

If you’re an assistive application developer, you don’t need to read this document. Instead, you should read _[Accessibility Programming Guide for OS X](https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/index.html#//apple_ref/doc/uid/TP40001078)_ to become familiar with the Mac OS X accessibility architecture and then you should read _Accessibility Reference for Assistive Applications_.

This document has the following chapters:

- [Accessibility and the Carbon Framework](Accessibility%20and%20the%20Carbon%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqg4wueqkci5fegr2h) describes how Carbon implements accessibility and provides support for access-enabling Carbon applications.
- [Making a Standard Carbon Application Accessible](Making%20a%20Standard%20Carbon%20Application%20Accessible.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqgywviucykjcummjqge) describes the steps you follow to access-enable a Carbon application that uses only standard HIObjects.
- [Making a Semistandard Carbon Application Accessible](Making%20a%20Semistandard%20Carbon%20Application%20Accessible.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrrgawviucykjcummjqge) describes additional steps you follow to access-enable a Carbon application that implements some custom subviews.
- [Making a Custom Carbon Application Accessible](Making%20a%20Custom%20Carbon%20Application%20Accessible.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrrgewviucykjcummjqge) provides guidelines to help you access-enable a Carbon application that implements a custom view subsystem or implements its interface procedurally.
- [Revision History](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqgqwugskiinauqrkc) describes changes to this document.

The Accessibility Reference Library contains several documents that cover accessibility:

- _Getting Started With Accessibility_ provides a brief introduction to accessibility and describes learning paths you might choose to follow.
- _[Accessibility Programming Guide for OS X](https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/index.html#//apple_ref/doc/uid/TP40001078)_ describes the Mac OS X accessibility architecture.
- _[Accessibility Programming Guidelines for Mac](../../Cocoa/Accessibility%20Programming%20Guidelines%20for%20Mac/Introduction%20to%20Accessibility%20Programming%20Guidelines%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeytq2i)_ describes how to access-enable a Cocoa application.
- _Accessibility Reference for Assistive Applications_
- _[Carbon Accessibility Reference](https://developer.apple.com/documentation/applicationservices/carbon_accessibility)_ describes the functions, data types, and constants used in accessible Carbon applications.
- NSAccessibility describes the NSAccessibility protocol and its methods and constants.

In addition to these documents, Apple maintains a website devoted to accessibility in Mac OS X, with links to more information about compatible assistive technologies:

- [http://www.apple.com/accessibility](http://www.apple.com/accessibility)
[Next](Accessibility%20and%20the%20Carbon%20Framework.md)

