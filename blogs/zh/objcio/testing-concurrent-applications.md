---
title: 测试并发应用
source: objc.io
source_key: objcio
source_url: 'https://www.objc.io/issues/2-concurrency/async-testing'
original_language: en
published: ''
status: frozen
license: 未声明（页面无版权声明，文章版权归各作者）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b8ff43de63dd1ba8'
translated: true
---

> 原文：[Testing Concurrent Applications](https://www.objc.io/issues/2-concurrency/async-testing)　·　objc.io

测试是开发过程中打造高质量应用的重要工具。过去，当并发还不是应用架构中那么重要的一部分时，测试相对直接。过去几年里，采用并发设计模式变得越来越重要，我们也面临挑战，需要发展出测试它们的新最佳实践。

测试并发代码的主要难点在于：程序或信息流不再体现在调用栈上。函数不会立刻把结果返回给调用方，而是稍后通过回调函数、block、通知或类似机制交付，这使得测试更加困难。

不过，测试异步代码也有好处：它能暴露糟糕的设计决策，并促成更干净的实现。

## 异步测试的问题

我们先回顾一个简单的同步单元测试示例。这个简易计算器的方法应把两个数相加：

```
+ (int)add:(int)a to:(int)b {
    return a + b;
}
```

测试这个方法很简单：调用方法，把结果与期望值比较。若不匹配，测试失败。

```
- (void)testAddition {
    int result = [Calculator add:2 to:2];
    STAssertEquals(result, 4, nil);
}
```

现在把该方法改成通过 completion block 异步返回结果。我们还会在实现里故意加一个 bug，以便期望测试失败：

```
+ (int)add:(int)a to:(int)b block:(void(^)(int))block {
    [[NSOperationQueue mainQueue] addOperationWithBlock^{
        block(a - b); // Buggy implementation
    }];
}
```

当然这是个刻意简化的例子，但它反映了在运算更重时你经常会用到的通用模式。

测试该方法的一种天真做法，只是把断言挪进 completion block。然而，尽管实现里有 bug，这样的测试却永远不会失败：

```
// don't use this code!
- (void)testAdditionAsync {
    [Calculator add:2 to:2 block^(int result) {
        STAssertEquals(result, 4, nil); // Never fails!
    }];
}
```

为什么这个断言不会失败？

## SenTestingKit 内部机制

Xcode 4 使用的测试框架基于 [OCUnit](http://www.sente.ch/software/ocunit/)，这让我们能更仔细地看内部实现。要理解异步测试的问题，需要看看测试套件各部分的执行顺序。下图是一个简化流程。

![](https://www.objc.io/images/issue-2/SenTestingKit-call-stack@2x_3c83bfa.png)

测试套件在主 run loop 上启动后，会执行以下主要步骤：

1. 搭建包含全部相关测试的测试套件（例如由工程 scheme 指定）。
2. 运行该套件，内部会调用所有以 _test_ 开头的测试用例方法。这次运行返回一个对象，其中包含每个测试的结果。
3. 通过调用 `exit()` 退出进程。

有趣的部分是每个单独测试如何被调用。在异步测试期间，包含断言的 completion block 会被排入主 run loop。由于测试框架在所有测试跑完后就会退出进程，这个 block 永远不会执行，因此也永远不会让测试失败。

有几种办法解决这个问题。但它们都必须在测试方法返回、框架检查结果之前，运行主 run loop 并处理已入队的操作。

[Kiwi](https://github.com/allending/Kiwi) 使用 probe poller，可在测试方法内调用。[GHUnit](https://github.com/gabriel/gh-unit/) 提供单独的测试类，需在测试方法内准备，并在结束时发通知。两种情况下，我们都要写一些代码，确保测试方法在测试完成前不会返回。

## SenTestingKit 的异步扩展

我们对这个问题的解决方案是一个内置测试套件的[扩展](https://github.com/nxtbgthng/SenTestingKitAsync)：它把栈上的同步执行拆开，把每一段作为 block 排入主队列。如下图所示，报告异步测试成功或失败的 block，会在检查整个套件结果之前入队。这种执行顺序让我们可以启动测试并等待其结果。

![](https://www.objc.io/images/issue-2/SenTestingKitAsync-call-stack@2x_6503fd7.png)

为了提示框架某个测试应按异步处理，方法名必须以 **Async** 结尾。此外，在异步测试中，我们必须手动报告测试用例成功，并包含超时，以防 completion block 永远不被调用。可以把上面有问题的测试改写成这样：

```
- (void)testAdditionAsync {
    [Calculator add:2 to:2 block^(int result) {
        STAssertEquals(result, 4, nil);
        STSuccess(); // Calling this macro reports success
    }];
    STFailAfter(2.0, @"Timeout");
}
```

## 设计异步测试

与同步测试一样，异步测试应始终比它们所测的实现简单一个数量级。复杂测试并不能促进更高的代码质量，因为测试本身出 bug 的可能性会增加。在测试驱动开发过程中，简单测试能让我们更清晰地思考组件边界、接口，以及架构的预期行为。

### 示例项目

为付诸实践，我们创建了一个名为 [PinacotecaCore](https://github.com/objcio/issue-2-async-testing) 的示例框架，它从一个假想服务器请求图片信息。它有一个资源管理器，作为面向开发者的接口，提供按图片 id 获取图片对象的方法。在后台，资源管理器从服务器拉取信息，并更新数据库中的属性。

尽管这只是为演示而设的示例项目，它与我们在多个应用中使用的模式相同。

![](https://www.objc.io/images/issue-2/PinacotecaCore@2x_97ecfbf.png)

有了架构的高层概览，我们就可以深入框架的测试。一般应测试三个组件：

1. 模型层
2. 服务器 API 控制器，抽象对服务器的请求
3. 资源管理器，管理 core data 栈，并把模型层与 API 控制器连在一起

### 模型层

只要可能，测试就应是同步的；模型层是个好例子。只要不同 managed object context 之间没有复杂依赖，测试用例就应搭建自己的 core data 栈，在主线程上的 context 中执行操作。

在本例中，[测试用例](https://github.com/objcio/issue-2-async-testing/blob/master/PinacotecaCore/PinacotecaCoreTests/PCModelLayerTests.m) 在 `setUp` 中搭建 core data 栈，检查 `PCImage` 的 entity description 是否存在，用构造器创建对象并更新其值。这与异步测试无关，此处不再展开。

### 服务器 API 控制器

架构的第二块积木是服务器 API 控制器。它包含把服务器 API 映射到模型的逻辑，并处理请求。总体而言，我们想评估下列方法的行为：

```
- [PCServerAPIController fetchImageWithId:queue:completionHandler:]
```

它应被传入图片 id，并在给定队列上调用 completion handler。

因为服务器尚不存在，也因为这是好习惯，我们会用 [OHHTTPStubs](https://github.com/AliSoftware/OHHTTPStubs) 对网络请求做 stub。在最新版本中，项目可以包含一个带有示例响应的 bundle，这些响应会交付给客户端。

要 stub 请求，需在测试 setup 或测试本身中配置 OHHTTPStubs。首先要加载包含响应的 bundle：

```
NSURL *url = [[NSBundle bundleForClass:[self class]]
                        URLForResource:@"ServerAPIResponses"
                         withExtension:@"bundle"];
                                             
NSBundle *bundle = [NSBundle url];
```

然后可以从 bundle 加载响应，并指定应对哪个请求返回：

```
OHHTTPStubsResponse *response;
response = [OHHTTPStubsResponse responseNamed:@"images/123"
                                   fromBundle:responsesBundle
                                 responseTime:0.1];

[OHHTTPStubs stubRequestsPassingTest:^BOOL(NSURLRequest *request) {
    return YES /* true, if it's the expected request */;
} withStubResponse:^OHHTTPStubsResponse *(NSURLRequest *request) {
    return response;
}];
```

有了这些设置，简化版的 [API 控制器测试](https://github.com/objcio/issue-2-async-testing/blob/master/PinacotecaCore/PinacotecaCoreTests/PCServerAPIControllerTests.m) 如下：

```
- (void)testFetchImageAsync
{
    [self.server
        fetchImageWithId:@"123"
                   queue:[NSOperationQueue mainQueue]
       completionHandler:^(id imageData, NSError *error) {
          STAssertEqualObjects([NSOperationQueue currentQueue], queue, nil);
          STAssertNil(error, [error localizedDescription]);
          STAssertTrue([imageData isKindOfClass:[NSDictionary class]], nil);
                
          // Check the values of the returned dictionary.
                
          STSuccess();
       }];
    STFailAfter(2.0, nil);    
}
```

### 资源管理器

最后一个组件是资源管理器，它把模型层与 API 控制器连在一起，并管理 core data 栈。这里我们要测试获取图片对象的方法：

```
-[PCResourceManager imageWithId:usingManagedObjectContext:queue:updateHandler:]
```

该方法应按给定 id 返回图片对象。若数据库中没有该图片，它会返回一个仅含 id 的新对象，并调用 API 控制器请求详细信息。

由于资源管理器的测试不应依赖 API 控制器，我们用 [OCMock](http://ocmock.org) 对其做 stub；它对方法的部分 stub 很理想。这在[资源管理器测试](https://github.com/objcio/issue-2-async-testing/blob/master/PinacotecaCore/PinacotecaCoreTests/PCResourceManagerTests.m)中完成：

```
OCMockObject *mo;
mo = [OCMockObject partialMockForObject:self.resourceManager.server];

id exp = [[serverMock expect] 
             andCall:@selector(fetchImageWithId:queue:completionHandler:)
            onObject:self];
[exp fetchImageWithId:OCMOCK_ANY queue:OCMOCK_ANY completionHandler:OCMOCK_ANY];
```

测试不会调用 API 控制器的真实方法，而是使用测试用例自身实现的方法。

有了这些，资源管理器的测试就很直接了。它调用管理器获取资源，内部会调用 API 控制器上被 stub 的方法。在那里我们可以检查控制器是否以正确参数被调用。调用结果 handler 之后，资源管理器更新模型，并会调用我们测试的结果 handler。

```
- (void)testGetImageAsync
{
    NSManagedObjectContext *ctx = self.resourceManager.mainManagedObjectContext;
    __block PCImage *img;
    img = [self.resourceManager imageWithId:@"123"
                  usingManagedObjectContext:ctx
                                      queue:[NSOperationQueue mainQueue]
                              updateHandler:^(NSError *error) {
                                       // Check if the error is nil and 
                                       // if the image has been updated.
                                       STSuccess();
                                   }];    
    STAssertNotNil(img, nil);
    STFailAfter(2.0, @"Timeout");
}
```

## 结论

一开始，测试采用并发设计模式的应用可能很有挑战，但一旦理解了差异并建立最佳实践，就会变得轻松而有趣。

在 [nxtbgthng](http://nxtbgthng.com)，我们日常使用本文所述流程以及 [SenTestingKitAsync](https://github.com/nxtbgthng/SenTestingKitAsync)。但其他方式，如 [Kiwi](https://github.com/allending/Kiwi) 或 [GHUnit](https://github.com/gabriel/gh-unit/)，也是做异步测试的好办法。你应该都试试，找到自己偏好的工具，然后开始做异步测试。

---
