---
title: afterLowLatencyCATransactionCommit
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiupdateactionphase/afterlowlatencycatransactioncommit
source_url: 'https://developer.apple.com/documentation/uikit/uiupdateactionphase/afterlowlatencycatransactioncommit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdateactionphase/afterlowlatencycatransactioncommit.json'
content_hash: 'sha256:908dcd5a34e4b865'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateActionPhase](../uiupdateactionphase.md)

# afterLowLatencyCATransactionCommit

<sub>Type Property</sub>

A phase that runs after a Core Animation transaction commit for a low-latency event.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class var afterLowLatencyCATransactionCommit: UIUpdateActionPhase { get }
```

## Discussion

This phase runs after [flush()](<../../quartzcore/catransaction/flush().md>) for a low-latency event. Any changes you make to the Core Animation layer tree during this phase or later appear onscreen with the next UI update instead of the current one.

This phase is off by default. You can request it to run by setting [wantsLowLatencyEventDispatch](../uiupdatelink/wantslowlatencyeventdispatch.md) to `true`.

## See Also

### Phases

- [afterUpdateScheduled](afterupdatescheduled.md) — A phase that runs after the scheduling of a UI update.
- [beforeEventDispatch](beforeeventdispatch.md) — A phase that runs before standard event handlers.
- [afterEventDispatch](aftereventdispatch.md) — A phase that runs after standard event handlers.
- [beforeCADisplayLinkDispatch](beforecadisplaylinkdispatch.md) — A phase that runs before Core Animation display link callbacks.
- [afterCADisplayLinkDispatch](aftercadisplaylinkdispatch.md) — A phase that runs after Core Animation display link callbacks.
- [beforeCATransactionCommit](beforecatransactioncommit.md) — A phase that runs before a Core Animation transaction commit.
- [afterCATransactionCommit](aftercatransactioncommit.md) — A phase that runs after a Core Animation transaction commit.
- [beforeLowLatencyEventDispatch](beforelowlatencyeventdispatch.md) — A phase that runs before low-latency event handlers.
- [afterLowLatencyEventDispatch](afterlowlatencyeventdispatch.md) — A phase that runs after low-latency event handlers.
- [beforeLowLatencyCATransactionCommit](beforelowlatencycatransactioncommit.md) — A phase that runs before a Core Animation transaction commit for a low-latency event.
- [afterUpdateComplete](afterupdatecomplete.md) — A phase that runs at the end of a UI update.
