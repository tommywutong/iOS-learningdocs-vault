---
title: objc与鸭子对象（下） · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2014/08/26/objc-duck-advanced/'
original_language: zh
published: 2014-08-26
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:ffb16f7c5e85e89b'
translated: n/a
---

> 原文：[objc与鸭子对象（下） · sunnyxx的技术博客](http://blog.sunnyxx.com/2014/08/26/objc-duck-advanced/)　·　sunnyxx (孙源)

# objc与鸭子对象（下）

2014年8月26日

# [#我是前言](#我是前言)我是前言

这是《objc与鸭子对象》的下半部分，[《objc与鸭子对象（上）》](http://blog.sunnyxx.com/2014/08/24/objc-duck/)中介绍了鸭子类型和它在objc中的实践，以及一个使用NSProxy实现JSON Entity的鸭子类。下半部分介绍鸭子对象的进阶用法，并简单介绍由鸭子对象思想衍生出的`依赖注入`，实现一个demo。

---

# [#被误解了的面向对象](#被误解了的面向对象)被误解了的面向对象

Smalltalk之父或者说面向对象之父（之一）的**Alan Kay**曾写过：

> I’m sorry that I long ago coined the term “objects” for this topic because it gets many people to focus on the lesser idea. The big idea is “messaging” - that is what the kernal of Smalltalk/Squeak is all about.

面向对象的思想的核心并不在于`object`或者`class`，而在于`message`，或者说**对象和类只是消息的载体**。面向对象思想将程序按功能和逻辑分成了若干个类，每个类包含自己的代码、功能实现并提供对外接口，以黑箱模式运行，使得外部无需了解内部而协同使用，分解了复杂度并控制在一个个较小规模中，以消息作为其间所有的协作方式。  
回到主题，理解了message才是全部，鸭子对象又可以更近一层，试想下整个程序，每个类除了知道自己的类之外其他类名一无所知，全部通过协议发消息：

```objc
- (void)schoolWillStart:(id<School>)school
{
    id<Teacher> teacher = school.teacher;
    for (id<Student> student in scholl.allStudents) {
        [student handIn:student.homework to:teacher];
    }
}
```

---

# [#Json-Entity的重构](#Json-Entity的重构)Json Entity的重构

回想上一篇中的JSON Entity类：

```objc
// XXDuckEntity.h
@interface XXDuckEntity : NSProxy
- (instancetype)initWithJSONString:(NSString *)json;
@end
```

干嘛caller要知道有这么个`Class`存在呢？它关心的只是能用哪些message通信而已。于是把类声明移动到`.m`中，简化成一个C的创建方法（类工厂方法同样会暴露类名）：

```objc
// XXDuckEntity.h
extern id XXDuckEntityCreateWithJSON(NSString *json);
// XXDuckEntity.m
id XXDuckEntityCreateWithJSON(NSString *json)
{
    return [[XXDuckEntity alloc] initWithJSONString:json];
}
```

如果这个类需要提供其他message接口供caller使用，则：

```objc
@protocol XXDuckEntity <NSObject, NSCopying, NSCoding>
@property (nonatomic, copy, readonly) NSString *jsonString;
- (void)foo;
@end
extern id/*<XXDuckEntity>*/ XXDuckEntityCreateWithJSON(NSString *json);
```

`<XXDuckEntity>`被注释掉是因为真实使用场景会造成类型不匹配造成编译警告，所以caller使用起来：

```objc
NSString *json = @"{\"name\": \"sunnyxx\", \"sex\": \"boy\", \"age\": 24}";
id<XXDuckEntity, XXUserEntity> entity= XXDuckEntityCreateWithJSON(json);
id<XXUserEntity> copied = [entity copy];
NSLog(@"%@, %@, %@", copied.jsonString, copied.name, copied.age);
```

这样重构的鸭子对象不仅隐藏了内部实现是个字典的事实，连它究竟是什么Class都隐藏了，但程序运行并无影响，骗一骗编译器罢了。不过这个思路的改变确引出另一个技术思路，那就是`依赖注入`。

---

# [#依赖注入](#依赖注入)依赖注入

`Dependency Injection`，简称`DI`，其实在这个场景下叫`动态实现注入`更合适。它的思想是将一个“对象”分成三部分，**protocol**、**proxy**和**implementation**，试想有两个协议，他们定义了彼此间该如何发送message：  
![](http://ww1.sinaimg.cn/bmiddle/51530583jw1ejqir7ys6zj20lu04ywes.jpg)  
运行时他们都是由proxy对象扮演：  
![](http://ww3.sinaimg.cn/bmiddle/51530583jw1ejqj0qchl2j20m009eq3k.jpg)  
但DI Proxy并不能响应任何message，真正的实现是动态被“注入”到Proxy中的：  
![](http://ww3.sinaimg.cn/bmiddle/51530583jw1ejqj6c7uqrj20l60dw75f.jpg)  
由于调用层只有协议没有类名，所以`Implement A`实现类并不依赖`Implement B`，就像贩毒团伙的两方只靠小弟来交易，完全不知道幕后大哥是谁，这就是所谓的“面向接口编程”吧。

## [#Let’s-demo-it](#Let’s-demo-it)Let’s demo it

重点在实现这个Proxy类，按照刚才重构Json Entity类的思路，头文件定义十分精简：

```objc
// XXDIProxy.h
@protocol XXDIProxy <NSObject>
- (void)injectDependencyObject:(id)object forProtocol:(Protocol *)protocol;
@end
extern id/*<XXDIProxy>*/ XXDIProxyCreate();
```

既然都叫Proxy了，再不使用`NSProxy`类都对不起它了。这个类使用一个字典来存储被注入的实现对象，以及与protocol的对应关系：

```objc
// XXDIProxy.m 这是个私有类
@interface XXDIProxy : NSProxy <XXDIProxy>
@property (nonatomic, strong) NSMutableDictionary *implementations;
- (id)init;
@end
```

实现`<XXDIProxy>`协议内容：

```objc
// XXDIProxy.m
- (void)injectDependencyObject:(id)object forProtocol:(Protocol *)protocol
{
    NSParameterAssert(object && protocol);
    NSAssert([object conformsToProtocol:protocol], @"object %@ does not conform to protocol: %@", object, protocol);
    self.implementations[NSStringFromProtocol(protocol)] = object;
}
```

关键步骤还是消息转发，非常简单，把收到的消息转发给能处理的implementation对象（如果用NSObject的`forwardingTargetForSelector`将更加简单）：

```objc
- (NSMethodSignature *)methodSignatureForSelector:(SEL)sel
{
    for (id object in self.implementations.allValues) {
        if ([object respondsToSelector:sel]) {
            return [object methodSignatureForSelector:sel];
        }
    }
    return [super methodSignatureForSelector:sel];
}
- (void)forwardInvocation:(NSInvocation *)invocation
{
    for (id object in self.implementations.allValues) {
        if ([object respondsToSelector:invocation.selector]) {
            [invocation invokeWithTarget:object];
            return;
        }
    }
    [super forwardInvocation:invocation];
}
```

有了Proxy类，下面是另外两个角色的测试代码，协议：

```objc
@protocol XXGirlFriend <NSObject>
- (void)kiss;
@end
```

实现类（汉字是可以正常编译运行的- -）：

```objc
@interface 林志玲 : NSObject <XXGirlFriend>
@end
@interface 凤姐 : NSObject <XXGirlFriend>
@end
```

测试代码：

```objc
林志玲 *implementA = [林志玲 new];
凤姐 *implementB = [凤姐 new];

id<XXDIProxy, XXGirlFriend> gf = XXDIProxyCreate();
[gf injectDependencyObject:implementA forProtocol:@protocol(XXGirlFriend)];
[gf kiss]; // Log: 林志玲 kissed me
[gf injectDependencyObject:implementB forProtocol:@protocol(XXGirlFriend)];
[gf kiss]; // Log: 凤姐 kissed me
```

这个简单的demo就完成了。  
这个demo的`源码`可以[-\>从这里下载\<-](https://github.com/sunnyxx/XXDuckDemo)，have fun.

---

# [#我是后语](#我是后语)我是后语

现在有一个完整的依赖注入框架[typhoon](http://www.typhoonframework.org/)，感兴趣的可以把玩一下。  
依赖注入不仅可以解耦依赖关系，也可以更好的Test和Mock，想测试某个对象只需要将实现对象注入成Test对象，想造假数据只需要将response对象替换成一个Mock对象，无需修改调用代码，天然不刺激~

_PS： 实际使用中可不要过度设计哦。。。_

---

# [#Reference](#Reference)Reference

[http://c2.com/cgi/wiki?AlanKayOnMessaging](http://c2.com/cgi/wiki?AlanKayOnMessaging)  
[http://www.typhoonframework.org/](http://www.typhoonframework.org/)
