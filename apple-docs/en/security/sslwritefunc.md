---
title: SSLWriteFunc
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sslwritefunc
source_url: 'https://developer.apple.com/documentation/security/sslwritefunc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslwritefunc.json'
content_hash: 'sha256:018da3fcb3b9702e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLWriteFunc

<sub>Type Alias</sub>

A pointer to a customized write function that secure transport calls to write data to the connection.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias SSLWriteFunc = (SSLConnectionRef, UnsafeRawPointer, UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `connection` — The SSL session connection reference.

- `data` — A pointer to the data to write to the connection.You must allocate this memory before calling this function.

- `dataLength` — Before calling, an integer representing the length of the data in bytes. On return, this is the number of bytes actually transferred.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

Before using the secure transport API, you must write the functions [SSLReadFunc](sslreadfunc.md) and [SSLWriteFunc](sslwritefunc.md) and provide them to the library by calling the [SSLSetIOFuncs](<sslsetiofuncs(______).md>) function.

You may configure the underlying connection to operate in a non-blocking manner. In that case, a write operation may well return [errSSLWouldBlock](errsslwouldblock.md), indicating less data than requested was transferred and nothing is wrong except that the requested I/O hasn’t completed. This result is returned to the caller from the functions [SSLRead](<sslread(________).md>), [SSLWrite](<sslwrite(________).md>), or [SSLHandshake](<sslhandshake(__).md>).
