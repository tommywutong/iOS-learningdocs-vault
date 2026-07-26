---
title: isEnabled
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/isenabled
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/isenabled.json'
content_hash: 'sha256:6388708353fced67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the view associated with this environment allows user interaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEnabled: Bool { get set }
```

## Discussion

The default value is `true`.

## See Also

### Managing view interaction

- [disabled(_:)](<../view/disabled(__).md>) — Adds a condition that controls whether users can interact with this view.
- [interactionActivityTrackingTag(_:)](<../view/interactionactivitytrackingtag(__).md>) — Sets a tag that you use for tracking interactivity.
- [invalidatableContent(_:)](<../view/invalidatablecontent(__).md>) — Mark the receiver as their content might be invalidated.
