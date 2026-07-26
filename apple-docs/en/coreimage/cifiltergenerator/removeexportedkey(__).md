---
title: 'removeExportedKey(_:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifiltergenerator/removeexportedkey(_:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltergenerator/removeexportedkey(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltergenerator/removeexportedkey%28_%3A%29.json'
content_hash: 'sha256:b047a0deffc4f6fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilterGenerator](../cifiltergenerator.md)

# removeExportedKey(_:)

<sub>Instance Method</sub>

Removes a key that was previously exported.

<sub>macOS</sub>

```swift
func removeExportedKey(_ exportedKeyName: String)
```

## Parameters

- `exportedKeyName` — The name of the key you want to remove.

## See Also

### Managing Exported Keys

- [exportedKeys](exportedkeys.md) — Returns an array of the exported keys.
- [- exportKey:fromObject:withName:](<exportkey(__from_withname_).md>) — Exports an input or output key of an object in the filter chain.
- [- setAttributes:forExportedKey:](<setattributes(__forexportedkey_).md>) — Sets a dictionary of attributes for an exported key.
