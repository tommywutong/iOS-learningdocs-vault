---
title: 'scan(_:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/just/scan(_:_:)'
source_url: 'https://developer.apple.com/documentation/combine/just/scan(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/just/scan%28_%3A_%3A%29.json'
content_hash: 'sha256:2c3a8e3e241595b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Just](../just.md)

# scan(_:_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scan<T>(_ initialResult: T, _ nextPartialResult: (T, Output) -> T) -> Result<T, Just<Output>.Failure>.Publisher
```

## See Also

### Mapping elements

- [map(_:)](<map(__).md>)
- [tryMap(_:)](<trymap(__).md>)
- [mapError(_:)](<maperror(__).md>)
- [tryScan(_:_:)](<tryscan(____).md>)
- [setFailureType(to:)](<setfailuretype(to_).md>)
