---
title: 事件驱动 XML 编程指南
apple_id: 10000186i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/XMLParsing/Articles/HandlingElements.html
archived_at: '2026-07-15T07:21:25.536451Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [事件驱动 XML 编程指南](Introduction%20to%20Event-Driven%20XML%20Programming%20Guide%20for%20Cocoa.md)


[下一篇](Handling%20Parsing%20Errors.md) [上一篇](XML%20Parsing%20Basics.md)

# 处理 XML 元素和属性

通常，解析 XML 文档时，大部分处理都围绕元素以及与元素相关的内容（例如属性和文本内容）展开。元素承载了 XML 文档中的大部分信息。当 NSXMLParser 对象遍历 XML 文档中的某个元素时，至少会按以下顺序向其委托发送三条不同消息：

- `parser:didStartElement:namespaceURI:qualifiedName:attributes:`
- `parser:foundCharacters:`
- `parser:didEndElement:namespaceURI:qualifiedName:`

对于同一个元素，解析器可能会多次发送 `parser:foundCharacters:` 消息；不过，如果字符只包含空白字符（空格、换行符、制表符及类似字符），解析器则会发送 `parser:foundIgnorableWhitespace:`。

解析 XML 元素时，可以采用一种高级技巧：在多个委托之间切换处理职责，让每个委托都知道如何处理某类元素。有关更多信息，请参阅[使用多个委托](Using%20Multiple%20Delegates.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dolkciffeurcfinba)。

在 Cocoa 这样的面向对象环境中，处理元素的一种常见策略是将元素（至少是嵌套层级较高的元素）映射为对象。根元素和其他顶层元素通常对应于 Cocoa 中由 NSDictionary 和 NSArray 对象表示的集合。其他元素则可能很容易映射为应用程序的一个或多个自定义模型对象。

不过，并非所有元素都最适合表示为对象。某些较低层级的元素，尤其是“叶”元素，更适合视为其父元素的属性（如果该父元素映射为对象）。当然，通常还会将任何元素的实际属性设为对应对象的属性（即实例变量）。

尽管有上述建议，但并不存在现成的映射公式；事实上，应用程序也可能无须执行任何元素到对象的映射即可实现目标。做出这些设计决策既需要认真考虑，也需要熟悉 XML 的结构。

以下讨论所引用的示例代码会处理一个包含个人地址信息的 XML 文件，并将这些信息转换为可添加到指定用户地址数据库的“通讯录”对象（ABPerson 和 ABMultipleValue）。XML 的一部分如下所示：

__清单 1__　示例 XML 的一部分

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE addresses SYSTEM "addresses.dtd">
<addresses owner="swilson">
    <person>
        <lastName>Doe</lastName>
        <firstName>John</firstName>
        <phone location="mobile">(201) 345-6789</phone>
        <email>jdoe@foo.com</email>
        <address>
            <street>100 Main Street</street>
            <city>Somewhere</city>
            <state>New Jersey</state>
            <zip>07670</zip>
        </address>
    </person>

    <!-- 此处还有更多 person 元素 -->

</addresses>
```

下面看看如何处理前三个元素。解析器首次遇到这些元素时，会调用委托的 `parser:didStartElement:namespaceURI:qualifiedName:attributes:` 方法。对于前两个元素，委托会创建对应的对象。对于第三个元素（`lastName`），委托会设置第二个对象的相应属性。清单 2 展示了委托对前三个元素开始标签的实现。

__清单 2__　实现 `parser:didStartElement:namespaceURI:qualifiedName:attributes:`

```objc
- (void)parser:(NSXMLParser *)parser didStartElement:(NSString *)elementName namespaceURI:(NSString *)namespaceURI qualifiedName:(NSString *)qName attributes:(NSDictionary *)attributeDict {

    if ( [elementName isEqualToString:@"addresses"]) {
        // addresses 是 NSMutableArray 实例变量
       if (!addresses)
             addresses = [[NSMutableArray alloc] init];
        return;
    }

    if ( [elementName isEqualToString:@"person"] ) {
        // currentPerson 是 ABPerson 实例变量
        currentPerson = [[ABPerson alloc] init];
        return;
    }

    if ( [elementName isEqualToString:@"lastName"] ) {
        [self setCurrentProperty:kABLastNameProperty];
        return;
    }
    // ……其余元素的处理代码……
}
```

委托会识别传入的元素（_elementName_），然后据此进行处理：

- 如果是 `addresses` 元素（根元素），则创建一个可变数组来保存 ABPerson 对象。该可变数组作为实例变量保存。
- 如果是 `person` 元素，则创建一个 ABPerson 对象。该对象保存在名为 `currentPerson` 的实例变量中。
- 如果是 `lastName` 元素，则设置一个保存当前“通讯录”属性的实例变量；该值是 Address Book 框架中声明的枚举常量。

这里的重要做法，是提供一种在解析器遍历当前元素的整个过程中跟踪该元素的方式（本例中使用实例变量）。这之所以重要，原因之一在于接下来很可能调用的委托方法 `parser:foundCharacters:` 的语义。对于同一个元素，此方法可能会调用多次。在该方法中，委托应将传入的字符追加到目前已为该元素累积的字符之后。NSMutableString 的 `appendString:` 方法很适合此用途，如清单 3 所示。

__清单 3__　实现 `parser:foundCharacters:`

```objc
- (void)parser:(NSXMLParser *)parser foundCharacters:(NSString *)string {
    if (!currentStringValue) {
        // currentStringValue 是 NSMutableString 实例变量
        currentStringValue = [[NSMutableString alloc] initWithCapacity:50];
    }
    [currentStringValue appendString:string];
}
```

代码同样使用实例变量（`currentStringValue`）来跟踪和收集当前元素的内容。如果解析器在元素内容中遇到空白字符，就会发送 `parser:foundIgnorableWhitespace:` 消息，让委托有机会保留制表符或换行符等空白字符。

最后，当解析器遇到元素的结束标签时，会调用委托方法 `parser:didEndElement:namespaceURI:qualifiedName:`。清单 4 展示了示例代码中委托采用的处理方式。

__清单 4__　实现 `parser:didEndElement:namespaceURI:qualifiedName:`

```objc
- (void)parser:(NSXMLParser *)parser didEndElement:(NSString *)elementName namespaceURI:(NSString *)namespaceURI qualifiedName:(NSString *)qName {
    // 忽略根元素和空元素
    if (( [elementName isEqualToString:@"addresses"]) ||
        ( [elementName isEqualToString:@"address"] )) return;

    if ( [elementName isEqualToString:@"person"] ) {
        // addresses 和 currentPerson 是实例变量
        [addresses addObject:currentPerson];
        [currentPerson release];
        return;
    }
    NSString *prop = [self currentProperty];

    // ……在此处理 ABMultiValue 对象……

    if (( [prop isEqualToString:kABLastNameProperty] ) ||
        ( [prop isEqualToString:kABFirstNameProperty] )) {
        [currentPerson setValue:(id)currentStringValue forProperty:prop];
    }
    // currentStringValue 是实例变量
    [currentStringValue release];
    currentStringValue = nil;
}
```

如果委托判定结束标签属于 `person` 元素，就会将 ABPerson 对象添加到 `addresses` 数组，并释放该 ABPerson 对象。例如，如果结束标签属于 `lastName` 元素，委托会使用 ABRecord 的 `setValue:forProperty:` 方法设置 ABPerson 对象中的相应属性（ABRecord 是 ABPerson 的超类）。最后，释放保存该元素累积内容的实例变量（`currentStringValue`）。

[清单 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dkljrgaydgnjsgmwueq2jinceqskk) 的示例 XML 中所示 `addresses` 元素包含一个属性：

```xml
<addresses owner="swilson">
```

在这个假设示例中，该属性允许解析 XML 的应用程序将创建的“通讯录”信息存储在多用户系统的特定用户目录中。

NSXMLParser 对象通过 `parser:didStartElement:namespaceURI:qualifiedName:attributes:` 的最后一个参数，以字典形式将元素属性提供给委托。清单 5 展示了示例中的委托如何处理 `owner` 属性。

__清单 5__　处理元素的属性

```objc
- (void)parser:(NSXMLParser *)parser didStartElement:(NSString *)elementName namespaceURI:(NSString *)namespaceURI qualifiedName:(NSString *)qName attributes:(NSDictionary *)attributeDict {

    if ( [elementName isEqualToString:@"addresses"]) {
        // addresses 是 NSMutableArray 实例变量
        if (!addresses)
            addresses = [[NSMutableArray alloc] init];
        NSString *thisOwner = [attributeDict objectForKey:@"owner"];
        if (thisOwner)
            [self setOwner:thisOwner forAddresses:addresses];
        return;
    // ……后续代码……
}}
```

委托使用属性名（`owner`）作为键，从 `attributeDict` 字典中提取所有者的用户名。然后，它调用一个私有方法，将该所有者与导入的“通讯录”数据关联起来。

[下一篇](Handling%20Parsing%20Errors.md) [上一篇](XML%20Parsing%20Basics.md)
