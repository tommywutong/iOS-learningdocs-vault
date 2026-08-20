---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/InformixEOAdaptor.framework/ObjC_classic/Classes/InformixContext.html
archived_at: '2026-07-15T08:11:45.911606Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
InformixEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../InformixEOAdaptorTOC.md)

# InformixContext

> __Inherits
> from:__  EOAdaptorContext : NSObject

> __Declared in:__  InformixEOAdaptor/InformixContext.h

---

## Class Description

---

An InformixContext represents a single transaction scope on
the database server to which its adaptor object is connected. If
the server supports multiple concurrent transaction sessions, the
adaptor may have several adaptor contexts. An InformixContext may
in turn have several InformixChannels, which handle actual access
to the data on the server.

The features the InformixContext class adds to EOAdaptorContext
are methods for setting Informix-specific characteristics for the
context.

## Method Types

---

> **Managing a connection
> to the server**
> : [- connect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyinxw45dfpb2c6y3pnzxgky3u)
> : [- connection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyinxw45dfpb2c6y3pnzxgky3unfxw4)
> : [- disconnect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyinxw45dfpb2c6zdjonrw63tomvrxi)
> : [- isConnected](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyinxw45dfpb2c62ltinxw43tfmn2gkza)
>
> **Returning information
> about an InformixContext**
> : [- fetchesInProgress](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyinxw45dfpb2c6ztforrwqzltjfxfa4tpm5zgk43t)
> : [- hasTransactions](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyinxw45dfpb2c62dbonkheyloonqwg5djn5xhg)
>
> **Returns information about
> the server**
> : [- isOnLine](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyinxw45dfpb2c62ltj5xey2lomu)

## Instance Methods

---

### connect

`- (void)connect`

Opens a connection to the database server. An
InformixChannel sends this message to its InformixContext when the
channel is about to open a connection to the server.

__See
Also:__  [- disconnect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyinxw45dfpb2c6zdjonrw63tomvrxi)

---

### connection

`- (long)connection`

Returns an identifier for the receiver's connection
to the server.

---

### disconnect

`- (void)disconnect`

Closes a connection to the database server.
An InformixChannel sends this message to its InformixContext when
the channel is about to close a connection to the server.

__See
Also:__  [- connect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyinxw45dfpb2c6y3pnzxgky3u)

---

### fetchesInProgress

`- (unsigned)fetchesInProgress`

Returns the number of fetches the receiver has
in progress.

---

### hasTransactions

`- (BOOL)hasTransactions`

Returns YES to indicate that the receiver has
transactions in process, NO otherwise.

---

### isConnected

`- (BOOL)isConnected`

Returns YES if the receiver has an open connection
to the database, NO otherwise.

__See Also:__  [- connect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyinxw45dfpb2c6y3pnzxgky3u), [- disconnect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxus3tgn5zg22lyinxw45dfpb2c6zdjonrw63tomvrxi)

---

### isOnLine

`- (BOOL)isOnLine`

Returns YES if the server is an Informix online
server, NO otherwise.

---

[![Table of Contents](attachments/images/up.gif)](../InformixEOAdaptorTOC.md)
