---
title: PHImageRequestOptionsVersion.current
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptionsversion/current
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptionsversion/current'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptionsversion/current.json'
content_hash: 'sha256:f620829ec5baed2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageRequestOptionsVersion](../phimagerequestoptionsversion.md)

# PHImageRequestOptionsVersion.current

<sub>Case</sub>

Request the most recent version of the image asset (the one that reflects all edits).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case current
```

## Discussion

The resulting image is the rendered output from all previously made adjustments.

## See Also

### Constants

- [PHImageRequestOptionsVersionUnadjusted](unadjusted.md) — Request a version of the image asset without adjustments.
- [PHImageRequestOptionsVersionOriginal](original.md) — Request the original, highest-fidelity version of the image asset.
