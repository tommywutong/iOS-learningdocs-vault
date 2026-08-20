---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Classes/WOHTTPConnection.html
archived_at: '2026-07-15T08:15:15.631004Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# WOHTTPConnection

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.appserver

---

## Class Description

---

The WOHTTPConnection class is intended to be used as a client for HTTP communications. It gives you direct access to the HTTP contents and headers. WOHTTPConnection's [sendRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsw4zcsmvyxkzltoq) method allows you to send a WORequest object directly to the server specified by the constructor's _host_ and _port_ parameters, and [readResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpojswczcsmvzxa33oonsq) allows you to receive WOResponse objects from that same server.

## Method Types

---

> **Constructing and initializing**
> : [WOHTTPConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpk5huqvcukbbw63tomvrxi2lpny)
>
> **Sending and receiving data**
> : [readResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpojswczcsmvzxa33oonsq): [sendRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsw4zcsmvyxkzltoq)
>
> **Working with connection settings**
> : [connectTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpmnxw43tfmn2fi2lnmvxxk5a): [keepAliveEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpnnswk4cbnruxmzkfnzqwe3dfmq): [receiveTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpojswgzljozsvi2lnmvxxk5a): [sendTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsw4zcunfwwk33voq): [setConnectTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiq3pnzxgky3ukruw2zlpov2a): [setKeepAliveEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxis3fmvyec3djozsuk3tbmjwgkza): [setReceiveTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiutfmnsws5tfkruw2zlpov2a): [setSendTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiu3fnzsfi2lnmvxxk5a)

## Constructors

---

### WOHTTPConnection

`public WOHTTPConnection( String hostName, int portNumber)`

Returns a WOHTTPConnection instance initialized with the specified host name and port number.

`public WOHTTPConnection ( String aHost, int portNumber, int timeOut)`

Description forthcoming.

---

## Static Methods

---

### expectContentLengthHeader

`public static void expectContentLengthHeader( boolean expectContentLengthHeader, int contentTimeout)`

This class method allows you to specify whether a content-length header is expected to accompany HTTP content, and, if a content-length header is not found, how long (in milliseconds) WOHTTPConnection should wait to determine that all HTTP content has been received. Set the first parameter to `true` and supply an appropriate timeout if a content-length header is always expected. (If a content-length header is detected, the value it specifies will be used to determine how much data to accumulate independent of the boolean parameter). If you set the first parameter to `false`, the timeout parameter is ignored and, if no content-length header is found among the HTTP content, no data will be returned when reading from the socket.

---

### socketForHostAndPortAndTimeout

`protected static java.net.Socket socketForHostAndPortAndTimeout( String host, int port, int timeout)`

Protected class method that returns a `java.net.Socket` for the provided hostname and port. This method may throw a `java.io.IOException` or a `java.net.UnknownHostException` if it is unable to create a new socket based upon the supplied hostname and port.

---

## Instance Methods

---

### connectTimeout

`public int connectTimeout()`

Returns the connection timeout interval in seconds.

__See Also:__ [receiveTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpojswgzljozsvi2lnmvxxk5a), [sendTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsw4zcunfwwk33voq), [setConnectTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiq3pnzxgky3ukruw2zlpov2a)

---

### isConnected

`public boolean isConnected()`

Description forthcoming.

---

### keepAliveEnabled

`public boolean keepAliveEnabled()`

Returns whether the socket will be left open after requests are sent.

__See Also:__ [setKeepAliveEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxis3fmvyec3djozsuk3tbmjwgkza)

---

### readResponse

`public WOResponse readResponse()`

Reads a response from the server and returns it as a WOResponse object. This method blocks until the contents of the response have been fully received. Returns `null` if an error is detected while reading or interpreting the response.

__readResponse__ sets the keep-alive enabled flag to `false` unless the response indicates that the connection should be held open.

__See Also:__ [sendRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsw4zcsmvyxkzltoq)

---

### receiveTimeout

`public int receiveTimeout()`

Returns the receive timeout interval in seconds.

__See Also:__ [connectTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpmnxw43tfmn2fi2lnmvxxk5a), [sendTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsw4zcunfwwk33voq), [setReceiveTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiutfmnsws5tfkruw2zlpov2a)

---

### sendRequest

`public boolean sendRequest(WORequest aRequest)`

Opens a socket connection to the server indicated by the receiver's host name and port number and writes _aRequest_ to that socket. Returns `true` if the socket is being held open for a subsequent invocation of __sendRequest__, or `false` if is has been closed. Use the [setKeepAliveEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxis3fmvyec3djozsuk3tbmjwgkza) method to control whether the socket is to be held open.

Throws an exception if the socket connection cannot be established.

__See Also:__ [readResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpojswczcsmvzxa33oonsq)

---

### sendTimeout

`public int sendTimeout()`

Returns the send timeout interval in seconds.

__See Also:__ [connectTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpmnxw43tfmn2fi2lnmvxxk5a), [receiveTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpojswgzljozsvi2lnmvxxk5a), [setSendTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiu3fnzsfi2lnmvxxk5a)

---

### setConnectTimeout

`public void setConnectTimeout(int timeout)`

Sets the connection timeout interval to _timeout_ seconds. The default value for this timeout is 5 seconds unless overridden by the WOHTTPConnectTimeout user default.

__See Also:__ [setReceiveTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiutfmnsws5tfkruw2zlpov2a), [setSendTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiu3fnzsfi2lnmvxxk5a)

---

### setKeepAliveEnabled

`public void setKeepAliveEnabled(boolean flag)`

Specifies according to _flag_ whether the socket is to be left open after each request has been sent so that subsequent requests don't require the socket to be re-opened.

__See Also:__ [keepAliveEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpnnswk4cbnruxmzkfnzqwe3dfmq), [readResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rpojswczcsmvzxa33oonsq), [sendRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsw4zcsmvyxkzltoq)

---

### setReceiveTimeout

`public void setReceiveTimeout(int timeout)`

Sets the receive timeout interval to _timeout_ seconds. The default value for this timeout is 30 seconds unless overridden by the WOHTTPReceiveTimeout user default.

__See Also:__ [setConnectTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiq3pnzxgky3ukruw2zlpov2a), [setSendTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiu3fnzsfi2lnmvxxk5a)

---

### setSendTimeout

`public void setSendTimeout(int timeout)`

Sets the send timeout interval to _timeout_ seconds. The default value for this timeout is 10 seconds unless overridden by the WOHTTPSendTimeout user default.

__See Also:__ [setConnectTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiq3pnzxgky3ukruw2zlpov2a), [setReceiveTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjbkfiucdn5xg4zldoruw63rponsxiutfmnsws5tfkruw2zlpov2a)

---

### toString

`public String toString()`

Returns a String containing a string representation of the receiver.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
