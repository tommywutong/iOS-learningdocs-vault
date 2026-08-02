---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/OracleEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/OracleContext.html
archived_at: '2026-07-18T01:28:49.159060Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/OracleEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](OracleChannel.md)
[!](OracleSQLExpression.md)

---

# OracleContext

__Inherits From:__
EOAdaptorContext : NSObject

__Inherits From:__
com.apple.yellow.oracleeoadaptorjava

---

## Class Description

An OracleContext represents a single transaction scope on the database server to which its adaptor object is connected. If the server supports multiple concurrent transaction sessions, the adaptor may have several adaptor contexts. An OracleContext may in turn have several OracleChannels, which handle actual access to the data on the server.

---

## Method Types

**Managing a connection to the server**

**[connect](#apple-geyte)

**[disconnect](#apple-geytm)

**[isConnected](#apple-gezdo)******

**Returning information about an OracleContext**

**[fetchesInProgress](#apple-gezda)**

---

## Instance Methods

---

### connect

public void `connect`()

Opens a connection to the database server. OracleChannel sends this message to OracleContext when it (OracleChannel) is about to open a channel to the server.

__See also:__
[`disconnect`](#apple-geytm)

---

### disconnect

public void `disconnect`()

Closes a connection to the database server. OracleChannel sends this message to OracleContext when it (OracleChannel) has just closed a channel to the server.

__See also:__
[`connect`](#apple-geyte)

---

### fetchesInProgress

public int `fetchesInProgress`()

Returns the number of fetches the receiver has in progress.

---

### isConnected

public boolean `isConnected`()

Returns `true` if the receiver has an open connection to the database, `false` otherwise.

__See also:__
[`connect`](#apple-geyte), [`disconnect`](#apple-geytm)

---

### 

---

[!](OracleChannel.md)
[!](OracleSQLExpression.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
