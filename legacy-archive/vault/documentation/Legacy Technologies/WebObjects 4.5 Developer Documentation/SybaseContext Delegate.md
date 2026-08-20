---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/SybaseEOAdaptor.framework/ObjC_classic/Protocols/SybaseContextDelegate.html
archived_at: '2026-07-15T08:11:46.625565Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
SybaseEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../SybaseEOAdaptorTOC.md) 

# SybaseContext Delegate

> __(informal protocol)__

> __Declared in:__  SybaseEOAdaptor/SybaseContext.h

## Protocol Description

---

The SybaseContext delegate object allows developers access
to all the messages returned from the Sybase client library or the
Sybase Server. If your implementation of these delegate methods
returns NO, the SybaseContext will not report the message (or error).
If your implementation returns YES, the SybaseContext will continue
as usual. Most messages are reported in exceptions, but messages
with a severity of 0 are simply ignored.

## Instance Methods

---

### sybaseContext:shouldReportClientMessage:

`- (BOOL)sybaseContext:(SybaseContext
*)context
shouldReportClientMessage:(NSDictionary
*)clientMessage`

Invoked when an exception results from a callback
to the CS_CLIENTMSG_CB (Sybase ClientMessage callback). Gives the
delegate the opportunity to substitute _clientMessage_ as
the __userInfo__ dictionary.

---

### sybaseContext:shouldReportServerMessage:

`- (BOOL)sybaseContext:(SybaseContext
*)context
shouldReportServerMessage:(NSDictionary
*)serverMessage`

Invoked when an exception results from a callback
to the CS_SERVERMSG_CB (Sybase ServerMessage callback). Gives the
delegate the opportunity to substitute _serverMessage_ as
the __userInfo__ dictionary.

---

[![Table of Contents](attachments/images/up.gif)](../SybaseEOAdaptorTOC.md)
