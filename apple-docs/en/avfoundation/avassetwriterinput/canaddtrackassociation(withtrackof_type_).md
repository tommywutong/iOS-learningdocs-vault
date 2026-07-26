---
title: 'canAddTrackAssociation(withTrackOf:type:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinput/canaddtrackassociation(withtrackof:type:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/canaddtrackassociation(withtrackof:type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/canaddtrackassociation%28withtrackof%3Atype%3A%29.json'
content_hash: 'sha256:abd1d0c82642dae1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# canAddTrackAssociation(withTrackOf:type:)

<sub>Instance Method</sub>

Determines whether it’s valid to associate another input’s track with this input’s track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func canAddTrackAssociation(withTrackOf input: AVAssetWriterInput, type trackAssociationType: String) -> Bool
```

## Parameters

- `input` — An asset writer input that contains the track to associate.

- `trackAssociationType` — The type of track association to test.

## Return Value

[true](../../swift/true.md) if the system can make the association between tracks; otherwise, [false](../../swift/false.md).

## Discussion

This method returns [false](../../swift/false.md) if the association type requires tracks of a media type that doesn’t match the input’s type, or if the output file type doesn’t support track associations.

## See Also

### Configuring track associations

- [- addTrackAssociationWithTrackOfInput:type:](<addtrackassociation(withtrackof_type_).md>) — Adds an association between input tracks.
