---
title: bottomAccessory
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/bottomaccessory
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/bottomaccessory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/bottomaccessory.json'
content_hash: 'sha256:540f623edf1bbcc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarController](../uitabbarcontroller.md)

# bottomAccessory

<sub>Instance Property</sub>

An optional bottom accessory of the tab bar controller.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var bottomAccessory: UITabAccessory? { get set }
```

## Discussion

The default value for this property is `nil`.

## See Also

### Customizing the tab bar appearance

- [tabBarHidden](istabbarhidden.md) — Determines if the active tab bar is currently hidden.
- [- setTabBarHidden:animated:](<settabbarhidden(__animated_).md>) — Changes the active tab bar’s visibility with an option to animate the change.
- [- setBottomAccessory:animated:](<setbottomaccessory(__animated_).md>) — Sets a bottom accessory with an option to animate the change.
- [compactTabIdentifiers](compacttabidentifiers.md) — An optional filter to display only select root-level tabs when in a compact appearance.
- [customizationIdentifier](customizationidentifier.md) — The customization identifier for the tab bar and sidebar for persistence.
- [prominentTabIdentifier](prominenttabidentifier.md) — The identifier of the tab that should be displayed as prominent. Where supported, the specified tab receives enhanced visual emphasis in the tab bar. If this property is nil, and there is a `UISearchTab` that could become prominent (when `automaticallyActivatesSearch = true`), then the search tab will receive the prominent treatment by default. _(beta)_
- [- setProminentTabIdentifier:animated:](<setprominenttabidentifier(__animated_).md>) — Sets the prominent tab identifier with an option to animate the change. _(beta)_
