---
title: sequenceCount
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/sequencecount
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/sequencecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/sequencecount.json'
content_hash: 'sha256:5137cff0ec0aaf0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# sequenceCount

<sub>Instance Property</sub>

The 1-based index of this photo in a bracketed capture sequence.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var sequenceCount: Int { get }
```

## Discussion

If this photo is part of a bracketed capture (requested with the [AVCapturePhotoBracketSettings](../avcapturephotobracketsettings.md) class), this property indicates the current result’s count in the sequence, starting with `1` for the first result.

If this photo is not part of a bracketed capture, this property’s value is `0`.

## See Also

### Examining bracketed capture information

- [bracketSettings](bracketsettings.md) — The variations available for bracketed capture settings for this photo.
- [lensStabilizationStatus](lensstabilizationstatus.md) — Information about the use of lens stabilization during bracketed photo capture.
- [LensStabilizationStatus](../avcapturedevice/lensstabilizationstatus.md) — Constants that indicate the status of optical image stabilization hardware during a bracketed photo capture.
