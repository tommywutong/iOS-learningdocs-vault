---
title: 'Friday Q&A 2014-08-29：Swift 内存转储'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-08-29-swift-memory-dumping.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e8a0896daa6c4fe6'
translated: true
---

> 原文：[Friday Q&A 2014-08-29: Swift Memory Dumping](https://www.mikeash.com/pyblog/friday-qa-2014-08-29-swift-memory-dumping.html)　·　mikeash.com Friday Q&A

发布于 2014-08-29 13:24 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([完整文本 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[短暂暂停](https://www.mikeash.com/pyblog/a-brief-pause.html)  
上一篇文章：[Friday Q&A 2014-08-15：Swift 名称修饰](https://www.mikeash.com/pyblog/friday-qa-2014-08-15-swift-name-mangling.html)

Friday Q&A 2014-08-29：Swift 内存转储

作者：[Mike Ash](https://www.mikeash.com/)

**代码**  
按惯例，内存转储器的完整代码可在 GitHub 上找到：

[https://github.com/mikeash/memorydumper](https://github.com/mikeash/memorydumper)

你可以在那里查看代码以便更轻松地跟上进度，自己运行它，或者干脆忽略它。

请注意，这段代码**不应**被视为风格、实现或任何方面的良好示例。Swift 对我们所有人来说都还比较新，这在我的代码中肯定有所体现。不过，至少它能让我们看到**如何**完成某些事情。

**指针**  
我们将大量使用指针。Swift 对原始指针的支持还算不错，但尚未完全达到这里所需的程度。这段代码确实希望将指针视为恰好代表地址的普通整数。为了简化这一点，`Pointer` `struct` 包含一个 `UInt` 类型的地址，以及一些用于处理指针的实用方法：

```
    struct Pointer: Hashable, Printable {
```

它实现了 `Hashable` 以便能在 `Dictionary` 中使用，而 `Printable` 则便于调试。它包含一个变量，即指针地址：

```
        let address: UInt
```

`Hashable` 的实现只是将地址转换为 `Int` 并返回。它不关心保留值或检测溢出，只想直接传递这些位。内置函数 `unsafeBitCast` 正是为此而生：

```
        var hashValue: Int {
            return unsafeBitCast(address, Int.self)
        }
```

对于 `Printable`，`NSString` 的 `format:` 初始化方法可以轻松创建地址的人类可读表示形式：

```
        var description: String {
            return NSString(format: "0x%0*llx", sizeof(address.dynamicType) * 2, address)
        }
```

`dladdr` 函数接受一个指针并返回对应符号的信息。具体来说，它返回包含该指针的二进制文件的路径名、该二进制文件的基地址、符号名称以及该符号的起始地址。这些信息对其他函数很有用，但直接调用 `dladdr` 有点麻烦，因此封装一下会很有帮助。由于调用可能会失败，它返回一个可选值：

```
        func symbolInfo() -> Dl_info? {
```

它首先创建一个 `Dl_info` `struct`。在 C 语言中，我们只需声明它并让它保持未初始化状态，但 Swift 需要一个初始值，因此这段代码只是创建了一个空的 `struct`：

```
            var info = Dl_info(dli_fname: "", dli_fbase: nil, dli_sname: "", dli_saddr: nil)
```

指针参数的类型是 `UnsafePointer`，但指针地址是 `UInt`。`unsafeBitCast` 函数弥合了这一差距：

```
            let ptr: UnsafePointer<Void> = unsafeBitCast(address, UnsafePointer<Void>.self)
```

有了这些变量后，实际调用就很简单了：

```
            let result = dladdr(ptr, &info)
```

`dladdr` 返回零表示失败，其他任何值表示成功。这决定了返回 `Dl_info` `struct` 还是 `nil`：

```
            return (result == 0 ? nil : info)
        }
```

符号名称作为内存转储的一部分显示是非常有用的信息。`Dl_info` `struct` 包含符号名称，但直接使用它有两个问题。首先，它是一个 C 字符串，因此必须转换为更友好的形式才能使用。其次，`dladdr` 查找的是指定地址之前最近的符号，而我们只希望在地址与符号地址完全匹配时（而不是有偏移时）才返回符号名称。这个 `symbolName` 函数处理了这些问题：

```
        func symbolName() -> String? {
```

`symbolInfo` 可能会失败，因此需要检查调用结果：

```
            if let info = symbolInfo() {
```

返回的符号地址是一个 `UnsafePointer`，但我们想要与 `address` 进行比较，并且只在它们相等时才返回符号名称。另一个 `unsafeBitCast` 调用解决了这个问题：

```
                let symbolAddress: UInt = unsafeBitCast(info.dli_saddr, UInt.self)
```

如果符号地址等于指针地址，则返回符号名称：

```
                if symbolAddress == address {
                    return String.fromCString(info.dli_sname)
                }
```

如果它们不匹配，或者 `dladdr` 完全失败，则返回 `nil`：

```
            }
            return nil
        }
```

另一个有用的函数是返回当前指针之后下一个符号的指针。符号不编码长度，只编码位置，但查找后续符号的位置可以为猜测长度提供一个合理的终点。内存转储代码将使用此信息来确定要读取多少内存。我们不想在出现问题时跑到超空间去，因此此函数还接受一个限制，用于搜索下一个符号的最大距离。它返回一个可选的 `Pointer`，`nil` 表示未找到后续符号：

```
        func nextSymbol(limit: Int) -> Pointer? {
```

和之前一样，调用 `symbolInfo` 可能会失败，必须进行检查：

```
            if let myInfo = symbolInfo() {
```

搜索策略是逐字节迭代，每次调用 `symbolInfo`。如果返回的符号基地址发生变化，则说明找到了一个新符号。如果在达到限制之前没有找到新符号，则返回 `nil`。首先，它从 `1` 循环到 `limit`：

```
                for i in 1..<limit {
```

通过将 `i` 加到 `self` 来生成一个候选指针，并获取其符号信息：

```
                    let candidate = self + i
                    let candidateInfo = candidate.symbolInfo()
```

如果 `symbolInfo` 失败，则搜索失败，返回 `nil`：

```
                    if candidateInfo == nil {
                        return nil
                    }
```

如果返回的地址与当前符号不同，则搜索成功，返回候选指针：

```
                    if myInfo.dli_saddr != candidateInfo!.dli_saddr {
                        return candidate
                    }
```

如果循环终止或最初的 `symbolInfo` 调用失败，则返回 `nil`：

```
                }
            }
            return nil
        }
    }
```

`Hashable` 包含 `Equatable`，这意味着 `Pointer` 需要实现 `==` 运算符：

```
    func ==(a: Pointer, b: Pointer) -> Bool {
        return a.address == b.address
    }
```

为了方便，`Pointer` 还实现了 `+` 和 `-` 运算符：

```
    func +(a: Pointer, b: Int) -> Pointer {
        return Pointer(address: a.address + UInt(b))
    }

    func -(a: Pointer, b: Pointer) -> Int {
        return Int(a.address - b.address)
    }
```

**内存**  
我们还将大量处理内存内容。从根本上说，一块内存只是一个字节数组，但我们希望存储一些关于它是什么类型内存的信息，并且我们想要一些有助于读取和扫描内存的函数。`Memory` `struct` 存储一个字节数组以及两个标志，分别指定内存是否由 `malloc` 分配以及它是否对应一个符号：

```
    struct Memory {
        let buffer: [UInt8]
        let isMalloc: Bool
        let isSymbol: Bool
```

这两个标志实际上不能同时为 `true`，因此有人可能会争辩说这应该是一个包含三种情况的 `enum`。不过，我认为使用两个标志操作起来更自然一些。

你如何**获取**一块内存？基本操作是接受一个 `Pointer` 并将其指向的内存读取到一个数组中：

```
        static func readIntoArray(ptr: Pointer, var _ buffer: [UInt8]) -> Bool {
```

在 Objective-C 中实现此功能的自然方法是将指针转换为 `void *`，然后调用 `memcpy`。事实上，在 Swift 中你也可以做几乎相同的事情。`Array` 上的 `withUnsafeBufferPointer` 方法可以让你获取目标缓冲区存储的指针，并且 `memcpy` 可以从 Swift 中调用。这种方法的缺点在于，无论使用哪种语言，如果指针无效或读取的数据量过长，它都会崩溃。

解决方案是使用 mach 虚拟内存调用来读取内存。这些调用请求内核代表你读取内存，并且内核拥有安全执行读取和优雅失败所需的所有信息。具体来说，`mach_vm_read_overwrite` 调用会将指针指向的内存读取到缓冲区中，如果内存不可读，则返回一个错误码。这就是我们在 [PLCrashReporter](https://www.plcrashreporter.org/) 中用于读取可能已在崩溃中损坏的数据结构时使用的方法。它在这里也运行得很好。

为了读取到 `buffer` 中，我们需要获取其存储的指针。`withUnsafeBufferPointer` 负责处理这件事：

```
            let result = buffer.withUnsafeBufferPointer {
                (targetPtr: UnsafeBufferPointer<UInt8>) -> kern_return_t in
```

`withUnsafeBufferPointer` 不直接返回指针。相反，它调用一个函数并将指针作为参数传递。它返回该函数返回的任何值。我们将返回 `mach_vm_read_overwrite` 的结果码，因此返回类型是 `kern_return_t`。

`mach_vm_read_overwrite` 将要读取的指针作为 64 位无符号整数，因此我们必须转换 `ptr` 的地址：

```
                let ptr64 = UInt64(ptr.address)
```

我们还需要将目标指针作为 64 位无符号整数。`unsafeBitCast` 函数负责将其转换为整数，然后可以将其转换为 `UInt64`：

```
                let target: UInt = unsafeBitCast(targetPtr.baseAddress, UInt.self)
                let target64 = UInt64(target)
```

该函数还使用一个输出参数返回实际读取的数据量。这个值对我们来说没用（据我所知，如果调用成功，它总是请求的量），但我们仍然必须传入一个指针供它写入，因此我们需要一个局部变量：

```
                var outsize: mach_vm_size_t = 0
```

所有参数就位后，就可以进行调用了：

```
                return mach_vm_read_overwrite(mach_task_self_, ptr64, mach_vm_size_t(buffer.count), target64, &outsize)
            }
```

在闭包之外，`result` 现在包含 `mach_vm_read_overwrite` 返回的结果码。如果它返回 `KERN_SUCCESS`，则 `buffer` 现在已填充了目标内存的内容。我们将结果码简化为一个简单的 `true`/`false` 返回给调用者：

```
            return result == KERN_SUCCESS
        }
```

接下来，我们需要一种方法，通过读取某个 `Pointer` 的内容，将其转换为一个 `Memory` 实例。`readIntoArray` 构成了这个过程的基础，但它需要一个大小，而我们通常**不会**知道任意 `Pointer` 的大小。`read` 函数接受一个 `Pointer` 和一个可选已知大小，并返回一个可选的 `Memory`：

```
        static func read(ptr: Pointer, knownSize: Int? = nil) -> Memory? {
```

第一步是尝试猜测指针所指向内存的大小。由于我们在追踪任意指针，我们并不总能可靠地确定这一点。我们将从调用 `malloc_size` 开始。这需要使用我们的老朋友 `unsafeBitCast` 将 `Pointer` 的地址转换为 `UnsafePointer`：

```
            let convertedPtr: UnsafePointer<Void> = unsafeBitCast(ptr.address, UnsafePointer<Void>.self)
            var length = Int(malloc_size(convertedPtr))
```

如果内存不是通过 `malloc` 分配的，`malloc_size` 会十分贴心地返回零。（文档中并未保证这一点，因此请不要编写依赖此特性的生产代码。）因此，我们可以通过检查 `length` 来填充 `isMalloc`：

```
            let isMalloc = length > 0
```

我们将通过检查指针是否有符号名称来填充 `isSymbol`：

```
            let isSymbol = ptr.symbolName() != nil
```

如果它是一个符号，那么我们将尝试通过查看从该符号到下一个符号的距离来猜测长度：

```
            if isSymbol {
                if let nextSymbol = ptr.nextSymbol(4096) {
                    length = nextSymbol - ptr
                }
            }
```

猜测长度可能会失败，并且可能没有已知大小。在这种情况下，我们将尝试连续读取 8 字节的内存块，直到读取失败或达到某个合理的长度：

```
            if length == 0 && knownSize == nil {
```

读取结果累积在一个初始为空的数组中：

```
                var result = [UInt8]()
```

我随意选择了一个 128 字节的限制来读取数据：

```
                while (result.count < 128) {
```

要读取 8 个字节，先创建一个 8 字节数组并调用 `readIntoArray`：

```
                    var eightBytes = [UInt8](count: 8, repeatedValue: 0)
                    let success = readIntoArray(ptr + result.count, eightBytes)
```

如果失败，则结束循环。否则，追加到 `result` 并继续：

```
                    if !success {
                        break
                    }
                    result.extend(eightBytes)
                }
```

如果根本读不到任何内容，则返回 `nil`。否则，创建一个新的 `Memory` 实例并返回：

```
                return (result.count > 0
                    ? Memory(buffer: result, isMalloc: false, isSymbol: isSymbol)
                    : nil)
```

如果能够猜测出大小或大小已知，情况就简单一些。创建一个适当大小的数组并读取其中：

```
            } else {
                if knownSize != nil {
                    length = knownSize!
                }

                var result = [UInt8](count: length, repeatedValue: 0)
                let success = readIntoArray(ptr, result)
```

如果读取成功，则返回一个 `Memory` 实例，否则返回 `nil`：

```
                return (success
                    ? Memory(buffer: result, isMalloc: isMalloc, isSymbol: isSymbol)
                    : nil)
            }
        }
```

内存转储器是递归工作的。它将一个指针读入一个缓冲区，从该缓冲区中提取指针，然后将这些指针读入缓冲区，并继续以这种方式进行。从缓冲区中提取指针是该过程的基础部分。很难确切知道缓冲区的哪些部分是指针。为了转储器的目的，它会假设每个自然对齐的、大小等于指针的量都是一个指针。猜错了也没什么大碍，因为内存读取器能容忍无效的指针。`scanPointers` 函数不接受参数（因为它操作的是 `Memory` 实例的内部缓冲区），并返回一个 `PointerAndOffset` 实例的数组。这是一个简单的 `struct`，包含一个 `Pointer` 和一个 `Int` 类型的偏移量。偏移量在打印结果时在其他地方很有用，因为它可以精确显示指针被发现的位置。以下是函数声明：

```
        func scanPointers() -> [PointerAndOffset] {
```

结果累积在一个数组中：

```
            var pointers = [PointerAndOffset]()
```

`Memory` 实例的内容位于 `buffer` 中，它是一个 `UInt8` 数组。我们需要从中读取指针大小的块。一种方法是每次读取几个元素，然后进行一些位移操作来构造一个指针。或者，既然我们已经在肆无忌惮地使用「不安全」的东西，我们可以直接将其转换为 `UInt` 指针并直接读取数据：

```
            buffer.withUnsafeBufferPointer {
                (memPtr: UnsafeBufferPointer<UInt8>) -> Void in

                let ptrptr = UnsafePointer<UInt>(memPtr.baseAddress)
```

`ptrptr` 包含一个指向缓冲区的指针，将其视为一个 `UInt` 数组。一个循环提取出其中包含的每个 `Pointer`：

```
                let count = self.buffer.count / 8
                for i in 0..<count {
                    pointers.append(PointerAndOffset(pointer: Pointer(address: ptrptr[i]), offset: i * 8))
                }
            }
```

数组填充完毕后，剩下的就是将其返回给调用者：

```
            return pointers
        }
```

许多内存块包含字符串，扫描字符串并以人类可读的形式打印出来是很有用的。不可能确切知道一块内存是否真的包含一个字符串，还是只包含恰好看起来像字符串的二进制数据，但通过一些启发式方法，可以做得相当不错。我选择将范围在 32-126（含）之间的任何至少连续四个字节的序列视为字符串。这个范围是 ASCII 字符中排除了不可打印控制字符的部分。与 `scanPointers` 类似，`scanStrings` 函数不接受参数并返回一个 `String` 数组：

```
        func scanStrings() -> [String] {
```

首先，创建上下限常量：

```
            let lowerBound: UInt8 = 32
            let upperBound: UInt8 = 126
```

当前的候选序列存储在一个局部数组中，到目前为止累积的字符串也如此：

```
            var current = [UInt8]()
            var strings = [String]()
```

现在，遍历缓冲区。程序在遍历缓冲区时，会在其末尾附加一个零字节，以确保每个候选序列都以一个超出边界的字节结束。这避免了在循环结束后对 `current` 进行最终检查的需要：

```
            for byte in buffer + [0] {
```

如果字节在边界内，则将其附加到 `current`：

```
                if byte >= lowerBound && byte <= upperBound {
                    current.append(byte)
```

否则，如果 `current` 包含至少四个字节，则将其转换为 `String` 并添加到 `strings` 中：

```
                } else {
                    if current.count >= 4 {
                        var str = String()
                        for byte in current {
                            str.append(UnicodeScalar(byte))
                        }
                        strings.append(str)
                    }
```

可能有更好的方法从 `UInt8` 数组创建 `String`，但这个方法已经足够好了。最后，为下一轮清空 `current`：

```
                    current.removeAll()
                }
            }
```

一切都完成后，返回这些字符串：

```
            return strings
        }
```

以十六进制原始形式显示内存内容也很不错。`hex` 函数处理此事：

```
        func hex() -> String {
```

我们希望每 8 个字节有一个空格：

```
            let spacesInterval = 8
```

输出累积在一个 `NSMutableString` 中。在追加时使用格式字符串的能力使得处理十六进制更容易：

```
            let str = NSMutableString(capacity: buffer.count * 2)
```

遍历缓冲区。使用 `enumerate` 来同时获取索引和字节值：

```
            for (index, byte) in enumerate(buffer) {
```

每 `spacesInterval` 个字节，添加一个空格：

```
                if index > 0 && (index % spacesInterval) == 0 {
                    str.appendString(" ")
                }
```

以十六进制形式添加当前字节：

```
                str.appendFormat("%02x", byte)
            }
```

一切完成后，返回累积的字符串：

```
            return str
        }
    }
```

为了完整起见，以下是上面使用的 `PointerAndOffset` `struct`：

```
    struct PointerAndOffset {
        let pointer: Pointer
        let offset: Int
    }
```

**打印**  
其余大部分代码涉及打印结果。内存转储器如果不显示找到的内容，就没多大用处。为了更轻松地以有用的方式打印结果，我构建了一个其他代码使用的 `Printer` 协议，以及一组实用函数。可以实现 `Printer` 协议来以不同形式输出结果。在这里，我将展示终端打印机的实现。我还创建了一个输出 HTML 的实现，你可以在 GitHub 上看到。

颜色是一种有用的方式，可以显示不同打印项之间的关系。一个 `enum` 定义了可用于打印的颜色：

```
    enum PrintColor {
        case Default
        case Red
        case Green
        case Yellow
        case Blue
        case Magenta
        case Cyan
    }
```

`Printer` 协议定义了打印机对象所需的能力。它并不多：允许用颜色打印字符串、用默认颜色打印字符串、打印换行符以及终止输出（在编写 HTML 时关闭标签是必需的）：

```
    protocol Printer {
        func print(color: PrintColor, _ str: String)
        func print(str: String)
        func println()
        func end()
    }
```

`TermPrinter` 类实现了 `Printer`：

```
    class TermPrinter: Printer {
```

在终端打印时，你可以使用包含颜色代码的转义序列来生成颜色。这个字典将 `PrintColor` `enum` 值映射到相应的颜色代码：

```
        let colorCodes: Dictionary<PrintColor, String> = [
            .Default: "39",
            .Red: "31",
            .Green: "32",
            .Yellow: "33",
            .Blue: "34",
            .Magenta: "35",
            .Cyan: "36"
        ]
```

颜色的完整转义序列由转义字符（ASCII 码 27）、一个 `[` 字符、数值颜色代码，然后是一个 `m` 字符组成。一个 `printEscape` 工具函数将 `PrintColor` 输出到终端作为相应转义序列的过程封装起来：

```
        func printEscape(color: PrintColor) {
            Swift.print("\u{1B}[\(colorCodes[color]!)m")
        }
```

注意，由于 `print` 被定义为本地方法，因此使用 `Swift.print` 来访问内置函数。

基本的 `print` 方法使用 `printEscape` 来打印给定颜色的转义码，打印字符串，然后为了安全起见恢复到默认颜色：

```
        func print(color: PrintColor, _ str: String) {
            printEscape(color)
            Swift.print(str)
            printEscape(.Default)
        }
```

单参数版本的方法只是用 `.Default` 调用双参数版本：

```
        func print(str: String) {
            print(.Default, str)
        }
```

`println` 只是调用内置函数：

```
        func println() {
            Swift.println()
        }
```

最后，`end()` 方法是空的，因为不需要做任何事情来结束终端打印：

```
        func end() {}
    }
```

一些便捷函数有助于生成格式良好的输出。这个 `pad` 函数如果字符串短于所需长度，则将其左对齐或右对齐。它并不那么有趣，因此我就不详细说明了：

```
    enum Alignment {
        case Right
        case Left
    }

    func pad(value: Any, minWidth: Int, padChar: String = " ", align: Alignment = .Right) -> String {
        var str = "\(value)"
        var accumulator = ""

        if align == .Left {
            accumulator += str
        }

        if minWidth > countElements(str) {
            for i in 0..<(minWidth - countElements(str)) {
                accumulator += padChar
            }
        }

        if align == .Right {
            accumulator += str
        }

        return accumulator
    }
```

类似地，`limit` 函数会截断超过最大长度的字符串：

```
    func limit(str: String, maxLength: Int, continuation: String = "...") -> String {
        if countElements(str) <= maxLength {
            return str
        }

        let start = str.startIndex
        let truncationPoint = advance(start, maxLength)
        return str[start..<truncationPoint] + continuation
    }
```

**Objective-C 类**  
在内存中探查时通常会遇到 Objective-C 类，因此为它们提供一些特殊处理是很有用的。这个 `struct` 封装了一个类：

```
    struct ObjCClass {
```

它包含一个从 `Pointer` 值到 `ObjCClass` 实例的映射：

```
        static let classMap: Dictionary<Pointer, ObjCClass> = {
            var tmpMap = Dictionary<Pointer, ObjCClass>()
            for c in AllClasses() { tmpMap[c.address] = c }
            return tmpMap
        }()
```

我稍后会展示 `AllClasses` 的实现。该字典被封装在一个函数中，使得事情稍微好一点：

```
        static func atAddress(address: Pointer) -> ObjCClass? {
            return classMap[address]
        }
```

一个静态辅助函数有助于转储对象的类以及所有超类：

```
        static func dumpObjectClasses(p: Printer, _ obj: AnyObject) {
            var classPtr: AnyClass! = object_getClass(obj)
            while classPtr != nil {
                ObjCClass(address: Pointer(address: unsafeBitCast(classPtr, UInt.self)), name: String.fromCString(class_getName(classPtr))!).dump(p)
                classPtr = class_getSuperclass(classPtr)
            }
        }
```

这个 `struct` 只是包装了一个 `Pointer`，因为所有其他数据都可以使用该指针从 Objective-C 运行时中检索：

```
        let address: Pointer
```

一个计算属性使得以 `AnyClass` 的形式检索 `address` 变得方便，这是 Objective-C 运行时函数希望看到的类型。我们的好朋友 `unsafeBitCast` 再次出现：

```
        var classPtr: AnyClass {
            return unsafeBitCast(address.address, AnyClass.self)
        }
```

有几段代码希望获取类的名称，一个计算属性简化了这一点：

```
        var name: String {
            return String.fromCString(class_getName(classPtr))!
        }
```

最后，我们希望类能够将自身转储到 `Printer`：

```
        func dump(p: Printer) {
```

在使用 Objective-C 运行时函数时，有一个非常常见的模式：函数返回一个指向以 `NULL` 结尾的数组的指针，并且你在使用完该数组后需要 `free` 它。在 Swift 中，这些指针被表示为 `UnsafeMutablePointer<COpaquePointer>`，因此一个便捷函数可以封装这些烦人的工作：

```
            func iterate(pointer: UnsafeMutablePointer<COpaquePointer>, callForEach: (COpaquePointer) -> Void) {
                if pointer != nil {
                    var i = 0
                    while pointer[i] != nil {
                        callForEach(pointer[i])
                        i++
                    }
                    free(pointer)
                }
            }
```

它首先打印类名，对于 `NSObject`，它只做这些：

```
            p.print("Objective-C class \(name)")

            if class_getName(classPtr) == "NSObject" {
                println()
            } else {
```

否则，它会使用 `iterate` 和尾随闭包语法转储出实例变量、属性和方法，使这项工作变得容易：

```
                p.print(":")
                p.println()
                iterate(class_copyIvarList(classPtr, nil)) {
                    p.print("    Ivar: \(ivar_getName($0)) \(ivar_getTypeEncoding($0))")
                    p.println()
                }
                iterate(class_copyPropertyList(classPtr, nil)) {
                    p.print("    Property: \(property_getName($0)) \(property_getAttributes($0))")
                    p.println()
                }
                iterate(class_copyMethodList(classPtr, nil)) {
                    p.print("    Method: \(sel_getName(method_getName($0))) \(method_getTypeEncoding($0))")
                    p.println()
                }
            }
        }
    }
```

`AllClasses` 函数调用 `objc_copyClassList` 并遍历结果：

```
    func AllClasses() -> [ObjCClass] {
        var count: CUnsignedInt = 0
        let classList = objc_copyClassList(&count)

        var result = [ObjCClass]()

        for i in 0..<count {
```

提取该索引处的类指针，然后 `unsafeBitCast` 再次登场，以便将其转换为 `Pointer`：

```
            let rawClass: AnyClass! = classList[Int(i)]
            let address: Pointer = Pointer(address: unsafeBitCast(rawClass, UInt.self))
```

从 `Pointer` 创建一个 `ObjCClass` 并添加到 `result` 数组中：

```
            result.append(ObjCClass(address: address))
        }
```

然后将 `result` 数组返回给调用者：

```
        return result
    }
```

**扫描数据结构**  
我们现在可以开始查看实际的扫描机制了。每个要扫描的内存地址都被包装在一个 `ScanEntry` 实例中。它持有一个父条目，指示指针被发现的位置、父条目内的偏移量、扫描地址以及一个索引。索引用于为每个条目分配一个数字，以便于在输出中交叉引用。这是一个 `class` 而不是 `struct`，因为多个数据结构需要引用同一个实例，并可能对其进行变动或看到其变动。以下是定义：

```
    class ScanEntry {
        let parent: ScanEntry?
        var parentOffset: Int
        let address: Pointer
        var index: Int

        init(parent: ScanEntry?, parentOffset: Int, address: Pointer, index: Int) {
            self.parent = parent
            self.parentOffset = parentOffset
            self.address = address
            self.index = index
        }
    }
```

对 `ScanEntry` 实际执行扫描会产生一个 `ScanResult`。一个 `ScanResult` 指向一个条目和一个父级。它还包含一个表示其内容的 `Memory`、一个子结果数组、一个缩进级别以及一个打印颜色：

```
    class ScanResult {
        let entry: ScanEntry
        let parent: ScanResult?
        let memory: Memory
        var children = [ScanResult]()
        var indent = 0
        var color: PrintColor = .Default
```

`init` 设置 `let` 变量：

```
        init(entry: ScanEntry, parent: ScanResult?, memory: Memory) {
            self.entry = entry
            self.parent = parent
            self.memory = memory
        }
```

为 `ScanResult` 获取一个名称很方便，但并非像查找那样简单：

```
        var name: String {
```

如果这个条目恰好引用了一个 Objective-C 类，那么我们可以向该类询问其名称：

```
            if let c = ObjCClass.atAddress(entry.address) {
                return c.name
            }
```

如果该条目引用了一个 Objective-C **对象**，那么内存的第一个指针大小的块将是一个指向该对象类的 `isa`。至少在那些不使用的[非指针 isa](http://www.sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html) 架构和操作系统上是这样。`Memory` 的 `scanPointers` 方法可以很容易（尽管效率不高）地获取第一个指针。如果第一个指针存在（即内存至少足够长以容纳一个指针）并且它指向一个 Objective-C 类，我们就伪造一个 `-description` 样式的名称并返回它：

```
            let pointers = memory.scanPointers()
            if pointers.count > 0 {
                if let c = ObjCClass.atAddress(pointers[0].pointer) {
                    return "<\(c.name): \(entry.address.description)>"
                }
            }
```

如果所有方法都失败了，则返回底层 `Pointer` 的 `description`：

```
            return entry.address.description
        }
```

一个条目知道如何将自身 `dump` 到 `Printer`：

```
        func dump(p: Printer) {
```

如果该条目有父级，它会打印父级的地址以及该条目在其中的偏移量，全部使用父级的颜色，以便于视觉交叉引用。否则，它会打印这是根指针的事实：

```
            if let parent = entry.parent {
                p.print("(")
                p.print(self.parent!.color, "\(pad(parent.index, 3)), \(pad(self.parent!.name, 24))@\(pad(entry.parentOffset, 3, align: .Left))")
                p.print(") <- ")
            } else {
                p.print("Starting pointer: ")
            }
```

接下来，打印条目的索引、描述和大小：

```
            p.print(color, "\(pad(entry.index, 3)) \(entry.address.description): ")

            p.print(color, "\(pad(memory.buffer.count, 5)) bytes ")
```

接下来，打印内存类型，无论是来自 `malloc`、是符号，还是只是未知类型：

```
            if memory.isMalloc {
                p.print(color, "<malloc> ")
            } else if memory.isSymbol {
                p.print(color, "<symbol> ")
            } else {
                p.print(color, "<unknwn> ")
            }
```

之后，转储内存内容，限制大块内存以节省大量空间：

```
            p.print(color, limit(memory.hex(), 101))
```

如果有符号名称，也要打印出来：

```
            if let symbolName = entry.address.symbolName() {
                p.print(" Symbol \(symbolName)")
            }
```

如果是一个 Objective-C 类，则打印出来：

```
            if let objCClass = ObjCClass.atAddress(entry.address) {
                p.print(" ObjC class \(objCClass.name)")
            }
```

如果内存包含任何人类可读的字符串，也打印出来：

```
            let strings = memory.scanStrings()
            if strings.count > 0 {
                p.print(" -- strings: (")
                p.print(", ".join(strings))
                p.print(")")
            }
```

然后打印一个换行符，我们就完成了：

```
            p.println()
        }
```

转储单个 `ScanResult` 并不那么有趣。有趣的是转储整个层级结构：

```
        func recursiveDump(p: Printer) {
```

有子级的条目将被分配一个颜色。为了确保多样性，颜色是通过在扫描每个条目时遍历一个颜色数组来选择的。一个辅助函数封装了这一切：

```
            var entryColorIndex = 0
            let entryColors: [PrintColor] = [ .Red, .Green, .Yellow, .Blue, .Magenta, .Cyan ]
            func nextColor() -> PrintColor {
                return entryColors[entryColorIndex++ % entryColors.count]
            }
```

要转储整个树，我们跟踪一个待处理条目的数组。我们从数组中移除一个条目并检查它。如果它有子级，我们将这些子级添加到数组中。我们一直这样做，直到数组用尽：

```
            var chain = [self]
            while chain.count > 0 {
```

要扫描的结果从数组末尾弹出：

```
                let result = chain.removeLast()
```

有子级的结果被分配一个颜色：

```
                if result.children.count > 0 {
                    result.color = nextColor()
                }
```

结果被缩进，然后转储：

```
                for i in 0..<result.indent {
                    p.print("  ")
                }
                result.dump(p)
```

然后子级被添加到数组中。它们的缩进也在此时设置：

```
                for child in result.children.reverse() {
                    child.indent = result.indent + 1
                    chain.append(child)
                }
            }
        }
    }
```

`reverse()` 改变了子级打印的顺序，导致第一个子级首先被打印。条目被添加到数组末尾以及从末尾移除的事实也改变了打印的方式，使其成为深度优先打印而不是广度优先打印。可以更改这些来改变转储输出的组织方式。

**扫描**  
我们终于到达了拼图的最后一块。`scanmem` 函数接受一个任意值并返回一个表示该值的 `ScanResult`。它还接受一个限制，即在返回之前要扫描多少个条目。否则，它可能会产生**大量**输出，因为它最终会扫描整个 Objective-C 类树以及它指向的所有内容。限制它可以避免它跑偏，并有助于确保输出与我们想要查看的内容相关。

该函数使用泛型编写，以确保它在调用者传入的值的精确类型上工作，并避免像 `Any` 可能发生的那种装箱或包装：

```
    func scanmem<T>(var x: T, limit: Int) -> ScanResult {
```

到目前为止看到的条目数量保存在 `count` 中：

```
        var count = 0
```

为了避免无限循环，跟踪已经看过的条目。一个映射到 `Void` 的 `Dictionary` 构成了一个方便的集合类型：

```
        var seen = Dictionary<Pointer, Void>()
```

待扫描的条目保存在一个数组中：

```
        var toScan = Array<ScanEntry>()
```

结果保存在以 `Pointer` 为键的 `Dictionary` 中，以便子级可以轻松地与其父级匹配：

```
        var results = Dictionary<Pointer, ScanResult>()
```

为了转储 `x`，我们需要一个指向它的指针。`withUnsafePointer` 函数接受一个值并提供指向它的指针。我们将获取那个指针，然后在内部完成所有脏活累活，最后返回根 `ScanResult`：

```
        return withUnsafePointer(&x) {
            (ptr: UnsafePointer<T>) -> ScanResult in
```

我们的朋友 `unsafeBitCast` 处理将 `ptr` 转换为 `UInt`，以便可用于创建 `Pointer`：

```
            let firstAddr: Pointer = Pointer(address: unsafeBitCast(ptr, UInt.self))
```

这个第一个地址的 `ScanEntry` 没有父级、没有偏移量，索引为零：

```
            let firstEntry = ScanEntry(parent: nil, parentOffset: 0, address: firstAddr, index: 0)
```

将 `firstAddr` 标记为已见，并将 `firstEntry` 添加到 `toScan` 数组：

```
            seen[firstAddr] = ()
            toScan.append(firstEntry)
```

扫描循环包括重复拉取一个条目、扫描它，并将子条目添加到 `toScan` 数组中，直到达到扫描限制或没有更多内容可扫描：

```
            while toScan.count > 0 && count < limit {
```

从数组末尾拉取要扫描的条目：

```
                let entry = toScan.removeLast()
```

从 `count` 设置条目的索引：

```
                entry.index = count
```

读取 `ScanEntry` 地址处的底层内存。在特殊情况下，当 `count` 为零并且我们**知道**我们正在读取 `x` 时，我们可以通过使用 `sizeof` 获取 `T` 的大小来向函数传入已知大小。否则，我们将传入 `nil` 并让 `Memory.read` 自己尝试确定大小：

```
                let memory: Memory! = Memory.read(entry.address, knownSize: count == 0 ? sizeof(T.self) : nil)
```

读取可能会失败。如果失败，那么 `entry` 可能不是一个真正的指针，我们将跳过它。否则，继续：

```
                if memory != nil {
```

如果它是一个真正的条目，那么我们可以增加 `count`：

```
                    count++
```

通过在 `results` 中查找父级的地址（如果存在）来查找父 `ScanResult`：

```
                    let parent = entry.parent.map{ results[$0.address] }?
```

为当前条目创建一个 `ScanResult`：

```
                    let result = ScanResult(entry: entry, parent: parent, memory: memory)
```

如果存在父 `ScanResult`，则将此条目添加到其子级中：

```
                    parent?.children.append(result)
```

也将其添加到 `results` 中：

```
                    results[entry.address] = result
```

这样就处理了该条目的 `ScanResult`。现在是时候为它包含的任何指针创建新条目了。首先，扫描内存中的指针并遍历它们：

```
                    let pointersAndOffsets = memory.scanPointers()
                    for pointerAndOffset in pointersAndOffsets {
                        let pointer = pointerAndOffset.pointer
                        let offset = pointerAndOffset.offset
```

只为尚未见过的指针创建条目：

```
                        if seen[pointer] == nil {
```

如果之前没见过这个指针，现在将其标记为已见，并为它创建一个新条目：

```
                            seen[pointer] = ()
                            let newEntry = ScanEntry(parent: entry, parentOffset: offset, address: pointer, index: count)
```

将新条目插入 `toScan` 的开头。也可以添加到末尾，这将使其成为深度优先扫描而不是广度优先扫描。我发现广度优先更适合探索：

```
                            toScan.insert(newEntry, atIndex: 0)
                        }
                    }
                }
            }
```

差不多就是这样！剩下的就是返回根 `ScanResult`。我们通过在 `results` 中查找来获取它：

```
            return results[firstAddr]!
        }
    }
```

**使用方法**  
要使用此函数，创建一个 `Printer`，用值和限制调用 `scanmem`，然后在结果上调用 `recursiveDump` 并调用 `Printer` 的 `end`：

```
    let printer = TermPrinter()
    scanmem(42, 30).recursiveDump(printer)
    printer.end()
```

输出：

起始指针：  0 0x00007fff52eb8a08:  8 字节  2a00000000000000

让我们尝试一个更复杂的例子：

```
    let printer = TermPrinter()
    class X {}
    scanmem(X(), 30).recursiveDump(printer)
    printer.end()
```

输出：

起始指针：  0 0x00007fff52184a08:  8 字节  60c5c019a17f0000  
  ( 0, 0x00007fff52184a08@0 ) \<-  1 0x00007fa119c0c560:  16 字节  1063a90d01000000 0400000001000000  
   ( 1, @0 ) \<-  2 0x000000010da96310:  128 字节  d062a90d01000000 a804c90d01000000 10ca968bff7f0000 0000000000000000 e14ec019a17f0000 0300000000000000... ObjC 类 memory.X  
    ( 2, memory.X@0 ) \<-  3 0x000000010da962d0:  48 字节  d004c90d01000000 d004c90d01000000 40d7c019a17f0000 0300000001000000 204fc019a17f0000 0000000000000000 符号 _TMmC6memory1X  
     ( 3, 0x000000010da962d0@0 ) \<-  9 0x000000010dc904d0:  40 字节  d004c90d01000000 a804c90d01000000 10ca968bff7f0000 0000000000000000 f031c019a17f0000 符号 OBJC_METACLASS_$_SwiftObject  
      ( 9, 0x000000010dc904d0@32 ) \<-  16 0x00007fa119c031f0:  64 字节  008018a007000000 28f6c80d01000000 3032c019a17f0000 0000000000000000 1033c019a17f0000 d062a90d01000000...  
       ( 16, 0x00007fa119c031f0@8 ) \<-  25 0x000000010dc8f628:  128 字节  0700000028000000 2800000000000000 0000000000000000 944ac70d01000000 58f2c80d01000000 10f6c80d01000000...  
       ( 16, 0x00007fa119c031f0@16 ) \<-  26 0x00007fa119c03230:  224 字节  1b00000009000000 49a6e587ff7f0000 194bc70d01000000 d094c50d01000000 15a8e587ff7f0000 044bc70d01000000...  
       ( 16, 0x00007fa119c031f0@32 ) \<-  27 0x00007fa119c03310:  16 字节  10f6c80d01000000 0000000000000000  
     ( 3, 0x000000010da962d0@16 ) \<-  10 0x00007fa119c0d740:  64 字节  0000000000000000 0000000000000000 f5a9e587ff7f0000 0095c50d01000000 0000000000000000 0000000000000000...  
      ( 10, 0x00007fa119c0d740@16 ) \<-  17 0x00007fff87e5a9f5:  128 字节  636c617373005f69 6e69745769746855 524c3a746167733a 006164644f626a65 63743a005f617379 6e6368726f6e6f75... -- 字符串：(class, _initWithURL:tags:, addObject:, _asynchronouslyWaitForURLToChangeThenSetTags, removeObject:, removeCachedResourceValueForKey:)  
      ( 10, 0x00007fa119c0d740@24 ) \<-  18 0x000000010dc59500:  16 字节  554889e54889f85d c30f1f8000000000 符号 +[SwiftObject class]  
     ( 3, 0x000000010da962d0@32 ) \<-  11 0x00007fa119c04f20:  64 字节  008018a007000000 0059a90d01000000 0000000000000000 0000000000000000 0000000000000000 0000000000000000...  
      ( 11, 0x00007fa119c04f20@8 ) \<-  19 0x000000010da95900:  128 字节  8100000028000000 2800000000000000 0000000000000000 252fa90d01000000 0000000000000000 0000000000000000...  
       ( 19, 0x000000010da95900@24 ) \<-  28 0x000000010da92f25:  128 字节  5f547443366d656d 6f72793158004336 6d656d6f72793158 0056534337646c5f 696e666f002f7573 722f6c69622f6c69... -- 字符串：(_TtC6memory1X, C6memory1X, VSC7dl_info, /usr/lib/libobjc.A.dylib, objc_readClassPair, NSUndoManagerProxy, _targetClass, _objc_readC)  
      ( 11, 0x00007fa119c04f20@48 ) \<-  20 0x000000010da96180:  40 字节  d004c90d01000000 d004c90d01000000 e00bc119a17f0000 0300000001000000 804ec019a17f0000 符号 _TMmC6memory10ScanResult  
       ( 20, 0x000000010da96180@16 ) \<-  29 0x00007fa119c10be0:  64 字节  0000000000000000 0000000000000000 f5a9e587ff7f0000 0095c50d01000000 0000000000000000 0000000000000000...  
    ( 2, memory.X@8 ) \<-  4 0x000000010dc904a8:  40 字节  d004c90d01000000 0000000000000000 10ca968bff7f0000 0000000000000000 b031c019a17f0000 符号 OBJC_CLASS_$_SwiftObject ObjC 类 SwiftObject  
     ( 4, SwiftObject@32 ) \<-  12 0x00007fa119c031b0:  64 字节  0080988000000000 10f9c80d01000000 2033c019a17f0000 5035c019a17f0000 a035c019a17f0000 1063a90d01000000...  
      ( 12, 0x00007fa119c031b0@8 ) \<-  21 0x000000010dc8f910:  128 字节  0600000000000000 1000000000000000 0000000000000000 944ac70d01000000 70f6c80d01000000 10f6c80d01000000...  
      ( 12, 0x00007fa119c031b0@16 ) \<-  22 0x00007fa119c03320:  560 字节  1b00000017000000 66a6e587ff7f0000 fc4ac70d01000000 4096c50d01000000 6ea6e587ff7f0000 194bc70d01000000...  
      ( 12, 0x00007fa119c031b0@24 ) \<-  23 0x00007fa119c03550:  80 字节  0000000000000000 0400000000000000 d835c70d01000000 dd35c70d01000000 e235c70d01000000 ed35c70d01000000...  
      ( 12, 0x00007fa119c031b0@32 ) \<-  24 0x00007fa119c035a0:  16 字节  10f6c80d01000000 0000000000000000  
    ( 2, memory.X@16 ) \<-  5 0x00007fff8b96ca10:  40 字节  0000000000000000 0000000000000000 0000000000000000 0000000000000000 0000000000005940 符号 _objc_empty_cache  
    ( 2, memory.X@32 ) \<-  6 0x00007fa119c04ee1:  128 字节  8098800000000048 59a90d0100000000 0000000000000000 0000000000000000 0000000000000000 00000000000000f0...  
    ( 2, memory.X@64 ) \<-  7 0x000000010da95360:  64 字节  0000000000000000 332fa90d01000000 000000000a000000 082ca90d01000000 c0a6a80d01000000 0000000000000000... 符号 _TMnC6memory1X  
     ( 7, 0x000000010da95360@8 ) \<-  13 0x000000010da92f33:  128 字节  43366d656d6f7279 3158005653433764 6c5f696e666f002f 7573722f6c69622f 6c69626f626a632e 412e64796c696200... -- 字符串：(C6memory1X, VSC7dl_info, /usr/lib/libobjc.A.dylib, objc_readClassPair, NSUndoManagerProxy, _targetClass, _objc_readClassPair, _objc)  
     ( 7, 0x000000010da95360@24 ) \<-  14 0x000000010da92c08:  128 字节  0000000000000000 4d75737420656e64 207072696e746572 206265666f726520 64657374726f7969 6e67206974002e2f... -- 字符串：(Must end printer before destroying it, ./memory.swift, assertion failed, can't unsafeBitCast betw)  
     ( 7, 0x000000010da95360@32 ) \<-  15 0x000000010da8a6c0:  160 字节  554889e54883ec30 488b05b9bd000048 3d0000000048897d f8488945f0756e31 c089c1b807000000 89c64889cf48894d... 符号 get_field_types_X  
    ( 2, memory.X@72 ) \<-  8 0x000000010da8a040:  16 字节  554889e548897df8 4889f85dc30f1f00 符号 _TFC6memory1XcfMS0_FT_S0_

真漂亮！

**结论**  
这远非正常或理智的 Swift 代码，但它能工作，并且结果确实很有用。它也是一个很好的例子，展示了 Swift 如何让你与各种底层 C 调用交互，而无需比从 C 中调用它们更麻烦。尽管你应该尽可能避免这些把戏，但能够执行 `unsafeBitCast` 并获取数组内部存储的指针这样的操作，在需要时确实非常方便。

今天就到这里。下次再见，带来更多疯狂的好东西。Friday Q&A 由读者的想法驱动，因此在那之前，请继续[发送你的主题建议](mailto:mike@mikeash.com)。

你喜欢这篇文章吗？我正在出售含有多篇文章的全套书籍！第二卷和第三卷现已出版！提供 ePub、PDF、印刷版，以及在 iBooks 和 Kindle 上阅读。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面评论 RSS Feed](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2014-08-29-swift-memory-dumping.html)

添加你的想法，发表评论：

垃圾邮件和偏离主题的帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
