---
title: 'objc_registerClassPair(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_registerclasspair(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_registerclasspair(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_registerclasspair%28_%3A%29.json'
content_hash: 'sha256:13d8f12940a31823'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_registerClassPair(_:)

<sub>Function</sub>

Registers a class that was allocated using [objc_allocateClassPair](<objc_allocateclasspair(______).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_registerClassPair(_ cls: AnyClass)
```

## Parameters

- `cls` — The class you want to register.

## See Also

### Adding Classes

- [objc_allocateClassPair](<objc_allocateclasspair(______).md>) — Creates a new class and metaclass.
- [objc_disposeClassPair](<objc_disposeclasspair(__).md>) — Destroys a class and its associated metaclass.
- [objc_duplicateClass](<objc_duplicateclass(______).md>) — Used by Foundation’s Key-Value Observing.
