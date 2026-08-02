---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/SybaseEOAdaptor.framework/Java/Classes/SybaseContext.html
archived_at: '2026-07-15T08:11:46.434436Z'
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

> __Package:__ com.apple.yellow.sybaseeoadaptor

---

## Class Description

---

A SybaseContext represents a single transaction scope on the
database server to which its adaptor object is connected. Since
a Sybase server supports multiple concurrent transaction sessions,
the adaptor may have several adaptor contexts. A SybaseContext may
in turn have a SybaseChannel, which handles actual access to the
data on the server.

The SybaseContext can have a delegate, which gives you access
to all messages returned from the Sybase client library or from
the Sybase Server. See the [SybaseContext.Delegate](SybaseContext.Delegate.md#apple-infeiqscijcuo) interface specification for
a complete description.

## Method Types

---

> **Setting the login time
> out interval**
> : [loginTimeOutInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jxsytbonsug33oorsxq5bpnrxwo2lokruw2zkpov2es3tumvzhmylm)
> : [setLoginTimeOutInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jxsytbonsug33oorsxq5bponsxitdpm5uw4vdjnvsu65lujfxhizlsozqwy)
>
> **Setting the time out
> interval**
> : [setTimeOutInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jxsytbonsug33oorsxq5bponsxivdjnvsu65lujfxhizlsozqwy)
> : [timeOutInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jxsytbonsug33oorsxq5bporuw2zkpov2es3tumvzhmylm)
>
> **Managing the connection**
> : [connect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkdn5xhizlyoqxwg33onzswg5a)
> : [currentChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkdn5xhizlyoqxwg5lsojsw45cdnbqw43tfnq)
> : [disconnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkdn5xhizlyoqxwi2ltmnxw43tfmn2a)
> : [isConnected](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkdn5xhizlyoqxws42dn5xg4zldorswi)
> : [setMaximumConnections](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jxsytbonsug33oorsxq5bponsxitlbpbuw25lninxw43tfmn2gs33oom)
> : [maximumConnections](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jxsytbonsug33oorsxq5bpnvqxq2lnovwug33onzswg5djn5xhg)
>
> **Setting the max text
> size default**
> : [maxTextSizeDefault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkdn5xhizlyoqxw2ylykrsxq5ctnf5gkrdfmzqxk3du)
> : [setMaxTextSizeDefault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkdn5xhizlyoqxxgzlujvqxqvdfpb2fg2l2mvcgkztbovwhi)
>
> **Setting the current exception**
> : [raiseCurrentException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkdn5xhizlyoqxxeyljonsug5lsojsw45cfpbrwk4dunfxw4)
> : [setCurrentException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkdn5xhizlyoqxxgzluin2xe4tfnz2ek6ddmvyhi2lpny)

## Static Methods

---

### maximumConnections

`public static int maximumConnections()`

Returns the value for CS_MAX_CONNECT, the maximum
number of database connections a Sybase client process can have
open simultaneously.

---

### loginTimeOutInterval

`public static int loginTimeOutInterval()`

Returns the login time out interval used by
SybaseContext.

__See Also:__  [setLoginTimeOutInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jxsytbonsug33oorsxq5bponsxitdpm5uw4vdjnvsu65lujfxhizlsozqwy)

---

### setLoginTimeOutInterval

`public static void setLoginTimeOutInterval(int seconds)`

Sets the login time out interval value SybaseContext
uses during the creation of new channels. The default is 0, which
means that there is no time out.

__See Also:__  [loginTimeOutInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jxsytbonsug33oorsxq5bpnrxwo2lokruw2zkpov2es3tumvzhmylm)

---

### setMaximumConnections

`public static boolean setMaximumConnections(int value)`

Sets CS_MAX_CONNECT, the maximum number of database
connections a Sybase client process can have open simultaneously.
Returns true if the operation is successful. By default the adaptor
uses the Sybase client library default, which is normally sufficient.
However, if your application communicates with many databases or
uses database authentication for each user, you might need to raise
the limit. It is possible to raise the limit after database connections
have been opened.

---

### setTimeOutInterval

`public static void setTimeOutInterval(int seconds)`

Sets the time out interval value that the SybaseContext
uses during the creation of new channels. The default is 0, which
means that there is no time out.

__See Also:__  [timeOutInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jxsytbonsug33oorsxq5bporuw2zkpov2es3tumvzhmylm)

---

### timeOutInterval

`public static int timeOutInterval()`

Returns the time out interval used by SybaseContext.

---

## Instance Methods

---

### connect

`public void connect()`

Opens a connection to the database server. SybaseChannel
sends this message to SybaseContext when it (SybaseChannel) is about
to open a channel to the server.

__See Also:__  [disconnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkdn5xhizlyoqxwi2ltmnxw43tfmn2a)

---

### currentChannel

`public SybaseChannel currentChannel()`

Returns the SybaseChannel currently associated
with the receiving context.

---

### disconnect

`public void disconnect()`

Closes a connection to the database server.
SybaseChannel sends this message to SybaseContext when it (SybaseChannel)
has just closed a channel to the server.

__See
Also:__  [connect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkdn5xhizlyoqxwg33onzswg5a)

---

### isConnected

`public boolean isConnected()`

Returns true if the receiver has an open connection
to the database, false otherwise.

__See Also:__  [connect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkdn5xhizlyoqxwg33onzswg5a), [disconnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkdn5xhizlyoqxwi2ltmnxw43tfmn2a)

---

### maxTextSizeDefault

`public int maxTextSizeDefault()`

Returns the maximum number of bytes to be returned
from a Sybase image to text field. The default is set to INT_MAX,
as defined for the host machine. This number can be overwritten
on a per-channel basis by sending the appropriate SQL to the channel
using the evaluateExpression: method.

---

### raiseCurrentException

`public void raiseCurrentException()`

If the receiver has an exception, raises it.

__See
Also:__  [setCurrentException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkdn5xhizlyoqxxgzluin2xe4tfnz2ek6ddmvyhi2lpny)

---

### setCurrentException

`public void setCurrentException(Throwable exception)`

Sets the receiver's current exception to _exception_.

When
the SybaseAdaptor encounters an error, it uses the error message
to build an NSException and stores the exception in the SybaseContext
using this method. The exception can then be reviewed by other components
to determine if the error is fatal.

__See
Also:__  [raiseCurrentException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzkdn5xhizlyoqxxeyljonsug5lsojsw45cfpbrwk4dunfxw4)

---

### setMaxTextSizeDefault

`public void setMaxTextSizeDefault(int textSize)`

Sets the receiver's default text size to _textSize_.
Any channels created after this method has been invoked will use
the newly specified text size.

---

[![Table of Contents](attachments/images/up.gif)](../SybaseEOAdaptorTOC.md)
