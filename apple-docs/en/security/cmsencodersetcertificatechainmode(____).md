---
title: 'CMSEncoderSetCertificateChainMode(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsencodersetcertificatechainmode(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsencodersetcertificatechainmode(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsencodersetcertificatechainmode%28_%3A_%3A%29.json'
content_hash: 'sha256:036f5cb3e141cec1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSEncoderSetCertificateChainMode(_:_:)

<sub>Function</sub>

Specifies which certificates to include in a signed CMS message.

<sub>macOS</sub>

```swift
func CMSEncoderSetCertificateChainMode(_ cmsEncoder: CMSEncoder, _ chainMode: CMSCertificateChainMode) -> OSStatus
```

## Parameters

- `cmsEncoder` — The CMSEncoder reference returned by the `CMSEncoderCreate` function.

- `chainMode` — A constant that indicates which certificate or certificates to include in the message. See [CMSCertificateChainMode](cmscertificatechainmode.md).

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This function is used only for signed messages and is optional. If you don’t call this function, the default, `kCMSCertificateChain`, is used. In this case the message includes the signer certificate plus all certificates needed to verify the signer certificate, up to but not including the root  certificate.

If you do call this function, you must call it before the first call to the `CMSEncoderUpdateContent` function.

## See Also

### Related Documentation

- [CMSEncoderUpdateContent](<cmsencoderupdatecontent(______).md>) — Feeds content bytes into the encoder.
- [CMSEncoderGetCertificateChainMode](<cmsencodergetcertificatechainmode(____).md>) — Obtains a constant that indicates which certificates are to be included in a signed CMS message.
- [CMSEncoderCreate](<cmsencodercreate(__).md>) — Creates a CMSEncoder reference.
