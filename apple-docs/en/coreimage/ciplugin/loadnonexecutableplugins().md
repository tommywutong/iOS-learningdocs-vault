---
title: loadNonExecutablePlugIns()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciplugin/loadnonexecutableplugins()
source_url: 'https://developer.apple.com/documentation/coreimage/ciplugin/loadnonexecutableplugins()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciplugin/loadnonexecutableplugins%28%29.json'
content_hash: 'sha256:69a7d95ffd5c2434'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIPlugIn](../ciplugin.md)

# loadNonExecutablePlugIns()

<sub>Type Method</sub>

Scans directories for plugins.

<sub>macOS</sub>

```swift
class func loadNonExecutablePlugIns()
```

## Discussion

This call scans for plugins with the extension `.plugin` in the following directories:

- /Library/Graphics/Image Units
- ~Library/Graphics/Image Units

This call adds new plug-ins. It doesn’t remove any plug-ins.

## See Also

### Loading Plug-ins

- [+ loadNonExecutablePlugIn:](<loadnonexecutableplugin(__).md>) — Loads a non-executable plug-in specified by its URL.
