---
title: 'CFSocketSendData(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsocketsenddata(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketsenddata(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketsenddata%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:7463d69e94112a9a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketSendData(_:_:_:_:)

<sub>Function</sub>

Sends data over a CFSocket object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketSendData(_ s: CFSocket!, _ address: CFData!, _ data: CFData!, _ timeout: CFTimeInterval) -> CFSocketError
```

## Parameters

- `s` — The CFSocket object to use.

- `address` — The address, stored as a `struct sockaddr` appropriate for the protocol family (`struct sockaddr_in` or `struct sockaddr_in6`, for example) in a CFData object, to which to send the contents of `data`. If `NULL`, the data are sent to the address to which `s` is already connected. This data object is used only for the duration of the function call.

- `data` — The data to send.

- `timeout` — The time to wait for the data to be sent.

## Return Value

An error code indicating success or failure.

## Discussion

This function sets the send timeout of the underlying socket (the `SO_SNDTIMEO` option at the `SOL_SOCKET` level), then calls send (or sendto if you provided an address) with the provided data.

This function makes no attempt to queue data for delivery beyond the queueing provided by the socket buffer itself. This means:

- If this function returns [kCFSocketSuccess](cfsocketerror/success.md), then by the time it returns, the data has been queued in the socket buffer for delivery.
- If the socket buffer is full and the timeout is nonzero, the function may return an error. If this happens, the app should wait for the socket buffer to have enough space available for writing before calling this function again.

## See Also

### Using Sockets

- [CFSocketConnectToAddress](<cfsocketconnecttoaddress(______).md>) — Opens a connection to a remote socket.
- [CFSocketCreateRunLoopSource](<cfsocketcreaterunloopsource(______).md>) — Creates a CFRunLoopSource object for a CFSocket object.
- [CFSocketGetTypeID](<cfsocketgettypeid().md>) — Returns the type identifier for the CFSocket opaque type.
- [CFSocketInvalidate](<cfsocketinvalidate(__).md>) — Invalidates a CFSocket object, stopping it from sending or receiving any more messages.
- [CFSocketIsValid](<cfsocketisvalid(__).md>) — Returns a Boolean value that indicates whether a CFSocket object is valid and able to send or receive messages.
