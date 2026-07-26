---
title: 'transition(to:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avexperiencecontroller/transition(to:)'
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/transition(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/transition%28to%3A%29.json'
content_hash: 'sha256:fc17497c45f23bbe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVExperienceController](../avexperiencecontroller.md)

# transition(to:)

<sub>Instance Method</sub>

Transitions the video to a different experience.

<sub>visionOS</sub>

```swift
@discardableResult @MainActor final func transition(to toExperience: AVExperienceController.Experience) async -> AVExperienceController.TransitionContext.TransitionResult
```

## Parameters

- `toExperience` — The experience to transition to.

## Return Value

A transition result.

## Discussion

Call this method to transition to a different experience such as [AVExperienceController.Experience.expanded](experience-swift.enum/expanded.md). When you initiate a transition, the system calls the experience controller’s delegate methods so your app can respond to experience changes.

You determine the success of a transition by evaluating the [TransitionResult](transitioncontext/transitionresult.md) this method returns. A transition result of [AVExperienceController.TransitionContext.TransitionResult.completed](transitioncontext/transitionresult/completed.md) indicates a successful transition, in which case the system updates the [experience](experience-swift.property.md) property to the new experience. A transition result of [AVExperienceController.TransitionContext.TransitionResult.reversed(reason:)](<transitioncontext/transitionresult/reversed(reason_).md>) indicates a failed transition. Evaluate the the result’s [ReversedReason](transitioncontext/reversedreason.md) to determine why the transition failed. A failure that occurs before the transition begins results in the system not invoking any delegate callback methods. If the failure happens after the callback to  [experienceController(_:prepareForTransitionUsing:)](<delegate-swift.protocol/experiencecontroller(__preparefortransitionusing_).md>) occurs, the transition context changes to [AVExperienceController.TransitionContext.Status.finished(result:)](<transitioncontext/status-swift.enum/finished(result_).md>).

## See Also

### Transitioning experiences

- [TransitionGroup](transitiongroup.md) — A group of experience transitions that prepare concurrently and run simultaneously as a single visual transition. _(beta)_
- [withTransitionGroup(body:)](<withtransitiongroup(body_).md>) — Coordinates multiple experience transitions to perform together as a single visual transition. _(beta)_
