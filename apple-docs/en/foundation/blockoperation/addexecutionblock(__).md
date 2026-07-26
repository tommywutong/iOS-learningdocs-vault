---
title: 'addExecutionBlock(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/blockoperation/addexecutionblock(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/blockoperation/addexecutionblock(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/blockoperation/addexecutionblock%28_%3A%29.json'
content_hash: 'sha256:dcf758bdff8115d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [BlockOperation](../blockoperation.md)

# addExecutionBlock(_:)

<sub>Instance Method</sub>

Adds the specified block to the receiver’s list of blocks to perform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addExecutionBlock(_ block: @escaping @Sendable () -> Void)
```

## Parameters

- `block` — The block to add to the receiver’s list. The block should take no parameters and have no return value.

## Discussion

The specified block should not make any assumptions about its execution environment.

Calling this method while the receiver is executing or has already finished causes an `NSInvalidArgumentException` exception to be thrown.

## See Also

### Managing the Blocks in the Operation

- [+ blockOperationWithBlock:](<init(block_).md>) — Creates and returns an `NSBlockOperation` object and adds the specified block to it.
- [executionBlocks](executionblocks.md) — The blocks associated with the receiver.
