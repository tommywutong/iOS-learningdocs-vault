---
title: 'SSLGetSessionOption(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.6+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslgetsessionoption(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslgetsessionoption(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetsessionoption%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:03e695a31fef01f9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetSessionOption(_:_:_:)

<sub>Function</sub>

Indicates the current setting of Secure Sockets Layer (SSL) session options.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLGetSessionOption(_ context: SSLContext, _ option: SSLSessionOption, _ value: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `option` — An SSL session option. Possible values are listed in [SSLSessionOption](sslsessionoption.md).

- `value` — On return, `true` if the option is enabled, or `false` otherwise.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).
