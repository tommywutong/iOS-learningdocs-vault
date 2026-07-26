---
title: UIBaselineAdjustment
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibaselineadjustment
source_url: 'https://developer.apple.com/documentation/uikit/uibaselineadjustment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibaselineadjustment.json'
content_hash: 'sha256:b160da70ebd22aa9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIBaselineAdjustment

<sub>Enumeration</sub>

Vertical adjustment options.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIBaselineAdjustment
```

## Overview

Baseline adjustment options determine how to adjust the position of text in cases where the text must be drawn using a different font size than the one originally specified. For example, with the [UIBaselineAdjustmentAlignBaselines](uibaselineadjustment/alignbaselines.md) option, the position of the baseline remains fixed at its initial location while the text appears to move toward that baseline. Similarly, the [UIBaselineAdjustmentNone](uibaselineadjustment/none.md) option makes it appear as if the text is moving upwards toward the top-left corner of the bounding box.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIBaselineAdjustmentAlignBaselines](uibaselineadjustment/alignbaselines.md) — Adjust text relative to the position of its baseline.
- [UIBaselineAdjustmentAlignCenters](uibaselineadjustment/aligncenters.md) — Adjust text relative to the center of its bounding box.
- [UIBaselineAdjustmentNone](uibaselineadjustment/none.md) — Adjust text relative to the top-left corner of the bounding box.

### Initializers

- [init(rawValue:)](<uibaselineadjustment/init(rawvalue_).md>)

## See Also

### Strings

- [NSStringDrawingContext](nsstringdrawingcontext.md) — An object that manages metrics for drawing attributed strings.
- [NSStringDrawingOptions](nsstringdrawingoptions.md) — Constants that specify the rendering options for drawing a string.
