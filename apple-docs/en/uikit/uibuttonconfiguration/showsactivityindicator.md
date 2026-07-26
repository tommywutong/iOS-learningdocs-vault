---
title: showsActivityIndicator
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/showsactivityindicator
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/showsactivityindicator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/showsactivityindicator.json'
content_hash: 'sha256:6ef53d81f9be9db2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# showsActivityIndicator

<sub>Instance Property</sub>

A Boolean value that determines whether the button displays an activity indicator instead of an image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, assign, readwrite) BOOL showsActivityIndicator;
```

## Discussion

The button respects the [imagePlacement](imageplacement.md) property when positioning the activity indicator.

## See Also

### Configuring the activity indicator

- [activityIndicatorColorTransformer](activityindicatorcolortransformer.md) — The color transformer for resolving the color of the activity indicator.
