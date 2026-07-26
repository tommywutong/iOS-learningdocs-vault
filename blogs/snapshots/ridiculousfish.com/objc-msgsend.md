---
title: objc_msgSend
source_url: 'https://ridiculousfish.com/blog/posts/objc_msgsend.html'
source_domain: ridiculousfish.com
source_group: single-site
original_language: en
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:ac5d70304bdfb203'
plan_ref: 第三周：Runtime 行为与 Cocoa 对象通信 / Day 1｜把方法调用还原为“查找行为”（对应 W1-03）
plan_week: 第三周：Runtime 行为与 Cocoa 对象通信
plan_day: Day 1｜把方法调用还原为“查找行为”（对应 W1-03）
container: '//div[contains(@class,''content'')]'
container_source: guess
---

> 原文：[objc_msgSend](https://ridiculousfish.com/blog/posts/objc_msgsend.html)

Sending messages can be fun! All you have to do is make a game of it. What kind of game, you ask? Well, for example, we could see how many we can send in four seconds, then try to beat that record. (Apologies to Bart and Principal Skinner.)

Objective-C is a dynamic language. When you send a message to an object, gcc emits a call to objc_msgSend() or one of its specialized, similiar functions. Since every Objective-C message send is funneled through objc_msgSend(), making objc_msgSend() as fast as possible is a priority. Let's see how fast we are and if we could do better.

### Profiling objc_msgSend()

I wrote some code to see how many times Objective-C could call a method in four seconds. I set an alarm using the alarm() function. Then I sent an increment message to an object in a loop until I received the SIGALRM signal, at which point I output how many times the method ran and exit. I compiled it with gcc4 on Tiger using -O3. Here is [my Objective-C code](https://ridiculousfish.com/blog/misc/objc_msg_send_test.html).

Over an average of three runs, I benchmarked 25681135 messages a second. All right.

As Skinner said, let's try to beat that record! And we'll start by profiling. My favorite profiling tool on OS X is, of course, [Shark](http://developer.apple.com/tools/sharkoptimize.html). Let's run it on our executable. Ok, [there we go](https://ridiculousfish.com/blog/images/objc_msgSend_Shark.png). Shark shows that 16% of the time is spent in the increment method itself, 34% of the time is spent in dyld_sub_objc_msgSend(), and 48% is spent in objc_msgSend() itself. What is this dyld_sub_objc_msgSend() function and why does it take so much time?

You may already know. objc_msgSend() is dynamically linked from a dynamic library, namely, libobjc. In order to call the actual objc_msgSend(), the code jumps to a stub function, dyld_stub_objc_msgSend(), which is responsible for loading the actual objc_msgSend() method and jumping to it. As you can see, the stub function is relatively expensive. If we could eliminate the need for it, we could see a performance improvement of up to 33%.

### Plan of attack

Here's one way to get rid of it. Instead of jumping through the stub function, let's grab a pointer to objc_msgSend() itself and always call objc_msgSend() through that pointer. In fact, it's not so different from inlining the stub.

Easier said than done! How will we do this? Well, we could edit the assembly of this little benchmark by hand, or even screw around with the C code, but that's pretty contrived. It would be great if we could make gcc do this work for us.

Yep, we're gonna hack on gcc. Feel free to download it and do it with me! Or just follow along vicariously. For every source file I mention, I will give the path to it in what you just downloaded, and also a link to it on Apple's opensource site.

### Getting the source

Download and extract [Apple's latest public version of gcc](http://www.opensource.apple.com/darwinsource/tarballs/other/gcc-4061.tar.gz). As of this writing, it's gcc-4061. Put it on a volume with enough space. Fully built, gcc will take up almost 1.1 GB.

### Building the source

All extracted? Great. Open up README.Apple in the gcc-4061 directory. It tells you to run two commands:

```
	mkdir -p build/obj build/dst build/sym
        gnumake install RC_OS=macos RC_ARCHS=ppc TARGETS=ppc \
                SRCROOT=`pwd` OBJROOT=`pwd`/build/obj \
                DSTROOT=`pwd`/build/dst SYMROOT=`pwd`/build/sym
```

Guess what? You run the commands. (Notice those are backticks, not single quotes!) Then go get some coffee or something. This may take a while, but we only have to do this once.

Back? Is it done? STILL? Ok, I'll wait.

### Testing our build

Done now? Great. Try it out. Compile something, like [my Objective-C code](https://ridiculousfish.com/blog/?page_id=20), with build/dst/usr/bin/gcc-4.0. Pretty easy:

```
gcc-4061/build/dst/usr/bin/gcc-4.0 -O3 -framework Foundation test1.m ; ./a.out
26129493
```

Great! It works! Now let's see if we can add our optimization.

### Hacking on gcc

All right. So the plan is to grab a pointer to objc_msgSend, stash it in a function pointer variable, and replace calls to the dynamically linked function objc_msgSend() with jumps through the function pointer. We could do it all in the compiler and not have to change a line of our benchmark code, but for now let's just do the last part - replacing calls to objc_msgSend(). We'll set up the variable in our Objective-C code, where it will be easier to tweak.

Man, this gcc thing is one big scary project. How does it all work? It looks like the source code proper is in the gcc-4061/gcc directory. Let's see if we can figure out what gcc does when we send an Objective-C message to an object. We'll start at the beginning, where gcc starts, and trace its control flow down into its depths. What's the beginning? Well, the lexer/parser seems like a reasonable choice. Grep for YACC...bunch of changelogs...ah-ha! [/gcc-4061/gcc/c-parse.in](http://www.opensource.apple.com/darwinsource/10.4.2/gcc-4061/gcc/c-parse.in)!

Ok, we're in. Looks like a pretty standard-issue grammar. This "objcmessageexpr" thing looks promising. Search for it - it leads us to objc_build_message_expr(). grep for that...it's in [/gcc-4061/gcc/objc/objc-act.c](http://www.opensource.apple.com/darwinsource/10.4.2/gcc-4061/gcc/objc/objc-act.c). Hey, check it out - at the top, it says that it implements classes and message passing for Objective-C. We're in the right place.

objc_build_message_expr() calls objc_finish_message_expr() calls build_objc_method_call() calls build_function_call()...wait, back up. That last function call looks like it's actually jumping to the objc_msgSend() function. Look for this:

```
 return build_function_call (t, method_params);
```

Yeah! So t there is the function, either objc_msgSend() or a similar function, and method_params are all the arguments. We want to replace t with our own thing - but only if it's not returning a struct and is not calling super (we'll leave those optimizations for another day).

What should we call our messenger function pointer? Let's call it _messengerFunctionPointer_! That'll do. You can call yours whatever you like, as long as you keep track of it and make the obvious changes.

So make this change. The new code is in red.

```
  /* ??? Selector is not at this point something we can use inside
     the compiler itself.  Set it to garbage for the nonce.  */
  t = build (OBJ_TYPE_REF, sender_cast, method, lookup_object, size_zero_node);
  if (sender == umsg_decl) t = lookup_name(get_identifier("messengerFunctionPointer"));
  return build_function_call (t, method_params);
```

Ok, what the heck does that do? Well, it says that if we're doing an ordinary message send (no struct return, no use of super), to call through whatever is in the variable messengerFunctionPointer instead of the function. Note that the code doesn't actually _make_ the  messengerFunctionPointer variable for us; that's our privilege, in our C code.

What's interesting about this is that we've hooked into gcc's ordinary variable lookup. Our messengerFunctionPointer variable can be local, global, static, extern, whatever, as long as it is somehow visible in the scope of any code that send an Objective-C message.

### We can rebuild it. We have the technology...

That's it! That wasn't so bad. So save the file and rebuild gcc, like you built it before. Since it only has one file to recompile, it won't take long. Here, so you don't have to scroll up:

```
        gnumake install RC_OS=macos RC_ARCHS=ppc TARGETS=ppc \
                SRCROOT=`pwd` OBJROOT=`pwd`/build/obj \
                DSTROOT=`pwd`/build/dst SYMROOT=`pwd`/build/sym
```

### Better...stronger...faster...

All done? Ok, let's try recompiling our code from before.

```
gcc-4061/build/dst/usr/bin/gcc-4.0 -O3 -framework Foundation test1.m
test1.m: In function 'main':
test1.m:29: internal compiler error: Bus error
```

Uh-oh! An ICE! But of course, it's looking for our variable called messengerFunctionPointer, which doesn't exist (and we don't get any warnings since gcc is looking for the variable after it would normally catch undeclared variables.) So let's add it to [my Objective-C code](https://ridiculousfish.com/blog/?page_id=20), and point it at objc_msgSend(), which we have to declare as well.

```
...
void signal_handler(int signal) {
        printf("%d\n", gFoo->val);
        exit(0);
}

id objc_msgSend(id, SEL, ...);
id (*messengerFunctionPointer)(id, SEL, ...) = objc_msgSend;

int main(void) {
        Foo* foo = [[Foo alloc] init];
        gFoo = foo;
        signal(SIGALRM, signal_handler);
...
```

```
gcc-4061/build/dst/usr/bin/gcc-4.0 -O3 -framework Foundation test1.m; ./a.out
35099819
```

It worked! _And it's faster!_ I averaged 34967726 messages a second, a 36% gain - even better than the prediction of 34%. And a session with Shark shows that dyld_stub_objc_msgSend() is no longer being called at all.

### More, more, more!

Can we do even better? Since it has to load the value of the global variable every time you send a message, maybe if we made it const we could see an even bigger benefit?

```
id objc_msgSend(id, SEL, ...);
id (* const messengerFunctionPointer)(id, SEL, ...) = objc_msgSend;
```

```
gcc-4061/build/dst/usr/bin/gcc-4.0 -O3 -framework Foundation test1.m; ./a.out
26488189
```

Wha? Making our variable const made our code SLOWER! What's going on? A quick check of the assembly shows that gcc is performing constant propagation on our const variable, replacing calls through the function pointer to calls to dyld_stub_objc_msgSend() again. It's undoing all of our hard work! (And proving that gcc's well meaning optimizations can, in fact, make things slower.) A simple fix:

```
id objc_msgSend(id, SEL, ...);
id (* const volatile messengerFunctionPointer)(id, SEL, ...) = objc_msgSend;
```

(Holy type qualifier, Batman! Not only did we find a use for volatile, it actually made things faster!)

Is this good for anything else? For one thing, it allows us to very quickly and dynamically switch among various messenger functions, including our own, so that we can do tricks such as additional logging or fancy message forwarding. We could even do something crazy like add [multiple dispatch](http://www.gwydiondylan.org/gdref/tutorial/multiple-dispatch.html). And programs built with this technique should (in principle) be backwards compatible enough to run on previous versions of OS X. Unfortunately, this trick does not affect already-compiled libraries, like AppKit.

### A closer-to-real-life test

For a more realistic example, here's a simple program that [sorts three million objects.](https://ridiculousfish.com/blog/misc/objc_msgsend-sorting-example.html) The optimization (made a little trickier) improves the run time from 17.93 seconds to 15.7 seconds.

Incidentally, the first person to post in the comments the correct explanation for why I didn't use qsort() in the above code wins [my click-pen](https://ridiculousfish.com/blog/images/apple_pen.jpg). Use your real e-mail address for this incredibly cheap swag.

### Disadvantages

Any reasons to not use this trick? Yes, lots. For one thing, my gcc change is a kludge. It generates some spurious warnings and may be incorrect in some cases. If anyone decided to implement this optimization seriously, it would have to be much more robust. For another, [global variables with position independent code isn't pretty](https://ridiculousfish.com/blog/archives/2005/05/29/nil/), and absent a way to get fast access to the variable (such as -mdynamic-no-pic, or making it a local variable, or ensuring it's cached in a register) the optimization will have less impact.

### Conclusion

So to sum up, objc_msgSend() spends a third of its time in its stub function. By tweaking the compiler to always call objc_msgSend() through a function pointer variable, we can eliminate that overhead and open up some interesting possibilities for dynamically modifying message dispatch.
