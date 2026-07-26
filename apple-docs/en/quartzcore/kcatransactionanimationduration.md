---
title: kCATransactionAnimationDuration
framework: Core Animation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/kcatransactionanimationduration
source_url: 'https://developer.apple.com/documentation/quartzcore/kcatransactionanimationduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/kcatransactionanimationduration.json'
content_hash: 'sha256:33e1dd6ba508f105'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# kCATransactionAnimationDuration

<sub>Global Variable</sub>

Duration, in seconds, for animations triggered within the transaction group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let kCATransactionAnimationDuration: String
```

## Discussion

The value for this key must be an instance of [NSNumber](../foundation/nsnumber.md).

## See Also

### Constants

- [kCATransactionDisableActions](kcatransactiondisableactions.md) — A key whose value indicates whether implicit actions for property changes made within the transaction group are suppressed.
- [kCATransactionAnimationTimingFunction](kcatransactionanimationtimingfunction.md)
- [kCATransactionCompletionBlock](kcatransactioncompletionblock.md)
