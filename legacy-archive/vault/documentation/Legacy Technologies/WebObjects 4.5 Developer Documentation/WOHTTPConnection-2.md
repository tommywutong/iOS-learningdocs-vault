---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/WOHTTPConnection.html
archived_at: '2026-07-15T08:11:47.611431Z'
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

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  WebObjects/WOHTTPConnection.h

---

## Class Description

---

The WOHTTPConnection class is intended
to be used as a client for HTTP communications. It gives you direct
access to the HTTP contents and headers. WOHTTPConnection's [sendRequest:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3tmvxgiutfof2wk43uhi) method allows
you to send a WORequest object directly to the server specified
by the init method's _host_ and _port_ parameters,
and [readResponse](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3smvqwiutfonyg63ttmu) allows
you to receive WOResponse objects from that same server.

## Instance Methods

---

### connectTimeout

`- (int)connectTimeout`

Returns the connection timeout interval in seconds.

__See Also:__
[- receiveTimeout](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3smvrwk2lwmvkgs3lfn52xi),
[- sendTimeout](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3tmvxgivdjnvsw65lu),
[- setConnectTimeout:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3tmv2eg33onzswg5cunfwwk33voq5a)

---

### initWithHost:onPort:

`- (id)initWithHost:(NSString*)hostName
onPort:(unsigned int)portNumber`

Initializes a WOHTTPConnection instance with
the specified host name and port number.

---

### keepAliveEnabled

`- (BOOL)keepAliveEnabled`

Returns whether the socket will be left
open after requests are sent.

__See
Also:__  [- setKeepAliveEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3tmv2ewzlfobawy2lwmvcw4ylcnrswioq)

---

### readResponse

`- (WOResponse *)readResponse`

Reads a response from the server and returns
it as a WOResponse object. This method blocks until the contents
of the response have been fully received. Returns nil if an error
is detected while reading or interpreting the response.

__readResponse__ sets
the keep-alive enabled flag to NO unless the response indicates
that the connection should be held open.

__See
Also:__  [- sendRequest:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3tmvxgiutfof2wk43uhi)

---

### receiveTimeout

`- (int)receiveTimeout`

Returns the receive timeout interval in seconds.

__See Also:__
[- connectTimeout](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3dn5xg4zldorkgs3lfn52xi),
[- sendTimeout](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3tmvxgivdjnvsw65lu),
[- setReceiveTimeout:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3tmv2fezldmvuxmzkunfwwk33voq5a)

---

### sendRequest:

`- (BOOL)sendRequest:(WORequest*)aRequest`

Opens a socket connection to the server
indicated by the receiver's host name and port number and writes _aRequest_ to
that socket. Returns YES if the socket is being held open for a
subsequent invocation of __sendRequest:__,
or NO if is has been closed. Use the [setKeepAliveEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3tmv2ewzlfobawy2lwmvcw4ylcnrswioq) method to control
whether the socket is to be held open.

Raises an NSGenericException if
the socket connection cannot be established.

__See
Also:__  [- readResponse](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3smvqwiutfonyg63ttmu)

---

### sendTimeout

`- (int)sendTimeout`

Returns the send timeout interval in seconds.

__See Also:__
[- connectTimeout](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3dn5xg4zldorkgs3lfn52xi),
[- receiveTimeout](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3smvrwk2lwmvkgs3lfn52xi),
[- setSendTimeout:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3tmv2fgzlomrkgs3lfn52xioq)

---

### setConnectTimeout:

`- (void)setConnectTimeout:(int)timeout`

Sets the connection timeout interval to _timeout_ seconds. The default value for this timeout is 5 seconds unless overridden by the WOHTTPConnectTimeout user default.

__See Also:__
[- setReceiveTimeout:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3tmv2fezldmvuxmzkunfwwk33voq5a),
[- setSendTimeout:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3tmv2fgzlomrkgs3lfn52xioq)

---

### setKeepAliveEnabled:

`- (void)setKeepAliveEnabled:(BOOL)flag`

Specifies according to _flag_ whether
the socket is to be left open after each request has been sent so
that subsequent requests don't require the socket to be re-opened.

__See
Also:__  [- keepAliveEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3lmvsxaqlmnf3gkrlomfrgyzle), [- readResponse](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3smvqwiutfonyg63ttmu), [- sendRequest:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3tmvxgiutfof2wk43uhi)

---

### setReceiveTimeout:

`- (void)setReceiveTimeout:(int)timeout`

Sets the receive timeout interval to _timeout_ seconds. The default value for this timeout is 30 seconds unless overridden by the WOHTTPReceiveTimeout user default.

__See Also:__
[- setConnectTimeout:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3tmv2eg33onzswg5cunfwwk33voq5a),
[- setSendTimeout:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3tmv2fgzlomrkgs3lfn52xioq)

---

### setSendTimeout:

`- (void)setSendTimeout:(int)timeout`

Sets the send timeout interval to _timeout_ seconds. The default value for this timeout is 10 seconds unless overridden by the WOHTTPSendTimeout user default.

__See Also:__
[- setConnectTimeout:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3tmv2eg33onzswg5cunfwwk33voq5a),
[- setReceiveTimeout:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2ikrkfaq3pnzxgky3unfxw4l3tmv2fezldmvuxmzkunfwwk33voq5a)

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
