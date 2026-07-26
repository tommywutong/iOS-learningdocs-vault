---
title: 'titleShadowColor(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/titleshadowcolor(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/titleshadowcolor(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/titleshadowcolor%28for%3A%29.json'
content_hash: 'sha256:61705b544b27f60d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# titleShadowColor(for:)

<sub>Instance Method</sub>

Returns the shadow color of the title used for a state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func titleShadowColor(for state: UIControl.State) -> UIColor?
```

## Parameters

- `state` — The state that uses the title shadow color. The possible values are described in [State](../uicontrol/state-swift.struct.md).

## Return Value

The color of the title’s shadow for the specified state.

## See Also

### Managing the title

- [titleLabel](titlelabel.md) — A view that displays the value of the `currentTitle` property for a button.
- [- titleForState:](<title(for_).md>) — Returns the title associated with the specified state.
- [- setTitle:forState:](<settitle(__for_).md>) — Sets the title to use for the specified state.
- [- attributedTitleForState:](<attributedtitle(for_).md>) — Returns the styled title associated with the specified state.
- [- setAttributedTitle:forState:](<setattributedtitle(__for_).md>) — Sets the styled title to use for the specified state.
- [- titleColorForState:](<titlecolor(for_).md>) — Returns the title color used for a state.
- [- setTitleColor:forState:](<settitlecolor(__for_).md>) — Sets the color of the title to use for the specified state.
- [- setTitleShadowColor:forState:](<settitleshadowcolor(__for_).md>) — Sets the color of the title shadow to use for the specified state.
