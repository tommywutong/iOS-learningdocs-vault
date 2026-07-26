---
title: 'CMSEncoderCopyEncodedContent(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsencodercopyencodedcontent(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsencodercopyencodedcontent(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsencodercopyencodedcontent%28_%3A_%3A%29.json'
content_hash: 'sha256:a76911ed0099aa4f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSEncoderCopyEncodedContent(_:_:)

<sub>Function</sub>

Finishes encoding the message and obtains the encoded result.

<sub>macOS</sub>

```swift
func CMSEncoderCopyEncodedContent(_ cmsEncoder: CMSEncoder, _ encodedContentOut: UnsafeMutablePointer<CFData?>) -> OSStatus
```

## Parameters

- `cmsEncoder` — The CMSEncoder reference returned by the `CMSEncoderCreate` function.

- `encodedContentOut` — On return, points to the encoded message. You must use the `CFRelease` function to free this reference when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This is the last function in the sequence of encoding functions you call when creating a signed or encrypted message. In many cases, you can call the `CMSEncode` function alone instead of using the sequence of encoding functions.
