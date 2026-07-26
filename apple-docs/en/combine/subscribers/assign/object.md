---
title: object
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/subscribers/assign/object
source_url: 'https://developer.apple.com/documentation/combine/subscribers/assign/object'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/assign/object.json'
content_hash: 'sha256:221622c0244e7f8a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Subscribers](../../subscribers.md) · [Assign](../assign.md)

# object

<sub>Instance Property</sub>

The object that contains the property to assign.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var object: Root? { get }
```

## Discussion

The subscriber holds a strong reference to this object until the upstream publisher calls [receive(completion:)](<../../subscriber/receive(completion_).md>), at which point the subscriber sets this property to `nil`.

## See Also

### Inspecting the assigned property

- [keyPath](keypath.md) — The key path that indicates the property to assign.
