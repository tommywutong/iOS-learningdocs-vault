---
title: symbolWeight()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifont/weight/symbolweight()
source_url: 'https://developer.apple.com/documentation/uikit/uifont/weight/symbolweight()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/weight/symbolweight%28%29.json'
content_hash: 'sha256:f1bdbc392dd4a578'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIFont](../../uifont.md) · [Weight](../weight.md)

# symbolWeight()

<sub>Instance Method</sub>

Provides the corresponding symbol weight for this font weight.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func symbolWeight() -> UIImage.SymbolWeight
```

## Return Value

The [SymbolWeight](../../uiimage/symbolweight.md) that most closely coordinates with the provided font weight.

## Discussion

When placing symbols adjacent to text, use this method to find the appropriate symbol weight to match the weight of the text. Similarly, if you want to display a symbol with a particular weight, you can use [UIFontWeightForImageSymbolWeight](<../../uiimage/symbolweight/fontweight().md>) to look up the matching font weight for adjacent text.
