---
title: 'CMSEncoderAddRecipients(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsencoderaddrecipients(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsencoderaddrecipients(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsencoderaddrecipients%28_%3A_%3A%29.json'
content_hash: 'sha256:7a638a1db3bdfc2f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSEncoderAddRecipients(_:_:)

<sub>Function</sub>

Specifies a message is to be encrypted and specifies the recipients of the message.

<sub>macOS</sub>

```swift
func CMSEncoderAddRecipients(_ cmsEncoder: CMSEncoder, _ recipientOrArray: CFTypeRef) -> OSStatus
```

## Parameters

- `cmsEncoder` — The CMSEncoder reference returned by the `CMSEncoderCreate` function.

- `recipientOrArray` — Either a single certificate containing a public encryption key for one message recipient, specified as a certificate object (type [SecCertificate](seccertificate.md)), or a set of certificates specified as a [CFArray](../corefoundation/cfarray.md) of certificate objects.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Your keychain must contain a certificate that supports encryption for each recipient. You can call this function more than once for the same message.

You can both sign and encrypt the same message; however, you cannot call both this function and the [CMSEncoderSetHasDetachedContent](<cmsencodersethasdetachedcontent(____).md>) function for the same message.

If you do call this function, you must call it before the first call to the [CMSEncoderUpdateContent](<cmsencoderupdatecontent(______).md>) function.

## See Also

### Related Documentation

- [CMSEncoderUpdateContent](<cmsencoderupdatecontent(______).md>) — Feeds content bytes into the encoder.
- [CMSEncoderCreate](<cmsencodercreate(__).md>) — Creates a CMSEncoder reference.
- [CMSEncoderCopyRecipients](<cmsencodercopyrecipients(____).md>) — Obtains the array of recipients specified with the `CMSEncoderAddRecipients` function.
- [CMSDecoderIsContentEncrypted](<cmsdecoderiscontentencrypted(____).md>) — Determines whether a CMS message was encrypted.
