---
title: 'title(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/title(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/title(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/title%28for%3A%29.json'
content_hash: 'sha256:83f7840ff182add6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# title(for:)

<sub>Instance Method</sub>

Returns the title associated with the specified state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func title(for state: UIControl.State) -> String?
```

## Parameters

- `state` — The state that uses the title. The possible values are described in [State](../uicontrol/state-swift.struct.md).

## Return Value

The title for the specified state. If no title has been set for the specific state, this method returns the title associated with the [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) state.

## See Also

### Managing the title

- [titleLabel](titlelabel.md) — A view that displays the value of the `currentTitle` property for a button.
- [- setTitle:forState:](<settitle(__for_).md>) — Sets the title to use for the specified state.
- [- attributedTitleForState:](<attributedtitle(for_).md>) — Returns the styled title associated with the specified state.
- [- setAttributedTitle:forState:](<setattributedtitle(__for_).md>) — Sets the styled title to use for the specified state.
- [- titleColorForState:](<titlecolor(for_).md>) — Returns the title color used for a state.
- [- setTitleColor:forState:](<settitlecolor(__for_).md>) — Sets the color of the title to use for the specified state.
- [- titleShadowColorForState:](<titleshadowcolor(for_).md>) — Returns the shadow color of the title used for a state.
- [- setTitleShadowColor:forState:](<settitleshadowcolor(__for_).md>) — Sets the color of the title shadow to use for the specified state.
