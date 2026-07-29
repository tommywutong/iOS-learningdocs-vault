---
title: Protobuf 几乎是一种流式格式
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2023/12/Protobuf-Is-Almost-Streamable/'
original_language: en
published: 2023-12-14
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c0627b0f880d148b'
translated: true
---

> 原文：[Protobuf Is Almost Streamable](https://belkadan.com/blog/2023/12/Protobuf-Is-Almost-Streamable/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Daylight Saving Is Temporal Time Zones](https://belkadan.com/blog/2023/12/Daylight-Saving-Is-Temporal-Time-Zones/)

[CellLVM](https://belkadan.com/blog/2023/12/CellLVM/) »

## [Protobuf 几乎是一种流式格式](#)

[Protobuf](https://protobuf.dev) 是一种由 Google 发明的二进制（非文本）编码格式。它既有良好的一面，也有不那么理想的地方。^[1](#fn:recommendation) 但让人有点沮丧的是，它*几乎*算得上是一种流式格式（streamable format）——也就是说，你可以在数据到达时立即处理，而无需等待读取完所有内容。

Protobuf 的编码方式大致是“字段编号、字段长度、字段内容”，对消息中的每个字段重复。对于整数、浮点数和布尔值，[实际编码](https://protobuf.dev/programming-guides/encoding/) 会更紧凑一些，但基本思路如此。protobuf v3（当前版本，通常写作“proto3”）中的所有字段类型都有一个默认值（对于嵌套消息，为 0、false、空或 `null`），因此如果你在流中未看到某个字段，可以假定它被设置为默认值。或者，你可以将字段标记为 `optional`，以使用 `null` 作为任何类型的默认值，或者标记为 `repeated`，将字段的每次出现收集到一个列表。所有这些模式对可流式处理（streamability）来说都有点麻烦，因为你直到流结束时才能获得某个字段的完整值，但具体取决于你的顶层记录中*实际包含*什么，这可能也还好。

然后还有[这个规则](https://protobuf.dev/programming-guides/encoding/#last-one-wins)：

> ### 最后一条获胜
>
> 通常，编码后的消息中不会出现同一个非 `repeated` 字段的多个实例。但是，解析器需要能够处理这种情况。对于数值类型和字符串，如果同一个字段出现多次，解析器接受它看到的*最后一个*值。对于嵌套消息字段，解析器会合并同一字段的多个实例，就像使用 `Message::MergeFrom` 方法一样——也就是说，后一个实例中的所有单一标量字段会替换前一个中的对应字段，单一的嵌套消息会被合并，而 `repeated` 字段会被拼接。这些规则的效果是，解析两条编码后消息的拼接结果，与你分别解析两条消息然后合并得到的对象完全一致。
>
> 这个特性偶尔很有用，因为它允许你（通过拼接）合并两条消息，即使你不知道它们的类型。

这破坏了流式处理。如果你处理了一个数值或字符串字段，你可能必须撤销并重试；如果你处理了一个嵌套消息，*你可能处理有误。* 而且无论如何，你都必须保留原始消息以执行合并，或者在你的处理函数中非常仔细地模拟它。

你可以尝试承诺你的 protobuf 绝不会这样做，但这意味着你正在使用 protobuf 规范的一个受限子集，并且你突然需要检查所有生成和修改 protobuf 的工具是否满足该要求。这些工具*可能*会满足，但并没有保证。你也可以将所有顶层字段声明为 `repeated`，然后在确实出现重复时抛出异常——这可能不是工具的最佳用途，但大多数 proto 都有超出基本类型的有效性约束。但那样你*就得跟工具较劲了*，而使用 Protobuf 的一半意义就在于能利用现有工具。

我认为这种“可拼接”的特性不值得牺牲流式处理能力。如果他们改为规定“第一个值获胜，其他值静默跳过”，那么流式处理就可以正常工作。但可惜啊。大多数需要流式处理的人都会放弃，转而发出带有前置长度以及可能一个标识来说明消息类型的独立 protobuf 消息。你知道，这听起来就像一个字段……但我又知道什么呢？

1. 如果你正在寻找一种新格式，可以考虑此后出现的一种较新的格式；如果你目前正在使用 protobuf，那很可能也没问题。 [↩︎](#fnref:recommendation)

这篇条目发布于 [2023](https://belkadan.com/blog/2023) 年 [12](https://belkadan.com/blog/2023/12) 月 14 日，归类于 [技术](https://belkadan.com/blog/technical)。标签：[编码](https://belkadan.com/blog/tags/encoding)
