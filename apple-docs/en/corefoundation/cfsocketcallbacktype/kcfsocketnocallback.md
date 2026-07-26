---
title: kCFSocketNoCallBack
framework: Core Foundation
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfsocketcallbacktype/kcfsocketnocallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype/kcfsocketnocallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketcallbacktype/kcfsocketnocallback.json'
content_hash: 'sha256:1115fb0cc06294c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFSocketCallBackType](../cfsocketcallbacktype.md)

# kCFSocketNoCallBack

<sub>Enumeration Case</sub>

No callback should be made for any activity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
kCFSocketNoCallBack
```

## See Also

### Constants

- [kCFSocketReadCallBack](readcallback.md) — The callback is called when data is available to be read or a new connection is waiting to be accepted. The data is not automatically read; the callback must read the data itself.
- [kCFSocketAcceptCallBack](acceptcallback.md) — New connections will be automatically accepted and the callback is called with the data argument being a pointer to a [CFSocketNativeHandle](../cfsocketnativehandle.md) of the child socket. This callback is usable only with listening sockets.
- [kCFSocketDataCallBack](datacallback.md) — Incoming data will be read in chunks in the background and the callback is called with the data argument being a CFData object containing the read data.
- [kCFSocketConnectCallBack](connectcallback.md)
- [kCFSocketWriteCallBack](writecallback.md) — The callback is called when the socket is writable. This callback type may be useful when large amounts of data are being sent rapidly over the socket and you want a notification when there is space in the kernel buffers for more data.
