---
title: 'How blocks are implemented (and the consequences) | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/10/how-blocks-are-implemented-and.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:52b6ca8ffa2c3970'
translated: false
---

> 原文：[How blocks are implemented (and the consequences) | Cocoa with Love](https://www.cocoawithlove.com/2009/10/how-blocks-are-implemented-and.html)　·　Cocoa with Love (Matt Gallagher)

This post is a look at how clang implements blocks and how this implementation leads to a number of strange behaviors including local variables that end up global, Objective-C objects allocated on the stack instead of the heap, C variables that behave like C++ references, Objective-C objects in non-Objective-C languages, copy methods that don't copy and retain methods that don't retain.

## What blocks are to the compiler

Blocks are addressable sections of code implemented inline (inside other functions). The inline-edness can be convenient but the real reason why blocks are different to regular functions and function pointers is that they can reference local variables from the scope of the function surrounding their implementation without the invoker of the block needing to know of the surrounding scope variables' existence.

A block is implemented internally using two pieces:

1. segment of the executable
2. a data structure that predominantly contains the values of the variables that the block uses from its surrounding scope

The compiled code lives in its own separate location and does not actually reside inside inside the code of its surrounding scope. In implementation, the code is a function like any other. If you run:

```objc
otool -tV MyCompiledExecutable
```

then you'll see your blocks appearing immediately after their surrounding functions with names like `___surroundingFunction_block_invoke_21`.

So it is not the code which makes blocks special, it is the separate data structure. It is this data structure that I will focus on for the remainder of this post.

## The block data structure

[Clang's basic documentation on block implementations](http://clang.llvm.org/docs/BlockImplementation.txt) indicates that the data structure describing the block looks something like this:

```objc
struct Block_literal {
    void *isa;

    int flags;
    int reserved; // is actually the retain count of heap allocated blocks

    void (*invoke)(void *, ...); // a pointer to the block's compiled code

    struct Block_descriptor {
        unsigned long int reserved; // always nil
        unsigned long int size; // size of the entire Block_literal
        
        // functions used to copy and dispose of the block (if needed)
        void (*copy_helper)(void *dst, void *src);
        void (*dispose_helper)(void *src); 
    } *descriptor;

    // Here the struct contains one entry for every surrounding scope variable.
    // For non-pointers, these entries are the actual const values of the variables.
    // For pointers, there are a range of possibilities (__block pointer,
    // object pointer, weak pointer, ordinary pointer)
};
```

Of course, the reality is that this structure is never explicitly declared like this in clang. Clang is a compiler — a code generator — and the format of this structure is _generated_ programmatically from the [CodeGenFunction::BuildBlockLiteralTmp](http://clang.llvm.org/doxygen/CGBlocks_8cpp-source.html#l00103) method.

## Stack blocks and global blocks

Since the biggest difference between a function pointer and a block is the ability to use variables from the surrounding scope, it is interesting to look at what happens when a block does not reference anything in the surrounding scope.

Normally, the `Block_literal` data appears on the stack (like a regular `struct` would in its surrounding function). With no references to the surrounding scope, clang configures the `Block_literal` as a _global_ block instead. This causes the block to appear in a fixed global location instead of on the stack (the `flags` value has the `BLOCK_IS_GLOBAL` flag set to indicate this at runtime but it's not immediately clear to me if this is ever used).

The implication of this is that global blocks are never actually copied or disposed, even if you invoke the functions to do so. This optimisation is possible because without any references to the surrounding scope, no part of the block (neither its code nor its `Block_literal`) will ever change — it becomes a shared constant value.

## Blocks are always objects

If you're familiar with how Objective-C objects are declared, the `isa` field in the `Block_literal` above should be familiar — blocks are Objective-C objects. This may not seem strange in Objective-C but the reality is that even in pure C or C++, blocks are still Objective-C objects and the runtime support for blocks handles the `retain`/`release`/`copy` behaviors for the block in an Objective-C messaging manner.

Clang uses the class names `_NSConcreteStackBlock` and `_NSConcreteGlobalBlock` to refer to the classes for block literals but in CoreFoundation projects, this will map onto `NSStackBlock` and `NSGlobalBlock`. If you copy an `NSStackBlock`, it will return an `NSMallocBlock` (indicating its changed allocation location).

## Blocks are slightly weird objects

The interesting point to note about `NSStackBlock` is that it is a stack allocated Objective-C object. If you have ever tried to allocate an Objective-C object on the stack (not as a pointer but statically allocated) you'll know that the compiler normally forbids this.

The reason why blocks are placed on the stack by default is speed. In the common case where the lifetime of the block is less than that of the stack function that contains it, this is a very good optimisation.

The implication of stack blocks being allocated on the stack, is that a stack block cannot simply be `retain`ed — it will become invalid once the function that contains it is popped from the stack. If you invoke `retain` on a stack block, it will have no effect (the retain count of the block will remain at 1).

For this reason, if you need to return a block from a function or method, you must `[[block copy] autorelease]` it, not simply `[[block retain] autorelease]` it.

## __block values can move magically

Scope variables used in a block are normally passed to the block by `const` value (the compiler won't let you change the value but even if it did, the change wouldn't affect the value of the variable outside the block).

To alter this behavior, the type specifier `__block` was added. Any variable declared `__block` is passed by reference into the block (value on the outside will be changed after the block is invoked).

In the implementation, `__block` variables are initially allocated on the stack but if any block which references them is copied, they are moved onto the heap (`malloc`ed). This leads to the following strange situation...

```objc
int (^function())()
{
    __block int x = 0;
    
    int (^block)() = ^{
        x += 1;
        return x;
    };
    
    NSLog(@"x's location is on the stack: %p", &x);
    block = [[block copy] autorelease];
    NSLog(@"x's location is now on the heap: %p", &x);
    
    return block;
}
```

In this example, x's address changes when the copy is invoked. This is because when we declare a `__block` variable, a pointer to the real variable is created and any attempt to use the variable dereferences it. When `copy` is invoked, the location pointed to by the pointer changes to the new heap location, so any use of `x` causes a dereference to this new location.

This makes `__block` similar to to a reference parameter in C++ since C++ references are also transparently dereferenced pointers.

## NSMallocBlock never actually copies

Copying a block doesn't really give you a copy of the block — if the block is already an `NSMallocBlock`, a `copy` simply increases the retain count of the block (this retain count is an internal `reserved` field — the `retainCount` returned from the object will remain at 1). This is perfectly appropriate since the scope of the block cannot change after it is created (therefore the block is constant) but it does mean that invoking `copy` on a block is not the same thing as recreating it.

Assume the following code is in the same program as the previous example.

```objc
int (^someBlock)() = counterBlock();
int (^someBlockCopy)() = [[someBlock copy] autorelease];
int (^anotherBlock)() = counterBlock();
```

The block returned from `counterBlock()` counts the number of times that it is invoked by saving the count in the `__block` variable `x`.

In this example though, `someBlock` and `someBlockCopy` share the same `x` variable — they are not actually separate copies. However, `anotherBlock` does have its own separate `x` value.

If you need a genuinely separate copy, recreate the block, don't copy it.

## Blocks retain their NSObject scope variables

Blocks will `retain` any `NSObject` that they use from their enclosing scope when they are copied.

The biggest implication of this is that you must remember to [avoid retain cycles](https://www.cocoawithlove.com/2009/07/rules-to-avoid-retain-cycles.html) if the block will be held beyond a simple stack lifetime.

A [pointed out elsewhere](http://www.mikeash.com/?page=pyblog/friday-qa-2009-08-14-practical-blocks.html), you can suppress this retain of `NSObject`s by assigning the object to a `__block` variable outside the block and only ever using the `__block` variable inside the block.

You can also do the reverse of this and force a pointer that isn't an `NSObject` derived class to be retained when copied. Do this by declaring the pointer with `__attribute__((NSObject))`. Of course, the situations where you'd want to do this are exceedingly rare.

## Conclusion

Blocks are very simple to use in the case where you declare one inline and immediately pass into another function but once you need to copy or hold onto a block for a while, there are a number of quirks, some of which I've covered in this post.

Sadly at this time, [Apple's documentation on blocks](http://developer.apple.com/mac/library/documentation/Cocoa/Conceptual/Blocks/Articles/00_Introduction.html) is fairly basic and lacking in detail. This is what led me to start looking at clang's source code.

Of course, you don't need to stare at someone else's C++ code to learn about blocks. There are other sources of lighter, more approachable documentation on the topic. In addition to sources that I've already linked, there's also:

- Friday Q&A 2008-12-26

  " — an excellent run-down of potential use-cases for blocks in Objective-C.
- Programming with C Blocks

  — a good general summary of most aspects of blocks
- Episode 2: Life Cycles

  — a look at stack and heap allocation of blocks with diagrams
- BlockLanguageSpec
