---
title: 'SSLRead(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslread(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslread(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslread%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:533a060ac883f43e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLRead(_:_:_:_:)

<sub>Function</sub>

Performs a normal application-level read operation.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLRead(_ context: SSLContext, _ data: UnsafeMutableRawPointer, _ dataLength: Int, _ processed: UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `data` — On return, points to the data read. You must allocate this buffer before calling the function. The size of this buffer must be equal to or greater than the value in the `dataLength` parameter.

- `dataLength` — The amount of data you would like to read.

- `processed` — On return, points to the number of bytes actually read.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

The [SSLRead](<sslread(________).md>) function might call the [SSLReadFunc](sslreadfunc.md) function that you provide (see [SSLSetIOFuncs](<sslsetiofuncs(______).md>). Because you may configure the underlying connection to operate in a nonblocking manner, a read operation might return `errSSLWouldBlock`, indicating that less data than requested was actually transferred. In this case, you should repeat the call to [SSLRead](<sslread(________).md>) until some other result is returned.
