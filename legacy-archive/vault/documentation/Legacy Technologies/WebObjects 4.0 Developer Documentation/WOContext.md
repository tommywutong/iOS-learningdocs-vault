---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/WOContext.html
archived_at: '2026-07-18T01:28:51.279173Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](WOComponent.md)
[!](WOCookie.md)

---

# WOContext

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.webobjects

---

## Class Description

A WOContext object lets you access objects and information that define the _context_ of a transaction. In a typical request-response loop (a transaction), several objects have a hand in what is going on: the [WOApplication](WOApplication.md) and [WOSession](WOSession.md) objects, the page involved in the request or response (a [WOComponent](WOComponent.md) object), the page's subcomponents (also WOComponents), plus the dynamic elements on the page. The WOContext object passed as an argument in the [`takeValuesFromRequest`](WOComponent.md#apple-ge3tg), [`invokeActionForRequest`](WOComponent.md#apple-geytg), and [`appendToResponse`](WOComponent.md#apple-geydgmq) messages allows access to these objects. A context is identified by the _context ID_, which appears in the URL after the session ID and page name. Each context ID is an integer that the session increments each time a new context is created.

WOContext objects provide other information and services related to the current transaction. From them you can get the entire URL currently in effect as well as portions of that URL, such as the element ID, the context ID, and the URL up to and including the session ID.

A WOContext object plays a further role behind the scenes. For the benefit of a page's dynamic elements, it keeps track of the _current component_, that is, the WOComponent associated with the current element in the request-handling cycle. The current component can be the WOComponent that represents one of the page's subcomponents or the page itself. By reference to the current component (accessed through WOContext's [`component`](#apple-gu3q) method), a dynamic element can exchange values associatively between itself and the WOComponent that contains it.

---

## Method Types

**Constructors**

**[WOContext](#apple-geytgnbw)**

**Creating new object instances**

**[contextWithRequest](#apple-gqyq)

******

**Obtaining attributes**

**[component](#apple-gu3q)

**[contextID](#apple-gy2q)

**[elementID](#apple-hayq)

**[hasSession](#apple-ha2q)

**[isInForm](#apple-gm3dmmy)

**[page](#apple-geydc)

**[request](#apple-geydk)

**[response](#apple-gm2tmnq)

**[session](#apple-geyto)

**[senderID](#apple-gu2dcna)

**[setInForm](#apple-gm3tamq)**********************

**Manipulating element ID**

****[appendElementIDComponent](#apple-gq2q)

**[appendZeroElementIDComponent](#apple-gq4q)

**[deleteAllElementIDComponents](#apple-gy4q)

**[deleteLastElementIDComponent](#apple-g4zq)

**[incrementLastElementIDComponent](#apple-ha4q)************

**Generating URLs**

**[directActionURLForActionNamed](#apple-g43q)

**[completeURLWithRequestHandlerKey](#apple-guzq)

**[componentActionURL](#apple-gyyq)

**[urlWithRequestHandlerKey](#apple-gezdc)

************

---

## Constructors

---

### WOContext

public `WOContext`()

Returns a WOContext instance initialized with a unique context ID.

---

## Class Methods

---

### contextWithRequest

public static WOContext `contextWithRequest`(WORequest _aRequest_)

Creates and returns a WOContext with _aRequest_. This is the preferred way to create a WOContext. All other constructors call this one, so if you subclass WOContext, you need to override only this one.

---

## Instance Methods

---

### appendElementIDComponent

public void `appendElementIDComponent`(java.lang.String _aString_)

Appends a string to the current element ID to create an identifier of an HTML element. For example, if the current element ID is "0.1.1" and you send this message with an argument of "NameField," the element ID for that field becomes "0.1.1.NameField".

__See also:__
[`deleteAllElementIDComponents`](#apple-gy4q), [`deleteLastElementIDComponent`](#apple-g4zq),
[`incrementLastElementIDComponent`](#apple-ha4q)

---

### appendZeroElementIDComponent

public void `appendZeroElementIDComponent`()

Appends a ".0" to the current element ID to create an identifier of the first "child" HTML element. For example, if the current element ID is "0.1.1", after you send this message the element ID becomes "0.1.1.0".

__See also:__
[`deleteAllElementIDComponents`](#apple-gy4q), [`deleteLastElementIDComponent`](#apple-g4zq),
[`incrementLastElementIDComponent`](#apple-ha4q)

---

### completeURLWithRequestHandlerKey

public java.lang.String `completeURLWithRequestHandlerKey`(java.lang.String _requestHandlerKey_,
java.lang.String _aRequestHandlerPath_,
java.lang.String _aQueryString_,
boolean _isSecure_,
int _somePort_)

Returns the complete URL for the specified request handler. The _requestHandlerKey_ is one of the keys provided by WOApplication. The _requestHandlerPath_ is any URL encoded string. The _queryString_ is added at the end of the URL behind a "?". If _isSecure_ is true, this method uses "https" instead of "http." If _somePort_ is 0 (zero), this method uses the default port.

__See also:__
[`urlWithRequestHandlerKey`](#apple-gezdc)

---

### component

public WOComponent `component`()

Returns the component that dynamic elements are currently using to push and pull values associatively. This component could represent the current request or response page or a subcomponent of that page.

__See also:__
[WOComponent](WOComponent.md) class, [`page`](#apple-geydc), [`request`](#apple-geydk), [`response`](#apple-gm2tmnq), [`senderID`](#apple-gu2dcna)

---

### componentActionURL

public java.lang.String `componentActionURL`()

Returns the complete URL for the component action.

---

### contextID

public java.lang.String `contextID`()

Returns the context ID of the receiver.

---

### deleteAllElementIDComponents

public void `deleteAllElementIDComponents`()

Deletes all components of the current element ID.

__See also:__
[`appendElementIDComponent`](#apple-gq2q), [`appendZeroElementIDComponent`](#apple-gq4q),
[`incrementLastElementIDComponent`](#apple-ha4q)

---

### deleteLastElementIDComponent

public void `deleteLastElementIDComponent`()

Deletes the last digit (or name) of the current element ID, along with its dot separator. Thus, after sending this message, "0.0.1.1" becomes "0.0.1".

__See also:__
[`appendElementIDComponent`](#apple-gq2q), [`appendZeroElementIDComponent`](#apple-gq4q),
[`incrementLastElementIDComponent`](#apple-ha4q)

---

### directActionURLForActionNamed

public java.lang.String `directActionURLForActionNamed`(java.lang.String _anActionName_,
NSDictionary _aQueryDict_)

Returns the complete URL for the specified action. You can specify _aQueryDict_, and _anActionName_ can be "ActionClass/ActionName" or "ActionName".

__See also:__
[WODirectAction](WODirectAction.md) class specification

---

### elementID

public java.lang.String `elementID`()

Returns the element ID identifying the current [WOElement](WOElement.md).This method helps you avoid creating a session in direct actions.

---

### hasSession

public boolean `hasSession`()

Returns whether a session exists for the receiving context.

__See also:__
[`senderID`](#apple-gu2dcna)

---

### incrementLastElementIDComponent

public void `incrementLastElementIDComponent`()

Increments the last digit of the current element ID. For example, after this message is sent, "0.0.1.2" becomes "0.0.1.3".

__See also:__
[`appendElementIDComponent`](#apple-gq2q), [`appendZeroElementIDComponent`](#apple-gq4q),
[`deleteAllElementIDComponents`](#apple-gy4q), [`deleteLastElementIDComponent`](#apple-g4zq)

---

### isInForm

public boolean `isInForm`()

Returns true when in the context of a WOForm.

__See also:__
[`setInForm`](#apple-gm3tamq)

---

### page

public WOComponent `page`()

Returns the [WOComponent](WOComponent.md) object that represents the request or response page.

__See also:__
[`component`](#apple-gu3q), [`request`](#apple-geydk), [`response`](#apple-gm2tmnq), [`senderID`](#apple-gu2dcna)

---

### request

public WORequest `request`()

Returns the transaction's [WORequest](WORequest.md) object.

__See also:__
[`component`](#apple-gu3q), [`page`](#apple-geydc), [`response`](#apple-gm2tmnq), [`senderID`](#apple-gu2dcna)

---

### response

public WOResponse `response`()

Returns the transaction's [WOResponse](WOResponse.md) object.

__See also:__
[`component`](#apple-gu3q), [`page`](#apple-geydc), [`response`](#apple-gm2tmnq), [`senderID`](#apple-gu2dcna)

---

### senderID

public java.lang.String `senderID`()

Returns the part of the WORequest's URI that identifies the dynamic element on the page (such as a form or an active image) responsible for submitting the request. The sender ID is the same as the element ID used to identify the dynamic element. A request's sender ID may be __null__ , as it always is on the first request of a session.

__See also:__
[`request`](#apple-geydk) , ____`uri` __(WORequest)__

---

### session

public WOSession `session`()

Returns the object representing the receiving context's session, if one exists. If the receiver does not have a session, this method creates a new session object and returns it. Note that not all contexts have a session: Direct Actions, for instance, don't always need a session. Use [`hasSession`](#apple-ha2q) to determine whether a context has a session associated with it.

__See also:__
[`component`](#apple-gu3q), [`page`](#apple-geydc), [`request`](#apple-geydk), [`response`](#apple-gm2tmnq), [WOSession](WOSession.md) class

---

### setInForm

public void `setInForm`(boolean _flag_)

If you write something that behaves like a WOForm, set this to notify WODynamicElements that they are in a form.

__See also:__
[`isInForm`](#apple-gm3dmmy)

---

### urlWithRequestHandlerKey

public java.lang.String `urlWithRequestHandlerKey`(java.lang.String _requestHandlerKey_,
java.lang.String _aRequestHandlerPath_,
java.lang.String _aQueryString_)

Returns a URL relative to `cgi-bin/WebObjects` for the specified request handler. The _requestHandlerKey_ is one of the keys provided by WOApplication. The _requestHandlerPath_ is any URL encoded string. The _queryString_ is added at the end of the URL behind a "?".

[`completeURLWithRequestHandlerKey`](#apple-guzq)

---

[!](WOComponent.md)
[!](WOCookie.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
