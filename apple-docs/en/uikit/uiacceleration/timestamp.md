---
title: timestamp
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiacceleration/timestamp
source_url: 'https://developer.apple.com/documentation/uikit/uiacceleration/timestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiacceleration/timestamp.json'
content_hash: 'sha256:14a32e079813e03a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAcceleration](../uiacceleration.md)

# timestamp

<sub>Instance Property</sub>

The relative time at which the acceleration event occurred.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) NSTimeInterval timestamp;
```

## Discussion

This value indicates the time relative to the device CPU time base register. Compare acceleration event timestamps to determine the elapsed time between them. Do not use a timestamp to determine the exact time at which an event occurred.

## See Also

### Accessing the acceleration values

- [x](x.md) — The acceleration value for the x axis of the device. _(deprecated)_
- [y](y.md) — The acceleration value for the y axis of the device. _(deprecated)_
- [z](z.md) — The acceleration value for the z axis of the device. _(deprecated)_
