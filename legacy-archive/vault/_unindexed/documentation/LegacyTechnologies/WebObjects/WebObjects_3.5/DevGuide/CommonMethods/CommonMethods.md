---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/CommonMethods/CommonMethods.html
archived_at: '2026-07-15T07:51:14.536325Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Top](../DevGuideTOC.md)

# Common Methods

---

The methods that you write for your WebObjects application provide the behavior that makes your application unique. Because you are writing subclasses of WOApplication, WOSession, and WOComponent (in Java, WebApplication, WebSession, and Component), you inherit the methods provided by those classes. These inherited methods take care of the details of receiving HTTP requests and generating responses. However, you'll sometimes find that you need to override some of the inherited methods to perform certain tasks.
This chapter describes the types of methods that you generally write in a WebObjects application. These types are:

- Action methods
- Initialization and deallocation methods
- Request-handling methods

In cases where you override existing methods, those methods are invoked at standard, predictable times during the application's request-response loop (the main loop for a WebObjects application). For background on the request-response loop, see the chapter ["WebObjects Viewed Through Its Classes"](../HowWOWorks/HowWOWorks.md).

As you're writing methods, refer to the class specifications for WOApplication, WOSession, and WOComponent to learn which messages you can send to these objects. The class specifications are in the online book [_WebObjects Class Referenc_](../../Reference/Reference.md)e.

[****
: __Action Methods__](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/CommonMethods/ActionsMethods.html#6452)

[****
: __Initialization and Deallocation Methods__](InitializationMethods.md#apple-gq2ds)

[****
: The Structures of init and awake](StructureOfInitAwake.md#apple-ge3dm)[****
: Application Initialization](ApplicationInit.md#apple-gu2tg)[****
: Session Initialization](SessionInit.md#apple-gizti)[****
: Component Initialization](ComponentInit.md#apple-gqzto)

[****
: __Request-Handling Methods__](RequestHandlingMethods.md#apple-gyztmoi)

[****
: Taking Input Values From a Request](takeValuesFromRequest.md#apple-gi4tk)[****
: Invoking an Action](invokeActionForRequest.md#apple-gi4to)

[****
: Limitations on Direct Requests](invokeActionForRequest.md#apple-gmyte)

[****
: Generating a Response](appenToResponse.md#apple-gi4tm)

[!First Section](ActionMethods.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
