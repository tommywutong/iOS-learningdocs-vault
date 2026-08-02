---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/InformixEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/InformixContext.html
archived_at: '2026-07-18T01:28:47.984659Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[InformixEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/InformixEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](InformixChannel-2.md)
[!](InformixSQLExpression-2.md)

---

# InformixContext

__Inherits From:__
EOAdaptorContext : NSObject

__Declared in:__
InformixEOAdaptor/InformixContext.h

---

## Class Description

An InformixContext represents a single transaction scope on the database server to which its adaptor object is connected. If the server supports multiple concurrent transaction sessions, the adaptor may have several adaptor contexts. An InformixContext may in turn have several InformixChannels, which handle actual access to the data on the server.

The features the InformixContext class adds to EOAdaptorContext are methods for setting Informix-specific characteristics for the context_._

---

## Method Types

**Managing a connection to the server**

**[- connect](#apple-gmza)

**[- connection](#apple-gm3a)

**[- disconnect](#apple-gq2a)

**[- isConnected](#apple-haya)********

**Returning information about an InformixContext**

**[- fetchesInProgress](#apple-gq4a)

**[- hasTransactions](#apple-gu3a)

**[- isOnLine](#apple-ha2a)******

---

## Instance Methods

---

### connect

- (void)`connect`

Opens a connection to the database server. InformixChannel sends this message to InformixContext when it (InformixChannel) is about to open a channel to the server.

__See also:__
[- `disconnect`](#apple-gq2a)

---

### connection

- (long)`connection`

Returns an identifier for the receiver's connection to the server.

---

### disconnect

- (void)`disconnect`

Closes a connection to the database server. InformixChannel sends this message to InformixContext when it (InformixChannel) has just closed a channel to the server.

__See also:__
[- `connect`](#apple-gmza)

---

### fetchesInProgress

- (unsigned)`fetchesInProgress`

Returns the number of fetches the receiver has in progress.

---

### hasTransactions

- (BOOL)`hasTransactions`

Returns YES to indicate that the receiver has transactions in process, NO otherwise.

---

### isConnected

- (BOOL)`isConnected`

Returns YES if the receiver has an open connection to the database, NO otherwise.

__See also:__
[- `connect`](#apple-gmza), [- `disconnect`](#apple-gq2a), [- `isConnected`](#apple-haya)

---

### isOnLine

- (BOOL)`isOnLine`

Returns YES if Is the server an Informix on-line server, NO otherwise.

****

---

[!](InformixChannel-2.md)
[!](InformixSQLExpression-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
