---
title: 'SSLGetNumberSupportedCiphers(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslgetnumbersupportedciphers(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslgetnumbersupportedciphers(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetnumbersupportedciphers%28_%3A_%3A%29.json'
content_hash: 'sha256:02fae4c2564aea32'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetNumberSupportedCiphers(_:_:)

<sub>Function</sub>

Determines the number of cipher suites supported.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLGetNumberSupportedCiphers(_ context: SSLContext, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `numCiphers` — On return, points to the number of supported cipher suites.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

You use the number of enabled cipher suites returned by this function when you call the [SSLGetNumberSupportedCiphers](<sslgetnumbersupportedciphers(____).md>) function to retrieve the list of currently enabled cipher suites.
