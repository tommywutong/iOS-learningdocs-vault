---
title: 'SSLCreateContext(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.8+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslcreatecontext(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslcreatecontext(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslcreatecontext%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:4c20eb05ba87b557'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLCreateContext(_:_:_:)

<sub>Function</sub>

Allocates and returns a new context.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLCreateContext(_ alloc: CFAllocator?, _ protocolSide: SSLProtocolSide, _ connectionType: SSLConnectionType) -> SSLContext?
```

## Parameters

- `alloc` — The allocator to use. Pass `NULL` or [kCFAllocatorDefault](../corefoundation/kcfallocatordefault.md) to use the default allocator.

- `protocolSide` — Either [kSSLServerSide](sslprotocolside/serverside.md) or [kSSLClientSide](sslprotocolside/clientside.md).

- `connectionType` — Either [kSSLStreamType](sslconnectiontype/streamtype.md) or [kSSLDatagramType](sslconnectiontype/datagramtype.md).

## Return Value

A new context. In Objective-C, use [CFRelease](../corefoundation/cfrelease.md) to release this object’s memory when you are done with it.
