---
title: 'SSLSetError(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 11.0+（13.0 起废弃）, iPadOS 11.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.13+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslseterror(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslseterror(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslseterror%28_%3A_%3A%29.json'
content_hash: 'sha256:cc75dc782d4c2b5c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetError(_:_:)

<sub>Function</sub>

Sets the status of a session context.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLSetError(_ context: SSLContext, _ status: OSStatus) -> OSStatus
```

## Parameters

- `context` — A session context.

- `status` — A status result for the context, not to be confused with the return result of this function call. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Return Value

A result code that represents the outcome of this function call, not to be confused with the `status` parameter. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

Call this function after handling the steps of an SSL handshake, such as server certificate validation.
