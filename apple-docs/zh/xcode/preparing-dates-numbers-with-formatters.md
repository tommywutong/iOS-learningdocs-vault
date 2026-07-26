---
title: 为翻译准备日期、货币和数字
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/preparing-dates-numbers-with-formatters
source_url: 'https://developer.apple.com/documentation/xcode/preparing-dates-numbers-with-formatters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/preparing-dates-numbers-with-formatters.json'
content_hash: 'sha256:7ce4d5333daeef79'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Localization](localization.md)

# 为翻译准备日期、货币和数字

<sub>文章</sub>

使用格式化程序，确保日期、货币和数字能在多种语言和区域设置下正确显示。

## 概述

不同的语言和地区呈现日期和数字的格式各不相同。有些语言使用句点（.）作为小数点分隔符，另一些使用逗号（,）。有些在格式化百分比时会把百分号放在数字前面。而且许多地区即便属于同一种语言，时间和日期的显示方式也不同。

与其自己尝试处理所有这些差异，不如使用 Foundation 内置的格式化程序，为你想要展示的日期和数字创建可本地化的版本。

### 使用预定义样式格式化日期

要将日期或数字转换为可本地化的字符串，请使用 Foundation 的格式化程序和样式。这些 API 接受你的日期和数字对象的实例，并根据你 App 运行所在设备的区域设置，将它们转换为可本地化的格式化字符串。

例如，要从日期对象创建一个可本地化的字符串，先创建你想要格式化的 [Date](../foundation/date.md) 的实例，然后在该日期上调用 [formatted()](<../foundation/date/formatted().md>) 函数。

```swift
// The current time and date. Example output is for en_US locale.en_US locale.
let date = Date.now

// A default, formatted, localizable date string.
let defaultFormatted = date.formatted()
// "8/25/2023, 12:03 PM"
```

要改变显示的日期组成部分，或只显示时间或日期，请在 `Date` 对象上使用 [formatted(date:time:)](<../foundation/date/formatted(date_time_).md>) 方法，并传入 [Date.FormatStyle.DateStyle](../foundation/date/formatstyle/datestyle.md) 和 [Date.FormatStyle.TimeStyle](../foundation/date/formatstyle/timestyle.md) 的实例。

```swift
// The date you want to format.
let meetingDate = Date.now

// A formatted date displaying only the date.
let formattedDate = meetingDate.formatted(date: .abbreviated, time: .omitted)
// "Aug 25, 2023"

// A formatted date displaying only the time.
let formattedTime = meetingDate.formatted(date: .omitted, time: .standard)
// "12:03:10 PM"

// A formatted date displaying both the date and time.
let formattedDateAndTime = meetingDate.formatted(date: .complete, time: .complete)
// "Friday, August 25, 2023 at 12:03:10 PM PDT"
```

### 创建自己的自定日期样式

要将日期格式化为特定样式，请创建你自己的自定日期样式，只包含你想要显示的日期属性。

例如，要创建一个只包含月、日、年的日期：

1. 创建你想要格式化的 `Date` 对象的实例。
2. 创建一个 [Date.FormatStyle](../foundation/date/formatstyle.md) 结构体，或使用 [dateTime](../foundation/formatstyle/datetime.md) 工厂变量，然后在连续的函数调用中把你想要显示的属性串联起来。
3. 然后把这个 `Date.FormatStyle` 结构体作为输入传给日期对象上的 [formatted(_:)](<../foundation/date/formatted(__).md>) 函数。

```swift
// A date string with specific attributes.
let myDate = Date.now
let formatStyle = Date.FormatStyle.dateTime.year().day().month()
let formatted = date.formatted(formatStyle)
// "Sep 7, 2023"
```

你也可以用一行代码实现相同的结果。

```swift
// Same result in one line using the `dateTime` factory variable.
let formatted = Date.now.formatted(.dateTime.year().day().month())
// "Sep 7, 2023"
```

你传入 `formatted(_:)` 函数的字段顺序并不重要。例如，下面这些代码行会产生相同的结果。

```swift
// Same result.
Date.now.formatted(.dateTime.year().month().day().hour().minute().second())
Date.now.formatted(.dateTime.second().minute().hour().day().month().year())
// "Sep 7, 2023 at 10:29:52 AM"
```

通过将 [Date.FormatStyle.Symbol](../foundation/date/formatstyle/symbol.md) 结构体的实例与各自对应的格式化属性串联起来，自定你想要显示的日期样式。

```swift
// A date string for a wide month format.
let formattedWide = date.formatted(.dateTime.year().day().month(.wide))
// "September 7, 2023"

// A date string for a wide weekday.
let formattedWeekday = date.formatted(.dateTime.weekday(.wide))
// "Thursday"

// A date string for the ISO 8601 time and date standard.
let logFormat = date.formatted(.iso8601)
// "2023-09-07T17:25:39Z"

// A date string representing a file format.
let fileNameFormat = date.formatted(.iso8601.year().month().day().dateSeparator(.dash))
// "2023-09-07"
```

### 格式化百分比和科学记数法数字

如果你想为数字（例如 [Int](../swift/int.md)、[Double](../swift/double.md)、[Decimal](../foundation/decimal.md) 或 [Float](../swift/float.md)）创建可本地化的字符串，请在该数字实例上调用 `formatted()` 或 `formatted(_:)`，并传入你想要显示的格式样式。

例如，要创建 `Int` 的格式化版本，请在该数字上调用 [formatted()](<../swift/binaryinteger/formatted().md>) 函数。

```swift
let value = 12345
// A default, formatted, localizable date string.
var formatted = value.formatted()
// "12,345"
```

要把数字格式化为百分比，请在你想要显示的数字上调用 `formatted(_ format:)`，并传入 [NumberFormatter.Style.percent](../foundation/numberformatter/style/percent.md) 数字格式样式。整数会使用整个数字直接转换为百分比。

```swift
let number = 25
let numberFormatted = number.formatted(.percent)
// "25%"
```

小数会在 0 到 1 的范围内转换。

```swift
let fraction = 0.25
let fractionFormatted = fraction.formatted(.percent)
// "25%"
```

要以科学记数法显示数字，请在该数字上调用 [formatted(_:)](<../swift/sequence/formatted(__).md>)，并使用 [scientific](../foundation/numberformatstyleconfiguration/notation/scientific.md)、[notation(_:)](<../foundation/floatingpointformatstyle/notation(__).md>) 和 [number](../foundation/formatstyle/number-3luf2.md) 格式样式来显示。

```swift
let scientific = 42e9
let scientificFormatted = scientific.formatted(.number.notation(.scientific))
// "4.2E10"
```

### 格式化货币

要将数字呈现为可本地化的货币：

1. 查找你想要显示的货币的[代码](https://en.wikipedia.org/wiki/ISO_4217)（例如加拿大的 `"CAD"`）。
2. 将该代码作为参数传给 [Decimal.FormatStyle.Currency](../foundation/decimal/formatstyle/currency.md) 格式样式的初始化方法 [init(code:locale:)](<../foundation/decimal/formatstyle/currency/init(code_locale_).md>)。
3. 然后在该数字上调用 [formatted(_:)](<../foundation/decimal/formatted(__).md>)，传入货币格式实例。

```swift
// A number formatted in different currencies.
let amount: Decimal = 12345.67
amount.formatted(.currency(code: "JPY"))
// "¥12,346"
amount.formatted(.currency(code: "EUR").presentation(.fullName))
// "12,345.67 euros"
amount.formatted(.currency(code: "USD").grouping(.automatic))
// "$12,345.67"
```

> [!note] 注意
> 为确保精确度，不要使用 [Float](../swift/float.md) 或 [Double](../swift/double.md) 来表示你 App 中的货币。请改用 [Decimal](../foundation/decimal.md)。

### 将时间格式化为区间或时长

要将一段时间区间显示为可本地化的字符串：

1. 创建两个 [Date](../foundation/date.md) 对象的实例——一个表示时间区间的开始，另一个表示结束。
2. 使用这两个日期，创建一个 [Range](../swift/range.md) 结构体，设置该区间的上下界。
3. 然后调用区间格式化程序之一——例如 [formatted()](<../swift/range/formatted().md>) 或 [formatted(date:time:)](<../swift/range/formatted(date_time_).md>)——传入你想要显示的时间和日期样式。

```swift
// An example of a time interval.

// The current time and date. Example output is for en_US locale.
let now = Date.now

// 5000 seconds from now.
let later = now + TimeInterval(5000)

// The default formatted display for a time interval.
let range = (now..<later).formatted()
// "9/8/2023, 10:44 AM – 12:07 PM"

// A time interval formatted using a predefined date format.
let noDate = (now..<later).formatted(date: .omitted, time: .complete)
// "10:44:39 AM PDT – 12:07:59 PM PDT"
```

要把时间显示为时长，你可以用类似的方式定义一个日期区间，并将该区间转换为时长。

```swift
// An example of a duration.

// Duration from a range of dates.
let timeDuration = (now..<later).formatted(.timeDuration)
// "1:23:20"

let components = (now..<later).formatted(.components(style: .wide))
// "1 hour, 23 minutes, 20 seconds"

let relative = later.formatted(.relative(presentation: .named, unitsStyle: .wide))
// "in 1 hour"
```

你还可以在 [Duration](../swift/duration.md) 结构体上使用像 [seconds(_:)](<../swift/duration/seconds(__)-5ifzr.md>) 这样的工厂方法，从单个数字生成可本地化的时长。

例如，要将给定的秒数显示为一段时长：

1. 将你想要显示的秒数传给 [Duration](../swift/duration.md) 结构体的 [seconds(_:)](<../swift/duration/seconds(__)-5ifzr.md>) 函数。
2. 然后调用 [formatted(_:)](<../swift/duration/formatted(__).md>)，传入 [Duration.TimeFormatStyle](../swift/duration/timeformatstyle.md) 或 [Duration.UnitsFormatStyle](../swift/duration/unitsformatstyle.md) 的实例，以获得你想要的格式和样式。

```swift
// Duration formatted from a single unit of time.
Duration.seconds(2000).formatted(.time(pattern: .hourMinute)) 
// "0:33"
Duration.seconds(2000).formatted(.time(pattern: .hourMinuteSecond)) 
// "0:33:20"
Duration.seconds(2000).formatted(.time(pattern: .minuteSecond)) 
// "33:20"
```

### 将条目格式化为列表

要以列表形式创建可本地化的字符串，请使用 [ListFormatStyle](../foundation/listformatstyle.md) 结构体，并搭配 [formatted()](<../swift/sequence/formatted().md>) 或 [formatted(_:)](<../swift/sequence/formatted(__).md>) 函数，为一个条目组成的 [Sequence](../swift/sequence.md) 创建字符串表示。

```swift
// An array of strings formatted into a list.
let sizes = ["small", "medium", "large"]
sizes.formatted(.list(type: .and, width: .narrow))
// "small, medium, large"
sizes.formatted(.list(type: .and, width: .standard))
// "small, medium, and large"
sizes.formatted(.list(type: .and, width: .short))
// "small, medium, & large"
```

你也可以通过调用 [list(memberStyle:type:width:)](<../foundation/formatstyle/list(memberstyle_type_width_).md>) 函数并搭配特定的列表格式样式，用不同的格式化样式创建列表。

```swift
// A list of numbers formatted as percentages.
[25, 50, 75].formatted(.list(memberStyle: .percent, type: .or))
// "25%, 50%, or 75%"
```

### 在不同区域设置间转换和显示测量单位

计量单位会因格式样式所使用的区域设置而有很大差异。例如，`en_US` 区域设置下以英尺表示的距离，在法语区域设置 `fr_FR` 下会以米显示。

要确保你的计量单位能在不同语言和地区之间正确转换和显示：

1. 使用 [Measurement](../foundation/measurement.md) 结构体定义一个表示你想要显示的计量单位的变量。
2. 然后在该变量上调用 [formatted(_:)](<../foundation/measurement/formatted(__).md>) 或 [formatted(_:)](<../foundation/measurement/formatted(__).md>)，得到你想要的显示样式。

例如，假设你想转换并显示以下测量值。

```swift
// Measurements to display.
let speedLimit = Measurement(value: 110, unit: UnitSpeed.kilometersPerHour)
let distanceToMoon = Measurement(value: 384400, unit: UnitLength.kilometers)
let surfBoardLength = Measurement(value: 8, unit: UnitLength.feet)
let waterTemperature = Measurement(value: 61.2, unit: UnitTemperature.fahrenheit)
```

要使用默认格式转换它们，请在该测量对象上调用 [formatted(_:)](<../foundation/measurement/formatted(__).md>)。

```swift
// Example output is for en_US locale.

// Default display for a unit of measure.
speedLimit.formatted()
// "68 mph"
distanceToMoon.formatted()
// "238,855 mi"
surfBoardLength.formatted()
// "8 ft"
waterTemperature.formatted()
// "61.2°F"
```

要自定输出，请在该测量值上调用 [formatted(_:)](<../foundation/measurement/formatted(__).md>) 函数，并使用 [measurement(width:usage:hidesScaleName:numberFormatStyle:)](<../foundation/formatstyle/measurement(width_usage_hidesscalename_numberformatstyle_).md>) 工厂方法来创建你想要的格式和样式。

```swift
// Custom display options for a unit of measure.
distanceToMoon.formatted(.measurement(width: .wide))
// "238,855 miles"
distanceToMoon.formatted(.measurement(width: .abbreviated))
// "238,855 mi"
distanceToMoon.formatted(.measurement(width: .narrow))
// "238,855mi"
```

### 在 SwiftUI 中格式化日期和数字

要在 SwiftUI 中格式化日期和数字，请在 SwiftUI 视图控制上使用 `format` 初始化方法，来自定这些字符串的显示方式。

例如，下面是一个 SwiftUI 视图，它使用 [Text](../swiftui/text.md) 视图的 [init(_:format:)](<../swiftui/text/init(__format_).md>) 初始化方法，显示 `Date` 的三种不同可本地化格式。

```swift
@State private var myDate = Date.now

var body: some View {
    VStack {
        Text(myDate, format: Date.FormatStyle(date: .numeric, time: .omitted))
        Text(myDate, format: Date.FormatStyle(date: .complete, time: .complete))
        Text(myDate, format: Date.FormatStyle().hour(.defaultDigits(amPM: .omitted)).minute())
    }
}
```

这个例子使用 [TextField](../swiftui/textfield.md) 视图的 [init(_:value:format:prompt:)](<../swiftui/textfield/init(__value_format_prompt_)-7flsn.md>) 初始化方法，将一个数字显示为小费的百分比。

```swift
@State private var tip = 0.15

var body: some View {
    HStack {
        Text("Tip")
        Spacer()
        TextField("Amount", value: $tip, format: .percent)
    }
}
```

## 测试格式化程序

要测试并查看你的格式化程序在不同语言和地区下的显示效果，请创建一个 [Locale](../foundation/locale.md) 对象的实例，传入你想要测试的地区的 `identifier`。然后将该区域设置应用到你格式化字符串的输出上，查看该字符串在该语言和地区下的显示效果。

例如，你可以按如下方式查看你的可本地化字符串在法语中的显示效果。

```swift
// The locale for France French.
let frenchLocale = Locale(identifier: "fr_FR")
                        
let stages = ["50", "75", "100"]
stages.formatted(.list(type: .and).locale(frenchLocale))
// "50, 75 et 100"
stages.formatted(.list(type: .or).locale(frenchLocale))
// "50, 75 ou 100"
```

要在 SwiftUI 中测试你的格式化程序，请在代码的 `#Preview` 部分中设置环境变量里的区域设置。

```swift
struct ContentView: View {
    @State private var myDate = Date.now
    @Environment(\.locale) var locale

    var body: some View {
        VStack {
            Text(myDate, format: .dateTime.second().minute().hour().day().month().year().locale(locale))
        }
    }
}

#Preview {
    Group {
        ContentView()
            .environment(\.locale, Locale(identifier: "fr_FR"))
        ContentView()
            .environment(\.locale, Locale(identifier: "pt_BR"))
    }
}
```

## 另请参阅

### 字符串与文本

- [为本地化准备你的界面](preparing-your-interface-for-localization.md) — 找出你 App 中需要翻译的文本，并验证你的界面能否适配已翻译的文本。
- [为翻译准备你 App 的文本](preparing-your-apps-text-for-translation.md) — 使用可本地化 API，自动用你 App 面向用户的文本填充字符串目录。
</content>
