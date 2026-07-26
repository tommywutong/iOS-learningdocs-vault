---
title: 'CMSDecoderCopySignerCert(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsdecodercopysignercert(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsdecodercopysignercert(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsdecodercopysignercert%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:4933bd0f8097e1ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSDecoderCopySignerCert(_:_:_:)

<sub>Function</sub>

Obtains the certificate of the specified signer of a CMS message.

<sub>macOS</sub>

```swift
func CMSDecoderCopySignerCert(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ signerCertOut: UnsafeMutablePointer<SecCertificate?>) -> OSStatus
```

## Parameters

- `cmsDecoder` — The CMSDecoder reference returned by the `CMSDecoderCreate` function.

- `signerIndex` — A number indicating which signer’s email address to return. Signer index numbers start with 0. Use the [CMSDecoderGetNumSigners](<cmsdecodergetnumsigners(____).md>) function to determine the total number of signers for a message.

- `signerCertOut` — On return, points to the certificate of the specified signer.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). Returns [errSecParam](errsecparam.md) if the CMS message was not signed or if `signerIndex` is greater than the number of signers of the message minus one (signerIndex \> (numSigners – 1)).

## Discussion

You cannot call this function until after you have called the [CMSDecoderFinalizeMessage](<cmsdecoderfinalizemessage(__).md>) function.

## See Also

### Related Documentation

- [CMSDecoderCreate](<cmsdecodercreate(__).md>) — Creates a CMSDecoder reference.
- [CMSDecoderFinalizeMessage](<cmsdecoderfinalizemessage(__).md>) — Indicates that there is no more data to decode.
