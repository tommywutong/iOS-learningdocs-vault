---
title: Defensive Programming in Cocoa
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-08-27-defensive-programming-in-cocoa.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e0f675ecd4278949'
translated: false
---

> 原文：[Defensive Programming in Cocoa](https://www.mikeash.com/pyblog/friday-qa-2010-08-27-defensive-programming-in-cocoa.html)　·　mikeash.com Friday Q&A

Posted at 2010-08-27 15:19 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Cocoa Unbound](https://www.mikeash.com/pyblog/cocoa-unbound.html)  
Previous article: [Friday Q&A 2010-08-12: Implementing NSCoding](https://www.mikeash.com/pyblog/friday-qa-2010-08-12-implementing-nscoding.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [defensive](https://www.mikeash.com/pyblog/?tag=defensive) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2010-08-27: Defensive Programming in Cocoa

by [Mike Ash](https://www.mikeash.com/)

**Recap**  
 Defensive coding essentially boils down to constantly asking yourself, "what if it fails?" and coding appropriately. Your code's response to failure can be ranked:

1. Corrupt/delete user data
2. Crash/freeze
3. Fail silently
4. Display an error
5. Work around the failure

The goal is to get as far down the list as is possible and reasonable.

When it comes to defensive Cocoa programming, a lot of failures are really just unanticipated changes. What happens if something makes a subclass of your class? What happens if your superclass's `dealloc` implementation changes? What happens if the behavior of an object changes but remains within the API contract?

**Initializers**  
 What better place to start than at the beginning of an object's lifecycle?

I wrote [a full post on implementing Cocoa initializers](https://www.mikeash.com/pyblog/the-how-and-why-of-cocoa-initializers.html), so I won't go into too much detail here. The main things you need to do to write a defensive initializer are to always ensure that your superclass's initializer gets called (even if it doesn't do anything, it could start doing something later), always assign `self` to the result, and always check the result for `nil`. Thus:

```
    - (id)init
    {
        self = [super init];
        if(self)
        {
            // ... initialize instance variables here
        }
        return self;
    }
```

**Deallocation**  
 When your object is destroyed, it must clean up after itself. Naturally, you need to be careful when doing this.

First, always write your `dealloc` implementation to tolerate an uninitialized or partially initialized object. It's possible that your initializer, or a superclass initializer, will encounter an error and decide to destroy your object before it's fully formed, and your code should tolerate this. You can take advantage of the fact that Objective-C objects start out zero-filled. For example:

```
    - (void)dealloc
    {
        // if statement guards against uninitialized object
        if(someStructPointer)
            [someStructPointer->object release];
        
        [super dealloc];
    }
```

Note that most of the time, you can simply take advantage of the fact that messages to `nil` do nothing, and not have to write any extra code to handle the case of an uninitialized object.

**Setters**  
 The same thing goes for setters, especially those which are overridden from a superclass. The superclass may call the setter with `nil` to destroy an object rather than directly using `release`. Always write your code to tolerate this. For example:

```
    - (void)setFoo: (id)newFoo
    {
        // make sure we don't do something bad if newFoo is nil!
        if(newFoo)
            [[NSNotificationCenter defaultCenter]
             addObserver: self
             selector: @selector(_fooChanged)
             name: FooDidChangeNotification
             object: newFoo];
        [super setFoo: newFoo];
    }
```

You should always do this even if you're sure it will never get called with `nil`. It's just good practice, and doesn't hurt.

**`+initialize`**  
 Just as you have to code defensively when initializing your objects, so do you have to for initializing your classes.

The `+initialize` method is extremely useful for doing basic setup of class-wide data. It's invoked automatically by the runtime the first time any message (such as `alloc`) is sent to your class.

For example, say you need a global dictionary to hold certain items:

```
    static NSMutableDictionary *gDictionary;
    
    + (void)initialize
    {
        gDictionary = [[NSMutableDictionary alloc] init];
    }
```

However, this is dangerous and wrong! The trouble occurs if there's a subclass which doesn't implement `+initialize`. The runtime still _sends_ the message, and so it ends up invoking your version instead. Suddenly you've leaked the old dictionary and lost all of the data in it. Whoops.

The fix is simple: just check the identify of `self` before you do your initialization.

```
    static NSMutableDictionary *gDictionary;
    
    + (void)initialize
    {
        if(self == [MyClass class])
            gDictionary = [[NSMutableDictionary alloc] init];
    }
```

As a general rule, the first line of any `+initialize` implementation should always be a check of `self` to ensure that it's the correct class.

You might be thinking that you didn't write any subclasses and don't plan to, so you don't need to do this. There are two problems with that approach.

First is the obvious one that you might simply be wrong about your future plans. If in a year you change your mind and decide that you do need a subclass, you don't want this code to suddenly break in mysterious and hard-to-debug ways.

Less obvious is the fact that subclasses of your class can be created dynamically at runtime. This is done by Cocoa's key-value observing system, a key component of Cocoa bindings. These dynamic subclasses still cause `+initialize` to execute, so be prepared for it.

**Memory Management**  
 If you have an object pointer instance variable, never assign to that variable except in `init`, `dealloc`, and a setter method. In other words, don't write code that does this directly:

```
    [myObjIvar release];
    myObjIvar = [[self makeNewObj] retain];
```

If you write that code directly, it's easy to forget a retain or release and cause havoc. It makes your code less dangerous and easier to understand to call through to a setter:

```
    [self setMyObjIvar: [self makeNewObj]];
```

That way all of the memory management code is contained in just one place, instead of being scattered all about.

On the subject of setters, if you're writing your own setter, remember that you must either do an `if` check to make sure that the object you have is genuinely new, or you must do a `retain` (or `copy`) _before_ you do a `release`, to make your code robust against calling the setter with the same object as is already held in the variable. In other words, don't do this:

```
    - (void)setMyObjIvar: (id)obj
    {
        [myObjIvar release]; // could destroy obj!
        myObjIvar = [obj retain];
    }
```

Instead, either do this:

```
    - (void)setMyObjIvar: (id)obj
    {
        if(obj != myObjIvar)
        {
            [myObjIvar release];
            myObjIvar = [obj retain];
        }
    }
```

Or this:

```
    - (void)setMyObjIvar: (id)obj
    {
        [obj retain]; // or obj = [obj copy];
        [myObjIvar release];
        myObjIvar = obj;
    }
```

Which one is better is essentially a matter of taste.

**Copying**  
 Object copying is a source of horrors when it comes to subclassing Cocoa objects, due to the two different ways that exist to create a copy of an object in the top-level implementation of `copyWithZone:`.

The _sane_ way to implement `copyWithZone:` is to either return `[self retain]` (only if the object is immutable) or to create a new instance of the object's class and populate it to hold the same values using accessors or direct instance variable access:

```
    - (id)copyWithZone: (NSZone *)zone
    {
        // note use of [self class] rather than MyClass
        // this is defensive programming against subclassing!
        MyClass *newObj = [[[self class] alloc] init];
        [newObj setFoo: _foo];
        [newObj setBar: _bar];
        return newObj;
    }
```

The completely _insane_ way to implement `copyWithZone:` is to use the `NSCopyObject` function. This function allocates a new object of the same class and returns it. The problem is that it also _performs a bitwise copy of all instance variables_. These instance variables include things like pointers to objects. It does not retain them, merely copies their value.

Never, ever, ever use `NSCopyObject`. Easy, right? The problem is that _Cocoa_ uses it, and if you ever subclass Cocoa objects, you have to be aware.

Even worse: you often can't count on the Cocoa implementation using one technique or another. It could use either one, and which one it uses could switch at any time. So if you ever subclass a Cocoa object that implements `NSCopying`, and you add instance variables, you need to write a `copyWithZone:` override that handles both cases correctly. Fortunately this is easier than it sounds.

First, let's examine the problem in more detail. Here's an example NSCell subclass:

```
    @interface MyCell : NSCell
    {
        NSString *_someString;
    }
    
    - (void)setSomeString: (NSString *)newString;
    
    @end
```

```
    @implementation MyCell
    
    - (void)setSomeString: (NSString *)newString
    {
        [newString retain];
        [_someString release];
        _someString = newString;
    }
    
    - (void)dealloc
    {
        [_someString release];
        [super dealloc];
    }
    
    @end
```

Now you write a bit of code that uses it:

```
    MyCell *cell = [[MyCell alloc] init];
    [cell setSomeString: string];
    MyCels *cell2 = [cell copy];
    [cell release];
    [cell2 release];
```

You run this and it crashes! Why?

The implementation of `-[NSCell copyWithZone:]` uses `NSCopyObject`. This means that it copies the `_someString` pointer, but does no memory management on it. You end up with two pointers to the string but only one of which is retained. They both get released in `dealloc`. Crash.

The solution is simple: override `copyWithZone:` and retain or copy the instance variable:

```
    - (id)copyWithZone: (NSZone *)zone
    {
        MyCell *newObj = [super copyWithZone: zone];
        [newObj->_someString retain];
        return newObj;
    }
```

This works, but is brittle. If the `NSCell` implementation changed to no longer call `NSCopyObject`, this implementation will fail, because `newObj->_someString` will be `nil`. It won't crash, but the copy won't be a proper copy either. And you can't just switch to using `[newObj setSomeString: _someString]` because that crashes the `NSCopyObject` case. We need code that works equally well for both.

The answer is to directly assign to the instance variable of the other object and do memory management at the same time, like so:

```
    - (id)copyWithZone: (NSZone *)zone
    {
        MyCell *newObj = [super copyWithZone: zone];
        newObj->_someString = [_someString retain];
        return newObj;
    }
```

You'll note that it works for both cases. For the sane case, it retains the string and puts the value into the new object's instance variable. For the `NSCopyObject` case, it overwrites the existing pointer with a new one, but without releasing the old one.

Note that `NSCell` is by far the most commonly subclassed class that conforms to `NSCopying`. If you ever subclass `NSCell` or one of its subclasses, you _must_ implement `copyWithZone:`, and you _must_ do it correctly using the above technique. Otherwise you leave yourself open to extremely mysterious crashes and corruption problems. I've been there, it's no fun.

**Error Returns**  
 A lot of Cocoa methods take `NSError **` parameters to tell you why something went wrong. Always check the retun value from these methods! And always at least log the error if there is one.

Don't do this:

```
    NSString *string = [NSString stringWithContentsOfFile: path encoding: NSUTF8StringEncoding error: NULL];
    [self corruptImportantDataIfNil: string];
```

Instead, check `string` and use the error if it's `nil`. At the very least, use an assert to nicely stop the current operation rather than continuing with bad data:

```
    NSError *error;
    NSString *string = [NSString stringWithContentsOfFile: path encoding: NSUTF8StringEncoding error: &error];
    NSAssert(string, @"Could not load string, error: %@", error);
    [self corruptImportantDataIfNil: string];
```

If possible and reasonable, try to either fail gracefully (maybe try a different, backup source of data) or at least report the error to the user in the GUI and allow the program to continue executing normally.

Always at least check for failure and log the error. Even if subsequent code won't corrupt data in the error case, it's still much easier to figure out why your code isn't working if you can catch the failure as early as possible.

**A Note on Checking Errors**  
 This has been repeated in many other places, but bears another mention. Always check _the return value_ of such a method, and not the `NSError` variable directly. For example, this is wrong:

```
    NSError *error = nil;
    NSString *string = [NSString stringWithContentsOfFile: path encoding: NSUTF8StringEncoding error: &error];
    NSAssert(!error, @"Could not load string, error: %@", error);
```

Apple reserves the right to fill your `error` variable with junk upon success. This is a stupid policy, but it's the policy which is there, so you must take it into account.

**Weak References**  
 The standard way to set up an `NSTableView` using a data source is to create an object to be the data source, implement the required methods, and then hook up the `dataSource` outlet of the table view. However, if you don't do anything else, this is actually a dangerous setup.

The problem is that the order of object destruction isn't defined. If your data source gets destroyed before the table view, the table view could potentially message the data source after it's been destroyed, causing your program to crash.

To ensure that this never happens, you must zero out the data source in your `dealloc`. However, simply adding that isn't safe either! It's possible for the table view to be destroyed first, and then your message to it will crash. What to do?

The answer to this conundrum is to _retain_ the table view outlet. Don't rely on direct instance variable twiddling, but rather write a setter for it that retains it. Then you can write your `dealloc` like this:

```
    - (void)dealloc
    {
        [tableView setDataSource: nil];
        [tableView release];
        [super dealloc];
    }
```

This is safe because it ensures that the table view is never destroyed before you zero out the weak reference.

Most weak references are subject to this problem, including most delegate references from Cocoa objects. Most of the time you can get away with ignoring it, but it's much safer to do it right.

For a more comprehensive solution to the problem of weak references, check out [MAZeroingWeakRef](https://www.mikeash.com/pyblog/introducing-mazeroingweakref.html). By using the `MAZeroingWeakProxy` class and the Objective-C associated object API, it becomes trivial to create delegate and data source connections which are completely safe.

**Categories**  
 Categories are a great feature of Objective-C. It's really handy to be able to add new methods to Cocoa classes that you can then use anywhere in your program. However, it can also be dangerous.

The danger comes when your method name clashes with one that Apple has put in the class. Your method will override the existing one. If they do different things, trouble will ensue. Even worse, your category method could be just fine today, but conflict with a method added by Apple in the next release of the OS.

For example, say you add a `map:` method to NSArray:

```
    @interface NSArray (MyAdditions)
    
    - (NSArray *)map: (id (^)(id obj))block;
    
    @end
```

This is fine now, but if Apple adds their own `map:` method in 10.7, and it doesn't have identical semantics, you'll be in big trouble.

The only way to avoid this is to ensure that your category methods on Apple classes will never have a name conflict. The most obvious way to ensure this is to add a prefix to the method name:

```
    - (NSArray *)ma_map: (id (^)(id obj))block;
```

This is ugly, but effective. As a bonus, it's often easier to find your category methods with Xcode's code completion, since you can just type in your prefix and let Xcode show all of them.

Another way to ensure that you never have a conflict is to give your method an extremely specific name that you can be confident will never be used by Apple. For example:

```
    - (NSArray *)arrayByMappingMyFooElements: (id (^)(MyFoo *foo))block;
```

But this can be a dangerous game to play. When in doubt, prefix.

**Conclusion**  
 Cocoa is a complex system that can have some hidden gotchas. However, for the most part, all you need to do is be aware of the fact that your application is really just one component in a larger system. Write your application to be a good citizen and cooperate nicely with the other components that get loaded into your process. Be particularly careful when subclassing and when making modifications to framework classes. The cases presented above are just a sampling of useful defensive programming techniques in Cocoa. Keep defensive programming on your mind no matter what you write, and your code will be better for it.

That's it for this round of Friday Q&A. I will probably be taking a few weeks off for (good) personal reasons, so don't panic if two weeks go by and I haven't posted another one. I will resume before too long, but won't make any promises as to when just yet.

As always, if you have ideas for topics that you would like to see covered here, [send them to me](mailto:mike@mikeash.com). I may not get to it right away, but I will certainly put your suggestion on my list for the future.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-08-27-defensive-programming-in-cocoa.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
