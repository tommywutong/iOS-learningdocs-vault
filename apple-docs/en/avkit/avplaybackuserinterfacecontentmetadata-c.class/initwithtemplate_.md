---
title: 'initWithTemplate:'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: '/documentation/avkit/avplaybackuserinterfacecontentmetadata-c.class/initwithtemplate:'
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentmetadata-c.class/initwithtemplate:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacecontentmetadata-c.class/initwithtemplate%3A.json'
content_hash: 'sha256:fd8d0797cf24144d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceContentMetadata](../avplaybackuserinterfacecontentmetadata-c.class.md)

# initWithTemplate:

<sub>Instance Method</sub>

Initializes a new metadata object by copying values from a metadata template.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
- (instancetype) initWithTemplate:(AVPlaybackUserInterfaceContentMetadataTemplate *) metadataTemplate;
```

## Parameters

- `metadataTemplate` — The metadata template to copy values from. If `nil`, returns a metadata object with default values.

## Discussion

This initializer creates an immutable [AVPlaybackUserInterfaceContentMetadata](../avplaybackuserinterfacecontentmetadata-c.class.md) instance from a mutable [AVPlaybackUserInterfaceContentMetadataTemplate](../avplaybackuserinterfacecontentmetadatatemplate.md), providing a convenient way to convert configured template data into stable metadata for playback interfaces.

All properties from the template are copied into the new metadata object, creating an independent immutable snapshot of the template’s current state. Subsequent changes to the template will not affect the created metadata object.
