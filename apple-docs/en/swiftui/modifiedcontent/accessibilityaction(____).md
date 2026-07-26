---
title: 'accessibilityAction(_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/modifiedcontent/accessibilityaction(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilityaction(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibilityaction%28_%3A_%3A%29.json'
content_hash: 'sha256:bb1c3b0ca014a0bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibilityAction(_:_:)

<sub>Instance Method</sub>

Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityAction(_ actionKind: AccessibilityActionKind = .default, _ handler: @escaping () -> Void) -> ModifiedContent<Content, Modifier>
```

## Discussion

For example, this is how a `.default` action to compose a new email could be added to a view.

```swift
var body: some View {
    ContentView()
        .accessibilityAction {
            // Handle action
        }
}
```
