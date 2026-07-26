---
title: next()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/throwingtaskgroup/next()
source_url: 'https://developer.apple.com/documentation/swift/throwingtaskgroup/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingtaskgroup/next%28%29.json'
content_hash: 'sha256:2178cdb83853dec5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ThrowingTaskGroup](../throwingtaskgroup.md)

# next()

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() async throws -> ChildTaskResult?
```

## See Also

### Accessing Individual Results

- [nextResult()](<nextresult().md>) — Wait for the next child task to complete, and return a result containing either the value that the child task returned or the error that it threw.
- [next(isolation:)](<next(isolation_).md>) — Wait for the next child task to complete, and return the value it returned or rethrow the error it threw.
- [isEmpty](isempty.md) — A Boolean value that indicates whether the group has any remaining tasks.
- [waitForAll()](<waitforall().md>) — Wait for all of the group’s remaining tasks to complete.
