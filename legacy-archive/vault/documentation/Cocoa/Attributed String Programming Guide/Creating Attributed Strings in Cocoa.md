---
title: 属性字符串编程指南
apple_id: 10000036i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AttributedStrings/Tasks/CreatingAttributedStrings.html
archived_at: '2026-07-15T05:25:52.344427Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [属性字符串编程指南](Introduction%20to%20Attributed%20String%20Programming%20Guide.md)


[下一页](Accessing%20Attributes.md)[上一页](Attributed%20Strings.md)

# 在 Cocoa 中创建属性字符串

你可以通过多种不同方式创建 `NSAttributedString` 对象：

- 你可以使用 `initWithString:`、`initWithString:attributes:` 或 `initWithAttributedString:` 方法创建新字符串。这些方法会用你提供的数据来初始化属性字符串，如下例所示：

```objc
NSFont *font = [NSFont fontWithName:@"Palatino-Roman" size:14.0];
NSDictionary *attrsDictionary =
        [NSDictionary dictionaryWithObject:font
                                    forKey:NSFontAttributeName];
NSAttributedString *attrString =
    [[NSAttributedString alloc] initWithString:@"strigil"
            attributes:attrsDictionary];
```

  Application Kit 框架提供的属性列表，请参阅 _NSAttributedString Application Kit Additions Reference_ 中的“Constants”一节。

  赋予属性字符串的属性值会成为该字符串的所有物，其他对象不应“绕过属性字符串”对其进行修改。这样做可能导致属性字符串内部状态变得不一致。请始终使用 `NSMutableAttributedString` 的 [setAttributes:range:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSMutableAttributedString/setAttributes:range:) 及相关方法来更改属性值。更多细节请参阅[更改属性字符串](Changing%20an%20Attributed%20String.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge3delkcijbuer2dirdq)。
- 你可以使用初始化方法 `initWithRTF:documentAttributes:`、`initWithRTFD:documentAttributes:` 和 `initWithRTFDFileWrapper:documentAttributes:`，从富文本格式（RTF）或带附件的富文本（RTFD）数据创建属性字符串，如下例所示：

```objc
NSData *rtfData = ...;  // assume rtfData is an NSData object containing valid RTF data
NSDictionary *docAttributes;
NSSize paperSize;

NSAttributedString *attrString;

if ((attrString = [[NSAttributedString alloc]
        initWithRTF: rtfData documentAttributes: &docAttributes])) {

    NSValue *value = [docAttrs objectForKey:@"PaperSize"];
    paperSize = [value sizeValue];
    // implementation continues...
```
- 你可以使用初始化方法 `initWithHTML:documentAttributes:` 和 `initWithHTML:baseURL:documentAttributes:`，从 HTML 数据创建属性字符串。这些方法会将 HTML 中定义的文本属性作为字符串的属性返回，并通过引用返回的 `NSDictionary` 对象来返回 HTML 中定义的文档级属性（例如纸张大小和页边距），具体说明见[RTF 文件与属性字符串](RTF%20Files%20and%20Attributed%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge3dilkcijbuessjijbq)。这些方法会尽可能将 HTML 转换为 Cocoa 文本系统的结构，但 Application Kit 并不提供对任意 HTML 的完整、真实渲染。

  __多核方面的考虑：__ 自 OS X v10.4 起，`NSAttributedString` 在导入（而非导出）所有 HTML 文档时都会使用 WebKit。由于 WebKit 的文档加载并非线程安全，因此在后台线程上使用一直是不安全的。对于链接到 OS X v10.5 及更高版本的应用程序，如果 `NSAttributedString` 在主线程以外的线程上导入 HTML 文档，WebKit 的使用会通过 [performSelectorOnMainThread:withObject:waitUntilDone:](https://developer.apple.com/documentation/objectivec/nsobject/1414900-performselector) 转移到主线程执行。这样可以使该操作变得线程安全，但要求主线程正在以某种常见模式运行事件循环（run loop）。可以通过将标准用户默认值 `NSRunWebKitOnAppKitThread` 设为 `YES`（无论链接版本如何都获得新行为）或 `NO`（无论链接版本如何都获得旧行为）来覆盖这一默认行为。

[下一页](Accessing%20Attributes.md)[上一页](Attributed%20Strings.md)

