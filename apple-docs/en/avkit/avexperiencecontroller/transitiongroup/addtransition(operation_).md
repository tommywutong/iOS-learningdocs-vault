---
title: 'addTransition(operation:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avkit/avexperiencecontroller/transitiongroup/addtransition(operation:)'
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitiongroup/addtransition(operation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/transitiongroup/addtransition%28operation%3A%29.json'
content_hash: 'sha256:ebadbb4f741544dd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVExperienceController](../../avexperiencecontroller.md) · [TransitionGroup](../transitiongroup.md)

# addTransition(operation:)

<sub>Instance Method</sub>

Adds a transition to the group, suspending it until all transitions are ready to run together.

<sub>visionOS</sub>

```swift
mutating func addTransition(operation: sending @escaping @isolated(any) () async -> ChildTransitionResult)
```

## Parameters

- `operation` — A closure that performs a transition and returns a result.

## Discussion

Call [transition(to:)](<../transition(to_).md>) on an [AVExperienceController](../../avexperiencecontroller.md) within the operation closure. The transition suspends until all transitions have been added to the group, then perform together with the others.

[withTransitionGroup(body:)](<../withtransitiongroup(body_).md>) includes the value you return from the closure in the order transitions were added.

```swift
group.addTransition {
    await controller.transition(to: .multiview)
}
```
