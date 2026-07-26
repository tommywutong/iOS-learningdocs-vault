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
doc_path: '/documentation/swift/result/publisher-swift.struct/init(_:)-516t'
source_url: 'https://developer.apple.com/documentation/swift/result/publisher-swift.struct/init(_:)-516t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/result/publisher-swift.struct/init%28_%3A%29-516t.json'
content_hash: 'sha256:e67c4b4fd94dcce8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Result](../../result.md) · [Publisher](../publisher-swift.struct.md)

# init(_:)

<sub>Initializer</sub>

Creates a publisher that delivers the specified result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ result: Result<Result<Success, Failure>.Publisher.Output, Failure>)
```

## Parameters

- `result` — The result to deliver to each subscriber.

## Discussion

If `result` is `Swift/Result/success`, then the publisher waits until it receives a request for at least one value, then sends the output to all subscribers and finishes normally. If `result` is `Swift/Result/failure`, then the publisher sends the failure immediately upon subscription.

## See Also

### Creating a Result Publisher

- [init(_:)](<init(__)-69fv4.md>) — Creates a publisher that immediately terminates upon subscription with the given failure.
- [init(_:)](<init(__)-7t2tt.md>) — Creates a publisher that sends the specified output to all subscribers and finishes normally.
