---
title: configurationWithoutWeight()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/symbolconfiguration-swift.class/configurationwithoutweight()
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/configurationwithoutweight()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/symbolconfiguration-swift.class/configurationwithoutweight%28%29.json'
content_hash: 'sha256:709217f1d4b8767c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [SymbolConfiguration](../symbolconfiguration-swift.class.md)

# configurationWithoutWeight()

<sub>Instance Method</sub>

Returns a copy of the current symbol configuration object without weight information.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func configurationWithoutWeight() -> Self
```

## Return Value

A new symbol configuration object without the specified information.

## Discussion

This method sets the weight value in the new object to [UIImageSymbolWeightUnspecified](../symbolweight/unspecified.md).

## See Also

### Removing configuration attributes

- [- configurationWithoutPointSizeAndWeight](<configurationwithoutpointsizeandweight().md>) — Returns a copy of the current symbol configuration object without point-size and weight information.
- [- configurationWithoutScale](<configurationwithoutscale().md>) — Returns a copy of the current symbol configuration object without scale information.
- [- configurationWithoutTextStyle](<configurationwithouttextstyle().md>) — Returns a copy of the current symbol configuration object without font text style information.
