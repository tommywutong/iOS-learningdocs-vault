---
title: isUndoing
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/isundoing
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/isundoing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/isundoing.json'
content_hash: 'sha256:b1a23e49fb735459'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# isUndoing

<sub>Instance Property</sub>

Returns a Boolean value that indicates whether the manager is in the process of performing an undo action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isUndoing: Bool { get }
```

## Discussion

The value is [true](../../swift/true.md) if the manager is performing its [- undo](<undo().md>) or [- undoNestedGroup](<undonestedgroup().md>) method, otherwise [false](../../swift/false.md).

## See Also

### Checking whether undo or redo is in process

- [redoing](isredoing.md) — Returns a Boolean value that indicates whether the manager is in the process of performing a redo action.
