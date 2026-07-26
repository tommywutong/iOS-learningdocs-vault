---
title: 'CMSDecoderCopyDetachedContent(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsdecodercopydetachedcontent(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsdecodercopydetachedcontent(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsdecodercopydetachedcontent%28_%3A_%3A%29.json'
content_hash: 'sha256:494ba24447b9265e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSDecoderCopyDetachedContent(_:_:)

<sub>Function</sub>

Obtains the detached content specified with the `CMSDecoderSetDetachedContent` function.

<sub>macOS</sub>

```swift
func CMSDecoderCopyDetachedContent(_ cmsDecoder: CMSDecoder, _ detachedContentOut: UnsafeMutablePointer<CFData?>) -> OSStatus
```

## Parameters

- `cmsDecoder` — The CMSDecoder reference returned by the `CMSDecoderCreate` function.

- `detachedContentOut` — On return, points to the data reference specified by an earlier call to the `CMSDecoderSetDetachedContent` function. Returns a NULL data reference if no detached content has been specified. You must use the `CFRelease` function to free this reference when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## See Also

### Related Documentation

- [CMSDecoderCreate](<cmsdecodercreate(__).md>) — Creates a CMSDecoder reference.
