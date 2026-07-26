---
title: 'init(formatDescription:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avspatialvideoconfiguration-swift.struct/init(formatdescription:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avspatialvideoconfiguration-swift.struct/init(formatdescription:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avspatialvideoconfiguration-swift.struct/init%28formatdescription%3A%29.json'
content_hash: 'sha256:acda6a968fb4298b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSpatialVideoConfiguration](../avspatialvideoconfiguration-swift.struct.md)

# init(formatDescription:)

<sub>Initializer</sub>

Initializes an AVSpatialVideoConfiguration with a format description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(formatDescription: CMFormatDescription)
```

## Parameters

- `formatDescription` — Format description to use to initialize the AVSpatialVideoConfiguration.

## Return Value

An instance of AVSpatialVideoConfiguration

## Discussion

The format description is not stored.

## See Also

### Creating a configuration

- [init()](<init().md>) — Initializes an AVSpatialVideoConfiguration instance with all the properties set to nil.
- [nonSpatial](nonspatial.md) — A non-spatial video configuration.
