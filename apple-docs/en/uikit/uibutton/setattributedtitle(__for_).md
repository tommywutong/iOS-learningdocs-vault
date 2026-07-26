---
title: 'setAttributedTitle(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/setattributedtitle(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/setattributedtitle(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/setattributedtitle%28_%3Afor%3A%29.json'
content_hash: 'sha256:ace283738eca8ac9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# setAttributedTitle(_:for:)

<sub>Instance Method</sub>

Sets the styled title to use for the specified state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setAttributedTitle(_ title: NSAttributedString?, for state: UIControl.State)
```

## Parameters

- `title` — The styled text string so use for the title.

- `state` — The state that uses the specified title. The possible values are described in [State](../uicontrol/state-swift.struct.md).

## Discussion

Use this method to set the title of the button, including any relevant formatting information. If you set both a title and an attributed title for the button, the button prefers the use of the attributed title.

At a minimum, you should set the value for the normal state. If a title is not specified for a state, the default behavior is to use the title associated with the [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) state. If the value for [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) is not set, then the property defaults to a system value.

## See Also

### Managing the title

- [titleLabel](titlelabel.md) — A view that displays the value of the `currentTitle` property for a button.
- [- titleForState:](<title(for_).md>) — Returns the title associated with the specified state.
- [- setTitle:forState:](<settitle(__for_).md>) — Sets the title to use for the specified state.
- [- attributedTitleForState:](<attributedtitle(for_).md>) — Returns the styled title associated with the specified state.
- [- titleColorForState:](<titlecolor(for_).md>) — Returns the title color used for a state.
- [- setTitleColor:forState:](<settitlecolor(__for_).md>) — Sets the color of the title to use for the specified state.
- [- titleShadowColorForState:](<titleshadowcolor(for_).md>) — Returns the shadow color of the title used for a state.
- [- setTitleShadowColor:forState:](<settitleshadowcolor(__for_).md>) — Sets the color of the title shadow to use for the specified state.
