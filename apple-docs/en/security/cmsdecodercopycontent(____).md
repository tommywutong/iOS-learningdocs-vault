---
title: 'CMSDecoderCopyContent(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsdecodercopycontent(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsdecodercopycontent(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsdecodercopycontent%28_%3A_%3A%29.json'
content_hash: 'sha256:562c262d681512f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSDecoderCopyContent(_:_:)

<sub>Function</sub>

Obtains the message content, if any.

<sub>macOS</sub>

```swift
func CMSDecoderCopyContent(_ cmsDecoder: CMSDecoder, _ contentOut: UnsafeMutablePointer<CFData?>) -> OSStatus
```

## Parameters

- `cmsDecoder` — The CMSDecoder reference returned by the `CMSDecoderCreate` function.

- `contentOut` — On return, points to the message’s content. Returns `NULL` if the content is detached. You must use the `CFRelease` function to free this reference when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

If the message has detached content, you are responsible for retrieving the content. In that case, you use the [CMSDecoderSetDetachedContent](<cmsdecodersetdetachedcontent(____).md>) function to tell the decoder the location of the content.

You cannot call this function until after you have called the `CMSDecoderFinalizeMessage` function.

## See Also

### Related Documentation

- [CMSEncoderSetHasDetachedContent](<cmsencodersethasdetachedcontent(____).md>) — Specifies whether the signed data is to be separate from the message.
- [CMSDecoderSetDetachedContent](<cmsdecodersetdetachedcontent(____).md>) — Specifies the message’s detached content, if any.
- [CMSDecoderCreate](<cmsdecodercreate(__).md>) — Creates a CMSDecoder reference.
- [CMSDecoderFinalizeMessage](<cmsdecoderfinalizemessage(__).md>) — Indicates that there is no more data to decode.
