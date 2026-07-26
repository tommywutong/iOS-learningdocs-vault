---
title: 'loadNonExecutablePlugIn(_:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciplugin/loadnonexecutableplugin(_:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciplugin/loadnonexecutableplugin(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciplugin/loadnonexecutableplugin%28_%3A%29.json'
content_hash: 'sha256:4bcae94deace451b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIPlugIn](../ciplugin.md)

# loadNonExecutablePlugIn(_:)

<sub>Type Method</sub>

Loads a non-executable plug-in specified by its URL.

<sub>macOS</sub>

```swift
class func loadNonExecutablePlugIn(_ url: URL!)
```

## Parameters

- `url` — The location of the plugin to load.

## Discussion

If the filters contain executable code the plugin isn’t loaded.

## See Also

### Loading Plug-ins

- [+ loadNonExecutablePlugIns](<loadnonexecutableplugins().md>) — Scans directories for plugins.
