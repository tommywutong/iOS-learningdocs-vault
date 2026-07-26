---
title: 'initWithTemplate:'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avinterfacemetadata/initwithtemplate:'
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacemetadata/initwithtemplate:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacemetadata/initwithtemplate%3A.json'
content_hash: 'sha256:31fbeee6cccf6c83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInterfaceMetadata](../avinterfacemetadata.md)

# initWithTemplate:

<sub>Instance Method</sub>

Initializes a new metadata object by copying values from a metadata template.

<sub>tvOS, visionOS</sub>

```objc
- (instancetype) initWithTemplate:(AVInterfaceMetadataTemplate *) metadataTemplate;
```

## Parameters

- `metadataTemplate` — The metadata template to copy values from. If nil, returns a metadata object with default values.

## Discussion

This initializer creates an immutable `AVInterfaceMetadata` instance from a mutable `AVInterfaceMetadataTemplate`, providing a convenient way to convert configured template data into stable metadata for playback interfaces.

All properties from the template are copied into the new metadata object, creating an independent immutable snapshot of the template’s current state. Subsequent changes to the template will not affect the created metadata object.

## See Also

### Creating metadata

- [initWithAudioOnly:presentationSize:title:subtitle:albumArtworkRepresentations:](initwithaudioonly_presentationsize_title_subtitle_albumartworkrepresentations_.md) — Initializes a new metadata object with the specified properties.
