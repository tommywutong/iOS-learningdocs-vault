---
title: WKApplicationDelegateAdaptor
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/wkapplicationdelegateadaptor
source_url: 'https://developer.apple.com/documentation/swiftui/wkapplicationdelegateadaptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkapplicationdelegateadaptor.json'
content_hash: 'sha256:9fd1c431ff3e8650'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WKApplicationDelegateAdaptor

<sub>Structure</sub>

A property wrapper that is used in `App` to provide a delegate from WatchKit.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency @propertyWrapper struct WKApplicationDelegateAdaptor<DelegateType> where DelegateType : NSObject, DelegateType : WKApplicationDelegate
```

## Relationships

- **Conforms To**: [DynamicProperty](dynamicproperty.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a delegate adaptor

- [init(_:)](<wkapplicationdelegateadaptor/init(__).md>) — Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application Delegate.

### Getting the delegate adaptor

- [projectedValue](wkapplicationdelegateadaptor/projectedvalue.md) — A projection of the observed object that creates bindings to its properties using dynamic member lookup.
- [wrappedValue](wkapplicationdelegateadaptor/wrappedvalue.md) — The underlying delegate.

## See Also

### Targeting watchOS

- [WKExtensionDelegateAdaptor](wkextensiondelegateadaptor.md) — A property wrapper type that you use to create a WatchKit extension delegate. _(deprecated)_
