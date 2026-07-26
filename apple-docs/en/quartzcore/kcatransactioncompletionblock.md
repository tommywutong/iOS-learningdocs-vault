---
title: kCATransactionCompletionBlock
framework: Core Animation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/kcatransactioncompletionblock
source_url: 'https://developer.apple.com/documentation/quartzcore/kcatransactioncompletionblock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/kcatransactioncompletionblock.json'
content_hash: 'sha256:5ad75dddf4a94fe9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# kCATransactionCompletionBlock

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let kCATransactionCompletionBlock: String
```

## Discussion

A completion block object that is guaranteed to be called (on the main thread) as soon as all animations subsequently added by this transaction group have completed (or have been removed.) If no animations are added before the current transaction group is committed (or the completion block is set to a different value,) the block will be invoked immediately.

## See Also

### Constants

- [kCATransactionAnimationDuration](kcatransactionanimationduration.md) — Duration, in seconds, for animations triggered within the transaction group.
- [kCATransactionDisableActions](kcatransactiondisableactions.md) — A key whose value indicates whether implicit actions for property changes made within the transaction group are suppressed.
- [kCATransactionAnimationTimingFunction](kcatransactionanimationtimingfunction.md)
