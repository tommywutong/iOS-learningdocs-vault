---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOExtensionsTOC.html
archived_at: '2026-07-15T07:55:24.406522Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Top](../Reference.md)

# WebObjects Extension Specifications

---

The WebObjects Extensions framework defines dynamic elements and components that you can use in any application that links to the framework. By default, when you create a WebObjectsApplication or WebObjectsFramework project in Project Builder, you are linked to the WOExtensions framework. In addition, WODefaultApp is already linked to the WOExtensions framework. Thus, you can use the elements and components defined in this framework in virtually all of your applications.
Here are the dynamic elements defined in the WOExtensions Framework:

> > [WOCheckBoxList](WOCheckBoxList.md#apple-gezti)
> > [WONestedList](WONestedList.md#apple-geztq)
> > [WORadioButtonList](WORadioButtonList.md#apple-ge2da)

In addition to dynamic elements, the WebObjects Extensions framework defines shared components. WebObjects has the ability to share components across applications. All you have to do is define a component, place it in a framework, place the framework in _NeXT_ROOT___/NextLibrary/Frameworks__ and you can use that component in any WebObjects application as long as it links to that framework.
Some shared components define attributes, similar to the way dynamic elements define attributes. To use such components, you must bind their attributes to values and methods from your component's script or code file.
Here are the shared components defined in the WOExtensions Framework:
> > [WORedirect](WORedirect.md#apple-gizti)
> > [WOSimpleArrayDisplay](WOSimpleArrayDisplay.md#apple-gizdi)
> > [WOSortOrder](WOSortOrder.md#apple-gizdk)
> > [WOStats](WOStats.md#apple-gi3tc)
> > [WOToManyRelationship](WOToManyRelationship.md#apple-gmyde)
> > [WOToOneRelationship](WOToOneRelationship.md#apple-gmyts)

See the [_WebObjects Developer's Guide_](../../DevGuide/DevGuideTOC.md) for a more complete introduction to shared components. See the [_Dynamic Elements Reference_](DynamicElementsTOC.md) to learn how to use the specifications in this guide.

[!First Section](WOCheckBoxList.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
