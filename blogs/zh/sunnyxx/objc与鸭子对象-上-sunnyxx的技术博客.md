---
title: objc与鸭子对象（上） · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2014/08/24/objc-duck/'
original_language: zh
published: 2014-08-24
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:32509080018b3d2e'
translated: n/a
---

> 原文：[objc与鸭子对象（上） · sunnyxx的技术博客](http://blog.sunnyxx.com/2014/08/24/objc-duck/)　·　sunnyxx (孙源)

# objc与鸭子对象（上）

2014年8月24日

这是《objc与鸭子对象》的上半部分，[《objc与鸭子对象（下）》](http://blog.sunnyxx.com/2014/08/26/objc-duck-advanced/)中介绍了鸭子类型的进阶用法、依赖注入以及demo。

# [#我是前言](#我是前言)我是前言

![](http://ww1.sinaimg.cn/mw690/51530583jw1ejqkwtxr1dj20rs0ijgo7.jpg)  
`鸭子类型`(Duck Type)即：**“当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子”**，换成程序猿语言就是：**“当调用者知道这个对象能调用什么方法时，管它这个对象到底是什么类的实例呢”**。本文对objc中的鸭子类型对象进行简单探究，并用一个“只用一个类实现Json Entity”的小demo实践下这个思路的魔力。进阶篇请看下半部分。

---

# [#objc与鸭子类型](#objc与鸭子类型)objc与鸭子类型

## [#id类型是个大鸭子](#id类型是个大鸭子)id类型是个大鸭子

鸭子类型是动态语言的特性，编译时并不决定函数调用关系，说白了所有的类型声明都是给编译器看的。objc在动态和静态方面找到了不错的平衡，既保留了严格的静态检查也没破坏运行时的动态特性。  
我们知道，向一个objc对象（或Class）发消息，实际上就是沿着它的`isa`指针寻找真正函数地址，所以只要一个对象满足下面的结构，就可以对它发送消息：

```objc
struct objc_object {
    Class isa;
} *id;
```

也就是熟知的`id`类型，objc在语言层面先天就支持了这个基本的鸭子类型，我们可以将任意一个对象强转为id类型从而向它发送消息，就算它并不能响应这个消息，编译器也无从知晓。  
正如[这篇文章](http://www.informit.com/articles/article.aspx?p=1353396)中对objc对象的简短定义：`The best definition for a Smalltalk or Objective-C "object" is "something that can respond to messages.` object并非一定是某个特定类型的实例，只要它能响应需要的消息就可以了。

## [#从-interface到-protocol](#从-interface到-protocol)从@interface到@protocol

正如objc先天支持的动态的`id`类型，`@protocol`为鸭子类型提供了编译时的强类型检查，实现了Cocoa中经典的鸭子类型使用场景：

```objc
@property (nonatomic, assign) id <UITableViewDataSource> dataSource;
@property (nonatomic, assign) id <UITableViewDelegate>   delegate;
```

利用鸭子类型设计的接口会给使用者更大的灵活度。同时`@protocol`可以用来建立`伪继承`关系

```objc
@protocol UIScrollViewDelegate<NSObject>
@protocol UITableViewDelegate<NSObject, UIScrollViewDelegate>
```

`<NSObject>`协议的存在一方面是给`NSProxy`这样的其他根类使用，同时也给了鸭子协议类型一个根类型，正如给了大部分类一个NSObject根类一样。说个小插曲，由于objc中Class也是`id`类型，形如`id<UITableViewDataSource>`的鸭子类型是可以用Class对象来扮演的，只需要把实例方法替换成类方法，如：

```objc
@implementation DataSource
+ (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView {
    return 0;
}
+ (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    return 0;
}
@end
```

设置table view的data source：

```objc
self.tableView.dataSource = (Class<UITableViewDataSource>)[DataSource class];
```

这种非主流写法合法且运行正常，归功于objc中加号和减号方法在`@selector`中并未体现，在`@protocol`中也是形同虚设，这种代码我相信没人真的写，但确实能体现鸭子类型的灵活性。

---

# [#Demo-一个类实现Json-Entity](#Demo-一个类实现Json-Entity)[Demo]一个类实现Json Entity

`Entity`对象表示某个**纯数据**的结构，如：

```objc
@interface XXUserEntity : NSObject
@property (nonatomic, copy) NSString *name;
@property (nonatomic, copy) NSString *sex;
@property (nonatomic, assign) NSInteger age;
// balabala....
@end
```

实际开发中这种类往往对应着server端返回的一个JSON串，如：

```plain
{"name": "sunnyxx", "sex": "boy", "age": 24, ...}
```

解析这些映射是个纯重复工作，建类、写属性、解析…如今已经有[JSONModel](https://github.com/icanzilb/JSONModel)，[Mantle](https://github.com/Mantle/Mantle)等不错的框架帮忙。这个demo我们要用鸭子类型的思想去重新设计，把这些Entity类简化成一个鸭子类。

由于上面的`UserEntity`类，只有属性的getter和setter，这正对应了`NSMutableDictionary`的`objectForKey:`和`setObjectForKey:`，同时，JSON数据也会解析成字典，这就完成了巧妙的对接，下面去实现这个类。

真正干活的是一个字典，保证封装性和纯粹性，这个类直接使用`NSProxy`作为纯代理类，只暴露一个初始化方法就好了：

```objc
// XXDuckEntity.h
@interface XXDuckEntity : NSProxy
- (instancetype)initWithJSONString:(NSString *)json;
@end
// XXDuckEntity.m
@interface XXDuckEntity ()
@property (nonatomic, strong) NSMutableDictionary *innerDictionary;
@end
```

`NSProxy`默认是没有初始化方法的，也省去了去规避其他初始化方法的麻烦，为了简单直接初始化时就把json串解开成字典（暂不考虑json是个array）：

```objc
- (instancetype)initWithJSONString:(NSString *)json
{
    NSData *data = [json dataUsingEncoding:NSUTF8StringEncoding];
    id jsonObject = [NSJSONSerialization JSONObjectWithData:data options:NSJSONReadingAllowFragments error:nil];
    if ([jsonObject isKindOfClass:[NSDictionary class]]) {
        self.innerDictionary = [jsonObject mutableCopy];
    }
    return self;
}
```

`NSProxy`可以说除了重载消息转发机制外没有别的用法，这也是它被设计的初衷，自己什么都不干，转给代理对象就好。往这个proxy发消息是注定会走消息转发的，首先判断下是不是一个getter或setter的selector：

```objc
- (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector
{
    SEL changedSelector = aSelector;
    if ([self propertyNameScanFromGetterSelector:aSelector]) {
        changedSelector = @selector(objectForKey:);
    }
    else if ([self propertyNameScanFromSetterSelector:aSelector]) {
        changedSelector = @selector(setObject:forKey:);
    }
    return [[self.innerDictionary class] instanceMethodSignatureForSelector:changedSelector];
}
```

签名替换成字典的两个方法后开始走转发，在这里设置参数和对内部字典的真正调用：

```objc
- (void)forwardInvocation:(NSInvocation *)invocation
{
    NSString *propertyName = nil;
    // Try getter
    propertyName = [self propertyNameScanFromGetterSelector:invocation.selector];
    if (propertyName) {
        invocation.selector = @selector(objectForKey:);
        [invocation setArgument:&propertyName atIndex:2]; // self, _cmd, key
        [invocation invokeWithTarget:self.innerDictionary];
        return;
    }
    // Try setter
    propertyName = [self propertyNameScanFromSetterSelector:invocation.selector];
    if (propertyName) {
        invocation.selector = @selector(setObject:forKey:);
        [invocation setArgument:&propertyName atIndex:3]; // self, _cmd, obj, key
        [invocation invokeWithTarget:self.innerDictionary];
        return;
    }
    [super forwardInvocation:invocation];
}
```

当然还有这两个必不可少的从getter和setter中获取属性名的Helper：

```objc
- (NSString *)propertyNameScanFromGetterSelector:(SEL)selector
{
    NSString *selectorName = NSStringFromSelector(selector);
    NSUInteger parameterCount = [[selectorName componentsSeparatedByString:@":"] count] - 1;
    if (parameterCount == 0) {
        return selectorName;
    }
    return nil;
}
- (NSString *)propertyNameScanFromSetterSelector:(SEL)selector
{
    NSString *selectorName = NSStringFromSelector(selector);
    NSUInteger parameterCount = [[selectorName componentsSeparatedByString:@":"] count] - 1;
    if ([selectorName hasPrefix:@"set"] && parameterCount == 1) {
        NSUInteger firstColonLocation = [selectorName rangeOfString:@":"].location;
        return [selectorName substringWithRange:NSMakeRange(3, firstColonLocation - 3)].lowercaseString;
    }
    return nil;
}
```

一个简单的鸭子Entity就完成了，之后所有的Entity都可以使用`@protocol`而非子类化的方式来定义，如：

```objc
@protocol XXUserEntity <NSObject>
@property (nonatomic, copy) NSString *name;
@property (nonatomic, copy) NSString *sex;
@property (nonatomic, strong) NSNumber *age;
@end
@protocol XXStudentEntity <XXUserEntity>
@property (nonatomic, copy) NSString *school;
@property (nonatomic, copy) NSString *teacher;
@end
```

当数据从网络层回来时，鸭子类型让这个对象用起来和真有这么个类没什么两样：

```objc
- (void)requestFinished:(XXDuckEntity<XXStudentEntity> *)student {
    NSLog(@"name: %@, school:%@", student.name, student.school);
}
```

至此，所有的entity被表示成了N个`<Protocol>`的`.h`文件加一个`XXDuckEntity`类，剩下的就靠想象力了。  
这个demo的源码将在[下半部分](http://blog.sunnyxx.com/2014/08/26/objc-duck-advanced/)之后给出

---

# [#Reference](#Reference)Reference

[http://en.wikipedia.org/wiki/Duck_typing](http://en.wikipedia.org/wiki/Duck_typing)  
[http://www.informit.com/articles/article.aspx?p=1353396](http://www.informit.com/articles/article.aspx?p=1353396)  
[https://github.com/facebook/facebook-ios-sdk](https://github.com/facebook/facebook-ios-sdk)
