---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Classes/WOElement.html
archived_at: '2026-07-15T08:15:15.593498Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# WOElement

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.appserver

---

## Class Description

---

The WOElement class is the abstract superclass of all objects that represent static and dynamic UI elements on a World Wide Web page (currently, HTML and PDF elements). You cannot directly instantiate objects from WOElement; you must create a concrete subclass of WOElement and generate objects from it.

|  |
| --- |
| __Note:__ For custom dynamic elements, you need to create a subclass of WODynamicElement. |

WOElement declares the three methods corresponding to the phases of the request-response loop (invoked in the following order), but WOElement's implementations do nothing:

- [takeValuesFromRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pivwgk3lfnz2c65dbnnsvmylmovsxgrtsn5wvezlrovsxg5a)
- [invokeActionForRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pivwgk3lfnz2c62loozxwwzkbmn2gs33oizxxeutfof2wk43u)
- [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pivwgk3lfnz2c6ylqobsw4zcun5jgk43qn5xhgzi)

The first argument of these messages is an object that represents the HTTP request or response (WORequest or WOResponse). The second argument is a WOContext object that represents the context of the transaction.

Concrete subclasses of WOElement (or WODynamicElement) must, at minimum, implement [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pivwgk3lfnz2c6ylqobsw4zcun5jgk43qn5xhgzi). Subclasses of WODynamicElement must implement one or both of the remaining methods.

## Constructors

---

### WOElement

`protected WOElement()`

Returns an initialized WOElement.

---

## Instance Methods

---

### appendToResponse

`public void appendToResponse( WOResponse aResponse, WOContext aContext)`

This method is invoked in WOElement objects in the request-handling phase when objects involved in the current transaction append their HTML content to the transaction's WOResponse object. If the WOElement has child WOElements, it should forward the message to them. WOElement's default implementation of this method does nothing.

__See Also:__ WOResponse class

---

### invokeActionForRequest

`public WOActionResults invokeAction( WORequest aRequest, WOContext aContext)`

This method is invoked in WOElements in the phase of request handling that results in the triggering of an action method and the return of a response WOComponent. In this phase, the message is propagated through the objects of the application until the dynamic element for the activated HTML control (for instance, a custom button) responds to the message by invoking the method in the request component that is bound to the action. To see if it has been activated, the dynamic element should check its element ID (obtained from its WOContext) against the sender ID in the request and context. To invoke the action method, the dynamic element should return the value of the action. The default WOElement implementation of this method returns null.

__See Also:__ WOContext class for a description of element IDs

---

### takeValuesFromRequest

`public void takeValuesFromRequest( WORequest aRequest, WOContext aContext)`

This method is invoked in (dynamic) WOElement objects during the phase of request handling that extracts user-entered data. Each dynamic element acquires any entered data (such as HTML form data) or changed state (such as a check in a check box) associated with an attribute and assigns the value to the WOComponent variable bound to the attribute. In this way, even back-end business objects are updated. The default WOElement implementation of this method does nothing.

__See Also:__ WORequest class for methods used to extract form data

---

### toString

`public String toString()`

Returns a String containing a string representation of the receiver.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
