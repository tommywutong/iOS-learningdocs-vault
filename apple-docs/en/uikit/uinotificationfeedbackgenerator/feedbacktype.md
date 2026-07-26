---
title: UINotificationFeedbackGenerator.FeedbackType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinotificationfeedbackgenerator/feedbacktype
source_url: 'https://developer.apple.com/documentation/uikit/uinotificationfeedbackgenerator/feedbacktype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinotificationfeedbackgenerator/feedbacktype.json'
content_hash: 'sha256:3ec7aefb50f401df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINotificationFeedbackGenerator](../uinotificationfeedbackgenerator.md)

# UINotificationFeedbackGenerator.FeedbackType

<sub>Enumeration</sub>

The type of notification that a notification feedback generator object generates.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum FeedbackType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UINotificationFeedbackTypeError](feedbacktype/error.md) — A notification feedback type that indicates a task has failed.
- [UINotificationFeedbackTypeSuccess](feedbacktype/success.md) — A notification feedback type that indicates a task has completed successfully.
- [UINotificationFeedbackTypeWarning](feedbacktype/warning.md) — A notification feedback type that indicates a task has produced a warning.

### Initializers

- [init(rawValue:)](<feedbacktype/init(rawvalue_).md>)

## See Also

### Producing notification feedback

- [- notificationOccurred:](<notificationoccurred(__).md>) — Triggers notification feedback.
- [- notificationOccurred:atLocation:](<notificationoccurred(__at_).md>) — Triggers notification feedback at the specified location.
