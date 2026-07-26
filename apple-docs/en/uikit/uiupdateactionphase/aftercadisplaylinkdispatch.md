---
title: afterCADisplayLinkDispatch
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiupdateactionphase/aftercadisplaylinkdispatch
source_url: 'https://developer.apple.com/documentation/uikit/uiupdateactionphase/aftercadisplaylinkdispatch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdateactionphase/aftercadisplaylinkdispatch.json'
content_hash: 'sha256:c2e36c29f3aca5ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateActionPhase](../uiupdateactionphase.md)

# afterCADisplayLinkDispatch

<sub>Type Property</sub>

A phase that runs after Core Animation display link callbacks.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class var afterCADisplayLinkDispatch: UIUpdateActionPhase { get }
```

## Discussion

This phase runs after [CADisplayLink](../../quartzcore/cadisplaylink.md) callbacks run.

## See Also

### Phases

- [afterUpdateScheduled](afterupdatescheduled.md) — A phase that runs after the scheduling of a UI update.
- [beforeEventDispatch](beforeeventdispatch.md) — A phase that runs before standard event handlers.
- [afterEventDispatch](aftereventdispatch.md) — A phase that runs after standard event handlers.
- [beforeCADisplayLinkDispatch](beforecadisplaylinkdispatch.md) — A phase that runs before Core Animation display link callbacks.
- [beforeCATransactionCommit](beforecatransactioncommit.md) — A phase that runs before a Core Animation transaction commit.
- [afterCATransactionCommit](aftercatransactioncommit.md) — A phase that runs after a Core Animation transaction commit.
- [beforeLowLatencyEventDispatch](beforelowlatencyeventdispatch.md) — A phase that runs before low-latency event handlers.
- [afterLowLatencyEventDispatch](afterlowlatencyeventdispatch.md) — A phase that runs after low-latency event handlers.
- [beforeLowLatencyCATransactionCommit](beforelowlatencycatransactioncommit.md) — A phase that runs before a Core Animation transaction commit for a low-latency event.
- [afterLowLatencyCATransactionCommit](afterlowlatencycatransactioncommit.md) — A phase that runs after a Core Animation transaction commit for a low-latency event.
- [afterUpdateComplete](afterupdatecomplete.md) — A phase that runs at the end of a UI update.
