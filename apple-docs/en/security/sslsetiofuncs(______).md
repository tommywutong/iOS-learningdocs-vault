---
title: 'SSLSetIOFuncs(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslsetiofuncs(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslsetiofuncs(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetiofuncs%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:3fe46fd4b6b4672f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetIOFuncs(_:_:_:)

<sub>Function</sub>

Specifies callback functions that perform the network I/O operations.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLSetIOFuncs(_ context: SSLContext, _ readFunc: SSLReadFunc, _ writeFunc: SSLWriteFunc) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `readFunc` — A pointer to your read callback function. See [SSLReadFunc](sslreadfunc.md) for information on defining this function.

- `writeFunc` — A pointer to your write callback function. See [SSLWriteFunc](sslwritefunc.md) for information on defining this function.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

Secure Transport calls your read and write callback functions to perform network I/O. You must define these functions before calling [SSLSetIOFuncs](<sslsetiofuncs(______).md>).

You must call [SSLSetIOFuncs](<sslsetiofuncs(______).md>) prior to calling the [SSLHandshake](<sslhandshake(__).md>) function. [SSLSetIOFuncs](<sslsetiofuncs(______).md>) cannot be called while a session is active.
