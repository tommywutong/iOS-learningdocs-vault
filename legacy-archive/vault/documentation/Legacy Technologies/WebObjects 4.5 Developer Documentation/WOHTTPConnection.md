---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/Java/Classes/WOHTTPConnection.html
archived_at: '2026-07-15T08:11:46.932415Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WOHTTPConnection

> __Inherits
> from:__  NSObject

> __Package:__ com.apple.yellow.webobjects

---

## Class Description

---

The WOHTTPConnection class is intended
to be used as a client for HTTP communications. It gives you direct
access to the HTTP contents and headers. WOHTTPConnection's [sendRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsw4zcsmvyxkzltoq) method allows
you to send a WORequest object directly to the server specified
by the constructor's _host_ and _port_ parameters,
and [readResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpojswczcsmvzxa33oonsq) allows
you to receive WOResponse objects from that same server.

## Constructors

---

### WOHTTPConnection

`public WOHTTPConnection(
String hostName,
int portNumber)`

Returns a WOHTTPConnection instance initialized
with the specified host name and port number.

---

## Instance Methods

---

### connectTimeout

`public int connectTimeout()`

Returns the connection timeout interval in seconds.

__See Also:__
[receiveTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpojswgzljozsvi2lnmvxxk5a),
[sendTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsw4zcunfwwk33voq),
[setConnectTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiq3pnzxgky3ukruw2zlpov2a)

---

### keepAliveEnabled

`public boolean keepAliveEnabled()`

Returns whether the socket will be left
open after requests are sent.

__See
Also:__  [setKeepAliveEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxis3fmvyec3djozsuk3tbmjwgkza)

---

### readResponse

`public WOResponse readResponse()`

Reads a response from the server and returns
it as a WOResponse object. This method blocks until the contents
of the response have been fully received. Returns null if an error
is detected while reading or interpreting the response.

__readResponse__ sets
the keep-alive enabled flag to false unless the response indicates
that the connection should be held open.

__See
Also:__  [sendRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsw4zcsmvyxkzltoq)

---

### receiveTimeout

`public int receiveTimeout()`

Returns the receive timeout interval in seconds.

__See Also:__
[connectTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpmnxw43tfmn2fi2lnmvxxk5a),
[sendTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsw4zcunfwwk33voq),
[setReceiveTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiutfmnsws5tfkruw2zlpov2a)

---

### sendRequest

`public boolean sendRequest(WORequest aRequest)`

Opens a socket connection to the server
indicated by the receiver's host name and port number and writes _aRequest_ to
that socket. Returns true if the socket is being held open for a
subsequent invocation of __sendRequest__, or false if
is has been closed. Use the [setKeepAliveEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxis3fmvyec3djozsuk3tbmjwgkza) method to control
whether the socket is to be held open.

Throws an exception if
the socket connection cannot be established.

__See
Also:__  [readResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpojswczcsmvzxa33oonsq)

---

### sendTimeout

`public int sendTimeout()`

Returns the send timeout interval in seconds.

__See Also:__
[connectTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpmnxw43tfmn2fi2lnmvxxk5a),
[receiveTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpojswgzljozsvi2lnmvxxk5a),
[setSendTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiu3fnzsfi2lnmvxxk5a)

---

### setConnectTimeout

`public void setConnectTimeout(int timeout)`

Sets the connection timeout interval to _timeout_ in seconds. The default value for this timeout is 5 seconds unless overridden by the WOHTTPConnectTimeout user default.

__See Also:__
[setReceiveTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiutfmnsws5tfkruw2zlpov2a),
[setSendTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiu3fnzsfi2lnmvxxk5a)

---

### setKeepAliveEnabled

`public void setKeepAliveEnabled(boolean flag)`

Specifies according to _flag_ whether
the socket is to be left open after each request has been sent so
that subsequent requests don't require the socket to be re-opened.

__See
Also:__  [keepAliveEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpnnswk4cbnruxmzkfnzqwe3dfmq), [readResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpojswczcsmvzxa33oonsq), [sendRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsw4zcsmvyxkzltoq)

---

### setReceiveTimeout

`public void setReceiveTimeout(int timeout)`

Sets the receive timeout interval to _timeout_ in seconds. The default value for this timeout is 30 seconds unless overridden by the WOHTTPReceiveTimeout user default.

__See Also:__
[setConnectTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiq3pnzxgky3ukruw2zlpov2a),
[setSendTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiu3fnzsfi2lnmvxxk5a)

---

### setSendTimeout

`public void setSendTimeout(int timeout)`

Sets the send timeout interval to _timeout_ in seconds. The default value for this timeout is 10 seconds unless overridden by the WOHTTPSendTimeout user default.

__See Also:__
[setConnectTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiq3pnzxgky3ukruw2zlpov2a),
[setReceiveTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiutfmnsws5tfkruw2zlpov2a)

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
