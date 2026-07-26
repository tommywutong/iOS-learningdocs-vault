---
title: sharedAccelerometer
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccelerometer/sharedaccelerometer
source_url: 'https://developer.apple.com/documentation/uikit/uiaccelerometer/sharedaccelerometer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccelerometer/sharedaccelerometer.json'
content_hash: 'sha256:b41242f4f1ed6d40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccelerometer](../uiaccelerometer.md)

# sharedAccelerometer

<sub>Type Method</sub>

Returns the shared accelerometer object for the system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (UIAccelerometer *) sharedAccelerometer;
```

## Return Value

The systemwide accelerometer object.

## Discussion

Always use this method to retrieve the shared system accelerometer object. Do not create new instances of the `UIAccelerometer` class.
