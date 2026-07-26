---
title: 'init(name:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifilter-swift.class/init(name:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/init(name:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/init%28name%3A%29.json'
content_hash: 'sha256:44cc4720a3d92404'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# init(name:)

<sub>Initializer</sub>

Creates a [CIFilter](../cifilter-swift.class.md) object for a specific kind of filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(name: String)
```

## Parameters

- `name` — The name of the filter. You must make sure the name is spelled correctly, otherwise your app will run but not produce any output images. For that reason, you should check for the existence of the filter after calling this method.

## Return Value

A [CIFilter](../cifilter-swift.class.md) object whose input values are undefined.

## Discussion

In macOS, after creating a filter with this method you must call [- setDefaults](<setdefaults().md>) or set parameters individually by calling [setValue(_:forKey:)](<../../objectivec/nsobject-swift.class/setvalue(__forkey_).md>). In iOS, the filter’s parameters are automatically set to default values.

## See Also

### Related Documentation

- [Image Unit Tutorial](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageUnitTutorial/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004531)
- [Core Image Filter Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP40004346)
- [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)

### Creating a filter

- [init(name:withInputParameters:)](<init(name_withinputparameters_).md>) — Creates a [CIFilter](../cifilter-swift.class.md) object for a specific kind of filter and initializes the input values.
