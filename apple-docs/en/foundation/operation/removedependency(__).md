---
title: 'removeDependency(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/operation/removedependency(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/operation/removedependency(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operation/removedependency%28_%3A%29.json'
content_hash: 'sha256:f8a3bf699c957c64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Operation](../operation.md)

# removeDependency(_:)

<sub>Instance Method</sub>

Removes the receiver’s dependence on the specified operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeDependency(_ op: Operation)
```

## Parameters

- `op` — The dependent operation to be removed from the receiver.

## Discussion

This method may change the `isReady` and `dependencies` properties of the receiver.

## See Also

### Managing Dependencies

- [- addDependency:](<adddependency(__).md>) — Makes the receiver dependent on the completion of the specified operation.
- [dependencies](dependencies.md) — An array of the operation objects that must finish executing before the current object can begin executing.
