---
title: loadAllPlugIns()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.4+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coreimage/ciplugin/loadallplugins()
source_url: 'https://developer.apple.com/documentation/coreimage/ciplugin/loadallplugins()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciplugin/loadallplugins%28%29.json'
content_hash: 'sha256:bf4c9d29d51bdb94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIPlugIn](../ciplugin.md)

# loadAllPlugIns()

<sub>Type Method</sub>

Scans directories for files that have the `.plugin` extension and then loads the image units.

<sub>macOS</sub>

```swift
class func loadAllPlugIns()
```

## Discussion

This method scans the following directories:

- `/Library/Graphics/Image Units`
- ~`/Library/Graphics/Image Units`

Call this method once. If you call this method more than once, Core Image loads newly added image units, but image units (and the filters they contain) that are already loaded are not removed.

## See Also

### Related Documentation

- [Image Unit Tutorial](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageUnitTutorial/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004531)
- [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)

### Deprecated

- [+ loadPlugIn:allowExecutableCode:](<load(__allowexecutablecode_).md>) — Loads filters from an image unit that have the appropriate executable status. _(deprecated)_
