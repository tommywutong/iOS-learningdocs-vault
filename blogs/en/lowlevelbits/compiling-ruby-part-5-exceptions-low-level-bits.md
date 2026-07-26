---
title: 'Compiling Ruby. Part 5: exceptions - Low Level Bits 🇺🇦'
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/compiling-ruby-part-5/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5c72d119d15ed02d'
translated: false
---

> 原文：[Compiling Ruby. Part 5: exceptions - Low Level Bits 🇺🇦](https://lowlevelbits.org/compiling-ruby-part-5/)　·　Low Level Bits (Alex Denisov)

# Compiling Ruby. Part 5: exceptions

_Published on Dec 22, 2023_

This article is part of the series "Compiling Ruby," in which I'm documenting my journey of building an ahead-of-time (AOT) compiler for [DragonRuby](https://dragonruby.org), which is based on [mruby](https://mruby.org) and heavily utilizes [MLIR](https://mlir.llvm.org) and [LLVM](https://llvm.org) infrastructure.

This series is mostly a brain dump, though sometimes I'm trying to make things easy to understand. Please, let me know if some specific part is unclear and you'd want me to elaborate on it.

Here is what you can expect from the series:

- [Motivation](https://lowlevelbits.org/compiling-ruby-part-0/): some background reading on what and why
- [Compilers vs Interpreters](https://lowlevelbits.org/compiling-ruby-part-1/): a high level overview of the chosen approach
- [RiteVM](https://lowlevelbits.org/compiling-ruby-part-2/): a high-level overview of the mruby Virtual Machine
- [MLIR and compilation](https://lowlevelbits.org/compiling-ruby-part-3/): covers what is MLIR and how it fits into the whole picture
- [Progress update](https://lowlevelbits.org/compiling-ruby-part-4/): short progress update with what's done and what's next
- **[Exceptions](https://lowlevelbits.org/compiling-ruby-part-5/): an overview of how exceptions work in Ruby**
- Garbage Collection (TBD): an overview of how mruby manages memory
- Fibers (TBD): what are fibers in Ruby, and how mruby makes them work

_Note: the list of TBD articles may change as I may want to split some parts into smaller chunks._

---

### Call Stack, Stack Frames, and Program Counter

During the program execution, a machine maintains a pointer to the instruction being executed. It’s called [Program Counter](https://en.wikipedia.org/wiki/Program_counter) (or `Instruction Pointer`).

When you call a method (or send a message if we are speaking of Ruby), the program counter is set to the first instruction on the called function (`callee`). The program somehow needs to know how to get back to the call site once the “child” method has completed its execution.

This information is typically maintained using the concept of a [Call Stack](https://en.wikipedia.org/wiki/Call_stack).

Consider the following program and its call stack on the right.

![Call Stack](https://lowlevelbits.org/img/compiling-ruby-5/call-stack.png)

The call stack consists of [Stack Frames](https://en.wikipedia.org/wiki/Call_stack#Structure). Whenever a function is called, a new stack frame is created and `push`ed onto the stack. When the called function returns - the stack frame is `pop`ed.

At every point, the call stack represents the actual [Stack Trace](https://en.wikipedia.org/wiki/Stack_trace).

The very top of the call stack represents the scope of the whole file, followed by the stack frame of the `first` function, followed by the `second` function, and so forth. In Ruby, the top function/file scope is referred to as simply `top`.

Now, imagine that we want to pass some information from the `second` function to the `top`. Some error or something _exceptional_ happened, and this specific program state needs some special handling.

There are several limited ways to handle such case: either return some special value up (thus, each function on the call stack should be aware of this), or we can use some global variable to communicate with the callers (e.g., `errno` in C) which is again “pollutes” the business logic through the call stack.

One way to handle this problem more elegantly is to use particular language constructs - exceptions.

Instead of polluting the whole call stack, we can `throw`/`raise` an exception and then add special handling at the `top`, like in this picture:

![Simple Exception](https://lowlevelbits.org/img/compiling-ruby-5/exception-example.png)

### Stack Unwinding

Now, the question is: How do we implement this feature? To answer it, let’s understand what needs to happen!

The program was in some specific state before it called the `first` function at the top. Now, the program is in another specific state around the `raise "error"` line in the `second` function.

We need to restore the state somehow as it was right before the `first` call and continue execution right after the `rescue` in `top` (by changing the program counter accordingly).

Conceptually, we can save the machine state before calling the `first` method and restoring it later. The problem is that storing the state of the whole machine is too expensive and adds overhead by saving more than needed.

Instead, we can put the responsibility for maintaining the program on the actual program developers.

Most languages provide useful features for dealing with this:

- Ruby has explicit `ensure` blocks
- Java has explicit `finally` statements
- C++ has RAII and implicit destructors
- (C has `setjmp`/`longjmp`, but we are only talking about useful features)

Here is how it works in the case of Ruby.

Whenever the exception is thrown, the program climbs up through the call stack and executes code from those [finalizers](https://en.wikipedia.org/wiki/Finalizer#Connection_with_finally)until it reaches the exception handler.

This process is called `Stack Unwinding`.

_I’m not a native speaker, but I’d say it should be called “Stack Winding”, but oh well_

Here is an updated example with explicit state restoration during the stack unwinding.

Without executing code from the `ensure` block, the hypothetical lock would never be released, thus breaking the program in terrible ways.

![Stack Unwinding](https://lowlevelbits.org/img/compiling-ruby-5/stack-unwinding.png)

### Exceptions in Ruby

Now, I can talk about different kinds of exceptions in Ruby. From my perspective, there are three different kinds:

- actual `raise`d exceptions
- `break` statements
- `return` statements

Both `break` and `return` statements have special meaning when used in the context of `Proc`s.

Let me elaborate on all the three with the examples.

#### Normal Exceptions

Actual exceptions climb up the stack, calling finalizers until an exception handler is found.

These are the normal exceptions you are all familiar with.

![Simple Exception](https://lowlevelbits.org/img/compiling-ruby-5/exception-example.png)

#### `return`s from a block

`return` statements behave differently depending on the lexical scope they are part of.

Here is a little puzzle for you.

What will be printed on the screen:

![Return from a block puzzle](https://lowlevelbits.org/img/compiling-ruby-5/return_blk-puzzle.png)

`return` is called from within a block. You may expect the `x * 4` to be returned from the block, but it’s returned from the enclosing function (lexical scope).

![Return from a block call stack](https://lowlevelbits.org/img/compiling-ruby-5/return_blk-example.png)

As you can see, `return x * 4` would return from `f` instead of from the block.

The code prints

```
2: 8
```

instead of

```
1: 8
2: 42
```

#### `break`s

_Almost_ like `return`s, `break`s allow returning from the enclosing function, but in a slightly different way.

This is the most complex example here. Let me write down the steps explicitly. You may want to open the picture in a separate tab to read it.

![Break example](https://lowlevelbits.org/img/compiling-ruby-5/break-example.png)

1. `top` calls the `loop` function and passes the block to it. The block is just another function under the hood; it’s presented separately here as the `__anonymous_block.`
2. Runtime creates a new stack frame for `loop` and puts it on the call stack.
3. `loop` calls the passed block (`__anonymous_block`).
4. Runtime creates new stack frame for `__anonymous_block` and puts it on the stack.
5. The `__anonymous_block` increments `i`, checks for equality, and returns to `loop`, nothing special.
6. Runtime removes the `__anonymous_block` stack frame from the call stack.
7. `loop`s stack frame is kept on the call stack, and the next iteration of `while true` calls the `__anonymous_block` again.
8. Runtime creates new stack frame for `__anonymous_block` and puts it on the stack.
9. The `__anonymous_block` increments `i`, checks for equality, and invokes `break`.
10. The `break` initiates stack unwinding and returns from the enclosing function (`loop`). See the dashed line.
11. `loop` returns, thus bypassing the endless loop `while true`.

The `break` construct is effectively equivalent to the following code:

![Break implemented using exception](https://lowlevelbits.org/img/compiling-ruby-5/break-exception.png)

### Implementation

All the language constructs described above (exceptions, `return`s and `break`s within a block) behave similarly: they unwind the stack (calling the finalizers on the way up) and stop at some well-defined point.

They are implemented slightly differently in the original mruby runtime. Still, I implemented them all as exceptions, with `return`s and `break`s being special exceptions: they need to carry a value and store information on where to stop the unwinding process.

The implementation from the LLVM perspective is covered in my recent talk at LLVM Social Berlin: [Stack unwinding, landing pads, and other catches](https://www.youtube.com/watch?v=gH5-lITYrMg).

Here, I’ll mainly focus on the details from the Mruby runtime perspective.

Consider the following example:

![Landing pads](https://lowlevelbits.org/img/compiling-ruby-5/landing-pads.png)

The blocks following `rescue` and `ensure` are called _**Landing Pads**_.

This example has two kinds of landing pads: catch (`rescue`) and cleanup (`ensure`). Catches are “conditional” landing pads: they will be executed only if the exception type matches their type. Note the last `rescue`: it doesn’t have any type attached, so it will just catch any exception.

Conversely, cleanups are “unconditional” - they will always run, but they will also forward the exception up to the next function on the call stack.

Another important detail in this example is the second `rescue`: it uses function argument as its type. That is, the landing pad type is only known at run time, and it could be anything.

_In C++, for example, all the `catch` types must be known upfront, and the compiler emits special Runtime Type Information (RTTI). Again, IMO, it should be Compile Time Type Information, but it’s C++…_

For this reason, Ruby VM always enters each landing pad. For catches, it first checks (at run time!) if the exception type matches the landing pad’s type, and if so, the exception is marked as caught, and the landing pad’s execution continues.

If the exception type doesn’t match - the exception is immediately re-thrown so the next landing pad can try to catch it.

### MLIR

I’d love to describe how I modeled exceptions at the MLIR level, but it will take more time to do it for several reasons:

- my original approach to constructing SSA right away didn’t work due to the way exceptions work (namely, some registers must spill on the stack), so the dialects have changed a bit, and I need to clean them up a bit
- the way I model them currently is more of a hack and only works because I have certain conventions, so it’s not a solid model yet
- I added JIT support (for `Kernel.eval`) and need to do some tweaking there to make exceptions work during just-in-time evaluation

I’ll write down all the low-level details at some point, but I don’t have an ETA, so I’ll stop here.

---

**Thank you so much for reaching this far!**

The following articles will focus on JIT compilation and debug information.

[Don’t miss those details!](https://lowlevelbits.org/subscribe/)
