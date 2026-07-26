---
title: 'setTitleColor(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/settitlecolor(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/settitlecolor(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/settitlecolor%28_%3Afor%3A%29.json'
content_hash: 'sha256:0f3c7000a973bbdb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# setTitleColor(_:for:)

<sub>Instance Method</sub>

Sets the color of the title to use for the specified state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setTitleColor(_ color: UIColor?, for state: UIControl.State)
```

## Parameters

- `color` — The color of the title to use for the specified state.

- `state` — The state that uses the specified color. The possible values are described in [State](../uicontrol/state-swift.struct.md).

## Discussion

In general, if a property is not specified for a state, the default is to use the [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) value. If the [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) value is not set, then the property defaults to a system value. Therefore, at a minimum, you should set the value for the normal state.

## See Also

### Managing the title

- [titleLabel](titlelabel.md) — A view that displays the value of the `currentTitle` property for a button.
- [- titleForState:](<title(for_).md>) — Returns the title associated with the specified state.
- [- setTitle:forState:](<settitle(__for_).md>) — Sets the title to use for the specified state.
- [- attributedTitleForState:](<attributedtitle(for_).md>) — Returns the styled title associated with the specified state.
- [- setAttributedTitle:forState:](<setattributedtitle(__for_).md>) — Sets the styled title to use for the specified state.
- [- titleColorForState:](<titlecolor(for_).md>) — Returns the title color used for a state.
- [- titleShadowColorForState:](<titleshadowcolor(for_).md>) — Returns the shadow color of the title used for a state.
- [- setTitleShadowColor:forState:](<settitleshadowcolor(__for_).md>) — Sets the color of the title shadow to use for the specified state.
