---
title: '通过 HTTP 获取并解析 XML 或 JSON 的类 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2011/05/classes-for-fetching-and-parsing-xml-or.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:dc847aab64705532'
translated: true
---

> 原文：[Classes for fetching and parsing XML or JSON via HTTP | Cocoa with Love](https://www.cocoawithlove.com/2011/05/classes-for-fetching-and-parsing-xml-or.html)　·　Cocoa with Love (Matt Gallagher)

本文中，我将展示两个用于通过 HTTP 获取数据的可复用类：一个将结果解析为 XML，另一个解析为 JSON。这些任务是相对简单的操作，但涉及多个步骤，如果没有健壮、可复用的代码来处理这些任务，它们会变得很繁琐。这些类可以在 iOS 或 Mac 上运行，但可选的错误提示和密码对话框仅针对 iOS 实现。

## 引言

根据我的经验，“通过 HTTP 获取数据”大概是 iOS 应用程序执行的第二大常见任务，仅次于“在表格中显示列表”。由于我[最近写了一篇文章，展示了我如何处理表格显示](https://www.cocoawithlove.com/2010/12/uitableview-construction-drawing-and.html)，接着展示我用于通过 HTTP 获取数据的可复用类似乎是合理的后续。

与关于 `UITableView` 管理的文章一样，本文的全部目的在于尽可能让 HTTP 的获取、处理和加工变得简单且可复用。

我希望展示的是，尽管 Cocoa API 看起来让你每次需要网络连接时都必须把 `NSURLConnection` 的委托方法硬塞到你自己的类中，但这并不意味着你每次需要网络连接时真的要做所有这些工作。对于像这样的最常见任务，你应该开发自己的、可复用的、你喜欢的、满足你需求的方法，这样能使新代码更容易编写。

有很多其他类似思路的替代方案。与完整的框架相比，我的实现是一个简单的实现（如果想了解沿同一思路的更详细实现，你可能会想看看 [RestKit](http://restkit.org/)）。不过，我希望你仍然能看到它与临时解决方案的对比，尤其如果你曾经在不考虑保持接口清晰简洁的情况下，把 HTTP 通信硬塞到你的项目中。

> 你可以下载本文讨论的四个类：[HTTPXMLJSONFetchers.zip](https://www.cocoawithlove.com/assets/objc-era/HTTPXMLJSONFetchers.zip)（16kB）

## Cocoa 中的 HTTP 连接

BSD sockets 和 `CFHTTPStream` 通常级别太低，不适合常规使用。除非你的程序需要对网络层进行精细控制，否则你可能希望使用 `NSURLConnection` 来处理 HTTP 获取。

从技术上讲，`NSURLConnection` 可以通过一条指令执行网络连接：`+[NSURLConnection sendSynchronousRequest:returningResponse:error:]`。除少数罕见的工作线程场景外，应避免使用同步连接，因为它会阻塞程序的用户界面，并且不允许进行细致的错误处理。

这意味着在通过 HTTP 获取数据时，你应该使用 `NSURLConnection` 的委托方法。这些委托方法是：

```objc
- (void)connection:(NSURLConnection *)connection didReceiveResponse:(NSURLResponse *)response
- (void)connection:(NSURLConnection *)connection didReceiveData:(NSData *)data
- (void)connection:(NSURLConnection *)connection didFailWithError:(NSError *)error
- (void)connection:(NSURLConnection *)aConnection didReceiveAuthenticationChallenge:(NSURLAuthenticationChallenge *)aChallenge
- (void)connectionDidFinishLoading:(NSURLConnection *)connection
```

一个完整的实现意味着要实现所有这 5 个方法。

一种常见的做法是把 `NSURLConnection` 的委托方法添加到你的 `UITableViewController` 中，并让那个视图控制器来管理连接。

虽然这看起来是个好主意（视图控制器可以跟踪连接状态、提供视觉更新并显示自己的错误），但现实是完整处理连接需要大量代码。有多少代码？我使用的代码有 530 行（包括注释和空格）。

但这还有一个更严重的问题：将 `NSURLConnection` 绑定到你的 `UITableViewController` 限制了代码的可复用性。如果你的网络代码与视图控制器紧密耦合，那么向其他视图控制器或程序的其他部分添加网络行为将需要更多的工作。

为什么实现 `NSURLConnection` 委托需要这么多代码？在最简单的情况下，不需要（你可能用大约 20 行就能管理一个连接），但你会忽略很多更微妙的行为。错误处理、密码认证、干净地取消连接以及提供简单构造 vs 精细构造，这些行为如果你每次都重写代码或者在严格的时间限制下操作，很可能就被遗漏了。

## HTTPFetcher

我的 `HTTPFetcher` 类背后的思路非常简单：它是一个可复用的 `NSURLConnection` 委托。它处理所有 `NSURLConnection` 的委托工作，并在得到结果时进行回调。它提供默认的错误处理、密码认证，虽然它有一个非常简单的默认构造器，但仍然提供了足够的钩子（hooks）让你可以自定义其行为。

该类的接口实际上只是构造方法、开始、取消和一些属性。`assign` 属性用于在启动之前配置连接。`readonly` 属性用于在连接完成后收集信息。

```objc
@interface HTTPFetcher : NSObject &lt;UITextFieldDelegate&gt;

@property (nonatomic, readonly) NSData *data;
@property (nonatomic, readonly) NSURLRequest *urlRequest;
@property (nonatomic, readonly) NSDictionary *responseHeaderFields;
@property (nonatomic, readonly) NSInteger failureCode;
@property (nonatomic, assign) BOOL showAlerts;
@property (nonatomic, assign) BOOL showAuthentication;
@property (nonatomic, assign) void *context;

- (id)initWithURLRequest:(NSURLRequest *)aURLRequest
    receiver:(id)aReceiver
    action:(SEL)receiverAction;
- (id)initWithURLString:(NSString *)aURLString
    receiver:(id)aReceiver
    action:(SEL)receiverAction;
- (id)initWithURLString:(NSString *)aURLString
    timeout:(NSTimeInterval)aTimeoutInterval
    cachePolicy:(NSURLCacheStoragePolicy)aCachePolicy
    receiver:(id)aReceiver
    action:(SEL)receiverAction;
- (void)start;
- (void)cancel;

@end
```

你可以以任何你喜欢的方式初始化该类（这里显示的中间那个 init 方法是最简单的），可选地配置该类（最常见的配置是设置 `context` 指针，这样当连接完成时，你可以记住在哪里设置数据），启动连接，然后它将调用你 `receiver` 对象的 `receiverAction`（接收者 action 接受一个参数：`HTTPFetcher` 自身）。

```objc
// 示例获取器创建
fetcher = [[HTTPFetcher alloc]
    initWithURLString:@"http://some-domain.com/some/path"
    receiver:self
    action:@selector(receiveResponse:)];
[fetcher start];

// 示例获取器响应处理
- (void)receiveResponse:(HTTPFetcher *)aFetcher
{
    NSAssert(aFetcher == fetcher,
        @"In this example, aFetcher is always the same as the fetcher ivar we set above");
    if ([fetcher.data length] &gt; 0)
    {
        [self doSomethingWithTheData:fetcher.data];
    }
    [fetcher release];
    fetcher = nil;
}
```

通常，你的程序会想要自定义呈现错误的代码，并使呈现方式与你的应用程序一致。你可以通过子类化或编辑 `HTTPFetcher` 类本身来实现，也可以禁用提示和认证功能，在类外部执行这些工作。但是，如果没有时间进行这种自定义，该类中的默认行为也能满足要求。

> **HTTPFetcher 内存管理**：`HTTPFetcher` 在运行时不会 retain 自己，也不会 retain `receiver`。这是因为预期的行为是接收者 retain `HTTPFetcher`，而我们不希望出现[保留循环（retain cycle）](https://www.cocoawithlove.com/2009/07/rules-to-avoid-retain-cycles.html)。如果你创建了 `HTTPFetcher` 但没有保持它的引用计数，它会立即自动取消 `cancel` 并 `dealloc`。

## XMLFetcher

如果你只是想要 HTTP 连接的数据，`HTTPFetcher` 就很好。但就我个人而言，我从未单独使用过 `HTTPFetcher`——我总是把它用作类的基类，这些类会在调用接收者回调方法之前对 HTTP 数据进行后处理。

`XMLFetcher` 类用于将 XML 响应转换为更有用的形式。你不需要查看 `HTTPFetcher` 的 `data` 属性，而是可以使用 `results` 属性，它是与 XML 结果中给定 XPath 查询匹配的节点数组。

```objc
@interface XMLFetcher : HTTPFetcher

@property (nonatomic, copy, readonly) NSString *xPathQuery;
@property (nonatomic, retain, readonly) NSArray *results;

- (id)initWithURLString:(NSString *)aURLString
    xPathQuery:(NSString *)query
    receiver:(id)aReceiver
    action:(SEL)receiverAction;

@end
```

我[之前说过](https://www.cocoawithlove.com/2008/10/using-libxml2-for-parsing-and-xpath.html)，我不喜欢 iOS API 中 Apple 推崇的事件驱动模型（有时称为 SAX 解析器）。对于大文件，它确实内存效率高且速度更快，但它要求你自己进行结构化的处理，这很繁琐、容易出错且不可复用。我个人更喜欢像 Mac OS X 中存在但 iOS 中没有的 `NSXML` API 那样的基于文档的模型。

`XMLFetcher` 类将基于 libXML 的 XPath 解析和查询与 `HTTPFetcher` 融合在一起。

不过，我也解决了之前基于 libXML 解析的一些缺点。那段早期代码的最大问题是它简单地将 XML 打包成 `NSDictionary`（充其量是不优雅的）——所以现在的结果是一个专用的 `XPathResultNode` 类，它可以清晰地表示 `attributes`、`childNodes` 和 `contentString`。此外，对于子节点两侧的内容字符串以及分散在子节点上的文本数据的拼接，也有了更好的处理。

```objc
@interface XPathResultNode : NSObject

@property (nonatomic, retain, readonly) NSString *name;
@property (nonatomic, retain, readonly) NSMutableDictionary *attributes;
@property (nonatomic, retain, readonly) NSMutableArray *content;

+ (NSArray *)nodesForXPathQuery:(NSString *)query onHTML:(NSData *)htmlData;
+ (NSArray *)nodesForXPathQuery:(NSString *)query onXML:(NSData *)xmlData;

- (NSArray *)childNodes;
- (NSString *)contentString;
- (NSString *)contentStringByUnifyingSubnodes;

@end
```

XPath 查询说明：XPath 查询可能需要一些时间来适应——如果你不熟悉 XPath，可能很难提取出你想要的精确节点。不过，像正则表达式一样，它们是一种用于提取数据的高度专用语言，一旦你理解了可用的不同函数，它们就是从 XML 中获取特定节点的最快方式。

> **编译器说明**：XPathResultNode.m 文件中的一段注释说明了使其正常工作所需的 Xcode 编译器设置。基本上，你需要在包含路径中包含 libxml，并将你的项目与 libxml2.dylib 链接。

## JSONFetcher

`JSONFetcher` 的思路与 `XMLFetcher` 基本相同——在完成时解析来自 `HTTPFetcher` 的结果，这次是作为 JSON 数据。

我编写的这个类依赖于 [SBJSON](http://stig.github.com/json-framework/)，Stig Brautaset 的 BSD 许可的 JSON 解析库。你需要单独下载这些文件并将它们包含到你的项目中（共 3 个 .m 文件和 4 个 .h 文件）。

在 iOS 或 Mac OS X 中，SBJSON 不是处理 JSON 的唯一选择。如果你更喜欢其他选择，这里有一些在 Stackoverflow 上讨论的[iOS 和 Mac 的其他 JSON 库](http://stackoverflow.com/questions/2256625/comparison-of-json-parser-for-objective-c-json-framework-yajl-touchjson-etc)。不过，显然你需要做一些小的调整来集成不同的解析器。

对于 JSON 响应，通常不存在在更大结果中查找子节点的需求（这在 XML 中是常见情况），所以 JSON 解析器简单地解析整个 JSON 结构并返回所有内容。

```objc
@interface JSONFetcher : HTTPFetcher

@property (nonatomic, readonly) id result;

@end
```

## 结论

> 你可以下载本文讨论的四个类：[HTTPXMLJSONFetchers.zip](https://www.cocoawithlove.com/assets/objc-era/HTTPXMLJSONFetchers.zip)（16kB）

我介绍了用于处理这些任务的类。我不期望每个人都有和我一样的数据和网络需求，所以你很可能需要非常不同的类来满足自己确切的需求。

关键在于考虑你代码中的可复用性——如何改进你的类，使得当你开始一个新项目时，需要重写的代码尽可能少——你只需引入自己的网络数据处理类，向它的构造器传递不同的参数，网络连接就完成了。

在我为自己组合出这些类之前，新项目需要数百行代码，这些代码通过复制、粘贴、重构从我已经写的现有项目中得来。虽然复制、粘贴、重构也能工作，但相比设计良好的可复用类，它更慢、更容易出错且更难保持最新。在大多数情况下，你应该将复制粘贴视为你流程上的失败。这是一个很难遵守的规则，因为复制、粘贴、重构比设计一个可复用类更快——至少在最初是这样（与预先的设计工作相比）。你需要有纪律，能识别类或项目之间的共同行为，并在需要时重构到共享类中。

最后一点思考：我意识到我并没有真正在一个示例程序中展示这些类的工作情况。如果你无法弄清楚如何在实际程序中使用它们，请等一两周：我计划分享一个使用它们处理所有网络通信的真实项目。
