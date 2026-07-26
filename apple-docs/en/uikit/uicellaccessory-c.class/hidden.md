---
title: hidden
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessory-c.class/hidden
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-c.class/hidden'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-c.class/hidden.json'
content_hash: 'sha256:396b2ed6845ba8be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-c.class.md)

# hidden

<sub>Instance Property</sub>

A Boolean value that determines whether the cell hides the accessory.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, getter=isHidden) BOOL hidden;
```

## Discussion

A hidden accessory takes up space in the layout, but it isn’t visible and doesn’t provide any behaviors.

Use this property to achieve a consistent layout across cells when some cells show this type of accessory and others don’t.

## See Also

### Customizing appearance

- [tintColor](tintcolor.md) — The tint color to apply to the accessory.
- [displayedState](displayedstate.md) — The cell-editing states that the accessory appears in.
- [UICellAccessoryDisplayedState](../uicellaccessorydisplayedstate.md) — Constants that describe the cell-editing states that the accessory appears in.
