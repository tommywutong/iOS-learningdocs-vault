---
title: 'init(name:withInputParameters:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifilter-swift.class/init(name:withinputparameters:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/init(name:withinputparameters:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/init%28name%3Awithinputparameters%3A%29.json'
content_hash: 'sha256:593891b0f8f77748'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# init(name:withInputParameters:)

<sub>Initializer</sub>

Creates a [CIFilter](../cifilter-swift.class.md) object for a specific kind of filter and initializes the input values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(name: String, withInputParameters params: [String : Any]?)
```

## Parameters

- `name` — The name of the filter. You must make sure the name is spelled correctly, otherwise your app will run but not produce any output images. For that reason, you should check for the existence of the filter after calling this method.

- `params` — A list of key-value pairs to set as input values to the filter. Each key is a constant that specifies the name of an input parameter for the filter, and the corresponding value is the value for that parameter. See [Core Image Filter Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP40004346) for built-in filters and their allowed parameters.

## Return Value

A [CIFilter](../cifilter-swift.class.md) object whose input values are initialized.

## Discussion

Use this method to quickly create and configure a [CIFilter](../cifilter-swift.class.md) instance, as in the example below.

```objc
CIFilter *f = [CIFilter filterWithName: @"CIColorControls"
                   withInputParameters: @{
                             @"inputImage"      : inImage,
                             @"inputSaturation" : @0.5,
                             @"inputBrightness" : @1.2,
                             @"inputContrast"   : @1.3
                                         }];
```

## See Also

### Creating a filter

- [+ filterWithName:](<init(name_).md>) — Creates a [CIFilter](../cifilter-swift.class.md) object for a specific kind of filter.
