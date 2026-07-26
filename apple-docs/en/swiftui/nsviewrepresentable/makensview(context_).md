---
title: 'makeNSView(context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nsviewrepresentable/makensview(context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewrepresentable/makensview(context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewrepresentable/makensview%28context%3A%29.json'
content_hash: 'sha256:9cee91040c3622af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSViewRepresentable](../nsviewrepresentable.md)

# makeNSView(context:)

<sub>Instance Method</sub>

Creates the view object and configures its initial state.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func makeNSView(context: Self.Context) -> Self.NSViewType
```

## Parameters

- `context` — A context structure containing information about the current state of the system.

## Return Value

Your AppKit view configured with the provided information.

## Discussion

You must implement this method and use it to create your view object. Configure the view using your app’s current data and contents of the `context` parameter. The system calls this method only once, when it creates your view for the first time. For all subsequent updates, the system calls the [updateNSView(_:context:)](<updatensview(__context_).md>) method.

## See Also

### Creating and updating the view

- [updateNSView(_:context:)](<updatensview(__context_).md>) — Updates the state of the specified view with new information from SwiftUI.
- [Context](context.md)
- [NSViewType](nsviewtype.md) — The type of view to present.
