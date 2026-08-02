---
title: 属性列表编程指南
apple_id: 10000048i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/UnderstandXMLPlist/UnderstandXMLPlist.html
archived_at: '2026-07-15T07:18:03.525361Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [属性列表编程指南](Introduction%20to%20Property%20Lists.md)


[下一页](Serializing%20a%20Property%20List.md)[上一页](Creating%20Property%20Lists%20Programmatically.md)

# 理解 XML 属性列表

在 OS X 和 iOS 上，存储属性列表的首选方式是使用一种称为 _XML 属性列表_（XML property list）或 _XML plist_ 的 XML 文件。这类文件的优点是人类可读，并且采用基于标准的 XML 格式。[NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray) 和 [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) 类都提供了把自身保存为 XML plist 的方法（例如 [descriptionWithLocale:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/descriptionWithLocale:) 和 [writeToFile:atomically:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/writeToFile:atomically:)），同时也提供了把 XML 属性列表还原成内存中对象的方法。CFPropertyList 则提供了在属性列表与其 XML 表示之间相互转换的函数。

Core Foundation 只支持用 XML 作为属性列表在磁盘上的静态表示介质。Cocoa 则允许属性列表以 XML 属性列表、二进制形式和“旧式”属性列表三种方式存储在磁盘上。旧式属性列表只能读取，不能写入；更多信息请参阅[旧式 ASCII 属性列表](Old-Style%20ASCII%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgaytelkcijbuerccjjcq)。

一般来说，你很少需要自己创建或编辑 XML 属性列表；如果确实需要，请使用 Xcode 内置的属性列表编辑器或 Property List Editor 应用程序（它是工具包的一部分）。除非你非常熟悉 XML 语法和属性列表的格式，否则不要在文本编辑器中编辑 XML 数据。此外，XML 属性列表中的元素在未来的版本中可能会发生变化，这一点也要记在心上。

即使你不编辑 XML 属性列表，了解它们的结构对设计和调试也很有帮助。和所有 XML 文件一样，XML plist 以标准的头信息开头，并包含一个根对象，该对象被 `<plist>` 文档类型标签包裹。`<plist>` 对象内部恰好包含一个对象，用[表 2-1](About%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2jninedglktk4yq) 中列出的某个 XML 元素表示。

对象图是通过嵌套表 2-1 中列出的 XML 元素来构建的。在编码字典时，用 `<key>` 元素表示字典的键，用其他某个属性列表标签表示该键对应的值。下面是一个由属性列表生成的 XML 数据示例：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist SYSTEM "file://localhost/System/Library/DTDs/PropertyList.dtd">
<plist version="1.0">
<dict>
    <key>Author</key>
    <string>William Shakespeare</string>
    <key>Lines</key>
    <array>
        <string>It is a tale told by an idiot,</string>
        <string>Full of sound and fury, signifying nothing.</string>
    </array>
    <key>Birthdate</key>
    <integer>1564</integer>
</dict>
</plist>
```

注意，`<data>` 和 `</data>` 标签之间的数据字节采用 base-64 编码。

[下一页](Serializing%20a%20Property%20List.md)[上一页](Creating%20Property%20Lists%20Programmatically.md)

