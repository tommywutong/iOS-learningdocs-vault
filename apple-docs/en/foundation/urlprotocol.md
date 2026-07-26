---
title: URLProtocol
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlprotocol
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocol.json'
content_hash: 'sha256:e76ef4eb60939a22'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLProtocol

<sub>Class</sub>

An abstract class that handles the loading of protocol-specific URL data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class URLProtocol
```

## Overview

Don’t instantiate a [URLProtocol](urlprotocol.md) subclass directly. Instead, create subclasses for any custom protocols or URL schemes that your app supports. When a download starts, the system creates the appropriate protocol object to handle the corresponding URL request. You define your protocol class and call the [+ registerClass:](<urlprotocol/registerclass(__).md>) class method during your app’s launch time so that the system is aware of your protocol.

> [!note] Note
> You cannot use this class to define custom URL schemes and protocols in watchOS 2 and later.

To support the customization of protocol-specific requests, create extensions to the [URLRequest](urlrequest.md) class to provide any custom API that you need. You can store and retrieve protocol-specific request data by using [URLProtocol](urlprotocol.md)’s class methods [+ propertyForKey:inRequest:](<urlprotocol/property(forkey_in_).md>) and [+ setProperty:forKey:inRequest:](<urlprotocol/setproperty(__forkey_in_).md>).

Create a [URLResponse](urlresponse.md) for each request your subclass processes successfully. You may want to create a custom [URLResponse](urlresponse.md) class to provide protocol specific information.

### Subclassing notes

When overriding methods of this class, be aware that methods that take a `task` parameter are preferred by the system to those that do not. Therefore, you should override the task-based methods when subclassing, as follows:

Swift:

- Initialization — Override [- initWithTask:cachedResponse:client:](<urlprotocol/init(task_cachedresponse_client_).md>) instead of or in addition to [- initWithRequest:cachedResponse:client:](<urlprotocol/init(request_cachedresponse_client_).md>). Also override the task-based [+ canInitWithTask:](<urlprotocol/caninit(with_)-18gbo.md>) instead of or in addition to the request-based [+ canInitWithRequest:](<urlprotocol/caninit(with_)-76brg.md>).

Objective-C:

- Initialization — Override [+ canInitWithTask:](<urlprotocol/caninit(with_)-18gbo.md>) and [- initWithTask:cachedResponse:client:](<urlprotocol/init(task_cachedresponse_client_).md>) instead of or in addition to [+ canInitWithRequest:](<urlprotocol/caninit(with_)-76brg.md>) and [- initWithRequest:cachedResponse:client:](<urlprotocol/init(request_cachedresponse_client_).md>).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating protocol objects

- [- initWithRequest:cachedResponse:client:](<urlprotocol/init(request_cachedresponse_client_).md>) — Creates a URL protocol instance to handle the request.
- [- initWithTask:cachedResponse:client:](<urlprotocol/init(task_cachedresponse_client_).md>) — Creates a URL protocol instance to handle the task.

### Registering and unregistering protocol classes

- [+ registerClass:](<urlprotocol/registerclass(__).md>) — Attempts to register a subclass of [URLProtocol](urlprotocol.md), making it visible to the URL loading system.
- [+ unregisterClass:](<urlprotocol/unregisterclass(__).md>) — Unregisters the specified subclass of [URLProtocol](urlprotocol.md).

### Determining If a subclass can handle a request

- [+ canInitWithRequest:](<urlprotocol/caninit(with_)-76brg.md>) — Determines whether the protocol subclass can handle the specified request.
- [+ canInitWithTask:](<urlprotocol/caninit(with_)-18gbo.md>) — Determines whether the protocol subclass can handle the specified task.

### Getting and setting request properties

- [+ propertyForKey:inRequest:](<urlprotocol/property(forkey_in_).md>) — Fetches the property associated with the specified key in the specified request.
- [+ setProperty:forKey:inRequest:](<urlprotocol/setproperty(__forkey_in_).md>) — Sets the property associated with the specified key in the specified request.
- [+ removePropertyForKey:inRequest:](<urlprotocol/removeproperty(forkey_in_).md>) — Removes the property associated with the specified key in the specified request.

### Providing a canonical version of a request

- [+ canonicalRequestForRequest:](<urlprotocol/canonicalrequest(for_).md>) — Returns a canonical version of the specified request.

### Determining if requests are cache equivalent

- [+ requestIsCacheEquivalent:toRequest:](<urlprotocol/requestiscacheequivalent(__to_).md>) — A Boolean value indicating whether two requests are equivalent for cache purposes.

### Starting and stopping downloads

- [- startLoading](<urlprotocol/startloading().md>) — Starts protocol-specific loading of the request.
- [- stopLoading](<urlprotocol/stoploading().md>) — Stops protocol-specific loading of the request.

### Getting protocol attributes

- [cachedResponse](urlprotocol/cachedresponse.md) — The protocol’s cached response.
- [client](urlprotocol/client.md) — The object the protocol uses to communicate with the URL loading system.
- [URLProtocolClient](urlprotocolclient.md) — The interface used by [URLProtocol](urlprotocol.md) subclasses to communicate with the URL Loading System.
- [request](urlprotocol/request.md) — The protocol’s request.
- [task](urlprotocol/task.md) — The protocol’s task.

## See Also

### Supporting custom protocols

- [protocolClasses](urlsessionconfiguration/protocolclasses.md) — An array of extra protocol subclasses that handle requests in a session.
