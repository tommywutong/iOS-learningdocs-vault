---
title: UIWritingToolsCoordinator.State
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/state-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/state-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/state-swift.enum.json'
content_hash: 'sha256:d9c47b717b00249e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# UIWritingToolsCoordinator.State

<sub>Enumeration</sub>

The states that indicate the current activity, if any, Writing Tools is performing in your view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum State
```

## Overview

Making changes to your view requires several different levels of interaction. Initially, Writing Tools displays its UI and collects information about what the person wants to do. When the person selects an operation, Writing Tools sends the relevant details to a large language model (LLM) and processes the results. It then works with the custom view to integrate any changes into the view’s text storage. During each of these activities, the coordinator reflects what’s happening in its [state](state-swift.property.md) property. You can use the current state as a guide to making decisions in other parts of your view.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the animation types

- [UIWritingToolsCoordinatorStateInactive](state-swift.enum/inactive.md) — A state that indicates Writing Tools isn’t currently performing any work on your view’s content.
- [UIWritingToolsCoordinatorStateNoninteractive](state-swift.enum/noninteractive.md) — A state that indicates Writing Tools is handling interactions in the system UI, instead of in your view.
- [UIWritingToolsCoordinatorStateInteractiveResting](state-swift.enum/interactiveresting.md) — A state that indicates Writing Tools is in the resting state for an inline editing experience.
- [UIWritingToolsCoordinatorStateInteractiveStreaming](state-swift.enum/interactivestreaming.md) — A state that indicates Writing Tools is processing a request and incorporating changes interactively into your view.

### Initializers

- [init(rawValue:)](<state-swift.enum/init(rawvalue_).md>)

## See Also

### Managing the current state

- [- stopWritingTools](<stopwritingtools().md>) — Stops the current Writing Tools operation and dismisses the system UI.
- [state](state-swift.property.md) — The current level of Writing Tools activity in your view.
