---
title: 构建本地化的餐饮订购 App
framework: Foundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, watchOS 8.0+, Xcode 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/building-a-localized-food-ordering-app
source_url: 'https://developer.apple.com/documentation/foundation/building-a-localized-food-ordering-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/building-a-localized-food-ordering-app.json'
content_hash: 'sha256:85e0a54893e6f89c'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [Data Formatting](data-formatting.md)

# 构建本地化的餐饮订购 App

<sub>示例代码</sub>

使用字符串格式化、属性字符串和自动语法一致性，对 App 的文本进行格式化、设置样式和本地化，以供多种语言使用。

## 概述

> [!note] 注意
> 此示例代码项目与 WWDC21 第 [10109 场：Foundation 新特性](https://developer.apple.com/wwdc21/10109/)相关。

Caffé 示例 App 会显示一份菜单，列出用户可以从咖啡馆订购的餐点，每种餐点都提供多种份量。在展示各种餐点并帮助用户准备订单时，App 会使用多种 Foundation API 对 App 文本进行本地化和样式设置：

- 基于 `FormatStyle` 的格式化可自定货币值、日期和时间以及字符串列表的显示方式。
- 属性字符串让 App 能够通过 Markdown 轻松创建带样式的文本，并在 SwiftUI 视图中显示。App 还会使用本地化的属性字符串在运行时构建字符串，即使不同语言中的词序会发生变化。
- 当某些语言中的字符串需要在运行时调整，以匹配语法性别或数量时，自动语法一致性会处理这些本地化情形。

### 使用格式化器在运行时格式化字符串

App 启动后，用户可以从几种餐点中选择一种添加到订单。用户选择某项餐点后，新视图会显示该餐点的配料，以及各个可选份量及其对应价格。

配料列表展示了格式化项目列表的示例，它使用 Swift [Sequence](https://developer.apple.com/documentation/swift/sequence) 类型上定义的 [formatted(_:)](https://developer.apple.com/documentation/swift/sequence/3767271-formatted) 方法。该过程从 `Food` 类型定义的 `ingredients` 数组开始。在 `FoodHeaderView` 中，`ingredientText` 变量取得配料字符串，将每个字符串映射为本地化字符串，然后使用 `formatted(_:)` 方法创建一个逗号分隔的列表。通过将 [ListFormatStyle](https://developer.apple.com/documentation/foundation/listformatstyle) 列表类型 [.and](https://developer.apple.com/documentation/foundation/listformatstyle/listtype/and) 添加为格式样式参数，格式化器会在列表最后一项前放置 “and”（或其本地化等效词）。

```swift
private var ingredientText: String {
    food.ingredients.map(\.localizedDescription).formatted(.list(type: .and))
}
```

在英语中，配料文本为 “Our pizza is made from: prosciutto, cheese, flour, and tomatoes.”。在西班牙语中，该列表为 “Nuestro pizza está hecho de: prosciutto, queso, harina y tomates.”。

App 还会使用字符串格式化器显示每项餐点的价格，如下所示：

```swift
func localizedPrice(_ size: FoodSize) -> String {
    price[size]!.formatted(.currency(code: "USD"))
}
```

与前面的配料列表一样，[formatted(_:)](https://developer.apple.com/documentation/swift/binaryinteger/3765927-formatted) 方法直接应用于它所格式化的类型。在此示例中，被格式化的类型是 [Decimal](https://developer.apple.com/documentation/foundation/decimal)；此类型符合 Swift 的 [BinaryInteger](https://developer.apple.com/documentation/swift/binaryinteger)，后者定义了 `formatted(_:)` 方法。[FormatStyle](https://developer.apple.com/documentation/foundation/formatstyle) 参数指明应使用美元将价格格式化为货币。

对于更复杂的格式化需求，某些格式样式支持串接修饰符方法来自定默认样式。Caffé App 包含一个配套的 Apple Watch App，用于显示用户下次有资格获得免费咖啡的日期。此视图中显示的 [Date](https://developer.apple.com/documentation/foundation/date) 会自定默认 [dateTime](https://developer.apple.com/documentation/foundation/date/formatstyle/3798884-datetime) 格式样式，仅显示星期、小时和分钟：

```swift
var str = date.formatted(.dateTime
                            .locale(locale)
                            .minute()
                            .hour()
                            .weekday()
                            .attributed)
```

### 使用属性字符串设置文本样式

前面的代码也使用 [attributed](https://developer.apple.com/documentation/foundation/date/formatstyle/3796283-attributed) 修饰符来返回 [AttributedString](https://developer.apple.com/documentation/foundation/attributedstring)。属性字符串包含文本，以及应用于该文本各个范围的元数据。在此示例中，格式化器返回的属性字符串使用 [dateField](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/3796121-datefield) 属性来标记哪些文本范围对应格式化日期的哪些部分。这样，App 就能在属性容器中找到星期属性，并将其替换为橙色前景色属性。随后，SwiftUI 视图可以在设置手表显示样式时使用此属性。

```swift
let weekday = AttributeContainer
    .dateField(.weekday)

let color = AttributeContainer
    .foregroundColor(.orange)

str.replaceAttributes(weekday, with: color)
```

[`AttributedString`](https://developer.apple.com/documentation/foundation/attributedstring) 是强类型的，这意味着所有属性都必须具有已定义的名称和值类型。`AttributedString` 会在其 [AttributeScopes](https://developer.apple.com/documentation/foundation/attributescopes) 类型中为 Foundation、SwiftUI、AppKit 和 UIKit 定义属性。对于强调和链接等常见行内属性，属性字符串支持使用 Markdown 语法进行初始化，语法既可以位于源代码中，也可以位于 `.strings` 文件中。以下来自西班牙语本地化 `Localizable.strings` 文件的条目展示了强强调（`**`）、常规强调（`_`）和链接（`[]` 包含链接文本，后跟括号中的 URL）的 Markdown 格式：

```
"**Thank you!**" = "**¡Gracias!**";
"_Please visit our [website](https://www.example.com)._" = "_Visita nuestro [sitio web](https://www.example.com)._";
```

App 还可以定义自定属性，Caffé 就通过 `RainbowAttribute` 类型定义了一个属性，用来指明要以多种颜色显示的文本范围。Caffé App 通过以下方式添加此属性：

1. 将 `RainbowAttribute` 定义为 [CodableAttributedStringKey](https://developer.apple.com/documentation/foundation/codableattributedstringkey) 的扩展，并提供属性的名称和值类型。
2. 扩展 [`AttributeScopes`](https://developer.apple.com/documentation/foundation/attributescopes)，定义一个名为 `CaffeAppAttributes` 的新 [AttributeScope](https://developer.apple.com/documentation/foundation/attributescope)，其唯一成员是 `RainbowAttribute` 类型的 `rainbow`。App 还使用 `caffeApp` 扩展 `AttributeScopes`，这是一个 `CaffeAppAttributes` 类型的变量，使其能够通过动态成员查找语法访问 Caffé App 的自定属性。
3. 扩展 [AttributeDynamicLookup](https://developer.apple.com/documentation/foundation/attributedynamiclookup)，提供一个接受 `CaffeAppAttributes` 类型键路径的下标方法。这使代码能在查找 `CaffeAppAttributes` 成员时使用点语法。

```swift
enum RainbowAttribute: CodableAttributedStringKey, MarkdownDecodableAttributedStringKey {
    enum Value: String, Codable, Hashable {
        case plain
        case fun
        case extreme
    }
    
    static var name: String = "rainbow"
}

extension AttributeScopes {
    struct CaffeAppAttributes: AttributeScope {
        let rainbow: RainbowAttribute
    }
    
    var caffeApp: CaffeAppAttributes.Type { CaffeAppAttributes.self }
}

extension AttributeDynamicLookup {
    subscript<T: AttributedStringKey>(dynamicMember keyPath: KeyPath<AttributeScopes.CaffeAppAttributes, T>) -> T {
        self[T.self]
    }
}
```

`RainbowText` 的实现通过创建一个 [`AttributedString`](https://developer.apple.com/documentation/foundation/attributedstring) 并调用私有 `annotateRainbowColors(from:)` 方法应用颜色属性，来使用这些属性。为了创建使用自定属性作用域的 `AttributedString`，Caffé 会使用 [init(localized:options:table:bundle:locale:comment:including:)](https://developer.apple.com/documentation/foundation/attributedstring/3867591-init) 初始化方法，并将自定属性名称的键路径作为 `including:` 参数传入：

```swift
init(_ localizedKey: String.LocalizationValue) {
    attributedString = RainbowText.annotateRainbowColors(
        from: AttributedString(localized: localizedKey, including: \.caffeApp))
}
```

要在字符串中应用自定属性，调用方会使用 Markdown 扩展语法，如以下示例所示，它应用了彩虹属性的两个不同值：

```swift
RainbowText("^[Fast](rainbow: 'fun') & ^[Delicious](rainbow: 'extreme') Food")
    .font(.slogan)
    .frame(maxWidth: 260, alignment: .leading)
```

### 通过自动执行语法一致性简化本地化

某些语言的语法要求名词、形容词、冠词及其他词类在数量或性别上与句子的其他部分保持一致。本地化属性字符串可以使用模板字符串在运行时格式化值，从而执行这种一致性处理。

在 Caffé 中，每种餐点的详细信息视图都有一个按钮，用于指明用户选择向订单添加多少份该餐点。App 会用数量、份量和要添加到订单的餐点填充此按钮文本：

```swift
Button(
    "Add ^[\(quantity) \(foodSizeSelection.localizedName) \(food.localizedName)](inflect: true) to your order",
    action: orderButtonTapped
)
```

语法 `^[text](inflect:true)` 会指示生成的属性字符串对字符串进行_词形变化_，即对方括号内的文本范围执行自动语法一致性。此过程会考虑任何数值替换项的值，以及字符串替换项的语法性别。在英语中，当 `quantity` 不等于 `1` 时，这会使餐点名称变为复数形式。

在西班牙语中，`.strings` 文件中的本地化字符串会使用参数重排语法将名词放在形容词前面，如下所示：

```
"Añadir ^[%1$lld %3$@ %2$@](inflect: true) a tu pedido";
```

当自动语法引擎为西班牙语生成的字符串执行词形变化时，它会像处理英语一样，使餐点名称变为复数。在西班牙语中，它还会调整形容词（`foodSizeSelection.localizedName`），使其与 `quantity` 的数量和 `food.localizedName` 的语法性别相匹配。例如，一份小份沙拉在西班牙语中为 “1 ensalada pequeña”，而两份小份沙拉为 “2 ensaladas pequeñas”。在这两种情况下，语法引擎都会更改形容词 “pequeño”，使其与 “ensalada” 的阴性性别相匹配。

在某些语言中，App 可能需要向词形变化引擎提供词类信息。例如在英语中，“sandwich” 和 “juice” 既可以是名词，也可以是动词。在西班牙语中，表示餐点份量的 “grande” 和 “enorme” 既可以用作形容词，也可以用作名词。词形变化引擎遇到此类歧义时会记录警告。为明确意图，词形变化引擎接受一种语法标记，它使用 `^[…](morphology: {…})` 语法包装替换项并提供词类信息。以下来自英语字符串文件的条目展示了消除这种歧义的示例：

```
"Add ^[%lld %@ %@](inflect: true) to your order" = "Add ^[%lld %@ ^[%@](morphology: { partOfSpeech: \"noun\" })](inflect: true) to your order";
```

## 另请参阅

### 基础

- [显示易于理解的内容](displaying-human-friendly-content.md) — 使用格式化器将数据转换为可读字符串或 Swift 对象。

## 下载

- [BuildingALocalizedFoodOrderingApp.zip](https://docs-assets.developer.apple.com/published/fd1004611382/BuildingALocalizedFoodOrderingApp.zip)
