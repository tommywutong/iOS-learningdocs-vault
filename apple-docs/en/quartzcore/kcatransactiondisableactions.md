---
title: kCATransactionDisableActions
framework: Core Animation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/kcatransactiondisableactions
source_url: 'https://developer.apple.com/documentation/quartzcore/kcatransactiondisableactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/kcatransactiondisableactions.json'
content_hash: 'sha256:78a2cb49cee48eb6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# kCATransactionDisableActions

<sub>Global Variable</sub>

A key whose value indicates whether implicit actions for property changes made within the transaction group are suppressed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let kCATransactionDisableActions: String
```

## Discussion

If [true](../swift/true.md), implicit actions for property changes made within the transaction group are suppressed.  The value for this key must be an instance of [NSNumber](../foundation/nsnumber.md).

## See Also

### Constants

- [kCATransactionAnimationDuration](kcatransactionanimationduration.md) — Duration, in seconds, for animations triggered within the transaction group.
- [kCATransactionAnimationTimingFunction](kcatransactionanimationtimingfunction.md)
- [kCATransactionCompletionBlock](kcatransactioncompletionblock.md)
