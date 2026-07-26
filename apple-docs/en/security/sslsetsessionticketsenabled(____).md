---
title: 'SSLSetSessionTicketsEnabled(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 11.0+（13.0 起废弃）, iPadOS 11.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.13+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslsetsessionticketsenabled(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslsetsessionticketsenabled(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetsessionticketsenabled%28_%3A_%3A%29.json'
content_hash: 'sha256:dfee14be2dc4bd04'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetSessionTicketsEnabled(_:_:)

<sub>Function</sub>

Enables or disables session ticket resumption.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLSetSessionTicketsEnabled(_ context: SSLContext, _ enabled: Bool) -> OSStatus
```

## Parameters

- `context` — A session context.

- `enabled` — A Boolean set to [true](../swift/true.md) to enable session ticket resumption, or [false](../swift/false.md) to disable it.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

By default, session tickets are disabled.
