---
title: 'withProminence(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolor/withprominence(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/withprominence(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/withprominence%28_%3A%29.json'
content_hash: 'sha256:4c140b4290040d37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# withProminence(_:)

<sub>Instance Method</sub>

Returns the version of the current color that results from applying the specified prominence.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func withProminence(_ prominence: UIColor.Prominence) -> UIColor
```

## Parameters

- `prominence` — The prominence to apply to the color. For options, see [Prominence](prominence-swift.enum.md).

## Return Value

The version of the color to display for the specified prominence.

## Discussion

Interface elements, such as text labels, can have a different level of prominence in the UI. For example, a title label appears more prominently than a subtitle or caption. When you specify a label’s color, you can pass one of the [Prominence](prominence-swift.enum.md) constants to [- colorWithProminence:](<withprominence(__).md>) to communicate how prominently to display that color in the UI.

The following code creates a label with a secondary, vibrant red color:

```swift
let label = UILabel()
label.preferredVibrancy = .automatic
label.textColor = .systemRed.withProminence(.secondary) 
```

## See Also

### Working with color prominence

- [prominence](prominence-swift.property.md)
- [Prominence](prominence-swift.enum.md) — A type that indicates the prominence of a color in the interface.
