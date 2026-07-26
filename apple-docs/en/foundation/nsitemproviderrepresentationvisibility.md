---
title: NSItemProviderRepresentationVisibility
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemproviderrepresentationvisibility
source_url: 'https://developer.apple.com/documentation/foundation/nsitemproviderrepresentationvisibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemproviderrepresentationvisibility.json'
content_hash: 'sha256:ae3fd47242b723f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSItemProviderRepresentationVisibility

<sub>Enumeration</sub>

Specifications that control which categories of processes can see an item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NSItemProviderRepresentationVisibility
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [NSItemProviderRepresentationVisibilityAll](nsitemproviderrepresentationvisibility/all.md) — A representation visibility specification conferring item visibility to all processes.
- [NSItemProviderRepresentationVisibilityGroup](nsitemproviderrepresentationvisibility/group.md) — A representation visibility specification confining item visibility to the app’s app group.
- [NSItemProviderRepresentationVisibilityOwnProcess](nsitemproviderrepresentationvisibility/ownprocess.md) — A representation visibility specification confining item visibility to the app that is the source of the item.
- [NSItemProviderRepresentationVisibilityTeam](nsitemproviderrepresentationvisibility/team.md) — A representation visibility specification confining item visibility to processes created by the app’s development team.

### Initializers

- [init(rawValue:)](<nsitemproviderrepresentationvisibility/init(rawvalue_).md>)

## See Also

### Constants

- [CompletionHandler](nsitemprovider/completionhandler.md) — A block that receives the item provider’s data.
- [LoadHandler](nsitemprovider/loadhandler.md) — A block that loads the item provider’s data and coerces it to the specified type.
- [Options Dictionary Key](options-dictionary-key.md) — Keys indicating options to use when generating the item provider’s data.
- [Keys for Items Accessed in JavaScript Code](keys-for-items-accessed-in-javascript-code.md) — Keys in property list items that the system recieves from or sends to JavaScript code.
- [NSItemProviderErrorDomain](nsitemprovider/errordomain.md) — The error domain associated with the item provider.
- [NSItemProviderFileOptions](nsitemproviderfileoptions.md) — Data-access specifications that declare how to handle items.
- [NSItemProviderReading](nsitemproviderreading.md) — The protocol for implementing a class to allow an item provider to create an instance of the class.
- [NSItemProviderWriting](nsitemproviderwriting.md) — The protocol for implementing a class to allow an item provider to retrieve data from an instance of the class.
- [ErrorCode](nsitemprovider/errorcode.md) — The error codes that describe problems with consuming data from an item provider.
