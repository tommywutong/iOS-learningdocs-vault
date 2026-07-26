---
title: offlineGPUCount()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicontext/offlinegpucount()
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/offlinegpucount()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/offlinegpucount%28%29.json'
content_hash: 'sha256:fbd04b470e887a2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# offlineGPUCount()

<sub>Type Method</sub>

Returns the number of GPUs not currently driving a display.

<sub>macOS</sub>

```swift
class func offlineGPUCount() -> UInt32
```

## Return Value

The number of offline GPU devices.

## Discussion

If this count is greater than zero, the system has attached GPU devices that are not currently driving a display. You can use these devices for Core Image rendering by creating a context with the [init(forOfflineGPUAtIndex:)](<init(forofflinegpuatindex_).md>) or[init(forOfflineGPUAtIndex:colorSpace:options:sharedContext:)](<init(forofflinegpuatindex_colorspace_options_sharedcontext_).md>) method.

## See Also

### Managing Resources

- [- clearCaches](<clearcaches().md>) — Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.
- [- reclaimResources](<reclaimresources().md>) — Runs the garbage collector to reclaim any resources that the context no longer requires.
- [workingColorSpace](workingcolorspace.md) — The working color space of the Core Image context.
- [workingFormat](workingformat.md) — The working pixel format of the Core Image context.
