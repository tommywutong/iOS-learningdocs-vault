---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/WOContext.html
archived_at: '2026-07-18T01:28:53.597778Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](WOComponent-2.md)
[!](WOCookie-2.md)

---

# WOContext

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
WebObjects/WOContext.h

---

## Class Description

A WOContext object lets you access objects and information that define the _context_ of a transaction. In a typical request-response loop (a transaction), several objects have a hand in what is going on: the [WOApplication](WOApplication-2.md) and [WOSession](WOSession-2.md) objects, the page involved in the request or response (a [WOComponent](WOComponent-2.md) object), the page's subcomponents (also WOComponents), plus the dynamic elements on the page. The WOContext object passed as an argument in the [__takeValuesFromRequest:inContext:__](WOComponent-2.md#apple-ge3tg), [__invokeActionForRequest:inContext:__](WOComponent-2.md#apple-geytg), and [__appendToResponse:inContext:__](WOComponent-2.md#apple-geydgmq) messages allows access to these objects. A context is identified by the _context ID_, which appears in the URL after the session ID and page name. Each context ID is an integer that the session increments each time a new context is created.

WOContext objects provide other information and services related to the current transaction. From them you can get the entire URL currently in effect as well as portions of that URL, such as the element ID, the context ID, and the URL up to and including the session ID.

A WOContext object plays a further role behind the scenes. For the benefit of a page's dynamic elements, it keeps track of the _current component_, that is, the WOComponent associated with the current element in the request-handling cycle. The current component can be the WOComponent that represents one of the page's subcomponents or the page itself. By reference to the current component (accessed through WOContext's [__component__](#apple-gu3q) method), a dynamic element can exchange values associatively between itself and the WOComponent that contains it.

---

# Adopted Protocols

**NSCopying**

**- copy

**- copyWithZone:****

---

## Method Types

**Creating new object instances**

**[+ contextWithRequest:](#apple-gqyq)

**[- init](#apple-geytaobv)

**[- initWithRequest:](#apple-geytaoju)

**********

**Obtaining attributes**

**[- component](#apple-gu3q)

**[- contextID](#apple-gy2q)

**[- elementID](#apple-hayq)

**[- hasSession](#apple-ha2q)

**[- isInForm](#apple-gm3dmmy)

**[- page](#apple-geydc)

**[- request](#apple-geydk)

**[- response](#apple-gm2tmnq)

**[- session](#apple-geyto)

**[- senderID](#apple-gu2dcna)

**[- setInForm:](#apple-gm3tamq)**********************

**Manipulating element ID**

****[- appendElementIDComponent:](#apple-gq2q)

**[- appendZeroElementIDComponent](#apple-gq4q)

**[- deleteAllElementIDComponents](#apple-gy4q)

**[- deleteLastElementIDComponent](#apple-g4zq)

**[- incrementLastElementIDComponent](#apple-ha4q)************

**Generating URLs**

**[- directActionURLForActionNamed:queryDictionary:](#apple-g43q)

**[- completeURLWithRequestHandlerKey:path:queryString:isSecure:
port:](#apple-guzq)

**[- componentActionURL](#apple-gyyq)

**[- urlWithRequestHandlerKey:path:queryString:](#apple-gezdc)

************

---

## Class Methods

---

### contextWithRequest:

+ (WOContext \*)__contextWithRequest:__ (WORequest \*)_aRequest_

Creates and returns a WOContext with _aRequest_. This is the preferred way to create a WOContext. All other constructors call this one, so if you subclass WOContext, you need to override only this one.

---

## Instance Methods

---

### appendElementIDComponent:

- (void)__appendElementIDComponent:__ (NSString \*)_aString_

Appends a string to the current element ID to create an identifier of an HTML element. For example, if the current element ID is "0.1.1" and you send this message with an argument of "NameField," the element ID for that field becomes "0.1.1.NameField".

__See also:__
[- __deleteAllElementIDComponents__](#apple-gy4q), [- __deleteLastElementIDComponent__](#apple-g4zq),
[- __incrementLastElementIDComponent__](#apple-ha4q)

---

### appendZeroElementIDComponent

- (void)__appendZeroElementIDComponent__

Appends a ".0" to the current element ID to create an identifier of the first "child" HTML element. For example, if the current element ID is "0.1.1", after you send this message the element ID becomes "0.1.1.0".

__See also:__
[- __deleteAllElementIDComponents__](#apple-gy4q), [- __deleteLastElementIDComponent__](#apple-g4zq),
[- __incrementLastElementIDComponent__](#apple-ha4q)

---

### completeURLWithRequestHandlerKey:path:queryString:isSecure:port:

- (NSString \*)__completeURLWithRequestHandlerKey:__ (NSString \*)_requestHandlerKey___path:__ (NSString \*)_aRequestHandlerPath___queryString:__ (NSString \*)_aQueryString___isSecure:__ (BOOL)_isSecure___port:__ (int)_somePort_

Returns the complete URL for the specified request handler. The _requestHandlerKey_ is one of the keys provided by WOApplication. The _requestHandlerPath_ is any URL encoded string. The _queryString_ is added at the end of the URL behind a "?". If _isSecure_ is YES, this method uses "https" instead of "http." If _somePort_ is 0 (zero), this method uses the default port.

__See also:__
[- __urlWithRequestHandlerKey:path:queryString:__](#apple-gezdc)

---

### component

- (WOComponent \*)__component__

Returns the component that dynamic elements are currently using to push and pull values associatively. This component could represent the current request or response page or a subcomponent of that page.

__See also:__
[WOComponent](WOComponent-2.md) class, [- __page__](#apple-geydc), [- __request__](#apple-geydk), [- __response__](#apple-gm2tmnq), [- __senderID__](#apple-gu2dcna)

---

### componentActionURL

- (NSString \*)__componentActionURL__

Returns the complete URL for the component action.

---

### contextID

- (NSString \*)__contextID__

Returns the context ID of the receiver.

---

### deleteAllElementIDComponents

- (void)__deleteAllElementIDComponents__

Deletes all components of the current element ID.

__See also:__
[- __appendElementIDComponent:__](#apple-gq2q), [- __appendZeroElementIDComponent__](#apple-gq4q),
[- __incrementLastElementIDComponent__](#apple-ha4q)

---

### deleteLastElementIDComponent

- (void)__deleteLastElementIDComponent__

Deletes the last digit (or name) of the current element ID, along with its dot separator. Thus, after sending this message, "0.0.1.1" becomes "0.0.1".

__See also:__
[- __appendElementIDComponent:__](#apple-gq2q), [- __appendZeroElementIDComponent__](#apple-gq4q),
[- __incrementLastElementIDComponent__](#apple-ha4q)

---

### directActionURLForActionNamed:queryDictionary:

- (NSString \*)__directActionURLForActionNamed:__ (NSString \*)_anActionName___queryDictionary:__ (NSDictionary \*)_aQueryDict_

Returns the complete URL for the specified action. You can specify _aQueryDict_, and _anActionName_ can be @"ActionClass/ActionName" or @"ActionName".

__See also:__
[WODirectAction](WODirectAction-2.md) class specification

---

### elementID

- (NSString \*)__elementID__

Returns the element ID identifying the current [WOElement](WOElement-2.md).This method helps you avoid creating a session in direct actions.

---

### hasSession

- (BOOL)__hasSession__

Returns whether a session exists for the receiving context.

__See also:__
[- __senderID__](#apple-gu2dcna)

---

### incrementLastElementIDComponent

- (void)__incrementLastElementIDComponent__

Increments the last digit of the current element ID. For example, after this message is sent, "0.0.1.2" becomes "0.0.1.3".

__See also:__
[- __appendElementIDComponent:__](#apple-gq2q), [- __appendZeroElementIDComponent__](#apple-gq4q),
[- __deleteAllElementIDComponents__](#apple-gy4q), [- __deleteLastElementIDComponent__](#apple-g4zq)

---

### init

- (id)__init__

Returns a WOContext instance initialized with a unique context ID. Generally, you should call [__initWithRequest:__](#apple-geytaoju) instead to ensure that the WOContext instance is properly initialized.

---

### initWithRequest:

- (id)__initWithRequest:__ (WORequest \*)_aRequest_

Returns a WOContext with _aRequest_.

---

### isInForm

- (BOOL)__isInForm__

Returns YES when in the context of a WOForm.

__See also:__
[__setInForm:__](#apple-gm3tamq)

---

### page

- (WOComponent \*)__page__

Returns the [WOComponent](WOComponent-2.md) object that represents the request or response page.

__See also:__
[- __component__](#apple-gu3q), [- __request__](#apple-geydk), [- __response__](#apple-gm2tmnq), [- __senderID__](#apple-gu2dcna)

---

### request

- (WORequest \*)__request__

Returns the transaction's [WORequest](WORequest-2.md) object.

__See also:__
[- __component__](#apple-gu3q), [- __page__](#apple-geydc), [- __response__](#apple-gm2tmnq), [- __senderID__](#apple-gu2dcna)

---

### response

- (WOResponse \*)__response__

Returns the transaction's [WOResponse](WOResponse-2.md) object.

__See also:__
[- __component__](#apple-gu3q), [- __page__](#apple-geydc), [- __response__](#apple-gm2tmnq), [- __senderID__](#apple-gu2dcna)

---

### senderID

- (NSString \*)__senderID__

Returns the part of the WORequest's URI that identifies the dynamic element on the page (such as a form or an active image) responsible for submitting the request. The sender ID is the same as the element ID used to identify the dynamic element. A request's sender ID may be `nil`, as it always is on the first request of a session.

__See also:__
`[-](#apple-geytaoju)`__initWithRequest:__ `,` [- __request__](#apple-geydk) , `[-](WORequest.md#apple-ge2tc)`__uri__  `(WORequest)`

---

### session

- (WOSession \*)__session__

Returns the object representing the receiving context's session, if one exists. If the receiver does not have a session, this method creates a new session object and returns it. Note that not all contexts have a session: Direct Actions, for instance, don't always need a session. Use [__hasSession__](#apple-ha2q) to determine whether a context has a session associated with it.

__See also:__
[- __component__](#apple-gu3q), [- __page__](#apple-geydc), [- __request__](#apple-geydk), [- __response__](#apple-gm2tmnq), [WOSession](WOSession-2.md) class

---

### setInForm:

- __setInForm:__ (BOOL)_flag_

If you write something that behaves like a WOForm, set this to notify WODynamicElements that they are in a form.

__See also:__
[__isInForm__](#apple-gm3dmmy)

---

### urlWithRequestHandlerKey:path:queryString:

- (NSString \*)__urlWithRequestHandlerKey:__ (NSString \*)_requestHandlerKey___path:__ (NSString \*)_aRequestHandlerPath___queryString:__ (NSString \*)_aQueryString_

Returns a URL relative to `cgi-bin/WebObjects` for the specified request handler. The _requestHandlerKey_ is one of the keys provided by WOApplication. The _requestHandlerPath_ is any URL encoded string. The _queryString_ is added at the end of the URL behind a "?".

[- __completeURLWithRequestHandlerKey:path:queryString:isSecure:port:__](#apple-guzq)

---

[!](WOComponent-2.md)
[!](WOCookie-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
