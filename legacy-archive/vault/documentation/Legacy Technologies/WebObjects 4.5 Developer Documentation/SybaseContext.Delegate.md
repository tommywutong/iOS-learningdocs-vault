---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/SybaseEOAdaptor.framework/Java/Protocols/SybaseContextDelegate.html
archived_at: '2026-07-15T08:11:46.501189Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
SybaseEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../SybaseEOAdaptorTOC.md) 

# SybaseContext.Delegate

> __(informal interface)__

> __Package:__
> com.apple.yellow.sybaseeoadaptor

## Interface Description

---

The SybaseContext delegate object allows developers access
to all the messages returned from the Sybase client library or the
Sybase Server. If your implementation of these delegate methods
returns false, the SybaseContext will not report the message (or
error). If your implementation returns true, the SybaseContext will
continue as usual. Most messages are reported in exceptions, but
messages with a severity of 0 are simply ignored.

## Instance Methods

---

### sybaseContextShouldReportClientMessage

`public abstract boolean sybaseContextShouldReportClientMessage(
SybaseContext context,
NSDictionary clientMessage)`

Invoked when an exception results from a callback
to the CS_CLIENTMSG_CB (Sybase ClientMessage callback). Gives the
delegate the opportunity to substitute _clientMessage_ as
the __userInfo__ dictionary.

---

### sybaseContextShouldReportServerMessage

`public abstract boolean sybaseContextShouldReportServerMessage(
SybaseContext context,
NSDictionary serverMessage)`

Invoked when an exception results from a callback
to the CS_SERVERMSG_CB (Sybase ServerMessage callback). Gives the
delegate the opportunity to substitute _serverMessage_ as
the __userInfo__ dictionary.

---

[![Table of Contents](attachments/images/up.gif)](../SybaseEOAdaptorTOC.md)
