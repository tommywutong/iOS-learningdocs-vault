---
title: 'SSLCopyCertificateAuthorities(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslcopycertificateauthorities(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslcopycertificateauthorities(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslcopycertificateauthorities%28_%3A_%3A%29.json'
content_hash: 'sha256:42441e7e51bad970'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLCopyCertificateAuthorities(_:_:)

<sub>Function</sub>

Retrieves the current list of certification authorities.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>macOS</sub>

```swift
func SSLCopyCertificateAuthorities(_ context: SSLContext, _ certificates: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `certificates` — On return, a pointer to a value of type `CFArrayRef`. This array contains values of type `SecCertificateRef` representing the current set of certification authorities (specified with the [SSLSetCertificateAuthorities](<sslsetcertificateauthorities(______).md>) function). Returns a `NULL` array if [SSLSetCertificateAuthorities](<sslsetcertificateauthorities(______).md>) has not been called. You must call the `CFRelease` function to release this array when you are finished with it.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## See Also

### Related Documentation

- [SSLCopyDistinguishedNames](<sslcopydistinguishednames(____).md>) — Retrieves the distinguished names of acceptable certification authorities. _(deprecated)_
