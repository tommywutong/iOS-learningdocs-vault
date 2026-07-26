---
title: UIWritingToolsCoordinator.State.inactive
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/state-swift.enum/inactive
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/state-swift.enum/inactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/state-swift.enum/inactive.json'
content_hash: 'sha256:8b32cfed89bda43d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [State](../state-swift.enum.md)

# UIWritingToolsCoordinator.State.inactive

<sub>Case</sub>

A state that indicates Writing Tools isn’t currently performing any work on your view’s content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case inactive
```

## Discussion

The coordinator starts in the `inactive` state, and transitions immediately to the [UIWritingToolsCoordinatorStateNoninteractive](noninteractive.md) or [UIWritingToolsCoordinatorStateInteractiveResting](interactiveresting.md) state when someone chooses an option from the Writing Tools UI. The coordinator returns to the `inactive` state when the person accepts the changes or dismisses the Writing Tools UI.

## See Also

### Getting the animation types

- [UIWritingToolsCoordinatorStateNoninteractive](noninteractive.md) — A state that indicates Writing Tools is handling interactions in the system UI, instead of in your view.
- [UIWritingToolsCoordinatorStateInteractiveResting](interactiveresting.md) — A state that indicates Writing Tools is in the resting state for an inline editing experience.
- [UIWritingToolsCoordinatorStateInteractiveStreaming](interactivestreaming.md) — A state that indicates Writing Tools is processing a request and incorporating changes interactively into your view.
