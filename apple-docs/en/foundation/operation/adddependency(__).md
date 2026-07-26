---
title: 'addDependency(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/operation/adddependency(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/operation/adddependency(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operation/adddependency%28_%3A%29.json'
content_hash: 'sha256:c29d60322a2fa8dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Operation](../operation.md)

# addDependency(_:)

<sub>Instance Method</sub>

Makes the receiver dependent on the completion of the specified operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addDependency(_ op: Operation)
```

## Parameters

- `op` — The operation on which the receiver should depend. The same dependency should not be added more than once to the receiver, and the results of doing so are undefined.

## Discussion

The receiver is not considered ready to execute until all of its dependent operations have finished executing. If the receiver is already executing its task, adding dependencies has no practical effect. This method may change the `isReady` and `dependencies` properties of the receiver.

It is a programmer error to create any circular dependencies among a set of operations. Doing so can cause a deadlock among the operations and may freeze your program.

## See Also

### Managing Dependencies

- [- removeDependency:](<removedependency(__).md>) — Removes the receiver’s dependence on the specified operation.
- [dependencies](dependencies.md) — An array of the operation objects that must finish executing before the current object can begin executing.
