---
title: 'CMSEncoderCopySupportingCerts(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsencodercopysupportingcerts(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsencodercopysupportingcerts(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsencodercopysupportingcerts%28_%3A_%3A%29.json'
content_hash: 'sha256:e2dbfd0f53fe6fca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSEncoderCopySupportingCerts(_:_:)

<sub>Function</sub>

Obtains the certificates added to a message with `CMSEncoderAddSupportingCerts`.

<sub>macOS</sub>

```swift
func CMSEncoderCopySupportingCerts(_ cmsEncoder: CMSEncoder, _ certsOut: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

## Parameters

- `cmsEncoder` — The CMSEncoder reference returned by the `CMSEncoderCreate` function.

- `certsOut` — On return, points to a CFArray of `SecCertificateRef` objects. You must use the `CFRelease` function to free this reference when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

A CMS message can contain arbitrary sets of certificates other than or in addition to those indicating the identity of signers. You can use this function to obtain any such certificates added with the `CMSEncoderAddSupportingCerts` function.  If `CMSEncoderAddSupportingCerts` has not been called, this function returns a `NULL` value for `certsOut`. Note that this function does not return the signing certificates, if any.

## See Also

### Related Documentation

- [CMSEncoderCreate](<cmsencodercreate(__).md>) — Creates a CMSEncoder reference.
- [CMSEncoderAddSupportingCerts](<cmsencoderaddsupportingcerts(____).md>) — Adds certificates to a message.
