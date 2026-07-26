---
title: PHImageRequestOptionsVersion.unadjusted
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptionsversion/unadjusted
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptionsversion/unadjusted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptionsversion/unadjusted.json'
content_hash: 'sha256:af1f916f5e99c5d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageRequestOptionsVersion](../phimagerequestoptionsversion.md)

# PHImageRequestOptionsVersion.unadjusted

<sub>Case</sub>

Request a version of the image asset without adjustments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case unadjusted
```

## Discussion

If the asset has been edited, the resulting image reflects the state of the asset before any edits were performed.

## See Also

### Constants

- [PHImageRequestOptionsVersionCurrent](current.md) — Request the most recent version of the image asset (the one that reflects all edits).
- [PHImageRequestOptionsVersionOriginal](original.md) — Request the original, highest-fidelity version of the image asset.
