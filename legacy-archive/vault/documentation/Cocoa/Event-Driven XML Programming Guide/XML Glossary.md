---
title: 事件驱动 XML 编程指南
apple_id: 10000186i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/XMLParsing/Articles/XMLGlossary.html
archived_at: '2026-07-15T07:21:28.539417Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [事件驱动 XML 编程指南](Introduction%20to%20Event-Driven%20XML%20Programming%20Guide%20for%20Cocoa.md)


[下一篇](Document%20Revision%20History.md) [上一篇](Validation%20Tips%20and%20Techniques.md)

# XML 术语表

本术语表定义了 XML、DTD 以及相关规范和技术中的一些专用术语，主要介绍 NSXMLParser、NSXMLNode、NSXMLDocument、NSXMLElement、NSXMLDTD 和 NSXMLDTDNode 类所声明的方法及常量名称中涉及的术语。

__原子值（atomic value）__：具有 XML Schema 标准所定义简单类型的值。这些类型包括字符串、十进制数、整数、浮点数、双精度浮点数、布尔值、日期、URI、数组和二进制数据。XQuery 查询返回一个项目_序列_，其中可包含一个或多个节点或原子值。

__属性（attribute）__：以名称-值对表示的_元素_特性。属性用于编码数据，或提供与元素关联的元数据。在以下示例中，“version”是元素 `plist` 的一个属性名称，其值为 `"1.0"`：

```xml
<plist version="1.0">
```

__属性列表声明（attribute list declaration）__：在 DTD 中标识具有属性的元素、这些属性的名称、属性可取的值以及默认值。例如：

```xml
<!ATTLIST phone location (home | office | mobile) "home">
```

在此示例中，`phone` 是元素名称，`location` 是属性名称，`(home | office | mobile)` 是允许的值，`home` 是默认值。

__规范形式（canonical）__：XML 文档的一种形式，可用于与另一文档进行等价性比较。如果两个物理表示不同的文档具有相同的规范形式，则在给定应用程序上下文中会被视为逻辑等价。XML 文档的规范形式由万维网联盟在 `http://www.w3.org/TR/xml-c14n` 中定义。

__CDATA 块（CDATA block）__：解析器应不作解释、直接传递给客户端应用程序的一段文本。它以元素内容的形式出现。CDATA 块通常用于包含“禁用”字符的代码或数据，即对解析器具有特殊语法意义的字符（例如“<”和“&”）。也可以使用_实体引用_表示这些禁用字符（例如，`&lt;` 是用于指定经“转义”的 `<` 字符的内置实体引用）。

__内容模型（content model）__：_元素声明_中定义元素可包含哪些内容的部分。内容模型由子元素名称、`#PCDATA`（表示文本）、实体引用或 `EMPTY`（表示 `<true/>` 之类的空元素）组成。子元素和 `#PCDATA` 放在括号内。子元素之间的逗号表示元素必须按给定顺序出现。以竖线字符（“|”）代替逗号表示逻辑“或”关系，并且可以与 `#PCDATA` 一起使用。出现次数修饰符可以应用于单个元素或元素组：

- “+”表示元素或元素组可以重复多次，但必须至少出现一次。
- “?”表示元素或元素组可选，并且最多只能出现一次。
- “\*”表示元素或元素组可选，并且可以出现多次。
- 没有修饰符表示元素或元素组必须且只能出现一次。

内容模型示例：

```text
(#PCDATA)
(%plistObject)*
(lastName, middleInitial?, firstName, phone*)*
```

__文档顺序（document order）__：XML 标记结构在文档中出现的顺序。在 NSXML 树中，如果依次向遇到的每个节点对象发送 NSXMLNode 的 `nextNode`（或 `previousNode`）消息，就是按文档顺序向前（或向后）遍历该树。

__DOM（Document Object Model，文档对象模型）__：一种以树结构形式访问和操作 XML 文档的 API。DOM 源自万维网联盟针对通用对象模型提出的建议，该模型用于在内存中存储分层结构文档。

__DTD（Document Type Definition，文档类型定义）__：定义 XML 文档中合法元素及其他构成部分的一种方式。

__元素（element）__：用于标识所包围内容性质的标记标签。元素具有名称，并且可以包含文本数据、子元素、_处理指令_、注释和 _CDATA 块_。除没有父元素的文档根元素外，每个元素都有一个父元素。元素还可以关联_属性_和_命名空间前缀_。元素也可以为空（即没有内容），开发者可将其用作标志。

以下示例展示了一个具有属性和混合内容的元素（本例中的内容包括文本、一个子元素和一个 CDATA 块）：

```xml
<para ref_num="80458">
    The following C++ code gives an example of how
    <code>cout</code> is used:
    <![CDATA[std::cout << "Hello, World!\n";
    ]]>
</para>
```

__元素声明（element declaration）__：在 DTD 中指定元素名称以及允许作为该元素内容的项目。声明可以将子元素、文本和实体引用指定为内容。它规定子元素的顺序，以及单个元素或整个元素组是否必需、是否可以出现多次。例如：

```xml
<!ELEMENT addresses (person)*>
<!ELEMENT person (lastName, firstName, phone*, email*, address*)>
<!ELEMENT lastName (#PCDATA)>
```

另请参阅_内容模型_。

__实体声明（entity declaration）__：在 DTD 中将名称与一段由_实体引用_标识的 XML 内容关联起来。该内容可以是字面值（如由字符引用标识的值）、在 DTD 其他位置指定的变量值，或外部文件中引用的文本值或二进制值。最后一种实体称为外部实体。例如：

```xml
<!ENTITY % plistObject "(array | date | dict | real | integer | string | true | false )" >
<!ENTITY CompanyLogo SYSTEM "/Library/Images/logo.gif" NDATA GIF87A>
```

__实体引用和字符引用（entity and character reference）__：文本中对外部或内部_实体声明_的引用。它必须以“&”开头，以分号结尾。你可以引用在其他位置声明的实体。有五个预定义实体：“<”、“>”、“&”、单引号字符和双引号字符。字符引用以“&#”开头，后跟数字码点。引用示例包括 `&apos;`、`&gt;` 和 `&#231;`；前两个是内置实体引用，最后一个是字符引用。另请参阅_未解析实体_。

__模型（model）__：请参阅_内容模型_。

__命名空间（namespace）__：一种 URI（Universal Resource Identifier，统一资源标识符），用于限定元素或属性名称，以避免文档包含来自不同来源的 XML 时发生名称冲突。声明命名空间时，需要在元素开始标签中为预定义的 `xmlns` 属性追加前缀（以冒号分隔），然后将其与 URI 值关联。例如：

```xml
<h:table xmlns:h="http://www.w3.org/TR/html4/">
```

此后，只需将_命名空间前缀_（上例中的“h”）与元素配合使用（以冒号分隔），即可明确标识该元素。带有命名空间声明的元素，其所有子元素都通过该前缀与同一命名空间关联。前缀与元素名称的组合（如上例中的 `h:table`）称为_限定名称_。如果 `xmlns` 后没有前缀，则该命名空间声明定义默认命名空间；但如果其值为空字符串，则表示“无命名空间”。命名空间声明中的 URI 无须指向任何实际内容；它只是一种便于获得唯一名称的方式。

__命名空间前缀（namespace prefix）__：在命名空间声明中定义的前缀，用于标识特定元素所关联的命名空间。命名空间的限定名称（`xmlns:`_localname_）只在输出时出现。获取或设置命名空间节点值等所有其他操作都只使用本地名称。另请参阅_命名空间_。

__规范化（normalize）__：将所有相邻的子文本节点合并为单个文本节点，同时移除空文本节点。强烈建议在执行 XPath 和 XQuery 查询之前进行规范化。

__记法（notation）__：以名称标识_未解析实体_的格式，或带有特定记法属性的元素格式；它还可以标识处理指令的目标。记法声明会为记法指定名称和外部标识符，使解析器或其客户端能够找到可处理该记法所指定数据的辅助应用程序。记法会出现在属性值、属性列表声明和实体声明中。

__处理指令（processing instruction）__：向处理 XML 文档的应用程序提供信息的一种结构。例如，指令可以告知应用程序如何解释 XML 或显示结果。处理指令可以出现在元素内部，也可以出现在文档顶层。处理指令的第一个词称为目标（即名称），其余所有内容都是对象值。例如：

```xml
<?sort alpha-ascending?>
```

__限定名称（qualified name）__：元素的完整名称，由前缀、冒号和本地名称组成。另请参阅_命名空间_。

__序列（sequence）__：项目的集合，其中每个项目都可以是节点或_原子值_。XQuery 查询会返回一个序列（在 Cocoa 中为 NSArray），其中可能只包含一个项目。

__验证（validation）__：依据关联 DTD（或其他模式）中的声明所描述的逻辑结构检查 XML 文档，以确认 XML 是否与其相符的过程。验证涉及的约束包括正确的元素顺序和嵌套关系、必需属性的指定以及正确的属性类型。例如，如果某元素应有一个或多个子元素但实际没有，则包含该元素的文档无效。XML 文档必须首先_格式良好_，之后才能进行验证。

__未解析实体（unparsed entity）__：由_实体引用_指向的外部资源，其内容可以是二进制数据或文本（包括非 XML 文本）。每个未解析实体都有与之关联的_记法_。

__格式良好（well-formed）__：指 XML 文档遵守 XML 语法。如果文档中的 XML 格式不良，解析器就无法解析该文档。检查文档格式是否良好时包括以下项目：

- 元素的开始标签必须有结束标签（空元素除外）。
- 属性值必须用引号括起。
- 参数实体必须先声明后使用。
- 标记结构只能出现在允许的位置。

__XHTML__：一种规定更严格的 HTML 版本，使其成为格式良好的 XML。XHTML 是万维网联盟的正式建议。

__XPath__：一种 XML 查询语言，用于在 XML 树结构中定位节点。它允许在查询中使用位置路径、谓词和通用表达式。Cocoa 实现使用 XPath 2.0，这是万维网联盟的一项建议。NSXMLNode 类通过其 `nodesForXPath:error:` 方法支持 XPath 查询。（请注意，NSXML 类不支持命名空间轴等已弃用的 XPath 1.0 功能。）

__XQuery__：一种灵活而强大的 XML 查询语言，可使用运算符、量词、函数和 FLWOR 表达式（指关键字 `for`、`let`、`order by`、`where` 和 `return`）组合逻辑复杂的查询。NSXMLNode 类通过其 `objectsForXQuery:error:` 方法支持 XQuery 1.0 查询。

__XSLT（Extensible Stylesheet Language Transformations，可扩展样式表语言转换）__：一种 XML 应用程序，用于将 XML 文档转换为另一 XML 文档，或转换为 HTML、RTF 或纯文本文档。转换中使用的样式表包含模板规则，每条规则都由模式和模板组成。NSXMLDocument 类允许通过其 `objectByApplyingXSLT:error:` 和 `objectByApplyingXSLTAtURL:error:` 方法访问 XSLT。

[下一篇](Document%20Revision%20History.md) [上一篇](Validation%20Tips%20and%20Techniques.md)
