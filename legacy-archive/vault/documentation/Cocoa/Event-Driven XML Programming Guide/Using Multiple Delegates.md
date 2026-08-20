---
title: 事件驱动 XML 编程指南
apple_id: 10000186i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/XMLParsing/Articles/UsingMultipleDelegates.html
archived_at: '2026-07-15T07:21:26.979741Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [事件驱动 XML 编程指南](Introduction%20to%20Event-Driven%20XML%20Programming%20Guide%20for%20Cocoa.md)


[下一篇](Constructing%20XML%20Tree%20Structures.md) [上一篇](Handling%20Parsing%20Errors.md)

# 使用多个委托

对于某些 XML 文档，尤其是庞大而复杂的文档，只为 NSXMLParser 对象设置一个委托可能不是最佳方案。处理所有不同解析事件的代码很容易变得过于复杂且难以管理。让多个委托分担解析事件的处理工作，是降低管理难度的一种方法。

以一个在遇到元素时据此构建 DOM 风格树的应用程序为例。从根元素开始，一个元素创建子元素，并将其设为委托，从而把控制权交给它。该子元素再创建自己的子元素（依此类推），每次都相应地重新设置委托。如果某个元素没有子元素，或者它是混合元素，则会为自身累积文本内容。最后，当解析器遇到某个元素的结束标签时，该元素会将委托设回其父元素。清单 1 展示了完成这一处理过程的相关代码。

__清单 1__　为下一个元素重新设置委托

```objc
- (void)parser:(NSXMLParser *)parser
        didStartElement:(NSString *)elementName
        namespaceURI:(NSString *)namespaceURI
        qualifiedName:(NSString *)qualifiedName
        attributes:(NSDictionary *)attributeDict {
    // Element 是用于表示元素节点对象的自定义类
    // 创建元素时会将子元素设为委托（见下文）
    [self addChild:[Element elementWithName:elementName
        attributes:attributeDict parent:self children:nil parser:parser]];
}

- (void)parser:(NSXMLParser *)parser foundCharacters:(NSString *)string {
    [self appendString:string];
}

- (void)parser:(NSXMLParser *)parser didEndElement:(NSString *)elementName namespaceURI:(NSString *)namespaceURI qualifiedName:(NSString *)qName {
    Element *parent = [self parent];
    [parser setDelegate:parent]; // 将委托重设为父元素
}

+ (id)elementWithName:(NSString *)elementName attributes:(NSDictionary *)attributes parent:(Element *)parent children:(NSArray *)children parser:(NSXMLParser *)parser {
    return [[[[self class] alloc] initWithName:elementName
        attributes:attributes parent:parent children:children
        parser:parser] autorelease];
}

- (id)initWithName:(NSString *)elementName attributes:(NSDictionary *)attributes parent:(id)parent children:(NSArray *)children parser:(NSXMLParser *)parser {
    self = [super init];
    if (self) {
         [self setName:elementName];
         if (attributes) {
               [self addAttributes:attributes];
         }
         [self setParent:parent];
         if (children) {
              [self addChildren:children];
         }
         [parser setDelegate:self]; // 将子元素设为委托
    }
    return self;
}
```

另一种管理多个委托的方法，是在 NSDictionary 等集合中维护多个委托对象，每个对象各司其职。这些对象能够识别给定上下文中的子元素和父元素，因此在完成当前元素的处理工作后，可以使用相应的字典键为下一个元素设置委托。

[下一篇](Constructing%20XML%20Tree%20Structures.md) [上一篇](Handling%20Parsing%20Errors.md)
