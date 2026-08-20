---
title: Objective-C 编程语言
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocExceptionHandling.html
archived_at: '2026-07-15T07:17:30.384045Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 编程语言](Introduction.md)


[下一页](Threading.md)[上一页](Selectors.md)

# 异常处理

Objective-C 语言拥有一套与 Java 和 C++ 类似的异常处理语法。通过将这套语法与 `NSException`、`NSError` 或自定义类结合使用，你可以为程序添加健壮的错误处理机制。本章概要介绍异常语法与处理方式；更多细节参见 _[异常编程专题](../Exception%20Programming%20Topics/Introduction%20to%20Exception%20Programming%20Topics%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgayte2i)_。

使用 GNU 编译器集合（GCC）3.3 及更高版本，Objective-C 提供了语言层面的异常处理支持。要开启对这些特性的支持，需使用 GNU 编译器集合（GCC）3.3 及更高版本的 `-fobjc-exceptions` 开关。（注意，使用这个开关会使应用程序只能在 OS X v10.3 及更高版本上运行，因为更早版本的系统不具备异常处理和同步所需的运行时支持。）

异常（exception）是一种中断程序正常执行流程的特殊状况。硬件和软件都可能因各种原因产生异常（异常通常被称为被_引发_或_抛出_）。例如算术错误（如除以零、下溢或上溢）、调用未定义的指令（比如试图调用一个未实现的方法），以及试图访问越界的集合元素。

Objective-C 的异常支持涉及四个编译器指令：`@try`、`@catch`、`@throw` 和 `@finally`：

- 可能抛出异常的代码放在 `@try{}` 块中。
- `@catch{}` 块包含针对 `@try{}` 块中抛出异常的处理逻辑。你可以使用多个 `@catch{}` 块来捕获不同类型的异常。（代码示例参见[捕获不同类型的异常](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjtfuytomjyg4zq)。）
- 使用 `@throw` 指令来抛出异常，异常本质上是一个 Objective-C 对象。你通常会使用 `NSException` 对象，但这并非强制要求。
- `@finally{}` 块包含无论是否抛出异常都必须执行的代码。

下面这个例子展示了一个简单的异常处理算法：

```objc
Cup *cup = [[Cup alloc] init];

@try {
    [cup fill];
}
@catch (NSException *exception) {
    NSLog(@"main: Caught %@: %@", [exception name], [exception reason]);
}
@finally {
    [cup release];
}
```


要捕获在 `@try{}` 块中抛出的异常，需在 `@try{}` 块之后使用一个或多个 `@catch{}` 块。`@catch{}` 块应当按照从最具体到最不具体的顺序排列。这样你就可以按组来定制异常的处理方式，如清单 10-1 所示。

__清单 10-1__  一个异常处理器


```objc
@try {
    ...
}
@catch (CustomException *ce) {   // 1
    ...
}
@catch (NSException *ne) {       // 2
    // 执行这一层需要的处理。
    ...

}
@catch (id ue) {
    ...
}
@finally {                       // 3
    // 执行无论是否发生异常都需要的处理。
    ...
}
```

以下列表说明了带编号的代码行：

1. 捕获最具体的异常类型。
2. 捕获更通用的异常类型。
3. 执行无论是否抛出异常都必须执行的清理处理。

要抛出一个异常，你必须实例化一个包含适当信息（例如异常名称和抛出原因）的对象。

```objc
NSException *exception = [NSException exceptionWithName: @"HotTeaException"
                                                 reason: @"The tea is too hot"
                                               userInfo: nil];
@throw exception;
```

在 `@catch{}` 块内部，你可以使用不带参数的 `@throw` 指令重新抛出已捕获的异常。在这种情况下省略参数可以让代码更具可读性。

你并不局限于只能抛出 `NSException` 对象。你可以把任何 Objective-C 对象当作异常对象抛出。`NSException` 类提供了有助于异常处理的方法，但如果你愿意，也可以实现自己的方法。你还可以将 `NSException` 子类化，以实现特定类型的异常，比如文件系统异常或通信异常。

[下一页](Threading.md)[上一页](Selectors.md)

