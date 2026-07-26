---
title: Swift 与 Objective-C 互操作中的 Optional
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/Optional-between-Swift-and-Objective-C/'
original_language: zh
published: 2020-07-13
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:96f9b79c55fef548'
translated: n/a
---

> 原文：[Swift 与 Objective-C 互操作中的 Optional](https://dirtmelon.github.io/posts/Optional-between-Swift-and-Objective-C/)　·　dirtmelon

参考 [Optionals in Swift Objective-C Interoperability](https://fabiancanas.com/blog/2020/1/9/swift-undefined-behavior.html)

> 本文基于 Swift 5.3 和 Xcode 12.0 beta 2 编写，不排除将来可能有变化。

## nonnull

为了与 `Swift` 的 `Optional` 类型交互， `Objective-C` 提供了 `nullable` ， `nonnull` 等关键字，用于表示某个属性是否有可能为 `nil` ，这里是相关说明 [Nullability](https://dirtmelon.github.io/2020/04/29/Apple-Keywords/#Nullability) 。 假设我们有这么一个 `Objective-C` 类：

```objc
#import <UIKit/UIKit.h>

NS_ASSUME_NONNULL_BEGIN

@interface SomeThing : NSObject

@property (nonatomic, nonnull) UIScrollView *scrollView;

@end

NS_ASSUME_NONNULL_END

#import "SomeThing.h"

@implementation SomeThing

@end
```

使用了 `nonnull` 声明 `UIScrollView *scrollView` 属性，以此向 `Swift` 表明这个 `scrollView` 不会为 `nil` ，不需要进行解包操作，可以直接使用。在 `SomeThing.m` 中可以看到并没有对这个 `scrollView` 进行初始化，也就是这个 `scrollView` 为 `nil` ，但是编译器没有显示相关警告或者错误。

> ps: 这在 Swift 中是不允许的，如果一个属性不是 `Optional` 或者隐式解包类型，那么在初始化中必须要设置对应的值，否则编译器会报错。

由于 `scrollView` 是 `UIScrollView` 类型，所以我们可以直接对其进行一些操作：

```swift
let thing: SomeThing = SomeThing()
let scrollView: UIScrollView = thing.scrollView
let contentSize: CGSize = scrollView.contentSize
print("contentSize: \(contentSize)")
let indicatorStyle = scrollView.indicatorStyle
switch indicatorStyle {
case .black:
  print("black")
case .white:
  print("white")
case .default:
  print("default")
@unknown default:
  print("unknown default")
}

let gestureRecognizer = scrollView.panGestureRecognizer
gestureRecognizer.isEnabled = false
```

由于 `scrollView` 本质上是 `nil` ，所以上述的代码运行后应该会导致崩溃才对，但是它是可以正常运行的，输出如下：

```shell
contentSize: (0.0, 0.0)
default
```

我们直接把 `scrollView` 添加到当前 `ViewController` 的 `view` 上，看看是否可以正常显示：

```swift
let scrollView: UIScrollView = thing.scrollView
scrollView.translatesAutoresizingMaskIntoConstraints = false
scrollView.backgroundColor = UIColor.blue
view.addSubview(scrollView)
NSLayoutConstraint.activate([
  scrollView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
  scrollView.topAnchor.constraint(equalTo: view.topAnchor),
  scrollView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
  scrollView.bottomAnchor.constraint(equalTo: view.bottomAnchor)
])
```

什么也没有，界面一片空白。这就有可能导致一些奇奇怪怪的 bug ，我们在实际编码时会以为 `scrollView` 是实际存在的，把它添加到某个 `view` 上，进行相关操作，到最后发现一无所获。

### 进行一些悲观的防护

虽然 `SomeThing` 使用了 `nonnull` 来声明 `scrollView` ，但是我们还是想要判断 `scrollView` 是否为 `nil` ，以防止一些奇怪的 bug 出现。那么问题来了，由于 `Swift` 认为 `scrollView` 不可能为空，所以当我们进行解包操作时编译器会发出警告或者报错：

```swift
guard let scrollView: UIScrollView = thing.scrollView else {
  return
}
```

> warning: Non-optional expression of type ‘UIScrollView’ used in a check for optionals

```swift
guard let scrollView = thing.scrollView else {
  return
}
```

> error: Initializer for conditional binding must have Optional type, not ‘UIScrollView’

又或者说直接判断是否为 `nil` ：

```swift
let scrollView = thing.scrollView
if scrollView == nil {
  print("The compiler says we won't get here.")
  print("But if we run the program, we do")
}
```

> warning: Comparing non-optional value of type ‘UIScrollView’ to ‘nil’ always returns false

虽然编译器也显示了警告说把一个 `non-optional` 值跟 `nil` 比较会一直返回 `false` ，但是我们运行相关代码时，控制台会输出相关的 log ：

```shell
The compiler says we won't get here.
But if we run the program, we do
```

我们编写一个函数来清除 `nonnull` 相关信息以避免出现相关警告或者错误：

```plaintext
func isNil(_ o: Any?) -> Bool {
  switch o {
  case .none:
    return true
  case .some(_):
    return false
  }
}

if isNil(scrollView) {
  print("This doesn't print.")
}
```

使用 `Any?` 作为参数时，不会返回 `true` ，因为 `nil` 也可以用 `Any` 来表示。所以需要使用 `AnyObject` ：

```swift
func isNil(_ o: AnyObject?) -> Bool {
  switch o {
  case .none:
    return true
  case .some(_):
    return false
  }
}

if isNil(scrollView) {
  print("It works if we make it an AnyObject?")
}
```

我们可以通过这个方法来进行二次 `nil` 的判断，上面的例子说明所有从 `Objective-C` 层传进来的属性都是不可靠的（如果不注意编码规范的话）。

## Swift Extensions

首先添加一个 `Objective-C` 类的 `Swift extension` ：

```swift
extension UIScrollView {
  func doAThing() {
    print("doing it")
  }
}
```

然后尝试调用相关的方法：

```swift
let scrollView = thing.scrollView
scrollView.doAThing()
```

`doAThing` 方法会运行。跟 `Objective-C` 不同，如果你在 `Objective-C` 下给某个 `nil` 对象发送方法消息，是不会运行对应的方法的。但是 因为在 `Swift` 中， `scrollView` 不是 `Optional` 类型，`Swift` 认为 `scrollView` 不可能为 `nil` 。所以 `Swift` 会直接执行这个方法。

## Foundation 对象

Foundation 对象也发生了一些有趣的事情。 `NSCalendar` 是 `Foundation` 中的类。我们尝试使用 `NSCalendar` 来重复上述实验：

```objc
let calendarProvider = CalendarProvider()
let calendar = calendarProvider.calendar
let weekStartsOn = calendar.firstWeekday
let weekdays: [String] = calendar.shortWeekdaySymbols
```

代码会在第 2 行崩溃：

> Thread 1: EXC_BAD_INSTRUCTION (code=EXC_I386_INVOP, subcode=0x0) 跟 `UIScrollView` 不同， `NSCalendar` 在 `Swift` 中对应的类型为 `Calendar` ，但是这不是仅仅重命名，它做了一层桥接。 `Swift` 会自动把 `NSCalendar` 类型转换为 `Calendar` 。 `Swift` 的 `Foundation` 库中提供了 `_ObjectiveCBridgeable` 协议用于跟 `Objective-C` 类型进行桥接，其中可以通过 `_unconditionallyBridgeFromObjectiveC` 由 `NSCalendar` 生成对应的 `Calendar` ：

```swift
public static func _unconditionallyBridgeFromObjectiveC(_ source: NSCalendar?) -> Calendar {
    var result: Calendar? = nil
    _forceBridgeFromObjectiveC(source!, result: &result)
    return result!
}
```

可以看到 `_unconditionallyBridgeFromObjectiveC` 方法接受一个 `Optional<NSCalendar>` 参数，但是在内部会进行强制解包，所以就触发了上述崩溃。这可以避免一些意料之外的行为。

## Array 属性

`nonnull` Array 通过一种奇怪的方式从 `Objective-C` 层桥接到 `Swift` 中。 首先定义以下 `Objective-C` 类，定义了 `description` 方法，用于输出相关数据：

```objc
@interface OffendingObject : NSObject

@property (nonatomic, nonnull) NSArray *array;

@end

@implementation OffendingObject

- (NSString *)description {
    return [NSString stringWithFormat: @"%@" "array: %@", [super description], self.array];
}
@end
```

`NSArray` 在 `Swift` 中会桥接为 `Array` ，下面来看下一些奇怪的现象：

```swift
let obj = OffendingObject()
print(obj)
print(obj.array)
print(obj)
obj.array.append("thing")
print(obj)
```

运行上述代码，输出如下：

```shell
<OffendingObject: 0x600003210270>array: (null) // 1
[] // 2
<OffendingObject: 0x600003210270>array: (null) // 3
<OffendingObject: 0x600003210270>array: (
    thing
)  // 4
```

输出 1 和 3 中的 `array` 为 `null` ，表现正常，但是输出 2 中的 `array` 是一个空的数组，这是因为 `Swift` 在进行桥接时如果 `array` 为 `nil` ， 就会返回一个空的 `Array` 。 当我们通过 `append` 给 `array` 添加数据时并不会崩溃，且在输出 4 中可以看到 `array` 已经包含刚添加的对象。 `NSArray` 是不可变的，但是 `Array(Swift)` 不同，在语义来说， `Array` 是值类型，不是引用类型。给 `Array` 添加一个新的元素时， `Swift` 会创建一个新的数组赋值给对应的属性，所以改变的是对应的属性，而不是 `Array` 。 虽然 `OffendingObject` 中的 `array` 是 `NSArray` 类型，不可变，但是 `array` 属性是可读写的。所以 `Swift` 可以通过创建一个新的数组然后赋值给 `array` 来修改 `array` 的值。

上面说到 `array` 为 `nil` 时 `Swift` 会返回一个空的数组，下面来看看为什么。跟 `NSCalendar` 一样， `NSArray` 会桥接为 `Array` ， `Swift` 中相关代码 [Array.swift](https://github.com/apple/swift-corelibs-foundation/blob/914a8ae328d04f71e286c74fc3cb6e79dd9461ae/Foundation/Array.swift) 如下：

```swift
static public func _unconditionallyBridgeFromObjectiveC(_ source: NSArray?) -> Array {
    if let object = source {
        var value: Array<Element>?
        _conditionallyBridgeFromObjectiveC(object, result: &value)
        return value!
    } else {
        return Array<Element>()
    }
}
```

可以看到对 `source` 进行判断，如果 `source` 为 `nil` 则返回一个空的 `Array` 。

## 最后

相关讨论：[SR-8622 Nonnull Objective-C property that falsely returns nil causes inconsistent Swift behavior](https://bugs.swift.org/browse/SR-8622)

> The cost of checking every nonnull return value was determined to be too high, but maybe we could do it in Debug builds. —Jordan Rose, _SR-8622_
