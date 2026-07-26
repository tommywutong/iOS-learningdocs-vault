---
title: 'SSLGetEnabledCiphers(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslgetenabledciphers(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslgetenabledciphers(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetenabledciphers%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:d65c1fd2829734ed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetEnabledCiphers(_:_:_:)

<sub>Function</sub>

Determines which SSL cipher suites are currently enabled.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLGetEnabledCiphers(_ context: SSLContext, _ ciphers: UnsafeMutablePointer<SSLCipherSuite>, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `ciphers` — On return, points to the enabled cipher suites. Before calling, you must allocate this buffer using the number of enabled cipher suites retrieved from a call to the [SSLGetNumberEnabledCiphers](<sslgetnumberenabledciphers(____).md>) function.

- `numCiphers` — Pointer to the number of enabled cipher suites. Before calling, retrieve this value by calling the [SSLGetNumberEnabledCiphers](<sslgetnumberenabledciphers(____).md>) function.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md). If the supplied buffer is too small, [errSSLBufferOverflow](errsslbufferoverflow.md) is returned.

## Discussion

Call the [SSLSetEnabledCiphers](<sslsetenabledciphers(______).md>) function to specify which SSL cipher suites are enabled.
