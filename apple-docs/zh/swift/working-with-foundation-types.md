---
title: 使用 Foundation 类型
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/working-with-foundation-types
source_url: 'https://developer.apple.com/documentation/swift/working-with-foundation-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/working-with-foundation-types.json'
content_hash: 'sha256:f178ea443422bf8b'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [导入的 C 与 Objective-C API](imported-c-and-objective-c-apis.md)

# 使用 Foundation 类型

<sub>文章</sub>

在你的 Swift 代码库中使用桥接的 Foundation 类型来处理日期、时间和其他值。

## 概述

在导入 Foundation 框架时，Swift overlay 为许多桥接的引用类型提供了值类型。许多其他类型会被重命名或嵌套，以理清它们之间的关系。

### 优先使用 Swift 值类型而非桥接的 Objective-C 引用类型

下表中的值类型与其对应的引用类型具有相同的功能。包含可变与不可变子类的类簇（class cluster），例如 `NSArray` 和 `NSMutableArray`，会被桥接为单一的值类型。

| Swift 值类型 | Objective-C 引用类型 |
|---|---|
| `AffineTransform` | `NSAffineTransform` |
| `Array` | `NSArray` |
| `Calendar` | `NSCalendar` |
| `CharacterSet` | `NSCharacterSet` |
| `Data` | `NSData` |
| `DateComponents` | `NSDateComponents` |
| `DateInterval` | `NSDateInterval` |
| `Date` | `NSDate` |
| `Decimal` | `NSDecimalNumber` |
| `Dictionary` | `NSDictionary` |
| `IndexPath` | `NSIndexPath` |
| `IndexSet` | `NSIndexSet` |
| `Locale` | `NSLocale` |
| `Measurement` | `NSMeasurement` |
| `Notification` | `NSNotification` |
| Swift 数值类型（`Int`、`Float` 等） | `NSNumber` |
| `PersonNameComponents` | `NSPersonNameComponents` |
| `Set` | `NSSet` |
| `String` | `NSString` |
| `TimeZone` | `NSTimeZone` |
| `URL` | `NSURL` |
| `URLComponents` | `NSURLComponents` |
| `URLQueryItem` | `NSURLQueryItem` |
| `URLRequest` | `NSURLRequest` |
| `UUID` | `NSUUID` |

当 Swift 代码导入 Objective-C API 时，导入器会将 Foundation 引用类型替换为它们对应的值类型。因此，你几乎永远不需要在自己的代码中直接使用桥接的引用类型。

如果你需要 Foundation 引用类型所附带的引用语义，可以通过它原本的 `NS` 类名前缀来访问。使用 `as` 关键字即可在 Swift 值类型与其对应的引用类型之间转换。

```swift
let dataValue = Data(base64Encoded: myString)
let dataReference = dataValue as NSData?
```

### 注意被重命名的引用类型

对于_未_桥接到值类型的 Foundation 类型，Swift overlay 会重命名类和协议，以及相关的枚举和常量。这些类型和协议会去掉 `NS` 前缀，但有以下例外：

- Objective-C 特有或与 Objective-C 运行时本质绑定的类，例如 `NSObject`、`NSAutoreleasePool`、`NSException` 和 `NSProxy`
- 特定于平台的类，例如 `NSBackgroundActivity`、`NSUserNotification` 和 `NSXPCConnection`

Foundation 类通常会声明枚举或常量类型。导入这些类型时，Swift 会把它们移为其相关类型的嵌套类型。例如，`NSJSONReadingOptions` 选项集会被导入为 `JSONSerialization.ReadingOptions`。

## 另请参阅

### Cocoa 框架

- [使用 Core Foundation 类型](working-with-core-foundation-types.md) — 在你的 Swift 代码中直接使用内存受管理的 Core Foundation 类型，并按需手动处理保留（retain）操作。
