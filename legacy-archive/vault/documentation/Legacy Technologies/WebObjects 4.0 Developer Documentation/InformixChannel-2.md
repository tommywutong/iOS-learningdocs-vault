---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/InformixEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/InformixChannel.html
archived_at: '2026-07-18T01:28:47.923345Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[InformixEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/InformixEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](InformixAdaptor-2.md)
[!](InformixContext-2.md)

---

# InformixChannel

__Inherits From:__
EOAdaptorChannel : NSObject

__Declared in:__
InformixEOAdaptor/InformixChannel.h
InformixEOAdaptor/InformixDescription.h

---

## Class Description

An InformixChannel represents an independent communication channel to the database server its InformixAdaptor is connected to. All of an InformixChannel's operations take place within the context of transactions controlled or tracked by its InformixContext. An InformixContext can manage multiple InformixChannels, and a channel is associated with only one context.

The features InformixChannel adds to EOAdaptorChannel are as follows:

- Informix-specific error handling
- The ability to configure the fetch buffer
- The ability to read a list of table names from the database

---

## Method Types

**Getting the cursor data area**

**[- cursorDataArea](#apple-gi4tgma)**

**Setting the isolation level**

**[- informixSetIsolationTo:](#apple-gmydini)**

**Setting the fetch buffer length**

**[- setFetchBufferLength:](#apple-g4zq)

**[- fetchBufferLength](#apple-gq4q)****

---

## Instance Methods

---

### cursorDataArea

- (struct informix_cursor \*)`cursorDataArea`

If the channel is connected, returns an Informix-specific data structure describing characteristics of the channel. Otherwise, returns NULL.

---

### fetchBufferLength

- (unsigned)`fetchBufferLength`

Returns the size, in bytes, of the fetch buffer. The larger the buffer, the more rows can be returned for each round trip to the server.

__See also:__
[- `setFetchBufferLength:`](#apple-g4zq)

---

### informixSetIsolationTo:

- (void)`informixSetIsolationTo:`(InformixIsolationLevel)_isol_

Sets to _isolationLevel_ the isolation transaction level of the connection represented by the receiver.

---

### setFetchBufferLength:

- (void)`setFetchBufferLength:`(unsigned)_length_

Sets to _length_ the size, in bytes, of the fetch buffer. The larger the buffer, the more rows can be returned for each round trip to the server.

__See also:__
[- `fetchBufferLength`](#apple-gq4q)

****

---

[!](InformixAdaptor-2.md)
[!](InformixContext-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
