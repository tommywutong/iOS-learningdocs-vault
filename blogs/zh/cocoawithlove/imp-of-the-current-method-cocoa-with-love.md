---
title: '当前方法的 IMP | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/02/imp-of-current-method.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:002349661d70e986'
translated: true
---

> 原文：[IMP of the current method | Cocoa with Love](https://www.cocoawithlove.com/2008/02/imp-of-current-method.html)　·　Cocoa with Love (Matt Gallagher)

我想让这个新博客以一种别处几乎见不到的内容开篇。这是一个用来访问 Objective-C 一项基础数据的冷门 hack。

## 不是个简单问题

> “如何找到当前方法的 IMP？”

本节标题没有说谎，这确实不是个简单问题。Objective-C（这门语言以能在运行时（runtime）查到任何东西而著称）没有任何能直接访问这个值的变量、函数、运算符或标识符。

务实的读者可能会问：“我为什么要关心这个？”

说实话，这些读者别再为难人了。这篇博客我才写了 7 句话，他们就已经开始给我找麻烦了。正如 George Mallory 那句名言所说：“因为山在那里”。的确，山确实在那里，而它也最终要了他的命。

如果这仍然不足以说服你，那么我承诺在以后的文章中给出一个理由 _[**编者注**：请看[这篇后续文章](https://www.cocoawithlove.com/2008/03/supersequent-implementation.html)]_。我现在暂且留着不说，因为我想留住回头读者，也想继续写这篇文章。

## 什么是 IMP？

IMP 是 “implementation”（实现）的缩写。它是一个代码块起始处的内存地址，这个代码块实现了一个 Method。如有需要，它可以像 C 函数一样被调用。不过通常的做法是：你向 Objective-C 对象发送一条消息（message），Objective-C 运行时会找到与该消息关联的 Method，并替你调用相应的 IMP。

不过在少数情况下，你可能想绕开典型的 “[object method:parameter];” 语法和 objc_msgSend() 函数。在这些情况下，你需要直接调用 IMP。这正是它的用处所在，也是你可能希望直接访问它的原因。

## Objective-C 运行时数据中的 IMP

在 Objective-C 中，程序里每个类的每个方法都有一个在运行时为它构建的数据结构。在 Objective-C 2.0 中，这个结构是官方意义上的“不透明”（opaque）的（它仍然存在，只是你要通过函数来访问其内容，而不是直接访问）。

我们来看看 Method 结构里都包含什么……

```objc
struct objc_method
{
  SEL method_name;
  char * method_types;
  IMP method_imp;
};
typedef objc_method Method;
```

这样看来，方法有 3 个属性：

- method_name 描述方法的签名（signature）；它的值由所有名称和参数名相同的方法共享
- method_types 描述方法参数的类型。
- method_imp 是函数指针（function pointer），即这个方法被选中执行时所调用代码的地址。

我们要费心去找的正是这个 “method_imp”。方法的 IMP 就是它代码的地址，也称为它的函数指针。

## 那么问题出在哪里？

看起来，获取当前方法的 IMP 应该很容易。每个方法都有一个 self 参数和一个很少用到的 _cmd 参数，利用它们我们可以这样调用：

```objc
[(NSObject *)[self class] instanceMethodForSelector:_cmd];
```

只不过，这样返回的永远只是 _默认_ 的 IMP。

像 _cmd 这样的选择器（selector）并不唯一；它们被每一次方法重写所共享，所以如果一个类层次（class hierarchy）在多个深度上都有与 _cmd 对应的实现，你就无法区分它们。

这是 Objective-C 设计者有意为之的。类层次的构造本就应当决定：对于给定的 SEL，你得到的是哪个 IMP。

我在这里有点吹毛求疵：我想访问的是当前这个 Method 的实现，而不管它是不是默认的那个。

别误会：如果你 _确实_ 想要的是默认 IMP（这很可能是常见情况），你 _应该_ 使用 +[NSObject instanceMethodForSelector:] 或某个类似的方法或函数。不过，本文关注的是你想要某个特定 IMP（不一定是默认那个）的情况。

## 难道不能像在 C 里那样直接引用函数吗？

在纯 C 中，获取等价于 IMP 的东西很容易，如下例所示：

```objc
void myFunction()
{
   void *myImplementation = myFunction;
  
   ...
}
```

在 C 中，获取当前函数的函数指针很容易：只要把函数名当作标识符使用即可（函数名在自己的函数体内始终处于作用域之内）。

曾经有一段时间，Objective-C 也同样简单。那时你可以通过方法的修饰名（mangled name）来引用它。像这样：

```objc
- (void)myMethodWithParam1:(int)someParameter andParam2:(int)otherParameter
{
   void *myImplementation = _i_MyClass_MyCategory_myMethodWithParam1_andParam2_;
  
   ...
}
```

那个时代早已远去，修饰名也不再可用。那么，怎样才能拿到你所在函数起始处的地址呢？

## 解决方案

我的解决方案从一个鲜为人知的 GCC “内建”（built-in）函数开始。

```objc
__builtin_return_address(0)
```

这个函数给出的是当前栈帧（stack frame）的返回地址（return address）。你可以传入零以外的数字（以获取其他栈帧），但只有零能保证有效。

可是，进入函数中部的返回地址并不等于指向函数起始处的 IMP，这有什么帮助呢？

其实，我们知道：

- Method 的实现是连续的
- 在目标 Method 实现的某个子函数（child function）中调用 __builtin_return_address(0)，得到的结果将是位于目标实现内部某处的一个地址

把这两个事实结合起来就可以保证：如果我们在某个 Method 实现的子函数中调用 __builtin_return_address(0)，那么该 Method 实现的 IMP 必定是程序中在 __builtin_return_address(0) 结果之前、距离它最近的那个 IMP。

由于我们可以通过方法的 “self” 参数取得一个 Class 的全部 Method IMP 集合，我们现在就有了解决问题的思路：

1. 在目标 Method 的一次调用期间，
2. 把该方法中的 self 和 _cmd 传入我们的“查找 IMP”函数。
3. 在这个函数内部，从对象的类及其超类中取出所有 Method 的集合。
4. 调用 __builtin_return_address(0) 并保存其结果。
5. 在这个集合中找出这样的 Method：其 method_name 等于 _cmd，且其 method_imp 是最接近 __builtin_return_address(0) 的结果而又不超过它的那个。
6. 这个最接近的 method_imp 就是目标 Method 的 IMP。

下面就是代码：

```objc
#import &lt;objc/objc-class.h&gt;
IMP impOfCallingMethod(id lookupObject, SEL selector)
{
    NSUInteger returnAddress = (NSUInteger)__builtin_return_address(0);
    NSUInteger closest = 0;
    
    // 遍历该类及其所有超类
    Class currentClass = object_getClass(lookupObject);
    while (currentClass)
    {
        // 遍历这个类的所有实例方法
        unsigned int methodCount;
        Method *methodList = class_copyMethodList(currentClass, &methodCount);
        unsigned int i;
        for (i = 0; i < methodCount; i++)
        {
            // 忽略选择器不同的方法
            if (method_getName(methodList[i]) != selector)
            {
                continue;
            }
            
            // 如果这个地址更近，就改用它
            NSUInteger address = (NSUInteger)method_getImplementation(methodList[i]);
            if (address &lt; returnAddress &amp;&amp; address &gt; closest)
            {
                closest = address;
            }
        }
    
        free(methodList);
        currentClass = class_getSuperclass(currentClass);
    }
    
    return (IMP)closest;
}
```

这段代码相当直白：遍历由各个 Class 构成的类层次，以及这些 Class 上的各个 Method（忽略与我们选择器不对应的 Method），并追踪位于 __builtin_return_address(0) 结果之前、距离它最近的 IMP。

现在我们可以这样调用它：

```objc
- (void)myMethodWithParam1:(int)someParameter andParam2:(int)otherParameter
{
   void *myImplementation = impOfCallingInstanceMethod([self class], _cmd);
  
   ...
}
```

## 总结

我喜欢能够访问程序中任何值所带来的满足感。在函数里默认就能拿到方法的选择器和当前对象，这固然可以，但语义含糊。知道自己能够取回 IMP，会让事情显得更整洁。

这种做法确实需要遍历当前类的类层次中的所有方法。严格来说，更快的做法是：直接从当前函数（而不是子函数）读取返回地址，再从那个位置开始反向遍历指令，找到调用当前函数的那条 “call” 或等价指令。这做起来会很棘手，而且与具体平台相关。

有人有兴趣试试吗？
