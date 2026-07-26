---
title: 在 Swift 中处理 Cocoa 错误
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/handling-cocoa-errors-in-swift
source_url: 'https://developer.apple.com/documentation/swift/handling-cocoa-errors-in-swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/handling-cocoa-errors-in-swift.json'
content_hash: 'sha256:c0510341fafda346'
translated: true
---

> 导航： [Technologies](../technologies.md) · [Swift](../swift.md) · [Cocoa Design Patterns](cocoa-design-patterns.md)

# 在 Swift 中处理 Cocoa 错误

<sub>文章</sub>

抛出并捕获使用 Cocoa 错误类型的错误。

## 概述

你可以使用 Swift 的 `throw` 语句和 `do`-`catch` 语句来抛出和捕获来自 Cocoa API 的错误。Swift 会把带有错误参数的 Cocoa 方法导入为会抛出错误的方法，具体说明见 [About Imported Cocoa Error Parameters](about-imported-cocoa-error-parameters.md)。

### 捕获错误

在 Swift 中，调用一个会抛出错误的方法需要显式的错误处理。由于带有错误参数的 Cocoa 方法会被导入为会抛出错误的方法，你需要使用 Swift 的 `do`-`catch` 语句来处理它们。

下面是在 Objective-C 中调用一个方法时如何处理错误的例子：

```occ
NSFileManager *fileManager = [NSFileManager defaultManager];
NSURL *fromURL = [NSURL fileURLWithPath:@"/path/to/old"];
NSURL *toURL = [NSURL fileURLWithPath:@"/path/to/new"];
NSError *error = nil;
BOOL success = [fileManager moveItemAtURL:fromURL toURL:toURL error:&error];
if (!success) {
    NSLog(@"Error: %@", error.domain);
}
```

下面是在 Swift 中处理同一个错误的方式：

```swift
let fileManager = FileManager.default
let fromURL = URL(fileURLWithPath: "/path/to/old")
let toURL = URL(fileURLWithPath: "/path/to/new")
do {
    try fileManager.moveItem(at: fromURL, to: toURL)
} catch let error as NSError {
    print("Error: \(error.domain)")
}
```

你也可以使用 `do`-`catch` 语句匹配特定的 Cocoa 错误码，以区分不同的失败情况：

```swift
do {
    try fileManager.moveItem(at: fromURL, to: toURL)
} catch CocoaError.fileNoSuchFile {
    print("Error: no such file exists")
} catch CocoaError.fileReadUnsupportedScheme {
    print("Error: unsupported scheme (should be 'file://')")
}
```

### 抛出错误

你可以通过初始化一个 Cocoa 错误类型，并传入相应的错误域和错误码，来抛出 Cocoa 错误：

```swift
throw NSError(domain: NSURLErrorDomain, code: NSURLErrorCannotOpenFile, userInfo: nil)
```

如果 Objective-C 代码调用了一个会抛出错误的 Swift 方法，该错误会自动传播到被桥接的 Objective-C 方法的错误指针参数中。

### 抛出并捕获来自自定义错误域的错误

你可以在 Cocoa 中使用自定义错误域，对相关类别的错误进行分组。下面的例子使用 `NS_ERROR_ENUM` 宏对错误常量进行分组：

```occ
extern NSErrorDomain const MyErrorDomain;
typedef NS_ERROR_ENUM(MyErrorDomain, MyError) {
    specificError1 = 0,
    specificError2 = 1
};
```

这个例子展示了如何在 Swift 中使用该自定义错误类型抛出错误：

```swift
func customThrow() throws {
    throw NSError(
        domain: MyErrorDomain,
        code: MyError.specificError2.rawValue,
        userInfo: [
            NSLocalizedDescriptionKey: "A customized error from MyErrorDomain."
        ]
    )
}
```

这个例子展示了如何捕获来自某个特定错误域的错误，并提请注意来自其他错误域的未处理错误：

```swift
do {
    try customThrow()
} catch MyError.specificError1 {
    print("Caught specific error #1")
} catch let error as MyError where error.code == .specificError2 {
    print("Caught specific error #2, ", error.localizedDescription)
    // Prints "Caught specific error #2. A customized error from MyErrorDomain."
} catch let error {
    fatalError("Some other error: \(error)")
}
```

### 只在 Objective-C 中处理异常

在 Objective-C 中，异常与错误是不同的概念。Objective-C 的异常处理使用 `@try`、`@catch` 和 `@throw` 语法，用来表示不可恢复的程序员错误。这与上文描述的 Cocoa 模式不同——后者使用一个末尾的 [NSError](../foundation/nserror.md) 参数来表示你在开发过程中会预先规划、可以恢复的错误。

在 Swift 中，你可以从使用 Cocoa 错误模式传递的错误中恢复，正如上文 [Catch Errors](handling-cocoa-errors-in-swift.md#Catch-Errors) 中所述。但是，在 Swift 中并没有安全的方式可以从 Objective-C 异常中恢复。要处理 Objective-C 异常，需要编写 Objective-C 代码，在异常到达任何 Swift 代码之前将其捕获。

## 另请参阅

### 常见模式

- [Using Key-Value Observing in Swift](using-key-value-observing-in-swift.md) — 就其他对象属性的变化通知相关对象。
- [Using Delegates to Customize Object Behavior](using-delegates-to-customize-object-behavior.md) — 代表委托方响应事件。
- [Managing a Shared Resource Using a Singleton](managing-a-shared-resource-using-a-singleton.md) — 使用单个共享的类实例，提供对共享资源的访问。
- [About Imported Cocoa Error Parameters](about-imported-cocoa-error-parameters.md) — 了解 Cocoa 错误参数是如何被转换为 Swift 中会抛出错误的方法的。
