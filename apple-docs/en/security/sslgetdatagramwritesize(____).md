---
title: 'SSLGetDatagramWriteSize(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.8+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslgetdatagramwritesize(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslgetdatagramwritesize(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetdatagramwritesize%28_%3A_%3A%29.json'
content_hash: 'sha256:fedf9fce8f75eda4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetDatagramWriteSize(_:_:)

<sub>Function</sub>

Provides the largest packet that the OS guarantees it can send without fragmentation.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLGetDatagramWriteSize(_ dtlsContext: SSLContext, _ bufSize: UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `dtlsContext` — The SSL context associated with the connection.

- `bufSize` — The address of a `size_t` integer for storing the length.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

Although any packet below this threshold size will not be fragmented by the OS when sent using [SSLWrite](<sslwrite(________).md>), this function provides no guarantees about whether the packet will be fragmented by routers en route. This size value is equal to the maximum Datagram Record size (set by calling [SSLSetMaxDatagramRecordSize](<sslsetmaxdatagramrecordsize(____).md>)) minus the DTLS Record header size.
