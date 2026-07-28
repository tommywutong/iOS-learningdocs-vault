---
title: UserDefaults
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/userdefaults
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults.json'
content_hash: 'sha256:cca056467d7ad6e1'
translated: true
---

> 导航： [技术](../technologies.md) · [Foundation](../foundation.md)

# UserDefaults

<sub>类</sub>

用户默认数据库的接口，该数据库存储系统级和 App 专属的设置。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UserDefaults
```

## 概述

`UserDefaults` 对象提供对默认系统的访问，这是一个用于 App 专属和系统级设置的持久化存储（persistent store）。你使用该系统来存储非敏感信息，例如 App 专属的配置细节。系统还存储适用于所有 App 的配置细节，例如设备的当前语言设置。在你的代码中，你检查该系统中的值，并使用它们动态地改变 App 的外观或行为。术语“默认”（defaults）指的是存储的数据决定了默认的启动状态和行为。

> [!important] 重要
> 不要将个人或敏感信息存储为设置。默认系统以未加密的格式将信息存储在磁盘上。请将个人或敏感信息存储在用户的钥匙串（Keychain）中。

要访问默认系统，获取一个 `UserDefaults` 对象并调用其方法来读写值。[standardUserDefaults](userdefaults/standard.md) 对象是一个共享对象，用于读写 App 的标准设置。你也可以创建唯一的 `UserDefaults` 对象来管理特定的设置集。例如，你可以创建一个 `UserDefaults` 对象，用于读写你的 App 与 App 扩展共享的设置。不要子类化（subclass）`UserDefaults`。

存储在默认对象中的每个项目都由一个键值对组成，其中每个键是用于定位项目的字符串，每个值是一个数据对象。默认数据库支持与属性列表（property list）文件相同的值类型，包括 [Int](../swift/int.md)、[Float](../swift/float.md)、[Double](../swift/double.md)、[Bool](../swift/bool.md)、[String](../swift/string.md)、[URL](url.md)、[NSNumber](nsnumber.md)、[Date](date.md)、[Array](../swift/array.md) 和 [Dictionary](../swift/dictionary.md) 等类型。要将其他类型的对象包含在默认数据库中，先将其归档为 [Data](data.md) 对象，然后存储该对象。尽可能优先使用简单类型而非自定义对象。

除了教育机构中的受管设备外，系统将默认设置本地存储在当前设备上。当你向 `UserDefaults` 对象写入值时，该对象会立即更新其内存中的该信息版本，并异步地将值写入磁盘。当用户备份其设备时，系统会将所有持久化默认数据库包含在备份数据中。由于数据是设备特定的，你不使用默认系统在设备之间共享数据。要在用户的设备之间共享数据，改用 [NSUbiquitousKeyValueStore](nsubiquitouskeyvaluestore.md)。

> [!warning] 警告
> 不要直接从文件系统访问默认数据库的文件。直接修改底层文件可能导致数据丢失、更改延迟生效或 App 崩溃。在 macOS 上，使用 `defaults` 命令行工具安全地查看或修改 App 外部的默认数据库。

当你的 App 运行时，默认系统会生成通知，让你知道值何时发生变化。要观察对单个设置的更改，向你的 `UserDefaults` 对象添加一个[键值观察者（key-value observer）](../swift/using-key-value-observing-in-swift.md)，使用键名构建指向你想要设置的路径。要观察对所有设置的更改，请使用你的 `UserDefaults` 对象注册 [DidChangeMessage](userdefaults/didchangemessage.md) 或 [NSUserDefaultsDidChangeNotification](userdefaults/didchangenotification.md)。

`UserDefaults` 类型是线程安全的（thread-safe），你可以在多个线程或任务（tasks）中同时使用同一个对象。

> [!important] 重要
> 此 API 可能被滥用于访问设备信号以尝试识别设备或用户，也称为指纹识别（fingerprinting）。无论用户是否授予你的 App 跟踪权限，都不允许进行指纹识别。当你在 App 或第三方 SDK（非 Apple 提供的 SDK）中使用此 API 时，请在 App 或第三方 SDK 的 `PrivacyInfo.xcprivacy` 文件中声明你的使用情况和使用原因。有关更多信息，包括使用此 API 的有效原因列表，请参阅[描述必需原因 API](../bundleresources/describing-use-of-required-reason-api.md)。

### 域与设置搜索路径

为了整合来自不同来源的设置，默认系统将它们组织成域。App 定义其自己的自定义设置，但系统定义的设置适用于所有 App。同样，你可能选择临时覆盖特定设置以测试 App 的某个功能。默认系统为这些情况以及其他一些情况提供了域。

当你请求某个设置的值时，`UserDefaults` 对象按其特定顺序搜索其域，直到找到你想要的值。下表列出了默认系统支持的关键域及其搜索顺序。某些域可能并非对所有 App 都存在。例如，受管域仅存在于管理员管理的设备上。

| 域 | 类型 | 描述 |
|---|---|---|
| Managed | 持久化 | 此域包含管理员为受管设备提供的设置。系统将这些值持久化保存在当前设备上。 |
| [Argument](userdefaults/argumentdomain.md) | 易失性 | 此域包含你从命令行或 Xcode 启动 App 时指定的设置。这些键代表设置的临时覆盖，系统在 App 退出后丢弃它们。 |
| Educational managed | 持久化 | 对于教育机构中的受管设备，此域包含为该机构保存到 iCloud 键值存储的任何设置。系统将这些设置持久化保存在服务器上，而不是设备上。 |
| App | 持久化 | 此域包含你的 App 保存的设置，无论是通过编程方式还是使用其设置界面。每个 `UserDefaults` 对象都将设置写入此组，并将它们与 App 本身或用于初始化该对象的 App Group 关联。系统将这些设置持久化保存在当前设备上。 |
| Suite | 持久化 | 此域包含来自 App Group 或你在运行时指定的其他 App 的自定义设置。默认情况下此域不存在，但你可以使用 [- addSuiteNamed:](<userdefaults/addsuite(named_).md>) 方法添加一个套件（suite）。系统将这些设置持久化保存在当前设备上。 |
| [Global](userdefaults/globaldomain.md) | 持久化 | 此域包含系统上所有 App 都存在的键。系统提供此域的键，App 无法向其中写入。系统将这些设置持久化保存在当前设备上。 |
| [Registration](userdefaults/registrationdomain.md) | 易失性 | 此域包含系统提供的默认值以及你在启动时为 App 注册的默认值。注册一组默认值可防止你的代码在请求设置时收到 `nil` 值。当你的 App 退出时，系统会丢弃这些值，因此你必须在每次 App 启动时重新注册它们。 |

系统将大多数持久化域的数据存储在当前设备上，并且不与其他设备共享该数据。要在用户的所有设备之间共享设置，请使用 [NSUbiquitousKeyValueStore](nsubiquitouskeyvaluestore.md) 对象保存它们。

### 受管环境中的设置

如果你的 App 支持受管环境，管理员可能会为任何受管设备配置一组默认设置。例如，在计算机实验室或教室环境中，老师可能设置课程所需的默认设置。App 无法写入受管域，因此如果你的 App 遇到受管设置，请禁用或隐藏任何用户可能用于更改该设置值的控制（control）。要确定某个设置是否受管，调用你的 `UserDefaults` 对象的 [- objectIsForcedForKey:](<userdefaults/objectisforced(forkey_).md>) 或 [- objectIsForcedForKey:inDomain:](<userdefaults/objectisforced(forkey_indomain_).md>) 方法。

在受管设备上运行的 App 可以使用 [NSUbiquitousKeyValueStore](nsubiquitouskeyvaluestore.md) 与用户的其他设备共享少量数据。将这种存储用于你的 App 可以安全地与其自身其他实例共享的数据。例如，教科书 App 可能会保存当前页码，以便用户可以在其任何设备上从同一位置继续阅读。

有关管理设备的更多详细信息，请参阅[设备管理](../devicemanagement.md)。

### 沙盒注意事项

沙盒化（Sandboxed）的 App 无法访问或修改另一个 App 或进程的设置，但以下情况除外：

- App 可以修改其某个 App 扩展的设置。
- App 可以修改其所属的 App Group 的设置。

如果你使用 [- addSuiteNamed:](<userdefaults/addsuite(named_).md>) 方法添加不相关 App 的标识符，该方法不会让你访问其他 App 的设置。相反，系统会将更改写入你的 App 的设置，而不是第三方 App 的设置。

> [!important] 重要
> 访问套件中设置的 App 还必须具有 [App Groups entitlement](../bundleresources/entitlements/com.apple.security.application-groups.md)。

## 关系

- **继承自**： [NSObject](../objectivec/nsobject-swift.class.md)

- **遵循**： [CVarArg](../swift/cvararg.md)，[CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)，[CustomStringConvertible](../swift/customstringconvertible.md)，[Equatable](../swift/equatable.md)，[Hashable](../swift/hashable.md)，[NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## 主题

### 创建用户默认对象

- [standardUserDefaults](userdefaults/standard.md) — 当前 App 的共享默认对象。
- [- init](<userdefaults/init().md>) — 创建一个新的默认对象，并使用 App 的当前设置对其进行初始化。
- [- initWithSuiteName:](<userdefaults/init(suitename_).md>) — 创建一个新的默认对象，并使用来自指定数据库的设置对其进行初始化。

### 注册默认设置

- [- registerDefaults:](<userdefaults/register(defaults_).md>) — 指定在 App 域没有设置时用作后备方案的默认设置和值集。

### 获取键的值

- [- boolForKey:](<userdefaults/bool(forkey_).md>) — 返回与指定键关联的布尔值。
- [- integerForKey:](<userdefaults/integer(forkey_).md>) — 返回与指定键关联的整数值。
- [- floatForKey:](<userdefaults/float(forkey_).md>) — 返回与指定键关联的浮点值。
- [- doubleForKey:](<userdefaults/double(forkey_).md>) — 返回与指定键关联的双精度值。
- [- URLForKey:](<userdefaults/url(forkey_).md>) — 返回与指定键关联的 URL。
- [- stringForKey:](<userdefaults/string(forkey_).md>) — 返回与指定键关联的字符串。
- [- stringArrayForKey:](<userdefaults/stringarray(forkey_).md>) — 返回与指定键关联的字符串数组。
- [- dataForKey:](<userdefaults/data(forkey_).md>) — 返回与指定键关联的数据对象。
- [- objectForKey:](<userdefaults/object(forkey_).md>) — 返回与指定键关联的对象。
- [- arrayForKey:](<userdefaults/array(forkey_).md>) — 返回与指定键关联的数组。
- [- dictionaryForKey:](<userdefaults/dictionary(forkey_).md>) — 返回与指定键关联的字典对象。
- [- dictionaryRepresentation](<userdefaults/dictionaryrepresentation().md>) — 返回一个包含来自所有域的所有键值对并集的字典。

### 设置键的值

- [- setBool:forKey:](<userdefaults/set(__forkey_)-3nn5m.md>) — 将指定键的值设置为布尔值。
- [- setInteger:forKey:](<userdefaults/set(__forkey_)-3v852.md>) — 将指定键的值设置为整数。
- [- setFloat:forKey:](<userdefaults/set(__forkey_)-1t5ec.md>) — 将指定键的值设置为浮点数。
- [- setDouble:forKey:](<userdefaults/set(__forkey_)-2w22f.md>) — 将指定键的值设置为双精度数。
- [- setURL:forKey:](<userdefaults/set(__forkey_)-2bqjt.md>) — 将指定键的值设置为 URL。
- [- setObject:forKey:](<userdefaults/set(__forkey_)-8ab6d.md>) — 将指定键的值设置为属性列表对象。

### 监控设置更改和问题

- [DidChangeMessage](userdefaults/didchangemessage.md) — 当用户默认设置更改时系统发送的消息。
- [NSUserDefaultsDidChangeNotification](userdefaults/didchangenotification.md) — 在当前进程更改设置的值时发布。
- [SizeLimitExceededMessage](userdefaults/sizelimitexceededmessage.md) — 当默认数据库中数据的大小超过最大值时系统发送的消息。
- [NSUserDefaultsSizeLimitExceededNotification](userdefaults/sizelimitexceedednotification.md) — 当默认数据库中的数据量超过允许的最大值时发布。

### 移除设置值

- [- removeObjectForKey:](<userdefaults/removeobject(forkey_).md>) — 从默认数据库中移除指定键的值。

### 添加和移除搜索域

- [- addSuiteNamed:](<userdefaults/addsuite(named_).md>) — 将指定域的设置插入当前对象的搜索列表。
- [- removeSuiteNamed:](<userdefaults/removesuite(named_).md>) — 从当前对象的搜索列表中移除指定的域。

### 获取域名

- [NSArgumentDomain](userdefaults/argumentdomain.md) — 包含命令行设置的域的标识符。
- [NSGlobalDomain](userdefaults/globaldomain.md) — 包含系统为所有 App 指定的设置的域的标识符。
- [NSRegistrationDomain](userdefaults/registrationdomain.md) — 包含 App 的已注册默认值的域的标识符。
- [volatileDomainNames](userdefaults/volatiledomainnames.md) — 与当前对象关联的易失性域的标识符数组。

### 管理域特定值

- [- persistentDomainForName:](<userdefaults/persistentdomain(forname_).md>) — 从指定的持久化域中检索设置。
- [- setPersistentDomain:forName:](<userdefaults/setpersistentdomain(__forname_).md>) — 用你提供的新键和值替换指定域中的键和值。
- [- volatileDomainForName:](<userdefaults/volatiledomain(forname_).md>) — 从指定的易失性域中检索设置。
- [- setVolatileDomain:forName:](<userdefaults/setvolatiledomain(__forname_).md>) — 用你提供的新键和值替换指定域中的键和值。
- [- removePersistentDomainForName:](<userdefaults/removepersistentdomain(forname_).md>) — 从指定的持久化域中移除键和值。
- [- removeVolatileDomainForName:](<userdefaults/removevolatiledomain(forname_).md>) — 从指定的易失性域中移除键和值。

### 检查受管键

- [- objectIsForcedForKey:](<userdefaults/objectisforced(forkey_).md>) — 返回一个布尔值，指示管理员是否为指定的键提供了值。
- [- objectIsForcedForKey:inDomain:](<userdefaults/objectisforced(forkey_indomain_).md>) — 返回一个布尔值，指示管理员是否为指定域中的键提供了值。

### 已废弃

- [- initWithUser:](<userdefaults/init(user_).md>) — 创建一个用指定用户帐户的默认值初始化的用户默认对象。_(已废弃)_
- [- synchronize](<userdefaults/synchronize().md>) — 等待默认数据库的任何待处理的异步更新并返回；此方法已无必要且不应使用。
- [+ resetStandardUserDefaults](<userdefaults/resetstandarduserdefaults().md>) — 此方法无效且不应使用。
- [- persistentDomainNames](<userdefaults/persistentdomainnames().md>) — 返回当前持久化域名的数组。_(已废弃)_
- [NSUbiquitousUserDefaultsCompletedInitialSyncNotification](userdefaults/completedinitialcloudsyncnotification.md) — 当 iCloud 默认值完成数据下载时发布，无论是设备首次连接到 iCloud 账户还是用户切换其主 iCloud 账户时。_(已废弃)_
- [NSUbiquitousUserDefaultsDidChangeAccountsNotification](userdefaults/didchangecloudaccountsnotification.md) — 当用户更改主 iCloud 账户时发布。_(已废弃)_
- [NSUbiquitousUserDefaultsNoCloudAccountNotification](userdefaults/nocloudaccountnotification.md) — 当设置云默认值但未登录 iCloud 用户时发布。_(已废弃)_
- [语言相关依赖信息常量](language-dependent-information-constants.md) — 这些常量已废弃，不应使用。

## 另请参阅

### App 专属设置

- [从代码访问设置](accessing-settings-from-your-code.md) — 在 App 运行时检索或更改设置，并监控这些值的外部更改。
