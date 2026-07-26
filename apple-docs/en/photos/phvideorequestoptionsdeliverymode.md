---
title: PHVideoRequestOptionsDeliveryMode
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phvideorequestoptionsdeliverymode
source_url: 'https://developer.apple.com/documentation/photos/phvideorequestoptionsdeliverymode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phvideorequestoptionsdeliverymode.json'
content_hash: 'sha256:c2e7e92a9b95ec66'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHVideoRequestOptionsDeliveryMode

<sub>Enumeration</sub>

Options for delivering requested video data, used by the [deliveryMode](phvideorequestoptions/deliverymode.md) property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum PHVideoRequestOptionsDeliveryMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [PHVideoRequestOptionsDeliveryModeAutomatic](phvideorequestoptionsdeliverymode/automatic.md) — Photos automatically determines which quality of video data to provide based on the request and current conditions.
- [PHVideoRequestOptionsDeliveryModeHighQualityFormat](phvideorequestoptionsdeliverymode/highqualityformat.md) — Photos provides only the highest quality video available.
- [PHVideoRequestOptionsDeliveryModeMediumQualityFormat](phvideorequestoptionsdeliverymode/mediumqualityformat.md) — Photos provides a video of moderate quality unless a higher quality version is locally cached.
- [PHVideoRequestOptionsDeliveryModeFastFormat](phvideorequestoptionsdeliverymode/fastformat.md) — Photos provides whatever quality of video can be most quickly loaded.

### Initializers

- [init(rawValue:)](<phvideorequestoptionsdeliverymode/init(rawvalue_).md>)

## See Also

### Specifying Video Request Options

- [version](phvideorequestoptions/version.md) — The version of the video to request.
- [PHVideoRequestOptionsVersion](phvideorequestoptionsversion.md) — Options for requesting a video asset with or without adjustments, used by the [version](phvideorequestoptions/version.md) property.
- [deliveryMode](phvideorequestoptions/deliverymode.md) — A mode specifying the requested video quality and delivery priority.
