---
title: 'assetVariantQualifierForMaximumValueInKeyPath:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetvariantqualifier/assetvariantqualifierformaximumvalueinkeypath:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariantqualifier/assetvariantqualifierformaximumvalueinkeypath:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariantqualifier/assetvariantqualifierformaximumvalueinkeypath%3A.json'
content_hash: 'sha256:1196327b36c6edba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetVariantQualifier](../avassetvariantqualifier.md)

# assetVariantQualifierForMaximumValueInKeyPath:

<sub>Type Method</sub>

Returns a qualifer for finding variant with maximum value in the input key path

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) assetVariantQualifierForMaximumValueInKeyPath:(NSString *) keyPath;
```

## Parameters

- `keyPath` — AVAssetVariant keyPath. Allowed keyPath values are peakBitRate, averageBitRate, videoAttributes.presentationSize. Must be a valid, non-nil NSString.

## See Also

### Creating a variant qualifier

- [+ assetVariantQualifierWithVariant:](<init(variant_).md>) — Creates a variant qualifier with an asset variant.
- [AVAssetVariant](../avassetvariant.md) — An object that represents a bit rate variant.
- [+ assetVariantQualifierWithPredicate:](<init(predicate_).md>) — Creates a variant qualifier with a predicate.
- [assetVariantQualifierForMinimumValueInKeyPath:](assetvariantqualifierforminimumvalueinkeypath_.md) — Returns a qualifer for finding variant with minimum value in the input key path.
