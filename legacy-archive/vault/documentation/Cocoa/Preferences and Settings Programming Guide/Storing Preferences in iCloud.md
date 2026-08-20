---
title: 偏好与设置编程指南
apple_id: 10000059i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UserDefaults/StoringPreferenceDatainiCloud/StoringPreferenceDatainiCloud.html
archived_at: '2026-07-15T07:21:03.235822Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [偏好与设置编程指南](About%20Preferences%20and%20Settings.md)


[下一页](Implementing%20an%20iOS%20Settings%20Bundle.md)[上一页](Accessing%20Preference%20Values.md)

# 在 iCloud 中存储偏好设置

应用可以使用 iCloud 键值存储，与运行在用户其他电脑和 iOS 设备上的自身实例共享少量数据。键值存储适用于像偏好设置那样的简单数据类型。例如，一个杂志应用可以存储用户当前正在阅读的期号和页码，这样该应用的其他实例启动时就能直接打开同一页。你不应该用这个存储来保存大量数据或复杂的数据类型。

要使用 iCloud 键值存储，请执行以下步骤：

1. 在 Xcode 中，为你的应用配置 `com.apple.developer.ubiquity-kvstore-identifier` 授权（entitlement）。
2. 在代码中创建共享的 [NSUbiquitousKeyValueStore](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore) 对象，并注册接收变更通知。
3. 使用 `NSUbiquitousKeyValueStore` 的方法读写值。

iCloud 中的键值数据仅限于简单的属性列表类型（字符串、数字、日期等）。

键值存储并不是为存储大量数据而设计的，它的用途是存储配置数据、偏好设置以及少量与应用相关的数据。要判断键值存储是否适合你的需求，可以考虑以下几点：

- 每个应用在键值存储中最多只能占用 1 MB 的总空间。（此外还有单个键 1 MB 的独立限制，最多允许 1024 个键。）因此，你无法用键值存储来共享大量数据。
- 键值存储只支持属性列表类型。属性列表类型包括 `NSNumber`、`NSString` 和 `NSDate` 对象这类简单类型。你也可以把原始数据块存入 `NSData` 对象，并用 `NSArray` 和 `NSDictionary` 对象来组织所有这些类型。
- 键值存储是为存储不常变化的数据而设计的。如果某台设备上的应用频繁修改键值存储，系统可能会推迟同步部分变更，以尽量减少与服务器往返通信的次数。应用改动得越频繁，后续变更被推迟、无法立即出现在其他设备上的可能性就越大。
- 键值存储并不能取代偏好设置或其他保存同类数据的本地手段。键值存储的目的是在多个应用之间共享数据，但如果 iCloud 未启用或在某台设备上不可用，你可能仍然需要在本地保留一份数据副本。

如果你用键值存储来共享偏好设置，一种做法是把实际的值存在用户默认设置数据库中，再用键值存储来同步它们。（如果你不想使用偏好设置系统，也可以把变更保存在自定义的属性列表文件或其他本地存储中。）当你在本地更改某个键的值时，请同时把该变更写入用户默认设置数据库和 iCloud 键值存储。为了接收来自外部的变更，请为 [NSUbiquitousKeyValueStoreDidChangeExternallyNotification](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1412267-didchangeexternallynotification) 通知添加一个观察者，并在处理方法中检测哪些键在外部发生了变化，然后更新用户默认设置数据库中的对应数据。这样一来，你的用户默认设置数据库中始终保存着正确的配置值，而 iCloud 键值存储只是一种确保用户默认设置数据库拿到最新变更的机制。

为了使用键值存储，应用必须显式配置 `com.apple.developer.ubiquity-kvstore-identifier` 授权。你可以用 Xcode 启用该授权并为应用指定它的值，具体做法参见 _App Distribution Guide_ 中的 Adding iCloud Support。

启用键值存储后，Xcode 会自动根据你的应用的 bundle 标识符为容器字段填入一个默认值。对大多数应用来说，这个默认值正是你想要的。不过，如果你的应用要与另一个应用共享键值存储，就必须改为指定另一个应用的 bundle 标识符。例如，如果你的应用有一个精简版，你可能希望它使用与付费版相同的键值存储。

要使用共享的 [NSUbiquitousKeyValueStore](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore) 对象，你只需启用该授权即可。只要授权配置好且包含有效的值，键值存储对象就会把数据写入用户 iCloud 账户中的相应位置。如果连接指定的 iCloud 容器时出现问题，任何读写键值的尝试都会失败。为了确保键值存储配置正确且可访问，你应当在应用启动流程的早期执行类似下面的代码：

```objc
NSUbiquitousKeyValueStore* store = [NSUbiquitousKeyValueStore defaultStore];
[[NSNotificationCenter defaultCenter] addObserver:self
          selector:@selector(updateKVStoreItems:)
          name:NSUbiquitousKeyValueStoreDidChangeExternallyNotification
          object:store];
[store synchronize];
```

建议在应用启动流程的早期创建键值存储对象，因为这能确保你的应用及时收到来自 iCloud 的更新。判断键和值是否发生变化的最佳方式，是注册接收 [NSUbiquitousKeyValueStoreDidChangeExternallyNotification](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1412267-didchangeexternallynotification) 通知。而在启动时，你应当手动调用 [synchronize](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1415989-synchronize) 方法，以检测外部是否做过任何变更。在应用运行期间的其他时刻，你不需要调用该方法。

关于如何为 iOS 应用配置授权的更多信息，请参阅 _App Distribution Guide_ 中的 Adding Capabilities。

你可以使用 [NSUbiquitousKeyValueStore](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore) 类的方法来读写键值存储中的值。该类提供了读写布尔型、`long long` 和 `double` 等标量值偏好设置的方法，也提供了读写值为 [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData)、[NSDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/cl/NSDate)、[NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString)、[NSNumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/cl/NSNumber)、[NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray) 或 [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) 对象的键的方法。

如果你把键值存储用作更新本地偏好设置的手段，可以用类似清单 3-1 中的代码来协调对用户默认设置数据库的更新。这个例子假定你在 iCloud 和用户默认设置数据库中使用了相同的键名及对应的值，同时也假定你此前已把 `updateKVStoreItems:` 方法注册为响应 [NSUbiquitousKeyValueStoreDidChangeExternallyNotification](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1412267-didchangeexternallynotification) 通知时要调用的方法。

__清单 3-1__  使用 iCloud 更新本地偏好设置的值

```objc
- (void)updateKVStoreItems:(NSNotification*)notification {
   // 获取发生变化的键的列表。
   NSDictionary* userInfo = [notification userInfo];
   NSNumber* reasonForChange = [userInfo objectForKey:NSUbiquitousKeyValueStoreChangeReasonKey];
   NSInteger reason = -1;

   // 如果无法确定变更原因，就什么都不更新。
   if (!reasonForChange)
      return;

   // 只针对来自服务器的变更做更新。
   reason = [reasonForChange integerValue];
   if ((reason == NSUbiquitousKeyValueStoreServerChange) ||
         (reason == NSUbiquitousKeyValueStoreInitialSyncChange)) {
      // 如果有内容在外部发生了变化，就取回这些变更
      // 并在本地更新对应的键。
      NSArray* changedKeys = [userInfo objectForKey:NSUbiquitousKeyValueStoreChangedKeysKey];
      NSUbiquitousKeyValueStore* store = [NSUbiquitousKeyValueStore defaultStore];
      NSUserDefaults* userDefaults = [NSUserDefaults standardUserDefaults];

      // 这个循环假定你在用户默认设置数据库和 iCloud 键值存储中
      // 使用了相同的键名
      for (NSString* key in changedKeys) {
         id value = [store objectForKey:key];
         [userDefaults setObject:value forKey:key];
      }
   }
}
```


每一次对 [NSUbiquitousKeyValueStore](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore) 方法的调用都被视为一次原子事务。把该事务的数据传输到 iCloud 时，整个事务要么全部失败，要么全部成功。如果成功，所有键都会被写入存储；如果失败，则一个键也不会被写入，不存在只写入部分键的情况。发生失败时，系统还会生成一个包含失败原因的 [NSUbiquitousKeyValueStoreDidChangeExternallyNotification](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1412267-didchangeexternallynotification) 通知。如果你在使用键值存储，就应当利用这个通知来发现可能存在的问题。

如果你有一组键，它们的值必须同时更新才有效，那就把它们放在同一个事务中一起保存。要在单次事务中写入多个键和值，请创建一个包含所有键和值的 [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) 对象，然后用 [setDictionary:forKey:](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1417155-setdictionary) 方法把这个字典对象写入键值存储。整体写入一个包含所有变更的字典，可以确保这些键要么全部写入，要么一个都不写入。

[下一页](Implementing%20an%20iOS%20Settings%20Bundle.md)[上一页](Accessing%20Preference%20Values.md)

