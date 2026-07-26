---
title: 'AsyncStream.Continuation.YieldResult.dropped(_:)'
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncstream/continuation/yieldresult/dropped(_:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncstream/continuation/yieldresult/dropped(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncstream/continuation/yieldresult/dropped%28_%3A%29.json'
content_hash: 'sha256:c14fa607fc369e9f'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [AsyncStream](../../../asyncstream.md) · [Continuation](../../continuation.md) · [YieldResult](../yieldresult.md)

# AsyncStream.Continuation.YieldResult.dropped(_:)

<sub>Case</sub>

The stream didn’t enqueue the element because the buffer was full.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case dropped(Element)
```

## Discussion

The associated element for this case is the element dropped by the stream.

## See Also

### Yield Results

- [AsyncStream.Continuation.YieldResult.enqueued(remaining:)](<enqueued(remaining_).md>) — The stream successfully enqueued the element.
- [AsyncStream.Continuation.YieldResult.terminated](terminated.md) — The stream didn’t enqueue the element because the stream was in a terminal state.
