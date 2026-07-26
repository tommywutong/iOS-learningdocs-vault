---
title: isPresented
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/ispresented
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/ispresented'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/ispresented.json'
content_hash: 'sha256:3d235dc124c17483'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# isPresented

<sub>Instance Property</sub>

A Boolean value that indicates whether the view associated with this environment is currently presented.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isPresented: Bool { get }
```

## Discussion

You can read this value like any of the other [EnvironmentValues](../environmentvalues.md) by creating a property with the [Environment](../environment.md) property wrapper:

```swift
@Environment(\.isPresented) private var isPresented
```

Read the value inside a view if you need to know when SwiftUI presents that view. For example, you can take an action when SwiftUI presents a view by using the [onChange(of:initial:_:)](<../view/onchange(of_initial___).md>) modifier:

```swift
.onChange(of: isPresented) { _, isPresented in
    if isPresented {
        // Do something when first presented.
    }
}
```

This behaves differently than [onAppear(perform:)](<../view/onappear(perform_).md>), which SwiftUI can call more than once for a given presentation, like when you navigate back to a view that’s already in the navigation hierarchy.

To dismiss the currently presented view, use [dismiss](dismiss.md).

## See Also

### Dismissing a presentation

- [dismiss](dismiss.md) — An action that dismisses the current presentation.
- [DismissAction](../dismissaction.md) — An action that dismisses a presentation.
- [interactiveDismissDisabled(_:)](<../view/interactivedismissdisabled(__).md>) — Conditionally prevents interactive dismissal of presentations like popovers, sheets, and inspectors.
