---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/OracleEOAdaptor.framework/ObjC_classic/Classes/OracleContext.html
archived_at: '2026-07-15T08:11:46.337554Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
OracleEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../OracleEOAdaptorTOC.md)

# OracleContext

> __Inherits
> from:__  EOAdaptorContext : NSObject

> __Declared in:__  OracleEOAdaptor/OracleContext.h

---

## Class Description

---

An OracleContext represents a single transaction scope on
the database server to which its adaptor object is connected. If
the server supports multiple concurrent transaction sessions, the
adaptor may have several adaptor contexts. An OracleContext may
in turn have several OracleChannels, which handle actual access
to the data on the server.

The features the OracleContext class adds to EOAdaptorContext
are methods for returning Oracle-specific data structures that describe
characteristics of the context: hostDataArea and logonDataArea.
hostDataArea returns the `hda_def` data
structure, and logonDataArea returns the `lda_def` data
structure. If you intend to extend the OracleContext by making calls
to the Oracle API, you'll need these data structures.

## Method Types

---

> **Managing a connection
> to the server**
> : [- connect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu64tbmnwgkq3pnz2gk6duf5rw63tomvrxi)
> : [- disconnect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu64tbmnwgkq3pnz2gk6duf5sgs43dn5xg4zldoq)
> : [- isConnected](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu64tbmnwgkq3pnz2gk6duf5uxgq3pnzxgky3umvsa)
>
> **Tracking fetches**
> : [- fetchesInProgress](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu64tbmnwgkq3pnz2gk6duf5tgk5ddnbsxgslokbzg6z3smvzxg)
>
> **Returning Oracle data
> structures**
> : [- hostDataArea](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu64tbmnwgkq3pnz2gk6duf5ug643uirqxiykbojswc)
> : [- logonDataArea](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu64tbmnwgkq3pnz2gk6duf5wg6z3pnzcgc5dbifzgkyi)

## Instance Methods

---

### connect

`- (void)connect`

Opens a connection to the database server. OracleChannel
sends this message to OracleContext when it (OracleChannel) is about
to open a channel to the server.

---

### disconnect

`- (void)disconnect`

Closes a connection to the database server.
OracleChannel sends this message to OracleContext when it (OracleChannel)
has just closed a channel to the server.

---

### fetchesInProgress

`- (unsigned)fetchesInProgress`

Returns the number of fetches the receiver has
in progress.

---

### hostDataArea

`- (unsigned char *)hostDataArea`

If the channel is connected, returns an Oracle-specific
data structure describing characteristics of the context. Otherwise,
returns NULL. This method is commonly used with the OracleChannel
method raiseOracleError to determine why an error occurred.

---

### isConnected

`- (BOOL)isConnected`

Returns YES if the receiver has an open connection
to the database, NO otherwise.

---

### logonDataArea

`- (void *)logonDataArea`

If the channel is connected, returns an Oracle-specific
data structure describing characteristics of the context. Otherwise,
returns NULL. This method is commonly used with the OracleChannel
method raiseOracleError to determine why an error occurred.

---

[![Table of Contents](attachments/images/up.gif)](../OracleEOAdaptorTOC.md)
