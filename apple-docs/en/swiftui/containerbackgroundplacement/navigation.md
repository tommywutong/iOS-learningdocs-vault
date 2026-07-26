---
title: navigation
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/containerbackgroundplacement/navigation
source_url: 'https://developer.apple.com/documentation/swiftui/containerbackgroundplacement/navigation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/containerbackgroundplacement/navigation.json'
content_hash: 'sha256:ddf1766931731cf6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContainerBackgroundPlacement](../containerbackgroundplacement.md)

# navigation

<sub>Type Property</sub>

A background placement inside a [NavigationStack](../navigationstack.md) or [NavigationSplitView](../navigationsplitview.md).

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
static let navigation: ContainerBackgroundPlacement
```

## Discussion

For translucent backgrounds in a navigation split view, combine this placement with [navigationSplitView](navigationsplitview.md).

```swift
NavigationSplitView {
     … sidebar …
    .containerBackground(.thinMaterial, for: .navigation)
    .containerBackground(Color.green, for: .navigationSplitView)
} detail: {
    // … detail …
    .containerBackground(.thickMaterial, for: .navigation)
}
```

## See Also

### Getting placements

- [tabView](tabview.md) — A background placement inside a [TabView](../tabview.md).
- [widget](widget.md) — The container background placement for a widget.
