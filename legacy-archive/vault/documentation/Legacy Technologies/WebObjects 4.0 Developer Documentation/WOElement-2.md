---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/WOElement.html
archived_at: '2026-07-18T01:28:54.049951Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](WODynamicElement-2.md)
[!](WOMailDelivery-2.md)

---

# WOElement

__Inherits From:__
NSObject

__Declared in:__
WebObjects/WOElement.h

---

## Class Description

The WOElement class is the abstract superclass of all objects that represent static and dynamic UI elements on a World Wide Web page (currently, HTML and PDF elements). You cannot directly instantiate objects from WOElement; you must create a concrete subclass of WOElement and generate objects from it.

__Note:__
For custom dynamic elements, you need to create a subclass of [WODynamicElement](WODynamicElement-2.md).

WOElement declares the three methods corresponding to the phases of the request-response loop (invoked in the following order), but WOElement's implementations do nothing:

- [__takeValuesFromRequest:inContext:__](#apple-g44a)
- [__invokeActionForRequest:inContext:__](#apple-g42a)
- [__appendToResponse:inContext:__](#apple-gi2tooa)

The first argument of these messages is an object that represents the HTTP request or response ([WORequest](WORequest-2.md) or [WOResponse](WOResponse-2.md)). The second argument is a [WOContext](WOContext-2.md) object that represents the context of the transaction.

Concrete subclasses of WOElement (or WODynamicElement) must, at minimum, implement [__appendToResponse:inContext:__](#apple-gi2tooa). Subclasses of WODynamicElement must implement one or both of the remaining methods.

---

## Method Types

**Handling requests**

**[- __appendToResponse:inContext:__](#apple-gi2tooa)

**[- __invokeActionForRequest:inContext:__](#apple-g42a)

**[- __takeValuesFromRequest:inContext:__](#apple-g44a)******

---

## Instance Methods

---

### appendToResponse:inContext:

- (void)__appendToResponse:__ (WOResponse \*)_aResponse_ __inContext:__ (WOContext \*)_aContext_

This method is invoked in WOElement objects in the request-handling phase when objects involved in the current transaction append their HTML content to the transaction's WOResponse object. If the WOElement has child WOElements, it should forward the message to them. WOElement's default implementation of this method does nothing.

__See also:__
[WOResponse](WOResponse-2.md) class for methods used to append HTML content

---

### invokeActionForRequest:inContext:

- (WOElement \*)__invokeActionForRequest:__ (WORequest \*)_aRequest_ __inContext:__ (WOContext \*)_aContext_

This method is invoked in WOElements in the phase of request handling that results in the triggering of an action method and the return of a response WOComponent. In this phase, the message is propagated through the objects of the application until the dynamic element for the activated HTML control (for instance, a custom button) responds to the message by invoking the method in the request component that is bound to the action. To see if it has been activated, the dynamic element should check its element ID (obtained from its WOContext) against the sender ID in the request and context. To invoke the action method, the dynamic element should return the value of the action. The default WOElement implementation of this method returns nil

__See also:__
[WOContext](WOContext-2.md) class for a description of element IDs

---

### takeValuesFromRequest:inContext:

- (void)__takeValuesFromRequest:__ (WORequest \*)_aRequest_ __inContext:__ (WOContext \*)_aContext_

This method is invoked in (dynamic) WOElement objects during the phase of request handling that extracts user-entered data. Each dynamic element acquires any entered data (such as HTML form data) or changed state (such as a check in a check box) associated with an attribute and assigns the value to the WOComponent variable bound to the attribute. In this way, even back-end business objects are updated. The default WOElement implementation of this method does nothing.

__See also:__
[WORequest](WORequest-2.md) class for methods used to extract form data

****

---

[!](WODynamicElement-2.md)
[!](WOMailDelivery-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
