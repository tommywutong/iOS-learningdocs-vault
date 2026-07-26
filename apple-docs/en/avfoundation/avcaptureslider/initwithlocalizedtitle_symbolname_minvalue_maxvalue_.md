---
title: 'initWithLocalizedTitle:symbolName:minValue:maxValue:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureslider/initwithlocalizedtitle:symbolname:minvalue:maxvalue:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureslider/initwithlocalizedtitle:symbolname:minvalue:maxvalue:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureslider/initwithlocalizedtitle%3Asymbolname%3Aminvalue%3Amaxvalue%3A.json'
content_hash: 'sha256:508369e7b15ea0c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSlider](../avcaptureslider.md)

# initWithLocalizedTitle:symbolName:minValue:maxValue:

<sub>Instance Method</sub>

Creates a continuous slider control that selects a value from a bounded range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithLocalizedTitle:(NSString *) localizedTitle symbolName:(NSString *) symbolName minValue:(float) minValue maxValue:(float) maxValue;
```

## Parameters

- `localizedTitle` — A localized title that describes the slider’s action.

- `symbolName` — A symbol name from the SF Symbols library.

- `minValue` — The lower bound of the range.

- `maxValue` — The upper bound of the range.

## Discussion

Use continuous sliders when your use case supports selecting any value in the specified range.

## See Also

### Creating a slider

- [initWithLocalizedTitle:symbolName:minValue:maxValue:step:](initwithlocalizedtitle_symbolname_minvalue_maxvalue_step_.md) — Creates a discrete slider control that selects a stepped value from a bounded range.
- [initWithLocalizedTitle:symbolName:values:](initwithlocalizedtitle_symbolname_values_.md) — Creates a discrete slider control that selects a value from a list.
