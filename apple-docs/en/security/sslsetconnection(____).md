---
title: 'SSLSetConnection(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslsetconnection(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslsetconnection(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetconnection%28_%3A_%3A%29.json'
content_hash: 'sha256:f030f2bbdb747ea2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetConnection(_:_:)

<sub>Function</sub>

Specifies an I/O connection for a specific session.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLSetConnection(_ context: SSLContext, _ connection: SSLConnectionRef?) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `connection` — An SSL session connection reference. The connection data is opaque to Secure Transport; you can set it to any value that your application can use to uniquely identify the connection in the callback functions [SSLReadFunc](sslreadfunc.md) and [SSLWriteFunc](sslwritefunc.md).

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

You must establish a connection before creating a secure session. After calling the [SSLCreateContext](<sslcreatecontext(______).md>) function to create an SSL session context, you call the [SSLSetConnection](<sslsetconnection(____).md>) function to specify the connection to which the context applies. You specify a value in the `connection` parameter that your callback routines can use to identify the connection. This value might be a pointer to a socket (if you are using the Sockets API) or an endpoint (if you are using Open Transport). For example, you might create a socket, start a connection on it, create a context reference, cast the socket to an [SSLConnectionRef](sslconnectionref.md), and then pass both the context reference and connection reference to the [SSLSetConnection](<sslsetconnection(____).md>) function.

Note that the Sockets API is the preferred networking interface for new development.

On the client side, it’s assumed that communication has been established with the desired server on this connection. On the server side, it’s assumed that a connection has been established in response to an incoming client request .

This function must be called prior to the [SSLHandshake](<sslhandshake(__).md>) function; consequently, this function can be called only when no session is active.
