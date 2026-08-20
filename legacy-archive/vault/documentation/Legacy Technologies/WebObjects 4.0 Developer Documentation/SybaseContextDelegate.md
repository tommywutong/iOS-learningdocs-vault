---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/SybaseContextDelegate.html
archived_at: '2026-07-18T01:28:50.706316Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](SybaseChannelDelegate.md)

---

# SybaseContextDelegate

__Adopted By:__
SybaseContext delegate objects

__Declared in:__
SybaseEOAdaptor/SybaseContext.h

---

## Class Description

The SybaseContext delegate object allows developers access to all the messages returned from the Sybase client library or the Sybase Server. If your implementation of these delegate methods returns NO, the SybaseContext will not report the message (or error). If your implementation returns YES, the SybaseContext will continue as usual. Most messages are reported in exceptions, but messages with a severity of 0 are simply ignored.

---

## Instance Methods

---

### sybaseContext:shouldReportClientMessage:

- (BOOL)__sybaseContext:__ (SybaseContext \*)_context_
__shouldReportClientMessage:__ (NSDictionary \*)_clientMessage_

Invoked when an exception results from a callback to the CS_CLIENTMSG_CB (Sybase ClientMessage callback). Gives the delegate the opportunity to substitute _clientMessage_ as the userInfo dictionary.

---

### sybaseContext:shouldReportServerMessage:

- (BOOL)__sybaseContext:__ (SybaseContext \*)_context_
__shouldReportServerMessage:__ (NSDictionary \*)_serverMessage_

Invoked when an exception results from a callback to the CS_SERVERMSG_CB (Sybase ServerMessage callback). Gives the delegate the opportunity to substitute _serverMessage_ as the userInfo dictionary.

---

[[TOC]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html) [[Prev]](SybaseChannelDelegate.md) [Next]

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
