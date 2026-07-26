---
title: callAsFunction()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/refreshaction/callasfunction()
source_url: 'https://developer.apple.com/documentation/swiftui/refreshaction/callasfunction()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/refreshaction/callasfunction%28%29.json'
content_hash: 'sha256:c140da1f2d1a2799'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [RefreshAction](../refreshaction.md)

# callAsFunction()

<sub>Instance Method</sub>

Initiates a refresh action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func callAsFunction() async
```

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [RefreshAction](../refreshaction.md) structure that you get from the [Environment](../environment.md):

```swift
struct RefreshableView: View {
    @Environment(\.refresh) private var refresh

    var body: some View {
        Button("Refresh") {
            Task {
                await refresh?()  // Implicitly calls refresh.callAsFunction()
            }
        }
        .disabled(refresh == nil)
    }
}
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in _The Swift Programming Language_. For information about asynchronous operations in Swift, see [Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html).
