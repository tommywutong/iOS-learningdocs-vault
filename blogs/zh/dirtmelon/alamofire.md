---
title: Alamofire
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/Alamofire/'
original_language: zh
published: 2020-06-15
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:75014b3c70a1eb02'
translated: n/a
---

> 原文：[Alamofire](https://dirtmelon.github.io/posts/Alamofire/)　·　dirtmelon

## 为什么需要一个第三方框架

对于大部分 App 来说都需要跟服务器做数据传输，通常情况下都是通过 HTTPS/HTTP 来完成。 `URLSession` 已经封装得很好，但是如果需要把网络层跟业务层分离开来，我们需要基于 `URLSession` 再做一层封装，对 method ，header ，上传，下载，错误处理等再做一层处理，让业务方在调用的时候更加舒服。 Alamofire 是基于 `URLSession` 进行的封装，使用 Swift 编写的一个优雅的网络框架。本文主要是讲述 Alamofire 的具体逻辑和用法，对应的 Alamofire 版本为 5.2.1 。

## URLSession 和 Alamofire 比较

举一个简单例子来说明下 `URLSession` 和 Alamofire 是如何发起请求的。

```swift
// URLSession
let session = URLSession.shared
let dataTask = session.dataTask(with: URL(string: “https://www.github.com”)!) { (data, response, error) in
  guard let data = data,
    let string = String(data: data, encoding: .utf8) else {
    return
  }
  print(string)
}
dataTask.resume()

// Alamofire
AF.request(“https://www.github.com”)
  .responseString { (response) in
    guard let string = response.value else { return }
    print(string)
}
```

可以看到 Alamofire 简洁之处，不再需要手动创建 `URLSessionDataTask` 和调用 `resume` ，也不需要自己对请求结果进行解码和格式转换。网络请求都需要进行错误处理，参数转换和结果处理，而 Alamofire 都为我们提供了一系列链式调用的处理方法，代码也更容易理解和统一。

## 整体架构

Alamofire 基本的整体架构如下图所示：

![Alamofire](https://raw.githubusercontent.com/dirtmelon/blog-images/main/Alamofire.png)

`Alamofire` 项目结构非常简单清晰，`Alamofire.swift` 只提供一个 `AF` 单例：

```swift
public let AF = Session.default
```

跟 4.0 版本比起来的好处就是不会污染全局的命名空间，且如果 `Session` 添加了新的接口， `Alamofire.swift` 文件也不需要作出改动。

```shell
-- Alamofire.swift
	-- Core
		-- AFError.swift
		-- HTTPHeaders.swift
		-- HTTPMethod.swift
		-- Notifications.swift
		-- ParameterEncoder.swift
		-- ParameterEncoding.swift
		-- Protected.swift
		-- Request.swift
		-- RequestTaskMap.swift
		-- Response.swift
		-- Session.swift
		-- SessionDelegate.swift
		-- URLConvertible+URLRequestConvertible.swift
	-- Extensions
		-- DispatchQueue+Alamofire.swift
		-- OperationQueue+Alamofire.swift
		-- Result+Alamofire.swift
		-- StringEncoding+Alamofire.swift
		-- URLRequest+Alamofire.swift
		-- URLSessionConfiguration+Alamofire.swift
	-- Features
		-- AlamofireExtended.swift
		-- AuthenticationInterceptor.swift
		-- CachedResponseHandler.swift
		-- Combine.swift
		-- EventMonitor.swift
		-- MultipartFormData.swift
		-- MultipartUpload.swift
		-- NetworkReachabilityManager.swift
		-- RedirectHandler.swift
		-- RequestInterceptor.swift
		-- ResponseSerialization.swift
		-- RetryPolicy.swift
		-- ServerTrustEvaluation.swift
		-- URLEncodedFormEncoder.swift
		-- Validation.swift
```

1. `Core` 里面包含的是网络请求过程中必须要调用的部分；
2. `Extensions` 为系统的一些类添加了便捷方法；
3. `Features` 则是 `Alamofire` 提供的一些特定功能，如缓存策略，重试策略，请求结果的处理等；

## 基础解析

为了在熟悉整个请求流程时各个参数，协议的作用，先来熟悉一下请求流程中都有使用到哪些类，协议或者方法。

### AFError

请求错误时的 `enum` 类型，因为网络请求错误的类型较多，所以分了两层，第一层是 `AFError` ，而每个 `error` 也有可能会因应自己的二级分类再定义一个 `enum` 类型，下面是二级 `enum` 类型：

```swift
MultipartEncodingFailureReason // 表单转码错误
ParameterEncodingFailureReason // 参数转码错误
ParameterEncoderFailureReason // 参数转码器错误
  - RequiredComponent // 缺少必要的组件
ResponseValidationFailureReason // 响应数据验证错误
ResponseSerializationFailureReason // 响应数据序列化错误
ServerTrustFailureReason // 服务器验证错误
URLRequestValidationFailureReason // 请求验证错误
```

除此之外，Alamofire 也提供了不少扩展方法给 `Error`和 `AFError` 使用，以求在使用上更便捷。如 `Error` 可以转化为 `AFError` ：

```swift
extension Error {
    /// Returns the instance cast as an `AFError`.
    public var asAFError: AFError? {
        self as? AFError
    }

    public func asAFError(orFailWith message: @autoclosure () -> String, file: StaticString = #file, line: UInt = #line) -> AFError {
        guard let afError = self as? AFError else {
            fatalError(message(), file: file, line: line)
        }
        return afError
    }

    func asAFError(or defaultAFError: @autoclosure () -> AFError) -> AFError {
        self as? AFError ?? defaultAFError()
    }
}
```

这里使用了 `@autoclosure` 来声明对应的 `Closure` 。

1. 使用闭包是为了利用其延迟执行的特性，如果 `Error` 其实是个 `AFError` ，那么我们就不需要获取 `defaultAFError` ，也不需要执行对应的代码，所以这里使用了闭包来传参。
2. 使用 `@autoclosure` 进行声明，这样调用方在调用的时候不需要加上 `{}` ，看起来跟普通的参数一样：

```swift
error.asAFError(or: .responseSerializationFailed(reason: .customSerializationFailed(error: error)))
```

### HTTPHeaders

`HTTPHeaders` 是一个 `Struct` 类型，保存了 HTTP 头的一些 name / value 配对。 `HTTPHeader` 则封装了一些快速生成 HTTP 头属性的方法。你可以使用 `URLSessionConfiguration.af.default` 来获取默认的 `HTTPHeaders` 对应的 `URLSessionConfiguration` 。 为了方便直接生成 `HTTPHeaders` ， 还支持 `ExpressibleByDictionaryLiteral` 和 `ExpressibleByArrayLiteral` 协议，可以直接使用 `Dictionary` 和 `Array` 的 字面表达式来直接生成：

```swift
extension HTTPHeaders: ExpressibleByDictionaryLiteral {
    public init(dictionaryLiteral elements: (String, String)…) {
        self.init()

        elements.forEach { update(name: $0.0, value: $0.1) }
    }
}

extension HTTPHeaders: ExpressibleByArrayLiteral {
    public init(arrayLiteral elements: HTTPHeader…) {
        self.init(elements)
    }
}

// 这里的 .authorization 和 .accpet 都是 HTTPHeader 中为了方便我们调用提供的初始化方法。
let headers: HTTPHeaders = [
    .authorization(username: "Username”, password: “Password"),
    .accept(“application/json”)
]
```

对于一些系统的类，也提供了便捷方法来获取 `HTTPHeaders` ：

```swift
extension URLRequest {
    public var headers: HTTPHeaders {
        get { allHTTPHeaderFields.map(HTTPHeaders.init) ?? HTTPHeaders() }
        set { allHTTPHeaderFields = newValue.dictionary }
    }
}

extension HTTPURLResponse {
    public var headers: HTTPHeaders {
        (allHeaderFields as? [String: String]).map(HTTPHeaders.init) ?? HTTPHeaders()
    }
}

public extension URLSessionConfiguration {
    var headers: HTTPHeaders {
        get { (httpAdditionalHeaders as? [String: String]).map(HTTPHeaders.init) ?? HTTPHeaders() }
        set { httpAdditionalHeaders = newValue.dictionary }
    }
}
```

在设定 HTTP 头时我们不再需要进行字符串的 hardcode ，通过 `ExpressibleByDictionaryLiteral` 和 `ExpressibleByArrayLiteral` 这两个协议，结合 `HTTPHeaders` 和 `HTTPHeader` 可以很舒服地设置相关的属性。

### Notifications

`Notifications.swift` 的结构分为几部分。 第一部分是 `Request` 的扩展，定义了请求相关的通知，通过 `static let` 定义相关通知，方便调用：

```swift
public extension Request {
    static let didResumeNotification = Notification.Name(rawValue: “org.alamofire.notification.name.request.didResume”)
}

// 调用
Request.didResumeNotification
```

第二部分是 `Notification` 和 `NotificationCenter` 的扩展，方便与 `Request` 进行交互：

```swift
extension Notification {
    /// 把userInfo 的 Request 通过 String.requestKey 封装起来，方便获取
    public var request: Request? {
        return userInfo?[String.requestKey] as? Request
    }

    /// 通过 Request 和 NotificationName 生成 Notification ，不需要每次都手动设置 userInfo
    init(name: Notification.Name, request: Request) {
        self.init(name: name, object: nil, userInfo: [String.requestKey: request])
    }
}
```

第三部分定义了一个 `AlamofireNotifications` 类，遵循 `EventMonitor`协议，通过 `AlamofireNotifications` 我们可以在需要的地方添加 `Request` 的相关通知，灵活地实现对应的方法，不需要统一配置，而发送通知的时机也嵌入到 `EventMonitor` 的逻辑中，不需要额外处理：

```swift
/// `EventMonitor` that provides Alamofire’s notifications.
public final class AlamofireNotifications: EventMonitor {
    public func requestDidResume(_ request: Request) {
        NotificationCenter.default.postNotification(named: Request.didResumeNotification, with: request)
    }

    public func requestDidSuspend(_ request: Request) {
        NotificationCenter.default.postNotification(named: Request.didSuspendNotification, with: request)
    }

    public func requestDidCancel(_ request: Request) {
        NotificationCenter.default.postNotification(named: Request.didCancelNotification, with: request)
    }

    public func requestDidFinish(_ request: Request) {
        NotificationCenter.default.postNotification(named: Request.didFinishNotification, with: request)
    }

    public func request(_ request: Request, didResumeTask task: URLSessionTask) {
        NotificationCenter.default.postNotification(named: Request.didResumeTaskNotification, with: request)
    }

    public func request(_ request: Request, didSuspendTask task: URLSessionTask) {
        NotificationCenter.default.postNotification(named: Request.didSuspendTaskNotification, with: request)
    }

    public func request(_ request: Request, didCancelTask task: URLSessionTask) {
        NotificationCenter.default.postNotification(named: Request.didCancelTaskNotification, with: request)
    }

    public func request(_ request: Request, didCompleteTask task: URLSessionTask, with error: AFError?) {
        NotificationCenter.default.postNotification(named: Request.didCompleteTaskNotification, with: request)
    }
}
```

### ParameterEncoder

`ParameterEncoder` 协议，一个参数编码器，用来编码支持 `Encodable` 协议类型到 `URLRequest` 中，只需要实现一个方法用于处理 `parameters` 并生成对应的 `URLRequest` ：

```swift
func encode<Parameters: Encodable>(_ parameters: Parameters?, into request: URLRequest) throws -> URLRequest
```

`JSONParameterEncoder` 用于 `JSON` 的编码，如果 `URLRequest` 的请求头没有设置 `Content-Type` ，它就会设置为 `application/json` 。 `JSONParameterEncoder` 只支持对 `URLRequest` 的 `httpBody` 属性进行设置：

```swift
open func encode<Parameters: Encodable>(_ parameters: Parameters?,
                                        into request: URLRequest) throws -> URLRequest {
    guard let parameters = parameters else { return request }

    var request = request

    do {
        let data = try encoder.encode(parameters)
        request.httpBody = data
        if request.headers["Content-Type"] == nil {
            request.headers.update(.contentType("application/json"))
        }
    } catch {
        throw AFError.parameterEncodingFailed(reason: .jsonEncodingFailed(error: error))
    }

    return request
}
```

`URLEncodedFormParameterEncoder` 用于生成 `URL` 编码方式的字符串，与 `JSONParameterEncoder` 不同，可以追加到 URL 后面，也可以设置到 body 中，取决于 `Destination` ：

```swift
enum Destination {
  case methodDependent // 如果是 .get， .head 和 .delete 方法则追加到 URL 链接后面，否则设置为 httpBody
  case methodDependent // 全都追加到 URL 链接后面
  case httpBody // 全都设置为 httpBody
}
```

`URLEncodedFormParameterEncoder` 的 `encoder` 属性是 `URLEncodedFormEncoder` 类型，用于编码时各种类型的转换。

```swift
open func encode<Parameters: Encodable>(_ parameters: Parameters?,
                                        into request: URLRequest) throws -> URLRequest {
    guard let parameters = parameters else { return request }

    var request = request
	  // 1.
    guard let url = request.url else {
        throw AFError.parameterEncoderFailed(reason: .missingRequiredComponent(.url))
    }
    // 2.
    guard let method = request.method else {
        let rawValue = request.method?.rawValue ?? "nil"
        throw AFError.parameterEncoderFailed(reason: .missingRequiredComponent(.httpMethod(rawValue: rawValue)))
    }
    // 3.
    if destination.encodesParametersInURL(for: method),
        var components = URLComponents(url: url, resolvingAgainstBaseURL: false) {
        // 4.
        let query: String = try Result<String, Error> { try encoder.encode(parameters) }
            .mapError { AFError.parameterEncoderFailed(reason: .encoderFailed(error: $0)) }.get()
        let newQueryString = [components.percentEncodedQuery, query].compactMap { $0 }.joinedWithAmpersands()
        components.percentEncodedQuery = newQueryString.isEmpty ? nil : newQueryString

        guard let newURL = components.url else {
            throw AFError.parameterEncoderFailed(reason: .missingRequiredComponent(.url))
        }

        request.url = newURL
    } else {
        // 5.
        if request.headers["Content-Type"] == nil {
            request.headers.update(.contentType("application/x-www-form-urlencoded; charset=utf-8"))
        }

        request.httpBody = try Result<Data, Error> { try encoder.encode(parameters) }
            .mapError { AFError.parameterEncoderFailed(reason: .encoderFailed(error: $0)) }.get()
    }

    return request
}
```

1. 判断 `request` 是否有 `url` ，如果没有则报 `AFError.parameterEncoderFailed(reason: .missingRequiredComponent(.httpMethod(rawValue: rawValue)))` 错误；
2. 判断 `request` 是否有指定 `method` ，如果没有则报 `AFError.parameterEncoderFailed(reason: .missingRequiredComponent(.httpMethod(rawValue: rawValue)))` 错误；
3. 根据参数编码类型判断是否追加到 `url` 中；
4. `mapError` 用于转换 `Result` 为 `failure` 时的 `error` ，`get()` 可以获取 `success value` ；
5. 参数编码后设置为 `httpBody` 。

### ParameterEncoding

`ParameterEncoding` 协议，跟 `ParameterEncoder` 协议的不同之处在于参数不再需要遵循 `Encodable` 协议，改为直接使用 `typealias Parameters = [String: Any]` ， 即 `key` 类型指定为 `String` 的 `Dictionary` 。 `ParameterEncoding` 的作用跟 `ParameterEncoder` 类似，这里不再赘述。

### `Protected<T>`

`Protected<T>` 支持范型，所以我们可以通过 `Protected<T>` 为各个类，结构体提供线程安全的封装，如同 `Protected<T>` 的说明。 为了实现线程安全，一般都需要一把锁， `Protected.swift` 里定义了一个 `private protocol Lock` ，这里对 `defer` 的使用也非常巧妙：

```swift
private protocol Lock {
    func lock()
    func unlock()
}

extension Lock {

    // 执行有返回值的 closure
    func around<T>(_ closure: () -> T) -> T {
        lock(); defer { unlock() }
        return closure()
    }

    /// 执行无返回值的 closure
    func around(_ closure: () -> Void) {
        lock(); defer { unlock() }
        closure()
    }
}
```

遵循 `Lock` 协议需要提供两个方法， `lock()` 和 `unlock()` ，而在 `Lock` 的 `extension` 里面，提供了两个结合 `closure` 实现加锁的方法，这两个方法可以满足大部分需要加锁的操作需求。之所以将 `Lock` 抽离为协议，是因为 Alamofire 需要支持 Linux ，而 Linux 无法使用 `os_unfair_lock` ，只能使用 `pthread_mutex_t` 。

```swift
#if os(Linux)
/// 5.1 新增的 MutexLock ，是 pthread_mutex_t 的 wrapper ，为了支持 Linux 平台。
final class MutexLock: Lock {
    private var mutex: UnsafeMutablePointer<pthread_mutex_t>

    init() {
        mutex = .allocate(capacity: 1)

        var attr = pthread_mutexattr_t()
        pthread_mutexattr_init(&attr)
        pthread_mutexattr_settype(&attr, .init(PTHREAD_MUTEX_ERRORCHECK))

        let error = pthread_mutex_init(mutex, &attr)
        precondition(error == 0, "Failed to create pthread_mutex")
    }

    deinit {
        let error = pthread_mutex_destroy(mutex)
        precondition(error == 0, "Failed to destroy pthread_mutex")
    }

    fileprivate func lock() {
        let error = pthread_mutex_lock(mutex)
        precondition(error == 0, "Failed to lock pthread_mutex")
    }

    fileprivate func unlock() {
        let error = pthread_mutex_unlock(mutex)
        precondition(error == 0, "Failed to unlock pthread_mutex")
    }
}
#endif

#if os(macOS) || os(iOS) || os(watchOS) || os(tvOS)
/// 原有的 os_unfair_lock ，苹果平台使用。
final class UnfairLock: Lock {
    private let unfairLock: os_unfair_lock_t

    init() {
        unfairLock = .allocate(capacity: 1)
        unfairLock.initialize(to: os_unfair_lock())
    }

    deinit {
        unfairLock.deinitialize(count: 1)
        unfairLock.deallocate()
    }

    fileprivate func lock() {
        os_unfair_lock_lock(unfairLock)
    }

    fileprivate func unlock() {
        os_unfair_lock_unlock(unfairLock)
    }
}
#endif
```

在定义了 `Lock` 类之后，`Protected<T>` 就可以通过 `Lock` 来实现线程安全，这里使用了 `@propertyWrapper` 来进行声明。

```swift
@propertyWrapper
final class Protected<T> {
    #if os(macOS) || os(iOS) || os(watchOS) || os(tvOS)
    private let lock = UnfairLock()
    #elseif os(Linux)
    private let lock = MutexLock()
    #endif
    private var value: T

    init(_ value: T) {
        self.value = value
    }

    /// 访问 wrappedValue 时必须要加锁。
    var wrappedValue: T {
        get { lock.around { value } }
        set { lock.around { value = newValue } }
    }

    var projectedValue: Protected<T> { self }

    init(wrappedValue: T) {
        value = wrappedValue
    }

    /// 同步获取值或者进行转换
    func read<U>(_ closure: (T) -> U) -> U {
        lock.around { closure(self.value) }
    }

    /// 同步修改值，同时可以返回修改后的值。
    @discardableResult
    func write<U>(_ closure: (inout T) -> U) -> U {
        lock.around { closure(&self.value) }
    }

	  /// 支持 @dynamicMemberLookup 后实现的方法，使得 Protected 声明的属性可以通过点语法来进行 keyPath 读写
    subscript<Property>(dynamicMember keyPath: WritableKeyPath<T, Property>) -> Property {
        get { lock.around { value[keyPath: keyPath] } }
        set { lock.around { value[keyPath: keyPath] = newValue } }
    }
}
```

为了方便使用， `Protected` 又添加了几个扩展。 这部分是为 `T` 实现了 `RangeReplaceableCollection` 协议后支持的方法，都是集合的 `append` 方法：

```swift
extension Protected where T: RangeReplaceableCollection {
    func append(_ newElement: T.Element) {
        write { (ward: inout T) in
            ward.append(newElement)
        }
    }

    func append<S: Sequence>(contentsOf newElements: S) where S.Element == T.Element {
        write { (ward: inout T) in
            ward.append(contentsOf: newElements)
        }
    }

    func append<C: Collection>(contentsOf newElements: C) where C.Element == T.Element {
        write { (ward: inout T) in
            ward.append(contentsOf: newElements)
        }
    }
}
```

`T` 为 `Data?` 类型时支持 `append` :

```swift
extension Protected where T == Data? {
    func append(_ data: Data) {
        write { (ward: inout T) in
            ward?.append(data)
        }
    }
}
```

`T` 为 `Request.MutableState` 时提供一些编辑方法，用于状态转换：

```swift
extension Protected where T == Request.MutableState {
    func attemptToTransitionTo(_ state: Request.State) -> Bool {
        lock.around {
            guard value.state.canTransitionTo(state) else { return false }

            value.state = state

            return true
        }
    }

    func withState(perform: (Request.State) -> Void) {
        lock.around { perform(value.state) }
    }
}
```

### Request

`Request` 是 Alamofire 中对应每个网络请求的父类，每次发起网络请求都会生成一个对应的子类对象，根据不同的网络请求会生成 `DataRequest` ，`DataStreamRequest` ， `DownloadRequest` 和 `UploadRequest` 。调用方不需要直接生成 `Request` 对象， `Request` 对象由 `Session` 负责生成。

`Request` 状态机：

```swift
// 当 Request 调用 resume() ， suspend() 或者 cancel() 方法时，处理状态之间的转换。
public enum State {
    /// 初始化状态
    case initialized
    /// 当调用 resume() 时就会切换为 resumed 状态，同时也会调用对应的 task 的 resume() 方法
    case resumed
    /// 当调用 suspend() 时就会切换为 suspended 状态，同时也会调用对应的 task 的 suspend() 方法
    case suspended
    /// 当调用 cancel() 时就会切换为 cancelled 状态，同时也会调用对应的 task 的 cancel() 方法
    /// 跟 resumed 和 suspended 状态不同，转换至 cancelled 状态后无法再转换至其它状态
    case cancelled
    /// 完成所有请求结果的序列化操作
    case finished

    /// 判断当前状态是否可以转换到其它状态
    func canTransitionTo(_ state: State) -> Bool {
        switch (self, state) {
        case (.initialized, _):
            return true
        case (_, .initialized), (.cancelled, _), (.finished, _):
            return false
        case (.resumed, .cancelled), (.suspended, .cancelled), (.resumed, .suspended), (.suspended, .resumed):
            return true
        case (.suspended, .suspended), (.resumed, .resumed):
            return false
        case (_, .finished):
            return true
        }
    }
}
```

状态机转换图如下：

![Request State Machine](https://raw.githubusercontent.com/dirtmelon/blog-images/main/Request%20State%20Machine.png)

`Request` 定义了一个 `MutableState` ，用于将可变属性和不可变属性区分开，所有可变属性到放到 `MutableState` 中，且使用 `@Protected` 声明，保证线程安全。

```swift
@Protected
fileprivate var mutableState = MutableState()
```

`Request` 的不可变属性：

```swift
/// `UUID` ，作为 `Request` 的唯一 id 使用，用于支持 `Hashble` 和 `Equatable` 协议
public let id: UUID
/// 串行队列， `Request` 内所有异步调用都是在这个队列内进行
public let underlyingQueue: DispatchQueue
/// 进行序列化时所使用到的队列，默认跟 `underlyingQueue` 一致
public let serializationQueue: DispatchQueue
/// `EventMonitor` ，下面会说到具体的作用
public let eventMonitor: EventMonitor?
/// `Request`'s interceptor ，用于 URL 适配，请求重试，认证等
public let interceptor: RequestInterceptor?
/// `Request`'s delegate ，用于调用 `Session` 的一些方法
public private(set) weak var delegate: RequestDelegate?
```

`Request` 的方法和具体内容在后面介绍整体的请求流程时再分析。

### RequestDelegate

`RequestDelegate` 负责提供一些 `Session` 的方法给 `Request` 调用， `Request` 的 `delegate` 都是 `Session` 对象。

```swift
public protocol RequestDelegate: AnyObject {
    /// 创建 `URLSessionTask` 时使用到的 `URLSessionConfiguration`
    var sessionConfiguration: URLSessionConfiguration { get }

    /// 是否直接开始，如果 `startImmediately` 为 `true` ，则当添加第一个 response handler 时就会调用 `resume()` 方法发送请求
    var startImmediately: Bool { get }

    /// 清除 Session 中关于 Request 的记录
    func cleanup(after request: Request)

    /// 异步调用 delegate 的方法，用于判断 Request 是否需要进行重试
    func retryResult(for request: Request, dueTo error: AFError, completion: @escaping (RetryResult) -> Void)

    /// 异步重试 Request
    func retryRequest(_ request: Request, withDelay timeDelay: TimeInterval?)
}
```

### RequestTaskMap

`RequestTaskMap` 用于串联 `URLSessionTask` 和 `Request` ，当请求结果更新时，需要根据 `URLSessionTask` 找到对应的 `Request` ，进行处理。或者通过 `Request` 找到对应的 `URLSessionTask` 。定义了两个 `Dictionary` ，用于实现两者之间的 `map` ，通过 `subscript` 方法提供下标设置和访问：

```swift
struct RequestTaskMap {
    private var tasksToRequests: [URLSessionTask: Request]
    private var requestsToTasks: [Request: URLSessionTask]

	  init(tasksToRequests: [URLSessionTask: Request] = [:],
         requestsToTasks: [Request: URLSessionTask] = [:],
         taskEvents: [URLSessionTask: (completed: Bool, metricsGathered: Bool)] = [:]) {
        self.tasksToRequests = tasksToRequests
        self.requestsToTasks = requestsToTasks
        self.taskEvents = taskEvents
    }

	  subscript(_ request: Request) -> URLSessionTask? {
        get { requestsToTasks[request] }
        set {
            guard let newValue = newValue else {
                guard let task = requestsToTasks[request] else {
                    fatalError("RequestTaskMap consistency error: no task corresponding to request found.")
                }

                requestsToTasks.removeValue(forKey: request)
                tasksToRequests.removeValue(forKey: task)
                taskEvents.removeValue(forKey: task)

                return
            }

            requestsToTasks[request] = newValue
            tasksToRequests[newValue] = request
            taskEvents[newValue] = (completed: false, metricsGathered: false)
        }
    }

    subscript(_ task: URLSessionTask) -> Request? {
        get { tasksToRequests[task] }
        set {
            guard let newValue = newValue else {
                guard let request = tasksToRequests[task] else {
                    fatalError("RequestTaskMap consistency error: no request corresponding to task found.")
                }

                tasksToRequests.removeValue(forKey: task)
                requestsToTasks.removeValue(forKey: request)
                taskEvents.removeValue(forKey: task)

                return
            }

            tasksToRequests[task] = newValue
            requestsToTasks[newValue] = task
            taskEvents[task] = (completed: false, metricsGathered: false)
        }
    }
}
```

### EventMonitor

`EventMonitor` 协议可以用来获取 `Request` 各种方法和状态的相关回调，一种最常见的用法就是打印日志：

```swift
final class Logger: EventMonitor {
    let queue = DispatchQueue(label: ...)

    // Event called when any type of Request is resumed.
    func requestDidResume(_ request: Request) {
        print("Resuming: \(request)")
    }

    // Event called whenever a DataRequest has parsed a response.
    func request<Value>(_ request: DataRequest, didParseResponse response: DataResponse<Value, AFError>) {
        debugPrint("Finished: \(response)")
    }
}
let logger = Logger()
let session = Session(eventMonitors: [logger])
```

可以看到 `Session` 支持多个 `eventMonitors` 。 Alamofire 里面为了让调用方可以更灵活地使用 `EventMonitor` ，添加了一个 `extension` ，里面实现了 `EventMonitor` 的全部方法和属性，这样调用方就不需要实现 `EventMonitor` 的全部方法，可以根据自己需要添加对应的方法即可，算是一种 `protocol` 实现 `optional` 方法的曲线救国方式。

为了支持多个 `eventMonitors` 和抽离 `EventMonitor` 的处理， Alamofire 实现了一个 `CompositeEventMonitor` 类，用于组合各个 `EventMonitors` ，在它自己的回调方法里遍历各个 `EventMonitors` ，调用对应的方法：

```swift
/// An `EventMonitor` which can contain multiple `EventMonitor`s and calls their methods on their queues.
public final class CompositeEventMonitor: EventMonitor {
    public let queue = DispatchQueue(label: "org.alamofire.compositeEventMonitor", qos: .utility)

    let monitors: [EventMonitor]

    init(monitors: [EventMonitor]) {
        self.monitors = monitors
    }

    func performEvent(_ event: @escaping (EventMonitor) -> Void) {
        queue.async {
            for monitor in self.monitors {
                monitor.queue.async { event(monitor) }
            }
        }
    }

    public func urlSession(_ session: URLSession, didBecomeInvalidWithError error: Error?) {
        performEvent { $0.urlSession(session, didBecomeInvalidWithError: error) }
    }
    // ...
}
```

`Session` 中则定义了一个 `eventMonitor: CompositeEventMonitor` 属性，用于组合多个 `EventMonitor` 。 Alamofire 提供了一个 打印日志的例子： [`NSLoggingEventMonitor.swift`](https://github.com/Alamofire/Alamofire/blob/master/Tests/NSLoggingEventMonitor.swift)

### Response

对请求结果进行封装，根据类型不同分为 `DataResponse` 和 `DownloadResponse` 。 `DataRequest` 或者 `UploadRequest` 请求返回的结果是 `DataResponse<Success, Failure: Error>` 。

```swift
public struct DataResponse<Success, Failure: Error> {
    /// 对应的 URLRequest
    public let request: URLRequest?

    /// 服务器返回的 HTTPURLResponse
    public let response: HTTPURLResponse?

    /// 服务器返回的 Data
    public let data: Data?

    /// 响应对应的 URLSessionTaskMetrics
    public let metrics: URLSessionTaskMetrics?

    /// 序列化所消耗的时间
    public let serializationDuration: TimeInterval

    /// 序列化的结果
    public let result: Result<Success, Failure>

    public var value: Success? { result.success }

    public var error: Failure? { result.failure }

    public init(request: URLRequest?,
                response: HTTPURLResponse?,
                data: Data?,
                metrics: URLSessionTaskMetrics?,
                serializationDuration: TimeInterval,
                result: Result<Success, Failure>) {
        self.request = request
        self.response = response
        self.data = data
        self.metrics = metrics
        self.serializationDuration = serializationDuration
        self.result = result
    }
}
```

跟 `Result` 类似， Alamofire 也为 `DataResponse` 添加了 `map<NewSuccess>` ， `tryMap<NewSuccess>` ， `mapError<NewFailure: Error>` 和 `tryMapError<NewFailure: Error>` 这几个方法。

`DownloadRequest` 对应的则是 `DownloadResponse<Success, Failure: Error>` ，大部分属性跟 `DataResponse` 一致，新增以下两个属性：

```swift
/// 用于存储响应的数据的文件 URL
public let fileURL: URL?

/// 取消请求时所接收到的数据
public let resumeData: Data?
```

### SessionDelegate

`SessionDelegate` 负责处理 `URLSessionDelegate` 的相关方法，相当于 `Session` 和 `URLSessionDelegate` 的一个中间层。

```swift
/// 负责调用 Session 的一些方法和获取对应的属性
protocol SessionStateProvider: AnyObject {
    var serverTrustManager: ServerTrustManager? { get }
    var redirectHandler: RedirectHandler? { get }
    var cachedResponseHandler: CachedResponseHandler? { get }

    func request(for task: URLSessionTask) -> Request?
    func didGatherMetricsForTask(_ task: URLSessionTask)
    func didCompleteTask(_ task: URLSessionTask, completion: @escaping () -> Void)
    func credential(for task: URLSessionTask, in protectionSpace: URLProtectionSpace) -> URLCredential?
    func cancelRequestsForSessionInvalidation(with error: Error?)
}
```

下面是默认的 `SessionDelegate` 实现，你可以在初始化 `Session` 时提供自定义的 `SessionDelegate` 的子类：

```swift
/// Class which implements the various `URLSessionDelegate` methods to connect various Alamofire features.
open class SessionDelegate: NSObject {
    private let fileManager: FileManager

    // stateProvider 就是 Session
    weak var stateProvider: SessionStateProvider?
    // eventMonitor
    var eventMonitor: EventMonitor?

    // 提供一个 fileManager 属性，用于管理下载文件
    public init(fileManager: FileManager = .default) {
        self.fileManager = fileManager
    }

    // 通过 stateProvider 即 Session 获取对应的 Request
    func request<R: Request>(for task: URLSessionTask, as type: R.Type) -> R? {
        guard let provider = stateProvider else {
            assertionFailure("StateProvider is nil.")
            return nil
        }

        return provider.request(for: task) as? R
    }
}
```

当 `URLSession` 无效后调用 `eventMonitor` 对应的方法，以及调用 `stateProvider` 取消所有 `requests` ：

```swift
extension SessionDelegate: URLSessionDelegate {
    open func urlSession(_ session: URLSession, didBecomeInvalidWithError error: Error?) {
        eventMonitor?.urlSession(session, didBecomeInvalidWithError: error)

        stateProvider?.cancelRequestsForSessionInvalidation(with: error)
    }
}
```

`SessionDelegate` 也定义了 `URLSessionTaskDelegate` ， `URLSessionDataDelegate` 和 `URLSessionDownloadDelegate` 的方法，基本实现和上面的大同小异，负责调用 `EventMonitor` ， `Session` 和 `Request` 的相关方法。

### URLConvertible+URLRequestConvertible

`URLconvertible` 协议，用于转化为 `URL` 。当我们发起一个网络请求时就需要构建一个对应的 `URL` ，为了方便调用方可以直接传递 `String` ， `URL` 或者 `URLComponents` 来生成 `URL` ，而不需要自己先生成 `URL` 。同时也可以自定义一些生成 `URL` 的规则，只要支持 `URLConvertible` 协议即可。

```swift
public protocol URLConvertible {
    func asURL() throws -> URL
}
```

`String` ， `URL` 和 `URLComponents` 默认支持 `URLConvertible` ：

```swift
extension String: URLConvertible {
    public func asURL() throws -> URL {
        guard let url = URL(string: self) else { throw AFError.invalidURL(url: self) }
        return url
    }
}

extension URL: URLConvertible {
    public func asURL() throws -> URL { self }
}

extension URLComponents: URLConvertible {
    public func asURL() throws -> URL {
        guard let url = url else { throw AFError.invalidURL(url: self) }
        return url
    }
}
```

所以 Alamofire 默认支持以下三种发起请求的方式：

```swift
let urlString = "https://httpbin.org/get"
AF.request(urlString)

let url = URL(string: urlString)!
AF.request(url)

let urlComponents = URLComponents(url: url, resolvingAgainstBaseURL: true)!
AF.request(urlComponents)
```

`URLRequestConvertible` 则是用于生成 `URLRequest` 的协议，通过 `URLRequest` 可以生成对应的 `URLSessionTask` 。 `URLRequest` 默认支持 `URLRequestConvertible` ：

```swift
public protocol URLRequestConvertible {
    func asURLRequest() throws -> URLRequest
}

extension URLRequestConvertible {
    public var urlRequest: URLRequest? { try? asURLRequest() }
}

extension URLRequest: URLRequestConvertible {
    public func asURLRequest() throws -> URLRequest { self }
}

// 给 URLRequest 添加了一个初始化方法，方便在初始化时直接设置 method 和 allHTTPHeaderFields
extension URLRequest {
    public init(url: URLConvertible, method: HTTPMethod, headers: HTTPHeaders? = nil) throws {
        let url = try url.asURL()

        self.init(url: url)

        httpMethod = method.rawValue
        allHTTPHeaderFields = headers?.dictionary
    }
}
```

通过 `URLRequest` 发送请求：

```swift
let url = URL(string: "https://httpbin.org/post")!
var urlRequest = URLRequest(url: url)
urlRequest.method = .post

let parameters = ["foo": "bar"]

do {
    urlRequest.httpBody = try JSONEncoder().encode(parameters)
} catch {
    // Handle error.
}

urlRequest.headers.add(.contentType("application/json"))
AF.request(urlRequest)
```

这样可以把具体对象抽离出来，提供的参数只需要支持 `URLRequestConvertible` 协议即可。当我们的 App 有大量的请求接口需要进行定义时，可以通过 `URLRequestConvertible` 协议来定义相关的参数编码，请求方法等。如下面代码所示，可以定一个 `enum Router` ， 支持 `URLRequestConvertible` 类型，这样在调用时生成对应的 `enum` 就可以了。这为调用方提供了横向扩展的能力， Alamofire 不需要知道具体的对象类型，只需要通过 `URLRequestConvertible` 来进行 `URLRequest` 转换，这样有利于我们对网络层的请求进行组织和整理。

```swift
enum Router: URLRequestConvertible {
    case get([String: String]), post([String: String])

    var baseURL: URL {
        return URL(string: "https://httpbin.org")!
    }

    var method: HTTPMethod {
        switch self {
        case .get: return .get
        case .post: return .post
        }
    }

    var path: String {
        switch self {
        case .get: return "get"
        case .post: return "post"
        }
    }

    func asURLRequest() throws -> URLRequest {
        let url = baseURL.appendingPathComponent(path)
        var request = URLRequest(url: url)
        request.method = method

        switch self {
        case let .get(parameters):
            request = try URLEncodedFormParameterEncoder().encode(parameters, into: request)
        case let .post(parameters):
            request = try JSONParameterEncoder().encode(parameters, into: request)
        }

        return request
    }
}
```

### Result+Alamofire

Alamofire 为了使用 `Result` 更方便而定义的一些便捷方法。 使用 `typealias` 定义了一个 `AFResult` ，其 `Failure` 类型固定为 `AFError` ：

```swift
public typealias AFResult<Success> = Result<Success, AFError>
```

判断是否为 `.success` 和 `.failure` ：

```swift
var isSuccess: Bool {
    guard case .success = self else { return false }
    return true
}

var isFailure: Bool {
    !isSuccess
}
```

获取对应的值：

```swift
var success: Success? {
    guard case let .success(value) = self else { return nil }
    return value
}

var failure: Failure? {
    guard case let .failure(error) = self else { return nil }
    return error
}
```

通过 `Success` 和 `Failure` 进行初始化：

```swift
init(value: Success, error: Failure?) {
    if let error = error {
        self = .failure(error)
    } else {
        self = .success(value)
    }
}
```

`tryMap` 对 `Success` 进行转换，在转换过程中可以抛出 `Error` ：

```swift
func tryMap<NewSuccess>(_ transform: (Success) throws -> NewSuccess) -> Result<NewSuccess, Error> {
    switch self {
    case let .success(value):
        do {
            return try .success(transform(value))
        } catch {
            return .failure(error)
        }
    case let .failure(error):
        return .failure(error)
    }
}
```

用法如下：

```swift
let possibleData: Result<Data, Error> = .success(Data(...))
let possibleObject = possibleData.tryMap {
    try JSONSerialization.jsonObject(with: $0)
}
```

`tryMapError` 对 `Failure` 进行转换，在转换过程中也可以抛出 `Error` ：

```swift
func tryMapError<NewFailure: Error>(_ transform: (Failure) throws -> NewFailure) -> Result<Success, Error> {
    switch self {
    case let .failure(error):
        do {
            return try .failure(transform(error))
        } catch {
            return .failure(error)
        }
    case let .success(value):
        return .success(value)
    }
}
```

用法如下：

```swift
let possibleData: Result<Data, Error> = .success(Data(...))
let possibleObject = possibleData.tryMapError {
    try someFailableFunction(taking: $0)
}
```

## 整体流程

`Session` 作为 Alamofire 的第一层入口，所有 `Alamofire.swift` 的请求方法都会调用 `Session` 里面对应的方法。`Session` 负责创建和管理 Alamofire 的 `Request` 类。同时也提供一些公共的方法给所有 `Request` 使用，如请求队列，信任管理，重定向处理和响应缓存处理等。`Session` 类似于一个 Manager 的角色，处理各个请求的创建流程。

当创建一个 `Request` 的子类后， Alamofire 会进行一系列的操作来完成这个请求。一个成功的请求包括以下流程：

1. 一些初始化参数，比如 HTTP 方法， HTTP 头和参数等会被封装进内部的 `URLRequestConvertible` 值中，用于初始化 `Request` ；
2. 调用 `URLRequestConvertible` 的 `asURLRequest()` 方法来创建第一个 `URLRequest` 。 `URLRequest` 会存储到 `Request` 的 `mutableState.requests` 属性中。如果有定义 `RequestModifier` ， 在生成 `URLRequest` 会进行调用来调整 `URLRequest` ；
3. 如果 `Session` 或者 `Request` 有提供 `RequestAdapters` 或者 `RequestInterceptors` ，则会对之前生成的 `URLRequest` 进行调整，同时也会存储到 `Request` 的 `mutableState.requests` 属性中；
4. `Session` 调用 `Request` 的方法来生成对应的 `URLSessionTask` ，不同的 `Request` 子类 会生成不同的 `URLSessionTask` ；
5. 当 `URLSessionTask` 完成任务，且已经收集到 `URLSessionTaskMetrics` ， `Request` 就会执行自己的 `Validators ` 来验证请求结果是否正确；
6. 通过验证后， `Request` 就会执行 `mutableState.responseSerializers` 来处理请求结果。在上面这些步骤中，每个步骤都有可能产生错误或者接收到网络返回的错误结果，这些错误会传递给对应的 `Request` 。在处理结果时会判断是否需要重试。 当 `Error` 传递给 `Request` 后，`Request` 会调用对应的 `RequestRetriers` 来判断是否需要进行重试，如果需要进行重试，则再走一次上面的流程。

下面以 `DataRequest` 为例讲一下发起网络请求的整体流程。

### 生成 DataRequest

Alamofire 为发起 `DataRequest` 提供了三个接口：

1. `parameters` 为 `Parameters` ，即 `[String: Any]` ：

```swift
open func request(_ convertible: URLConvertible,
                  method: HTTPMethod = .get,
                  parameters: Parameters? = nil,
                  encoding: ParameterEncoding = URLEncoding.default,
                  headers: HTTPHeaders? = nil,
                  interceptor: RequestInterceptor? = nil,
                  requestModifier: RequestModifier? = nil) -> DataRequest {
    let convertible = RequestConvertible(url: convertible,
                                         method: method,
                                         parameters: parameters,
                                         encoding: encoding,
                                         headers: headers,
                                         requestModifier: requestModifier)

    return request(convertible, interceptor: interceptor)
}
```

定义一个 `struct RequestConvertible` ，支持 `URLRequestConvertible` 协议，负责处理参数的编码和生成对应的 `URLRequest` ：

```swift
public typealias RequestModifier = (inout URLRequest) throws -> Void

struct RequestConvertible: URLRequestConvertible {
    let url: URLConvertible
    let method: HTTPMethod
    let parameters: Parameters?
    let encoding: ParameterEncoding
    let headers: HTTPHeaders?
    let requestModifier: RequestModifier?

    func asURLRequest() throws -> URLRequest {
        var request = try URLRequest(url: url, method: method, headers: headers)
        try requestModifier?(&request)

        return try encoding.encode(request, with: parameters)
    }
}
```

1. `parameters` 支持 `Encodable` ：

```swift
open func request<Parameters: Encodable>(_ convertible: URLConvertible,
                                         method: HTTPMethod = .get,
                                         parameters: Parameters? = nil,
                                         encoder: ParameterEncoder = URLEncodedFormParameterEncoder.default,
                                         headers: HTTPHeaders? = nil,
                                         interceptor: RequestInterceptor? = nil,
                                         requestModifier: RequestModifier? = nil) -> DataRequest {
    let convertible = RequestEncodableConvertible(url: convertible,
                                                  method: method,
                                                  parameters: parameters,
                                                  encoder: encoder,
                                                  headers: headers,
                                                  requestModifier: requestModifier)

    return request(convertible, interceptor: interceptor)
}
```

由于参数编码方式不同，所以需要定义一个 `struct RequestEncodableConvertible<Parameters: Encodable>` ，来处理参数为 `Encodable` 时的编码和生成 `URLRequest` ：

```swift
struct RequestEncodableConvertible<Parameters: Encodable>: URLRequestConvertible {
    let url: URLConvertible
    let method: HTTPMethod
    let parameters: Parameters?
    let encoder: ParameterEncoder
    let headers: HTTPHeaders?
    let requestModifier: RequestModifier?

    func asURLRequest() throws -> URLRequest {
        var request = try URLRequest(url: url, method: method, headers: headers)
        try requestModifier?(&request)

        return try parameters.map { try encoder.encode($0, into: request) } ?? request
    }
}
```

1. 上面两个接口经过处理生成对应的 `URLRequestConvertible` 后会调用这个接口来生成 `DataRequest` ，在使用的时候也可以自己生成 `URLRequestConvertible` ，直接调用这个接口：

```swift
open func request(_ convertible: URLRequestConvertible, interceptor: RequestInterceptor? = nil) -> DataRequest {
    let request = DataRequest(convertible: convertible,
                              underlyingQueue: rootQueue,
                              serializationQueue: serializationQueue,
                              eventMonitor: eventMonitor,
                              interceptor: interceptor,
                              delegate: self)

    perform(request)

    return request
}
```

这样可以统一 `DataRequest` 的处理流程，虽然可以通过不同的参数来生成 `DataRequest` ，但是在 `Session` 内部的处理时，会通过 `URLRequestConvertible` 进行转换，收敛到同一个接口中。

### perform

这里 `perform` 跟 `resume` 不同，不会发起真正的网络请求，只是用来进行进行请求前的准备工作：

```swift
func perform(_ request: Request) {
    rootQueue.async {
        // 1.
        guard !request.isCancelled else { return }
        // 2.
        self.activeRequests.insert(request)
        self.requestQueue.async {
            // 3.
            switch request {
            case let r as UploadRequest: self.performUploadRequest(r) // UploadRequest must come before DataRequest due to subtype relationship.
            case let r as DataRequest: self.performDataRequest(r)
            case let r as DownloadRequest: self.performDownloadRequest(r)
            case let r as DataStreamRequest: self.performDataStreamRequest(r)
            default: fatalError("Attempted to perform unsupported Request subclass: \(type(of: request))")
            }
        }
    }
}
```

1. 判断 `request` 是否有取消，因为有可能还没发起请求就已经被取消了；
2. 添加到 `activeRequests` 中；
3. 使用 switch case let 进行类型判断

然后调用 `performSetupOperations` 方法进行一些请求前的准备工作。 在处理过程中会判断是否有设置 `adapter` ，如果有设置 `adapter` ，则调用 `adapter` 对请求做一次适配。

```swift
func performSetupOperations(for request: Request, convertible: URLRequestConvertible) {
    dispatchPrecondition(condition: .onQueue(requestQueue))

    let initialRequest: URLRequest

    do {
        // 1.
        initialRequest = try convertible.asURLRequest()
        // 2.
        try initialRequest.validate()
    } catch {
        rootQueue.async { request.didFailToCreateURLRequest(with: error.asAFError(or: .createURLRequestFailed(error: error))) }
        return
    }
    // 3.
    rootQueue.async { request.didCreateInitialURLRequest(initialRequest) }
    guard !request.isCancelled else { return }
    // 4.
    guard let adapter = adapter(for: request) else {
        rootQueue.async { self.didCreateURLRequest(initialRequest, for: request) }
        return
    }
    // 5.
    adapter.adapt(initialRequest, for: self) { result in
        do {
            let adaptedRequest = try result.get()
            try adaptedRequest.validate()

            self.rootQueue.async {
                request.didAdaptInitialRequest(initialRequest, to: adaptedRequest)
                self.didCreateURLRequest(adaptedRequest, for: request)
            }
        } catch {
            self.rootQueue.async { request.didFailToAdaptURLRequest(initialRequest, withError: .requestAdaptationFailed(error: error)) }
        }
    }
}
```

1. 尝试生成对应的 `URLRequest` ；
2. 检验 `URLRequest` 是否符合格式要求，如果是 `GET` 请求，而且 `httpBody` 中有数据，就会报一个 `bodyDataInGETRequest` 的错；
3. 调用 `request` 的 `didCreateInitialURLRequest` 方法，负责更新 request 的 mutableState 和调用 eventMonitor 对应的方法；
4. 判断是否有 `adapter` ，如果没有则调用 `didCreateURLRequest` 进行一些最后的处理工作；
5. 使用 `adapter` 对 `request` 进行转换，然后调用 `request.didAdaptInitialRequest` 和 `didCreateURLRequest` ；

可以看到上面的代码在调用 `request` 的方法时都会通过 `rootRequeue` 进行异步调用，以保证线程安全。 再看一下 `Request` 中对应的方法都做了哪些处理：

```swift
func didCreateInitialURLRequest(_ request: URLRequest) {
    dispatchPrecondition(condition: .onQueue(underlyingQueue))

    $mutableState.write { $0.requests.append(request) }

    eventMonitor?.request(self, didCreateInitialURLRequest: request)
}
```

`Session` 中调用 `request` 的方法都跟上面的实现类似：

1. 更新 `request.state` ；
2. 通过 `eventMonitor` 调用相关回调；

`didCreateURLRequest` 则负责创建对应的 `URLSessionTask` ，在 `requestTaskMap` 中添加对应的记录：

```swift
func didCreateURLRequest(_ urlRequest: URLRequest, for request: Request) {
    dispatchPrecondition(condition: .onQueue(rootQueue))

    request.didCreateURLRequest(urlRequest)

    guard !request.isCancelled else { return }

    let task = request.task(for: urlRequest, using: session)
    requestTaskMap[request] = task
    request.didCreateTask(task)
    // 根据 request 的 state 对 task 进行操作
    updateStatesForTask(task, request: request)
}
```

这里之所以需要根据 `request` 的 `state` 对 `task` 进行操作，是因为当 `request` 进行重试时也需要调用这个方法，所以如果是重试，就需要根据 `request` 的 `state` 来调用 `task` 对应的方法：

```swift
func updateStatesForTask(_ task: URLSessionTask, request: Request) {
    dispatchPrecondition(condition: .onQueue(rootQueue))

    request.withState { state in
        switch state {
        case .initialized, .finished:
            break
        case .resumed:
            task.resume()
            rootQueue.async { request.didResumeTask(task) }
        case .suspended:
            task.suspend()
            rootQueue.async { request.didSuspendTask(task) }
        case .cancelled:
            task.resume()
            task.cancel()
            rootQueue.async { request.didCancelTask(task) }
        }
    }
}
```

至此已经走完了一个 `Request` 的创建流程，流程如下图所示：

![Generate Request](https://raw.githubusercontent.com/dirtmelon/blog-images/main/Generate%20Request.png)

### 响应处理

#### 进度

我们可以通过相关的 `cloures` 来设置进度的回调：

```swift
AF.request(...)
    .uploadProgress { progress in
        print(progress)
    }
    .downloadProgress { progress in
        print(progress)
    }
    .responseDecodable(of: SomeType.self) { response in
        debugPrint(response)
    }
```

```swift
@discardableResult
public func downloadProgress(queue: DispatchQueue = .main, closure: @escaping ProgressHandler) -> Self {
    mutableState.downloadProgressHandler = (handler: closure, queue: queue)
    return self
}

@discardableResult
public func uploadProgress(queue: DispatchQueue = .main, closure: @escaping ProgressHandler) -> Self {
    mutableState.uploadProgressHandler = (handler: closure, queue: queue)

    return self
}
```

使用 `mutableState` 来保存相关的 `uploadProgressHandler` 和 `downloadProgressHandler` ， `uploadProgressHandler` 和 `downloadProgressHandler` 只支持设置一个，同时会返回 `Self` ，这样就可以进行链式调用。

在 `SessionDelegate` 中，如果有进度更新，就会通过 `stateProvider(session)` 获取 `request` ，调用 `request` 对应的方法进行进度更新：

```swift
// SessionDelegate
open func urlSession(_ session: URLSession,
                     task: URLSessionTask,
                     didSendBodyData bytesSent: Int64,
                     totalBytesSent: Int64,
                     totalBytesExpectedToSend: Int64) {
    eventMonitor?.urlSession(session,
                             task: task,
                             didSendBodyData: bytesSent,
                             totalBytesSent: totalBytesSent,
                             totalBytesExpectedToSend: totalBytesExpectedToSend)

    stateProvider?.request(for: task)?.updateUploadProgress(totalBytesSent: totalBytesSent,
                                                            totalBytesExpectedToSend: totalBytesExpectedToSend)
}

// Request
func updateUploadProgress(totalBytesSent: Int64, totalBytesExpectedToSend: Int64) {
    uploadProgress.totalUnitCount = totalBytesExpectedToSend
    uploadProgress.completedUnitCount = totalBytesSent

    uploadProgressHandler?.queue.async { self.uploadProgressHandler?.handler(self.uploadProgress) }
}
```

这些`closure` 的配置需要在添加 `response handler` 前，因为添加 `response handler` 之后， `request` 有可能会直接调用 `resume()` 方法，导致在更新进度时可能 `uploadProgress` 和 `downloadProgress` 还没进行配置，错过部分进度更新的回调。

#### 重定向

Alamofire 提供了一个重定向协议 `RedirectHandler` ，提供了以下方法，可以生成新的 `URLRequest` ，也可以直接调用 `completion(nil)` 来拒绝重定向：

```swift
public protocol RedirectHandler {
    func task(_ task: URLSessionTask,
              willBeRedirectedTo request: URLRequest,
              for response: HTTPURLResponse,
              completion: @escaping (URLRequest?) -> Void)
}
```

```swift
let redirector = Redirector(behavior: .follow)
AF.request(...)
    .redirect(using: redirector)
    .responseDecodable(of: SomeType.self) { response in
        debugPrint(response)
    }
```

`Redirector` 为 Alamofire 提供了的一个重定向默认实现，在重定向时根据 `behavior` 来判断如何进行重定向的相关操作：

```swift
public enum Behavior {
    case follow
    case doNotFollow
    case modify((URLSessionTask, URLRequest, HTTPURLResponse) -> URLRequest?)
}

extension Redirector: RedirectHandler {
    public func task(_ task: URLSessionTask,
                     willBeRedirectedTo request: URLRequest,
                     for response: HTTPURLResponse,
                     completion: @escaping (URLRequest?) -> Void) {
        switch behavior {
        case .follow:
            completion(request)
        case .doNotFollow:
            completion(nil)
        case let .modify(closure):
            let request = closure(task, request, response)
            completion(request)
        }
    }
}
```

在设置完 `redirectHandler` 后， `SessionDelegate` 中也会调用对应的 `redirectHandler` 进行重定向：

```swift
open func urlSession(_ session: URLSession,
                     task: URLSessionTask,
                     willPerformHTTPRedirection response: HTTPURLResponse,
                     newRequest request: URLRequest,
                     completionHandler: @escaping (URLRequest?) -> Void) {
    eventMonitor?.urlSession(session, task: task, willPerformHTTPRedirection: response, newRequest: request)
    // 获取对应的 redirectHandler ，如果 request 的 redirectHandler 为 nil ，就尝试获取 session 的 redirectHandler
    if let redirectHandler = stateProvider?.request(for: task)?.redirectHandler ?? stateProvider?.redirectHandler {
        redirectHandler.task(task, willBeRedirectedTo: request, for: response, completion: completionHandler)
    } else {
        completionHandler(request)
    }
}
```

#### 自定义缓存

Alamofire 提供了一个自定义协议 `CachedResponseHandler` ，用于判断是否需要缓存当前的 HTTP 响应结果，可以生成新的 `CachedURLResponse` ，也可以调用 `completion(nil)` 来拒绝进行缓存：

```swift
public protocol CachedResponseHandler {
    func dataTask(_ task: URLSessionDataTask,
                  willCacheResponse response: CachedURLResponse,
                  completion: @escaping (CachedURLResponse?) -> Void)
}
```

跟 `RedirectHandler` 类似， `ResponseCacher` 是 Alamofire 提供的遵循 `CachedResponseHandler` 协议的一个类，也是通过 `Behavior` 来判断如何实现缓存。

```swift
open func urlSession(_ session: URLSession,
                     dataTask: URLSessionDataTask,
                     willCacheResponse proposedResponse: CachedURLResponse,
                     completionHandler: @escaping (CachedURLResponse?) -> Void) {
    eventMonitor?.urlSession(session, dataTask: dataTask, willCacheResponse: proposedResponse)
	  // 获取对应的 cachedResponseHandler ，如果 request 的 cachedResponseHandler 为 nil ，就尝试获取 session 的 cachedResponseHandler
    if let handler = stateProvider?.request(for: dataTask)?.cachedResponseHandler ?? stateProvider?.cachedResponseHandler {
        handler.dataTask(dataTask, willCacheResponse: proposedResponse, completion: completionHandler)
    } else {
        completionHandler(proposedResponse)
    }
}
```

其它的一些相关配置的实现原理也大致相同，这里不再赘述。

### 处理请求结果

`Request` 处理请求结果的流程：

![响应处理](https://raw.githubusercontent.com/dirtmelon/blog-images/main/%E5%93%8D%E5%BA%94%E5%A4%84%E7%90%86.png)

每个 `ResponseSerializer` 完成处理后都会调用 `responseSerializerDidComplete(completion: @escaping () -> Void)` ，获取下一个 `nextResponseSerializer()` 。

`DataRequest` 和 `DownloadRequest` 都提供了对结果不做任何序列化操作的方法：

```swift
// DataRequest
func response(queue: DispatchQueue = .main, completionHandler: @escaping (AFDataResponse<Data?>) -> Void) -> Self

// DownloadRequest
func response(queue: DispatchQueue = .main, completionHandler: @escaping (AFDownloadResponse<URL?>) -> Void) -> Self
```

`DataRequest` 对应的方法实现：

```swift
func response(queue: DispatchQueue = .main, completionHandler: @escaping (AFDataResponse<Data?>) -> Void) -> Self {
    appendResponseSerializer {

        let result = AFResult<Data?>(value: self.data, error: self.error)
		  // 1.
        self.underlyingQueue.async {
            // 2.
			  let response = DataResponse(request: self.request,
                                        response: self.response,
                                        data: self.data,
                                        metrics: self.metrics,
                                        serializationDuration: 0,
                                        result: result)

            self.eventMonitor?.request(self, didParseResponse: response)
			  // 3.
            self.responseSerializerDidComplete { queue.async { completionHandler(response) } }
        }
    }

    return self
}
```

1. 完成序列化操作后，转换到 `underlyingQueue` 中进行处理，因为在进行序列化操作时是在 `serializationQueue` 进行处理；
2. 生成对应的 `DataResponse` ，因为不做任何序列化操作，所以 `serializationDuration` 直接设置 0 ；
3. 调用 `responseSerializerDidComplete` 添加 `completionHandler` ；

添加 `ResponseSerializer` ：

```swift
func appendResponseSerializer(_ closure: @escaping () -> Void) {
    $mutableState.write { mutableState in
        mutableState.responseSerializers.append(closure)
        // 1.
        if mutableState.state == .finished {
            mutableState.state = .resumed
        }
        // 2.
        if mutableState.responseSerializerProcessingFinished {
            underlyingQueue.async { self.processNextResponseSerializer() }
        }
        // 3.
        if mutableState.state.canTransitionTo(.resumed) {
            underlyingQueue.async { if self.delegate?.startImmediately == true { self.resume() } }
        }
    }
}
```

1. 这里之所以把状态由 `.finished` 为 `.resumed` ，是因为如果 `ResponseSerializer` 序列化失败，会重新发送请求，而重新发送请求时会调用 `updateStatesForTask` 方法，只有 `request` 的状态为 `resumed` 时才会调用 `task.resume()` ， 所以这里要设置为 `resumed` ，使得可以调用 `task.resume()` ，重新发送请求；
2. 是否已经处理完其它 `ResponseSerializer` ，如果已经处理完，则直接开始处理新增的 `ResponseSerializer` ；
3. 是否需要直接开始进行网络请求；

调用下一个 `ResponseSerializer` 进行处理，如果所有 `ResponseSerializer` 都处理完毕则调用所有的 `completions` ：

```swift
func processNextResponseSerializer() {
        guard let responseSerializer = nextResponseSerializer() else {

            var completions: [() -> Void] = []

            $mutableState.write { mutableState in
                completions = mutableState.responseSerializerCompletions
				   // 1.
                mutableState.responseSerializers.removeAll()
                mutableState.responseSerializerCompletions.removeAll()

                if mutableState.state.canTransitionTo(.finished) {
                    mutableState.state = .finished
                }

                mutableState.responseSerializerProcessingFinished = true
                mutableState.isFinishing = false
            }
            completions.forEach { $0() }
            cleanup()

            return
        }
		  // 3.
        serializationQueue.async { responseSerializer() }
    }
```

1. 如果已经完成所有序列化操作，优先移除所有的 `ResponseSerializers` 和 `ResponseSerializerCompletions` ， 这个 [PR](https://github.com/Alamofire/Alamofire/pull/2778) 有提到具体原因；
2. 执行所有 `ResponseSerializerCompletions` ；
3. 如果还有序列化操作未执行，就先执行；

获取下一个序列化操作，因为只有完成了序列化操作后才会添加对应的 `ResponseSerializerCompletion` ，所以通过 `responseSerializers` 和 `responseSerializerCompletions` 的 `count` 来比较即可知道是否还有序列化操作未处理：

```swift
func nextResponseSerializer() -> (() -> Void)? {
    var responseSerializer: (() -> Void)?

    $mutableState.write { mutableState in
        let responseSerializerIndex = mutableState.responseSerializerCompletions.count

        if responseSerializerIndex < mutableState.responseSerializers.count {
            responseSerializer = mutableState.responseSerializers[responseSerializerIndex]
        }
    }

    return responseSerializer
}
```

#### 添加序列化操作

Alamofire 提供了 `DataResponseSerializerProtocol` 和 `DownloadResponseSerializerProtocol` 协议，用于添加一些自定义的序列化操作：

```swift
public protocol DataResponseSerializerProtocol {
    associatedtype SerializedObject
    func serialize(request: URLRequest?, response: HTTPURLResponse?, data: Data?, error: Error?) throws -> SerializedObject
}

public protocol DownloadResponseSerializerProtocol {
    associatedtype SerializedObject

    func serializeDownload(request: URLRequest?, response: HTTPURLResponse?, fileURL: URL?, error: Error?) throws -> SerializedObject
}
```

这两个协议都比较好理解，定义了一个关联类型 `SerializedObject` 和一个用于将原始数据转换为 `SerializedObject` 的方法。 `DataRequest` 提供了以下方法给我们添加自定义的序列化操作：

```swift
public func response<Serializer: DataResponseSerializerProtocol>(queue: DispatchQueue = .main,
                                                                 responseSerializer: Serializer,
                                                                 completionHandler: @escaping (AFDataResponse<Serializer.SerializedObject>) -> Void)
    -> Self {
    appendResponseSerializer {
        // 1. 进行序列化转换，记录时间
        let start = ProcessInfo.processInfo.systemUptime
        let result: AFResult<Serializer.SerializedObject> = Result {
            try responseSerializer.serialize(request: self.request,
                                             response: self.response,
                                             data: self.data,
                                             error: self.error)
        }.mapError { error in
            error.asAFError(or: .responseSerializationFailed(reason: .customSerializationFailed(error: error)))
        }

        let end = ProcessInfo.processInfo.systemUptime

        self.underlyingQueue.async {
            // 2. 生成对应的 DataResponse ，调用 eventMonitor 对应的方法
            let response = DataResponse(request: self.request,
                                        response: self.response,
                                        data: self.data,
                                        metrics: self.metrics,
                                        serializationDuration: end - start,
                                        result: result)

            self.eventMonitor?.request(self, didParseResponse: response)
			   // 3. 如果没有错误，就调用 completionHandler
            guard let serializerError = result.failure, let delegate = self.delegate else {
                self.responseSerializerDidComplete { queue.async { completionHandler(response) } }
                return
            }
			   // 4. 判断是否重试
            delegate.retryResult(for: self, dueTo: serializerError) { retryResult in
                var didComplete: (() -> Void)?

                defer {
                    if let didComplete = didComplete {
                        self.responseSerializerDidComplete { queue.async { didComplete() } }
                    }
                }

                switch retryResult {
                case .doNotRetry:
                    didComplete = { completionHandler(response) }

                case let .doNotRetryWithError(retryError):
                    let result: AFResult<Serializer.SerializedObject> = .failure(retryError.asAFError(orFailWith: "Received retryError was not already AFError"))
                    // 5. 不进行重试
                    let response = DataResponse(request: self.request,
                                                response: self.response,
                                                data: self.data,
                                                metrics: self.metrics,
                                                serializationDuration: end - start,
                                                result: result)

                    didComplete = { completionHandler(response) }

                case .retry, .retryWithDelay:
                    delegate.retryRequest(self, withDelay: retryResult.delay)
                }
            }
        }
    }

    return self
}
```

而 Alamofire 也提供了一些常见的序列化操作给我们使用：

1. `responseString(queue:encoding:completionHandler:)` 通过 `StringResponseSerializer` 将 `Data` 转换为 `String` ；
2. `responseJSON(queue:options:completionHandler)` 通过 `JSONResponseSerializer(JSONSerialization)` 将 `Data` 转换为 `JSON` 对象；
3. `responseDecodable(of:queue:decoder:completionHandler:)` 通过 `DecodableResponseSerializer` 将 `Data` 转换为 `Decodable` 对象， `decoder` 默认为 `JSONDecoder` ；

这里也是通过协议来对自动的序列化操作进行抽象。

## NetworkReachabilityManager

`NetworkReachabilityManager` 是 Alamofire 提供的用于检测网络状态的工具类。 `NetworkReachabilityManager` 只用获取监测网络状态，在设备的网络状态改变时收到通知，不要以此来判断是否可以连接某个 host 或者地址。

### NetworkReachabilityStatus

`NetworkReachabilityManager` 首先定义了 `NetworkReachabilityStatus` 的 `enum` 类型：

```swift
public enum NetworkReachabilityStatus {
    /// 不确定网络状态
    case unknown
    /// 无法连接
    case notReachable
    /// 可以连接，具体类型由 ConnectionType 定义
    case reachable(ConnectionType)

    init(_ flags: SCNetworkReachabilityFlags) {
        // isActuallyReachable 为 Alamofire 定义的 extension 属性
        guard flags.isActuallyReachable else { self = .notReachable; return }
		  // 先初始化为 .ethernetOrWiFi ，然后判断是否为蜂窝网络，如果是蜂窝网络再转为 . cellular
        var networkStatus: NetworkReachabilityStatus = .reachable(.ethernetOrWiFi)
        if flags.isCellular { networkStatus = .reachable(.cellular) }
        self = networkStatus
    }

    /// 定义可以连接时的网络状态类型
    public enum ConnectionType {
        case ethernetOrWiFi
        case cellular
    }
}
```

### MutableState

`MutableState` 为 `NetworkReachabilityManager` 一些可变状态的封装：

```swift
struct MutableState {
    var listener: Listener?
    var listenerQueue: DispatchQueue?
    var previousStatus: NetworkReachabilityStatus?
}
```

`NetworkReachabilityManager` 的 `mutableState` 属性使用 `@Protected` 进行声明，保证线程安全。

### 属性

监听 0.0.0.0 地址的单例， `listenerQueue` 为 `.main` ：

```swift
public static let `default` = NetworkReachabilityManager()
```

```swift
/// 当前的网络状态是否可以连接
open var isReachable: Bool { return isReachableOnCellular || isReachableOnEthernetOrWiFi }

/// 当前的蜂窝网络是否可用
/// - 用于判断一些是否推荐执行一些需要高或者低带宽的请求，如视频自动播放
open var isReachableOnCellular: Bool { return status == .reachable(.cellular) }

/// 当前的 WiFi 是否可用
open var isReachableOnEthernetOrWiFi: Bool { return status == .reachable(.ethernetOrWiFi) }

/// `DispatchQueue` 系统 Reachability的更新 queue.
public let reachabilityQueue = DispatchQueue(label: "org.alamofire.reachabilityQueue")

/// 可选的 SCNetworkReachabilityFlags
open var flags: SCNetworkReachabilityFlags? {
    var flags = SCNetworkReachabilityFlags()

    return (SCNetworkReachabilityGetFlags(reachability, &flags)) ? flags : nil
}

/// 当前网络状态，使用 Optional 的 map 方法动态生成
open var status: NetworkReachabilityStatus {
    return flags.map(NetworkReachabilityStatus.init) ?? .unknown
}

/// 系统的 `SCNetworkReachability` ，用于发送通知
private let reachability: SCNetworkReachability

/// 线程安全的 `MutableState`
@Protected
private var mutableState = MutableState()
```

### 初始化

`NetworkReachabilityManager` 提供了两个 `convenience init?` 方法：

```swift
// 监听指定 host
public convenience init?(host: String) {
    guard let reachability = SCNetworkReachabilityCreateWithName(nil, host) else { return nil }
    self.init(reachability: reachability)
}

// 监听 0.0.0.0 地址
public convenience init?() {
    var zero = sockaddr()
    zero.sa_len = UInt8(MemoryLayout<sockaddr>.size)
    zero.sa_family = sa_family_t(AF_INET)

    guard let reachability = SCNetworkReachabilityCreateWithAddress(nil, &zero) else { return nil }

    self.init(reachability: reachability)
}

// 上面两个方法如果成功生成 SCNetworkReachability ，到最后会调用这个方法来进行初始化
private init(reachability: SCNetworkReachability) {
    self.reachability = reachability
}
```

### 流程

`startListening` 添加监听：

```swift
@discardableResult
open func startListening(onQueue queue: DispatchQueue = .main,
                         onUpdatePerforming listener: @escaping Listener) -> Bool {
    stopListening()
    // 修改 mutableState ，这里使用的是 @propertyWrapper 的语法糖，直接访问 projectedValue 也就是 Protected<MutableState>
    // 这样就可以调用 Protected<MutableState> 的 write 方法
    $mutableState.write { state in
        state.listenerQueue = queue
        state.listener = listener
    }
    // 与 SCNetworkReachability 交互，添加 callBack 。
    var context = SCNetworkReachabilityContext(version: 0,
                                               info: Unmanaged.passUnretained(self).toOpaque(),
                                               retain: nil,
                                               release: nil,
                                               copyDescription: nil)
    let callback: SCNetworkReachabilityCallBack = { _, flags, info in
        guard let info = info else { return }

        let instance = Unmanaged<NetworkReachabilityManager>.fromOpaque(info).takeUnretainedValue()
        instance.notifyListener(flags)
    }

    let queueAdded = SCNetworkReachabilitySetDispatchQueue(reachability, reachabilityQueue)
    let callbackAdded = SCNetworkReachabilitySetCallback(reachability, callback, &context)

    // 因为 SCNetworkReachability 不会在初始化时调用一次 callBack ，所以这里有手动调一下。
    if let currentFlags = flags {
        reachabilityQueue.async {
            self.notifyListener(currentFlags)
        }
    }

    return callbackAdded && queueAdded
}
```

由于 `NetworkReachabilityManager.default` 获取的是单例，调用 `startListening` 会清空之前的 `mutableState` ，导致无法调用之前的 `listener` ，所以还是使用自己生成的 `NetworkReachabilityManager` 比较好，各自管理自己的 `mutableState` 。

`notifyListener` 网络状态变化时调用，执行对应的 `listener` ：

```swift
func notifyListener(_ flags: SCNetworkReachabilityFlags) {
    let newStatus = NetworkReachabilityStatus(flags)

    $mutableState.write { state in
		  // 如果状态相等就不调用 listener
        guard state.previousStatus != newStatus else { return }

        state.previousStatus = newStatus

        let listener = state.listener
        state.listenerQueue?.async { listener?(newStatus) }
    }
}
```

`stopListening` 停止监听，调用 `SCNetworkReachabilitySetCallback` 和 `SCNetworkReachabilitySetDispatchQueue` 清空 `reachability` ，然后清空 `mutableState` 的属性：

```swift
open func stopListening() {
    SCNetworkReachabilitySetCallback(reachability, nil, nil)
    SCNetworkReachabilitySetDispatchQueue(reachability, nil)
    $mutableState.write { state in
        state.listener = nil
        state.listenerQueue = nil
        state.previousStatus = nil
    }
}
```

### 总结

1. 不要通过 `NetworkReachabilityManager` 来判断是否应该发送请求；
2. 当网络状态切换时，可以考虑重新发送请求；
3. 网络状态可以为用户请求失败提供一些更明确的提示；
4. 判断用户的网络状态来执行不同的流量策略，如视频的清晰度；

## 最后

Alamofire 作为一个使用 `Swift` 编写的网络库，提供的发起网络请求接口十分简单，学习成本非常低，有不少值得学习和借鉴的地方：

1. 使用协议进行抽象；
2. 使用 `@propertyWrapper` 来实现属性的线程安全；
3. 支持链式调用，使用上更加优雅和方便；
4. 借用 `extension` 来为 `protocol` 提供默认的方法实现，从而使得 `protocol` 的方法是可选的； ……
