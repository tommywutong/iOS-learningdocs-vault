---
title: 测试任意指针是否为有效对象指针 | Cocoa with Love
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/10/testing-if-arbitrary-pointer-is-valid.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:5e022040f1c118bd'
translated: true
---

> 原文：[Testing if an arbitrary pointer is a valid object pointer | Cocoa with Love](https://www.cocoawithlove.com/2010/10/testing-if-arbitrary-pointer-is-valid.html)　·　Cocoa with Love (Matt Gallagher)

在这篇文章中，我探讨了一种测试任意指针是否为有效 Objective-C 对象指针的方法。测试结果并非绝对准确，而且如果指针指向的不是有效内存位置，可能会干扰 gdb 调试。因此，你不会想经常使用这个方法（当然也肯定不会在生产代码中使用）。但当你面对并非由你分配的内存、茫然无措时，它可以成为一个方便的调试工具。

## 介绍

我最初编写这段代码时，正在检查本地 `CFNotificationCenter` 发出的所有通知，试图找出我在一些 AVFoundation 视频代码中出错的地方（AVFoundation 在媒体播放时会产生大量通知）。

这些通知的回调函数拥有以下原型（prototype）：

```objc
void MyNotificationCallBack (
   CFNotificationCenterRef center,
   void *observer,
   CFStringRef name,
   const void *object,
   CFDictionaryRef userInfo
);
```

与通知关联的 `object` 以 `void *` 形式传递。大多数情况下，`object` 的值会是一个 Objective-C 对象，但在少数情况下不是，此时如果直接将其传入 `NSLog`，可能会导致程序崩溃。

## 你需要测试什么？

再次回到这个问题：什么是有效的 Objective-C 对象？

对于向对象发送消息而言，你只需要对象指针所指向的值（即 `isa` 指针）是一个已注册的 `Class` 值。这是需要测试的最重要一点——任意内存值碰巧是一个有效 `Class` 的概率相当低（尽管并非为零）。

但要成为一个可用的对象，还有一个要求：`isa` 指针之后的内存空间必须是有效的。这并不容易测试，但可以测试对象本身是否至少分配了与类实例大小（instance size）一样大的内存。

然而，这个分配测试对于非堆分配（heap allocated）对象，不必返回肯定结果。在 Objective-C 中，非堆分配对象最常见的例子是编译器创建的字符串。因此，对于一个以 `isa` 指针开头的内存块，如果它在堆上的分配得当，几乎可以保证该对象是一个有效的 Objective-C 对象；但这个测试失败并不能排除它是一个有效对象的可能性。

最后，在进行所有这些操作时，你测试的指针可能根本指向一个无效的内存位置。如果你有兴趣处理这种情况，需要设置一个信号处理程序（signal handler）（或 Mach 异常处理程序）来捕获 `SIGBUS` 和 `SIGSEGV` 信号（如果走 Mach 异常路线，则是 `EXC_BAD_ACCESS`）。

## 代码

```objc
#import &lt;malloc/malloc.h&gt;
#import &lt;objc/runtime.h&gt;

static sigjmp_buf sigjmp_env;

void
PointerReadFailedHandler(int signum)
{
    siglongjmp (sigjmp_env, 1);
}

BOOL IsPointerAnObject(const void *testPointer, BOOL *allocatedLargeEnough)
{
    *allocatedLargeEnough = NO;
    
    // 设置 SIGSEGV 和 SIGBUS 处理程序
    struct sigaction new_segv_action, old_segv_action;
    struct sigaction new_bus_action, old_bus_action;
    new_segv_action.sa_handler = PointerReadFailedHandler;
    new_bus_action.sa_handler = PointerReadFailedHandler;
    sigemptyset(&new_segv_action.sa_mask);
    sigemptyset(&new_bus_action.sa_mask);
    new_segv_action.sa_flags = 0;
    new_bus_action.sa_flags = 0;
    sigaction (SIGSEGV, &new_segv_action, &old_segv_action);
    sigaction (SIGBUS, &new_bus_action, &old_bus_action);

    // 若信号被触发，信号处理程序会将我们带回到这里
    if (sigsetjmp(sigjmp_env, 1))
    {
        sigaction (SIGSEGV, &old_segv_action, NULL);
        sigaction (SIGBUS, &old_bus_action, NULL);
        return NO;
    }
    
    Class testPointerClass = *((Class *)testPointer);

    // 获取类列表并查找 testPointerClass
    BOOL isClass = NO;
    NSInteger numClasses = objc_getClassList(NULL, 0);
    Class *classesList = malloc(sizeof(Class) * numClasses);
    numClasses = objc_getClassList(classesList, numClasses);
    for (int i = 0; i < numClasses; i++)
    {
        if (classesList[i] == testPointerClass)
        {
            isClass = YES;
            break;
        }
    }
    free(classesList);

    // 信号处理程序使用完毕（恢复之前的处理程序）
    sigaction (SIGSEGV, &old_segv_action, NULL);
    sigaction (SIGBUS, &old_bus_action, NULL);
    
    // 指针不指向有效的 isa 指针
    if (!isClass)
    {
        return NO;
    }
    
    // 检查分配大小
    size_t allocated_size = malloc_size(testPointer);
    size_t instance_size = class_getInstanceSize(testPointerClass);
    if (allocated_size > instance_size)
    {
        *allocatedLargeEnough = YES;
    }
    
    return YES;
}
```

## 函数的运行结果

运行此测试程序：

```objc
void LogPointerInformation(const void *somePointer)
{
    BOOL allocatedLargeEnough;
    BOOL isMessageableObject = IsPointerAnObject(somePointer, &allocatedLargeEnough);
    NSLog(@"The pointer %p is %@ and is %@.",
        somePointer,
        isMessageableObject ?
            @"a valid object" :
            @"not a valid object",
        allocatedLargeEnough ?
            @"allocated at least as large as the required instance size" :
            @"not a known allocation");
}

int main (int argc, const char * argv[]) {
    NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];

    LogPointerInformation(@"");
    LogPointerInformation([[[NSObject alloc] init] autorelease]);
    LogPointerInformation(LogPointerInformation);
    LogPointerInformation(0x12345678);

    [pool drain];
    return 0;
}
```

得到以下结果（为简洁起见，我截断了 `NSLog` 的时间戳）：

```objc
The pointer 0x100001130 is a valid object and is not a known allocation.
The pointer 0x10011e940 is a valid object and is allocated at least as large as the required instance size.
The pointer 0x100000c0d is not a valid object and is not a known allocation.
The pointer 0x12345678 is not a valid object and is not a known allocation.
```

## 此方法的局限性

此方法最严重的局限性在于它永远无法保证任何事情。正因如此，切勿在生产代码中使用它。

函数会完全失效的最明显情况是，当测试一个 `malloc` 分配的、元素为 Objective-C 类指针的 C 数组时。这个内存块确实以一个有效的 `Class` 值开头，并且 `malloc_size` 甚至可能大于该类实例的大小——但这个块从未被真正分配为对象，如果该类有任何重要的实例值，它们都可能是无效的。

对于非堆分配的对象，很难保证其实例内存位于可寻址内存中。这意味着你可能会触发 `SIGSEGV` 或 `SIGBUS` 信号。

还是关于信号的问题。虽然我在代码中包含了信号处理，但你很可能永远不希望它被调用，因为它会直接让 gdb 停止。

通常情况下，你可以给 gdb 一个 `handle signal nostop noprint pass` 命令让它在信号发生后继续执行，但在这里行不通。让 Mac 版本的 gdb 在 `EXC_BAD_ACCESS` 之后继续执行存在一些问题。实际上，让 gdb 捕获信号，然后在 Xcode 中将程序执行点手动拖到 `sigsetjmp` 块的顶部会更简单。

最后一点注意事项：我编写的信号处理代码严格来说不是线程安全的（thread-safe），也不可重入（non-reentrant）。

## 结论

这个结果更像是一种启发式（heuristic）判断，而非绝对裁决。

然而，此方法是一种有用的工具，可以在调试目的下，对某个值是否为有效对象提供“可接受的”验证。在将值发送给 `NSLog` 之前进行测试，它无疑是足够好的。

当触发无效内存访问信号时，gdb 会出现问题，这很烦人。我很想知道是否有办法避免这种情况。这无疑进一步降低了在真正任意的值上使用此代码的积极性。
