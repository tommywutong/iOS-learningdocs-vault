---
title: 'apply(_:arguments:options:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifilter-swift.class/apply(_:arguments:options:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/apply(_:arguments:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/apply%28_%3Aarguments%3Aoptions%3A%29.json'
content_hash: 'sha256:b8e16415fbfa8962'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# apply(_:arguments:options:)

<sub>Instance Method</sub>

Produces a [CIImage](../ciimage.md) object by applying arguments to a kernel function and using options to control how the kernel function is evaluated.

<sub>macOS</sub>

```swift
func apply(_ k: CIKernel, arguments args: [Any]?, options dict: [String : Any]? = nil) -> CIImage?
```

## Parameters

- `k` — A `CIKernel` object that contains a kernel function.

- `args` — The arguments that are type compatible with the function signature of the kernel function.

- `dict` — A dictionary that contains options (key-value pairs) to control how the kernel function is evaluated.

## Return Value

The [CIImage](../ciimage.md) object produced by a filter.

## Discussion

If you are implementing a custom filter, this method needs to be called from within the [outputImage](outputimage.md) method in order to apply your kernel function to the [CIImage](../ciimage.md) object. You can pass any of the keys defined in [Options for Applying a Filter](../options-for-applying-a-filter.md), along with appropriate values, into the options dictionary.
