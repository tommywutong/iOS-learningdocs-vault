---
title: 键值观察编程指南
apple_id: 10000177i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html
archived_at: '2026-07-15T07:16:19.102348Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Registering%20for%20Key-Value%20Observing.md)

# 键值观察编程指南简介

键值观察是一种机制，允许对象在其他对象的指定属性发生变化时收到通知。

键值观察提供了一种机制，允许对象在其他对象的特定属性发生变化时收到通知。它在应用[模型层和控制器层](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MVC.html#//apple_ref/doc/uid/TP40008195-CH32)之间的通信中尤为有用。（在 OS X 中，[控制器层](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11)绑定技术大量依赖键值观察。）[控制器对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11)通常观察模型对象的属性，而视图对象通过控制器观察模型对象的属性。不过除此之外，模型对象也可以观察其他模型对象（通常用于确定依赖值何时变化），甚至观察其自身（同样是为了确定依赖值何时变化）。

你可以观察包括简单属性、对一关系和对多关系在内的属性。对多关系的观察者会被告知所做更改的类型，以及更改涉及哪些对象。

一个简单的例子可以说明 KVO 在应用中的用处。假设一个 `Person` 对象与一个 `Account` 对象交互，后者表示此人在银行的储蓄账户。`Person` 实例可能需要知道 `Account` 实例的某些方面（例如余额或利率）何时发生变化。

![Art/kvo_objects_properties.png](attachments/Art/kvo_objects_properties.png)

如果这些属性是 `Account` 的公开属性，`Person` 可以定期轮询 `Account` 来发现变化，但这显然效率低下，而且往往不切实际。更好的做法是使用 KVO，这类似于在变化发生时 `Person` 收到一个中断。

要使用 KVO，首先必须确保被观察的对象（本例中的 `Account`）符合 KVO 规范。通常，只要你的对象继承自 `NSObject` 并以常规方式创建属性，你的对象及其属性就会自动符合 KVO 规范，也可以手动实现合规。[符合 KVO 规范](KVO%20Compliance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tqlkciffekqkjivcq)介绍了自动与手动键值观察之间的区别，以及如何实现这两种方式。

接下来，必须将你的观察者实例（`Person`）注册到被观察实例（`Account`）上。`Person` 针对每个被观察的键路径，向 `Account` 发送一条 [addObserver:forKeyPath:options:context:](https://developer.apple.com/documentation/objectivec/nsobject/1412787-addobserver) 消息，并将自己指定为观察者。

![Art/kvo_objects_add.png](attachments/Art/kvo_objects_add.png)

为了接收来自 `Account` 的更改通知，`Person` 需要实现 [observeValueForKeyPath:ofObject:change:context:](https://developer.apple.com/documentation/objectivec/nsobject/1416553-observevalueforkeypath) 方法，这是所有观察者都必须实现的方法。每当已注册的键路径之一发生变化时，`Account` 都会向 `Person` 发送这条消息。随后 `Person` 可以根据更改通知采取适当的操作。

![Art/kvo_objects_observe.png](attachments/Art/kvo_objects_observe.png)

最后，当 `Person` 实例不再需要通知时——最迟也要在它被释放之前——必须通过向 `Account` 发送 [removeObserver:forKeyPath:](https://developer.apple.com/documentation/objectivec/nsobject/1408054-removeobserver) 消息来注销。

![Art/kvo_objects_remove.png](attachments/Art/kvo_objects_remove.png)

[注册键值观察](Registering%20for%20Key-Value%20Observing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2telkciffekqkjivcq)介绍了注册、接收和注销键值观察通知的完整生命周期。

KVO 的主要优点在于，你不必在每次属性变化时自行实现发送通知的方案。它定义完善的基础设施拥有框架级支持，易于采用——通常你无需向项目添加任何代码。此外，该基础设施功能完备，可以轻松支持单个属性的多个观察者以及依赖值。

[注册依赖键](Registering%20Dependent%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tslkciffekqkjivcq)说明了如何指定某个键的值依赖于另一个键的值。

与使用 [NSNotificationCenter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/cl/NSNotificationCenter) 的通知不同，KVO 没有为所有观察者提供更改通知的中心对象。相反，发生更改时通知会直接发送给观察对象。`NSObject` 提供了键值观察的这一基础实现，你几乎不需要[重写](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MethodOverriding.html#//apple_ref/doc/uid/TP40008195-CH57)这些方法。

[键值观察实现细节](Key-Value%20Observing%20Implementation%20Details.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydolkciffekqkjivcq)介绍了键值观察的实现方式。

[下一页](Registering%20for%20Key-Value%20Observing.md)
