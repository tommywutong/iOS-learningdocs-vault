---
title: 'SSLGetSupportedCiphers(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslgetsupportedciphers(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslgetsupportedciphers(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetsupportedciphers%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:66e9440aebef9878'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetSupportedCiphers(_:_:_:)

<sub>Function</sub>

Determines the values of the supported cipher suites.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLGetSupportedCiphers(_ context: SSLContext, _ ciphers: UnsafeMutablePointer<SSLCipherSuite>, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `ciphers` — On return, points to the values of the supported cipher suites. Before calling, you must allocate this buffer using the number of supported cipher suites retrieved from a call to the [SSLGetNumberSupportedCiphers](<sslgetnumbersupportedciphers(____).md>) function.

- `numCiphers` — Points to the number of supported cipher suites that you want returned. Before calling, retrieve this value by calling the [SSLGetNumberSupportedCiphers](<sslgetnumbersupportedciphers(____).md>) function.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md). If the supplied buffer is too small, [errSSLBufferOverflow](errsslbufferoverflow.md) is returned.

## Discussion

All the supported cipher suites are enabled by default. Use the [SSLSetEnabledCiphers](<sslsetenabledciphers(______).md>) function to enable a subset of the supported cipher suites. Use the [SSLGetEnabledCiphers](<sslgetenabledciphers(______).md>) function to determine which cipher suites are currently enabled.
