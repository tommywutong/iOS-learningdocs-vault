---
title: TabBarPlacement
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabbarplacement
source_url: 'https://developer.apple.com/documentation/swiftui/tabbarplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabbarplacement.json'
content_hash: 'sha256:c693bcaea5dd3863'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TabBarPlacement

<sub>Structure</sub>

A placement for tabs in a tab view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TabBarPlacement
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Type Properties

- [bottomBar](tabbarplacement/bottombar.md) — Bottom bar of a tab view.
- [ornament](tabbarplacement/ornament.md) — Tab view displaying as an ornament.
- [pageIndicator](tabbarplacement/pageindicator.md) — Tab view displaying as an indicator that shows the position within the pages.
- [sidebar](tabbarplacement/sidebar.md) — The sidebar of a tab view.
- [topBar](tabbarplacement/topbar.md) — Top bar of a tab view.

## See Also

### Configuring a tab bar

- [defaultAdaptableTabBarPlacement(_:)](<view/defaultadaptabletabbarplacement(__).md>) — Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.
- [defaultTabBarPlacement(_:)](<view/defaulttabbarplacement(__).md>) — Specifies the preferred placement for the tabs of a [TabView](tabview.md) in the [sidebarAdaptable](tabviewstyle/sidebaradaptable.md) style on platforms where the tab bar cannot adapt between different representations, and only one representation can be shown. _(beta)_
- [tabViewSidebarHeader(content:)](<view/tabviewsidebarheader(content_).md>) — Adds a custom header to the sidebar of a tab view.
- [tabViewSidebarFooter(content:)](<view/tabviewsidebarfooter(content_).md>) — Adds a custom footer to the sidebar of a tab view.
- [tabViewSidebarBottomBar(content:)](<view/tabviewsidebarbottombar(content_).md>) — Adds a custom bottom bar to the sidebar of a tab view.
- [AdaptableTabBarPlacement](adaptabletabbarplacement.md) — A placement for tabs in a tab view using the adaptable sidebar style.
- [tabBarPlacement](environmentvalues/tabbarplacement.md) — The current placement of the tab bar.
- [isTabBarShowingSections](environmentvalues/istabbarshowingsections.md) — A Boolean value that determines whether a tab view shows the expanded contents of a tab section.
- [tabBarMinimizeBehavior(_:)](<view/tabbarminimizebehavior(__).md>) — Sets the behavior for tab bar minimization.
- [TabBarMinimizeBehavior](tabbarminimizebehavior.md)
- [TabViewBottomAccessoryPlacement](tabviewbottomaccessoryplacement.md) — A placement of the bottom accessory in a tab view. You can use this to adjust the content of the accessory view based on the placement.
