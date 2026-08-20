---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/OracleEOAdaptor.framework/Java/Classes/OracleChannel.html
archived_at: '2026-07-15T08:11:46.222421Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
OracleEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../OracleEOAdaptorTOC.md) 

# OracleChannel

> __Inherits
> from:__  EOAdaptorChannel : NSObject

> __Package:__ com.apple.yellow.oracleeoadaptorjava

---

## Class Description

---

An OracleChannel represents an independent communication channel
to the database server its OracleAdaptor is connected to. All of
an OracleChannel's operations take place within the context of transactions
controlled or tracked by its OracleContext. An OracleContext can
manage multiple OracleChannels, and a channel is associated with
only one context.

The features OracleChannel adds to EOAdaptorChannel are as
follows:

- Oracle-specific error handling
- The ability to configure the fetch buffer
- The ability to read a default list of table names from the
  database

## Method Types

---

> **Finding table names**
> : [oracleTableNamesSQL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hxeyldnrsug2dbnzxgk3bpn5zgcy3mmvkgcytmmvhgc3lfonjvcta)
> : [setOracleTableNamesSQL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hxeyldnrsug2dbnzxgk3bponsxit3smfrwyzkumfrgyzkomfwwk42tkfga)
> : [describeTableNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkdnbqw43tfnqxwizltmnzgsytfkrqwe3dfjzqw2zlt)
>
> **Accessing the fetch buffer
> length**
> : [fetchBufferLength](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkdnbqw43tfnqxwmzlumnuee5lgmzsxetdfnztxi2a)
> : [setFetchBufferLength](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkdnbqw43tfnqxxgzluizsxiy3iij2wmztfojggk3thorua)
>
> **Error handling**
> : [raiseOracleError](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkdnbqw43tfnqxxeyljonsu64tbmnwgkrlsojxxe)

## Static Methods

---

### oracleTableNamesSQL

`public static String oracleTableNamesSQL()`

Returns the SQL statement that will be executed
when building a default model.

---

### setOracleTableNamesSQL

`public static void setOracleTableNamesSQL(String sql)`

Sets to _sql_ the
SQL statement that will be used to return a list of table names
from the database. By default, this list is the result of the SQL
statement:SELECT TABLE_NAME FROM USER_TABLES ORDER
BY TABLE_NAME

This setting is used by all OracleChannels
in an application. You can specify a different SQL statement using
the defaults write command, for example:

% defaults
write NSGlobalDomain OracleTableNamesSQL "SELECT TABLE_NAME
FROM..."

Once you use [setOracleTableNamesSQL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hxeyldnrsug2dbnzxgk3bponsxit3smfrwyzkumfrgyzkomfwwk42tkfga) to specify
a setting, it supersedes values set with the `defaults write` command.

---

## Instance Methods

---

### describeTableNames

`public NSArray describeTableNames()`

Overrides the EOAdaptorChannel implementation
to return an array of the names of all the tables owned by the current
user. Uses the SQL returned by [oracleTableNamesSQL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hxeyldnrsug2dbnzxgk3bpn5zgcy3mmvkgcytmmvhgc3lfonjvcta).

---

### fetchBufferLength

`public int fetchBufferLength()`

Returns the size, in bytes, of the fetch buffer.
The larger the buffer, the more rows can be returned for each round
trip to the server.

---

### raiseOracleError

`public void raiseOracleError()`

Examines Oracle structures for error flags and
raises an exception if one is found. The userInfo of the exception
contains the Oracle error code in an entry with the key [OracleErrorKey](OracleAdaptor.md#apple-ijbukq2bifauq).

---

### setFetchBufferLength

`public void setFetchBufferLength(int length)`

Sets to _length_ the
size, in bytes, of the fetch buffer. The larger the buffer, the
more rows can be returned for each round trip to the server.

---

[![Table of Contents](attachments/images/up.gif)](../OracleEOAdaptorTOC.md)
