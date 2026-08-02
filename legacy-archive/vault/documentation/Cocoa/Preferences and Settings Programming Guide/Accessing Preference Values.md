---
title: 偏好与设置编程指南
apple_id: 10000059i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UserDefaults/AccessingPreferenceValues/AccessingPreferenceValues.html
archived_at: '2026-07-15T07:21:01.840033Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [偏好与设置编程指南](About%20Preferences%20and%20Settings.md)


[下一页](Storing%20Preferences%20in%20iCloud.md)[上一页](About%20the%20User%20Defaults%20System.md)

# 访问偏好设置的值

你可以使用 [NSUserDefaults](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/cl/NSUserDefaults) 类来访问应用的偏好设置。系统为每个应用提供了该类的唯一一个实例，可通过 [standardUserDefaults](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/clm/NSUserDefaults/standardUserDefaults) 类方法获取。你可以用这个共享的用户默认设置（user defaults）对象来：

- 在启动时为应用的偏好设置指定各种默认值。
- 读取和设置存储在应用域中的单项偏好设置值。
- 移除偏好设置的值。
- 查看易失偏好设置域中的内容。

使用 Cocoa 绑定的 Mac 应用可以用 [NSUserDefaultsController](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller) 对象自动地读写偏好设置。你通常会把这样一个对象添加到用于显示面向用户的偏好设置界面的那个 nib 文件中。然后把界面控件绑定到用户默认设置控制器中的条目上，由它来负责在用户默认设置数据库中读写值的整个过程。

偏好设置的值必须是标准属性列表对象类型之一：[NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData)、[NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString)、[NSNumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/cl/NSNumber)、[NSDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/cl/NSDate)、[NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray) 或 [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary)。`NSUserDefaults` 类还内置了把 [NSURL](https://developer.apple.com/documentation/foundation/nsurl) 对象作为偏好设置值存储的处理逻辑。关于属性列表及其内容的更多信息，请参阅 _[属性列表编程指南](../Property%20List%20Programming%20Guide/Introduction%20to%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2i)_。

应用应当在启动时，为所有它期望存在且有效的偏好设置注册默认值。当你请求一项从未被设置过的偏好设置的值时，[NSUserDefaults](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/cl/NSUserDefaults) 类的方法会返回与该数据类型相称的默认值。对于数值型标量，这通常意味着返回 `0`；而对于字符串和其他对象，则意味着返回 `nil`。如果这些标准默认值不适合你的应用，你可以用 [registerDefaults:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/registerDefaults:) 方法注册自己的默认值。该方法会把你的自定义默认值放入 [NSRegistrationDomain](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSRegistrationDomain) 域，这样当某项偏好设置没有被显式设置时就会返回这些值。

调用 `registerDefaults:` 方法时，你必须提供一个包含所有待注册默认值的字典。清单 2-1 展示了一个 iOS 应用在启动流程的早期注册默认值的例子。当然，你可以在任何时候注册默认值，但一定要在尝试读取任何偏好设置值之前完成注册。

__清单 2-1__  注册偏好设置的默认值

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
   // 尽早注册偏好设置的默认值。
    NSDictionary *appDefaults = [NSDictionary
        dictionaryWithObject:[NSNumber numberWithBool:YES] forKey:@"CacheDataAgressively"];
    [[NSUserDefaults standardUserDefaults] registerDefaults:appDefaults];

   // 其他初始化工作……
}
```

为标量类型注册默认值时，请使用 [NSNumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/cl/NSNumber) 对象来指定数值。如果你想注册一项值为 URL 的偏好设置，请先用 `NSKeyedArchiver` 的 [archivedDataWithRootObject:](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1413189-archiveddata) 方法把该 URL 编码进一个 [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) 对象。虽然你可以对其他类型的对象采用类似的技巧，但只要有更简单的方案可选，就应该避免这么做。

你可以用 [NSUserDefaults](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/cl/NSUserDefaults) 类的方法来读取和设置偏好设置的值。该类提供了读写布尔型、`integer`、`float` 和 `double` 等标量值偏好设置的方法，也提供了读写值为 [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData)、[NSDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/cl/NSDate)、[NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString)、[NSNumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/cl/NSNumber)、[NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray)、[NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) 和 [NSURL](https://developer.apple.com/documentation/foundation/nsurl) 类型对象的偏好设置的方法。有两种场景下你可能会读取偏好设置的值，有一种场景下你可能会设置它们：

- 读取偏好设置的值：

  - 当你需要用这个值来配置应用的行为时。
  - 当你需要在偏好设置界面中显示这个值时。
- 当用户在你的偏好设置界面中更改了某个值时，设置偏好设置的值。

下面的代码展示了如何在代码中读取一项偏好设置的值。在这个例子中，代码读取了 `CacheDataAggressively` 键的值，这是应用可能用来决定其缓存策略的一个自定义键。类似这样的代码可以用在任何需要处理应用自定义配置的地方。如果你想把这项偏好设置的值展示给用户，也可以用类似的代码来配置偏好设置界面中的控件。

```objc
if ([[NSUserDefaults standardUserDefaults] boolForKey:@"CacheDataAggressively"]) {
   // 删除备份文件。
}
```

要以编程方式设置偏好设置的值，请调用 [NSUserDefaults](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/cl/NSUserDefaults) 中对应的设置方法。设置对象值时，必须使用 [setObject:forKey:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/setObject:forKey:) 方法。调用该方法时，你必须确保对象属于标准属性列表类型之一。下面的例子根据应用偏好设置界面的状态设置了几项偏好设置。

```objc
NSUserDefaults* defaults = [NSUserDefaults standardUserDefaults];
if ([cacheAgressivelyButton state] == NSOnState) {
   // 用户希望积极地缓存文件。
   [defaults setBool:YES forKey:@"CacheDataAggressively"];
   [defaults setObject:[NSDate dateWithTimeIntervalSinceNow:(3600 * 24 * 7)]
             forKey:@"CacheExpirationDate"]; // 设置一周后过期
} else {
    // 用户希望使用惰性缓存。
   [defaults setBool:NO forKey:@"CacheDataAggressively"];
   [defaults removeObjectForKey:@"CacheExpirationDate"];
}
```

你不必为所有值都提供偏好设置界面来管理。你的应用可以用偏好设置来缓存一些有价值的信息。例如，[NSWindow](https://developer.apple.com/documentation/appkit/nswindow) 对象会把自己当前的位置存储在用户默认设置系统中，这样下次用户启动应用时它们就能回到相同的位置。

由于 [NSUserDefaults](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/cl/NSUserDefaults) 类会缓存值，有时需要把缓存的值与用户默认设置数据库的当前内容同步。修改用户默认设置数据库的并不总是只有你的应用。在 iOS 中，「设置」应用可以修改带有 Settings bundle 的应用的偏好设置值。在 OS X 中，系统和其他应用也可能响应用户操作而修改偏好设置的值。例如，如果用户更改了首选语言，系统就会把新值写入用户默认设置数据库。在 OS X v10.5 及更高版本中，共享的 `NSUserDefaults` 对象会按固定周期自动同步其缓存。不过，应用也可以手动调用 [synchronize](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/synchronize) 方法来强制更新缓存中的值。

为了检测偏好设置值何时发生变化，应用还可以注册接收 [NSUserDefaultsDidChangeNotification](https://developer.apple.com/documentation/foundation/userdefaults/1408206-didchangenotification) 通知。每当共享的 `NSUserDefaults` 对象检测到某个持久化域中的偏好设置发生变化时，就会向你的应用发送这个通知。你可以利用这个通知来响应那些可能影响用户界面的变化。例如，你可以用它来检测用户首选语言的变化，并相应地更新应用内容。

Mac 应用可以使用 Cocoa 绑定，直接从用户界面设置偏好设置的值。用绑定来修改偏好设置的做法是：把一个 [NSUserDefaultsController](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller) 对象添加到合适的 nib 文件中，再把控件的值绑定到用户默认设置数据库中的偏好设置值上。当应用显示该界面时，用户默认设置控制器会自动从用户默认设置数据库加载值并用它们设置控件的值。同样地，当用户更改某个控件的值时，用户默认设置控制器也会更新用户默认设置数据库中的值。

关于如何使用 `NSUserDefaultsController` 类把偏好设置值绑定到用户界面的更多信息，请参阅 _[Cocoa 绑定编程主题](../Cocoa%20Bindings%20Programming%20Topics/Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3do2i)_ 中的 [User Defaults and Bindings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/Concepts/NSUserDefaultsController.html#//apple_ref/doc/uid/TP40001092)。

Core Foundation 框架提供了自己的一套接口，用于访问存储在用户默认设置数据库中的偏好设置。与 `NSUserDefaults` 类一样，你可以用 Core Foundation 函数读写偏好设置的值并同步用户默认设置数据库。与 `NSUserDefaults` 不同的是，你可以用 Core Foundation 函数为不同的应用、在不同的计算机上写入偏好设置。注意，修改某些偏好设置域（不属于当前应用和当前用户的那些）需要 root 权限（在 OS X v10.6 之前是管理员权限）；关于如何获取合适的权限，请参阅 _[授权服务编程指南](../../Security/Authorization%20Services%20Programming%20Guide/Introduction%20to%20Authorization%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojv)_。安装在沙盒中的应用无法在应用域之外写入数据。

关于用于读写偏好设置的 Core Foundation 函数的信息，请参阅 _[Preferences Utilities Reference](https://developer.apple.com/documentation/corefoundation/preferences_utilities)_。

偏好设置以键值对的形式存储。键必须是 CFString 对象，而值可以是任意 Core Foundation 属性列表值（参阅 _[Core Foundation 属性列表编程主题](../../Core%20Foundation/Property%20List%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Property%20List%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezta2i)_），包括容器类型。例如，你可能有一个名为 `defaultWindowWidth` 的键，用来定义应用创建的新窗口的宽度（以像素为单位），它的值多半是 CFNumber 类型。你也可以把窗口的宽和高合并成一项名为 `defaultWindowSize` 的偏好设置，并让它的值是一个包含两个 CFNumber 对象的 CFArray 对象。

清单 2-2 中的代码演示了如何为应用 MyTextEditor 创建一项简单的偏好设置。这个例子把应用的默认文本颜色设为蓝色。

__清单 2-2__  写入一项简单的默认设置

```c
CFStringRef textColorKey = CFSTR("defaultTextColor");
CFStringRef colorBLUE = CFSTR("BLUE");

// 设置该偏好设置。
CFPreferencesSetAppValue(textColorKey, colorBLUE,
        kCFPreferencesCurrentApplication);

// 把偏好设置数据写出去。
CFPreferencesAppSynchronize(kCFPreferencesCurrentApplication);
```

注意，只调用 `CFPreferencesSetAppValue` 并不足以创建这项新的偏好设置，还必须调用 `CFPreferencesAppSynchronize` 才能真正保存该值。如果你要写入多项偏好设置，只在设置完最后一个值之后同步一次，比每设置一个值就同步一次更高效。例如，如果你实现的是一个偏好设置面板，可以只在用户按下「好」按钮时才同步。在另一些情况下，你可能希望直到应用退出时才同步——不过要注意，如果应用崩溃，所有未保存的偏好设置都会丢失。

定位并读取偏好设置值最简单的方式是使用 `CFPreferencesCopyAppValue` 函数。该调用会依次搜索各个偏好设置域，直到找到你指定的键为止。如果某项偏好设置是在一个不那么具体的域中设置的（比如「任意应用」域），那么在找不到更具体的版本时，这次调用就会取回该域中的值。清单 2-3 展示了如何读取在[清单 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2ts2jninedglkciffeeskjizdq)中保存的文本颜色偏好设置。

__清单 2-3__  读取一项简单的默认设置

```c
CFStringRef textColorKey = CFSTR("defaultTextColor");
CFStringRef textColor;

// 读取该偏好设置。
textColor = (CFStringRef)CFPreferencesCopyAppValue(textColorKey,
        kCFPreferencesCurrentApplication);
// 用完这个值之后，你必须释放它
// CFRelease(textColor);
```

从偏好设置中返回的所有值都是不可变的，即便你刚刚是用一个可变对象设置的该值。

[下一页](Storing%20Preferences%20in%20iCloud.md)[上一页](About%20the%20User%20Defaults%20System.md)

