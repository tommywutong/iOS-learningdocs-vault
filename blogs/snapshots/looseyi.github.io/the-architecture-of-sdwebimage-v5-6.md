---
title: The Architecture of SDWebImage v5.6
source_url: 'https://looseyi.github.io/post/sourcecode-ios/source-code-sdweb-en1/'
source_domain: looseyi.github.io
source_group: single-site
original_language: en
published: 2020-04-12
archived_at: 2026-07-27
content_hash: 'sha256:b2d16286f54d23a1'
plan_ref: 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 7｜第二遍才看性能与取消（对应 W6-05、W6-09）
plan_week: 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天）
plan_day: Day 7｜第二遍才看性能与取消（对应 W6-05、W6-09）
container: '//*[contains(@class,''post-content'')]'
container_source: guess
---

> 原文：[The Architecture of SDWebImage v5.6](https://looseyi.github.io/post/sourcecode-ios/source-code-sdweb-en1/)

This article is based on SDWebImage 5.6. Why i write this article, cause i found that SD’s API is constantly iterating, and many of the structures are different from earlier versions. Here is to make a record. We will start from the top of the API’s level list below, force on the entire framework’s data flow.

![highlevel](https://raw.githubusercontent.com/SDWebImage/SDWebImage/master/Docs/Diagrams/SDWebImageHighLevelDiagram.jpeg)

## 5.0 Migration Guid

It is highly recommended to watch the official [migration document](https://github.com/SDWebImage/SDWebImage/wiki/5.0-Migration-guide), which mentioned the mainly features in version 5.0.

- Brand new Animated Image View (was `FLAnimatedImageView` in 4.0);
- Image Transform is provided to easy way to scale, rotate, rounded corner and other operations after the image was downloaded;
- Customization, you can customize [cache](https://github.com/SDWebImage/SDWebImage/wiki/Advanced-Usage#custom-cache-50), [loader](https://github.com/SDWebImage/SDWebImage/wiki/Advanced-Usage#custom-loader-50), [coder](https://github.com/SDWebImage/SDWebImage/wiki/Advanced-Usage#custom-coder-420), which are base on the protocol;
- Added View Indicator to identify the loading status of Image;

I could say that the protocolization for the core classes is the biggest change in the 5.x SD version, which means the image request, loading, decoding, caching and other operations are pluggable and replaceable as you want.

So, let’s see the main part first:

| 4.x | 5.x |
|---|---|
| SDWebImageCacheSerializerBlock | id\<SDWebImageCacheSerializer\> |
| SDWebImageCacheKeyFilterBlock | id\<SDWebImageCacheKeyFilter\> |
| SDWebImageDownloader | id\<SDImageLoader\> |
| SDImageCache | id\<SDImageCache\> |
| SDWebImageDownloaderProgressBlock | id\<SDWebImageIndicator\> |
| FLAnimatedImageView | id\<SDAnimatedImage\> |

## View Category

All the view’s convenience method for image operation are base on `UIView + WebCache`, including the following:

- UIImageView+HighlightedWebCache
- UIImageView+WebCache
- UIView+WebCacheOperation
- UIButton+WebCache
- NSButton+WebCache

Firstly, let ’s take a look at [SDWebImageCompat.h](https://github.com/SDWebImage/SDWebImage/blob/09f06159a3284f6981d5495728e5c3cb3dfb82fa/SDWebImage/Core/SDWebImageCompat.h) , which defines **SD_MAC, SD_UIKIT, SD_WATCH** macros are used to Simplify the definition of the system, and used to unify the differences platforms API, such as using `# define UIImage NSImage` to redefine NSImage to UIImage. Another thing you would like to know is:

```objective
1#ifndef dispatch_main_async_safe
2#define dispatch_main_async_safe(block)\
3    if (dispatch_queue_get_label(DISPATCH_CURRENT_QUEUE_LABEL) == dispatch_queue_get_label(dispatch_get_main_queue())) {\
4        block();\
5    } else {\
6        dispatch_async(dispatch_get_main_queue(), block);\
7    }
8#endif
```

different from the earler version:

```objective
1#define dispatch_main_async_safe(block)\
2    if ([NSThread isMainThread]) {\
3        block();\
4    } else {\
5        dispatch_async(dispatch_get_main_queue(), block);\
6    }
7#endif
```

- use `#ifndef` to prevent repeated definition of `dispatch_main_async_safe`;
- Main thread detect change from `isMainThread` to `dispatch_queue_t` label

Abount the second point, here is a [Discussion of SD](https://github.com/SDWebImage/SDWebImage/pull/781), and another explanation [GCD’s Main Queue vs. Main Thread](http://blog.benjamin-encz.de/post/main-queue-vs-main-thread/))

> Calling an API from a non-main queue that is executing on the main thread will lead to issues if the library (like VektorKit) relies on checking for execution on the main queue.

Cause **tasks in the main queue must be put into the main thread to execute**.

Compared to the category of UIImageView, UIButton needs to store images under different `UIControlState` and backgrounImage, and SD associate has an internal dictionary ` (NSMutableDictionary <NSString *, NSURL *> *) sd_imageURLStorage` to store the images.

All view category’s `setImageUrl:` finally refer to the following method:

```objective
1- (void)sd_internalSetImageWithURL:(nullable NSURL *)url
2                  placeholderImage:(nullable UIImage *)placeholder
3                           options:(SDWebImageOptions)options
4                           context:(nullable SDWebImageContext *)context
5                     setImageBlock:(nullable SDSetImageBlock)setImageBlock
6                          progress:(nullable SDImageLoaderProgressBlock)progressBlock
7                         completed:(nullable SDInternalCompletionBlock)completedBlock;
```

This method’s implementation is quite long, here is the briefly describes:

1. Copy and convert `SDWebImageContext` to immutable, get the value of ` validOperationKey` as the verification id, the default value is the class name of the current view;
2. Call `sd_cancelImageLoadOperationWithKey` to cancel the last task, which to ensure that there is no asynchronous download operation currently in progress and no conflict with the upcoming operation;
3. Set the placeholder image;
4. Initialize `SDWebImageManager` , ` SDImageLoaderProgressBlock` , reset `NSProgress`, ` SDWebImageIndicator`;
5. Start downloading, call `loadImageWithURL:` and save the returned `SDWebImageOperation` into ` sd_operationDictionary`, which key is `validOperationKey`;
6. After getting the picture, call `sd_setImage:` and add transition animation to the new image;
7. Stop the indicator after the animation ends.

A tips, the `SDWebImageOperation` is a **strong-weak** NSMapTable, which is also added by the associated value:

```objective
1// key is strong, value is weak because operation instance is retained by SDWebImageManager's runningOperations property
2// we should use lock to keep thread-safe because these method may not be acessed from main queue
3typedef NSMapTable<NSString *, id<SDWebImageOperation>> SDOperationsDictionary;
```

Weak is used because the operation instance is stored in SDWebImageManager’s runningOperations, and the reference here is saved to easy cancel the task.

### SDWebImageContext

> A SDWebImageContext object which hold the original context options from top-level API.

Image context runs through the entire workflow of image processing. It brings data into each processing task step by step. There are two types of ImageContext:

```objectivec
1typedef NSString * SDWebImageContextOption NS_EXTENSIBLE_STRING_ENUM;
2typedef NSDictionary<SDWebImageContextOption, id> SDWebImageContext;
3typedef NSMutableDictionary<SDWebImageContextOption, id>SDWebImageMutableContext;
```

SDWebImageContextOption is an extensible String enumeration, there are currently 15 types. Basically, you can guess its function just by looking at the name, here is the [document](https://github.com/SDWebImage/SDWebImage/blob/5c3c40288f7e465ba94db9736e624f663831951a/SDWebImage/Core/SDWebImageDefine.h), summarized as follows:

![image context](http://ww1.sinaimg.cn/large/8157560cgy1gcbeto2gb6j20xj1whajv.jpg)

## ImagePrefetcher

Prefetcher has nothing to do with the entire processing stream of SD. It mainly uses imageManger for batch image download. Below is the core method:

```objective
1- (nullable SDWebImagePrefetchToken *)prefetchURLs:(nullable NSArray<NSURL *> *)urls
2                                          progress:(nullable SDWebImagePrefetcherProgressBlock)progressBlock
3                                         completed:(nullable SDWebImagePrefetcherCompletionBlock)completionBlock;
```

It stores the downloaded URLs as `transactions` in `SDWebImagePrefetchToken`, which do not cancel previous request and it separate different prefetching process. When you call `prefetchURLs` for different url lists, you can get callback for different completion block.

Each download task is in the autoreleasesepool, and will use `SDAsyncBlockOperation` to wrap the real download task to achieve the cancelable operation of the task:

```objective
 1@autoreleasepool {
 2    @weakify(self);
 3    SDAsyncBlockOperation *prefetchOperation = [SDAsyncBlockOperation blockOperationWithBlock:^(SDAsyncBlockOperation * _Nonnull asyncOperation) {
 4        @strongify(self);
 5        if (!self || asyncOperation.isCancelled) {
 6            return;
 7        }
 8        /// load Image ...
 9    }];
10    @synchronized (token) {
11        [token.prefetchOperations addPointer:(__bridge void *)prefetchOperation];
12    }
13    [self.prefetchQueue addOperation:prefetchOperation];
14}
```

Finally, the task is stored in prefetchQueue, which limit the maximum number of downloads to 3 by default. The real task of URLs downloading is in `token.loadOperations`:

```objective
1NSPointerArray *operations = token.loadOperations;
2id<SDWebImageOperation> operation = [self.manager loadImageWithURL:url options:self.options context:self.context progress:nil completed:^(UIImage * _Nullable image, NSData * _Nullable data, NSError * _Nullable error, SDImageCacheType cacheType, BOOL finished, NSURL * _Nullable imageURL) {
3    /// progress handler    
4}];
5NSAssert(operation != nil, @"Operation should not be nil, [SDWebImageManager loadImageWithURL:options:context:progress:completed:] break prefetch logic");
6@synchronized (token) {
7    [operations addPointer:(__bridge void *)operation];
8}
```

`loadOperations` and `prefetchOperations` All use **NSPointerArray**, which uses its [NSPointerFunctionsWeakMemory](apple-reference-documentation: // hcx77yk4jV) feature and can store ` Null` values, although its performance is not very good, see: [basic collection Class](https://objccn.io/issue-7-1/)

Another important thing is that PrefetchToken use the [c++11 memory_order_relaxed](https://zhuanlan.zhihu.com/p/45566448) to ensure the thread-safe。

```c++
1atomic_ulong _skippedCount;
2atomic_ulong _finishedCount;
3atomic_flag  _isAllFinished;
4    
5unsigned long _totalCount;
```

Simply, it use memory order and atomic operations to achieve lock-free concurrency and improving efficiency.

## ImageLoader

ImageLoader is the default implementation of the `SDImageLoader` protocol, which provides HTTP / HTTPS / FTP or local URL NSURLSession source image acquisition capabilities. And it also maximizes the configurability of the entire download process. Main interface as fellow:

```objective
 1@interface SDWebImageDownloader : NSObject
 2
 3@property (nonatomic, copy, readonly, nonnull) SDWebImageDownloaderConfig *config;
 4@property (nonatomic, strong, nullable) id<SDWebImageDownloaderRequestModifier> requestModifier;
 5@property (nonatomic, strong, nullable) id<SDWebImageDownloaderResponseModifier> responseModifier;
 6@property (nonatomic, strong, nullable) id<SDWebImageDownloaderDecryptor> decryptor;
 7/* ... */
 8
 9-(nullable SDWebImageDownloadToken *)downloadImageWithURL:(nullable NSURL *)url
10    options:(SDWebImageDownloaderOptions)options
11    context:(nullable SDWebImageContext *)context
12   progress:(nullable SDWebImageDownloaderProgressBlock)progressBlock
13  completed:(nullable SDWebImageDownloaderCompletedBlock)completedBlock;
14
15@end
```

the **downloaderConfig** supports the NSCopy protocol, below is the main configurations provided:

```objective
 1/// The maximum number of concurrent downloads.
 2@property (nonatomic, assign) NSInteger maxConcurrentDownloads;
 3/// The timeout value (in seconds) for each download operation.
 4@property (nonatomic, assign) NSTimeInterval downloadTimeout;
 5/// The session configuration, it's immutable after the downloader instance initialized. 
 6@property (nonatomic, strong, nullable) NSURLSessionConfiguration *sessionConfiguration;
 7/// Passing `NSOperation<SDWebImageDownloaderOperation>` to set as default. Passing `nil` will revert to `SDWebImageDownloaderOperation`.
 8@property (nonatomic, assign, nullable) Class operationClass;
 9/// The download operations execution order, default is FIFO
10@property (nonatomic, assign) SDWebImageDownloaderExecutionOrder executionOrder;
```

the **requestModifier**, provide modification before download request,

```objective
1/// Modify the original URL request and return a new one instead. You can modify the HTTP header, cachePolicy, etc for this URL.
2@protocol SDWebImageDownloaderRequestModifier <NSObject>
3   
4- (nullable NSURLRequest *)modifiedRequestWithRequest:(nonnull NSURLRequest *)request;
5
6@end
```

Similarly, the **responseModifier** provides modification of the return value,

```objective
1/// Modify the original URL response and return a new response. You can use this to check MIME-Type, mock server response, etc.
2
3@protocol SDWebImageDownloaderResponseModifier <NSObject>
4
5- (nullable NSURLResponse *)modifiedResponseWithResponse:(nonnull NSURLResponse *)response;
6
7@end
```

The last **decryptor** is used for image decryption, which provides base64 conversion of imageData by default.

```objective
1/// Decrypt the original download data and return a new data. You can use this to decrypt the data using your perfereed algorithm.
2@protocol SDWebImageDownloaderDecryptor <NSObject>
3
4- (nullable NSData *)decryptedDataWithData:(nonnull NSData *)data response:(nullable NSURLResponse *)response;
5
6@end
```

Processing data through these protocolded objects origins the **[strategy pattern](https://www.wikiwand.com/en/Strategy_pattern)**. By obtaining the protocol object through configuration, the caller only needs to care about the method provided by the protocol object, and does not need to care about its internal implementation to achieve the purpose of decoupling.

###DownloadImageWithURL

Before downloading, check whether the URL exists.

If not, directly throw an error and return. After getting the URL, try to reuse the operation generated before:

```objective
1NSOperation<SDWebImageDownloaderOperation> *operation = [self.URLOperations objectForKey:url];
```

If operation exists, call

```objective
1@synchronized (operation) {
2    downloadOperationCancelToken = [operation addHandlersForProgress:progressBlock completed:completedBlock];
3}
```

And set the queuePriority. Here the `@synchronized (operation)` is used to compare the `@synchronized (self)`, which is used inside the operation to ensure the thread safety of the operation between two different classes. Because the operation may be passed to the decoding or proxy queue.

Then `addHandlersForProgres` method will save progressBlock and completedBlock into `NSMutableDictionary <NSString *, id> SDCallbacksDictionary` and then return and save it into downloadOperationCancelToken.

In addition, operation in `addHandlersForProgress` method does not clear the previous stored callbacks. They are saved increamently, which means that all the callBacks will be executed in sequence after download completion.

If the operation is nil、isFinished or isCancelled will call `createDownloaderOperationWithUrl:options:context:` to create a new operation and store it in URLOperations and configure completionBlock. So that URLOperations can be cleared when the task is completed. Then call `addHandlersForProgress:completed:` to save progressBlock and completedBlock. At last submit operation to the downloadQueue.

The final operation, url, request, and downloadOperationCancelToken are packaged into **SDWebImageDownloadToken**, which the end of the download task.

###CreateDownloaderOperation

After downloading, let’s talk about how the operation is created. The first is to generate a URLRequest:

```objective
1// In order to prevent from potential duplicate caching (NSURLCache + SDImageCache) we disable the cache for image requests if told otherwise
2NSURLRequestCachePolicy cachePolicy = options & SDWebImageDownloaderUseNSURLCache ? NSURLRequestUseProtocolCachePolicy : NSURLRequestReloadIgnoringLocalCacheData;
3NSMutableURLRequest *mutableRequest = [[NSMutableURLRequest alloc] initWithURL:url cachePolicy:cachePolicy timeoutInterval:timeoutInterval];
4mutableRequest.HTTPShouldHandleCookies = SD_OPTIONS_CONTAINS(options, SDWebImageDownloaderHandleCookies);
5mutableRequest.HTTPShouldUsePipelining = YES;
6SD_LOCK(self.HTTPHeadersLock);
7mutableRequest.allHTTPHeaderFields = self.HTTPHeaders;
8SD_UNLOCK(self.HTTPHeadersLock);
```

It is mainly configured by obtaining parameters through SDWebImageDownloaderOptions. The timeout is determined by downloader’s `config.downloadTimeout`, the default is 15s.

Then remove `id <SDWebImageDownloaderRequestModifier> requestModifier` from imageContext to transform the request.

```objective
1// Request Modifier
2id<SDWebImageDownloaderRequestModifier> requestModifier;
3if ([context valueForKey:SDWebImageContextDownloadRequestModifier]) {
4    requestModifier = [context valueForKey:SDWebImageContextDownloadRequestModifier];
5} else {
6    requestModifier = self.requestModifier;
7}
```

What you need to pay attention to is that the access to requestModifier has **priority**, and the priority obtained through imageContext is higher than the downloader. This kind of method not only satisfies the controllability of the caller, but also supports the global configuration, which is suitable for all ages.

Similarly, `id <SDWebImageDownloaderResponseModifier> responseModifier` and` id <SDWebImageDownloaderDecryptor> decryptor` are also the same approach.

After that, the confirmed responseModifier and decryptor will be saved in imageContext again for later use.

Finally, remove operationClass from downloaderConfig to create operation:

```objective
1Class operationClass = self.config.operationClass;
2if (operationClass && [operationClass isSubclassOfClass:[NSOperation class]] && [operationClass conformsToProtocol:@protocol(SDWebImageDownloaderOperation)]) {
3    // Custom operation class
4} else {
5    operationClass = [SDWebImageDownloaderOperation class];
6}
7NSOperation<SDWebImageDownloaderOperation> *operation = [[operationClass alloc] initWithRequest:request inSession:self.session options:options context:context];
```

Set the _credential, minimumProgressInterval, queuePriority, pendingOperation_.

By default, each task is added to the downloadQueue in FIFO order. If you set it as LIFO, the task priority will be modified before adding to the queue:

```objective
1if (self.config.executionOrder == SDWebImageDownloaderLIFOExecutionOrder) {
2    // Emulate LIFO execution order by systematically, each previous adding operation can dependency the new operation
3    // This can gurantee the new operation to be execulated firstly, even if when some operations finished, meanwhile you appending new operations
4    // Just make last added operation dependents new operation can not solve this problem. See test case #test15DownloaderLIFOExecutionOrder
5    for (NSOperation *pendingOperation in self.downloadQueue.operations) {
6        [pendingOperation addDependency:operation];
7    }
8}
```

###Data Processing

SDWebImageDownloaderOperation is also a protocolization class, which confirm NSURLSessionTaskDelegate, NSURLSessionDataDelegate. It handles URL request data, supports background downloading, supports responseData modification (by responseModifier), and supports download ImageData decryption (by decryptor). The main internal properties are as follows:

```objective
 1@property (assign, nonatomic, readwrite) SDWebImageDownloaderOptions options;
 2@property (copy, nonatomic, readwrite, nullable) SDWebImageContext *context;
 3@property (strong, nonatomic, nonnull) NSMutableArray<SDCallbacksDictionary *> *callbackBlocks;
 4
 5@property (strong, nonatomic, nullable) NSMutableData *imageData;
 6@property (copy, nonatomic, nullable) NSData *cachedData; // for `SDWebImageDownloaderIgnoreCachedResponse`
 7@property (assign, nonatomic) NSUInteger expectedSize; // may be 0
 8@property (assign, nonatomic) NSUInteger receivedSize;
 9
10@property (strong, nonatomic, nullable) id<SDWebImageDownloaderResponseModifier> responseModifier; // modifiy original URLResponse
11@property (strong, nonatomic, nullable) id<SDWebImageDownloaderDecryptor> decryptor; // decrypt image data
12// This is weak because it is injected by whoever manages this session. If this gets nil-ed out, we won't be able to run
13// the task associated with this operation
14@property (weak, nonatomic, nullable) NSURLSession *unownedSession;
15// This is set if we're using not using an injected NSURLSession. We're responsible of invalidating this one
16@property (strong, nonatomic, nullable) NSURLSession *ownedSession;
17
18@property (strong, nonatomic, nonnull) dispatch_queue_t coderQueue; // the queue to do image decoding
19#if SD_UIKIT
20@property (assign, nonatomic) UIBackgroundTaskIdentifier backgroundTaskId;
21
22- (nonnull instancetype)initWithRequest:(nullable NSURLRequest *)request
23                              inSession:(nullable NSURLSession *)session
24                                options:(SDWebImageDownloaderOptions)options
25                                context:(nullable SDWebImageContext *)context;
```

There is nothing special about initialization. You should noted that the `nullable session` passed here is saved with unownedSessin, which is different from the **ownedSession** generated by default internally. If the session is empty during initialization, the ownedSession will be created at `start`.

Then the problem is coming, because we need to observe the various states of the session, we need to set up the delegate.

```objective
1[NSURLSession sessionWithConfiguration:delegate:delegateQueue:];
```

The delegate of the ownedSession is undoubtedly inside the operation, while the delegate of unownedSessin is the downloader. It will retrieve the operation through taskID and forwarding of the callback through the operation’s delegate. Here is the code:

```objective
1- (void)URLSession:(NSURLSession *)session task:(NSURLSessionTask *)task didCompleteWithError:(NSError *)error {
2    
3    // Identify the operation that runs this task and pass it the delegate method
4    NSOperation<SDWebImageDownloaderOperation> *dataOperation = [self operationWithTask:task];
5    if ([dataOperation respondsToSelector:@selector(URLSession:task:didCompleteWithError:)]) {
6        [dataOperation URLSession:session task:task didCompleteWithError:error];
7    }
8}
```

Then, as a real consumer operation trigger the download task. The entire download process including start, end, and cancellation will send corresponding notifications.

1. In **didReceiveResponse**, `response.expectedContentLength` will be saved as expectedSize. Then call `modifiedResponseWithResponse:` to save the edited response.
2. Every time **didReceiveData** will append data to imageData: `[self.imageData appendData: data]`, update receivedSize`self.receivedSize = self.imageData.length`. Finally, when receivedSize bigger then expectedSize, which means the download task is completed, and move to the next stage. If you support `SDWebImageDownloaderProgressiveLoad`, you will be able to decoding while downloading in coderQueue:

```objective
 1// progressive decode the image in coder queue
 2dispatch_async(self.coderQueue, ^{
 3    @autoreleasepool {
 4        UIImage *image = SDImageLoaderDecodeProgressiveImageData(imageData, self.request.URL, finished, self, [[self class] imageOptionsFromDownloaderOptions:self.options], self.context);
 5        if (image) {
 6            // We do not keep the progressive decoding image even when `finished`=YES. Because they are for view rendering but not take full function from downloader options. And some coders implementation may not keep consistent between progressive decoding and normal decoding.
 7            
 8            [self callCompletionBlocksWithImage:image imageData:nil error:nil finished:NO];
 9        }
10    }
11});
```

​ Otherwise, the decoding operation will be completed when **didCompleteWithError**: `SDImageLoaderDecodeImageData`, but you need to decrypt it before decoding:

```objective
1if (imageData && self.decryptor) {
2    imageData = [self.decryptor decryptedDataWithData:imageData response:self.response];
3}
```

​ 3. Handle the complete callback;

_We will talk about the logic of decode finally._

## ImageCache

The design of Cache classes are consistent with the ImageLoader. There will be a **SDImageCacheConfig** to configure the cache expiration time, capacity, read and write permissions, and dynamically MemoryCache / DiskCache class.

The main properties of SDImageCacheConfig are as follows:

```objective
 1@property (assign, nonatomic) BOOL shouldDisableiCloud;
 2@property (assign, nonatomic) BOOL shouldCacheImagesInMemory;
 3@property (assign, nonatomic) BOOL shouldUseWeakMemoryCache;
 4@property (assign, nonatomic) BOOL shouldRemoveExpiredDataWhenEnterBackground;
 5@property (assign, nonatomic) NSDataReadingOptions diskCacheReadingOptions;
 6@property (assign, nonatomic) NSDataWritingOptions diskCacheWritingOptions;
 7@property (assign, nonatomic) NSTimeInterval maxDiskAge;
 8@property (assign, nonatomic) NSUInteger maxDiskSize;
 9@property (assign, nonatomic) NSUInteger maxMemoryCost;
10@property (assign, nonatomic) NSUInteger maxMemoryCount;
11@property (assign, nonatomic) SDImageCacheConfigExpireType diskCacheExpireType;
12/// Defaults to built-in `SDMemoryCache` class.
13@property (assign, nonatomic, nonnull) Class memoryCacheClass;
14/// Defaults to built-in `SDDiskCache` class.
15@property (assign ,nonatomic, nonnull) Class diskCacheClass;
```

MemoryCache and DiskCache instantiation depends on SDImageCacheConfig:

```objective
1/// SDMemoryCache
2- (nonnull instancetype)initWithConfig:(nonnull SDImageCacheConfig *)config;
3/// SDDiskCache
4- (nullable instancetype)initWithCachePath:(nonnull NSString *)cachePath config:(nonnull SDImageCacheConfig *)config;
```

As a cache protocol, their interface declarations are basically the same, all of which are CURD for data. The difference is that MemoryCache Protocl operates on the **id** type (NSCache’s limitation), and DiskCache is on NSData.

### SDMemoryCache

```objective
1/**
2 A memory cache which auto purge the cache on memory warning and support weak cache.
3 */
4@interface SDMemoryCache <KeyType, ObjectType> : NSCache <KeyType, ObjectType> <SDMemoryCache>
5
6@property (nonatomic, strong, nonnull, readonly) SDImageCacheConfig *config;
7
8@end
```

Internally, **NSCache** is the implementation for SDMemoryCache, and add **NSMapTable \<KeyType, ObjectType\> * weakCache** property, which use semaphore lock to ensure thread safety. The weak-cache is a feature added only on the _iOS / tvOS_ platform, because on macOS, NSCache will not clear the corresponding cache, when receiving system memory warning. WeakCache uses strong-weak references without additional memory overhead and does not affect the life cycle of the object.

The role of weakCache is to restore the cache. It is controlled by the **shouldUseWeakMemoryCache** switch of CacheConfig. For details, you can check the [CacheConfig](https://github.com/SDWebImage/SDWebImage/blob/master/SDWebImage/Core/SDImageCacheConfig.h).

First, look at how _objectForKey_ is implemented:

```objective
 1- (id)objectForKey:(id)key {
 2    id obj = [super objectForKey:key];
 3    if (!self.config.shouldUseWeakMemoryCache) {
 4        return obj;
 5    }
 6    if (key && !obj) {
 7        // Check weak cache
 8        SD_LOCK(self.weakCacheLock);
 9        obj = [self.weakCache objectForKey:key];
10        SD_UNLOCK(self.weakCacheLock);
11        if (obj) {
12            // Sync cache
13            NSUInteger cost = 0;
14            if ([obj isKindOfClass:[UIImage class]]) {
15                cost = [(UIImage *)obj sd_memoryCost];
16            }
17            [super setObject:obj forKey:key cost:cost];
18        }
19    }
20    return obj;
21}
```

Since NSCache follows [`NSDiscardableContent`](apple-reference-documentation://hcnVx1bA-q) to store temporary objects. When the memory is tight, the cached objects may be cleaned up by the system. At this time, once the application accesses MemoryCache and the cache missing, which will be transferred to the diskCache query operation. And that may cause the image to flicker. And when shouldUseWeakMemoryCache is true, because weakCache holds the weak reference of the object (when the object is cleaned by NSCache but not released), we can get the cache by weakCache and stuff it into NSCache, which will reduces disk I/O.

### SDDiskCache

This is simpler, internally uses NSFileManager to manage the reading and writing of image data, and calls SDDiskCacheFileNameForKey to process the key MD5 as fileName and store it in the diskCachePath directory. The other is to clear the expired cache:

1. Sort by SDImageCacheConfigExpireType to get `NSDirectoryEnumerator * fileEnumerator` and start filtering;
2. Use `cacheConfig.maxDiskAage` to determine whether it is expired, and store the expired URL in urlsToDelete;
3. Call `[self.fileManager removeItemAtURL: fileURL error: nil];`
4. According to `cacheConfig.maxDiskSize` to delete the data cached on the disk, clean up to 1/2 of maxDiskSize.

By the way, SDDiskCache, like **[YYKVStorage](https://github.com/ibireme/YYCache/blob/master/YYCache/YYKVStorage.h)**, also supports adding extendData to UIImage to store additional information, for example, the zoom ratio of the picture, [URL rich link](https://sspai.com/post/55279), time And other data.

However, **YYKVStorage** store the extended_data field by the _**manifest**_ table in the database. SDDiskCache solution is a different way, by use system API \<sys/xattr.h\> **setxattr**, **getxattr**, **listxattr** to save extendData, which is really amazing. One more thing, the corresponding key is _SDDiskCacheExtendedAttributeName_.

### SDImageCache

It is also a protocold class, which is responsible for scheduling SDMemoryCache and SDDiskCache, and its Properties are as follows:

```objective
1@property (nonatomic, strong, readwrite, nonnull) id<SDMemoryCache> memoryCache;
2@property (nonatomic, strong, readwrite, nonnull) id<SDDiskCache> diskCache;
3@property (nonatomic, copy, readwrite, nonnull) SDImageCacheConfig *config;
4@property (nonatomic, copy, readwrite, nonnull) NSString *diskCachePath;
5@property (nonatomic, strong, nullable) dispatch_queue_t ioQueue;
```

> Note: The memoryCache and diskCache instances are generated according to the class defined in CacheConfig, and the defaults are SDMemoryCache and SDDiskCache.

Let’s take a look at its core method:

```objective
1- (void)storeImage:(nullable UIImage *)image
2         imageData:(nullable NSData *)imageData
3            forKey:(nullable NSString *)key
4          toMemory:(BOOL)toMemory
5            toDisk:(BOOL)toDisk
6        completion:(nullable SDWebImageNoParamsBlock)completionBlock;
```

1. Make sure that image and key exist;
2. When **shouldCacheImagesInMemory** is YES, it calls `[self.memoryCache setObject:image forKey:key cost:cost]` to write memoryCache;
3. Write diskCache, put the operation logic into ioQueue and autoreleasepool.

  ```objective
   1dispatch_async(self.ioQueue, ^{
   2    @autoreleasepool {
   3        NSData *data = ... // 根据 SDImageFormat 对 image 进行编码获取
   4        /// data = [[SDImageCodersManager sharedManager] encodedDataWithImage:image format:format options:nil];
   5        [self _storeImageDataToDisk:data forKey:key];
   6        if (image) {
   7            // Check extended data
   8            id extendedObject = image.sd_extendedObject;
   9            // ... get extended data
  10            [self.diskCache setExtendedData:extendedData forKey:key];
  11        }
  12    }
  13    // call completionBlock in main queue
  14});
  ```

Another important method is image query, which is defined in the SDImageCache protocol:

```objective
 1- (id<SDWebImageOperation>)queryImageForKey:(NSString *)key options:(SDWebImageOptions)options context:(nullable SDWebImageContext *)context completion:(nullable SDImageCacheQueryCompletionBlock)completionBlock {
 2    SDImageCacheOptions cacheOptions = 0;
 3    if (options & SDWebImageQueryMemoryData) cacheOptions |= SDImageCacheQueryMemoryData;
 4    if (options & SDWebImageQueryMemoryDataSync) cacheOptions |= SDImageCacheQueryMemoryDataSync;
 5    if (options & SDWebImageQueryDiskDataSync) cacheOptions |= SDImageCacheQueryDiskDataSync;
 6    if (options & SDWebImageScaleDownLargeImages) cacheOptions |= SDImageCacheScaleDownLargeImages;
 7    if (options & SDWebImageAvoidDecodeImage) cacheOptions |= SDImageCacheAvoidDecodeImage;
 8    if (options & SDWebImageDecodeFirstFrameOnly) cacheOptions |= SDImageCacheDecodeFirstFrameOnly;
 9    if (options & SDWebImagePreloadAllFrames) cacheOptions |= SDImageCachePreloadAllFrames;
10    if (options & SDWebImageMatchAnimatedImageClass) cacheOptions |= SDImageCacheMatchAnimatedImageClass;
11    
12    return [self queryCacheOperationForKey:key options:cacheOptions context:context done:completionBlock];
13}
```

**queryImageForKey** converts SDWebImageOptions to SDImageCacheOptions, then call `queryCacheOperationForKey:`, which logic is as follows:

First, First, if the query key exists, the transformer will be obtained from the imageContext and the query key will be converted:

```objective
1key = SDTransformedKeyForKey(key, transformerKey);
```

Try to get the image from the memory cache, if it exists:

1. If SDImageCacheDecodeFirstFrameOnly is satisfied and comforts to SDAnimatedImage protocol, CGImage will be taken out for conversion

  ```objective
  1// Ensure static image
  2Class animatedImageClass = image.class;
  3if (image.sd_isAnimated || ([animatedImageClass isSubclassOfClass:[UIImage class]] && [animatedImageClass conformsToProtocol:@protocol(SDAnimatedImage)])) {
  4#if SD_MAC
  5    image = [[NSImage alloc] initWithCGImage:image.CGImage scale:image.scale orientation:kCGImagePropertyOrientationUp];
  6#else
  7    image = [[UIImage alloc] initWithCGImage:image.CGImage scale:image.scale orientation:image.imageOrientation];
  8#endif
  9}
  ```
2. If SDImageCacheMatchAnimatedImageClass is satisfied, it will be forced to check whether the image type matches, otherwise the data will be nil:

  ```objective
  1// Check image class matching
  2Class animatedImageClass = image.class;
  3Class desiredImageClass = context[SDWebImageContextAnimatedImageClass];
  4if (desiredImageClass && ![animatedImageClass isSubclassOfClass:desiredImageClass]) {
  5    image = nil;
  6}
  ```

When the image can be obtained from the memory cache and is SDImageCacheQueryMemoryData, return directly, otherwise continue;

Start reading diskCache, and use shouldQueryDiskSync to specify query cache sync/async behavior.

```objective
1// Check whether we need to synchronously query disk
2// 1. in-memory cache hit & memoryDataSync
3// 2. in-memory cache miss & diskDataSync
4BOOL shouldQueryDiskSync = ((image && options & SDImageCacheQueryMemoryDataSync) ||
5                            (!image && options & SDImageCacheQueryDiskDataSync));
```

The entire diskQuery is stored in queryDiskBlock and wrapped with autorelease:

```objective
 1void(^queryDiskBlock)(void) =  ^{
 2    if (operation.isCancelled) {
 3        // call doneBlock & return
 4    }
 5    @autoreleasepool {
 6        NSData *diskData = [self diskImageDataBySearchingAllPathsForKey:key];
 7        UIImage *diskImage;
 8        SDImageCacheType cacheType = SDImageCacheTypeNone;
 9        if (image) {
10            // the image is from in-memory cache, but need image data
11            diskImage = image;
12            cacheType = SDImageCacheTypeMemory;
13        } else if (diskData) {
14            cacheType = SDImageCacheTypeDisk;
15            // decode image data only if in-memory cache missed
16            diskImage = [self diskImageForKey:key data:diskData options:options context:context];
17            if (diskImage && self.config.shouldCacheImagesInMemory) {
18                NSUInteger cost = diskImage.sd_memoryCost;
19                [self.memoryCache setObject:diskImage forKey:key cost:cost];
20            }
21        }
22        // call doneBlock
23        if (doneBlock) {
24            if (shouldQueryDiskSync) {
25                doneBlock(diskImage, diskData, cacheType);
26            } else {
27                dispatch_async(dispatch_get_main_queue(), ^{
28                    doneBlock(diskImage, diskData, cacheType);
29                });
30            }
31        }
32    }
33}
```

For large amounts of temporary memory operations, SD will put it into autoreleasepool to ensure that the memory can be released in time.

**Special emphasis**, once the code is executed here, there must be disk querying operations, so if you don’t have to get imageData, you can use **SDImageCacheQueryMemoryData** to improve query efficiency.

One more thing, the conversion logic of `SDTransformedKeyForKey` is the transformerKey of **SDImageTransformer**, which is spliced behind the image key in order. E.g:

```objective
1'image.png' |> flip(YES,NO) |> rotate(pi/4,YES)  => 
2'image-SDImageFlippingTransformer(1,0)-SDImageRotationTransformer(0.78539816339,1).png'
```

## SDImageManaer

SDImageManger serves as the dispatch center of the entire library, who is the master of the above various logics. It connects the components in series, from View \> Downloading \> Decodering \> Cache. The only core method it exposes is **loadImage**:

```objective
 1@property (strong, nonatomic, readonly, nonnull) id<SDImageCache> imageCache;
 2@property (strong, nonatomic, readonly, nonnull) id<SDImageLoader> imageLoader;
 3@property (strong, nonatomic, nullable) id<SDImageTransformer> transformer;
 4@property (nonatomic, strong, nullable) id<SDWebImageCacheKeyFilter> cacheKeyFilter;
 5@property (nonatomic, strong, nullable) id<SDWebImageCacheSerializer> cacheSerializer;
 6@property (nonatomic, strong, nullable) id<SDWebImageOptionsProcessor> optionsProcessor;
 7
 8@property (nonatomic, class, nullable) id<SDImageCache> defaultImageCache;
 9@property (nonatomic, class, nullable) id<SDImageLoader> defaultImageLoader;
10
11- (nullable SDWebImageCombinedOperation *)loadImageWithURL:(nullable NSURL *)url
12                                                   options:(SDWebImageOptions)options
13                                                   context:(nullable SDWebImageContext *)context
14                                                  progress:(nullable SDImageLoaderProgressBlock)progressBlock
15                                                 completed:(nonnull SDInternalCompletionBlock)completedBlock;
```

Let’s briefly talk about the three left APIs cacheKeyFilter, cacheSerializer and optionsProcessor, the rest of which have been mentioned above.

**SDWebImageCacheKeyFilter**

By default, the `URL.absoluteString` is used as cacheKey, and if fileter is set, cacheKey will be replaced by `cacheKeyForURL:`;

**SDWebImageCacheSerializer**

By default, ImageCache will directly cache downloadData, and when we use other image formats for transmission, such as WEBP format, then the data with WEBP format will be storaged to the disk directly. This will cause a problem, every time when we query the image from the disk, we have to repeat the decoding operation. The CacheSerializer can directly convert downloadData to JPEG / PNG format NSData cache, thereby improving access efficiency.

**SDWebImageOptionsProcessor**

Used to control the global parameters in SDWebImageOptions and SDWebImageContext. E.g::

```objective
 1SDWebImageManager.sharedManager.optionsProcessor = [SDWebImageOptionsProcessor optionsProcessorWithBlock:^SDWebImageOptionsResult * _Nullable(NSURL * _Nullable url, SDWebImageOptions options, SDWebImageContext * _Nullable context) {
 2     // Only do animation on `SDAnimatedImageView`
 3     if (!context[SDWebImageContextAnimatedImageClass]) {
 4        options |= SDWebImageDecodeFirstFrameOnly;
 5     }
 6     // Do not force decode for png url
 7     if ([url.lastPathComponent isEqualToString:@"png"]) {
 8        options |= SDWebImageAvoidDecodeImage;
 9     }
10     // Always use screen scale factor
11     SDWebImageMutableContext *mutableContext = [NSDictionary dictionaryWithDictionary:context];
12     mutableContext[SDWebImageContextImageScaleFactor] = @(UIScreen.mainScreen.scale);
13     context = [mutableContext copy];
14 
15     return [[SDWebImageOptionsResult alloc] initWithOptions:options context:context];
16 }];
```

### LoadImage

The first parameter of the method, the **url**, which serves as the connection core of SD, was designed to be nullable. This design may be for the convenience of users. Internally through the nil judgment of the url and the compatibility with the NSString type (forced conversion to NSURL) to ensure the subsequent process, otherwise the call ends.

After the download started, it was split into the following 6 methods:

- callCacheProcessForOperation
- callDownloadProcessForOperation
- callStoreCacheProcessForOperation
- callTransformProcessForOperation
- callCompletionBlockForOperation
- safelyRemoveOperationFromRunning

They are cache query, download, storage, conversion, execution callback, and cleanup callback. You can find that each method is delivered through the operation, which will be ready when the loadImage is loaded, then trigger the cache query.

```objective
 1SDWebImageCombinedOperation *operation = [SDWebImagCombinedOperation new];
 2operation.manager = self;
 3
 4///  1
 5BOOL isFailedUrl = NO;
 6if (url) {
 7    SD_LOCK(self.failedURLsLock);
 8    isFailedUrl = [self.failedURLs containsObject:url];
 9    SD_UNLOCK(self.failedURLsLock);
10}
11
12if (url.absoluteString.length == 0 || (!(options & SDWebImageRetryFailed) && isFailedUrl)) {
13    [self callCompletionBlockForOperation:operation completion:completedBlock error:[NSError errorWithDomain:SDWebImageErrorDomain code:SDWebImageErrorInvalidURL userInfo:@{NSLocalizedDescriptionKey : @"Image url is nil"}] url:url];
14    return operation;
15}
16
17SD_LOCK(self.runningOperationsLock);
18[self.runningOperations addObject:operation];
19SD_UNLOCK(self.runningOperationsLock);
20
21// 2. Preprocess the options and context arg to decide the final the result for manager
22SDWebImageOptionsResult *result = [self processedResultForURL:url options:options context:context];
```

The implementation of **loadImage** is relatively simple, and the core is to generate an operation then transfer it to a chache querey.

After the operation is initialized, it will checks whether failedURLs contains the current url:

- If yes, and options is SDWebImageRetryFailed, directly return operation and retun;
- If pass, the operation will be stored in `runningOperations`. Enclose options and imageContext in **SDWebImageOptionsResult**.

then will update imageContext, mainly store the transformer, cacheKeyFilter, cacheSerializer as the global default setting, and then call **optionsProcessor** to fulfill user’s custom options to modify imageContext again.

If you see here from the front, you should have an impression of this routine. The priority logic of requestModifer in the previous ImageLoader is similar to this, but the implementation is somewhat different. Finally, transfer to CacheProcess.

The operation of **loadImage** is a combineOperation, which is a combination of cache and loader operation tasks, so that it can clean up the cache query and download tasks in one step. The statement is as follows:

```objective
1@interface SDWebImageCombinedOperation : NSObject <SDWebImageOperation>
2/// imageCache queryImageForKey: 的 operation
3@property (strong, nonatomic, nullable, readonly) id<SDWebImageOperation> cacheOperation;
4/// imageLoader requestImageWithURL: 的 operation
5@property (strong, nonatomic, nullable, readonly) id<SDWebImageOperation> loaderOperation;
6/// Cancel the current operation, including cache and loader process
7- (void)cancel;
8@end
```

The cancel method provided by it will gradually check two types of opration and then call the cancel operation one by one.

####CallCacheProcessForOperation

First check the value of **SDWebImageFromLoaderOnly** to determine whether need to start the download task directly.

If yes, forward to downloadProcess.

Otherwise, create a query task through `imageCache` and save it to combineOperation’s cacheOperation:

```objective
1operation.cacheOperation = [self.imageCache queryImageForKey:key options:options context:context completion:^(UIImage * _Nullable cachedImage, NSData * _Nullable cachedData, SDImageCacheType cacheType) {
2   if (!operation || operation.isCancelled) {
3    	/// 1  
4   }
5  	/// 2
6}];
```

There are two situations that need to be handled for the results of the cache query:

1. When the operation is executing in the queue and operaton was marked as canceled, will end the donwload task;
2. Otherwise, forward to downloadProcess.

####CallDownloadProcessForOperation

The most complex of the 6 methods. First, We need to decide whether we need to create a new download task, which is controlled by three variables:

```objective
1BOOL shouldDownload = !SD_OPTIONS_CONTAINS(options, SDWebImageFromCacheOnly);
2    shouldDownload &= (!cachedImage || options & SDWebImageRefreshCached);
3    shouldDownload &= (![self.delegate respondsToSelector:@selector(imageManager:shouldDownloadImageForURL:)] || [self.delegate imageManager:self shouldDownloadImageForURL:url]);
4    shouldDownload &= [self.imageLoader canRequestImageForURL:url];
```

- check options value is set as SDWebImageFromCacheOnly or SDWebImageRefreshCached;
- check the delegate method **shouldDownloadImageForURL** value;
- check whether the imageLoader **canRequestImageForURL**;

1. If shouldDownload is NO, close the download task. And perform **callCompletionBlockForOperation** and**safelyRemoveOperationFromRunning**. By the way, if cacheImage exists, it will be returned with completionBlock.
2. If shouldDownload is YES, create a new download task and save it in combineOperation’s loaderOperation. Before creating a new task, if cacheImage exist and SDWebImageRefreshCached is set, the cacheImage will be stored in imageContext (if not will create a imageContext).
3. After downloading, return to callBack, there are several situations to deal with:

    - If the operation is canceled, the downloaded image and data will be discarded. And call the completion block and close the download task ;
    - Error caused by reqeust is cacneled, call the completion block and close the download task ;
    - Image refresh hit the NSURLCache cache, do not call the completion block;
    - errro, **callCompletionBlockForOperation** and add url to failedURLs;
    - None of the above conditions, if successful by retry, will remove the url from failedURLs first, call **storeCacheProcess**;

Finally, call the **safelyRemoveOperation** for operation which marked as finished;

####CallStoreCacheProcessForOperation

Pour out storeCacheType、originalStoreCacheType、transformer、cacheSerializer from imageContext.

Check if it is necessary to store the converted image data, original data, and wait for the end of the cache storage:

```objective
1BOOL shouldTransformImage = downloadedImage && (!downloadedImage.sd_isAnimated || (options & SDWebImageTransformAnimatedImage)) && transformer;
2BOOL shouldCacheOriginal = downloadedImage && finished;
3BOOL waitStoreCache = SD_OPTIONS_CONTAINS(options, SDWebImageWaitStoreCache);
```

If shouldCacheOriginal is NO, directly transfer to **transformProcess**. Otherwise, first confirm whether the storage type is the original data:

```objective
1// normally use the store cache type, but if target image is transformed, use original store cache type instead
2SDImageCacheType targetStoreCacheType = shouldTransformImage ? originalStoreCacheType : storeCacheType;
```

If cacheSerializer exists during storage, it will first convert the data format, and finally call `[self stroageImage: ...]`

When the storage is over, go to the last step, **transformProcess**.

####CallTransformProcessForOperation

Before the conversion starts, it will routinely judge whether it needs to be converted.

```objective
1id<SDImageTransformer> transformer = context[SDWebImageContextImageTransformer];
2id<SDWebImageCacheSerializer> cacheSerializer = context[SDWebImageContextCacheSerializer];
3BOOL shouldTransformImage = originalImage && (!originalImage.sd_isAnimated || (options & SDWebImageTransformAnimatedImage)) && transformer;
4BOOL waitStoreCache = SD_OPTIONS_CONTAINS(options, SDWebImageWaitStoreCache);
```

If conversion is required, it will enter the global queue to start processing:

```objective
 1dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_HIGH, 0), ^{
 2    @autoreleasepool {
 3        UIImage *transformedImage = [transformer transformedImageWithImage:originalImage forKey:key];
 4        if (transformedImage && finished) {
 5				/// 1
 6        } else {
 7				callCompletionBlock
 8        }
 9    }
10});        
```

After the conversion is successful, the image will be stored according to

```objective
1cacheData = [cacheSerializer cacheDataWithImage: originalData: imageURL:];
```

After storing, call completion block. The end.

## The End

I am honored that you can reach here. I hope you can get a general understanding of the work-flow of SD, as well as some details of processing and thinking. In SD 5.x, the most personal feeling is that the design of its architecture is worth learning.

- How to design a stable and extensible API that can safely support dynamic parameter addition?
- How to design a decoupled and dynamically pluggable architecture?

Finally, this article actually lacks **SDImageCoder**, which will be left for the next SDWebImage plugin and its extension.
