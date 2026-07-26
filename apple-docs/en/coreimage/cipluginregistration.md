---
title: CIPlugInRegistration
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cipluginregistration
source_url: 'https://developer.apple.com/documentation/coreimage/cipluginregistration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cipluginregistration.json'
content_hash: 'sha256:a49332d982368b03'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIPlugInRegistration

<sub>Protocol</sub>

The interface for loading Core Image image units.

<sub>macOS</sub>

```swift
protocol CIPlugInRegistration
```

## Overview

The principal class of an image unit—a loadable bundle containing custom Core Image filters for macOS—must support this protocol.

## Topics

### Initializing Plug-ins

- [- load:](<cipluginregistration/load(__).md>) — Loads and initializes an image unit, performing custom tasks as needed.

## See Also

### Image Units

- [CIPlugIn](ciplugin.md) — The mechanism for loading image units in macOS.
- [CIFilterGenerator](cifiltergenerator.md) — An object that creates and configures chains of individual image filters.
- [CIFilterConstructor](cifilterconstructor.md) — A general interface for objects that produce filters.
