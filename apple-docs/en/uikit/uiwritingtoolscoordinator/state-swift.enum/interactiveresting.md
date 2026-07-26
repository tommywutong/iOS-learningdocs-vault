---
title: UIWritingToolsCoordinator.State.interactiveResting
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/state-swift.enum/interactiveresting
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/state-swift.enum/interactiveresting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/state-swift.enum/interactiveresting.json'
content_hash: 'sha256:2ed0077fb128b8a3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [State](../state-swift.enum.md)

# UIWritingToolsCoordinator.State.interactiveResting

<sub>Case</sub>

A state that indicates Writing Tools is in the resting state for an inline editing experience.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case interactiveResting
```

## Discussion

When someone initially selects a tool with an interactive experience, the coordinator transitions briefly to this state and starts the operation. The coordinator transitions swiftly to the [UIWritingToolsCoordinatorStateInteractiveStreaming](interactivestreaming.md) state when it submits the request and delivers the results to your view. When it finishes delivering the results, it transitions back to the `interactiveResting` state and awaits further commands. If the person accepts the changes or dismisses the Writing Tools UI, the coordinator transitions from this state to the [UIWritingToolsCoordinatorStateInactive](inactive.md) state.

## See Also

### Getting the animation types

- [UIWritingToolsCoordinatorStateInactive](inactive.md) — A state that indicates Writing Tools isn’t currently performing any work on your view’s content.
- [UIWritingToolsCoordinatorStateNoninteractive](noninteractive.md) — A state that indicates Writing Tools is handling interactions in the system UI, instead of in your view.
- [UIWritingToolsCoordinatorStateInteractiveStreaming](interactivestreaming.md) — A state that indicates Writing Tools is processing a request and incorporating changes interactively into your view.
