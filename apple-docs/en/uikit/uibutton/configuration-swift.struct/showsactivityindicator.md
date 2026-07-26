---
title: showsActivityIndicator
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/showsactivityindicator
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/showsactivityindicator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/showsactivityindicator.json'
content_hash: 'sha256:d25fcc55dfaeecd8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# showsActivityIndicator

<sub>Instance Property</sub>

A Boolean value that determines whether the button displays an activity indicator instead of an image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var showsActivityIndicator: Bool { get set }
```

## Discussion

The button respects the [imagePlacement](imageplacement.md) property when positioning the activity indicator.

## See Also

### Configuring the activity indicator

- [activityIndicatorColorTransformer](activityindicatorcolortransformer.md) — The color transformer for resolving the color of the activity indicator.
