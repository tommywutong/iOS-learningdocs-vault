---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/SybaseChannel.html
archived_at: '2026-07-18T01:28:49.845448Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](SybaseAdaptor.md)
[!](SybaseContext.md)

---

# SybaseChannel

__Inherits From:__
EOAdaptorChannel : NSObject

__Inherits From:__
com.apple.yellow.sybaseeoadaptor

---

## Class Description

A SybaseChannel represents an independent communication channel to the database server its SybaseAdaptor is connected to. All of a SybaseChannel's operations take place within the context of transactions controlled or tracked by its SybaseContext. A Sybase adaptor context manages one channel, and a channel is associated with only one context.

The feature SybaseChannel adds to EOAdaptorChannel is processing for compute rows and stored procedures (see the framework introduction for more information).

SybaseChannel has two delegate methods; for a complete description, see the [SybaseChannel.Delegate](SybaseChannel.Delegate.md) interface specification.

---

[!](SybaseAdaptor.md)
[!](SybaseContext.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
