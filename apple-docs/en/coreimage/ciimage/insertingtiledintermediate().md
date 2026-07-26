---
title: insertingTiledIntermediate()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimage/insertingtiledintermediate()
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/insertingtiledintermediate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/insertingtiledintermediate%28%29.json'
content_hash: 'sha256:0463e9a155b7a547'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# insertingTiledIntermediate()

<sub>Instance Method</sub>

Create an image that inserts a intermediate that is cached in tiles

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func insertingTiledIntermediate() -> CIImage
```

## Return Value

An autoreleased [CIImage](../ciimage.md).

## Discussion

This intermediate will be cacheable even if [kCIContextCacheIntermediates](../cicontextoption/cacheintermediates.md) is false.
