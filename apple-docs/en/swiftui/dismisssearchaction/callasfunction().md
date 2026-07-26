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
doc_path: /documentation/swiftui/dismisssearchaction/callasfunction()
source_url: 'https://developer.apple.com/documentation/swiftui/dismisssearchaction/callasfunction()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dismisssearchaction/callasfunction%28%29.json'
content_hash: 'sha256:5e1a038d4b455f08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DismissSearchAction](../dismisssearchaction.md)

# callAsFunction()

<sub>Instance Method</sub>

Dismisses the current search operation, if any.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func callAsFunction()
```

## Discussion

Don’t call this method directly. SwiftUI calls it for you when you call the [DismissSearchAction](../dismisssearchaction.md) structure that you get from the [Environment](../environment.md):

```swift
struct SearchedView: View {
    @Environment(\.dismissSearch) private var dismissSearch

    var body: some View {
        Button("Cancel") {
            dismissSearch() // Implicitly calls dismissSearch.callAsFunction()
        }
    }
}
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in _The Swift Programming Language_.
