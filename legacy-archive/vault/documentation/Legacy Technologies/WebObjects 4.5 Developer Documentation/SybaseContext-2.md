---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/SybaseEOAdaptor.framework/ObjC_classic/Classes/SybaseContext.html
archived_at: '2026-07-15T08:11:46.553482Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
SybaseEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../SybaseEOAdaptorTOC.md)

# SybaseContext

> __Inherits
> from:__  EOAdaptorContext : NSObject

> __Declared in:__  SybaseEOAdaptor/SybaseContext.h

---

## Class Description

---

A SybaseContext represents a single transaction scope on the
database server to which its adaptor object is connected. Since
a Sybase server supports multiple concurrent transaction sessions,
the adaptor may have several adaptor contexts. A SybaseContext may
in turn have a SybaseChannel, which handles actual access to the
data on the server.

The features the SybaseContext class adds to EOAdaptorContext
are methods for returning Sybase-specific data structures that describe
characteristics of the context. The method [contextPointer](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpkn4weyltmvbw63tumv4hil3dn5xhizlyorig62loorsxe) returns
the Sybase global context pointer, so that you can make direct calls
to the Sybase client library. The method [connection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvg6lcmfzwkq3pnz2gk6duf5rw63tomvrxi2lpny) returns the SybaseContext's
CT library connection (CS_CONNECTION \*).

The SybaseContext can have a delegate, which gives you access
to all messages returned from the Sybase client library or from
the Sybase Server. See the [SybaseContext Delegate](SybaseContext%20Delegate.md#apple-infeiqscijcuo) protocol specification for
a complete description.

## Method Types

---

> **Getting the context pointer**
> : [+ contextPointer](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpkn4weyltmvbw63tumv4hil3dn5xhizlyorig62loorsxe)
>
> **Setting the login time
> out interval**
> : [+ loginTimeOutInterval](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpkn4weyltmvbw63tumv4hil3mn5tws3sunfwwkt3vorew45dfoj3gc3a)
> : [+ setLoginTimeOutInterval:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpkn4weyltmvbw63tumv4hil3tmv2ey33hnfxfi2lnmvhxk5cjnz2gk4twmfwdu)
>
> **Setting the time out
> interval**
> : [+ setTimeOutInterval:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpkn4weyltmvbw63tumv4hil3tmv2fi2lnmvhxk5cjnz2gk4twmfwdu)
> : [+ timeOutInterval](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpkn4weyltmvbw63tumv4hil3unfwwkt3vorew45dfoj3gc3a)
>
> **Managing the connection**
> : [- connect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvg6lcmfzwkq3pnz2gk6duf5rw63tomvrxi)
> : [- connection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvg6lcmfzwkq3pnz2gk6duf5rw63tomvrxi2lpny)
> : [- currentChannel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvg6lcmfzwkq3pnz2gk6duf5rxk4tsmvxhiq3imfxg4zlm)
> : [- disconnect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvg6lcmfzwkq3pnz2gk6duf5sgs43dn5xg4zldoq)
> : [- isConnected](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvg6lcmfzwkq3pnz2gk6duf5uxgq3pnzxgky3umvsa)
> : [+ setMaximumConnections:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpkn4weyltmvbw63tumv4hil3tmv2e2ylynfwxk3kdn5xg4zldoruw63tthi)
> : [+ maximumConnections](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpkn4weyltmvbw63tumv4hil3nmf4gs3lvnvbw63tomvrxi2lpnzzq)
>
> **Setting the max text
> size default**
> : [- maxTextSizeDefault](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvg6lcmfzwkq3pnz2gk6duf5wwc6cumv4hiu3jpjsuizlgmf2wy5a)
> : [- setMaxTextSizeDefault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvg6lcmfzwkq3pnz2gk6duf5zwk5cnmf4fizlyorjws6tfirswmylvnr2du)
>
> **Setting the current exception**
> : [- raiseCurrentException](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvg6lcmfzwkq3pnz2gk6duf5zgc2ltmvbxk4tsmvxhirlymnsxa5djn5xa)
> : [- setCurrentException:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvg6lcmfzwkq3pnz2gk6duf5zwk5cdovzhezloorcxqy3fob2gs33ohi)

## Class Methods

---

### contextPointer

`+ (void *)contextPointer`

Returns the Sybase global context pointer (CS_CONTEXT
\*). You can use this to make direct calls to the Sybase client library.

---

### maximumConnections

`public static int maximumConnections()`

`+ (int)maximumConnections`

Returns the value for CS_MAX_CONNECT, the maximum
number of database connections a Sybase client process can have
open simultaneously.

---

### loginTimeOutInterval

`+ (int)loginTimeOutInterval`

Returns the login time out interval used by
SybaseContext.

__See Also:__  [+ setLoginTimeOutInterval:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpkn4weyltmvbw63tumv4hil3tmv2ey33hnfxfi2lnmvhxk5cjnz2gk4twmfwdu)

---

### setLoginTimeOutInterval:

`+ (void)setLoginTimeOutInterval:(int)seconds`

Sets the login time out interval value SybaseContext
uses during the creation of new channels. The default is 0, which
means that there is no time out.

__See Also:__  [+ loginTimeOutInterval](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpkn4weyltmvbw63tumv4hil3mn5tws3sunfwwkt3vorew45dfoj3gc3a)

---

### setMaximumConnections:

`+(BOOL)setMaximumConnections:(int)value`

Sets CS_MAX_CONNECT, the maximum number of database
connections a Sybase client process can have open simultaneously.
Returns YES if the operation is successful. By default the adaptor
uses the Sybase client library default, which is normally sufficient.
However, if your application communicates with many databases or
uses database authentication for each user, you might need to raise
the limit. It is possible to raise the limit after database connections
have been opened.

---

### setTimeOutInterval:

`+ (void)setTimeOutInterval:(int)seconds`

Sets the time out interval value that the SybaseContext
uses during the creation of new channels. The default is 0, which
means that there is no time out.

__See Also:__  [+ timeOutInterval](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpkn4weyltmvbw63tumv4hil3unfwwkt3vorew45dfoj3gc3a)

---

### timeOutInterval

`+ (int)timeOutInterval`

Returns the time out interval used by SybaseContext.

---

## Instance Methods

---

### connect

`- (void)connect`

Opens a connection to the database server. SybaseChannel
sends this message to SybaseContext when it (SybaseChannel) is about
to open a channel to the server.

__See Also:__  [- disconnect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvg6lcmfzwkq3pnz2gk6duf5sgs43dn5xg4zldoq)

---

### connection

`- (void *)connection`

Returns the CT library connection (CS_CONNECTION
\*) for the receiver.

---

### currentChannel

`- (SybaseChannel *)currentChannel`

Returns the SybaseChannel currently associated
with the receiving context.

---

### disconnect

`- (void)disconnect`

Closes a connection to the database server.
SybaseChannel sends this message to SybaseContext when it (SybaseChannel)
has just closed a channel to the server.

__See
Also:__  [- connect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvg6lcmfzwkq3pnz2gk6duf5rw63tomvrxi)

---

### isConnected

`- (BOOL)isConnected`

Returns YES if the receiver has an open connection
to the database, NO otherwise.

__See Also:__  [- connect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvg6lcmfzwkq3pnz2gk6duf5rw63tomvrxi), [- disconnect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvg6lcmfzwkq3pnz2gk6duf5sgs43dn5xg4zldoq)

---

### maxTextSizeDefault

`- (int)maxTextSizeDefault`

Returns the maximum number of bytes to be returned
from a Sybase image to text field. The default is set to INT_MAX,
as defined for the host machine. This number can be overwritten
on a per-channel basis by sending the appropriate SQL to the channel
using the evaluateExpression: method.

---

### raiseCurrentException

`- (void)raiseCurrentException`

If the receiver has an exception, raises it.

__See
Also:__  [- setCurrentException:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvg6lcmfzwkq3pnz2gk6duf5zwk5cdovzhezloorcxqy3fob2gs33ohi)

---

### setCurrentException:

`- (void)setCurrentException:(NSException
*)exception`

Sets the receiver's current exception to _exception_.

When
the SybaseAdaptor encounters an error, it uses the error message
to build an NSException and stores the exception in the SybaseContext
using this method. The exception can then be reviewed by other components
to determine if the error is fatal.

__See
Also:__  [- raiseCurrentException](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvg6lcmfzwkq3pnz2gk6duf5zgc2ltmvbxk4tsmvxhirlymnsxa5djn5xa)

---

### setMaxTextSizeDefault:

`- (void)setMaxTextSizeDefault:(int)textSize`

Sets the receiver's default text size to _textSize_.
Any channels created after this method has been invoked will use
the newly specified text size.

---

[![Table of Contents](attachments/images/up.gif)](../SybaseEOAdaptorTOC.md)
