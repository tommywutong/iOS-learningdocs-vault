---
title: 事件驱动 XML 编程指南
apple_id: 10000186i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/XMLParsing/Articles/HandlingParseErrors.html
archived_at: '2026-07-15T07:21:25.975153Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [事件驱动 XML 编程指南](Introduction%20to%20Event-Driven%20XML%20Programming%20Guide%20for%20Cocoa.md)


[下一篇](Using%20Multiple%20Delegates.md) [上一篇](Handling%20XML%20Elements%20and%20Attributes.md)

# 处理解析错误

当解析器在 XML 文档中遇到语法错误或任何其他导致文档无法保持格式良好的问题时，它会停止解析并向委托发送消息。如果委托实现了 `parser:parseErrorOccurred:` 方法，就会收到这条消息。该方法的实现应显示一条消息，告知用户问题所在。解析错误是致命的（即不可恢复），因此实际上能做的只有通知用户。用户可根据这些信息修复 XML，使文档能够成功解析。

清单 1 展示了 `parser:parseErrorOccurred:` 的一种实现方式。

__清单 1__　处理解析错误

```objc
- (void)parser:(NSXMLParser *)parser parseErrorOccurred:(NSError *)parseError {
    NSWindow *modWin = [self windowForSheet];
    if (!modWin) modWin = [NSApp mainWindow];
    NSAlert *parserAlert = [[NSAlert alloc] init];
    [parserAlert setMessageText:@"Parsing Error!"];
    [parserAlert setInformativeText:[NSString stringWithFormat:@"Error %i,
        Description: %@, Line: %i, Column: %i", [parseError code],
        [[parser parserError] localizedDescription], [parser lineNumber],
        [parser columnNumber]]];
    [parserAlert addButtonWithTitle:@"OK"];
    [parserAlert beginSheetModalForWindow:modWin modalDelegate:self
        didEndSelector:@selector(alertDidEnd:returnCode:contextInfo:)
        contextInfo:nil];
    [parserAlert release];
}

- (void)alertDidEnd:(NSAlert *)alert returnCode:(int)returnCode contextInfo:(void *)contextInfo { }
```

本例中的关键代码行是构建 NSAlert 对象说明文本的语句。该文本包含错误代码（一个 `NSXMLParserError` 枚举常量）、错误的本地化描述，以及用于确定错误在 XML 文档中位置的行号和列号（嵌套层级）。在本例中，委托从两个不同来源获取这些信息：方法第一个参数提供的解析器对象本身，以及第二个参数提供的 NSError 对象。委托也可以从解析器对象取得 NSError 对象，再从中取得本地化描述。

不过，NSError 的默认本地化描述较为简略。你可能希望提供自己的本地化描述，而不是依赖从 NSError 对象取得的描述。有时，解析错误可能需要结合具体应用程序来解释。为此实现函数或方法时，可以根据定义错误的 `NSXMLParserError` 常量，确定应在 `NSLocalizedString` 宏中使用哪个自定义键。（当然，你还必须创建 `strings` 文件，并完成应用程序国际化所需的其他工作。）

[下一篇](Using%20Multiple%20Delegates.md) [上一篇](Handling%20XML%20Elements%20and%20Attributes.md)
