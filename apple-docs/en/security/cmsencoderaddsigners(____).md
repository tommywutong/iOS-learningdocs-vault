---
title: 'CMSEncoderAddSigners(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsencoderaddsigners(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsencoderaddsigners(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsencoderaddsigners%28_%3A_%3A%29.json'
content_hash: 'sha256:6ddde5b4316d4f72'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSEncoderAddSigners(_:_:)

<sub>Function</sub>

Specifies signers of the message.

<sub>macOS</sub>

```swift
func CMSEncoderAddSigners(_ cmsEncoder: CMSEncoder, _ signerOrArray: CFTypeRef) -> OSStatus
```

## Parameters

- `cmsEncoder` — The CMSEncoder reference returned by the `CMSEncoderCreate` function.

- `signerOrArray` — The identity object for the identity of one signer, specified as type `SecIdentityRef`, or a `CFArray` of identity objects of type`SecIdentityRef`.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Call this function only if the message is to be signed. You can call this function more than once for the same message.

If you do call this function, you must call it before the first call to the [CMSEncoderUpdateContent](<cmsencoderupdatecontent(______).md>) function.

## See Also

### Related Documentation

- [CMSEncoderUpdateContent](<cmsencoderupdatecontent(______).md>) — Feeds content bytes into the encoder.
- [CMSEncoderCopySigners](<cmsencodercopysigners(____).md>) — Obtains the array of signers specified with the `CMSEncoderAddSigners` function.
- [CMSEncoderCreate](<cmsencodercreate(__).md>) — Creates a CMSEncoder reference.
- [CMSDecoderCopySignerStatus](<cmsdecodercopysignerstatus(______________).md>) — Obtains the status of a CMS message’s signature.
