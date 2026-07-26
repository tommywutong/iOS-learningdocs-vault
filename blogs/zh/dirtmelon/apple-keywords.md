---
title: Apple Keywords
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/Apple-Keywords/'
original_language: zh
published: 2020-04-29
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0d1070e30d1b0328'
translated: n/a
---

> 原文：[Apple Keywords](https://dirtmelon.github.io/posts/Apple-Keywords/)　·　dirtmelon

## Why

熟悉 Apple 提供的一些 Keyword ，在适当的时候使用，有助于写出更规范的接口，也可以提高代码质量。

## Nullability

在 Swift 中可以使用 ? 和 ! 来显式声明一个对象是 `optional` 还是 `non-optional` ，但是 Objective-C 中没有这一行为，所有对象都默认是可以设置为 `nil` 的，在 Swift 与 Objective-C 混编时， Swift 层不知道 Objective-C 层的对象是否为 `optional` ，它会统一当成 `non-optional` 来处理。这样导致 Swift 层在调用时有可能对 `nil` 进行强制解包导致崩溃。

为了解决这个问题，Xcode 引入了一个 Objective-C 的新特性： Nullability Annotations ，如果我们没有显示地声明一个对象是否可以设置为 `nil` 时，编译器就会产生警告。 对于属性，方法返回值，方法参数，推荐使用 `nullable` 和 `nonnull` ：

```objc
- (nullable AAPLListItem *)itemWithName:(nonnull NSString *)name;
- (NSInteger)indexOfItem:(nonnull AAPLListItem *)item;
@property (copy, nullable) NSString *name;
@property (copy, readonly, nonnull) NSArray *allItems;
```

对于 C 函数相关参数，Block 参数和 Block 返回值，使用 `_Nonnull` 和 `_Nullable` 。 Xcode 提供了两个宏定义： `NS_ASSUME_NONNULL_BEGIN` 和 `NS_ASSUME_NONNULL_END` ，在两个宏定义之间的对象都是 `nonnull` ，可以根据需要指定某个对象为 `nullable` 。

```objc
NS_ASSUME_NONNULL_BEGIN
@interface AAPLList : NSObject <NSCoding, NSCopying>
// …
- (nullable AAPLListItem *)itemWithName:(NSString *)name;
- (NSInteger)indexOfItem:(AAPLListItem *)item;

@property (copy, nullable) NSString *name;
@property (copy, readonly) NSArray *allItems;
// …
@end
NS_ASSUME_NONNULL_END
```

在生成新的 Objective-C 文件时，Xcode 会自动添加 `NS_ASSUME_NONNULL_BEGIN` 和 `NS_ASSUME_NONNULL_END` ，只需要根据实际情况将某个对象设为 nullable 即可。

`null_resettable` ：需要重写 `setter` 或者 `getter` 来处理 `nil` ， `getter` 不可为空。可在 `setter` 可以为 `nil` 时使用。 `null_unspecified` ：`Swift` 可选类型的隐式解包，这个暂时不清楚怎么使用，只看到 `WKNavigationDelegate` 有使用到。

官方博客说明： [Nullability and Objective-C - Swift Blog - Apple Developer](https://developer.apple.com/swift/blog/?id=25)

## **attribute**((noescape))

Swift 的 `closure` 分为逃逸 `escaping` 和非逃逸 `non-escaping` 。

- 逃逸背包表示可能会在函数返回之后才调用，比如一些网络请求。逃逸背包因为可能会在函数返回之后才调用，所以需要捕获 `self` ，处理 `self` 的持有和释放，在使用时为了循环引用，需要添加 `[weak self]` 声明，如果需要调用 `self` 的属性，需要添加 `self.` 。
- 非逃逸背包择表示会在函数结束前调用，编译器会进行一些优化，去掉对 `self` 的相关管理，调用 `self` 的属性不需要添加 `self.` 。

Swift 使用 `non-escaping` 作为默认属性，如果是逃逸闭包则需要显式声明 `@escaping` ：

```swift
func withLock(perform closure: @escaping () -> Void) {
    myLock.lock()
    closure()
    myLock.unlock()
}

class MyClass {
    var counter = 0

    func incrementCounter() {
        counter += 1  // “self.” elided in an instance method
        withLock { [weak self] in
            // Without @noescape, the following line would produce the error
            //   “reference to property ‘counter' in closure requires
            //    explicit ‘self.’ to make capture semantics explicit”.
            self.counter += 1
        }
    }
}
```

为了更好地服务 Swift 和让编译器进行相关优化， Objective-C 的一些基础框架也支持了 `non-escaping` ：

```objc
// GCD
#if __has_attribute(noescape)
#define DISPATCH_NOESCAPE __attribute__((__noescape__))
#else
#define DISPATCH_NOESCAPE
#endif

dispatch_sync(dispatch_queue_t queue, DISPATCH_NOESCAPE dispatch_block_t block);

// CoreFoundation
#if __has_attribute(noescape)
#define CF_NOESCAPE __attribute__((noescape))
#else
#define CF_NOESCAPE
#endif

void CFArrayApplyFunction(CFArrayRef theArray, CFRange range, CFArrayApplierFunction CF_NOESCAPE applier, void *context);

// Foundation
#define NS_NOESCAPE CF_NOESCAPE

// NSArray
- (NSArray<ObjectType> *)sortedArrayUsingFunction:(NSInteger (NS_NOESCAPE *)(ObjectType, ObjectType, void * _Nullable))comparator context:(nullable void *)context;
```

在编写 Objective-C 代码时，如果 `block` 会在函数返回前调用，建议加上 `NS_NOESCAPE` ，或者直接使用 `(__attribute__((noescape))` 。

提案链接：[swift-evolution/0012-add-noescape-to-public-library-api.md at master · apple/swift-evolution · GitHub](https://github.com/apple/swift-evolution/blob/master/proposals/0012-add-noescape-to-public-library-api.md) [swift-evolution/0103-make-noescape-default.md at master · apple/swift-evolution · GitHub](https://github.com/apple/swift-evolution/blob/master/proposals/0103-make-noescape-default.md)

## NS_SWIFT_NAME

与 `Objective-C` 不同， `Swift` 有命名空间，不需要通过添加前缀来避免类名重复等问题。如果你想在 `Swift` 中调用时去掉丑陋的前缀， 可以使用 `NS_SWIFT_NAME` 来重定义`Objective-C` API 在 `Swift` 层的命名。 `NS_SWIFT_NAME` 适用于类型，属性，方法，函数。

```objc
NS_SWIFT_NAME(Sandwich.Preferences)
@interface SandwichPreferences : NSObject

@property BOOL includesCrust NS_SWIFT_NAME(isCrusty);

@end

@interface Sandwich : NSObject
@end
```

`Swift` 调用代码：

```swift
var preferences = Sandwich.Preferences()
preferences.isCrusty = true
```

官方文档：[Renaming Objective-C APIs for Swift

Apple Developer Documentation](https://developer.apple.com/documentation/swift/objective-c_and_c_code_customization/renaming_objective-c_apis_for_swift)

## NS_REFINED_FOR_SWIFT

如果你想要 Objective-C API 在 Swift 层的声明不同，可以使用 `NS_REFINED_FOR_SWIFT` ，使用之后可以加多一层封装来添加更 Swift 的 API 。

```objc
@interface ObjcClass : NSObject

- (instancetype)initWithName:(NSString *)name aka:(NSString *)name NS_REFINED_FOR_SWIFT;

@end
```

```swift
extension ObjcClass {
    @nonobjc convenience init(name: String = “”, aka: String) {
        self.init(__name: name, aka: aka)
    }
}

let objc = ObjcClass(aka: “Test”)
```

注意：加了 `NS_REFINED_FOR_SWIFT` 之后，带有 `__` 不会自动补全，需要手打出来。

好处：

- 提供一些默认参数；
- 封装层给 `block` 添加 `@escaping` ；
- 更 Swift 的 API 。

官方文档：[Improving Objective-C API Declarations for Swift

Apple Developer Documentation](https://developer.apple.com/documentation/swift/objective-c_and_c_code_customization/improving_objective-c_api_declarations_for_swift)

## NS_CLOSED_ENUM

Swift 5 引入了 `Frozen enums` ，如果 C enum 或者系统的 enums 没有添加 `NS_CLOSED_ENUM` ， Xcode 就会产生如下警告：

```plaintext
Switch covers known cases, but ‘AccountType’ may have additional unknown values
```

这表示 `AccountType` 在将来可能会添加其它的 values 。点击 Fix 后会新增一个 `@unknown default` 的 case ，用于处理以后增加的其它 values 。 与 `case default` 不同，在添加了其它 values 后， Xcode 还是会产生如下警告：

```plaintext
Switch must be exhaustive
```

如果使用 `case default` ，就不会产生警告。这个警告有助于提示你处理新增的 values 。 如果你确保未来不会新增 values ，那么就可以使用 `NS_CLOSED_ENUM` 来说明。 `NSComparisonResult` 使用了 `NS_CLOSED_ENUM` 来表明不会新增 values 。 Swift 层在进行 `switch` 的时候也无需添加 `@unknown default` 。

```objc
typedef NS_CLOSED_ENUM(NSInteger, NSComparisonResult) {
    NSOrderedAscending = -1L,
    NSOrderedSame,
    NSOrderedDescending
};
```

[Swift 5 Frozen enums](https://useyourloaf.com/blog/swift-5-frozen-enums)

[swift-evolution/0192-non-exhaustive-enums.md at master · apple/swift-evolution · GitHub](https://github.com/apple/swift-evolution/blob/master/proposals/0192-non-exhaustive-enums.md)

## NS_TYPED_ENUM

使用 `NS_TYPED_ENUM` 来给一组常量进行定义，和在 Swift 中使用 `struct` 和 `static` 属性来定义一组类型相似。

```objc
// Store the three traffic light color options as 0, 1, and 2.
typedef long TrafficLightColor NS_TYPED_ENUM;

TrafficLightColor const TrafficLightColorRed;
TrafficLightColor const TrafficLightColorYellow;
TrafficLightColor const TrafficLightColorGreen;
```

其作用跟 Swift 以下代码一致：

```swift
struct TrafficLightColor: RawRepresentable, Equatable, Hashable {
    typealias RawValue = Int

    init(rawValue: RawValue)
    var rawValue: RawValue { get }

    static var red: TrafficLightColor { get }
    static var yellow: TrafficLightColor { get }
    static var green: TrafficLightColor { get }
}
```

但是 `NS_TYPED_ENUM` 对应的 `struct` 不允许使用 `extension` ，如果需要使用到 `extension` ，则需要使用 `NS_TYPED_EXTENSIBLE_ENUM ` 来进行声明。

## availability

在 `Swift` 中我们可以使用 `@available` 来声明 API 在某个特定的平台或者系统上可用， `Objective-C` 中可以使用 `API_AVAILABLE` 来实现同样的功能：

```objc
@interface MyViewController : UIViewController
- (void) newMethod API_AVAILABLE(ios(11), macosx(10.13));
@end
```

其作用跟以下 `Swift` 代码一致：

```swift
@available(iOS 11, macOS 10.13, *)
func newMethod() {
    // Use iOS 11 APIs.
}
```

使用 `@available()` 来判断是否满足某些系统版本：

```objc
if (@available(iOS 11, *)) {
    // Use iOS 11 APIs.
} else {
    // Alternative code for earlier versions of iOS.
}
```

其作用跟以下 `Swift` 代码一致：

```swift
if #available(iOS 11, *) {
    // Use iOS 11 APIs.
} else {
    // Alternative code for earlier versions of iOS.
}
```

## NS_UNAVAILABLE

如果需要禁止使用某些方法，比如禁止使用系统提供的 `init` 方法：

```objc
- (instancetype)init NS_UNAVAILABLE;
```

在调用对应的 `init` 方法时就会报错。 如果只需要禁止 Swift 调用，可以使用 `NS_SWIFT_UNAVAILABLE` 。

## CF_SWIFT_NAME

因为 C 中的 `struct` 无法提供方法，属性或者自定义初始化方法，不得不通过编写全局函数来实现以上功能。Swift 中的 `struct` 则可以定义方法，属性或者初始化方法，如果需要将 C 中的方法桥接到 Swift 的 `struct` 中，可以使用 `CF_SWIFT_NAME` 。

```c
Color ColorCreateWithCMYK(float c, float m, float y, float k) CF_SWIFT_NAME(Color.init(c:m:y:k:));

float ColorGetHue(Color color) CF_SWIFT_NAME(getter:Color.hue(self:));
void ColorSetHue(Color color, float hue) CF_SWIFT_NAME(setter:Color.hue(self:newValue:));

Color ColorDarkenColor(Color color, float amount) CF_SWIFT_NAME(Color.darken(self:amount:));

extern const Color ColorBondiBlue CF_SWIFT_NAME(Color.bondiBlue);

Color ColorGetCalibrationColor(void) CF_SWIFT_NAME(getter:Color.calibration());
Color ColorSetCalibrationColor(Color color) CF_SWIFT_NAME(setter:Color.calibration(newValue:));
```

对应的 Swift 代码如下：

```swift
extension Color {
    init(c: Float, m: Float, y: Float, k: Float)

    var hue: Float { get set }

    func darken(amount: Float) -> Color

    static var bondiBlue: Color

    static var calibration: Color
}
```

当我们想为 C 中的全局方法提供更 Swift 的 API 时，可以考虑使用 CF_SWIFT_NAME 。

## NS_ERROR_ENUM

结合 `NS_ERROR_ENUM` ，在 Swift 层可以 `catch` 特定的 `error` 来进行特定的处理：

```swift
extern NSErrorDomain const MyErrorDomain;
typedef NS_ERROR_ENUM(MyErrorDomain, MyError) {
    specificError1 = 0,
    specificError2 = 1
};
```

```swift
@objc func customThrow() throws {
    throw NSError(
        domain: MyErrorDomain,
        code: MyError.specificError2.rawValue,
        userInfo: [
            NSLocalizedDescriptionKey: "A customized error from MyErrorDomain."
        ]
    )
}
```

```swift
do {
    try customThrow()
} catch MyError.specificError1 {
    print("Caught specific error #1")
} catch let error as MyError where error.code == .specificError2 {
    print("Caught specific error #2, ", error.localizedDescription)
    // Prints "Caught specific error #2. A customized error from MyErrorDomain."
} let error {
    fatalError("Some other error: \(error)")
}
```

同时也支持 Objective-C 进行调用，在 Objective-C 层的调用方式如下：

```objc
NSError *error;
[object customThrowAndReturnError:&error];
```

提案链接： [swift-evolution/0112-nserror-bridging.md at master · apple/swift-evolution · GitHub](https://github.com/apple/swift-evolution/blob/master/proposals/0112-nserror-bridging.md)
