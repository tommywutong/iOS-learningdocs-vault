---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/ODBCContext.html
archived_at: '2026-07-18T01:28:48.807886Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[ODBCEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](ODBCChannel-2.md)
[!](ODBCSQLExpression-2.md)

---

# ODBCContext

__Inherits From:__
EOAdaptorContext : NSObject

__Declared in:__
ODBCEOAdaptor/ODBCContext.h

---

## Class Description

An ODBCContext represents a single transaction scope on the database server to which its adaptor object is connected. If the server supports multiple concurrent transaction sessions, the adaptor may have several adaptor contexts. An ODBCContext may in turn have several ODBCChannels, which handle actual access to the data on the server.

The features the ODBCContext class adds to EOAdaptorContext are methods for managing ODBC connections and for getting information about the driver.

---

## Instance Methods

---

### odbcConnect

- (void)`odbcConnect`

Opens a connection to the database server. ODBCChannel sends this message to ODBCContext when it (ODBCChannel) is about to open a channel to the server. This method is called automatically by the framework.

---

### odbcDatabaseConnection

- (void \*)`odbcDatabaseConnection`

Returns the ODBC Database Connection Handle (HDBC) as a `void*`; you must cast it to HDBC to work with it.

__See also:__
- `setOdbcDatabaseConnection:`

---

### odbcDisconnect

- (void)`odbcDisconnect`

Closes the connection to the database server. ODBCChannel sends this message to ODBCContext when it (ODBCChannel) has just closed a channel to the server.

---

### setOdbcDatabaseConnection:

- (void)`setOdbcDatabaseConnection:`(void \*)_odbcDatabaseConnection_

Sets to _odbcDatabaseConnection_ the ODBC Database Connection Handle (HDBC). You can invoke this method from the delegate method `adaptorContextShouldConnect:` to set up a connection in an alternative way (by using SQLBrowseConnect(), for example).

__See also:__
- `odbcDatabaseConnection`

---

[!](ODBCChannel-2.md)
[!](ODBCSQLExpression-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
