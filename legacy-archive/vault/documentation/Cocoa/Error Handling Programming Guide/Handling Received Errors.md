---
title: 错误处理编程指南
apple_id: TP40001806
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-01-07'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ErrorHandlingCocoa/HandleReceivedError/HandleReceivedError.html
archived_at: '2026-07-15T07:15:26.552217Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [错误处理编程指南](Introduction%20to%20Error%20Handling%20Programming%20Guide%20For%20Cocoa.md)


[下一页](Recovering%20From%20Errors.md) [上一页](Error%20Responders%20and%20Error%20Recovery.md)

# 处理接收到的错误

向某些符合条件的对象发送 `presentError:` 或 `presentError:modalForWindow:delegate:didPresentSelector:contextInfo:` 消息时，该消息会沿应用程序中称为错误响应者链的一系列对象向上传递（参见[错误响应者链](Error%20Responders%20and%20Error%20Recovery.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbwfvbuqmrqgmwugsscjbaueqkb)）。链中大多数对象的默认实现会先向 `self` 发送 `willPresentError:`，再向下一个对象发送 `presentError:`。`willPresentError:` 消息使自定义子类实例有机会检查链中传递的错误对象，并视需要进行自定义。当错误对象到达链末端时，全局应用程序对象 NSApp 会向用户显示错误警告；不过在显示之前，NSApp 会调用 `application:willPresentError:`，让其委托获得同样的处理机会。

以下各节讨论实现 `willPresentError:` 和 `application:willPresentError:` 方法的策略。

如果你有 [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument)、[NSDocumentController](https://developer.apple.com/documentation/appkit/nsdocumentcontroller)、[NSWindowController](https://developer.apple.com/documentation/appkit/nswindowcontroller)、[NSWindow](https://developer.apple.com/documentation/appkit/nswindow)、[NSPanel](https://developer.apple.com/documentation/appkit/nspanel) 或任意视图类的子类，就可以重写 `willPresentError:` 方法来自定义错误的呈现方式。当子类实例比应用程序中的其他对象更了解特定错误的上下文时，通常适合这样做。一般而言，`willPresentError:` 的实现会检查传入的 [NSError](https://developer.apple.com/documentation/foundation/nserror) 对象；例如，当本地化描述不够充分，或子类知道如何从错误中恢复时，它会创建并返回一个新的 `NSError` 对象。大多数情况下，自定义错误对象会保留传入对象中的部分信息。

`willPresentError:` 方法的实现应始终以错误域和错误代码为依据，决定是否返回自定义错误对象。不要依据用户信息字典中的字符串进行判断，因为这些字符串可能经过本地化，并且在不同调用之间可能有所不同。如果实现决定不自定义错误，不要直接返回传入对象，而应向 `super` 发送 `willPresentError:` 消息。清单 4-1 演示了其中一些策略。

__清单 4-1__　处理沿错误响应者链向上传递的错误

```objc
- (NSError *)willPresentError:(NSError *)error {

    if ([[error domain] isEqualToString:NSCocoaErrorDomain]) {
        switch([error code]) {
            case NSFileLockingError:
            case NSFileReadNoSuchFileError:
            { // 自定义子类的私有方法。
                return [self customizeError:error];
            }
            default:
                return [super willPresentError:error];
        }
    }
    return [super willPresentError:error];
}
```

要自定义用于呈现的 `NSError` 对象，并不一定要创建子类。应用程序[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)可以改为实现 [application:willPresentError:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428721-application) 方法。上文针对 `willPresentError:` 给出的说明和准则同样适用于 `application:willPresentError:`，区别在于：如果决定不自定义错误，可以直接返回原始错误对象。

在[清单 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbwfvbuqmrqguwueqkkinduir2g)的 `willPresentError:` 示例中，代码调用一个私有方法来自定义错误对象，这样做是为了让实现结构更清晰。如果将自定义代码直接内联，其形式可能类似清单 4-2 中的 `willPresentError:` 实现。该代码检查传入对象是否包含失败原因；如果有，就附加该失败原因，创建更贴合应用程序的错误描述，然后以这个不同的描述创建新的 [NSError](https://developer.apple.com/documentation/foundation/nserror) 对象。

__清单 4-2__　自定义 NSError 对象

```objc
- (NSError *)willPresentError:(NSError *)error {

    if ([[error domain] isEqualToString:NSCocoaErrorDomain]) {
        switch([error code]) {
            case NSFileLockingError:
            case NSFileReadNoSuchFileError:
            {
                NSString *locFailure = [error localizedFailureReason];
                if (locFailure) {
                    NSMutableDictionary *newUserInfo = [NSMutableDictionary
                        dictionaryWithCapacity:[[[error userInfo] allKeys] count]];
                    [newUserInfo setDictionary:[error userInfo]];
                    NSString *errorDesc = [NSString stringWithFormat:
                        NSLocalizedString(@"MyGreatApp cannot open the file. %@", @""),
                        locFailure];
                    [newUserInfo setObject:errorDesc
                        forKey:NSLocalizedDescriptionKey];
                    NSError *newError = [NSError errorWithDomain:[error domain]
                        code:[error code] userInfo:newUserInfo];
                    return newError;
                }
                else {
                    return [super willPresentError:error];
                }
            }
            default:
                return [super willPresentError:error];
        }
    }
    return [super willPresentError:error];
}
```

此示例实质上通过克隆原始错误对象来创建新对象。新错误对象包含更具体的错误描述，并在其中附加了失败原因。

如[沿错误响应者链向上传递错误](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbwfvbuqmrqguwueqkki5eucssk)所述，实现 `willPresentError:` 与委托方法 `application:willPresentError:` 并无区别；唯一例外是，在后一个方法中，如果不自定义错误，可以直接返回传入的错误对象。

[下一页](Recovering%20From%20Errors.md) [上一页](Error%20Responders%20and%20Error%20Recovery.md)
