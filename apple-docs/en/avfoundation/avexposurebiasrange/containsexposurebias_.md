---
title: 'containsExposureBias:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avexposurebiasrange/containsexposurebias:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avexposurebiasrange/containsexposurebias:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexposurebiasrange/containsexposurebias%3A.json'
content_hash: 'sha256:7a11a4f4abf66283'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExposureBiasRange](../avexposurebiasrange.md)

# containsExposureBias:

<sub>Instance Method</sub>

Determines whether the range contains the specified exposure bias.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (BOOL) containsExposureBias:(float) exposureBias;
```

## Parameters

- `exposureBias` — The exposure bias to test, in EV units.

## Return Value

`true` if the range contains the exposure bias; otherwise, `false`.

## See Also

### Inspecting the exposure bias range

- [minExposureBias](minexposurebias.md) — The minimum exposure bias in EV units that this range supports.
- [maxExposureBias](maxexposurebias.md) — The maximum exposure bias in EV units that this range supports.
