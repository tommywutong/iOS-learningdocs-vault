---
title: 'list(memberStyle:type:width:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatstyle/list(memberstyle:type:width:)'
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/list(memberstyle:type:width:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/list%28memberstyle%3Atype%3Awidth%3A%29.json'
content_hash: 'sha256:79177d65192dd367'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# list(memberStyle:type:width:)

<sub>Type Method</sub>

Returns a format style to format a list of items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func list<MemberStyle, Base>(memberStyle: MemberStyle, type: ListFormatStyle<MemberStyle, Base>.ListType, width: ListFormatStyle<MemberStyle, Base>.Width = .standard) -> Self where Self == ListFormatStyle<MemberStyle, Base>, MemberStyle : FormatStyle, Base : Sequence, MemberStyle.FormatInput == Base.Element, MemberStyle.FormatOutput == String
```

## Parameters

- `memberStyle` — The format style to apply to each item in the list.

- `type` — The list type to apply, such as cumulative ([ListFormatStyle.ListType.and](../listformatstyle/listtype-swift.enum/and.md)) or alternative ([ListFormatStyle.ListType.or](../listformatstyle/listtype-swift.enum/or.md)) elements.

- `width` — The width to use when formatting, such as [ListFormatStyle.Width.standard](../listformatstyle/width-swift.enum/standard.md) or [ListFormatStyle.Width.narrow](../listformatstyle/width-swift.enum/narrow.md).

## Return Value

A list format style that formats an array as a textual list of items.

## Discussion

Use the dot-notation form of this type method when the call point allows the use of [ListFormatStyle](../listformatstyle.md). You typically do this when calling the [formatted(_:)](<../../swift/sequence/formatted(__).md>) method of [Sequence](../../swift/sequence.md).

The following example creates an array of integers, then uses [formatted(_:)](<../../swift/sequence/formatted(__).md>) and the list format style provided by this method to format the items. By using a currency [IntegerFormatStyle](../integerformatstyle.md), the list format style expresses each member as US dollars. The example also modifies the list format style to use the `en_US` locale, so the resulting string uses US English conventions for commas and conjunctions (“and”).

```swift
let items: [Int] = [100, 1000, 10000, 100000, 1000000]
let formatted = items.formatted(
    .list(memberStyle: .currency(code: "USD"),
          type: .and)
    .locale(Locale(identifier: "en_US"))) // "$100.00, $1,000.00, $10,000.00, $100,000.00, and $1,000,000.00"
```

## See Also

### Applying list styles

- [list(type:width:)](<list(type_width_).md>) — Returns a format style to format a list of strings.
