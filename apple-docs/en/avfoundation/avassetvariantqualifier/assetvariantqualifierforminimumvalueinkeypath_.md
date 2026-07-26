---
title: 'assetVariantQualifierForMinimumValueInKeyPath:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetvariantqualifier/assetvariantqualifierforminimumvalueinkeypath:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariantqualifier/assetvariantqualifierforminimumvalueinkeypath:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariantqualifier/assetvariantqualifierforminimumvalueinkeypath%3A.json'
content_hash: 'sha256:e7d24179adff73d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetVariantQualifier](../avassetvariantqualifier.md)

# assetVariantQualifierForMinimumValueInKeyPath:

<sub>Type Method</sub>

Returns a qualifer for finding variant with minimum value in the input key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) assetVariantQualifierForMinimumValueInKeyPath:(NSString *) keyPath;
```

## Parameters

- `keyPath` — AVAssetVariant keyPath. Allowed keyPath values are peakBitRate, averageBitRate, videoAttributes.presentationSize. Must be a valid, non-nil NSString.

## See Also

### Creating a variant qualifier

- [+ assetVariantQualifierWithVariant:](<init(variant_).md>) — Creates a variant qualifier with an asset variant.
- [AVAssetVariant](../avassetvariant.md) — An object that represents a bit rate variant.
- [+ assetVariantQualifierWithPredicate:](<init(predicate_).md>) — Creates a variant qualifier with a predicate.
- [assetVariantQualifierForMaximumValueInKeyPath:](assetvariantqualifierformaximumvalueinkeypath_.md) — Returns a qualifer for finding variant with maximum value in the input key path
