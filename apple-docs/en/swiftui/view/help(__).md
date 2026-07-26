---
title: 'help(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/help(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/help(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/help%28_%3A%29.json'
content_hash: 'sha256:91deea44eaa46ca1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# help(_:)

<sub>Instance Method</sub>

Adds help text to a view using a localized string resource that you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func help(_ textKey: LocalizedStringResource) -> some View

```

## Parameters

- `textKey` — Text resource for the localized text to use as help.

## Discussion

Adding help to a view configures the view’s accessibility hint and its help tag (also called a _tooltip_) in macOS or visionOS. For more information on using help tags, see [Offering help](../../design/human-interface-guidelines/offering-help.md) in the Human Interface Guidelines.

```swift
Button(action: composeMessage) {
    Image(systemName: "square.and.pencil")
}
.help("Compose a new message")
```
