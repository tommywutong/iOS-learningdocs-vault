---
title: 'canEditVideo(atPath:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uivideoeditorcontroller/caneditvideo(atpath:)'
source_url: 'https://developer.apple.com/documentation/uikit/uivideoeditorcontroller/caneditvideo(atpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uivideoeditorcontroller/caneditvideo%28atpath%3A%29.json'
content_hash: 'sha256:802fbbdfc5c3cdd3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIVideoEditorController](../uivideoeditorcontroller.md)

# canEditVideo(atPath:)

<sub>Type Method</sub>

Returns a Boolean value indicating whether a video file can be edited.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class func canEditVideo(atPath videoPath: String) -> Bool
```

## Parameters

- `videoPath` — The filesystem path to the video file you want to edit.

## Return Value

[true](../../swift/true.md) if the specified video file can be edited on the current device or [false](../../swift/false.md) if it cannot.

## Discussion

Video editing requires the presence of specific hardware and is available only for specific file formats. Use this method to check whether video editing is available for a given video file, before you create a video editor.
