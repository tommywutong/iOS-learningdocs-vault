---
title: Swift 与指针
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/Swift-and-Pointer/'
original_language: zh
published: 2020-05-18
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:dd2b9b1e0c55dfe5'
translated: n/a
---

> 原文：[Swift 与指针](https://dirtmelon.github.io/posts/Swift-and-Pointer/)　·　dirtmelon

## 为什么使用指针

Swift 是一门非常安全的语言，强类型，`Optinal` 都是为了提高安全性所引入的，当我们对一个值为 `nil` 的 `Optional` 进行强制解包时就会触发崩溃，这是为了安全而触发的崩溃，可以防止程序有预期之外的行为。如果这里不崩溃，可能导致后续程序行为不可预期。 大多数情况下，我们在使用 Swift 时都不需要使用指针，但是在某些情况下我们不可避免地需要使用指针相关 API ：

1. 追求性能，直接操作内存；
2. 与 C 进行交互；
3. 通过修改指针的值来进行数据通讯；

但是当我们越过类型的边界，直接对内存进行操作时，所有一切都变得不安全，从严格意义上来说，我们不能确定某个指针所指向的地址包含的类型是什么，对指针的操作必须小心翼翼。所以在 Swift 中，所有与指针操作相关的 API 都带有 `unsafe` 的关键字。

## MemoryLayout

Swift 提供了 `MemoryLayout` 来提供类型在内存占用中的信息，如：`size` ， `alignment` 和 `stride` 。

物理内存以字节 (byte) 为单位，一个字节 (byte) 代表 8 bit ，bit 表示 0 或 1 。CPU 在读写内存时，会按照 word size 来读取内存，64 bit 的 CPU 会以 8 字节为 word size ，每次都会读取 word size 倍数的内存。有了内存对齐，使得每次读取都可以通过读取CPU 在读取的时候就不需要多次读取，提高效率。更详细的说明在这里：[Purpose of memory alignment - Stack Overflow](https://stackoverflow.com/questions/381244/purpose-of-memory-alignment) 。

1. alignment 表示内存对齐的字节，对应的对象地址必须是 alignment 的倍数，某些计算机系统要求对象的起始地址必须要是 1，2，4，8 的倍数；
2. size 表示对象所占用的真实内存字节大小；
3. stride 则表示对象在进行内存对齐后所占用的内存字节；

```swift
// 基本类型的内存布局
MemoryLayout<Int16>.size        // returns 2
MemoryLayout<Int16>.alignment   // returns 2
MemoryLayout<Int16>.stride      // returns 2

MemoryLayout<Bool>.size         // returns 1
MemoryLayout<Bool>.alignment    // returns 1
MemoryLayout<Bool>.stride       // returns 1

MemoryLayout<Float>.size        // returns 4
MemoryLayout<Float>.alignment   // returns 4
MemoryLayout<Float>.stride      // returns 4

MemoryLayout<String>.size       // returns 16
MemoryLayout<String>.alignment  // returns 8
MemoryLayout<String>.stride     // returns 16
```

大多数基本类型的 `stride` ， `alignment` 和 `stride` 都是一致的，但是当我们将其组合成 Struct 时就会发生一点变化了：

```swift
struct Memory {
  let boolValue: Bool
  let floatValue: Float
  let int16: Int16
}

MemoryLayout<Memory>.size      // returns 10
MemoryLayout<Memory>.alignment // returns 4
MemoryLayout<Memory>.stride    // returns 12
```

如果按照上面所显示的 size 来计算： `MemoryLayout<Bool>.size + MemoryLayout<Float>.size + MemoryLayout<Int16>.size = 1 + 2 + 4 = 7` 。 为什么 `MemoryLayout<Memory>.size` 是 10 呢？这是因为内存对齐所造成的影响。假设 `Memory` 以 0x0 为起始内存地址，那么 `Memory` 详细的内存布局如下：

```swift
struct Memory {
  let boolValue: Bool // 0x0
  // padding 3
  let floatValue: Float // 0x4 内存对齐
  let int16: Int16 // 0x8
	// padding 2 内存对齐
}
```

因为 `floatValue` 需要以 4 的倍数来作为起始地址，所以会在 `boolValue` 后加上 3 个字节作为补充，而 `Memory` 的 `alignment` 则以其所包含属性的 `alignment` 的最大值为自己的 `alignment` 。 这里如果对 `Memory` 的属性声明顺序进行以下调整可以减少 `Memory` 在内存中占用的字节大小：

```swift
struct Memory {
  let boolValue: Bool // 0x0
  // padding 1
  let int16: Int16 // 0x2
  let floatValue: Float // 0x4
}
```

这样调整后 `Memory` 的 `size` 和 `stride` 都是 8 ，可以减少一些 `Memory` 的内存占比。 这里有个详细分析 Swift 中各种数据类型的内存布局的 repo ： [GitHub - TannerJin/Swift-MemoryLayout: Swift MemoryLayout](https://github.com/TannerJin/Swift-MemoryLayout) 。

## UnsafePointer

`UnsafePointer` 的声明如下：

```swift
@frozen struct UnsafePointer<Pointee>
```

`Pointee` 表示其内存中所包含的类型，你可以通过 `pointee` 属性来访问对应的类型，当使用 `UnsafePointer` 时，我们就负担起对生命周期进行管理的责任，调用一些初始化和释放相关的函数。

### 指针的内存状态

一个指针的对象可以有多种状态。很多指针的操作只在特定的内存状态中起作用，你必须要了解你所操作的内存的状态，明白各种操作在不同的状态下的区别。指针的内存可以有以下几种状态：

1. 未类型化和未初始化；
2. 类型化但未初始化；
3. 类型化和初始化；

未初始化的内存在读取前必须要进行初始化，已经初始化内存的指针可以通过 `pointee` 属性或者下标法进行访问：

```swift
let pointer: UnsafePointer<Int> = ...
print(pointer.pointee)
print(pointer[0])
```

### 将内存绑定到不同的类型

当你通过 `UnsafePointer` 对象来操作内存时， `Pointee` 的类型必须要和内存中的类型一致。如果需要转换为其它类型的 `UnsafePointer` ， Swift 提供了类型安全的方式来临时或者永久地修改内存中的类型，也可以从原始的内存中直接加载类型的对象。

比如说我们初始化了一个 `UnsafePointer<UInt8>` 对象，可以通过 `withMemoryRebound(to:capacity:)` 方法将其临时转化为 `UnsafePointer<Int8>` ：

```swift
let pointer: UnsafePointer<UInt8> = ... // 255
print(pointer.pointee) // 255
pointer.withMemoryRebound(to: Int8.self, capacity: 8) {
  print($0.pointee) // -1
}
```

在讲内存绑定到不同的类型时，你必须要保证两者之间的内存布局是可兼容的。

如果需要永久地将内存绑定到不同的类型，首先需要初始化一个 `raw` 的指针，然后调用 `bindMemory(to:capacity:) ` 方法将其绑定到对应的类型：

```swift
let pointer: UnsafePointer<Bool> = ... // true
let uint64Pointer = UnsafeRawPointer(pointer).bindMemory(to: UInt64.self, capacity: 1)
let uint64Value  = uint64Pointer.pointee // 1
let originalBoolValue = pointer.pointee // true
```

也可以通过 `UnsafePointer` 的 `load(as:)` 方法直接进行类型转换：

```swift
let rawPointer = UnsafeRawPointer(pointer)
let uint64Value  = rawPointer.load(as: UInt64.self) // 1
let originalBoolValue =  rawPointer.load(as: Bool.self)  // true
```

### 指针的运算

指针支持根据 `Pointee` 的类型进行步长 `strides` 相关的运算：

```swift
// 数组第一个值的指针
let intPointer: UnsafePointer<Int> = // [10, 20, 30, 40]
print(intPointer.pointee) // 10
print((intPointer + 2).pointee) // 30
print(intPointer[2]) // 30
```

### 隐式转换与桥接

当调用含有 `UnsafePointer` 参数的方法或者函数时，你可以使用指向对应类型的指针，也可以使用指向兼容类型的指针，还可以使用 Swift 的隐式桥接。

```swift
func printInt(atAddress p: UnsafePointer<Int>) {
  print(p.pointee)
}

printInt(atAddress: intPointer)

let mutableIntPointer = UnsafeMutablePointer(mutating: intPointer)
printInt(atAddress: mutableIntPointer) // 兼容类型，进行隐式转化

printInt(atAddress: &number) // Swift 隐式桥接

let numbers = [5, 10, 15, 20]
printInt(atAddress: numbers) // numbers 第一个元素的地址，即 5
```

> 经由隐式桥接创建的对象或者数组元素只在调用的函数的执行期间有效。在其之后对指针进行操作都是未定义的行为，我们无法保证内存中还是对应的数据，尤其不要在 `UnsafePointer` 初始化中使用隐式桥接

```swift
var number = 5
let numberPointer = UnsafePointer<Int>(&number)
// Accessing 'numberPointer' is undefined behavior.
```

## UnsafeMutablePointer

与 `UnsafePointer` 不同， `UnsafeMutablePointer` 支持通过 `allocate` 和 `initialize` 来进行分配内存和初始化：

```swift
var bytes: [UInt8] = [1, 2, 3, 4, 5, 6, 7, 8]
let uint8Pointer = UnsafeMutablePointer<UInt8>.allocate(capacity: 8)
uint8Pointer.initialize(from: &bytes, count: 8)
bytes[0] = 9
print(uint8Pointer.pointee)
```

同时因为需要自己管理指针的生命周期，所以需要手动销毁指针：

```swift
uint8Pointer.deinitialize(count: 8)
uint8Pointer.deallocate()
```

## UnsafeBufferPointer & UnsafeMutableBufferPointer

`UnsafeBufferPointer` 是一段在连续的内存中存储元素的指针，对应的是 Swift 中的集合。 在更低级别上使用 `UnsafeBufferPointer` 可以去除单一性检测和边界检测（ Release 模式），提高性能。 `UnsafeBufferPointer` 只是一个进入对应内存的入口，它并不拥有它所引用的内存对象，对它进行拷贝不会拷贝对应的内存对象。

`UnsafeMutableBufferPointer` 是 `UnsafeBufferPointer` 的可变版本。 Buffer Pointer 提供了大量与 Swift 集合类型一致的 api ，在调用的时候非常方便：

```swift
var array = [1, 2, 3, 4, 5]
let bufferPointer = UnsafeMutableBufferPointer<Int>(start: &array, count: array.count)

for (index, pointer) in bufferPointer.enumerated() {
  print(index, pointer)
}
```

## UnsafeRawPointer & UnsafeMutableRawPointer

与上面对应具体类型的指针不同， `Raw` 指针不清楚自己指向的数据具体类型是什么，它不是类型安全的。在 Raw 指针分配内存后，需要调用 `bindMemory(to:count:)` 方法在没初始化的情况下将内存绑定到某个类型。 当通过 Raw 指针读取已经绑定到某个类型的内存时，你必须要保证满足所有内存对齐的条件。

### 运算

Raw 指针也支持进行运算

```swift
// 设置 byteCount 和 alignment
let bytesPointer = UnsafeMutableRawPointer.allocate(byteCount: 4, alignment: 4)
// 初始化值为 0xFFFFFFFF 的 UInt32
bytesPointer.storeBytes(of: 0xFFFF_FFFF, as: UInt32.self)

// 加载第一个字节为 UInt8
let x = bytesPointer.load(as: UInt8.self)       // 255

// 移动两个字节，加载第三个和第四个字节
let offsetPointer = bytesPointer + 2
let y = offsetPointer.load(as: UInt16.self)     // 65535

// 释放内存
bytesPointer.deallocate()
```

### 隐式转换和桥接

首先定义一个 `print(address:as:)` 函数， 第一个参数为 `UnsafeRawPointer` 对象。

```swift
func print<T>(address p: UnsafeMutableRawPointer, as type: T.Type) {
  let value = p.load(as: type)
  print(value)
}
```

输入 `Raw` 指针作为参数：

```swift
let bytesPointer = UnsafeMutableRawPointer.allocate(byteCount: 4, alignment: 4)
bytesPointer.storeBytes(of: 123, as: UInt32.self)

print(address: bytesPointer, as: UInt32.self)
bytesPointer.deallocate()
```

所有类型指针都可以隐式转换为 `Raw` 指针，所以也可以输入类型指针作为参数：

```swift
let mutableIntPointer = UnsafeMutablePointer<Int>.allocate(capacity: 1)
mutableIntPointer.initialize(to: 456)

print(address: mutableIntPointer, as: Int.self)
mutableIntPointer.deinitialize(count: 1)
mutableIntPointer.deallocate()
```

也可以通过 Swift 的隐式桥接来输入对象的指针或者数组作为参数：

```swift
var value: Int = 23
print(address: &value, as: Int.self)

let numbers = [5, 10, 15, 20]
print(address: numbers, as: Int.self)
```

## COpaquePointer

`COpaquePointer` 用于指向一些不能在 Swift 中表示的类型，比如说 C struct ：

```c
struct SomeStruct;
void opaquePointer(struct SomeStruct *someStruct);
```

```swift
func opaquePointer(someStruct: COpaquePointer)
```

## 指针转换

Swift 不支持 C 那样使用 `&` 获取地址后直接进行操作，所以提供了一系列以 `withUnsafe` 为前缀的方法，同样地也有可变和不可变版本。

```swift
func withUnsafePointer<T, Result>(to value: inout T, _ body: (UnsafePointer<T>) throws -> Result) rethrows -> Result
```

第一个参数是 `inout` 类型，第二个是闭包， 这个方法会将第一个参数转换为对应的指针，你可以在闭包中进行相关处理，比如调用接收指针参数的 Objective-C API ，但是不要在闭包范围外使用这个指针，因为在闭包范围外的释放时机是不确定的。

```swift
var number: Int = 1
let value = withUnsafePointer(to: &number) { (pointer) -> Int in
  return pointer.pointee + 1
}
```

Swift 也提供指针版本的 `swap` ：

```swift
func swap<T>(_ a: inout T, _ b: inout T)

var a: Int = 1
var b: Int = 2
swap(&a, &b)
print(a, b)
```

### unsafeBitCast

通过 `unsafeBitCast` 可以强制将指针指向的内存转为另一种类型。在进行 `unsafeBitCast` 转换时必须保证两者在内存布局上必须是兼容的，苹果文档 [unsafeBitCast(_:to:)](https://developer.apple.com/documentation/swift/1641250-unsafebitcast) 也使用 `Warning` 标明 `unsafeBitCast` 不受 Swift 的类型系统保护，所以必须要非常小心。一般来说， `unsafeBitCast` 用于指针间的相互转换，因为指针的大小是相同的，某些 C API 要求的参数是 `void *` ，可以通过 `unsafeBitCast` 进行转换，结合 `withUnsafe` 函数可以将 `UnsafePointer<T>` 转换为 `UnsafePointer<Void>` ：

```plaintext
var number = 4
withUnsafePointer(&number, { (ptr: UnsafePointer<Int>) -> Int32 in
  var voidPtr: UnsafePointer<Void> = unsafeBitCast(ptr, UnsafePointer<Void>.self)
  return takesAnObjectAndReturnsAnInt(voidPtr)
})
```

### assumingMemoryBound

通过 `UnsafeMutableRawPointer` 的 [`assumingMemoryBound(to:)`](https://developer.apple.com/documentation/swift/unsaferawpointer/2431721-assumingmemorybound) 方法可以生成一个指向同样内存地址的 `UnsafeMutablePointer<T>` ，使用 `assumingMemoryBound(to:)` 需要保证内存已经绑定至对应的类型。

```swift
struct Struct {
    var a: UInt8 = 2
    var b: UInt16 = 2
}

var structValue = Struct()
let pointer = withUnsafePointer(to: &structValue) { UnsafeMutableRawPointer(mutating: $0) }.advanced(by: 2).assumingMemoryBound(to: UInt16.self)
pointer.pointee = 4
print(structValue.b) // 4
```

## Unmanaged

为了与 C 进行交互，有时我们需要在 `Raw` 指针和 Swift 对象之间进行转换，为此，Swift 提供了 `Unmanaged` 给我们使用。 而 Swift 对象和 `Raw` 指针的转换分为两部分：

- `void *` 与 Swift 对象之间的转换；
- 内存管理，当指针传递给 C 之后，Swift 的 ARC 就失效了，这时需要我们进行手动管理内存；

### Swift To C

- `Unmanaged.passRetained(obj)` 会增加引用计数，需要在适当的时机调用 `release` ，否则会造成内存泄露；
- `Unmanaged.passUnretained(obj)` 不会增加引用计数，可以在一些会在内部处理 ownership 或者直接使用值的 C API 中使用；

```swift
let str0 = "boxcar" as CFString
let bits = Unmanaged.passRetained(str0)
let ptr = bits.toOpaque()
```

`Unmanaged` 调用 `toOpaque()` 方法可以转换为 `UnsafeMutableRawPointer` ，与 C 的 `void *` 等价，可以与 C API 交互。

### C To Swift

`Unmanaged` 也提供了相关方法将 `Raw` 指针转换为 Swift 对象，转换为 Swift 对象时，你必须要指定类型：

```swift
let string = Unmanaged<CFString>.fromOpaque(ptr).takeRetainedValue()
```

`takeRetainedValue()` 会执行一次 `release` ，与 `passRetained` 对应，如果在转换为 `UnsafeMutableRawPointer` 时使用的是 `passRetained` ，这里就需要调用 `takeRetainedValue()` 。如果不需要进行 `retain` 或者 `release` ，这里可以调用 `takeUnretainedValue()` 。

### C 指针和 Swift 指针的对应表

| C | Swift |
|---|---|
| const T * | UnsafePointer |
| T * | UnsafeMutablePointer |
| const T * [] | UnsafeBufferPointer |
| T * [] | UnsafeMutableBufferPointer |
| T ** | AutoreleasingUnsafeMutablePointer |
| const void * | UnsafeRawPointer |
| void * | UnsafeMutableRawPointer |
| void * [] | UnsafeBufferRawPointer |

## 示例

### UIScrollViewDelegate

`UIScrollViewDelegate` 中有这么一个方法： `scrollViewWillEndDragging(_:withVelocity:targetContentOffset:)` ，当用户停止滑动使调用：

```swift
optional func scrollViewWillEndDragging(_ scrollView: UIScrollView,
                           withVelocity velocity: CGPoint,
                    targetContentOffset: UnsafeMutablePointer<CGPoint>)
```

其中 `targetContentOffset` 是一个 `UnsafeMutablePointer<CGPoint>` ，通过修改 `targetContentOffset` 的值可以在 `UIScrollView` 完成滑动时调整 offset ，因为 `CGPoint` 是一个 `struct` ，这里使用指针，从而修改对应内存上的值， `UIScrollView` 也可以获取到调用后的结果。

### ReachabilitySwift

在 iOS 中，如果需要监听或者获取当前的网络状态，就需要跟 `SCNetworkReachability` 打交道，`SCNetworkReachabilityContext` 提供了 `retain` 和 `release` callback ，可以通过 callback 来进行内存管理，也可以直接通过 `Unmanaged` 对应的方法来进行内存管理。

[ReachabilitySwift](https://github.com/ashleymills/Reachability.swift) 采取通过 callback 来进行内存管理的方式：

```swift
// Class ReachabilityWeakifier
class ReachabilityWeakifier {
    weak var reachability: Reachability?
    init(reachability: Reachability) {
        self.reachability = reachability
    }
}

func startNotifier() throws {
    guard !notifierRunning else { return }

    let callback: SCNetworkReachabilityCallBack = { (reachability, flags, info) in
        guard let info = info else { return }

        // info 是一个 UnsafeMutableRawPointer ，对应的是下面设置 context 的 info 类型
		  // 这里通过 Unmanaged 的 fromOpaque 来转换成 ReachabilityWeakifier ，这里不需要 takeRetainedValue ，
        // 内存管理由 context 对应的 callbacks 负责
        let weakifiedReachability = Unmanaged<ReachabilityWeakifier>.fromOpaque(info).takeUnretainedValue()
        weakifiedReachability.reachability?.flags = flags
    }

    let weakifiedReachability = ReachabilityWeakifier(reachability: self)
    // 这里同样不需要增加计数，调用 passUnretained 。
    let opaqueWeakifiedReachability = Unmanaged<ReachabilityWeakifier>.passUnretained(weakifiedReachability).toOpaque()

    var context = SCNetworkReachabilityContext(
        version: 0,
        info: UnsafeMutableRawPointer(opaqueWeakifiedReachability),
        retain: { (info: UnsafeRawPointer) -> UnsafeRawPointer in
            // 在 Unmanaged 和 UnsafeRawPointer 间转换，同时 retain 增加计数
            let unmanagedWeakifiedReachability = Unmanaged<ReachabilityWeakifier>.fromOpaque(info)
            _ = unmanagedWeakifiedReachability.retain()
            return UnsafeRawPointer(unmanagedWeakifiedReachability.toOpaque())
        },
        release: { (info: UnsafeRawPointer) -> Void in
			  // 调用 release 减少计数
            let unmanagedWeakifiedReachability = Unmanaged<ReachabilityWeakifier>.fromOpaque(info)
            unmanagedWeakifiedReachability.release()
        },
        copyDescription: { (info: UnsafeRawPointer) -> Unmanaged<CFString> in
            let unmanagedWeakifiedReachability = Unmanaged<ReachabilityWeakifier>.fromOpaque(info)
            let weakifiedReachability = unmanagedWeakifiedReachability.takeUnretainedValue()
            let description = weakifiedReachability.reachability?.description ?? "nil"
            return Unmanaged.passRetained(description as CFString)
        }
    )
	  // ...
}
```

[Alamofire](https://github.com/Alamofire/Alamofire) 在 `deinit` 时设置 `callback` 为 `nil` ，所以不需要额外进行生命周期的管理，老版本的 `Alamofire` 是这样，`5.0` 后可能在写代码时没注意，而且有大量代码提交， `review` 的时候没太注意，调用了 `Unmanaged.passRetained` ，造成内存泄露。

[10 lines of code = 10 issues.500 lines of code = “looks fine.”Code reviews.”](https://twitter.com/iamdevloper/status/397664295875805184) 。

我提了个 [Fix memory leak in NetworkReachabilityManager](https://github.com/Alamofire/Alamofire/pull/3180) ，已经 `merged` 了。

```swift
open func startListening(onQueue queue: DispatchQueue = .main,
                         onUpdatePerforming listener: @escaping Listener) -> Bool {
    stopListening()

    $mutableState.write { state in
        state.listenerQueue = queue
        state.listener = listener
    }
    // 都调用 unretainedValue 方法，不进行内存管理
    var context = SCNetworkReachabilityContext(version: 0,
                                               info: Unmanaged.passUnretained(self).toOpaque(),
                                               retain: nil,
                                               release: nil,
                                               copyDescription: nil)
    let callback: SCNetworkReachabilityCallBack = { _, flags, info in
        guard let info = info else { return }

        let instance = Unmanaged<NetworkReachabilityManager>.fromOpaque(info).takeUnretainedValue()
        instance.notifyListener(flags)
    }

    let queueAdded = SCNetworkReachabilitySetDispatchQueue(reachability, reachabilityQueue)
    let callbackAdded = SCNetworkReachabilitySetCallback(reachability, callback, &context)

    // Manually call listener to give initial state, since the framework may not.
    if let currentFlags = flags {
        reachabilityQueue.async {
            self.notifyListener(currentFlags)
        }
    }

    return callbackAdded && queueAdded
}
```

### 实现系统的 `swap` 方法

下面是 Swift 自己的实现， 为了减少 `retain/release` 带来的消耗，直接通过地址进行赋值操作：

```swift
@inlinable

public func swap<T>(_ a: inout T, _ b: inout T) {
  // Semantically equivalent to (a, b) = (b, a).
  // Microoptimized to avoid retain/release traffic.
  let p1 = Builtin.addressof(&a)
  let p2 = Builtin.addressof(&b)
  _debugPrecondition(
    p1 != p2,
    "swapping a location with itself is not supported")
  // Take from P1.
  let tmp: T = Builtin.take(p1)
  // Transfer P2 into P1.
  Builtin.initialize(Builtin.take(p2) as T, p1)
  // Initialize P2.
  Builtin.initialize(tmp, p2)
}
```

Builtin 是 Swift 内部框架，用于跟 LLVM IR 的类型进行交互。所以我使用 `UnsafeMutableRawPointer` 来实现自己 `swap` 方法：

```swift
func mySwap<T>(_ a: inout T, _ b: inout T) {

    let p1 = withUnsafeMutablePointer(to: &a) { (pointer) -> UnsafeMutableRawPointer in
        UnsafeMutableRawPointer(pointer)
    }
    let p2 = withUnsafeMutablePointer(to: &b) { (pointer) -> UnsafeMutableRawPointer in
        UnsafeMutableRawPointer(pointer)
    }
    guard p1 != p2 else {
        fatalError()
    }
    let temp = p1.load(as: T.self)
    p1.storeBytes(of: b, as: T.self)
    p2.storeBytes(of: temp, as: T.self)
}
```

## 总结

由于安全的原因，在 Swift 上使用指针显得比较啰嗦，需要写一点代码来保证安全。虽然大多数情况下我们不需要与指针交互，但是当我们需要与某些 C 的库打交道，或者需要进行一些极致的性能优化时，熟悉指针的基本操作和相关知识可以让我们避免像上面那样造成内存泄露或者出现崩溃的情况。当然，进行指针操作应该是我们最后的手段，如果不足够谨慎，有可能带来的只是负收益。

## 参考

[The 5-Minute Guide to C Pointers](https://denniskubes.com/2017/01/24/the-5-minute-guide-to-c-pointers/) [Swift 皇冠上的明珠：不安全的 Swift 和指针类型](https://academy.realm.io/cn/posts/nate-cook-tryswift-tokyo-unsafe-swift-and-pointer-types/) [Swift 对象内存模型探究（一）](https://mp.weixin.qq.com/s/zIkB9KnAt1YPWGOOwyqY3Q) [Swifter - Swift 必备 tips - UNSAFEPOINTER](https://swifter.tips/unsafe/) [UnsafeRawPointer - Swift Standard Library | Apple Developer Documentation](https://developer.apple.com/documentation/swift/unsaferawpointer) [swift-evolution/0101-standardizing-sizeof-naming](https://github.com/apple/swift-evolution/blob/9cf2685293108ea3efcbebb7ee6a8618b83d4a90/proposals/0101-standardizing-sizeof-naming.md) [Calling Functions With Pointer Parameters | Apple Developer Documentation](https://developer.apple.com/documentation/swift/swift_standard_library/manual_memory_management/calling_functions_with_pointer_parameters) [Swift 中的指针使用](https://onevcat.com/2015/01/swift-pointer/)
