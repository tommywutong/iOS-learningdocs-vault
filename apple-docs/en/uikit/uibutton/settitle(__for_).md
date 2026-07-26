---
title: 'setTitle(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/settitle(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/settitle(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/settitle%28_%3Afor%3A%29.json'
content_hash: 'sha256:770582d8b379c901'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# setTitle(_:for:)

<sub>Instance Method</sub>

Sets the title to use for the specified state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setTitle(_ title: String?, for state: UIControl.State)
```

## Parameters

- `title` — The title to use for the specified state.

- `state` — The state that uses the specified title. [State](../uicontrol/state-swift.struct.md) describes the possible values.

## Discussion

Use this method to set the title for the button. The title you specify derives its formatting from the button’s associated label object. If you set both a title and an attributed title for the button, the button prefers the use of the attributed title over this one.

At a minimum, set the value for the [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) state. If you don’t specify a title for the other states, the button uses the title associated with the [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) state. If you don’t set the value for [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md), then the property defaults to a system value.

> [!important] Important
> When the user interface idiom is [UIUserInterfaceIdiomMac](../uiuserinterfaceidiom/mac.md) and [behavioralStyle](behavioralstyle.md) is [UIBehavioralStyleMac](../uibehavioralstyle/mac.md), your app throws an exception if you use this method to set the title for any state other than [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md).

## See Also

### Managing the title

- [titleLabel](titlelabel.md) — A view that displays the value of the `currentTitle` property for a button.
- [- titleForState:](<title(for_).md>) — Returns the title associated with the specified state.
- [- attributedTitleForState:](<attributedtitle(for_).md>) — Returns the styled title associated with the specified state.
- [- setAttributedTitle:forState:](<setattributedtitle(__for_).md>) — Sets the styled title to use for the specified state.
- [- titleColorForState:](<titlecolor(for_).md>) — Returns the title color used for a state.
- [- setTitleColor:forState:](<settitlecolor(__for_).md>) — Sets the color of the title to use for the specified state.
- [- titleShadowColorForState:](<titleshadowcolor(for_).md>) — Returns the shadow color of the title used for a state.
- [- setTitleShadowColor:forState:](<settitleshadowcolor(__for_).md>) — Sets the color of the title shadow to use for the specified state.
