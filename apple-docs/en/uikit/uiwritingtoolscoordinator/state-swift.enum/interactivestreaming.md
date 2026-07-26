---
title: UIWritingToolsCoordinator.State.interactiveStreaming
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/state-swift.enum/interactivestreaming
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/state-swift.enum/interactivestreaming'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/state-swift.enum/interactivestreaming.json'
content_hash: 'sha256:3dd586db06a9e9bc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [State](../state-swift.enum.md)

# UIWritingToolsCoordinator.State.interactiveStreaming

<sub>Case</sub>

A state that indicates Writing Tools is processing a request and incorporating changes interactively into your view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case interactiveStreaming
```

## Discussion

The coordinator transitions swiftly from the [UIWritingToolsCoordinatorStateInteractiveResting](interactiveresting.md) state to this state at the start of an operation. In this state, the coordinator submits the request for processing and delivers the results back to your view. When the coordinator finishes delivering the results, it transitions back to the [UIWritingToolsCoordinatorStateInteractiveResting](interactiveresting.md) state.

## See Also

### Getting the animation types

- [UIWritingToolsCoordinatorStateInactive](inactive.md) — A state that indicates Writing Tools isn’t currently performing any work on your view’s content.
- [UIWritingToolsCoordinatorStateNoninteractive](noninteractive.md) — A state that indicates Writing Tools is handling interactions in the system UI, instead of in your view.
- [UIWritingToolsCoordinatorStateInteractiveResting](interactiveresting.md) — A state that indicates Writing Tools is in the resting state for an inline editing experience.
