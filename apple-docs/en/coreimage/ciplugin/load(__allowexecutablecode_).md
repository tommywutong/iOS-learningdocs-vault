---
title: 'load(_:allowExecutableCode:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.7+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/ciplugin/load(_:allowexecutablecode:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciplugin/load(_:allowexecutablecode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciplugin/load%28_%3Aallowexecutablecode%3A%29.json'
content_hash: 'sha256:75c4a71fa0c39937'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIPlugIn](../ciplugin.md)

# load(_:allowExecutableCode:)

<sub>Type Method</sub>

Loads filters from an image unit that have the appropriate executable status.

<sub>macOS</sub>

```swift
class func load(_ url: URL!, allowExecutableCode: Bool)
```

## Parameters

- `url` — The location of the image unit to load.

- `allowExecutableCode` — `true` to load all filters from the image unit, or `false` to load only those filters without CPU executable code.

## Discussion

You need to call this method only once to load a specific image unit. The behavior of this method is not defined for multiple calls for the same image unit. If you pass `false` for the `allowExecutableCode` parameter, Core Image will load only pure kernel filters that run entirely on the GPU, ignoring filters implemented using compiled Objective-C code.

## See Also

### Deprecated

- [+ loadAllPlugIns](<loadallplugins().md>) — Scans directories for files that have the `.plugin` extension and then loads the image units. _(deprecated)_
