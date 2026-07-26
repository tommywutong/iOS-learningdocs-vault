---
title: 'registeredTypeIdentifiers(fileOptions:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/registeredtypeidentifiers(fileoptions:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registeredtypeidentifiers(fileoptions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registeredtypeidentifiers%28fileoptions%3A%29.json'
content_hash: 'sha256:7d78407e0e58366f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registeredTypeIdentifiers(fileOptions:)

<sub>Instance Method</sub>

Returns an array with a subset of type identifiers for the item provider, according to the specified file options, in the same order they were registered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func registeredTypeIdentifiers(fileOptions: NSItemProviderFileOptions = []) -> [String]
```

## Parameters

- `fileOptions` — An array of [NSItemProviderFileOptions](../nsitemproviderfileoptions.md).

## Return Value

An array of type identifier strings.

## Discussion

To access the array of all registered UTIs, pass the value `0` in the `fileOptions` parameter.

## See Also

### Querying the provider’s contents

- [- canLoadObjectOfClass:](<canloadobject(ofclass_)-3eig9.md>) — Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [canLoadObject(ofClass:)](<canloadobject(ofclass_)-40grc.md>) — Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [- hasItemConformingToTypeIdentifier:](<hasitemconformingtotypeidentifier(__).md>) — Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier file options parameter with a value of zero.
- [- hasRepresentationConformingToTypeIdentifier:fileOptions:](<hasrepresentationconforming(totypeidentifier_fileoptions_).md>) — Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier and to specified open-in-place behavior.
- [registeredTypeIdentifiers](registeredtypeidentifiers.md) — Returns the array of type identifiers for the item provider, in the same order they were registered.
