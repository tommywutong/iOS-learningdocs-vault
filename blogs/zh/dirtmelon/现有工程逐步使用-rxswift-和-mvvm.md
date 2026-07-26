---
title: 现有工程逐步使用 RxSwift 和 MVVM
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/migrate-to-rxswift-and-mvvm/'
original_language: zh
published: 2019-09-03
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:cc84112cf59d3c79'
translated: n/a
---

> 原文：[现有工程逐步使用 RxSwift 和 MVVM](https://dirtmelon.github.io/posts/migrate-to-rxswift-and-mvvm/)　·　dirtmelon

## 现状

目前项目采用的是 `MVC` 结构，`UIViewController` 包含大量代码，包括网络请求，数据处理，布局代码等，难于测试（虽然也不写测试）。随着项目发展，这部分内容会越来越多，越来越复杂，导致 `UIViewController` 中的代码越来越难维护。为了项目的可持续发展，决定开始开始使用 `RxSwift` 和 `MVVM` 。

## ViewModel

![MVVMPattern](https://raw.githubusercontent.com/dirtmelon/blog-images/main/MVVMPattern.png)

`ViewModel` 扮演的是处理业务逻辑的角色，负责处理数据和为 `ViewController` 提供数据源。一般来说有几下几点要求：

- 可测试的，这样可以直接为 `ViewModel` 编写单元测试。
- 不知道 `ViewController` 或者 `View` 的存在，只负责自己处理数据。
- 团队编写 `ViewModel` 时需要严格按照现有规范来编写。
- 配合 `RxSwift` 食用更佳

### 如何将 ViewModel 与数据源绑定

一般来说 `ViewModel` 与数据源绑定，指的是如何将用户的操作，网络状态绑定到 `ViewModel` 上，再将 `ViewModel` 的数据源绑定到 `UI` 上。

#### 第一种绑定方式— protocol 与转换

首先定义一个 `ViewModelType` 协议，协议中包含 `Input`，`Output` 和一个将 `Input` 转换为 `Output` 的方法。 [RxSwift + MVVM: how to feed ViewModels](https://medium.com/blablacar-tech/rxswift-mvvm-66827b8b3f10) 的 **First approach — without Subjects** 和 [CleanArchitectureRxSwift/ViewModelType.swift at 55c852bbd7b4e5f9ee30426e2acdb7b038e848be · sergdort/CleanArchitectureRxSwift · GitHub](https://github.com/sergdort/CleanArchitectureRxSwift/blob/55c852bbd7b4e5f9ee30426e2acdb7b038e848be/CleanArchitectureRxSwift/Common/ViewModelType.swift) 都是采用了这种写法。

这种写法，一看之下非常好用，也很干净，没有用到 `Subject` ，所有的处理都经由 `transform` 方法完成，但是有些情况下并不适用， 可以看到转换的机会只有一次，你必须在一开始就获取到所有 `input` 的数据源，通过 `transform` 方法将 `input` 转化为 `output` 。**How to feed ViewModels** 这篇文章里面也有提到，有些时候我们并不能一次过获取到所有的数据源，不同的数据源需要分开获取，这就需要使用第二种绑定方式。

#### 第二种绑定方式 — 将 Input 和 Output 抽出来

在某些情况下，可能需要分开获取不同的数据源，这时候就需要借用 `Subject` ，但是我们可以不将 `Subject` 暴露出来。具体写法参考：[RxSwift + MVVM: how to feed ViewModels](https://medium.com/blablacar-tech/rxswift-mvvm-66827b8b3f10) 的 **Second approach — with Subjects** 。

`Subject` 属性是私有的，它为 `input` 提供了绑定来源，结构体 `Input` 有多少个属性就需要提供多少个 `Subject` 。同时 `Subject` 也可以作为 `output` 的数据来源，它是 `input` 和 `output` 两者之间的数据桥梁。

KickStarter 也是通过类似的方法将 `Subject` 隐藏起来，只不过 KickStarter 使用的是 `ReactiveCocoa` ，而且是通过方法来进行更新 `Property`(Subject)，而不是通过 `Struct` 来进行转换。 在 [vm-structure.md](https://github.com/kickstarter/native-docs/blob/master/vm-structure.md) 中有提到所有 `inputs` 都提供对应的 `MutableProperty` （`Property` 相当于 `RxSwift` 的 `Subject` ），然后在 `inputs` 函数中更新对应的 `Property` 。

### 是否使用 Subject

在任何情况下，`ViewModel` 在处理数据时都是单向流动的，即 `Input` 接受数据输入，`Output` 输出处理后的数据，上面两种写法都满足这个要求。但是如果 `Output` 里包含了 `Subject` ，`ViewController` 就可以通过调用 `Ouput` 相关 `Subject` 的 `onNext` 方法来达到输出数据的目的，这样数据流动就没有经过 `ViewModel` 进行处理了，这显然违背了 `ViewModel` 的设计原则，所以如果要使用 `Subject` ，那对应的属性则应该是私有的。

### Cell，View 等控件是否有需要添加 ViewModel

如果 `Cell`，`View` 等 UI 控件的逻辑比较简单，可以先不添加 `ViewModel` ，对于比较复杂的 `Cell` 和 `View` 等 UI 控件，可以考虑添加 `ViewModel` 。

## Network 层与 JSON 转换

现有项目使用的 [Moya](https://github.com/Moya/Moya) 来组织网络层，使用 [ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper) 来进行 `JSON` 和 `Model` 层的转换。 由于要将不同类别的接口分到不同的 `enum` 类中，创建一个 `MultiMoyaProdider` 类，可执行 `TargetType` 的请求。

```swift
class MultiMoyaProvider: MoyaProvider<MultiTarget> {

	typealias Target = MultiTarget

	init() {
	  let plugins: [PluginType]
	  #if DEBUG
	  plugins = [NetworkLoggerPlugin(verbose: true)]
	  #else
	  plugins = []
	  #endif
	  let endpointClosure = { (target: Target) -> Endpoint in
		let endpoint: Endpoint =
		  Endpoint(url: target.baseURL.absoluteString + target.path,
				   sampleResponseClosure: {
					 .networkResponse(200, target.sampleData)},
				   method: target.method,
				   task: target.task,
				   httpHeaderFields: target.headers)
			return endpoint
		}
		super.init(endpointClosure: endpointClosure, plugins: plugins)
	}

	@discardableResult
	func multiRequest<T: TargetType>(_ target: T, completion: @escaping Completion) -> Cancellable {
    return request(MultiTarget(target), completion: completion)
	}

}
```

有了 `MultiMoyaProvider` 后可以进行 `Rx` 化的改造，`Moya` 本身就提供了对于 `RxSwift` 的支持：[Moya/RxSwift.md at master · Moya/Moya · GitHub](https://github.com/Moya/Moya/blob/master/docs/RxSwift.md)。 通过 `MultiMoyaProvider` ，可以提供三种方法来返回 `Observable`。

```swift
typealias JSONDictionary = [String: Any]

// 1. 直接返回 Observable<JSONDictionary>
func jsonObservable(target: TargetType) -> Observable<JSONDictionary> {
   return Observable.create { observer in
     return provider.rx.request(MultiTarget(target))
        .subscribe(onSuccess: { (response) in
		    // 验证 response 格式
          if let error = valid(response) {
            observer.onError(error)
            return
          }
          guard let dictionary = try? response.mapJSON() as? JSONDictionary else {
            observer.onError(MoyaError.jsonMapping(response))
            return
          }
          observer.onNext(dictionary)
        },
                    onError: { (error) in
                      observer.onError(error)
      })
    }
}

// 2. 返回单个 Model 类型
func objectObservable<T: Mappable>(target: TargetType, objectType: T.Type) -> Observable<T> {
    return Observable.create { observer in
      return provider.rx.request(MultiTarget(target))
        .subscribe(onSuccess: { (response) in
          if let error = valid(response) {
            observer.onError(error)
            return
          }
          guard let object = try? response.mapObject(objectType.self) else {
            observer.onError(MoyaError.jsonMapping(response))
            return
          }
          observer.onNext(object)
        },
                   onError: { (error) in
                    observer.onError(error)
        })
    }
  }

// 3.  返回 Model 数组
func objectArrayObservable<T: Mappable>(target: TargetType, objectType: T.Type) -> Observable<[T]> {
    return Observable.create { observer in
      return provider.rx.request(MultiTarget(target))
        .subscribe(onSuccess: { (response) in
          if let error = valid(response) {
            observer.onError(error)
            return
          }
          guard let objectArray = try? response.mapArray(objectType.self) else {
            observer.onError(MoyaError.jsonMapping(response))
            return
          }
          observer.onNext(objectArray)
        },
                   onError: { (error) in
                    observer.onError(error)
        })
    }
  }
```

为了方便 `Response` 与 `Model` 间的转换，给 `Response` 新增两个方法：

```swift
extension Response {

  /// Maps data received from the signal into an object which implements the Mappable protocol.
  /// If the conversion fails, the signal errors.
  func mapObject<T: BaseMappable>(_ type: T.Type, context: MapContext? = nil) throws -> T {
    guard let object = Mapper<T>(context: context).map(JSONObject: try mapJSON()) else {
      throw MoyaError.jsonMapping(self)
    }
    return object
  }

  /// Maps data received from the signal into an array of objects which implement the Mappable
  /// protocol.
  /// If the conversion fails, the signal errors.
  func mapArray<T: BaseMappable>(_ type: T.Type, context: MapContext? = nil) throws -> [T] {
    guard let array = try mapJSON() as? [[String: Any]] else {
      throw MoyaError.jsonMapping(self)
    }
    return Mapper<T>(context: context).mapArray(JSONArray: array)
  }

}
```

然后在 `ViewModel` 具体的 `input` 中通过 `flatMap` 来调用网络请求：

```swift
  input.flatMap {
	  jsonObservable...
	}
	.subscribe
	...
```

## 相关资源

1. [http://community.rxswift.org/](http://community.rxswift.org/)
2. [https://github.com/kickstarter/native-docs/blob/master/vm-structure.md](https://github.com/kickstarter/native-docs/blob/master/vm-structure.md)
3. [native-docs/inputs-outputs.md at master · kickstarter/native-docs · GitHub](https://github.com/kickstarter/native-docs/blob/master/inputs-outputs.md) KickStarter 重度使用 `MVVM` 和 `ViewModel` ，上文阐述了他们关于 `ViewModel` 的设计理念。
4. [RxSwift 中文文档 · RxSwift 中文文档](https://beeth0ven.github.io/RxSwift-Chinese-Documentation/)
5. [http://davesexton.com/blog/post/To-Use-Subject-Or-Not-To-Use-Subject.aspx](http://davesexton.com/blog/post/To-Use-Subject-Or-Not-To-Use-Subject.aspx)
6. [RxSwift + MVVM: how to feed ViewModels](https://medium.com/blablacar-tech/rxswift-mvvm-66827b8b3f10)
7. [GitHub - sergdort/CleanArchitectureRxSwift: Example of Clean Architecture of iOS app using RxSwift](https://github.com/sergdort/CleanArchitectureRxSwift)
8. [是时候学习 RxSwift 了 - Limboy’s HQ](https://limboy.me/tech/2016/12/11/time-to-learn-rxswift.html)
