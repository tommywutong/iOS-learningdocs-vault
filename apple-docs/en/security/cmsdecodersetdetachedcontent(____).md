---
title: 'CMSDecoderSetDetachedContent(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsdecodersetdetachedcontent(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsdecodersetdetachedcontent(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsdecodersetdetachedcontent%28_%3A_%3A%29.json'
content_hash: 'sha256:80bfccf6a7a5a88e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSDecoderSetDetachedContent(_:_:)

<sub>Function</sub>

Specifies the message’s detached content, if any.

<sub>macOS</sub>

```swift
func CMSDecoderSetDetachedContent(_ cmsDecoder: CMSDecoder, _ detachedContent: CFData) -> OSStatus
```

## Parameters

- `cmsDecoder` — The CMSDecoder reference returned by the `CMSDecoderCreate` function.

- `detachedContent` — A reference to the message’s detached content.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

The data of a signed CMS message can optionally be sent separately from the message. If the message’s content is detached from the message, you must call this function to tell the decoder where to find the message content.

Encrypted messages, including those that are also signed, cannot use detached content.

You can call this function either before or after decoding the message (by calling the `CMSDecoderUpdateMessage` and `CMSDecoderFinalizeMessage` functions). If a signed message has detached content, however, you must call this function before you can use the `CMSDecoderCopySignerStatus` function to ascertain the signature status.

## See Also

### Related Documentation

- [CMSEncoderSetHasDetachedContent](<cmsencodersethasdetachedcontent(____).md>) — Specifies whether the signed data is to be separate from the message.
- [CMSDecoderCreate](<cmsdecodercreate(__).md>) — Creates a CMSDecoder reference.
- [CMSDecoderCopySignerStatus](<cmsdecodercopysignerstatus(______________).md>) — Obtains the status of a CMS message’s signature.
