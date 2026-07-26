---
title: exportedKeys
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifiltergenerator/exportedkeys
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltergenerator/exportedkeys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltergenerator/exportedkeys.json'
content_hash: 'sha256:470cebcd733689b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilterGenerator](../cifiltergenerator.md)

# exportedKeys

<sub>Instance Property</sub>

Returns an array of the exported keys.

<sub>macOS</sub>

```swift
var exportedKeys: [AnyHashable : Any] { get }
```

## Return Value

An array of dictionaries that describe the exported key and target object. See [kCIFilterGeneratorExportedKey](../kcifiltergeneratorexportedkey.md), [kCIFilterGeneratorExportedKeyTargetObject](../kcifiltergeneratorexportedkeytargetobject.md),  and [kCIFilterGeneratorExportedKey](../kcifiltergeneratorexportedkey.md) for keys used in the dictionary.

## Discussion

This method returns the keys that you exported using the [- exportKey:fromObject:withName:](<exportkey(__from_withname_).md>) method or that were exported before being written to the file from which you read the filter chain.

## See Also

### Managing Exported Keys

- [- exportKey:fromObject:withName:](<exportkey(__from_withname_).md>) — Exports an input or output key of an object in the filter chain.
- [- removeExportedKey:](<removeexportedkey(__).md>) — Removes a key that was previously exported.
- [- setAttributes:forExportedKey:](<setattributes(__forexportedkey_).md>) — Sets a dictionary of attributes for an exported key.
