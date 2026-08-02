---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/WORequestHandler.html
archived_at: '2026-07-18T01:28:52.122437Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](WORequest.md)
[!](WOResourceManager.md)

---

# WORequestHandler

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.webobjects

---

## Class Description

WORequestHandler is an abstract class that defines request handlers. A request handler is an object that can handle requests received by the WebObjects adaptor. All WebObjects applications have multiple request handlers that can handle certain types of requests. Three private request handlers are defined in the WebObjects framework:

- WOComponentRequestHandler, which handles requests for actions implemented in a component.
- WODirectActionRequestHandler, which handles requests for actions implemented in a WODirectAction class.
- WOResourceRequestHandler, which handles requests for resources.

These three request handlers handle most styles of requests that an application can typically receive. If you want to create your own style of request, then you should write your own WORequestHandler. Unless you write your own request handler, your code typically won't have to directly interact with WORequestHandler objects at all.

---

## Method Types

**Constructor**

**[`WORequestHandler`](#apple-gm3teoi)**

**Handling Requests**

**[handleRequest](#apple-ge4teoa)

******

---

## Constructors

---

### WORequestHandler

public `WORequestHandler`()

Returns an initialized WORequestHandler.

---

## Instance Methods

---

### handleRequest

public WOResponse `handleRequest`(WORequest _aRequest_)

Request handlers must implement this method and perform all request-specific handling. By default, a request is an HTTP request. You must supply your own server-side adaptor to accept anything other than HTTP.

****

---

[!](WORequest.md)
[!](WOResourceManager.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
