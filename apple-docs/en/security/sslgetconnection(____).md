---
title: 'SSLGetConnection(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslgetconnection(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslgetconnection(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetconnection%28_%3A_%3A%29.json'
content_hash: 'sha256:25420560f2a7f634'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetConnection(_:_:)

<sub>Function</sub>

Retrieves an I/O connection—such as a socket or endpoint—for a specific session.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLGetConnection(_ context: SSLContext, _ connection: UnsafeMutablePointer<SSLConnectionRef?>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `connection` — On return, a pointer to a session connection reference. If no connection has been set using the [SSLSetConnection](<sslsetconnection(____).md>) function, then this parameter is `NULL` on return.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

You can use this function on either the client or server to retrieve the connection associated with a secure session.
