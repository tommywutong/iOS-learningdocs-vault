---
title: 错误处理编程指南
apple_id: TP40001806
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-01-07'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ErrorHandlingCocoa/CreateCustomizeNSError/CreateCustomizeNSError.html
archived_at: '2026-07-15T07:15:23.604752Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [错误处理编程指南](Introduction%20to%20Error%20Handling%20Programming%20Guide%20For%20Cocoa.md)


[下一页](Error%20Responders%20and%20Error%20Recovery.md) [上一页](Error%20Objects%2C%20Domains%2C%20and%20Codes.md)

# 使用和创建错误对象

以下各节介绍如何处理[框架](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56)方法返回的 `NSError` 对象、如何使用错误对象显示错误消息、如何创建错误对象，以及如何实现通过引用返回错误对象的方法。

[Cocoa 和 Cocoa Touch](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Cocoa.html#//apple_ref/doc/uid/TP40008195-CH9) 类的许多方法都把指向 [NSError](https://developer.apple.com/documentation/foundation/nserror) 对象的直接或间接引用作为最后一个参数。在某些 Foundation 和 UIKit 方法中，`NSError` 对象还会作为[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)方法的参数。以下声明来自 UIKit 框架的 [UIWebViewDelegate](https://developer.apple.com/documentation/uikit/uiwebviewdelegate) 协议；委托可实现此类方法以确定某项操作是否失败：

```objc
- (void)webView:(UIWebView *)webView didFailLoadWithError:(NSError *)error;
```

调用的某些 Cocoa 框架方法包含对 `NSError` 对象的间接引用；这些方法通常执行创建文档、写入文件或加载 URL 等操作。例如，以下方法声明来自 [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) 类的头文件：

```objc
- (BOOL)writeToURL:(NSURL *)absoluteURL
    ofType:(NSString *)typeName
    error:(NSError **)outError;
```

如果此类方法在实现中遇到错误，会直接返回 `NO` 表示失败，并通过最后一个参数间接返回（如果客户端代码请求）用于描述错误的 `NSError` 对象。

如果要评估错误，请在调用 `writeToURL:ofType:error:` 等方法之前声明一个 `NSError` 对象变量，并在调用方法时传入指向该变量的指针。（如果不关心错误，只需传入 `NULL`。）如果方法直接返回 `nil` 或 `NO`，可检查 `NSError` 对象以确定错误原因，也可以直接显示错误警告。清单 2-1 演示了这种方式。

__清单 2-1__　处理 AppKit 方法返回的 `NSError` 对象

```objc
NSError *theError;
BOOL success = [myDoc writeToURL:[self docURL] ofType:@"html" error:&theError];

if (success == NO) {
    // 可以先尝试确定错误原因并进行恢复。
    NSAlert *theAlert = [NSAlert alertWithError:theError];
    [theAlert runModal]; // 忽略返回值。
}
```

清单 2-1 中的代码使用返回的 `NSError` 立即向用户显示错误警告。（与 [NSAlert](https://developer.apple.com/documentation/appkit/nsalert) 对应的 UIKit 类 [UIAlertView](https://developer.apple.com/documentation/uikit/uialertview) 没有与 [alertWithError:](https://developer.apple.com/documentation/appkit/nsalert/1531823-init) 等效的方法。）Cocoa 域中的错误对象始终经过[本地化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Internationalization.html#//apple_ref/doc/uid/TP40008195-CH23)，可直接呈现给用户，因此通常无需进一步评估即可显示。

除了根据 `NSError` 对象显示错误消息，还可以检查对象以确定是否能采取其他措施。例如，可以稍微改变方式重新执行操作，从而绕过错误；但如果这样做，应先请求用户允许执行修改后的操作。

评估 `NSError` 对象时，始终应以对象的域和错误代码作为检查依据，而不要依据描述错误或恢复方法的字符串。字符串通常经过本地化，因此很可能发生变化。除少数例外（如 [NSURLErrorDomain](https://developer.apple.com/documentation/foundation/nsurlerrordomain) 域）外，Cocoa 框架方法返回的预定义错误始终位于 `NSCocoaErrorDomain` 域；但由于确实存在例外，可能需要检查顶层错误是否属于该域。Cocoa 方法返回的错误对象通常可以包含底层错误对象，表示 BSD 层（`NSPOSIXErrorDomain`）等较低层子系统返回的错误。

要成功评估错误，当然必须预先考虑方法调用可能返回哪些错误，同时还应确保代码能妥善处理未来可能返回的新错误。

如果正在开发 Mac 应用，收到 `NSError` 对象后还可以采取许多其他措施：

- 如果知道如何从错误中恢复，但需要用户批准，可以创建错误对象的新版本，并为其添加恢复尝试器（参见[从错误中恢复](Recovering%20From%20Errors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbwfvbuqmrqgywueq2jircuor2g)）。
- 沿错误响应者链向上传递错误对象，让应用程序中的其他对象可以补充信息或尝试从错误中恢复。

  在此之前，可以根据当前编程上下文补充错误信息，再创建包含这些增强信息的新错误对象。
- 如果以返回的 `NSError` 对象为基础，通过添加恢复尝试器或补充信息创建新错误对象，可以：

  - 立即显示消息。
  - 将错误传递给下一个错误响应者。

  有关自定义沿错误响应者链向上传递的错误，参见[处理接收到的错误](Handling%20Received%20Errors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbwfvbuqmrqguwueqkkiveecssd)。

有多种方式可以显示 `NSError` 对象中的信息。可以从错误对象提取本地化描述（或失败原因）、恢复建议和恢复选项，并用它们初始化 [NSAlert](https://developer.apple.com/documentation/appkit/nsalert)、[UIAlertView](https://developer.apple.com/documentation/uikit/uialertview) 或 [UIActionSheet](https://developer.apple.com/documentation/uikit/uiactionsheet) 对象（或 OS X 模态文档表单）的标题及消息文本。这种通用方式可以高度控制错误警告的内容和呈现形式。

例如，清单 2-2 的代码使用从传入 `NSError` 对象取得的本地化描述和失败原因，组合 `UIAlertView` 对象的消息文本。

__清单 2-2__　显示主要由错误对象属性组成的警告

```objc
- (void)webView:(UIWebView *)webView didFailLoadWithError:(NSError *)error {

    NSString *titleString = @"Error Loading Page";
    NSString *messageString = [error localizedDescription];
    NSString *moreString = [error localizedFailureReason] ?
                        [error localizedFailureReason] :
                        NSLocalizedString(@"Try typing the URL again.", nil);
    messageString = [NSString stringWithFormat:@"%@. %@", messageString, moreString];

    UIAlertView *alertView = [[UIAlertView alloc] initWithTitle:titleString
        message:messageString delegate:self
        cancelButtonTitle:@"Cancel" otherButtonTitles:nil];
    [alertView show];
}
```

不过，并非必须使用框架提供的[本地化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Internationalization.html#//apple_ref/doc/uid/TP40008195-CH23)错误字符串。例如，如果认为这些字符串的描述不够充分，或希望补充特定于上下文的信息，可以通过域和代码识别错误，然后替换为自己的字符串值。以上一示例所用的委托方法为例，在 [webView:didFailLoadWithError:](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/1617970-webview) 中传给委托的错误对象几乎总是属于 [NSURLErrorDomain](https://developer.apple.com/documentation/foundation/nsurlerrordomain) 域。可以确定该域中的哪个代码与错误相关，再用自己的字符串替换错误对象中包含的字符串。（`NSURLErrorDomain` 及其代码在 `NSURLError.h` 中声明。）清单 2-3 给出了示例。

__清单 2-3__　根据错误域和代码指定自定义消息字符串

```objc
- (void)webView:(UIWebView *)webView didFailLoadWithError:(NSError *)error {

    NSString *errorMsg;

    if ([[error domain] isEqualToString:NSURLErrorDomain]) {
        switch ([error code]) {
            case NSURLErrorCannotFindHost:
                errorMsg = NSLocalizedString(@"Cannot find specified host. Retype URL.", nil);
                break;
            case NSURLErrorCannotConnectToHost:
                errorMsg = NSLocalizedString(@"Cannot connect to specified host. Server may be down.", nil);
                break;
            case NSURLErrorNotConnectedToInternet:
                errorMsg = NSLocalizedString(@"Cannot connect to the internet. Service may not be available.", nil);
                break;
            default:
                errorMsg = [error localizedDescription];
                break;
        }
    } else {
        errorMsg = [error localizedDescription];
    }

    UIAlertView *av = [[UIAlertView alloc] initWithTitle:
        NSLocalizedString(@"Error Loading Page", nil)
        message:errorMsg delegate:self
        cancelButtonTitle:@"Cancel" otherButtonTitles:nil];
    [av show];
}
```


Application Kit 提供了几个显示错误警告的便捷方法。`presentError:` 和 [presentError:modalForWindow:delegate:didPresentSelector:contextInfo:](https://developer.apple.com/documentation/appkit/nsresponder/1534705-presenterror) 可发起最终由全局应用程序对象 `NSApp` 显示的错误警告；前一个方法请求应用程序模态警告，后一个方法请求文档模态警告。必须将这两种错误呈现消息之一发送给错误响应者链中的对象（参见[错误响应者链](Error%20Responders%20and%20Error%20Recovery.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbwfvbuqmrqgmwugsscjbaueqkb)）：视图对象、窗口对象、[NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) 对象、[NSWindowController](https://developer.apple.com/documentation/appkit/nswindowcontroller) 对象、[NSDocumentController](https://developer.apple.com/documentation/appkit/nsdocumentcontroller) 对象或 `NSApp`。（如果向视图发送消息，理想情况下该视图对象应与产生错误的条件存在某种关联。）清单 2-4 演示了如何调用文档模态 `presentError:modalForWindow:delegate:didPresentSelector:contextInfo:` 方法。

__清单 2-4__　显示文档模态错误警告

```objc
NSError *theError;
NSData *theData = [doc dataOfType:@"xml" error:&theError];
if (!theData && theError)
    [anyView presentError:theError
            modalForWindow:[doc windowForSheet]
            delegate:self
            didPresentSelector:
                @selector(didPresentErrorWithRecovery:contextInfo:)
            contextInfo:nil];
```

用户关闭警告后，`NSApp` 会调用模态委托实现的方法（由 `didPresentSelector:` 关键字指定）。如清单 2-5 所示，模态委托会在该方法中检查恢复尝试器对象（如果存在）是否成功从错误中恢复，并作出相应处理。

__清单 2-5__　模态委托处理用户响应

```objc
- (void)didPresentErrorWithRecovery:(BOOL)recover contextInfo:(void *)info {
    if (recover == NO) { // 恢复未成功，或未尝试恢复。
        // 进行相应处理。
    }
}
```

有关恢复尝试器对象的更多信息，参见[从错误中恢复](Recovering%20From%20Errors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbwfvbuqmrqgywueq2jircuor2g)。

有时可能不希望沿错误响应者链向上传递错误对象并由 `NSApp` 显示，而是希望立即向用户显示错误警告，又不想自行构建警告。`NSAlert` 类为此提供了 `alertWithError:` 方法。

__清单 2-6__　直接显示错误警告对话框

```objc
NSAlert *theAlert = [NSAlert alertWithError:theError];
NSInteger button = [theAlert runModal];
if (button != NSAlertFirstButtonReturn) {
    // 处理
}
```


可以声明并实现自己的方法，间接返回 `NSError` 对象。适合采用 `NSError` 参数的方法包括打开和读取文件、加载资源、解析格式化文本等。通常，这些方法不应通过是否存在 `NSError` 对象来表示错误，而应通过返回 `NO` 或 `nil` 表示发生了错误，再返回 `NSError` 对象对错误进行描述。

如果要在此类方法的实现中通过引用返回 `NSError` 对象，就必须创建该对象。可以分配错误对象，再使用 `NSError` 的 `initWithDomain:code:userInfo:` 方法初始化；也可以使用类工厂方法 `errorWithDomain:code:userInfo:`。正如两个方法的关键字所示，必须向初始化器提供域（字符串常量）、错误代码（有符号整数）以及包含描述和辅助信息的“用户信息”字典。（这些数据项的完整说明参见[错误对象、域和代码](Error%20Objects%2C%20Domains%2C%20and%20Codes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbwfvbuqmrqgiwugssci5ausqsk)。）应确保用户信息字典中的所有字符串都经过本地化。

清单 2-7 是一个方法示例；为便于说明，该方法调用 POSIX 层的 `open` 函数打开文件。如果此函数返回错误，该方法会创建 `NSPOSIXErrorDomain` 域的 `NSError` 对象，并将其作为返回给调用方的自定义错误域错误的底层错误。

__清单 2-7__　实现返回 `NSError` 对象的方法

```objc
- (NSString *)fooFromPath:(NSString *)path error:(NSError **)anError {

    const char *fileRep = [path fileSystemRepresentation];
    int fd = open(fileRep, O_RDWR|O_NONBLOCK, 0);

    if (fd == -1) {

        if (anError != NULL) {
            NSString *description;
            NSDictionary *uDict;
            int errCode;

            if (errno == ENOENT) {
                description = NSLocalizedString(@"No file or directory at requested location", @"");
                errCode = MyCustomNoFileError;
            } else if (errno == EIO) {
                // 继续处理每个可能的 POSIX 错误……
            }

            // 创建底层错误。
            NSError *underlyingError = [[NSError alloc] initWithDomain:NSPOSIXErrorDomain
                code:errno userInfo:nil];
            // 创建并返回自定义域错误。
            NSDictionary *errorDictionary = @{ NSLocalizedDescriptionKey : description,
                NSUnderlyingErrorKey : underlyingError, NSFilePathErrorKey : path };

            *anError = [[NSError alloc] initWithDomain:MyCustomErrorDomain
                    code:errCode userInfo:errorDictionary];
        }
        return nil;
    }
    // ...
```

在此示例中，返回错误对象的用户信息字典包含导致错误的路径。

如清单 2-7 的示例所示，可以将源自底层子系统的错误作为返回给调用方的错误对象的基础。代码所处理的已抛出异常也能以相同方式使用。[NSException](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/cl/NSException) 对象在属性方面与 `NSError` 对象兼容，包含名称、原因和用户信息字典。可以轻松地将异常对象中的信息转移到错误对象。

必须牢记 Cocoa 和 Cocoa Touch 中错误对象与[异常](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ExceptionHandling.html#//apple_ref/doc/uid/TP40008195-CH18)对象之间的区别，并了解何时在代码中使用哪一种。它们用途不同，不应混淆。

异常（由 [NSException](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/cl/NSException) 对象表示）用于数组索引越界或方法参数无效等编程错误。用户级错误（由 `NSError` 对象表示）用于文件找不到或无法读取某种编码的字符串等运行时错误。引发异常的条件源于编程错误，应在产品发布前处理。运行时错误则始终可能发生，应通过 `NSError` 对象向用户传达必要的详细信息。

虽然理想情况下应在部署前处理所有异常，但已发布的应用程序仍可能因“内存不足”或“启动宗卷不可用”等真正的异常情况而发生异常。最好让应用程序的最高层级——全局应用程序对象本身——处理这些情况。

[下一页](Error%20Responders%20and%20Error%20Recovery.md) [上一页](Error%20Objects%2C%20Domains%2C%20and%20Codes.md)
