---
title: 'makeBody(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/controlgroupstyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/controlgroupstyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlgroupstyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:3a58c96b22312027'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlGroupStyle](../controlgroupstyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view representing the body of a control group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@ContentBuilder @MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

## Parameters

- `configuration` — The properties of the control group instance being created.

## Discussion

This method will be called for each instance of [ControlGroup](../controlgroup.md) created within a view hierarchy where this style is the current `ControlGroupStyle`.

## See Also

### Creating custom control group styles

- [Configuration](configuration.md) — The properties of a `ControlGroup` instance being created.
- [Body](body.md) — A view representing the body of a control group.
