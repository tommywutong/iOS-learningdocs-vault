---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/OracleEOAdaptor.framework/ObjC_classic/Classes/OracleChannel.html
archived_at: '2026-07-15T08:11:46.323534Z'
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

> __Declared in:__  OracleEOAdaptor/OracleChannel.h
> OracleEOAdaptor/OracleDescription.h

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
> : [+ oracleTableNamesSQL](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5zgcy3mmvbwqylonzswyl3pojqwg3dfkrqwe3dfjzqw2zltkniuy)
> : [+ setOracleTableNamesSQL:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5zgcy3mmvbwqylonzswyl3tmv2e64tbmnwgkvdbmjwgkttbnvsxgu2rjq5a)
> : [- describeTableNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu64tbmnwgkq3imfxg4zlmf5sgk43dojuwezkumfrgyzkomfwwk4y)
>
> **Accessing the fetch buffer
> length**
> : [- fetchBufferLength](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu64tbmnwgkq3imfxg4zlmf5tgk5ddnbbhkztgmvzeyzlom52gq)
> : [- setFetchBufferLength:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu64tbmnwgkq3imfxg4zlmf5zwk5cgmv2gg2ccovtgmzlsjrsw4z3una5a)
>
> **Error handling**
> : [- raiseOracleError](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu64tbmnwgkq3imfxg4zlmf5zgc2ltmvhxeyldnrsuk4tsn5za)
> : [- cursorDataArea](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu64tbmnwgkq3imfxg4zlmf5rxk4ttn5zeiylumfaxezlb)

## Class Methods

---

### oracleTableNamesSQL

`+ (NSString *)oracleTableNamesSQL`

Returns the SQL statement that will be executed
when building a default model.

---

### setOracleTableNamesSQL:

`+ (void)setOracleTableNamesSQL:(NSString
*)sql`

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

Once you use [setOracleTableNamesSQL:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5zgcy3mmvbwqylonzswyl3tmv2e64tbmnwgkvdbmjwgkttbnvsxgu2rjq5a) to specify
a setting, it supersedes values set with the `defaults write` command.

---

## Instance Methods

---

### cursorDataArea

`- (struct cda_def *)cursorDataArea`

If the channel is connected, returns an Oracle-specific
data structure (`cda_def`)
describing characteristics of the channel. Otherwise, returns `NULL`.
This method is commonly used with the method [raiseOracleError](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu64tbmnwgkq3imfxg4zlmf5zgc2ltmvhxeyldnrsuk4tsn5za) to
determine why an error occurred.

---

### describeTableNames

`- (NSArray *)describeTableNames`

Overrides the EOAdaptorChannel implementation
to return an array of the names of all the tables owned by the current
user. Uses the SQL returned by [oracleTableNamesSQL](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5zgcy3mmvbwqylonzswyl3pojqwg3dfkrqwe3dfjzqw2zltkniuy).

---

### fetchBufferLength

`- (unsigned)fetchBufferLength`

Returns the size, in bytes, of the fetch buffer.
The larger the buffer, the more rows can be returned for each round
trip to the server.

---

### raiseOracleError

`- (void)raiseOracleError`

Examines Oracle structures for error flags and
raises an exception if one is found. The userInfo of the exception
contains the Oracle error code in an entry with the key [OracleErrorKey](OracleAdaptor-2.md#apple-ijbukq2bifauq).

---

### setFetchBufferLength:

`- (void)setFetchBufferLength:(unsigned)length`

Sets to _length_ the
size, in bytes, of the fetch buffer. The larger the buffer, the
more rows can be returned for each round trip to the server.

---

[![Table of Contents](attachments/images/up.gif)](../OracleEOAdaptorTOC.md)
