---
title: AVExperienceController.TransitionGroup
framework: AVKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/transitiongroup
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitiongroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/transitiongroup.json'
content_hash: 'sha256:9f84633cf67cc330'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVExperienceController](../avexperiencecontroller.md)

# AVExperienceController.TransitionGroup

<sub>Structure</sub>

A group of experience transitions that prepare concurrently and run simultaneously as a single visual transition.

<sub>visionOS</sub>

```swift
struct TransitionGroup<ChildTransitionResult> where ChildTransitionResult : Sendable
```

## Overview

Use [withTransitionGroup(body:)](<withtransitiongroup(body_).md>) to create a transition group. Add transitions using [addTransition(operation:)](<transitiongroup/addtransition(operation_).md>), and they perform together once all have been added and prepared.

Transitions in a group prepare concurrently, then perform their animations simultaneously, creating a single cohesive visual transition. Each transition completes with its own result, allowing you to handle individual successes and failures.

## Handle Failures

Individual transitions may fail during preparation or execution without affecting other transitions in the group.

## Topics

### Adding transitions

- [addTransition(operation:)](<transitiongroup/addtransition(operation_).md>) — Adds a transition to the group, suspending it until all transitions are ready to run together. _(beta)_

## See Also

### Transitioning experiences

- [withTransitionGroup(body:)](<withtransitiongroup(body_).md>) — Coordinates multiple experience transitions to perform together as a single visual transition. _(beta)_
- [transition(to:)](<transition(to_).md>) — Transitions the video to a different experience.
