---
title: SDWebImage 实现原理与源码简析
source_url: 'https://www.cnblogs.com/zhangzhang-y/p/13584570.html'
source_domain: cnblogs.com
source_group: platform
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:52b090f7bff8b17a'
plan_ref: 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 6｜SDWebImage 第一遍只看成功路径（对应 W6-05）
plan_week: 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天）
plan_day: Day 6｜SDWebImage 第一遍只看成功路径（对应 W6-05）
container: '//div[@id=''cnblogs_post_body'']'
container_source: map
---

> 原文：[SDWebImage 实现原理与源码简析](https://www.cnblogs.com/zhangzhang-y/p/13584570.html)

本文主要用来 对 **[SDWebImage](https://github.com/SDWebImage/SDWebImage)**的整体实现原理和源码进行简单解析。

**SDWebImage 架构图：**

![](https://img2020.cnblogs.com/blog/842658/202008/842658-20200831111832534-214390971.png)

流程简概：

![](https://img2020.cnblogs.com/blog/842658/202008/842658-20200831112415835-1221017647.png)

**图片加载流程**

![](https://img2020.cnblogs.com/blog/842658/202008/842658-20200831114248017-1113051574.png)

**一、加载图片流程**

加载图片时，首先 图片是在本地缓存还是网络

```
- (void)sd_internalSetImageWithURL:(nullable NSURL *)url
                  placeholderImage:(nullable UIImage *)placeholder
                           options:(SDWebImageOptions)options
                      operationKey:(nullable NSString *)operationKey
                     setImageBlock:(nullable SDSetImageBlock)setImageBlock
                          progress:(nullable SDWebImageDownloaderProgressBlock)progressBlock
                         completed:(nullable SDExternalCompletionBlock)completedBlock
                           context:(nullable NSDictionary *)context;
```

1、判断当前是否已存在任务(查找/下载)，通过 operationKey 值查询任务(NSMapTable 存储，当前的UI控件正在进行的任务)，进行相应的取消时也是通过相应的 key 进行操作。

- (void)sd_cancelImageLoadOperationWithKey:(nullable NSString *)key{ }

2、加载图片 loadImageWithURL:

3、加载完成之后 --\> 此时图片是否需要特殊处理(传给调用者 or 直接显示sd_setNeedsLayout)

**二、缓存模块 - SDImageCache**

SD 内存/磁盘双缓存。

SDImageCacheConfig：缓存的一些配置项 --\> shouldCacheImagesInMemory / shouldUseWeakMemoryCache ...

SDImageCache： 缓存逻辑

**1、内存缓存 SDMemoryCache (继承 NSCache)**

1.1）为何不直接使用 NSCache？ --\> 系统自行清理缓存，清理时间内容无法自行控制

SDMemoryCache 通过 NSMapTable 存储，并监听了 内存警告 didReceiveMemoryWarning 对内存缓存进行相应清理处理。

1.2）缓存逻辑

**重写 NSCache 的方法**

```
- (id)objectForKey:(id)key {
    id obj = [super objectForKey:key];
    if (!self.config.shouldUseWeakMemoryCache) {
        return obj;
    }
    if (key && !obj) {
        // Check weak cache
        SD_LOCK(self.weakCacheLock);
        obj = [self.weakCache objectForKey:key];
        SD_UNLOCK(self.weakCacheLock);
        if (obj) {
            // Sync cache
            NSUInteger cost = 0;
            if ([obj isKindOfClass:[UIImage class]]) {
                cost = [(UIImage *)obj sd_memoryCost];
            }
            [super setObject:obj forKey:key cost:cost];
        }
    }
    return obj;
}
```

缓存首先在 NSCache 中存一份 --\> shouldUseWeakMemoryCache 属性 ture的话，会再次在自己创建的 weakCache 中再存一份。--\> 同时将缓存信息同步到 NSCache 中

为何这样操作？ --\> NSCache 清理内存时不可控，当我们需要使用某个缓存C时，若不自己处理，C可能已经被释放掉，我们便需要再次请求 --\> 但是当我们又自行存储一份时，可直接从 weakCache 中取出数据。 --\> 以空间换时间

**2、磁盘缓存 disk**

```
// 创建文件 --> _diskCachePath
- (nullable NSString *)makeDiskCachePath:(nonnull NSString*)fullNamespace {
    NSArray<NSString *> *paths = NSSearchPathForDirectoriesInDomains(NSCachesDirectory, NSUserDomainMask, YES);
    return [paths[0] stringByAppendingPathComponent:fullNamespace];
}

// 文件目录
- (nullable NSString *)cachePathForKey:(nullable NSString *)key inPath:(nonnull NSString *)path {
    NSString *filename = [self cachedFileNameForKey:key];
    return [path stringByAppendingPathComponent:filename];
}

// 缓存文件名
- (nullable NSString *)cachedFileNameForKey:(nullable NSString *)key {
    const char *str = key.UTF8String;
    if (str == NULL) {
        str = "";
    }
    unsigned char r[CC_MD5_DIGEST_LENGTH];
    CC_MD5(str, (CC_LONG)strlen(str), r);
    NSURL *keyURL = [NSURL URLWithString:key];
    NSString *ext = keyURL ? keyURL.pathExtension : key.pathExtension;
    NSString *filename = [NSString stringWithFormat:@"%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%@",
                          r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10],
                          r[11], r[12], r[13], r[14], r[15], ext.length == 0 ? @"" : [NSString stringWithFormat:@".%@", ext]];
    return filename;
}
```

存放在文件目录中 --\> 创建目录 --\> 为每个缓存文件创建一个MD5的文件名 --\> 保证了文件的唯一性

存储：

```
// 缓存存储
- (void)storeImage:(nullable UIImage *)image
            forKey:(nullable NSString *)key
            toDisk:(BOOL)toDisk
        completion:(nullable SDWebImageNoParamsBlock)completionBlock {
    [self storeImage:image imageData:nil forKey:key toDisk:toDisk completion:completionBlock];
}

- (void)storeImage:(nullable UIImage *)image
         imageData:(nullable NSData *)imageData
            forKey:(nullable NSString *)key
            toDisk:(BOOL)toDisk
        completion:(nullable SDWebImageNoParamsBlock)completionBlock {

    if (!image || !key) {
        if (completionBlock) {
            completionBlock();
        }
        return;
    }
    // if memory cache is enabled 存入内存缓存中
    if (self.config.shouldCacheImagesInMemory) {
        NSUInteger cost = SDCacheCostForImage(image);
        [self.memCache setObject:image forKey:key cost:cost];
    }
    
    if (toDisk) {
        dispatch_async(self.ioQueue, ^{
            @autoreleasepool {
                NSData *data = imageData;
                if (!data && image) {
                    // If we do not have any data to detect image format, use PNG format
                    data = [[SDWebImageCodersManager sharedInstance] encodedDataWithImage:image format:SDImageFormatPNG];
                }
                [self storeImageDataToDisk:data forKey:key];
            }
            
            if (completionBlock) {
                dispatch_async(dispatch_get_main_queue(), ^{
                    completionBlock();
                });
            }
        });
    } else {
        if (completionBlock) {
            completionBlock();
        }
    }
}
```

**3、读缓存**

SDWebImageManager 中 方法 loadImageWithURL中 [self.imageCache queryCacheOperationForKey:key done:block{}]// 查询缓存的逻辑- (nullable NSOperation *)queryCacheOperationForKey:(nullable NSString *)key done:(nullable SDCacheQueryCompletedBlock)doneBlock {

```
if (!key) {
        if (doneBlock) {
            doneBlock(nil, nil, SDImageCacheTypeNone);
        }
        return nil;
    }

    // First check the in-memory cache...
    UIImage *image = [self imageFromMemoryCacheForKey:key];
    if (image) {
        NSData *diskData = nil;
        if (image.images) {
            diskData = [self diskImageDataBySearchingAllPathsForKey:key];
        }
        if (doneBlock) {
            doneBlock(image, diskData, SDImageCacheTypeMemory);
        }
        return nil;
    }　　 // 磁盘缓存
　　 // 查询磁盘缓存的任务    NSOperation *operation = [NSOperation new];
    dispatch_async(self.ioQueue, ^{
        if (operation.isCancelled) {
            // do not call the completion if cancelled
            return;
        }

        @autoreleasepool {
            NSData *diskData = [self diskImageDataBySearchingAllPathsForKey:key];
            UIImage *diskImage = [self diskImageForKey:key];
            if (diskImage && self.config.shouldCacheImagesInMemory) {
                NSUInteger cost = SDCacheCostForImage(diskImage);
                [self.memCache setObject:diskImage forKey:key cost:cost];
            }

            if (doneBlock) {
                dispatch_async(dispatch_get_main_queue(), ^{
                    doneBlock(diskImage, diskData, SDImageCacheTypeDisk);
                });
            }
        }
    });

    return operation;
}
```

3.1）首先查询内存缓存 --\> key 对应的 value 都是我们 存储在 memoryCache 中的 UIImage

3.2）内存没有 去磁盘 --\> 初始化 operation 任务，此任务用来给调用者，且保存(用来查询任务时使用)。 --\>

- (nullable NSData *)diskImageDataBySearchingAllPathsForKey:(nullable NSString *)key; // 查找当前文件目录 文件名

--\> 将查询到的2进制图片data 数据取出，归档处理成 UIImage 对象, NSData ==\> UIImage.

**三、下载 - SDWebImageDownloader**

**1、SDWebImageDownloader**

管理类，一些公共设置处理。

1. 配置下载相关的属性

2. 任务顺序 --\> 下载队列的先后顺序

3. 下载任务最大并发量

......

**1.1）源码解析**

```
// 处理 下载逻辑 
- (nullable SDWebImageDownloadToken *)downloadImageWithURL:(nullable NSURL *)url
                                                   options:(SDWebImageDownloaderOptions)options
                                                   context:(nullable SDWebImageContext *)context
                                                  progress:(nullable SDWebImageDownloaderProgressBlock)progressBlock
                                                 completed:(nullable SDWebImageDownloaderCompletedBlock)completedBlock {

    // The URL will be used as the key to the callbacks dictionary so it cannot be nil. If it is nil immediately call the completed block with no image or data.
    if (url == nil) {
        if (completedBlock) {
            NSError *error = [NSError errorWithDomain:SDWebImageErrorDomain code:SDWebImageErrorInvalidURL userInfo:@{NSLocalizedDescriptionKey : @"Image url is nil"}];
            completedBlock(nil, nil, error, YES);
        }
        return nil;
    }
    
    SD_LOCK(self.operationsLock);
    id downloadOperationCancelToken;
    NSOperation<SDWebImageDownloaderOperation> *operation = [self.URLOperations objectForKey:url];
    // There is a case that the operation may be marked as finished or cancelled, but not been removed from `self.URLOperations`.
    if (!operation || operation.isFinished || operation.isCancelled) {
        
        // url 来初始化任务 - SDWebImageDownloaderOperation
        operation = [self createDownloaderOperationWithUrl:url options:options context:context];
        if (!operation) {
            SD_UNLOCK(self.operationsLock);
            if (completedBlock) {
                NSError *error = [NSError errorWithDomain:SDWebImageErrorDomain code:SDWebImageErrorInvalidDownloadOperation userInfo:@{NSLocalizedDescriptionKey : @"Downloader operation is nil"}];
                completedBlock(nil, nil, error, YES);
            }
            return nil;
        }
        @weakify(self);
        operation.completionBlock = ^{
            @strongify(self);
            if (!self) {
                return;
            }
            SD_LOCK(self.operationsLock);
            [self.URLOperations removeObjectForKey:url];
            SD_UNLOCK(self.operationsLock);
        };
        self.URLOperations[url] = operation;
        // Add the handlers before submitting to operation queue, avoid the race condition that operation finished before setting handlers.
        downloadOperationCancelToken = [operation addHandlersForProgress:progressBlock completed:completedBlock];
        // Add operation to operation queue only after all configuration done according to Apple's doc.
        // `addOperation:` does not synchronously execute the `operation.completionBlock` so this will not cause deadlock.
        [self.downloadQueue addOperation:operation];
    } else {
        // When we reuse the download operation to attach more callbacks, there may be thread safe issue because the getter of callbacks may in another queue (decoding queue or delegate queue)
        // So we lock the operation here, and in `SDWebImageDownloaderOperation`, we use `@synchonzied (self)`, to ensure the thread safe between these two classes.
        @synchronized (operation) {
            downloadOperationCancelToken = [operation addHandlersForProgress:progressBlock completed:completedBlock];
        }
        if (!operation.isExecuting) {
            if (options & SDWebImageDownloaderHighPriority) {
                operation.queuePriority = NSOperationQueuePriorityHigh;
            } else if (options & SDWebImageDownloaderLowPriority) {
                operation.queuePriority = NSOperationQueuePriorityLow;
            } else {
                operation.queuePriority = NSOperationQueuePriorityNormal;
            }
        }
    }
    SD_UNLOCK(self.operationsLock);
    
    SDWebImageDownloadToken *token = [[SDWebImageDownloadToken alloc] initWithDownloadOperation:operation];
    token.url = url;
    token.request = operation.request;
    token.downloadOperationCancelToken = downloadOperationCancelToken;
    
    return token;
}
```

```
// NSOperation 创建逻辑
// Request 各属性设置 / 证书urlCredential / 下载优先级 / ...
- (nullable NSOperation<SDWebImageDownloaderOperation> *)createDownloaderOperationWithUrl:(nonnull NSURL *)url
                                                                                  options:(SDWebImageDownloaderOptions)options
                                                                                  context:(nullable SDWebImageContext *)context {
    NSTimeInterval timeoutInterval = self.config.downloadTimeout;
    if (timeoutInterval == 0.0) {
        timeoutInterval = 15.0;
    }
    
    // In order to prevent from potential duplicate caching (NSURLCache + SDImageCache) we disable the cache for image requests if told otherwise
    NSURLRequestCachePolicy cachePolicy = options & SDWebImageDownloaderUseNSURLCache ? NSURLRequestUseProtocolCachePolicy : NSURLRequestReloadIgnoringLocalCacheData;
    NSMutableURLRequest *mutableRequest = [[NSMutableURLRequest alloc] initWithURL:url cachePolicy:cachePolicy timeoutInterval:timeoutInterval];
    mutableRequest.HTTPShouldHandleCookies = SD_OPTIONS_CONTAINS(options, SDWebImageDownloaderHandleCookies);
    mutableRequest.HTTPShouldUsePipelining = YES;
    SD_LOCK(self.HTTPHeadersLock);
    mutableRequest.allHTTPHeaderFields = self.HTTPHeaders;
    SD_UNLOCK(self.HTTPHeadersLock);
    
    // Context Option
    SDWebImageMutableContext *mutableContext;
    if (context) {
        mutableContext = [context mutableCopy];
    } else {
        mutableContext = [NSMutableDictionary dictionary];
    }
    
    // Request Modifier
    id<SDWebImageDownloaderRequestModifier> requestModifier;
    if ([context valueForKey:SDWebImageContextDownloadRequestModifier]) {
        requestModifier = [context valueForKey:SDWebImageContextDownloadRequestModifier];
    } else {
        requestModifier = self.requestModifier;
    }
    
    NSURLRequest *request;
    if (requestModifier) {
        NSURLRequest *modifiedRequest = [requestModifier modifiedRequestWithRequest:[mutableRequest copy]];
        // If modified request is nil, early return
        if (!modifiedRequest) {
            return nil;
        } else {
            request = [modifiedRequest copy];
        }
    } else {
        request = [mutableRequest copy];
    }
    // Response Modifier
    id<SDWebImageDownloaderResponseModifier> responseModifier;
    if ([context valueForKey:SDWebImageContextDownloadResponseModifier]) {
        responseModifier = [context valueForKey:SDWebImageContextDownloadResponseModifier];
    } else {
        responseModifier = self.responseModifier;
    }
    if (responseModifier) {
        mutableContext[SDWebImageContextDownloadResponseModifier] = responseModifier;
    }
    // Decryptor
    id<SDWebImageDownloaderDecryptor> decryptor;
    if ([context valueForKey:SDWebImageContextDownloadDecryptor]) {
        decryptor = [context valueForKey:SDWebImageContextDownloadDecryptor];
    } else {
        decryptor = self.decryptor;
    }
    if (decryptor) {
        mutableContext[SDWebImageContextDownloadDecryptor] = decryptor;
    }
    
    context = [mutableContext copy];
    
    // Operation Class
    Class operationClass = self.config.operationClass;
    if (operationClass && [operationClass isSubclassOfClass:[NSOperation class]] && [operationClass conformsToProtocol:@protocol(SDWebImageDownloaderOperation)]) {
        // Custom operation class
    } else {
        operationClass = [SDWebImageDownloaderOperation class];
    }
    NSOperation<SDWebImageDownloaderOperation> *operation = [[operationClass alloc] initWithRequest:request inSession:self.session options:options context:context];
    
    if ([operation respondsToSelector:@selector(setCredential:)]) {
        if (self.config.urlCredential) {
            operation.credential = self.config.urlCredential;
        } else if (self.config.username && self.config.password) {
            operation.credential = [NSURLCredential credentialWithUser:self.config.username password:self.config.password persistence:NSURLCredentialPersistenceForSession];
        }
    }
        
    if ([operation respondsToSelector:@selector(setMinimumProgressInterval:)]) {
        operation.minimumProgressInterval = MIN(MAX(self.config.minimumProgressInterval, 0), 1);
    }
    
    if (options & SDWebImageDownloaderHighPriority) {
        operation.queuePriority = NSOperationQueuePriorityHigh;
    } else if (options & SDWebImageDownloaderLowPriority) {
        operation.queuePriority = NSOperationQueuePriorityLow;
    }
    
    // 下载优先级 
    if (self.config.executionOrder == SDWebImageDownloaderLIFOExecutionOrder) {// 后进先出
        // Emulate LIFO execution order by systematically, each previous adding operation can dependency the new operation
        // This can gurantee the new operation to be execulated firstly, even if when some operations finished, meanwhile you appending new operations
        // Just make last added operation dependents new operation can not solve this problem. See test case #test15DownloaderLIFOExecutionOrder
        for (NSOperation *pendingOperation in self.downloadQueue.operations) {
            [pendingOperation addDependency:operation];
        }
    }
    return operation;
}
```

**1.2）下载优先级的控制**

_如上代码优先级分为两种：**FIFO / LIFO**_

```
/// Operation execution order
typedef NS_ENUM(NSInteger, SDWebImageDownloaderExecutionOrder) {
    /**
     * Default value. All download operations will execute in queue style (first-in-first-out).　　　　默认值 - 先进先出 所有下载操作以队列形式执行
     */
    SDWebImageDownloaderFIFOExecutionOrder,
    
    /**
     * All download operations will execute in stack style (last-in-first-out).　　　　后进先出 下载操作以栈的方式执行
     */
    SDWebImageDownloaderLIFOExecutionOrder
};
```

如何管理：SDWebImageDownloaderExecutionOrder

当前的 operation 设置依赖 --\> LIFO，当前的新进来的 operation 执行完成之后 之前的任务才执行。

**2、SDWebImageDownloaderOperation：**

具体的下载任务由它完成.

继承 NSOperation.

2.1）Operation 创建完成，进入 SDWebImageDownloaderOperation

重写了-(void)start; 方法

**3、下载完成后，在相应的 NSURLSessionDataDelegate 代理回调中处理相关数据.**

待续。。。

**---------------------------------**

_简单介绍：NSMapTable 和 NSDictionary -- [NSMapTable 苹果文档](https://developer.apple.com/documentation/foundation/nsmaptable?preferredLanguage=occ)_

NSDictionary 中 setValue:forKey: 中 key 必须妈祖实现 NSCoping 协议，此时，当我们以自定义类 MYXXX 为key 时，会自动进行copy 其 内存地址会发生改变。

NSMapTable 类似于 NSDictionary，但 NSMapTable 可提供更多的内存语义；

```
self.weakCache = [[NSMapTable alloc] initWithKeyOptions:NSPointerFunctionsStrongMemory valueOptions:NSPointerFunctionsWeakMemory capacity:0];
```

NSMapTable ， key: strongMemory value: weakMemory --\> 意味着，当前存储的value 弱引用,不会对其他对象产生任何影响，只是存在了全局的 weak表中，当对象释放时，对应的value就会被释放 --\> 即 NSMapTable 会自动删除 当前的 key/Value.
