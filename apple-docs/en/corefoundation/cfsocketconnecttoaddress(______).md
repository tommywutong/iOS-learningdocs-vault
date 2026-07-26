---
title: 'CFSocketConnectToAddress(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsocketconnecttoaddress(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketconnecttoaddress(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketconnecttoaddress%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:d869ff8787b1eaec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketConnectToAddress(_:_:_:)

<sub>Function</sub>

Opens a connection to a remote socket.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketConnectToAddress(_ s: CFSocket!, _ address: CFData!, _ timeout: CFTimeInterval) -> CFSocketError
```

## Parameters

- `s` — The CFSocket object with which to connect to `address`.

- `address` — A CFData object containing a `struct sockaddr` appropriate for the protocol family of `s` (`struct sockaddr_in` or `struct sockaddr_in6`, for example), indicating the remote address to which to connect. This data object is used only for the duration of the function call.

- `timeout` — The time to wait for a connection to succeed. If a negative value is used, this function does not wait for the connection and instead lets the connection attempt happen in the background. If `s` requested a `kCFSocketConnectCallBack`, you will receive a callback when the background connection succeeds or fails.

## Return Value

An error code indicating success or failure of the connection attempt.

## See Also

### Using Sockets

- [CFSocketCreateRunLoopSource](<cfsocketcreaterunloopsource(______).md>) — Creates a CFRunLoopSource object for a CFSocket object.
- [CFSocketGetTypeID](<cfsocketgettypeid().md>) — Returns the type identifier for the CFSocket opaque type.
- [CFSocketInvalidate](<cfsocketinvalidate(__).md>) — Invalidates a CFSocket object, stopping it from sending or receiving any more messages.
- [CFSocketIsValid](<cfsocketisvalid(__).md>) — Returns a Boolean value that indicates whether a CFSocket object is valid and able to send or receive messages.
- [CFSocketSendData](<cfsocketsenddata(________).md>) — Sends data over a CFSocket object.
