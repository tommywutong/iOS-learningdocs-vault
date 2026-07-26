---
title: isScrollEnabled
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/isscrollenabled
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/isscrollenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/isscrollenabled.json'
content_hash: 'sha256:a0a24d66c5b58bb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# isScrollEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether any scroll views associated with this environment allow scrolling to occur.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isScrollEnabled: Bool { get set }
```

## Discussion

The default value is `true`. Use the [scrollDisabled(_:)](<../view/scrolldisabled(__).md>) modifier to configure this property.

## See Also

### Disabling scrolling

- [scrollDisabled(_:)](<../view/scrolldisabled(__).md>) — Disables or enables scrolling in scrollable views.
