---
title: acceptCallBack
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfsocketcallbacktype/acceptcallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype/acceptcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketcallbacktype/acceptcallback.json'
content_hash: 'sha256:60dab86301484ec9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFSocketCallBackType](../cfsocketcallbacktype.md)

# acceptCallBack

<sub>Type Property</sub>

New connections will be automatically accepted and the callback is called with the data argument being a pointer to a [CFSocketNativeHandle](../cfsocketnativehandle.md) of the child socket. This callback is usable only with listening sockets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var acceptCallBack: CFSocketCallBackType { get }
```

## See Also

### Constants

- [kCFSocketReadCallBack](readcallback.md) — The callback is called when data is available to be read or a new connection is waiting to be accepted. The data is not automatically read; the callback must read the data itself.
- [kCFSocketDataCallBack](datacallback.md) — Incoming data will be read in chunks in the background and the callback is called with the data argument being a CFData object containing the read data.
- [kCFSocketConnectCallBack](connectcallback.md)
- [kCFSocketWriteCallBack](writecallback.md) — The callback is called when the socket is writable. This callback type may be useful when large amounts of data are being sent rapidly over the socket and you want a notification when there is space in the kernel buffers for more data.
