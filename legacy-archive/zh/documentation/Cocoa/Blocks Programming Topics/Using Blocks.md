---
title: Block 编程主题
apple_id: TP40007502
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Blocks/Articles/bxUsing.html
archived_at: '2026-07-15T07:11:19.260976Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Block 编程主题](Introduction.md)


[下一页](Document%20Revision%20History.md)[上一页](Blocks%20and%20Variables.md)

# 使用 Block

如果你把 block 声明为一个变量，就可以像使用函数那样使用它，如下面这两个示例所示：

```c
int (^oneFrom)(int) = ^(int anInt) {
    return anInt - 1;
};

printf("1 from 10 is %d", oneFrom(10));
// 输出 "1 from 10 is 9"

float (^distanceTraveled)(float, float, float) =
                         ^(float startingSpeed, float acceleration, float time) {

    float distance = (startingSpeed * time) + (0.5 * acceleration * time * time);
    return distance;
};

float howFar = distanceTraveled(0.0, 9.8, 1.0);
// howFar = 4.9
```

不过更常见的做法是把 block 作为实参传给函数或方法。这种情况下，你通常会“内联”创建 block。

你可以像传递任何其他实参那样把 block 作为函数实参传入。但在很多情况下，你并不需要声明 block；只要在需要它作为实参的地方直接内联实现就可以了。下面的示例使用了 `qsort_b` 函数。`qsort_b` 与标准的 `qsort_r` 函数类似，但它的最后一个实参是一个 block。

```c
char *myCharacters[3] = { "TomJohn", "George", "Charles Condomine" };

qsort_b(myCharacters, 3, sizeof(char *), ^(const void *l, const void *r) {
    char *left = *(char **)l;
    char *right = *(char **)r;
    return strncmp(left, right, 1);
});
// block 实现在 "}" 处结束

// myCharacters 现在是 { "Charles Condomine", "George", "TomJohn" }
```

注意，block 是包含在函数的实参列表之内的。

下一个示例展示如何配合 `dispatch_apply` 函数使用 block。`dispatch_apply` 的声明如下：

```c
void dispatch_apply(size_t iterations, dispatch_queue_t queue, void (^block)(size_t));
```

该函数把一个 block 提交给某个派发队列，以便多次调用。它接受三个实参：第一个指定要执行的迭代次数；第二个指定 block 提交到的队列；第三个就是 block 本身，而该 block 又接受一个实参——当前的迭代索引。

你可以非常简单地用 `dispatch_apply` 来打印迭代索引，如下所示：

```c
#include <dispatch/dispatch.h>
size_t count = 10;
dispatch_queue_t queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);

dispatch_apply(count, queue, ^(size_t i) {
    printf("%u\n", i);
});
```


[Cocoa](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Cocoa.html#//apple_ref/doc/uid/TP40008195-CH9) 提供了不少使用 block 的方法。你可以像传递任何其他实参那样把 block 作为方法实参传入。

下面的示例找出数组前五个元素中出现在给定过滤集合里的那些元素的索引。

```objc
NSArray *array = @[@"A", @"B", @"C", @"A", @"B", @"Z", @"G", @"are", @"Q"];
NSSet *filterSet = [NSSet setWithObjects: @"A", @"Z", @"Q", nil];

BOOL (^test)(id obj, NSUInteger idx, BOOL *stop);

test = ^(id obj, NSUInteger idx, BOOL *stop) {

    if (idx < 5) {
        if ([filterSet containsObject: obj]) {
            return YES;
        }
    }
    return NO;
};

NSIndexSet *indexes = [array indexesOfObjectsPassingTest:test];

NSLog(@"indexes: %@", indexes);

/*
输出：
indexes: <NSIndexSet: 0x10236f0>[number of indexes: 2 (in 2 ranges), indexes: (0 3)]
*/
```

下面的示例判断一个 `NSSet` 对象是否包含某个局部变量所指定的单词，如果包含，就把另一个局部变量（`found`）的值设为 `YES`（并停止搜索）。注意 `found` 也被声明为 `__block` 变量，而且 block 是内联定义的：

```objc
__block BOOL found = NO;
NSSet *aSet = [NSSet setWithObjects: @"Alpha", @"Beta", @"Gamma", @"X", nil];
NSString *string = @"gamma";

[aSet enumerateObjectsUsingBlock:^(id obj, BOOL *stop) {
    if ([obj localizedCaseInsensitiveCompare:string] == NSOrderedSame) {
        *stop = YES;
        found = YES;
    }
}];

// 此时，found == YES
```


通常来说，你不需要拷贝（或保留）一个 block。只有当你预期该 block 在其声明所在的作用域被销毁之后仍会被使用时，才需要做一次拷贝。拷贝会把 block 移到堆上。

你可以用以下 C 函数来拷贝和释放 block：

```c
Block_copy();
Block_release();
```

为避免内存泄漏，你必须始终让每一次 `Block_copy()` 都与一次 `Block_release()` 配对。

一个 block 字面量（也就是 `^{ ... }`）是一个表示该 block 的_栈上局部_数据结构的地址。因此这个栈上局部数据结构的作用域就是它所在的外围复合语句，所以你应当_避免_下面示例中展示的这些写法：

```c
void dontDoThis() {
    void (^blockArray[3])(void);  // 一个含有 3 个 block 引用的数组

    for (int i = 0; i < 3; ++i) {
        blockArray[i] = ^{ printf("hello, %d\n", i); };
        // 错误：block 字面量的作用域是这个 "for" 循环。
    }
}

void dontDoThisEither() {
    void (^block)(void);

    int i = random():
    if (i > 1000) {
        block = ^{ printf("got i at: %d\n", i); };
        // 错误：block 字面量的作用域是这个 "then" 分支。
    }
    // ...
}
```


你可以设置断点，并单步进入 block。你可以在 GDB 会话中用 `invoke-block` 调用一个 block，如下面这个示例所示：

```
$ invoke-block myBlock 10 20
```

如果你想传入一个 C 字符串，必须给它加上引号。例如，若要把 `this string` 传给 `doSomethingWithString` 这个 block，你应该这样写：

```
$ invoke-block doSomethingWithString "\"this string\""
```

[下一页](Document%20Revision%20History.md)[上一页](Blocks%20and%20Variables.md)

