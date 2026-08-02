---
title: Block 编程主题
apple_id: TP40007502
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Blocks/Articles/bxGettingStarted.html
archived_at: '2026-07-15T07:11:18.897846Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Block 编程主题](Introduction.md)


[下一页](Conceptual%20Overview.md)[上一页](Introduction.md)

# Block 入门

下面几节通过实际示例帮助你上手 block。

你用 `^` 运算符声明 block 变量，同时它也标志着一个 block 字面量的开始。block 自身的主体包含在 `{}` 中，如下面这个示例所示（和 C 语言的惯例一样，`;` 表示语句结束）：

```c
int multiplier = 7;
int (^myBlock)(int) = ^(int num) {
    return num * multiplier;
};
```

下图对这个示例作了说明：

![../Art/blocks.jpg](attachments/Art/blocks.jpg)

注意，block 能够使用其定义所在的那个作用域中的变量。

如果你把 block 声明为一个变量，就可以像使用函数那样使用它：

```c
int multiplier = 7;
int (^myBlock)(int) = ^(int num) {
    return num * multiplier;
};

printf("%d", myBlock(3));
// 输出 "21"
```


在很多情况下，你并不需要声明 block 变量；只要在需要把它作为实参传入的地方直接内联写一个 block 字面量就可以了。下面的示例使用了 `qsort_b` 函数。`qsort_b` 与标准的 `qsort_r` 函数类似，但它的最后一个实参是一个 block。

```c
char *myCharacters[3] = { "TomJohn", "George", "Charles Condomine" };

qsort_b(myCharacters, 3, sizeof(char *), ^(const void *l, const void *r) {
    char *left = *(char **)l;
    char *right = *(char **)r;
    return strncmp(left, right, 1);
});

// myCharacters 现在是 { "Charles Condomine", "George", "TomJohn" }
```


[Cocoa](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Cocoa.html#//apple_ref/doc/uid/TP40008195-CH9) [框架](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56)中有若干方法接受 block 作为实参，通常用来对一组对象执行某项操作，或者在某项操作完成后作为回调使用。下面的示例展示了如何配合 `NSArray` 的 [sortedArrayUsingComparator:](https://developer.apple.com/documentation/foundation/nsarray/1411195-sortedarray) 方法使用 block。该方法只接受一个实参——block。为便于说明，这里把 block 定义为一个 [NSComparator](https://developer.apple.com/documentation/foundation/nscomparator) 类型的局部变量：

```objc
NSArray *stringsArray = @[ @"string 1",
                           @"String 21",
                           @"string 12",
                           @"String 11",
                           @"String 02" ];

static NSStringCompareOptions comparisonOptions = NSCaseInsensitiveSearch | NSNumericSearch |
        NSWidthInsensitiveSearch | NSForcedOrderingSearch;
NSLocale *currentLocale = [NSLocale currentLocale];

NSComparator finderSortBlock = ^(id string1, id string2) {

    NSRange string1Range = NSMakeRange(0, [string1 length]);
    return [string1 compare:string2 options:comparisonOptions range:string1Range locale:currentLocale];
};

NSArray *finderSortArray = [stringsArray sortedArrayUsingComparator:finderSortBlock];
NSLog(@"finderSortArray: %@", finderSortArray);

/*
输出：
finderSortArray: (
    "string 1",
    "String 02",
    "String 11",
    "string 12",
    "String 21"
)
*/
```


block 的一项强大特性是它们可以修改同一词法作用域（lexical scope）中的变量。你通过 `__block` 存储类型修饰符来表明某个变量可以被 block 修改。把 [在 Cocoa 中使用 Block](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tkmbsfvbuqnznknlti) 中的示例改造一下，就可以用一个 block 变量来统计有多少个字符串被判定为相等，如下面的示例所示。为便于说明，这里直接使用了 block，并把 `currentLocale` 当作 block 内部的只读变量来用：

```objc
NSArray *stringsArray = @[ @"string 1",
                          @"String 21", // <-
                          @"string 12",
                          @"String 11",
                          @"Strîng 21", // <-
                          @"Striñg 21", // <-
                          @"String 02" ];

NSLocale *currentLocale = [NSLocale currentLocale];
__block NSUInteger orderedSameCount = 0;

NSArray *diacriticInsensitiveSortArray = [stringsArray sortedArrayUsingComparator:^(id string1, id string2) {

    NSRange string1Range = NSMakeRange(0, [string1 length]);
    NSComparisonResult comparisonResult = [string1 compare:string2 options:NSDiacriticInsensitiveSearch range:string1Range locale:currentLocale];

    if (comparisonResult == NSOrderedSame) {
        orderedSameCount++;
    }
    return comparisonResult;
}];

NSLog(@"diacriticInsensitiveSortArray: %@", diacriticInsensitiveSortArray);
NSLog(@"orderedSameCount: %d", orderedSameCount);

/*
输出：

diacriticInsensitiveSortArray: (
    "String 02",
    "string 1",
    "String 11",
    "string 12",
    "String 21",
    "Str\U00eeng 21",
    "Stri\U00f1g 21"
)
orderedSameCount: 2
*/
```

关于这一点，[Block 与变量](Blocks%20and%20Variables.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tkmbsfvbuqnrnknltc) 中有更详细的讨论。

[下一页](Conceptual%20Overview.md)[上一页](Introduction.md)

