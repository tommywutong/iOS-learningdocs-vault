---
title: iOS block底层原理分析(1)--循环引用
source_url: 'https://www.jianshu.com/p/809a9bca597f'
source_domain: jianshu.com
source_group: platform
original_language: zh
published: 2021-10-13
archived_at: 2026-07-27
content_hash: 'sha256:9228ea057d151c33'
plan_ref: 第二周：weak、属性关键字与 Block / Day 5｜循环引用是 Day 4 所有权图的推论（对应 W2-14、W2-16）
plan_week: 第二周：weak、属性关键字与 Block
plan_day: Day 5｜循环引用是 Day 4 所有权图的推论（对应 W2-14、W2-16）
container: //article
container_source: map
---

> 原文：[iOS block底层原理分析(1)--循环引用](https://www.jianshu.com/p/809a9bca597f)

## 准备工作

[weak实现原理](https://www.jianshu.com/p/1b566137b3fe)

## 1. block的分类

`block`的分类主要分为以下的三种：

- `__NSGlobalBlock__ 全局block`
- `__NSStackBlock__ 栈区block`
- `__NSMallocBlock__ 堆区block`

**`block`在`MRC`和`ARC`环境出现的情况：**

- **`MRC`环境下**  
   引入以下的案例：

```
    void(^block)(void);
    int aa = 0;

    NSLog(@"\n********A**********");

    void (^blockA)(void) = ^{
    };
    NSLog(@"blockA is : %@ -----retainCount : %lu", blockA, [blockA retainCount]);
    block = [blockA copy];
    NSLog(@"copy blockA is : %@ -----retainCount : %lu",  block, [blockA retainCount]);

    NSLog(@"\n********B**********");

    void (^blockB)(void) = ^{
        NSLog(@"hello aa %d", aa);
    };
    NSLog(@"blockB is : %@ -----retainCount : %lu", blockB, [blockB retainCount]);
    block = [blockB copy];
    NSLog(@"copy blockB is : %@ -----retainCount : %lu",  block, [block retainCount]);
```

运行结果如下：

运行结果

由以上的案例运行结果可知，`blockA`与`blockB`的差异只在于`有没有调用外部变量`，这点差异导致它们的`类型不同`，`存储位置不同`。

- `NSGlobalBlock`  
   `block`内部`没有引用外部变量`，`Block`类型都是`NSGlobalBlock`类型，存储于`全局数据区`，由`系统`管理其内存，`retain`、`copy`、`release`操作都无效。如果访问了外部`static`或者 `全局变量`也是这种类型。
- `NSStackBlock`  
   `block`内部引用外部变量，`retain`、`release`操作无效，存储于`栈区`，变量作用域结束时，其被系统`自动释放销毁`。
- `NSMallocBlock`  
   上例中的`[blockB copy]`操作后变量类型变为`NSMallocBlock`，支持`retain`、`release`，虽然`retainCount`始终是`1`，但内存管理器中仍然会`增加`、`减少计数`，当`引用计数为零的时候释放`。
- **`ARC`环境下**  
   引入以下的案例：

```
    void(^block)(void);
    int aa = 0;

    NSLog(@"\n********A**********");

    void (^blockA)(void) = ^{
    };
    NSLog(@"blockA is : %@ -----retainCount : %lu", blockA, CFGetRetainCount(((__bridge CFTypeRef)blockA)));
    block = [blockA copy];
    NSLog(@"copy blockA is : %@ -----retainCount : %lu",  block, CFGetRetainCount(((__bridge CFTypeRef)block)));

    NSLog(@"\n********B**********");

    void (^blockB)(void) = ^{
        NSLog(@"hello aa %d", aa);
    };
    NSLog(@"blockB is : %@ -----retainCount : %lu", blockB, CFGetRetainCount(((__bridge CFTypeRef)blockB)));
    block = [blockB copy];
    NSLog(@"copy blockB is : %@ -----retainCount : %lu",  block, CFGetRetainCount(((__bridge CFTypeRef)block)));

    NSLog(@"\n********C**********");

    void (^__weak blockC)(void) = ^{
        NSLog(@"hello aa %d", aa);
    };
    NSLog(@"blockC is : %@ -----retainCount : %lu", blockC, CFGetRetainCount(((__bridge CFTypeRef)blockC)));
    block = [blockB copy];
    NSLog(@"copy blockC is : %@ -----retainCount : %lu",  block, CFGetRetainCount(((__bridge CFTypeRef)block)));
```

运行结果如下：

运行结果

查看运行结果发现，`blockB`在`MRC`下是`NSStackBlock`类型，而在`ARC`下是`NSMallocBlock`类型。

- `NSGlobalBlock`  
   此种情况和`MRC`一样，`block`内部没有引用外部变量的，`Block`类型都是`NSGlobalBlock`类型，存储于`全局数据区`，由`系统管理其内存`，如果访问了外部`static`或者`全局变量`也是这种类型。
- `NSStackBlock`  
   访问了外部变量，但`没有强引用指向这个block`，如直接打印出来的`block`，如下：

  弱引用block
- `NSMallocBlock`  
  `ARC`环境下只要访问了`外部变量`，而且有`强引用指向该block`(或者作为函数返回值)就会`自动将__NSStackBlock类型copy到堆上`。

## 2. block的内存分析

#### 2.1 捕获外部变量引用计数案例分析

`ARC`环境，案例中定义了两个`block`，跟踪`objc`的引用计数变化。引入相关案例如下：

```
    NSObject * objc = [NSObject alloc];
    NSLog(@"objc -----retainCount : %lu", CFGetRetainCount(((__bridge CFTypeRef)objc)));

    void (^__weak blockA)(void) = ^{
        NSLog(@"A objc -----retainCount : %lu", CFGetRetainCount(((__bridge CFTypeRef)objc)));
    };
    blockA();

    void (^blockB)(void) = ^{
        NSLog(@"B objc -----retainCount : %lu", CFGetRetainCount(((__bridge CFTypeRef)objc)));
    };
    blockB();
```

运行结果如下：

运行结果

查看运行结果看出引用计数分别是`1，2，4`，第一个是`1`应该多数人是没问题的，那么后面为什么是`2，4`呢？接着往下分析：

- 首先`objc`对象创建好之后，调用`CFGetRetainCount`函数获取引用计数，此时应该为`1`；
- `blockA`为`__weak`，也就是`没有强引用指向这个block`，并且访问了外部变量，所以是`NSStackBlock`，因为`blockA`对变量`objc`进行了捕获，并在其结构体内部创建了一个`objc`的变量，所以此时引用计数应该变成`2`；
- `blockB`是一个`NSMallocBlock`，`ARC`环境下只要访问了`外部变量`，而且有强引用指向该`block`就会自动将`__NSStackBlock`类型`copy`到堆上，所以这个过程进行了一次`block`的`copy`，所以这个地方引用计数加`2`，变为`4`。

#### 2.2 堆栈释放差异

- **`差异1`**  
   首先还是引入以下的一个案例，查看运行的情况，如下：

```
- (void)blockDemo{
    int a = 0;
    void(^__weak weakBlock)(void) = nil;
    {
        void(^__weak strongBlock)(void) = ^{
            NSLog(@"---%d", a);
        };

        weakBlock = strongBlock;
        NSLog(@"1 - %@ - %@", weakBlock,strongBlock);
    }
    weakBlock();
}
```

运行结果如下：

运行结果

可以知道案例的运行是没有出现问题的，那么结果分析如下：

- 声明了一个`weakBlock`，该`block`为`NSStackBlock`；
- 在代码块中，定义了`strongBlock`，其也为`NSStackBlock`；
- 对`weakBlock`进行了赋值，此时两个`block`均指向同一个`NSStackBlock`；
- 因为这两个`栈block`的生命周期到`blockDemo`方法运行结束，并`不会被提前释放`；
- 所以调用`weakBlock()`可以正常运行，并能够输出`a`的值。
- **`差异2`**  
   对上面的案例`strongBlock`修改成了`NSMallocBlock`，其他没有变化。如下：

```
- (void)blockDemo{
    int a = 0;
    void(^__weak weakBlock)(void) = nil;
    {
        void(^strongBlock)(void) = ^{
            NSLog(@"---%d", a);
        };
        weakBlock = strongBlock;
        NSLog(@"1 - %@ - %@", weakBlock,strongBlock);
    }
    weakBlock();
}
```

运行结果如下：

运行结果

可以知道这个案例运行是有问题的，出现了崩溃，常规办法我们用`lldb`调试看看：

lldb调试结果

结合`lldb`调试结果分析：

- `strongBlock`为`NSMallocBlock`，其生命周期范围在代码块`{}`内，也就是`出了代码块其就会被释放`；
- 在代码块中对`weakBlock`进行了赋值，`指针拷贝`，指向了对应的`NSMallocBlock`，但是并没有强引用指向这个`block`；
- 代码块执行完毕后，该`NSMallocBlock`就会`被释放`，此时`weakBlock`指向的对象已经`被释放`，形成`野指针`，所以无法正常执行。

`lldb`继续验证是否为指针拷贝，如下：

指针拷贝

如果将`weakBlock`去掉`__weak`修饰呢？请继续往下看：

去掉__weak修饰

可以知道这样子是完全没有问题的，分析如下：

- 对`weakBlock`进行了赋值时，`weakBlock`对堆中的`block`进行了`强引用`。所以代码块运行完后`不会释放`，能够正常运行。

## 3. block循环引用

众所周知，正常情况下，持有释放，按照下图的逻辑：

持有情况下

释放情况下

循环引用就是对方面持有导致对象不能正常释放，会发生`内存泄漏`，如下：

循环引用

#### 3.1 循环引用的案例

引入一个循环引用的案例如下：

```
typedef void(^TBlock)(void);

@interface ViewController ()
@property (nonatomic, strong) TBlock block;
@property (nonatomic, copy) NSString *name;
@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];

    // 循环引用
    self.name = @"Hello";
    self.block = ^(){
        NSLog(@"%@", self.name);
    };
    self.block();
}
```

这里`self`持有了`block`，`block`持有了`self`，导致循环引用。编译时`Xcode`也会给出提示，在此块中强烈捕获`self`可能会导致循环循环。

**`特殊案例`**  
 以下代码并没有引起循环引用，如下：

```
- (void)viewDidLoad {
    [super viewDidLoad];

    // 循环引用
    self.name = @"Hello";

    void(^block)(void);
    block = ^(){
        NSLog(@"%@", self.name);
    };
    block();
}
```

为什么这个案例就没有出现循环引用的状况呢？因为当前`self`，也就是`ViewController`并没有对`block`进行强持有，`block`的生命周期只在`viewDidLoad`方法内，`viewDidLoad`方法执行完，`block`就会释放。

#### 3.2 循环引用解决方法

最常用的也是我们最熟知的`_weak`。`__weak`之所以能够解决循环引用，根本原因是`__weak不会对引用计数进行操作`。

- **`weak`的使用**

```
__weak typeof(self) weakSelf = self;
```

上面的案例修改成`weak`来避免循环引用如下：

```
    // 循环引用
    self.name = @"Hello";

    __weak typeof(self) weakSelf = self;
    self.block = ^(){
        NSLog(@"%@", weakSelf.name);
    };

    self.block();
```

此时`self`持有`block`，`block`弱引用`self`，弱引用会自动变为`nil`，强持有中断，所以不会引起循环引用。

- **反面案例**  
   如果在以上的案例中修改成如下的话，会发生代码执行过程中对象被释放的情况，如下：

  反面案例

  虽然没有引起循环引用，但是`block`中延迟`2`秒钟执行任务，如果此时`ViewController`被销毁，此时`block`已经无法获取`ViewController`的属性`name`，很不合理。那么要结果这个问题需要怎么操作呢？请继续往下！
- **强弱共舞**  
   将上面的案例再改进一下：

```
    self.name = @"Hello";

    __weak typeof(self) weakSelf = self;
    self.block = ^(){
        __strong __typeof(weakSelf)strongWeak = weakSelf;

        dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(2 * NSEC_PER_SEC)), dispatch_get_main_queue(), ^{
            NSLog(@"%@", strongWeak.name);
        });
    };
    self.block();
```

运行结果如下：

运行结果

通过运行结果发现，完全解决了以上`self`中途被释放的问题，这是为什么呢？分析如下：

- 在完成`block`中的操作之后，才调用了`dealloc`方法。添加`strongWeak`之后，持有关系为：`self` -\> `block` -\> `strongWeak` -\> `weakSelf` -\> `self`。
- `weakSelf`被强引用了就`不会自动释放`，因为`strongWeak`只是一个临时变量，它的声明周期只在`block`内部，`block`执行完毕后，`strongWeak`就会释放，而弱引用`weakSelf`也会`自动释放`。
- **手动中断持有关系**  
   引入案例代码如下：

```
    self.name = @"Hello";

    __block ViewController * ctrl = self;
    self.block = ^(){
        __strong __typeof(weakSelf)strongWeak = weakSelf;

        dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(2 * NSEC_PER_SEC)), dispatch_get_main_queue(), ^{
            NSLog(@"%@", ctrl.name);
            ctrl = nil;
        });
    };
    self.block();
```

运行结果如下：

运行结果

使用`ctrl`之后，持有关系为： `self` -\> `block` -\> `ctrl` -\> `self`，`ctrl`在`block`使用完成后，被置空，至此`block`对`self`持有就解除，不构成循环引用。

- **`block`传参**  
  `block传参的方式`解决循环引用问题，见下面代码：

```
    // 循环引用
    self.name = @"Hello";
    self.block = ^(ViewController * ctrl){
        dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(2 * NSEC_PER_SEC)), dispatch_get_main_queue(), ^{
            NSLog(@"%@", ctrl.name);
        });
    };
    self.block(self);
```

将`self`作为参数参入`block`中，进行`指针拷贝`，并没有对`self`进行持有。运行结果如下：

运行结果

#### 3.3 block循环引用案例

- **静态变量持有**

```
    // staticSelf_定义：
    static ViewController *staticSelf_;

    - (void)blockWeak_static {
        __weak typeof(self) weakSelf = self;
        staticSelf_ = weakSelf;
    }
```

以上会出现循环引用，`weakSelf`虽然是弱引用，但是`staticSelf_`静态变量，并对`weakSelf`进行了持有，`staticSelf_`释放不掉，所以`weakSelf`也释放不掉！导致循环引用！

- **`__strong`持有问题**

```
- (void)block_weak_strong {

    __weak typeof(self) weakSelf = self;

    self.doWork = ^{
        __strong typeof(self) strongSelf = weakSelf;
        NSLog(@"B objc -----retainCount : %lu", CFGetRetainCount(((__bridge CFTypeRef)strongSelf)));

        weakSelf.doStudent = ^{
            NSLog(@"%@", strongSelf);
            NSLog(@"B objc -----retainCount : %lu", CFGetRetainCount(((__bridge CFTypeRef)strongSelf)));
        };

       weakSelf.doStudent();
    };

   self.doWork();
}
```

同样这个案例也会出现循环引用的情况，分析如下：

- 在`doWork`内部，`__strong typeof(self) strongSelf = weakSelf`;
- 用强引用持有了`weakSelf`，和前的情况类似，`strongSelf`的生命周期也就在`doWork`方法内;
- 这里需要注意的是，`doStudent`这个内部`block`调用了外部变量，所以他会从`栈block copy到堆`中，从而导致`strongSelf`的引用计数`增加`，`无法释放`掉，进而导致循环引用！

## 总结

这篇文章主要分析了`block`在开发过程中我们容易犯错的地方，下一篇文章我们就根据源码分析`block`底层究竟做了什么，请拭目以待！！哈哈
