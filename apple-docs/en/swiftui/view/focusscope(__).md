---
title: 'focusScope(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 12.0+, tvOS 14.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/focusscope(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/focusscope(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/focusscope%28_%3A%29.json'
content_hash: 'sha256:17ea994337de890c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# focusScope(_:)

<sub>Instance Method</sub>

Creates a focus scope that SwiftUI uses to limit default focus preferences.

<sub>macOS, tvOS, watchOS</sub>

```swift
nonisolated func focusScope(_ namespace: Namespace.ID) -> some View

```

## Parameters

- `namespace` — A namespace identifier that SwiftUI can use to scope default focus preferences.

## Return Value

A view that sets the namespace of descendants for default focus.

## Discussion

The returned view gets associated with the provided namespace. Pass this namespace to [prefersDefaultFocus(_:in:)](<prefersdefaultfocus(__in_).md>) and the [resetFocus](../environmentvalues/resetfocus.md) function.

## See Also

### Setting focus scope

- [focusSection()](<focussection().md>) — Indicates that the view’s frame and cohort of focusable descendants should be used to guide focus movement.
