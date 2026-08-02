---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/WORequestHandler.html
archived_at: '2026-07-18T01:28:54.263072Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](WORequest-2.md)
[!](WOResourceManager-2.md)

---

# WORequestHandler

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
WebObjects/WOResourceManager.h

---

## Class Description

WORequestHandler is an abstract class that defines request handlers. A request handler is an object that can handle requests received by the WebObjects adaptor. All WebObjects applications have multiple request handlers that can handle certain types of requests. Three private request handlers are defined in the WebObjects framework:

- WOComponentRequestHandler, which handles requests for actions implemented in a component.
- WODirectActionRequestHandler, which handles requests for actions implemented in a WODirectAction class.
- WOResourceRequestHandler, which handles requests for resources.

These three request handlers handle most styles of requests that an application can typically receive. If you want to create your own style of request, then you should write your own WORequestHandler. Unless you write your own request handler, your code typically won't have to directly interact with WORequestHandler objects at all.

---

# Adopted Protocols

**NSLocking**

**- lock

**- unlock****

---

## Method Types

**Handling Requests**

**[- handleRequest:](#apple-ge4teoa)

******

---

## Instance Methods

---

### handleRequest:

- (WOResponse \*)`handleRequest:`(WORequest \*)_aRequest_

Request handlers must implement this method and perform all request-specific handling. (See "Writing Your Own Request Handler" in the class description for examples. <<Find this cross-ref>>) By default, a request is an HTTP request. You must supply your own server-side adaptor to accept anything other than HTTP.

****

---

[!](WORequest-2.md)
[!](WOResourceManager-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
