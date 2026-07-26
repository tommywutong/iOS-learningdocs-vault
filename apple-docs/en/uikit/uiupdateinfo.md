---
title: UIUpdateInfo
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiupdateinfo
source_url: 'https://developer.apple.com/documentation/uikit/uiupdateinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdateinfo.json'
content_hash: 'sha256:921a94a1dff2c0b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIUpdateInfo

<sub>Class</sub>

An object that contains detailed information about the current UI update state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIUpdateInfo
```

## Overview

During a UI update, this object provides details about the state of the update. When using a [UIUpdateLink](uiupdatelink.md), you can query this UI update information object to learn about the current UI update.

A UI update can service views on different displays simultaneously, which means these views can have a different [UIUpdateInfo](uiupdateinfo.md). Get the UI update information for a specific view using [+ currentUpdateInfoForView:](<uiupdateinfo/current(for_)-34zby.md>) or a specific window using [+ currentUpdateInfoForWindowScene:](<uiupdateinfo/current(for_)-6y1z9.md>). The UI update information can also change as the current UI update progresses through its phases.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Getting the current UI update information

- [+ currentUpdateInfoForView:](<uiupdateinfo/current(for_)-34zby.md>) — Returns an object that describes the current UI update state for the specified view.
- [+ currentUpdateInfoForWindowScene:](<uiupdateinfo/current(for_)-6y1z9.md>) — Returns an object that describes the current UI update state for the specified window.

### Getting information about timing

- [modelTime](uiupdateinfo/modeltime.md) — The time interval that represents a reference point for the current time of the UI update.
- [completionDeadlineTime](uiupdateinfo/completiondeadlinetime.md) — The time interval that represents the time by which an app needs to finish submitting changes to the render server.
- [estimatedPresentationTime](uiupdateinfo/estimatedpresentationtime.md) — The time interval that represents an estimate for when current UI update changes become visible onscreen.

### Working with low-latency updates

- [immediatePresentationExpected](uiupdateinfo/isimmediatepresentationexpected.md) — A Boolean value that indicates whether the system presents UI updates immediately upon completion.
- [lowLatencyEventDispatchConfirmed](uiupdateinfo/islowlatencyeventdispatchconfirmed.md) — A Boolean value that indicates whether the system runs low-latency phases for the UI update.
- [performingLowLatencyPhases](uiupdateinfo/isperforminglowlatencyphases.md) — A Boolean value that indicates whether the UI update is in the low-latency phases.

## See Also

### UI updates

- [UIUpdateLink](uiupdatelink.md) — An object you use to observe, participate in, and affect the UI update process.
- [UIUpdateActionPhase](uiupdateactionphase.md) — An object that defines specific phases of the UI update process.
