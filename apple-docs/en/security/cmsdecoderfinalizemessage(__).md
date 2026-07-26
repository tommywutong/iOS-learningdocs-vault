---
title: 'CMSDecoderFinalizeMessage(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsdecoderfinalizemessage(_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsdecoderfinalizemessage(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsdecoderfinalizemessage%28_%3A%29.json'
content_hash: 'sha256:93c660c5b293a1cf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSDecoderFinalizeMessage(_:)

<sub>Function</sub>

Indicates that there is no more data to decode.

<sub>macOS</sub>

```swift
func CMSDecoderFinalizeMessage(_ cmsDecoder: CMSDecoder) -> OSStatus
```

## Parameters

- `cmsDecoder` — The CMSDecoder reference returned by the `CMSDecoderCreate` function.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). Returns [errSecUnknownFormat](errsecunknownformat.md) upon detection of an improperly formatted CMS message.

## Discussion

When you call this function, the decoder finishes decoding the message. If the message was encrypted and this function returns a result code of `noErr`, the message was successfully decrypted. Call the [CMSDecoderCopyContent](<cmsdecodercopycontent(____).md>) function to retrieve the message content. Call the [CMSDecoderGetNumSigners](<cmsdecodergetnumsigners(____).md>) function to find out if the message was signed and, if so, how many signers there were.

## See Also

### Related Documentation

- [CMSDecoderGetNumSigners](<cmsdecodergetnumsigners(____).md>) — Obtains the number of signers of a message.
- [CMSDecoderCreate](<cmsdecodercreate(__).md>) — Creates a CMSDecoder reference.
- [CMSDecoderCopyContent](<cmsdecodercopycontent(____).md>) — Obtains the message content, if any.
