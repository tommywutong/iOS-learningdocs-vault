---
title: workingFormat
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicontext/workingformat
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/workingformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/workingformat.json'
content_hash: 'sha256:cfec1c14bee47bf6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# workingFormat

<sub>Instance Property</sub>

The working pixel format of the Core Image context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var workingFormat: CIFormat { get }
```

## Discussion

The working format determines the pixel format that Core Image uses to create intermediate buffers for executing filter kernels. Core Image automatically converts to and from the source and destination pixel formats of input images and output  contexts. You specify a working pixel format using the [kCIContextWorkingFormat](../cicontextoption/workingformat.md) key in the `options` dictionary when creating a Core Image context.

## See Also

### Managing Resources

- [- clearCaches](<clearcaches().md>) — Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.
- [- reclaimResources](<reclaimresources().md>) — Runs the garbage collector to reclaim any resources that the context no longer requires.
- [+ offlineGPUCount](<offlinegpucount().md>) — Returns the number of GPUs not currently driving a display.
- [workingColorSpace](workingcolorspace.md) — The working color space of the Core Image context.
