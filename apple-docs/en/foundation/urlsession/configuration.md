---
title: configuration
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession/configuration
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/configuration.json'
content_hash: 'sha256:ac202fab830bcc9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# configuration

<sub>Instance Property</sub>

A copy of the configuration object for this session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var configuration: URLSessionConfiguration { get }
```

## Discussion

Beginning in iOS 9 and OS X 10.11, [URLSession](../urlsession.md) objects store a copy of the [URLSessionConfiguration](../urlsessionconfiguration.md) object passed to their initializers, such that a session’s configuration is immutable after initialization. Any further changes to mutable properties on the configuration object passed to a session’s initializer or the value returned from a session’s configuration property do not affect the behavior of that session. However, you can create a new session with the modified configuration object.

> [!note] Note
> On previous versions of iOS and macOS, a bug in the implementation causes [URLSession](../urlsession.md) objects to store a _reference_ to configuration objects passed to their initializers rather than a copy. This allows the behavior of a session to be further configured after initialization by modifying the configuration object passed to a session’s initializer or the value returned from a session’s [configuration](configuration.md) property. You can ensure consistent behavior across different platform versions by explicitly calling [copy()](<../../objectivec/nsobject-swift.class/copy().md>) on configuration objects passed to a [URLSession](../urlsession.md) initializer or returned from the [configuration](configuration.md) property.

## See Also

### Creating a session

- [+ sessionWithConfiguration:](<init(configuration_).md>) — Creates a session with the specified session configuration.
- [+ sessionWithConfiguration:delegate:delegateQueue:](<init(configuration_delegate_delegatequeue_).md>) — Creates a session with the specified session configuration, delegate, and operation queue.
- [URLSessionConfiguration](../urlsessionconfiguration.md) — A configuration object that defines behavior and policies for a URL session.
