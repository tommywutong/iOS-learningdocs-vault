---
title: AVExperienceController.TransitionContext.Status
framework: AVKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/transitioncontext/status-swift.enum
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/status-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/transitioncontext/status-swift.enum.json'
content_hash: 'sha256:2f9c51cb6722d633'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVExperienceController](../../avexperiencecontroller.md) · [TransitionContext](../transitioncontext.md)

# AVExperienceController.TransitionContext.Status

<sub>Enumeration</sub>

Describes the status of a transition.

<sub>visionOS</sub>

```swift
@preconcurrency enum Status
```

## Overview

Transitions go through a sequence of `Status`s as they progress.

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Statuses

- [AVExperienceController.TransitionContext.Status.preparing](status-swift.enum/preparing.md) — The transition is preparing for `toExperience`.
- [AVExperienceController.TransitionContext.Status.transitioning](status-swift.enum/transitioning.md) — The transition is in progress.
- [AVExperienceController.TransitionContext.Status.finished(result:)](<status-swift.enum/finished(result_).md>) — Transition finished. Perform cleanup based on result.

## See Also

### Understanding transition results

- [TransitionResult](transitionresult.md) — Describes the result of a transition.
- [ReversedReason](reversedreason.md)
