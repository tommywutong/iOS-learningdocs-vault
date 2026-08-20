---
title: 事件驱动 XML 编程指南
apple_id: 10000186i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/XMLParsing/Articles/UsingParser.html
archived_at: '2026-07-15T07:21:27.492455Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [事件驱动 XML 编程指南](Introduction%20to%20Event-Driven%20XML%20Programming%20Guide%20for%20Cocoa.md)


[下一篇](Handling%20XML%20Elements%20and%20Attributes.md) [上一篇](Parser%20Capabilities%20and%20Architecture.md)

# XML 解析基础

使用 NSXMLParser 解析 XML 文档的基本步骤很直观。你需要完成以下常规步骤：

1. 找到 XML。

   清单 1 展示了让用户通过文件系统浏览器（NSOpenPanel）选择 XML 文件的代码。

   __清单 1__　打开 XML 文件

```objc
- (void)openXMLFile {

    NSArray *fileTypes = [NSArray arrayWithObject:@"xml"];
    NSOpenPanel *oPanel = [NSOpenPanel openPanel];
    NSString *startingDir = [[NSUserDefaults standardUserDefaults] objectForKey:@"StartingDirectory"];
    if (!startingDir)
        startingDir = NSHomeDirectory();
    [oPanel setAllowsMultipleSelection:NO];
    [oPanel beginSheetForDirectory:startingDir file:nil types:fileTypes
      modalForWindow:[self window] modalDelegate:self
      didEndSelector:@selector(openPanelDidEnd:returnCode:contextInfo:)
      contextInfo:nil];
}

- (void)openPanelDidEnd:(NSOpenPanel *)sheet returnCode:(int)returnCode contextInfo:(void *)contextInfo {
    NSString *pathToFile = nil;
    if (returnCode == NSOKButton) {
        pathToFile = [[[sheet filenames] objectAtIndex:0] copy];
    }
    if (pathToFile) {
        NSString *startingDir = [pathToFile stringByDeletingLastPathComponent];
        [[NSUserDefaults standardUserDefaults] setObject:startingDir forKey:@"StartingDirectory"];
        [self parseXMLFile:pathToFile];
    }
}
```

   尽管 XML 通常来自文件，但其来源也可能不是文件。你可能从另一个对象接收到属性列表对象（如 NSDictionary）形式的 XML，或通过网络接收到字节流形式的 XML。在这些情况下，必须先将 XML 转换为 NSData 对象，然后再初始化 NSXMLParser 实例（见下一步）。
2. 创建并初始化 NSXMLParser 实例，确保为其设置委托。

   清单 2 展示了一种实现方式。

   __清单 2__　创建并初始化 NSXMLParser 实例

```objc
- (void)parseXMLFile:(NSString *)pathToFile {
    BOOL success;
    NSURL *xmlURL = [NSURL fileURLWithPath:pathToFile];
    if (addressParser) // addressParser 是 NSXMLParser 实例变量
        [addressParser release];
    addressParser = [[NSXMLParser alloc] initWithContentsOfURL:xmlURL];
    [addressParser setDelegate:self];
    [addressParser setShouldResolveExternalEntities:YES];
    success = [addressParser parse]; // 未使用返回值
                // 如果解析失败，则通知委托发生了错误
}
```

   在此方法中，客户端对象将 XML 文件的路径转换为 NSURL 对象，然后使用该对象通过 `initWithContentsOfURL:` 初始化 NSXMLParser 实例。它还将自己设为委托，并告知解析器需要解析外部实体（例如外部 DTD 声明）。NSXMLParser 的其他方法可用于设置各种命名空间相关选项。最后，客户端向 NSXMLParser 实例发送 `parse` 消息，使其开始解析 XML。

   如果 XML 不是文件形式，应将其转换为 NSData 对象，然后使用 `initWithData:` 初始化器：

```objc
addressParser = [[NSXMLParser alloc] initWithData:xmlData];
```
3. 实现你需要的委托方法。

   NSXMLParser 对象解析 XML 时，会针对遇到的每个 XML 结构向委托发送消息（但前提是委托实现了相应方法）。这些方法的实现因结构类型而异，例如 DTD 声明、命名空间前缀、元素等。元素是最常处理的 XML 结构类型；有关详情，请参阅[处理 XML 元素和属性](Handling%20XML%20Elements%20and%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dklkcineuurshjjeq)。

   所有解析操作都从委托接收 `parserDidStartDocument:` 开始，以委托接收 `parserDidEndDocument:` 结束（当然，前提是委托实现了这些方法）。前一个方法提供了分配和设置解析操作所需资源的时机；后一个方法则适合释放这些资源并妥善处理所有结果。
4. 处理所有解析错误。

   如果解析器遇到错误，就会停止解析并调用委托方法 `parser:parseErrorOccurred:`。请实现此方法来解释错误并通知用户。（所有解析器错误均不可恢复。）有关更多信息，请参阅[处理解析错误](Handling%20Parsing%20Errors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dmlkdjjbesrciizba)。

解析 XML 时，需要格外关注内存管理。处理 XML 通常需要创建大量对象；这些对象在不再有用后，不应继续堆积在内存中。处理这些生成对象的一种方法，是让委托在每个已实现委托方法的开头创建局部自动释放池，并在方法返回前释放该自动释放池。`NSXMLParser` 会管理其创建并发送给委托的各个对象的内存。

[下一篇](Handling%20XML%20Elements%20and%20Attributes.md) [上一篇](Parser%20Capabilities%20and%20Architecture.md)
