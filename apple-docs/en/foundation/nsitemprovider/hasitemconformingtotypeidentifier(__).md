---
title: 'hasItemConformingToTypeIdentifier(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/hasitemconformingtotypeidentifier(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/hasitemconformingtotypeidentifier(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/hasitemconformingtotypeidentifier%28_%3A%29.json'
content_hash: 'sha256:dbdf198ac107395d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# hasItemConformingToTypeIdentifier(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier file options parameter with a value of zero.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hasItemConformingToTypeIdentifier(_ typeIdentifier: String) -> Bool
```

## Parameters

- `typeIdentifier` — A string that represents the desired UTI.

## See Also

### Querying the provider’s contents

- [- canLoadObjectOfClass:](<canloadobject(ofclass_)-3eig9.md>) — Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [canLoadObject(ofClass:)](<canloadobject(ofclass_)-40grc.md>) — Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [- hasRepresentationConformingToTypeIdentifier:fileOptions:](<hasrepresentationconforming(totypeidentifier_fileoptions_).md>) — Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier and to specified open-in-place behavior.
- [registeredTypeIdentifiers](registeredtypeidentifiers.md) — Returns the array of type identifiers for the item provider, in the same order they were registered.
- [- registeredTypeIdentifiersWithFileOptions:](<registeredtypeidentifiers(fileoptions_).md>) — Returns an array with a subset of type identifiers for the item provider, according to the specified file options, in the same order they were registered.
