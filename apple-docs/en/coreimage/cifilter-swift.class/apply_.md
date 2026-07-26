---
title: 'apply:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifilter-swift.class/apply:'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/apply:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/apply%3A.json'
content_hash: 'sha256:ab60583d64eb9140'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# apply:

<sub>Instance Method</sub>

Produces a [CIImage](../ciimage.md) object by applying a kernel function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (CIImage *) apply:(CIKernel *) k;
```

## Parameters

- `k` — A [CIKernel](../cikernel.md) object that contains a kernel function.

## Discussion

If you are implementing a custom filter, this method needs to be called from within the [outputImage](outputimage.md) method in order to apply your kernel function to the [CIImage](../ciimage.md) object. For example, if the kernel function has this signature:

```objc
kernel vec4 brightenEffect (sampler src, float k)
```

You would supply two arguments after the `k` argument  to the `apply:k, ...` method. In this case, the first argument must be a sampler and the second a floating-point value. For more information on kernels, see [Core Image Kernel Language Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397).

## See Also

### Applying a filter

- [- apply:arguments:options:](<apply(__arguments_options_).md>) — Produces a [CIImage](../ciimage.md) object by applying arguments to a kernel function and using options to control how the kernel function is evaluated.
