---
title: compactTabIdentifiers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/compacttabidentifiers
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/compacttabidentifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/compacttabidentifiers.json'
content_hash: 'sha256:86a6c8619a732fe6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarController](../uitabbarcontroller.md)

# compactTabIdentifiers

<sub>Instance Property</sub>

An optional filter to display only select root-level tabs when in a compact appearance.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var compactTabIdentifiers: [String]? { get set }
```

## Discussion

The default value is is `nil`, which would make all tabs available.

## See Also

### Customizing the tab bar appearance

- [tabBarHidden](istabbarhidden.md) — Determines if the active tab bar is currently hidden.
- [- setTabBarHidden:animated:](<settabbarhidden(__animated_).md>) — Changes the active tab bar’s visibility with an option to animate the change.
- [bottomAccessory](bottomaccessory.md) — An optional bottom accessory of the tab bar controller.
- [- setBottomAccessory:animated:](<setbottomaccessory(__animated_).md>) — Sets a bottom accessory with an option to animate the change.
- [customizationIdentifier](customizationidentifier.md) — The customization identifier for the tab bar and sidebar for persistence.
- [prominentTabIdentifier](prominenttabidentifier.md) — The identifier of the tab that should be displayed as prominent. Where supported, the specified tab receives enhanced visual emphasis in the tab bar. If this property is nil, and there is a `UISearchTab` that could become prominent (when `automaticallyActivatesSearch = true`), then the search tab will receive the prominent treatment by default. _(beta)_
- [- setProminentTabIdentifier:animated:](<setprominenttabidentifier(__animated_).md>) — Sets the prominent tab identifier with an option to animate the change. _(beta)_
