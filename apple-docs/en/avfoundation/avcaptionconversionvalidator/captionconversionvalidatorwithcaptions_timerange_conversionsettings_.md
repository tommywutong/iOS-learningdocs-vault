---
title: 'captionConversionValidatorWithCaptions:timeRange:conversionSettings:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptionconversionvalidator/captionconversionvalidatorwithcaptions:timerange:conversionsettings:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator/captionconversionvalidatorwithcaptions:timerange:conversionsettings:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionconversionvalidator/captionconversionvalidatorwithcaptions%3Atimerange%3Aconversionsettings%3A.json'
content_hash: 'sha256:cff9418a17ff7fe3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionConversionValidator](../avcaptionconversionvalidator.md)

# captionConversionValidatorWithCaptions:timeRange:conversionSettings:

<sub>Type Method</sub>

A convenience initializer to create an object that validates captions for a conversion operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```objc
+ (instancetype) captionConversionValidatorWithCaptions:(NSArray<AVCaption *> *) captions timeRange:(CMTimeRange) timeRange conversionSettings:(NSDictionary<NSString *,id> *) conversionSettings;
```

## Parameters

- `captions` — The array of captions that the system validates.

- `timeRange` — The time range of the media timeline where the captions exist.

- `conversionSettings` — A dictionary that describes the conversion operation.

## See Also

### Creating a validator

- [- initWithCaptions:timeRange:conversionSettings:](<init(captions_timerange_conversionsettings_).md>) — Creates an object that validates captions for a conversion operation.
