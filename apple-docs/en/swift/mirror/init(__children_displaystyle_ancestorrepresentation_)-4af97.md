---
title: 'init(_:children:displayStyle:ancestorRepresentation:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mirror/init(_:children:displaystyle:ancestorrepresentation:)-4af97'
source_url: 'https://developer.apple.com/documentation/swift/mirror/init(_:children:displaystyle:ancestorrepresentation:)-4af97'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mirror/init%28_%3Achildren%3Adisplaystyle%3Aancestorrepresentation%3A%29-4af97.json'
content_hash: 'sha256:34362ebf5485b565'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Mirror](../mirror.md)

# init(_:children:displayStyle:ancestorRepresentation:)

<sub>Initializer</sub>

Creates a mirror representing the given subject with a specified structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Subject, C>(_ subject: Subject, children: C, displayStyle: Mirror.DisplayStyle? = nil, ancestorRepresentation: Mirror.AncestorRepresentation = .generated) where C : Collection, C.Element == (label: String?, value: Any)
```

## Parameters

- `subject` — The instance to represent in the new mirror.

- `children` — The structure to use for the mirror. The collection traversal modeled by `children` is captured so that the resulting mirror’s children may be upgraded to a bidirectional or random access collection later. See the `children` property for details.

- `displayStyle` — The preferred display style for the mirror when presented in the debugger or in a playground. The default is `nil`.

- `ancestorRepresentation` — The means of generating the subject’s ancestor representation. `ancestorRepresentation` is ignored if `subject` is not a class instance. The default is `.generated`.

## Discussion

You use this initializer from within your type’s `customMirror` implementation to create a customized mirror.

If `subject` is a class instance, `ancestorRepresentation` determines whether ancestor classes will be represented and whether their `customMirror` implementations will be used. By default, the `customMirror` implementation of any ancestors is ignored. To prevent bypassing customized ancestors, pass `.customized({ super.customMirror })` as the `ancestorRepresentation` parameter when implementing your type’s `customMirror` property.
