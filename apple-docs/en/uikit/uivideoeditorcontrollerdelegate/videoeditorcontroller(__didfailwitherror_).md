---
title: 'videoEditorController(_:didFailWithError:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uivideoeditorcontrollerdelegate/videoeditorcontroller(_:didfailwitherror:)'
source_url: 'https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/videoeditorcontroller(_:didfailwitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uivideoeditorcontrollerdelegate/videoeditorcontroller%28_%3Adidfailwitherror%3A%29.json'
content_hash: 'sha256:b8457620b8937ba6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIVideoEditorControllerDelegate](../uivideoeditorcontrollerdelegate.md)

# videoEditorController(_:didFailWithError:)

<sub>Instance Method</sub>

Notifies the delegate when the video editor is unable to load or save a movie.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func videoEditorController(_ editor: UIVideoEditorController, didFailWithError error: any Error)
```

## Parameters

- `editor` — The video editor that was unable to load or save a movie.

- `error` — The loading or saving error.

## Discussion

Loading a movie into the video editor could fail because of an invalid filesystem path or an invalid media format. Saving could fail because of a lack of disk space or other reasons.
