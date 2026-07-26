---
title: UIBandSelectionInteraction.State
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibandselectioninteraction/state-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uibandselectioninteraction/state-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibandselectioninteraction/state-swift.enum.json'
content_hash: 'sha256:5a7998d3a77c1dee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBandSelectionInteraction](../uibandselectioninteraction.md)

# UIBandSelectionInteraction.State

<sub>Enumeration</sub>

Constants that indicate whether a band selection interaction object is inactive or currently tracking an interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum State
```

## Overview

Use the [State](state-swift.enum.md) constants in the handler of a [UIBandSelectionInteraction](../uibandselectioninteraction.md) object to determine the current state of the interaction. When the interaction object is idle, it sets the state to [UIBandSelectionInteractionStatePossible](state-swift.enum/possible.md). After the interaction starts, the state changes to other values to reflect the progress toward the completion of that interaction.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the selection state

- [UIBandSelectionInteractionStatePossible](state-swift.enum/possible.md) — A state that indicates the interaction object is ready to start a new interaction.
- [UIBandSelectionInteractionStateBegan](state-swift.enum/began.md) — A state that indicates the interaction object began a new interaction.
- [UIBandSelectionInteractionStateSelecting](state-swift.enum/selecting.md) — A state that indicates the interaction object is tracking changes to the selection rectangle.
- [UIBandSelectionInteractionStateEnded](state-swift.enum/ended.md) — A state that indicates the current interaction ended.

### Initializers

- [init(rawValue:)](<state-swift.enum/init(rawvalue_).md>)

## See Also

### Band selection

- [UIBandSelectionInteraction](../uibandselectioninteraction.md) — An object that tracks the selection of multiple items using pointer-based input.
