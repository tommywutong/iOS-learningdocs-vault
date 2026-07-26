---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccelerometer/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uiaccelerometer/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccelerometer/delegate.json'
content_hash: 'sha256:3fd0106cfc5ef46a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccelerometer](../uiaccelerometer.md)

# delegate

<sub>Instance Property</sub>

The delegate object you want to receive acceleration events.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, weak, nullable) id<UIAccelerometerDelegate> delegate;
```

## Discussion

The [UIAccelerometerDelegate](../uiaccelerometerdelegate.md) is a formal protocol, so your delegate object must implement the method it defines. The shared accelerometer object delivers the acceleration data to your delegate at the specified interval. It delivers these events on the main thread of your application when it is in the NSDefaultRunLoopMode run loop mode.

## See Also

### Accessing the accelerometer properties

- [updateInterval](updateinterval.md) — The interval at which to deliver acceleration data to the delegate. _(deprecated)_
