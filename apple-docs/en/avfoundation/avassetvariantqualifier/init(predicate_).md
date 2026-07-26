---
title: 'init(predicate:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetvariantqualifier/init(predicate:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariantqualifier/init(predicate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariantqualifier/init%28predicate%3A%29.json'
content_hash: 'sha256:961af1e7ab6eab93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetVariantQualifier](../avassetvariantqualifier.md)

# init(predicate:)

<sub>Initializer</sub>

Creates a variant qualifier with a predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(predicate: NSPredicate)
```

## Parameters

- `predicate` — A predicate to find a particular asset variant.

## See Also

### Creating a variant qualifier

- [+ assetVariantQualifierWithVariant:](<init(variant_).md>) — Creates a variant qualifier with an asset variant.
- [AVAssetVariant](../avassetvariant.md) — An object that represents a bit rate variant.
