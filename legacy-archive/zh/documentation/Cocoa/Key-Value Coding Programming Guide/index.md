---
title: 键值编码编程指南
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html
archived_at: '2026-07-15T07:16:17.113389Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)



## 关于键值编码

键值编码是由 `NSKeyValueCoding` 非正式协议提供的一种机制。对象采用该机制后，可以间接访问自身属性。当对象符合键值编码规范时，可以通过简洁、统一的消息接口，用字符串参数访问其属性。这种间接访问机制是实例变量及其相关访问器方法所提供的直接访问的补充。

通常，你会使用访问器方法访问对象属性。取值访问器（getter）返回属性值，设值访问器（setter）设置属性值。在 Objective-C 中，还可以直接访问属性的底层实例变量。这些访问方式都很直观，但需要调用特定于属性的方法或变量名。随着属性列表增加或变化，访问这些属性的代码也必须随之改变。相比之下，符合键值编码规范的对象会为其所有属性提供一致而简单的消息接口。

键值编码是许多其他 Cocoa 技术的基础概念，例如键值观察、Cocoa 绑定、Core Data 和 AppleScript 脚本支持。在某些情况下，键值编码还能帮助简化代码。

### 使用符合键值编码规范的对象

对象通常通过直接或间接继承 `NSObject` 来采用键值编码。`NSObject` 既采用 `NSKeyValueCoding` 协议，也为其基本方法提供默认实现。其他对象可以通过简洁的消息接口，对这类对象执行以下操作：

- __访问对象属性。__ 该协议指定了通用 getter [valueForKey:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/instm/NSObject/valueForKey:) 和通用 setter [setValue:forKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415969-setvalue) 等方法，用于通过属性名称（即以字符串参数表示的键）访问对象属性。这些方法及相关方法的默认实现会使用键定位底层数据并与之交互，具体参阅[访问对象属性](BasicPrinciples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3talkciffekqkjivcq)。
- __操作集合属性。__ 访问方法的默认实现会像处理其他属性一样处理对象的集合属性（例如 `NSArray` 对象）。此外，如果对象为某个属性定义了集合访问器方法，就可以通过键值方式访问集合内容。这通常比直接访问更高效，并允许你通过标准化接口操作自定义集合对象，具体参阅[访问集合属性](AccessingCollectionProperties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedilktk4yq)。
- __对集合对象调用集合运算符。__ 访问符合键值编码规范的对象中的集合属性时，可以在键字符串中插入_集合运算符_，如[使用集合运算符](CollectionOperators.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tmlkciffekqkjivcq)所述。集合运算符指示默认的 `NSKeyValueCoding` getter 实现对集合执行操作，然后返回经过筛选的新集合，或表示集合某项特征的单个值。
- __访问非对象属性。__ 协议的默认实现可以检测标量和结构体等非对象属性，并自动将其装箱为对象或从对象拆箱，以便在协议接口中使用，具体参阅[表示非对象值](DataTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tclkciffekqkjivcq)。此外，该协议还声明了一个方法，允许符合规范的对象在通过键值编码接口为非对象属性设置 `nil` 时采取适当操作。
- __通过键路径访问属性。__ 如果存在由符合键值编码规范的对象组成的层级结构，可以使用基于键路径的方法调用深入其中，只需一次调用即可获取或设置层级深处的值。

### 让对象采用键值编码

要让自己的对象符合键值编码规范，需要确保它们采用 `NSKeyValueCoding` 非正式协议并实现相应方法，例如将 [valueForKey:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/instm/NSObject/valueForKey:) 作为通用 getter，将 [setValue:forKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415969-setvalue) 作为通用 setter。幸运的是，如上所述，[NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intf/NSObject) 已采用该协议，并为这些方法及其他基本方法提供默认实现。因此，只要对象派生自 `NSObject`（或其众多子类之一），大部分工作就已经完成。

为了让默认方法正常工作，需要确保对象的访问器方法和实例变量遵循明确定义的模式。这样，默认实现便能在响应键值编码消息时找到对象属性。随后，你可以选择提供验证方法和处理某些特殊情况的方法，以扩展和自定义键值编码。

### 在 Swift 中使用键值编码

继承自 `NSObject` 或其某个子类的 Swift 对象，其属性默认符合键值编码规范。在 Objective-C 中，属性访问器和实例变量必须遵循特定模式，而 Swift 中的标准属性声明会自动保证这一点。另一方面，该协议的许多功能要么与 Swift 无关，要么更适合使用 Objective-C 中不存在的原生 Swift 构造或技术来处理。例如，由于所有 Swift 属性都是对象，因此永远不会用到默认实现对非对象属性的特殊处理。

因此，尽管键值编码协议方法可以直接映射到 Swift，本指南仍主要关注 Objective-C：在 Objective-C 中，需要做更多工作才能确保符合规范，而且键值编码通常也更有用。本指南会在各处注明需要在 Swift 中采用显著不同方式的情况。

有关将 Swift 与 Cocoa 技术结合使用的更多信息，请阅读《配合 Cocoa 和 Objective-C 使用 Swift（Swift 3）》。有关 Swift 的完整说明，请阅读《Swift 编程语言（Swift 3）》。

### 其他 Cocoa 技术依赖键值编码

符合键值编码规范的对象可以参与许多依赖这种访问方式的 Cocoa 技术，包括：

- __键值观察。__ 该机制允许对象注册由其他对象属性变化触发的异步通知，具体参阅《[键值观察编程指南](../Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)》。
- __Cocoa 绑定。__ 这组技术完整实现了模型—视图—控制器范式：模型封装应用数据，视图显示和编辑这些数据，控制器在两者之间进行协调。阅读《[Cocoa 绑定编程主题](../Cocoa%20Bindings%20Programming%20Topics/Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3do2i)》，进一步了解 Cocoa 绑定。
- __Core Data。__ 该框架为对象生命周期和对象图管理（包括持久化）相关的常见任务提供通用的自动化解决方案。有关 Core Data 的内容，请参阅《[Core Data 编程指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)》。
- __AppleScript。__ 这种脚本语言可以直接控制支持脚本的应用以及 macOS 的许多部分。Cocoa 的脚本支持利用键值编码获取和设置可脚本化对象中的信息。`NSScriptKeyValueCoding` 非正式协议中的方法为键值编码提供了额外功能，包括按多值键中的索引获取和设置键值，以及将键值强制转换为适当的数据类型。《[AppleScript 概览](../../Apple%20Script/AppleScript%20Overview/Introduction%20to%20AppleScript%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tm2i)》从较高层面概述了 AppleScript 及其相关技术。

[访问对象属性](BasicPrinciples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3talkciffekqkjivcq)
