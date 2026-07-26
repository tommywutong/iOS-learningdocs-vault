---
title: 'makeNSViewController(context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nsviewcontrollerrepresentable/makensviewcontroller(context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentable/makensviewcontroller(context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewcontrollerrepresentable/makensviewcontroller%28context%3A%29.json'
content_hash: 'sha256:37a610ce4ae13ded'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSViewControllerRepresentable](../nsviewcontrollerrepresentable.md)

# makeNSViewController(context:)

<sub>Instance Method</sub>

Creates the view controller object and configures its initial state.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func makeNSViewController(context: Self.Context) -> Self.NSViewControllerType
```

## Parameters

- `context` — A context structure containing information about the current state of the system.

## Return Value

Your AppKit view controller configured with the provided information.

## Discussion

You must implement this method and use it to create your view controller object. Create the view controller using your app’s current data and contents of the `context` parameter. The system calls this method only once, when it creates your view controller for the first time. For all subsequent updates, the system calls the [updateNSViewController(_:context:)](<updatensviewcontroller(__context_).md>) method.

## See Also

### Creating and updating the view controller

- [updateNSViewController(_:context:)](<updatensviewcontroller(__context_).md>) — Updates the state of the specified view controller with new information from SwiftUI.
- [Context](context.md)
- [NSViewControllerType](nsviewcontrollertype.md) — The type of view controller to present.
