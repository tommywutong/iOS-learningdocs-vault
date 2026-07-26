---
title: 'CMSDecoderCreate(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsdecodercreate(_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsdecodercreate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsdecodercreate%28_%3A%29.json'
content_hash: 'sha256:0eea9ecfd4feb729'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSDecoderCreate(_:)

<sub>Function</sub>

Creates a CMSDecoder reference.

<sub>macOS</sub>

```swift
func CMSDecoderCreate(_ cmsDecoderOut: UnsafeMutablePointer<CMSDecoder?>) -> OSStatus
```

## Parameters

- `cmsDecoderOut` — On return, points to a CMSDecoder reference. You must use the `CFRelease` function to free this reference when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This is the first function in a sequence of decoder functions that you call to get information from a CMS message. The other functions in the sequence require you to pass in the CMSDecoder reference returned by this function. The next function in the sequence is `CMSDecoderUpdateMessage`.

## See Also

### Related Documentation

- [CMSDecoderUpdateMessage](<cmsdecoderupdatemessage(______).md>) — Feeds raw bytes of the message to be decoded into the decoder.
