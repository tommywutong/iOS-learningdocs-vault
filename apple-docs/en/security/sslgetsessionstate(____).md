---
title: 'SSLGetSessionState(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslgetsessionstate(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslgetsessionstate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetsessionstate%28_%3A_%3A%29.json'
content_hash: 'sha256:ff7b06de2e82da3c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetSessionState(_:_:)

<sub>Function</sub>

Retrieves the state of an SSL session.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLGetSessionState(_ context: SSLContext, _ state: UnsafeMutablePointer<SSLSessionState>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `state` — On return, points to a constant that indicates the state of the SSL session. See [SSLSessionState](sslsessionstate.md) for possible values.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).
