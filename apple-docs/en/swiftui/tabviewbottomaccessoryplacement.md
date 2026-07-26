---
title: TabViewBottomAccessoryPlacement
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabviewbottomaccessoryplacement
source_url: 'https://developer.apple.com/documentation/swiftui/tabviewbottomaccessoryplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabviewbottomaccessoryplacement.json'
content_hash: 'sha256:bd0e4cd032ff2e39'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TabViewBottomAccessoryPlacement

<sub>Enumeration</sub>

A placement of the bottom accessory in a tab view. You can use this to adjust the content of the accessory view based on the placement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum TabViewBottomAccessoryPlacement
```

## Overview

The following example shows playback controls when the view is inline, and an expanded slider player view when the view is expanded.

```swift
struct MusicPlaybackView: View {
    @Environment(\.tabViewBottomAccessoryPlacement) var placement

    var body: some View {
        switch placement {
        case .inline:
            ControlsPlaybackView()
        case .expanded:
            SliderPlaybackView()
    }
}
```

You can set the `TabView` bottom accessory using [tabViewBottomAccessory(content:)](<view/tabviewbottomaccessory(content_).md>)

```swift
TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }

    Tab("Alerts", systemImage: "bell") {
        AlertsView()
    }

    TabSection("Categories") {
        Tab("Climate", systemImage: "fan") {
            ClimateView()
        }

        Tab("Lights", systemImage: "lightbulb") {
            LightsView()
        }
    }
}
.tabViewBottomAccessory {
    HomeStatusView()
}
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [TabViewBottomAccessoryPlacement.expanded](tabviewbottomaccessoryplacement/expanded.md) — The bar is expanded on top of the bottom tab bar, if there is a bottom tab bar, or at the bottom of the tab’s content view.
- [TabViewBottomAccessoryPlacement.inline](tabviewbottomaccessoryplacement/inline.md) — The view is displayed in line with the bottom tab bar.

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
- [TabBarMinimizeBehavior](tabbarminimizebehavior.md)
