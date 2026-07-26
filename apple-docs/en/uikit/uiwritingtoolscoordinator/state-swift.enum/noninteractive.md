---
title: UIWritingToolsCoordinator.State.noninteractive
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/state-swift.enum/noninteractive
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/state-swift.enum/noninteractive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/state-swift.enum/noninteractive.json'
content_hash: 'sha256:81c7f5b6701e1114'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [State](../state-swift.enum.md)

# UIWritingToolsCoordinator.State.noninteractive

<sub>Case</sub>

A state that indicates Writing Tools is handling interactions in the system UI, instead of in your view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case noninteractive
```

## Discussion

Writing Tools transitions to this state when the coordinator uses the [UIWritingToolsBehaviorLimited](../../uiwritingtoolsbehavior/limited.md) experience or when someone chooses an option that displays its results in the Writing Tools UI. When the person accepts the changes from the tool or dismisses the Writing Tools UI, the coordinator returns to the [UIWritingToolsCoordinatorStateInactive](inactive.md) state. If the person discards the change and selects a tool with an interactive experience instead, the coordinator transitions to the [UIWritingToolsCoordinatorStateInteractiveResting](interactiveresting.md) state.

## See Also

### Getting the animation types

- [UIWritingToolsCoordinatorStateInactive](inactive.md) — A state that indicates Writing Tools isn’t currently performing any work on your view’s content.
- [UIWritingToolsCoordinatorStateInteractiveResting](interactiveresting.md) — A state that indicates Writing Tools is in the resting state for an inline editing experience.
- [UIWritingToolsCoordinatorStateInteractiveStreaming](interactivestreaming.md) — A state that indicates Writing Tools is processing a request and incorporating changes interactively into your view.
