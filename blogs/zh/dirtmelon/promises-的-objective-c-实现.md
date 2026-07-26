---
title: Promises 的 Objective-C 实现
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/promise-second/'
original_language: zh
published: 2021-11-28
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a8a56278ab475fe7'
translated: n/a
---

> 原文：[Promises 的 Objective-C 实现](https://dirtmelon.github.io/posts/promise-second/)　·　dirtmelon

[https://github.com/google/promises](https://github.com/google/promises) 是 Google 开源的 Promise 库，支持 Objective-C 和 Swift ， podspec 分为 [PromisesObjC.podspec](https://github.com/google/promises/blob/master/PromisesObjC.podspec) 和 [PromisesSwift.podspec](https://github.com/google/promises/blob/master/PromisesSwift.podspec) ，可以看到 PromisesSwift.podspec 的 dependency 为 PromisesObjC 。下面会从 Promises 的 Objective-C 版基础用法开始解析源码。

## 创建 Promises

`PromiseState` 的定义：

```objectivec
typedef NS_ENUM(NSInteger, FBLPromiseState) {
  FBLPromiseStatePending = 0,
  FBLPromiseStateFulfilled,
  FBLPromiseStateRejected,
};
```

`FBLPromiseObserver` 则定义了 Observer 的相关 block ：

```objectivec
typedef void (^FBLPromiseObserver)(FBLPromiseState state, id __nullable resolution);
```

`gFBLPromiseDefaultDispatchQueue` 是默认的处理队列，在 `FBLPromise` 的 `initialize` 方法中进行初始化：

```objectivec
+ (void)initialize {
  if (self == [FBLPromise class]) {
    gFBLPromiseDefaultDispatchQueue = dispatch_get_main_queue();
  }
}
```

`FBLPromise` 在 `initialize` 方法中对 `gFBLPromiseDefaultDispatchQueue` 进行初始化，这样就可以在 `FBLPromise` 第一次调用方法前就自动设置，至于为什么要判断 `self` 是否为 `FBLPromise class` ，可以看下 [initialize](https://www.notion.so/initialize-0b5c185c88b541028ed1c0132cfe62bb) 的解析。

`FBLPromise` 的对象属性如下：

```objectivec
@implementation FBLPromise {
  // Promise 当前的状态
  FBLPromiseState _state;
  // 对处理中的对象进行强引用，处理完之后会自动置 nil
  NSMutableSet *__nullable _pendingObjects;
  // fulfilled 时对应的值
  id __nullable _value;
  // rejected 时对应的 错误
  NSError *__nullable _error;
  // 对应的 Observers ，当 Promise 处理完之后就会调用
  NSMutableArray<FBLPromiseObserver> *_observers;
}
```

创建 Promises 有两种方式，一种是还没知道结果，依赖于后续的异步操作，一种是已经知道结果，是值或者错误。

`initPending` 是还没知道结果，依赖于后续异步操作的初始化方法： `(**instancetype**)initPending NS_SWIFT_UNAVAILABLE("")` ， `NS_SWIFT_UNAVAILABLE` 表明这个方法在 Swift 中是不可用的： [making_objective-c_apis_unavailable_in_swift](https://developer.apple.com/documentation/swift/objective-c_and_c_code_customization/making_objective-c_apis_unavailable_in_swift) 。

```objectivec
- (instancetype)initPending {
  self = [super init];
  if (self) {
    dispatch_group_enter(FBLPromise.dispatchGroup);
  }
  return self;
}
```

这里调用了一下 `dispatch_group_enter` ，但是整个库的实现并没有利用到 `dispatch_group` 的相关特性，这里之所以使用了 `dispatch_group` ，是为了方便测试，具体可以查看这里 https://github.com/google/promises/issues/13 的讨论。

`initWithResolution:` 则是初始化时就知道对应的结果，不依赖后续的异步操作：

```objectivec
- (instancetype)initWithResolution:(nullable id)resolution {
  self = [super init];
  if (self) {
    // 根据 resolution 是否为 NSError 进行区分
    if ([resolution isKindOfClass:[NSError class]]) {
      _state = FBLPromiseStateRejected;
      _error = (NSError *)resolution;
    } else {
      _state = FBLPromiseStateFulfilled;
      _value = resolution;
    }
  }
  return self;
}
```

同时为了方便调用，也通过 block 的方式来提供点语法的调用：

```objectivec
+ (instancetype (^)(void))pending {
  return ^(void) {
    return [self pendingPromise];
  };
}

+ (instancetype (^)(id __nullable))resolved {
  return ^(id resolution) {
    return [self resolvedWith:resolution];
  };
}
```

使用方式：

```objectivec
FBLPromise.pending()
FBLPromise.resolved(value)
```

`FBLPromise` 提供了 `fulfill:` 方法，可以在异步操作成功后处理对应的值：

```objectivec
- (void)fulfill:(nullable id)value {
  // 由于 value 是 id 类型，所以这里加多了个是否为 NSError 的判断
  if ([value isKindOfClass:[NSError class]]) {
    [self reject:(NSError *)value];
  } else {
    @synchronized(self) {
      // 只有是 FBLPromiseStatePending 状态才可以转换为 FBLPromiseStateFulfilled
      if (_state == FBLPromiseStatePending) {
        _state = FBLPromiseStateFulfilled;
        _value = value;
        _pendingObjects = nil;
        // 通知 Observers
        for (FBLPromiseObserver observer in _observers) {
          observer(_state, _value);
        }
        _observers = nil;
        dispatch_group_leave(FBLPromise.dispatchGroup);
      }
    }
  }
}
```

`FBLPromise` 为了线程安全，不少方法都加上了 `@synchronized(self)` ，性能上可能会有点差距。可以考虑使用下 `pthread_mutex` ，具体可以看 [Lock](https://www.notion.so/Lock-794065e788bb4741a870c4434323de5b) 的解析。

`FBLPromise` 也提供了 `reject:` 方法，异步操作可以在由错误生成时调用：

```objectivec
- (void)reject:(NSError *)error {
  NSAssert([error isKindOfClass:[NSError class]], @"Invalid error type.");

  if (![error isKindOfClass:[NSError class]]) {
    // Release 模式下调用 throw 抛出错误
    @throw error;  // NOLINT
  }
  @synchronized(self) {
    //
    if (_state == FBLPromiseStatePending) {
      _state = FBLPromiseStateRejected;
      _error = error;
      _pendingObjects = nil;
      for (FBLPromiseObserver observer in _observers) {
        observer(_state, _error);
      }
      _observers = nil;
      dispatch_group_leave(FBLPromise.dispatchGroup);
    }
  }
}
```

结合 `pending` ， `fulfill:` 和 `reject:` 方法，我们就可以不通过异步 block 来进行一些异步操作：

```objectivec
FBLPromise<NSString *> *promise = [FBLPromise pendingPromise];
// ...
if (success) {
	[promise fulfill:@"Hello world"];
} else {
	[promise reject:someError];
}
```

也可以直接生成已经处理完成的 `FBLPromise` :

```objectivec
- (FBLPromise<NSData *> *) getDataAtURL:(NSURL *)anURL {
	if (anURL.absoluteString.length == 0) {
		return [FBLPromise resolvedWith:nil];
  }
	return [self loadURL:anURL];
}
```

`FBLPromise` 对内有提供添加 Observer 的方法，可以分别处理 `fulfill` 和 `reject` ：

```objectivec
- (void)observeOnQueue:(dispatch_queue_t)queue
               fulfill:(FBLPromiseOnFulfillBlock)onFulfill
                reject:(FBLPromiseOnRejectBlock)onReject {
  @synchronized(self) {
    switch (_state) {
      // 如果是在 FBLPromiseStatePending 状态，就添加到 Observers 中
      case FBLPromiseStatePending: {
        if (!_observers) {
          _observers = [[NSMutableArray alloc] init];
        }
        [_observers addObject:^(FBLPromiseState state, id __nullable resolution) {
          dispatch_group_async(FBLPromise.dispatchGroup, queue, ^{
            switch (state) {
              case FBLPromiseStatePending:
                break;
              case FBLPromiseStateFulfilled:
                onFulfill(resolution);
                break;
              case FBLPromiseStateRejected:
                onReject(resolution);
                break;
            }
          });
        }];
        break;
      }
      // 如果当前是 FBLPromiseStateFulfilled 状态，直接调用 onFulfill 处理 _value 即可
      case FBLPromiseStateFulfilled: {
        dispatch_group_async(FBLPromise.dispatchGroup, queue, ^{
          onFulfill(self->_value);
        });
        break;
      }
      // 如果当前是 FBLPromiseStateRejected 状态，直接调用 onnReject 处理 _error 即可
      case FBLPromiseStateRejected: {
        dispatch_group_async(FBLPromise.dispatchGroup, queue, ^{
          onReject(self->_error);
        });
        break;
      }
    }
  }
}
```

`FBLPromise` 也提供了链式调用的方法，虽然说 Objective-C 的 `[]` 方法调用会使得链式调用写起来比较啰嗦：

```objectivec
- (FBLPromise *)chainOnQueue:(dispatch_queue_t)queue
              chainedFulfill:(FBLPromiseChainedFulfillBlock)chainedFulfill
               chainedReject:(FBLPromiseChainedRejectBlock)chainedReject {
  FBLPromise *promise = [[FBLPromise alloc] initPending];
  // resolver 的 block
  __auto_type resolver = ^(id __nullable value) {
    // 判断一下 value 是否为 FBLPromise
    // 如果是 FBLPromise ，就添加一个 Observer ，在这个 FBLPromise 的回调中进行处理
    if ([value isKindOfClass:[FBLPromise class]]) {
      [(FBLPromise *)value observeOnQueue:queue
          fulfill:^(id __nullable value) {
            [promise fulfill:value];
          }
          reject:^(NSError *error) {
            [promise reject:error];
          }];
    } else {
      // 如果不是 FBLPromise ，就直接调用 fulfill: 方法
      // fulfill 内部会判断 value 是否为 error ，所以这里不用进行区分
      [promise fulfill:value];
    }
  };
  // 添加 Observer 到 self
  [self observeOnQueue:queue
      fulfill:^(id __nullable value) {
        value = chainedFulfill ? chainedFulfill(value) : value;
        resolver(value);
      }
      reject:^(NSError *error) {
        id value = chainedReject ? chainedReject(error) : error;
        resolver(value);
      }];
  return promise;
}
```

`FBLPromise` 最基本的方法已经介绍完毕，通过 `FBLPromise` 的这些方法可以将一些异步操作转换为 Promise 的形式，而 Promise 这个库在基础的方法上又提供了一些扩展。

## 基础用法

### Async

通过 `async` 操作符，可以直接在 block 中异步处理任务，然后调用 `fulfill()` 或者 `reject()` ：

```objectivec
FBLPromise<NSString *> *promise = [FBLPromise onQueue:dispatch_get_main_queue()
                                                async:^(FBLPromiseFulfillBlock fulfill,
                                                        FBLPromiseRejectBlock reject) {
  // 异步执行任务
  if (success) {
    fulfill(@"Hello world.");
  } else {
    reject(someError);
  }
}];
```

```objectivec
typedef void (^FBLPromiseFulfillBlock)(Value __nullable value) NS_SWIFT_UNAVAILABLE("");
typedef void (^FBLPromiseRejectBlock)(NSError *error) NS_SWIFT_UNAVAILABLE("");
typedef void (^FBLPromiseAsyncWorkBlock)(FBLPromiseFulfillBlock fulfill,
                                         FBLPromiseRejectBlock reject) NS_SWIFT_UNAVAILABLE("");

+ (instancetype)onQueue:(dispatch_queue_t)queue async:(FBLPromiseAsyncWorkBlock)work {
  FBLPromise *promise = [[FBLPromise alloc] initPending];
  dispatch_group_async(FBLPromise.dispatchGroup, queue, ^{
    // block 的参数还是两个 block
    work(
        // FBLPromiseFulfillBlock
        ^(id __nullable value) {
          // 返回的 value 是 FBLPromise ，就添加 Observer ，然后在 FBLPromise 的结果处理中调用原来 FBLPromise 的方法
          if ([value isKindOfClass:[FBLPromise class]]) {
            [(FBLPromise *)value observeOnQueue:queue
                fulfill:^(id __nullable value) {
                  [promise fulfill:value];
                }
                reject:^(NSError *error) {
                  [promise reject:error];
                }];
          } else {
            [promise fulfill:value];
          }
        },
        // FBLPromiseRejectBlock
        ^(NSError *error) {
          [promise reject:error];
        });
  });
  return promise;
}
```

### Do

如果任务不需要异步执行，可以使用 `do` 操作符，它比 `async` 更加简介：

```objectivec
FBLPromise<NSString *> *promise = [FBLPromise do:^id {
  // Called asynchronously on the default queue.
  return success ? @"Hello world" : someError;
}];
```

```objectivec
+ (instancetype)onQueue:(dispatch_queue_t)queue do:(FBLPromiseDoWorkBlock)work {
  FBLPromise *promise = [[FBLPromise alloc] initPending];
  dispatch_group_async(FBLPromise.dispatchGroup, queue, ^{
    // 和 async 不同，这里直接调用 work() block 获取结果
    id value = work();
    if ([value isKindOfClass:[FBLPromise class]]) {
      [(FBLPromise *)value observeOnQueue:queue
          fulfill:^(id __nullable value) {
            [promise fulfill:value];
          }
          reject:^(NSError *error) {
            [promise reject:error];
          }];
    } else {
      [promise fulfill:value];
    }
  });
  return promise;
}
```

由于 Objective-C 不是强类型语言，这里只能通过判断返回的 `value` 是否为 `FBLPromise` 来进行不同的处理。

### Then

`then` 操作符支持将 `FBLPromise` 转换为另一个 `FBLPromise` 或者 value 。

```objectivec
FBLPromise<NSNumber *> *numberPromise = [FBLPromise resolvedWith:@42];

// 返回新的 FBLPromise
FBLPromise<NSString *> *chainedStringPromise = [numberPromise then:^id(NSNumber *number) {
  return [self stringFromNumber:number];
}];

// 返回 value
FBLPromise<NSString *> *chainedStringPromise = [numberPromise then:^id(NSNumber *number) {
  return [number stringValue];
}];

// 返回错误
FBLPromise<NSString *> *chainedStringPromise = [numberPromise then:^id(NSNumber *number) {
  return [NSError errorWithDomain:@"" code:0 userInfo:nil];
}];

// 假的 void return ，可以返回 nil 或者直接返回同样的 value
FBLPromise<NSString *> *chainedStringPromise = [numberPromise then:^id(NSNumber *number) {
  NSLog(@"%@", number);
  return nil;
  // OR
  return number;
}];
```

`then` 的实现比较简单，只是直接调用了 `chainOnQueue:chainedFulfill:chainedReject:` ：

```objectivec
- (FBLPromise *)onQueue:(dispatch_queue_t)queue then:(FBLPromiseThenWorkBlock)work {
  // error 部分会在新的 FBLPromise 中处理，所以这里的 chainedReject 传 nil 就可以了
  return [self chainOnQueue:queue chainedFulfill:work chainedReject:nil];
}
```

由于 Objective-C 不支持方法重载，所以这里不能提供一个 `void` 返回的 `then` 操作符版本，只能通过返回 `nil` 或者返回原有的值来达到相同的目的，建议返回原有的值，后续还可以继续通过 `then` 来进行链式调用。通过 `then` 来进行链式调用：

```objectivec
- (FBLPromise<NSString *> *)work1:(NSString *)string {
	return [FBLPromise do:^id {
		return string;
	}];
}

- (FBLPromise<NSNumber *> *)work2:(NSString *)string {
  return [FBLPromise do:^id {
    return @(string.integerValue);
  }];
}

- (NSNumber *)work3:(NSNumber *)number {
  return @(number.integerValue * number.integerValue);
}

[[[[self work1:@"10"] then:^id(NSString *string) {
  return [self work2:string];
}] then:^id(NSNumber *number) {
  return [self work3:number];
}] then:^id(NSNumber *number) {
  NSLog(@"%@", number);  // 100
  return number;
}];
```

### Catch

`catch` 操作符和 `then` 相反，只处理错误部分，同时也会隐式得返回新的 `FBLPromise` 。

```objectivec
[[self numberFromString:@"abc"] catch:^(NSError *error) {
  NSLog(@"Cannot convert string to number: %@", error);
}];
```

通过 `catch` 和 `then` 结合，可以不需要在每次异步操作时都需要进行错误处理 ，而在上层统一处理错误：

```objectivec
- (FBLPromise<NSString *> *)work1:(NSString *)string {
  return [FBLPromise do:^id {
    return string;
  }];
}

- (FBLPromise<NSNumber *> *)work2:(NSString *)string {
  return [FBLPromise do:^id {
    NSInteger number = string.integerValue;
    return number > 0 ? @(number) : [NSError errorWithDomain:@"" code:0 userInfo:nil];
  }];
}

- (NSNumber *)work3:(NSNumber *)number {
  return @(number.integerValue * number.integerValue);
}

[[[[[self work1:@"abc"] then:^id(NSString *string) {
  return [self work2:string];
}] then:^id(NSNumber *number) {
  return [self work3:number];  // Never executed.
}] then:^id(NSNumber *number) {
  NSLog(@"%@", number);  // Never executed.
  return number;
}] catch:^(NSError *error) {
  NSLog(@"Cannot convert string to number: %@", error);
}];
```

## 进阶

通过上面的 `async` ， `do` ， `then` 和 `catch` 操作符，就可以使用 `FBLPromise` 实现大多数异步操作序列。如果需要开箱即用的模式，这里还有一些进阶操作符。

### All

`all` 操作符是由类方法提供，它会等待数组中所有的 `FBLPromise` 都变为 `fulfilled` 后才会调用 `fulfill:` 方法。只要有其中一个 `FBLPromise` 被 `rejected` 了， `all` 方法生成的 `FBLPromise` 都会收到相同的错误。

```objectivec
// 相同类型的 FBLPromise
[[FBLPromise all:[contacts fbl_map:^id(MyContact *contact) {
  return [MyClient getAvatarForContact:contact];
}]] then:^id(NSArray<UIImage *> *avatars) {
  [self updateAvatars:avatars];
  return nil;
}];

// 不同类型的 FBLPromise
[[FBLPromise
    all:@[ [MyClient getLocationForContact:contact], [MyClient getAvatarForContact:contact] ]]
    then:^id(NSArray *locationAndAvatar) {
      [self updateContactLocation:locationAndAvatar.firstObject
                        andAvatar:locationAndAvatar.lastObject];
      return nil;
    }];
```

由于 Objective-C 不是强类型语言，所以调用 `all` 时需要非常小心，避免传输错误的类型。上面的 Objective-C 代码使用了 `NSArray` 的 `fbl_map` 方法，这个是 Google 出的一个为 Objective-C 补上缺少的函数式操作符的库：https://github.com/google/functional-objc 。

`all` 方法的实现也比较朴实无华，我本来以为会用到 `dispatch_group` 之类的，没想到并没有，只是用一个 `for` 循环，在每次更新数组的 `FBLPromise` 状态时判断是否所有 `FBLPromise` 都已经完成处理。

```objectivec
+ (FBLPromise<NSArray *> *)onQueue:(dispatch_queue_t)queue all:(NSArray *)allPromises {
  // 如果 allPromises 为空，就直接返回
  if (allPromises.count == 0) {
    return [[FBLPromise alloc] initWithResolution:@[]];
  }
  NSMutableArray *promises = [allPromises mutableCopy];
  return [FBLPromise
      onQueue:queue
        async:^(FBLPromiseFulfillBlock fulfill, FBLPromiseRejectBlock reject) {
          // 这里需要处理传进来的数据，如果不是 FBLPromise 则将它转换为 FBLPromise
          for (NSUInteger i = 0; i < promises.count; ++i) {
            id promise = promises[i];
            if ([promise isKindOfClass:self]) {
              continue;
            } else if ([promise isKindOfClass:[NSError class]]) {
              // 如果是 NSError 就直接调用 reject 方法。
              reject(promise);
              return;
            } else {
              [promises replaceObjectAtIndex:i
                                  withObject:[[FBLPromise alloc] initWithResolution:promise]];
            }
          }
          for (FBLPromise *promise in promises) {
            [promise observeOnQueue:queue
                fulfill:^(id __unused _) {
                  // 每个 promise fulfill 时都判断下是否还有 promise 没处理完，
							    // 时间复杂度 O(n) ，但是一般 promise 数组的数量也不会太多，所以影响不大
                  for (FBLPromise *promise in promises) {
                    if (!promise.isFulfilled) {
                      return;
                    }
                  }
                  // 通过 key-value 的方式来返回 promises 的 value 数组
                  fulfill([promises valueForKey:NSStringFromSelector(@selector(value))]);
                }
                reject:^(NSError *error) {
                  reject(error);
                }];
          }
        }];
}
```

### Always

`always` 操作符用于在 Promise 管道上执行一些代码，不管这个 Promise 是 `fulfilled` 还是 `rejected` ：

```objectivec
[[[[self getCurrentUserContactsAvatars] then:^id(NSArray<UIImage *> *avatars) {
  [self updateAvatars:avatars];
  return avatars;
}] catch:^(NSError *error) {
  [self showErrorAlert:error];
}] always:^{
  self.label.text = @"All done.";
}];
```

`always` 是通过 `chainOnQueue:chainedFulfill:chainedReject:` 来实现的，以此来生成新的 `FBLPromise` ，和在 `filfilled` 和 `rejected` 中都调用 `work` ：

```objectivec
- (FBLPromise *)onQueue:(dispatch_queue_t)queue always:(FBLPromiseAlwaysWorkBlock)work {
  return [self chainOnQueue:queue
      chainedFulfill:^id(id value) {
        work();
        return value;
      }
      chainedReject:^id(NSError *error) {
        work();
        return error;
      }];
}
```

### Any

`any` 操作符和 `all` 类似，但是只有所有 promises 都是 `rejected` 才会调用 `reject` 方法，只要有一个 promise 是 `fulfilled` 都会调用 `fulfill` 方法：

```objectivec
// 获取 promises 中的 value 或者 error
static NSArray *FBLPromiseCombineValuesAndErrors(NSArray<FBLPromise *> *promises) {
  NSMutableArray *combinedValuesAndErrors = [[NSMutableArray alloc] init];
  for (FBLPromise *promise in promises) {
    if (promise.isFulfilled) {
      [combinedValuesAndErrors addObject:promise.value ?: [NSNull null]];
      continue;
    }
    if (promise.isRejected) {
      [combinedValuesAndErrors addObject:promise.error];
      continue;
    }
    assert(!promise.isPending);
  };
  return combinedValuesAndErrors;
}

+ (FBLPromise<NSArray *> *)onQueue:(dispatch_queue_t)queue any:(NSArray *)anyPromises {
  if (anyPromises.count == 0) {
    return [[FBLPromise alloc] initWithResolution:@[]];
  }
  NSMutableArray *promises = [anyPromises mutableCopy];
  return [FBLPromise
      onQueue:queue
        async:^(FBLPromiseFulfillBlock fulfill, FBLPromiseRejectBlock reject) {
          // 照样转换为 FBLPromise
          for (NSUInteger i = 0; i < promises.count; ++i) {
            id promise = promises[i];
            if ([promise isKindOfClass:self]) {
              continue;
            } else {
              [promises replaceObjectAtIndex:i
                                  withObject:[[FBLPromise alloc] initWithResolution:promise]];
            }
          }
          for (FBLPromise *promise in promises) {
            [promise observeOnQueue:queue
                fulfill:^(id __unused _) {
                  // 判断是否还有 promise 在处理中
                  for (FBLPromise *promise in promises) {
                    if (promise.isPending) {
                      return;
                    }
                  }
                  // 所有 promises 都处理完毕后，调用 fulfill
                  fulfill(FBLPromiseCombineValuesAndErrors(promises));
                }
                reject:^(NSError *error) {
                  BOOL atLeastOneIsFulfilled = NO;
                  for (FBLPromise *promise in promises) {
                    if (promise.isPending) {
                      return;
                    }
                    if (promise.isFulfilled) {
                      atLeastOneIsFulfilled = YES;
                    }
                  }
                  // 数组中只要有一个 promise 是 fulfilled ，就调用 fulfill
                  if (atLeastOneIsFulfilled) {
                    fulfill(FBLPromiseCombineValuesAndErrors(promises));
                  } else {
                    reject(error);
                  }
                }];
          }
        }];
}
```

### **AwaitPromise**

使用 `awaitPromise` 操作符，可以通过同步的方式来等待不同线程中的 promise 完成处理。当需要从多个异步操作中以不同的方式混合多个操作结果时，就可以使用 `awaitPromise` 来进行操作：

```objectivec
[[[FBLPromise do:^id {
  NSError *error;
  NSNumber *minusFive = FBLPromiseAwait([calculator negate:@5], &error);
  if (error) return error;
  NSNumber *twentyFive = FBLPromiseAwait([calculator multiply:minusFive by:minusFive], &error);
  if (error) return error;
  NSNumber *twenty = FBLPromiseAwait([calculator add:twentyFive to:minusFive], &error);
  if (error) return error;
  NSNumber *five = FBLPromiseAwait([calculator subtract:twentyFive from:twenty], &error);
  if (error) return error;
  NSNumber *zero = FBLPromiseAwait([calculator add:minusFive to:five], &error);
  if (error) return error;
  NSNumber *result = FBLPromiseAwait([calculator multiply:zero by:five], &error);
  if (error) return error;
  return result;
}] then:^id(NSNumber *result) {
  // ...
}] catch:^(NSError *error) {
  // ...
}];
```

`FBLPromiseAwait` 通过 `dispatch_semaphore_t` 来将异步操作强制为同步：

```objectivec
id __nullable FBLPromiseAwait(FBLPromise *promise, NSError **outError) {
  static dispatch_once_t onceToken;
  static dispatch_queue_t queue;
  dispatch_once(&onceToken, ^{
    queue = dispatch_queue_create("com.google.FBLPromises.Await", DISPATCH_QUEUE_CONCURRENT);
  });
  dispatch_semaphore_t semaphore = dispatch_semaphore_create(0);
  id __block resolution;
  NSError __block *blockError;
  [promise chainOnQueue:queue
      chainedFulfill:^id(id value) {
        resolution = value;
        dispatch_semaphore_signal(semaphore);
        return value;
      }
      chainedReject:^id(NSError *error) {
        blockError = error;
        dispatch_semaphore_signal(semaphore);
        return error;
      }];
  // 等待 promise 调用 fulfill 或者 reject
  dispatch_semaphore_wait(semaphore, DISPATCH_TIME_FOREVER);
  if (outError) {
    *outError = blockError;
  }
  return resolution;
}
```

### Delay

`delay` 操作符支持在 `fulfill` 中加入延迟时间，或者直接调用 `reject` ，可以用来在 promise 链式调用中添加人为的暂停：

```objectivec
- (FBLPromise *)onQueue:(dispatch_queue_t)queue delay:(NSTimeInterval)interval {
  FBLPromise *promise = [[FBLPromise alloc] initPending];
  [self observeOnQueue:queue
      fulfill:^(id __nullable value) {
        dispatch_after(dispatch_time(0, (int64_t)(interval * NSEC_PER_SEC)), queue, ^{
          [promise fulfill:value];
        });
      }
      reject:^(NSError *error) {
        [promise reject:error];
      }];
  return promise;
}
```

### Race

`race` 操作符和 `all` 相似，但是它会采用第一个完成处理的 promise 的结果：

```objectivec
+ (instancetype)onQueue:(dispatch_queue_t)queue race:(NSArray *)racePromises {
  NSArray *promises = [racePromises copy];
  return [FBLPromise onQueue:queue
                       async:^(FBLPromiseFulfillBlock fulfill, FBLPromiseRejectBlock reject) {
                         for (id promise in promises) {
                           if (![promise isKindOfClass:self]) {
                             fulfill(promise);
                             return;
                           }
                         }
                         // 虽然订阅了所有的 promise ，
                         // 但是只有第一个完成处理的 promise 开业改变所返回的 promise 的状态
                         for (FBLPromise *promise in promises) {
                           [promise observeOnQueue:queue fulfill:fulfill reject:reject];
                         }
                       }];
}
```

### Recover

`recover` 操作符允许我们 `catch` 错误，不会破坏 promise 的链式调用。

```objectivec
[[[self getCurrentUserContactsAvatars] recover:^id(NSError *error) {
  NSLog(@"Fallback to default avatars due to error: %@", error);
  return [self getDefaultsAvatars];
}] then:^id(NSArray<UIImage *> *avatars) {
  [self updateAvatars:avatars];
  return avatars;
}];
```

实现也比较简单，在链式调用中加多一个中间层的处理：

```objectivec
- (FBLPromise *)onQueue:(dispatch_queue_t)queue recover:(FBLPromiseRecoverWorkBlock)recovery {
  return [self chainOnQueue:queue
             chainedFulfill:nil
              chainedReject:^id(NSError *error) {
                // 调用 recovery 对 error 进行转换
                return recovery(error);
              }];
}
```

### Reduce

`reduce` 操作符使得可以指定 block 来从 promises 集合中生成单个值。比如说将数字数组转换为单个字符串：

```objectivec
NSArray<NSNumber *> *numbers = @[ @1, @2, @3 ];
[[[FBLPromise resolvedWith:@"0"] reduce:numbers
                                combine:^id(NSString *partialString, NSNumber *nextNumber) {
  return [NSString stringWithFormat:@"%@, %@", partialString, nextNumber.stringValue];
}] then:^id(NSString *string) {
  // Final result = 0, 1, 2, 3
  NSLog(@"Final result = %@", string);
  return nil;
}];
```

```objectivec
- (FBLPromise *)onQueue:(dispatch_queue_t)queue
                 reduce:(NSArray *)items
                combine:(FBLPromiseReducerBlock)reducer {
  FBLPromise *promise = self;
  for (id item in items) {
    promise = [promise chainOnQueue:queue
                     chainedFulfill:^id(id value) {
                       return reducer(value, item);
                     }
                      chainedReject:nil];
  }
  return promise;
}
```

### Retry

`retry` 操作符提供了 promise 相关任务在失败时重试的灵活性。默认情况下， `retry` 操作符会在第一次 `reject` 后延迟一秒进行重试。如果默认操作不满足自己的需求，可以自定义队列，最大重试次数，延迟时间间隔以及不满足条件时提前退出。

```objectivec
- (FBLPromise<NSData *, NSURLResponse *> *)fetchWithURL:(NSURL *)url {
  return [FBLPromise wrap2ObjectsOrErrorCompletion:^(FBLPromise2ObjectsOrErrorCompletion handler) {
    [NSURLSession.sharedSession dataTaskWithURL:url completionHandler:handler];
  }];
}

NSURL *url = [NSURL URLWithString:@"https://myurl.com"];

// 默认延迟 1s
[[[FBLPromise retry:^id {
  return [self fetchWithURL:url];
}] then:^id(NSArray *values) {
  NSLog(@"%@", values);
  return nil;
}] catch:^(NSError *error) {
  NSLog(@"%@", error);
}];

// 自定义队列，最大尝试次数，延迟时间和是否提前退出
dispatch_queue_t customQueue = dispatch_get_global_queue(QOS_CLASS_USER_INITIATED, 0);
[[[FBLPromise onQueue:customQueue
    attempts:5
    delay:2.0
    condition:^BOOL(NSInteger remainingAttempts, NSError *error) {
      return error.code == NSURLErrorNotConnectedToInternet;
    }
    retry:^id {
      return [self fetchWithURL:url];
}] then:^id(NSArray *values) {
  // 当 retry 成功时就会调用 then
  NSLog(@"%@", values);
  return nil;
}] catch:^(NSError *error) {
  // 不满足 retry 条件时就会抛出 error
  NSLog(@"%@", error);
}];
```

```objectivec
static void FBLPromiseRetryAttempt(FBLPromise *promise, dispatch_queue_t queue, NSInteger count,
                                   NSTimeInterval interval, FBLPromiseRetryPredicateBlock predicate,
                                   FBLPromiseRetryWorkBlock work) {
  __auto_type retrier = ^(id __nullable value) {
    if ([value isKindOfClass:[NSError class]]) {
      // 如果 count <= 0 或者不满足重试条件，就不进行重试
      if (count <= 0 || (predicate && !predicate(count, value))) {
        [promise reject:value];
      } else {
        // 延迟指定时间后重试， count - 1
        dispatch_after(dispatch_time(0, (int64_t)(interval * NSEC_PER_SEC)), queue, ^{
          FBLPromiseRetryAttempt(promise, queue, count - 1, interval, predicate, work);
        });
      }
    } else {
      // 如果不是 error ，就调用 fulfill:
      [promise fulfill:value];
    }
  };
  id value = work();
  //  如果 work() 处理之后是 FBLPromise ，就添加对应的监听
  if ([value isKindOfClass:[FBLPromise class]]) {
    [(FBLPromise *)value observeOnQueue:queue fulfill:retrier reject:retrier];
  } else  {
    retrier(value);
  }
}

+ (FBLPromise *)onQueue:(dispatch_queue_t)queue
               attempts:(NSInteger)count
                  delay:(NSTimeInterval)interval
              condition:(nullable FBLPromiseRetryPredicateBlock)predicate
                  retry:(FBLPromiseRetryWorkBlock)work {
  FBLPromise *promise = [[FBLPromise alloc] initPending];
  FBLPromiseRetryAttempt(promise, queue, count, interval, predicate, work);
  return promise;
}
```

### Timeout

`timeout` 操作符支持在等待指定时间后，如果 promise 还没完成，就主动调用 `reject` ，错误类型为 `FBLPromiseErrorCodeTimedOut` 。

```objectivec
- (FBLPromise *)onQueue:(dispatch_queue_t)queue timeout:(NSTimeInterval)interval {
  FBLPromise *promise = [[FBLPromise alloc] initPending];
  [self observeOnQueue:queue
      fulfill:^(id __nullable value) {
        [promise fulfill:value];
      }
      reject:^(NSError *error) {
        [promise reject:error];
      }];
  typeof(self) __weak weakPromise = promise;
  // 超过指定时间后就主动调用 reject
  dispatch_after(dispatch_time(0, (int64_t)(interval * NSEC_PER_SEC)), queue, ^{
    NSError *timedOutError = [[NSError alloc] initWithDomain:FBLPromiseErrorDomain
                                                        code:FBLPromiseErrorCodeTimedOut
                                                    userInfo:nil];
    [weakPromise reject:timedOutError];
  });
  return promise;
}
```

### **Validate**

`validate` 操作符使得可以对值进行检查而不破坏 promise 的链式调用。它和 `then` 类似，接收 promise 解析后的值，然后返回一个 `bool` 值。如果返回 `false` ，就会抛出一个错误，错误类型为 `FBLPromiseErrorCodeValidationFailure` 。

```objectivec
[[[[self getAuthToken] validate:^BOOL(NSString *authToken) {
  return authToken.length > 0;
}] then:^id(NSString *authToken) {
  return [self getDataWithToken:authToken];
}] catch:^(NSError *error) {
  NSLog(@"Failed to get auth token: %@", error);
}];
```

`validate` 的实现，实现也比较简单：

```objectivec
- (FBLPromise*)onQueue:(dispatch_queue_t)queue validate:(FBLPromiseValidateWorkBlock)predicate {

  FBLPromiseChainedFulfillBlock chainedFulfill = ^id(id value) {
    // predicate 判断下，如果不满足就抛出 FBLPromiseErrorCodeValidationFailure
    return predicate(value) ? value :
                              [[NSError alloc] initWithDomain:FBLPromiseErrorDomain
                                                         code:FBLPromiseErrorCodeValidationFailure
                                                     userInfo:nil];
  };
  return [self chainOnQueue:queue chainedFulfill:chainedFulfill chainedReject:nil];
}
```

### Wrap

`wrap` 操作符提供了一个便利的转换方式，支持将比较通用的回调，比如说 `^(id, NSError *)` 转换为 `FBLPromise` ：

```objectivec
- (FBLPromise<NSData*> *)newAsyncMethodReturningAPromise {
  return [FBLPromise wrapObjectOrErrorCompletion:^(FBLPromiseObjectOrErrorCompletion handler) {
    [MyClient wrappedAsyncMethodWithTypicalCompletion:handler];
  }];
}
```

`wrap` 的实现：

```objectivec
typedef void (^FBLPromiseObjectOrErrorCompletion)(id __nullable, NSError* __nullable);

+ (instancetype)onQueue:(dispatch_queue_t)queue
    wrapObjectOrErrorCompletion:(void (^)(FBLPromiseObjectOrErrorCompletion))work {
  return [self onQueue:queue
                 async:^(FBLPromiseFulfillBlock fulfill, FBLPromiseRejectBlock reject) {
                   // 调用 work 来获取异步操作的结果，然后调用 FBLPromise 对应的方法
                   work(^(id __nullable value, NSError *__nullable error) {
                     if (error) {
                       reject(error);
                     } else {
                       fulfill(value);
                     }
                   });
                 }];
}
```

## 其它一些需要注意的问题

### 默认的 GCD 队列

`Promises` 内部使用 GCD 来派发不同的任务到不同的队列。如果没有指定，默认是主队列，为了避免造成主队列过于忙碌，影响用户的体验，通常会调整默认队列：

```objectivec
FBLPromise.defaultDispatchQueue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
```

### 循环引用

对于 promise 来说，你几乎不需要关心它们的循环引用。当 promise 完成任务时，它会释放掉所有 block 的强引用。尽管如此，还是有可能会产生循环引用。比如给说在 promise 的链式调用 block 中使用 promise 对象，如果你已经 promise 保存在一个局部变量中，就可能会发生循环引用，特别是创建一个不关联任何 block 的未完成解析的 promise 时：

```objectivec
@implementation MyClass {
  FBLPromise<NSNumber *> *_promise;
}

- (FBLPromise<NSString *> *)doSomething {
  if (_promise == nil) {
    _promise = [FBLPromise pendingPromise];
  }
  return [_promise then:^id(id number) {
    return [self doSomethingElse:number];
  }];
}

- (NSString *)doSomethingElse:(NSNumber *)number {
  return number.stringValue;
}

@end
```

`self` 持有 `promise` ，而 `promise` 又在 `then` block 中捕获 `self` 。我们可以通过 `weak` 引用来解决，因为我们知道 `MyClass` 的代码细节，但是这种情况有可能变得更加难以察觉：

```objectivec
[[myClass doSomething] then:^id(NSString *string) {
  [myClass doSomeOtherThing];
}];
```

我们通过 `MyClass` 的方法来获取一个 promise ，然后通过链式调用来添加监听 block ，在里面再捕获 `MyClass` 的对象，这样也会产生循环引用。这部分代码并不知道 `MyClass` 会对 promise 进行强引用，而且还没有对应的 `reslove` 代码，所以这个循环引用不会被打破。

对于 Promise 的循环引用来说，它和我们日常开发中遇到的循环引用情况差不多，并没有银弹，我们需要单独考虑每种情况。尽量避免使用 `pending` 的 promises ，一旦 promise 完成解析，就调用对应的方法。

### Objective-C 的点语法

当在 Objective-C 中使用链式调用时，就会出现大量的方括号和其它一些格式问题，对于每个操作符， `FBLPromise` 都通过 block 的方式提供了点语法的调用方式：

```objectivec
[self work1:@"abc"]
    .then(^id(NSString *string) {
      return [self work2:string];
    })
    .then(^id(NSNumber *number) {
      return [self work3:number];
    })
    .then(^id(NSNumber *number) {
      NSLog(@"%@", number);
      return nil;
    })
    .catch(^(NSError *error) {
      NSLog(@"Cannot convert string to number: %@", error);
    });
```

## 总结

Promises 的 Objective-C 层实现比较简单，也比较小巧，代码量不多，主要是按照 Promise 的规则来，结合 GCD 提供符合定义的接口就好来。
