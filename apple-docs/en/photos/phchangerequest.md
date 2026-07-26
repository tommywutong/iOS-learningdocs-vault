---
title: PHChangeRequest
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phchangerequest
source_url: 'https://developer.apple.com/documentation/photos/phchangerequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phchangerequest.json'
content_hash: 'sha256:f246ddd7debd7afb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHChangeRequest

<sub>Class</sub>

The abstract base class of the framework’s photo library change requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHChangeRequest
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [PHAssetChangeRequest](phassetchangerequest.md), [PHAssetCollectionChangeRequest](phassetcollectionchangerequest.md), [PHAssetResourceUploadJobChangeRequest](phassetresourceuploadjobchangerequest.md), [PHCollectionListChangeRequest](phcollectionlistchangerequest.md), [PHProjectChangeRequest](phprojectchangerequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

### Updating the Library

- [Requesting Changes to the Photo Library](../photokit/requesting-changes-to-the-photo-library.md) — Create, delete, or modify assets and collections in a photo library by making change requests.
- [- performChanges:completionHandler:](<phphotolibrary/performchanges(__completionhandler_).md>) — Asynchronously runs a block that requests changes to the photo library.
- [- performChangesAndWait:error:](<phphotolibrary/performchangesandwait(__).md>) — Synchronously runs a block that requests changes to be performed in the photo library.
- [PHAssetChangeRequest](phassetchangerequest.md) — A request to create, delete, change metadata for, or edit the content of a Photos asset, for use in a photo library change block.
- [PHAssetCollectionChangeRequest](phassetcollectionchangerequest.md) — A request to create, delete, or modify a Photos asset collection, for use in a photo library change block.
- [PHCollectionListChangeRequest](phcollectionlistchangerequest.md) — A request to create, delete, or modify a Photos collection list, for use in a photo library change block.
- [PHObjectPlaceholder](phobjectplaceholder.md) — A read-only proxy object that represents a Photos asset or collection to create.
