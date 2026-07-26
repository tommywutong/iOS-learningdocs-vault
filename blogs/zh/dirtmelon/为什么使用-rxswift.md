---
title: 为什么使用 RxSwift
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/why-use-rxswift/'
original_language: zh
published: 2017-03-09
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:c4f8775d80337603'
translated: n/a
---

> 原文：[为什么使用 RxSwift](https://dirtmelon.github.io/posts/why-use-rxswift/)　·　dirtmelon

原文链接:[Why](https://github.com/ReactiveX/RxSwift/blob/master/Documentation/Why.md)

**RxSwift支持以声明的方式来构建App。**

### Bindings

```swift
Observable.combineLatest(firstName.rx.text, lastName.rx.text) { $0 + " " + $1 }
    .map { "Greetings, \($0)" }
    .bindTo(greetingLabel.rx.text)
```

也适用于`UITableView`和`UICollectionView`。

```swift
viewModel
    .rows
    .bindTo(resultsTableView.rx.items(cellIdentifier: "WikipediaSearchCell", cellType: WikipediaSearchCell.self)) { (_, viewModel, cell) in
        cell.title = viewModel.title
        cell.url = viewModel.url
    }
    .disposed(by: disposeBag)
```

**我们建议你使用`.disposed(by: disposeBag)`，即使它在简单的bindings中不是必须的。**

### Retries

如果API的调用不会失败是极好的，但是不幸的是它们会。让我们以下面的方法来进行说明：

```swift
func doSomethingIncredible(forWho: String) throws -> IncredibleThing
```

如果你正在使用这个函数，在它失败时进行重试是非常困难的。更不用说复杂性建模了。当然是可以进行重试的，但是代码可能会包含很多你不在意的临时状态，而且是不可重用的。

在理想情况下，你想要获取到重试的本质，并将其应用于所有操作中。

下面是你使用Rx来实现简单的重试的代码。

```swift
doSomethingIncredible("me")
    .retry(3)
```

你可以很容易地实现自定义的重试操作。

### Delegates

使用下面的方式：

```swift
self.resultsTableView
    .rx.contentOffset
    .map { $0.x }
    .bindTo(self.leftPositionConstraint.rx.constant)
```

来替代繁琐和不明了的操作：

```swift
public func scrollViewDidScroll(scrollView: UIScrollView) { [weak self] // what scroll view is this bound to?
    self?.leftPositionConstraint.constant = scrollView.contentOffset.x
}
```

### KVO

使用 [`rx.observe` and `rx.observeWeakly`](https://github.com/ReactiveX/RxSwift/blob/master/Documentation/GettingStarted.md)

使用下面的方式：

```swift
view.rx.observe(CGRect.self, "frame")
    .subscribe(onNext: { frame in
        print("Got new frame \(frame)")
    })
    .disposed(by: disposeBag)
```

或者：

```swift
someSuspiciousViewController
    .rx.observeWeakly(Bool.self, "behavingOk")
    .subscribe(onNext: { behavingOk in
        print("Cats can purr? \(behavingOk)")
    })
    .disposed(by: disposeBag)
```

来替代：

```plaintext
当`TickTock`被释放，Observers仍然监听这个对象时。监听者信息就会产生内存泄漏，甚至可能错误地附加到其它对象中。
```

和

```objc
-(void)observeValueForKeyPath:(NSString *)keyPath
                     ofObject:(id)object
                       change:(NSDictionary *)change
                      context:(void *)context
```

### Notifications

使用下面的方式：

```swift
NotificationCenter.default
    .rx.notification(Notification.Name.UITextViewText, object: myTextView)
    .map{ /*do something with data*/ }
	  ...
```

来替代：

```swift
@available(iOS 4.0, *)
public func addObserverForName(name: String?, object obj: AnyObject?, queue: NSOperationQueue?, usingBlock block: (NSNotification) -> Void) -> NSObjectProtocol
```

### Transient state

在编写异步程序时临时状态会有许多问题。一个典型的例子是自动填充搜索框。

如果你曾在不使用Rx的情况下编写自动填充的代码，第一个问题是当打出`abc`中的`c`时，有一个关于`ab`的待处理请求，这个请求需要取消掉。OK，这应该不太难解决，你只需创建一个额外的变量来引用挂起的请求。

下一个问题是如果请求失败了，你需要执行混乱的重试逻辑。一些捕获了重试次数的字段也需要进行清理。

如果在程序向服务器发送请求之前等待一段时间是非常好的。毕竟我们不想在有人打一段很长的文字时不停地向服务器发送垃圾数据。或许需要添加一个额外的计时器字段。

还需要处理执行搜索时在屏幕上显示的内容和所有重试都失败时需要显示什么。

编写所有这些情况并正确测试它是乏味的。下面是使用Rx来编写具有相同逻辑的代码：

```swift
searchTextField.rx.text
    .throttle(0.3, scheduler: MainScheduler.instance)
    .distinctUntilChanged()
    .flatMapLatest { query in
        API.getSearchResults(query)
            .retry(3)
            .startWith([]) // clears results on new search term
            .catchErrorJustReturn([])
    }
    .subscribe(onNext: { results in
      // bind to ui
    })
    .disposed(by: disposeBag)
```

这里不需要任何额外的标志和字段。Rx负责处理所有混乱的临时状态。

### Compositional disposal

让我们假设你需要在一个表格中展示模糊的照片。首先需要从 URL 中获取到图片，然后解码和让图片变得模糊。

当图片不在表格的可见范围时，如果整个过程可以取消是非常好的。因为模糊操作会消耗大量的带宽和处理器的时间。

当照片一出现在表格上时，如果我们不立即进行操作是非常好的。因为用户会快速滚动，会发起和取消大量的请求。

如果我们可以限制同时处理照片的数量也是非常好的，因为模糊是个非常昂贵的操作。

下面是我们使用Rx来进行处理的例子：

```swift
let imageSubscription = imageURLs
    .throttle(0.2, scheduler: MainScheduler.instance)
    .flatMapLatest { imageURL in
        API.fetchImage(imageURL)
    }
    .observeOn(operationScheduler)
    .map { imageData in
        return decodeAndBlurImage(imageData)
    }
    .observeOn(MainScheduler.instance)
    .subscribe(onNext: { blurredImage in
        imageView.image = blurredImage
    })
    .disposed(by: reuseDisposeBag)
```

这部分代码会完成上述的所有操作。并且当`imageSubscription`被处理时，它将取消所有相关的异步操作，确保没有多余的图像绑定到UI。

### Aggregating network request

当你需要发起两个请求并在它们都完成后处理结果时应该怎么做？

嗯，你需要`zip`操作符。

```swift
let userRequest: Observable<User> = API.getUser("me")
let friendsRequest: Observable<[Friend]> = API.getFriends("me")

Observable.zip(userRequest, friendsRequest) { user, friends in
	  return (user, friends)
}
.subscribe(onNext: { user, friends in
	  // bind them to the user interface
})
.disposed(by: disposeBag)
```

那么，如果这些API是在后台线程返回结果，并且绑定必须发生在主线程上呢？你需要`observeOn`。

```swift
let userRequest: Observable<User> = API.getUser("me")
let friendsRequest: Observable<[Friend]> = API.getFriends("me")

Observable.zip(userRequest, friendsRequest) { user, friends in
    return (user, friends)
}
.observeOn(MainScheduler.instance)
.subscribe(onNext: { user, friends in
    // bind them to the user interface
})
.disposed(by: disposeBag)
```

### State

允许改变的语言使得容易访问全局状态并改变它。全局状态的不可控改变很容易导致 [组合性爆炸](https://en.wikipedia.org/wiki/Combinatorial_explosion#Computing)。

为了对抗组合性爆炸，通常使用的方法是保持状态尽可能地简单，和使用[单向数据流](https://developer.apple.com/videos/play/wwdc2014-229)来为导出数据建模。

这是Rx真正闪耀的地方。

Rx是函数式和命令式两个世界中的甜蜜地带。它让你以一种可靠可组合的方式去使用不可变的定义和纯代码，来处理可变状态的快照。

那么实际的例子呢？

### Easy integration

如果你需要创建你自己的Observable，应该怎么做呢？很简单。这部分代码取自RxCocoa，这是需要用`URLSession`封装HTTP请求的实现。

```swift
extension URLSession {
    public func response(request: URLRequest) -> Observable<(Data, HTTPURLResponse)> {
        return Observable.create { observer in
            let task = self.base.dataTask(with: request) { (data, response, error) in
            
                guard let response = response, let data = data else {
                    observer.on(.error(error ?? RxCocoaURLError.unknown))
                    return
                }

                guard let httpResponse = response as? HTTPURLResponse else {
                    observer.on(.error(RxCocoaURLError.nonHTTPResponse(response: response)))
                    return
                }

                observer.on(.next(data, httpResponse))
                observer.on(.completed)
            }

            task.resume()

            return Disposables.create(with: task.cancel)
        }
    }
}
```

### Benefits

总之，使用Rx会使你的代码：

- 可组合 \<- 因为Rx是组合的昵称
- 可重用 \<- 因为它是可组合的
- 声明式 \<- 因为定义是不可变的，只有数据是可变的
- 可理解和间接性 \<- 提高抽象级别，消除临时状态
- 稳定性 \<- 因为Rx的代码全部都经过单元测试的
- 无状态 \<- 因为你使用单向数据流来为应用建模
- 无泄漏 \<- 因为资源管理很容易

### It’s not all or nothing

尽可能地使用Rx来编写应用程序通常是个好主意。

但是如果你不知道所有的运算符，或者是否存在一些运算符符合你的特定情况时，该怎么办？

好的，所有的Rx运算符都是基于数学的，应该是非常直观的。

好消息是大概有10-15操作符可以覆盖大部分典型的用法。这个列表包括了一些熟悉的操作符，如：`map`，`filter`，`zip`，`observeOn`等等。

这里是[Rx操作符列表](http://reactivex.io/documentation/operators/retry.html)

对于每个操作符，这里有个[文档](http://reactivex.io/documentation/operators/retry.html)，有助于解释它是如何工作的。

如果你需要的操作符不在列表上？你可以自己定义操作符。

但是如果因为某些原因难于创建对应的操作符，或者你需要使用某些遗留的状态代码？好吧，你或许感到非常混乱，但是你可以轻易地[跳出Rx monads](https://github.com/dirtmelon/RxSwift/blob/master/Documentation/GettingStarted.md#life-happens)，处理完数据再返回。
