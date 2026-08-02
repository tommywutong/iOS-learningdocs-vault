---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/ODBCEOAdaptor.framework/Java/Classes/ODBCChannel.html
archived_at: '2026-07-15T08:11:46.031838Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
ODBCEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../ODBCEOAdaptorTOC.md) 

# ODBCChannel

> __Inherits
> from:__  EOAdaptorChannel : NSObject

> __Package:__ com.apple.yellow.odbceoadaptor

---

## Class Description

---

An ODBCChannel represents an independent communication channel
to the database server its ODBCAdaptor is connected to. All of an
ODBCChannel's operations take place within the context of transactions
controlled or tracked by its ODBCContext. An ODBCContext can manage
multiple ODBCChannels, and a channel is associated with only one
context.

The feature ODBCChannel adds to EOAdaptorChannel is a method
for returning a dictionary-formatted result from `SQLTypeInfo()`.

## Instance Methods

---

### closeChannel

`public void closeChannel()`

Overrides the EOAdaptorChannel method __closeChannel__ to
close the channel so that it can't perform operations with the
server. Any fetch in progress is canceled. This method has the side
effect of closing the receiver's adaptor context's connection
with the database if the receiver is its adaptor context's last open
channel.

---

### odbcTypeInfo

`public NSDictionary odbcTypeInfo()`

Returns the result from `SQLTypeInfo()`,
formatted in an NSDictionary ready to incorporate into a model file.

---

[![Table of Contents](attachments/images/up.gif)](../ODBCEOAdaptorTOC.md)
