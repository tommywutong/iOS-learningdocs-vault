---
title: DTD 节点种类常量
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dtd_node_kind_constants
source_url: 'https://developer.apple.com/documentation/foundation/dtd_node_kind_constants'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dtd_node_kind_constants.json'
content_hash: 'sha256:7f6352c4f5b5e68f'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [归档与序列化](archives-and-serialization.md) · [XML 处理与建模](xml-processing-and-modeling.md) · [XMLDTDNode](xmldtdnode.md)

# DTD 节点种类常量

<sub>API 集合</sub>

这些常量指定 `NSXMLDTDNode` 对象所表示的 DTD 声明的种类或子种类。使用 doc:nsxmldtdnode/1806486-setdtdkind 方法设置 DTD 节点种类。

## 主题

### 常量

- [NSXMLEntityGeneralKind](xmldtdnode/dtdkind-swift.enum/general.md) — 标识一般实体声明。
- [NSXMLEntityParsedKind](xmldtdnode/dtdkind-swift.enum/parsed.md) — 标识已解析实体声明。
- [NSXMLEntityUnparsedKind](xmldtdnode/dtdkind-swift.enum/unparsed.md) — 标识未解析实体声明。
- [NSXMLEntityParameterKind](xmldtdnode/dtdkind-swift.enum/parameter.md) — 标识参数实体声明。
- [NSXMLEntityPredefined](xmldtdnode/dtdkind-swift.enum/predefined.md) — 标识预定义实体声明。
- [NSXMLAttributeCDATAKind](xmldtdnode/dtdkind-swift.enum/cdataattribute.md) — 标识值类型为 `CDATA`（字符数据）的特性（attribute）列表声明。
- [NSXMLAttributeIDKind](xmldtdnode/dtdkind-swift.enum/idattribute.md) — 标识值类型为 `ID`（每个文稿中唯一的元素名称）的特性列表声明。
- [NSXMLAttributeIDRefKind](xmldtdnode/dtdkind-swift.enum/idrefattribute.md) — 标识值类型为 `IDREF`（引用元素的 `ID` 类型）的特性列表声明。
- [NSXMLAttributeIDRefsKind](xmldtdnode/dtdkind-swift.enum/idrefsattribute.md) — 标识值类型为 `IDREFS`（引用多个元素的 `ID` 类型）的特性列表声明。
- [NSXMLAttributeEntityKind](xmldtdnode/dtdkind-swift.enum/entityattribute.md) — 标识值类型为 `ENTITY`（引用文稿中声明的未解析实体）的特性列表声明。
- [NSXMLAttributeEntitiesKind](xmldtdnode/dtdkind-swift.enum/entitiesattribute.md) — 标识值类型为 `ENTITIES`（引用文稿中其他位置声明的多个未解析实体）的特性列表声明。
- [NSXMLAttributeNMTokenKind](xmldtdnode/dtdkind-swift.enum/nmtokenattribute.md) — 标识值类型为 `NMTOKEN`（名称标记）的特性列表声明。
- [NSXMLAttributeNMTokensKind](xmldtdnode/dtdkind-swift.enum/nmtokensattribute.md) — 标识值类型为 `NMTOKENS`（多个名称标记）的特性列表声明。
- [NSXMLAttributeEnumerationKind](xmldtdnode/dtdkind-swift.enum/enumerationattribute.md) — 标识具有枚举值类型（所有可能值的列表）的特性列表声明。
- [NSXMLAttributeNotationKind](xmldtdnode/dtdkind-swift.enum/notationattribute.md) — 标识值类型为 `NOTATION`（已声明符号的名称）的特性列表声明。
- [NSXMLElementDeclarationUndefinedKind](xmldtdnode/dtdkind-swift.enum/undefineddeclaration.md) — 标识未定义的元素声明。
- [NSXMLElementDeclarationEmptyKind](xmldtdnode/dtdkind-swift.enum/emptydeclaration.md) — 标识空元素的声明（`EMPTY`）。
- [NSXMLElementDeclarationAnyKind](xmldtdnode/dtdkind-swift.enum/anydeclaration.md) — 标识 `ANY` 元素声明。
- [NSXMLElementDeclarationMixedKind](xmldtdnode/dtdkind-swift.enum/mixeddeclaration.md) — 标识具有混合内容（`(#PCDATA | child)`）的元素声明。
- [NSXMLElementDeclarationElementKind](xmldtdnode/dtdkind-swift.enum/elementdeclaration.md) — 标识包含子元素的元素声明。

## 另请参阅

### 常量

- [DTDKind](xmldtdnode/dtdkind-swift.enum.md) — 为指定 `NSXMLDTDNode` 对象所表示 DTD 声明种类和子种类的常量定义的类型。使用 doc:nsxmldtdnode/1806486-setdtdkind 方法设置 DTD 节点种类。
