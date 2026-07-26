---
title: 'accessibilityAction(named:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/modifiedcontent/accessibilityaction(named:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilityaction(named:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibilityaction%28named%3A_%3A%29.json'
content_hash: 'sha256:e0af36b0a71e80cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibilityAction(named:_:)

<sub>Instance Method</sub>

Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func accessibilityAction(named nameResource: LocalizedStringResource, _ handler: @escaping () -> Void) -> ModifiedContent<Content, Modifier>
```

## Discussion

For example, this is how a custom action to compose a new email could be added to a view.

```swift
var body: some View {
    ContentView()
        .accessibilityAction(named: "New Message") {
            // Handle action
        }
}
```
