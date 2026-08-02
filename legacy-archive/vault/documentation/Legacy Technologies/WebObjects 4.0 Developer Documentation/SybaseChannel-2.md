---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/SybaseChannel.html
archived_at: '2026-07-18T01:28:50.398262Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](SybaseAdaptor-2.md)
[!](SybaseContext-2.md)

---

# SybaseChannel

__Inherits From:__
EOAdaptorChannel : NSObject

__Declared in:__
SybaseEOAdaptor/SybaseChannel.h

---

## Class Description

A SybaseChannel represents an independent communication channel to the database server its SybaseAdaptor is connected to. All of a SybaseChannel's operations take place within the context of transactions controlled or tracked by its SybaseContext. A Sybase adaptor context manages one channel, and a channel is associated with only one context.

The feature SybaseChannel adds to EOAdaptorChannel is processing for compute rows and stored procedures (see the framework introduction for more information).

SybaseChannel has two delegate methods; for a complete description, see the [SybaseChannelDelegate](SybaseChannelDelegate.md) protocol specification.

---

[!](SybaseAdaptor-2.md)
[!](SybaseContext-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
