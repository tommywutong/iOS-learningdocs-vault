---
title: clearCaches()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicontext/clearcaches()
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/clearcaches()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/clearcaches%28%29.json'
content_hash: 'sha256:6af5580402569a88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# clearCaches()

<sub>Instance Method</sub>

Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func clearCaches()
```

## Discussion

You can use this method to remove textures from the texture cache that reference deleted images.

## See Also

### Managing Resources

- [- reclaimResources](<reclaimresources().md>) — Runs the garbage collector to reclaim any resources that the context no longer requires.
- [+ offlineGPUCount](<offlinegpucount().md>) — Returns the number of GPUs not currently driving a display.
- [workingColorSpace](workingcolorspace.md) — The working color space of the Core Image context.
- [workingFormat](workingformat.md) — The working pixel format of the Core Image context.
