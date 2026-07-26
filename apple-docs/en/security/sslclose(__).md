---
title: 'SSLClose(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslclose(_:)'
source_url: 'https://developer.apple.com/documentation/security/sslclose(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslclose%28_%3A%29.json'
content_hash: 'sha256:e7cc4a62614d1c4e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLClose(_:)

<sub>Function</sub>

Terminates the current SSL session.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLClose(_ context: SSLContext) -> OSStatus
```

## Parameters

- `context` — The SSL session context reference of the session you want to terminate.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).
