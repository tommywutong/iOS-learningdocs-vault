---
title: 'CMSEncoderGetCertificateChainMode(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsencodergetcertificatechainmode(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsencodergetcertificatechainmode(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsencodergetcertificatechainmode%28_%3A_%3A%29.json'
content_hash: 'sha256:5dd45e98797db230'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSEncoderGetCertificateChainMode(_:_:)

<sub>Function</sub>

Obtains a constant that indicates which certificates are to be included in a signed CMS message.

<sub>macOS</sub>

```swift
func CMSEncoderGetCertificateChainMode(_ cmsEncoder: CMSEncoder, _ chainModeOut: UnsafeMutablePointer<CMSCertificateChainMode>) -> OSStatus
```

## Parameters

- `cmsEncoder` — The CMSEncoder reference returned by the `CMSEncoderCreate` function.

- `chainModeOut` — On return, a constant that indicates which certificate or certificates are to be included in the message. See [CMSCertificateChainMode](cmscertificatechainmode.md).

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## See Also

### Related Documentation

- [CMSEncoderCreate](<cmsencodercreate(__).md>) — Creates a CMSEncoder reference.
