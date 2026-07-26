---
title: block proxying
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-10-28-generic-block-proxying.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:617bb0aa557b7a9f'
translated: false
---

> 原文：[block proxying](https://www.mikeash.com/pyblog/friday-qa-2011-10-28-generic-block-proxying.html)　·　mikeash.com Friday Q&A

Posted at 2011-10-28 13:57 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2011-11-11: Building a Memoizing Block Proxy](https://www.mikeash.com/pyblog/friday-qa-2011-11-11-building-a-memoizing-block-proxy.html)  
Previous article: [Friday Q&A 2011-10-14: What's New in GCD](https://www.mikeash.com/pyblog/friday-qa-2011-10-14-whats-new-in-gcd.html)  
Tags: [blocks](https://www.mikeash.com/pyblog/?tag=blocks) [evil](https://www.mikeash.com/pyblog/?tag=evil) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hack](https://www.mikeash.com/pyblog/?tag=hack) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2011-10-28: Generic Block Proxying

by [Mike Ash](https://www.mikeash.com/)

**What It Means**  
In Objective-C, it's possible to intercept messages. Any message sent to an object that isn't implemented gets an `NSInvocation` object constructed, and that is then sent to `forwardInvocation:`. In there, you can do whatever you like with the message, like messing with its parameters before passing it on to another object, or sending it over a network.

The most common use for this facility is to write a proxy class which doesn't implement much of anything. Nearly any message sent to it will be caught by the forwarding mechanism, and the proxy can then do clever things with any message, while still mostly acting like the object being proxied. This is useful for building things like [transparent futures](https://github.com/mikeash/MAFuture) and [transparent zeroing weak references](https://github.com/mikeash/MAZeroingWeakRef/blob/master/Source/MAZeroingWeakProxy.h).

Block proxying is much the same, but with blocks instead of objects. You wrap an arbitrary block with another block which is able to intercept the call and interfere as it sees fit.

The technique I'm about to present works well, but it's definitely _not_ supported and should not be used in real code. It relies on private APIs and private quirks of public APIs. It's an interesting experiment, not a stable library.

**Code**  
As usual, the code is available on GitHub. Today's journey into the forbidding depths can be found here:

[https://github.com/mikeash/MABlockForwarding](https://github.com/mikeash/MABlockForwarding)

**Theory**  
Objective-C message dispatch works by taking the selector and the class and looking up the method in the class that corresponds to that selector. More specifically, it looks up the function, or `IMP`, that actually implements the method, then calls that function.

Message forwarding hooks right into this system. When looking up a function, if no method is found in the class, a special forwarding `IMP` is returned. That function takes care of all the painful and platform-specific details of how to turn a function call into an `NSInvocation` object.

If we can obtain this special forwarding `IMP` then we can build a fake block around it and accomplish our goal of forwarding blocks. Turns out that the special forwarding `IMP` is really easy to obtain. All you need to do is ask the system for the `IMP` for an unimplemented selector. There are several ways to do this, but the easiest is to simply call `[self methodForSelector:...]` and pass a selector you know doesn't exist in the class.

A block is just an Objective-C object with a function pointer in the right place. To call the block, the compiler calls the function pointer and passes the object as the first parameter. We can construct an Objective-C object with a pointer to the forwarding `IMP` in the right place, and the forwarding machinery will kick into action, build an `NSInvocation`, and then call our `forwardInvocation:` method.

The forwarding machinery needs the method signature of the method being called in order to know how to package the arguments. Fortunately, with reasonably recent compilers, blocks embed signature information in the same format.

Forwarding deals with messages, which have two implicit arguments: the object and the selector. Blocks only have one implicit argument: the block object. The second argument to a block can be anything, or not even exist at all (for a block with no parameters). Fortunately, the forwarding function doesn't seem to care about the type of the second parameter, as long as it's present. For blocks that don't have a second parameter, a fake one can be inserted into the signature without screwing things up.

**Implementation**  
The goal is to build this function:

```
    typedef void (^BlockInterposer)(NSInvocation *inv, void (^call)(void));

    id MAForwardingBlock(BlockInterposer interposer, id block);
```

`MAForwardingBlock` takes two parameters. The first is the interposer block, which is the block which is called to handle the invocation. The second is the original block to wrap. The interposer gets a block as a parameter which, when called, will call through to the original block using the `NSInvocation` as the parameters. The function returns a new block which forwards calls to the interposer block passed in.

The first thing to do is to create a new class which will pretend to be a block. Instances of this class will act like blocks and will handle all of the proxying duties. The layout of this class needs to be compatible with the layout of a block. A block contains five fields which can then be followed by other data. There's an `isa` field (necessary for it to work as an Objective-C object), flags, some reserved space, the block's function pointer, and a pointer to a block descriptor which contains other useful information about the block.

The `isa` field is already taken care of, and then the rest can be laid out as instance variables. After the block fields are laid out, other data can follow. In this case, the class stores the interposer block and the original block as instance variables after the block fields:

```
    @interface MAFakeBlock : NSObject
    {
        int _flags;
        int _reserved;
        IMP _invoke;
        struct BlockDescriptor *_descriptor;

        id _forwardingBlock;
        BlockInterposer _interposer;
    }
```

This class has a single method in its interface, an initializer:

```
    - (id)initWithBlock: (id)block interposer: (BlockInterposer)interposer;
```

Everything else happens through block calling conventions and forwarding, so nothing else needs to be done. The implementation for this method copies and stores the two blocks passed in, and then sets the `invoke` field to the forwarding `IMP` by fetching a method that isn't implemented:

```
    - (id)initWithBlock: (id)block interposer: (BlockInterposer)interposer
    {
        if((self = [super init]))
        {
            _forwardingBlock = [block copy];
            _interposer = [interposer copy];
            _invoke = [self methodForSelector: @selector(thisDoesNotExistOrAtLeastItReallyShouldnt)];
        }
        return self;
    }
```

With everything now set up, whenever an instance of `MAFakeBlock` is called like a block, it will end up going through the regular Objective-C forwarding machinery. There are two steps in the general forwarding path: first, the runtime fetches the method signature using `methodSignatureForSelector:`, then it constructs an `NSInvocation` and calls `forwardInvocation:`.

To figure out the method signature to give to the runtime, we first need to get the method signature of the block being wrapped. This is done by delving into that `BlockDescriptor` structure and pulling out the signature. The details are a bit boring, and I'm going to skip over them and simply assume that there's a `BlockSig` function which takes a block and returns its signature as a C string. For the curious, the code is [on GitHub](https://github.com/mikeash/MABlockForwarding/blob/master/MABlockForwarding.m#L26).

`NSMethodSignature` provides a method to get a signature object from a C string, `+signatureWithObjCTypes:`. The only wrinkle is that the forwarding machinery will crash if the provided signature doesn't have at least two objects. To fix that, I fake it by adding extra fake `void *` parameters to the signature so that it has at least the required number of parameters. These extra parameters are harmless, although they will be filled with random junk from registers or the stack. The `methodSignatureForSelector:` implementation then looks like this:

```
    - (NSMethodSignature *)methodSignatureForSelector: (SEL)sel
    {
        const char *types = BlockSig(_forwardingBlock);
        NSMethodSignature *sig = [NSMethodSignature signatureWithObjCTypes: types];
        while([sig numberOfArguments] < 2)
        {
            types = [[NSString stringWithFormat: @"%s%s", types, @encode(void *)] UTF8String];
            sig = [NSMethodSignature signatureWithObjCTypes: types];
        }
        return sig;
    }
```

The implementation of `-forwardInvocation:` is then pretty simple. Change the invocation's target to the original block, then call the interposer:

```
    - (void)forwardInvocation: (NSInvocation *)inv
    {
        [inv setTarget: _forwardingBlock];
        _interposer(inv, ^{
```

The call block that gets passed to the interposer is a bit tricky. In its public interface, `NSInvocation` only provides methods to invoke it with a particular selector, which goes through `objc_msgSend`. This is no good for calling a block, of course.

Fortunately, there's a private method called `invokeUsingIMP:`. This bypasses `objc_msgSend` and simply calls the provided `IMP`. In practice, it'll call any arbitrary function pointer, as long as it's compatible with the signature that it has. We can then pass it the function pointer for the inner block, and off we go:

```
            [inv invokeUsingIMP: BlockImpl(_forwardingBlock)];
        });
    }
```

Again, I use a little helper function here to deal with internal block structure. `BlockImpl` fetches the function pointer out of a block. This one is really simple: it just interprets the object as a block structure and fetches the `invoke` field. If want to see it, [the code is available](https://github.com/mikeash/MABlockForwarding/blob/master/MABlockForwarding.m#L12).

All that remains for this class is a dummy implementation of `copyWithZone:`, since blocks are copied a lot. Nothing has to be done for this implementation besides retaining the fake block, since there isn't any mutable state in this class:

```
    - (id)copyWithZone: (NSZone *)zone
    {
        return [self retain];
    }
```

Now that this class is complete, all that remains is the implementation of `MAForwardingBlock`. All this function has to do is create and return a new instance of the fake block class, properly initialized:

```
    id MAForwardingBlock(BlockInterposer interposer, id block)
    {
        return [[[MAFakeBlock alloc] initWithBlock: block interposer: interposer] autorelease];
    }
```

That's it! Now we can proxy blocks. Here's a silly example:

```
    void (^block)(int) = ForwardingBlock(^(NSInvocation *inv, void (^call)(void)) {
        [inv setArgument: &(int){ 4242 } atIndex: 1];
        call();
    }, ^(int testarg){
        NSLog(@"%d %d", argc, testarg);
    });
    block(42);
```

Even though the block is called with `42`, the call actually prints `4242`, since the interposing block changes the argument before calling the original block.

Since this code leverages Cocoa's forwarding machinery, it will work with nearly any block taking nearly any combination of parameters and return values, not just simple `int` blocks. It suffers from the same limitations of Cocoa's forwarding, of course. In particular, it's not able to handle blocks that take variable arguments or unions. It also doesn't deal with the peculiarities of struct returns. Because of how struct returns work on most architectures, there's actually a separate forwarding `IMP` for those. To work with struct returns, this code would have to detect whether the block signature uses the struct return calling convention and fetch that separate `IMP` instead.

**Conclusion**  
Understanding how mechanisms like message forwarding work at a low level makes it possible to twist them to do entirely new things. Sometimes you get something really useful. Sometimes you just get an interesting toy that can't really be used in real code. While this one is just a toy, it's still an interesting exploration of the guts of the system, and this sort of thing can often lead to real, solid, useful code later on.

That's it for today. Come back in two weeks when I discuss how to use this block proxying code to implement [memoization](http://en.wikipedia.org/wiki/Memoization). Until then, keep sending your ideas for topics. With the occasional exception, Friday Q&A is driven by reader suggestions, so if you have a topic that you would like to see covered here, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
