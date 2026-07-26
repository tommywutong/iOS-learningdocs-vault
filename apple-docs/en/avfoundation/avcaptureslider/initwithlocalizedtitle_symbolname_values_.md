---
title: 'initWithLocalizedTitle:symbolName:values:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureslider/initwithlocalizedtitle:symbolname:values:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureslider/initwithlocalizedtitle:symbolname:values:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureslider/initwithlocalizedtitle%3Asymbolname%3Avalues%3A.json'
content_hash: 'sha256:3b3bf43047bbb3ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSlider](../avcaptureslider.md)

# initWithLocalizedTitle:symbolName:values:

<sub>Instance Method</sub>

Creates a discrete slider control that selects a value from a list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithLocalizedTitle:(NSString *) localizedTitle symbolName:(NSString *) symbolName values:(NSArray<NSNumber *> *) values;
```

## Parameters

- `localizedTitle` — A localized title that describes the slider’s action.

- `symbolName` — A symbol name from the SF Symbols library.

- `values` — An array of floating-point values.

## Discussion

Use discrete sliders when your app supports selecting from a specific list of values.

## See Also

### Creating a slider

- [initWithLocalizedTitle:symbolName:minValue:maxValue:](initwithlocalizedtitle_symbolname_minvalue_maxvalue_.md) — Creates a continuous slider control that selects a value from a bounded range.
- [initWithLocalizedTitle:symbolName:minValue:maxValue:step:](initwithlocalizedtitle_symbolname_minvalue_maxvalue_step_.md) — Creates a discrete slider control that selects a stepped value from a bounded range.
