---
title: 'tryMap(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/just/trymap(_:)'
source_url: 'https://developer.apple.com/documentation/combine/just/trymap(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/just/trymap%28_%3A%29.json'
content_hash: 'sha256:e64ff29a2d5bc5a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Just](../just.md)

# tryMap(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryMap<T>(_ transform: (Output) throws -> T) -> Result<T, any Error>.Publisher
```

## See Also

### Mapping elements

- [map(_:)](<map(__).md>)
- [mapError(_:)](<maperror(__).md>)
- [scan(_:_:)](<scan(____).md>)
- [tryScan(_:_:)](<tryscan(____).md>)
- [setFailureType(to:)](<setfailuretype(to_).md>)
