---
title: MemorySafety
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/MemorySafety/'
original_language: zh
published: 2020-09-30
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:3d01327a78bc0c09'
translated: n/a
---

> 原文：[MemorySafety](https://dirtmelon.github.io/posts/MemorySafety/)　·　dirtmelon

原文：[MemorySafety](https://docs.swift.org/swift-book/LanguageGuide/MemorySafety.html)

在默认情况下， Swift 会防止你的代码中发生不安全的行为。举个例子， Swift 保证所有变量在使用前都已经完成了初始化，当它们被释放后无法对内存进行存取，数组的索引越界时报错。 Swift 还要求修改内存内容的代码具有独占的访问权限，以此来保证同时对同一区域内存的多次访问不会造成冲突。因为 Swift 会自动管理内存，所以大多数情况下你都不需要考虑有关内存访问的问题。然而，弄明白什么地方有可能发生冲突仍然非常重要，你可以避免写出访问内存时造成冲突的代码。如果你的代码保护这些冲突，那么你会得到一个编译时或者运行时的错误。

## 存取内存时的冲突

当你执行像是设置变量的值或者将参数传递给函数之类的操作时，就会在代码中访问内存。举个例子，下面的代码就包含读取访问和写入访问：

```swift
// A write access to the memory where one is stored.
var one = 1

// A read access from the memory where one is stored.
print("We're number \(one)!")
```

当你的代码中不同的部分试图同时访问内存中同一块区域时，对内存的存取就会产生冲突。同时对内存中的同一个区域进行多次访问会造成不可预期或者不一致的行为。在 Swift 中，有多种方法可以在修改跨越几行代码中的值，使得可以在修改过程中访问一些中间值。 通过下面这个如何更新纸条上的预算的例子，你可以看到类似的问题。更新预算分为两个步骤：首先，你需要添加项目的名字和价格，然后你需要根据当前纸条上的预算来更新总金额。在更新前和更新后，你都可以从预算中读取任何信息和获取正确的答案，如下图所示：

![memory_shopping_2x](https://raw.githubusercontent.com/dirtmelon/blog-images/main/memory_shopping_2x.png)

当你向预算中添加项目时，它处于一个临时的，无效的状态中，因为总金额尚未根据你添加的项目进行更新。在添加项目的过程中读取总金额会得到错误的信息。 这个例子还说明了在解决内存冲突时可能会遇到的挑战：有时有几种方法来解决冲突，但是会导致不同的答案，且哪个答案是正确的有时是件不明显的事情。在这个示例中，根据你要需要的是原始的金额还是更新后的金额， $5 和 $320 都可以是正确答案。在你解决冲突前，必须要清楚需要获取的金额是哪个。

> Note 如果你编写了并发或者多线程的代码，那么对内存的冲突访问可能是一个常见的问题。但是这里讨论的冲突访问是发生在单线程中，不会涉及并发或者多线程的代码。 如果你在单线程中对内存的访问存在冲突， Swift 会保证在编译时或者运行时报错。对于多线程代码，可以使用 Thread Sanitizer 来帮助你检查线程中的冲突访问。

## 内存访问的特征

在访问冲突的情况下需要考虑访问内存的三个特征：

1. 访问是读访问还是写访问；
2. 访问的持续时间；
3. 访问的内存的位置； 具体来说，如果你有两个满足以下所有条件的访问时，就会产生冲突：
4. 至少有一个写操作；
5. 访问内存中同一个位置；
6. 持续时间重叠； 读写操作之间的区别通常非常明显：写操作会改变内存中的位置，读操作不会。内存中的位置指向要访问的内容，如变量，常量和属性等。内存访问的持续时间可以是瞬间的，也可以是长期的。 如果说在访问开始到结束之间无法执行其它代码，那么访问的持续时间就是瞬间的。从本质上来说，两个瞬间的访问是不可能同时发生。大多数内存访问都是瞬间的。在下面的代码中，所有的访问都是瞬间的：

```swift
func oneMore(than number: Int) -> Int {
    return number + 1
}

var myNumber = 1
myNumber = oneMore(than: myNumber)
print(myNumber)
// Prints "2"
```

但是，有几种方法可以长期访问内存，跨越其他代码的执行过程。瞬间访问和长期访问的区别在于，其它代码有可能在长期访问开始到结束之间执行，这种情况称之为重叠。长期访问可以和其它长期或者瞬间访问重叠。 重叠访问主要出现在使用了 `in-out` 参数的函数，方法或者结构体的可变方法中。下面所讨论的特定 Swift 代码都使用了长期访问。

## In-Out 参数的冲突访问

一个函数对于它所有的 `in-out` 参数都具备长期写访问的权限。在所有非 `in-out` 参数完成求值后，就开始对 `in-out` 参数进行写访问，并持续到整个函数完成执行。如果有多个 `in-out` 参数，那么写访问开始的顺序与参数出现的顺序一致。 长期写访问的一个影响是你无法访问 `in-out` 参数的原始变量，即使满足作用域规则和访问权限，所有访问原始变量的操作都会造成冲突。举个例子：

```swift
var stepSize = 1

func increment(_ number: inout Int) {
    number += stepSize
}

increment(&stepSize)
// Error: conflicting accesses to stepSize
```

在上述代码中， `stepSize` 是一个全局变量，所以在 `increment(_:)` 方法中可以直接访问它。然而， `stepSize` 的读访问和 `number` 的写访问重叠了。如下面配图所示， `number` 和 `stepSize` 都指向内存中同一个位置。读访问和写访问都指向相同的内存，且它们重叠了，因此产生了冲突。

![memory_increment_2x](https://raw.githubusercontent.com/dirtmelon/blog-images/main/memory_increment_2x.png)

一个解决的办法是拷贝 `stepSize` ：

```swift
// Make an explicit copy.
var copyOfStepSize = stepSize
increment(&copyOfStepSize)

// Update the original.
stepSize = copyOfStepSize
// stepSize is now 2
```

当你在调用 `increment(_:)` 前对 `stepSize` 进行拷贝时， `copyOfStepSize` 会加上当前的 `stepSize` 。读访问在写访问开始前已经结束了，所以这里是没有冲突的。 长期写访问的另外一个影响是无法传递同一个变量给同一个函数中的多个 `in-out` 参数，否则会产生冲突。举个例子：

```swift
func balance(_ x: inout Int, _ y: inout Int) {
    let sum = x + y
    x = sum / 2
    y = sum - x
}
var playerOneScore = 42
var playerTwoScore = 30
balance(&playerOneScore, &playerTwoScore) // OK
balance(&playerOneScore, &playerOneScore)
// Error: conflicting accesses to playerOneScore
```

上面的 `balance(_:_:)` 函数会对它的两个参数进行操作，对它们的和进行等分。调用这个方法时如果使用 `playerOneScore` 和 `playerTwoScore` 作为参数是不会产生冲突的，虽然这个时候有两个写访问重叠了，但是它们访问的是内存中不同的位置。相反地，如果使用 `playerOneScore` 作为两个参数就会产生冲突，因为它试图在同一时间内对内存中相同的位置执行写访问。

> Note 因为操作符也是函数，它们也对 `in-out` 参数有长期访问。如果说 `balance(_:_:)` 是一个名称为 `<^>` 的操作符， `playerOneScore <^> playerOneScore` 跟 `balance(&playerOneScore, &playerOneScore)` 会产生相同的冲突。

## 在方法中访问自身时冲突

`struct` 的可变方法在执行期间对 `self` 持有写访问，假设有一个这样的游戏玩家，有生命值和能量两种属性，血量在收到伤害时会减少，能量在使用特殊技能时减少。

```swift
struct Player {
    var name: String
    var health: Int
    var energy: Int

    static let maxHealth = 10
    mutating func restoreHealth() {
        health = Player.maxHealth
    }
}
```

在上面的 `restoreHealth()` 方法中， `self` 的写访问从方法开始持续到结束。在这个例子中， `restoreHealth()` 中没有访问 `Player` 对象属性的代码。下面的 `shareHealth(with:)` 方法接受两个 `Player` 对象作为 `in-out` 参数，因此有可能产生访问重叠。

```swift
extension Player {
    mutating func shareHealth(with teammate: inout Player) {
        balance(&teammate.health, &health)
    }
}

var oscar = Player(name: "Oscar", health: 10, energy: 10)
var maria = Player(name: "Maria", health: 5, energy: 10)
oscar.shareHealth(with: &maria)  // OK
```

在上面的例子中，调用 `shareHealth(with:)` 方法来共享 Oscar 玩家和 Maria 玩家之间的生命值不会产生冲突。在执行方法期间会存在一个对 `oscar` 的写访问，因为这是一个 `mutating` 的方法。然后还有对 `maria` 的写访问，因为 `maria` 是作为一个 `in-out` 参数传递进来的。如下图所示，它们指向的是内存中不同的位置，所以即使两个写访问在时间上重叠了，它们也不会产生冲突。

![memory_share_health_maria_2x](https://raw.githubusercontent.com/dirtmelon/blog-images/main/memory_share_health_maria_2x.png)

然而，如果你将 `oscar` 作为 `shareHealth(with:)` 的参数进行传递，就会产生冲突：

```swift
oscar.shareHealth(with: &oscar)
// Error: conflicting accesses to oscar
```

`mutating` 方法在执行期间对 `self` 有写访问， `in-out` 参数同时对 `teammate` 有写访问。所以 `self` 和 `teammate` 同时指向内存中相同的位置，如下所示，它们指向相同的内存，且重叠，所以会产生冲突。

![memory_share_health_oscar_2x](https://raw.githubusercontent.com/dirtmelon/blog-images/main/memory_share_health_oscar_2x.png)

## 访问属性时冲突

`stuct` ， `tuple` 和 `enum` 这些类型由不同的独立的值组成，比如说 `struct` 的 `property` 和 `tuple` 的 `element` 。因为它们是值类型，所以修改任何一部分都会修改整个值，这意味着对于属性的读或者写访问会持有对整个值的读或者写访问。举个例子，对 `tuple` 的不同 `element` 写访问重叠时就会产生冲突：

```swift
var playerInformation = (health: 10, energy: 20)
balance(&playerInformation.health, &playerInformation.energy)
// Error: conflicting access to properties of playerInformation
```

在上面的例子中，调用 `balance(_:_:)` 方法时如果传递的是 `tuple` 的元素，那么就会产生冲突，因为 `playerInformation` 的写访问重叠了。 `playerInfomation.health` 和 `playerInfomation.energy` 作为 `in-out` 参数进行传递，这意味着 `balance(_:_:)` 需要对它们进行写访问，对 `tuple` 的 `element` 进行写访问意味对整个 `tuple` 进行写访问。所以这两个针对 `playerInformation` 的写访问重叠了，产生冲突。

下面的代码也显示了相同的错误，当对一个全局的 `struct` 变量的不同属性同时进行写访问时也会产生相同的冲突。

```swift
var holly = Player(name: "Holly", health: 10, energy: 10)
balance(&holly.health, &holly.energy)  // Error
```

实际上，大多数对 `struct` 的属性的访问都可以安全地进行重叠。我们可以将上面的 `holly` 改成局部变量而不是全局变量，编译器可以在此保证对 `struct` 的存储属性进行的重叠访问是安全的。

```swift
func someFunction() {
    var oscar = Player(name: "Oscar", health: 10, energy: 10)
    balance(&oscar.health, &oscar.energy)  // OK
}
```

在上面的例子中， Oscar 的生命值和能量值作为 `balance(_:_:)` 的两个 `in-out` 参数进行传递。编译器可以保证内存是安全的，因为这两个存储属性不会进行任何交互。 对于结构提的属性来说，保证内存访问安全不一定需要进行重叠访问的限制。内存安全只是一个期望得到的保证，独占访问会比内存安全要求更严格，这意味着即使某些代码违反了对内存的独占性访问，也可以保证内存安全。如果说编译器可以保证对内存的非独占访问是安全的， Swift 就会允许执行这段非独占性的代码。 如果满足以下条件，那么就可以证明对 `struct` 的属性进行重叠访问是安全的：

- 只访问实例的存储属性，不访问计算属性或者类属性；
- 是局部变量，不是全局变量；
- 没有被其它闭包捕获，或者只被非逃逸闭包捕获； 如果编译器无法保证这次访问是安全的，它就不会允许这次访问。
