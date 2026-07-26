---
title: 'Friday Q&A 2014-08-29: Swift Memory Dumping'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-08-29-swift-memory-dumping.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e8a0896daa6c4fe6'
translated: false
---

> 原文：[Friday Q&A 2014-08-29: Swift Memory Dumping](https://www.mikeash.com/pyblog/friday-qa-2014-08-29-swift-memory-dumping.html)　·　mikeash.com Friday Q&A

Posted at 2014-08-29 13:24 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [A Brief Pause](https://www.mikeash.com/pyblog/a-brief-pause.html)  
Previous article: [Friday Q&A 2014-08-15: Swift Name Mangling](https://www.mikeash.com/pyblog/friday-qa-2014-08-15-swift-name-mangling.html)

Friday Q&A 2014-08-29: Swift Memory Dumping

by [Mike Ash](https://www.mikeash.com/)

**Code**  
As is traditional, the full code for the memory dumper can be found on GitHub:

[https://github.com/mikeash/memorydumper](https://github.com/mikeash/memorydumper)

You can take a look at it there to more easily follow along, run it yourself, or just ignore it.

Note that this code should _not_ be considered a good example of style, implementation, or much of anything. Swift is still new to all of us and it certainly shows in my code. It is useful to see _how_ certain things can be done, at least.

**Pointers**  
We're going to be doing a lot of work with pointers. Swift supports raw pointers fairly well, but not _quite_ to the extent that's needed here. This code really wants to treat pointers like plain integers that happen to represent an address. To make that easier, the `Pointer` `struct` contains an address as a `UInt`, and some utility methods for working with them:

```
    struct Pointer: Hashable, Printable {
```

It's `Hashable` so it can be used in a `Dictionary`, and `Printable` is convenient for debugging. It contains one variable, the pointer address:

```
        let address: UInt
```

The implementation of `Hashable` just returns the address converted to an `Int`. It doesn't care about preserving values or detecting overflows, and just wants to sling the bits across. The builtin function `unsafeBitCast` does exactly that:

```
        var hashValue: Int {
            return unsafeBitCast(address, Int.self)
        }
```

For `Printable`, `NSString`'s `format:` initializer makes it easy to create a human-readable representation of the address:

```
        var description: String {
            return NSString(format: "0x%0*llx", sizeof(address.dynamicType) * 2, address)
        }
```

The `dladdr` function takes a pointer and returns information about the corresponding symbol. Specifically, it returns the path name of the binary that contains it, the base address of that binary, the name of the symbol, and the starting address of that symbol. This information will come in handy for other functions, but `dladdr` is a bit of a pain to call, so a wrapper will prove handy. It returns an optional value since the call can fail:

```
        func symbolInfo() -> Dl_info? {
```

It starts by creating a `Dl_info` `struct`. In C, we'd just declare it and let it sit uninitialized, but Swift requires an initial value, so this code just creates an empty one:

```
            var info = Dl_info(dli_fname: "", dli_fbase: nil, dli_sname: "", dli_saddr: nil)
```

The pointer parameter is typed as `UnsafePointer`, but the pointer address is a `UInt`. The `unsafeBitCast` function bridges the gap:

```
            let ptr: UnsafePointer<Void> = unsafeBitCast(address, UnsafePointer<Void>.self)
```

With these variables in place, the actual call is straightforward:

```
            let result = dladdr(ptr, &info)
```

`dladdr` returns zero for failure and any other value for success. This determines whether the `Dl_info` `struct` is returned, or `nil`:

```
            return (result == 0 ? nil : info)
        }
```

The symbol name is really useful information to display as part of a memory dump. The `Dl_info` `struct` contains the symbol name, but there are two problems with using it directly. First, it's a C string, so it has to be converted to a nicer form in order to use it. Second, `dladdr` looks up the nearest symbol that comes before the specified address, while we only want the the symbol name for an address if it exactly matches the symbol address, not if it's offset. This `symbolName` function takes care of these:

```
        func symbolName() -> String? {
```

It's possible for `symbolInfo` to fail, so the call needs to be checked:

```
            if let info = symbolInfo() {
```

The returned symbol address is an `UnsafePointer`, but we want to compare it with `address` and only return the symbol name if they're equal. Another `unsafeBitCast` call solves the problem:

```
                let symbolAddress: UInt = unsafeBitCast(info.dli_saddr, UInt.self)
```

If the symbol address equals the pointer address, return the symbol name:

```
                if symbolAddress == address {
                    return String.fromCString(info.dli_sname)
                }
```

If they don't match, or if `dladdr` failed altogether, return `nil`:

```
            }
            return nil
        }
```

Another useful function return the pointer to the next symbol following the current pointer. Symbols don't encode lengths, just locations, but looking up the location of the following symbol gives a reasonable ending point for guessing a length. The memory dumping code will use this information to figure out how much memory to read. We don't want to run off into hyperspace if something goes wrong, so this function also takes a limit for how far to search for the next symbol. It returns an optional `Pointer`, with `nil` indicating that no following symbol was found:

```
        func nextSymbol(limit: Int) -> Pointer? {
```

As before, the call to `symbolInfo` can fail and must be checked:

```
            if let myInfo = symbolInfo() {
```

The search strategy is to iterate byte by byte, calling `symbolInfo` each time. If the returned symbol base address changes, it's a new symbol. If it hits the limit without finding a new symbol, return `nil`. To start, it loops from `1` to the limit:

```
                for i in 1..<limit {
```

Generate a candidate pointer by adding `i` to `self` and get its symbol info:

```
                    let candidate = self + i
                    let candidateInfo = candidate.symbolInfo()
```

If `symbolInfo` fails, the search has failed, return `nil`:

```
                    if candidateInfo == nil {
                        return nil
                    }
```

If the returned address is different from the current symbol, the such has succeeded, return the candidate:

```
                    if myInfo.dli_saddr != candidateInfo!.dli_saddr {
                        return candidate
                    }
```

If the loop terminates or the original `symbolInfo` call fals, return `nil`:

```
                }
            }
            return nil
        }
    }
```

`Hashable` includes `Equatable` which means that `Pointer` needs an implementation of the `==` operator:

```
    func ==(a: Pointer, b: Pointer) -> Bool {
        return a.address == b.address
    }
```

For convenience, `Pointer` also gets implementations of the `+` and `-` operators:

```
    func +(a: Pointer, b: Int) -> Pointer {
        return Pointer(address: a.address + UInt(b))
    }

    func -(a: Pointer, b: Pointer) -> Int {
        return Int(a.address - b.address)
    }
```

**Memory**  
We're also going to be doing a lot of work with memory contents. Fundamentally, a chunk of memory is just an array of bytes, but we want to store a bit of info about what kind of memory it is, and we want some functions that help with reading and scanning memory. The `Memory` `struct` stores an array of bytes as well as two flags that specify whether the memory was allocated with `malloc` and whether it corresponds to a symbol:

```
    struct Memory {
        let buffer: [UInt8]
        let isMalloc: Bool
        let isSymbol: Bool
```

These two flags can't really both be `true` simultaneously, so one could argue that this ought to be a three-case `enum` instead. I thought the two flags were a bit more natural to work with, though.

How do you _get_ a chunk of memory? The fundamental operation is to take a `Pointer` and read the memory it points to into an array:

```
        static func readIntoArray(ptr: Pointer, var _ buffer: [UInt8]) -> Bool {
```

The natural way to implement this in Objective-C would be to cast the pointer to a `void *` and then call `memcpy`. In fact, you can do pretty much the same thing in Swift. The `withUnsafeBufferPointer` method on `Array` lets you get a pointer to the target buffer's storage, and `memcpy` is callable from Swift. The problem with this approach, in either language, is that it will crash if the pointer is bad or if the amount being read is too long.

The solution is to read the memory with the mach virtual memory calls. These calls ask the kernel to read the memory on your behalf, and it has all the information it needs to perform the read safely and fail gracefully. Specifically, the `mach_vm_read_overwrite` call will read memory from a pointer into a buffer, and return an error code if the memory isn't readable. This is the approach we use in [PLCrashReporter](https://www.plcrashreporter.org/) to read data when walking data structures which may have been corrupted in a crash. It works great here.

In order to read into `buffer`, we need to get a pointer to its storage. The `withUnsafeBufferPointer` takes care of that:

```
            let result = buffer.withUnsafeBufferPointer {
                (targetPtr: UnsafeBufferPointer<UInt8>) -> kern_return_t in
```

`withUnsafeBufferPointer` doesn't return the pointer. Instead, it calls a function and passes the pointer as a parameter. It returns whatever value the function returns. We'll return the result code from `mach_vm_read_overwrite`, thus the `kern_return_t` return type.

`mach_vm_read_overwrite` takes the pointer to read as a 64-bit unsigned integer, so we have to convert the address of `ptr`:

```
                let ptr64 = UInt64(ptr.address)
```

We also need the target pointer as a 64-bit unsigned integer. The `unsafeBitCast` function takes care of getting it into an integer, and then that can be converted to a `UInt64`:

```
                let target: UInt = unsafeBitCast(targetPtr.baseAddress, UInt.self)
                let target64 = UInt64(target)
```

The function also returns the amount of data read using an out parameter. This value isn't useful to us (as far as I can tell, it's always the amount requested if the call succeeds) but we still have to pass in a pointer for it to write to, so we need a local variable for it:

```
                var outsize: mach_vm_size_t = 0
```

With all the parameters in place, it's time to make the call:

```
                return mach_vm_read_overwrite(mach_task_self_, ptr64, mach_vm_size_t(buffer.count), target64, &outsize)
            }
```

Outside of the closure, `result` now contains the result code returned by `mach_vm_read_overwrite`. If it returned `KERN_SUCCESS`, `buffer` is now filled with contents of the target memory. We'll boil down the result code to a simple `true`/`false` for the caller:

```
            return result == KERN_SUCCESS
        }
```

Next up, we need a way to take a `Pointer` and turn it into a `Memory` instance by reading the contents of that pointer. `readIntoArray` forms the foundation of this process, but it requires a size, whereas we usually _won't_ know the size of an arbitrary `Pointer`. The `read` function takes a `Pointer` and an optional known size and returns an optional `Memory`:

```
        static func read(ptr: Pointer, knownSize: Int? = nil) -> Memory? {
```

The first step is to try to guess the size of the pointed-to memory. Since we're chasing arbitrary pointers, we can't always figure this out reliably. We'll start by calling `malloc_size`. This requires converting the address of the `Pointer` to an `UnsafePointer` using our good friend `unsafeBitCast`:

```
            let convertedPtr: UnsafePointer<Void> = unsafeBitCast(ptr.address, UnsafePointer<Void>.self)
            var length = Int(malloc_size(convertedPtr))
```

`malloc_size` helpfully returns zero if the memory wasn't allocated with `malloc`. (This is not guaranteed in the documentation, so please don't write production code that relies on this fact.) Thus, we can populate `isMalloc` by checking `length:

```
            let isMalloc = length > 0
```

We'll populate `isSymbol` by checking to see if there's a symbol name for the pointer:

```
            let isSymbol = ptr.symbolName() != nil
```

If it's a symbol, then we'll try to guess the length by looking at the distance from that symbol to the following symbol:

```
            if isSymbol {
                if let nextSymbol = ptr.nextSymbol(4096) {
                    length = nextSymbol - ptr
                }
            }
```

Guessing the length may fail, and there may not be a known size. In that case, we'll just try reading successive eight-byte chunks of memory until either it fails or we hit some reasonable length:

```
            if length == 0 && knownSize == nil {
```

The reads are accumulated in an array that starts out empty:

```
                var result = [UInt8]()
```

I arbitrarily chose a limit of 128 bytes while reading data here:

```
                while (result.count < 128) {
```

To read eight bytes, create an eight-byte array and call `readIntoArray`:

```
                    var eightBytes = [UInt8](count: 8, repeatedValue: 0)
                    let success = readIntoArray(ptr + result.count, eightBytes)
```

On failure, end the loop. Otherwise, append to `result` and keep going:

```
                    if !success {
                        break
                    }
                    result.extend(eightBytes)
                }
```

If nothing could be read at all, return `nil`. Otherwise, create a new `Memory` instance and return that:

```
                return (result.count > 0
                    ? Memory(buffer: result, isMalloc: false, isSymbol: isSymbol)
                    : nil)
```

If the size could be guessed or was already known, life is a bit simpler. Create an array of the appropriate size and read into it:

```
            } else {
                if knownSize != nil {
                    length = knownSize!
                }

                var result = [UInt8](count: length, repeatedValue: 0)
                let success = readIntoArray(ptr, result)
```

If the read succeeded, return a `Memory` instance, otherwise return `nil`:

```
                return (success
                    ? Memory(buffer: result, isMalloc: isMalloc, isSymbol: isSymbol)
                    : nil)
            }
        }
```

The memory dumper works recursively. It reads a pointer into a buffer, extracts pointers from that buffer, then reads those pointers into buffers and continues in that fashion. Extracting pointers from a buffer is a fundamental part of that process. It's difficult to know exactly what parts of a buffer are pointers. For the purposes of the dumper, it will assume that every naturally aligned pointer-sized quantity is a pointer. There's little harm in guessing wrong, since the memory reader tolerates bad pointers. The `scanPointers` function takes no parameters (since it operates on a the internal buffer of a `Memory` instance) and returns an array of `PointerAndOffset` instances. This is a simple `struct` that contains one `Pointer` and one offset as an `Int`. The offset is useful elsewhere when printing the results, since it can show exactly where a pointer was found. Here's the function declaration:

```
        func scanPointers() -> [PointerAndOffset] {
```

Results are accumulated in an array:

```
            var pointers = [PointerAndOffset]()
```

The contents of the `Memory` instance are in `buffer` which is an array of `UInt8`. We need to read pointer-sized chunks of this. One way would be to read several elements at a time and do some bitshifting to construct a pointer. Or, since we're already slinging "unsafe" stuff around with reckless abandon, we could just convert it to a `UInt` pointer and read the data out directly:

```
            buffer.withUnsafeBufferPointer {
                (memPtr: UnsafeBufferPointer<UInt8>) -> Void in

                let ptrptr = UnsafePointer<UInt>(memPtr.baseAddress)
```

`ptrptr` contains a pointer to the buffer, treating it as an array of `UInt`. A loop extracts each `Pointer` that lies within:

```
                let count = self.buffer.count / 8
                for i in 0..<count {
                    pointers.append(PointerAndOffset(pointer: Pointer(address: ptrptr[i]), offset: i * 8))
                }
            }
```

With the array filled out, all that remains is to return it to the caller:

```
            return pointers
        }
```

A lot of memory chunks contain strings, and it's useful to scan for strings and print them out in a human-readable fashion. It's impossible to know for sure whether a chunk of memory actually contains a string or just contains binary data that happens to look like a string, but with some heuristics it's possible to do a decent job. I chose to treat any sequence of at least four consecutive bytes in the range of 32-126 inclusive as a string. This range is the range of ASCII characters excluding unprintable control characters. Similar to `scanPointers`, the `scanStrings` function takes no parameters and returns an array of `String`:

```
        func scanStrings() -> [String] {
```

First, make constants for the upper and lower bound:

```
            let lowerBound: UInt8 = 32
            let upperBound: UInt8 = 126
```

The current candidate sequence is stored in a local array, as are the strings accumulated so far:

```
            var current = [UInt8]()
            var strings = [String]()
```

Now, loop through the buffer. The program tacks a zero byte on the end of the buffer when looping through it to ensure that every candidate sequence ends with a byte that's outside the bounds. This avoids the need for a final check of `current` after the loop ends:

```
            for byte in buffer + [0] {
```

If the byte is within the bounds, tack it on to `current`:

```
                if byte >= lowerBound && byte <= upperBound {
                    current.append(byte)
```

Otherwise, if `current` contains at least four bytes, turn it into a `String` and add it to `strings`:

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

There's probably a better way to create a `String` from an array of `UInt8`, but this works well enough. Finally, clear `current` for the next round:

```
                    current.removeAll()
                }
            }
```

Once all is done, return the strings:

```
            return strings
        }
```

It's also nice to show a raw hexadecimal representation of the memory contents. The `hex` function handles this:

```
        func hex() -> String {
```

We want spaces every eight bytes:

```
            let spacesInterval = 8
```

The output is accumulated in an `NSMutableString`. The ability to use format strings when appending makes it easier to deal with hexademical:

```
            let str = NSMutableString(capacity: buffer.count * 2)
```

Iterate over the buffer. Use `enumerate` to get both the index and the byte value:

```
            for (index, byte) in enumerate(buffer) {
```

Every `spacesInterval` bytes, add a space:

```
                if index > 0 && (index % spacesInterval) == 0 {
                    str.appendString(" ")
                }
```

Add the current byte as hexadecimal:

```
                str.appendFormat("%02x", byte)
            }
```

When it's all done, return the accumulated string:

```
            return str
        }
    }
```

For completeness, here's the `PointerAndOffset` `struct` used above:

```
    struct PointerAndOffset {
        let pointer: Pointer
        let offset: Int
    }
```

**Printing**  
A lot of the rest of the code involves printing results. A memory dumper isn't very useful unless it shows you what it finds. To make it easier to print results in a useful way, I built a `Printer` protocol that the other code uses, along with a set of utility functions. The `Printer` protocol can be implemented to dump output in different forms. Here, I'll show the terminal printer implementation. I also created an implementation that outputs HTML, which you can see on GitHub.

Color is a useful way to show relationships between different printed items. An `enum` defines available colors for printing:

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

The `Printer` protocol defines the capabilities needed for a printer object. It's not extensive: it allows for printing a string with a color, printing a string with the default color, printing a newline, and terminating output (necessary for closing tags when writing HTML):

```
    protocol Printer {
        func print(color: PrintColor, _ str: String)
        func print(str: String)
        func println()
        func end()
    }
```

The `TermPrinter` class implements `Printer`:

```
    class TermPrinter: Printer {
```

When printing to the terminal, you can produce colors with an escape sequence that contains a color code. This dictionary maps the `PrintColor` `enum` values to the appropriate color codes:

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

The full escape sequence for a color consists of the escape character (ASCII code 27), a `[` character, the numeric color code, and then a `m` character. A `printEscape` utility function captures the process of outputting a `PrintColor` to the terminal as the appropriate escape sequence:

```
        func printEscape(color: PrintColor) {
            Swift.print("\u{1B}[\(colorCodes[color]!)m")
        }
```

Note that since `print` is defined as a local method, `Swift.print` is used to access the built-in function.

The base `print` method uses `printEscape` to print the escape code for the given color, prints the string, then for safety goes back to the default color:

```
        func print(color: PrintColor, _ str: String) {
            printEscape(color)
            Swift.print(str)
            printEscape(.Default)
        }
```

The single-argument version of the method just calls the two-argument version with `.Default`:

```
        func print(str: String) {
            print(.Default, str)
        }
```

`println` just calls through to the built-in function:

```
        func println() {
            Swift.println()
        }
```

Finally, the `end()` method is empty, since there's nothing that needs to be done to wrap up printing to the terminal:

```
        func end() {}
    }
```

A couple of convenience functions help with making nicely-formatted output. This `pad` function pads a string to align it to the left or right if it's shorter than requested. It's not all that interesting, so I won't go into details:

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

Similarly, a `limit` function truncates strings longer than a maximum length:

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

**Objective-C Classes**  
Objective-C classes are commonly found when poking around in memory, so it's useful to have some special handling for them. This `struct` encapsulates a class:

```
    struct ObjCClass {
```

It contains a map from `Pointer` values to `ObjCClass` instances:

```
        static let classMap: Dictionary<Pointer, ObjCClass> = {
            var tmpMap = Dictionary<Pointer, ObjCClass>()
            for c in AllClasses() { tmpMap[c.address] = c }
            return tmpMap
        }()
```

I'll show the implementation of `AllClasses` in a bit. The dictionary gets wrapped in a fuction to make things marginally nicer:

```
        static func atAddress(address: Pointer) -> ObjCClass? {
            return classMap[address]
        }
```

A static helper function assists in dumping the class of an object, as well as all superclasses:

```
        static func dumpObjectClasses(p: Printer, _ obj: AnyObject) {
            var classPtr: AnyClass! = object_getClass(obj)
            while classPtr != nil {
                ObjCClass(address: Pointer(address: unsafeBitCast(classPtr, UInt.self)), name: String.fromCString(class_getName(classPtr))!).dump(p)
                classPtr = class_getSuperclass(classPtr)
            }
        }
```

The `struct` just wraps a `Pointer` since all other data can be retrieved from the Objective-C runtime using that pointer:

```
        let address: Pointer
```

A computed property makes it convenient to retrieve `address` as an `AnyClass`, which is the type that the Objective-C runtime functions want to see. Our good friend `unsafeBitCast` makes yet another appearance:

```
        var classPtr: AnyClass {
            return unsafeBitCast(address.address, AnyClass.self)
        }
```

There are a few bits of code that want to retrieve a class's name, and a computed property makes that easy:

```
        var name: String {
            return String.fromCString(class_getName(classPtr))!
        }
```

Finally, we want classes to be able to dump themselves to a `Printer`:

```
        func dump(p: Printer) {
```

When working with Objective-C runtime functions, there's a really common pattern where the function returns a pointer to an array that's terminated by `NULL`, and you're required to `free` the array when you're done using it. In Swift, the pointers are represented as `UnsafeMutablePointer<COpaquePointer>`, so one convenient function can wrap up the annoying work:

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

It starts by printing the class name, and for `NSObject` that's all it bothers with:

```
            p.print("Objective-C class \(name)")

            if class_getName(classPtr) == "NSObject" {
                println()
            } else {
```

Otherwise, it dumps out the instance variables, properties, and methods, using `iterate` and trailing closure syntax to make the job easy:

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

The `AllClasses` function calls `objc_copyClassList` and iterates over the result:

```
    func AllClasses() -> [ObjCClass] {
        var count: CUnsignedInt = 0
        let classList = objc_copyClassList(&count)

        var result = [ObjCClass]()

        for i in 0..<count {
```

The class pointer at that index is extracted, then `unsafeBitCast` makes another appearance so the thing can be converted to a `Pointer`:

```
            let rawClass: AnyClass! = classList[Int(i)]
            let address: Pointer = Pointer(address: unsafeBitCast(rawClass, UInt.self))
```

An `ObjCClass` is created from the `Pointer` and added to the `result` array:

```
            result.append(ObjCClass(address: address))
        }
```

The `result` array is then returned to the caller:

```
        return result
    }
```

**Scanning Data Structures**  
We're ready to start looking at the actual scanning machinery now. Each memory address to be scanned is wrapped up in a `ScanEntry` instance. This holds a parent entry that indicates where the pointer was found, an offset within the parent, the scanned address, and an index. The index is used to assign each entry a number to make it easier to cross-reference them in the output. This is a `class` rather than a `struct` because multiple data structures need to refer to the same instance, and potentially mutate it or see mutations. Here's the definition:

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

Actually performing a scan on a `ScanEntry` produces a `ScanResult`. A `ScanResult` points to an entry and a parent. It also contains a `Memory` that represents its contents, an array of child results, an indentation level, and a print color:

```
    class ScanResult {
        let entry: ScanEntry
        let parent: ScanResult?
        let memory: Memory
        var children = [ScanResult]()
        var indent = 0
        var color: PrintColor = .Default
```

`init` sets up the `let` variables:

```
        init(entry: ScanEntry, parent: ScanResult?, memory: Memory) {
            self.entry = entry
            self.parent = parent
            self.memory = memory
        }
```

It's handy to get a name for a `ScanResult`, but it's not quite as easy as just looking it up:

```
        var name: String {
```

If this entry happens to refer to an Objective-C class, then we can ask that class for its name:

```
            if let c = ObjCClass.atAddress(entry.address) {
                return c.name
            }
```

If the entry refers to an Objective-C _object_ then the first pointer-sized chunk of the memory will be an `isa` that refers to the object's class. At least on architectures and OSes that don't use a [non-pointer isa](http://www.sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html). `Memory`'s `scanPointers` method makes it easy albeit inefficient to grab the first pointer. If the first pointer exists (i.e. the memory is at least long enough to contain one) and it points to an Objective-C class, we fake up a `-description` style name and return that:

```
            let pointers = memory.scanPointers()
            if pointers.count > 0 {
                if let c = ObjCClass.atAddress(pointers[0].pointer) {
                    return "<\(c.name): \(entry.address.description)>"
                }
            }
```

If all else fails, return the `description` of the underlying `Pointer`:

```
            return entry.address.description
        }
```

An entry knows how to `dump` itself to a `Printer`:

```
        func dump(p: Printer) {
```

If the entry has a parent, it prints the parent's address and this entry's offset within it, all in the parent's color to make it easier to visually cross-reference. Otherwise, it prints the fact that this is the root pointer:

```
            if let parent = entry.parent {
                p.print("(")
                p.print(self.parent!.color, "\(pad(parent.index, 3)), \(pad(self.parent!.name, 24))@\(pad(entry.parentOffset, 3, align: .Left))")
                p.print(") <- ")
            } else {
                p.print("Starting pointer: ")
            }
```

Next, print the entry's index, description, and size:

```
            p.print(color, "\(pad(entry.index, 3)) \(entry.address.description): ")

            p.print(color, "\(pad(memory.buffer.count, 5)) bytes ")
```

Next, print the type of memory, whether it came from `malloc`, is a symbol, or is just unknown:

```
            if memory.isMalloc {
                p.print(color, "<malloc> ")
            } else if memory.isSymbol {
                p.print(color, "<symbol> ")
            } else {
                p.print(color, "<unknwn> ")
            }
```

After this, the memory contents are dumped, limited so that large chunks don't occupy tons of room:

```
            p.print(color, limit(memory.hex(), 101))
```

If there's a symbol name, print that too:

```
            if let symbolName = entry.address.symbolName() {
                p.print(" Symbol \(symbolName)")
            }
```

If it's an Objective-C class, print that:

```
            if let objCClass = ObjCClass.atAddress(entry.address) {
                p.print(" ObjC class \(objCClass.name)")
            }
```

If the memory contains any human-readable strings, print them out as well:

```
            let strings = memory.scanStrings()
            if strings.count > 0 {
                p.print(" -- strings: (")
                p.print(", ".join(strings))
                p.print(")")
            }
```

Then print a newline and we're done:

```
            p.println()
        }
```

Dumping a single `ScanResult` isn't so interesting. What's interesting is dumping the whole hierarchy:

```
        func recursiveDump(p: Printer) {
```

Entries with children will be assigned a color. To ensure variety, the color is chosen by iterating through an array of colors as each entry is scanned. A helper function wraps it all up:

```
            var entryColorIndex = 0
            let entryColors: [PrintColor] = [ .Red, .Green, .Yellow, .Blue, .Magenta, .Cyan ]
            func nextColor() -> PrintColor {
                return entryColors[entryColorIndex++ % entryColors.count]
            }
```

To dump the entire tree, we track an array of pending entries. We remove an entry from the array and examine it. If it has children, we add those children to the array. We keep doing this until we run out of array:

```
            var chain = [self]
            while chain.count > 0 {
```

The result to scan is popped off the end of the array:

```
                let result = chain.removeLast()
```

Results with children get assigned a color:

```
                if result.children.count > 0 {
                    result.color = nextColor()
                }
```

The result is indented and then dumped:

```
                for i in 0..<result.indent {
                    p.print("  ")
                }
                result.dump(p)
```

Children are then added to the array. Their indentation is also set at this time:

```
                for child in result.children.reverse() {
                    child.indent = result.indent + 1
                    chain.append(child)
                }
            }
        }
    }
```

The `reverse()` swaps the order in which children are printed, causing the first child to be printed first. The fact that entries are added to and removed from the end also changes how things are printed, making it a depth-first print rather than a breadth-first print. These can be changed around to change how the dump output is organized.

**Scanning**  
We've finally reached the last piece of the puzzle. The `scanmem` function takes an arbitrary value and returns a `ScanResult` representing that value. It also takes a limit of how many entries to scan before returning. It can produce a _lot_ of output otherwise as it ends up scanning the whole Objective-C class tree and everything it points to. Limiting it keeps it from jumping off into the weeds and helps to ensure that the output is relevant to what we want to view.

The function is written using generics to ensure it works on the exact type of value that's passed in by the caller and to avoid any boxing or wrapping as might happen with `Any`:

```
    func scanmem<T>(var x: T, limit: Int) -> ScanResult {
```

The number of entries seen so far is kept in `count`:

```
        var count = 0
```

To avoid infinite loops, entries that have already been seen are tracked. A `Dictionary` mapping to `Void` makes for a handy set type:

```
        var seen = Dictionary<Pointer, Void>()
```

Entries pending to be scanned are held in an array:

```
        var toScan = Array<ScanEntry>()
```

Results are held in a `Dictionary` keyed on their `Pointer` so that children can be easily matched with their parents:

```
        var results = Dictionary<Pointer, ScanResult>()
```

In order to dump `x`, we need a pointer to it. The `withUnsafePointer` function takes a value and provides a pointer to it. We'll take that pointer and then do all the dirty work inside, finally returning the root `ScanResult`:

```
        return withUnsafePointer(&x) {
            (ptr: UnsafePointer<T>) -> ScanResult in
```

Our friend `unsafeBitCast` handles the conversion of `ptr` to a `UInt` that can be used to create a `Pointer`:

```
            let firstAddr: Pointer = Pointer(address: unsafeBitCast(ptr, UInt.self))
```

The `ScanEntry` for this first address has no parent, no offset, and an index of zero:

```
            let firstEntry = ScanEntry(parent: nil, parentOffset: 0, address: firstAddr, index: 0)
```

Mark `firstAddr` as seen, and add `firstEntry` to the `toScan` array:

```
            seen[firstAddr] = ()
            toScan.append(firstEntry)
```

The scan loop consists of repeatedly pulling en entry, scanning it, and adding child entries to the `toScan` array until either the scan limit is reached or it runs out of stuff to scan:

```
            while toScan.count > 0 && count < limit {
```

Pull the entry to scan off the end of the array:

```
                let entry = toScan.removeLast()
```

Set the index of the entry from `count`:

```
                entry.index = count
```

Read the underlying memory at the `ScanEntry`'s address. In the special case where `count` is zero and we _know_ that we're reading `x`, we can pass a known size in to the function by using `sizeof` to get the size of `T`. Otherwise, we'll pass `nil` and let `Memory.read` try to figure out the size on its own:

```
                let memory: Memory! = Memory.read(entry.address, knownSize: count == 0 ? sizeof(T.self) : nil)
```

The read may fail. If it does, then `entry` probably isn't for a real pointer, and we'll just skip it. Otherwise, proceed:

```
                if memory != nil {
```

If it's a real entry, then we can increment `count`:

```
                    count++
```

Look up the parent `ScanResult` by looking in `results` for the parent's address, if it exists:

```
                    let parent = entry.parent.map{ results[$0.address] }?
```

Create a `ScanResult` for the current entry:

```
                    let result = ScanResult(entry: entry, parent: parent, memory: memory)
```

If there's a parent `ScanResult`, add this one to its children:

```
                    parent?.children.append(result)
```

Also add it to `results`:

```
                    results[entry.address] = result
```

That handles the `ScanResult` for this entry. Now it's time to create new entries for any pointers it contains. First, scan the memory for pointers and iterate over them:

```
                    let pointersAndOffsets = memory.scanPointers()
                    for pointerAndOffset in pointersAndOffsets {
                        let pointer = pointerAndOffset.pointer
                        let offset = pointerAndOffset.offset
```

Only create entries for pointers that haven't already been seen:

```
                        if seen[pointer] == nil {
```

If the pointer hasn't been seen before, mark it as seen now, and make a new entry for it:

```
                            seen[pointer] = ()
                            let newEntry = ScanEntry(parent: entry, parentOffset: offset, address: pointer, index: count)
```

Insert the new entry at the beginning of `toScan`. This could also be added at the end, which would make this a depth-first scan rather than a breadth-first scan. I found breadth-first to be more useful for exploration:

```
                            toScan.insert(newEntry, atIndex: 0)
                        }
                    }
                }
            }
```

And that's about it! All that remains is to return the root `ScanResult`. We grab that by looking it up in `results`:

```
            return results[firstAddr]!
        }
    }
```

**Usage**  
To use this function, create a `Printer`, call `scanmem` with a value and a limit, then call `recursiveDump` on the result and `end` the `Printer`:

```
    let printer = TermPrinter()
    scanmem(42, 30).recursiveDump(printer)
    printer.end()
```

This produces:

Starting pointer:  0 0x00007fff52eb8a08:  8 bytes  2a00000000000000

Let's try a more complicated example:

```
    let printer = TermPrinter()
    class X {}
    scanmem(X(), 30).recursiveDump(printer)
    printer.end()
```

This produces:

Starting pointer:  0 0x00007fff52184a08:  8 bytes  60c5c019a17f0000  
  ( 0, 0x00007fff52184a08@0 ) \<-  1 0x00007fa119c0c560:  16 bytes  1063a90d01000000 0400000001000000  
   ( 1, @0 ) \<-  2 0x000000010da96310:  128 bytes  d062a90d01000000 a804c90d01000000 10ca968bff7f0000 0000000000000000 e14ec019a17f0000 0300000000000000... ObjC class memory.X  
    ( 2, memory.X@0 ) \<-  3 0x000000010da962d0:  48 bytes  d004c90d01000000 d004c90d01000000 40d7c019a17f0000 0300000001000000 204fc019a17f0000 0000000000000000 Symbol _TMmC6memory1X  
     ( 3, 0x000000010da962d0@0 ) \<-  9 0x000000010dc904d0:  40 bytes  d004c90d01000000 a804c90d01000000 10ca968bff7f0000 0000000000000000 f031c019a17f0000 Symbol OBJC_METACLASS_$_SwiftObject  
      ( 9, 0x000000010dc904d0@32 ) \<-  16 0x00007fa119c031f0:  64 bytes  008018a007000000 28f6c80d01000000 3032c019a17f0000 0000000000000000 1033c019a17f0000 d062a90d01000000...  
       ( 16, 0x00007fa119c031f0@8 ) \<-  25 0x000000010dc8f628:  128 bytes  0700000028000000 2800000000000000 0000000000000000 944ac70d01000000 58f2c80d01000000 10f6c80d01000000...  
       ( 16, 0x00007fa119c031f0@16 ) \<-  26 0x00007fa119c03230:  224 bytes  1b00000009000000 49a6e587ff7f0000 194bc70d01000000 d094c50d01000000 15a8e587ff7f0000 044bc70d01000000...  
       ( 16, 0x00007fa119c031f0@32 ) \<-  27 0x00007fa119c03310:  16 bytes  10f6c80d01000000 0000000000000000  
     ( 3, 0x000000010da962d0@16 ) \<-  10 0x00007fa119c0d740:  64 bytes  0000000000000000 0000000000000000 f5a9e587ff7f0000 0095c50d01000000 0000000000000000 0000000000000000...  
      ( 10, 0x00007fa119c0d740@16 ) \<-  17 0x00007fff87e5a9f5:  128 bytes  636c617373005f69 6e69745769746855 524c3a746167733a 006164644f626a65 63743a005f617379 6e6368726f6e6f75... -- strings: (class, _initWithURL:tags:, addObject:, _asynchronouslyWaitForURLToChangeThenSetTags, removeObject:, removeCachedResourceValueForKey:)  
      ( 10, 0x00007fa119c0d740@24 ) \<-  18 0x000000010dc59500:  16 bytes  554889e54889f85d c30f1f8000000000 Symbol +[SwiftObject class]  
     ( 3, 0x000000010da962d0@32 ) \<-  11 0x00007fa119c04f20:  64 bytes  008018a007000000 0059a90d01000000 0000000000000000 0000000000000000 0000000000000000 0000000000000000...  
      ( 11, 0x00007fa119c04f20@8 ) \<-  19 0x000000010da95900:  128 bytes  8100000028000000 2800000000000000 0000000000000000 252fa90d01000000 0000000000000000 0000000000000000...  
       ( 19, 0x000000010da95900@24 ) \<-  28 0x000000010da92f25:  128 bytes  5f547443366d656d 6f72793158004336 6d656d6f72793158 0056534337646c5f 696e666f002f7573 722f6c69622f6c69... -- strings: (_TtC6memory1X, C6memory1X, VSC7dl_info, /usr/lib/libobjc.A.dylib, objc_readClassPair, NSUndoManagerProxy, _targetClass, _objc_readC)  
      ( 11, 0x00007fa119c04f20@48 ) \<-  20 0x000000010da96180:  40 bytes  d004c90d01000000 d004c90d01000000 e00bc119a17f0000 0300000001000000 804ec019a17f0000 Symbol _TMmC6memory10ScanResult  
       ( 20, 0x000000010da96180@16 ) \<-  29 0x00007fa119c10be0:  64 bytes  0000000000000000 0000000000000000 f5a9e587ff7f0000 0095c50d01000000 0000000000000000 0000000000000000...  
    ( 2, memory.X@8 ) \<-  4 0x000000010dc904a8:  40 bytes  d004c90d01000000 0000000000000000 10ca968bff7f0000 0000000000000000 b031c019a17f0000 Symbol OBJC_CLASS_$_SwiftObject ObjC class SwiftObject  
     ( 4, SwiftObject@32 ) \<-  12 0x00007fa119c031b0:  64 bytes  0080988000000000 10f9c80d01000000 2033c019a17f0000 5035c019a17f0000 a035c019a17f0000 1063a90d01000000...  
      ( 12, 0x00007fa119c031b0@8 ) \<-  21 0x000000010dc8f910:  128 bytes  0600000000000000 1000000000000000 0000000000000000 944ac70d01000000 70f6c80d01000000 10f6c80d01000000...  
      ( 12, 0x00007fa119c031b0@16 ) \<-  22 0x00007fa119c03320:  560 bytes  1b00000017000000 66a6e587ff7f0000 fc4ac70d01000000 4096c50d01000000 6ea6e587ff7f0000 194bc70d01000000...  
      ( 12, 0x00007fa119c031b0@24 ) \<-  23 0x00007fa119c03550:  80 bytes  0000000000000000 0400000000000000 d835c70d01000000 dd35c70d01000000 e235c70d01000000 ed35c70d01000000...  
      ( 12, 0x00007fa119c031b0@32 ) \<-  24 0x00007fa119c035a0:  16 bytes  10f6c80d01000000 0000000000000000  
    ( 2, memory.X@16 ) \<-  5 0x00007fff8b96ca10:  40 bytes  0000000000000000 0000000000000000 0000000000000000 0000000000000000 0000000000005940 Symbol _objc_empty_cache  
    ( 2, memory.X@32 ) \<-  6 0x00007fa119c04ee1:  128 bytes  8098800000000048 59a90d0100000000 0000000000000000 0000000000000000 0000000000000000 00000000000000f0...  
    ( 2, memory.X@64 ) \<-  7 0x000000010da95360:  64 bytes  0000000000000000 332fa90d01000000 000000000a000000 082ca90d01000000 c0a6a80d01000000 0000000000000000... Symbol _TMnC6memory1X  
     ( 7, 0x000000010da95360@8 ) \<-  13 0x000000010da92f33:  128 bytes  43366d656d6f7279 3158005653433764 6c5f696e666f002f 7573722f6c69622f 6c69626f626a632e 412e64796c696200... -- strings: (C6memory1X, VSC7dl_info, /usr/lib/libobjc.A.dylib, objc_readClassPair, NSUndoManagerProxy, _targetClass, _objc_readClassPair, _objc)  
     ( 7, 0x000000010da95360@24 ) \<-  14 0x000000010da92c08:  128 bytes  0000000000000000 4d75737420656e64 207072696e746572 206265666f726520 64657374726f7969 6e67206974002e2f... -- strings: (Must end printer before destroying it, ./memory.swift, assertion failed, can't unsafeBitCast betw)  
     ( 7, 0x000000010da95360@32 ) \<-  15 0x000000010da8a6c0:  160 bytes  554889e54883ec30 488b05b9bd000048 3d0000000048897d f8488945f0756e31 c089c1b807000000 89c64889cf48894d... Symbol get_field_types_X  
    ( 2, memory.X@72 ) \<-  8 0x000000010da8a040:  16 bytes  554889e548897df8 4889f85dc30f1f00 Symbol _TFC6memory1XcfMS0_FT_S0_

Beautiful!

**Conclusion**  
This is far from normal or sane Swift code, but it works and the results are really useful. It's also a great example of how Swift lets you interact with all sorts of low-level C calls without much more of a fuss than it takes to call them from C. Although you should probably avoid these shenanigans when you can, the fact that you can do stuff like `unsafeBitCast` and get pointers to the internal storage of arrays is really handy when you need it.

That's it for today. Come back next time for more wacky goodness. Friday Q&A is driven by reader ideas, so until then, keep [sending in your topic suggestions](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
