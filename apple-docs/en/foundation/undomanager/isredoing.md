---
title: isRedoing
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/isredoing
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/isredoing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/isredoing.json'
content_hash: 'sha256:707aff2fcc783774'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# isRedoing

<sub>Instance Property</sub>

Returns a Boolean value that indicates whether the manager is in the process of performing a redo action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isRedoing: Bool { get }
```

## Discussion

The value is [true](../../swift/true.md) if the manager is performing its [- redo](<redo().md>) method, otherwise [false](../../swift/false.md).

## See Also

### Checking whether undo or redo is in process

- [undoing](isundoing.md) — Returns a Boolean value that indicates whether the manager is in the process of performing an undo action.
