---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/WOElement.html
archived_at: '2026-07-15T08:11:47.576507Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WOElement

> __Inherits
> from:__  NSObject

> __Declared in:__  WebObjects/WOElement.h

---

## Class Description

---

The WOElement class is the abstract superclass of all objects
that represent static and dynamic UI elements on a World Wide Web
page (currently, HTML and PDF elements). You cannot directly instantiate
objects from WOElement; you must create a concrete subclass of WOElement
and generate objects from it.

|  |
| --- |
| For custom dynamic elements, you need to create a subclass of [WODynamicElement](WODynamicElement-2.md#apple-k5hui6lomfwwsy2fnrsw2zlooq). |

WOElement declares the three methods corresponding to the
phases of the request-response loop (invoked in the following order),
but WOElement's implementations do nothing:

- [takeValuesFromRequest:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2fnrsw2zlooqxxiyllmvlgc3dvmvzum4tpnvjgk4lvmvzxiotjnzbw63tumv4hioq)
- [invokeActionForRequest:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2fnrsw2zlooqxws3twn5vwkqldoruw63sgn5zfezlrovsxg5b2nfxeg33oorsxq5b2)
- [appendToResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2fnrsw2zlooqxwc4dqmvxgivdpkjsxg4dpnzzwkotjnzbw63tumv4hioq)

The first argument of these messages is an object that represents
the HTTP request or response ( [WORequest](WORequest-2.md#apple-k5hvezlrovsxg5a) or [WOResponse](WOResponse-2.md#apple-k5hvezltobxw443f)). The second argument is
a [WOContext](WOContext-2.md#apple-k5hug33oorsxq5a) object that represents the
context of the transaction.

Concrete subclasses of WOElement (or WODynamicElement) must,
at minimum, implement [appendToResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2fnrsw2zlooqxwc4dqmvxgivdpkjsxg4dpnzzwkotjnzbw63tumv4hioq).
Subclasses of WODynamicElement must implement one or both of the remaining
methods.

## Instance Methods

---

### appendToResponse:inContext:

`- (void)appendToResponse:(WOResponse
*)aResponse
inContext:(WOContext *)aContext`

This method is invoked in WOElement objects
in the request-handling phase when objects involved in the current
transaction append their HTML content to the transaction's WOResponse
object. If the WOElement has child WOElements, it should forward
the message to them. WOElement's default implementation of this
method does nothing.

__See Also:__  [WOResponse](WOResponse-2.md#apple-k5hvezltobxw443f) class

---

### invokeActionForRequest:inContext:

`- (WOElement *)invokeActionForRequest:(WORequest
*)aRequest
inContext:(WOContext *)aContext`

This method is invoked in WOElements in the
phase of request handling that results in the triggering of an action
method and the return of a response WOComponent. In this phase,
the message is propagated through the objects of the application
until the dynamic element for the activated HTML control (for instance,
a custom button) responds to the message by invoking the method
in the request component that is bound to the action. To see if
it has been activated, the dynamic element should check its element
ID (obtained from its WOContext) against the sender ID in the request
and context. To invoke the action method, the dynamic element should
return the value of the action. The default WOElement implementation
of this method returns nil.

__See Also:__  [WOContext](WOContext-2.md#apple-k5hug33oorsxq5a) class for a description
of element IDs

---

### takeValuesFromRequest:inContext:

`- (void)takeValuesFromRequest:(WORequest
*)aRequest
inContext:(WOContext *)aContext`

This method is invoked in (dynamic) WOElement
objects during the phase of request handling that extracts user-entered
data. Each dynamic element acquires any entered data (such as HTML
form data) or changed state (such as a check in a check box) associated
with an attribute and assigns the value to the WOComponent variable
bound to the attribute. In this way, even back-end business objects
are updated. The default WOElement implementation of this method
does nothing.

__See Also:__  [WORequest](WORequest-2.md#apple-k5hvezlrovsxg5a) class for methods used to
extract form data

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
