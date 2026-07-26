---
title: UIUpdateActionPhase
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiupdateactionphase
source_url: 'https://developer.apple.com/documentation/uikit/uiupdateactionphase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdateactionphase.json'
content_hash: 'sha256:c1721396f9d0457f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIUpdateActionPhase

<sub>Class</sub>

An object that defines specific phases of the UI update process.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIUpdateActionPhase
```

## Overview

Each UI update consists of several phases that run in a consistent order, and the [UIUpdateActionPhase](uiupdateactionphase.md) object defines constants that represent these phases. When using a [UIUpdateLink](uiupdatelink.md), you can use these constants to decide which phase of the UI update process you want its actions to run in.

There are two _phase groups_: standard and low-latency. The standard phase group runs for each UI update. This phase group includes these phases, which run in the following order:

1. [beforeEventDispatch](uiupdateactionphase/beforeeventdispatch.md)
2. [afterEventDispatch](uiupdateactionphase/aftereventdispatch.md)
3. [beforeCADisplayLinkDispatch](uiupdateactionphase/beforecadisplaylinkdispatch.md)
4. [afterCADisplayLinkDispatch](uiupdateactionphase/aftercadisplaylinkdispatch.md)
5. [beforeCATransactionCommit](uiupdateactionphase/beforecatransactioncommit.md)
6. [afterCATransactionCommit](uiupdateactionphase/aftercatransactioncommit.md)

The low-latency phase group is optional, and it’s off by default. It runs only if you explicitly request low-latency event dispatch using [wantsLowLatencyEventDispatch](uiupdatelink/wantslowlatencyeventdispatch.md). The low-latency phase group includes these phases, which run in the following order (after the standard phases):

1. [beforeLowLatencyEventDispatch](uiupdateactionphase/beforelowlatencyeventdispatch.md)
2. [afterLowLatencyEventDispatch](uiupdateactionphase/afterlowlatencyeventdispatch.md)
3. [beforeLowLatencyCATransactionCommit](uiupdateactionphase/beforelowlatencycatransactioncommit.md)
4. [afterLowLatencyCATransactionCommit](uiupdateactionphase/afterlowlatencycatransactioncommit.md)

When a phase group runs, all phases inside the group run. Phases run one after another in the specified order without exiting back into the run loop.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Phases

- [afterUpdateScheduled](uiupdateactionphase/afterupdatescheduled.md) — A phase that runs after the scheduling of a UI update.
- [beforeEventDispatch](uiupdateactionphase/beforeeventdispatch.md) — A phase that runs before standard event handlers.
- [afterEventDispatch](uiupdateactionphase/aftereventdispatch.md) — A phase that runs after standard event handlers.
- [beforeCADisplayLinkDispatch](uiupdateactionphase/beforecadisplaylinkdispatch.md) — A phase that runs before Core Animation display link callbacks.
- [afterCADisplayLinkDispatch](uiupdateactionphase/aftercadisplaylinkdispatch.md) — A phase that runs after Core Animation display link callbacks.
- [beforeCATransactionCommit](uiupdateactionphase/beforecatransactioncommit.md) — A phase that runs before a Core Animation transaction commit.
- [afterCATransactionCommit](uiupdateactionphase/aftercatransactioncommit.md) — A phase that runs after a Core Animation transaction commit.
- [beforeLowLatencyEventDispatch](uiupdateactionphase/beforelowlatencyeventdispatch.md) — A phase that runs before low-latency event handlers.
- [afterLowLatencyEventDispatch](uiupdateactionphase/afterlowlatencyeventdispatch.md) — A phase that runs after low-latency event handlers.
- [beforeLowLatencyCATransactionCommit](uiupdateactionphase/beforelowlatencycatransactioncommit.md) — A phase that runs before a Core Animation transaction commit for a low-latency event.
- [afterLowLatencyCATransactionCommit](uiupdateactionphase/afterlowlatencycatransactioncommit.md) — A phase that runs after a Core Animation transaction commit for a low-latency event.
- [afterUpdateComplete](uiupdateactionphase/afterupdatecomplete.md) — A phase that runs at the end of a UI update.

## See Also

### UI updates

- [UIUpdateLink](uiupdatelink.md) — An object you use to observe, participate in, and affect the UI update process.
- [UIUpdateInfo](uiupdateinfo.md) — An object that contains detailed information about the current UI update state.
