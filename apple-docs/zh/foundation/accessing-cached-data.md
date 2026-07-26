---
title: 访问缓存数据
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/accessing-cached-data
source_url: 'https://developer.apple.com/documentation/foundation/accessing-cached-data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/accessing-cached-data.json'
content_hash: 'sha256:9f8f30c5794090ec'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md)

# 访问缓存数据

<sub>文章</sub>

控制 URL 请求如何使用先前缓存的数据。

## 概述

URL Loading System 会同时在内存和磁盘上缓存响应，从而提升性能并减少网络流量。

[URLCache](urlcache.md) 类用于缓存来自网络资源的响应。你的 App 可以通过 `URLCache` 的 [sharedURLCache](urlcache/shared.md) 属性直接访问共享的缓存实例。你也可以为不同用途创建自己的缓存，并在你的 [URLSessionConfiguration](urlsessionconfiguration.md) 对象上设置各自不同的缓存。

### 为 URL 请求设置缓存策略

每个 [URLRequest](urlrequest.md) 实例都包含一个 [CachePolicy](urlrequest/cachepolicy-swift.typealias.md) 对象，用于指明是否应执行缓存以及如何执行缓存。你可以更改该策略来控制该请求的缓存行为。

为方便起见，[URLSessionConfiguration](urlsessionconfiguration.md) 有一个名为 [requestCachePolicy](urlsessionconfiguration/requestcachepolicy.md) 的属性；使用该配置创建的会话所生成的所有请求，都会从该配置继承其缓存策略。

各种策略的行为见 doc:accessing-cached-data#Table-1。该表展示了各策略在从缓存加载还是从原始来源（例如服务器或本地文件系统）加载方面各自的偏好。目前，只有 HTTP 和 HTTPS 响应会被缓存。对于 FTP 和文件 URL，某项策略唯一的作用是决定该请求是否被允许访问原始来源。

| Cache policy | Local cache | Originating source |
|---|---|---|
| [NSURLRequestReloadIgnoringLocalCacheData](nsurlrequest/cachepolicy-swift.enum/reloadignoringlocalcachedata.md) | 忽略 | 仅访问 |
| [NSURLRequestReturnCacheDataDontLoad](nsurlrequest/cachepolicy-swift.enum/returncachedatadontload.md) | 仅访问 | 忽略 |
| [NSURLRequestReturnCacheDataElseLoad](nsurlrequest/cachepolicy-swift.enum/returncachedataelseload.md) | 优先尝试 | 仅在需要时访问 |
| [NSURLRequestUseProtocolCachePolicy](nsurlrequest/cachepolicy-swift.enum/useprotocolcachepolicy.md) | 取决于协议 | 取决于协议 |

有关 `useProtocolCachePolicy` 在 HTTP 和 HTTPS 中是如何实现的说明，请参阅 [CachePolicy](nsurlrequest/cachepolicy-swift.enum.md)。`useProtocolCachePolicy` 是 `URLRequest` 对象的默认值。

> [!note] 注意
> `useProtocolCachePolicy` 会将 HTTPS 响应缓存到磁盘，这对于保护用户数据的安全性而言可能并不理想。你可以按照[以编程方式管理缓存](accessing-cached-data.md#Manage-caching-programmatically)中所述，通过手动处理缓存行为来更改此行为。

### 直接访问该缓存

你可以通过某个会话的 [configuration](urlsession/configuration.md) 对象的 [URLCache](urlsessionconfiguration/urlcache.md) 属性，获取或设置某个 `URLSession` 对象所使用的缓存对象。

要查找某个给定请求对应的缓存响应，请在该缓存上调用 [- cachedResponseForRequest:](<urlcache/cachedresponse(for_).md>)。如果该请求存在已缓存的数据，此调用会返回一个 [CachedURLResponse](cachedurlresponse.md) 对象；否则，它会返回 `nil`。

你可以查看该缓存所使用的资源。[currentDiskUsage](urlcache/currentdiskusage.md) 和 [diskCapacity](urlcache/diskcapacity.md) 属性表示该缓存所使用的文件系统资源，而 [currentMemoryUsage](urlcache/currentmemoryusage.md) 和 [memoryCapacity](urlcache/memorycapacity.md) 表示内存使用情况。

你可以使用 [- removeCachedResponseForRequest:](<urlcache/removecachedresponse(for_)-1dh89.md>) 移除单个条目的缓存数据。你也可以使用 [- removeCachedResponsesSinceDate:](<urlcache/removecachedresponses(since_).md>) 同时清除多个缓存条目（它会移除某个给定日期之后的缓存条目），或者使用 [- removeAllCachedResponses](<urlcache/removeallcachedresponses().md>) 清空整个缓存。

### 以编程方式管理缓存

你可以使用 [- storeCachedResponse:forRequest:](<urlcache/storecachedresponse(__for_)-7p7bl.md>) 方法，传入一个新的 `CachedURLResponse` 对象和一个 `URLRequest` 对象，以编程方式写入该缓存。

通常情况下，你会在某个响应正被某个 `URLSessionTask` 对象处理期间管理其缓存。要按响应逐一管理缓存，请实现 [URLSessionDataDelegate](urlsessiondatadelegate.md) 协议的 [- URLSession:dataTask:willCacheResponse:completionHandler:](<urlsessiondatadelegate/urlsession(__datatask_willcacheresponse_completionhandler_).md>) 方法。请注意，该委托方法只会针对上传任务和数据任务被调用，对于使用后台或临时配置的会话则不会被调用。

该委托会接收两个参数：一个 `CachedURLResponse` 对象和一个完成处理程序。你的委托_必须_直接调用该完成处理程序，并传入以下之一：

- 提供的 `CachedURLResponse` 对象，以原样缓存所提议的响应
- `nil`，以阻止缓存
- 一个新创建的 `CachedURLResponse` 对象，通常基于所提供的对象，但按你的需要修改了其 [storagePolicy](cachedurlresponse/storagepolicy.md) 和 [userInfo](cachedurlresponse/userinfo.md) 字典

以下示例展示了 `urlSession(_:dataTask:willCacheResponse:completionHandler:)` 的一种实现，它拦截了对 HTTPS 请求的响应，并只允许这些响应被存储在内存缓存中。

处理 urlSession(_:dataTask:willCacheResponse:completionHandler:) 回调

```swift
func urlSession(_ session: URLSession, dataTask: URLSessionDataTask,
                willCacheResponse proposedResponse: CachedURLResponse,
                completionHandler: @escaping (CachedURLResponse?) -> Void) {
    if proposedResponse.response.url?.scheme == "https" {
        let updatedResponse = CachedURLResponse(response: proposedResponse.response,
                                                data: proposedResponse.data,
                                                userInfo: proposedResponse.userInfo,
                                                storagePolicy: .allowedInMemoryOnly)
        completionHandler(updatedResponse)
    } else {
        completionHandler(proposedResponse)
    }
}
```

## 另请参阅

### Cache behavior

- [CachedURLResponse](cachedurlresponse.md) — 对某个 URL 请求的缓存响应。
- [URLCache](urlcache.md) — 一个将 URL 请求映射到缓存响应对象的对象。
