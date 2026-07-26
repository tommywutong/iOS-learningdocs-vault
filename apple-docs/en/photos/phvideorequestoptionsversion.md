---
title: PHVideoRequestOptionsVersion
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phvideorequestoptionsversion
source_url: 'https://developer.apple.com/documentation/photos/phvideorequestoptionsversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phvideorequestoptionsversion.json'
content_hash: 'sha256:522110a273d49add'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHVideoRequestOptionsVersion

<sub>Enumeration</sub>

Options for requesting a video asset with or without adjustments, used by the [version](phvideorequestoptions/version.md) property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum PHVideoRequestOptionsVersion
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [PHVideoRequestOptionsVersionCurrent](phvideorequestoptionsversion/current.md) — Request the most recent version of the video asset, reflecting all edits.
- [PHVideoRequestOptionsVersionOriginal](phvideorequestoptionsversion/original.md) — Request a version of the video asset without adjustments.

### Initializers

- [init(rawValue:)](<phvideorequestoptionsversion/init(rawvalue_).md>)

## See Also

### Specifying Video Request Options

- [version](phvideorequestoptions/version.md) — The version of the video to request.
- [deliveryMode](phvideorequestoptions/deliverymode.md) — A mode specifying the requested video quality and delivery priority.
- [PHVideoRequestOptionsDeliveryMode](phvideorequestoptionsdeliverymode.md) — Options for delivering requested video data, used by the [deliveryMode](phvideorequestoptions/deliverymode.md) property.
