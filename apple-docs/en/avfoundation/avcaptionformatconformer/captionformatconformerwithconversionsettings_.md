---
title: 'captionFormatConformerWithConversionSettings:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptionformatconformer/captionformatconformerwithconversionsettings:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionformatconformer/captionformatconformerwithconversionsettings:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionformatconformer/captionformatconformerwithconversionsettings%3A.json'
content_hash: 'sha256:045ef49da92ba167'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionFormatConformer](../avcaptionformatconformer.md)

# captionFormatConformerWithConversionSettings:

<sub>Type Method</sub>

A class method that creates a new object with format conversion settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```objc
+ (instancetype) captionFormatConformerWithConversionSettings:(NSDictionary<NSString *,id> *) conversionSettings;
```

## Parameters

- `conversionSettings` — A dictionary that specifies the conversion settings that this instance uses.

## Return Value

A new instance of [AVCaptionFormatConformer](../avcaptionformatconformer.md).

## See Also

### Creating a format conformer

- [- initWithConversionSettings:](<init(conversionsettings_).md>) — Creates a new object with format conversion settings.
