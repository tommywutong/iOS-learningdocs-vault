---
title: 'commitEditingAndReturnError:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/commiteditingandreturnerror:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/commiteditingandreturnerror:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/commiteditingandreturnerror%3A.json'
content_hash: 'sha256:38b8c204037faf77'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# commitEditingAndReturnError:

<sub>实例方法</sub>

尝试提交挂起的编辑，失败时返回错误。

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) commitEditingAndReturnError:(NSError **) error;
```

## 参数

- `error` — 若提交操作期间发生错误，返回时包含描述该问题的 `NSError` 对象。

## 返回值

若提交成功则为 [YES](../yes.md)，否则为 [NO](../no.md)。

## 讨论

在自动存储期间，由于存在挂起的编辑，提交编辑可能会失败。与其用意外警告打断用户，此方法为调用者提供了呈现错误或静默失败的选项，从而保留挂起的编辑且不打断用户的编辑。在此方法的实现中，你应尝试提交编辑，但若失败则返回 [NO](../no.md)，并在 `error` 中提供一个错误对象，以便按需呈现或忽略。

> [!note] 在 Swift 中处理错误
> 在 Swift 中，此方法返回 `Void`，并标有 `throws` 关键字，以指示在失败情况下会抛出错误。
>
> 你在 `try` 表达式中调用此方法，并在 `do` 语句的 `catch` 子句中处理任何错误，如 [The Swift Programming Language](https://docs.swift.org/swift-book/) 中的 [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) 以及 `About Imported Cocoa Error Parameters` 所述。
