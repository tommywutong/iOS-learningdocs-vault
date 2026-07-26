---
title: UIPageControl.InteractionState
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipagecontrol/interactionstate-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrol/interactionstate-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrol/interactionstate-swift.enum.json'
content_hash: 'sha256:e56b3563a053aa9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageControl](../uipagecontrol.md)

# UIPageControl.InteractionState

<sub>Enumeration</sub>

Constants that define the interaction states of the page control.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum InteractionState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIPageControlInteractionStateNone](interactionstate-swift.enum/none.md) — The default interaction state, where no interaction has occurred.
- [UIPageControlInteractionStateDiscrete](interactionstate-swift.enum/discrete.md) — The interaction state for which the page changes through a single, discrete interaction.
- [UIPageControlInteractionStateContinuous](interactionstate-swift.enum/continuous.md) — The interaction state for which the page changes through a continuous interaction.

### Initializers

- [init(rawValue:)](<interactionstate-swift.enum/init(rawvalue_).md>)

## See Also

### Customizing the interaction state

- [allowsContinuousInteraction](allowscontinuousinteraction.md) — A Boolean value that determines whether the page control allows continuous interaction.
- [interactionState](interactionstate-swift.property.md) — The interaction state when the current page changes.
