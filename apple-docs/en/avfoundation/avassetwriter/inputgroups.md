---
title: inputGroups
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/inputgroups
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/inputgroups'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/inputgroups.json'
content_hash: 'sha256:f8f4cdcea6f51220'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# inputGroups

<sub>Instance Property</sub>

The input groups an asset writer contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var inputGroups: [AVAssetWriterInputGroup] { get }
```

## Discussion

Add input groups to the asset writer using its [- addInputGroup:](<add(__)-3san4.md>) method.

## See Also

### Configuring input groups

- [- canAddInputGroup:](<canadd(__)-8s1oh.md>) — Determines whether the asset writer supports adding the input group.
- [- addInputGroup:](<add(__)-3san4.md>) — Adds an input group to an asset writer.
