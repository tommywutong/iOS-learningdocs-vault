---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/WORequestHandler.html
archived_at: '2026-07-15T08:11:47.708711Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)

# WORequestHandler

> __Inherits
> from:__  NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  WebObjects/WOResourceManager.h

---

## Class Description

---

WORequestHandler is an abstract class that defines request
handlers. A request handler is an object that can handle requests
received by the WebObjects adaptor. All WebObjects applications
have multiple request handlers that can handle certain types of
requests. Three private request handlers are defined in the WebObjects
framework:

- WOComponentRequestHandler, which handles requests
  for actions implemented in a component.
- WODirectActionRequestHandler, which handles requests for actions
  implemented in a WODirectAction class.
- WOResourceRequestHandler, which handles requests for resources.

These three request handlers handle most styles of requests
that an application can typically receive. If you want to create
your own style of request, then you should write your own WORequestHandler. Unless
you write your own request handler, your code typically won't
have to directly interact with WORequestHandler objects at all.

## Adopted Protocols

---

> NSLocking: - lock
> : - unlock

## Instance Methods

---

### handleRequest:

`- (WOResponse *)handleRequest:(WORequest
*)aRequest`

Request handlers must implement this method
and perform all request-specific handling. By default, a request
is an HTTP request. You must supply your own server-side adaptor
to accept anything other than HTTP.

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
