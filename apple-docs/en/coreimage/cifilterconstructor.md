---
title: CIFilterConstructor
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilterconstructor
source_url: 'https://developer.apple.com/documentation/coreimage/cifilterconstructor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilterconstructor.json'
content_hash: 'sha256:46ddbd17548edcbb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIFilterConstructor

<sub>Protocol</sub>

A general interface for objects that produce filters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIFilterConstructor
```

## Overview

Objects implementing this protocol are called _filter constructors_—they produce new instances of [CIFilter](cifilter-swift.class.md) subclasses when filters are requested by name. You can create a filter constructor to provide new, custom filters that other Core Image clients can discover using the `CIFilter` class. Normally, you create and register custom filters by packaging them as Image Units (see [Packaging and Loading Image Units](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_image_units/ci_image_units.html#//apple_ref/doc/uid/TP30001185-CH7)), but you can use this protocol to provide new filters within your app that are compositions of existing filters.

To provide custom filters using this protocol, you must:

1. Create your custom filters as `CIFilter` subclasses.
2. Create a class that implements this protocol to vend instances of the appropriate `CIFilter` subclasses when requested.
3. Call the `CIFilter` class method [+ registerFilterName:constructor:classAttributes:](<cifilter-swift.class/registername(__constructor_classattributes_).md>) for each custom filter, providing the filter’s name, an instance of your filter constructor class, and information about the filter’s attributes.

## Relationships

- **Conforming Types**: [CIFilterGenerator](cifiltergenerator.md)

## Topics

### Providing Filter Objects

- [- filterWithName:](<cifilterconstructor/filter(withname_).md>) — Returns a filter object specified by name.

## See Also

### Image Units

- [CIPlugIn](ciplugin.md) — The mechanism for loading image units in macOS.
- [CIFilterGenerator](cifiltergenerator.md) — An object that creates and configures chains of individual image filters.
- [CIPlugInRegistration](cipluginregistration.md) — The interface for loading Core Image image units.
