---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/ODBCContext.html
archived_at: '2026-07-18T01:28:48.440826Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[ODBCEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](ODBCChannel.md)
[!](ODBCSQLExpression.md)

---

# ODBCContext

__Inherits From:__
EOAdaptorContext : NSObject

__Inherits From:__
com.apple.yellow.odbceoadaptor

---

## Class Description

An ODBCContext represents a single transaction scope on the database server to which its adaptor object is connected. If the server supports multiple concurrent transaction sessions, the adaptor may have several adaptor contexts. An ODBCContext may in turn have several ODBCChannels, which handle actual access to the data on the server.

The features the ODBCContext class adds to EOAdaptorContext are methods for managing ODBC connections and for getting information about the driver.

---

## Instance Methods

---

### odbcConnect

public void `odbcConnect`()

Opens a connection to the database server. ODBCChannel sends this message to ODBCContext when it (ODBCChannel) is about to open a channel to the server. This method is called automatically by the framework.

---

### odbcDisconnect

public void `odbcDisconnect`()

Closes the connection to the database server. ODBCChannel sends this message to ODBCContext when it (ODBCChannel) has just closed a channel to the server.

---

[!](ODBCChannel.md)
[!](ODBCSQLExpression.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
