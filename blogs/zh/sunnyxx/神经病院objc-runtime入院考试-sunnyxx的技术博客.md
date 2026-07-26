---
title: 神经病院objc runtime入院考试 · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2014/11/06/runtime-nuts/'
original_language: zh
published: 2014-11-06
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:d0c597ca679fcaf6'
translated: n/a
---

> 原文：[神经病院objc runtime入院考试 · sunnyxx的技术博客](http://blog.sunnyxx.com/2014/11/06/runtime-nuts/)　·　sunnyxx (孙源)

# 神经病院objc runtime入院考试

2014年11月6日

《神经病眼中的objc runtime》北京线下分享活动顺利完成，为了配合讲解编造的几个runtime考题发出来分享下：

1. 为分享内容配合讲解用，可不是为了面试别人的哦（容易被抽）
2. 这几个题分别对应了runtime中几个隐蔽的知识点，挺非主流的，没必要深究
3. 答案在本页末尾给出，有同学针对这几道题写了讲解，所以就一笔带过了
4. 分享的具体内容争取找个时间写个blog总结下

# [#神经病院objc-runtime入院考试](#神经病院objc-runtime入院考试)神经病院objc runtime入院考试

(1) 下面的代码输出什么？

```objc
@implementation Son : Father
- (id)init {
    self = [super init];
    if (self) {
        NSLog(@"%@", NSStringFromClass([self class]));
        NSLog(@"%@", NSStringFromClass([super class]));
    }
    return self;
}
@end
```

(2) 下面代码的结果？

```objc
BOOL res1 = [(id)[NSObject class] isKindOfClass:[NSObject class]];
BOOL res2 = [(id)[NSObject class] isMemberOfClass:[NSObject class]];
BOOL res3 = [(id)[Sark class] isKindOfClass:[Sark class]];
BOOL res4 = [(id)[Sark class] isMemberOfClass:[Sark class]];
```

(3) 下面的代码会？Compile Error / Runtime Crash / NSLog…?

```objc
@interface NSObject (Sark)
+ (void)foo;
@end
@implementation NSObject (Sark)
- (void)foo {
    NSLog(@"IMP: -[NSObject (Sark) foo]");
}
@end
// 测试代码
[NSObject foo];
[[NSObject new] foo];
```

(4) 下面的代码会？Compile Error / Runtime Crash / NSLog…?

```objc
@interface Sark : NSObject
@property (nonatomic, copy) NSString *name;
@end
@implementation Sark
- (void)speak {
    NSLog(@"my name's %@", self.name);
}
@end
@implementation ViewController
- (void)viewDidLoad {
    [super viewDidLoad];
    id cls = [Sark class];
    void *obj = &cls;
    [(__bridge id)obj speak];
}
@end
```

# [#答案](#答案)答案

(1) Son / Son 因为super为编译器标示符，向super发送的消息被编译成`objc_msgSendSuper`，但仍以self作为reveiver  
(2) YES / NO / NO / NO `<NSObject>`协议有一套类方法的隐藏实现，所以编译运行正常；由于NSObject meta class的父类为NSObject class，所以只有第一句为YES  
(3) 编译运行正常，两行代码都执行`-foo`。 [NSObject foo]方法查找路线为 NSObject meta class –super-\> NSObject class，和第二题知识点很相似。  
(4)编译运行正常，输出ViewController中的`self`对象。 编译运行正常，调用了`-speak`方法，由于

```objc
id cls = [Sark class];
void *obj = &cls;
```

`obj`已经满足了构成一个objc对象的全部要求（首地址指向ClassObject），遂能够正常走消息机制；  
由于这个人造的对象在栈上，而取`self.name`的操作本质上是self指针在内存向高位地址偏移（32位下一个指针是4字节），按viewDidLoad执行时各个变量入栈顺序从高到底为（self, _cmd, self.class, self, obj）（前两个是方法隐含入参，随后两个为super调用的两个压栈参数），遂栈低地址的obj+4取到了self。
