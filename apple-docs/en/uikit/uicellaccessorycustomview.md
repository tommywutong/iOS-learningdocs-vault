---
title: UICellAccessoryCustomView
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessorycustomview
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessorycustomview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessorycustomview.json'
content_hash: 'sha256:6ab5eeb010d5434d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICellAccessoryCustomView

<sub>Class</sub>

A custom cell accessory.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UICellAccessoryCustomView : UICellAccessory
```

## Relationships

- **Inherits From**: [UICellAccessory](uicellaccessory-c.class.md)

## Topics

### Creating Configuration Options

- [initWithCustomView:placement:](uicellaccessorycustomview/initwithcustomview_placement_.md) — Creates a custom accessory with the specified view and cell accessory placement.
- [initWithCoder:](uicellaccessorycustomview/initwithcoder_.md) — Creates a custom accessory from data in an unarchiver.

### Accessing Configuration Options

- [customView](uicellaccessorycustomview/customview.md) — The custom view to display for the accessory.
- [placement](uicellaccessorycustomview/placement.md) — The placement for the accessory.
- [position](uicellaccessorycustomview/position.md) — The index position of the cell accessory in relation to the other accessories in the accessories array.
- [maintainsFixedSize](uicellaccessorycustomview/maintainsfixedsize.md) — A Boolean value that determines whether to preserve the frame size of the custom view.
