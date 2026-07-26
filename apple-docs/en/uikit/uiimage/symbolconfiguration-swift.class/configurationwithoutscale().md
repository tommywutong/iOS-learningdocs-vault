---
title: configurationWithoutScale()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/symbolconfiguration-swift.class/configurationwithoutscale()
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/configurationwithoutscale()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/symbolconfiguration-swift.class/configurationwithoutscale%28%29.json'
content_hash: 'sha256:a87770e1825cc251'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [SymbolConfiguration](../symbolconfiguration-swift.class.md)

# configurationWithoutScale()

<sub>Instance Method</sub>

Returns a copy of the current symbol configuration object without scale information.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func configurationWithoutScale() -> Self
```

## Return Value

A new symbol configuration object without the specified information.

## Discussion

This method sets the scale value in the new object to [UIImageSymbolScaleUnspecified](../symbolscale/unspecified.md).

## See Also

### Removing configuration attributes

- [- configurationWithoutPointSizeAndWeight](<configurationwithoutpointsizeandweight().md>) — Returns a copy of the current symbol configuration object without point-size and weight information.
- [- configurationWithoutTextStyle](<configurationwithouttextstyle().md>) — Returns a copy of the current symbol configuration object without font text style information.
- [- configurationWithoutWeight](<configurationwithoutweight().md>) — Returns a copy of the current symbol configuration object without weight information.
