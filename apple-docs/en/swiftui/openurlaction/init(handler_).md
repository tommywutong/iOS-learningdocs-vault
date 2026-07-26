---
title: 'init(handler:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/openurlaction/init(handler:)'
source_url: 'https://developer.apple.com/documentation/swiftui/openurlaction/init(handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/openurlaction/init%28handler%3A%29.json'
content_hash: 'sha256:8766b4d43abb9f9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [OpenURLAction](../openurlaction.md)

# init(handler:)

<sub>Initializer</sub>

Creates an action that opens a URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(handler: @escaping (URL) -> OpenURLAction.Result)
```

## Parameters

- `handler` — The closure to run for the given URL. The closure takes a URL as input, and returns a [Result](result.md) that indicates the outcome of the action.

## Discussion

Use this initializer to create a custom action for opening URLs. Provide a handler that takes a URL and returns an [Result](result.md). Place your handler in the environment using the [environment(_:_:)](<../view/environment(____).md>) view modifier:

```swift
Text("Visit [Example Company](https://www.example.com) for details.")
    .environment(\.openURL, OpenURLAction { url in
        handleURL(url) // Define this method to take appropriate action.
        return .handled
    })
```

Any views that read the action from the environment, including the built-in [Link](../link.md) view and [Text](../text.md) views with markdown links, or links in attributed strings, use your action.

SwiftUI translates the value that your custom action’s handler returns into an appropriate Boolean result for the action call. For example, a view that uses the action declared above receives `true` when calling the action, because the handler always returns [handled](result/handled.md).

## See Also

### Creating the action

- [Result](result.md) — The result of a custom open URL action.
