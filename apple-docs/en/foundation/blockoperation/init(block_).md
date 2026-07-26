---
title: 'init(block:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/blockoperation/init(block:)'
source_url: 'https://developer.apple.com/documentation/foundation/blockoperation/init(block:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/blockoperation/init%28block%3A%29.json'
content_hash: 'sha256:233632899d9624ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [BlockOperation](../blockoperation.md)

# init(block:)

<sub>Initializer</sub>

Creates and returns an `NSBlockOperation` object and adds the specified block to it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(block: @escaping @Sendable () -> Void)
```

## Parameters

- `block` — The block to add to the new block operation object’s list. The block should take no parameters and have no return value.

## Return Value

A new block operation object.

## See Also

### Related Documentation

- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)

### Managing the Blocks in the Operation

- [- addExecutionBlock:](<addexecutionblock(__).md>) — Adds the specified block to the receiver’s list of blocks to perform.
- [executionBlocks](executionblocks.md) — The blocks associated with the receiver.
