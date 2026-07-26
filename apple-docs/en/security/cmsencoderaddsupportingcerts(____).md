---
title: 'CMSEncoderAddSupportingCerts(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsencoderaddsupportingcerts(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsencoderaddsupportingcerts(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsencoderaddsupportingcerts%28_%3A_%3A%29.json'
content_hash: 'sha256:8ac59eccb1471728'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSEncoderAddSupportingCerts(_:_:)

<sub>Function</sub>

Adds certificates to a message.

<sub>macOS</sub>

```swift
func CMSEncoderAddSupportingCerts(_ cmsEncoder: CMSEncoder, _ certOrArray: CFTypeRef) -> OSStatus
```

## Parameters

- `cmsEncoder` — The CMSEncoder reference returned by the `CMSEncoderCreate` function.

- `certOrArray` — Either a single certificate, specified as a certificate object (type `SecCertificateRef`), or a set of certificates specified as a `CFArray` of certificate objects.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

A CMS message can contain arbitrary sets of certificates other than or in addition to those indicating the identity of signers. You can use this function to add such certificates to a message. It is not necessary to call this function for a normal signed message. When you create a signed message, Cryptographic Message Services automatically adds the signer certificates and any intermediate certificates needed to verify the signers.

You can use this function even if you don’t sign or encrypt the message, in order to transport one or more certificates. To do so, call `CMSEncoderCreate` to obtain a `CMSEncoderRef` reference, call `CMSEncoderAddSupportingCerts` one or more times, and then call `CMSEncoderCopyEncodedContent` to complete the message. No additional content need be specified.

If you do add content to the message in addition to the certificates, you must call this function before the first call to the `CMSEncoderUpdateContent` function.

## See Also

### Related Documentation

- [CMSEncoderUpdateContent](<cmsencoderupdatecontent(______).md>) — Feeds content bytes into the encoder.
- [CMSEncoderCreate](<cmsencodercreate(__).md>) — Creates a CMSEncoder reference.
- [CMSDecoderCopyAllCerts](<cmsdecodercopyallcerts(____).md>) — Obtains an array of all of the certificates in a message.
- [CMSEncoderCopyEncodedContent](<cmsencodercopyencodedcontent(____).md>) — Finishes encoding the message and obtains the encoded result.
- [CMSEncoderCopySupportingCerts](<cmsencodercopysupportingcerts(____).md>) — Obtains the certificates added to a message with `CMSEncoderAddSupportingCerts`.
