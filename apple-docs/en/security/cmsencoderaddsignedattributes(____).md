---
title: 'CMSEncoderAddSignedAttributes(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsencoderaddsignedattributes(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsencoderaddsignedattributes(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsencoderaddsignedattributes%28_%3A_%3A%29.json'
content_hash: 'sha256:78c6d507dc480744'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSEncoderAddSignedAttributes(_:_:)

<sub>Function</sub>

Specifies attributes for a signed message.

<sub>macOS</sub>

```swift
func CMSEncoderAddSignedAttributes(_ cmsEncoder: CMSEncoder, _ signedAttributes: CMSSignedAttributes) -> OSStatus
```

## Parameters

- `cmsEncoder` — The CMSEncoder reference returned by the `CMSEncoderCreate` function.

- `signedAttributes` — Attribute flags as defined in [CMSSignedAttributes](cmssignedattributes.md).

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Attributes are optional for signed messages. They are not used for other types of CMS messages.  The use of attributes is described in section 2.5 of the S/MIME 3.1 specification.

If you do call this function, you must call it before the first call to the [CMSEncoderUpdateContent](<cmsencoderupdatecontent(______).md>) function.

## See Also

### Related Documentation

- [CMSEncoderUpdateContent](<cmsencoderupdatecontent(______).md>) — Feeds content bytes into the encoder.
- [CMSEncoderCreate](<cmsencodercreate(__).md>) — Creates a CMSEncoder reference.
