---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/result/publisher-swift.struct/init(_:)-7t2tt'
source_url: 'https://developer.apple.com/documentation/swift/result/publisher-swift.struct/init(_:)-7t2tt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/result/publisher-swift.struct/init%28_%3A%29-7t2tt.json'
content_hash: 'sha256:5158e0c966e37f54'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Result](../../result.md) · [Publisher](../publisher-swift.struct.md)

# init(_:)

<sub>Initializer</sub>

Creates a publisher that sends the specified output to all subscribers and finishes normally.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ output: Result<Success, Failure>.Publisher.Output)
```

## Parameters

- `output` — The output to deliver to each subscriber.

## See Also

### Creating a Result Publisher

- [init(_:)](<init(__)-516t.md>) — Creates a publisher that delivers the specified result.
- [init(_:)](<init(__)-69fv4.md>) — Creates a publisher that immediately terminates upon subscription with the given failure.
