---
title: executionBlocks
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/blockoperation/executionblocks
source_url: 'https://developer.apple.com/documentation/foundation/blockoperation/executionblocks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/blockoperation/executionblocks.json'
content_hash: 'sha256:849dc8eb8e4441fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [BlockOperation](../blockoperation.md)

# executionBlocks

<sub>Instance Property</sub>

The blocks associated with the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var executionBlocks: [@Sendable () -> Void] { get }
```

## Discussion

The blocks in this array are copies of those originally added using the [- addExecutionBlock:](<addexecutionblock(__).md>) method.

## See Also

### Managing the Blocks in the Operation

- [+ blockOperationWithBlock:](<init(block_).md>) — Creates and returns an `NSBlockOperation` object and adds the specified block to it.
- [- addExecutionBlock:](<addexecutionblock(__).md>) — Adds the specified block to the receiver’s list of blocks to perform.
