---
title: 'CMSEncoderGetHasDetachedContent(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsencodergethasdetachedcontent(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsencodergethasdetachedcontent(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsencodergethasdetachedcontent%28_%3A_%3A%29.json'
content_hash: 'sha256:8e49c8bf8a68f2f5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSEncoderGetHasDetachedContent(_:_:)

<sub>Function</sub>

Indicates whether the message is to have detached content.

<sub>macOS</sub>

```swift
func CMSEncoderGetHasDetachedContent(_ cmsEncoder: CMSEncoder, _ detachedContentOut: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus
```

## Parameters

- `cmsEncoder` — The CMSEncoder reference returned by the `CMSEncoderCreate` function.

- `detachedContentOut` — Returns `TRUE` if the message has detached content.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This function returns the value specified in `CMSEncoderSetHasDetachedContent` if that function has been called; otherwise it returns `FALSE`.

## See Also

### Related Documentation

- [CMSEncoderSetHasDetachedContent](<cmsencodersethasdetachedcontent(____).md>) — Specifies whether the signed data is to be separate from the message.
- [CMSDecoderCreate](<cmsdecodercreate(__).md>) — Creates a CMSDecoder reference.
