---
title: 'materialActiveAppearance(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/material/materialactiveappearance(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/material/materialactiveappearance(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/material/materialactiveappearance%28_%3A%29.json'
content_hash: 'sha256:9e55660b42c104bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Material](../material.md)

# materialActiveAppearance(_:)

<sub>Instance Method</sub>

Sets an explicit active appearance for this material.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func materialActiveAppearance(_ appearance: MaterialActiveAppearance) -> Material
```

## Discussion

Materials used as the `window` container background on macOS will automatically appear inactive when their the window appears inactive, but can be made to always appear active by setting the active appearance behavior to be always active:

```swift
Text("Hello, World!")
    .containerBackground(
        Material.regular.materialActiveAppearance(.active),
        for: .window)
```
