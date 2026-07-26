---
title: CIPlugIn
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciplugin
source_url: 'https://developer.apple.com/documentation/coreimage/ciplugin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciplugin.json'
content_hash: 'sha256:7250532271a1d4b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIPlugIn

<sub>Class</sub>

The mechanism for loading image units in macOS.

<sub>macOS</sub>

```swift
class CIPlugIn
```

## Overview

An image unit is an image processing bundle that contains one or more Core Image filters. Th`e.plugin` extension indicates one or more filters packaged as an image unit.

> [!note] Note
> Starting in macOS 10.15, loading executable CIFilter plugins is deprecated.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Loading Plug-ins

- [+ loadNonExecutablePlugIns](<ciplugin/loadnonexecutableplugins().md>) — Scans directories for plugins.
- [+ loadNonExecutablePlugIn:](<ciplugin/loadnonexecutableplugin(__).md>) — Loads a non-executable plug-in specified by its URL.

### Deprecated

- [+ loadAllPlugIns](<ciplugin/loadallplugins().md>) — Scans directories for files that have the `.plugin` extension and then loads the image units. _(deprecated)_
- [+ loadPlugIn:allowExecutableCode:](<ciplugin/load(__allowexecutablecode_).md>) — Loads filters from an image unit that have the appropriate executable status. _(deprecated)_

## See Also

### Image Units

- [CIFilterGenerator](cifiltergenerator.md) — An object that creates and configures chains of individual image filters.
- [CIPlugInRegistration](cipluginregistration.md) — The interface for loading Core Image image units.
- [CIFilterConstructor](cifilterconstructor.md) — A general interface for objects that produce filters.
