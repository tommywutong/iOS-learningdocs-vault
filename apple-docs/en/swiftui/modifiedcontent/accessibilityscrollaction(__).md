---
title: 'accessibilityScrollAction(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/modifiedcontent/accessibilityscrollaction(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilityscrollaction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibilityscrollaction%28_%3A%29.json'
content_hash: 'sha256:38d404481a9dc5e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibilityScrollAction(_:)

<sub>Instance Method</sub>

Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityScrollAction(_ handler: @escaping (Edge) -> Void) -> ModifiedContent<Content, Modifier>
```

## Discussion

For example, this is how a scroll action to trigger a refresh could be added to a view.

```swift
var body: some View {
    ScrollView {
        ContentView()
    }
    .accessibilityScrollAction { edge in
        if edge == .top {
            // Refresh content
        }
    }
}
```
