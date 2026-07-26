---
title: 'Friday Q&A 2009-08-14: Practical Blocks'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-08-14-practical-blocks.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:af10c3a33bd3115b'
translated: false
---

> 原文：[Friday Q&A 2009-08-14: Practical Blocks](https://www.mikeash.com/pyblog/friday-qa-2009-08-14-practical-blocks.html)　·　mikeash.com Friday Q&A

Posted at 2009-08-14 20:06 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-08-21: Writing Vararg Macros and Functions](https://www.mikeash.com/pyblog/friday-qa-2009-08-21-writing-vararg-macros-and-functions.html)  
Previous article: [Friday Q&A 2009-07-17: Format Strings Tips and Tricks](https://www.mikeash.com/pyblog/friday-qa-2009-07-17-format-strings-tips-and-tricks.html)  
Tags: [blocks](https://www.mikeash.com/pyblog/?tag=blocks) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2009-08-14: Practical Blocks

by [Mike Ash](https://www.mikeash.com/)

Although Apple has yet to ship blocks with any of their developer tools, they have released code for their blocks implementation due to their participation in the open-source compilers gcc and clang. Landon has used this code to put together [PLBlocks](http://code.google.com/p/plblocks/), which allows building and running blocks-based code on Mac OS X 10.5. While there are no blocks-based APIs on 10.5 (aside from the very basics which are part of the runtime), they can still be used to great effect.

I'm not going to cover the installation or basic use of PLBlocks here, as the PLBlocks page covers this in great detail. If you want to follow along, go there and follow the directions. For more information about how blocks work, see Clang's [blocks language spec](http://clang.llvm.org/docs/BlockLanguageSpec.txt) and [implementation spec](http://clang.llvm.org/docs/BlockImplementation.txt).

I'm also going to assume that you know the basics of block syntax and usage, as covered in [my last Friday Q&A on the subject](https://www.mikeash.com/pyblog/friday-qa-2008-12-26.html). Today's is essentially Part II of that one. If you haven't already, go read that one first.

**Fundamentals**  
 Blocks are Objective-C objects. When you write a block in code, that is an expression of object type, much like the `@"..."` constant string syntax gives you an expression of object type. You can then use this object like you would any other Objective-C object, by sending it messages that it responds to, putting it into containers, passing it as a parameter, returning it, etc.

There is a major difference from the constant string syntax. Unlike constant strings, blocks are not exactly the same each time through a piece of code. This is because blocks capture their enclosing scope, and that scope is different every time they're called. In short, each time code execution hits a `^{...}` construct, a new object is created.

Allocating a new object every time would be kind of slow, so blocks take an unusual approach: the object you get from a `^{...}` construct is a _stack object_. This means that it has the same lifetime as local variables, and will be destroyed automatically upon leaving the current scope. Weird, huh?

It's frequently useful for a block to outlive the scope where it was created. For example, you may want to return a block, or save it for later. For this to work, you must copy the block. You can do this like any other Objective-C object by sending it the `-copy` message. And like any other Objective-C object, if you aren't running under Garbage Collection then you own the resulting object and must eventually dispose of it using `-release` or `-autorelease`.

This, then, is an example of returning a block from a method:

```
    - (void (^)(void))block { return [[^{ ... } copy] autorelease]; }
```

Note that external variable capture gives const copies of those variables by default. In other words, this is not legal:

```
    int i;
    ^{ i++; };
```

The way to work around this is to use the `__block` keyword, like so:

```
    __block int i;
    ^{ i++; };
```

The reason for requiring explicit marking of local variables like this is because `__block` variables are significantly more costly than the regular kind, and have different semantics when applied to Objective-C object pointers (more details on that later), so rather than figure out a one-size-fits-all policy, the blocks guys decided it was better to just let the programmer choose.

**Examples**  
 I'm going to be showing a bunch of examples for how to use blocks with PLBlocks on 10.5. Those of you who want to follow along may wish to look at the example project I built, which you can get out of my public subversion repository here:

```
    svn co http://www.mikeash.com/svn/PLBlocksPlayground/
```

If you just want to browse the code you can just click on the link in that command.

**Custom APIs**  
 That's the basic idea of how they work, now let's see what we can do with them.

As I mentioned in my first blocks post, blocks essentially allow you to build new control constructs without needing to modify the language. Before we get into it, I want to introduce a little typedef to keep things simple. Most control-construct blocks are blocks which take no parameters and return no value. As such, it's nice to have that type wrapped up in something a little nicer to write:

```
    typedef void (^BasicBlock)(void);
```

As a really simple example, let's take a fairly common task in Cocoa: that of running some code with an inner autorelease pool to keep your high water mark low. Normally this would look like:

```
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    ...
    [pool release];
```

This is not all that bad, but it's a little verbose. We could write a macro to do this, but macros are fairly evil, and often have hidden gotchas. Instead, let's write a little function to do this, using blocks:

```
    void WithAutoreleasePool(BasicBlock block)
    {
        NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
        block();
        [pool release];
    }
```

And then we can use it like so:

```
    for(id obj in array)
        WithAutoreleasePool(^{
            [self createLotsOfTemporaryObjectsWith:obj];
        });
```

That's quicker and easier than writing it out manually, and just as readable at the end. Nice!

Let's attack something a little more complicated. It's common in Cocoa programs to need to run some code after a short delay, using `-performSelector:withObject:afterDelay:`. Often we'll use a zero delay to mean "run this code immediately after returning to the runloop". The trouble with this is that it requires an object and a separate method, and getting the relevant context over can be painful. Let's write a quickie blocks function instead:

```
    void RunAfterDelay(NSTimeInterval delay, BasicBlock block)
    {
        [[[block copy] autorelease] performSelector: @selector(my_callBlock) withObject: nil afterDelay: delay];
    }
```

Notice how we have to do a copy/autorelease on the block so that the object stays alive until the perform is complete. This makes use of a small category on NSObject to actually invoke the block, taking advantage of the fact that blocks are NSObjects too:

```
    @implementation NSObject (BlocksAdditions)
    
    - (void)my_callBlock
    {
        void (^block)(void) = (id)self;
        block();
    }
    
    @end
```

Then we can use it like so:

```
    NSString *something = ...;
    RunAfterDelay(0, ^{
        NSLog(@"%@", something);
        [self doWorkWithSomething: something];
    });
```

This is a lot easier to work with than the typical Cocoa pattern for anything more complex.

Another thing that we frequently write is a critical section of code protected by a lock. Normally this would look like:

```
    [lock lock];
    ...do stuff...
    [lock unlock];
```

However this can be somewhat error prone. For example if you forget to unlock the lock in one code path, or return from the middle, or throw an exception, then your application will deadlock. The safest way to write the above is to use a `@try/@finally` block like so:

```
    [lock lock];
    @try
    {
        ...do stuff...
    }
    @finally
    {
        [lock unlock];
    }
```

Which is sort of cumbersome. We can turn this idiom into a blocks-based method on NSLock to handle locking and unlocking completely automatically:

```
    @implementation NSLock (BlocksAdditions)
    
    - (void)whileLocked: (BasicBlock)block
    {
        [self lock];
        @try
        {
            block();
        }
        @finally
        {
            [self unlock];
        }
    }
    
    @end
```

This isn't exactly the same. For example, with the explicit `@try/@finally` you can return a value from the method from within the `@try` block and it works, whereas doing this from inside the block will simply error, because you'll be returning a value from the block instead, which will make the block's type incompatible. This can be worked around by using a `__block` qualified variable to hold the return value. In my opinion this is superior, as it helps discourage tricky behavior inside the critical section, where the potential for bugs is high.

**A Stylistic Note**  
 There are two interesting choices in the above code, both due to the same reason. The first choice is that these are functions, not methods. Since blocks are NSObjects, category methods on NSObjects can be used for them. Rather than a `RunAfterDelay` function, we could write a `-runAfterDelay:` method on NSObject. The second choice is to always put the block parameter last, even though it's the most significant parameter and would make more sense to go first.

The reason for both of these is that you want the block to come absolutely last so that your code remains readable when the block is split onto multiple lines. For example, imagine some nested blocks code using the above functions recast using methods instead:

```
    [^{
        for(id obj in array)
            [^{
                [self doImportantWork:obj];
            } withAutoreleasePool];
    } runAfterDelay: 0];
```

This is significantly less readable. The code appears first, and what's being done with it only comes at the end, which can come much later. When nested, you have to read everything in LIFO order. For this reason, it's a bad idea to write control constructs using methods, and when taking a block as a parameter, always put the block last.

**Collections**  
 Using blocks with collections can make for powerful looping constructs. Let's start out with this really simple substitute for a for loop, as a method on `NSArray`:

```
    - (void)do: (void (^)(id obj))block
    {
        for(id obj in self)
            block(obj);
    }
```

This is not really all that interesting. It ends up being just like a `for/in` loop, but without the ability to statically type the objects. (It would have been nice to have before Apple introduced `for/in`, at least, illustrating the idea of adding your own control constructs using blocks.) Example use:

```
    NSArray *array = ...;
    [array do: ^(id obj){ NSLog(@"%@", obj); }];
```

Not too exciting. Here's one that's more interesting. This uses a block to map one array to a new array:

```
    - (NSArray *)map: (id (^)(id obj))block
    {
        NSMutableArray *new = [NSMutableArray array];
        for(id obj in self)
        {
            id newObj = block(obj);
            [new addObject: newObj ? newObj : [NSNull null]];
        }
        return new;
    }
```

This shows how you could use it to construct an array of name strings from an array of people:

```
    NSArray *people = ...;
    NSArray *names = [people map: ^(id person){
        return [NSString stringWithFormat: @"%@ %@", [person firstName], [person lastName]];
    }];
```

This is much nicer than manually writing the loop encapsulated in the `-map:` method. By passing blocks around, we only have to write that loop once, then reuse it many times.

One more example, this allows filtering an array:

```
    - (NSArray *)select: (BOOL (^)(id obj))block
    {
        NSMutableArray *new = [NSMutableArray array];
        for(id obj in self)
            if(block(obj))
                [new addObject: obj];
        return new;
    }
```

An example of using it to filter out strings that are too short:

```
    NSArray *longStrings = [strings select: ^ BOOL (id obj) { return [obj length] > 5; }];
```

Note the explicit return value. The result from C comparison operators is `int`, not `BOOL`, so allowing the compiler to infer the return value would produce a block of incompatible type. An alternative would be to cast the expression used in the return statement.

Here's an example of a use in a GUI application, for getting all the text fields inside a particular view:

```
    NSArray *textFields = [[view subviews] select: ^(id obj){ return [obj isKindOfClass: [NSTextField class]]; }];
```

**Callbacks**  
 Callbacks-based APIs are a place where blocks really shine. Instead of passing a selector/delegate pair, or a function pointer/context pointer pair, pass a block. It makes it much easier to pass context around (since the block packages up all needed context automatically) and keeps all of the code nearby.

An obvious example of a callback is notifications. While there's often a benefit to having separated methods for notifications, the implementation is easy and it can sometimes make for nicer code:

```
    @implementation NSNotificationCenter (BlocksAdditions)
    
    - (void)addObserverForName: (NSString *)name object: (id)object block: (void (^)(NSNotification *note))block
    {
        [self addObserver: [block copy] selector: @selector(my_callBlockWithObject:) name: name object: object];
    }
    
    @end
```

The `my_callBlockWithObject:` method is implemented in a category on `NSObject`, much like the `my_callBlock` method seen earlier, except that it takes a parameter and passes that parameter on to the block.

You can use it like so:

```
    [[NSNotificationCenter defaultCenter] addObserverForName: NSApplicationDidBecomeActiveNotification
                                                      object: nil
                                                       block: ^(NSNotification *note){ NSLog(@"Did become active"); }];
```

Note that there is no mechanism provided for deactivating the notification block. This could be added, but would require additional state to be managed by the caller. Such a mechanism is left as an exercise for the reader.

Sheets are a good example of a painful callbacks-based API in Cocoa. You have to implement a callback method, then cram all of the state associated with the sheet, which is often large, either into the single `void *` context parameter provided, or into instance variables. Neither way is particularly nice.

Here is a small category which translates this API to use blocks instead:

```
    @implementation NSApplication (SheetAdditions)
    
    - (void)beginSheet: (NSWindow *)sheet modalForWindow:(NSWindow *)docWindow didEndBlock: (void (^)(NSInteger returnCode))block
    {
        [self beginSheet: sheet
          modalForWindow: docWindow
           modalDelegate: self
          didEndSelector: @selector(my_blockSheetDidEnd:returnCode:contextInfo:)
             contextInfo: [block copy]];
    }
    
    - (void)my_blockSheetDidEnd: (NSWindow *)sheet returnCode: (NSInteger)returnCode contextInfo: (void *)contextInfo
    {
        void (^block)(NSInteger returnCode) = contextInfo;
        block(returnCode);
        [block release];
    }
    
    @end
```

Now you can simply provide a block inline, right in with the rest of your code, and access all of the necessary context directly.

Another example of a similarly painful API is `NSURLConnection`. It provides two modes: synchronous and asynchronous. The synchronous mode can only be used from a secondary thread which can be blocked for arbitrarily long amounts of time, since any network operation can take a long time to complete. The asynchronous mode requires writing a lot of boilerplate code. Let's write a method that adds an asynchronous mode that simply makes a single call to a block when it's done to hand over the data, the response metadata, and the error, if any. To do this, we'll just use the synchronous API in a background thread. This code uses two functions, `RunInBackground` and `RunOnThread`, which are blocks-based APIs for spawning a new thread and running a block on an existing thread, respectively. These functions are pretty straightforward to implement and I won't duplicate them here, but you can get them in the sample project if you need.

Here's what the code looks like:

```
    @implementation NSURLConnection (BlocksAdditions)
    
    + (void)sendAsynchronousRequest: (NSURLRequest *)request
                    completionBlock: (void (^)(NSData *data, NSURLResponse *response, NSError *error))block
    {
        NSThread *originalThread = [NSThread currentThread];
        
        RunInBackground(^{
            WithAutoreleasePool(^{
                NSURLResponse *response = nil;
                NSError *error = nil;
                NSData *data = [self sendSynchronousRequest: request returningResponse: &response error: &error;];
                RunOnThread(originalThread, NO, ^{ block(data, response, error); });
            });
        });
    }
    
    @end
```

There are a couple of notable features here. First, notice how the current thread is saved into a local variable, then later on accessed inside a block which will be executed on a different thread. This shows how blocks can be used to easily pass context around in callbacks. Notice then how the block passed to `RunInBackground` ends with a call to `RunOnThread` which uses another block to call back to the originating thread. This kind of nested block messaging is handy for making asynchronous callbacks in a concise manner.

Here's an example of using this API:

```
    NSURLRequest *request = [NSURLRequest requestWithURL: [NSURL URLWithString: @"http://www.google.com/"]];
    [NSURLConnection sendAsynchronousRequest: request
                             completionBlock: ^(NSData *data, NSURLResponse *response, NSError *error){
        NSLog(@"data: %ld bytes  response: %@  error: %@", (long)[data length], response, error);
    }];
```

This is very nice! The equivalent using the asynchronous APIs would require implementing several methods, and possibly a whole new class. Using the synchronous API explicitly, and doing all the work of managing the secondary thread, and calling back to the main thread when done, passing along all of the objects that were received, would require many more lines of code than this does.

**Caveats**  
 It should be no surprise that there are some things to look out for when working with blocks.

When blocks are copied, any local object variables they refer to get automatically retained. They are then automatically released when the block is destroyed. This is convenient to ensure that the references remain valid. Any reference to `self` is a reference to a local object variable, causing `self` to be retained. Any reference to an instance variable is an implicit reference to `self` and causes the same thing. However, this makes it easy to cause a retain cycle in some instances. Imagine using a more fleshed-out version of that blocks-based notification API which allows unregistering the notification. If your block refers to `self` in any way, and you do the standard Cocoa thing of unregistering the notification in `-dealloc`, your object will leak because the block will hold a reference to your object.

A simple workaround to this lies in the fact that `__block` variables are _not_ retained. This is because such variables are mutable, and automatic memory management of them would require each mutation to generate memory management code behind the scenes. This was seen as too intrusive and difficult to get right, especially since the same block may be executing from multiple threads simultaneously. Thus you can avoid the retain cycle like so:

```
    __block MyClass *blockSelf = self;
    ^{
        [blockSelf message];
        [blockSelf->ivar message];
    };
```

CoreFoundation types need to be retain/released when captured in non-`__block` variables, just like Objective-C objects, since they really are Objective-C objects as well. However, the compiler doesn't see them this way. To help with this, the compilers have added an attribute, `__attribute__((NSObject))`, which causes struct pointers to be treated like Objective-C objects as far as their block retain/release semantics. We can assume that Apple will be applying this attribute to all `CFTypes` on 10.6. While we're stuck in 10.5, however, they won't have this attribute, and so CoreFoundation objects will not be correctly memory managed when captured by blocks. To avoid problems, either avoid capturing CoreFoundation objects in blocks (declaring the variables to be of the equivalent Objective-C toll-free bridged type instead will convince the compiler to retain/release them) or ensure that the lifetime of the CF objects is at least as long as the lifetime of the block.

Another pitfall with blocks is due to the fact that they are stack objects. Using the `^{...}` syntax is essentially the same, behind the scenes, as declaring a local variable and then taking its address for something. The address can be passed around, but as soon as you leave the scope in which the local variable was declared, it's no longer valid. Thus, something as innocent as this ends up being broken code:

```
    BasicBlock block;
    if(condition)
        block = ^{...};
    else
        block = ^{...};
```

The body of the `if` statement (and the `else` clause) is a separate scope from the main body which is destroyed as soon as control flow exits the `if`/`else` clause. The block reference which is being stored in `block` is invalid as soon as control flow returns to the main body! It's simple to fix this just by copying the blocks:

```
    BasicBlock block;
    if(condition)
        block = [[^{...} copy] autorelease];
    else
        block = [[^{...} copy] autorelease];
```

The main danger with this isn't that it's hard to fix (it's not) but that it's not necessarily easy to notice when you do it.

**Conclusion**  
 That wraps up this week's Friday Q&A. You've seen how to get blocks up and running with your current tool chain, a few examples of how they can be used in a useful manner, and some problems to watch out for. Now you're ready to start using blocks in your 10.5 apps today, no need to wait for 10.6 to ship.

Questions about blocks? Have your own ideas for how best to use them? Post below.

Come back next week for another edition of Friday Q&A. As always, Friday Q&A is driven by your ideas. If you have a topic that you would like to see covered here, post it below or [e-mail it to me](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-08-14-practical-blocks.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
