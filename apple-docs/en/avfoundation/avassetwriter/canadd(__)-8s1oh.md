---
title: 'canAdd(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriter/canadd(_:)-8s1oh'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/canadd(_:)-8s1oh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/canadd%28_%3A%29-8s1oh.json'
content_hash: 'sha256:32d11f6c533f6dba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# canAdd(_:)

<sub>Instance Method</sub>

Determines whether the asset writer supports adding the input group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func canAdd(_ inputGroup: AVAssetWriterInputGroup) -> Bool
```

## Parameters

- `inputGroup` — The asset writer input group to add.

## Return Value

[true](../../swift/true.md) if you can add the input group to the asset writer; otherwise [false](../../swift/false.md).

## Discussion

This method returns [false](../../swift/false.md) if the asset writer’s output file type doesn’t support mutually exclusive relationships among tracks, or if the input group contains inputs with media types that you can’t relate.

## See Also

### Configuring input groups

- [inputGroups](inputgroups.md) — The input groups an asset writer contains.
- [- addInputGroup:](<add(__)-3san4.md>) — Adds an input group to an asset writer.
