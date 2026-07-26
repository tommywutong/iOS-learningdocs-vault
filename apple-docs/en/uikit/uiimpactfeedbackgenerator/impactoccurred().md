---
title: impactOccurred()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimpactfeedbackgenerator/impactoccurred()
source_url: 'https://developer.apple.com/documentation/uikit/uiimpactfeedbackgenerator/impactoccurred()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimpactfeedbackgenerator/impactoccurred%28%29.json'
content_hash: 'sha256:87a924c7eb4bff9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImpactFeedbackGenerator](../uiimpactfeedbackgenerator.md)

# impactOccurred()

<sub>Instance Method</sub>

Triggers impact feedback.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func impactOccurred()
```

## Discussion

This method tells the generator that an impact has occurred. In response, the generator may play the appropriate haptics based on the [FeedbackStyle](feedbackstyle.md) value passed to the generator’s [- initWithStyle:](<init(style_).md>) initializer.

For information on setting up a feedback generator, see the [UIFeedbackGenerator](../uifeedbackgenerator.md) class.

## See Also

### Related Documentation

- [- prepare](<../uifeedbackgenerator/prepare().md>) — Prepares the generator to trigger feedback.

### Reporting impacts

- [- impactOccurredWithIntensity:](<impactoccurred(intensity_).md>) — Triggers impact feedback with a specific intensity.
- [- impactOccurredAtLocation:](<impactoccurred(at_).md>) — Triggers impact feedback at the specified location.
- [- impactOccurredWithIntensity:atLocation:](<impactoccurred(intensity_at_).md>) — Triggers impact feedback with a specific intensity at the specified location.
