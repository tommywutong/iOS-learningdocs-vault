---
title: 'Friday Q&A 2009-06-05: Introduction to Valgrind'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-06-05-introduction-to-valgrind.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:371d8e927e288d69'
translated: false
---

> 原文：[Friday Q&A 2009-06-05: Introduction to Valgrind](https://www.mikeash.com/pyblog/friday-qa-2009-06-05-introduction-to-valgrind.html)　·　mikeash.com Friday Q&A

Posted at 2009-06-05 15:55 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-06-19: Mac OS X Process Memory Statistics](https://www.mikeash.com/pyblog/friday-qa-2009-06-19-mac-os-x-process-memory-statistics.html)  
Previous article: [Friday Q&A 2009-05-22: Objective-C Class Loading and Initialization](https://www.mikeash.com/pyblog/friday-qa-2009-05-22-objective-c-class-loading-and-initialization.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [valgrind](https://www.mikeash.com/pyblog/?tag=valgrind)

Friday Q&A 2009-06-05: Introduction to Valgrind

by [Mike Ash](https://www.mikeash.com/)

**What It Is**  
 A few months ago I talked about the [Clang Static Analyzer](https://www.mikeash.com/pyblog/friday-qa-2009-03-06-using-the-clang-static-analyzer.html) and how it could help you find bugs in your code. Valgrind is a similar sort of program except it checks for errors at runtime instead.

There's an entire class of bugs which are easy to write and difficult to track down in C-based languages, such as reading from uninitialized memory or writing past the end of an array. Reading from uninitialized memory just gives junk values and a lot of times those junk values actually work. Writing past the end of an array is frequently harmless since arrays are generally backed by storage that's larger than what was requested. Because of this, these code bugs might only show up as crashes rarely. For really bad ones, they never crash, but just cause bad behavior. Figuring out what piece of code is causing the misbehavior can be extremely difficult.

Thus Valgrind. The way it works is it essentially runs your program inside an emulator. By doing this, it has total control over everything your program does. Something that's undetectable when running on the processor, like reading from a memory location that was never initialized, suddenly becomes easy to see.

There are some downsides to this approach. The most obvious one is that the target program runs about an order of magnitude slower than it normally would, due to being run under emulation. A less obvious downside is that Valgrind needs to know the behavior of every syscall in order to make everything work properly, and right now on the Mac there are some missing ones. For example, QuickTime uses the `aio` family of functions which aren't currently supported by Valgrind, so QuickTime won't work. Still, lots of things _do_ work, and you can run an entire Cocoa application under Valgrind.

**How to Get It**  
 Valgrind's Mac support has only recently been merged into their main code repository, and is not yet available as an official release. This means that, for now, the only way to get it is by pulling down their subversion repository:

```
    $ svn co svn://svn.valgrind.org/valgrind/trunk valgrind
```

From there, building it is like any other UNIX program. Read the

or just do this:

```
    $ cd valgrind
    $ ./autogen.sh
    $ ./configure
    $ make
    $ sudo make install
```

At this point you should be able to run Valgrind. You can give it a quick test by just typing

in the shell. Note that as far as I know, Valgrind for Mac only works on Intel machines. If you have a PowerPC Mac you're probably out of luck, although there's no harm in trying.

```
    $ sudo /usr/local/hermes/bin/hermesctl unload
```

And when you're done using Valgrind, you can re-enable it like so:

```
    $ sudo /usr/local/hermes/bin/hermesctl load
```

**Finding Bugs**  
 Let's take a look at this example program:

```
    #include <stdlib.h>
    #include <stdio.h>
    #include <string.h>
    
    char *bad_strdup(char *s)
    {
        char *ret = malloc(strlen(s));
        strcpy(ret, s);
        return ret;
    }
    
    int main(int argc, char **argv)
    {
        char *str = "hello world";
        char *str2 = bad_strdup(str);
        int i;
        printf("%s\n", str2);
        printf("%d\n", i);
        free(str2);
        return 0;
    }
```

This program contains two bugs. One of them is really obvious: it prints the value of

at the end, even though that variable was never initialized. One of them is more subtle:

doesn't allocate enough memory to hold the

byte at the end of the string. This would normally go undetected, because memory allocations are padded, and that extra byte is often available. It would only fail when the string length were a nice round number, and even then it might simply fail by overwriting something else and causing corrupted data far later.

Let's compile and run with Valgrind:

```
    $ gcc -g valgrind.c
    $ valgrind ./a.out
    ==4296== Memcheck, a memory error detector.
    ==4296== Copyright (C) 2002-2009, and GNU GPL'd, by Julian Seward et al.
    ==4296== Using LibVEX rev 1899, a library for dynamic binary translation.
    ==4296== Copyright (C) 2004-2009, and GNU GPL'd, by OpenWorks LLP.
    ==4296== Using valgrind-3.5.0.SVN, a dynamic binary instrumentation framework.
    ==4296== Copyright (C) 2000-2009, and GNU GPL'd, by Julian Seward et al.
    ==4296== For more details, rerun with: -v
    ==4296== 
    ==4296== Invalid write of size 1
    ==4296==    at 0x18B9E: strcpy (mc_replace_strmem.c:303)
    ==4296==    by 0x1F8C: bad_strdup (valgrind.c:8)
    ==4296==    by 0x1FB6: main (valgrind.c:15)
    ==4296==  Address 0x3ec35b is 0 bytes after a block of size 11 alloc'd
    ==4296==    at 0x15516: malloc (vg_replace_malloc.c:193)
    ==4296==    by 0x1F77: bad_strdup (valgrind.c:7)
    ==4296==    by 0x1FB6: main (valgrind.c:15)
    ==4296== 
    ==4296== Invalid read of size 1
    ==4296==    at 0x17BB1: strlen (mc_replace_strmem.c:275)
    ==4296==    by 0x268125: puts (in /usr/lib/libSystem.B.dylib)
    ==4296==    by 0x1FC4: main (valgrind.c:17)
    ==4296==  Address 0x3ec35b is 0 bytes after a block of size 11 alloc'd
    ==4296==    at 0x15516: malloc (vg_replace_malloc.c:193)
    ==4296==    by 0x1F77: bad_strdup (valgrind.c:7)
    ==4296==    by 0x1FB6: main (valgrind.c:15)
    hello world
    ==4296== 
    ==4296== Conditional jump or move depends on uninitialised value(s)
    ==4296==    at 0x1F8E5E: __vfprintf (in /usr/lib/libSystem.B.dylib)
    ==4296==    by 0x22CE66: vfprintf_l (in /usr/lib/libSystem.B.dylib)
    ==4296==    by 0x251FBA: printf (in /usr/lib/libSystem.B.dylib)
    ==4296==    by 0x1FD9: main (valgrind.c:18)
    ==4296== 
    ==4296== Conditional jump or move depends on uninitialised value(s)
    ==4296==    at 0x2C9A66: __ultoa (in /usr/lib/libSystem.B.dylib)
    ==4296==    by 0x1FA305: __vfprintf (in /usr/lib/libSystem.B.dylib)
    ==4296==    by 0x22CE66: vfprintf_l (in /usr/lib/libSystem.B.dylib)
    ==4296==    by 0x251FBA: printf (in /usr/lib/libSystem.B.dylib)
    ==4296==    by 0x1FD9: main (valgrind.c:18)
    ...
```

I've snipped off the report here even though it goes on quite a bit longer. The important stuff is here. First, we see an invalid write past the end of the memory block. It says how big the write is, the exact stack trace where it happened, the address where it happened, how big the block really was, and where it was allocated. This is all incredibly useful stuff. Following that we get an invalid read because we then print that string and it ends up reading this same memory location.

After that you can see it successfully printing "hello world", then it tries to print the uninitialized `i`, which it immediately catches and complains about. Valgrind appears to cascade the uninitialized state of memory as that memory moves around, as it complains about uninitialized memory access many, many times during the course of printing (most of which I cut out for the sake of brevity). This bug manifests in an obvious way here, but it's not uncommon to have uninitialized variable reads which cause much more subtle bugs than this.

**Conclusion**  
 It's easy to write extremely difficult bugs in C and C-based languages, and Valgrind is an incredibly useful tool for discovering and tracking down these bugs, and we're fortunate to have a tool of this caliber available on the Mac.

That wraps up this edition of Friday Q&A. Come back... well, probably in two weeks for another exciting installment.

As always, Friday Q&A is powered by your suggestions. If you have a topic you would like to see discussed here, post it below or [e-mail it to me](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
