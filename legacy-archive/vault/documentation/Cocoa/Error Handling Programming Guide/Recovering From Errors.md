---
title: 错误处理编程指南
apple_id: TP40001806
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-01-07'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ErrorHandlingCocoa/RecoverFromErrors/RecoverFromErrors.html
archived_at: '2026-07-15T07:15:26.577798Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [错误处理编程指南](Introduction%20to%20Error%20Handling%20Programming%20Guide%20For%20Cocoa.md)


[下一页](Document%20Revision%20History.md) [上一页](Handling%20Received%20Errors.md)

# 从错误中恢复

如[恢复尝试器](Error%20Objects%2C%20Domains%2C%20and%20Codes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbwfvbuqmrqgiwueqsdjjeeuskh)所述，[NSError](https://developer.apple.com/documentation/foundation/nserror) 对象可以指定一个恢复尝试器，即在用户请求时尝试从错误中恢复的对象。错误对象会在其用户信息[字典](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10)中保存恢复尝试器的引用，因此即使错误对象在应用程序内部传递，恢复尝试器也会始终伴随它。用户信息字典还必须包含恢复选项，即一个用作按钮标题的[本地化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Internationalization.html#//apple_ref/doc/uid/TP40008195-CH23)字符串数组，其中至少有一个选项用于请求恢复。当警告中呈现错误且用户选择恢复选项时，系统便向恢复尝试器发送消息，请求其执行工作。

理想情况下，恢复尝试器应是独立对象，了解错误发生的条件以及绕过这些条件的最佳方式。应用程序甚至可以设置一个专门负责从各种错误中恢复的对象。恢复尝试器必须实现 `NSErrorRecoveryAttempting` 非正式[协议](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45)中的至少一个方法：`attemptRecoveryFromError:optionIndex:delegate:didRecoverSelector:contextInfo:` 或 `attemptRecoveryFromError:optionIndex:`。对于以文档模态形式呈现的错误警告，应实现前一个方法；对于应用程序模态警告，则实现后一个方法。

还必须准备错误对象，使错误恢复能够进行。为此，请向错误对象的用户信息字典添加以下三项：

- 以 `NSRecoveryAttempterErrorKey` 为键保存恢复尝试器对象
- 以 `NSLocalizedRecoveryOptionsErrorKey` 为键保存恢复选项（本地化字符串数组）
- 以 `NSLocalizedRecoverySuggestionErrorKey` 为键保存同样经过本地化的恢复建议字符串。尽管严格来说此属性并非必需，但按照人机界面指南，提供恢复选项的错误警告应显示该字符串。如果字符串提及具体按钮标题，应使用与恢复选项数组中相同的标题。

  有关 OS X 错误警告的准则，请参见《OS X 人机界面指南》（“UI 元素指南：窗口”中的对话框章节）。

清单 5-1 演示了一个涉及 [NSXMLDocument](https://developer.apple.com/documentation/foundation/xmldocument) 类的案例。在此示例中，[NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) 对象尝试使用 `NSXMLDocument` 的 `initWithContentsOfURL:options:error:` 方法创建表示 XML 文档的内部树。如果尝试失败，通常是因为源 XML 格式错误，例如元素缺少结束标签，或属性值未加引号。如果先“整理”源 XML 并修复结构问题，就可能成功创建 XML 树。

在清单 5-1 的示例中，如果调用 `initWithContentsOfURL:options:error:` 通过引用返回错误对象，文档对象就会自定义该错误对象，在其用户信息字典中加入恢复尝试器对象、本地化恢复选项和本地化恢复建议等内容。随后，它向 `self` 发送 `presentError:modalForWindow:delegate:didPresentSelector:contextInfo:`。

__清单 5-1__　为错误恢复做准备

```objc
- (BOOL)readFromURL:(NSURL *)furl ofType:(NSString *)type error:(NSError **)anError {
    NSError *err;

    // xmlDoc 是一个 NSXMLDocument 实例变量。
    if (xmlDoc != nil) {
        xmlDoc = nil;
    }

    xmlDoc = [[NSXMLDocument alloc] initWithContentsOfURL:furl
            options:NSXMLNodeOptionsNone error:&err];

    if (xmlDoc == nil && err) {
        NSString *newDesc = [[err localizedDescription] stringByAppendingString:
            ([err localizedFailureReason] ? [err localizedFailureReason] : @"")];

        NSDictionary *newDict = @{ NSLocalizedDescriptionKey : newDesc,
            NSURLErrorKey : furl,
            NSRecoveryAttempterErrorKey : self,
            NSLocalizedRecoverySuggestionErrorKey :
                NSLocalizedString(@"Would you like to tidy the XML and try again?", @""),
            NSLocalizedRecoveryOptionsErrorKey :
                @[NSLocalizedString(@"Try Again", @""), NSLocalizedString(@"Cancel", @"")] };

        NSError *newError = [[NSError alloc] initWithDomain:[err domain]
            code:[err code] userInfo:newDict];
        [self presentError:newError modalForWindow:[self windowForSheet]
            delegate:self
            didPresentSelector:@selector(didPresentErrorWithRecovery:contextInfo:)
            contextInfo:nil];
    }
// ...
```

请注意，文档对象还把标识 XML 来源的 URL 添加到了用户信息字典。恢复尝试器尝试创建表示 XML 的树时会使用此 URL。

错误对象沿错误响应者链向上传递，最终由 `NSApp` 显示。用户点击错误警告中的任意按钮时，`NSApp` 会检查错误对象是否同时具有恢复尝试器和恢复选项。如果两个条件都满足，它会调用恢复尝试器所实现、与警告模式（文档模态或应用程序模态）相对应的方法。

清单 5-2 展示了 XML 文档的恢复尝试器如何实现 `attemptRecoveryFromError:optionIndex:delegate:didRecoverSelector:contextInfo:` 方法。

__清单 5-2__　从错误中恢复并通知模态委托

```objc
- (void)attemptRecoveryFromError:(NSError *)error
                     optionIndex:(unsigned int)recoveryOptionIndex
                        delegate:(id)delegate
              didRecoverSelector:(SEL)didRecoverSelector
                     contextInfo:(void *)contextInfo {

    BOOL success = NO;
    NSError *err;
    NSInvocation *invoke = [NSInvocation invocationWithMethodSignature:
                               [delegate methodSignatureForSelector:didRecoverSelector]];
    [invoke setSelector:didRecoverSelector];

    if (recoveryOptionIndex == 0) { // 用户请求恢复。
        xmlDoc = [[NSXMLDocument alloc] initWithContentsOfURL:[[error userInfo]
                objectForKey:NSURLErrorKey] options:NSXMLDocumentTidyXML error:&err];
        if (xmlDoc != nil) {
            success = YES;
        }
    }
    [invoke setArgument:(void *)&success atIndex:2];
    if (err)
        [invoke setArgument:&err atIndex:3];
    [invoke invokeWithTarget:delegate];
}
```

上述示例的关键在于恢复尝试器如何判断用户是否点击了“重试”按钮：它会检查 `recoveryOptionIndex` 的值。如果用户确实点击了该按钮，恢复尝试器会再次调用 `initWithContentsOfURL:options:error:`，但这次使用 `NSXMLDocumentTidyXML` 选项。然后，它创建并调用 [NSInvocation](https://developer.apple.com/documentation/foundation/nsinvocation) 对象，从而向错误警告的模态[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)发送所需消息。调用对象包含委托[选择器](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48)所需的两个参数：一个表示恢复尝试是否成功的布尔值，以及一个“上下文信息”参数；在本例中，后者包含恢复尝试返回的错误对象。

如清单 5-3 所示，模态委托收到恢复尝试器的消息后，可以作出相应处理。

__清单 5-3__　模态委托响应恢复尝试器

```objc
- (void)didPresentErrorWithRecovery:(BOOL)didRecover
            contextInfo:(void *)contextInfo {

    NSError *theError = (NSError *)contextInfo;
    if (didRecover) {
        [tableView reloadData];
    } else if (theError && [theError isKindOfClass:[NSError class]]) {
        [NSAlert alertWithError:theError];
    }
}
```

[下一页](Document%20Revision%20History.md) [上一页](Handling%20Received%20Errors.md)
