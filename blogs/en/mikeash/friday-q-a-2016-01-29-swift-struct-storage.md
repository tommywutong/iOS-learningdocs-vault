---
title: 'Friday Q&A 2016-01-29: Swift Struct Storage'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2016-01-29-swift-struct-storage.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ade20e3e6f280e24'
translated: false
---

> 原文：[Friday Q&A 2016-01-29: Swift Struct Storage](https://www.mikeash.com/pyblog/friday-qa-2016-01-29-swift-struct-storage.html)　·　mikeash.com Friday Q&A

Posted at 2016-01-29 14:57 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2016-02-19: What Is the Secure Enclave?](https://www.mikeash.com/pyblog/friday-qa-2016-02-19-what-is-the-secure-enclave.html)  
Previous article: [Friday Q&A 2015-12-25: Swifty Target/Action](https://www.mikeash.com/pyblog/friday-qa-2015-12-25-swifty-targetaction.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [memory](https://www.mikeash.com/pyblog/?tag=memory) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2016-01-29: Swift Struct Storage

by [Mike Ash](https://www.mikeash.com/)

**Simple `struct`s**  
To explore how `struct`s get stored in memory, I built a test program consisting of two files. I compiled the test program with optimizations enabled but without whole-module optimization. By building tests that make calls from one file to the other, I was able to prevent the compiler from inlining everything, providing a clearer picture of where everything gets stored and how the data is passed between functions.

To start out, I created a simple `struct` with three elements:

```
    struct ExampleInts {
        var x: Int
        var y: Int
        var z: Int
    }
```

I created three functions that take an instance of this `struct` and return one of the fields:

```
    func getX(parameter: ExampleInts) -> Int {
        return parameter.x
    }

    func getY(parameter: ExampleInts) -> Int {
        return parameter.y
    }

    func getZ(parameter: ExampleInts) -> Int {
        return parameter.z
    }
```

In the other file, I created an instance of the `struct` and called each get function:

```
    func testGets() {
        let s = ExampleInts(x: 1, y: 2, z: 3)
        getX(s)
        getY(s)
        getZ(s)
    }
```

The compiler generates this code for `getX`:

```
    pushq   %rbp
    movq    %rsp, %rbp

    movq    %rdi, %rax

    popq    %rbp
    retq
```

Consulting our [cheat sheet](https://en.wikipedia.org/wiki/X86_calling_conventions#System_V_AMD64_ABI), we recall that arguments are passed sequentially in registers `rdi`, `rsi`, `rdx`, `rcx`, `r8`, and `r9`, and return values are placed in `rax`. The first two instructions here are just the function prologue, and the last two are the epilogue. The real work being done here is the `movq %rdi, %rax`, which takes the first parameter and returns it. Let's look at `getY`:

```
    pushq   %rbp
    movq    %rsp, %rbp

    movq    %rsi, %rax

    popq    %rbp
    retq
```

This is almost the same, but it returns the second parameter. How about `getZ`?

```
    pushq   %rbp
    movq    %rsp, %rbp

    movq    %rdx, %rax

    popq    %rbp
    retq
```

Again, almost the same, but it returns the third parameter. From this we can see that the individual `struct` elements are treated as separate parameters and passed to the functions individually. Picking out an element on the receiving end is a simple matter of picking the right register.

Let's confirm this on the calling end. Here's the generated code for `testGets`:

```
    pushq   %rbp
    movq    %rsp, %rbp

    movl    $1, %edi
    movl    $2, %esi
    movl    $3, %edx
    callq   __TF4main4getXFVS_11ExampleIntsSi

    movl    $1, %edi
    movl    $2, %esi
    movl    $3, %edx
    callq   __TF4main4getYFVS_11ExampleIntsSi

    movl    $1, %edi
    movl    $2, %esi
    movl    $3, %edx
    popq    %rbp
    jmp __TF4main4getZFVS_11ExampleIntsSi
```

We can see it constructing the `struct` instance directly in the parameter registers. (The `edi`, `esi`, and `edx` registers refer to the lower 32 bits of the `rdi`, `rsi`, and `rdx` registers, respectively.) It doesn't even bother trying to save the values across the calls, but just rebuilds the `struct` instance each time. Since the compiler knows exactly what the contents are, it can deviate significantly from how the Swift code is written. Note how the call to `getZ` is generated a bit differently from the other two. Since it's the last thing in the function, the compiler generates it as a tail call, cleaning up the local call frame and setting up `getZ` to return directly to the function that called `testGets`.

Let's see what sort of code the compiler generates when it doesn't know the `struct` contents. Here's a variant on this test function which gets the `struct` instance from elsewhere:

```
    func testGets2() {
        let s = getExampleInts()
        getX(s)
        getY(s)
        getZ(s)
    }
```

`getExampleInts` just creates the `struct` instance and returns it, but it's in the other file so the compiler can't see what's going on when optimizing `testGets2`. Here's that function:

```
    func getExampleInts() -> ExampleInts {
        return ExampleInts(x: 1, y: 2, z: 3)
    }
```

What sort of code does `testGets2` generate, now that the compiler can't know what the `struct` contains? Here it is:

```
    pushq   %rbp
    movq    %rsp, %rbp

    pushq   %r15
    pushq   %r14
    pushq   %rbx
    pushq   %rax

    callq   __TF4main14getExampleIntsFT_VS_11ExampleInts
    movq    %rax, %rbx
    movq    %rdx, %r14
    movq    %rcx, %r15

    movq    %rbx, %rdi
    movq    %r14, %rsi
    movq    %r15, %rdx
    callq   __TF4main4getXFVS_11ExampleIntsSi

    movq    %rbx, %rdi
    movq    %r14, %rsi
    movq    %r15, %rdx
    callq   __TF4main4getYFVS_11ExampleIntsSi

    movq    %rbx, %rdi
    movq    %r14, %rsi
    movq    %r15, %rdx

    addq    $8, %rsp
    popq    %rbx
    popq    %r14
    popq    %r15
    popq    %rbp
    jmp __TF4main4getZFVS_11ExampleIntsSi
```

Since the compiler can't reconstitute the values at each step, it has to save them. It places the three `struct` elements into the registers `rbx`, `r14`, and `r15`, then loads the parameter registers from those registers at each call. Those registers are saved by the caller, which means that their values are preserved across the call. And again, the compiler generates a tail call for `getZ`, with some more extensive cleanup beforehand.

At the top of the function, it calls `getExampleInts` and then loads values from `rax`, `rdx`, and `rcx`. Apparently the `struct` values are returned in those registers. Let's look at `getExampleInts` to confirm:

```
    pushq   %rbp
    movl    $1, %edi
    movl    $2, %esi
    movl    $3, %edx
    popq    %rbp
    jmp __TFV4main11ExampleIntsCfMS0_FT1xSi1ySi1zSi_S0_
```

This places the values `1`, `2`, and `3` into the argument registers, then calls the `struct`'s constructor. Here's the generated code for that constructor:

```
    pushq   %rbp
    movq    %rsp, %rbp

    movq    %rdx, %rcx
    movq    %rdi, %rax
    movq    %rsi, %rdx

    popq    %rbp
    retq
```

Sure enough, it returns the three values in `rax`, `rdx`, and `rcx`. The [cheat sheet](https://en.wikipedia.org/wiki/X86_calling_conventions#System_V_AMD64_ABI) says nothing about returning multiple values in multiple registers. How about the [official PDF](http://x86-64.org/documentation/abi.pdf)? It does say that two values can be returned in `rax` and `rdx`, but there's no mention of returning a third value in `rcx`. That's clearly what's happening, though. That's the fun of a new language: it doesn't always have to play by the old rules. If it was interoperating with C code it would have to follow the standard conventions, but Swift-to-Swift calls can invent new ones.

How about `inout` parameters? If they work like we'd do it in C, we'd expect the `struct` to be laid out in memory and a pointer passed in. Here are two test functions (in two different files, of course):

```
    func testInout() {
        var s = getExampleInts()
        totalInout(&s)
    }

    func totalInout(inout parameter: ExampleInts) -> Int {
        return parameter.x + parameter.y + parameter.z
    }
```

Here's the generated code for `testInout`:

```
    pushq   %rbp
    movq    %rsp, %rbp
    subq    $32, %rsp

    callq   __TF4main14getExampleIntsFT_VS_11ExampleInts

    movq    %rax, -24(%rbp)
    movq    %rdx, -16(%rbp)
    movq    %rcx, -8(%rbp)
    leaq    -24(%rbp), %rdi
    callq   __TF4main10totalInoutFRVS_11ExampleIntsSi

    addq    $32, %rsp
    popq    %rbp
    retq
```

In the prologue, it creates a 32-byte stack frame. It then calls `getExampleInts`, and after the call saves the resulting values into stack slots at offsets `-24`, `-16`, and `-8`. It then calculates a pointer to offset `-24`, loads that into the `rdi` parameter register, and calls `totalInout`. Here's the generated code for that function:

```
    pushq   %rbp
    movq    %rsp, %rbp
    movq    (%rdi), %rax
    addq    8(%rdi), %rax
    jo  LBB4_3
    addq    16(%rdi), %rax
    jo  LBB4_3
    popq    %rbp
    retq
    LBB4_3:
    ud2
```

This loads the values by offset from the parameter that's passed in, totaling them up and returning the result in `rax`. The `jo` instructions are checking for overflow. If either of the `addq` instructions produce an oveflow, the `jo` instructions will jump down to the `ud2` instruction which terminates the program.

We can see that it's exactly as we expected: when passing the `struct` to an `inout` parameter, the `struct` is laid out contiguously in memory and then a pointer to it is passed in.

**Big `struct`s**  
What happens if we're dealing with a larger struct, bigger than fits comfortably in registers? Here's a test `struct` with ten elements:

```
    struct TenInts {
        var elements = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    }
```

Here's a get function that constructs an instance and returns it. This is placed in a separate file to avoid inlining:

```
    func getHuge() -> TenInts {
        return TenInts()
    }
```

Here's a function that gets an element out of this `struct`:

```
    func getHugeElement(parameter: TenInts) -> Int {
        return parameter.elements.5
    }
```

Finally, a test function that exercises these:

```
    func testHuge() {
        let s = getHuge()
        getHugeElement(s)
    }
```

Let's look at the generated code, starting with `testHuge`:

```
    pushq   %rbp
    movq    %rsp, %rbp
    subq    $160, %rsp

    leaq    -80(%rbp), %rdi
    callq   __TF4main7getHugeFT_VS_7TenInts

    movups  -80(%rbp), %xmm0
    movups  -64(%rbp), %xmm1
    movups  -48(%rbp), %xmm2
    movups  -32(%rbp), %xmm3
    movups  -16(%rbp), %xmm4
    movups  %xmm0, -160(%rbp)
    movups  %xmm1, -144(%rbp)
    movups  %xmm2, -128(%rbp)
    movups  %xmm3, -112(%rbp)
    movups  %xmm4, -96(%rbp)

    leaq    -160(%rbp), %rdi
    callq   __TF4main14getHugeElementFVS_7TenIntsSi

    addq    $160, %rsp
    popq    %rbp
    retq
```

This code (excluding the function prologue and epilogue) can be broken into three pieces.

The first piece calculates the address for offset `-80` relative to the stack frame, and calls `getHuge`, passing that address as a parameter. The `getHuge` function has no parameters in the source code, but it's common to use a hidden parameter to return larger `struct`s. The caller allocates storage for the return value, then passes a pointer to that storage in the hidden parameter. That appears to be what's going on here, with that allocated storage residing on the stack.

The second piece copies the returned `struct` from stack offset `-80` to stack offset `-160`. It loads pieces of the `struct` sixteen bytes at a time into five `xmm` registers, then places the contents of those registers back on the stack starting at offset `-160`. I'm not clear why the compiler generates this copy rather than using the original value in place. I suspect the optimizer just isn't quite smart enough to realize that it doesn't need the copy.

The third piece calculates the address for stack offset `-160` and then calls `getHugeElement` passing that address as a parameter. In our previous experiment with a three-element `struct`, it was passed by value in registers. With this larger `struct`, it's passed by pointer instead.

The generated code for the other functions confirms this: the `struct` is passed in and out by pointer, and lives on the stack. Here's `getHugeElement` to start with:

```
    pushq   %rbp
    movq    %rsp, %rbp
    movq    40(%rdi), %rax
    popq    %rbp
    retq
```

This loads offset `40` from the parameter passed in. Each element is eight bytes, so offset `40` corresponds to `elements.5`. The function then returns this value.

Here's `getHuge`:

```
    pushq   %rbp
    movq    %rsp, %rbp
    pushq   %rbx
    subq    $88, %rsp

    movq    %rdi, %rbx
    leaq    -88(%rbp), %rdi
    callq   __TFV4main7TenIntsCfMS0_FT_S0_

    movups  -88(%rbp), %xmm0
    movups  -72(%rbp), %xmm1
    movups  -56(%rbp), %xmm2
    movups  -40(%rbp), %xmm3
    movups  -24(%rbp), %xmm4
    movups  %xmm0, (%rbx)
    movups  %xmm1, 16(%rbx)
    movups  %xmm2, 32(%rbx)
    movups  %xmm3, 48(%rbx)
    movups  %xmm4, 64(%rbx)
    movq    %rbx, %rax

    addq    $88, %rsp
    popq    %rbx
    popq    %rbp
    retq
```

This looks a lot like `testHuge` above: it allocates stack space, calls a function, in this case, the `TenInts` constructor function, then copies the return value to its final location. Here, that final location is the pointer passed in as the implicit parameter.

While we're here, let's take a look at the `TenInts` constructor:

```
    pushq   %rbp
    movq    %rsp, %rbp

    movq    $1, (%rdi)
    movq    $2, 8(%rdi)
    movq    $3, 16(%rdi)
    movq    $4, 24(%rdi)
    movq    $5, 32(%rdi)
    movq    $6, 40(%rdi)
    movq    $7, 48(%rdi)
    movq    $8, 56(%rdi)
    movq    $9, 64(%rdi)
    movq    $10, 72(%rdi)
    movq    %rdi, %rax

    popq    %rbp
    retq
```

Like the other functions, this takes a pointer to memory for the new `struct` as an implicit parameter. It then stores the values `1` through `10` into that memory and returns.

I came across an interesting case while building out these test cases. Here's a test function which makes three calls to `getHugeElement` intsead of just one:

```
    func testThreeHuge() {
        let s = getHuge()
        getHugeElement(s)
        getHugeElement(s)
        getHugeElement(s)
    }
```

Here's the generated code:

```
    pushq   %rbp
    movq    %rsp, %rbp
    pushq   %r15
    pushq   %r14
    pushq   %r13
    pushq   %r12
    pushq   %rbx
    subq    $392, %rsp

    leaq    -120(%rbp), %rdi
    callq   __TF4main7getHugeFT_VS_7TenInts
    movq    -120(%rbp), %rbx
    movq    %rbx, -376(%rbp)
    movq    -112(%rbp), %r8
    movq    %r8, -384(%rbp)
    movq    -104(%rbp), %r9
    movq    %r9, -392(%rbp)
    movq    -96(%rbp), %r10
    movq    %r10, -400(%rbp)
    movq    -88(%rbp), %r11
    movq    %r11, -368(%rbp)
    movq    -80(%rbp), %rax
    movq    -72(%rbp), %rcx
    movq    %rcx, -408(%rbp)
    movq    -64(%rbp), %rdx
    movq    %rdx, -416(%rbp)
    movq    -56(%rbp), %rsi
    movq    %rsi, -424(%rbp)
    movq    -48(%rbp), %rdi

    movq    %rdi, -432(%rbp)
    movq    %rbx, -200(%rbp)
    movq    %rbx, %r14
    movq    %r8, -192(%rbp)
    movq    %r8, %r15
    movq    %r9, -184(%rbp)
    movq    %r9, %r12
    movq    %r10, -176(%rbp)
    movq    %r10, %r13
    movq    %r11, -168(%rbp)
    movq    %rax, -160(%rbp)
    movq    %rax, %rbx
    movq    %rcx, -152(%rbp)
    movq    %rdx, -144(%rbp)
    movq    %rsi, -136(%rbp)
    movq    %rdi, -128(%rbp)
    leaq    -200(%rbp), %rdi
    callq   __TF4main14getHugeElementFVS_7TenIntsSi

    movq    %r14, -280(%rbp)
    movq    %r15, -272(%rbp)
    movq    %r12, -264(%rbp)
    movq    %r13, -256(%rbp)
    movq    -368(%rbp), %rax
    movq    %rax, -248(%rbp)
    movq    %rbx, -240(%rbp)
    movq    -408(%rbp), %r14
    movq    %r14, -232(%rbp)
    movq    -416(%rbp), %r15
    movq    %r15, -224(%rbp)
    movq    -424(%rbp), %r12
    movq    %r12, -216(%rbp)
    movq    -432(%rbp), %r13
    movq    %r13, -208(%rbp)
    leaq    -280(%rbp), %rdi
    callq   __TF4main14getHugeElementFVS_7TenIntsSi

    movq    -376(%rbp), %rax
    movq    %rax, -360(%rbp)
    movq    -384(%rbp), %rax
    movq    %rax, -352(%rbp)
    movq    -392(%rbp), %rax
    movq    %rax, -344(%rbp)
    movq    -400(%rbp), %rax
    movq    %rax, -336(%rbp)
    movq    -368(%rbp), %rax
    movq    %rax, -328(%rbp)
    movq    %rbx, -320(%rbp)
    movq    %r14, -312(%rbp)
    movq    %r15, -304(%rbp)
    movq    %r12, -296(%rbp)
    movq    %r13, -288(%rbp)
    leaq    -360(%rbp), %rdi
    callq   __TF4main14getHugeElementFVS_7TenIntsSi

    addq    $392, %rsp
    popq    %rbx
    popq    %r12
    popq    %r13
    popq    %r14
    popq    %r15
    popq    %rbp
    retq
```

The structure of this function is similar to the previous version. It calls `getHuge`, copies the result, then calls `getHugeElement` three times. For each call, it copies the `struct` _again_, presumably to guard against `getHugeElement` making modifications. What I found really interesting is that the copies are all done one element at a time using integer registers, rather than two elements at a time in `xmm` registers as `testHuge` did. I'm not sure what causes the compiler to choose the integer registers here, as it seems like copying two elements at a time with the `xmm` registers would be more efficient and result in smaller code.

I also experimented with really large `structs`:

```
    struct HundredInts {
        var elements = (TenInts(), TenInts(), TenInts(), TenInts(), TenInts(), TenInts(), TenInts(), TenInts(), TenInts(), TenInts())
    }

    struct ThousandInts {
        var elements = (HundredInts(), HundredInts(), HundredInts(), HundredInts(), HundredInts(), HundredInts(), HundredInts(), HundredInts(), HundredInts(), HundredInts())
    }

    func getThousandInts() -> ThousandInts {
        return ThousandInts()
    }
```

The generated code for `getThousandInts` is pretty crazy:

```
    pushq   %rbp
    pushq   %rbx
    subq    $8008, %rsp

    movq    %rdi, %rbx
    leaq    -8008(%rbp), %rdi
    callq   __TFV4main12ThousandIntsCfMS0_FT_S0_
    movq    -8008(%rbp), %rax
    movq    %rax, (%rbx)
    movq    -8000(%rbp), %rax
    movq    %rax, 8(%rbx)
    movq    -7992(%rbp), %rax
    movq    %rax, 16(%rbx)
    movq    -7984(%rbp), %rax
    movq    %rax, 24(%rbx)
    movq    -7976(%rbp), %rax
    movq    %rax, 32(%rbx)
    movq    -7968(%rbp), %rax
    movq    %rax, 40(%rbx)
    movq    -7960(%rbp), %rax
    movq    %rax, 48(%rbx)
    movq    -7952(%rbp), %rax
    movq    %rax, 56(%rbx)
    movq    -7944(%rbp), %rax
    movq    %rax, 64(%rbx)
    movq    -7936(%rbp), %rax
    movq    %rax, 72(%rbx)
    ...
    movq    -104(%rbp), %rax
    movq    %rax, 7904(%rbx)
    movq    -96(%rbp), %rax
    movq    %rax, 7912(%rbx)
    movq    -88(%rbp), %rax
    movups  -80(%rbp), %xmm0
    movups  -64(%rbp), %xmm1
    movups  -48(%rbp), %xmm2
    movups  -32(%rbp), %xmm3
    movq    %rax, 7920(%rbx)
    movq    -16(%rbp), %rax
    movups  %xmm0, 7928(%rbx)
    movups  %xmm1, 7944(%rbx)
    movups  %xmm2, 7960(%rbx)
    movups  %xmm3, 7976(%rbx)
    movq    %rax, 7992(%rbx)
    movq    %rbx, %rax

    addq    $8008, %rsp
    popq    %rbx
    popq    %rbp
    retq
```

The compiler generates two thousand instructions to copy this `struct`. This seems like a good place to emit a call to `memcpy`, but I imagine that optimizing for absurdly gigantic `struct`s isn't a high priority for the compiler team right now.

**Class Fields**  
Let's take a look at what happens when the `struct` fields are more complicated than simple integers. Here's a simple `class`, and a `struct` which contains one:

```
    class ExampleClass {}
    struct ContainsClass {
        var x: Int
        var y: ExampleClass
        var z: Int
    }
```

Here's a set of functions (split across two files to defeat inlining) which exercise them:

```
    func testContainsClass() {
        let s = ContainsClass(x: 1, y: getExampleClass(), z: 3)
        getClassX(s)
        getClassY(s)
        getClassZ(s)
    }

    func getExampleClass() -> ExampleClass {
        return ExampleClass()
    }

    func getClassX(parameter: ContainsClass) -> Int {
        return parameter.x
    }

    func getClassY(parameter: ContainsClass) -> ExampleClass {
        return parameter.y
    }

    func getClassZ(parameter: ContainsClass) -> Int {
        return parameter.z
    }
```

Let's start by looking at the generated code for the getters. Here's `getClassX`:

```
    pushq   %rbp
    movq    %rsp, %rbp
    pushq   %rbx
    pushq   %rax

    movq    %rdi, %rbx
    movq    %rsi, %rdi
    callq   _swift_release
    movq    %rbx, %rax

    addq    $8, %rsp
    popq    %rbx
    popq    %rbp
    retq
```

The three `struct` elements will be passed in the first three parameter registers, `rdi`, `rsi`, and `rdx`. This function wants to return the value in `rdi` by moving it to `rax` and then returning, but it has to do some bookkeeping first. It appears that the object reference passed in `rsi` is passed retained, and must be released before the function returns. This code moves `rdi` into a safe temporary register, `rbx`, then moves the object reference to `rdi` and calls `swift_release` to release it. It then moves the value in `rbx` to the return register `rax` and returns from the function.

The code for `getClassZ` is pretty much the same, except instead of taking the value from `rdi`, it takes it from `rdx`:

```
    pushq   %rbp
    movq    %rsp, %rbp
    pushq   %rbx
    pushq   %rax

    movq    %rdx, %rbx
    movq    %rsi, %rdi
    callq   _swift_release
    movq    %rbx, %rax

    addq    $8, %rsp
    popq    %rbx
    popq    %rbp
    retq
```

The code for `getClassY` will be the odd one, since it returns an object reference rather than an integer. Here it is:

```
    pushq   %rbp
    movq    %rsp, %rbp
    movq    %rsi, %rax
    popq    %rbp
    retq
```

This is short! It moves the value from `rsi`, which is the object reference, into `rax` and returns it. There's no bookkeeping, just a quick shuffling of data. Apparently, the value is passed in retained, but also returned retained, so this code doesn't have to do any memory management at all.

So far we've seen that the code for dealing with this `struct` is much like the code for dealing with the `struct` containing three `Int` fields, except that the object reference field is passed in retained and must be released by the callee. With that in mind, let's look at the generated code for testContainsClass:

```
    pushq   %rbp
    movq    %rsp, %rbp
    pushq   %r14
    pushq   %rbx

    callq   __TF4main15getExampleClassFT_CS_12ExampleClass
    movq    %rax, %rbx

    movq    %rbx, %rdi
    callq   _swift_retain
    movq    %rax, %r14
    movl    $1, %edi
    movl    $3, %edx
    movq    %rbx, %rsi
    callq   __TF4main9getClassXFVS_13ContainsClassSi

    movq    %r14, %rdi
    callq   _swift_retain
    movl    $1, %edi
    movl    $3, %edx
    movq    %rbx, %rsi
    callq   __TF4main9getClassYFVS_13ContainsClassCS_12ExampleClass
    movq    %rax, %rdi
    callq   _swift_release

    movl    $1, %edi
    movl    $3, %edx
    movq    %rbx, %rsi

    popq    %rbx
    popq    %r14
    popq    %rbp
    jmp __TF4main9getClassZFVS_13ContainsClassSi
```

The first thing this function does is call `getExampleClass` to get the `ExampleClass` instance it stores in the `struct`. It takes the returned reference and moves it to `rbx` for safekeeping.

Next, it calls `getClassX`, and to do so it has to build a copy of the `struct` in the parameter registers. The two integer fields are easy, but the object field needs to be retained to match what the functions expect. The code calls `swift_retain` on the value stored in `rbx`, then places that value in `rsi` and places `1` and `3` in `rdi` and `rdx` to build the complete struct. Finally, it calls `getClassX`.

The code to call `getClassY` is nearly the same. However, `getClassY` returns an object reference which needs to be released. After the call, this code moves the return value into `rdi` and calls `swift_release` to take care of its required memory management.

This function calls `getClassZ` as a tail call, so the code here is a bit different. The object reference came retained from `getExampleClass`, so it doesn't need to be retained separately for this final call. This code places it into `rsi`, places `1` and `3` into `rdi` and `rdx` again, then cleans up the stack and jumps to `getClassZ` to make the final call.

Ultimately, there's little change from a `struct` with all `Int`s. The only real difference is that copying a `struct` with an object in it requires retaining that object, and disposing of that `struct` requires releasing the object.

**Conclusion**  
`struct` storage in Swift is ultimately pretty straightforward, and much of what we've seen carries over from C's much simpler `struct`s. A `struct` instance is largely treated as a loose collection of independent values, which can be manipulated collectively when required. Local `struct` variables might be stored on the stack or the individual pieces might be stored in registers, depending on the size of the `struct`, the register usage of the rest of the code, and the whims of the compiler. Small `struct`s are passed and returned in registers, while larger `struct`s are passed and returned by reference. `struct`s get copied whenever they're passed and returned. Although you can use `struct`s to implement copy-on-write data types, the base language construct is copied eagerly and more or less blindly.

That's it for today. Come back next time for more daring feats of programming. Friday Q&A is driven by reader ideas, so if you grow bored while waiting for the next installment and have something you'd like to see discussed, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
