---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/InformixEOAdaptor.framework/Java/Classes/InformixContext.html
archived_at: '2026-07-15T08:11:45.788013Z'
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

> __Package:__ com.apple.yellow.informixeoadaptor

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
> : [connect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbbw63tumv4hil3dn5xg4zldoq)
> : [connection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbbw63tumv4hil3dn5xg4zldoruw63q)
> : [disconnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbbw63tumv4hil3enfzwg33onzswg5a)
> : [isConnected](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbbw63tumv4hil3jonbw63tomvrxizle)
>
> **Returning information
> about an InformixContext**
> : [fetchesInProgress](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbbw63tumv4hil3gmv2gg2dfonew4udsn5txezltom)
> : [hasTransactions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbbw63tumv4hil3imfzvi4tbnzzwcy3unfxw44y)
>
> **Returns information about
> the server**
> : [isOnLine](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbbw63tumv4hil3jonhw4tdjnzsq)

## Instance Methods

---

### connect

`public void connect()`

Opens a connection to the database server. An
InformixChannel sends this message to its InformixContext when the
channel is about to open a connection to the server.

__See
Also:__  [disconnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbbw63tumv4hil3enfzwg33onzswg5a)

---

### connection

`public int connection()`

Returns an identifier for the receiver's connection
to the server.

---

### disconnect

`public void disconnect()`

Closes a connection to the database server.
An InformixChannel sends this message to its InformixContext when
the channel is about to close a connection to the server.

__See
Also:__  [connect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbbw63tumv4hil3dn5xg4zldoq)

---

### fetchesInProgress

`public int fetchesInProgress()`

Returns the number of fetches the receiver has
in progress.

---

### hasTransactions

`public boolean hasTransactions()`

Returns true to indicate that the receiver has
transactions in process, false otherwise.

---

### isConnected

`public boolean isConnected()`

Returns true if the receiver has an open connection
to the database, false otherwise.

__See Also:__  [connect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbbw63tumv4hil3dn5xg4zldoq), [disconnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbbw63tumv4hil3enfzwg33onzswg5a)

---

### isOnLine

`public boolean isOnLine()`

Returns true if the server is an Informix online
server, false otherwise.

---

[![Table of Contents](attachments/images/up.gif)](../InformixEOAdaptorTOC.md)
