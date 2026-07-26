---
title: 'SSLGetBufferedReadSize(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslgetbufferedreadsize(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslgetbufferedreadsize(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetbufferedreadsize%28_%3A_%3A%29.json'
content_hash: 'sha256:af2ac7b50d637922'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetBufferedReadSize(_:_:)

<sub>Function</sub>

Determines how much data is available to be read.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLGetBufferedReadSize(_ context: SSLContext, _ bufferSize: UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `bufferSize` — On return, the size of the data to be read.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

This function determines how much data you can be guaranteed to obtain in a call to the [SSLRead](<sslread(________).md>) function. This function does not block or cause any low-level read operations to occur.
