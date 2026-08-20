---
title: 用 Objective-C 编程
apple_id: TP40011210
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/ErrorHandling/ErrorHandling.html
archived_at: '2026-07-15T07:17:57.916774Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [用 Objective-C 编程](About%20Objective-C.md)


[下一页](Conventions.md)[上一页](Working%20with%20Blocks.md)

# 错误处理

几乎每个应用都会遇到错误。有些错误超出了你的控制范围，比如磁盘空间不足或网络连接中断。有些错误是可恢复的，比如无效的用户输入。而且，尽管所有开发者都追求完美，但偶尔也难免出现程序员的错误。

如果你是从其他平台或语言转过来的，可能习惯于在大多数错误处理中使用异常。而在使用 Objective-C 编写代码时，异常仅用于程序员的错误，比如数组越界访问或无效的方法参数。这些都是你应该在测试期间就找出并修复的问题，而不应该带到应用发布之后。

其他所有错误都由 `NSError` 类的实例来表示。本章简要介绍如何使用 `NSError` 对象，包括如何与那些可能失败并返回错误的框架方法打交道。有关更多信息，请参阅 _[错误处理编程指南](../Error%20Handling%20Programming%20Guide/Introduction%20to%20Error%20Handling%20Programming%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbw)_。

错误是任何应用生命周期中都无法避免的一部分。举例来说，如果你需要向远程 web 服务请求数据，可能会出现各种各样的潜在问题，包括：

- 没有网络连接
- 远程 web 服务可能无法访问
- 远程 web 服务可能无法提供你所请求的信息
- 你收到的数据可能与预期不符

遗憾的是，不可能为每一个可以想到的问题都构建应对方案和解决办法。相反，你必须对错误有所规划，并知道如何处理它们，从而提供尽可能好的用户体验。

如果你正在为某个执行特定任务（比如从远程 web 服务下载信息）的框架类实现一个委托对象，通常会发现你至少需要实现一个与错误相关的方法。举例来说，`NSURLConnectionDelegate` 协议就包含一个 `connection:didFailWithError:` 方法：

```objc
- (void)connection:(NSURLConnection *)connection didFailWithError:(NSError *)error;
```

如果发生错误，就会调用这个委托方法，向你提供一个 `NSError` 对象来描述这个问题。

一个 `NSError` 对象包含一个数字错误代码、错误域和描述，以及打包在用户信息字典中的其他相关信息。

Cocoa 和 Cocoa Touch 的错误并不要求每个可能的错误都有一个唯一的数字代码，而是将它们划分到不同的错误域中。举例来说，如果 `NSURLConnection` 中发生了错误，上面的 `connection:didFailWithError:` 方法就会提供一个来自 `NSURLErrorDomain` 的错误。

错误对象还包含一段本地化的描述，比如"找不到指定主机名的服务器"。

有些 Cocoa 和 Cocoa Touch API 会通过引用传回错误。举例来说，你可能会决定把从 web 服务收到的数据写入磁盘保存，使用 `NSData` 的 `writeToURL:options:error:` 方法。这个方法的最后一个参数是一个指向 `NSError` 指针的引用：

```objc
- (BOOL)writeToURL:(NSURL *)aURL
           options:(NSDataWritingOptions)mask
             error:(NSError **)errorPtr;
```

在调用这个方法之前，你需要创建一个合适的指针，以便传入它的地址：

```objc
    NSError *anyError;
    BOOL success = [receivedData writeToURL:someLocalFileURL
                                    options:0
                                      error:&anyError];
    if (!success) {
        NSLog(@"Write failed with error: %@", anyError);
        // 向用户展示这个错误
    }
```

如果发生错误，`writeToURL:...` 方法会返回 `NO`，并更新你的 `anyError` 指针，使其指向一个描述该问题的错误对象。

在处理通过引用传递的错误时，重要的是要像上面那样，通过测试方法的返回值来判断是否发生了错误，而不要只是测试错误指针是否被设置指向了某个错误。

最好的用户体验是让你的应用能够透明地从错误中恢复。举例来说，如果你正在发起一个远程 web 请求，可以尝试改用另一台服务器重新发起请求。或者，你可能需要在重试之前，向用户请求额外的信息，比如有效的用户名或密码凭据。

如果无法从错误中恢复，你应该提醒用户。如果你是在为 iOS 使用 Cocoa Touch 进行开发，需要创建并配置一个 `UIAlertView` 来显示这个错误。如果你是在为 OS X 使用 Cocoa 进行开发，可以在任何 `NSResponder` 对象（比如视图、窗口，甚至是应用对象本身）上调用 `presentError:`，这个错误就会沿着响应者链向上传播，以便进行进一步的配置或恢复。当它到达应用对象时，应用会通过一个警告面板向用户呈现这个错误。

有关向用户呈现错误的更多信息，请参阅[从错误对象中显示信息](../Error%20Handling%20Programming%20Guide/Using%20and%20Creating%20Error%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbwfvbuqmrqgqwueqkkineuoskb)。

为了创建你自己的 `NSError` 对象，你需要定义自己的错误域，其形式应该是：

```
com.companyName.appOrFrameworkName.ErrorDomain
```

你还需要为你的错误域中可能发生的每一个错误选取一个唯一的错误代码，以及一段合适的描述，这段描述会被存储在该错误的用户信息字典中，就像这样：

```objc
    NSString *domain = @"com.MyCompany.MyApplication.ErrorDomain";
    NSString *desc = NSLocalizedString(@"Unable to…", @"");
    NSDictionary *userInfo = @{ NSLocalizedDescriptionKey : desc };

    NSError *error = [NSError errorWithDomain:domain
                                         code:-101
                                     userInfo:userInfo];
```

这个示例使用 `NSLocalizedString` 函数，从一个 `Localizable.strings` 文件中查找错误描述的本地化版本，具体描述见 Localizing String Resources。

如果你需要像前面所描述的那样通过引用传回一个错误，你的方法签名应该包含一个指向 `NSError` 对象指针的指针参数。你还应该使用返回值来表明成功还是失败，就像这样：

```objc
- (BOOL)doSomethingThatMayGenerateAnError:(NSError **)errorPtr;
```

如果发生错误，在你尝试解引用错误指针以设置错误、然后返回 `NO` 表示失败之前，应该先检查错误参数所提供的指针是否为非 `NULL`，就像这样：

```objc
- (BOOL)doSomethingThatMayGenerateAnError:(NSError **)errorPtr {
    ...
    // 发生了错误
    if (errorPtr) {
        *errorPtr = [NSError errorWithDomain:...
                                        code:...
                                    userInfo:...];
    }
    return NO;
}
```


Objective-C 支持异常的方式与其他编程语言大致相同，语法与 Java 或 C++ 相似。和 `NSError` 一样，Cocoa 和 Cocoa Touch 中的异常也是对象，由 `NSException` 类的实例来表示

如果你需要编写可能引发异常的代码，可以把这段代码包裹在一个 try-catch 块中：

```objc
    @try {
        // 做一些可能抛出异常的事情
    }
    @catch (NSException *exception) {
        // 处理这个异常
    }
    @finally {
        // 可选的清理代码块
        // 无论是否发生异常都会执行
    }
```

如果 `@try` 块内的代码抛出了异常，它会被 `@catch` 块捕获，这样你就可以处理它。举例来说，如果你正在使用某个使用异常进行错误处理的底层 C++ 库，你可能会捕获它抛出的异常，并生成合适的 `NSError` 对象展示给用户。

如果一个异常被抛出但没有被捕获，默认的未捕获异常处理程序会向控制台记录一条消息，并终止应用。

你不应该用 try-catch 块来代替 Objective-C 方法中标准的编程检查。以 `NSArray` 为例，在尝试访问某个索引处的对象之前，你应该始终先检查数组的 `count`，以确定条目的数量。`objectAtIndex:` 方法在你发出越界请求时会抛出异常，这样你就能在开发周期的早期发现代码中的 bug——在发布给用户的应用中，你应该避免抛出异常。

有关 Objective-C 应用中异常的更多信息，请参阅 _[异常编程主题](../Exception%20Programming%20Topics/Introduction%20to%20Exception%20Programming%20Topics%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgayte2i)_。

[下一页](Conventions.md)[上一页](Working%20with%20Blocks.md)

