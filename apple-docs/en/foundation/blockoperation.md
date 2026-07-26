---
title: BlockOperation
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/blockoperation
source_url: 'https://developer.apple.com/documentation/foundation/blockoperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/blockoperation.json'
content_hash: 'sha256:5043c1551151d44a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# BlockOperation

<sub>Class</sub>

An operation that manages the concurrent execution of one or more blocks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class BlockOperation
```

## Overview

The [BlockOperation](blockoperation.md) class is a concrete subclass of [Operation](operation.md) that manages the concurrent execution of one or more blocks. You can use this object to execute several blocks at once without having to create separate operation objects for each. When executing more than one block, the operation itself is considered finished only when all blocks have finished executing.

Blocks added to a block operation are dispatched with default priority to an appropriate work queue. The blocks themselves should not make any assumptions about the configuration of their execution environment.

For more information about blocks, see [Blocks Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Blocks/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40007502).

## Relationships

- **Inherits From**: [Operation](operation.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Managing the Blocks in the Operation

- [+ blockOperationWithBlock:](<blockoperation/init(block_).md>) — Creates and returns an `NSBlockOperation` object and adds the specified block to it.
- [- addExecutionBlock:](<blockoperation/addexecutionblock(__).md>) — Adds the specified block to the receiver’s list of blocks to perform.
- [executionBlocks](blockoperation/executionblocks.md) — The blocks associated with the receiver.

## See Also

### Operations

- [OperationQueue](operationqueue.md) — A queue that regulates the execution of operations.
- [Operation](operation.md) — An abstract class that represents the code and data associated with a single task.
