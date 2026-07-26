---
title: 'objc_duplicateClass(_:_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_duplicateclass(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_duplicateclass(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_duplicateclass%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:5041e076c1d7cbe5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_duplicateClass(_:_:_:)

<sub>Function</sub>

Used by Foundation’s Key-Value Observing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_duplicateClass(_ original: AnyClass, _ name: UnsafePointer<CChar>, _ extraBytes: Int) -> AnyClass
```

## Discussion

Do not call this function yourself.

## See Also

### Adding Classes

- [objc_allocateClassPair](<objc_allocateclasspair(______).md>) — Creates a new class and metaclass.
- [objc_disposeClassPair](<objc_disposeclasspair(__).md>) — Destroys a class and its associated metaclass.
- [objc_registerClassPair](<objc_registerclasspair(__).md>) — Registers a class that was allocated using [objc_allocateClassPair](<objc_allocateclasspair(______).md>).
