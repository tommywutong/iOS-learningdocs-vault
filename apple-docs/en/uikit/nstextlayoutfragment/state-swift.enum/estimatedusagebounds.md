---
title: NSTextLayoutFragment.State.estimatedUsageBounds
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutfragment/state-swift.enum/estimatedusagebounds
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutfragment/state-swift.enum/estimatedusagebounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutfragment/state-swift.enum/estimatedusagebounds.json'
content_hash: 'sha256:2aae31191d6c3211'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [NSTextLayoutFragment](../../nstextlayoutfragment.md) · [State](../state-swift.enum.md)

# NSTextLayoutFragment.State.estimatedUsageBounds

<sub>Case</sub>

The text layout manager hasn’t performed a full layout yet for the region covered by this layout fragment and is returning an estimated bounds.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case estimatedUsageBounds
```

## See Also

### Constants that describe layout bounds

- [NSTextLayoutFragmentStateCalculatedUsageBounds](calculatedusagebounds.md) — The layout fragment measurements are available without text line fragments.
- [NSTextLayoutFragmentStateLayoutAvailable](layoutavailable.md) — Measurements for the text line fragments and layout fragment are available.
- [NSTextLayoutFragmentStateNone](none.md) — No layout information is available.
