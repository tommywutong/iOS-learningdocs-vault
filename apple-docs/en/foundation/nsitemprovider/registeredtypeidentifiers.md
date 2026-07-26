---
title: registeredTypeIdentifiers
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemprovider/registeredtypeidentifiers
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registeredtypeidentifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registeredtypeidentifiers.json'
content_hash: 'sha256:340c29b3063e25a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registeredTypeIdentifiers

<sub>Instance Property</sub>

Returns the array of type identifiers for the item provider, in the same order they were registered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var registeredTypeIdentifiers: [String] { get }
```

## See Also

### Querying the provider’s contents

- [- canLoadObjectOfClass:](<canloadobject(ofclass_)-3eig9.md>) — Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [canLoadObject(ofClass:)](<canloadobject(ofclass_)-40grc.md>) — Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [- hasItemConformingToTypeIdentifier:](<hasitemconformingtotypeidentifier(__).md>) — Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier file options parameter with a value of zero.
- [- hasRepresentationConformingToTypeIdentifier:fileOptions:](<hasrepresentationconforming(totypeidentifier_fileoptions_).md>) — Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier and to specified open-in-place behavior.
- [- registeredTypeIdentifiersWithFileOptions:](<registeredtypeidentifiers(fileoptions_).md>) — Returns an array with a subset of type identifiers for the item provider, according to the specified file options, in the same order they were registered.
