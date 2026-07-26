---
title: 'setBottomAccessory(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontroller/setbottomaccessory(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/setbottomaccessory(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/setbottomaccessory%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:2aa26c2013250dc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarController](../uitabbarcontroller.md)

# setBottomAccessory(_:animated:)

<sub>Instance Method</sub>

Sets a bottom accessory with an option to animate the change.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func setBottomAccessory(_ bottomAccessory: UITabAccessory?, animated: Bool)
```

## See Also

### Customizing the tab bar appearance

- [tabBarHidden](istabbarhidden.md) — Determines if the active tab bar is currently hidden.
- [- setTabBarHidden:animated:](<settabbarhidden(__animated_).md>) — Changes the active tab bar’s visibility with an option to animate the change.
- [bottomAccessory](bottomaccessory.md) — An optional bottom accessory of the tab bar controller.
- [compactTabIdentifiers](compacttabidentifiers.md) — An optional filter to display only select root-level tabs when in a compact appearance.
- [customizationIdentifier](customizationidentifier.md) — The customization identifier for the tab bar and sidebar for persistence.
- [prominentTabIdentifier](prominenttabidentifier.md) — The identifier of the tab that should be displayed as prominent. Where supported, the specified tab receives enhanced visual emphasis in the tab bar. If this property is nil, and there is a `UISearchTab` that could become prominent (when `automaticallyActivatesSearch = true`), then the search tab will receive the prominent treatment by default. _(beta)_
- [- setProminentTabIdentifier:animated:](<setprominenttabidentifier(__animated_).md>) — Sets the prominent tab identifier with an option to animate the change. _(beta)_
