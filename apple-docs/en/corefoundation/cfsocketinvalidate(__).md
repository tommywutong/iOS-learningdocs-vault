---
title: 'CFSocketInvalidate(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsocketinvalidate(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketinvalidate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketinvalidate%28_%3A%29.json'
content_hash: 'sha256:8fbcc8011b87aca8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketInvalidate(_:)

<sub>Function</sub>

Invalidates a CFSocket object, stopping it from sending or receiving any more messages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketInvalidate(_ s: CFSocket!)
```

## Parameters

- `s` — The CFSocket object to invalidate.

## Discussion

You should always invalidate a socket object when you are through using it. Invalidating a CFSocket object prevents the object from sending or receiving any more messages, but does not release the socket object itself.

If a run loop source was created for `s`, the run loop source is invalidated.

If a release callback was specified in [CFSocketContext](cfsocketcontext.md) object, this function calls it to release the object in the  `info` field (which was provided when `s` was created).

By default, this call closes the underlying socket. If you have explicitly cleared the `kCFSocketCloseOnInvalidate` flag by calling [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>), you must close the socket yourself _after_ calling this function.

## See Also

### Using Sockets

- [CFSocketConnectToAddress](<cfsocketconnecttoaddress(______).md>) — Opens a connection to a remote socket.
- [CFSocketCreateRunLoopSource](<cfsocketcreaterunloopsource(______).md>) — Creates a CFRunLoopSource object for a CFSocket object.
- [CFSocketGetTypeID](<cfsocketgettypeid().md>) — Returns the type identifier for the CFSocket opaque type.
- [CFSocketIsValid](<cfsocketisvalid(__).md>) — Returns a Boolean value that indicates whether a CFSocket object is valid and able to send or receive messages.
- [CFSocketSendData](<cfsocketsenddata(________).md>) — Sends data over a CFSocket object.
