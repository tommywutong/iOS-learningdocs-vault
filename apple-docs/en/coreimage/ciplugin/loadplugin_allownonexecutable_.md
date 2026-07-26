---
title: 'loadPlugIn:allowNonExecutable:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.4+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/ciplugin/loadplugin:allownonexecutable:'
source_url: 'https://developer.apple.com/documentation/coreimage/ciplugin/loadplugin:allownonexecutable:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciplugin/loadplugin%3Aallownonexecutable%3A.json'
content_hash: 'sha256:09fbb3158de0b693'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIPlugIn](../ciplugin.md)

# loadPlugIn:allowNonExecutable:

<sub>Type Method</sub>

Loads filters from an image unit that have the appropriate executable status.

> [!warning] Deprecated
> Instead use [+ loadPlugIn:allowExecutableCode:](<load(__allowexecutablecode_).md>).

<sub>macOS</sub>

```objc
+ (void) loadPlugIn:(NSURL *) url allowNonExecutable:(BOOL) allowNonExecutable;
```

## Parameters

- `url` — The location of the image unit to load.

- `allowNonExecutable` — `TRUE` to load only those filters that are marked by the image unit as non-executable filters.

## Discussion

You need to call this method only once to load a specific image unit. The behavior of this method is not defined for multiple calls for the same image unit.

## See Also

### Deprecated

- [+ loadAllPlugIns](<loadallplugins().md>) — Scans directories for files that have the `.plugin` extension and then loads the image units. _(deprecated)_
- [+ loadPlugIn:allowExecutableCode:](<load(__allowexecutablecode_).md>) — Loads filters from an image unit that have the appropriate executable status. _(deprecated)_
