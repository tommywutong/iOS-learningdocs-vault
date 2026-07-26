---
title: 'withTransitionGroup(body:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avkit/avexperiencecontroller/withtransitiongroup(body:)'
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/withtransitiongroup(body:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/withtransitiongroup%28body%3A%29.json'
content_hash: 'sha256:622e123c89fa62fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVExperienceController](../avexperiencecontroller.md)

# withTransitionGroup(body:)

<sub>Type Method</sub>

Coordinates multiple experience transitions to perform together as a single visual transition.

<sub>visionOS</sub>

```swift
@discardableResult nonisolated(nonsending) static func withTransitionGroup<ChildTransitionResult>(body: @_lifetime(0: copy 0) (inout AVExperienceController.TransitionGroup<ChildTransitionResult>) async -> Void) async -> [ChildTransitionResult] where ChildTransitionResult : Sendable
```

## Parameters

- `body` — A closure that adds transitions to the group using `addTransition(operation:)`.

## Return Value

An array of transition results in the order transitions were added.

## Discussion

Use this method when you need to transition multiple [AVExperienceController](../avexperiencecontroller.md) instances simultaneously, creating a smooth, coordinated animation.

All transitions prepare concurrently, then perform together once preparation completes. Individual transitions may succeed or fail independently — the group continues with successful transitions and collects results for all.

```swift
let results = await AVExperienceController.withTransitionGroup { group in
    for controller in controllers {
        group.addTransition {
            await controller.transition(to: .multiview)
        }
    }
}

// Check which transitions succeeded
for (index, result) in results.enumerated() {
    if case .reversed(let reason) = result {
        print("Controller \(index) failed: \(reason)")
    }
}
```

## See Also

### Transitioning experiences

- [TransitionGroup](transitiongroup.md) — A group of experience transitions that prepare concurrently and run simultaneously as a single visual transition. _(beta)_
- [transition(to:)](<transition(to_).md>) — Transitions the video to a different experience.
