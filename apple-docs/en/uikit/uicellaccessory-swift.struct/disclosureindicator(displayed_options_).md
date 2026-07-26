---
title: 'disclosureIndicator(displayed:options:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicellaccessory-swift.struct/disclosureindicator(displayed:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/disclosureindicator(displayed:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/disclosureindicator%28displayed%3Aoptions%3A%29.json'
content_hash: 'sha256:04e9e52b2180181c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# disclosureIndicator(displayed:options:)

<sub>Type Method</sub>

Creates a disclosure indicator system accessory with the specified display state and configuration options.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func disclosureIndicator(displayed: UICellAccessory.DisplayedState = .always, options: UICellAccessory.DisclosureIndicatorOptions = DisclosureIndicatorOptions()) -> UICellAccessory
```

## Parameters

- `displayed` — The cell-editing states that the disclosure indicator appears in. This parameter has a default value of [UICellAccessory.DisplayedState.always](displayedstate/always.md).

- `options` — Configuration options for the disclosure indicator. See [DisclosureIndicatorOptions](disclosureindicatoroptions.md) for possible configuration options.

## Return Value

A configured disclosure indicator cell accessory. This accessory is a disclosure chevron that points in the trailing direction. This accessory appears on the trailing edge of the cell.

## Discussion

Use this cell accessory to indicate that users can tap on the cell to disclose additional content.

## See Also

### Creating a disclosure indicator

- [DisclosureIndicatorOptions](disclosureindicatoroptions.md) — Configuration options for a disclosure indicator.
