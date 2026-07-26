---
title: NSFileProviderService
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfileproviderservice
source_url: 'https://developer.apple.com/documentation/foundation/nsfileproviderservice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileproviderservice.json'
content_hash: 'sha256:7e6f8a4428883675'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFileProviderService

<sub>Class</sub>

A service that provides a custom communication channel between your app and a File Provider extension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class NSFileProviderService
```

## Overview

To communicate, both your app and the File Provider extension must implement their part of the service:

- Your app requests the proxy object, and calls its methods.
- The File Provider extension declares the supported services and vends a proxy object that implements the protocol for each service.

The app and File Provider extension communicate using an XPC service. This service performs actions only on items managed by the File Provider extension. For more information, see [Creating XPC Services](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingXPCServices.html#//apple_ref/doc/uid/10000172i-SW6).

### Defining the Service’s Protocol

Services let you define custom actions that are not provided by Apple’s APIs. Both the app and the File Provider extension must agree upon the service’s name and protocol.  Communicate the name and protocol through an outside source (for example, posting a header file that defines both the name and protocol, or publishing a library that includes them both).

The service can be defined by either the app or the File Provider extension:

- Apps can define a service for features they would like to use. File providers can then choose to support those features by implementing the service.
- File Provider extensions can provide a service for the features they support. Apps can then choose to use the specified service.

When defining a service’s protocol, the parameters for each method must adhere to the following rules:

- The parameter’s class must conform to [NSSecureCoding](nssecurecoding.md).
- The parameter’s class must be defined in both the app and the File Provider extension (for example, standard system types or classes defined in a library imported by both sides).
- If a collection parameter contains types other than property list types (see [Property List Types and Objects](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44-SW2)), declare the valid types using the [NSXPCInterface](nsxpcinterface.md) class’s [- classesForSelector:argumentIndex:ofReply:](<nsxpcinterface/classes(for_argumentindex_ofreply_).md>) method.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing the Service

- [name](nsfileproviderservice/name.md) — The File Provider service’s name.
- [- getFileProviderConnectionWithCompletionHandler:](<nsfileproviderservice/getfileproviderconnection(completionhandler_).md>) — Asynchronously returns the service’s connection object.

## See Also

### Accessing file provider services

- [- getFileProviderServicesForItemAtURL:completionHandler:](<filemanager/getfileproviderservicesforitem(at_completionhandler_).md>) — Returns the services provided by the File Provider extension that manages the item at the given URL.
- [NSFileProviderServiceName](nsfileproviderservicename.md) — The name used to identify a File Provider service.
