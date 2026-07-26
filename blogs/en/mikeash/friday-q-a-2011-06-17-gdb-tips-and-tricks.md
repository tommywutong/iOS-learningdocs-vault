---
title: 'Friday Q&A 2011-06-17: gdb Tips and Tricks'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-06-17-gdb-tips-and-tricks.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6345238da69dde81'
translated: false
---

> 原文：[Friday Q&A 2011-06-17: gdb Tips and Tricks](https://www.mikeash.com/pyblog/friday-qa-2011-06-17-gdb-tips-and-tricks.html)　·　mikeash.com Friday Q&A

Posted at 2011-06-17 19:49 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A Delayed Again](https://www.mikeash.com/pyblog/friday-qa-delayed-again.html)  
Previous article: [Friday Q&A 2011-06-03: Objective-C Blocks vs. C++0x Lambdas: Fight!](https://www.mikeash.com/pyblog/friday-qa-2011-06-03-objective-c-blocks-vs-c0x-lambdas-fight.html)  
Tags: [debugging](https://www.mikeash.com/pyblog/?tag=debugging) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gdb](https://www.mikeash.com/pyblog/?tag=gdb)

Friday Q&A 2011-06-17: gdb Tips and Tricks

by [Mike Ash](https://www.mikeash.com/)

**Getting Started**  
Most Cocoa programmers access `gdb` though Xcode's debugger, which is really just a graphical wrapper around `gdb`. While this is useful, it can also get in the way, and it fails to expose a lot of useful capabilities. Because of this, I'm going to cover the use of `gdb` directly. Virtually everything I discuss can be used at the `(gdb)` prompt in Xcode's debugger console as well, but by learning to use `gdb` on its own, you'll have a better idea of just what's happening behind the scenes. It can also be inconvenient to use the Xcode debugger in some circumstances, and in those cases it's good to be fluent in using `gdb` directly.

First, let's create an example program to debug:

```
    #import <Foundation/Foundation.h>

    int main(int argc, char **argv)
    {
        NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
        NSLog(@"Hello, world!");
        [pool release];

        return 0;
    }
```

We'll compile it with the `-g` flag to tell the compiler to emit debug symbols:

```
    gcc -g -framework Foundation test.m
```

To run it in the debugger, simply invoke `gdb` with the binary as the parameter, which in this case is `a.out`:

```
    gdb a.out
```

A bunch of legal mumbo jumbo gets dumped, but eventually we are presented with a prompt:

```
    (gdb)
```

The debugger is loaded as well as the program we just built. Note, however, that the program has not actually been executed yet. The debugger stops here to give us a chance to set things up before starting the program to be debugged. Here, there's no setup to do, so we'll just run it:

```
    (gdb) run
    Starting program: /Users/mikeash/shell/a.out 
    Reading symbols for shared libraries .++++....................... done
    2011-06-16 20:28:53.658 a.out[2946:a0f] Hello, world!

    Program exited normally.
    (gdb)
```

Let's insert a bug into the program and try it again. Without repeating the entire thing, here are the pertinent bits:

```
    int x = 42;
    NSLog("Hello, world! x = %@", x);
```

And now we get a nice crash when running in the debugger:

```
    (gdb) run
    Starting program: /Users/mikeash/shell/a.out 
    Reading symbols for shared libraries .++++....................... done

    Program received signal EXC_BAD_ACCESS, Could not access memory.
    Reason: 13 at address: 0x0000000000000000
    0x00007fff84f1011c in objc_msgSend ()
    (gdb)
```

Rather than just tossing us back to the shell as would happen if we ran the program directly, `gdb` halts the program but leaves it in memory, allowing us to inspect it. The first thing we want to do is see where the program crashed. From the initial output from `gdb`, we can see that it crashed in `objc_msgSend_fixup`, but that doesn't tell us where it's crashing in _our_ code. To find this out, we want to get a listing of the call stack of the current thread. This can be done with the `backtrace` command, or simply abbreviated as `bt`:

```
    (gdb) bt
    #0  0x00007fff84f1011c in objc_msgSend ()
    #1  0x00007fff864ff30b in _CFStringAppendFormatAndArgumentsAux ()
    #2  0x00007fff864ff27d in _CFStringCreateWithFormatAndArgumentsAux ()
    #3  0x00007fff8657e9ef in _CFLogvEx ()
    #4  0x00007fff87beab3e in NSLogv ()
    #5  0x00007fff87beaad6 in NSLog ()
    #6  0x0000000100000ed7 in main () at test.m:10
```

Now we can see that it's crashing in the call to `NSLog`. Let's see exactly where the call is. Although this is obvious in such a small program, this can be handy in bigger ones. First we need to jump up to the stack frame which contains our code, in this case `#6`. We'll do this using the `up` command, which allows us to move between stack frames:

```
    (gdb) up 6
    #6  0x0000000100000ed7 in main () at test.m:10
    9       NSLog("Hello, world! x = %@", x);
```

This not only shows us the stack frame, but also the line of code in question. If we wanted to go back down the stack from here, the `down` command will do this. To get more context, we can use the `list` command, abbreviated as `l`:

```
    (gdb) l
    5   
    6   int main(int argc, char **argv)
    7   {
    8       NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    9       int x = 42;
    10      NSLog("Hello, world! x = %@", x);
    11      [pool release];
    12      
    13      return 0;
    14  }
```

Of course, we can see all of the code by simply opening `test.m` in a text editor and looking at line 9, but it's sometimes convenient to inspect the code directly from the debugger.

At this point, now that we see the line in question, it should be obvious that we're missing a `@` from the beginning of the format string. Let's fix that and re-run the program.

```
    (gdb) run
    Starting program: /Users/mikeash/shell/a.out 
    Reading symbols for shared libraries .++++....................... done

    Program received signal EXC_BAD_ACCESS, Could not access memory.
    Reason: KERN_INVALID_ADDRESS at address: 0x000000000000002a
    0x00007fff84f102b3 in objc_msgSend_fixup ()
    (gdb) bt
    #0  0x00007fff84f102b3 in objc_msgSend_fixup ()
    #1  0x0000000000000000 in ?? ()
```

Unfortunately, it still crashes. Worse, the stack got screwed up and we can't even see where `objc_msgSend_fixup` is being called from. To figure out which line of code is at fault, let's set a breakpoint so that the debugger will stop on the first line of code. This is done using the `break` command, abbreviated as `b`. It can take a symbol or a `file:line` combination:

```
    (gdb) b test.m:8
    Breakpoint 1 at 0x100000e8f: file test.m, line 8.
```

The debugger tells us that the breakpoint is set. This is breakpoint 1, which is useful in order to disable, enable, or delete the breakpoint later (using, surprise, the `disable`, `enable`, and `delete` commands). Now we can run the program again:

```
    (gdb) run
    The program being debugged has been started already.
    Start it from the beginning? (y or n) y
    Starting program: /Users/mikeash/shell/a.out 

    Breakpoint 1, main (argc=1, argv=0x7fff5fbff628) at test.m:8
    8       NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
```

The debugger is now stopped on the line of code in question. This lets us take control before the crash actually occurs. Now, we'll step through the code line by line to see which line is crashing. The `next` command, abbreviated as `n`, will do this:

```
    (gdb) n
    9       int x = 42;
    (gdb) 
    10      NSLog(@"Hello, world! x = %@", x);
    (gdb) 

    Program received signal EXC_BAD_ACCESS, Could not access memory.
    Reason: KERN_INVALID_ADDRESS at address: 0x000000000000002a
    0x00007fff84f102b3 in objc_msgSend_fixup ()
```

Note that simply hitting return will tell the debugger to repeat the last command, so the above does `next` three times. Now we can see that the crash is once again on the `NSLog`, even though we can't get a good backtrace. This is hopefully enough for us to realize that this second crash is due to using `%@` instead of `%d` to print an `int`. The address that it crashed on, `0x000000000000002a`, is 42 in hexadecimal, and comes from treating `x` like a pointer.

**Printing Values**  
Printing the value of variables or expressions is extremely useful for debugging. This can be done using the `print` command, abbreviated as `p`:

```
    (gdb) p x
    $1 = 42
```

The format of the output can be controlled by using `/format` after the `p` command, where `format` is a format letter known to `gdb`. Useful format letters include `x` for hexadecimal, `c` for char, and `a` for address:

```
    (gdb) p/x x
    $2 = 0x2a
```

The `po` command, short for `print-object` will print the description of an Objective-C object. It works by sending the `debugDescription` message to the object, which is usually equivalent to the more familiar `description` message. For example, we can check out that lovely autorelease pool:

```
    (gdb) po pool
    <NSAutoreleasePool: 0x10010e820>
```

These commands can also take complete expressions. For example, let's check out the method signature of `NSObject`'s `-debugDescription` method:

```
    (gdb) po [NSObject instanceMethodSignatureForSelector: @selector(debugDescription)]
    <NSMethodSignature: 0x10010f320>
        number of arguments = 2
        frame size = 224
        is special struct return? NO
        return value: -------- -------- -------- --------
            type encoding (@) '@'
            flags {isObject}
            modifiers {}
            frame {offset = 0, offset adjust = 0, size = 8, size adjust = 0}
            memory {offset = 0, size = 8}
        argument 0: -------- -------- -------- --------
            type encoding (@) '@'
            flags {isObject}
            modifiers {}
            frame {offset = 0, offset adjust = 0, size = 8, size adjust = 0}
            memory {offset = 0, size = 8}
        argument 1: -------- -------- -------- --------
            type encoding (:) ':'
            flags {}
            modifiers {}
            frame {offset = 8, offset adjust = 0, size = 8, size adjust = 0}
            memory {offset = 0, size = 8}
```

When using class methods like this, the debugger occasionally becomes obstinate and refuses to recognize class names. To work around this, use `NSClassFromString` to obtain the class in the expression:

```
    (gdb) po [NSClassFromString(@"NSObject") instanceMethodSignatureForSelector: @selector(debugDescription)]
```

We can also print the result of messages which return primitive values. However, `gdb` is not smart enough to figure out the return type in this case, so we have to tell it by adding a cast to the expression:

```
    (gdb) p [NSObject instancesRespondToSelector: @selector(doesNotExist)]
    Unable to call function "objc_msgSend" at 0x7fff84f100f4: no return type information available.
    To call this function anyway, you can cast the return type explicitly (e.g. 'print (float) fabs (3.0)')
    (gdb) p (char)[NSObject instancesRespondToSelector: @selector(doesNotExist)]
    $5 = 0 '\000'
```

`gdb` also isn't always smart about Cocoa-specific typedefs like `BOOL`, so in this case I've used the equivalent `char`. While you want to call things by their proper names when writing code, when debugging it's usually perfectly fine to play a little fast and loose with things like type names, as long as they're equivalent on the architecture you're currently debugging.

You'll notice that when using `p`, the expression is printed with something like `$1 =` in front of it. These are actually `gdb` variables, and they can be used to refer to the value of that expression later. For example, we can `malloc` some memory, zero it out, then free it without having to manually copy/paste the address each time:

```
    (gdb) p (int *)malloc(4)
    $6 = (int *) 0x100105ab0
    (gdb) p (void)bzero($6, 4)
    $7 = void
    (gdb) p *$6
    $8 = 0
    (gdb) p (void)free($6)
    $9 = void
```

Note that, as with methods, we usually have to explicitly inform `gdb` of the return type of functions we tell it to call. The same technique can be used with objects, although unfortunately the `po` command doesn't save its return value to a variable, so we have to first do a `p` and then follow it with a `po` of the new variable:

```
    (gdb) p (void *)[[NSObject alloc] init]
    $10 = (void *) 0x100105950
    (gdb) po $10
    <NSObject: 0x100105950>
    (gdb) p (long)[$10 retainCount]
    $11 = 1
    (gdb) p (void)[$10 release]
    $12 = void
```

**Inspecting Memory**  
Sometimes, printing a single value isn't enough. Instead, we want to print out the contents of a whole bunch of memory at once. The oddly named `x` command can do this for us.

The `x` command looks like this: `x/format address`. The address is an expression which evaluates to the address of the memory you want to inspect. The format gets a little trickier, because the syntax is extremely dense. The format consists of three components. The first component is the number of items to print, as a plain text integer. The second component is a format letter. The full list can be found by typing `help x` at the `(gdb)` prompt, but useful ones include `x` for hexadecimal, `d` for decimal, and `c` for char. The last component is a size letter. The size letter is one of `b`, `h`, `w`, or `g`, which correspond to 1, 2, 4, and 8 bytes, respectively. For example, to print eight four-byte hex components at `ptr`:

```
    (gdb) x/4xw ptr
```

More concretely, let's inspect the contents of the NSObject class:

```
    (gdb) x/4xg (void *)[NSObject class]
    0x7fff70adb468 <OBJC_CLASS_$_NSObject>: 0x00007fff70adb440  0x0000000000000000
    0x7fff70adb478 <OBJC_CLASS_$_NSObject+16>:  0x0000000100105ac0  0x0000000100104ac0
```

I won't get into the details of interpreting all of these values, but you can see that it's easy to get a raw dump of the contents. Let's try another one, this time taking a look at what an `NSObject` instance looks like:

```
    (gdb) x/1xg (void *)[NSObject new]
    0x100105ba0:    0x00007fff70adb468
```

Notice how the beginning of this object contains the same value as the location of the `NSObject` class shown just above.

Using the `i` format, for `instruction`, we can even dump a disassembly of a particular location in memory:

```
    (gdb) x/5iw main
    0x100000e50 <main>: push   %rbp
    0x100000e51 <main+1>:   mov    %rsp,%rbp
    0x100000e54 <main+4>:   sub    $0x20,%rsp
    0x100000e58 <main+8>:   mov    %edi,-0x14(%rbp)
    0x100000e5b <main+11>:  mov    %rsi,-0x20(%rbp)
```

There is also a dedicated `disas` command, which produces largely the same output.

**Setting Variables**  
Sometimes it's useful not only to inspect data, but actually alter it. To sent the contents of a variable, simply use the `set` command:

```
    (gdb) set x = 43
```

An arbitrary expression can be used for the new value. To assign a variable to a new object, you can do:

```
    (gdb) set obj = (void *)[[NSObject alloc] init]
```

This can be handy to create places in your program where you want it to wait for you to manipulate it with the debugger for some reason. Write what appears to be an infinite loop, checking a variable which never changes:

```
    NSLog(@"Waiting for debugger....");

    volatile int debugged = 0;
    while(!debugged)
        sleep(1);
```

Once it reaches this loop, you can hop into the debugger and make the program continue by changing the variable:

```
    (gdb) set debugged = 1
    (gdb) continue
```

Note that it's necessary to declare the variable as `volatile` to ensure that the compiler doesn't simply optimize away the check altogether.

**Breakpoints**  
A breakpoint is a location in the program where, if execution reaches that location, the program is stopped and the debugger activates. As mentioned previously, a breakpoint can be made with the `break` command, abbreviated as `b`. There are several forms which can be used to indicate the target of a breakpoint:

- `SymbolName`: write the name of a function, and the breakpoint will target that function.
- `file.c:1234`: set a breakpoint on the specified line of the given file.
- `-[ClassName method:name:]`: set a breakpoint on an Objective-C method. Use `+` for class methods.
- `*0xdeadbeef`: break at a particular address in memory. Not usually useful unless you're debugging assembly or something of the sort.

Breakpoints can be toggled on and off using `enable` and `disable` on the breakpoint number. If you want to remove one completely, use `delete`. To get a list of all existing breakpoints, use the `info breakpoints` command, which can be abbreviated as `info b` or even just `i b`.

Breakpoints can be made conditional by adding `if` followed by an expression after the breakpoint target. In this case, the debugger only pauses execution of the program when the condition evaluates to true. For example, to break on a method only if the parameter is equal to 5:

```
    (gdb) b -[Class myMethod:] if parameter == 5
```

Finally, breakpoints can have commands added to them. To do this, type `commands` followed by the breakpoint number. If you want to add commands to a breakpoint you just set, you don't need to provide the number. Breakpoint commands are just a list of standard `gdb` commands terminated by `end`. This is useful if you know you always want to do something whenever a particular breakpoint is hit. For example, let's say you wanted a backtrace from every `NSLog` call:

```
    (gdb) b NSLog
    Breakpoint 4 at 0x7fff87beaa62
    (gdb) commands
    Type commands for when breakpoint 4 is hit, one per line.
    End with a line saying just "end".
    >bt
    >end
```

Now, whenever `NSLog` is hit, the debugger will automatically print a backtrace before pausing the program and showing the `(gdb)` prompt.

Sometimes you simply want the debugger to print some information but not pause the program. This effectively allows you to add logging statements on the fly. To do this, simply put `continue` at the end of your breakpoint commands, and execution will immediately resume. Here's an example of setting a breakpoint which dumps a backtrace, prints a parameter, and then continues:

```
    (gdb) b -[Class myMethod:]
    Breakpoint 5 at 0x7fff864f1404
    (gdb) commands
    Type commands for when breakpoint 5 is hit, one per line.
    End with a line saying just "end".
    >bt
    >p parameter
    >continue
    >end
```

One final useful tidbit is the `return` command, which causes the currently executing function to return control to its caller. If a parameter is given, that value is returned. This can be used to disable functions or methods altogether. For example, to turn off `NSLog`:

```
    (gdb) commands
    Type commands for when breakpoint 6 is hit, one per line.
    End with a line saying just "end".
    >return
    >continue
    >end
```

While these tricks are extremely useful, it's important to note that any time `gdb` gets involved with the target program, performance takes a huge hit. A trick like the above will disable `NSLog`, but it will also make each call to NSLog take significantly longer, because each call has to break into the debugger, the debugger has to execute the commands given, and every action involves a bunch of tricky cross-process manipulation. Usually this is fine, but you generally wouldn't want to do something like put a conditional breakpoint on `objc_msgSend`, as it will cause your app to take forever to do anything.

**Function and Method Arguments Without Source**  
Sometimes you end up in code where you don't have the source. Frequently you end up with a crash or other misbehavior occurring deep in Cocoa, and you need to figure out what's going wrong. One of the most useful things you can do at this point is to inspect the arguments to the function or method in question to try to figure out what's going on.

Clark Cox has [an excellent reference](http://www.clarkcox.com/blog/2009/02/04/inspecting-obj-c-parameters-in-gdb/) on how parameters are represented at the machine level on various architectures. It doesn't cover ARM (iOS devices), but fortunately ARM is easy: parameters are passed in order in registers `$r0`, `$r1`, `$r2`, and `$r3`. Note that for all of the architectures which pass parameters in registers (all of them besides `i386`), these can only be reliably used at the very beginning of the function, as it's likely that the registers in question will be reused for other data as the function proceeds.

As an example, we can print the argument passed to `NSLog`:

```
    Breakpoint 2, 0x00007fff87beaa62 in NSLog ()
    (gdb) po $rdi
    Hello, world!
```

This can also be extremely useful when using breakpoint conditions. As an example, let's say that a mysterious call to `NSLog` is resulting in a crash, but it's impractical to put a general breakpoint there because it's called too frequently. However, we can write a breakpoint condition based on the content of the log:

```
    (gdb) break NSLog if (char)[$rdi hasPrefix: @"crashing"]
```

When doing this sort of thing, keep in mind that the first two parameters to methods are taken up by `self` and `_cmd`, so your explicit parameters will start out at `$rdx` (on x86_64) or `$r2` (on ARM).

**Debugging Exceptions**  
Exceptions are thrown in Objective-C with the runtime function `objc_exception_throw`. It's extremely useful to keep a breakpoint on this function, since exceptions are usually rare in Objective-C and when they do happen, it's often the first sign of something going seriously wrong. Without a breakpoint here, you'll generally only find out about the exception after it's been caught, so you have no information about where it was thrown.

With a breakpoint set, you'll stop as the exception is being thrown, which gives you the opportunity to see the full stack trace of what's throwing it, and inspect your program to figure out why. However, the breakpoint stops _before_ any information about the exception is logged. Fortunately, this is easy to work around. The exception being thrown is the first (and only) argument to `objc_exception_throw`, so it can be printed using the techniques discussed above for accessing the arguments of a function without that function's source code.

**Threads**  
In this modern age, we work with a lot of multithreaded code, and it's important to be able to deal with that in the debugger. Here's some quick GCD code that spins off a few background threads and just sits:

```
    dispatch_apply(3, dispatch_get_global_queue(0, 0), ^(size_t x){
        sleep(100);
    });
```

I'll run this in the debugger, then use control-C to stop execution while it's sleeping:

```
    (gdb) run
    Starting program: /Users/mikeash/shell/a.out 
    Reading symbols for shared libraries .+++........................ done
    ^C
    Program received signal SIGINT, Interrupt.
    0x00007fff88c6ff8a in __semwait_signal ()
    (gdb) bt
    #0  0x00007fff88c6ff8a in __semwait_signal ()
    #1  0x00007fff88c6fe19 in nanosleep ()
    #2  0x00007fff88cbcdf0 in sleep ()
    #3  0x0000000100000ea7 in __main_block_invoke_1 (.block_descriptor=0x1000010a0, x=0) at test.m:12
    #4  0x00007fff88cbbbc8 in _dispatch_apply2 ()
    #5  0x00007fff88cb31e5 in dispatch_apply_f ()
    #6  0x0000000100000e6a in main (argc=1, argv=0x7fff5fbff628) at test.m:11
```

This is pretty much what we'd expect. Notice how `dispatch_apply` is smart enough to borrow the main thread to execute one of the blocks. But how about the other two blocks, which are running on a background thread somewhere? We can get a list of all threads with the `info threads` command:

```
    (gdb) info threads
      3 "com.apple.root.default-priorit" 0x00007fff88c6ff8a in __semwait_signal ()
      2 "com.apple.root.default-priorit" 0x00007fff88c6ff8a in __semwait_signal ()
    * 1 "com.apple.root.default-priorit" 0x00007fff88c6ff8a in __semwait_signal ()
```

The `*` next to thread 1 indicates that this is the one we're currently on. Let's see what thread 2 is up to. We can switch with `thread 2`, then get a backtrace from there:

```
    (gdb) thread 2
    [Switching to thread 2 (process 4794), "com.apple.root.default-priority"]
    0x00007fff88c6ff8a in __semwait_signal ()
    (gdb) bt
    #0  0x00007fff88c6ff8a in __semwait_signal ()
    #1  0x00007fff88c6fe19 in nanosleep ()
    #2  0x00007fff88cbcdf0 in sleep ()
    #3  0x0000000100000ea7 in __main_block_invoke_1 (.block_descriptor=0x1000010a0, x=1) at test.m:12
    #4  0x00007fff88cbbbc8 in _dispatch_apply2 ()
    #5  0x00007fff88c4f7f1 in _dispatch_worker_thread2 ()
    #6  0x00007fff88c4f128 in _pthread_wqthread ()
    #7  0x00007fff88c4efc5 in start_wqthread ()
```

There we can see that this second block is running on a dispatch worker thread being managed by the `pthread_wqthread` system. This is useful, but a bit tedious. We only have three threads, but what if we had 300? We can apply a command to all threads using `thread apply all`. To get a backtrace of each thread, we can do `thread apply all backtrace`, or as an amusingly dense shortcut, `t a a bt`:

```
    (gdb) t a a bt

    Thread 3 (process 4794):
    #0  0x00007fff88c6ff8a in __semwait_signal ()
    #1  0x00007fff88c6fe19 in nanosleep ()
    #2  0x00007fff88cbcdf0 in sleep ()
    #3  0x0000000100000ea7 in __main_block_invoke_1 (.block_descriptor=0x1000010a0, x=2) at test.m:12
    #4  0x00007fff88cbbbc8 in _dispatch_apply2 ()
    #5  0x00007fff88c4f7f1 in _dispatch_worker_thread2 ()
    #6  0x00007fff88c4f128 in _pthread_wqthread ()
    #7  0x00007fff88c4efc5 in start_wqthread ()

    Thread 2 (process 4794):
    #0  0x00007fff88c6ff8a in __semwait_signal ()
    #1  0x00007fff88c6fe19 in nanosleep ()
    #2  0x00007fff88cbcdf0 in sleep ()
    #3  0x0000000100000ea7 in __main_block_invoke_1 (.block_descriptor=0x1000010a0, x=1) at test.m:12
    #4  0x00007fff88cbbbc8 in _dispatch_apply2 ()
    #5  0x00007fff88c4f7f1 in _dispatch_worker_thread2 ()
    #6  0x00007fff88c4f128 in _pthread_wqthread ()
    #7  0x00007fff88c4efc5 in start_wqthread ()

    Thread 1 (process 4794):
    #0  0x00007fff88c6ff8a in __semwait_signal ()
    #1  0x00007fff88c6fe19 in nanosleep ()
    #2  0x00007fff88cbcdf0 in sleep ()
    #3  0x0000000100000ea7 in __main_block_invoke_1 (.block_descriptor=0x1000010a0, x=0) at test.m:12
    #4  0x00007fff88cbbbc8 in _dispatch_apply2 ()
    #5  0x00007fff88cb31e5 in dispatch_apply_f ()
    #6  0x0000000100000e6a in main (argc=1, argv=0x7fff5fbff628) at test.m:11
```

Here we can easily see the entire program's thread state at a glance. If we want to inspect a particular thread more thoroughly, we can easily switch to a given thread using the `thread` command, then use other debugger commands as usual.

**Attaching to a Running Process**  
The debugger is normally used by having it start the target program, but sometimes that isn't practical. Maybe your program started misbehaving in the middle of a run where you didn't use the debugger, or maybe you need to investigate a situation where the program is already being started by something else, like `launchd`, and it's inconvenient to get the debugger involved in the start.

In this scenario, it's handy to be able to attach the debugger to a process which is already running. This can be done by telling `gdb` to attach to a particular pid, either when starting `gdb` from the command line:

```
    $ gdb attach 12345
```

Or from the `gdb` command prompt after starting it separately:

```
    (gdb) attach 12345
```

Once attached, everything behaves pretty much like it would if you had started the program directly from the debugger. Once exception to this is that if you quit the debugger, it will simply detach the program rather than killing it as it would normally do.

**Command Line Arguments and Environment Variables**  
Providing command line arguments and environment variables is easy but not completely straightforward. If you try to provide command line arguments in the shell, `gdb` will think that you're giving it more files to examine, and it will complain:

```
    $ gdb /bin/echo hello world
    Excess command line arguments ignored. (world)
    [...]
    /Users/mikeash/shell/hello: No such file or directory
```

Instead, command line arguments are provided to the `run` command at the gdb prompt:

```
    (gdb) run hello world
    Starting program: /bin/echo hello world
    Reading symbols for shared libraries +. done
    hello world
```

Environment variables can be set in the shell prior to starting `gdb`, but they will be visible to `gdb` as well. Often, this is fine, but if you're manipulating something which can have a major effect on every program that it touches, like setting `DYLD_INSERT_LIBRARIES`, it's a bad idea to put them into `gdb` as well. In this case, the `set env` command can be used to set environment variables only for the target:

```
    (gdb) set env DYLD_INSERT_LIBRARIES /gdb/crashes/if/this/is/inserted.dylib
```

**Conclusion**  
That wraps up today's exploration of `gdb`. It's a difficult but powerful tool. Being able to fluently use `gdb` from the command line is often the difference between throwing up your hands in despair or tediously adding logging statements, and quickly diving in and getting the information you need to solve your problem.

`gdb` goes much deeper than I discussed here. For more information, consult its extensive internal help system by entering `help` at the prompt. Every command has help as well, which can be accessed with `help command`.

As usual, come back in two weeks for the next Friday Q&A. Until that time, enjoy `gdb`. As always, Friday Q&A is driven by reader suggestions, so if you have a topic you'd like to see discussed here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-06-17-gdb-tips-and-tricks.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
