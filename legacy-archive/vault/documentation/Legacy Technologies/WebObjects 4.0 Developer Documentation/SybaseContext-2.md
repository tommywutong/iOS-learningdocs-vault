---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/SybaseContext.html
archived_at: '2026-07-18T01:28:50.448605Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](SybaseChannel-2.md)
[!](SybaseSQLExpression-2.md)

---

# SybaseContext

__Inherits From:__
EOAdaptorContext : NSObject

__Declared in:__
SybaseEOAdaptor/SybaseContext.h

---

## Class Description

A SybaseContext represents a single transaction scope on the database server to which its adaptor object is connected. Since a Sybase server supports multiple concurrent transaction sessions, the adaptor may have several adaptor contexts. A SybaseContext may in turn have a SybaseChannel, which handles actual access to the data on the server.

The features the SybaseContext class adds to EOAdaptorContext are methods for returning Sybase-specific data structures that describe characteristics of the context. The method [`contextPointer`](#apple-gmydoma) returns the Sybase global context pointer, so that you can make direct calls to the Sybase client library. The method [`connection`](#apple-gmytqni) returns the SybaseContext's CT library connection (CS_CONNECTION \*).

The SybaseContext can have a delegate, which gives you access to all messages returned from the Sybase client library or from the Sybase Server. See the [SybaseContextDelegate](SybaseContextDelegate.md) protocol specification for a complete description. SybaseContext also provides the following callback methods for use by the SybaseChannel:

- sybaseChannelDidClose
- sybaseChannelDidEndFetching
- sybaseChannelWillBeginFetching
- sybaseChannelWillOpen

---

## Method Types

**Getting the context pointer**

**[+ contextPointer](#apple-gmydoma)**

**Setting the login time out interval**

**[+ loginTimeOutInterval](#apple-giyda)

**[+ setLoginTimeOutInterval:](#apple-giydi)****

**Setting the time out interval**

**[+ setTimeOutInterval:](#apple-giydq)

**[+ timeOutInterval](#apple-giyte)****

**Managing the connection**

**[- connect](#apple-giyto)

**[- connection](#apple-gmytqni)

**[- currentChannel](#apple-ge3tsoa)

**[- disconnect](#apple-gizdi)

**[- isConnected](#apple-gizdq)**********

**Setting the max text size default**

**[- maxTextSizeDefault](#apple-gizte)

**[- setMaxTextSizeDefault:](#apple-gi2dk)****

**Setting the current exception**

**[- raiseCurrentException](#apple-giztm)

**[- setCurrentException:](#apple-gi2da)****

---

## Class Methods

---

### contextPointer

+ (void \*)__contextPointer__

Returns the Sybase global context pointer (CS_CONTEXT \*). You can use this to make direct calls to the Sybase client library.

---

### loginTimeOutInterval

+ (int)__loginTimeOutInterval__

Returns the login time out interval used by SybaseContext.

__See also:__
[+ `setLoginTimeOutInterval:`](#apple-giydi)

---

### setLoginTimeOutInterval:

+ (void)__setLoginTimeOutInterval:__ (int)_seconds_

Sets the login time out interval value SybaseContext uses during the creation of new channels. The default is 0, which means that there is no time out.

__See also:__
[+ `loginTimeOutInterval`](#apple-giyda)

---

### setTimeOutInterval:

+ (void)__setTimeOutInterval:__ (int)_seconds_

Sets the time out interval valueSybaseContext uses during the creation of new channels. The default is 0, which means that there is no time out.

__See also:__
[+ `timeOutInterval`](#apple-giyte)

---

### timeOutInterval

+ (int)__timeOutInterval__

Returns the time out interval used by SybaseContext.

__See also:__
[+ `setTimeOutInterval:`](#apple-giydq)

---

## Instance Methods

---

### connect

- (void)__connect__

Opens a connection to the database server. SybaseChannel sends this message to SybaseContext when it (SybaseChannel) is about to open a channel to the server.

__See also:__
[- `disconnect`](#apple-gizdi)

---

### connection

- (void \*)__connection__

Returns the CT library connection (CS_CONNECTION \*) for the receiver.

---

### currentChannel

- (SybaseChannel \*)__currentChannel__

Returns the SybaseChannel currently associated with the receiving context.

---

### disconnect

- (void)__disconnect__

Closes a connection to the database server. SybaseChannel sends this message to SybaseContext when it (SybaseChannel) has just closed a channel to the server.

__See also:__
[- `connect`](#apple-giyto)

---

### isConnected

- (BOOL)__isConnected__

Returns YES if the receiver has an open connection to the database, NO otherwise.

__See also:__
[- `connect`](#apple-giyto), [- `disconnect`](#apple-gizdi)

---

### maxTextSizeDefault

- (int)__maxTextSizeDefault__

Returns the maximum number of bytes to be returned from a Sybase image to text field. The default is set to INT_MAX, as defined for the host machine. This number can be overwritten on a per-channel basis by sending the appropriate SQL to the channel using the __evaluateExpression:__  method.

__See also:__
[- `setMaxTextSizeDefault:`](#apple-gi2dk)

---

### raiseCurrentException

- (void)__raiseCurrentException__

If the receiver has an exception, raises it.

__See also:__
[- `setCurrentException:`](#apple-gi2da)

---

### setCurrentException:

- (void)__setCurrentException:__ (NSException \*)_exception_

Sets to _exception_ the receiver's current exception.

When the SybaseAdaptor encounters an error, it uses the error message to build an NSException and stores the exception in the SybaseContext using this method. The exception can then be reviewed by other components to determine if the error is fatal.

__See also:__
[- `raiseCurrentException`](#apple-giztm)

---

### setMaxTextSizeDefault:

- (void)__setMaxTextSizeDefault:__ (int)_textSize_

Sets to _textSize_ the receiver's default textsize. Any channels created after this method has been invoked will use the newly specified _textSize_.

__See also:__
[- `maxTextSizeDefault`](#apple-gizte)

---

[!](SybaseChannel-2.md)
[!](SybaseSQLExpression-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
