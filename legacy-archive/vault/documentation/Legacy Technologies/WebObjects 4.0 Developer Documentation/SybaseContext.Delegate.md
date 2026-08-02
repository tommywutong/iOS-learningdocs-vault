---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/SybaseContextDelegate.html
archived_at: '2026-07-18T01:28:50.241162Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](SybaseChannel.Delegate.md)

---

# SybaseContext.Delegate

SybaseContext delegate objects

__Inherits From:__
com.apple.yellow.sybaseeoadaptor

---

## Class Description

The SybaseContext delegate object allows developers access to all the messages returned from the Sybase client library or the Sybase Server. If your implementation of these delegate methods returns `false`, the SybaseContext will not report the message (or error). If your implementation returns `true`, the SybaseContext will continue as usual. Most messages are reported in exceptions, but messages with a severity of 0 are simply ignored.

---

## Instance Methods

---

### sybaseContextShouldReportClientMessage

public abstract boolean `sybaseContextShouldReportClientMessage`(SybaseContext _context_,
NSDictionary _clientMessage_)

Invoked when an exception results from a callback to the CS_CLIENTMSG_CB (Sybase ClientMessage callback). Gives the delegate the opportunity to substitute _clientMessage_ as the userInfo dictionary.

---

### sybaseContextShouldReportServerMessage

public abstract boolean `sybaseContextShouldReportServerMessage`(SybaseContext _context_,
NSDictionary _serverMessage_)

Invoked when an exception results from a callback to the CS_SERVERMSG_CB (Sybase ServerMessage callback). Gives the delegate the opportunity to substitute _serverMessage_ as the userInfo dictionary.

---

[!](SybaseChannel.Delegate.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
