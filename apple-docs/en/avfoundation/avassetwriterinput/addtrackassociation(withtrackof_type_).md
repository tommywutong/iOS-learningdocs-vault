---
title: 'addTrackAssociation(withTrackOf:type:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinput/addtrackassociation(withtrackof:type:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/addtrackassociation(withtrackof:type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/addtrackassociation%28withtrackof%3Atype%3A%29.json'
content_hash: 'sha256:5e8ba61b908acffa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# addTrackAssociation(withTrackOf:type:)

<sub>Instance Method</sub>

Adds an association between input tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addTrackAssociation(withTrackOf input: AVAssetWriterInput, type trackAssociationType: String)
```

## Parameters

- `input` — The input that contains the track to associate with this input’s track.

- `trackAssociationType` — The type of track association to add.

## Discussion

The system raises an error if the association type requires tracks of a media type that doesn’t match the input’s type, or if the output file type doesn’t support track associations.

You can’t add track associations after writing starts.

## See Also

### Configuring track associations

- [- canAddTrackAssociationWithTrackOfInput:type:](<canaddtrackassociation(withtrackof_type_).md>) — Determines whether it’s valid to associate another input’s track with this input’s track.
