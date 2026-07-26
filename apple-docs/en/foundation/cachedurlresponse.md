---
title: CachedURLResponse
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/cachedurlresponse
source_url: 'https://developer.apple.com/documentation/foundation/cachedurlresponse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/cachedurlresponse.json'
content_hash: 'sha256:1977e18e9f71af0c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# CachedURLResponse

<sub>Class</sub>

A cached response to a URL request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CachedURLResponse
```

## Overview

A [CachedURLResponse](cachedurlresponse.md) object provides the server’s response metadata in the form of a [URLResponse](urlresponse.md) object, along with an [NSData](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) object containing the actual cached content data. Its storage policy determines whether the response should be cached on disk, in memory, or not at all.

Cached responses also contain a user info dictionary where you can store app-specific information about the cached item.

The [URLCache](urlcache.md) class stores and retrieves instances of [CachedURLResponse](cachedurlresponse.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a cached URL response

- [- initWithResponse:data:](<cachedurlresponse/init(response_data_).md>) — Creates a cached URL response instance.
- [- initWithResponse:data:userInfo:storagePolicy:](<cachedurlresponse/init(response_data_userinfo_storagepolicy_).md>) — Creates a cached URL response with a given server response, data, user-info dictionary, and storage policy.

### Getting cached URL response properties

- [data](cachedurlresponse/data.md) — The cached response’s data.
- [response](cachedurlresponse/response.md) — The URL response object associated with the instance.
- [storagePolicy](cachedurlresponse/storagepolicy.md) — The cached response’s storage policy.
- [userInfo](cachedurlresponse/userinfo.md) — The cached response’s user info dictionary.

### Setting cache storage policies

- [StoragePolicy](urlcache/storagepolicy.md) — These constants specify the caching strategy used by an [CachedURLResponse](cachedurlresponse.md) object.

### Initializers

- [init(coder:)](<cachedurlresponse/init(coder_).md>)

## See Also

### Cache behavior

- [Accessing cached data](accessing-cached-data.md) — Control how URL requests make use of previously cached data.
- [URLCache](urlcache.md) — An object that maps URL requests to cached response objects.
