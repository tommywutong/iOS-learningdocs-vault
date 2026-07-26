---
title: CIFilterGenerator
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifiltergenerator
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltergenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltergenerator.json'
content_hash: 'sha256:5f077d9331209450'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIFilterGenerator

<sub>Class</sub>

An object that creates and configures chains of individual image filters.

<sub>macOS</sub>

```swift
class CIFilterGenerator
```

## Overview

The `CIFilterGenerator` class provides methods for creating a [CIFilter](cifilter-swift.class.md) object by chaining together existing `CIFilter` objects to create complex effects. (A **filter chain** refers to the `CIFilter` objects that are connected in the `CIFilterGenerator` object.) The complex effect can be encapsulated as a [CIFilterGenerator](cifiltergenerator.md) object and saved as a file so that it can be used again. The **filter generator file** contains an archived instance  of all the `CIFilter` objects that are chained together.

Any filter generator files that you copy to `/Library/Graphics/Image Units/` are loaded when any of the loading methods provided by the [CIPlugIn](ciplugin.md) class are invoked. A `CIFilterGenerator` object is registered by its filename or, if present, by a class attribute that you supply in its description.

You can create a  `CIFilterGenerator` object  programmatically, using the methods provided by the `CIFilterGenerator` class, or by using the editor view provided by Core Image.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CIFilterConstructor](cifilterconstructor.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Initializing a Filter Generator Object

- [- initWithContentsOfURL:](<cifiltergenerator/init(contentsof_).md>) — Initializes a filter generator object with the contents of a filter generator file.

### Connecting and Disconnecting Objects

- [- connectObject:withKey:toObject:withKey:](<cifiltergenerator/connect(__withkey_to_withkey_).md>) — Adds an object to the filter chain.
- [- disconnectObject:withKey:toObject:withKey:](<cifiltergenerator/disconnectobject(__withkey_to_withkey_).md>) — Removes the connection between two objects in the filter chain.

### Managing Exported Keys

- [exportedKeys](cifiltergenerator/exportedkeys.md) — Returns an array of the exported keys.
- [- exportKey:fromObject:withName:](<cifiltergenerator/exportkey(__from_withname_).md>) — Exports an input or output key of an object in the filter chain.
- [- removeExportedKey:](<cifiltergenerator/removeexportedkey(__).md>) — Removes a key that was previously exported.
- [- setAttributes:forExportedKey:](<cifiltergenerator/setattributes(__forexportedkey_).md>) — Sets a dictionary of attributes for an exported key.

### Setting and Getting Class Attributes

- [classAttributes](cifiltergenerator/classattributes.md) — The class attributes associated with the filter.

### Archiving a Filter Generator Object

- [- writeToURL:atomically:](<cifiltergenerator/write(to_atomically_).md>) — Archives a filter generator object to a filter generator file.

### Registering a Filter Chain

- [- registerFilterName:](<cifiltergenerator/registerfiltername(__).md>) — Registers the name associated with a filter chain.

### Creating a Filter from a Filter Chain

- [- filter](<cifiltergenerator/filter().md>) — Creates a filter object based on the filter chain.

### Constants

- [Exported Keys](exported-keys.md) — Keys for the exported parameters of a filter generator object.

### Initializers

- [init(coder:)](<cifiltergenerator/init(coder_).md>)
- [init(contentsOfURL:)](<cifiltergenerator/init(contentsofurl_)-4nqjf.md>)
- [init(contentsOfURL:)](<cifiltergenerator/init(contentsofurl_)-8q8ic.md>)

## See Also

### Image Units

- [CIPlugIn](ciplugin.md) — The mechanism for loading image units in macOS.
- [CIPlugInRegistration](cipluginregistration.md) — The interface for loading Core Image image units.
- [CIFilterConstructor](cifilterconstructor.md) — A general interface for objects that produce filters.
