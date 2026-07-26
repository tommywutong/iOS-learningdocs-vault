---
title: 'SSLSetCertificateAuthorities(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslsetcertificateauthorities(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslsetcertificateauthorities(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetcertificateauthorities%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:95973d40e6ad3990'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetCertificateAuthorities(_:_:_:)

<sub>Function</sub>

Adds one or more certificates to a server’s list of certification authorities (CAs) acceptable for client authentication.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>macOS</sub>

```swift
func SSLSetCertificateAuthorities(_ context: SSLContext, _ certificateOrArray: CFTypeRef, _ replaceExisting: Bool) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `certificateOrArray` — A value of type `SecCertificateRef`, or a value of type `CFArray` containing an array of `SecCertificateRef` values, representing one or more certificates to be added to the server’s list of acceptable certification authorities (CAs).

- `replaceExisting` — A Boolean value specifying whether to replace or append the current set of certification authorities. If this value is `true`, the specified certificates replace the existing list of acceptable CAs, if any. If `false`, the specified certificates are appended to the existing list of.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md). Returns [errSecParam](errsecparam.md) if this function is called for a session that is configured as a client, or when a session is active.

## Discussion

Each successive call to this function with the `replaceExisting` parameter set to [false](../swift/false.md) results in accumulation of additional certification authorities. To see the current set of certification authorities, call the [SSLCopyCertificateAuthorities](<sslcopycertificateauthorities(____).md>) function.

## See Also

### Related Documentation

- [SSLCopyDistinguishedNames](<sslcopydistinguishednames(____).md>) — Retrieves the distinguished names of acceptable certification authorities. _(deprecated)_
