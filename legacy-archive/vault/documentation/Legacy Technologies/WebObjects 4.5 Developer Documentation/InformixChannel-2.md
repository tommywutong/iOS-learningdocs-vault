---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/InformixEOAdaptor.framework/ObjC_classic/Classes/InformixChannel.html
archived_at: '2026-07-15T08:11:45.895363Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
InformixEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../InformixEOAdaptorTOC.md)

# InformixChannel

> __Inherits
> from:__  EOAdaptorChannel : NSObject

> __Declared in:__  InformixEOAdaptor/InformixChannel.h
> InformixEOAdaptor/InformixDescription.h

---

## Class Description

---

An InformixChannel represents an independent communication
channel to the database server its InformixAdaptor is connected
to. All of an InformixChannel's operations take place within the
context of transactions controlled or tracked by its InformixContext.
An InformixContext can manage multiple InformixChannels, and a channel
is associated with only one context.

The features InformixChannel adds to EOAdaptorChannel are
as follows:

- Informix-specific error handling (see [InformixChannel Delegate](InformixChannel%20Delegate.md#apple-indeerchifcuo))
- The ability to configure the fetch buffer
- The ability to read a list of table names from the database

## Method Types

---

> **Finding table names**
> : [- setInformixTableNamesSQL:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyinugc3tomvwc643forew4ztpojwws6cumfrgyzkomfwwk42tkfgdu)
> : [- informixTableNamesSQL](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyinugc3tomvwc62lomzxxe3ljpbkgcytmmvhgc3lfonjvcta)
>
> **Getting the cursor data
> area**
> : [- cursorDataArea](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyinugc3tomvwc6y3vojzw64semf2gcqlsmvqq)
>
> **Setting the isolation
> level**
> : [- informixSetIsolationTo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyinugc3tomvwc62lomzxxe3ljpbjwk5cjonxwyylunfxw4vdphi)
>
> **Setting the fetch buffer
> length**
> : [- setFetchBufferLength:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyinugc3tomvwc643fordgk5ddnbbhkztgmvzeyzlom52gqoq)
> : [- fetchBufferLength](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyinugc3tomvwc6ztforrwqqtvmztgk4smmvxgo5di)

## Instance Methods

---

### cursorDataArea

`- (struct informix_cursor *)cursorDataArea`

If the channel is connected, returns an Informix-specific
data structure describing characteristics of the channel. Otherwise,
returns NULL.

---

### fetchBufferLength

`- (unsigned)fetchBufferLength`

Returns the size, in bytes, of the fetch buffer.
The larger the buffer, the more rows can be returned for each round
trip to the server.

---

### informixSetIsolationTo:

`- (void)informixSetIsolationTo:(InformixIsolationLevel)isolationLevel`

Sets the isolation transaction level of the
connection represented by the receiver to _isolationLevel_.

---

### informixTableNamesSQL

`- (NSString *)informixTableNamesSQL`

Returns the SQL statement the receiver uses
to find table names. The user default InformixTableNamesSQL overrides
a statement set with [setInformixTableNamesSQL:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyinugc3tomvwc643forew4ztpojwws6cumfrgyzkomfwwk42tkfgdu).

---

### setFetchBufferLength:

`- (void)setFetchBufferLength:(unsigned)length`

Sets the size (in bytes) of the fetch buffer
to _length_. The larger the buffer,
the more rows can be returned for each round trip to the server.

---

### setInformixTableNamesSQL:

`- (void)setInformixTableNamesSQL:(NSString
*)sql`

Set the SQL statement the receiver uses to find
table names to _sql_.

---

[![Table of Contents](attachments/images/up.gif)](../InformixEOAdaptorTOC.md)
