---
title: 'Friday Q&A 2009-03-27: Objective-C Message Forwarding'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-03-27-objective-c-message-forwarding.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:13664c1b4e8f69f3'
translated: false
---

> 原文：[Friday Q&A 2009-03-27: Objective-C Message Forwarding](https://www.mikeash.com/pyblog/friday-qa-2009-03-27-objective-c-message-forwarding.html)　·　mikeash.com Friday Q&A

Posted at 2009-03-27 16:50 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-04-03: On Hold](https://www.mikeash.com/pyblog/friday-qa-2009-04-03-on-hold.html)  
Previous article: [Friday Q&A 2009-03-20: Objective-C Messaging](https://www.mikeash.com/pyblog/friday-qa-2009-03-20-objective-c-messaging.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2009-03-27: Objective-C Message Forwarding

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Chinese (translation by neoman)](https://github.com/0oneo/iOSArchive/wiki/%E7%BF%BB%E8%AF%91-Objective-C-Message-Forwarding).

**No Such Method**  
 [Last week](https://www.mikeash.com/pyblog/friday-qa-2009-03-20-objective-c-messaging.html) I talked about how Objective-C messaging works, and mentioned that interesting things happen when no method is found for a given selector. Those interesting things are what make forwarding happen.

(If you aren't totally clear on what a **selector** is or what the difference is between a **method** and a **message**, you might want to go read through that article real quick, or at least re-read the Definitions section if you already read it.)

Just what is message forwarding? Simply speaking, it allows unknown messages to be trapped and reacted to. In other words, any time an unknown message is sent, it gets delivered to your code in a nice package, at which point you can do whatever you like with it.

This kind of thing is incredibly powerful and allows for doing all kinds of nifty, clever things.

Right about now, you're probably wondering, "Why is it called _forwarding?_" There doesn't seem to be much of a link between taking arbitrary actions in response to unknown messages, and "forwarding". The reason for this is because this technique was mainly intended to allow objects to let other objects handle the message for them, thus "forwarding".

**What Happens**  
 What happens when you do `[foo bar]` and `foo` doesn't implement a `bar` method? When it _does_ implement such a method, it's pretty straightforward: it looks up the appropriate method, then jumps to it. When no such method can be found, a complicated sequence of events ensues:

1. **Lazy method resolution.** This is done by sending `resolveInstanceMethod:` (`resolveClassMethod:` for class methods) to the class in question. If that method returns YES, the message send is restarted under the assumption that the appropriate method has now been added.
2. **Fast forwarding path.** This is done by sending `forwardingTargetForSelector:` to the target, if it implements it. If it implements this method and it returns something other than `nil` or `self`, the whole message sending process is restarted with that return value as the new target.
3. **Normal forwarding path.** First the runtime will send `methodSignatureForSelector:` to see what kind of argument and return types are present. If a method signature is returned, the runtime creates an `NSInvocation` describing the message being sent and then sends `forwardInvocation:` to the object. If no method signature is found, the runtime sends `doesNotRecognizeSelector:`.

**Lazy Resolution**  
 As we learned last week, the runtime sends messages by looking up a method, or `IMP`, and then jumping to it. Sometimes it can be useful to dynamically plug IMPs into a class instead of setting them all up beforehand. Doing this allows for really fast "forwarding", because after the method is resolved, it gets invoked as part of the normal message sending process. The disadvantage is, of course, that this isn't very flexible, since you need to have an IMP ready to plug in, and that in turn means that you need to have already anticipated the argument and return types that will be arriving.

This kind of thing is great for stuff like @dynamic properties. The method signature is something you should know in advance: you'll either take one parameter with a void return, or have no parameters and return one value. The types of the values will vary, but you can cover the common cases. Since the IMP gets passed the selector that's been sent to the object, it can use that selector to get the name of the property and look it up dynamically. Plug it in to the class using `+resolveInstanceMethod:` and off you go.

**Fast Forwarding**  
 The next thing the runtime does is see if you want to just send the whole message unchanged to a different object. Since this is a common case of forwarding, this allows it to be done with minimal overhead.

For some reason, fast forwarding is really poorly documented. The only place Apple even mentions it, aside from a commented-out declaration in `NSObject.h`, is in the [Leopard release notes](http://developer.apple.com/ReleaseNotes/Cocoa/Foundation.html). (Search for "New forwarding fast path".)

This technique is great for faking multiple inheritence. You can write a little override like this:

```
    - (id)forwardingTargetForSelector:(SEL)sel { return _otherObject; }
```

This will cause any unknown message to be sent to `_otherObject`, which will make your object appear from the outside as though it combined your object with this other object in one.

**Normal Forwarding**  
 The first two are basically just optimizations that allow forwarding to go faster. If you don't take advantage of them, the full forwarding mechanism goes into action. This creates an `NSInvocation` object which fully encapsulates the message being sent. It holds the target, the selector, and all of the arguments. It also allows full control over the return value.

Before the runtime can build the `NSInvocation` it needs an `NSMethodSignature`, so it requests one using `-methodSignatureForSelector:`. This is required due to Objective-C's C heritage. In order to bundle the arguments up in the `NSInvocation`, the runtime needs to know what kind of arguments there are, and how many of them there are. This information isn't normally provided in a C runtime environment, so it has to do an end run around the C "bag of bytes" view of the world and get that type information in another way.

Once the invocation is constructed, the runtime then invokes your `forwardInvocation:` method. From there you can do whatever you want with the invocation it hands you. The possibilities are endless.

Here's one quick example. Imagine you're tired of writing loops, so you want to be able to manipulate arrays more directly. Add this little category to `NSArray`:

```
    @implementation NSArray (ForwardingIteration)
    
    - (NSMethodSignature *)methodSignatureForSelector:(SEL)sel
    {
        NSMethodSignature *sig = [super methodSignatureForSelector:sel];
        if(!sig)
        {
            for(id obj in self)
                if((sig = [obj methodSignatureForSelector:sel]))
                    break;
        }
        return sig;
    }
    
    - (void)forwardInvocation:(NSInvocation *)inv
    {
        for(id obj in self)
            [inv invokeWithTarget:obj];
    }
    
    @end
```

Then you can write code like this:

```
    [(NSWindow *)windowsArray setHidesOnDeactivate:YES];
```

I don't recommend writing code like this. The trouble is that forwarding won't catch any methods already implemented by NSArray, so you'll end up being able to capture some but not others. A much better approach is to write a trampoline class by subclassing `NSProxy`.

`NSProxy` is basically a class that's expilicitly designed for proxying. It implements a minimal subset of methods, leaving everything else up for grabs. This means that a subclass that implements forwarding can capture basically any message.

To use `NSProxy` for this kind of thing, you'd write an NSProxy subclass that can be initialized to point at an array, and then add a little stub method to `NSArray` that returns a new instance of the proxy, like so:

```
    @implementation NSArray (ForwardingIteration)
    - (id)do { return [MyArrayProxy proxyWithArray:self]; }
    @end
```

Then you'd use it like this:

```
    [[windowsArray do] setHidesOnDeactivate:YES];
```

This whole area of writing trampolines to capture messages and have them do interesting things has been well explored and has been given the name [Higher-Order Messaging](http://cocoadev.com/index.pl?HigherOrderMessaging). I won't go into more detail about it in this post, but there's a lot of neat stuff out there.

**Declarations**  
 Another consequence of Objective-C's C heritage is that the compiler needs to know the full method signature of every message that you're going to send in your code, even purely forwarded ones. To make a contrived example, imagine writing a class that uses forwarding to produce integers from code, so that you can write this:

```
    int x = [converter convert_42];
```

This is obviously not very useful, but you could certainly do it. More useful variants of this technique are possible.

The trouble is that the compiler doesn't know about any `convert_42` method, so it has no idea what kind of value it returns. It will give you a nasty warning, and will assume that it returns `id`. The fix to this is simple, just declare one somewhere:

```
    @interface NSObject (Conversion)
    - (int)convert_42;
    - (int)convert_29;
    @end
```

Again, this obviously isn't very useful to do, but in cases where you have a more practical forwarding situation, this can help you make peace with the compiler. For example, if you use forwarding to fake multiple inheritence, use a category to declare all of the methods of the other class as applying to the multiply-inheriting class as well. That way the compiler knows that it has both sets of methods. One set gets handled by forwarding, but that doesn't matter to the compiler.

**Conclusion**  
 Message forwarding is a powerful technique that greatly multiplies the expressiveness of Objective-C. Cocoa uses it for things like `NSUndoManager` and distributed objects, and it can let you do a lot of nifty things in your own code.

That wraps up this week's Friday Q&A. Tune in next week for more riveting tales of programming, and leave your comments on this edition below.

Friday Q&A is powered by the contribution of your ideas. If you have an idea you'd like to see discussed here, post it in the comments or [e-mail it directly](mailto:mike@mikeash.com). I will use your name unless you ask me not to.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-03-27-objective-c-message-forwarding.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
