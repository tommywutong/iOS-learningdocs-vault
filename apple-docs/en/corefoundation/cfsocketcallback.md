---
title: CFSocketCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfsocketcallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketcallback.json'
content_hash: 'sha256:e0142013066287ad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketCallBack

<sub>Type Alias</sub>

Callback invoked when certain types of activity takes place on a CFSocket object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFSocketCallBack = (CFSocket?, CFSocketCallBackType, CFData?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `s` — The CFSocket object that experienced some activity.

- `callbackType` — The type of activity detected.

- `address` — A CFData object holding the contents of a `struct sockaddr` appropriate for the protocol family of `s` (`struct sockaddr_in` or `struct sockaddr_in6`, for example), identifying the remote address to which `s` is connected. This value is `NULL` except for `kCFSocketAcceptCallBack` and `kCFSocketDataCallBack` callbacks.

- `data` — Data appropriate for the callback type. For a `kCFSocketConnectCallBack` that failed in the background, it is a pointer to an `SInt32` error code; for a `kCFSocketAcceptCallBack`, it is a pointer to a [CFSocketNativeHandle](cfsocketnativehandle.md); or for a `kCFSocketDataCallBack`, it is a CFData object containing the incoming data. In all other cases, it is `NULL`.

- `info` — The `info` member of the [CFSocketContext](cfsocketcontext.md) structure that was used when creating the CFSocket object.

## Discussion

You specify this callback when you create the CFSocket object with [CFSocketCreate](<cfsocketcreate(______________).md>), [CFSocketCreateConnectedToSocketSignature](<cfsocketcreateconnectedtosocketsignature(____________).md>), [CFSocketCreateWithNative](<cfsocketcreatewithnative(__________).md>), or [CFSocketCreateWithSocketSignature](<cfsocketcreatewithsocketsignature(__________).md>).
