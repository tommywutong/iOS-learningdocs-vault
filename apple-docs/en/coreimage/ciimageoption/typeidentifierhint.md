---
title: typeIdentifierHint
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/coreimage/ciimageoption/typeidentifierhint
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageoption/typeidentifierhint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageoption/typeidentifierhint.json'
content_hash: 'sha256:f406edf039cea8bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageOption](../ciimageoption.md)

# typeIdentifierHint

<sub>Type Property</sub>

The uniform type identifier string to use in cases where a file’s format cannot be conclusively determined based solely on its contents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let typeIdentifierHint: CIImageOption
```

## Discussion

The value of this key should be an `NSString` containing a hint. It is most commonly needed for some RAW file formats which can also be
interpreted as TIFF files.

This option is only supported by these APIs:

- `/CIImage/imageWithContentsOfURL:options:`
- `/CIImage/initWithContentsOfURL:options:`
- `/CIImage/imageWithData:options:`
- `/CIImage/initWithData:options:`

> [!note] Note
> The key `kCGImageSourceTypeIdentifierHint` key can also be used for this purpose.
