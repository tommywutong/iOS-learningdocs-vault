---
title: CustomPresentationDetent
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/custompresentationdetent
source_url: 'https://developer.apple.com/documentation/swiftui/custompresentationdetent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/custompresentationdetent.json'
content_hash: 'sha256:6ce980b84a255c4f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# CustomPresentationDetent

<sub>Protocol</sub>

The definition of a custom detent with a calculated height.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol CustomPresentationDetent
```

## Overview

You can create and use a custom detent with built-in detents.

```swift
extension PresentationDetent {
    static let bar = Self.custom(BarDetent.self)
    static let small = Self.height(100)
    static let extraLarge = Self.fraction(0.75)
}

private struct BarDetent: CustomPresentationDetent {
    static func height(in context: Context) -> CGFloat? {
        max(44, context.maxDetentValue * 0.1)
    }
}

struct ContentView: View {
    @State private var showSettings = false
    @State private var selectedDetent = PresentationDetent.bar

    var body: some View {
        Button("View Settings") {
            showSettings = true
        }
        .sheet(isPresented: $showSettings) {
            SettingsView(selectedDetent: $selectedDetent)
                .presentationDetents(
                    [.bar, .small, .medium, .large, .extraLarge],
                    selection: $selectedDetent)
        }
    }
}
```

## Topics

### Getting the height

- [height(in:)](<custompresentationdetent/height(in_).md>) — Calculates and returns a height based on the context.
- [Context](custompresentationdetent/context.md) — Information that you can use to calculate the height of a custom detent.

## See Also

### Configuring a sheet’s height

- [presentationDetents(_:)](<view/presentationdetents(__).md>) — Sets the available detents for the enclosing sheet.
- [presentationDetents(_:selection:)](<view/presentationdetents(__selection_).md>) — Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [presentationContentInteraction(_:)](<view/presentationcontentinteraction(__).md>) — Configures the behavior of swipe gestures on a presentation.
- [presentationDragIndicator(_:)](<view/presentationdragindicator(__).md>) — Sets the visibility of the drag indicator on top of a sheet.
- [PresentationDetent](presentationdetent.md) — A type that represents a height where a sheet naturally rests.
- [PresentationContentInteraction](presentationcontentinteraction.md) — A behavior that you can use to influence how a presentation responds to swipe gestures.
