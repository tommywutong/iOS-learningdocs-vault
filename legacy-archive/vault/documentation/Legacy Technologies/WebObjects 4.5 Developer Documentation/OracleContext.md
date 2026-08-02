---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/OracleEOAdaptor.framework/Java/Classes/OracleContext.html
archived_at: '2026-07-15T08:11:46.239845Z'
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

> __Package:__ com.apple.yellow.oracleeoadaptorjava

---

## Class Description

---

An OracleContext represents a single transaction scope on
the database server to which its adaptor object is connected. If
the server supports multiple concurrent transaction sessions, the
adaptor may have several adaptor contexts. An OracleContext may
in turn have several OracleChannels, which handle actual access
to the data on the server.

## Method Types

---

> **Managing a connection
> to the server**
> : [connect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkdn5xhizlyoqxwg33onzswg5a)
> : [disconnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkdn5xhizlyoqxwi2ltmnxw43tfmn2a)
> : [isConnected](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkdn5xhizlyoqxws42dn5xg4zldorswi)
>
> **Tracking fetches**
> : [fetchesInProgress](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkdn5xhizlyoqxwmzlumnugk42jnzihe33hojsxg4y)

## Instance Methods

---

### connect

`public void connect()`

Opens a connection to the database server. OracleChannel
sends this message to OracleContext when it (OracleChannel) is about
to open a channel to the server.

---

### disconnect

`public void disconnect()`

Closes a connection to the database server.
OracleChannel sends this message to OracleContext when it (OracleChannel)
has just closed a channel to the server.

---

### fetchesInProgress

`public int fetchesInProgress()`

Returns the number of fetches the receiver has
in progress.

---

### isConnected

`public boolean isConnected()`

Returns true if the receiver has an open connection
to the database, false otherwise.

---

[![Table of Contents](attachments/images/up.gif)](../OracleEOAdaptorTOC.md)
