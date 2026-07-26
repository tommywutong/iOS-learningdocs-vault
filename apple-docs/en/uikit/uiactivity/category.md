---
title: UIActivity.Category
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivity/category
source_url: 'https://developer.apple.com/documentation/uikit/uiactivity/category'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivity/category.json'
content_hash: 'sha256:5111ae4ebf749ab7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivity](../uiactivity.md)

# UIActivity.Category

<sub>Enumeration</sub>

An enumeration that defines categories of activities.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum Category
```

## Overview

Activities have a defined category, and the activity UI may show activities grouped by category.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIActivityCategoryAction](category/action.md) — Activities whose primary purpose is to take an action on the selected item, like copying an image or saving it to the camera roll.
- [UIActivityCategoryShare](category/share.md) — Activities whose primary purpose is to share the selected item, like sending an image by email.

### Initializers

- [init(rawValue:)](<category/init(rawvalue_).md>)

## See Also

### Getting the activity information

- [activityCategory](activitycategory.md) — The category of the activity, which may be used to group activities in the UI.
- [activityType](activitytype-swift.property.md) — The type of service being provided.
- [ActivityType](activitytype-swift.struct.md) — A structure that describes the types of activities for which the system has built-in support.
- [activityTitle](activitytitle.md) — A user-readable string that describes the service.
- [activityImage](activityimage.md) — An image that identifies the service to the user.
