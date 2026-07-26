---
title: 'SSLSetEnabledCiphers(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslsetenabledciphers(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslsetenabledciphers(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetenabledciphers%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:52270ec6f911c218'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetEnabledCiphers(_:_:_:)

<sub>Function</sub>

Specifies a restricted set of SSL cipher suites to be enabled by the current SSL session context.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLSetEnabledCiphers(_ context: SSLContext, _ ciphers: UnsafePointer<SSLCipherSuite>, _ numCiphers: Int) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `ciphers` — A pointer to the cipher suites to enable.

- `numCiphers` — The number of cipher suites to enable.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

You can call this function, for example, to limit cipher suites to those that use exportable key sizes or to those supported by a particular protocol version.

This function can be called only when no session is active. The default set of enabled cipher suites is the complete set of supported cipher suites obtained by calling the [SSLGetSupportedCiphers](<sslgetsupportedciphers(______).md>) function.

Call the [SSLGetEnabledCiphers](<sslgetenabledciphers(______).md>) function to determine which SSL cipher suites are currently enabled.
