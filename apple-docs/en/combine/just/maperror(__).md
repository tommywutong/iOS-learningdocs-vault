---
title: 'mapError(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/just/maperror(_:)'
source_url: 'https://developer.apple.com/documentation/combine/just/maperror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/just/maperror%28_%3A%29.json'
content_hash: 'sha256:4e195156e8045293'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Just](../just.md)

# mapError(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mapError<E>(_ transform: (Just<Output>.Failure) -> E) -> Result<Output, E>.Publisher where E : Error
```

## See Also

### Mapping elements

- [map(_:)](<map(__).md>)
- [tryMap(_:)](<trymap(__).md>)
- [scan(_:_:)](<scan(____).md>)
- [tryScan(_:_:)](<tryscan(____).md>)
- [setFailureType(to:)](<setfailuretype(to_).md>)
