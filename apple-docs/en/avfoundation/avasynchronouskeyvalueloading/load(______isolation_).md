---
title: 'load(_:_:_:isolation:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avasynchronouskeyvalueloading/load(_:_:_:isolation:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/load(_:_:_:isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronouskeyvalueloading/load%28_%3A_%3A_%3Aisolation%3A%29.json'
content_hash: 'sha256:4d5bf1f20ea6b62f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousKeyValueLoading](../avasynchronouskeyvalueloading.md)

# load(_:_:_:isolation:)

<sub>Instance Method</sub>

Loads two or more properties asynchronously and returns the values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: macOS 26.0, iOS 26.0, tvOS 26.0, watchOS 26.0, visionOS 26.0)
func load<A, B, each C>(_ firstProperty: AVAsyncProperty<Self, A>, _ secondProperty: AVAsyncProperty<Self, B>, _ properties: repeat AVAsyncProperty<Self, each C>, isolation: isolated (any Actor)? = #isolation) async throws -> (A, B, repeat each C)
```

## Parameters

- `firstProperty` — A property to load.

- `secondProperty` — A second property to load.

- `properties` — Additional properties to load.

- `isolation` — The isolation context.

## Return Value

The loaded properties in a tuple.

## Discussion

See the [load(_:isolation:)](<load(__isolation_).md>) method for more information.

## See Also

### Loading property values

- [load(_:isolation:)](<load(__isolation_).md>) — Loads a property asynchronously and returns the value.
