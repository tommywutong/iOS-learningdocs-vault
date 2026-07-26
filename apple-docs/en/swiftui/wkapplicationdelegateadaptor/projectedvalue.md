---
title: projectedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/wkapplicationdelegateadaptor/projectedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/wkapplicationdelegateadaptor/projectedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkapplicationdelegateadaptor/projectedvalue.json'
content_hash: 'sha256:6492ddacc2f95d24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WKApplicationDelegateAdaptor](../wkapplicationdelegateadaptor.md)

# projectedValue

<sub>Instance Property</sub>

A projection of the observed object that creates bindings to its properties using dynamic member lookup.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency var projectedValue: ObservedObject<DelegateType>.Wrapper { get }
```

## Discussion

Use the projected value to pass a binding value down a view hierarchy. To get the `projectedValue`, prefix the property variable with `$`.

## See Also

### Getting the delegate adaptor

- [wrappedValue](wrappedvalue.md) — The underlying delegate.
