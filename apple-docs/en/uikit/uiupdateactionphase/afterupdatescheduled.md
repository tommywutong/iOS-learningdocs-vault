---
title: afterUpdateScheduled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiupdateactionphase/afterupdatescheduled
source_url: 'https://developer.apple.com/documentation/uikit/uiupdateactionphase/afterupdatescheduled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdateactionphase/afterupdatescheduled.json'
content_hash: 'sha256:44e935d1b4968e36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateActionPhase](../uiupdateactionphase.md)

# afterUpdateScheduled

<sub>Type Property</sub>

A phase that runs after the scheduling of a UI update.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class var afterUpdateScheduled: UIUpdateActionPhase { get }
```

## Discussion

This phase runs after timing information for the UI update is available. Use this phase to perform tasks that rely on UI update timing information, but don’t need user input events, such as time-driven animations or noninteractive simulations.

## See Also

### Phases

- [beforeEventDispatch](beforeeventdispatch.md) — A phase that runs before standard event handlers.
- [afterEventDispatch](aftereventdispatch.md) — A phase that runs after standard event handlers.
- [beforeCADisplayLinkDispatch](beforecadisplaylinkdispatch.md) — A phase that runs before Core Animation display link callbacks.
- [afterCADisplayLinkDispatch](aftercadisplaylinkdispatch.md) — A phase that runs after Core Animation display link callbacks.
- [beforeCATransactionCommit](beforecatransactioncommit.md) — A phase that runs before a Core Animation transaction commit.
- [afterCATransactionCommit](aftercatransactioncommit.md) — A phase that runs after a Core Animation transaction commit.
- [beforeLowLatencyEventDispatch](beforelowlatencyeventdispatch.md) — A phase that runs before low-latency event handlers.
- [afterLowLatencyEventDispatch](afterlowlatencyeventdispatch.md) — A phase that runs after low-latency event handlers.
- [beforeLowLatencyCATransactionCommit](beforelowlatencycatransactioncommit.md) — A phase that runs before a Core Animation transaction commit for a low-latency event.
- [afterLowLatencyCATransactionCommit](afterlowlatencycatransactioncommit.md) — A phase that runs after a Core Animation transaction commit for a low-latency event.
- [afterUpdateComplete](afterupdatecomplete.md) — A phase that runs at the end of a UI update.
