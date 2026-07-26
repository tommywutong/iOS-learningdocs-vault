---
title: 'CMSDecoderCopyAllCerts(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsdecodercopyallcerts(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsdecodercopyallcerts(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsdecodercopyallcerts%28_%3A_%3A%29.json'
content_hash: 'sha256:a88efe31259c2f35'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSDecoderCopyAllCerts(_:_:)

<sub>Function</sub>

Obtains an array of all of the certificates in a message.

<sub>macOS</sub>

```swift
func CMSDecoderCopyAllCerts(_ cmsDecoder: CMSDecoder, _ certsOut: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

## Parameters

- `cmsDecoder` — The CMSDecoder reference returned by the `CMSDecoderCreate` function.

- `certsOut` — On return, points to an array of `SecCertificateRef` objects. Returns `NULL` if the message does not contain any certificates (the message was encrypted but not signed); this is not considered an error. You must use the `CFRelease` function to free this reference when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

A CMS message can contain arbitrary sets of certificates other than or in addition to those indicating the identity of signers. You can use this function to retrieve such certificates from a message. If the message was signed, it contains signer certificates. You can use the [CMSDecoderGetNumSigners](<cmsdecodergetnumsigners(____).md>) and [CMSDecoderCopySignerCert](<cmsdecodercopysignercert(______).md>) functions to retrieve the certificates for a specific signer.

You cannot call this function until after you have called the [CMSDecoderFinalizeMessage](<cmsdecoderfinalizemessage(__).md>) function.

## See Also

### Related Documentation

- [CMSDecoderCopySignerCert](<cmsdecodercopysignercert(______).md>) — Obtains the certificate of the specified signer of a CMS message.
- [CMSEncoderAddSupportingCerts](<cmsencoderaddsupportingcerts(____).md>) — Adds certificates to a message.
- [CMSDecoderGetNumSigners](<cmsdecodergetnumsigners(____).md>) — Obtains the number of signers of a message.
- [CMSDecoderCreate](<cmsdecodercreate(__).md>) — Creates a CMSDecoder reference.
- [CMSDecoderFinalizeMessage](<cmsdecoderfinalizemessage(__).md>) — Indicates that there is no more data to decode.
