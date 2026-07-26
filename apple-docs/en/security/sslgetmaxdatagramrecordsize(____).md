---
title: 'SSLGetMaxDatagramRecordSize(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.8+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslgetmaxdatagramrecordsize(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslgetmaxdatagramrecordsize(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetmaxdatagramrecordsize%28_%3A_%3A%29.json'
content_hash: 'sha256:978e150a8b121647'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetMaxDatagramRecordSize(_:_:)

<sub>Function</sub>

Obtains the maximum datagram record size allowed by the application for a given context.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLGetMaxDatagramRecordSize(_ dtlsContext: SSLContext, _ maxSize: UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `dtlsContext` — The SSL context associated with the connection.

- `maxSize` — The address of a `size_t` integer for storing the length.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

The returned size includes all Datagram Transport Layer Security (DTLS) headers.

You can specify a new size by calling [SSLSetMaxDatagramRecordSize](<sslsetmaxdatagramrecordsize(____).md>), up to the maximum size of a UDP packet (which, in turn, is based on the underlying IP protocol).
