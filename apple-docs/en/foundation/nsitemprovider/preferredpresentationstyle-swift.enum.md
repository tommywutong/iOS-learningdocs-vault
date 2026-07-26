---
title: NSItemProvider.PreferredPresentationStyle
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemprovider/preferredpresentationstyle-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/preferredpresentationstyle-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/preferredpresentationstyle-swift.enum.json'
content_hash: 'sha256:31ab510b8ce42b98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# NSItemProvider.PreferredPresentationStyle

<sub>Enumeration</sub>

The presentation styles that determine how a view shows an item provider’s data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
enum PreferredPresentationStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Presentation Styles

- [NSItemProvider.PreferredPresentationStyle.unspecified](preferredpresentationstyle-swift.enum/unspecified.md) — A presentation style indicating that no preferred style is specified.
- [NSItemProvider.PreferredPresentationStyle.inline](preferredpresentationstyle-swift.enum/inline.md) — A presentation style indicating that the item provider data should be presented inline.
- [NSItemProvider.PreferredPresentationStyle.attachment](preferredpresentationstyle-swift.enum/attachment.md) — A presentation style indicating that the item provider data should be presented as an attachment.

### Initializers

- [init(rawValue:)](<preferredpresentationstyle-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring the provider

- [preferredPresentationSize](preferredpresentationsize.md) — The ideal presentation size of the item.
- [preferredPresentationStyle](preferredpresentationstyle-swift.property.md) — The preferred style for presenting the item provider’s data.
- [suggestedName](suggestedname.md) — The filename to use when writing the provided data to a file on disk.
- [teamData](teamdata.md) — The collection of data an app uses to hold private team information during drag and drop.
