---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/OracleEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/OracleChannel.html
archived_at: '2026-07-18T01:28:49.452497Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/OracleEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](OracleAdaptor-2.md)
[!](OracleContext-2.md)

---

# OracleChannel

__Inherits From:__
EOAdaptorChannel : NSObject

__Declared in:__
OracleEOAdaptor/OracleChannel.h
OracleEOAdaptor/OracleDescription.h

---

## Class Description

An OracleChannel represents an independent communication channel to the database server its OracleAdaptor is connected to. All of an OracleChannel's operations take place within the context of transactions controlled or tracked by its OracleContext. An OracleContext can manage multiple OracleChannels, and a channel is associated with only one context.

The features OracleChannel adds to EOAdaptorChannel are as follows:

- Oracle-specific error handling
- The ability to configure the fetch buffer
- The ability to read a default list of table names from the database

---

## Method Types

**Setting channel characteristics**

**[+ oracleTableNamesSQL](#apple-ge2to)

**[+ setOracleTableNamesSQL:](#apple-ge3da)

**[- cursorDataArea](#apple-gi2dsni)

**[- fetchBufferLength](#apple-ge4di)

**[- setFetchBufferLength:](#apple-ge4tc)

**************

**Returning information from the server**

**[- describeModelWithTableNames:](#apple-gi2tana)

**[- describeTableNames](#apple-gi2tgoi)****

**Error handling**

**[- raiseOracleError](#apple-ge4dq)**

---

## Class Methods

---

### oracleTableNamesSQL

+ (NSString \*)__oracleTableNamesSQL__

Returns the SQL statement that will be executed when building a default model.

---

### setOracleTableNamesSQL:

+ (void)__setOracleTableNamesSQL:__ (NSString \*)_sql_

Sets to _sql_ the SQL statement that will be used to return a list of table names from the database. By default, this list is the result of the SQL statement:

> ```
> SELECT TABLE_NAME FROM USER_TABLES ORDER BY TABLE_NAME
> ```

This setting is used by all OracleChannels in an application. You can specify a different SQL statement using the __defaults write__  command, for example:

> ```
> % defaults write NSGlobalDomain OracleTableNamesSQL "SELECT TABLE_NAME FROM..."
> ```

Once you use [`setOracleTableNamesSQL:`](#apple-ge3da) to specify a setting, it supersedes values set with the __defaults write__  command.

---

## Instance Methods

---

### cursorDataArea

- (struct cda_def \*)__cursorDataArea__

If the channel is connected, returns an Oracle-specific data structure (__cda_def__ ) describing characteristics of the channel. Otherwise, returns NULL. This method is commonly used with the method [`raiseOracleError`](#apple-ge4dq) to determine why an error occurred.

---

### describeModelWithTableNames:

- (EOModel \*)__describeModelWithTableNames:__ (NSArray \*)_tableNames_

Overrides the EOAdaptorChannel method [`describeModelWithTableNames:`](#apple-gi2tana) to create and return a default model containing entities for the tables specified in _tableNames_. Assigns the adaptor name and connection dictionary to the new model. This method is typically used in conjunction with [`describeTableNames`](#apple-gi2tgoi). Raises an exception if an error occurs.

__See also:__
[- `describeTableNames`](#apple-gi2tgoi)

---

### describeTableNames

- (NSArray \*)__describeTableNames__

Overrides the EOAdaptorChannel method [`describeTableNames`](#apple-gi2tgoi) to return an array of the names of all the tables owned by the current user. Uses the SQL defined in EOOracleTableNamesSQL if it exists.

This method is used in conjunction with [`describeModelWithTableNames:`](#apple-gi2tana) to build a default model.

__See also:__
[- `describeModelWithTableNames:`](#apple-gi2tana)

---

### fetchBufferLength

- (unsigned)__fetchBufferLength__

Returns the size, in bytes, of the fetch buffer. The larger the buffer, the more rows can be returned for each round trip to the server.

__See also:__
[- `setFetchBufferLength:`](#apple-ge4tc)

---

### raiseOracleError

- (void)__raiseOracleError__

Examines Oracle structures for error flags and raises an exception if one is found. Takes an error code and converts it into an error message. This _method is invoked whenever the channel encounters an error reported by the Oracle server. This uses_ [`cursorDataArea`](#apple-gi2dsni)_,_[`hostDataArea`](OracleContext.md#apple-ge2dcoa)_, and_ [`logonDataArea`](OracleContext.md#apple-ge2dmmi) _to retrieve Oracle-specific data structures from the channel and context to determine what error has occurred. (The_ [`hostDataArea`](OracleContext.md#apple-ge2dcoa) _and_ [`logonDataArea`](OracleContext.md#apple-ge2dmmi) _methods are declared in the OracleContext class.)_

---

### setFetchBufferLength:

- (void)__setFetchBufferLength:__ (unsigned)_length_

Sets to _length_ the size, in bytes, of the fetch buffer. The larger the buffer, the more rows can be returned for each round trip to the server.

__See also:__
[- `fetchBufferLength`](#apple-ge4di)

---

[!](OracleAdaptor-2.md)
[!](OracleContext-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
