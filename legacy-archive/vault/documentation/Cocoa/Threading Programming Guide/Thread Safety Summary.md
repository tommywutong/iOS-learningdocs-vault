---
title: 多线程编程指南
apple_id: 10000057i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Performance
technology: null
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/ThreadSafetySummary/ThreadSafetySummary.html
archived_at: '2026-07-15T07:16:47.622339Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [多线程编程指南](Introduction.md)


[下一页](Glossary.md)[上一页](Synchronization.md)

# 线程安全性总结

本附录介绍 OS X 和 iOS 中一些关键框架的高层线程安全性。本附录中的信息可能会有所变化。

从多个线程使用 Cocoa 时的准则包括以下几点：

- 不可变对象通常是线程安全的。一旦创建了这些对象，你就可以安全地在线程之间来回传递它们。另一方面，可变对象通常是非线程安全的。要在多线程应用程序中使用可变对象，应用程序必须进行适当的同步。更多信息请参阅 [Mutable Versus Immutable](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ztmljrgi3damjq)。
- 许多被认为"非线程安全"的对象，其实只是不能同时从多个线程使用。这些对象中的许多都可以在任意线程上使用，只要一次只在一个线程上使用即可。那些明确限定只能在应用程序主线程上使用的对象会被特别指出。
- 应用程序的主线程负责处理事件。尽管即便有其他线程参与事件路径，Application Kit 仍能继续正常工作，但操作可能会乱序发生。
- 如果你想用某个线程为某个视图绘图，请把所有绘图代码都放在 [NSView](https://developer.apple.com/documentation/appkit/nsview) 的 [lockFocusIfCanDraw](https://developer.apple.com/documentation/appkit/nsview/1483285-lockfocusifcandraw) 和 [unlockFocus](https://developer.apple.com/documentation/appkit/nsview/1483711-unlockfocus) 方法之间。
- 要在 Cocoa 中使用 POSIX 线程，你必须先把 Cocoa 切换到多线程模式。更多信息请参阅 [Using POSIX Threads in a Cocoa Application](Thread%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ztqljrgi2tamru)。

有一种误解认为 Foundation 框架是线程安全的，而 Application Kit 框架不是。遗憾的是，这是一种过于笼统且有些误导性的说法。每个框架都有一部分是线程安全的，也有一部分是非线程安全的。以下各节将介绍 Foundation 框架的总体线程安全性。

下列类和函数通常被认为是线程安全的。你可以在多个线程中使用同一个实例，而无需先获取锁。

- [NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray)
- [NSAssertionHandler](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAssertionHandler/Description.html#//apple_ref/occ/cl/NSAssertionHandler)
- [NSAttributedString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/cl/NSAttributedString)
- [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle)
- [NSCalendar](https://developer.apple.com/documentation/foundation/nscalendar)
- [NSCalendarDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/cl/NSCalendarDate)
- [NSCharacterSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/cl/NSCharacterSet)
- [NSConditionLock](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConditionLock/Description.html#//apple_ref/occ/cl/NSConditionLock)
- [NSConnection](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/cl/NSConnection)
- [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData)
- [NSDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/cl/NSDate)
- [NSDateFormatter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateFormatter/Description.html#//apple_ref/occ/cl/NSDateFormatter)
- `NSDecimal` functions
- [NSDecimalNumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDecimalNumber/Description.html#//apple_ref/occ/cl/NSDecimalNumber)
- [NSDecimalNumberHandler](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDecimalNumberHandler/Description.html#//apple_ref/occ/cl/NSDecimalNumberHandler)
- [NSDeserializer](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDeserializer/Description.html#//apple_ref/occ/cl/NSDeserializer)
- [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary)
- [NSDistantObject](https://developer.apple.com/documentation/foundation/nsdistantobject)
- [NSDistributedLock](https://developer.apple.com/documentation/foundation/nsdistributedlock)
- [NSDistributedNotificationCenter](https://developer.apple.com/documentation/foundation/nsdistributednotificationcenter)
- [NSException](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/cl/NSException)
- [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager)
- [NSFormatter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSFormatter/Description.html#//apple_ref/occ/cl/NSFormatter)
- [NSHost](https://developer.apple.com/documentation/foundation/host)
- [NSJSONSerialization](https://developer.apple.com/documentation/foundation/nsjsonserialization)
- [NSLock](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSLock/Description.html#//apple_ref/occ/cl/NSLock)
- [NSLog](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSLog)/[NSLogv](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSLogv)
- [NSMethodSignature](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSMethodSignature/Description.html#//apple_ref/occ/cl/NSMethodSignature)
- [NSNotification](https://developer.apple.com/documentation/foundation/nsnotification)
- [NSNotificationCenter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/cl/NSNotificationCenter)
- [NSNumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/cl/NSNumber)
- [NSNumberFormatter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/cl/NSNumberFormatter)
- [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject)
- [NSOrderedSet](https://developer.apple.com/documentation/foundation/nsorderedset)
- [NSPortCoder](https://developer.apple.com/documentation/foundation/nsportcoder)
- [NSPortMessage](https://developer.apple.com/documentation/foundation/nsportmessage)
- [NSPortNameServer](https://developer.apple.com/documentation/foundation/nsportnameserver)
- [NSProgress](https://developer.apple.com/documentation/foundation/nsprogress)
- [NSProtocolChecker](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProtocolChecker/Description.html#//apple_ref/occ/cl/NSProtocolChecker)
- [NSProxy](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProxy/Description.html#//apple_ref/occ/cl/NSProxy)
- [NSRecursiveLock](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRecursiveLock/Description.html#//apple_ref/occ/cl/NSRecursiveLock)
- [NSSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSSet)
- [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString)
- [NSThread](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSThread/Description.html#//apple_ref/occ/cl/NSThread)
- [NSTimer](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimer/Description.html#//apple_ref/occ/cl/NSTimer)
- [NSTimeZone](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimeZoneClassCluster/Description.html#//apple_ref/occ/cl/NSTimeZone)
- [NSUserDefaults](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/cl/NSUserDefaults)
- [NSValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/cl/NSValue)
- [NSXMLParser](https://developer.apple.com/documentation/foundation/xmlparser)
- 对象分配和保留计数函数
- 区域（zone）和内存函数

下列类和函数通常是非线程安全的。在大多数情况下，只要一次只在一个线程中使用，你就可以在任意线程中使用这些类。更多细节请查阅相应类的文档。

- [NSArchiver](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArchiver/Description.html#//apple_ref/occ/cl/NSArchiver)
- [NSAutoreleasePool](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAutoreleasePool/Description.html#//apple_ref/occ/cl/NSAutoreleasePool)
- [NSCoder](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCoder/Description.html#//apple_ref/occ/cl/NSCoder)
- [NSCountedSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCountedSet/Description.html#//apple_ref/occ/cl/NSCountedSet)
- [NSEnumerator](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSEnumerator/Description.html#//apple_ref/occ/cl/NSEnumerator)
- [NSFileHandle](https://developer.apple.com/documentation/foundation/filehandle)
- `NSHashTable` functions
- [NSInvocation](https://developer.apple.com/documentation/foundation/nsinvocation)
- `NSMapTable` functions
- [NSMutableArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSMutableArray)
- [NSMutableAttributedString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/cl/NSMutableAttributedString)
- [NSMutableCharacterSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/cl/NSMutableCharacterSet)
- [NSMutableData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSMutableData)
- [NSMutableDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSMutableDictionary)
- [NSMutableOrderedSet](https://developer.apple.com/documentation/foundation/nsmutableorderedset)
- [NSMutableSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSMutableSet)
- [NSMutableString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSMutableString)
- [NSNotificationQueue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationQueue/Description.html#//apple_ref/occ/cl/NSNotificationQueue)
- [NSPipe](https://developer.apple.com/documentation/foundation/nspipe)
- [NSPort](https://developer.apple.com/documentation/foundation/nsport)
- [NSProcessInfo](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProcessInfo/Description.html#//apple_ref/occ/cl/NSProcessInfo)
- [NSRunLoop](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRunLoop/Description.html#//apple_ref/occ/cl/NSRunLoop)
- [NSScanner](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/cl/NSScanner)
- [NSSerializer](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSerializer/Description.html#//apple_ref/occ/cl/NSSerializer)
- [NSTask](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/cl/NSTask)
- [NSUnarchiver](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUnarchiver/Description.html#//apple_ref/occ/cl/NSUnarchiver)
- [NSUndoManager](https://developer.apple.com/documentation/foundation/undomanager)
- 用户名和主目录函数

请注意，尽管 `NSArchiver`、`NSCoder` 和 `NSEnumerator` 对象本身是线程安全的，但之所以在此列出，是因为在使用期间更改它们所封装的数据对象是不安全的。例如，对归档器而言，更改正在归档的对象图是不安全的；对枚举器而言，任何线程更改被枚举的集合都是不安全的。

下列类只能在应用程序的主线程中使用。

- [NSAppleScript](https://developer.apple.com/documentation/foundation/nsapplescript)

不可变对象通常是线程安全的；一旦创建了这些对象，你就可以安全地在线程之间来回传递它们。当然，使用不可变对象时，你仍然需要记得正确地使用引用计数。如果你不恰当地释放了一个自己并未保留的对象，之后可能会引发异常。

可变对象通常是非线程安全的。要在多线程应用程序中使用可变对象，应用程序必须使用锁来同步对它们的访问（更多信息请参阅 [Atomic Operations](Synchronization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedqlktk4za)）。一般来说，涉及变更时，集合类（例如 [NSMutableArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSMutableArray)、[NSMutableDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSMutableDictionary)）是非线程安全的。也就是说，如果有一个或多个线程正在更改同一个数组，就可能出现问题。你必须在发生读写的地方加锁，以确保线程安全。

即便某个方法声称返回一个不可变对象，你也不应该想当然地认为返回的对象就是不可变的。根据方法实现的不同，返回的对象可能是可变的，也可能是不可变的。例如，一个返回类型为 [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) 的方法，其实现方式可能导致它实际返回的是一个 [NSMutableString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSMutableString)。如果你想确保自己拿到的对象确实是不可变的，就应该制作一份不可变拷贝。

只有当某个操作"调用"同一对象或不同对象上的其他操作时，重入才有可能发生。保留和释放对象就是一种常被忽视的"调用"。

下表列出了 Foundation 框架中明确可重入的部分。其他所有类可能是可重入的，也可能不是，将来也可能被改为可重入。目前从未对可重入性做过完整的分析，这份列表可能并不详尽。

- Distributed Objects
- [NSConditionLock](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConditionLock/Description.html#//apple_ref/occ/cl/NSConditionLock)
- [NSDistributedLock](https://developer.apple.com/documentation/foundation/nsdistributedlock)
- [NSLock](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSLock/Description.html#//apple_ref/occ/cl/NSLock)
- [NSLog](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSLog)/[NSLogv](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSLogv)
- [NSNotificationCenter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/cl/NSNotificationCenter)
- [NSRecursiveLock](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRecursiveLock/Description.html#//apple_ref/occ/cl/NSRecursiveLock)
- [NSRunLoop](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRunLoop/Description.html#//apple_ref/occ/cl/NSRunLoop)
- [NSUserDefaults](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/cl/NSUserDefaults)

Objective-C 运行时系统会在某个类接收任何其他消息之前，先向其发送一条 `initialize` 消息。这使得该类有机会在被使用之前设置好自己的运行时环境。在多线程应用程序中，运行时会保证只有一个线程——也就是恰好向该类发送第一条消息的那个线程——执行 `initialize` 方法。如果在第一个线程仍处于 `initialize` 方法中时，第二个线程试图向该类发送消息，那么第二个线程会被阻塞，直到 `initialize` 方法执行完毕。与此同时，第一个线程可以继续调用该类的其他方法。`initialize` 方法不应该依赖第二个线程来调用该类的方法；如果它这样做，两个线程就会发生死锁。

由于 OS X 10.1.x 及更早版本中的一个 bug，一个线程可能会在另一个线程完成该类的 `initialize` 方法执行之前，就向该类发送消息。此时该线程可能访问到尚未完全初始化的值，甚至导致应用程序崩溃。如果你遇到这个问题，需要引入锁以防止在这些值初始化完成之前被访问，或者在应用程序进入多线程模式之前强制该类先完成初始化。

每个线程都维护着自己的一份 [NSAutoreleasePool](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAutoreleasePool/Description.html#//apple_ref/occ/cl/NSAutoreleasePool) 对象栈。Cocoa 期望当前线程的栈上始终有一个可用的自动释放池。如果没有可用的池，对象就不会被释放，从而造成内存泄漏。基于 Application Kit 的应用程序会在主线程中自动创建和销毁一个 `NSAutoreleasePool` 对象，但次线程（以及仅使用 Foundation 的应用程序）必须在使用 Cocoa 之前自行创建。如果你的线程生命周期较长，并且可能会产生大量自动释放对象，你应该定期销毁并重新创建自动释放池（就像 Application Kit 在主线程上所做的那样）；否则，自动释放的对象会不断累积，导致你的内存占用不断增长。如果你的分离线程不使用 Cocoa，就不需要创建自动释放池。

每个线程有且只有一个运行循环。不过，每个运行循环——也就是每个线程——都有自己的一套输入模式，用来决定运行循环运行时会监听哪些输入源。一个运行循环中定义的输入模式不会影响另一个运行循环中定义的输入模式，即便它们可能有相同的名称。

如果你的应用程序基于 Application Kit，主线程的运行循环会自动运行，但次线程（以及仅使用 Foundation 的应用程序）必须自己运行运行循环。如果一个分离线程没有进入运行循环，该线程会在其分离方法执行完毕后立即退出。

尽管从表面上看不一定如此，[NSRunLoop](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRunLoop/Description.html#//apple_ref/occ/cl/NSRunLoop) 类实际上并不是线程安全的。你应该只从拥有该实例的线程中调用它的实例方法。

以下各节介绍 Application Kit 框架的总体线程安全性。

下列类和函数通常是非线程安全的。在大多数情况下，只要一次只在一个线程中使用，你就可以在任意线程中使用这些类。更多细节请查阅相应类的文档。

- [NSGraphicsContext](https://developer.apple.com/documentation/appkit/nsgraphicscontext)。更多信息请参阅 [NSGraphicsContext Restrictions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcmrngezdmnzrgi)。
- [NSImage](https://developer.apple.com/documentation/appkit/nsimage)。更多信息请参阅 [NSImage Restrictions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcmrngezdmnzsha)。
- [NSResponder](https://developer.apple.com/documentation/appkit/nsresponder)
- [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) 及其所有子类。更多信息请参阅 [Window Restrictions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcmrngezdgmzwgq)。

下列类只能在应用程序的主线程中使用。

- [NSCell](https://developer.apple.com/documentation/appkit/nscell) 及其所有子类
- [NSView](https://developer.apple.com/documentation/appkit/nsview) 及其所有子类。更多信息请参阅 [NSView Restrictions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcmrngezdgnbsg4)。

你可以在次线程中创建一个窗口。Application Kit 会确保与该窗口相关联的数据结构在主线程上被释放，以避免出现竞态条件。在需要并发处理大量窗口的应用程序中，窗口对象仍有一定可能发生泄漏。

你可以在次线程中创建一个模态窗口。当主线程运行模态循环时，Application Kit 会阻塞发起调用的次线程。

应用程序的主线程负责处理事件。主线程就是阻塞在 [NSApplication](https://developer.apple.com/documentation/appkit/nsapplication) 的 `run` 方法中的那个线程，该方法通常在应用程序的 `main` 函数中被调用。尽管即便有其他线程参与事件路径，Application Kit 仍能继续正常工作，但操作可能会乱序发生。例如，如果两个不同的线程都在响应按键事件，这些按键就可能被乱序接收。让主线程处理事件，可以获得更一致的用户体验。事件一旦被接收，如果需要，还可以被派发给次线程做进一步处理。

你可以从次线程调用 `NSApplication` 的 [postEvent:atStart:](https://developer.apple.com/documentation/appkit/nsapplication/1428710-postevent) 方法，把一个事件发布到主线程的事件队列中。不过，相对于用户输入事件而言，顺序并不能得到保证。应用程序的主线程仍然负责处理事件队列中的事件。

Application Kit 在使用其图形函数和类（包括 [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath) 和 [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) 类）进行绘图时通常是线程安全的。使用特定类的细节将在以下各节中说明。关于绘图与线程的更多信息，请参阅 _[Cocoa Drawing Guide](../Cocoa%20Drawing%20Guide/Introduction%20to%20Cocoa%20Drawing%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojq)_。

[NSView](https://developer.apple.com/documentation/appkit/nsview) 类通常是非线程安全的。你应该只在应用程序的主线程中创建、销毁、调整大小、移动 `NSView` 对象，以及对其执行其他操作。只要用 [lockFocusIfCanDraw](https://developer.apple.com/documentation/appkit/nsview/1483285-lockfocusifcandraw) 和 [unlockFocus](https://developer.apple.com/documentation/appkit/nsview/1483711-unlockfocus) 把绘图调用括起来，从次线程绘图就是线程安全的。

如果应用程序的次线程想要让视图的某些部分在主线程上重新绘制，就不能使用诸如 `display`、[setNeedsDisplay:](https://developer.apple.com/documentation/appkit/nsview/1483360-needsdisplay)、[setNeedsDisplayInRect:](https://developer.apple.com/documentation/appkit/nsview/1483475-setneedsdisplayinrect) 或 [setViewsNeedDisplay:](https://developer.apple.com/documentation/appkit/nswindow/1419609-viewsneeddisplay) 这样的方法。相反，它应该向主线程发送一条消息，或者改用 [performSelectorOnMainThread:withObject:waitUntilDone:](https://developer.apple.com/documentation/objectivec/nsobject/1414900-performselector) 方法来调用这些方法。

视图系统的图形状态（gstate）是按线程划分的。使用图形状态曾经是一种能在单线程应用程序之上获得更好绘图性能的方式，但现在已不再如此。不正确地使用图形状态实际上可能导致绘图代码的效率反而低于在主线程中绘图。

[NSGraphicsContext](https://developer.apple.com/documentation/appkit/nsgraphicscontext) 类代表底层图形系统所提供的绘图上下文。每个 `NSGraphicsContext` 实例都持有各自独立的图形状态：坐标系、裁剪区域、当前字体等等。系统会在主线程上为每个 [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) 实例自动创建一个该类的实例。如果你从次线程进行任何绘图，系统会专门为该线程创建一个新的 `NSGraphicsContext` 实例。

如果你从次线程进行任何绘图，就必须手动刷新你的绘图调用。Cocoa 不会自动用次线程绘制的内容来更新视图，因此完成绘图后，你需要调用 `NSGraphicsContext` 的 [flushGraphics](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1527919-flushgraphics) 方法。如果你的应用程序只从主线程绘制内容，就不需要刷新绘图调用。

一个线程可以创建一个 [NSImage](https://developer.apple.com/documentation/appkit/nsimage) 对象，向图像缓冲区绘图，然后把它交给主线程进行绘制。底层的图像缓存在所有线程之间是共享的。关于图像及其缓存机制的更多信息，请参阅 _[Cocoa Drawing Guide](../Cocoa%20Drawing%20Guide/Introduction%20to%20Cocoa%20Drawing%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojq)_。

Core Data 框架通常支持多线程，不过在使用上有一些注意事项。关于这些注意事项，请参阅 _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_ 中的 Concurrency with Core Data 一节。

只要你小心编程，Core Foundation 就已经足够线程安全，不会遇到与线程竞争相关的问题。在常见的情况下——比如查询、保留、释放以及传递不可变对象——它是线程安全的。即便是可能被多个线程查询的中心共享对象，也能可靠地保证线程安全。

与 Cocoa 一样，Core Foundation 在涉及对对象或其内容进行变更时是非线程安全的。例如，修改一个可变数据对象或可变数组对象是非线程安全的，这符合预期，但修改不可变数组内部的对象同样是非线程安全的。原因之一是性能——在这些场景下性能至关重要。而且，在这个层面上通常也不可能实现绝对的线程安全。举例来说，你无法排除因保留从某个集合中取出的对象而产生的不确定行为——该集合本身可能在保留其所含对象的调用发生之前就已经被释放了。

在需要从多个线程访问并变更 Core Foundation 对象的场合，你的代码应该在访问点使用锁来防止并发访问。例如，枚举 Core Foundation 数组对象的代码，应该在枚举代码块前后使用适当的加锁调用，以防止其他线程同时修改该数组。

[下一页](Glossary.md)[上一页](Synchronization.md)

