---
title: Notification Once · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2015/03/09/notification-once/'
original_language: zh
published: 2015-03-09
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:cbf225dc72381ada'
translated: n/a
---

> 原文：[Notification Once · sunnyxx的技术博客](http://blog.sunnyxx.com/2015/03/09/notification-once/)　·　sunnyxx (孙源)

# Notification Once

2015年3月9日

前段时间整理项目中的`AppDelegate`，发现很多写在`- application:didFinishLaunchingWithOptions:`中的代码都只是为了在程序启动时获得一次调用机会，多为某些模块的初始化工作，如：

```objc
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // ...
    [FooModule setup];
    [[BarModule sharedInstance] setup];
    // ...
    return YES;
}
```

其实这些代码完全可以利用`Notification`的方式在自己的模块内部搞定，分享一个巧妙的方法：

```objc
/// FooModule.m
+ (void)load
{
    __block id observer =
    [[NSNotificationCenter defaultCenter]
     addObserverForName:UIApplicationDidFinishLaunchingNotification
     object:nil
     queue:nil
     usingBlock:^(NSNotification *note) {
         [self setup]; // Do whatever you want
         [[NSNotificationCenter defaultCenter] removeObserver:observer];
     }];
}
```

解释：

- `+ load`方法在足够早的时间点被调用
- block 版本的通知注册会产生一个`__NSObserver *`对象用来给外部 remove 观察者
- block 对 observer 对象的捕获早于函数的返回，所以若不加`__block`，会捕获到 nil
- 在 block 执行结束时移除 observer，无需其他清理工作
- 这样，在模块内部就完成了在程序启动点代码的挂载

值得注意的是，通知是在`- application:didFinishLaunchingWithOptions:`调用完成后才发送的。  
顺便提下给 AppDelegate 瘦身的建议：AppDelegate 作为程序级状态变化的 delegate，应该只做**路由**和**分发**的作用，具体逻辑实现代码还是应该在分别的模块中，这个文件应该保持整洁，除了`<UIApplicationDelegate>`的方法外不应该出现其他方法。
