---
title: dataDetectorTypes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/datadetectortypes
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/datadetectortypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/datadetectortypes.json'
content_hash: 'sha256:7aced2e5c64cb2f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# dataDetectorTypes

<sub>Instance Property</sub>

The types of data that convert to tappable URLs in the text view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var dataDetectorTypes: UIDataDetectorTypes { get set }
```

## Discussion

You can use this property to specify the types of data (phone numbers, `http` links, and so on) that should be automatically converted to URLs in the text view. When tapped, the text view opens the application responsible for handling the URL type and passes it the URL. Note that data detection does not occur if the text view’s [editable](iseditable.md) property is set to [true](../../swift/true.md).

## See Also

### Formatting special data in text

- [UIDataDetectorTypes](../uidatadetectortypes.md) — Constants that define the types of information to detect in text-based content.
