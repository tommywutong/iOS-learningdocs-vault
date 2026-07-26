---
title: NSFileProviderServiceName
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfileproviderservicename
source_url: 'https://developer.apple.com/documentation/foundation/nsfileproviderservicename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileproviderservicename.json'
content_hash: 'sha256:9dff905e5b7263c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFileProviderServiceName

<sub>Structure</sub>

The name used to identify a File Provider service.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSFileProviderServiceName
```

## Discussion

The team providing the protocol also defines the name. To create a new service’s name:

- Use reverse domain name notation for the interfaces name (for example, `com.example.MyInterface`).
- (Optional) Incorporate versioning by appending a version number to the end of the name (`com.example.MyInterface.v2`).

For more information on defining a service’s protocol, see [Defining the Service’s Protocol](nsfileproviderservice.md#Defining-the-Services-Protocol).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<nsfileproviderservicename/init(__).md>) — Instantiates a new service name from the provided string.
- [init(rawValue:)](<nsfileproviderservicename/init(rawvalue_).md>) — Instantiates a new service name from the provided string.

## See Also

### Accessing file provider services

- [- getFileProviderServicesForItemAtURL:completionHandler:](<filemanager/getfileproviderservicesforitem(at_completionhandler_).md>) — Returns the services provided by the File Provider extension that manages the item at the given URL.
- [NSFileProviderService](nsfileproviderservice.md) — A service that provides a custom communication channel between your app and a File Provider extension.
