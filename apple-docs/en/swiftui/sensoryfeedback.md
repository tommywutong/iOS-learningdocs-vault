---
title: SensoryFeedback
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sensoryfeedback
source_url: 'https://developer.apple.com/documentation/swiftui/sensoryfeedback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sensoryfeedback.json'
content_hash: 'sha256:97efd777f5705e28'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SensoryFeedback

<sub>Structure</sub>

Represents a type of haptic and/or audio feedback that can be played.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SensoryFeedback
```

## Overview

This feedback can be passed to `View.sensoryFeedback` to play it.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Indicating start and stop

- [start](sensoryfeedback/start.md) — Indicates that an activity started.
- [stop](sensoryfeedback/stop.md) — Indicates that an activity stopped.

### Indicating changes and selections

- [alignment](sensoryfeedback/alignment.md) — Indicates the alignment of a dragged item.
- [decrease](sensoryfeedback/decrease.md) — Indicates that an important value decreased below a significant threshold.
- [increase](sensoryfeedback/increase.md) — Indicates that an important value increased above a significant threshold.
- [levelChange](sensoryfeedback/levelchange.md) — Indicates movement between discrete levels of pressure.
- [selection](sensoryfeedback/selection.md) — Indicates that a UI element’s values are changing.
- [pathComplete](sensoryfeedback/pathcomplete.md) — Indicates a drawn path has completed and/or recognized.

### Indicating the outcome of an operation

- [success](sensoryfeedback/success.md) — Indicates that a task or action has completed.
- [warning](sensoryfeedback/warning.md) — Indicates that a task or action has produced a warning of some kind.
- [error](sensoryfeedback/error.md) — Indicates that an error has occurred.

### Producing a physical impact

- [impact](sensoryfeedback/impact.md) — Provides a physical metaphor you can use to complement a visual experience.
- [impact(weight:intensity:)](<sensoryfeedback/impact(weight_intensity_).md>) — Provides a physical metaphor you can use to complement a visual experience.
- [impact(flexibility:intensity:)](<sensoryfeedback/impact(flexibility_intensity_).md>) — Provides a physical metaphor you can use to complement a visual experience.
- [Flexibility](sensoryfeedback/flexibility.md) — The flexibility to be represented by a type of feedback.
- [Weight](sensoryfeedback/weight.md) — The weight to be represented by a type of feedback.

### Structures

- [PressFeedback](sensoryfeedback/pressfeedback.md) — Feedback that can be played in response to a press (touch down) on a control.
- [ReleaseFeedback](sensoryfeedback/releasefeedback.md) — Feedback that can be played in response to a release (touch up) of a control.
- [SelectionFeedback](sensoryfeedback/selectionfeedback.md) — Feedback that can be played in response to a specific UI element’s values changing.

### Type Methods

- [press(_:)](<sensoryfeedback/press(__).md>) — Plays feedback in response to a specific UI element being pressed (touch down).
- [release(_:)](<sensoryfeedback/release(__).md>) — Plays feedback in response to a specific UI element being released (touch up).
- [selection(_:)](<sensoryfeedback/selection(__).md>) — Plays feedback in response to a specific UI element’s values changing.

## See Also

### Providing haptic feedback

- [sensoryFeedback(_:trigger:)](<view/sensoryfeedback(__trigger_).md>) — Plays the specified `feedback` when the provided `trigger` value changes.
- [sensoryFeedback(trigger:_:)](<view/sensoryfeedback(trigger___).md>) — Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [sensoryFeedback(_:trigger:condition:)](<view/sensoryfeedback(__trigger_condition_).md>) — Plays the specified `feedback` when the provided `trigger` value changes and the `condition` closure returns `true`.
