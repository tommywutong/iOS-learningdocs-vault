---
title: SSLReadFunc
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sslreadfunc
source_url: 'https://developer.apple.com/documentation/security/sslreadfunc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslreadfunc.json'
content_hash: 'sha256:816f6f358a8fb868'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLReadFunc

<sub>Type Alias</sub>

A pointer to a customized read function that secure transport calls to read data from the connection.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias SSLReadFunc = (SSLConnectionRef, UnsafeMutableRawPointer, UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `connection` — A connection reference.

- `data` — On return, your callback should overwrite the memory at this location with the data read from the connection.

- `dataLength` — On input, a pointer to an integer representing the length of the data in bytes. On return, your callback should overwrite that integer with the number of bytes actually transferred.

## Return Value

Your callback must return an appropriate result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

Before using the secure transport API, you must create a read function (conforming to the [SSLReadFunc](sslreadfunc.md) prototype) and a write function (conforming to  the [SSLWriteFunc](sslwritefunc.md) prototype) and provide them to the library by calling the [SSLSetIOFuncs](<sslsetiofuncs(______).md>) function.

You may configure the underlying connection to operate in a non-blocking manner; in that case, a read operation may well return [errSSLWouldBlock](errsslwouldblock.md), indicating less data than requested was transferred and nothing is wrong except that the requested I/O hasn’t completed. This result is returned to the caller from the functions [SSLRead](<sslread(________).md>), [SSLWrite](<sslwrite(________).md>), or [SSLHandshake](<sslhandshake(__).md>).
