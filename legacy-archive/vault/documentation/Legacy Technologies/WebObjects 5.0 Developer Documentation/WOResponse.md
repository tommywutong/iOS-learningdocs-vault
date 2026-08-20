---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Classes/WOResponse.html
archived_at: '2026-07-15T08:15:15.822928Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# WOResponse

> **__Inherits from:__**
> : [WOResponse](#apple-k5hvezltobxw443f):

> **__Implements:__**
> : WOActionResults: Cloneable

> **__Package:__**
> : com.appserver.webobjects

---

## Class Description

---

A WOResponse object represents an HTTP response that an application returns to a Web server to complete a cycle of the request-response loop. The composition of a response occurs during the third and final phase of this loop, a phase marked by the propagation of the appendToResponse message through the objects of the application. The WOApplication object first sends this message, passing in a newly-created WOResponse object as an argument. WOElement objects, which represent the dynamic and static HTML elements on a page, respond to the message by appending their HTML representation to the content of the WOResponse object. WOApplication, WOSession, and WOComponent objects can also respond to the message by adding information to the WOResponse object.

A WOResponse has two major parts: HTML content and HTTP information. The content is what is displayed in a Web browser; it can include _escaped_ HTML, which is HTML code shown "as is," uninterpreted. The other information encapsulated by a WOResponse object is used when handling the response. This HTTP data includes headers, status codes, and version string. See the HTTP specification or HTTP documentation for descriptions of these items.

The [WOResponse](#apple-k5hvezltobxw443f) class-from which WOResponse inherits-declares most of the methods you use when constructing a response. These methods can be divided into two groups, those that add to a response's HTML content and those that read and set HTTP information. For images and other binary data, use appendContentData (declared in the [WOResponse](#apple-k5hvezltobxw443f) class). You can obtain and set the entire content of the response with [WOResponse](#apple-k5hvezltobxw443f)'s content and setContent methods. The following example shows a sequence of __appendContent...__ messages that compose an HTTP "POST" message:

> ```
> aResponse.appendContentString("<form method=\"POST\" action=\"");
> aResponse.appendContentHTMLAttributeValue(aContext.url());
> aResponse.appendContentCharacter('"');
> aResponse.appendContentString(">");
> ```

The remaining WOResponse instance methods set and read the the HTTP status code. WOResponse also provides two class methods that allow you to escape string objects.

## Interfaces Implemented

---

> : WOActionResults: [generateResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg4dpnzzwkl3hmvxgk4tborsvezltobxw443f):

## Method Types

---

> **Creation**
> : [WOResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg4dpnzzwkl2xj5jgk43qn5xhgzi)
>
> **Working with HTTP status**
> : [setStatus](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg4dpnzzwkl3tmv2fg5dbor2xg): [status](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg4dpnzzwkl3torqxi5lt)
>
> **Working with HTML content**
> : [generateResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg4dpnzzwkl3hmvxgk4tborsvezltobxw443f)
>
> **Controlling Client Caching**
> : [disableClientCaching](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg4dpnzzwkl3enfzwcytmmvbwy2lfnz2egyldnbuw4zy)

## Constructors

---

### WOResponse

`public WOResponse()`

Returns an initialized WOResponse instance. HTTP status is set to 200 (OK), client caching is enabled, and the default string encoding is made ISO Latin 1.

---

## Instance Methods

---

### __clone__

`public Object clone()`

Conformance to Cloneable.

---

### disableClientCaching

`public void disableClientCaching()`

Attempts to disable caching in the client browser by appending a "no-cache" Cache-Control response directive to the HTTP response and by appending Expires and Date values that equal (they are both set to the current date and time).

This method shouldn't be invoked more than once for a given response.

---

### generateResponse

`public WOResponse generateResponse()`

Returns a WOResponse object. WOResponse's implementation simply returns itself.

__See Also:__ [generateResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg4dpnzzwkl3hmvxgk4tborsvezltobxw443f) (WOComponent)

---

### setStatus

`public void setStatus(int anInt)`

Sets the HTTP status to _anInt_. Consult the HTTP specification or HTTP documentation for the significance of status integers.

__See Also:__ [status](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg4dpnzzwkl3torqxi5lt)

---

### status

`public int status()`

Returns an integer code representing the HTTP status. Consult the HTTP specification or HTTP documentation for the significance of these status codes.

By default, the status is 200 ("OK" status).

__See Also:__ [setStatus](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg4dpnzzwkl3tmv2fg5dbor2xg)

---

### __toString__

`public String toString()`

Returns a String representation of the receiver suitable for debugging purposes.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
