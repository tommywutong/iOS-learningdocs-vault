---
title: 'updateNSView(_:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nsviewrepresentable/updatensview(_:context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewrepresentable/updatensview(_:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewrepresentable/updatensview%28_%3Acontext%3A%29.json'
content_hash: 'sha256:23e135a7b3a56a34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSViewRepresentable](../nsviewrepresentable.md)

# updateNSView(_:context:)

<sub>Instance Method</sub>

Updates the state of the specified view with new information from SwiftUI.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func updateNSView(_ nsView: Self.NSViewType, context: Self.Context)
```

## Parameters

- `nsView` — Your custom view object.

- `context` — A context structure containing information about the current state of the system.

## Discussion

When the state of your app changes, SwiftUI updates the portions of your interface affected by those changes. SwiftUI calls this method for any changes affecting the corresponding AppKit view. Use this method to update the configuration of your view to match the new state information provided in the `context` parameter.

## See Also

### Creating and updating the view

- [makeNSView(context:)](<makensview(context_).md>) — Creates the view object and configures its initial state.
- [Context](context.md)
- [NSViewType](nsviewtype.md) — The type of view to present.
