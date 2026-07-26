---
title: UIDropSessionProgressIndicatorStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidropsessionprogressindicatorstyle
source_url: 'https://developer.apple.com/documentation/uikit/uidropsessionprogressindicatorstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropsessionprogressindicatorstyle.json'
content_hash: 'sha256:7f274f1fd2918d14'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDropSessionProgressIndicatorStyle

<sub>Enumeration</sub>

The drop-progress indicator styles for the drop session, used while data is moving from the source to the destination.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum UIDropSessionProgressIndicatorStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Progress indicator styles

- [UIDropSessionProgressIndicatorStyleDefault](uidropsessionprogressindicatorstyle/default.md) — The indicator style for using the system’s default drop-progress indication.
- [UIDropSessionProgressIndicatorStyleNone](uidropsessionprogressindicatorstyle/none.md) — The indicator style for no drop-progress indication.

### Initializers

- [init(rawValue:)](<uidropsessionprogressindicatorstyle/init(rawvalue_).md>)

## See Also

### Drop destinations

- [UIDropSession](uidropsession.md) — The interface for querying a drop session about its state and associated drag items.
- [UIDropProposal](uidropproposal.md) — A configuration for the behavior of a drop interaction, required if a view accepts drop activities.
- [UIDropOperation](uidropoperation.md) — Operation types that determine how a drag and drop activity resolves when the user drops a drag item.
