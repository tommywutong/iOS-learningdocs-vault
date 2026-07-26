---
title: 'exportKey(_:from:withName:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifiltergenerator/exportkey(_:from:withname:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltergenerator/exportkey(_:from:withname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltergenerator/exportkey%28_%3Afrom%3Awithname%3A%29.json'
content_hash: 'sha256:ac40e7b13f6b6835'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilterGenerator](../cifiltergenerator.md)

# exportKey(_:from:withName:)

<sub>Instance Method</sub>

Exports an input or output key of an object in the filter chain.

<sub>macOS</sub>

```swift
func exportKey(_ key: String, from targetObject: Any, withName exportedKeyName: String?)
```

## Parameters

- `key` — The key to export from the target object (for example, `inputImage`).

- `targetObject` — The object associated with the key (for example, the filter).

- `exportedKeyName` — A unique name to use for the exported key. Pass `nil` to use the original key name.

## Discussion

When you create a [CIFilter](../cifilter-swift.class.md) object from a [CIFilterGenerator](../cifiltergenerator.md) object, you might want the filter client to be able to set some of the parameters associated with the filter chain. You can make a parameter settable by  exporting the key associated with the parameter. If the exported key represents an input parameter of the filter, the key is exported as an input key. If the key represents an output parameter, it is exported as an output key.

## See Also

### Managing Exported Keys

- [exportedKeys](exportedkeys.md) — Returns an array of the exported keys.
- [- removeExportedKey:](<removeexportedkey(__).md>) — Removes a key that was previously exported.
- [- setAttributes:forExportedKey:](<setattributes(__forexportedkey_).md>) — Sets a dictionary of attributes for an exported key.
