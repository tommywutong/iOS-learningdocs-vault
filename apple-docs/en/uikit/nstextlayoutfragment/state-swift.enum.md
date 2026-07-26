---
title: NSTextLayoutFragment.State
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutfragment/state-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutfragment/state-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutfragment/state-swift.enum.json'
content_hash: 'sha256:b0f836cfd857f973'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutFragment](../nstextlayoutfragment.md)

# NSTextLayoutFragment.State

<sub>Enumeration</sub>

Values that describe the possible layout states.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum State
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants that describe layout bounds

- [NSTextLayoutFragmentStateCalculatedUsageBounds](state-swift.enum/calculatedusagebounds.md) — The layout fragment measurements are available without text line fragments.
- [NSTextLayoutFragmentStateEstimatedUsageBounds](state-swift.enum/estimatedusagebounds.md) — The text layout manager hasn’t performed a full layout yet for the region covered by this layout fragment and is returning an estimated bounds.
- [NSTextLayoutFragmentStateLayoutAvailable](state-swift.enum/layoutavailable.md) — Measurements for the text line fragments and layout fragment are available.
- [NSTextLayoutFragmentStateNone](state-swift.enum/none.md) — No layout information is available.

### Initializers

- [init(rawValue:)](<state-swift.enum/init(rawvalue_).md>)

## See Also

### Getting element information

- [state](state-swift.property.md) — The layout information state.
- [rangeInElement](rangeinelement.md) — The range inside the text element relative to the document origin.
- [textElement](textelement.md) — The parent text element.
