---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/SybaseEOAdaptor.framework/ObjC_classic/Classes/SybaseChannel.html
archived_at: '2026-07-15T08:11:46.541309Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
SybaseEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../SybaseEOAdaptorTOC.md)

# SybaseChannel

> __Inherits
> from:__  EOAdaptorChannel : NSObject

> __Declared in:__  SybaseEOAdaptor/SybaseChannel.h

---

## Class Description

---

A SybaseChannel represents an independent communication channel
to the database server its SybaseAdaptor is connected to. All of
a SybaseChannel's operations take place within the context of transactions
controlled or tracked by its SybaseContext. A Sybase adaptor context
manages one channel, and a channel is associated with only one context.

[![Table of Contents](attachments/images/up.gif)](../SybaseEOAdaptorTOC.md)
