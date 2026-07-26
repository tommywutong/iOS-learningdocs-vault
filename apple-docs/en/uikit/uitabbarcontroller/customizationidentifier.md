---
title: customizationIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/customizationidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/customizationidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/customizationidentifier.json'
content_hash: 'sha256:e7e5bc8f5e486507'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarController](../uitabbarcontroller.md)

# customizationIdentifier

<sub>Instance Property</sub>

The customization identifier for the tab bar and sidebar for persistence.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var customizationIdentifier: String? { get set }
```

## Discussion

The identifier is useful for when an app has multiple tab bar controllers, each with their own customizations. If the customization identifier is `nil`, a system default is used. Default is `nil`.

## See Also

### Customizing the tab bar appearance

- [tabBarHidden](istabbarhidden.md) — Determines if the active tab bar is currently hidden.
- [- setTabBarHidden:animated:](<settabbarhidden(__animated_).md>) — Changes the active tab bar’s visibility with an option to animate the change.
- [bottomAccessory](bottomaccessory.md) — An optional bottom accessory of the tab bar controller.
- [- setBottomAccessory:animated:](<setbottomaccessory(__animated_).md>) — Sets a bottom accessory with an option to animate the change.
- [compactTabIdentifiers](compacttabidentifiers.md) — An optional filter to display only select root-level tabs when in a compact appearance.
- [prominentTabIdentifier](prominenttabidentifier.md) — The identifier of the tab that should be displayed as prominent. Where supported, the specified tab receives enhanced visual emphasis in the tab bar. If this property is nil, and there is a `UISearchTab` that could become prominent (when `automaticallyActivatesSearch = true`), then the search tab will receive the prominent treatment by default. _(beta)_
- [- setProminentTabIdentifier:animated:](<setprominenttabidentifier(__animated_).md>) — Sets the prominent tab identifier with an option to animate the change. _(beta)_
