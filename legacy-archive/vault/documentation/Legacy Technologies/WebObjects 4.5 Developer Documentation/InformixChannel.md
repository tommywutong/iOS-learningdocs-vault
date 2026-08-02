---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/InformixEOAdaptor.framework/Java/Classes/InformixChannel.html
archived_at: '2026-07-15T08:11:45.768460Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
InformixEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../InformixEOAdaptorTOC.md)

# InformixChannel

> __Inherits
> from:__  EOAdaptorChannel : NSObject

> __Package:__ com.apple.yellow.informixeoadaptor

---

## Class Description

---

An InformixChannel represents an independent communication
channel to the database server its InformixAdaptor is connected
to. All of an InformixChannel's operations take place within the
context of transactions controlled or tracked by its InformixContext.
An InformixContext can manage multiple InformixChannels, and a channel
is associated with only one context.

The features InformixChannel adds to EOAdaptorChannel are
as follows:

- Informix-specific error handling (see [InformixChannel.Delegate](InformixChannel.Delegate.md#apple-indeerchifcuo))
- The ability to configure the fetch buffer
- The ability to read a list of table names from the database

## Method Types

---

> **Finding table names**
> : [setInformixTableNamesSQL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbbwqylonzswyl3tmv2es3tgn5zg22lykrqwe3dfjzqw2zltkniuy)
> : [informixTableNamesSQL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbbwqylonzswyl3jnztg64tnnf4fiylcnrsu4ylnmvzvgukm)
>
> **Setting the fetch buffer
> length**
> : [setFetchBufferLength](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbbwqylonzswyl3tmv2emzlumnuee5lgmzsxetdfnztxi2a)
> : [fetchBufferLength](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbbwqylonzswyl3gmv2gg2ccovtgmzlsjrsw4z3una)

## Instance Methods

---

### fetchBufferLength

`public int fetchBufferLength()`

Returns the size, in bytes, of the fetch buffer.
The larger the buffer, the more rows can be returned for each round
trip to the server.

---

### informixTableNamesSQL

`public String informixTableNamesSQL()`

Returns the SQL statement the receiver uses
to find table names. The user default InformixTableNamesSQL overrides
a statement set with [setInformixTableNamesSQL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6slomzxxe3ljpbbwqylonzswyl3tmv2es3tgn5zg22lykrqwe3dfjzqw2zltkniuy).

---

### setFetchBufferLength

`public void setFetchBufferLength(int length)`

Sets the size (in bytes) of the fetch buffer
to _length_. The larger the buffer,
the more rows can be returned for each round trip to the server.

---

### setInformixTableNamesSQL

`public void setInformixTableNamesSQL(String sql)`

Set the SQL statement the receiver uses to find
table names to _sql_.

---

[![Table of Contents](attachments/images/up.gif)](../InformixEOAdaptorTOC.md)
