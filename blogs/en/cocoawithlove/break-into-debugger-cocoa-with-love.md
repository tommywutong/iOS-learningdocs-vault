---
title: 'Break into Debugger | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/03/break-into-debugger.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:0b80e1a815648571'
translated: false
---

> 原文：[Break into Debugger | Cocoa with Love](https://www.cocoawithlove.com/2008/03/break-into-debugger.html)　·　Cocoa with Love (Matt Gallagher)

For your debugging pleasure: a DebugBreak() macro to programmatically stop the debugger at a line of code (not inside a child function). Some of this code can be found elsewhere but I present it here, PPC and Intel capable and ready to run.

> **Updated July 31, 2008:** Fixed assembler statements so that they work again.

## Why programmatically stop the debugger?

If you're debugging and you have consistency checks in your code, sometimes you can just log any errors to the console. But there are other times when you want to enter the debugger and explore the memory yourself. Maybe you want to explore the state of your variables to find why things have gone wrong. Maybe any debug information would get lost in your console output.

To allow this, you need a command which will stop GDB at the current line of code. Microsoft's Visual Studio has a handy DebugBreak() command to do just this. On Mac OS X, we get Debugger() and DebugStr() but these don't stop the debugger at the line which invokes them, they instead break the debugger deep inside their own contents.

## How do you stop GDB anyway?

GDB will stop if it encounters a SIGINT (an interrupt signal). There are all kinds of ways to send a SIGINT — pthread_kill() is a good example — however performing this inside a function call has a disadvantage: the debugger will be inside the function which sends the SIGINT when it breaks, not at the line of your code where you called it.

## Inline assembly

The way around this stack issue is to invoke the sys_kill system call or int machine instruction (depending on your CPU) directly inline in your code using inline assembler. That way, the stack doesn't increase and your function is still on the top when you enter the debugger.

## The code

> **Language note:**  
> Most code in this blog is Objective-C only but the following code should compile in any of C, Objective-C or C++ under GCC.

Here's the code to do it. Put it in a header somewhere. Maybe even include the header in your .pch (precompiled header) file.

```objc
#ifdef DEBUG
    #if __ppc64__ || __ppc__
        #define DebugBreak() \
            if(AmIBeingDebugged()) \
            { \
                __asm__("li r0, 20\nsc\nnop\nli r0, 37\nli r4, 2\nsc\nnop\n" \
                    : : : "memory","r0","r3","r4" ); \
            }
    #else
        #define DebugBreak() if(AmIBeingDebugged()) {__asm__("int $3\n" : : );}
    #endif

    bool AmIBeingDebugged(void);
#else
    #define DebugBreak()
#endif
```

You'll also need to copy AmIBeingDebugged() from [Apple's Technical Q&A QA1361 Detecting the Debugger](http://developer.apple.com/qa/qa2004/qa1361.html) and put it in a source file (not a header) somewhere. It's a good idea to put #ifdef DEBUG and #endif around that code too.

If you don't have a DEBUG preprocessor macro defined (you really should) you'll also need to set it up.

1. Right-click on your target (normally same name as your project or executable but it's under the "Targets" heading in the tree view in XCode).
2. Select "Get Info" from the context menu that pops up.
3. Go to the "Build" tab.
4. Make sure the "Configuration" is set to "Debug".
5. Type DEBUG into the field next to "Preprocessor Macros" under "GCC 4.0 - Preprocessing".

## What does the code do?

First: it does nothing outside of DEBUG, that's important. Then it invokes AmIBeingDebugged() to check if GDB is actually running (just because you have the Debug build, doesn't mean GDB is running). Then comes the assembly.

On Intel machines, it's easy: "int $3" (send a SIGINT interrupt to the current process).

On PPC platforms, there's more to do (RISC is more wordy than CISC). Relevant PPC assembler information:

- "li" - load integer, puts the second argument into the location specified by the first
- "sc" - system call, invokes the UNIX system call indicated by the integer in register zero with other arguments starting at register 3.
- "nop" - No operation. Required to wait for some operations to complete.

So here's what the PPC assembly code does:

1. loads 20 into register 0
2. makes a system call, which will be call "20" (sys_getpid) which returns the process ID of the current process into register 3.
3. wait for "sc" to complete
4. loads 37 into register 0
5. loads 2 into register 4
6. makes a system call, which will be call "37" (sys_kill) which sends the signal identified by the integer in register 4 (2 = SIGINT) to the process with ID specified by register 3 (our own PID as returned from the last system call).

If you're wondering what the : : : "memory","r0","r3","r4" stuff is all about, it's just telling the compiler that the assembly block may alter the contents of "memory" and registers 0, 3 and 4.
