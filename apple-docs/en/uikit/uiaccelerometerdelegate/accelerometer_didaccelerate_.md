---
title: 'accelerometer:didAccelerate:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccelerometerdelegate/accelerometer:didaccelerate:'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccelerometerdelegate/accelerometer:didaccelerate:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccelerometerdelegate/accelerometer%3Adidaccelerate%3A.json'
content_hash: 'sha256:b1ea75c53a86c6f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccelerometerDelegate](../uiaccelerometerdelegate.md)

# accelerometer:didAccelerate:

<sub>Instance Method</sub>

Delivers the latest acceleration data to the delegate.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) accelerometer:(UIAccelerometer *) accelerometer didAccelerate:(UIAcceleration *) acceleration;
```

## Parameters

- `accelerometer` — The application-wide accelerometer object.

- `acceleration` — The most recent acceleration data.

## Discussion

The shared [UIAccelerometer](../uiaccelerometer.md) object invokes this method at the desired interval, providing your delegate with updated acceleration data each time.

This method is always invoked on your application’s main thread when it is in the NSDefaultRunLoopMode run loop mode.
