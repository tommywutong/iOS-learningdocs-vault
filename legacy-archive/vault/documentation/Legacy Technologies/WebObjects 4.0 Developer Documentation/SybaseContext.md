---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/SybaseContext.html
archived_at: '2026-07-18T01:28:49.936903Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](SybaseChannel.md)
[!](SybaseSQLExpression.md)

---

# SybaseContext

__Inherits From:__
EOAdaptorContext : NSObject

__Inherits From:__
com.apple.yellow.sybaseeoadaptor

---

## Class Description

A SybaseContext represents a single transaction scope on the database server to which its adaptor object is connected. Since a Sybase server supports multiple concurrent transaction sessions, the adaptor may have several adaptor contexts. A SybaseContext may in turn have a SybaseChannel, which handles actual access to the data on the server.

The features the SybaseContext class adds to EOAdaptorContext are methods for returning Sybase-specific data structures that describe characteristics of the context.

The SybaseContext can have a delegate, which gives you access to all messages returned from the Sybase client library or from the Sybase Server. See the [SybaseContext.Delegate](SybaseContext.Delegate.md) interface specification for a complete description. SybaseContext also provides the following callback methods for use by the SybaseChannel:

- sybaseChannelDidClose
- sybaseChannelDidEndFetching
- sybaseChannelWillBeginFetching
- sybaseChannelWillOpen

---

## Method Types

**Setting the login time out interval**

**[loginTimeOutInterval](#apple-giyda)

**[setLoginTimeOutInterval](#apple-giydi)****

**Setting the time out interval**

**[setTimeOutInterval](#apple-giydq)

**[timeOutInterval](#apple-giyte)****

**Managing the connection**

**[connect](#apple-giyto)

**[currentChannel](#apple-ge3tsoa)

**[disconnect](#apple-gizdi)

**[isConnected](#apple-gizdq)********

**Setting the max text size default**

**[maxTextSizeDefault](#apple-gizte)

**[setMaxTextSizeDefault](#apple-gi2dk)****

**Setting the current exception**

**[raiseCurrentException](#apple-giztm)

**[setCurrentException](#apple-gi2da)****

---

## Class Methods

---

### loginTimeOutInterval

public static int `loginTimeOutInterval`()

Returns the login time out interval used by SybaseContext.

__See also:__
[`setLoginTimeOutInterval`](#apple-giydi)

---

### setLoginTimeOutInterval

public static void `setLoginTimeOutInterval`(int _seconds_)

Sets the login time out interval value SybaseContext uses during the creation of new channels. The default is 0, which means that there is no time out.

__See also:__
[`loginTimeOutInterval`](#apple-giyda)

---

### setTimeOutInterval

public static void `setTimeOutInterval`(int _seconds_)

Sets the time out interval valueSybaseContext uses during the creation of new channels. The default is 0, which means that there is no time out.

__See also:__
[`timeOutInterval`](#apple-giyte)

---

### timeOutInterval

public static int `timeOutInterval`()

Returns the time out interval used by SybaseContext.

__See also:__
[`setTimeOutInterval`](#apple-giydq)

---

## Instance Methods

---

### connect

public void `connect`()

Opens a connection to the database server. SybaseChannel sends this message to SybaseContext when it (SybaseChannel) is about to open a channel to the server.

__See also:__
[`disconnect`](#apple-gizdi)

---

### currentChannel

public SybaseChannel `currentChannel`()

Returns the SybaseChannel currently associated with the receiving context.

---

### disconnect

public void `disconnect`()

Closes a connection to the database server. SybaseChannel sends this message to SybaseContext when it (SybaseChannel) has just closed a channel to the server.

__See also:__
[`connect`](#apple-giyto)

---

### isConnected

public boolean `isConnected`()

Returns YES if the receiver has an open connection to the database, NO otherwise.

__See also:__
[`connect`](#apple-giyto), [`disconnect`](#apple-gizdi)

---

### maxTextSizeDefault

public int `maxTextSizeDefault`()

Returns the maximum number of bytes to be returned from a Sybase image to text field. The default is set to INT_MAX, as defined for the host machine. This number can be overwritten on a per-channel basis by sending the appropriate SQL to the channel using the __evaluateExpression:__  method.

__See also:__
[`setMaxTextSizeDefault`](#apple-gi2dk)

---

### raiseCurrentException

public void `raiseCurrentException`()

If the receiver has an exception, raises it.

__See also:__
[`setCurrentException`](#apple-gi2da)

---

### setCurrentException

public void `setCurrentException`(java.lang.Throwable _exception_)

Sets to _exception_ the receiver's current exception.

When the SybaseAdaptor encounters an error, it uses the error message to build an NSException and stores the exception in the SybaseContext using this method. The exception can then be reviewed by other components to determine if the error is fatal.

__See also:__
[`raiseCurrentException`](#apple-giztm)

---

### setMaxTextSizeDefault

public void `setMaxTextSizeDefault`(int _textSize_)

Sets to _textSize_ the receiver's default textsize. Any channels created after this method has been invoked will use the newly specified _textSize_.

__See also:__
[`maxTextSizeDefault`](#apple-gizte)

---

[!](SybaseChannel.md)
[!](SybaseSQLExpression.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
