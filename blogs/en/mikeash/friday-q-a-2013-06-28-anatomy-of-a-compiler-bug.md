---
title: 'Friday Q&A 2013-06-28: Anatomy of a Compiler Bug'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-06-28-anatomy-of-a-compiler-bug.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:fb8208e5ac640c7a'
translated: false
---

> 原文：[Friday Q&A 2013-06-28: Anatomy of a Compiler Bug](https://www.mikeash.com/pyblog/friday-qa-2013-06-28-anatomy-of-a-compiler-bug.html)　·　mikeash.com Friday Q&A

Posted at 2013-06-28 13:04 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2013-08-02: Type-Safe Scalars with Single-Field Structs](https://www.mikeash.com/pyblog/friday-qa-2013-08-02-type-safe-scalars-with-single-field-structs.html)  
Previous article: [Friday Q&A 2013-06-14: Reachability](https://www.mikeash.com/pyblog/friday-qa-2013-06-14-reachability.html)  
Tags: [assembly](https://www.mikeash.com/pyblog/?tag=assembly) [compiler](https://www.mikeash.com/pyblog/?tag=compiler) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2013-06-28: Anatomy of a Compiler Bug

by [Mike Ash](https://www.mikeash.com/)

**Bug Context**  
The bug in question is a code generation bug in clang. The bug existed in the version of clang that shipped with Xcode 4.4.1, and it has since been fixed. The demo code for this article was built with the clang in 4.4.1.

Additionally, the bug only causes ill effects when calling into code compiled with gcc! When clang code calls other clang code, the bug is harmless. Interesting things only happen if the callee was built with gcc.

Daniel originally discovered the bug when building with clang and deploying onto Mac OS X 10.6, where the frameworks were still built with gcc. Since it's annoying to boot back into 10.6, I'm building some demo code using a locally-built copy of gcc 4.2.

In short, you have nothing to fear from this bug. It's extremely hard to trigger, and has been fixed for quite a while. However, it is utterly _fascinating_.

**Demo Code**  
Because the bug requires code built with two compilers, the demo code is split into two files.

The first is a class that will be compiled with gcc. This is a quick wrapper around`-[NSString initWithFormat:arguments:]`. In the original bug case, it was `+[NSString stringWithFormat:]` that encountered the bug, and this is an easy way to replicate the situation:

```
    @implementation GCCClass

    + (NSString *)format: (NSString *)format, ...
    {
        va_list args;
        va_start(args, format);

        NSString *str = [[NSString alloc] initWithFormat: format arguments: args];

        va_end(args);

        return str;
    }

    @end
```

There is a corresponding clang class. It contains a test method, which calls another method that exercises the `+format:` method above:

```
    @implementation ClangClass

    + (void)test
    {
        fprintf(stderr, "Testing\n");
        NSString *str = [ClangClass formattedTimeStringForSeconds: 1];
        fprintf(stderr, "Result is %s\n", [str UTF8String]);
    }

    + (NSString *)formattedTimeStringForSeconds:(int)timeInSeconds
    {
        NSUInteger HOURS = 3600;
        NSUInteger MINUTES = 60;

        NSUInteger minutes = (timeInSeconds % HOURS) / MINUTES;

        return [GCCClass format: @"%lu", minutes];
    }

    @end
```

Finally, there is a quick `main` function to exercise all of this. It doesn't much matter, but I built it with clang:

```
    int main (void)
    {
        @autoreleasepool
        {
            [ClangClass test];
        }

        return 0;
    }
```

First, let's build both files using a recent clang and see what it does:

```
    $ clang -framework Foundation *.m
    $ ./a.out 
    Testing
    Result is 0
    Formatted time string is: 0
```

It behaves as expected. Now let's build the files using gcc and the buggy version of clang. I built a quick shell script to hide the ugly details, since the paths to the specific versions are long and obscure:

```
    $ cat build.sh 
    ~/Development/gcc-5666.3/build/dst/usr/bin/gcc-4.2 -c -O3 -g gcc.m
    /Applications/Xcode441/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -c -O3 -g clang.m

    clang -framework Foundation clang.o gcc.o
    MikeAir:~/shell/vararg-bug mikeash$ ./build.sh 
    MikeAir:~/shell/vararg-bug mikeash$ ./a.out 
    Testing
    Testing
    Testing
    Testing
    Testing
    Testing
    Testing
    Testing
    Testing
    Testing
```

I'll skip over about thirty thousand lines of mostly identical output here, in the interests of sanity. There are occasional partial lines like this:

```
    Testing
    sting
    Testing
```

Or:

```
    Testing
    g
    Testing
```

It eventually terminates with:

```
    Testing
    Testing
    Testing
    Testing
    Testing
    Testing
    Segmentation fault: 11
```

Well... that's not right.

**Initial Debugging**  
Let's fire up the debugger and see where it's crashing:

```
    (lldb) run
    Process 4663 launched: '/Users/mikeash/Dropbox/shell/vararg-bug/a.out' (x86_64)
```

I'll skip over the mountain of output from the program. The debugger eventually stops it:

```
    Process 4663 stopped
    * thread #1: tid = 0x1c03, 0x00007fff910d8220 libsystem_c.dylib`__sfvwrite + 8, stop reason = EXC_BAD_ACCESS (code=2, address=0x7fff5f3ffff8)
        frame #0: 0x00007fff910d8220 libsystem_c.dylib`__sfvwrite + 8
    libsystem_c.dylib`__sfvwrite + 8:
    -> 0x7fff910d8220:  pushq  %r13
    0x7fff910d8222:  pushq  %r12
    0x7fff910d8224:  pushq  %rbx
    0x7fff910d8225:  subq   $40, %rsp
```

It's crashing somewhere in `__sfvwrite`. I assume that's being called from `fprintf`. Let's get a backtrace:

```
    (lldb) bt
    * thread #1: tid = 0x1c03, 0x00007fff910d8220 libsystem_c.dylib`__sfvwrite + 8, stop reason = EXC_BAD_ACCESS (code=2, address=0x7fff5f3ffff8)
        frame #0: 0x00007fff910d8220 libsystem_c.dylib`__sfvwrite + 8
        frame #1: 0x00007fff910d8861 libsystem_c.dylib`fwrite + 114
        frame #2: 0x0000000100000be7 a.out`+[ClangClass test] + 39 at clang.m:12
```

No sign of `fprintf`, but it looks like the compiler has just optimized it into a call to `fwrite`, since it's printing a constant string.

This doesn't explain why the code apparently loops endlessly. It actually looks like endless recursion, since it's crashing on a `pushq` instruction, presumably due to overflowing the stack.

Let's re-run the program with a breakpoint on `fwrite`, stopping after the a few calls to see what it looks like in the middle of the loop or recursion or whatever is going on. First, set the breakpoint:

```
    (lldb) b fwrite
    warning: (x86_64) /usr/lib/libstdc++.6.dylib empty dSYM file detected, dSYM was created with an executable with no debug info.
    Breakpoint 1: where = libsystem_c.dylib`fwrite, address = 0x000000000007f7ef
```

Now tell lldb to ignore the breakpoint the first ten times it's hit:

```
    (lldb) breakpoint modify -i 10
```

Then run the program again:

```
    (lldb) run
    Process 4795 launched: '/Users/mikeash/Dropbox/shell/vararg-bug/a.out' (x86_64)
    Testing
    Testing
    Testing
    Testing
    Testing
    Testing
    Testing
    Testing
    Testing
    Testing
    Process 4795 stopped
    * thread #1: tid = 0x1c03, 0x00007fff910d87ef libsystem_c.dylib`fwrite, stop reason = breakpoint 1.1
        frame #0: 0x00007fff910d87ef libsystem_c.dylib`fwrite
    libsystem_c.dylib`fwrite:
    -> 0x7fff910d87ef:  pushq  %rbp
    0x7fff910d87f0:  movq   %rsp, %rbp
    0x7fff910d87f3:  pushq  %r15
    0x7fff910d87f5:  pushq  %r14
```

Let's see if the backtrace is more informative:

```
    (lldb) bt
    * thread #1: tid = 0x1c03, 0x00007fff910d87ef libsystem_c.dylib`fwrite, stop reason = breakpoint 1.1
        frame #0: 0x00007fff910d87ef libsystem_c.dylib`fwrite
        frame #1: 0x0000000100000be7 a.out`+[ClangClass test]() + 39 at clang.m:12
```

Nope! Let's back up and see if the very first call makes sense:

```
    (lldb) run
    There is a running process, kill it and restart?: [Y/n] y
    Process 4807 launched: '/Users/mikeash/Dropbox/shell/vararg-bug/a.out' (x86_64)
    Process 4807 stopped
    * thread #1: tid = 0x1c03, 0x00007fff910d87ef libsystem_c.dylib`fwrite, stop reason = breakpoint 1.1
        frame #0: 0x00007fff910d87ef libsystem_c.dylib`fwrite
    libsystem_c.dylib`fwrite:
    -> 0x7fff910d87ef:  pushq  %rbp
    0x7fff910d87f0:  movq   %rsp, %rbp
    0x7fff910d87f3:  pushq  %r15
    0x7fff910d87f5:  pushq  %r14
    (lldb) bt
    * thread #1: tid = 0x1c03, 0x00007fff910d87ef libsystem_c.dylib`fwrite, stop reason = breakpoint 1.1
        frame #0: 0x00007fff910d87ef libsystem_c.dylib`fwrite
        frame #1: 0x0000000100000be7 a.out`+[ClangClass test]() + 39 at clang.m:12
        frame #2: 0x0000000100000cb2 a.out`main + 34 at clang.m:33
        frame #3: 0x00007fff8c7b77e1 libdyld.dylib`start + 1
```

Finally, sanity! Everything is as it should be on the first call. Let's see what the second call looks like:

```
    (lldb) cont
    Process 4807 resuming
    Testing
    Process 4807 stopped
    * thread #1: tid = 0x1c03, 0x00007fff910d87ef libsystem_c.dylib`fwrite, stop reason = breakpoint 1.1
        frame #0: 0x00007fff910d87ef libsystem_c.dylib`fwrite
    libsystem_c.dylib`fwrite:
    -> 0x7fff910d87ef:  pushq  %rbp
    0x7fff910d87f0:  movq   %rsp, %rbp
    0x7fff910d87f3:  pushq  %r15
    0x7fff910d87f5:  pushq  %r14
    (lldb) bt
    * thread #1: tid = 0x1c03, 0x00007fff910d87ef libsystem_c.dylib`fwrite, stop reason = breakpoint 1.1
        frame #0: 0x00007fff910d87ef libsystem_c.dylib`fwrite
        frame #1: 0x0000000100000be7 a.out`+[ClangClass test]() + 39 at clang.m:12
        frame #2: 0x00007fff8c5be240 libobjc.A.dylib`_cache_getImp + 76
        frame #3: 0x0000000100000c04 a.out`+[ClangClass test]() + 68 at clang.m:13
        frame #4: 0x0000000100000cb2 a.out`main + 34 at clang.m:33
        frame #5: 0x00007fff8c7b77e1 libdyld.dylib`start + 1
```

`clang.m:13` is this line:

```
    NSString *str = [ClangClass formattedTimeStringForSeconds: 1];
```

According to this backtrace, which is highly suspect, this call invokes `_cache_getImp`, which is part of the `objc_msgSend` machinery. That call then somehow invokes `+test` again, even though that should be impossible.

Let's continue for one more call and see how things look from there:

```
    (lldb) cont
    Process 4807 resuming
    (lldb) Testing
    Process 4807 stopped
    * thread #1: tid = 0x1c03, 0x00007fff910d87ef libsystem_c.dylib`fwrite, stop reason = breakpoint 1.1
        frame #0: 0x00007fff910d87ef libsystem_c.dylib`fwrite
    libsystem_c.dylib`fwrite:
    -> 0x7fff910d87ef:  pushq  %rbp
    0x7fff910d87f0:  movq   %rsp, %rbp
    0x7fff910d87f3:  pushq  %r15
    0x7fff910d87f5:  pushq  %r14
    (lldb) bt
    * thread #1: tid = 0x1c03, 0x00007fff910d87ef libsystem_c.dylib`fwrite, stop reason = breakpoint 1.1
        frame #0: 0x00007fff910d87ef libsystem_c.dylib`fwrite
        frame #1: 0x0000000100000be7 a.out`+[ClangClass test]() + 39 at clang.m:12
```

Now the stack trace is getting cut off. Between the stack disappearing here and the impossible call from `_cache_getImp` to `+test` above, it looks like something is seriously corrupting the stack.

It looks like the interval between the first and second calls isn't very large, so let's start over, then step through line by line to see exactly how it gets there. I'm going to trim the output from lldb a bit, since it wants to dump a bunch of context from the source code whenever it reaches a new line:

```
    (lldb) run
    There is a running process, kill it and restart?: [Y/n] y
    Process 4905 launched: '/Users/mikeash/Dropbox/shell/vararg-bug/a.out' (x86_64)
    Process 4905 stopped
    * thread #1: tid = 0x1c03, 0x00007fff910d87ef libsystem_c.dylib`fwrite, stop reason = breakpoint 1.1
        frame #0: 0x00007fff910d87ef libsystem_c.dylib`fwrite
    libsystem_c.dylib`fwrite:
    -> 0x7fff910d87ef:  pushq  %rbp
    0x7fff910d87f0:  movq   %rsp, %rbp
    0x7fff910d87f3:  pushq  %r15
    0x7fff910d87f5:  pushq  %r14
    (lldb) finish
    Testing
    -> 13          NSString *str = [ClangClass formattedTimeStringForSeconds: 1];
```

So far so good. It steps out of `fwrite`, and the next line is what we expect.

```
    (lldb) step
    -> 22          NSUInteger minutes = (timeInSeconds % HOURS) / MINUTES;
```

This is the first real line of code in the `formattedTimeStringForSeconds:` method, so this is sensible.

```
    (lldb) step
    -> 24          return [GCCClass format: @"%lu", minutes];
```

This is the next line, still to be expected.

```
    (lldb) step
    -> 22          NSUInteger minutes = (timeInSeconds % HOURS) / MINUTES;
```

This is a little odd, as it's moving backwards. However, it's not uncommon in optimized code, where the generated assembly language can be organized pretty differently from the original code.

```
    (lldb) step
    -> 24          return [GCCClass format: @"%lu", minutes];
    (lldb) step
    -> 24          return [GCCClass format: @"%lu", minutes];
```

Back to this line, twice. More optimizations confusing the debugger, apparently.

```
    (lldb) step
    libsystem_c.dylib`fwrite:
    -> 0x7fff910d87ef:  pushq  %rbp
```

And just like that, we're back in `fwrite`. I didn't delete any steps in between. This is what actually happened! One moment, it's calling `+[GCCClass format:]`, the next moment it's in `fwrite`.

**Assembly-Level Debugging**  
Since source-level debugging wasn't very informative, let's try it again, but step one instruction at a time rather than one line at a time. That will help avoid the troubling influence of optimizations, and might show something about what's happening between these last two steps. First, I re-run the program and let it stop in `fwrite`. I then tell lldb to print a disassembly for the current PC every time the program stops, so I don't have to do it manually:

```
    (lldb) target stop-hook add
    Enter your stop hook command(s).  Type 'DONE' to end.
    > disassemble --pc
    > DONE
    Stop hook #1 added.
```

I step out of `fwrite` and it shows me both source and disassembly:

```
    (lldb) finish
    Testing
    Process 6147 stopped
    -> 13          NSString *str = [ClangClass formattedTimeStringForSeconds: 1];
    -> 0x100000be7:  movq   1514(%rip), %rsi          ; "formattedTimeStringForSeconds:"
```

Looks good. Let's work through one instruction at a time:

```
    (lldb) si
    -> 13          NSString *str = [ClangClass formattedTimeStringForSeconds: 1];
    -> 0x100000bee:  movq   1579(%rip), %rdi          ; (void *)0x0000000100001238: ClangClass
    (lldb) si
    -> 13          NSString *str = [ClangClass formattedTimeStringForSeconds: 1];
    -> 0x100000bf5:  movq   1052(%rip), %r14          ; (void *)0x00007fff8c5be240: objc_msgSend
    (lldb) si
    -> 13          NSString *str = [ClangClass formattedTimeStringForSeconds: 1];
    -> 0x100000bfc:  movl   $1, %edx
    (lldb) si
    -> 13          NSString *str = [ClangClass formattedTimeStringForSeconds: 1];
    -> 0x100000c01:  callq  *%r14
    (lldb) si
    libobjc.A.dylib`objc_msgSend:
    -> 0x7fff8c5be240:  testq  %rdi, %rdi
```

Everything looks good here. It sets up the call, then calls `objc_msgSend` to make the `formattedTimeStringForSeconds:` call. That call is uninteresting, so let's skip directly to the method it eventually invokes:

```
    -> 22          NSUInteger minutes = (timeInSeconds % HOURS) / MINUTES;
    -> 0x100000c34:  movslq %edx, %rcx
```

Let's keep going:

```
    (lldb) si
    -> 22          NSUInteger minutes = (timeInSeconds % HOURS) / MINUTES;
    -> 0x100000c37:  movq   %rcx, %rax
    (lldb) si
    -> 22          NSUInteger minutes = (timeInSeconds % HOURS) / MINUTES;
    -> 0x100000c3a:  shrq   $4, %rax
    (lldb) si
    -> 22          NSUInteger minutes = (timeInSeconds % HOURS) / MINUTES;
    -> 0x100000c3e:  movabsq$655884233731895169, %rdx
    (lldb) si
    -> 22          NSUInteger minutes = (timeInSeconds % HOURS) / MINUTES;
    -> 0x100000c48:  mulq   %rdx
    (lldb) si
    -> 22          NSUInteger minutes = (timeInSeconds % HOURS) / MINUTES;
    -> 0x100000c4b:  shrq   $3, %rdx
    (lldb) si
    -> 22          NSUInteger minutes = (timeInSeconds % HOURS) / MINUTES;
    -> 0x100000c4f:  imulq  $3600, %rdx, %rax
    (lldb) si
    -> 22          NSUInteger minutes = (timeInSeconds % HOURS) / MINUTES;
    -> 0x100000c56:  subq   %rax, %rcx
```

There's some weird stuff going on here, as clang has optimized the calculation into something pretty far removed from the original mod/divide code. But nothing is wrong with this, it's just optimized code.

```
    (lldb) si
    -> 24          return [GCCClass format: @"%lu", minutes];
    -> 0x100000c59:  movq   1416(%rip), %rsi          ; "format:"
    (lldb) si
    -> 24          return [GCCClass format: @"%lu", minutes];
    -> 0x100000c60:  movq   1473(%rip), %rdi          ; (void *)0x00000001000012b0: GCCClass
    (lldb) si
    -> 24          return [GCCClass format: @"%lu", minutes];
    -> 0x100000c67:  leaq   1642(%rip), %r8           ; @"%lu"
    (lldb) si
    -> 24          return [GCCClass format: @"%lu", minutes];
    -> 0x100000c6e:  movabsq$-8608480567731124087, %rdx
    (lldb) si
    -> 22          NSUInteger minutes = (timeInSeconds % HOURS) / MINUTES;
    -> 0x100000c78:  movq   %rcx, %rax
    (lldb) si
    -> 22          NSUInteger minutes = (timeInSeconds % HOURS) / MINUTES;
    -> 0x100000c7b:  mulq   %rdx
    (lldb) si
    -> 22          NSUInteger minutes = (timeInSeconds % HOURS) / MINUTES;
    -> 0x100000c7e:  movq   %rdx, %rcx
    (lldb) si
    -> 22          NSUInteger minutes = (timeInSeconds % HOURS) / MINUTES;
    -> 0x100000c81:  shrq   $5, %rcx
    (lldb) si
    -> 24          return [GCCClass format: @"%lu", minutes];
    -> 0x100000c85:  movq   %r8, %rdx
    (lldb) si
    -> 24          return [GCCClass format: @"%lu", minutes];
    -> 0x100000c88:  popq   %rbp
    (lldb) si
    -> 24          return [GCCClass format: @"%lu", minutes];
    -> 0x100000c89:  jmpq   *905(%rip)                ; (void *)0x00007fff8c5be240: objc_msgSend
    (lldb) si
    libobjc.A.dylib`objc_msgSend:
    -> 0x7fff8c5be240:  testq  %rdi, %rdi
```

It makes it to `objc_msgSend` again. Let's skip over that and stop in `+format:`

```
    (lldb) b +[GCCClass format:]
    Breakpoint 3: where = a.out`+[GCCClass format:] + 97 at gcc.m:45, address = 0x0000000100000d31
    (lldb) cont
    Process 6147 resuming
    Process 6147 stopped
    * thread #1: tid = 0x1c03, 0x00007fff910d87ef libsystem_c.dylib`fwrite, stop reason = breakpoint 1.1
        frame #0: 0x00007fff910d87ef libsystem_c.dylib`fwrite
    libsystem_c.dylib`fwrite:
    -> 0x7fff910d87ef:  pushq  %rbp
```

Whoops, it never even makes it to the breakpoint. Right back to `fwrite`. While extremely weird, this at least narrows the field considerably. Whatever ends up calling `fwrite` again, it's either in `objc_msgSend`, or it's very early in `+format:`. Note how lldb puts the breakpoint well into the actual code for `+format:`, at offset 97. Let's see if it gets into `+format:` at all by putting a breakpoint on the very first instruction:

```
    (lldb) p (void *)[NSClassFromString(@"GCCClass") methodForSelector:@selector(format:)]
    (void *) $0 = 0x0000000100000cd0
    (lldb) b 0x0000000100000cd0
    Breakpoint 4: where = a.out`+[GCCClass format:] at gcc.m:43, address = 0x0000000100000cd0
```

Now re-run the program:

```
    (lldb) cont
    Process 9370 resuming
    Testing
    Process 9370 stopped
    -> 43      {
    -> 0x100000cd0:  pushq  %rbp
```

It works! Execution reaches the beginning of `+format:`. Whatever causes the second call to `fwrite`, it's in the prolog of `+format:`.

Let's step through:

```
    (lldb) si
    -> 43      {
    -> 0x100000cd1:  movq   %rsp, %rbp
    (lldb) si
    -> 43      {
    -> 0x100000cd4:  pushq  %r12
    (lldb) si
    -> 43      {
    -> 0x100000cd6:  pushq  %rbx
    (lldb) si
    -> 43      {
    -> 0x100000cd7:  subq   $208, %rsp
    (lldb) si
    -> 43      {
    -> 0x100000cde:  movq   %rcx, -168(%rbp)
    (lldb) si
    -> 43      {
    -> 0x100000ce5:  movq   %r8, -160(%rbp)
    (lldb) si
    -> 43      {
    -> 0x100000cec:  movq   %r9, -152(%rbp)
```

This is all pretty standard function prolog stuff here.

```
    (lldb) si
    -> 43      {
    -> 0x100000cf3:  movzbl %al, %ecx
    (lldb) si
    -> 43      {
    -> 0x100000cf6:  leaq   (,%rcx,4), %rax
    (lldb) si
    -> 43      {
    -> 0x100000cfe:  leaq   41(%rip), %rcx            ; +[GCCClass format:] + 94 at gcc.m:43
    (lldb) si
    -> 43      {
    -> 0x100000d05:  subq   %rax, %rcx
    (lldb) si
    -> 43      {
    -> 0x100000d08:  leaq   -17(%rbp), %rax
    (lldb) si
    -> 43      {
    -> 0x100000d0c:  jmpq   *%rcx
```

This is a bit odd. The code calculates some sort of address and then jumps to it. Let's see where it goes:

```
    (lldb) si
    a.out`_mh_execute_header + 2826:
    -> 0x100000b0a:  addb   %al, (%rax)
```

Well, _that_ is most certainly not right. `_mh_execute_header` isn't even a real symbol, it's just a dummy that indicates the beginning of a section of the executable. And the instruction, `addb %al, (%rax)`, is actually just what you get when you interpret zero bytes as x86 instructions. In short, we've jumped somewhere in a field of zeroes that happens to be executable. Let's keep stepping and see where it goes.

The field of zeroes continues on for quite some time. The zero instructions are legal, and so the CPU keeps executing them. Finally, after stepping through a lot of these instructions, it begins to approach the end:

```
    (lldb) si
    Process 9370 stopped
    * thread #1: tid = 0x1c03, 0x0000000100000bba a.out`_mh_execute_header + 3002, stop reason = instruction step into
        frame #0: 0x0000000100000bba a.out`_mh_execute_header + 3002
    a.out`_mh_execute_header + 3002:
    -> 0x100000bba:  addb   %al, (%rax)
    0x100000bbc:  addb   %al, (%rax)
    0x100000bbe:  addb   %al, (%rax)

    a.out`+[ClangClass test] + 3008 at clang.m:10:
    0x100000bc0:  pushq  %rbp
```

Well, look at that! The code for `+test` immediately follows this field of executable zero bytes. If we keep stepping, we'll go right back into `+test`:

```
    (lldb) si
    -> 0x100000bbc:  addb   %al, (%rax)
    (lldb) si
    -> 0x100000bbe:  addb   %al, (%rax)
    (lldb) si
    -> 10      + (void)test
    -> 0x100000bc0:  pushq  %rbp
```

And if we keep going, we'll get to the `fwrite` call again.

Here's a summary of what we know so far:

1. .
2. The prolog computes an address and jumps to it.
3. That address ends up being in the middle of a field of executable zero bytes before the program's code.
4. The CPU executes these zero bytes repeatedly until it reaches the program's code again, at which point it starts to execute that.
5. is the first piece of code in the app, it runs again.
6. Because this is triggered from a function prolog, the stack is not entirely set up. This results in something that's kind of halfway between a loop and a recursive call, and explains the messed up stack we saw before.

The question is: what exactly is that computed jump in the prolog of `+[GCCClass format:]`, and why does it end up flying off into hyperspace?

**Dissecting the Prolog**  
The first part of the prolog is pretty routine, it just creates a new stack frame and saves the integer registers that might contain variable arguments. I'll skip over that part.

Here's the part of the prolog that involves the computed jump:

```
    movzbl %al, %ecx
    leaq (,%rcx,4), %rax
    leaq 41(%rip), %rcx
    subq %rax, %rcx
    leaq -17(%rbp), %rax
    jmpq *%rcx
    movaps %xmm7, -15(%rax)
    movaps %xmm6, -31(%rax)
    movaps %xmm5, -47(%rax)
    movaps %xmm4, -63(%rax)
    movaps %xmm3, -79(%rax)
    movaps %xmm2, -95(%rax)
    movaps %xmm1, -111(%rax)
    movaps %xmm0, -127(%rax)
```

Let's take this line by line. This is the first instruction:

```
    movzbl %al, %ecx
```

This moves the contents of the `%al` register into `%ecx`. This is a confusing part of the `x86-64` instruction set, as there are sixteen 64-bit general-purpose integer registers, but there are also some pseudo-registers that map to pieces of those. The `%al` register maps to the low eight bits of the 64-bit `%rax` register, and `%ecx` maps to the low 32 bits of `%rcx`. To add even more confusion, when the destination register is `%ecx`, the instruction zeroes the top `32` bits of `%rcx`. In short, this basically computes:

```
    %rcx = %rax & 0xff;
```

Just what is in the `%al` register at this point? It's not referenced earlier in the prolog, not as `%al`, `%rax`, `%eax`, or `%ax`. It must come from the caller. Let's consult the [`x86-64` ABI](http://www.uclibc.org/docs/psABI-x86_64.pdf). A quick search for "%al" turns up the relevant section:

> For calls that may call functions that use varargs or stdargs (prototype-less calls or calls to functions containing ellipsis (...) in the declaration) `%al` is used as hidden argument to specify the number of SSE registers used. The contents of %al do not need to match exactly the number of registers, but must be an upper bound on the number of SSE registers used and is in the range 0-8 inclusive.

SSE registers are used to pass variable arguments of floating-point type. The `%al` register therefore contains the number of floating-point variable arguments passed into the function (excluding any beyond eight that get passed on the stack). Optionally, the caller can lie and pass in a number that's larger than the actual value at the expense of some efficiency, as long as it's still in the range 0-8.

In short, the `%rcx` register now contains the number of floating-point registers used to pass variable arguments.

```
    leaq (,%rcx,4), %rax
```

The `leaq` instruction is an odd beast. Intel processors can interpret fairly complicated memory references in machine instructions. The `lea` family of instructions lets you use that ability without actually loading the target memory. It gives you access to a somewhat simplified arithmetic unit that can be faster than using the more obvious arithmetic instructions. In this case, it computes `%rcx * 4` and places the result into `%rax`. The `%rax` register now contains the number of floating-point registers used, multiplied by four.

```
    leaq 41(%rip), %rcx
```

The `%rip` register is the current instruction pointer, and this just adds `41` to it and stores the value in `%rcx`. The instruction that's `41` bytes past this instruction is the instruction right after the sequence of `movaps` instructions, so `%rcx` now contains the address of the instruction at the end of that `movaps` sequence.

```
    subq %rax, %rcx
```

This instruction is equivalent to:

```
    %rcx -= %rax;
```

`%rcx` currently contains the address past the end of the `movaps` instructions. `%rax` contains the number of floating-point registers used, multiplied by four. And, surprise surprise, these `movaps` instructions are four bytes each. Things are starting to become clear. After this subtraction, `%rcx` points to the `movaps` instruction corresponding to the number of floating-point registers used. If four registers are used, it points to the `movaps` instruction for `%xmm3`. If one register is used, it points to the `movaps` instruction for `%xmm0`. If no registers are used, it points past all of the `movaps` instructions.

```
    leaq -17(%rbp), %rax
```

This computes an address relative to the frame pointer, which is used as part of the address computation in the `movaps` instructions. The specific values aren't too important for us here.

```
    jmpq *%rcx
```

Here's where the magic happens. The previous code computed the address of one of the `movaps` instructions, and this instruction then jumps to it. It'll end up somewhere in here:

```
    movaps %xmm7, -15(%rax)
    movaps %xmm6, -31(%rax)
    movaps %xmm5, -47(%rax)
    movaps %xmm4, -63(%rax)
    movaps %xmm3, -79(%rax)
    movaps %xmm2, -95(%rax)
    movaps %xmm1, -111(%rax)
    movaps %xmm0, -127(%rax)
```

And wherever it ends up, it'll execute that instruction and all of the subsequent ones. It's essentially equivalent to this C pseudo-code:

```
    switch(%al)
    {
        case 8:
            save_xmm7();
        case 7:
            save_xmm6();
        case 6:
            save_xmm5();
        case 5:
            save_xmm4();
        case 4:
            save_xmm3();
        case 3:
            save_xmm2();
        case 2:
            save_xmm1();
        case 1:
            save_xmm0();
    }
```

Making liberal use of fallthrough so that when `%al` contains, for example, four, it saves `%xmm3` _and_ `%xmm0-2`. It's a clever bit of efficient code that saves exactly the registers needed.

**Dissecting the Jump**  
Since the `%al` register can only contain nine possible values in this scenario, there are only nine possible places where this jump instruction can go, and all of them make sense. How, then, is it ending up off in hyperspace when we run this program?

Let's run the program in the debugger and stop right before all this computation, and see what's going on:

```
    (lldb) b 0x0000000100000cf3
    Breakpoint 1: address = 0x0000000100000cf3
    (lldb) run
    -> 0x100000cf3:  movzbl %al, %ecx
```

Let's see what the caller put in `%al`:

```
    (lldb) p $al
    (unsigned char) $0 = '\x89'
```

Well, that's not right. The ABI clearly specifies that `%al` must contain a number from 0 to 8, but it contains `137`!

Running `137` through the rest of the computation reveals the cause of the hyperspace jump. It multiplies `137` by `4`, yielding `548`. It subtracts that number from the address at the end of the `movaps` sequence, yielding an address `548` bytes earlier in the code. It then blindly jumps to that address.

There is one crucial difference between this assembly code and the C pseudo-code `switch` I showed above: C will do bounds checking on your `switch` value, while the assembly code does not. There's nothing wrong with not doing any bounds checking here, because `%al` is not allowed to contain any values out of range. The fault lies with the caller.

**Dissecting the Caller**  
Here's the disassembly of the calling code:

```
    +[ClangClass formattedTimeStringForSeconds:]:
    pushq %rbp
    movq %rsp, %rbp
    movslq %edx, %rcx
    movq %rcx, %rax
    shrq $4, %rax
    movabsq $655884233731895169, %rdx
    mulq %rdx
    shrq $3, %rdx
    imulq $3600, %rdx, %rax
    subq %rax, %rcx
    movq 1416(%rip), %rsi
    movq 1473(%rip), %rdi
    leaq 1642(%rip), %r8
    movabsq $-8608480567731124087, %rdx
    movq %rcx, %rax
    mulq %rdx
    movq %rdx, %rcx
    shrq $5, %rcx
    movq %r8, %rdx
    popq %rbp
    jmpq *905(%rip)
```

It's not obvious, but the last instruction to affect the value of `%al` is the `mulq %rdx` instruction near the end. Although it's not explicitly shown as an operand in the instruction, the `mulq` instruction uses `%rax` as an accumulator. That particular instruction performs:

```
    tmp = %rax * %rdx;
    %rax = low_half(tmp)
    %rdx = high_half(tmp)
```

This code only uses the value in `%rdx`, but the value in `%rax` lives on until it's read out as `%al` in the next bit of code.

The problem is fundamentally a failure to zero out the `%rax` register, or at least the `%al` chunk of it, before making the call to `+format:`. Clang's optimizer got a little too aggressive here and decided that the code to zero it out was unnecessary, even though that's not the case. Building with a more recent clang produces code like the above, but with an extra instruction just before the call at the end:

```
    xorb %al, %al
```

This zeroes out `%al` by XORing it with itself, restoring correct behavior.

**Clang's Prolog**  
It's interesting that this bug only shows up when calling into gcc-compiled code. Using the buggy version of clang to call into other clang-compiled code doesn't cause any trouble. A quick look at the prolog generated by clang reveals why:

```
    testb %al, %al
    je 0x100000d3e
    movaps %xmm0, -176(%rbp)
    movaps %xmm1, -160(%rbp)
    movaps %xmm2, -144(%rbp)
    movaps %xmm3, -128(%rbp)
    movaps %xmm4, -112(%rbp)
    movaps %xmm5, -96(%rbp)
    movaps %xmm6, -80(%rbp)
    movaps %xmm7, -64(%rbp)
```

`0x100000d3e` is the address just off the end of the `movaps` sequence. It's superficially similar, but there's no computed jump. Clang goes for simplicity over efficiency in its prolog. Rather than save exactly the number of registers needed through a clever computed jump, clang just checks to see whether any registers need saving, and if they do, it saves them all. Saving extra registers does no harm aside from a tiny performance hit, so when this code executes with a wacky value in `%al` instead of zero, nothing bad happens.

It's important to note that gcc's code is not _wrong_. It's less robust against bad input, but the actual bug was in clang, which produced that bad input in the first place. However, the bug in clang never does any harm until the two compilers are brought together.

**Bug Recap**  
There are a lot of moving parts to this bug, so let's step through them all briefly one more time.

First, the `x86-64` ABI specifies that the number of floating-point registers used to pass variable arguments into a function is to be stored in the `%al` register. This is presumably to save the time needed to save all eight registers if they're not all used.

Second, gcc implements the prolog of variadic functions to use a computed jump, without bounds checking, to efficiently save precisely the right number of floating-point registers.

Third, clang implements this prolog in a simpler way that either saves all registers or none, with a simple is-zero check. Thus, the common case where clang code calls other clang code hides the bug.

Fourth, in some circumstances, this particular version of clang omits the instruction that zeroes `%al` when making a variadic call that has no floating-point arguments.

Fifth, the remaining code built with clang places a junk value in `%al`.

Sixth, gcc's computed jump reacts to that junk value by jumping several hundred bytes earlier in the program.

What happens from there is up for grabs. In this case, it resulted in the original calling code running again, with a mildly corrupted stack, in what ended up being an infinite loop that was terminated by running out of stack space. In other cases, it could end up crashing immediately, or behaving even weirder. The end result is tough to debug because the state of the program can be pretty corrupted, and the bug involves "impossible" behavior.

**Debugging Recap**  
The first step was to examine the behavior of the buggy program, and pinpoint where it starts to misbehave. In this case, the second time it outputs "Testing" is the first external sign that something is wrong.

The next step was to put a breakpoint on the code that outputs "Testing" to stop the program in the debugger as close to the problem as possible, and see what was calling it.

When that failed due to the corrupted stack, the next step was to verify that the first, expected call was happening the way it was expected.

With the first call verified good and the second call very bad, the next step was to step through the program in the debugger, line-by-line, starting from the good point, until a problem was seen. In this case, the problem manifested as the call to `+format:` not actually invoking the body of `+format:`, but intsead going straight to the second call to print "Testing".

This left the question of whether things went wrong in `objc_msgSend` or in the function prolog for `+format:`. The next step was to put a breakpoint on the very first instruction of `+format:` to see if execution got that far. This showed that the problem lay in the prolog of `+format:`.

The next step was to step through `+format:` one instruction at a time until something went wrong, which showed that the computed jump caused the unwanted behavior.

Knowing what caused the problem, the next step was to examine the relevant assembly in detail to figure out exactly what it did and what it was for. This revealed that it existed to save a number of floating-point registers depending on the value of `%al`.

The next step here was to check the actual value of `%al` in the problem case, which revealed that it contained garbage. An examination of the calling code then revealed the missing instruction to zero `%al` before making the call.

It's a tough road to travel, but persistence pays off.

**Conclusion**  
Compiler bugs can be among the most difficult to diagnose. You need familiarity with a lot of the software stack that we don't often encounter. You also need the ability to throw out fundamental assumptions about how software works, such as the idea that control flow proceeds in a comprehensible manner.

Despite these problems, they _can_ be diagnosed and understood. It can take a lot of work, but problems like this always have a cause somewhere.

Finally, I'd like to mention once more that this bug in clang has since been fixed, and you don't have to worry about encountering it in the wild unless you're using old versions of Xcode _and_ are running your code on 10.6 (or are otherwise calling into gcc-built variadic functions).

That's it for today. I hope you enjoyed this exploration of compiler trouble, and learned the valuable lesson not to trust anything, ever. Friday Q&A is driven by reader ideas, so as always, if you have an idea for a topic you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
