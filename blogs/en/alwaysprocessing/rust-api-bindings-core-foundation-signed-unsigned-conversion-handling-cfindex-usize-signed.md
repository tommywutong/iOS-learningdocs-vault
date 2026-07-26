---
title: 'Rust API Bindings: Core Foundation Signed/Unsigned Conversion Handling CFIndex/usize (signed/unsigned) conversion is important in crafting idiomatic Rust API bindings. I looked at how Apple handled th'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/12/27/rust-ffi-signed-conv'
original_language: en
published: 2023-12-27
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:5c37a4c62412dbda'
translated: false
---

> 原文：[Rust API Bindings: Core Foundation Signed/Unsigned Conversion Handling CFIndex/usize (signed/unsigned) conversion is important in crafting idiomatic Rust API bindings. I looked at how Apple handled th](https://alwaysprocessing.blog/2023/12/27/rust-ffi-signed-conv)　·　Always Processing (Brian T. Kelley)

# Rust API Bindings: Core Foundation Signed/Unsigned Conversion

![Small green and blue images swirling around in a vortex. The scene is somehow both chaotic and orderly.](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/e27c94ae-84aa-4171-1a67-9c061159e800/public)

Handling `CFIndex`/`usize` (signed/unsigned) conversion is important in crafting idiomatic Rust API bindings. I looked at how Apple handled this conversion between Core Foundation and Foundation, and between Foundation and Swift to help inform the direction for my Core Foundation crate.

Core Foundation’s canonical index type and size type, `CFIndex`, is signed. Foundation’s canonical index type and size type, `NSUInteger`, is unsigned, and Rust’s canonical type, `usize`, is unsigned too.

Handling `CFIndex`/`usize` (signed/unsigned) conversion is important in crafting idiomatic Rust API bindings. Before implementing an approach for my crate, I looked at how Apple handled this problem for Core Foundation↔Foundation and Foundation↔Swift to understand how they balanced performance (an unchecked bit cast) with correctness (detect and handle a sign change).

## Toll-Free Bridging Approach

Many Core Foundation and Foundation [types are interchangeable](https://alwaysprocessing.blog/2023/02/16/objc-unrealized-classes#toll-free-bridging). `CFIndex` is used throughout Core Foundation, while Foundation’s equivalent interface uses `NSUInteger`. I don’t have access to the Foundation source code, but in peeking at the assembly (examples below), it seems **Foundation effectively uses an unchecked bit cast** when converting between `CFIndex` and `NSUInteger`—the values pass through without detection of a potential sign change. So, integer values with the bit at `1 << sizeof(size_t) * 8 - 1` set to `1` will be negative in the Core Foundation interface but positive in the Foundation interface.

The only acknowledgment of the type mismatch in Apple’s documentation (as far as I’m aware) is this (slightly edited) description of the `location` and `length` fields on [`CFRange`](https://developer.apple.com/documentation/corefoundation/cfrange) and [`NSRange`](https://developer.apple.com/documentation/foundation/nsrange/1459533-location):

> For type compatibility with the rest of the system, `LONG_MAX` is the maximum value you should use for location and length.

An interesting related quirk is the difference between [`kCFNotFound`](https://github.com/apple/swift-corelibs-foundation/blob/swift-5.9-RELEASE/CoreFoundation/Base.subproj/CFBase.h#L497) and [`NSNotFound`](https://github.com/apple/swift-corelibs-foundation/blob/swift-5.9-RELEASE/Darwin/Foundation-swiftoverlay/Foundation.swift#L26). Although many Core Foundation and Foundation types are interchangeable, the semantic "not found" value is interface-dependent. `kCFNotFound` is defined as `-1` while `NSNotFound` is `NSIntegerMax` (i.e., the maximum value of `CFIndex`, `LONG_MAX`). So, the addressable range of failable Foundation methods returning an `NSRange` is effectively limited to `[0, LONG_MAX)`.

Using a signed type in the underlying Core Foundation implementation and `NSNotFound`'s definition as the maximum signed value inhibit Foundation from utilizing the full range of the unsigned type.

### Unchecked Bit Cast Examples

`-[NSString length]` returns an `NSUInteger`, but its implementation is a simple tail call into Core Foundation’s [`_CFStringGetLength2`](https://github.com/apple/swift-corelibs-foundation/blob/swift-5.9-RELEASE/CoreFoundation/String.subproj/CFString.c#L2098-L2102), which returns a `CFIndex`.

```
CoreFoundation`-[__NSCFString length]:
  b       _CFStringGetLength2
```

Every method in Objective-C has two implicit arguments:

1. `self`: The pointer to the object instance
2. `_cmd`: The `SEL` that resolved to the method

The above tail call works because `_CFStringGetLength2` has one argument, the pointer to the object instance, so the Objective-C method and the Core Foundation C function have the same ABI, and no work is required to forward the arguments. (`_CFStringGetLength2` ignores the second argument.)

`-[NSString getCharacters:range:]`, on the other hand, has to do some work before and after its call to Core Foundation’s [`_CFStringCheckAndGetCharacters`](https://github.com/apple/swift-corelibs-foundation/blob/swift-5.9-RELEASE/CoreFoundation/String.subproj/CFString.c#L2165-L2172):

- The Objective-C method has four arguments (`self`, `_cmd`, `buffer`, and `range`), while the Core Foundation function has three (`str`, `range`, `buffer`). Removing `_cmd` requires moving the arguments that follow it. Also, in this case, the last two arguments are swapped between the interfaces and need to be reordered.
- Generally, Core Foundation does not do bounds checking, while Foundation does. Foundation calls a Core Foundation SPI (System Programming Interface) that returns an error code if the range is out of bounds so Foundation can raise an exception.

```
CoreFoundation`-[__NSCFString getCharacters:range:]:
  pacibsp                         ; insert PAC into LR using SP as the modifier and key B
  stp     x20, x19, [sp, #-0x20]! ; SP -= 0x20; SP[0x00] = x20; SP[0x08] = x19
  stp     x29, x30, [sp, #0x10]   ; SP[0x10] = FP; SP[0x18] = LR;
  add     x29, sp, #0x10          ; FP = SP + 0x10 (address of {FP, LR})
  mov     x8, x2                  ; x8 = buffer (temporary)
  mov     x19, x1                 ; x19 = _cmd
  mov     x20, x0                 ; x20 = self
  mov     x1, x3                  ; x1 = range.location (arg 1, part 1/2)
  mov     x2, x4                  ; x2 = range.length   (arg 1, part 2/2)
  mov     x3, x8                  ; x3 = buffer         (arg 2)
  bl      _CFStringCheckAndGetCharacters
  cbnz    w0, raiseException      ; goto raiseException if _CFStringCheckAndGetCharacters did not return 0
  ldp     x29, x30, [sp, #0x10]   ; FP = SP[0x10]; LR = SP[0x18]
  ldp     x20, x19, [sp], #0x20   ; x20 = SP[0x00]; x19 = SP[0x08]; SP += 0x20
  retab                           ; return using PAC with SP as the modifier and key B
raiseException:
  mov     x0, x20                 ; x0 = self
  mov     x1, x19                 ; x1 = _cmd
  bl      -[__NSCFString getCharacters:range:].cold.1
```

Although some code is required to adapt the Foundation interface to Core Foundation, there is no validation of the range’s unsigned to signed conversion.

## Swift’s Approach

For Apple’s frameworks (e.g., AppKit, Foundation, UIKit, etc.), the Swift compiler imports `NSUInteger` as `Int`. To make C and Objective-C interfaces visible to Swift code, the Swift compiler "imports" a [Clang module](https://clang.llvm.org/docs/Modules.html) to build a Swift module, where "import" is a Swift compiler process that constructs a Swift-native representation of the compatible declarations, definitions, and types present in the Clang module.

Normally, `NSUInteger` imports as `UInt`. But, in system modules (i.e., modules found under a directory given by an `-isystem` flag), **Swift silently retypes `NSUInteger` to `Int`** unless the `NSUInteger` declares the type of an enum. This retyping operation occurs during the construction of the Swift module. The compiler does not record any metadata about this change, and the operation is not visible to other parts of the compiler. Therefore, any thunks emitted by the compiler to facilitate crossing the language boundary do not check for a potential sign change.

### Down the Rabbit Hole

I looked at the Swift compiler implementation to see under what conditions the change from unsigned to signed took place and how it was implemented.

1. Swift’s `ClangImporter`'s [`shouldAllowNSUIntegerAsInt`](https://github.com/apple/swift/blob/swift-5.9-RELEASE/lib/ClangImporter/ImportType.cpp#L1736-L1751) member function contains the main logic to determine if the compiler should change the type of `NSUInteger` to `Int`. It returns `true` if:

    - The declaration is from a system module.
    - And the declaration’s name **does not** contain `Unsigned` or `unsigned`, which is a special case to preserve `NSUInteger` for `+[NSNumber numberWithUnsignedInteger:]`, `-[NSNumber initWithUnsignedInteger:]`, and `-[NSNumber unsignedIntegerValue]`.
2. There are [two ways](https://github.com/llvm/llvm-project/blob/llvmorg-17.0.1/clang/lib/Lex/ModuleMap.cpp#L2091-L2092) to identify a Clang module as a system module:

    - Its module map has the [`[system]` attribute](https://github.com/llvm/llvm-project/blob/llvmorg-17.0.1/clang/lib/Lex/ModuleMap.cpp#L3000-L3002).
    - The compiler loaded the module map from a [system directory](https://github.com/llvm/llvm-project/blob/llvmorg-17.0.1/clang/lib/Lex/ModuleMap.cpp#L3081).

          1. In this case, the loading of the module map occurs when resolving [header search](https://github.com/llvm/llvm-project/blob/llvmorg-17.0.1/clang/lib/Lex/HeaderSearch.cpp#L1717) paths.
          2. The module inherits the `IsSystem` flag [from the directory](https://github.com/llvm/llvm-project/blob/llvmorg-17.0.1/clang/lib/Lex/HeaderSearch.cpp#L331) containing its module map.
          3. Any directory that’s [not a user directory](https://github.com/llvm/llvm-project/blob/llvmorg-17.0.1/clang/include/clang/Lex/DirectoryLookup.h#L140-L143) is a system directory.
          4. Clang identifies [non-user directories](https://github.com/llvm/llvm-project/blob/llvmorg-17.0.1/clang/lib/Lex/InitHeaderSearch.cpp#L156-L164) as those belonging to one of its system [directory groups](https://github.com/llvm/llvm-project/blob/llvmorg-17.0.1/clang/include/clang/Lex/HeaderSearchOptions.h#L27-L62).
          5. The [compiler invocation arguments](https://github.com/llvm/llvm-project/blob/llvmorg-17.0.1/clang/lib/Frontend/CompilerInvocation.cpp#L3142-L3172) identify which directories belong to the system directory groups.

## My Crate’s Approach

In considering various signed/unsigned conversion approaches for my Core Foundation Rust API bindings, I evaluated Foundation’s and Swift’s approach (transparent retyping) with Rust’s [behavior considered undefined](https://doc.rust-lang.org/reference/behavior-considered-undefined.html). Although Foundation’s and Swift’s approaches may lead to an unexpected sign change, they are not considered unsafe by Rust’s definition. The only potentially related undefined behavior is "Calling a function with the wrong call ABI," but signed-ness is not generally considered part of the C ABI.

I introduced [two traits](https://github.com/briantkelley/apple-rs/blob/e8259656737238f02df6d13e53619c78fed131b8/lib/corefoundation/src/base/ffi/convert.rs) to facilitate signed/unsigned conversion:

- `ExpectFrom` performs the signed/unsigned conversion and panics if the conversion fails. Implementations are a convenience wrapper for `<T as TryFrom>::try_from(value).expect("")`, which, while trivial, reduces the number of ad hoc `expect`s in bindings code to improve readability. This trait primarily facilitates conversions from idiomatic Rust types into native Core Foundation types. It provides a user-visible signal if `CFIndex` cannot represent an index or size.
- `FromUnchecked` performs the signed/unsigned conversion and assumes the result is correct, emulating the transparent retyping approach of Foundation and Swift. This trait primarily facilitates conversions from native Core Foundation types into idiomatic Rust types where it’s reasonable to assume the value is in bounds.

If a sign change goes undetected, safe Rust code will panic. Unsafe code must ensure all values are in bounds for the given domain so an undetected sign change does not impose any additional burden, assuming a sign change would cause the value to go out of bounds.
