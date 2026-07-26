---
title: 'SSLSetDiffieHellmanParams(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslsetdiffiehellmanparams(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslsetdiffiehellmanparams(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetdiffiehellmanparams%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8131026ae4bd5620'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetDiffieHellmanParams(_:_:_:)

<sub>Function</sub>

Specifies Diffie-Hellman parameters for a given context.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>macOS</sub>

```swift
func SSLSetDiffieHellmanParams(_ context: SSLContext, _ dhParams: UnsafeRawPointer?, _ dhParamsLen: Int) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `dhParams` — A pointer to a buffer containing the Diffie-Hellman parameters in Open SSL DER format.

- `dhParamsLen` — A value representing the size of the buffer pointed to by the `dhParams` parameter.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

You can use this function to specify a set of Diffie-Hellman parameters to be used by Secure Transport for a specific session. Use of this function is optional. If Diffie-Hellman ciphers are allowed, the server and client negotiate a Diffie-Hellman cipher, and this function has not been called, then secure transport calculates a set of process wide parameters. However, that process can take as long as 30 seconds. Diffie-Hellman ciphers are enabled by default. See [SSLSetEnabledCiphers](<sslsetenabledciphers(______).md>).

In SSL/TLS, Diffie-Hellman parameters are always specified by the server. Therefore, this function can be called only by the server side of the connection.

You can use the [SSLGetDiffieHellmanParams](<sslgetdiffiehellmanparams(______).md>) function to retrieve Diffie-Hellman parameters specified in an earlier call to [SSLSetDiffieHellmanParams](<sslsetdiffiehellmanparams(______).md>).
