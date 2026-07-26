---
title: UIImpactFeedbackGenerator.FeedbackStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimpactfeedbackgenerator/feedbackstyle
source_url: 'https://developer.apple.com/documentation/uikit/uiimpactfeedbackgenerator/feedbackstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimpactfeedbackgenerator/feedbackstyle.json'
content_hash: 'sha256:f0640f8ef9b91932'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImpactFeedbackGenerator](../uiimpactfeedbackgenerator.md)

# UIImpactFeedbackGenerator.FeedbackStyle

<sub>Enumeration</sub>

The mass of the objects in the collision simulated by an impact feedback generator object.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum FeedbackStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIImpactFeedbackStyleHeavy](feedbackstyle/heavy.md) — A collision between large, heavy user interface elements.
- [UIImpactFeedbackStyleLight](feedbackstyle/light.md) — A collision between small, light user interface elements.
- [UIImpactFeedbackStyleMedium](feedbackstyle/medium.md) — A collision between moderately sized user interface elements.
- [UIImpactFeedbackStyleRigid](feedbackstyle/rigid.md) — A collision between user interface elements that are rigid, exhibiting a small amount of compression or elasticity.
- [UIImpactFeedbackStyleSoft](feedbackstyle/soft.md) — A collision between user interface elements that are soft, exhibiting a large amount of compression or elasticity.

### Initializers

- [init(rawValue:)](<feedbackstyle/init(rawvalue_).md>)

## See Also

### Initializing the feedback generator

- [+ feedbackGeneratorWithStyle:forView:](<init(style_view_).md>) — Creates an impact feedback generator with the specified style and view.
