---
title: 常见后台实践
source: objc.io
source_key: objcio
source_url: 'https://www.objc.io/issues/2-concurrency/common-background-practices'
original_language: en
published: ''
status: frozen
license: 未声明（页面无版权声明，文章版权归各作者）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:26cee37f62584858'
translated: true
---

> 原文：[Common Background Practices](https://www.objc.io/issues/2-concurrency/common-background-practices)　·　objc.io

本文将描述在后台执行常见任务的最佳实践。我们会看看如何并发使用 Core Data、如何并发绘制，以及如何做异步网络请求。最后，我们会看看如何在保持较低内存占用的同时异步处理大文件。

异步编程很容易出错。因此，本文所有示例都会采用非常简单的方法。使用简单结构有助于我们想通代码并保持全局视野。若你最终得到复杂的嵌套回调，大概应该重新审视一些设计决策。

## Operation Queues 与 Grand Central Dispatch

目前，iOS 和 OS X 上有两套主要的现代并发 API：[operation queues](http://developer.apple.com/library/ios/#documentation/Cocoa/Reference/NSOperationQueue_class/Reference/Reference.html) 和 [Grand Central Dispatch](https://developer.apple.com/library/ios/#documentation/Performance/Reference/GCD_libdispatch_Ref/Reference/reference.html)（GCD）。GCD 是底层 C API，而 operation queues 构建在 GCD 之上，并提供 Objective-C API。关于可用并发 API 的更全面概览，见本期的[并发 API 与挑战](https://www.objc.io/issues/2-concurrency/concurrency-apis-and-pitfalls/)一文。

Operation queues 提供一些用 GCD 不易复现的便利特性。实践中，最重要的之一是可以取消队列中的 operations，如下文所示。Operation queues 也让管理 operations 之间的依赖稍容易一些。另一方面，GCD 给你更多控制以及 operation queues 所没有的底层功能。更多细节请参阅[底层并发 API](https://www.objc.io/issues/2-concurrency/low-level-concurrency-apis/)一文。

进一步阅读：

- [StackOverflow: NSOperation vs. Grand Central Dispatch](http://stackoverflow.com/questions/10373331/nsoperation-vs-grand-central-dispatch)
- [Blog: When to use NSOperation vs. GCD](http://eschatologist.net/blog/?p=232)

### 后台中的 Core Data

**2015 年 3 月更新**：本文基于现已过时的 Core Data Concurrency Guide 中较旧的建议。

在用 Core Data 做任何并发事情之前，把基础做对很重要。我们强烈建议通读 Apple 的 [Concurrency with Core Data](https://developer.apple.com/library/mac/#documentation/cocoa/conceptual/CoreData/Articles/cdConcurrency.html) 指南。该文档规定了基本规则，例如绝不在线程之间传递 managed objects。这不仅意味着你绝不该在另一线程上修改 managed object，还意味着你绝不该从中读取任何属性。要传递对象，应传递其 object ID，并从与另一线程关联的 context 中取回对象。

只要遵守这些规则并使用本文描述的方法，用 Core Data 做并发编程就很简单。

Xcode 模板中 Core Data 的标准设置是：一个 persistent store coordinator，加上一个在主线程上运行的 managed object context。对许多用例，这已经够用。创建一些新对象、修改现有对象非常便宜，可以毫无问题地在主线程上完成。然而，若你想做大块工作，就适合在后台 context 中进行。典型例子是把大型数据集导入 Core Data。

我们的方法非常简单，且在现有文献中已有充分讨论：

1. 我们为导入工作创建一个单独的 operation
2. 我们创建一个与主 managed object context 使用同一 persistent store coordinator 的 managed object context
3. 一旦导入 context 保存，我们就通知主 managed object context 并合并变更

在[示例应用](https://github.com/objcio/issue-2-background-core-data)中，我们将导入柏林市的一大套公交数据。导入期间，我们显示进度指示器，并希望在导入过久时能够取消当前导入。此外，我们用 table view 显示迄今已有的全部数据，并在新数据到来时自动更新。示例数据集以 Creative Commons 许可公开，可在[此处](http://stg.daten.berlin.de/datensaetze/vbb-fahrplan-2013)下载。它符合 [General Transit Feed](https://developers.google.com/transit/gtfs/reference) 格式——一种开放的公交数据标准。

我们创建 `ImportOperation` 作为 `NSOperation` 的子类，由其处理导入。我们重写 `main` 方法，这是将完成全部工作的方法。这里我们创建一个使用 private queue concurrency type 的独立 managed object context。这意味着该 context 会管理自己的队列，且其上的所有操作都需要用 `performBlock` 或 `performBlockAndWait` 执行。这对确保它们在正确线程上执行至关重要。

```
NSManagedObjectContext* context = [[NSManagedObjectContext alloc]
    initWithConcurrencyType:NSPrivateQueueConcurrencyType];
context.persistentStoreCoordinator = self.persistentStoreCoordinator;
context.undoManager = nil;
[self.context performBlockAndWait:^
{
    [self import];
}];
```

注意我们复用了现有的 persistent store coordinator。在现代代码中，你应以 `NSPrivateQueueConcurrencyType` 或 `NSMainQueueConcurrencyType` 初始化 managed object contexts。第三种并发类型常量 `NSConfinementConcurrencyType` 用于遗留代码，我们的建议是不要再使用它。

要做导入，我们遍历文件中的行，并为每一行可解析的内容创建一个 managed object：

```
[lines enumerateObjectsUsingBlock:
  ^(NSString* line, NSUInteger idx, BOOL* shouldStop)
  {
      NSArray* components = [line csvComponents];
      if(components.count < 5) {
          NSLog(@"couldn't parse: %@", components);
          return;
      }
      [Stop importCSVComponents:components intoContext:context];
  }];
```

要启动此 operation，我们从 view controller 执行如下代码：

```
ImportOperation* operation = [[ImportOperation alloc] 
     initWithStore:self.store fileName:fileName];
[self.operationQueue addOperation:operation];
```

对于后台导入，你要做的就是这些。现在我们添加取消支持，幸运的是，只需在枚举 block 中加一处检查即可：

```
if(self.isCancelled) {
    *shouldStop = YES;
    return;
}
```

最后，为支持进度指示，我们在 operation 上创建一个 `progressCallback` 属性。必须在主线程上更新进度指示器，否则 UIKit 会崩溃。

```
operation.progressCallback = ^(float progress) 
{
    [[NSOperationQueue mainQueue] addOperationWithBlock:^
    {
        self.progressIndicator.progress = progress;
    }];
};
```

要调用进度 block，我们在枚举 block 中加入以下行：

```
self.progressCallback(idx / (float) count);
```

然而，若运行此代码，你会看到一切都慢得离谱。而且看起来 operation 不会立即取消。原因是主 operation queue 被想要更新进度指示器的 blocks 塞满了。简单的解决办法是降低更新粒度，即我们只对已导入行数的百分之一调用进度回调：

```
NSInteger progressGranularity = lines.count / 100;

if (idx % progressGranularity == 0) {
    self.progressCallback(idx / (float) count);
}
```

### 更新主 Context

我们应用中的 table view 由主线程上的 fetched results controller 支撑。在导入期间与之后，我们希望在 table view 中显示导入结果。

要使这工作，还缺一块：导入后台 context 的数据不会传播到主 context，除非我们显式告诉它这样做。我们在设置 Core Data 栈的 `Store` 类的 `init` 方法中加入以下代码：

```
[[NSNotificationCenter defaultCenter] 
    addObserverForName:NSManagedObjectContextDidSaveNotification
                object:nil
                 queue:nil
            usingBlock:^(NSNotification* note)
{
    NSManagedObjectContext *moc = self.mainManagedObjectContext;
    if (note.object != moc)
        [moc performBlock:^(){
            [moc mergeChangesFromContextDidSaveNotification:note];
        }];
    }];
}];
```

注意，通过对主 managed object context 调用 `performBlock:`，该 block 会在主线程上被调用。若你现在启动应用，会注意到 table view 在导入结束时重新加载数据。然而，这会阻塞用户界面好几秒。

要修复这一点，我们需要做本就该做的事：分批保存。做大型导入时，你要确保定期保存，否则可能耗尽内存，性能通常也会变差。此外，定期保存会把主线程上更新 table view 的工作随时间摊开。

多久保存一次是试错问题。保存太频繁，你会在 I/O 上花太多时间。保存太少，应用会变得无响应。我们在尝试不同数字后把批大小设为 250。现在导入流畅，会更新 table view，也不会长时间阻塞主 context。

### 其他考虑

在导入 operation 中，我们把整个文件读入字符串，再按行拆分。这对相对较小的文件可行，但对较大文件，按行惰性读取更合理。本文最后一个例子会用输入流恰好做到这一点。Dave DeLong 在 StackOverflow 上也有一篇出色的[文章](http://stackoverflow.com/questions/3707427/how-to-read-data-from-nsfilehandle-line-by-line/3711079#3711079)展示如何做。

与其在应用首次运行时把大型数据集导入 Core Data，你也可以在应用包中附带一个 sqlite 文件，或从服务器下载——你甚至可以在服务器上动态生成它。若你的具体用例适用此方案，会快得多，并节省设备上的处理时间。

最后，近来关于 child contexts 有很多嘈杂讨论。我们的建议是不要把它们用于后台操作。若你把后台 context 创建为主 context 的子 context，保存后台 context 时[仍会大量阻塞主线程](http://floriankugler.com/blog/2013/4/29/concurrent-core-data-stack-performance-shootout)。若你把主 context 创建为后台 context 的子 context，与使用两个独立 contexts 的更传统设置相比，你实际上一无所获，因为你仍须手动把后台的变更合并到主 context。

一个 persistent store coordinator 加两个独立 contexts 的设置，是在后台做 Core Data 的久经考验的方式。除非有非常充分的理由，否则坚持用它。

进一步阅读：

- [Core Data Programming Guide: Efficiently importing data](http://developer.apple.com/library/ios/#documentation/Cocoa/Conceptual/CoreData/Articles/cdImporting.html)
- [Core Data Programming Guide: Concurrency with Core Data](http://developer.apple.com/library/ios/#documentation/Cocoa/Conceptual/CoreData/Articles/cdConcurrency.html#//apple_ref/doc/uid/TP40003385-SW1j)
- [StackOverflow: Rules for working with Core Data](http://stackoverflow.com/questions/2138252/core-data-multi-thread-application/2138332#2138332)
- [WWDC 2012 Video: Core Data Best Practices](https://developer.apple.com/videos/wwdc/2012/?id=214)
- [Book: Core Data by Marcus Zarra](http://pragprog.com/book/mzcd/core-data)

## 后台中的 UI 代码

首先：UIKit 只在主线程上工作。话虽如此，UI 代码中有些部分并不直接与 UIKit 相关，却可能花费相当长时间。这些任务可以移到后台，以免长时间阻塞主线程。但在开始把部分 UI 代码移到后台队列之前，衡量哪部分代码才是真正的问题至关重要。这很关键，否则你可能在优化错误的东西。

若你已识别出可以隔离的昂贵操作，把它放进 operation queue：

```
__weak id weakSelf = self;
[self.operationQueue addOperationWithBlock:^{
    NSNumber* result = findLargestMersennePrime();
    [[NSOperationQueue mainQueue] addOperationWithBlock:^{
        MyClass* strongSelf = weakSelf;
        strongSelf.textLabel.text = [result stringValue];
    }];
}];
```

如你所见，这并非完全直截了当；我们需要对 self 做弱引用，否则会创建循环引用（block retain 了 self，私有 operation queue retain 了 block，self 又 retain 了 operation queue）。在 block 内我们再转回强引用，确保运行 block 期间它不会被释放。

### 后台绘制

若你的测量显示 `drawRect:` 是性能瓶颈，可以把这段绘制代码移到后台。不过在此之前，检查是否有其他方式达到同样效果，例如使用 core animation layers，或用预渲染图像代替纯 Core Graphics 绘制。见 Florian 关于当前设备图形性能测量的[这篇博文](http://floriankugler.com/blog/2013/5/24/layer-trees-vs-flat-drawing-graphics-performance-across-ios-device-generations)，或 UIKit 工程师 Andy Matuschak 的[这条评论](https://lobste.rs/s/ckm4uw/a_performance-minded_take_on_ios_design/comments/itdkfh)，以好好感受其中涉及的所有微妙之处。

若你确实认定最佳选项是在后台执行绘制代码，解决方案相当简单。取出 `drawRect:` 方法中的代码，放进一个 operation。然后用 image view 替换原来的 view，并在 operation 完成后更新它。在绘制方法中，用 `UIGraphicsBeginImageContextWithOptions` 代替 `UIGraphicsGetCurrentContext`：

```
UIGraphicsBeginImageContextWithOptions(size, NO, 0);
// drawing code here
UIImage *i = UIGraphicsGetImageFromCurrentImageContext();
UIGraphicsEndImageContext();
return i;
```

把 `0` 作为第三个参数传入时，设备主屏幕的 scale 会自动填入，图像在 retina 与非 retina 设备上都会好看。

若你在 table view 或 collection view 的 cells 中做自定义绘制，把它们全部放进 operation 子类是合理的。你可以把它们加入后台 operation queue，并在用户把 cells 滚出可见范围时，从 `didEndDisplayingCell` 委托方法中取消它们。这一切在 [WWDC 2012 Session 211 -- Building Concurrent User Interfaces on iOS](https://developer.apple.com/videos/wwdc/2012/) 中有详细讲解。

除了自己在后台调度绘制代码，你还应试验 `CALayer` 的 `drawsAsynchronously` 属性。不过务必衡量其效果。有时它能加速，有时反而适得其反。

## 异步网络请求

你的所有网络请求都应异步完成。然而，使用 Grand Central Dispatch 时，你有时会看到这样的代码：

```
// Warning: please don't use this code.
dispatch_async(backgroundQueue, ^{
   NSData* contents = [NSData dataWithContentsOfURL:url]
   dispatch_async(dispatch_get_main_queue(), ^{
      // do something with the data.
   });
});
```

这看起来可能挺聪明，但这段代码有个大问题：没有办法取消这个同步网络调用。它会阻塞线程直到完成。若操作超时，这可能要很长时间（例如 `dataWithContentsOfURL` 的超时是 30 秒）。

若队列是串行队列，它会在整个期间被阻塞。若队列是并发的，GCD 不得不启动新线程，以弥补你正在阻塞的那条线程。两种情况都不好。最好彻底避免阻塞。

为改进这一状况，我们将使用 `NSURLConnection` 的异步方法，并把一切包装进一个 operation。这样我们就能获得 operation queues 的全部能力与便利：可以轻松控制并发 operations 数量、添加依赖，以及取消 operations。

不过这样做时有一点要注意：URL connections 在 run loop 中投递事件。最简单的是为此使用主 run loop，因为数据投递不会花太多时间。然后我们可以把对传入数据的处理派发到后台线程。

另一种可能是像 [AFNetworking](http://afnetworking.com) 这类库采取的做法：创建单独线程，在该线程上设置 run loop，并在那里调度 url connection。但你大概不会想自己做这件事。

要启动 URL connection，我们在自定义 operation 子类中重写 `start` 方法：

```
- (void)start
{
    NSURLRequest* request = [NSURLRequest requestWithURL:self.url];
    self.isExecuting = YES;
    self.isFinished = NO;
    [[NSOperationQueue mainQueue] addOperationWithBlock:^
    {
        self.connection = [NSURLConnection connectionWithRequest:request
                                                        delegate:self];
    }];
}
```

由于我们重写了 `start` 方法，现在必须自己管理 operation 的状态属性 `isExecuting` 和 `isFinished`。要取消一个 operation，我们需要取消 connection，然后设置正确的标志，好让 operation queue 知道该 operation 已完成。

```
- (void)cancel
{
    [super cancel];
    [self.connection cancel];
    self.isFinished = YES;
    self.isExecuting = NO;
}
```

当 connection 完成加载时，它会发送委托回调：

```
- (void)connectionDidFinishLoading:(NSURLConnection *)connection 
{
    self.data = self.buffer;
    self.buffer = nil;
    self.isExecuting = NO;
    self.isFinished = YES;
}
```

这就是全部了。完整源代码见 GitHub 上的[示例项目](https://github.com/objcio/issue-2-background-networking)。作为结语，我们建议要么花时间把这件事做对，要么使用像 [AFNetworking](http://afnetworking.com) 这样的库。它们提供了诸如 `UIImageView` 上异步从 URL 加载图像的分类等便利工具。在 table view 代码中使用它，会自动处理取消图像加载 operations。

进一步阅读：

- [Concurrency Programming Guide](http://developer.apple.com/library/ios/#documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091-CH1-SW1)
- [NSOperation Class Reference: Concurrent vs. Non-Concurrent Operations](http://developer.apple.com/library/ios/#documentation/Cocoa/Reference/NSOperation_class/Reference/Reference.html%23http://developer.apple.com/library/ios/#documentation/Cocoa/Reference/NSOperation_class/Reference/Reference.html%23//apple_ref/doc/uid/TP40004591-RH2-SW15)
- [Blog: synchronous vs. asynchronous NSURLConnection](http://www.cocoaintheshell.com/2011/04/nsurlconnection-synchronous-asynchronous/)
- [GitHub: `SDWebImageDownloaderOperation.m`](https://github.com/rs/SDWebImage/blob/master/SDWebImage/SDWebImageDownloaderOperation.m)
- [Blog: Progressive image download with ImageIO](http://www.cocoaintheshell.com/2011/05/progressive-images-download-imageio/)
- [WWDC 2012 Session 211: Building Concurrent User Interfaces on iOS](https://developer.apple.com/videos/wwdc/2012/)

## 进阶：后台中的文件 I/O

在 Core Data 后台示例中，我们把要导入的整个文件读入内存。这对较小文件可行，但对较大文件不可行，因为 iOS 设备上内存有限。为解决此问题，我们将构建一个做两件事的类：它在不把整个文件放进内存的情况下逐行读取文件，并在后台队列上处理文件以使应用保持响应。

为此我们使用 `NSInputStream`，它让我们能对文件做异步处理。[文档](http://developer.apple.com/library/ios/#documentation/FileManagement/Conceptual/FileSystemProgrammingGUide/TechniquesforReadingandWritingCustomFiles/TechniquesforReadingandWritingCustomFiles.html)说：若你总是从头到尾读写文件内容，流为异步这样做提供了简单接口。

无论是否使用流，逐行读取文件的一般模式如下：

1. 有一个中间缓冲区，在尚未找到换行符时向其追加
2. 从流中读取一块数据
3. 对块中找到的每个换行符，取出中间缓冲区，追加流中直到（并包括）换行符的数据，然后输出它
4. 把剩余字节追加到中间缓冲区
5. 回到第 2 步，直到流关闭

为付诸实践，我们创建了一个带有 `Reader` 类的[示例应用](https://github.com/objcio/issue-2-background-file-io)，该类正是做这件事。接口非常简单：

```
@interface Reader : NSObject
- (void)enumerateLines:(void (^)(NSString*))block
            completion:(void (^)())completion;
- (id)initWithFileAtPath:(NSString*)path;
@end
```

注意这不是 `NSOperation` 的子类。与 URL connections 一样，输入流使用 run loop 投递事件。因此，我们再次用主 run loop 做事件投递，然后把数据处理派发到后台 operation queue。

```
- (void)enumerateLines:(void (^)(NSString*))block
            completion:(void (^)())completion
{
    if (self.queue == nil) {
        self.queue = [[NSOperationQueue alloc] init];
        self.queue.maxConcurrentOperationCount = 1;
    }
    self.callback = block;
    self.completion = completion;
    self.inputStream = [NSInputStream inputStreamWithURL:self.fileURL];
    self.inputStream.delegate = self;
    [self.inputStream scheduleInRunLoop:[NSRunLoop currentRunLoop]
                                forMode:NSDefaultRunLoopMode];
    [self.inputStream open];
}
```

现在输入流会（在主线程上）向我们发送委托消息，我们通过添加 block operation，在 operation queue 上做处理：

```
- (void)stream:(NSStream*)stream handleEvent:(NSStreamEvent)eventCode
{
    switch (eventCode) {
        ...
        case NSStreamEventHasBytesAvailable: {
            NSMutableData *buffer = [NSMutableData dataWithLength:4 * 1024];
            NSUInteger length = [self.inputStream read:[buffer mutableBytes] 
                                             maxLength:[buffer length]];
            if (0 < length) {
                [buffer setLength:length];
                __weak id weakSelf = self;
                [self.queue addOperationWithBlock:^{
                    [weakSelf processDataChunk:buffer];
                }];
            }
            break;
        }
        ...
    }
}
```

处理一块数据会查看当前缓冲的数据，并追加新流入的块。然后按换行符拆成组件，并发出每一行。剩余部分再次被存下：

```
- (void)processDataChunk:(NSMutableData *)buffer;
{
    if (self.remainder != nil) {
        [self.remainder appendData:buffer];
    } else {
        self.remainder = buffer;
    }
    [self.remainder obj_enumerateComponentsSeparatedBy:self.delimiter
                                            usingBlock:^(NSData* component, BOOL last) {
        if (!last) {
            [self emitLineWithData:component];
        } else if (0 < [component length]) {
            self.remainder = [component mutableCopy];
        } else {
            self.remainder = nil;
        }
    }];
}
```

若运行示例应用，你会看到应用保持非常响应，内存也非常低（在我们的测试运行中，无论文件大小如何，堆大小都保持在 800 KB 以下）。对于分块处理大文件，这项技术大概正是你想要的。

进一步阅读：

- [File System Programming Guide: Techniques for Reading and Writing Files Without File Coordinators](http://developer.apple.com/library/ios/#documentation/FileManagement/Conceptual/FileSystemProgrammingGUide/TechniquesforReadingandWritingCustomFiles/TechniquesforReadingandWritingCustomFiles.html)
- [StackOverflow: How to read data from NSFileHandle line by line?](http://stackoverflow.com/questions/3707427/how-to-read-data-from-nsfilehandle-line-by-line)

## 结论

在以上示例中，我们演示了如何在后台异步执行常见任务。在所有这些方案中，我们尽量保持代码简单，因为并发编程很容易在不知不觉中出错。

很多时候你或许只需在主线程上完成工作就行，而当你能这样做时，生活会轻松得多。但若你发现性能瓶颈，就用尽可能简单的方法把这些任务放到后台。

上述示例中展示的模式，对其它任务也是稳妥选择。在主队列上接收事件或数据，然后用后台 operation queue 执行实际工作，再回到主队列交付结果。

---
