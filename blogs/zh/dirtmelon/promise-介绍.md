---
title: Promise - 介绍
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/promise-first/'
original_language: zh
published: 2021-11-23
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7092d98bbf83aae5'
translated: n/a
---

> 原文：[Promise - 介绍](https://dirtmelon.github.io/posts/promise-first/)　·　dirtmelon

## 异步代码的问题

通常来说，异步操作都会通过 block 的方式来执行回调，block 的参数会提供结果和错误。如果需要执行多个异步操作，需要将第二个异步操作嵌套在第一个操作的 block 中，同时也需要处理错误。在这样的嵌套代码中进行修改会变得非常痛苦。 Objective-C 的异步嵌套代码：

```objectivec
- (void)getCurrentUserContactsAvatars:(void (^)(NSArray<UIImage *> *, NSError *))completion {
  [MyClient getCurrentUserWithCompletion:^(MyUser *currentUser, NSError *error) {
    if (error) {
      completion(nil, error);
      return;
    }
    [MyClient getContactsForUser:currentUser
                      completion:^(NSArray<MyContact *> *contacts, NSError *error) {
      if (error) {
        completion(nil, error);
        return;
      }
      if (contacts.count == 0) {
        completion(@[], nil);
        return;
      }
      NSMutableArray<UIImage *> *avatars = [NSMutableArray array];
      NSUInteger __block count = contacts.count;
      BOOL __block errorReported = NO;
      for (NSUInteger index = 0; index < count; ++index) {
        [avatars addObject:[NSNull null]];
      }
      [contacts enumerateObjectsUsingBlock:^(MyContact *contact, NSUInteger index, BOOL __unused *_) {
        [MyClient getAvatarForContact:contact completion:^(UIImage *avatar, NSError *error) {
          if (errorReported) {
            return;
          }
          if (error) {
            completion(nil, error);
            errorReported = YES;
            return;
          }
          if (avatar) {
            avatars[index] = avatar;
          }
          if (--count == 0) {
            completion(avatars, nil);
          }
        }];
      }];
    }];
  }];
}
```

Swift 的：

```swift
func getCurrentUserContactsAvatars(_ completion: ([UIImage]?, Error?) -> Void) {
  MyClient.getCurrentUser() { currentUser, error in
    guard error == nil else {
      completion(nil, error)
      return
    }
    MyClient.getContacts(currentUser) { contacts, error in
      guard error == nil else {
        completion(nil, error)
        return
      }
      guard let contacts = contacts, !contacts.isEmpty() else {
        completion([UIImage](), nil)
        return
      }
      var count = contacts.count
      var avatars = [UIImage](repeating: nil, count: count)
      var errorReported = false
      for (index, contact) in contacts.enumerated() {
        MyClient.getAvatar(contact) { avatar, error in
          if (errorReported) {
            return
          }
          guard error == nil {
            completion(nil, error)
            errorReported = true
            return
          }
          if let avatar = avatar {
            avatars[index] = avatar
          }
          count -= 1
          if count == 0 {
            completion(avatars.flatMap { $0 }, nil)
          }
        }
      }
    }
  }
}
```

由于 Swift 是使用 `.` 语法进行方法调用的，少了方括号，所以看起来会舒服点。一般来说如果有多个异步操作嵌套时，可以通过方法来进行封装，不会像上面这样，把所有异步操作的处理都放在同一个方法里。但是我们也可以通过 Promise 来进行优化：

Objective-C ：

```objectivec
- (FBLPromise<NSArray<UIImage *> *> *)getCurrentUserContactsAvatars {
  return [[[MyClient getCurrentUser] then:^id(MyUser *currentUser) {
    return [MyClient getContactsForUser:currentUser];
  }] then:^id(NSArray<MyContact *> *contacts) {
    return [FBLPromise all:[contacts fbl_map:^id(MyContact *contact) {
      return [MyClient getAvatarForContact:contact];
    }]];
  }];
```

Swift ：

```swift
func getCurrentUserContactsAvatars() -> Promise<[UIImage]> {
  return MyClient.getCurrentUser().then(MyClient.getContacts).then { contacts in
    all(contacts.map(MyClient.getAvatar))
  }
}
```

而所有异步操作的 error 都可以上层调用中统一处理。

## 什么是 Promise

通常来说， Promise 代表了一个异步任务最终有可能发生的结果或者任务失败的原因。类似的概念有 futures ，具体可以看维基上的说明：[Futures and promises](http://en.wikipedia.org/wiki/Futures_and_promises) 。

- pending （处理中）， Promise 还没有处理完毕；
- fulfilled ， Promise 已完成解析，包含某个值；
- rejected ，Promise 已完成解析，包含某个错误。

一旦转换至 fulfilled 或者 rejected ，Promise 就无法再改变状态。

Promise 同时还可以有无数个观察者，监听着它的状态，一旦 Promise 的状态有所更新，观察者就会接收到相应的消息。每个观察者在进行订阅时会生成一个新的 Promise ，这样可以进行链式的调用，也可以在不同的线程上进行异步的处理或者值转换。

因此， Promise 是一种格式化处理异步回调，使得链式异步处理更加容易的方式。使得以下操作更加容易：

- 链式执行有依赖的异步操作，并且在最后执行回调；
- 统一处理不同的错误；
- 同时执行独立的异步操作，在最后执行回调；
- 执行很多异步操作，并且返回第一个值；
- 重试异步操作；
- 等等。

iOS 有不少实现来 Promise 或者有类似功能的库：

[Promises](https://github.com/google/promises)

[PromiseKit: Promises for Swift & ObjC.](https://github.com/mxcl/PromiseKit)

[BrightFutures: Write great asynchronous code in Swift using futures and promises](https://github.com/Thomvis/BrightFutures)

[Hydra: ⚡️ Lightweight full-featured Promises, Async & Await Library in Swift](https://github.com/malcommac/Hydra)

[RxSwift: Reactive Programming in Swift](https://github.com/ReactiveX/RxSwift)

后续会对 Promises 和 PromiseKit 进行源码解析。
