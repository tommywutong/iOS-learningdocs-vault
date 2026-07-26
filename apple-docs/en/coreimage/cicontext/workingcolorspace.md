---
title: workingColorSpace
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicontext/workingcolorspace
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/workingcolorspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/workingcolorspace.json'
content_hash: 'sha256:1c8b84127f6e4931'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# workingColorSpace

<sub>Instance Property</sub>

The working color space of the Core Image context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var workingColorSpace: CGColorSpace? { get }
```

## Discussion

The working color space determines the color space used when executing filter kernels; Core Image automatically converts to and from the source and destination color spaces of input images and output contexts. You specify a working color space using the [kCIContextWorkingColorSpace](../cicontextoption/workingcolorspace.md) key in the `options` dictionary when creating a Core Image context.

## See Also

### Managing Resources

- [- clearCaches](<clearcaches().md>) — Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.
- [- reclaimResources](<reclaimresources().md>) — Runs the garbage collector to reclaim any resources that the context no longer requires.
- [+ offlineGPUCount](<offlinegpucount().md>) — Returns the number of GPUs not currently driving a display.
- [workingFormat](workingformat.md) — The working pixel format of the Core Image context.
