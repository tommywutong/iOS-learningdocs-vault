---
title: 用 Objective-C 编程
apple_id: TP40011210
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/WorkingwithBlocks/WorkingwithBlocks.html
archived_at: '2026-07-15T07:17:59.433127Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [用 Objective-C 编程](About%20Objective-C.md)


[下一页](Dealing%20with%20Errors.md)[上一页](Values%20and%20Collections.md)

# 使用 Block

Objective-C 类定义的对象会把数据和相关行为结合在一起。不过有时候，你想表达的只是单个任务或行为单元，而不是一组方法的集合，这样做才更合适。

Block 是添加到 C、Objective-C 和 C++ 中的一种语言级特性，它让你可以创建独立的代码段，并像值一样把它们传递给方法或函数。Block 是 Objective-C 对象，这意味着它们可以被加入 `NSArray` 或 `NSDictionary` 这样的集合中。它们还能够捕获所在作用域中的值，这一点让它们与其他编程语言中的_闭包（closure）_或 _lambda_ 很相似。

本章讲解声明和引用 block 的语法，并说明如何用 block 简化常见任务，比如集合枚举。要了解更多信息，请参阅 _[Blocks 编程主题](../Blocks%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tkmbs)_。

定义 block 字面量的语法使用插入符号（`^`），就像这样：

```objc
    ^{
         NSLog(@"This is a block");
    }
```

和函数、方法定义一样，花括号标示 block 的起止。在这个例子中，该 block 不返回任何值，也不接受任何参数。

就像你可以用函数指针来引用一个 C 函数一样，你也可以声明一个变量来保存 block，就像这样：

```objc
    void (^simpleBlock)(void);
```

如果你不习惯处理 C 的函数指针，这种语法可能会显得有点儿不寻常。这个例子声明了一个名为 `simpleBlock` 的变量，用来引用一个不接受参数、也不返回值的 block，这意味着可以把上面展示的 block 字面量赋值给这个变量，就像这样：

```objc
    simpleBlock = ^{
        NSLog(@"This is a block");
    };
```

这与其他任何变量赋值一样，因此语句必须以右花括号后跟一个分号结束。你也可以把变量声明和赋值合并在一起：

```objc
    void (^simpleBlock)(void) = ^{
        NSLog(@"This is a block");
    };
```

声明并赋值一个 block 变量之后，你就可以用它来调用该 block：

```objc
    simpleBlock();
```


Block 也可以像方法和函数一样接受参数并返回值。

举个例子，考虑一个变量，它引用一个返回两个值相乘结果的 block：

```objc
    double (^multiplyTwoValues)(double, double);
```

对应的 block 字面量可能是这样的：

```objc
    ^ (double firstValue, double secondValue) {
        return firstValue * secondValue;
    }
```

`firstValue` 和 `secondValue` 用来引用 block 被调用时传入的值，就像任何函数定义一样。在这个例子中，返回类型是根据 block 内部的 return 语句推断出来的。

如果你愿意，也可以在插入符号和参数列表之间指定返回类型，让它显式化：

```objc
    ^ double (double firstValue, double secondValue) {
        return firstValue * secondValue;
    }
```

声明并定义好 block 之后，你就可以像调用函数一样调用它：

```objc
    double (^multiplyTwoValues)(double, double) =
                              ^(double firstValue, double secondValue) {
                                  return firstValue * secondValue;
                              };

    double result = multiplyTwoValues(2,4);

    NSLog(@"The result is %f", result);
```


除了包含可执行代码之外，block 还有能力从其所在的作用域捕获状态。

举例来说，如果你在一个方法内部声明一个 block 字面量，就可以捕获该方法作用域内可以访问的任何值，就像这样：

```objc
- (void)testMethod {
    int anInteger = 42;

    void (^testBlock)(void) = ^{
        NSLog(@"Integer is: %i", anInteger);
    };

    testBlock();
}
```

在这个例子中，`anInteger` 是在 block 外部声明的，但它的值会在 block 定义时被捕获。

默认情况下只有值会被捕获，除非你另行指定。这意味着，如果你在定义 block 之后、调用它之前改变了这个变量在外部的值，就像这样：

```objc
    int anInteger = 42;

    void (^testBlock)(void) = ^{
        NSLog(@"Integer is: %i", anInteger);
    };

    anInteger = 84;

    testBlock();
```

block 捕获到的值不会受到影响。也就是说，日志输出仍然会显示：

```
Integer is: 42
```

这也意味着 block 无法改变原始变量的值，甚至无法改变被捕获的这个值（它是作为 `const` 变量被捕获的）。

如果你需要在 block 内部改变被捕获变量的值，可以在原始变量声明上使用 `__block` 存储类型修饰符。这意味着该变量存储在一块共享的存储空间里，这块空间由原始变量所在的词法作用域和该作用域内声明的所有 block 共享。

举个例子，你可以把前面的例子改写成这样：

```objc
    __block int anInteger = 42;

    void (^testBlock)(void) = ^{
        NSLog(@"Integer is: %i", anInteger);
    };

    anInteger = 84;

    testBlock();
```

因为 `anInteger` 被声明为 `__block` 变量，它的存储空间与 block 声明是共享的。这意味着日志输出现在会显示：

```
Integer is: 84
```

这也意味着 block 可以修改原始值，就像这样：

```objc
    __block int anInteger = 42;

    void (^testBlock)(void) = ^{
        NSLog(@"Integer is: %i", anInteger);
        anInteger = 100;
    };

    testBlock();
    NSLog(@"Value of original variable is now: %i", anInteger);
```

这一次，输出会显示：

```
Integer is: 42
Value of original variable is now: 100
```


本章前面的每个例子都是在 block 定义之后立即调用它。而在实践中，更常见的做法是把 block 传给函数或方法，在别处调用。举例来说，你可能会用 Grand Central Dispatch 在后台调用一个 block，或者定义一个 block 来表示需要重复调用的任务，比如枚举一个集合时。并发和枚举将在本章后面介绍。

Block 也用于回调，也就是用来定义任务完成时要执行的代码。举例来说，你的 app 可能需要响应用户的操作，创建一个执行复杂任务的对象，比如向 Web 服务请求信息。因为这个任务可能耗时较长，你应该在任务进行期间显示某种进度指示，任务完成后再把它隐藏起来。

用委托来实现这一点也是可行的：你需要创建一个合适的委托协议，实现所需的方法，把你的对象设为该任务的委托，然后等待任务完成后调用你对象上的委托方法。

不过，用 block 来做这件事要简单得多，因为你可以在发起任务的同时定义回调行为，就像这样：

```objc
- (IBAction)fetchRemoteInformation:(id)sender {
    [self showProgressIndicator];

    XYZWebTask *task = ...

    [task beginTaskWithCallbackBlock:^{
        [self hideProgressIndicator];
    }];
}
```

这个例子调用一个方法来显示进度指示，然后创建任务并让它开始执行。回调 block 指定了任务完成后要执行的代码；在这个例子中，它只是调用一个方法来隐藏进度指示。注意，这个回调 block 捕获了 `self`，这样才能在被调用时调用 `hideProgressIndicator` 方法。捕获 `self` 时要格外小心，因为很容易造成强引用循环，具体说明见后文的[捕获 self 时避免强引用循环](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqobnknltcnq)。

从代码可读性的角度来说，block 让你可以在一处清楚地看到任务完成前后将要发生的事情，不必再去追踪委托方法才能弄清楚接下来会发生什么。

这个例子中展示的 `beginTaskWithCallbackBlock:` 方法的声明大概是这样的：

```objc
- (void)beginTaskWithCallbackBlock:(void (^)(void))callbackBlock;
```

`(void (^)(void))` 表示该参数是一个不接受任何参数、也不返回任何值的 block。方法的实现可以按通常的方式调用这个 block：

```objc
- (void)beginTaskWithCallbackBlock:(void (^)(void))callbackBlock {
    ...
    callbackBlock();
}
```

期望接受一个或多个参数的 block 的方法参数，其声明方式与 block 变量相同：

```objc
- (void)doSomethingWithBlock:(void (^)(double, double))block {
    ...
    block(21.0, 2.0);
}
```


最佳实践是一个方法只使用一个 block 参数。如果该方法还需要其他非 block 参数，block 应该放在最后：

```objc
- (void)beginTaskWithName:(NSString *)name completion:(void(^)(void))callback;
```

这样一来，以内联方式指定 block 时，方法调用会更容易阅读，就像这样：

```objc
    [self beginTaskWithName:@"MyTask" completion:^{
        NSLog(@"The task is complete");
    }];
```


如果你需要定义多个具有相同签名的 block，不妨为该签名定义一个自己的类型。

举个例子，你可以为一个不接受参数、也没有返回值的简单 block 定义一个类型，就像这样：

```objc
typedef void (^XYZSimpleBlock)(void);
```

然后你就可以把自定义类型用于方法参数，或者用来创建 block 变量：

```objc
    XYZSimpleBlock anotherBlock = ^{
        ...
    };
```

```objc
- (void)beginFetchWithCallbackBlock:(XYZSimpleBlock)callbackBlock {
    ...
    callbackBlock();
}
```

当你需要处理返回 block、或者以其他 block 作为参数的 block 时，自定义类型定义会特别有用。看看下面这个例子：

```objc
void (^(^complexBlock)(void (^)(void)))(void) = ^ (void (^aBlock)(void)) {
    ...
    return ^{
        ...
    };
};
```

`complexBlock` 变量引用的是一个 block，它接受另一个 block 作为参数（`aBlock`），并返回另外一个 block。

把这段代码改写成使用类型定义，可读性会大大提升：

```objc
XYZSimpleBlock (^betterBlock)(XYZSimpleBlock) = ^ (XYZSimpleBlock aBlock) {
    ...
    return ^{
        ...
    };
};
```


声明一个用来保存 block 的属性，其语法与 block 变量类似：

```objc
@interface XYZObject : NSObject
@property (copy) void (^blockProperty)(void);
@end
```

block 属性的设置和调用方式与任何其他 block 变量相同：

```objc
    self.blockProperty = ^{
        ...
    };
    self.blockProperty();
```

block 属性声明也同样可以使用类型定义，就像这样：

```objc
typedef void (^XYZSimpleBlock)(void);

@interface XYZObject : NSObject
@property (copy) XYZSimpleBlock blockProperty;
@end
```


如果你需要在 block 中捕获 `self`，比如定义一个回调 block 时，就需要认真考虑内存管理方面的影响。

Block 会对所有被捕获的对象保持强引用，包括 `self`，这意味着如果某个对象持有一个 `copy` 属性来保存捕获了 `self` 的 block，就很容易形成强引用循环：

```objc
@interface XYZBlockKeeper : NSObject
@property (copy) void (^block)(void);
@end
```

```objc
@implementation XYZBlockKeeper
- (void)configureBlock {
    self.block = ^{
        [self doSomething];    // 捕获对 self 的强引用，
                               // 会造成强引用循环
    };
}
...
@end
```

对于这样一个简单的例子，编译器会给出警告，但更复杂的例子可能涉及多个对象之间的多重强引用才形成循环，这会让问题更难以诊断。

为了避免这个问题，最佳实践是捕获一个指向 `self` 的弱引用，就像这样：

```objc
- (void)configureBlock {
    XYZBlockKeeper * __weak weakSelf = self;
    self.block = ^{
        [weakSelf doSomething];   // 捕获弱引用，
                                  // 从而避免引用循环
    }
}
```

通过捕获指向 `self` 的弱指针，block 就不会再对 `XYZBlockKeeper` 对象保持强关联。如果该对象在 block 被调用之前就已经被释放，`weakSelf` 指针只会被简单地设为 `nil`。

除了通用的完成回调之外，许多 Cocoa 和 Cocoa Touch API 都使用 block 来简化常见任务，比如集合枚举。举例来说，`NSArray` 类就提供了三个基于 block 的方法，包括：

```objc
- (void)enumerateObjectsUsingBlock:(void (^)(id obj, NSUInteger idx, BOOL *stop))block;
```

这个方法只接受一个参数，也就是一个会针对数组中每一项调用一次的 block：

```objc
    NSArray *array = ...
    [array enumerateObjectsUsingBlock:^ (id obj, NSUInteger idx, BOOL *stop) {
        NSLog(@"Object at index %lu is %@", idx, obj);
    }];
```

block 本身接受三个参数，前两个分别是当前对象及其在数组中的索引。第三个参数是一个指向布尔变量的指针，你可以用它来停止枚举，就像这样：

```objc
    [array enumerateObjectsUsingBlock:^ (id obj, NSUInteger idx, BOOL *stop) {
        if (...) {
            *stop = YES;
        }
    }];
```

你还可以通过 `enumerateObjectsWithOptions:usingBlock:` 方法来定制枚举行为。举例来说，指定 `NSEnumerationReverse` 选项会让集合按逆序遍历。

如果枚举 block 中的代码对处理器负担较重——并且可以安全地并发执行——你可以使用 `NSEnumerationConcurrent` 选项：

```objc
    [array enumerateObjectsWithOptions:NSEnumerationConcurrent
                            usingBlock:^ (id obj, NSUInteger idx, BOOL *stop) {
        ...
    }];
```

这个标志表示枚举 block 的调用可能会被分派到多个线程上执行，如果 block 代码对处理器负担特别重，这样做可能带来性能提升。注意，使用这个选项时枚举的顺序是不确定的。

`NSDictionary` 类也提供了基于 block 的方法，包括：

```objc
    NSDictionary *dictionary = ...
    [dictionary enumerateKeysAndObjectsUsingBlock:^ (id key, id obj, BOOL *stop) {
        NSLog(@"key: %@, value: %@", key, obj);
    }];
```

与使用传统循环相比，这样枚举每个键值对会更方便。

block 代表一个独立的工作单元，把可执行代码和从周围作用域中捕获的可选状态结合在一起。这使它非常适合用 OS X 和 iOS 提供的并发选项之一进行异步调用。你不必再去搞清楚如何使用线程这样的底层机制，只需用 block 定义你的任务，然后让系统在处理器资源可用时去执行这些任务。

OS X 和 iOS 提供了多种并发相关的技术，其中包括两种任务调度机制：操作队列和 Grand Central Dispatch。这些机制都围绕着一个等待被调用的任务队列这一理念展开。你按需要的调用顺序把 block 加入队列，系统会在处理器时间和资源可用时把它们从队列中取出并调用。

_串行队列（serial queue）_一次只允许一个任务执行——队列中的下一个任务要等到前一个任务完成后才会被取出并调用。_并发队列（concurrent queue）_则会尽可能多地调用任务，而不必等待前面的任务完成。

操作队列是 Cocoa 和 Cocoa Touch 处理任务调度的方式。你创建一个 `NSOperation` 实例，把一个工作单元连同所需的数据封装起来，然后把这个操作加入 `NSOperationQueue` 以供执行。

虽然你可以创建自己的 `NSOperation` 子类来实现复杂任务，但你也可以使用 `NSBlockOperation` 通过 block 来创建一个操作，就像这样：

```objc
NSBlockOperation *operation = [NSBlockOperation blockOperationWithBlock:^{
    ...
}];
```

手动执行一个操作也是可行的，但操作通常会被添加到一个已有的操作队列，或者你自己创建的队列中，等待执行：

```objc
// 在主队列上调度任务：
NSOperationQueue *mainQueue = [NSOperationQueue mainQueue];
[mainQueue addOperation:operation];

// 在后台队列上调度任务：
NSOperationQueue *queue = [[NSOperationQueue alloc] init];
[queue addOperation:operation];
```

如果你使用操作队列，就可以配置操作之间的优先级或依赖关系，比如指定某个操作要等到一组其他操作全部完成之后才能执行。你还可以通过键值观察来监控操作状态的变化，这样一来，比如在任务完成时更新进度指示就会很方便。

关于操作和操作队列的更多信息，请参阅[操作队列](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/OperationObjects/OperationObjects.html#//apple_ref/doc/uid/TP40008091-CH101)。

如果你需要调度任意一段代码去执行，可以直接使用由 Grand Central Dispatch（GCD）控制的_派发队列（dispatch queue）_。派发队列让你可以方便地相对于调用者同步或异步地执行任务，并按先进先出的顺序执行这些任务。

你既可以创建自己的派发队列，也可以使用 GCD 自动提供的队列之一。举例来说，如果你需要调度一个任务以并发执行，可以使用 `dispatch_get_global_queue()` 函数并指定一个队列优先级，来获取一个已有队列的引用，就像这样：

```objc
dispatch_queue_t queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
```

要把 block 派发到队列，可以使用 `dispatch_async()` 或 `dispatch_sync()` 函数。`dispatch_async()` 函数会立即返回，不会等待 block 被调用：

```objc
dispatch_async(queue, ^{
    NSLog(@"Block for asynchronous execution");
});
```

`dispatch_sync()` 函数要等到 block 执行完成后才会返回；举例来说，你可能会在并发 block 需要等待主线程上的另一个任务完成之后才能继续时用到它。

关于派发队列和 GCD 的更多信息，请参阅[派发队列](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/OperationQueues/OperationQueues.html#//apple_ref/doc/uid/TP40008091-CH102)。

[下一页](Dealing%20with%20Errors.md)[上一页](Values%20and%20Collections.md)

