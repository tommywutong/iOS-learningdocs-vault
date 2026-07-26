---
title: URLCache
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcache
source_url: 'https://developer.apple.com/documentation/foundation/urlcache'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcache.json'
content_hash: 'sha256:986da9471862042d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLCache

<sub>Class</sub>

An object that maps URL requests to cached response objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class URLCache
```

## Overview

The [URLCache](urlcache.md) class implements the caching of responses to URL load requests, by mapping [NSURLRequest](nsurlrequest.md) objects to [CachedURLResponse](cachedurlresponse.md) objects. It provides a composite in-memory and on-disk cache, and lets you manipulate the sizes of both the in-memory and on-disk portions. You can also control the path where cache data is persistently stored.

> [!note] Note
> In iOS, the on-disk cache may be purged when the system runs low on disk space, but only when your app is not running.

### Thread safety

In iOS 8 and later, and macOS 10.10 and later, [URLCache](urlcache.md) is thread safe.

Although [URLCache](urlcache.md) instance methods can safely be called from multiple execution contexts at the same time, be aware that methods like  [- cachedResponseForRequest:](<urlcache/cachedresponse(for_).md>) and [- storeCachedResponse:forRequest:](<urlcache/storecachedresponse(__for_)-7p7bl.md>) have an unavoidable race condition when attempting to read or write responses for the same request.

Subclasses of [URLCache](urlcache.md) must implement overridden methods in such a thread-safe manner.

### Subclassing notes

The [URLCache](urlcache.md) class is meant to be used as-is, but you can subclass it when you have specific needs. For example, you might want to screen which responses are cached, or reimplement the storage mechanism for security or other reasons.

When overriding methods of this class, be aware that methods that take a `task` parameter are preferred by the system to those that do not. Therefore, you should override the task-based methods when subclassing, as follows:

- Storing responses in the cache — Override the task-based [- storeCachedResponse:forDataTask:](<urlcache/storecachedresponse(__for_)-8uq91.md>), instead of or in addition to the request-based [- storeCachedResponse:forRequest:](<urlcache/storecachedresponse(__for_)-7p7bl.md>).
- Getting responses from the cache — Override [- getCachedResponseForDataTask:completionHandler:](<urlcache/getcachedresponse(for_completionhandler_).md>), instead of or in addition to [- cachedResponseForRequest:](<urlcache/cachedresponse(for_).md>).
- Removing cached responses — Override the task-based [- removeCachedResponseForDataTask:](<urlcache/removecachedresponse(for_)-1zwp6.md>), instead of or in addition to the request-based [- removeCachedResponseForRequest:](<urlcache/removecachedresponse(for_)-1dh89.md>).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting and setting shared cache

- [sharedURLCache](urlcache/shared.md) — The shared URL cache instance.

### Creating a new cache object

- [init(memoryCapacity:diskCapacity:directory:)](<urlcache/init(memorycapacity_diskcapacity_directory_).md>) — Creates a URL cache object with the specified memory and disk capacities, in the specified directory.
- [- initWithMemoryCapacity:diskCapacity:diskPath:](<urlcache/init(memorycapacity_diskcapacity_diskpath_).md>) — Creates a URL cache object with the specified values. _(deprecated)_

### Getting and storing cached objects

- [- cachedResponseForRequest:](<urlcache/cachedresponse(for_).md>) — Returns the cached URL response in the cache for the specified URL request.
- [- storeCachedResponse:forRequest:](<urlcache/storecachedresponse(__for_)-7p7bl.md>) — Stores a cached URL response for a specified request.
- [- getCachedResponseForDataTask:completionHandler:](<urlcache/getcachedresponse(for_completionhandler_).md>) — Gets the cached URL response for a data task, passing it to the provided completion handler.
- [- storeCachedResponse:forDataTask:](<urlcache/storecachedresponse(__for_)-8uq91.md>) — Stores a cached URL response for a specified data task.

### Removing cached objects

- [- removeCachedResponseForRequest:](<urlcache/removecachedresponse(for_)-1dh89.md>) — Removes the cached URL response for a specified URL request.
- [- removeCachedResponseForDataTask:](<urlcache/removecachedresponse(for_)-1zwp6.md>) — Removes the cached URL response for a specified data task.
- [- removeCachedResponsesSinceDate:](<urlcache/removecachedresponses(since_).md>) — Clears the given cache of any cached responses since the provided date.
- [- removeAllCachedResponses](<urlcache/removeallcachedresponses().md>) — Clears the receiver’s cache, removing all stored cached URL responses.

### Getting and setting on-disk cache properties

- [currentDiskUsage](urlcache/currentdiskusage.md) — The current size of the on-disk cache, in bytes.
- [diskCapacity](urlcache/diskcapacity.md) — The capacity of the on-disk cache, in bytes.

### Getting and setting in-memory cache properties

- [currentMemoryUsage](urlcache/currentmemoryusage.md) — The current size of the in-memory cache, in bytes.
- [memoryCapacity](urlcache/memorycapacity.md) — The capacity of the in-memory cache, in bytes.

### Cache storage policies

- [StoragePolicy](urlcache/storagepolicy.md) — These constants specify the caching strategy used by an [CachedURLResponse](cachedurlresponse.md) object.

## See Also

### Cache behavior

- [Accessing cached data](accessing-cached-data.md) — Control how URL requests make use of previously cached data.
- [CachedURLResponse](cachedurlresponse.md) — A cached response to a URL request.
