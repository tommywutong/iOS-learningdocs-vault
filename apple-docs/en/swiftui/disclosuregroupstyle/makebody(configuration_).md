---
title: 'makeBody(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/disclosuregroupstyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/disclosuregroupstyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/disclosuregroupstyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:616b1f4da7dbe882'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DisclosureGroupStyle](../disclosuregroupstyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view that represents the body of a disclosure group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@ContentBuilder @MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

## Parameters

- `configuration` — The properties of the instance being created.

## Discussion

SwiftUI calls this method for each instance of [DisclosureGroup](../disclosuregroup.md) that you create within a view hierarchy where this style is the current [DisclosureGroupStyle](../disclosuregroupstyle.md).

## See Also

### Creating custom disclosure group styles

- [DisclosureGroupStyleConfiguration](../disclosuregroupstyleconfiguration.md) — The properties of a disclosure group instance.
- [Configuration](configuration.md) — The properties of a disclosure group instance.
- [Body](body.md) — A view that represents the body of a disclosure group.
