---
title: wrappedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [watchOS 7.0+（9.2 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/wkextensiondelegateadaptor/wrappedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/wkextensiondelegateadaptor/wrappedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkextensiondelegateadaptor/wrappedvalue.json'
content_hash: 'sha256:b68c62550cb35be2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WKExtensionDelegateAdaptor](../wkextensiondelegateadaptor.md)

# wrappedValue

<sub>Instance Property</sub>

The underlying delegate.

> [!warning] Deprecated
> Use WKApplicationDelegateAdaptor with a WKApplicationDelegate instead.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency var wrappedValue: DelegateType { get }
```

## See Also

### Getting the delegate adaptor

- [projectedValue](projectedvalue.md) — A projection of the observed object that provides bindings to its properties. _(deprecated)_
