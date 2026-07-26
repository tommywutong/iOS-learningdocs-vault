---
title: 'Friday Q&A 2012-05-04: PLCrashReporter and Unwinding the Stack With DWARF, Part 2'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-05-04-plcrashreporter-and-unwinding-the-stack-with-dwarf-part-2.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:55194055ae60a5c4'
translated: false
---

> 原文：[Friday Q&A 2012-05-04: PLCrashReporter and Unwinding the Stack With DWARF, Part 2](https://www.mikeash.com/pyblog/friday-qa-2012-05-04-plcrashreporter-and-unwinding-the-stack-with-dwarf-part-2.html)　·　mikeash.com Friday Q&A

Posted at 2012-05-04 18:44 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Solving Simulator Bootstrap Errors](https://www.mikeash.com/pyblog/solving-simulator-bootstrap-errors.html)  
Previous article: [Friday Q&A 2012-04-27: PLCrashReporter and Unwinding the Stack With DWARF](https://www.mikeash.com/pyblog/friday-qa-2012-04-27-plcrashreporter-and-unwinding-the-stack-with-dwarf.html)  
Tags: [dangerous](https://www.mikeash.com/pyblog/?tag=dangerous) [debugging](https://www.mikeash.com/pyblog/?tag=debugging) [dwarf](https://www.mikeash.com/pyblog/?tag=dwarf) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [guest](https://www.mikeash.com/pyblog/?tag=guest) [semi-evil](https://www.mikeash.com/pyblog/?tag=semi-evil)

Friday Q&A 2012-05-04: PLCrashReporter and Unwinding the Stack With DWARF, Part 2

by [Gwynne Raskind](http://blog.darkrainfall.org/)

---

**Why not just use one of those things over there?**  
The first thing I did when I took this project on was look for a simple solution. They do exist, in a lot of cases, and they end up unused because no one knew quite there to find them.

The first idea I had was to use Apple's own implementation of `libunwind`. It's built into the system, always available, and does exactly what was needed: providing the addresses of functions on the stack, using all information available. Whoops. Apple's library:

- Has no public API for accessing the stack of any thread other than the current one.
- (not async-signal safe)
- (not async-signal safe)
- Allocates memory (not async-signal safe)
- Has no fallback when compact unwinding, DWARF, and frame pointer walking all fail.
- Doesn't symbolicate.
- Isn't guaranteed to be available before Lion.
- Is licensed under APSL, which made forking it not an option.

So, it was basically completely useless for our purposes. The next thought was the original `libunwind`, [available here](http://www.nongnu.org/libunwind). Whoops again:

- No Darwin support.
- No Mach-O support.
- No compact unwind encoding support.
- No fallback stack scanner.
- Convoluted source code with no documentation on porting or extending.

Also essentially useless for our purposes.

The remaining option was to create my own implementation of a DWARF parser, a compact unwind encoding parser, and a stack scanner. I could have integrated it directly into PLCrashReporter, but the lack of a stack unwinding library in the wild made me think it would be better to write it as entirely independent code. So I popped open Xcode and created a new target, which I called `libtinyunwind`.

**A little API design**  
The idea behind `libtinyunwind` was to be exactly what it said: A nice, small unwinding library that did only as much as was necessary to gather a backtrace after a crash. (It could also potentially be used for exception unwinding, but only if I were to implement the C++ ABI for doing so. Apple's `libunwind` already does that.) Because I was trying to solve the issue on x86_64 only, I also didn't worry too much about making it cross-platform just yet, though I kept it in mind.

I took quite a bit of inspiration from both `PLCrashReporter` and the original `libunwind` when designing the API. First, the public interface to the library. A stack unwinder has to provide:

- Tracking of binary images loaded into (and unloaded from) the active process.
- Derivation of state contexts from any existing thread.
- One-at-a-time in-order iteration of stack frames in a context.
- Access to whatever register data is available in each frame.
- Preferably, symbolication of any returned function addresses.

Based on `PLCrashReporter`'s higher-level implementation, I created the following set of functions. In this discussion, I use the short function and data type names for simplicity and readability, but the real function names and data types are namespaced with a `tinyunw_` prefix.

```
    int set_image_tracking(bool tracking_flag);
    int getcontext(context_t *context);
    int getthreadcontext(context_t *context, thread_t thread);
    int init_cursor(context_t *context, cursor_t *cursor);
    int step(cursor_t *cursor, flags_t flags);
    int get_register(cursor_t *cursor, register_t regnum, word_t *value);
    const char *register_name(register_t regnum);
    int get_symbol_info(word_t ip, word_t *start_addr, const char **name);
```

The `context_t` is a `typedef` around `x86_thread_state64_t`, whereas the `cursor_t` is an opaque structure type. `register_t` is an enum of the available registers on x86_64, and `word_t` is a typedef of `uint64_t`. Making them opaque types will simplify making the library cross-platform at a later date.

Because the code that uses the context and cursor must be async-signal safe, I couldn't simply write `typedef cursor_struct *cursor_t;`. The client code has to be able to allocate context and cursors on its stack, and if the compiler doesn't know the size of the structure, it can't do that. The solution was this somewhat ugly trick:

```
    typedef struct cursor_t {
        uint64_t opaque[120];
    } cursor_t;
```

In fact, the actual cursor structure, defined in an internal header, weighs in at only 352 bytes, not 960, but the extra space allows for 1) future expansion without breaking binary compatibility, and 2) leeway in the actual implementation. Since in the library's intended use case, you would only have one cursor around at any given time, a loss of 608 bytes in a 64-bit address space wasn't particularly worrisome. It is a little bit excessive, but not difficult to adjust as needed.

The public header also defines a set of error codes, in the UNIX style, for the functions to return (again, remember that the real ones have prefixes):

```
    enum {
        ESUCCESS            = 0,            /* no error */
        ENOFRAME            = 1,            /* no more frames to unwind */
        EUNSPEC             = -6540,        /* unknown error */
        ENOMEM              = -6541,        /* out of memory */
        EBADREG             = -6542,        /* bad register number */
        EINVALIDIP          = -6545,        /* invalid IP */
        EBADFRAME           = -6546,        /* bad frame */
        EINVAL              = -6547,        /* unsupported operation or bad value */
        ENOINFO             = -6549,        /* no unwind info available */
    };
```

Most of these codes correspond to the same values in Apple's `libunwind.h` header file, for closer interoperability with those familiar with that library.

There is also a set of flags for the `step()` function:

```
    enum {
        FLAG_NO_DWARF = (1 << 0),
        FLAG_NO_COMPACT = (1 << 1),
        FLAG_NO_STACKSCAN = (1 << 2),
        FLAG_TRY_FRAME_POINTER = (1 << 3),
    };
    typedef int flags_t;
```

This allows the client of the library to control exactly which information gets used during an attempt to step through a stack. This is useful in several cases:

- If a bug is discovered in one of the implementations, that implementation can be shut off without removing the entire library.
- If the client code knows ahead of time what information is and isn't available, or if it just wants faster execution at the expense of accuracy (DWARF is much slower than the other methods), it can avoid what might otherwise be a costly search through the binary's debug information.
- If the client is concerned with accuracy more than the maximum information possible, turning off the stack scanner removes most of the potential for garbage data.
- A client of the library could offer a user (presumably a developer) the option of using only some of the data available so that they could see whether a program had included (or excluded) the desired information.

Here's a very basic example of how to use the API:

```
    int     main(int argc, char **argv)
    {
        /* ... */
        set_image_tracking(true);
        /* ... */
    }

    void    walk_thread_stack(thread_t thread)
    {
        context_t context;
        cursor_t cursor;
        int res = ESUCCESS, n = 0;
        word_t reg = 0, addr = 0;
        const char *name = NULL;

        getthreadcontext(&context, thread);
        init_cursor(&context, &cursor);
        while (true)
        {
            res = step(&cursor, 0);
            if (res == ESUCCESS)
            {
                if (get_register(&cursor, X86_64_RIP, &reg) != ESUCCESS)
                    break;
                if (get_symbol_info(reg, &addr, &name) != ESUCCESS)
                    break;
                printf("Frame %d has IP %p, which is in function %s, starting at address %p\n", n, reg, addr, name);
                continue;
            }
            else if (res == ENOFRAME || res == ENOINFO)
                printf("End of stack.\n");
            else
                printf("Error %d\n", res);
            break;
        }
    }
```

The call to `set_image_tracking()` at the beginning is extremely important; without it, only the stack scanner works, and addresses can't be symbolicated.

**Why do I have to track binary images, anyway?**  
You might wonder why the library doesn't just scan the address space of the process to find the information it needs. Unfortunately, that's just not feasible. There are a lot of gotchas involved in how libraries are loaded into an executable at runtime, so many that it would be a practical impossibility to figure it all out during async-signal time. This means the library has to keep internal track of binary images as they're loaded into and unloaded from a process.

Fortunately, `dyld` provides a nice easy (and more importantly, documented and stable) way to do that: `_dyld_register_func_for_add_image` and `_dyld_register_func_for_remove_image`.

When an image (keep in mind that in this context, "image" means any bit of executable code loaded into a process during runtime, including the executable itself) is loaded, `libtinyunwind` immediately parses it as Mach-O and stores it in an async-safe read-write-locked linked list (implementation courtesy of `PLCrashReporter`, a very nice bit of code on Landon's part!)

Why, you might ask? Because that's how it finds:

- The address of the image's executable code, also known as its TEXT section. Used by all methods.
- and

  sections. Used by the DWARF parser.
- section. Used by the compact unwind parser.
- segment and symbol tables. Used by symbolication.

All of this information could be parsed out at async-signal time, but there's no reason not to parse it as soon as the image is loaded into the process, and there is one advantage to doing it when it's safe to call normal APIs: It can (and does) also call `dladdr()` to get the image's name on disk. It's all very nice to know that someone called a function named `foo`, but was it `foo` in the main application, `foo` in some third-party library, or `foo` in CoreFoundation? (No, there isn't really a `foo` there. :)

Armed with all of this data, `libtinyunwind` can get to the work of actually unwinding a stack.

**Let's put it all in context**  
Step one of unwinding a stack is getting a thread state, also known as a context. This is, in its simplest form, a snapshot of all the CPU registers for the thread you're trying to examine. It can be obtained from the Mach API `thread_get_state` (which is how `getthreadcontext()` works), or retrieved directly in assembly language if you happen to already be executing on the thread in question. For fun, here's the `getcontext()` implementation:

```
    movq    %rax,   (%rdi)
    movq    %rbx,  8(%rdi)
    movq    %rcx, 16(%rdi)
    movq    %rdx, 24(%rdi)
    movq    %rdi, 32(%rdi)
    movq    %rsi, 40(%rdi)
    movq    %rbp, 48(%rdi)
    movq    %rsp, 56(%rdi)
    addq    $8,   56(%rdi)
    movq    %r8,  64(%rdi)
    movq    %r9,  72(%rdi)
    movq    %r10, 80(%rdi)
    movq    %r11, 88(%rdi)
    movq    %r12, 96(%rdi)
    movq    %r13,104(%rdi)
    movq    %r14,112(%rdi)
    movq    %r15,120(%rdi)
    movq    (%rsp),%rsi
    movq    %rsi,128(%rdi) # store return address as rip
    # skip rflags - pushq is unsafe with stack in unknown state, lahf may be unsupported
    # skip cs
    # skip fs
    # skip gs
    xorl    %eax, %eax # return TINYUNW_ESUCCESS
    ret
```

The function has no prologue or epilogue, as that would corrupt the base and stack pointers. The context in which to store the information is pointed to by `rdi` (first integer argument register). The register values are mostly loaded directly into the context. The stack pointer is incremented by 8 (one 64-bit word) to compensate for the saved return address pushed by the `call` to this function. The return address is stored as `rip` in the context structure, obtained by dereferencing the stack pointer per the semantics of `call`. In essence, this function pretends that it is not itself on the stack. The flags register is skipped because there's no safe way to load it at async-signal safe time, and the segment registers are skipped because they're not meaningful in 64-bit code.

There's not really a lot of point to using this in lieu of just calling `thread_get_state()` unless you're concerned about calling as few system APIs as possible. It's also useful on non-Mach-based platforms, where getting at a context state can get a good bit harder.

**Lay back and unwind**  
So, now you have a context, and a cursor with which to iterate it. How does that iteration actually work?

The `step()` function uses the following logic:

1. Is the cursor's `rip` value `NULL`, or does it fall in the predetermined range for the symbols `start` or `thread_start`? If so, immediately return `ENOFRAME`; the top of the stack has been reached.

  The scanner explicitly stops at `start` and `thread_start` because the stack scanner has a tendency to run off the bottom of thread stacks in particular, and because the DWARF and compact unwind encodings do not always encode a foolproof way to detect the bottom of the stack which can be used to avoid trying the stack scanner. One of these symbols is guaranteed to always be at the bottom of any stack, so they're safe stopping points.
2. If the client has not requested that the compact unwind encoding be skipped, try to find a stack frame using it. Return on success or any error; if no compact unwind information exists, continue.
3. If the client has not requested that DWARF not be used, try to find a stack frame that way. Return on success or any error; if no DWARF information exists, continue.
4. If the client has requested a frame pointer scan, try to use `rbp` as a pointer to the next stack frame. Return on success or... well, you get the idea.
5. Finally, if all else has failed, try a stack scan starting from the last valid frame.

Let's examine each method in order.

**Wow, that's compact; can you expand on that?**  
The compact unwind encoding parser first checks whether any image loaded into the process contains the current `rip` value in the cursor's current context. If not, it immediately returns "no info", because if can't even tell where to look. It's not useful to search the unwind table of every image in the process; that's no better for false positives than the stack scanner. It also returns no info if the image it found doesn't have compact unwind information.

The next step is to do the two-level table lookup of the `rip` value, as discussed in part 1. Since both levels of table are ordered ascending, the lookup code does a binary search for the function address. Addresses in the unwind table are stored as offsets from the image's Mach-O header address, so the `rip` value first has that subtracted from it. Assuming a matching entry is found, the second-level table contains the encoding of the function's unwind information.

The compact unwind encoding has five types of actual information encoding:

- and

  interpret it as meaning "no unwind information available".
- handles this by simply returning "no info" and letting the DWARF parser search next.
- is dereferenced to find the new

  ,

  is set to the old

  plus two words (frame pointer and return address), and

  is set to the return address on the stack (

  + 8).
- instruction, which is parsed to get the stack size.

  is set to the old

  , plus the stack size, minus the number of saved registers, plus 8 (the return address).

  is set to the return address on the stack.

And that's it! With `rsp` and `rip` (and when possible, `rbp`) updated, everything necessary to proceed to the next stack frame has been done. Success is returned at this point.

**I'm feeling a little DWARFed by the (virtual) machine**  
If only DWARF parsing were so simple! Unfortunately, it isn't.

The DWARF parser starts off with the same step the compact unwind parser does: Look for the image containing `rip`. No image? No DWARF info? Give up right then and there.

Oh drat, we found something. Now we have to search the debug info section for an Function Data Entry (as [discussed last week](https://www.mikeash.com/pyblog/friday-qa-2012-04-27-plcrashreporter-and-unwinding-the-stack-with-dwarf.html)) matching the function address. This means parsing out the whole thing. We start at the beginning of the section and parse one entry at a time. The algorithim goes like this:

1. Is the next entry an FDE or a CIE? If it's a CIE, skip it. We parse those as part of the FDE. Unfortunately, that means we parse each CIE one time for every single FDE parsed. That's because we're running at async-signal time, and there's nowhere to cache the CIEs we find.
2. It's an FDE? Parse it out, including the CIE. If it contains the function address we're looking for, return it. Otherwise continue onward.

I'm going to interrupt myself here to discuss a bit about how DWARF data is parsed. DWARF is a very interesting data format; it contains a number of different encodings for various information, all of which may end up being used at any given time.

For example, a CIE starts with simple 32-bit and 64-bit and 8-bit numbers. Then it has a C string which describes the "augmentations" for all FDEs that use it. Then it has a couple of "ULEB128" and "SLEB128" numbers. "LEB128" stands for "Little Endian Base-128", which the DWARF standard says is "a scheme for encoding integers densely that exploits the assumption that most integers are small in magnitude." Despite the name, it is not in fact little-endian.

In my own opinion, LEB128 exists mostly to make things more difficult; I think it's more than a little foolish trying to save a couple zero bytes in integer numbers in an encoding that deals with virtual machine opcodes. I can only assume there's some thought behind it that I don't understand.

In any case, the augmentation string in a CIE must be parsed character-by-character to learn certain critical things about the data in associated FDEs. In particular, it gives the size of augmentation data (necessary to correctly parse an FDE) and the encoding of pointer values in the FDE (necessary to even tell whether a function offset is contained by the entry at all). Other information in the CIE gives alignment factors for code and data, points out which column in the virtual CFA table represents the function return address, and gives the actual version of the DWARF data. Versions 1 (a .eh_frame section produced by GCC or Clang) and 3 (DWARF 2 standard) are identical, and are the only ones `libtinyunwind` tries to understand.

The pointer encodings are also a bit fun; a pointer in an FDE can be encoded in no less than 36 different ways (9 numerical representations, ranging from signed and unsigned 8-bit to signed and unsigned 64-bit and including uleb128 and sleb128, several encodings (of which only two are supported) for the "base value" of the pointer, and a flag for indirection of the value).

When all of this is said and done, we end up with (hopefully) an FDE (with included CIE) for the function we're unwinding. Now we have to run the CFA program. This means setting up a virtual machine state, running all instructions in the CIE, then running all instructions in the FDE, halting immediately once the virtual CFA PC passes the current value of `rip` for the function. Running any instructions past this point would result in an incorrect register state, since the actual code that was run never got there!

DWARF has push and pop state instructions. Since we can't allocate memory, a hard size limit on the depth of the virtual stack is imposed. The virtual state is fairly large, so the limit is 8. Fortunately, I've yet to see a DWARF encoding that uses even one, so I think that limit is safe.

The actual opcodes are mostly straightforward. The virtual machine maintains a CFA register number, a CFA register offset, a CFA PC, and a set of register values and locations, encoded by numbers. The machine registers that those numbers correspond to are architecture-specific; `libtinyunwind` maps them onto the x86_64 register set with the obvious switch-case statement. DWARF has opcodes which:

- Do nothing (nop)
- Modify the CFA PC (set to n, advance by 1/2/4/n)
- Modify a register's value (set to n, set to CFA +/- n, set to other register, set undefined, set to result of expression)
- Save and restore the DWARF state (push/pop the virtual stack)
- Set CFA register (set to n, set to n +/- m, set to current +/- m, set to result of expression)
- , as they aren't used on Darwin or in modern code (with one exception; the args_size opcode is parsed but not used).

Once the CFA program has been run, it produces a virtual machine state, a snapshot of the DWARF CFA table at the given `rip`. This state must now be applied to the current register state.

First, the value of the CFA register is determined. The CFA register can be either the value of a particular machine register (before applying any changes) plus or minus an offset, or the result of a DWARF expression. `libtinyunwind` does not currently parse DWARF expressions, as they're very rare in the wild and missing data falls back on the stack scanner; it will be implemented at some point in the furture.

Next, for every register in the virtual state, apply the virtual register value and location to the real register. A register's location can be "unused" (don't change the real one), "CFA value +/- offset" (set the real register to the CFA register's value), "register" (set the real register to the current value of another virtual register), or "expression" (as above, unimplemented).

Finally, update `rip` with the value of the virtual register listed in the CIE as the return address register, and update `rsp` to the value of the CFA register (the CFA register is defined as always being the final value of the stack pointer).

And we're _finally_ done. If an error occurred during _any_ of this, it's immediately returned, and the DWARF parser bails out completely. Recovering from anything going wrong in all that is just not worth the trouble.

**Function to CPU: I was framed!**  
Walking the stack with the frame pointer is by far the simplest method of them all. All it takes is dereferencing the current value of `rbp`, and doing a simple check to make sure it points to somewhere remotely sane in the process stack. There's no way of being entirely certain that it hasn't put you in entirely the wrong place, of course. If you trust it, update `rsp` with the old `rbp` plus 16, update `rip` by dereferencing the old `rbp` + 8, and you're done.

`libtinyunwind`'s frame pointer function currently doesn't exist. Another thing to do in the future, like the DWARF expression evaluator. This is mostly because the frame pointer attempt isn't much better than the stack scanner for functions with stack frames, and it's worse for functions without them.

**Do you see a return address in this stack? Take your time.**  
A stack scanner does work something a bit like a police lineup, in fact; it goes through the stack one pointer-sized word at a time until it finds something that looks like a return address, and uses it.

There's not too much to say about the implementation of the stack scanner in `libtinyunwind`. It just saves off the last place it looked on the stack each time it finds something that looks like a return address, and uses that as its starting point next time it's called. If it doesn't find an address within some arbitrary number of words (50 was the value coded in), it gives up. `rip` is updated with the found address, `rbp` is updated with the next word before it on the stack (a best guess), and that's that.

**You left without even getting the function's name?**  
Once a function has been found on the stack, it's really rather helpful to know just which function it is, and maybe even where inside it the process was at the time. `libtinyunwind` provides a symbolication facility with the aforementioned `get_symbol_info` function. `get_symbol_info` is the _only_ function in `libtinyunwind` that currently works for 32-bit processes.

`get_symbol_info` first checks whether image tracking is turned on, because without it there's nothing to symbolicate with. Next, it does the same thing all the unwinding methods do: Looks for an image that contains the `rip` value being searched. If it can't find an image, or that image doesn't seem to have a symbol table, it gives up.

Next, it searches the image's global and local symbol tables for a matching symbol. A symbol table is stored as a list of starting addresses. This means that if the image has five symbols starting at 0x001, 0x005, 0x009, 0x015, and 0x020, and you ask for a function containing address 0x014, the table has to be searched until both 0x009 and 0x015 are found so that both lower and upper bounds are established. The global table is searched first, then the local table. Both are always searched in their entirety; symbol tables are not guaranteed to be ordered, and the only way to be sure a given result is correct is to make sure every bound has been checked.

When a matching symbol table entry is found, its starting address is read from the entry, and the name is read from the image's string table. A direct, read-only pointer to the name is returned, making the function async-signal safe.

**Memory safety**  
One particular quirk of `libtinyunwind` is that an async-signal safe crash handler, running after something has already gone horribly wrong enough to cause a crash in the first place, may be working with hugely invalid memory addresses. In this situation, any memory you read from could result in a crash, and crashing in a crash handler either deadlocks the process (as the UNIX signal remains blocked even though the signal handler can't continue executing) or just causes immediate termination. Either way, you've lost the crash data you were so interested in gathering.

Fortunately, you can read process memory in a way that simply returns an error if you access an invalid address, instead of setting off a fresh `EXC_BAD_ACCESS`. I have to credit Landon for this one as well, as it's another bit I copied from `PLCrashReporter` itself. The key is the [`vm_read_overwrite()`](http://web.mit.edu/darwin/src/modules/xnu/osfmk/man/vm_read.html) function. I do not know exactly how it works, and I certainly don't understand why it's named the way it is, but it reads process memory without crashing the process on invalid access, and that's the important part. `libtinyunwind` uses it all over the place so it can fail gracefully when memory's too corrupted to do anything with.

**Conclusion**  
That just about wraps up my discussion of stack unwinding. As you've seen during my commentary, there are some pieces still missing from `libtinyunwind`, most importantly multi-architecture support, but they won't be missing forever. I had a whole lot of fun with this project, and I'm very grateful to have had the opportunity to do it; I intend to continue. The code is licensed under the same terms as `PLCrashReporter` itself; I hope there will be a release fairly soon. I'll be back with another Friday Q&A after Mike's next articles. Until then, happy coding!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
