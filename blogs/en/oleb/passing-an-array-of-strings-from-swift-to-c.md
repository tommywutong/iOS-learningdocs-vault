---
title: Passing an Array of Strings from Swift to C
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/10/swift-array-of-c-strings/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:b6e5f45372afd922'
translated: false
---

> 原文：[Passing an Array of Strings from Swift to C](https://oleb.net/blog/2016/10/swift-array-of-c-strings/)　·　Ole Begemann

# Passing an Array of Strings from Swift to C

Swift allows you to pass a native Swift string directly to a C API that takes a C String (i.e. a `char *`). For example, you can call the [`strlen`](https://linux.die.net/man/3/strlen) function from Swift like this:

```
import Darwin // or Glibc on Linux
strlen("Hello 😃") // → 10
```

This works even though Swift imports the `const char *` parameter as an `UnsafePointer<Int8>!`. The full type of the `strlen` function as imported by Swift looks like this:

```
func strlen(_ __s: UnsafePointer<Int8>!) -> UInt
```

The type checker allows you to [pass a `String` value to an `UnsafePointer<Int8>` or `UnsafePointer<UInt8>` parameter](https://developer.apple.com/library/content/documentation/Swift/Conceptual/BuildingCocoaApps/InteractingWithCAPIs.html#//apple_ref/doc/uid/TP40014216-CH8-ID17). When you do that, the compiler will transparently create a buffer containing the UTF-8-encoded[1](#fn:1), null-terminated string, and pass a pointer to that buffer to the function.

# No built-in support for arrays of C strings

The way Swift handles single `char *` arguments is very convenient. However, some C functions take an array of strings (a `char **` or `char *[]`), and there is no built-in support in Swift for passing a `[String]` to a `char **` parameter.

An example where this would be useful is the [`posix_spawn`](https://linux.die.net/man/3/posix_spawn) function to launch a child process. The last two arguments of `posix_spawn`, `argv` and `envp`, are arrays of strings in which you pass the new process’s arguments and environment variables. Specifically, the documentation says this:

> `argv` [and `envp`] is a pointer to a null-terminated array of character pointers to null-terminated character strings.

Swift translates these arguments’ C type of `char *const argv[]` to the unwieldy `UnsafePointer<UnsafeMutablePointer<Int8>?>!`.[2](#fn:iou)

# Converting an array of Swift strings to an array of C strings

Suppose we want to provide a nice Swift interface for `posix_spawn`. [3](#fn:2) Our wrapper function should take the path of the program being launched and an array of strings for the arguments:

```
/// Spawns a child process.
///
/// - Returns: A pair containing the return value
///   of `posix_spawn` and the pid of the spawned
///   process.
func spawn(path: String, arguments: [String]) -> Int32
```

To make this interface work, we need to convert the `arguments` array to the format `posix_spawn` expects. This requires several steps:

- Convert the element strings to UTF-8-encoded, null-terminated C strings.
- Copy all these C strings into a single buffer.
- Add another null byte at the end of the buffer to denote the end of the C array.
- .

## withArrayOfCStrings in the standard library

The Swift team needed the same functionality for running the unit tests of the standard library, and that’s why the standard library’s source includes a function named [`withArrayOfCStrings`](https://github.com/apple/swift/blob/c3b7709a7c4789f1ad7249d357f69509fb8be731/stdlib/private/SwiftPrivate/SwiftPrivate.swift#L68-L90) that does just that. Now this is an internal function that is not exposed publicly to stdlib clients (although it is declared `public`, presumably because otherwise the unit tests wouldn’t see it). But we can still take a look at how it works. This is the function’s interface:

```
public func withArrayOfCStrings<R>(
  _ args: [String],
  _ body: ([UnsafeMutablePointer<CChar>?]) -> R
) -> R
```

It has the same form as [`withUnsafePointer`](https://developer.apple.com/reference/swift/2431879-withunsafepointer) and its variants: it’s generic over a result type `R` and takes a closure. The idea is that, after performing the conversion of the strings array to a C array, `withArrayOfCStrings` calls the closure, passing the C array in, and forwards the closure’s return value to its caller. This gives the `withArrayOfCStrings` function full control over the lifetime of the buffer it creates.

Before we look how the function is implemented, let’s write the `spawn` function that uses `withArrayOfCStrings`:

```
/// Spawns a child process.
///
/// - Returns: A pair containing the return value
///   of `posix_spawn` and the pid of the spawned
///   process.
func spawn(path: String, arguments: [String]) -> (retval: Int32, pid: pid_t) {
    // Add the program's path to the arguments
    let argsIncludingPath = [path] + arguments
    
    return withArrayOfCStrings(argsIncludingPath) {
        argv in
        var pid: pid_t = 0
        let retval = posix_spawn(&pid, path, 
            nil, nil, argv, nil)
        return (retval, pid)
    }
}
```

Why does this work? You’ll notice that `withArrayOfCStrings`’s closure parameter has the type `([UnsafeMutablePointer<CChar>?]) -> R`. The argument type `[UnsafeMutablePointer<CChar>?]` doesn’t seem to be compatible with the `UnsafePointer<UnsafeMutablePointer<Int8>?>!` type that `posix_spawn` requires, but it is. `CChar` is just a typealias for `Int8`. And just like Swift has special handling for passing strings to C, the compiler transparently bridges native Swift arrays to C functions that take an `UnsafePointer<Element>`, so we can pass the array directly to `posix_spawn`, as long as its element type matches the pointer’s pointee type.

This is how `spawn` looks in use:

```
let (retval, pid) = spawn(path: "/bin/ls",
    arguments: ["-l", "-a"])
```

And this is the output when you execute the program:

```
$ swift spawn.swift
posix_spawn result: 0
new process pid: 17477
total 24
drwxr-xr-x   4 elo  staff   136 Oct 27 17:04 .
drwx---r-x@ 41 elo  staff  1394 Oct 24 20:12 ..
-rw-r--r--@  1 elo  staff  6148 Oct 27 17:04 .DS_Store
-rw-r--r--@  1 elo  staff  2342 Oct 27 15:28 spawn.swift
```

(Note that `posix_spawn` returns an error if you call it in a playground, presumably because a playground’s sandbox doesn’t allow spawning child processes. It’s best to try this from the command line or by creating a new command-line project in Xcode.)

## How does it work?

The full [implementation of `withArrayOfCStrings`](https://github.com/apple/swift/blob/c3b7709a7c4789f1ad7249d357f69509fb8be731/stdlib/private/SwiftPrivate/SwiftPrivate.swift#L68-L90) looks like this:

```
public func withArrayOfCStrings<R>(
  _ args: [String],
  _ body: ([UnsafeMutablePointer<CChar>?]) -> R
) -> R {
  let argsCounts = Array(args.map { $0.utf8.count + 1 })
  let argsOffsets = [ 0 ] + scan(argsCounts, 0, +)
  let argsBufferSize = argsOffsets.last!

  var argsBuffer: [UInt8] = []
  argsBuffer.reserveCapacity(argsBufferSize)
  for arg in args {
    argsBuffer.append(contentsOf: arg.utf8)
    argsBuffer.append(0)
  }

  return argsBuffer.withUnsafeMutableBufferPointer {
    (argsBuffer) in
    let ptr = UnsafeMutableRawPointer(argsBuffer.baseAddress!).bindMemory(
      to: CChar.self, capacity: argsBuffer.count)
    var cStrings: [UnsafeMutablePointer<CChar>?] = argsOffsets.map { ptr + $0 }
    cStrings[cStrings.count - 1] = nil
    return body(cStrings)
  }
}
```

Let’s go through it line by line. The first line creates an array of the UTF-8-encoded character counts (plus 1 for the null-termination byte) for the input strings:

```
let argsCounts = Array(args.map { $0.utf8.count + 1 })
```

The next line takes these character counts and computes the character _offset_ for each input string, i.e. at what position in the buffer each string will begin. The first string will of course be positioned at offset 0, and the subsequent offsets are computed by cumulating the character counts:

```
let argsOffsets = [ 0 ] + scan(argsCounts, 0, +)
```

The code uses a helper function named `scan` for this, which is [defined in the same file](https://github.com/apple/swift/blob/c3b7709a7c4789f1ad7249d357f69509fb8be731/stdlib/private/SwiftPrivate/SwiftPrivate.swift#L27-L39). Note that `argsOffsets` contains one more element than `argsCounts`. The last element of `argsOffsets` is the offset _behind_ the last input string, i.e. the required size of the buffer.

The next step is to create an array of bytes (the element type is `UInt8`) that serves as the buffer. The call to `reserveCapacity` is not strictly necessary because the buffer would grow automatically, but if you know the required capacity beforehand, reserving it at the start can avoid repeated reallocations:

```
let argsBufferSize = argsOffsets.last!

var argsBuffer: [UInt8] = []
argsBuffer.reserveCapacity(argsBufferSize)
```

Now the UTF-8-encoded bytes can be written into the buffer, adding a null byte after each input string:

```
for arg in args {
  argsBuffer.append(contentsOf: arg.utf8)
  argsBuffer.append(0)
}
```

At this point, we have an array of bytes (`UInt8`) in the correct format. We still need to construct the array of pointers that point to the elements in the buffer. That’s what the final section of the function does:

```
return argsBuffer.withUnsafeMutableBufferPointer {
  (argsBuffer) in
  let ptr = UnsafeMutableRawPointer(argsBuffer.baseAddress!).bindMemory(
    to: CChar.self, capacity: argsBuffer.count)
  var cStrings: [UnsafeMutablePointer<CChar>?] = argsOffsets.map { ptr + $0 }
  cStrings[cStrings.count - 1] = nil
  return body(cStrings)
}
```

We ask the array for a pointer to its elements buffer using [`withUnsafeMutableBufferPointer`](https://developer.apple.com/reference/swift/array/1538652-withunsafemutablebufferpointer). The first line in the inner closure then converts the element pointer’s type from `UnsafeMutablePointer<UInt8>` to `UnsafeMutablePointer<CChar>` by way of `UnsafeMutableRawPointer`. (Since Swift 3.0, you can’t directly convert between typed pointers anymore, [you have to go through `Unsafe[Mutable]RawPointer` first](https://github.com/apple/swift-evolution/blob/master/proposals/0107-unsaferawpointer.md).) This is not very readable, but the only important thing for us is that after this line, the local `ptr` variable is an `UnsafeMutablePointer<CChar>` that points to the first byte in the buffer.

Now, to construct the array of pointers, we map over the array of character offsets we created in line 2, and increment the base pointer by each offset. The final step is then to set the final element in the resulting array to `nil`. This serves as the final null pointer that denotes the end of the array (remember that we said above that `argsOffset` contains one more element than the input array, so overwriting the last element is correct).

Finally, we can call the closure passed from the caller, passing in the array of pointers to C strings.

# Alternative: `strdup` and `free`

**Update April 26, 2017:** Daniel Duan [tweeted](https://twitter.com/daniel_duan/status/843953105557307392) an [alternative solution](https://gist.github.com/dduan/20534149ca788882475ae0c5925a3eba) that is much shorter (slightly modified):

```
import Foundation // needed for strdup and free

public func withArrayOfCStrings<R>(
    _ args: [String],
    _ body: ([UnsafeMutablePointer<CChar>?]) -> R
) -> R {
    var cStrings = args.map { strdup($0) }
    cStrings.append(nil)
    defer {
        cStrings.forEach { free($0) }
    }
    return body(cStrings)
}
```

This uses the [`strdup`](https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man3/strdup.3.html) function from the C standard library to create a copy of each string, and since it’s a C library function the return values are C strings, of course. The `strdup($0)` call takes advantage of a Swift compiler feature I already mentioned above: you can [pass a Swift string directly to a function that expects a C string](https://developer.apple.com/library/content/documentation/Swift/Conceptual/BuildingCocoaApps/InteractingWithCAPIs.html#//apple_ref/doc/uid/TP40014216-CH8-ID17). Note that the caller is responsible for freeing the pointers returned by `strdup`. We use a `defer` block to call `free` for each C string we created when the function returns.

Compared with the first variant above, this solution is a lot less code and way easier to understand. The downside is that it is less efficient because it makes many small allocations (one per string in the array) vs. one large allocation (all strings are copied into a single buffer) in the standard library version.

1. Notice that `strlen` counts the emoji character above as 4 “characters” because it is passed as UTF-8. [↩︎](#fnref:1)
2. The exclamation point, denoting an [implicitly unwrapped optional](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/TheBasics.html#//apple_ref/doc/uid/TP40014097-CH5-ID330), tells us that this API doesn’t have nullability annotations, i.e. Swift doesn’t know if the function accepts passing `NULL` (in which case the outer `UnsafePointer` would be an optional) or not. We must refer to the documentation to answer this question. In this example, the documentation states explicitly that `argv` must contain at least one element (the file name of the program being spawned). `envp` can be `NULL` to signify that it should inherit the environment of its parent process. [↩︎](#fnref:iou)
3. I’m using `posix_spawn` here as a convenient example. In production code, you should probably use the higher-level [`Process`](https://developer.apple.com/reference/foundation/process) class (née `NSTask`) from Foundation for this purpose. But many other C APIs expect arrays of C strings, so this technique is useful in many situations. [↩︎](#fnref:2)
