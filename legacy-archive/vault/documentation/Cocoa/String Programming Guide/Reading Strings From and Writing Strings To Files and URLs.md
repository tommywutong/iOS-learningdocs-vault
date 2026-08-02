---
title: 字符串编程指南
apple_id: 10000035i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/readingFiles.html
archived_at: '2026-07-15T07:19:33.702883Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [字符串编程指南](Introduction%20to%20String%20Programming%20Guide.md)


[下一页](Searching%2C%20Comparing%2C%20and%20Sorting%20Strings.md)[上一页](String%20Format%20Specifiers.md)

# 从文件和 URL 读取字符串以及将字符串写入文件和 URL

只要你知道资源使用的是什么编码，用 `NSString` 读取文件或 URL 就很简单——如果不知道编码，读取资源就要棘手得多。而当你写入文件或 URL 时，必须指定所使用的编码。（在可能的情况下应优先使用 URL，因为这样效率更高。）

`NSString` 提供了多种从文件和 URL 读取数据的方法。一般来说，如果你知道数据的编码，读取起来会容易得多。如果你拿到的是纯文本却不了解它的编码，那么处境已经相当不利了。你应当尽一切可能避免让自己陷入这种境地——凡是需要使用纯文本文件的场合，都应当指定编码（最好是 UTF-8 或带 BOM 的 UTF-16）。

要从已知编码的文件或 URL 读取内容，可以使用 [stringWithContentsOfFile:encoding:error:](https://developer.apple.com/documentation/foundation/nsstring/1497327-stringwithcontentsoffile) 或 [stringWithContentsOfURL:encoding:error:](https://developer.apple.com/documentation/foundation/nsstring/1497360-stringwithcontentsofurl)，也可以使用对应的 `init...` 方法，如下面的例子所示。

```objc
NSURL *URL = ...;
NSError *error;
NSString *stringFromFileAtURL = [[NSString alloc]
                                      initWithContentsOfURL:URL
                                      encoding:NSUTF8StringEncoding
                                      error:&error];
if (stringFromFileAtURL == nil) {
    // 发生了错误
    NSLog(@"Error reading file at %@\n%@",
              URL, [error localizedFailureReason]);
    // 实现代码继续 ...
```

你也可以用一个 data 对象来[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)字符串，如下面的例子所示。同样，你必须指定正确的编码。

```objc
NSURL *URL = ...;
NSData *data = [NSData dataWithContentsOfURL:URL];

// 假设 data 采用 UTF8 编码。
NSString *string = [NSString stringWithUTF8String:[data bytes]];

// 如果 data 采用其他编码，例如 ISO-8859-1
NSString *string = [[NSString alloc]
            initWithData:data encoding: NSISOLatin1StringEncoding];
```


如果你手上的文本编码未知，最好确保有某种机制可以纠正难免会出现的错误。例如，Apple 的 Mail 和 Safari 应用提供了编码菜单，而 TextEdit 允许用户用显式指定的编码重新打开文件。

如果你不得不去猜测编码（请注意，在缺乏明确信息的情况下，这的确只是一种_猜测_）：

1. 先尝试 [stringWithContentsOfFile:usedEncoding:error:](https://developer.apple.com/documentation/foundation/nsstring/1497254-stringwithcontentsoffile) 或 [initWithContentsOfFile:usedEncoding:error:](https://developer.apple.com/documentation/foundation/nsstring/1418227-initwithcontentsoffile)（或者它们基于 URL 的等价方法）。

   这些方法会尝试判定资源的编码，成功时通过引用返回所使用的编码。
2. 如果第 (1) 步失败，尝试以 UTF-8 作为编码来读取该资源。
3. 如果第 (2) 步失败，尝试某种合适的传统编码。

   这里的“合适”多少取决于具体情况；它可能是默认的 C 字符串编码，可能是 ISO 或 Windows Latin 1，也可能是别的编码，这取决于你的数据来自何处。
4. 最后，你还可以尝试 Application Kit 中 `NSAttributedString` 的加载方法（例如 [initWithURL:options:documentAttributes:error:](https://developer.apple.com/documentation/foundation/nsattributedstring/1530490-initwithurl)）。

   这些方法会尝试加载纯文本文件，并返回所使用的编码。它们可以用于处理或多或少任意的文本文档；如果你的应用在文本处理方面没有特别的专长，这些方法值得考虑。而对于 Foundation 层的工具，或者内容并非自然语言文本的文档，它们可能就不太合适了。

与从文件或 URL 读取数据相比，写入要直接得多——`NSString` 提供了两个便捷方法：[writeToFile:atomically:encoding:error:](https://developer.apple.com/documentation/foundation/nsstring/1407654-write) 和 [writeToURL:atomically:encoding:error:](https://developer.apple.com/documentation/foundation/nsstring/1417341-write)。你必须指定应当使用的编码，并选择是否原子性地写入该资源。如果你选择不原子性地写入，字符串会直接写到你指定的路径。如果你选择原子性地写入，字符串会先写入一个辅助文件，然后该辅助文件再被重命名为目标路径。这个选项可以保证：即使系统在写入过程中崩溃，该文件（如果它存在的话）也不会损坏。如果你写入的是 URL，而目标类型不支持原子性访问，那么原子性选项会被忽略。

```objc
NSURL *URL = ...;
NSString *string = ...;
NSError *error;
BOOL ok = [string writeToURL:URL atomically:YES
                  encoding:NSUnicodeStringEncoding error:&error];
if (!ok) {
    // 发生了错误
    NSLog(@"Error writing file at %@\n%@",
              path, [error localizedFailureReason]);
    // 实现代码继续 ...
```


下表汇总了在文件和 URL 之间读写字符串对象最常用的几种方式：

| 来源 | 创建方法 | 提取方法 |
| --- | --- | --- |
| URL 内容 | [stringWithContentsOfURL:encoding:error:](https://developer.apple.com/documentation/foundation/nsstring/1497360-stringwithcontentsofurl)  [stringWithContentsOfURL:usedEncoding:error:](https://developer.apple.com/documentation/foundation/nsstring/1497408-stringwithcontentsofurl) | [writeToURL:atomically:encoding:error:](https://developer.apple.com/documentation/foundation/nsstring/1417341-write) |
| 文件内容 | [stringWithContentsOfFile:encoding:error:](https://developer.apple.com/documentation/foundation/nsstring/1497327-stringwithcontentsoffile)  [stringWithContentsOfFile:usedEncoding:error:](https://developer.apple.com/documentation/foundation/nsstring/1497254-stringwithcontentsoffile) | [writeToFile:atomically:encoding:error:](https://developer.apple.com/documentation/foundation/nsstring/1407654-write) |

[下一页](Searching%2C%20Comparing%2C%20and%20Sorting%20Strings.md)[上一页](String%20Format%20Specifiers.md)

