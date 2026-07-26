---
title: 'Friday Q&A 2018-06-29: Debugging with C-Reduce'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2018-06-29-debugging-with-c-reduce.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2c16b0b77557249d'
translated: false
---

> 原文：[Friday Q&A 2018-06-29: Debugging with C-Reduce](https://www.mikeash.com/pyblog/friday-qa-2018-06-29-debugging-with-c-reduce.html)　·　mikeash.com Friday Q&A

Posted at 2018-06-29 13:35 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [objc_msgSend's New Prototype](https://www.mikeash.com/pyblog/objc_msgsends-new-prototype.html)  
Previous article: [Friday Q&A 2018-04-27: Generating Text With Markov Chains in Swift](https://www.mikeash.com/pyblog/friday-qa-2018-04-27-generating-text-with-markov-chains-in-swift.html)  
Tags: [debugging](https://www.mikeash.com/pyblog/?tag=debugging) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2018-06-29: Debugging with C-Reduce

by [Mike Ash](https://www.mikeash.com/)

**Overview**  
C-Reduce is based on two main ideas.

First, there's the idea of a reduction pass. This is a transformation performed on some source code which produces a reduced version of that code. C-Reduce has a bunch of different passes, including things like deleting lines or renaming tokens to shorter versions.

Second, there's the idea of an interestingness test. The reduction passes are blind, and often produce programs which no longer contain the bug, or which don't compile at all. When you use C-Reduce, you provide not only a program to reduce but also a small script which tests whether a reduced program is "interesting." Exactly what "interesting" means is up to you. If you're trying to isolate a bug, then "interesting" would mean that the bug still occurs in the program. You can define it to mean whatever you want, as long as you can script it. Whatever test you provide, C-Reduce will try to provide a reduced version of the program that still passes the test.

**Installation**  
C-Reduce has a lot of dependencies and can be difficult to install. Thankfully, Homebrow has it, so you can let it take care of things:

```
    brew install creduce
```

If you'd rather do it yourself, [take a look at C-Reduce's INSTALL file](https://github.com/csmith-project/creduce/blob/master/INSTALL).

**Simple Example**  
It's difficult to come up with small examples for C-Reduce, since its whole purpose is to start from something large and _produce_ a small example, but we'll give it our best try. Here's a simple C program that produces a somewhat cryptic warning:

```
    $ cat test.c
    #include <stdio.h>

    struct Stuff {
        char *name;
        int age;
    }

    main(int argc, char **argv) {
        printf("Hello, world!\n");
    }
    $ clang test.c
    test.c:3:1: warning: return type of 'main' is not 'int' [-Wmain-return-type]
    struct Stuff {
    ^
    test.c:3:1: note: change return type to 'int'
    struct Stuff {
    ^~~~~~~~~~~~
    int
    test.c:10:1: warning: control reaches end of non-void function [-Wreturn-type]
    }
    ^
    2 warnings generated.
```

Somehow our `struct` is messing with `main`! How could that be? Maybe reducing it would help us figure it out.

We need an interestingness test. We'll write a small shell script to compile this program and check for the warning in the output. C-Reduce is eager to please and can easily reduce a program far beyond what we really want. To keep it under control, we'll write a script that not only checks for the warning, but also rejects any program that produces an error, and requires `struct Stuff` to be somewhere in the compiler output. Here's the script:

```
    #!/bin/bash

    clang test.c &> output.txt
    grep error output.txt && exit 1
    grep "warning: return type of 'main' is not 'int'" output.txt &&
    grep "struct Stuff" output.txt
```

First, it compiles the program and saves the compiler output into `output.txt`. If the output contains the text "error" then it immediately signals that this program is not interesting by exiting with error code 1. Otherwise it checks for both the warning and for `struct Stuff` in the output. `grep` exits with code `0` if it finds a match, so the result is that this script exits with code `0` if both of those match, and code `1` if either one fails. Exit code `0` signals to C-Reduce that the reduced program is interesting, while code `1` signals that it's not interesting and should be discarded.

Now we have enough to run C-Reduce:

```
    $ creduce interestingness.sh test.c 
    ===< 4907 >===
    running 3 interestingness tests in parallel
    ===< pass_includes :: 0 >===
    (14.6 %, 111 bytes)

    ...lots of output...

    ===< pass_clex :: rename-toks >===
    ===< pass_clex :: delete-string >===
    ===< pass_indent :: final >===
    (78.5 %, 28 bytes)
    ===================== done ====================

    pass statistics:
      method pass_balanced :: parens-inside worked 1 times and failed 0 times
      method pass_includes :: 0 worked 1 times and failed 0 times
      method pass_blank :: 0 worked 1 times and failed 0 times
      method pass_indent :: final worked 1 times and failed 0 times
      method pass_indent :: regular worked 2 times and failed 0 times
      method pass_lines :: 3 worked 3 times and failed 30 times
      method pass_lines :: 8 worked 3 times and failed 30 times
      method pass_lines :: 10 worked 3 times and failed 30 times
      method pass_lines :: 6 worked 3 times and failed 30 times
      method pass_lines :: 2 worked 3 times and failed 30 times
      method pass_lines :: 4 worked 3 times and failed 30 times
      method pass_lines :: 0 worked 4 times and failed 20 times
      method pass_balanced :: curly-inside worked 4 times and failed 0 times
      method pass_lines :: 1 worked 6 times and failed 33 times

              ******** .../test.c ********

    struct Stuff {
    } main() {
    }
```

At the end, it outputs the reduced version of the program that it came up with. It also saves the reduced version into the original file. Beware of this when working on real code! Be sure to run C-Reduce on a copy of the code (or on a file that's already checked into version control), not on an irreplaceable original.

This reduced version makes the problem more apparent: we forgot the semicolon at the end of the declaration of `struct Stuff`, and we forgot the return type on `main`, which causes the compiler to interpret `struct Stuff` as the return type to `main`. This is bad, because `main` has to return `int`, thus the warning.

**Xcode Projects**  
That's fine for something we've already reduced to a single file, but what about something more complex? Most of us have Xcode projects, so what if we want to reduce one of those?

This gets awkward because of the way C-Reduce works. It copies the file to reduce into a new directory, then runs your interestingness script there. This allows it to run a lot of tests in parallel, but this breaks if you need other stuff for it to work. Since your interestingness script can run arbitrary commands, you can work around this by copying the rest of the project into the temporary directory.

I created a standard Cocoa Objective-C app project in Xcode and then modified the `AppDelegate.m` file like so:

```
    #import "AppDelegate.h"

    @interface AppDelegate () {
        NSWindow *win;
    }

    @property (weak) IBOutlet NSWindow *window;
    @end

    @implementation AppDelegate

    - (void)applicationDidFinishLaunching: (NSRect)visibleRect {
        NSLog(@"Starting up");
        visibleRect = NSInsetRect(visibleRect, 10, 10);
        visibleRect.size.height *= 2.0/3.0;
        win = [[NSWindow alloc] initWithContentRect: NSMakeRect(0, 0, 100, 100) styleMask:NSWindowStyleMaskTitled backing:NSBackingStoreBuffered defer:NO];
        [win makeKeyAndOrderFront: nil];
        NSLog(@"Off we go");
    }

    @end
```

This strange code crashes the app on startup:

```
    * thread #1, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=EXC_I386_GPFLT)
      * frame #0: 0x00007fff3ab3bf2d CoreFoundation`__CFNOTIFICATIONCENTER_IS_CALLING_OUT_TO_AN_OBSERVER__ + 13
```

This is not a very informative backtrace. We could try to debug (or just notice the problem), but instead let's reduce!

The interestingness test needs to do some more work here. Let's start with a helper to run the app with a timeout. We're looking for a crash, and if the app _doesn't_ crash it'll just stay open, so we need to kill it after a few seconds. I found this handy perl snippet repeated all over the internet:

```
    function timeout() { perl -e 'alarm shift; exec @ARGV' "$@"; }
```

Next, we need to copy the Xcode project over:

```
    cp -a ~/Development/creduce-examples/Crasher .
```

The `AppDelegate.m` file isn't automatically placed in the appropriate location, so copy that across. (Note: C-Reduce will copy the file back if it finds a reduction, so be sure to use `cp` here rather than `mv`. Using `mv` will result in a cryptic fatal error.)

```
    cp AppDelegate.m Crasher/Crasher
```

Then switch into the `Crasher` directory and build the project, exiting on failure:

```
    cd Crasher
    xcodebuild || exit 1
```

If it worked, run the app with a timeout. My system is configured so that `xcodebuild` places the build result in a local `build` directory. Yours may be configured differently, so check first. Note that if your configuration builds to a shared build directory, you'll want to disable C-Reduce's parallel builds by adding `--n 1` to the command line when invoking it.

```
    timeout 5 ./build/Release/Crasher.app/Contents/MacOS/Crasher
```

If it crashes, it'll exit with the special code `139`. Translate that into an exit code of `0`, and in all other cases exit with code `1`:

```
    if [ $? -eq 139 ]; then
        exit 0
    else
        exit 1
    fi
```

Now we're ready to run C-Reduce:

```
    $ creduce interestingness.sh Crasher/AppDelegate.m
    ...
    (78.1 %, 151 bytes)
    ===================== done ====================

    pass statistics:
      method pass_ints :: a worked 1 times and failed 2 times
      method pass_balanced :: curly worked 1 times and failed 3 times
      method pass_clex :: rm-toks-7 worked 1 times and failed 74 times
      method pass_clex :: rename-toks worked 1 times and failed 24 times
      method pass_clex :: delete-string worked 1 times and failed 3 times
      method pass_blank :: 0 worked 1 times and failed 1 times
      method pass_comments :: 0 worked 1 times and failed 0 times
      method pass_indent :: final worked 1 times and failed 0 times
      method pass_indent :: regular worked 2 times and failed 0 times
      method pass_lines :: 8 worked 3 times and failed 43 times
      method pass_lines :: 2 worked 3 times and failed 43 times
      method pass_lines :: 6 worked 3 times and failed 43 times
      method pass_lines :: 10 worked 3 times and failed 43 times
      method pass_lines :: 4 worked 3 times and failed 43 times
      method pass_lines :: 3 worked 3 times and failed 43 times
      method pass_lines :: 0 worked 4 times and failed 23 times
      method pass_lines :: 1 worked 6 times and failed 45 times

              ******** /Users/mikeash/Development/creduce-examples/Crasher/Crasher/AppDelegate.m ********

    #import "AppDelegate.h"
    @implementation AppDelegate
    - (void)applicationDidFinishLaunching:(NSRect)a {
      a = NSInsetRect(a, 0, 10);
      NSLog(@"");
    }
    @end
```

That's a lot shorter! The `NSLog` line looks harmless, although it must be part of the crash if C-Reduce didn't remove it. The `a = NSInsetRect(a, 0, 10);` line is the only other thing that actually does something. Where does `a` come from and why would writing to it do something bad? It's just the parameter to `applicationDidFinishLaunching:` which... is not an `NSRect`.

```
    - (void)applicationDidFinishLaunching:(NSNotification *)notification;
```

Oops! The parameter type mismatch resulted in stack corruption that caused the uninformative crash.

C-Reduce took a long time to run on this example, because building an Xcode project takes longer than compiling a single file, and because a lot of the test cases hit the five-second timeout when running. C-Reduce copies the reduced file back to the original directory on every success, so you can leave it open in a text editor to watch it at work. If you think it's gone far enough, you can ^C it and you'll be left with the partially-reduced file. If you decide you want to run it some more, re-run it and it will continue from there.

**Swift**  
What if you're using Swift and want to reduce a problem? Given the name, I originally thought that C-Reduce only worked on C (and maybe C++, since so many tools do both).

Thankfully, I was wrong. C-Reduce does have some C-specific reduction passes, but it has a lot of others that are relatively language agnostic. It may be less effective, but as long as you can write an interestingness test for your problem, C-Reduce can probably work on it no matter what language you're using.

Let's try it. I found a [nice compiler bug on bugs.swift.org](https://bugs.swift.org/browse/SR-7354). It's already been fixed, but Xcode 9.3's Swift crashes on it and I happen to have that version handy. Here's a slightly modified version of the example from that bug:

```
    import Foundation

    func crash() {
        let blah = ProblematicEnum.problematicCase.problematicMethod()
        NSLog("\(blah)")
    }

    enum ProblematicEnum {
        case first, second, problematicCase

        func problematicMethod() -> SomeClass {
            let someVariable: SomeClass

            switch self {
            case .first:
                someVariable = SomeClass()
            case .second:
                someVariable = SomeClass()
            case .problematicCase:
                someVariable = SomeClass(someParameter: NSObject())
                _ = NSObject().description
                return someVariable // EXC_BAD_ACCESS (simulator: EXC_I386_GPFLT, device: code=1)
            }

            let _ = [someVariable]
            return SomeClass(someParameter: NSObject())
        }

    }

    class SomeClass: NSObject {
        override init() {}
        init(someParameter: NSObject) {}
    }

    crash()
```

Let's try running it with optimizations enabled:

```
    $ swift -O test.swift 
    <unknown>:0: error: fatal error encountered during compilation; please file a bug report with your project and the crash log
    <unknown>:0: note: Program used external function '__T04test15ProblematicEnumON' which could not be resolved!
    ...
```

The interestingness test is fairly simple for this one. Run that command and check the exit code:

```
    swift -O test.swift
    if [ $? -eq 134 ]; then
        exit 0
    else
        exit 1
    fi
```

Running C-Reduce on this, it produces the following example:

```
    enum a {
        case b, c, d
        func e() -> f {
            switch self {
            case .b:
                0
            case .c:
                0
            case .d:
                0
            }
            return f()
        }
    }
    class f{}
```

Diving into the actual compiler bug is beyond the scope of this article, but this reduction would be really handy if we actually set out to fix it. We have a considerably simpler test case to work with. We can also infer that there's some interaction between the swift statement and the instantiation of the class, since C-Reduce probably would have removed one of them if it were unnecessary. This would give us some good hints about what might be happening in the compiler to cause this crash.

**Conclusion**  
Blind reduction of a test case is not a very sophisticated debugging technique, but the ability to automate it can make it extremely useful. C-Reduce can be a fantastic addition to your debugging toolbox. It's not suitable for everything, but what is? For problems where it's useful, it can help enormously. It can be a bit tricky to get it to work with multi-file test cases, but some cleverness with the interestingness script solves the problem. Despite the name, it works out of the box on Swift and many other languages, so don't give up on it just because you're not working in C.

That's it for today. Check back next time for more fun, games, and code. Friday Q&A is driven by reader ideas, so if you have something you'd like to see covered here next time or some other time, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2018-06-29-debugging-with-c-reduce.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
