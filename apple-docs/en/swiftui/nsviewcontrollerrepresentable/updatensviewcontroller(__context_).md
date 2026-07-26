---
title: 'updateNSViewController(_:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nsviewcontrollerrepresentable/updatensviewcontroller(_:context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentable/updatensviewcontroller(_:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewcontrollerrepresentable/updatensviewcontroller%28_%3Acontext%3A%29.json'
content_hash: 'sha256:7da62d36a3985f2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSViewControllerRepresentable](../nsviewcontrollerrepresentable.md)

# updateNSViewController(_:context:)

<sub>Instance Method</sub>

Updates the state of the specified view controller with new information from SwiftUI.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func updateNSViewController(_ nsViewController: Self.NSViewControllerType, context: Self.Context)
```

## Parameters

- `nsViewController` — Your custom view controller object.

- `context` — A context structure containing information about the current state of the system.

## Discussion

When the state of your app changes, SwiftUI updates the portions of your interface affected by those changes. SwiftUI calls this method for any changes affecting the corresponding AppKit view controller. Use this method to update the configuration of your view controller to match the new state information provided in the `context` parameter.

## See Also

### Creating and updating the view controller

- [makeNSViewController(context:)](<makensviewcontroller(context_).md>) — Creates the view controller object and configures its initial state.
- [Context](context.md)
- [NSViewControllerType](nsviewcontrollertype.md) — The type of view controller to present.
