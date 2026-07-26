---
title: videoMaximumDuration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uivideoeditorcontroller/videomaximumduration
source_url: 'https://developer.apple.com/documentation/uikit/uivideoeditorcontroller/videomaximumduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uivideoeditorcontroller/videomaximumduration.json'
content_hash: 'sha256:657101e077882b5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIVideoEditorController](../uivideoeditorcontroller.md)

# videoMaximumDuration

<sub>Instance Property</sub>

The maximum duration, in seconds, permitted for trimmed movies saved by the video editor.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var videoMaximumDuration: TimeInterval { get set }
```

## Discussion

The system-enforced maximum duration for a video recording is 10 minutes; you can set this value to 10 minutes or less. The default value for this property is also 10 minutes.

The video editor user interface forces the user to trim a loaded movie to fit within this property’s value prior to saving.

## See Also

### Configuring the editor

- [videoPath](videopath.md) — The filesystem path to the movie to be loaded by the video editor.
- [videoQuality](videoquality.md) — The video quality to use when saving a trimmed movie.
