---
title: PHImageRequestOptionsVersion.original
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptionsversion/original
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptionsversion/original'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptionsversion/original.json'
content_hash: 'sha256:9e849096ddffd224'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageRequestOptionsVersion](../phimagerequestoptionsversion.md)

# PHImageRequestOptionsVersion.original

<sub>Case</sub>

Request the original, highest-fidelity version of the image asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case original
```

## Discussion

The resulting image is originally captured or imported version of the asset, regardless of any edits made.

If the image asset contains data in multiple formats, the resulting image data uses the highest quality format. For example, for an asset containing both RAW and JPEG data, Photos returns the RAW data.

## See Also

### Constants

- [PHImageRequestOptionsVersionCurrent](current.md) — Request the most recent version of the image asset (the one that reflects all edits).
- [PHImageRequestOptionsVersionUnadjusted](unadjusted.md) — Request a version of the image asset without adjustments.
