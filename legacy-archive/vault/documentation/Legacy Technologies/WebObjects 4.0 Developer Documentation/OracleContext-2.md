---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/OracleEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/OracleContext.html
archived_at: '2026-07-18T01:28:49.525813Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/OracleEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](OracleChannel-2.md)
[!](OracleSQLExpression-2.md)

---

# OracleContext

__Inherits From:__
EOAdaptorContext : NSObject

__Declared in:__
OracleEOAdaptor/OracleContext.h

---

## Class Description

An OracleContext represents a single transaction scope on the database server to which its adaptor object is connected. If the server supports multiple concurrent transaction sessions, the adaptor may have several adaptor contexts. An OracleContext may in turn have several OracleChannels, which handle actual access to the data on the server.

The features the OracleContext class adds to EOAdaptorContext are methods for returning Oracle-specific data structures that describe characteristics of the context: __hostDataArea__  and __logonDataArea__ . __hostDataArea__  returns the __hda_def__  data structure, and __logonDataArea__  returns the __lda_def__  data structure. If you intend to extend the OracleContext by making calls to the Oracle API, you'll need these data structures.

---

## Method Types

**Managing a connection to the server**

**[- connect](#apple-geyte)

**[- disconnect](#apple-geytm)

**[- isConnected](#apple-gezdo)******

**Returning information about an OracleContext**

**[- fetchesInProgress](#apple-gezda)

**[- hostDataArea](#apple-ge2dcoa)

**[- logonDataArea](#apple-ge2dmmi)******

---

## Instance Methods

---

### connect

- (void)__connect__

Opens a connection to the database server. OracleChannel sends this message to OracleContext when it (OracleChannel) is about to open a channel to the server.

__See also:__
[- `disconnect`](#apple-geytm)

---

### disconnect

- (void)__disconnect__

Closes a connection to the database server. OracleChannel sends this message to OracleContext when it (OracleChannel) has just closed a channel to the server.

__See also:__
[- `connect`](#apple-geyte)

---

### fetchesInProgress

- (unsigned)__fetchesInProgress__

Returns the number of fetches the receiver has in progress.

---

### hostDataArea

- (unsigned char \*)__hostDataArea__

If the channel is connected, returns an Oracle-specific data structure describing characteristics of the context. Otherwise, returns NULL. This method is commonly used with the OracleChannel method __raiseOracleError__  to determine why an error occurred.

__See also:__
[- `logonDataArea`](#apple-ge2dmmi)

---

### isConnected

- (BOOL)__isConnected__

Returns YES if the receiver has an open connection to the database, NO otherwise.

__See also:__
[- `connect`](#apple-geyte), [- `disconnect`](#apple-geytm)

---

### logonDataArea

- (void \*)__logonDataArea__

If the channel is connected, returns an Oracle-specific data structure describing characteristics of the context. Otherwise, returns NULL. This method is commonly used with the OracleChannel method __raiseOracleError__  to determine why an error occurred.

__See also:__
[- `hostDataArea`](#apple-ge2dcoa)

---

### 

---

[!](OracleChannel-2.md)
[!](OracleSQLExpression-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
