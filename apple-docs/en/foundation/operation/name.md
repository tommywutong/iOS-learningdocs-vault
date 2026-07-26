---
title: name
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operation/name
source_url: 'https://developer.apple.com/documentation/foundation/operation/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operation/name.json'
content_hash: 'sha256:d106e54de45b09a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Operation](../operation.md)

# name

<sub>Instance Property</sub>

The name of the operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var name: String? { get set }
```

## Discussion

Assign a name to the operation object to help identify it during debugging.

## See Also

### Getting the Operation Status

- [cancelled](iscancelled.md) — A Boolean value indicating whether the operation has been cancelled
- [executing](isexecuting.md) — A Boolean value indicating whether the operation is currently executing.
- [finished](isfinished.md) — A Boolean value indicating whether the operation has finished executing its task.
- [concurrent](isconcurrent.md) — A Boolean value indicating whether the operation executes its task asynchronously.
- [asynchronous](isasynchronous.md) — A Boolean value indicating whether the operation executes its task asynchronously.
- [ready](isready.md) — A Boolean value indicating whether the operation can be performed now.
