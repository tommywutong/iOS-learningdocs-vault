---
title: videoQuality
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uivideoeditorcontroller/videoquality
source_url: 'https://developer.apple.com/documentation/uikit/uivideoeditorcontroller/videoquality'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uivideoeditorcontroller/videoquality.json'
content_hash: 'sha256:ca59d894ad39b528'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIVideoEditorController](../uivideoeditorcontroller.md)

# videoQuality

<sub>Instance Property</sub>

The video quality to use when saving a trimmed movie.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var videoQuality: UIImagePickerController.QualityType { get set }
```

## Discussion

The available video qualities are described in the [QualityType](../uiimagepickercontroller/qualitytype.md) enumeration. The default value for this property is [UIImagePickerControllerQualityTypeLow](../uiimagepickercontroller/qualitytype/typelow.md).

If a user attempts to reencode a movie to a higher quality, the movie is saved at its existing quality. Reencoding never increases movie dimensions, frame rate, or bit rate.

## See Also

### Configuring the editor

- [videoMaximumDuration](videomaximumduration.md) — The maximum duration, in seconds, permitted for trimmed movies saved by the video editor.
- [videoPath](videopath.md) — The filesystem path to the movie to be loaded by the video editor.
