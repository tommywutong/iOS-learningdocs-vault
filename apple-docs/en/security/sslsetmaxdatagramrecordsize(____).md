---
title: 'SSLSetMaxDatagramRecordSize(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.8+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslsetmaxdatagramrecordsize(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslsetmaxdatagramrecordsize(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetmaxdatagramrecordsize%28_%3A_%3A%29.json'
content_hash: 'sha256:f67331714268701c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetMaxDatagramRecordSize(_:_:)

<sub>Function</sub>

Sets the maximum datagram record size allowed by the application for a given context.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLSetMaxDatagramRecordSize(_ dtlsContext: SSLContext, _ maxSize: Int) -> OSStatus
```

## Parameters

- `dtlsContext` — The SSL context associated with the connection.

- `maxSize` — The length value.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

The size you indicate includes all Datagram Transport Layer Security (DTLS) headers.

You can specify a new value up to the maximum size of a UDP packet (which, in turn, is based on the underlying IP protocol).
