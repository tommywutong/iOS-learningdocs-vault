---
title: waitForAll()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/taskgroup/waitforall()
source_url: 'https://developer.apple.com/documentation/swift/taskgroup/waitforall()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/taskgroup/waitforall%28%29.json'
content_hash: 'sha256:938f27d413a37b2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [TaskGroup](../taskgroup.md)

# waitForAll()

<sub>Instance Method</sub>

Wait for all of the group’s remaining tasks to complete.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated(nonsending) mutating func waitForAll() async
```

## See Also

### Accessing Individual Results

- [next()](<next().md>)
- [next(isolation:)](<next(isolation_).md>) — Waits for the next child task to complete, and returns the value it returned.
- [isEmpty](isempty.md) — A Boolean value that indicates whether the group has any remaining tasks.
