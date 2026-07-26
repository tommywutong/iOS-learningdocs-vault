---
title: 'setAttributes(_:forExportedKey:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifiltergenerator/setattributes(_:forexportedkey:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltergenerator/setattributes(_:forexportedkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltergenerator/setattributes%28_%3Aforexportedkey%3A%29.json'
content_hash: 'sha256:d4f24b02a7c7ae66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilterGenerator](../cifiltergenerator.md)

# setAttributes(_:forExportedKey:)

<sub>Instance Method</sub>

Sets a dictionary of attributes for an exported key.

<sub>macOS</sub>

```swift
func setAttributes(_ attributes: [AnyHashable : Any], forExportedKey key: String)
```

## Parameters

- `attributes` — A dictionary that describes the attributes associated with the specified key.

- `key` — The exported key whose attributes you want to set.

## Discussion

By default, the exported key inherits the attributes from its original key and target object. You can use this method to change one or more of the existing attributes for the key, such as the default value or maximum value. For more information on attributes, see [CIFilter](../cifilter-swift.class.md) and [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185).

## See Also

### Managing Exported Keys

- [exportedKeys](exportedkeys.md) — Returns an array of the exported keys.
- [- exportKey:fromObject:withName:](<exportkey(__from_withname_).md>) — Exports an input or output key of an object in the filter chain.
- [- removeExportedKey:](<removeexportedkey(__).md>) — Removes a key that was previously exported.
