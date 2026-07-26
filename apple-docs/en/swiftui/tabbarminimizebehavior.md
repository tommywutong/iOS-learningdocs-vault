---
title: TabBarMinimizeBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabbarminimizebehavior
source_url: 'https://developer.apple.com/documentation/swiftui/tabbarminimizebehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabbarminimizebehavior.json'
content_hash: 'sha256:fe057461d349cd7a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TabBarMinimizeBehavior

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TabBarMinimizeBehavior
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [automatic](tabbarminimizebehavior/automatic.md) — Determine the behavior automatically based on the surrounding context.
- [never](tabbarminimizebehavior/never.md) — Never minimize the tab bar.
- [onScrollDown](tabbarminimizebehavior/onscrolldown.md) — Minimize the tab bar when downwards scrolling starts. Minimizing is supported for tab bars on only iPhone.
- [onScrollUp](tabbarminimizebehavior/onscrollup.md) — Minimize the tab bar when upwards scrolling starts. Minimizing is supported for tab bars on only iPhone.

## See Also

### Configuring a tab bar

- [defaultAdaptableTabBarPlacement(_:)](<view/defaultadaptabletabbarplacement(__).md>) — Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.
- [defaultTabBarPlacement(_:)](<view/defaulttabbarplacement(__).md>) — Specifies the preferred placement for the tabs of a [TabView](tabview.md) in the [sidebarAdaptable](tabviewstyle/sidebaradaptable.md) style on platforms where the tab bar cannot adapt between different representations, and only one representation can be shown. _(beta)_
- [tabViewSidebarHeader(content:)](<view/tabviewsidebarheader(content_).md>) — Adds a custom header to the sidebar of a tab view.
- [tabViewSidebarFooter(content:)](<view/tabviewsidebarfooter(content_).md>) — Adds a custom footer to the sidebar of a tab view.
- [tabViewSidebarBottomBar(content:)](<view/tabviewsidebarbottombar(content_).md>) — Adds a custom bottom bar to the sidebar of a tab view.
- [AdaptableTabBarPlacement](adaptabletabbarplacement.md) — A placement for tabs in a tab view using the adaptable sidebar style.
- [tabBarPlacement](environmentvalues/tabbarplacement.md) — The current placement of the tab bar.
- [TabBarPlacement](tabbarplacement.md) — A placement for tabs in a tab view.
- [isTabBarShowingSections](environmentvalues/istabbarshowingsections.md) — A Boolean value that determines whether a tab view shows the expanded contents of a tab section.
- [tabBarMinimizeBehavior(_:)](<view/tabbarminimizebehavior(__).md>) — Sets the behavior for tab bar minimization.
- [TabViewBottomAccessoryPlacement](tabviewbottomaccessoryplacement.md) — A placement of the bottom accessory in a tab view. You can use this to adjust the content of the accessory view based on the placement.
