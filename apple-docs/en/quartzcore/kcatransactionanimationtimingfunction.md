---
title: kCATransactionAnimationTimingFunction
framework: Core Animation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/kcatransactionanimationtimingfunction
source_url: 'https://developer.apple.com/documentation/quartzcore/kcatransactionanimationtimingfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/kcatransactionanimationtimingfunction.json'
content_hash: 'sha256:78ccd8b58c2d57a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# kCATransactionAnimationTimingFunction

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let kCATransactionAnimationTimingFunction: String
```

## Discussion

An instance of [CAMediaTimingFunction](camediatimingfunction.md) that overrides the timing function for all animations triggered within the transaction group.

## See Also

### Constants

- [kCATransactionAnimationDuration](kcatransactionanimationduration.md) — Duration, in seconds, for animations triggered within the transaction group.
- [kCATransactionDisableActions](kcatransactiondisableactions.md) — A key whose value indicates whether implicit actions for property changes made within the transaction group are suppressed.
- [kCATransactionCompletionBlock](kcatransactioncompletionblock.md)
