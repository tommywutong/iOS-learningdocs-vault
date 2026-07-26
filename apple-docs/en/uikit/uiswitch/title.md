---
title: title
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiswitch/title
source_url: 'https://developer.apple.com/documentation/uikit/uiswitch/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiswitch/title.json'
content_hash: 'sha256:9003373b7bc9c965'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISwitch](../uiswitch.md)

# title

<sub>Instance Property</sub>

The title displayed next to a checkbox-style switch.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var title: String? { get set }
```

## Discussion

Set [title](title.md) only when the user interface idiom is [UIUserInterfaceIdiomMac](../uiuserinterfaceidiom/mac.md); otherwise, a runtime exception occurs.

```swift
let showFavoritesAtTop = UISwitch()
showFavoritesAtTop.preferredStyle = .checkbox
if traitCollection.userInterfaceIdiom == .mac {
    showFavoritesAtTop.title = "Always show favorite recipes at the top"
}
```

The switch ignores [title](title.md) when the value of [style](style-swift.property.md) isn’t [UISwitchStyleCheckbox](style-swift.enum/checkbox.md).

## See Also

### Setting the display style

- [Displaying a checkbox in your Mac app built with Mac Catalyst](../displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst.md) — Present a switch control as a Mac-style checkbox when your app runs in the Mac user interface idiom.
- [preferredStyle](preferredstyle.md) — The preferred display style for the switch.
- [style](style-swift.property.md) — The display style for the switch.
- [Style](style-swift.enum.md) — Styles that determine the appearance of the switch.
