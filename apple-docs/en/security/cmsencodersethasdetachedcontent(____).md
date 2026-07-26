---
title: 'CMSEncoderSetHasDetachedContent(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsencodersethasdetachedcontent(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsencodersethasdetachedcontent(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsencodersethasdetachedcontent%28_%3A_%3A%29.json'
content_hash: 'sha256:e9643a98ced0e670'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSEncoderSetHasDetachedContent(_:_:)

<sub>Function</sub>

Specifies whether the signed data is to be separate from the message.

<sub>macOS</sub>

```swift
func CMSEncoderSetHasDetachedContent(_ cmsEncoder: CMSEncoder, _ detachedContent: Bool) -> OSStatus
```

## Parameters

- `cmsEncoder` — The CMSEncoder reference returned by the [CMSEncoderCreate](<cmsencodercreate(__).md>) function.

- `detachedContent` — `TRUE` if the message should exclude the data to be signed. Prior to calling this function, the encoder defaults to `FALSE` for this setting, indicating that the message contains the data to be signed.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

A signed CMS message can optionally be sent separately from the signed data. Set `detachedContent` to `TRUE` to indicate that the signed data is to be kept separate from the message.

Encrypted messages, including those that are also signed, cannot use detached content.

If you do call this function, you must call it before the first call to the [CMSEncoderUpdateContent](<cmsencoderupdatecontent(______).md>) function.

## See Also

### Related Documentation

- [CMSEncoderGetHasDetachedContent](<cmsencodergethasdetachedcontent(____).md>) — Indicates whether the message is to have detached content.
- [CMSEncoderUpdateContent](<cmsencoderupdatecontent(______).md>) — Feeds content bytes into the encoder.
- [CMSEncoderCreate](<cmsencodercreate(__).md>) — Creates a CMSEncoder reference.
- [CMSDecoderSetDetachedContent](<cmsdecodersetdetachedcontent(____).md>) — Specifies the message’s detached content, if any.
