---
title: 'discussed in last week''s article'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-04-27-plcrashreporter-and-unwinding-the-stack-with-dwarf.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:273093b18796abe7'
translated: false
---

> 原文：[discussed in last week's article](https://www.mikeash.com/pyblog/friday-qa-2012-04-27-plcrashreporter-and-unwinding-the-stack-with-dwarf.html)　·　mikeash.com Friday Q&A

Posted at 2012-04-27 14:11 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-05-04: PLCrashReporter and Unwinding the Stack With DWARF, Part 2](https://www.mikeash.com/pyblog/friday-qa-2012-05-04-plcrashreporter-and-unwinding-the-stack-with-dwarf-part-2.html)  
Previous article: [Friday Q&A 2012-04-13: Nib Memory Management](https://www.mikeash.com/pyblog/friday-qa-2012-04-13-nib-memory-management.html)  
Tags: [dangerous](https://www.mikeash.com/pyblog/?tag=dangerous) [debugging](https://www.mikeash.com/pyblog/?tag=debugging) [dwarf](https://www.mikeash.com/pyblog/?tag=dwarf) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [guest](https://www.mikeash.com/pyblog/?tag=guest) [semi-evil](https://www.mikeash.com/pyblog/?tag=semi-evil)

Friday Q&A 2012-04-27: PLCrashReporter and Unwinding the Stack With DWARF

by [Gwynne Raskind](http://blog.darkrainfall.org/)

---

**Walking the stack with steel-toed boots**  
On any given architecture, the frame pointer - a reserved general-purpose register set aside specifically for the purpose of keeping track of the function call stack - is optional. The `-fomit-frame-pointer` flag to the compiler is commonly used for optimized code, as making an extra register available is a significant win for many applications. The problem is that without a frame pointer, a naive debugger has no reliable way of walking stack frames, making it difficult or impossible to generate a backtrace in case of a crash, or even just for stopping at breakpoints.

A stopgap solution to this problem is a stack scanner, a bit of code that walks the thread's stack in pointer-sized chunks looking for something that seems like a return address and following whatever it finds. In pseudo-code, a simple one looks a bit like this:

```
    void *getNextStackFrame(void **threadSP)
    {
        for (void *loc = *threadSP; loc <= *threadSP + sizeof(void *) * 30; ++loc)
        {
            if (looksLikeReturnAddress(*loc))
                return (*threadSP = loc);
        }
        return NULL;
    }
```

Unfortunately, a stack scanner will return false positives pretty often, because a lot of things on a function's stack can look like a return address. For example, the following contrived code is guaranteed to make a stack scanner return bogus results on i386:

```
    int main(int argc, char **argv)
    {
        pthread_create(NULL, NULL, myCaller, NULL);
        sleep(10);
        return 0;
    }

    void myCaller(void)
    {
        myCallee(^ { printf("I'm a crashing block %p %p %p %p %p %p %p!\n"); });
    }

    void myCallee(dispatch_block_t block)
    {
        block();
    }
```

The address of the block is passed on the stack when `myCallee()` is called. A stack scanner will find the pushed return address of `myCaller()` and return that as the next frame - and then when another frame is requested, it will see the address of the block next and return _that_. Because the block is a valid symbol in the executable, it looks legitimate.

And don't forget, the secondary thread's stack is often adjacent to the main thread's for reasons of efficiency, so when the scanner reaches the end, it's gonna keep right on going and give you at least some the trace for a thread that's not even involved. The result looks something like this:

```
    Thread 1:
    1. __timed_sigwait + ??
    2. _sleep + ??
    3. _main + ??
    4. start + ??

    Thread 2 crashed:
    1.  _printf + ??
    2.  ___myCaller_block_invoke_0 + 0
    3.  myCallee + ??
    4.  ___myCaller_block_invoke_0 + 0
    5.  myCaller + ??
    6.  _pthread_start + ??
    7.  thread_start + ??
    8.  __timed_sigwait + ??
    9.  _sleep + ??
    10. _main + ??
    11. start + ??
```

You can figure out what's going on from this, but that block frame right in the middle of nowhere looks pretty odd, and seeing a bunch of frames from the main thread is confusing. If only there were a better way, especially on `x86_64`, where omitting the frame pointer is the default for release builds!

**Debugging information**  
There is a better way. The compiler embeds robust debugging information into an executable or library when it's built, unless asked not to. Even release builds without a frame pointer will often have the debugging information, or some subset of it, available. Any binary that uses C++ or Objective-C is all but guaranteed to have unwinding information, which for the purpose of this discussion is the same thing.

Unwinding information on OS X is stored in two different ways. One is generally conformant to the DWARF-2 specification, with extensions. The other is a "compact unwind encoding", which encodes the same information in the vast majority of cases using about a fifth as much space and requring orders of magnitude less effort to parse. The compiler generates the information necessary to trace function calls in the DWARF format, and OS X's linker automatically synthesizes the faster and smaller compact encoding based on that data.

**DWARF**  
Unwinding information in DWARF is stored as a miniature program which must be executed to determine the correct values for saved registers in a given stack frame, including the return address.

A DWARF program is represented as a series of opcodes which manipulate a CFA (Canonical Frame Address) and register set. Conceptually, DWARF constructs a Call Frame Information table which gives the values of any saved registers at a given PC address; in practice, almost every row in a CFI table will be identical. The CFA opcodes are _deltas_, giving the changes in the saved registers as they happen rather than listing identical values over and over.

The CFA program is in turn stored in two data structures: Any number of Function Data Entries (FDE), each of which represents the CFA program for a single function in the executable, and some number of Common Information Entries (CIE), which define a set of common data for a set of FDEs. An FDE gives the CFA program for a particular range of the instruction pointer (they're indexed by it, rather than by symbol name), and a CIE gives a set of initial CFA instructions for all the FDEs which use it.

Given this trivial x86_64 function (the hex offsets are not accurate):

```
    0x100000000 pushq %rbp
    0x100000001 movq %rsp, %rbp
    0x100000004 subq $16, %rsp
    0x100000008 movl $0, -4(%rbp)           # int a = 0;
    0x10000000F leaq L_.str(%rip), %rdi
    0x100000016 leaq -4(%rbp), %rsi
    0x10000001A xorb %al, %al
    0x10000001C callq _scanf                # scanf("%d", &a);
    0x100000022 movl -4(%rbp), %esi
    0x100000025 leaq L_.str1(%rip), %rdi
    0x10000002C xorb %al, %al
    0x10000002E callq _printf               # printf("%d", a);
    0x100000034 xorl %eax, %eax
    0x100000036 addq $16, %rsp
    0x10000003A popq %rbp
    0x10000003B ret                         # return 0;
```

Assuming that RIP starts at 0x100000000, RSP starts with the value 0x10, and RBP starts with the value 0x00, the raw CFA table for the function looks like this:

```
    RIP              RBP              RSP
    0x100000000      0x00             0x10
    0x100000001      0x10             0x10
    0x100000004      0x10             0x00
    ...              ...              ...
    [10 identical entries omitted]
    ...              ...              ...
    0x100000036      0x10             0x10
    0x10000003A      0x00             0x10
    0x10000003B      0x00             0x10
```

In turn, the compiled DWARF CFA looks like this:

```
    Set RSP as CFA register, with offset of +8.
    Set RIP to *(CFA - 8)
    Advance CFA PC by 1.
    Set RSP as CFA register, with offset of +16.
    Set RBP to *(CFA - 16)
    Advance CFA PC by 3.
    Set RBP as CFA register, with offset of +16.
```

Once a CFA program is run, the state it generates is then applied to the register state. As the CFA register at the end of evaluation is defined to be the stack pointer, we can derive that, at the end of the function:

```
    1. CFA = RBP + 16
    2. RSP = CFA, therefore RSP = RBP + 16
    3. RBP = *(CFA - 16), therefore  RBP = *RBP
    4. RIP = *(CFA - 8), therefore RIP = *(RBP + 8)
```

Or, the stack pointer is restored to its original value, the frame pointer is set to the previous frame pointer, and the program counter is set to the return address on the stack.

Here's what the CFA program looks like when `-fomit-frame-pointer` is used:

```
    Set RSP = CFA + 8
    Set RIP = *(CFA - 8)
    CFA PC += 1
    CFA = RSP + 16
```

Therefore, RSP = RSP + 16 and RIP = *(RSP + 8). The result is the same, just without the frame pointer being saved.

Parsing all of this data isn't complicated. However, it is very, very tedious, especially at async-signal time, which is when a crash handler must be run. Memory can not be allocated at async-signal time, so it's not practical to usefully cache the results of CIE/FDE parsing. What this boils down to is that the entire DWARF information section for a given PC has to be re-parsed for every single function on the call stack.

At this point, you have to be thinking that there must be a better, faster way to store debug information, which doesn't involve having to run the equivelant of a tiny virtual machine with significant saved state. Fortunately, you're right.

**Compact unwind encoding**  
The majority of time spent reading DWARF data is spent in two places: Running the CFA program, and searching the FDEs of an image for the PC being looked up. In the overwhelming majority of cases, all the complexity and verbosity of DWARF information is completely unnecessary for its most common use: Exception frame unwinding. (And, as a bonus, call stack unwinding for crash reporting needs no more information than exception unwinding.)

So was born the compact unwind encoding. To my knowledge (I could find no clear information on the subject, just hints in documentation and headers), the compact encoding was developed by Apple, adopted by LLVM, and later included in GCC.

Compact unwind encoding stores the information necessary to restore saved registers in a two-level lookup table, indexed by the PC of the function being searched. Each entry in the second-level table is a set of compressed register values. A set of register numbers is encoded, and the unwinding code reads the process stack at the appropriate location to get the saved values.

For example, this extremely contrived code:

```
    int     fn(int b, int c, int d, int e, int f, int g)
    {
        int     h = rand(), i = rand(), j = rand(), k = rand();

        return b + c - d * e / f % g + h - i * j / k;
    }

    int     main(int argc, char **argv)
    {
        int     a = 0, b = 0, c = 0, d = 0, e = 0, f = 0, g = 0;

        scanf("%d %d %d %d %d %d %d", &a, &b, &c, &d, &e, &f, &g);
        a = fn(b, c, d, e, f, g);
        printf("%d\n", a);
        return 0;
    }
```

... has the following compact unwind information when compiled normally:

```
    First level index:
        [entry 0] functions beginning above offset 0x00000D78 use entry 0
        [entry 1] functions beginning above offset 0x00000ECD do not exist
    Second level index:
        [entry 0]:
            [encoding 0] functions starting higher than offset 0x0000D78: no unwinding information
            [encoding 1] functions starting higher than offset 0x0000DB4: RBP frame, RBX, R12, R13, R14, R15 saved
            [encoding 2] functions starting higher than offset 0x0000E2C: RBP frame, no registers saved
```

... and when compiled with -fomit-frame-pointer:

```
    First level index:
        [entry 0] functions beginning above offset 0x00000D64 use entry 0
        [entry 1] functions beginning above offset 0x00000EC2 do not exist
    Second level index:
        [entry 0]:
            [encoding 0] functions starting higher than offset 0x0000D64: no unwinding information
            [encoding 1] functions starting higher than offset 0x0000DA0: stack size = 64, RBX, R12, R13, R14, R15, RBP saved
            [encoding 2] functions starting higher than offset 0x0000E2C: stack size = 64, no registers saved
```

**Conclusion**  
Having looked at all the ways to unwind a stack frame, the next step is to extract and use all this information. Unfortunately, it's a topic worthy of an entirely separate article, so I'll be back next week with a detailed look at how to find and use all this data, as well as the thought behind how I implemented it in PLCrashReporter. See you next week!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-04-27-plcrashreporter-and-unwinding-the-stack-with-dwarf.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
