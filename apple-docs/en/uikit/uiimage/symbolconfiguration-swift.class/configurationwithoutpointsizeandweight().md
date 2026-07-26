---
title: configurationWithoutPointSizeAndWeight()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/symbolconfiguration-swift.class/configurationwithoutpointsizeandweight()
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/configurationwithoutpointsizeandweight()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/symbolconfiguration-swift.class/configurationwithoutpointsizeandweight%28%29.json'
content_hash: 'sha256:5f8ce1405e70da07'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [SymbolConfiguration](../symbolconfiguration-swift.class.md)

# configurationWithoutPointSizeAndWeight()

<sub>Instance Method</sub>

Returns a copy of the current symbol configuration object without point-size and weight information.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func configurationWithoutPointSizeAndWeight() -> Self
```

## Return Value

A new symbol configuration object without the specified information.

## Discussion

This method sets the weight value in the new object to [UIImageSymbolWeightUnspecified](../symbolweight/unspecified.md) and removes the point-size information.

## See Also

### Removing configuration attributes

- [- configurationWithoutScale](<configurationwithoutscale().md>) — Returns a copy of the current symbol configuration object without scale information.
- [- configurationWithoutTextStyle](<configurationwithouttextstyle().md>) — Returns a copy of the current symbol configuration object without font text style information.
- [- configurationWithoutWeight](<configurationwithoutweight().md>) — Returns a copy of the current symbol configuration object without weight information.
