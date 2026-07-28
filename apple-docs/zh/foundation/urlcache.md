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
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# URLCache

<sub>类</sub>

一个将 URL 请求映射到已缓存响应对象的对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class URLCache
```

## 概述

[URLCache](urlcache.md) 类通过将 [NSURLRequest](nsurlrequest.md) 对象映射到 [CachedURLResponse](cachedurlresponse.md) 对象，实现了对 URL 加载请求响应的缓存。它提供了一个内存和磁盘的复合缓存，并允许你操作内存和磁盘部分的大小。你还可以控制持久化存储缓存数据的路径。

> [!note] 注意
> 在 iOS 中，当系统磁盘空间不足时，磁盘缓存可能会被清除，但这只会在你的 App 未运行时发生。

### 线程安全

在 iOS 8 及更高版本以及 macOS 10.10 及更高版本中，[URLCache](urlcache.md) 是线程安全的（thread safe）。

虽然可以从多个执行上下文同时安全地调用 [URLCache](urlcache.md) 实例方法，但请注意，当尝试对同一请求读取或写入响应时，诸如 [- cachedResponseForRequest:](<urlcache/cachedresponse(for_).md>) 和 [- storeCachedResponse:forRequest:](<urlcache/storecachedresponse(__for_)-7p7bl.md>) 之类的方法存在不可避免的竞态条件（race condition）。

[URLCache](urlcache.md) 的子类必须以这种线程安全的方式重写方法。

### 子类化说明

[URLCache](urlcache.md) 类旨在按原样使用，但当你具有特定需求时，可以为其创建子类。例如，你可能希望筛选哪些响应被缓存，或出于安全或其他原因重新实现存储机制。

在重写此类的方法时，请注意，带有 `task` 参数的方法比不带该参数的方法更受系统青睐。因此，在派生子类时，你应该重写基于任务（task）的方法，具体如下：

- 在缓存中存储响应——重写基于任务的 [- storeCachedResponse:forDataTask:](<urlcache/storecachedresponse(__for_)-8uq91.md>)，以替代或补充基于请求的 [- storeCachedResponse:forRequest:](<urlcache/storecachedresponse(__for_)-7p7bl.md>)。
- 从缓存获取响应——重写 [- getCachedResponseForDataTask:completionHandler:](<urlcache/getcachedresponse(for_completionhandler_).md>)，以替代或补充 [- cachedResponseForRequest:](<urlcache/cachedresponse(for_).md>)。
- 移除缓存的响应——重写基于任务的 [- removeCachedResponseForDataTask:](<urlcache/removecachedresponse(for_)-1zwp6.md>)，以替代或补充基于请求的 [- removeCachedResponseForRequest:](<urlcache/removecachedresponse(for_)-1dh89.md>)。

## 关系

- **继承自**：[NSObject](../objectivec/nsobject-swift.class.md)

- **遵循**：[CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## 主题

### 获取和设置共享缓存

- [sharedURLCache](urlcache/shared.md) — 共享 URL 缓存实例。

### 创建新的缓存对象

- [init(memoryCapacity:diskCapacity:directory:)](<urlcache/init(memorycapacity_diskcapacity_directory_).md>) — 使用指定的内存容量和磁盘容量在指定目录中创建一个 URL 缓存对象。
- [- initWithMemoryCapacity:diskCapacity:diskPath:](<urlcache/init(memorycapacity_diskcapacity_diskpath_).md>) — 使用指定的值创建一个 URL 缓存对象。_(已废弃)_

### 获取和存储缓存对象

- [- cachedResponseForRequest:](<urlcache/cachedresponse(for_).md>) — 返回缓存中指定 URL 请求对应的缓存 URL 响应。
- [- storeCachedResponse:forRequest:](<urlcache/storecachedresponse(__for_)-7p7bl.md>) — 为指定的请求存储一个缓存的 URL 响应。
- [- getCachedResponseForDataTask:completionHandler:](<urlcache/getcachedresponse(for_completionhandler_).md>) — 获取数据任务（data task）对应的缓存 URL 响应，并将其传递给提供的完成处理程序（completion handler）。
- [- storeCachedResponse:forDataTask:](<urlcache/storecachedresponse(__for_)-8uq91.md>) — 为指定的数据任务存储一个缓存的 URL 响应。

### 移除缓存对象

- [- removeCachedResponseForRequest:](<urlcache/removecachedresponse(for_)-1dh89.md>) — 移除指定 URL 请求对应的缓存 URL 响应。
- [- removeCachedResponseForDataTask:](<urlcache/removecachedresponse(for_)-1zwp6.md>) — 移除指定数据任务对应的缓存 URL 响应。
- [- removeCachedResponsesSinceDate:](<urlcache/removecachedresponses(since_).md>) — 从缓存中清除自指定日期以来的所有缓存响应。
- [- removeAllCachedResponses](<urlcache/removeallcachedresponses().md>) — 清空接收方的缓存，移除所有已存储的缓存 URL 响应。

### 获取和设置磁盘缓存属性

- [currentDiskUsage](urlcache/currentdiskusage.md) — 磁盘缓存的当前大小（以字节为单位）。
- [diskCapacity](urlcache/diskcapacity.md) — 磁盘缓存的容量（以字节为单位）。

### 获取和设置内存缓存属性

- [currentMemoryUsage](urlcache/currentmemoryusage.md) — 内存缓存的当前大小（以字节为单位）。
- [memoryCapacity](urlcache/memorycapacity.md) — 内存缓存的容量（以字节为单位）。

### 缓存存储策略

- [StoragePolicy](urlcache/storagepolicy.md) — 这些常量指定了 [CachedURLResponse](cachedurlresponse.md) 对象使用的缓存策略。

## 另请参阅

### 缓存行为

- [访问缓存数据](accessing-cached-data.md) — 控制 URL 请求如何利用之前缓存的数据。
- [CachedURLResponse](cachedurlresponse.md) — 对 URL 请求的缓存响应。
