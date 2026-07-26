---
title: 'convert(_:consumer:options:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+, macOS 10.3+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpsconverter/convert(_:consumer:options:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpsconverter/convert(_:consumer:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpsconverter/convert%28_%3Aconsumer%3Aoptions%3A%29.json'
content_hash: 'sha256:e7395fbff2451d52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPSConverter](../cgpsconverter.md)

# convert(_:consumer:options:)

<sub>Instance Method</sub>

Uses a PostScript converter to convert PostScript data to PDF data.

<sub>Mac Catalyst, macOS</sub>

```swift
func convert(_ provider: CGDataProvider, consumer: CGDataConsumer, options: CFDictionary?) -> Bool
```

## Parameters

- `provider` — A Quartz data provider that supplies PostScript data.

- `consumer` — A Quartz data provider that will receive the resulting PDF data.

- `options` — This parameter should be `NULL`; it is reserved for future expansion of the API.

## Return Value

A Boolean value that indicates whether the PostScript conversion completed successfully (`true` if it did).

## Discussion

The conversion is thread safe, however it is not possible to have more than one conversion job in process within a given address space or process. If a given thread is running a conversion and another thread starts a new conversion, the second conversion will block until the first conversion is complete.

> [!important] Important
> Although `CGPSConverterConvert` is thread safe (it uses locks to prevent more than one conversion at a time in the same process), it is not thread safe with respect to the Resource Manager. If your application uses the Resource Manager on a separate thread, you should either use locks to prevent `CGPSConverterConvert` from executing during your usage of the Resource Manager or you should perform your conversions using the Post Script converter in a separate process.
>
> In general, you can avoid this issue by using nib files instead of Resource Manager resources.

## See Also

### Instance Methods

- [CGPSConverterAbort](<abort().md>) — Tells a PostScript converter to abort a conversion at the next available opportunity.
