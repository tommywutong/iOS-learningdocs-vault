---
title: 'storeWhileEntityActive(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 26.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/cancellable/storewhileentityactive(_:)'
source_url: 'https://developer.apple.com/documentation/combine/cancellable/storewhileentityactive(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/cancellable/storewhileentityactive%28_%3A%29.json'
content_hash: 'sha256:dde344552fb489fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Cancellable](../cancellable.md)

# storeWhileEntityActive(_:)

<sub>Instance Method</sub>

Retains the `Cancellable` as long as the entity is active (see `Entity.isActive`). If the entity is deactivated, the `Cancellable` is released.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func storeWhileEntityActive(_ entity: Entity)
```

## Discussion

This method does nothing if the entity is already inactive.

Internally, this method stores an `AnyCancellable` in a transient component of the entity. The component is removed when the _deactivate_ event for this entity is received.
