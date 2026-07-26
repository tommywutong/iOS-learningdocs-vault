---
title: AVExperienceController.TransitionContext.TransitionResult
framework: AVKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/transitioncontext/transitionresult
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/transitionresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/transitioncontext/transitionresult.json'
content_hash: 'sha256:5e41f2c788674b49'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVExperienceController](../../avexperiencecontroller.md) · [TransitionContext](../transitioncontext.md)

# AVExperienceController.TransitionContext.TransitionResult

<sub>Enumeration</sub>

Describes the result of a transition.

<sub>visionOS</sub>

```swift
@preconcurrency enum TransitionResult
```

## Overview

A transition can successfully complete to the `toExperience` or reverse back to the `fromExperience`.

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Results

- [AVExperienceController.TransitionContext.TransitionResult.completed](transitionresult/completed.md)
- [AVExperienceController.TransitionContext.TransitionResult.reversed(reason:)](<transitionresult/reversed(reason_).md>)

## See Also

### Understanding transition results

- [Status](status-swift.enum.md) — Describes the status of a transition.
- [ReversedReason](reversedreason.md)
