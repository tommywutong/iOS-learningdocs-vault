---
title: tabBarPlacement
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/tabbarplacement
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/tabbarplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/tabbarplacement.json'
content_hash: 'sha256:c89d1c4bb2051d37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# tabBarPlacement

<sub>Instance Property</sub>

The current placement of the tab bar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var tabBarPlacement: TabBarPlacement? { get }
```

## Discussion

Note that this value is only set within the content views of a [TabView](../tabview.md).

A `nil` value corresponds to an undefined placement.

## See Also

### Configuring a tab bar

- [defaultAdaptableTabBarPlacement(_:)](<../view/defaultadaptabletabbarplacement(__).md>) — Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.
- [defaultTabBarPlacement(_:)](<../view/defaulttabbarplacement(__).md>) — Specifies the preferred placement for the tabs of a [TabView](../tabview.md) in the [sidebarAdaptable](../tabviewstyle/sidebaradaptable.md) style on platforms where the tab bar cannot adapt between different representations, and only one representation can be shown. _(beta)_
- [tabViewSidebarHeader(content:)](<../view/tabviewsidebarheader(content_).md>) — Adds a custom header to the sidebar of a tab view.
- [tabViewSidebarFooter(content:)](<../view/tabviewsidebarfooter(content_).md>) — Adds a custom footer to the sidebar of a tab view.
- [tabViewSidebarBottomBar(content:)](<../view/tabviewsidebarbottombar(content_).md>) — Adds a custom bottom bar to the sidebar of a tab view.
- [AdaptableTabBarPlacement](../adaptabletabbarplacement.md) — A placement for tabs in a tab view using the adaptable sidebar style.
- [TabBarPlacement](../tabbarplacement.md) — A placement for tabs in a tab view.
- [isTabBarShowingSections](istabbarshowingsections.md) — A Boolean value that determines whether a tab view shows the expanded contents of a tab section.
- [tabBarMinimizeBehavior(_:)](<../view/tabbarminimizebehavior(__).md>) — Sets the behavior for tab bar minimization.
- [TabBarMinimizeBehavior](../tabbarminimizebehavior.md)
- [TabViewBottomAccessoryPlacement](../tabviewbottomaccessoryplacement.md) — A placement of the bottom accessory in a tab view. You can use this to adjust the content of the accessory view based on the placement.
