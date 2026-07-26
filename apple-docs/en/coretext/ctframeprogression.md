---
title: CTFrameProgression
framework: Core Text
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctframeprogression
source_url: 'https://developer.apple.com/documentation/coretext/ctframeprogression'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctframeprogression.json'
content_hash: 'sha256:30e16e04ecf3e547'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFrameProgression

<sub>Enumeration</sub>

Constants that specify frame progression types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CTFrameProgression
```

## Overview

The lines of text within a frame may stack for either horizontal or vertical text. Values are enumerated for each stacking type supported by [CTFrameProgression](ctframeprogression.md). Frames with a progression type that specifies vertical text rotate lines 90 degrees counterclockwise during drawing.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCTFrameProgressionTopToBottom](ctframeprogression/toptobottom.md) — Lines stack top to bottom for horizontal text.
- [kCTFrameProgressionRightToLeft](ctframeprogression/righttoleft.md) — Lines stack right to left for vertical text.
- [kCTFrameProgressionLeftToRight](ctframeprogression/lefttoright.md) — Lines stack left to right for vertical text.

### Initializers

- [init(rawValue:)](<ctframeprogression/init(rawvalue_).md>)

## See Also

### Constants

- [kCTFrameProgressionAttributeName](kctframeprogressionattributename.md) — Specifies progression for a frame.
- [kCTFramePathFillRuleAttributeName](kctframepathfillruleattributename.md) — The key used to specify the fill rule for a frame.
- [kCTFramePathWidthAttributeName](kctframepathwidthattributename.md) — The key used to specify the frame width.
- [kCTFrameClippingPathsAttributeName](kctframeclippingpathsattributename.md) — Specifies array of paths to clip frame.
- [kCTFramePathClippingPathAttributeName](kctframepathclippingpathattributename.md) — Specifies clipping path.
