---
title: 'Friday Q&A 2011-12-02: Object File Inspection Tools'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-12-02-object-file-inspection-tools.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7660bf69495d4314'
translated: false
---

> 原文：[Friday Q&A 2011-12-02: Object File Inspection Tools](https://www.mikeash.com/pyblog/friday-qa-2011-12-02-object-file-inspection-tools.html)　·　mikeash.com Friday Q&A

Posted at 2011-12-02 14:45 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2011-12-16: Disassembling the Assembly, Part 1](https://www.mikeash.com/pyblog/friday-qa-2011-12-16-disassembling-the-assembly-part-1.html)  
Previous article: [Testing Hashcash-Based Anti-Spam Measures](https://www.mikeash.com/pyblog/testing-hashcash-based-anti-spam-measures.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2011-12-02: Object File Inspection Tools

by [Mike Ash](https://www.mikeash.com/)

**The Tools**  
Two of the tools I'm going to discuss today, `otool` and `nm`, come with Xcode, so you probably already have them installed. The other two, `otx` and `class-dump`, are third-party tools you'll have to obtain separately. You can get `otx` here:

[http://otx.osxninja.com/](http://otx.osxninja.com/)

Note that the prepackaged download is a bit old, and in particular doesn't handle `x86_64` binaries, so the best way to get it is to check out the source code from Subversion and build it yourself. You can get `class-dump` here:

[http://www.codethecode.com/projects/class-dump/](http://www.codethecode.com/projects/class-dump/)

Note that this will not be a _comprehensive_ guide to these tools, but rather a tour of some of the more useful facilities that they offer.

**Sample App**  
In order to have something to inspect, I put together a sample application to play with. Here is the code for that:

```
    // clang -framework Cocoa -fobjc-arc test.m

    #import <Cocoa/Cocoa.h>

    @interface MyClass : NSObject
    {
        NSString *_name;
        int _number;
    }

    - (id)initWithName: (NSString *)name number: (int)number;

    @property (strong) NSString *name;
    @property int number;

    @end

    @implementation MyClass

    @synthesize name = _name, number = _number;

    - (id)initWithName: (NSString *)name number: (int)number
    {
        if((self = [super init]))
        {
            _name = name;
            _number = number;
        }
        return self;
    }

    @end

    NSString *MyFunction(NSString *parameter)
    {
        NSString *string2 = [@"Prefix" stringByAppendingString: parameter];
        NSLog(@"%@", string2);
        return string2;
    }

    int main(int argc, char **argv)
    {
        @autoreleasepool
        {
            MyClass *obj = [[MyClass alloc] initWithName: @"name" number: 42];
            NSString *string = MyFunction([obj name]);
            NSLog(@"%@", string);
            return 0;
        }
    }
```

**Library Paths**  
A common source of frustration on the Mac is debugging dynamic linker problems when using embedded frameworks and libraries. The dynamic linker uses paths stored in the various binaries to figure out where to find libraries. Being able to inspect those binaries is extremely useful when debugging these problems.

The `otool -L` command will show all of the libraries a binary links against, as well as where those libraries are expected to be located at runtime. Here's the output of `otool -L` on our sample app:

```
    $ otool -L a.out
    a.out:
        /System/Library/Frameworks/Cocoa.framework/Versions/A/Cocoa (compatibility version 1.0.0, current version 17.0.0)
        /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 159.1.0)
        /usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)
        /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation (compatibility version 150.0.0, current version 635.15.0)
        /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation (compatibility version 300.0.0, current version 833.20.0)
```

We can see that it links against Cocoa, `libSystem` (which contains the standard C library, POSIX functions, and other common code), `libobjc` (the Objective-C runtime), CoreFoundation, and Foundation. We can also see exactly where each one is expected to be when this app is run, as well as the version of each library that was linked against.

This also works on libraries. Let's see what `libSystem` links against:

```
    $ otool -L libSystem.dylib 
    libSystem.dylib:
        /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 159.1.0)
        /usr/lib/system/libcache.dylib (compatibility version 1.0.0, current version 47.0.0)
        /usr/lib/system/libcommonCrypto.dylib (compatibility version 1.0.0, current version 55010.0.0)
        /usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 6.0.0)
        /usr/lib/system/libcopyfile.dylib (compatibility version 1.0.0, current version 85.1.0)
        ...
```

That's a lot of libraries! I snipped out about twenty additional lines. We can see that `libSystem` includes a _lot_ of functionality.

Note how the first line points back to `libSystem` itself. That's because each library contains a reference to its own canonical path, referred to as the "install name". For more details on what all these paths mean and how they work, see my previous article, [Linking and Install Names](http://mikeash.com/pyblog/friday-qa-2009-11-06-linking-and-install-names.html).

**Garbage Collection Support and Other Metadata**  
The `otool -o` command shows various Objective-C metadata, including, perhaps most usefully on the Mac, the binary's garbage collection status. Let's compile the test program with garbage collection and see what the output is:

```
    $ otool -o a.out
    a.out:
    Contents of (__DATA,__objc_classlist) section
    0000000100002080 0x10d2a52bf + 0x100002250
    Contents of (__DATA,__objc_classrefs) section
    0000000100002240 0x10d2a52bf + 0x100002250
    Contents of (__DATA,__objc_superrefs) section
    0000000100002248 0x10d2a52bf + 0x100002250
    Contents of (__DATA,__objc_msgrefs) section
      imp 0x0
      sel 0x100001de9 alloc
    Contents of (__DATA,__objc_imageinfo) section
      version 0
        flags 0x2 OBJC_IMAGE_SUPPORTS_GC
```

The flags at the bottom show that this supports garbage collection. Let's re-run it on the regular ARC version of the binary:

```
    ...
        flags 0x0
```

This isn't something you need often, but it can be invaluable when you're trying to track down why a library or plugin refuses to load. This occasionally appears when using Xcode unit tests. The tests are loaded as a plugin, and garbage collection capability mismatches can cause bizarre errors there.

While we're at it, let's check out the output from `otool -l`, which is a more generalized version of `otool -o` that dumps a lot more info. There's a tremendous amount of output, so I won't print it all, but there are some interesting bits.

Here, we can see the binary specify its dynamic linker:

```
    Load command 7
              cmd LC_LOAD_DYLINKER
          cmdsize 32
             name /usr/lib/dyld (offset 12)
```

It seems that if one wanted to, one could write a different dynamic linker and specify that one instead, although this would no doubt be a huge undertaking.

This section defines the minimum OS requirement:

```
    Load command 9
          cmd LC_VERSION_MIN_MACOSX
      cmdsize 16
      version 10.7
```

Now you know what happens when you set that value in Xcode.

This one defines the full register state for when the app starts:

```
    Load command 10
            cmd LC_UNIXTHREAD
        cmdsize 184
         flavor x86_THREAD_STATE64
          count x86_THREAD_STATE64_COUNT
       rax  0x0000000000000000 rbx 0x0000000000000000 rcx  0x0000000000000000
       rdx  0x0000000000000000 rdi 0x0000000000000000 rsi  0x0000000000000000
       rbp  0x0000000000000000 rsp 0x0000000000000000 r8   0x0000000000000000
        r9  0x0000000000000000 r10 0x0000000000000000 r11  0x0000000000000000
       r12  0x0000000000000000 r13 0x0000000000000000 r14  0x0000000000000000
       r15  0x0000000000000000 rip 0x0000000100001880
    rflags  0x0000000000000000 cs  0x0000000000000000 fs   0x0000000000000000
        gs  0x0000000000000000
```

You may have wondered, just what is the initial state of an executing program when it first starts running? Well, now you know: the registers contain these values. Or perhaps different ones, depending on what the linker put in there when you built your app.

**Symbols**  
It's often useful to see exactly what symbols are present in a binary. The `nm` command displays these. Here's the result of running `nm` on the test app:

```
    0000000100001a90 t -[MyClass .cxx_destruct]
    00000001000018c0 t -[MyClass initWithName:number:]
    00000001000019c0 t -[MyClass name]
    0000000100001a40 t -[MyClass number]
    00000001000019f0 t -[MyClass setName:]
    0000000100001a60 t -[MyClass setNumber:]
    0000000100001ad0 T _MyFunction
                     U _NSLog
    0000000100002350 S _NXArgc
    0000000100002358 S _NXArgv
    0000000100002290 S _OBJC_CLASS_$_MyClass
                     U _OBJC_CLASS_$_NSObject
    00000001000022e0 S _OBJC_IVAR_$_MyClass._name
    00000001000022e8 S _OBJC_IVAR_$_MyClass._number
    00000001000022b8 S _OBJC_METACLASS_$_MyClass
                     U _OBJC_METACLASS_$_NSObject
                     U ___CFConstantStringClassReference
    0000000100002368 S ___progname
    0000000100000000 A __mh_execute_header
                     U __objc_empty_cache
                     U __objc_empty_vtable
    0000000100002360 S _environ
                     U _exit
    0000000100001b70 T _main
                     U _objc_autoreleasePoolPop
                     U _objc_autoreleasePoolPush
                     U _objc_autoreleaseReturnValue
                     U _objc_getProperty
                     U _objc_msgSend
                     U _objc_msgSendSuper2
                     U _objc_msgSend_fixup
                     U _objc_release
                     U _objc_retain
                     U _objc_retainAutoreleasedReturnValue
                     U _objc_setProperty
                     U _objc_storeStrong
    0000000100002000 s _pvars
                     U dyld_stub_binder
    0000000100001880 T start
```

We get an interesting mix of obvious and less-obvious symbols. Most of the `MyClass` symbols are methods we wrote. The `-[MyClass .cxx_destruct]` method is generated by the compiler. It was originally intended for calling C++ destructors (thus `cxx`) but now serves double duty as the method where ARC disposes of your strong instance variables.

The first column of the output is the address of the symbol, and the last column is the name, but what's the second column? This is the symbol's type. The symbols marked as `T` indicate symbols that are in the text section, which is the strange name given to the section which contains the program's executable code. The symbols marked as `t` are also in the text section, but are not visible outside the binary where they're stored. Symbols marked `U` are "undefined", which means that they are expected to be found in another library when the program is run. If you look at this listing, you'll see that all of the `U` symbols are functions and classes which come from Cocoa, the Objective-C runtime, or `libSystem`. The `nm` man page has a complete listing of what these type letters mean.

Examining the symbols in a library can be really useful for figuring out linker errors. For this, we don't care about symbols which are local to the library, only those which are visible to the outside world. The `nm -g` flag filters out all local symbols, giving you a less cluttered list to examine when tracking down these errors.

**Class Dumps**  
There's tons of useful information available, but some of it can be difficult to decode. When you're trying to figure out the guts of some Objective-C code, it can be nice to have all of the information presented in a more familiar manner. Fortunately, there's enough metadata stored in the binary to allow completely reconstructing an `@interface` of a class. The `class-dump` tool does exactly that. Let's run this tool on the test app and see what it produces (block comments omitted for brevity):

```
    $ class-dump a.out
    ...
    @interface MyClass : NSObject
    {
        NSString *_name;
        int _number;
    }

    @property int number; // @synthesize number=_number;
    @property(retain) NSString *name; // @synthesize name=_name;
    - (void).cxx_destruct;
    - (id)initWithName:(id)arg1 number:(int)arg2;

    @end
```

There's the whole interface to our test class laid out in valid Objective-C. Of course you don't get an `@implementation`, which would be much more complicated. You also lose parameter names, but the descriptiveness of Objective-C method names usually makes it clear enough what the parameters are.

Dumping out your own code is not all that interesting. Running `class-dump /System/Library/Frameworks/AppKit.framework/AppKit` produces much more interesting results. Here's an amusing excerpt from the massive quantity of data that results:

```
    @interface NSStopTouchingMeBox : NSBox
    {
        NSView *sibling1;
        NSView *sibling2;
        double offset;
    }

    - (id)initWithFrame:(struct CGRect)arg1;
    - (void)setSibling1:(id)arg1;
    - (void)setSibling2:(id)arg1;
    - (void)setFrameSize:(struct CGSize)arg1;
    - (void)setOffset:(double)arg1;
    - (void)tile;
    - (void)viewDidEndLiveResize;

    @end
```

Of course, you should never ship code that uses the private classes and methods that you'll discover, but it can still be very interesting and even useful to see these internals.

**Disassembly**  
Now we finally reach the juicy part. That which separates the men from the boys. Where few dare to tread. The howling darkness. The tangible substance of earth's supreme terror. Abandon hope all ye who enter here.

Now that we've gotten rid of all the lightweights, let's proceed.

As you probably already know, compiled Objective-C code consists of machine code. This is raw bytes that are executed directly by your computer's CPU. It's extremely tedious to manually interpret.

Between Objective-C and machine code is assembly language. This is a low level language which translates more or less directly to machine code, but is, relatively speaking, much more readable. This translation goes both ways: you can take machine code and turn it back into somewhat more readable assembly code.

I don't plan to provide a comprehensive guide on reading and interpreting assembly, but I will show how to obtain it and give a few handy pointers.

You can disassemble a binary using the `otool -tV` command. The `t` flag tells `otool` to display the text segment (where the code lives), and the `V` flag tells `otool` to disassemble it.

The output of `otool -tV` omits some useful data, however. For example, here's a snippet from the disassembly of the test app's `main` function:

```
    0000000100001bdd    callq   0x100001c90 ; symbol stub for: _objc_msgSend
    0000000100001be2    movq    %rax,0xe8(%rbp)
    0000000100001be6    movq    0xe8(%rbp),%rax
    0000000100001bea    movq    0x0000066f(%rip),%rsi
    0000000100001bf1    movq    %rax,%rdi
    0000000100001bf4    callq   0x100001c90 ; symbol stub for: _objc_msgSend
```

We can see two calls to `objc_msgSend`, the function that's used to send Objective-C messages, but we can't really see any other information about those calls. It turns out that for just about all message sends, it's usually possible to figure out which selector was being sent as well, which is tremendously useful.

Enter `otx`. This is a third-party wrapper around `otool` which adds better annotations to the output, including Objective-C message send selectors. Simply run `otx` on a binary (after obtaining it from the site discussed at the beginning of this article) and out comes the disassembly, fully annotated. I like to add the `-b` flag, which tells `otx` to add a blank line between logical blocks of instructions, making it much easier to see the structure of the code. Here's the above section of code disassembled by `otx`:

```
      +109  0000000100001bdd  e8ae000000                callq       0x100001c90                   -[%rdi initWithName:number:]
      +114  0000000100001be2  488945e8                  movq        %rax,0xe8(%rbp)
      +118  0000000100001be6  488b45e8                  movq        0xe8(%rbp),%rax
      +122  0000000100001bea  488b356f060000            movq        0x0000066f(%rip),%rsi         name
      +129  0000000100001bf1  4889c7                    movq        %rax,%rdi
      +132  0000000100001bf4  e897000000                callq       0x100001c90                   -[%rdi name]
```

Now we can see the methods in question, not just the fact that a message send is occurring. Instead of a relatively opaque disassembly like before, we can now see that this section of code simply calls the initializer and then the `name` accessor.

Let's check out the annotated disassembly of the `initWithName:number:` method:

```
    -[MyClass initWithName:number:]:
        +0  00000001000018c0  55                        pushq       %rbp
        +1  00000001000018c1  4889e5                    movq        %rsp,%rbp
        +4  00000001000018c4  4883ec60                  subq        $0x60,%rsp
        +8  00000001000018c8  488d45f0                  leaq        0xf0(%rbp),%rax
       +12  00000001000018cc  4c8d45c8                  leaq        0xc8(%rbp),%r8
       +16  00000001000018d0  48897df0                  movq        %rdi,0xf0(%rbp)
       +20  00000001000018d4  488975e8                  movq        %rsi,0xe8(%rbp)
       +24  00000001000018d8  4889d7                    movq        %rdx,%rdi
       +27  00000001000018db  894dc0                    movl        %ecx,0xc0(%rbp)
       +30  00000001000018de  4c8945b8                  movq        %r8,0xb8(%rbp)
       +34  00000001000018e2  488945b0                  movq        %rax,0xb0(%rbp)
       +38  00000001000018e6  e8b7030000                callq       0x100001ca2                   _objc_retain
       +43  00000001000018eb  488945e0                  movq        %rax,0xe0(%rbp)
       +47  00000001000018ef  8b4dc0                    movl        0xc0(%rbp),%ecx
       +50  00000001000018f2  894ddc                    movl        %ecx,0xdc(%rbp)
       +53  00000001000018f5  488b45f0                  movq        0xf0(%rbp),%rax
       +57  00000001000018f9  48c745f000000000          movq        $0x00000000,0xf0(%rbp)
       +65  0000000100001901  488945c8                  movq        %rax,0xc8(%rbp)
       +69  0000000100001905  488b057c090000            movq        0x0000097c(%rip),%rax
       +76  000000010000190c  488945d0                  movq        %rax,0xd0(%rbp)
       +80  0000000100001910  488b3531090000            movq        0x00000931(%rip),%rsi         init
       +87  0000000100001917  488b7db8                  movq        0xb8(%rbp),%rdi
       +91  000000010000191b  e876030000                callq       0x100001c96                   -[[%rdi super] init]
       +96  0000000100001920  4889c2                    movq        %rax,%rdx
       +99  0000000100001923  488955f0                  movq        %rdx,0xf0(%rbp)
      +103  0000000100001927  488b55b0                  movq        0xb0(%rbp),%rdx
      +107  000000010000192b  4889c6                    movq        %rax,%rsi
      +110  000000010000192e  4889d7                    movq        %rdx,%rdi
      +113  0000000100001931  488945a8                  movq        %rax,0xa8(%rbp)
      +117  0000000100001935  e87a030000                callq       0x100001cb4                   _objc_storeStrong
      +122  000000010000193a  488b45a8                  movq        0xa8(%rbp),%rax
      +126  000000010000193e  483d00000000              cmpq        $0x00000000,%eax
      +132  0000000100001944  0f8430000000              je          0x10000197a                   return;

      +138  000000010000194a  488b45e0                  movq        0xe0(%rbp),%rax
      +142  000000010000194e  488b4df0                  movq        0xf0(%rbp),%rcx
      +146  0000000100001952  488b1587090000            movq        0x00000987(%rip),%rdx         _name
      +153  0000000100001959  4801ca                    addq        %rcx,%rdx
      +156  000000010000195c  4889d7                    movq        %rdx,%rdi
      +159  000000010000195f  4889c6                    movq        %rax,%rsi
      +162  0000000100001962  e84d030000                callq       0x100001cb4                   _objc_storeStrong
      +167  0000000100001967  448b45dc                  movl        0xdc(%rbp),%r8d
      +171  000000010000196b  488b45f0                  movq        0xf0(%rbp),%rax
      +175  000000010000196f  488b0d72090000            movq        0x00000972(%rip),%rcx         _number
      +182  0000000100001976  44890408                  movl        %r8d,(%rax,%rcx)

      +186  000000010000197a  488b45f0                  movq        0xf0(%rbp),%rax
      +190  000000010000197e  4889c7                    movq        %rax,%rdi
      +193  0000000100001981  e81c030000                callq       0x100001ca2                   _objc_retain
      +198  0000000100001986  488945f8                  movq        %rax,0xf8(%rbp)
      +202  000000010000198a  c745c401000000            movl        $0x00000001,0xc4(%rbp)
      +209  0000000100001991  488b45e0                  movq        0xe0(%rbp),%rax
      +213  0000000100001995  4889c7                    movq        %rax,%rdi
      +216  0000000100001998  e8ff020000                callq       0x100001c9c                   _objc_release
      +221  000000010000199d  488b45f0                  movq        0xf0(%rbp),%rax
      +225  00000001000019a1  4889c7                    movq        %rax,%rdi
      +228  00000001000019a4  e8f3020000                callq       0x100001c9c                   _objc_release
      +233  00000001000019a9  488b45f8                  movq        0xf8(%rbp),%rax
      +237  00000001000019ad  4883c460                  addq        $0x60,%rsp
      +241  00000001000019b1  5d                        popq        %rbp
      +242  00000001000019b2  c3                        ret
```

There are a lot of stuff in here that would take quite a while to analyze, but simply from looking at the annotations and basic control flow, we can still see a lot. It's particularly interesting to examine code compiled with ARC, since all of the extra memory management calls inserted by ARC show up in the dump.

After the initial setup, this code calls `objc_retain`. Given the context, we can deduce that this is a call to retain the `name` parameter, which ARC does in order to ensure that the `name` object remains live even if subsequent code zeroes out all other strong references to it. We can verify that it is indeed the `name` parameter by looking at the `movq %rdx,%rdi` instruction a couple of lines prior. `%rdx` contains the third parameter to a function, or the first explicit Objective-C method parameter, which in this case is `name`. `%rdi` contains the first parameter to a function. So this code moves `name` into the spot where `objc_retain` will expect to find its parameter.

Next comes the call to `[super init]`. The annotation is a little confusing here, but `-[[%rdi super] init]` means that a `super` call is being made with the object stored in `%rdi` as the target of the call. In this case, we know that's `self`, which should be the case for any `super` call.

After that, there's a call to `objc_storeStrong`. This one is a little strange. After considerable investigation, it appears that this call is a redundant assignment to `self` after the call to `super` completes, and after the `=` assignment in the source code takes place. This call disappears when the code is compiled with optimizations, so it seems to be bit of ARC defensiveness that doesn't actually need to be there in this case.

Next, there's a compare and then a conditional jump. This is the `if` statement. If the return value is `nil`, then control jumps down to the third block of code, otherwise control continues with the second block of code. In the second block of code, we can see the two instance variable assignments, with the assignment to `_name` using a call to `objc_storeStrong` that's actually useful this time. Since `_number` is just an `int`, it doesn't need any fancy calls.

Finally, we do a bit of memory management and then return. There's a redundant pair of `objc_retain`/`objc_release`, which again appears to be ARC defensiveness leaking out (and which also disappears under optimizations), an `objc_release` on the `name` parameter to balance the `objc_retain` at the beginning of the function, and then control is returned to the caller.

Even without understanding the meaning and purpose of every single instruction, we can still get a lot out of this dump. This can be incredibly useful for checking into possible compiler bugs or figuring out how some Cocoa method works on the inside.

**Conclusion**  
We've taken a tour of several different facilities for inspecting executables, libraries, and plugins. Whether you're tracking down library paths, figuring out missing symbols, or diving into the disassembly of a problematic method, the developer tools (and third parties) provide ways to get a huge amount of information. There's more out there as well, and this is just a sampling of the parts I find most useful. Whenever you have a mysterious problem, don't be afraid to dive in and figure out exactly what's happening underneath the covers. Being able to inspect low-level information can often make the difference between a frustratingly difficult bug and a trivial one.

That wraps things up for today. Friday Q&A relies on you, the reader, for a steady supply of interesting subjects to discuss. If you have a topic that you'd like to see written up, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
