---
title: updateInterval
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccelerometer/updateinterval
source_url: 'https://developer.apple.com/documentation/uikit/uiaccelerometer/updateinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccelerometer/updateinterval.json'
content_hash: 'sha256:cd6d75cb3e63b8ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccelerometer](../uiaccelerometer.md)

# updateInterval

<sub>Instance Property</sub>

The interval at which to deliver acceleration data to the delegate.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) NSTimeInterval updateInterval;
```

## Discussion

This property is measured in seconds. The value of this property is capped to certain minimum and maximum values. The maximum value is determined by the maximum frequency supported by the hardware. To ensure that it can deliver device orientation events in a timely fashion, the system determines the appropriate minimum value based on its needs.

Changes to this property are delivered synchronously to the accelerometer hardware. You may change this property while the delegate is non-`nil`.

## See Also

### Accessing the accelerometer properties

- [delegate](delegate.md) — The delegate object you want to receive acceleration events. _(deprecated)_
