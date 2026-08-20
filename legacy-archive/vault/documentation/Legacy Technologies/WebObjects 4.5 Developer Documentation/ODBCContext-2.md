---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/ODBCEOAdaptor.framework/ObjC_classic/Classes/ODBCContext.html
archived_at: '2026-07-15T08:11:46.135961Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
ODBCEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../ODBCEOAdaptorTOC.md) 

# ODBCContext

> __Inherits
> from:__  EOAdaptorContext : NSObject

> __Declared in:__  ODBCEOAdaptor/ODBCContext.h

---

## Class Description

---

An ODBCContext represents a single transaction scope on the
database server to which its adaptor object is connected. If the
server supports multiple concurrent transaction sessions, the adaptor
may have several adaptor contexts. An ODBCContext may in turn have
several ODBCChannels, which handle actual access to the data on
the server.

The features the ODBCContext class adds to EOAdaptorContext
are methods for managing ODBC connections and for getting information
about the driver.

## Instance Methods

---

### odbcConnect

`- (void)odbcConnect`

Opens a connection to the database server. ODBCChannel
sends this message to ODBCContext when it (ODBCChannel) is about
to open a channel to the server. This method is called automatically
by the framework.

---

### odbcDatabaseConnection

`- (void *)odbcDatabaseConnection`

Returns the ODBC Database Connection Handle
(HDBC) as a __void\*__; you must cast it to
HDBC to work with it.

---

### odbcDisconnect

`- (void)odbcDisconnect`

Closes the connection to the database server.
ODBCChannel sends this message to ODBCContext when it (ODBCChannel)
has just closed a channel to the server.

---

### odbcDriverInfo

`- (NSDictionary *)odbcDriverInfo`

Returns a dictionary summarizing some important
information about the driver (driver name, version, support of NOT
NULL, and so on). Connects to the database if a connection isn't
already in place.

---

### setOdbcDatabaseConnection:

`- (void)setOdbcDatabaseConnection:(void
*)odbcDatabaseConnection`

Sets to _odbcDatabaseConnection_ the
ODBC Database Connection Handle (HDBC). You can invoke this method
from the delegate method __adaptorContextShouldConnect:__ to
set up a connection in an alternative way (by using `SQLBrowseConnect()`,
for example).

---

[![Table of Contents](attachments/images/up.gif)](../ODBCEOAdaptorTOC.md)
