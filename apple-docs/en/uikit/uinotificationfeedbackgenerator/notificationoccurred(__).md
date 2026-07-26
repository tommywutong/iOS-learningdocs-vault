---
title: 'notificationOccurred(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinotificationfeedbackgenerator/notificationoccurred(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinotificationfeedbackgenerator/notificationoccurred(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinotificationfeedbackgenerator/notificationoccurred%28_%3A%29.json'
content_hash: 'sha256:668b0a0e3b7bdd31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINotificationFeedbackGenerator](../uinotificationfeedbackgenerator.md)

# notificationOccurred(_:)

<sub>Instance Method</sub>

Triggers notification feedback.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func notificationOccurred(_ notificationType: UINotificationFeedbackGenerator.FeedbackType)
```

## Parameters

- `notificationType` — The type of notification feedback. For a list of valid notification types, see the [FeedbackType](feedbacktype.md) enumeration.

## Discussion

This method tells the generator that a task or action has succeeded, failed, or produced a warning. In response, the generator may play the appropriate haptics, based on the provided [FeedbackType](feedbacktype.md) value.

For more information on setting up a feedback generator, see the [UIFeedbackGenerator](../uifeedbackgenerator.md) class.

## See Also

### Related Documentation

- [- prepare](<../uifeedbackgenerator/prepare().md>) — Prepares the generator to trigger feedback.

### Producing notification feedback

- [- notificationOccurred:atLocation:](<notificationoccurred(__at_).md>) — Triggers notification feedback at the specified location.
- [FeedbackType](feedbacktype.md) — The type of notification that a notification feedback generator object generates.
