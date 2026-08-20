---
title: 在 Swift 中构建更优质的 Core Data 模型
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2015/02/17/better-coredata-models-in-swift/'
original_language: en
published: 2015-02-17
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e5501cbadf3b1679'
translated: true
---

> 原文：[Better Core Data models in Swift](https://www.jessesquires.com/blog/2015/02/17/better-coredata-models-in-swift/)　·　Jesse Squires

随着我继续在 [Core Data](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/) 和 [Swift](http://www.apple.com/swift/) 上工作，我一直试图找到让 Core Data **更好**的方法。我的目标之一是清晰与安全，尤其是在类型方面。幸运的是，我们可以利用 Swift 的可选类型、枚举和其他特性来让托管对象（managed object）更加健壮和清晰。但即便 Swift 带来了这些改进，Xcode 目前的工具集仍存在一些缺陷和限制。

### 可选类型的绝佳应用场景

社区中关于[可选类型（optional）](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/TheBasics.html#//apple_ref/doc/uid/TP40014097-CH5-ID330)以及它们[使用起来往往很繁琐](http://natashatherobot.com/unit-testing-optionals-in-swift-xctassertnotnil/)的[反馈](http://owensd.io/2014/10/18/optionals-beware.html)已经很多了。然而，这种相对简单的构造为 Core Data 中的托管对象带来了令人欣喜的清晰度。在 Core Data 中定义实体（entity）时，可以在 Data Model Inspector 中为实体的特性（attribute）设置一些基本的验证规则。

![Core Data 模型检查器示意图](https://www.jessesquires.com/img/blog/coredata_inspector.jpg)

<sub>Core Data 托管对象的 Data Model Inspector</sub>

你可以定义最小值和最大值，提供默认值，将特性标记为可选值，等等。这并不新鲜。但在 Objective-C 中，托管对象上某个属性（property）是否为可选值，只能通过在 Xcode 中打开 `.xcdatamodeld` 文件，然后选中实体，再选中特性，最后在侧边栏中打开 Data Model Inspector 才能发现。或者，在运行时你才发现你的 `NSManagedObjectContext` 因为 `Cocoa error 1570` 而无法保存。这两种体验都不令人愉快。

例如，假设我们有下面的 `Employee` 类。哪些字段是成功保存所必需的？

```
@interface Employee : NSManagedObject

@property (nonatomic, retain) NSString * address;
@property (nonatomic, retain) NSDate * dateOfBirth;
@property (nonatomic, retain) NSString * email;

@property (nonatomic, retain) NSString * firstName;
@property (nonatomic, retain) NSString * lastName;
@property (nonatomic, retain) NSString * middleName;

@property (nonatomic, retain) NSDecimalNumber * salary;
@property (nonatomic, retain) NSNumber * status;

@end
```

相比之下，在使用 Swift 时，我们只需查看代码就能立刻知道哪些属性是可选的。

```
class Employee: NSManagedObject {

    @NSManaged var address: String?
    @NSManaged var dateOfBirth: NSDate
    @NSManaged var email: String?

    @NSManaged var firstName: String
    @NSManaged var lastName: String
    @NSManaged var middleName: String?

    @NSManaged var salary: NSDecimalNumber
    @NSManaged var status: Int32
}
```

**注意：** Xcode 在生成 Swift 类时，如果涉及可选特性，并不会准确地处理。你必须手动为可选值加上 `?`。此外，尽管 _The Swift Programming Language_ 指南[推荐](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/TheBasics.html#//apple_ref/doc/uid/TP40014097-CH5-ID317)对所有整型变量使用 `Int`，但 Core Data 推荐使用特定的整型尺寸，并且如果你尝试使用其他类型会报错，因此 `status` 属性使用了 `Int32`。

这似乎是一个小细节，但却是一个巨大的进步——尤其是在你开始在 App 的其他部分使用你的模型时。与一般情况下的可选类型一样，你需要显式地处理 `nil`（我认为这是一个积极的副作用）。但即使没有了[_末日金字塔_](http://www.scottlogic.com/blog/2014/12/08/swift-optional-pyramids-of-doom.html)，如果你有大量可选类型，这仍然可能不那么愉快。如果是这样，希望这能促使你_重新考虑你的设计_。这个字段_真的_必要吗？这个属性能从其他数据推导出来吗？这个属性是否应该是_必需的_？这些都是设计模型类时始终应该问自己的问题，但也许 Objective-C 的宽松性让这些问题以前被忽略了。**可选类型会让你的模型复杂化**，这是一个很好的动机来尽可能少地使用它们，并保持简单。

鉴于此，让我们重新审视一下我们的 `Employee` 类。`middleName` 重要吗？不重要，我们移除它。假设我们知道所有员工的邮箱地址格式都为 `<firstName><LastName>@<companyName>.com`。我们真的需要存储它吗？不需要，我们可以写一个函数或计算属性来生成它。最后，我们假设员工必须有 `address` 字段。啊，现在看起来好多了。

```
class Employee: NSManagedObject {

    @NSManaged var address: String
    @NSManaged var dateOfBirth: NSDate

    @NSManaged var firstName: String
    @NSManaged var lastName: String

    @NSManaged var salary: NSDecimalNumber
    @NSManaged var status: Int32
}
```

### 利用 `typealias`

我们可以使用的另一个 Swift 特性是[类型别名声明](https://developer.apple.com/library/prerelease/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Declarations.html#//apple_ref/doc/uid/TP40014097-CH34-ID361)，它允许为一个已有类型创建一个新名称。对于 `Employee` 来说，使用 `Salary` 类型而不是 `NSDecimalNumber` 类型来工作会非常有帮助。在代码库的深处，可能有一些对 `NSDecimalNumber` 值的操作，但这些值代表什么并不清楚。一个 `typealias` 使我们的模型更具描述性，并允许我们对一个更具表现力的 `Salary` 类型进行操作。

```
class Employee: NSManagedObject {
    // 其他属性...

    typealias Salary = NSDecimalNumber

    @NSManaged var salary: Salary
}
```

然后我们可以编写接收和返回 `Employee.Salary` 类型的函数。这样的函数可以保持简洁，同时最大化其清晰度。

```
func computeRaise(salary: Employee.Salary) -> Employee.Salary
```

正如 [objc.io](http://www.objc.io) 所指出的，_我们可以更进一步_，通过使用[包装类型](http://www.objc.io/snippets/8.html)。要在 `NSManagedObject` 的子类中实现这一点，我们需要做一些包装和解包的工作（并非双关语）。首先，Core Data 中的原始属性应被标记为 `private`。然后，我们可以为新的包装类型使用一个计算属性，该属性在私有属性值与包装值之间进行转换。这需要一些工作，但我们从中获得的清晰度和安全性是完全值得的。

```
struct Salary {
    let amount: NSDecimalNumber
}

class Employee: NSManagedObject {
    // 其他属性...

    @NSManaged private var salaryAmount: NSDecimalNumber

    var salary: Salary {
        get {
            return Salary(amount: self.salaryAmount)
        }
        set {
            self.salaryAmount = newValue.amount
        }
    }
}

// 用法
employee.salary = Salary(amount:10000.0)
```

不幸的是，对于获取请求（fetch request），你仍然需要使用底层的私有属性名称 `salaryAmount`。这是因为 Core Data 不知道 `salary` 计算属性，也不知道 `Salary` 类型。不过，我认为这里使用的命名约定可以将混淆降到最低。也就是说，`salary.amount` 对应的是私有属性 `salaryAmount`。

### 使用 Swift 枚举

模型对象将某种状态编码为枚举（`enum`）的情况并不少见。对于 Objective-C，你可以定义一个 `NS_ENUM` 并在托管对象中存储一个整型属性。但 Objective-C 中的 `enum` 不过是一个美化了的整数。通过采用类似于上面包装类型的方法，我们可以直接在托管对象中获得 Swift `enum` 的所有强大功能。这非常有用。

让我们看看这在 `Employee` 类的 `status` 属性上是什么样的。

```
enum EmployeeStatus: Int32 {
    case ReadyForHire, Hired, Retired, Resigned, Fired, Deceased
}

class Employee: NSManagedObject {
    // 其他属性...

    @NSManaged private var statusValue: Int32

    var status: EmployeeStatus {
        get {
            return EmployeeStatus(rawValue: self.statusValue)!
        }
        set {
            self.statusValue = newValue.rawValue
        }
    }
}

// 用法
employee.status = .Hired
```

**注意：** 和之前的例子一样，对于获取请求，你仍然需要使用私有属性名称 `statusValue`。

此外，这并不局限于整数。你可以将此策略应用于 Core Data 支持的**任何**类型的枚举。例如，对于 `Employee`，可能有固定的薪资数额对应于员工的角色。稍加努力，你甚至可以支持带有[关联值](https://developer.apple.com/library/prerelease/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Enumerations.html#//apple_ref/doc/uid/TP40014097-CH12-ID148)的枚举。这部分留给读者作为练习。

### 清晰，或稍微不那么糟糕

Swift 在改进 Core Data 方面有很大的潜力，但它确实需要开发者付出更多努力，并且存在一些不太方便的变通方法和缺点。虽然我认为这值得投入时间，但上面描述的值包装和解包实现起来可能很繁琐。而且在获取请求中不得不使用底层的私有属性名称，这感觉很不优雅。好的一面是，我们可以免费获得可选类型和类型别名——这是向前迈出的一大步。

无论如何，我确实认为这比以前更好。有时候，Swift 似乎暴露了 Cocoa 和 Objective-C 最糟糕的一面。希望工具集能够改进——当 Cocoa 最终[消亡](http://nshipster.com/the-death-of-cocoa/)时，我会为 Core Data 的 Swift 重写版本欢呼。
