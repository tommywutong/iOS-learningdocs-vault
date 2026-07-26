---
title: 'hasRepresentationConforming(toTypeIdentifier:fileOptions:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/hasrepresentationconforming(totypeidentifier:fileoptions:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/hasrepresentationconforming(totypeidentifier:fileoptions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/hasrepresentationconforming%28totypeidentifier%3Afileoptions%3A%29.json'
content_hash: 'sha256:4086cecab93f9b2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# hasRepresentationConforming(toTypeIdentifier:fileOptions:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier and to specified open-in-place behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hasRepresentationConforming(toTypeIdentifier typeIdentifier: String, fileOptions: NSItemProviderFileOptions = []) -> Bool
```

## Discussion

To check all registered UTIs for type conformance, pass the value `0` in the `fileOptions` parameter.

## See Also

### Querying the provider’s contents

- [- canLoadObjectOfClass:](<canloadobject(ofclass_)-3eig9.md>) — Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [canLoadObject(ofClass:)](<canloadobject(ofclass_)-40grc.md>) — Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [- hasItemConformingToTypeIdentifier:](<hasitemconformingtotypeidentifier(__).md>) — Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier file options parameter with a value of zero.
- [registeredTypeIdentifiers](registeredtypeidentifiers.md) — Returns the array of type identifiers for the item provider, in the same order they were registered.
- [- registeredTypeIdentifiersWithFileOptions:](<registeredtypeidentifiers(fileoptions_).md>) — Returns an array with a subset of type identifiers for the item provider, according to the specified file options, in the same order they were registered.
