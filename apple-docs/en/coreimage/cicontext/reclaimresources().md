---
title: reclaimResources()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicontext/reclaimresources()
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/reclaimresources()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/reclaimresources%28%29.json'
content_hash: 'sha256:7204de5f4e89b751'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# reclaimResources()

<sub>Instance Method</sub>

Runs the garbage collector to reclaim any resources that the context no longer requires.

<sub>macOS</sub>

```swift
func reclaimResources()
```

## Discussion

The system calls this method automatically after every rendering operation. You can use this method to remove textures from the texture cache that reference deleted images.

## See Also

### Managing Resources

- [- clearCaches](<clearcaches().md>) — Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.
- [+ offlineGPUCount](<offlinegpucount().md>) — Returns the number of GPUs not currently driving a display.
- [workingColorSpace](workingcolorspace.md) — The working color space of the Core Image context.
- [workingFormat](workingformat.md) — The working pixel format of the Core Image context.
