---
title: 'initWithLocalizedTitle:symbolName:minValue:maxValue:step:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureslider/initwithlocalizedtitle:symbolname:minvalue:maxvalue:step:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureslider/initwithlocalizedtitle:symbolname:minvalue:maxvalue:step:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureslider/initwithlocalizedtitle%3Asymbolname%3Aminvalue%3Amaxvalue%3Astep%3A.json'
content_hash: 'sha256:9f031266bd48e04c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSlider](../avcaptureslider.md)

# initWithLocalizedTitle:symbolName:minValue:maxValue:step:

<sub>Instance Method</sub>

Creates a discrete slider control that selects a stepped value from a bounded range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithLocalizedTitle:(NSString *) localizedTitle symbolName:(NSString *) symbolName minValue:(float) minValue maxValue:(float) maxValue step:(float) step;
```

## Parameters

- `localizedTitle` — A localized title that describes the slider’s action.

- `symbolName` — A symbol name from the SF Symbols library.

- `minValue` — The lower bound of the range.

- `maxValue` — The upper bound of the range.

- `step` — The distance between each valid value. This specified value must be greater than `0` or the system throws an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md).

## Discussion

Use discrete sliders when your use case supports selecting stepped values within the specified range.

## See Also

### Creating a slider

- [initWithLocalizedTitle:symbolName:minValue:maxValue:](initwithlocalizedtitle_symbolname_minvalue_maxvalue_.md) — Creates a continuous slider control that selects a value from a bounded range.
- [initWithLocalizedTitle:symbolName:values:](initwithlocalizedtitle_symbolname_values_.md) — Creates a discrete slider control that selects a value from a list.
