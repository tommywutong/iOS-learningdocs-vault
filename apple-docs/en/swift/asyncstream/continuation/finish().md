---
title: finish()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncstream/continuation/finish()
source_url: 'https://developer.apple.com/documentation/swift/asyncstream/continuation/finish()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncstream/continuation/finish%28%29.json'
content_hash: 'sha256:018b3e756b12748c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncStream](../../asyncstream.md) · [Continuation](../continuation.md)

# finish()

<sub>Instance Method</sub>

Resume the task awaiting the next iteration point by having it return nil, which signifies the end of the iteration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func finish()
```

## Discussion

Calling this function more than once has no effect. After calling finish, the stream enters a terminal state and doesn’t produce any additional elements.
