---
title: 'Use it or lose it: why safe C is sometimes unsafe Swift | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/2016/02/16/use_it_or_lose_it_why_safe_c_is_sometimes_unsafe_swift.html'
original_language: en
published: 2016-02-16
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:757e9edd00170137'
translated: false
---

> 原文：[Use it or lose it: why safe C is sometimes unsafe Swift | Cocoa with Love](https://www.cocoawithlove.com/blog/2016/02/16/use_it_or_lose_it_why_safe_c_is_sometimes_unsafe_swift.html)　·　Cocoa with Love (Matt Gallagher)

Swift is a memory safe language so that means no memory safety bugs, right? Not quite. Swift often needs to interact with C and C remains memory unsafe. To further complicate matters, C and Swift have different models of how memory works, leading to some subtle situations that would have been totally safe in C becoming unsafe in Swift.

In this article, I’ll look at a class of memory safety bug that occurred multiple times while I was writing [the previous article](https://www.cocoawithlove.com/blog/2016/02/02/partial-functions-part-two-catching-precondition-failures.html). This particular bug occurs only in Release builds and can occur even when your code has no occurrence of the word “unsafe” anywhere in it.

## An example

The following example shows an Objective-C test that creates a C string from an Objective-C string, copies the C string using `strcpy` and converts back to Objective-C, testing that the result is the same as the original.

```objc
- (void)testProblem
{
   NSString *source = @"Hi, all!";
   const char *cs = [source cStringUsingEncoding:NSUTF8StringEncoding];

   char string1[10] = {0};
   char string2[10] = {cs[0], cs[1], cs[2], cs[3], cs[4], cs[5], cs[6], cs[7], 0, 0};

   strcpy(&string1[0], &string2[0]);
   
   NSString *destination = [NSString stringWithUTF8String:string1];
   XCTAssert([destination isEqualToString:source]);
}
```

There are some minor quirks in how I’ve written this but it is totally valid C/Objective-C and the `XCTAssert` check succeeds. Let’s recreate it as accurately as possible in Swift:

```swift
func testProblem() {
   typealias TenCChars = (CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar)
   
   let source = "Hi, all!"
   let cs = source.cString(using: String.Encoding.utf8)!

   var string1 = TenCChars(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
   var string2 = TenCChars(cs[0], cs[1], cs[2], cs[3], cs[4], cs[5], cs[6], cs[7], 0, 0)

   // Hint: the problem occurs on this line
   strcpy(&string1.0, &string2.0)
   
   // And also on this line
   let destination = String(validatingUTF8: &string1.0)!
   XCTAssert(destination == source)
}
```

Swift is doing exactly what the Objective-C code does. The code compiles and works correctly in Debug.

In Release, there is a memory safety problem and the `XCTAssert` fails. This memory safety problem occurs despite the fact that the word “unsafe” does not appear anywhere in the code. The problem is particularly subtle: change the order of `string1` and `string2` and you’ll still have memory unsafety but the test will pass.

Can you see the problem?

## C’s memory layout

The source of the problem is a difference in memory layout between C and Swift.

In C’s memory layout:

1. every variable has an address
2. every field in a structure can be reached by offsetting a pointer from another field in the structure

Despite being part of C’s memory layout, these points are not necessarily true – particularly after optimization. Variables in registers don’t have addresses. Variables, fields and whole structures may be omitted if they are unused.

But the optimizer in C is required to maintain the illusion of the memory layout. Maintaining this illusion requires something very specific:

> If you take the address of any field of a struct then the compiler must ensure the entire struct – and any parent struct that contains it – is allocated in an addressable location and fields may not be reordered or omitted.

So when we write:

```objc
strcpy(&string1[0], &string2[0]);
```

in C, we are forcing the compiler to ensure that the entire `string1` and `string2` arrays are addressable and complete. They cannot be registers, they cannot be truncated, they cannot be eliminated.

Maintaining the C memory layout has a cost – the optimizer becomes limited in what it can do. Potentially unnecessary stack allocations have a performance overhead relative to register allocations or elimination.

## Swift’s memory layout

In Swift’s memory layout:

1. variables don’t necessarily have addresses except inside a scope that creates an address
2. a pointer to one field of a tuple or struct offers zero knowledge about siblings or parents

You can create an `UnsafeMutablePointer` to a variable in Swift but Swift may need to copy that variable to the stack specifically for the `UnsafeMutablePointer` creation and may immediately remove it from the stack afterwards.

Specifically for this article:

> you cannot create a pointer to a field within a tuple or struct and then use that pointer to access sibling or parent fields in the same tuple or struct.

That is the simple answer to what’s gone wrong in the Swift version: we tried to use a pointer to the first element of a tuple to read and write to the whole tuple. Creating a pointer to the first element of a larger structure and using that as a proxy for the whole structure is common in C and C++ but it’s simply not allowed in Swift.

## A destructuring optimization pass

The optimization pass that causes the problem in this article occurs in the [SILSROA optimization pass](https://github.com/apple/swift/blob/master/lib/SILOptimizer/Transforms/SILSROA.cpp) in the Swift compiler. It is applied during the `runSILOptimizationPasses` function in [Passes.cpp](https://github.com/apple/swift/blob/master/lib/SILOptimizer/PassManager/Passes.cpp). This SROA (scalar replacement of aggregates) optimization destructures structs and tuples that are only used for their component fields (never used in their entirety). This lets the separate fields of the struct be moved around and optimized separately – as though they were separately declared variables.

For the example in this article, after destructuring the tuple the Swift compiler realizes that – according to the rules of the Swift memory layout – only the zeroth field of the `string1` and `string2` tuples are ever read so the initialization of the remaining fields is marked as a “dead store” and the dead fields 1-9 are omitted from the function entirely (never allocated on the stack).

The result is that `strcpy`, when it advances the pointer past the first element, overwrites whatever is on the stack past `string1`. I’ve organized the variables so that the source of the copy (`string2`) is immediately overwritten – causing an obvious and testable problem – but depending on how your variables on the stack are organized, you might not overwrite anything important, making this a very difficult bug to spot.

## The fix

The solution isn’t particularly difficult: if we _need_ the entire structure then we must _use_ the entire structure. To do this, replace the line:

```swift
strcpy(&string1.0, &string2.0)
```

with

```swift
withUnsafeMutablePointer(to: &string1) {
   $0.withMemoryRebound(to: CChar.self, capacity: 10) { str1Ptr in
      withUnsafePointer(to: &string2) {
         $0.withMemoryRebound(to: CChar.self, capacity: 10) { str2Ptr in
            _ = strcpy(str1Ptr, str2Ptr)
         }
      }
   }
}
```

This code makes its pointers from the entire `string1` and `string2` tuples (not just the zeroth elements). This guarantees the entire tuple remains intact. Once inside the `withUnsafeMutablePointer` scope, we can recast the pointer to `CChar` (from the 10 element tuple type) to satisfy the `strcpy` function signature.

For completeness, we should also fix the `String.fromCString` line:

```swift
let destination = withUnsafePointer(&string1) {
   $0.withMemoryRebound(to: CChar.self, capacity: 10) {
       String.fromCString($0)!
   }
}
```

The bug will go away if we fix just one of the two uses of `string1` but both uses were technically wrong so both should be fixed.

## How does this relate to the previous article?

The code that originally triggered this problem for me comes from `machMessageHandler` in [CwlCatchBadInstruction.swift](https://github.com/mattgallagher/CwlPreconditionTesting/blob/master/Sources/CwlPreconditionTesting/CwlCatchBadInstruction.swift?ts=3). It was originally:

```swift
guard mach_exc_server(&request.Head, &reply.Head) != 0 else { throw MachExcServer.Any }
```

but I was forced to rewrite it as:

```swift
guard request.withMsgHeaderPointer(in: { requestPtr in reply.withMsgHeaderPointer { replyPtr in
   mach_exc_server(requestPtr, replyPtr)
} }) != 0 else { throw MachExcServer.code(reply.RetCode) }
```

(using specialized functions to handle the ugliness of the pointer recasting).

In this example, `request` and `reply` are large structures for storing incoming and outgoing Mach messages but the `mach_exc_server` function only takes a pointer to their first field. Before the fix, in Release the `reply` structure was blank past the `Head` field and the Mach exception handler failed to do anything (the `EXC_BAD_INSTRUCTION` remained uncaught and the program crashed).

There are numerous other examples in the same file where I’ve wrapped statements in `withUnsafeMutablePointer` (or custom functions that wrap `withUnsafeMutablePointer`) to avoid the same problem. Curiously though, the `machMessageHandler` function was the only location that produced an easily observable bug. The other occurrences either avoided SROA optimization (for various reasons) or they didn’t actually write past their bounds or they overwrote unimportant variables.

You can see then that the problem requires a number of conditions to be true before it causes clear problems. It might seem like this works in your favor (simple chance may protect you from adverse effects) but without a clear crash or test failure every time, you might end up making this mistake in multiple places. Or the problem might remain dormant in your code and only cause a crash later when changes made elsewhere alter the arrangement of stack variables.

## Conclusion

This article is really just an aside, commenting on an interesting quirk from the previous article. The lesson that we need to construct pointers over the correct bounds in Swift is a straightforward one but it’s important to understand that bugs of this type can be very subtle; practically invisible. Any unsafe pointer – including an implicitly created one – can result in unsafe memory usage if the user of the pointer tries to access memory outside the bounds of the pointer’s creation.
