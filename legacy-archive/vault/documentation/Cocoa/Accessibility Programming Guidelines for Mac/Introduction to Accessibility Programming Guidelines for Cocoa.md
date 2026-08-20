---
title: Accessibility Programming Guidelines for Mac
apple_id: 10000118i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Accessibility/cocoaAXIntro/cocoaAXintro.html
archived_at: '2026-07-15T05:25:25.759548Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Accessibility%20Objects%20and%20the%20Accessibility%20Hierarchy.md)

# Introduction to Accessibility Programming Guidelines for Cocoa

All Cocoa applications can and should be accessible to users with disabilities. The process of making an application accessible is called access enabling. In Cocoa applications, accessibility is achieved by user interface classes adopting the NSAccessibility informal protocol. Because standard Cocoa controls and views automatically adopt the NSAccessibility protocol, there is very little you have to do to access enable your application if you rely only on standard control and view objects.

If your application implements custom controls or views, however, you need to provide additional accessibility information to make your application completely accessible.

This topic discusses how Cocoa implements accessibility and describes specific tasks you need to perform to access enable your application.

All Cocoa application developers should read this document to learn how to access enable their applications. Even if your application uses only standard Cocoa views and controls, there is some information you need to supply to ensure your application is both completely accessible and provides a good user experience. If you’re new to accessibility or if you’re unsure why your application should be accessible, you should read _[Accessibility Programming Guide for OS X](https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/index.html#//apple_ref/doc/uid/TP40001078)_ to learn how applications make themselves accessible to assistive technologies in OS X.

If you’re an assistive application developer, you don’t need to read this document. Instead, you should read _[Accessibility Programming Guide for OS X](https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/index.html#//apple_ref/doc/uid/TP40001078)_ to become familiar with the OS X accessibility architecture and learn about the attributes associated with each type of accessibility object.

The following articles describe how Cocoa implements accessibility:

- [Accessibility Objects and the Accessibility Hierarchy](Accessibility%20Objects%20and%20the%20Accessibility%20Hierarchy.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga2tolkciffeeq2kjbfa) describes the accessibility object as it is implemented by the Application Kit. It also describes the accessibility hierarchy that represents an application and discusses how an assistive application interacts with the accessibility objects in your application.
- [Hit-Testing and Keyboard Focus](Hit-Testing%20and%20Keyboard%20Focus.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga3dalkcineumssii5fa) discusses how an assistive application can access user interface objects by screen position and by keyboard focus.
- [Accessibility Notifications](Accessibility%20Notifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga3dclkdjjbeercfifca) discusses how an application notifies assistive applications that some change has occurred in the user interface, such as a new window opening.

The following articles describe how to access enable your application:

- [Access Enabling a Cocoa Application](Access%20Enabling%20a%20Cocoa%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga2tslkciffeuskcizaq) provides guidance on which tasks you may need to perform to access enable your application.
- [Supporting Attributes](Supporting%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga3delkcineueskeivda) describes how to add an attribute to a custom accessible object.
- [Supporting Actions](Supporting%20Actions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga3dglkcijbusrkiivaq) describes how to add an action to a custom accessible object.
- [Manipulating the Accessibility Hierarchy](Manipulating%20the%20Accessibility%20Hierarchy.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga3dilkcineuosscinda) describes how to change an accessibility object’s status in the accessibility hierarchy.

The Accessibility Reference Library contains several documents that cover accessibility.

- _Getting Started with Accessibility_ provides a brief introduction to accessibility and describes learning paths you might choose to follow.
- _[Accessibility Programming Guide for OS X](https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/index.html#//apple_ref/doc/uid/TP40001078)_ describes the OS X accessibility architecture.
- NSAccessibility describes the NSAccessibility protocol and its methods and constants.
- _[Accessibility Programming Guidelines for Carbon](../../Carbon/Accessibility%20Programming%20Guidelines%20for%20Carbon/Introduction%20to%20Accessibility%20Programming%20Guidelines%20for%20Carbon.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrx)_ describes how to access-enable a Carbon application.
- _[Carbon Accessibility Reference](https://developer.apple.com/documentation/applicationservices/carbon_accessibility)_ describes the functions, data types, and constants used in accessible Carbon applications.

In addition to these documents, Apple maintains a website devoted to accessibility in OS X, with links to more information about compatible assistive technologies:

- [http://www.apple.com/accessibility](http://www.apple.com/accessibility)
[Next](Accessibility%20Objects%20and%20the%20Accessibility%20Hierarchy.md)

