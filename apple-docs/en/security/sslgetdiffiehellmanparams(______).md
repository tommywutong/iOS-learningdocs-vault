---
title: 'SSLGetDiffieHellmanParams(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslgetdiffiehellmanparams(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslgetdiffiehellmanparams(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetdiffiehellmanparams%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:63baa9b07bc3b477'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetDiffieHellmanParams(_:_:_:)

<sub>Function</sub>

Retrieves the Diffie-Hellman parameters for a given context.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>macOS</sub>

```swift
func SSLGetDiffieHellmanParams(_ context: SSLContext, _ dhParams: UnsafeMutablePointer<UnsafeRawPointer?>, _ dhParamsLen: UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `dhParams` — On return, points to a buffer containing the Diffie-Hellman parameter block in Open SSL DER format.The returned data is not copied and belongs to the SSL session context reference; therefore, you cannot modify the data and it is released automatically when you dispose of the context.

- `dhParamsLen` — On return, points to the length of the buffer pointed to by the `dhParams` parameter.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

This function returns the parameter block specified in an earlier call to the [SSLSetDiffieHellmanParams](<sslsetdiffiehellmanparams(______).md>) function. If that function was never called, the `dhParams` parameter returns `NULL` and the `dhParamsLen` parameter returns `0`.
