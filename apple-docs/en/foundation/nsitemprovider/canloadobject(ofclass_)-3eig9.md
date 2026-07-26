---
title: 'canLoadObject(ofClass:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/canloadobject(ofclass:)-3eig9'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/canloadobject(ofclass:)-3eig9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/canloadobject%28ofclass%3A%29-3eig9.json'
content_hash: 'sha256:2dfc8d4ad97a3e87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# canLoadObject(ofClass:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether an item provider can load objects of a specified class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func canLoadObject(ofClass aClass: any NSItemProviderReading.Type) -> Bool
```

## Parameters

- `aClass` — The object class for comparison.

## Return Value

`true` if the item provider can load objects of the class.

## See Also

### Querying the provider’s contents

- [canLoadObject(ofClass:)](<canloadobject(ofclass_)-40grc.md>) — Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [- hasItemConformingToTypeIdentifier:](<hasitemconformingtotypeidentifier(__).md>) — Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier file options parameter with a value of zero.
- [- hasRepresentationConformingToTypeIdentifier:fileOptions:](<hasrepresentationconforming(totypeidentifier_fileoptions_).md>) — Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier and to specified open-in-place behavior.
- [registeredTypeIdentifiers](registeredtypeidentifiers.md) — Returns the array of type identifiers for the item provider, in the same order they were registered.
- [- registeredTypeIdentifiersWithFileOptions:](<registeredtypeidentifiers(fileoptions_).md>) — Returns an array with a subset of type identifiers for the item provider, according to the specified file options, in the same order they were registered.
