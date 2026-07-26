---
title: 'SSLWrite(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslwrite(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslwrite(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslwrite%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:6a4e8fb0e0db8f4d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLWrite(_:_:_:_:)

<sub>Function</sub>

Performs a typical application-level write operation.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLWrite(_ context: SSLContext, _ data: UnsafeRawPointer?, _ dataLength: Int, _ processed: UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `data` — A pointer to the buffer of data to write.

- `dataLength` — The amount, in bytes, of data to write.

- `processed` — On return, the length, in bytes, of the data actually written.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

The [SSLWrite](<sslwrite(________).md>) function might call the [SSLWriteFunc](sslwritefunc.md) function that you provide (see [SSLSetIOFuncs](<sslsetiofuncs(______).md>)). Because you may configure the underlying connection to operate in a no-blocking manner, a write operation might return `errSSLWouldBlock`, indicating that less data than requested was actually transferred. In this case, you should repeat the call to [SSLWrite](<sslwrite(________).md>) until some other result is returned.
