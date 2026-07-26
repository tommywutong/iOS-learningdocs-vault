---
title: 'initWithFormatDescription:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avspatialvideoconfiguration-c.class/initwithformatdescription:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avspatialvideoconfiguration-c.class/initwithformatdescription:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avspatialvideoconfiguration-c.class/initwithformatdescription%3A.json'
content_hash: 'sha256:d5692011c702ef76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSpatialVideoConfiguration](../avspatialvideoconfiguration-c.class.md)

# initWithFormatDescription:

<sub>Instance Method</sub>

Initializes an AVSpatialVideoConfiguration with a format description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithFormatDescription:(CMFormatDescriptionRef) formatDescription;
```

## Parameters

- `formatDescription` — Format description to use to initialize the AVSpatialVideoConfiguration.

## Return Value

An instance of AVSpatialVideoConfiguration

## Discussion

The format description is not stored.

## See Also

### Creating a configuration

- [init](init.md)
