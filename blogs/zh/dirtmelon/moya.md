---
title: Moya
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/Moya/'
original_language: zh
published: 2020-07-05
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6e0504209082f5d3'
translated: n/a
---

> 原文：[Moya](https://dirtmelon.github.io/posts/Moya/)　·　dirtmelon

## 是什么和为什么

通过 [Alamofire](https://github.com/Alamofire/Alamofire) 可以对 `URLSession` 进行封装，使我们不需要过多关注一些琐碎的细节。但是在 Alamofire 的上层，我们可能还需要再做一层封装，这层封装针对于我们的 App ，更接近业务层。 Moya 正是对应的这层封装。 一般来说 App 的网络架构可能如下图所示：

![diagram](https://raw.githubusercontent.com/dirtmelon/blog-images/main/diagram.png)

可能看到加入 Moya 后，整个 App 的网络层功能非常清晰， App 不会直接与 Alamofire 交互，所有网络请求都是通过 Moya 发起。 Moya 支持以下特性：

- 编译时检测是否使用正确的 `API endpoint` ；
- 通过 enum 的关联值来对不同的 `endpoints` 定义清晰的用法；
- 测试插桩为一等值，使得单元测试变得非常容易；

接入 Moya 后，你不再也不应该直接与 Alamofire 交互，所有的一切都由 Moya 来完成。 Moya 设计得非常灵活，可以满足各个开发者的需求。它更像是一个关于如何看待网络请求的库。 Moya 基本的整体架构如下图所示：

![Moya](https://raw.githubusercontent.com/dirtmelon/blog-images/main/Moya.png)

## 基础类型

Moya 对请求的处理流水线如下图所示： ![68747470733a2f2f7261772e6769746875622e636f6d2f4d6f79612f4d6f79612f6d61737465722f7765622f706970656c696e652e706e67](https://raw.githubusercontent.com/dirtmelon/blog-images/main/68747470733a2f2f7261772e6769746875622e636f6d2f4d6f79612f4d6f79612f6d61737465722f7765622f706970656c696e652e706e67.png)

`Target(TargetType)` 提供给开发者用于定义各个接口的参数， `URL` ， 测试数据等， 而 `Endpoint` 则是 `Target` 和 `URLRequest` 的中间态，所有 `URLRequest` 到最后都会经过 `Endpoint` 生成。

### TargetType

`TargetType` 的定义如下：

```swift
public protocol TargetType {

    var baseURL: URL { get }

    /// path 追加到 baseURL 中来构成当前请求的完整 URL
    var path: String { get }

    /// HTTP Method ，内部其实是 Alamofire.HTTPMethod
    var method: Moya.Method { get }

    /// 插桩测试时所用到的数据
    var sampleData: Data { get }

    /// 所需要执行的 HTTP 任务
    var task: Task { get }

	  /// 执行请求时的验证类型，默认为 .none
    var validationType: ValidationType { get }

    /// 用于设置请求的 headers
    var headers: [String: String]? { get }
}
```

可以看到 `TargetType` 定义了一个请求所需要的基本数据，是开发者与 Moya 进行交互的第一层入口。 Moya 建议定义 `enum` 类型来支持 `TargetType` ，这样可以通过 `switch case` 和关联值来对不同的接口设置不同的数据，在添加了新的 `case` 后，编译器也可以及时检查和报错来提示我们编写对应的代码，如果使用 `class` 或者 `struct` ，就会失去这个优点。虽然使用 `enum` 需要编写大量的 `switch case` ，但在更加安全。

1. `baseURL` 属性对于同一个 `enum` 类型来说应该是相同的，也就是说我们可以根据 `baseURL` 的不同把接口放到不同的 `enum` 类型中，如果说一个 `enum` 中包含不同的 `baseURL` ，那么可以考虑拆成 多个 `enum` ；
2. `task` 属性用于表示你如何发送/接收数据，如何添加数据，文件和数据流到请求的 body 中；
3. `validationType` 属性用于定于哪些状态码是可以通过验证的；

### Endpoint

`Endpoint` 由 `TargetType` 转换而成，基本属性和初始化方法如下：

```swift
open class Endpoint {
    public typealias SampleResponseClosure = () -> EndpointSampleResponse

    /// 用于生成 URLRequest 的 string
    public let url: String

    /// 插桩测试时返回的数据 `EndpointSampleResponse`
    public let sampleResponseClosure: SampleResponseClosure

    /// HTTP Method ，内部其实是 Alamofire.HTTPMethod
    public let method: Moya.Method

    /// 所需要执行的 HTTP 任务
    public let task: Task

    /// 用于设置请求的 headers
    public let httpHeaderFields: [String: String]?

	  /// 初始化方法
    public init(url: String,
                sampleResponseClosure: @escaping SampleResponseClosure,
                method: Moya.Method,
                task: Task,
                httpHeaderFields: [String: String]?) {

        self.url = url
        self.sampleResponseClosure = sampleResponseClosure
        self.method = method
        self.task = task
        self.httpHeaderFields = httpHeaderFields
    }

	///
}
```

`Endpoint` 和 `TargetType` 没有多大区别，为什么需要 `Endpoint` 这个中间态呢？后面再来解释下这个问题。在了解 `TargetType` 和 `Endpoint` 后，我们就可以进一步对 Moya 发起请求的流程进行探索。

### MoyaProvider

```swift
open class MoyaProvider<Target: TargetType>: MoyaProviderType {

    /// 用于 Target 转换为 Endpoint 的闭包
    public typealias EndpointClosure = (Target) -> Endpoint

    /// 用于判断 URLRequest 是否需要执行以及对 URLRequest 进行哪些设置的闭包
    public typealias RequestResultClosure = (Result<URLRequest, MoyaError>) -> Void

    /// 用于 Endpoint 转换为 RequestResultClosure 的闭包
    public typealias RequestClosure = (Endpoint, @escaping RequestResultClosure) -> Void

    /// 用于判断 Target 是否需要和如何进行插桩测试
    public typealias StubClosure = (Target) -> Moya.StubBehavior

    public let endpointClosure: EndpointClosure

    public let requestClosure: RequestClosure

    public let stubClosure: StubClosure

	  /// Alamofire 的 session ，用于发起请求
    public let session: Session

    /// 插件
    public let plugins: [PluginType]

	  /// 是否过滤重复的请求，如果有重复的请求在处理中，就不会发起新的请求而是把 completion 添加到对应的 inflightCompletionBlocks 中，根据 Endpoint 来判断是否为重复的请求
    public let trackInflights: Bool

    open internal(set) var inflightRequests: [Endpoint: [Moya.Completion]] = [:]

    /// 与 Alamfire 的 callbackQueue 进行隔离，如果没有定义就会调用 Alamofire 默认的 queue （ main queue ）
    let callbackQueue: DispatchQueue?

    let lock: NSRecursiveLock = NSRecursiveLock()

    public init(endpointClosure: @escaping EndpointClosure = MoyaProvider.defaultEndpointMapping,
                requestClosure: @escaping RequestClosure = MoyaProvider.defaultRequestMapping,
                stubClosure: @escaping StubClosure = MoyaProvider.neverStub,
                callbackQueue: DispatchQueue? = nil,
                session: Session = MoyaProvider<Target>.defaultAlamofireSession(),
                plugins: [PluginType] = [],
                trackInflights: Bool = false) {
        self.endpointClosure = endpointClosure
        self.requestClosure = requestClosure
        self.stubClosure = stubClosure
        self.session = session
        self.plugins = plugins
        self.trackInflights = trackInflights
        self.callbackQueue = callbackQueue
    }

	  ///
}
```

可以看到 `MoyaProvider` 支持了 `MoyaProviderType` 协议：

```swift
public protocol MoyaProviderType: AnyObject {

    associatedtype Target: TargetType

    func request(_ target: Target, callbackQueue: DispatchQueue?, progress: Moya.ProgressBlock?, completion: @escaping Moya.Completion) -> Cancellable
}
```

抽离 `MoyaProvider` 的最小接口，用于跟 `Reactive` 框架交互。 同时 `MoyaProvider` 也使用了范型 `<Target: TargetType>` ，在声明时需要定义 `Target` 的具体类型，如：

```swift
let provider = MoyaProvider<UserAPI>()
```

大多数情况下都不需要关心 `MoyaProvider` 的其它初始化参数， Moya 也为我们提供了一系列的默认初始化参数。

`defaultEndpointMapping` 对 `Target` 不做任何处理，直接生成 `Endpoint`:

```swift
final class func defaultEndpointMapping(for target: Target) -> Endpoint {
    return Endpoint(
        url: URL(target: target).absoluteString,
        sampleResponseClosure: { .networkResponse(200, target.sampleData) },
        method: target.method,
        task: target.task,
        httpHeaderFields: target.headers
    )
}
```

`defaultRequestMapping` 将 `Endpoint` 转换为 `RequestResultClosure` ，可以异步执行，默认实现也不做任何处理，只鹅姐通过 `Endpoint` 的 `urlRequest()` 方法生成 `URLRequest` ，或者返回对应的 `MoyaError` ：

```swift
final class func defaultRequestMapping(for endpoint: Endpoint, closure: RequestResultClosure) {
    do {
        let urlRequest = try endpoint.urlRequest()
        closure(.success(urlRequest))
    } catch MoyaError.requestMapping(let url) {
        closure(.failure(MoyaError.requestMapping(url)))
    } catch MoyaError.parameterEncoding(let error) {
        closure(.failure(MoyaError.parameterEncoding(error)))
    } catch {
        closure(.failure(MoyaError.underlying(error, nil)))
    }
}
```

`stubClosure` 默认为 `MoyaProvider.neverStub` ，不进行测试插桩：

```swift
final class func neverStub(_: Target) -> Moya.StubBehavior {
    return .never
}
```

`defaultAlamofireSession()` 默认使用 `URLSessionConfiguration.default` 来生成 `Session` ，这里会设置 `startRequestsImmediately` 为 `false` ，如果不设置为 `false` ， Alamofire 在创建 `Request` 后就会直接发起请求，即使在进行插桩测试的情况下。但是在 Alamofire5 中这块逻辑已经做了调整，在创建 `Request` 时不会直接发起请求，只有在调用 `.response` 相关方法添加响应处理后才会发起请求。

```swift
final class func defaultAlamofireSession() -> Session {
    let configuration = URLSessionConfiguration.default
    configuration.headers = .default

    return Session(configuration: configuration, startRequestsImmediately: false)
}
```

### PluginType

Moya 提供的插件协议 ，用于请求发送或者接收时调用，这里也使用协议对具体的对象类型进行抽象， `MoyaProvider` 不需要知道具体的类型是什么，只需要实现 `PluginType` 协议即可：

```swift
public protocol PluginType {
    /// 发送请求前调用，可以用来对 URLRequest 进行修改
    func prepare(_ request: URLRequest, target: TargetType) -> URLRequest

    /// 发送请求前最后调用的方法，不管是插桩测试还是真正的网络请求都会调用这个方法
    func willSend(_ request: RequestType, target: TargetType)

	  /// 接收到响应结果时调用，会先调用该方法后再调用 MoyaProvider 调用自己的 completionHandler
    func didReceive(_ result: Result<Moya.Response, MoyaError>, target: TargetType)

	  /// 响应结果的预处理器
    func process(_ result: Result<Moya.Response, MoyaError>, target: TargetType) -> Result<Moya.Response, MoyaError>
}
```

插件请求前的处理借由 Alamofire 的 `RequestInterceptor` 协议来实现。每次发起请求时， `MoyaProvider` 都会生成一个 ` MoyaRequestInterceptor` ，其实现如下：

```swift
final class MoyaRequestInterceptor: RequestInterceptor {
    private let lock: NSRecursiveLock = NSRecursiveLock()

    var prepare: ((URLRequest) -> URLRequest)?
    private var internalWillSend: ((URLRequest) -> Void)?

    var willSend: ((URLRequest) -> Void)? {
        get {
            lock.lock(); defer { lock.unlock() }
            return internalWillSend
        }

        set {
            lock.lock(); defer { lock.unlock() }
            internalWillSend = newValue
        }
    }

    init(prepare: ((URLRequest) -> URLRequest)? = nil, willSend: ((URLRequest) -> Void)? = nil) {
        self.prepare = prepare
        self.willSend = willSend
    }

    func adapt(_ urlRequest: URLRequest, for session: Alamofire.Session, completion: @escaping (Result<URLRequest, Error>) -> Void) {
        // 先调 prepare 对 urlRequest 进行处理，再调 willSend 。
		  let request = prepare?(urlRequest) ?? urlRequest
        willSend?(request)
        completion(.success(request))
    }
}

/// 初始化
private func interceptor(target: Target) -> MoyaRequestInterceptor {
    return MoyaRequestInterceptor(prepare: { [weak self] urlRequest in
		  // 使用 reduce 简化代码
        return self?.plugins.reduce(urlRequest) { $1.prepare($0, target: target) } ?? urlRequest
    })
}
```

## 请求流程

### 请求前的处理

大多数情况下我们都是通过 `MoyaProvider` 下面的接口来发起请求：

```swift
open func request(_ target: Target,
                  callbackQueue: DispatchQueue? = .none,
                  progress: ProgressBlock? = .none,
                  completion: @escaping Completion) -> Cancellable {

    let callbackQueue = callbackQueue ?? self.callbackQueue
    return requestNormal(target, callbackQueue: callbackQueue, progress: progress, completion: completion)
}
```

这个接口的返回结果使用了 `Cancellable` 协议进行封装：

```swift
public protocol Cancellable {
	  /// 判断请求是否已经取消
    var isCancelled: Bool { get }
	  /// 取消请求
    func cancel()
}
```

可以看到也是同样使用协议提供了最小接口和对实际的对象进行抽象，调用方不需要知道具体的对象是什么，只需要通过 `Cancellable` 的接口来进行相关调用。 经过一层 `callbackqueue` 的处理后会调用下面的方法，方法有点长，下面拆开几部分来讲解下：

```swift
func requestNormal(_ target: Target, callbackQueue: DispatchQueue?, progress: Moya.ProgressBlock?, completion: @escaping Moya.Completion) -> Cancellable {
	  /// 1.
    let endpoint = self.endpoint(target)
    /// 2.
    let stubBehavior = self.stubClosure(target)
    /// 3.
    let cancellableToken = CancellableWrapper()

    // 4.
    let pluginsWithCompletion: Moya.Completion = { result in
        let processedResult = self.plugins.reduce(result) { $1.process($0, target: target) }
        completion(processedResult)
    }

    ///
}
```

1. 将 `Target` 转换为对应的 `Endpoint` ：

```swift
open func endpoint(_ token: Target) -> Endpoint {
        return endpointClosure(token)
}
```

1. 获取 Target 对应的插桩行为；
2. 生成一个 `CancellableWrapper` ：

```swift
internal class CancellableWrapper: Cancellable {
    internal var innerCancellable: Cancellable = SimpleCancellable()

    var isCancelled: Bool { return innerCancellable.isCancelled }

    internal func cancel() {
        innerCancellable.cancel()
    }
}

internal class SimpleCancellable: Cancellable {
    var isCancelled = false
    func cancel() {
        isCancelled = true
    }
}
```

`CancellableWrapper` 内部使用一个 `SimpleCancellable` 来实现 `Cancellable` 协议，如果进行插桩测试，就直接使用 `SimpleCancellable` ，如果发起实际请求，就会生成对应的 `Cancellable` ，替换 `SimpleCancellable` ；

1. 使用 `reduce`调用插件的 `process` 方法对相应结果进行处理；

做完上面的预处理后，就会判断是否需要处理重复的请求，进行相关的处理：

```swift
if trackInflights {
    lock.lock()
	  /// 根据 Endpoint 获取对应的回调
    var inflightCompletionBlocks = self.inflightRequests[endpoint]
    /// 追加新的 pluginsWithCompletion
    inflightCompletionBlocks?.append(pluginsWithCompletion)
    self.inflightRequests[endpoint] = inflightCompletionBlocks
    lock.unlock()

    /// 如果 inflightCompletionBlocks 不为空，则表示有重复的请求在处理中，不需要发起新的请求，返回 cancellableToken 即可
    if inflightCompletionBlocks != nil {
        return cancellableToken
    } else {
        /// 否则设置对应的回调到 inflightRequests 中
        lock.lock()
        self.inflightRequests[endpoint] = [pluginsWithCompletion]
        lock.unlock()
    }
}
```

接下来就会设置一个 `performNetworking` 的 `closure` ：

```swift
let performNetworking = { (requestResult: Result<URLRequest, MoyaError>) in
    /// 1.
	  if cancellableToken.isCancelled {
        self.cancelCompletion(pluginsWithCompletion, target: target)
        return
    }

    var request: URLRequest!
	  /// 2.
    switch requestResult {
    case .success(let urlRequest):
        request = urlRequest
    case .failure(let error):
        pluginsWithCompletion(.failure(error))
        return
    }
	  /// 3.
    let networkCompletion: Moya.Completion = { result in
      if self.trackInflights {
        self.inflightRequests[endpoint]?.forEach { $0(result) }

        self.lock.lock()
        self.inflightRequests.removeValue(forKey: endpoint)
        self.lock.unlock()
      } else {
        pluginsWithCompletion(result)
      }
    }
	  /// 4.
    cancellableToken.innerCancellable = self.performRequest(target, request: request, callbackQueue: callbackQueue, progress: progress, completion: networkCompletion, endpoint: endpoint, stubBehavior: stubBehavior)
}

/// 5.
requestClosure(endpoint, performNetworking)

return cancellableToken
```

1. 判断请求是否已经取消，如果已经取消就不用发起请求；
2. 判断 `requestRequest` 是否为 `.success` ，如果不是则调用 `pluginsWithCompletion` 处理对应的 `error` ；
3. 生成 `networkCompletion` ，也是根据 `trackInflights` 调用不同的 `closure` ；
4. 调用 `performRequest` 执行请求，同时替换 `cancellableToken` 的 `innerCancellable` ；
5. 调用 `requestClosure` 来将 `Endpoint` 转换为 `URLRequest` ，转换完成后则调用 `performNetworking` ，而上述步骤也都是在 `performNetworking` 内执行，之所以使用 `closure` 来进行处理，是为了支持异步转换，调用方可以在异步将 `Endpoint` 转换为 `URLRequest` 后再调用 `performNetworking` ；

### 发起请求

`performRequest` 会根据是否需要进行插桩测试来调用不同的方法：

1. 如果进行插桩测试，就调用 `stubRequest` ；
2. 如果不进行插桩测试，就调用 `sendRequest` ；

#### stubRequest

当进行插桩测试时，不会发起真正的网络请求，而是通过 `Endpoint` 获取对应的假数据，进行回调：

```swift
open func stubRequest(_ target: Target, request: URLRequest, callbackQueue: DispatchQueue?, completion: @escaping Moya.Completion, endpoint: Endpoint, stubBehavior: Moya.StubBehavior) -> CancellableToken {
    let callbackQueue = callbackQueue ?? self.callbackQueue
    /// 1.
    let cancellableToken = CancellableToken { }
    /// 2.
    let preparedRequest = notifyPluginsOfImpendingStub(for: request, target: target)
    let plugins = self.plugins
	  /// 3.
    let stub: () -> Void = createStubFunction(cancellableToken, forTarget: target, withCompletion: completion, endpoint: endpoint, plugins: plugins, request: preparedRequest)
    switch stubBehavior {
    case .immediate:
        switch callbackQueue {
        case .none:
            stub()
        case .some(let callbackQueue):
            callbackQueue.async(execute: stub)
        }
    case .delayed(let delay):
        let killTimeOffset = Int64(CDouble(delay) * CDouble(NSEC_PER_SEC))
        let killTime = DispatchTime.now() + Double(killTimeOffset) / Double(NSEC_PER_SEC)
        (callbackQueue ?? DispatchQueue.main).asyncAfter(deadline: killTime) {
            stub()
        }
    case .never:
        fatalError("Method called to stub request when stubbing is disabled.")
    }

    return cancellableToken
}
```

1. 生成 `CancellableToken` ，由于不会发起真正的请求，所以这里的 `CancellableToken` 没有包含对应的 `Request` ， `cancelAction` 也是一个空的实现；
2. 调用插件的相关方法，这里有调用 `Request` 的 `cancel()` 方法，其实在 Alamofire5 里是不需要调用 `cancel()` 方法来取消请求了，因为 Alamofire5 里只有在添加 `response` 后才会发起请求，如果进行插桩测试是不会添加 `responnse` 的：

```swift
func notifyPluginsOfImpendingStub(for request: URLRequest, target: Target) -> URLRequest {
    let alamoRequest = session.request(request)
    alamoRequest.cancel()

    let preparedRequest = plugins.reduce(request) { $1.prepare($0, target: target) }
	  /// 使用 RequestTypeWrapper 进行封装，抽象成 RequestType 协议
    let stubbedAlamoRequest = RequestTypeWrapper(request: alamoRequest, urlRequest: preparedRequest)
    plugins.forEach { $0.willSend(stubbedAlamoRequest, target: target) }

    return preparedRequest
}
```

1. 而 `createStubFunction` 则会进行验证和经由 `Endpoint` 的 `sampleResponseClosure` 来获取对应的假数据，同时也会调用插件的对应方法；

#### sendRequest

```swift
func sendRequest(_ target: Target, request: URLRequest, callbackQueue: DispatchQueue?, progress: Moya.ProgressBlock?, completion: @escaping Moya.Completion) -> CancellableToken {
    /// 1.
    let interceptor = self.interceptor(target: target)
    let initialRequest = session.request(request, interceptor: interceptor)
    /// 2.
    setup(interceptor: interceptor, with: target, and: initialRequest)

    let validationCodes = target.validationType.statusCodes
    let alamoRequest = validationCodes.isEmpty ? initialRequest : initialRequest.validate(statusCode: validationCodes)
    /// 3.
    return sendAlamofireRequest(alamoRequest, target: target, callbackQueue: callbackQueue, progress: progress, completion: completion)
}
```

1. 生成 `MoyaRequestInterceptor` ，用于调用插件对应的方法；
2. 设置 `interceptor` 的 `willSend` ；
3. 调用 Alamofire 的方法发送请求；

```swift
func sendAlamofireRequest<T>(_ alamoRequest: T, target: Target, callbackQueue: DispatchQueue?, progress progressCompletion: Moya.ProgressBlock?, completion: @escaping Moya.Completion) -> CancellableToken where T: Requestable, T: Request {
    /// 1.
    let plugins = self.plugins
    var progressAlamoRequest = alamoRequest
    let progressClosure: (Progress) -> Void = { progress in
        let sendProgress: () -> Void = {
            progressCompletion?(ProgressResponse(progress: progress))
        }

        if let callbackQueue = callbackQueue {
            callbackQueue.async(execute: sendProgress)
        } else {
            sendProgress()
        }
    }

    /// 2.
    if progressCompletion != nil {
        switch progressAlamoRequest {
        case let downloadRequest as DownloadRequest:
            if let downloadRequest = downloadRequest.downloadProgress(closure: progressClosure) as? T {
                progressAlamoRequest = downloadRequest
            }
        case let uploadRequest as UploadRequest:
            if let uploadRequest = uploadRequest.uploadProgress(closure: progressClosure) as? T {
                progressAlamoRequest = uploadRequest
            }
        case let dataRequest as DataRequest:
            if let dataRequest = dataRequest.downloadProgress(closure: progressClosure) as? T {
                progressAlamoRequest = dataRequest
            }
        default: break
        }
    }
	  /// 3.
    let completionHandler: RequestableCompletion = { response, request, data, error in
        let result = convertResponseToResult(response, request: request, data: data, error: error)
        plugins.forEach { $0.didReceive(result, target: target) }
        if let progressCompletion = progressCompletion {
            let value = try? result.get()
            switch progressAlamoRequest {
            case let downloadRequest as DownloadRequest:
                progressCompletion(ProgressResponse(progress: downloadRequest.downloadProgress, response: value))
            case let uploadRequest as UploadRequest:
                progressCompletion(ProgressResponse(progress: uploadRequest.uploadProgress, response: value))
            case let dataRequest as DataRequest:
                progressCompletion(ProgressResponse(progress: dataRequest.downloadProgress, response: value))
            default:
                progressCompletion(ProgressResponse(response: value))
            }
        }
        completion(result)
    }

    progressAlamoRequest = progressAlamoRequest.response(callbackQueue: callbackQueue, completionHandler: completionHandler)

    progressAlamoRequest.resume()

    return CancellableToken(request: progressAlamoRequest)
}
```

1. 获取插件，生成对应的 `progressClosure` ；
2. 这里不太明白为什么先生成 `progressClosure` 再通过 `progressCompletion` 判断是否使用，为什么不通过 `progressCompletion` 一起判断？
3. 生成 `completionHandler` ，这一步的目的是为了将 Alamofire 的 `response` 转换为 Moya 所需要的格式，调用插件的 `didReceive` 方法；

至此，已经走完了 Moya 发送请求和处理相应结果的基本流程，可以看到 Moya 在 Alamofire 的基础上再提供了一层封装，简单易用，只需要进行少量的定义就可以直接使用，也提供了足够灵活的插件和入口给调用方使用。

## 一些总结

### 使用协议进行抽象

Moya 中使用了协议来对接口进行抽象，如`TargetType` ， `Cancellable` 和 `PluginType` 等，使用协议可以隐藏具体的类型，也可以通过 `extension` 来提供默认实现：

```swift
public extension TargetType {
    var validationType: ValidationType {
        return .none
    }
}
```

### 借用 enum 实现安全检查

Moya 中也有使用 enum 来调用不同的逻辑，而 enum 在我们没有实现对应的逻辑时则会报错，这样可以避免我们遗漏 case ：

```swift
public enum StubBehavior {

    /// Do not stub.
    case never

    /// Return a response immediately.
    case immediate

    /// Return a response after a delay.
    case delayed(seconds: TimeInterval)
}

public enum EndpointSampleResponse {

    /// The network returned a response, including status code and data.
    case networkResponse(Int, Data)

    /// The network returned response which can be fully customized.
    case response(HTTPURLResponse, Data)

    /// The network failed to send the request, or failed to retrieve a response (eg a timeout).
    case networkError(NSError)
}
```

### 对 Alamofire 的类型进行桥接

由于 Moya 是在 Alamofire 基础上进行的封装，很多类型都是由 Alamofire 提供，使用类型桥接可以把 Alamofire 隐藏掉，调用方在使用时完全不知道 Alamofire 的存在：

```swift
public typealias Session = Alamofire.Session

/// Represents an HTTP method.
public typealias Method = Alamofire.HTTPMethod

/// Choice of parameter encoding.
public typealias ParameterEncoding = Alamofire.ParameterEncoding
public typealias JSONEncoding = Alamofire.JSONEncoding
public typealias URLEncoding = Alamofire.URLEncoding

/// Multipart form.
public typealias RequestMultipartFormData = Alamofire.MultipartFormData

/// Multipart form data encoding result.
public typealias DownloadDestination = Alamofire.DownloadRequest.Destination

/// Represents Request interceptor type that can modify/act on Request
public typealias RequestInterceptor = Alamofire.RequestIntercepto
```

为了避免把 Alamofire 暴露给插件，使用 `RequestType` 对 Alamofire 的 `Request` 进行抽象：

```swift
extension Request: RequestType {
    public var sessionHeaders: [String: String] {
        return delegate?.sessionConfiguration.httpAdditionalHeaders as? [String: String] ?? [:]
    }
}
```

### 高阶函数

Moya 的 `Response` 提供了不少高阶函数给调用方使用，如 `filter` ，`mapJSON()` 等：

#### Filter

```swift
func filter<R: RangeExpression>(statusCodes: R) throws -> Response where R.Bound == Int {
    guard statusCodes.contains(statusCode) else {
        throw MoyaError.statusCode(self)
    }
    return self
}

func filter(statusCode: Int) throws -> Response {
    return try filter(statusCodes: statusCode...statusCode)
}

func filterSuccessfulStatusCodes() throws -> Response {
    return try filter(statusCodes: 200...299)
}
```

使用 `RangeExpression` 以支持字面量的 Range 参数， `filter` 会过滤掉所有 `statusCode` 不在对应范围的响应结果，并抛出一个 `MoyaError.statusCode` 。

#### MapJSON

```swift
func mapJSON(failsOnEmptyData: Bool = true) throws -> Any {
    do {
        return try JSONSerialization.jsonObject(with: data, options: .allowFragments)
    } catch {
        if data.count < 1 && !failsOnEmptyData {
            return NSNull()
        }
        throw MoyaError.jsonMapping(self)
    }
}
```

`mapJSON()` 会将响应结果转换为 JSONObject ，如果失败则抛出 `MoyaError.jsonMapping` 。

更多的用法可以这个文档： [Moya/Response.md](https://github.com/Moya/Moya/blob/master/docs/Examples/Response.md)

### 类型擦除

#### Encodable

Moya 的 Task 支持 `Encodable` 进行编码：

```swift
/// A request body set with `Encodable` type
case requestJSONEncodable(Encodable)
```

在 `Endpoint` 生成对应的 `URLRequest` 时会通过 `Encodable` 参数来设置 `httpBody` ：

```swift
internal extension URLRequest {
    mutating func encoded(encodable: Encodable, encoder: JSONEncoder = JSONEncoder()) throws -> URLRequest {
        do {
            let encodable = AnyEncodable(encodable)
            httpBody = try encoder.encode(encodable)

            let contentTypeHeaderName = "Content-Type"
            if value(forHTTPHeaderField: contentTypeHeaderName) == nil {
                setValue("application/json", forHTTPHeaderField: contentTypeHeaderName)
            }

            return self
        } catch {
            throw MoyaError.encodableMapping(error)
        }
    }
}
```

这里需要声明方法为 `mutating` ，因为方法会修改属性。可以看到方法会通过 `encodable` 参数生成一个 `AnyEncodable struct` ：

```swift
struct AnyEncodable: Encodable {

    private let encodable: Encodable

    public init(_ encodable: Encodable) {
        self.encodable = encodable
    }

    func encode(to encoder: Encoder) throws {
        try encodable.encode(to: encoder)
    }
}
```

通过 `AnyEncodable` 可以把传进行来的协议参数转换成具体的值参数，而这个参数是遵循 `Encodable` 协议的。这是在 `Swift` 上进行类型擦除的一种方式，把具体的类型隐藏起来。为什么要进行类型擦除呢？因为 `JSONEncoder` 的 `encode` 方法只接收具体的类型参数，不接受协议参数：

```swift
open func encode<T>(_ value: T) throws -> Data where T : Encodable
```

它表示 `T` 为遵循了 `Encodable` 协议的类型，也就是说我们无法通过以下方式调用 `encode` 方法：

```swift
mutating func encoded(encodable: Encodable, encoder: JSONEncoder = JSONEncoder()) throws -> URLRequest {
    do {
        httpBody = try encoder.encode(encodable)
        return self
    } catch {
        throw MoyaError.encodableMapping(error)
    }
}
```

`Value of protocol type ‘Encodable’ cannot conform to ‘Encodable’; only struct/enum/class types can conform to protocols` ，我们无法直接使用 `Encodable` 参数。 至于为什么 `JSONEncoder` 需要 `encode` 为具体的类型，而不是协议，又是另外一个问题了。

#### MultiTarget

`MoyaProvider` 在使用时需要指定 `TargetType` 的类型，而 App 中可能会根据 `baseURL` 分成多个 `TargetType` ，这样导致我们需要根据不同的 `TargetType` 提供不同的 `MoyaProvider` ，那么有没有办法只使用一个 `MoyaProvider` 就可以支持所有的 `TargetType` ？答案是使用 `MultiTarget` ：

```swift
enum MultiTarget: TargetType {
    case target(TargetType)

    public init(_ target: TargetType) {
        self = MultiTarget.target(target)
    }
    public var path: String {
        return target.path
    }
    public var baseURL: URL {
        return target.baseURL
    }
    public var method: Moya.Method {
        return target.method
    }
    public var sampleData: Data {
        return target.sampleData
    }
    public var task: Task {
        return target.task
    }
    public var validationType: ValidationType {
        return target.validationType
    }
    public var headers: [String: String]? {
        return target.headers
    }
    public var target: TargetType {
        switch self {
        case .target(let target): return target
        }
    }
}
```

`MultiTarget` 为 `enum` 类型，只有一个由 `TargetType` 生成的 `case` ，内部属性也是对应的 `TargetType` ，这就可以将协议抽象成具体的类型。用法如下：

```swift
let provider = MoyaProvider<MultiTarget>(plugins: [NetworkLoggerPlugin(configuration: .init(logOptions: .verbose))])

provider.request(MultiTarget(GitHub.userRepositories(username))) { result in
	/// ...
}
```

### 与响应式框架交互

#### RxSwift

```swift
extension Reactive where Base: MoyaProviderType {
    func request(_ token: Base.Target, callbackQueue: DispatchQueue? = nil) -> Single<Response> {
        return Single.create { [weak base] single in
            let cancellableToken = base?.request(token, callbackQueue: callbackQueue, progress: nil) { result in
                switch result {
                case let .success(response):
                    single(.success(response))
                case let .failure(error):
                    single(.error(error))
                }
            }

            return Disposables.create {
                cancellableToken?.cancel()
            }
        }
    }
}
```

普通请求返回的是 `Single` ， `Single` 是 `Observable` 的另外一个版本，不可以发出多个元素，只能发出一个元素或者一个 `error` 事件，这和网络请求的流程一致，每个请求只能返回一个响应结果。

带有进度的请求：

```swift
func requestWithProgress(_ token: Base.Target, callbackQueue: DispatchQueue? = nil) -> Observable<ProgressResponse> {
    let progressBlock: (AnyObserver) -> (ProgressResponse) -> Void = { observer in
        return { progress in
            observer.onNext(progress)
        }
    }

    let response: Observable<ProgressResponse> = Observable.create { [weak base] observer in
        let cancellableToken = base?.request(token, callbackQueue: callbackQueue, progress: progressBlock(observer)) { result in
            switch result {
            case .success:
                observer.onCompleted()
            case let .failure(error):
                observer.onError(error)
            }
        }

        return Disposables.create {
            cancellableToken?.cancel()
        }
    }

    // Accumulate all progress and combine them when the result comes
    return response.scan(ProgressResponse()) { last, progress in
        let progressObject = progress.progressObject ?? last.progressObject
        let response = progress.response ?? last.response
        return ProgressResponse(progress: progressObject, response: response)
    }
}
```

这里使用 `Observable` ，因为在请求过程中会调用 `onNext` 更新进度。使用 `scan` 操作符判断是否需要使用之前的 `response` 。

#### ReactiveCocoa

```swift
func request(_ token: Base.Target, callbackQueue: DispatchQueue? = nil) -> SignalProducer<Response, MoyaError> {
    return SignalProducer { [weak base] observer, lifetime in
        let cancellableToken = base?.request(token, callbackQueue: callbackQueue, progress: nil) { result in
            switch result {
            case let .success(response):
                observer.send(value: response)
                observer.sendCompleted()
            case let .failure(error):
                observer.send(error: error)
            }
        }

        lifetime.observeEnded {
            cancellableToken?.cancel()
        }
    }
}
```

由于 `ReactiveCocoa` 没有类似 `RxSwift` 那样的 `Single` ，所以对于普通请求，会在 `send(value: Value)` 之后立即调用 `sendComplete()` 。
