---
title: 'Friday Q&A 2009-10-16: Creating a Blocks-Based Object System'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-10-16-creating-a-blocks-based-object-system.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:53969ea4af9353ad'
translated: false
---

> 原文：[Friday Q&A 2009-10-16: Creating a Blocks-Based Object System](https://www.mikeash.com/pyblog/friday-qa-2009-10-16-creating-a-blocks-based-object-system.html)　·　mikeash.com Friday Q&A

Posted at 2009-10-16 15:50 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-10-23: A Preview of Coming Attractions](https://www.mikeash.com/pyblog/friday-qa-2009-10-23-a-preview-of-coming-attractions.html)  
Previous article: [XBolo is Out!](https://www.mikeash.com/pyblog/xbolo-is-out.html)  
Tags: [blocks](https://www.mikeash.com/pyblog/?tag=blocks) [evil](https://www.mikeash.com/pyblog/?tag=evil) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2009-10-16: Creating a Blocks-Based Object System

by [Mike Ash](https://www.mikeash.com/)

**Warning**  
 This system is weird and fairly impractical. The purpose of this article is to explore the system and think about what lessons might be learned from it that could transfer into more realistic situations. It is _not_ meant to be something that you would actually go out and use.

**Source Code**  
 For those of you who would like to follow along at home, you can get the full source code to my rudimentary blocks-based object system, plus a small example class and some testing code, [from my public subversion repository](http://www.mikeash.com/svn/blockobj/).

**C Object Orientation**  
 C has seen a number of object systems over the years, and not just the ones with language extensions like C++ and Objective-C. A common way to program in C is to use opaque structs and provide functions that operate on them. CoreFoundation is a good example of this. Here's what such a thing looks like:

```
    typedef struct MyFakeClass *MyFakeClassRef;
    
    MyFakeClassRef NewMyFakeClass(void);
    void DoSomethingInterestingWithFakeClass(MyFakeClassRef obj, int foo);
    void DestroyMyFakeClass(MyFakeClassRef obj);
```

This gives you many of the advantages of object-oriented programming without ever having to leave C. You get encapsulated data (other code doesn't know what the contents of a MyFakeClass are), a strong link between a data structure and the code that operates on it, better organization, etc.

Of course it's missing some key features of object orientation as well, like inheritence. You might remedy that by making the "methods" actually be members of the struct:

```
    struct MyFakeClass
    {
        void (*doSomethingInteresting)(struct MyFakeClass *obj, int foo);
        void (*destroy)(struct MyFakeClass *obj);
    };
```

The trouble with this is that it gets a little redundant, using the object both to find the function pointer and then having to pass it as a parameter too:

```
    struct MyFakeClass *obj = ...;
    obj->doSomethingInteresting(obj /* UGLY! */, 42);
```

And then you need a reference to the object's data somewhere, and the most natural place to put it is in the struct next to all of the function pointers, right in plain view.

**Enter Blocks**  
 Apple's new blocks extension to C gives us something much like function pointers, but which have implicit context. When you call them, they can automatically access whatever data is necessary without the caller needing to give it to them explicitly. The struct then looks like this:

```
    struct MyFakeClass
    {
        void (^doSomethingInteresting)(int foo);
        void (^destroy)(void);
    };
```

And you'd call things on it like this:

```
    struct MyFakeClass *obj = ...;
    obj->doSomethingInteresting(42);
```

Not bad at all!

This system allows overriding existing "methods" by simply putting in a new block, and having that block call through to the one that used to be there. Defining entirely new methods for a "subclass" gets a little trickier, but it's not bad. Define the subclass to contain the parent:

```
    struct MyFakeSubclass
    {
        struct MyFakeClass parent;
        
        void (^additionalMethod)(void);
    };
```

Then callers can call parent methods like this:

```
    struct MyFakeSubclass *obj = ...;
    obj->parent.doSomethingInteresting(42);
```

That `parent` is not ideal, but it's workable. As a bonus, this technique separates the ideas of overriding an existing method and implementing a new method with the same name. In most OO systems it's impossible to implement a new method with the same name, as it's automatically an override. Here, they're two separate actions.

By putting `parent` at the front, this allows subtype polymorphism. By casting an instance of `MyFakeSubclass` to a `struct MyFakeClass *`, the result is still a valid object which continues to work as an instance of its parent class, but with any overridden behavior given by its subclass.

**Building the System**  
 That's the theory. Let's go ahead and actually build it now.

The first question is what objects will actually look like. We'll define them as structs containing blocks pointer members, and possibly a pointer to a parent struct/class. These are our methods. The struct contains nothing else: any per-object data is done using local variables which get captured by the method blocks.

We can then define a root object like this:

```
    struct RootObject
    {
        void (^retain)(void);
        void (^release)(void);
        void (^dealloc)(void);
        
        struct String *(^copyDescription)(void);
        int (^isEqual)(struct RootObject *);
    };
```

We need a function to create new instances of the root object. We'll call it `NewRootObject`. It takes one parameter: the size of the object to allocate. Subclasses may be bigger, and the memory needs to be contiguous, so `NewRootObject` needs to know how much to allocate.

To ease the task of creating new objects (and figuring out how much memory to allocate), we'll create a convention that new objects are always created using a function called `NewClassName` which takes a single size parameter. We can then create a little macro for creating new objects:

```
    #define Alloc(classname) New ## classname(sizeof(struct classname))
```

Using this, you'd allocate a new instance of the root class like so:

```
    struct RootObject *obj = Alloc(RootObject);
```

Now, what does `NewRootObject` actually look like?

The first thing it needs are the "instance variables", which in this case are just `__block` qualified local variables.

```
    struct RootObject *NewRootObject(size_t size)
    {
        // "ivars"
        __block int retainCount = 1;
```

Next, it needs to actually allocate memory:

```
        // make the object
        struct RootObject *self = calloc(size, 1);
```

Then it can start filling out methods. It does this by just declaring blocks and assigning them to the slots. One wrinkle: since these blocks need to outlive their enclosing scope, we need to call `Block_copy` on them:

```
        // "methods"
        self->retain = Block_copy(^{ retainCount++; });
        self->release = Block_copy(^{
            retainCount--;
            if(retainCount <= 0)
                self->dealloc();
        });
```

Of course, that means that we eventually need to `Block_release` them. Having to go through and manually release every method in `dealloc` would be really tedious and error-prone, though. To work around this problem, the `dealloc` method can just scan the entire object for block pointers and release them all automatically. Since the only data in the object struct itself is block pointers, we can just scan one pointer-sized chunk at a time to get them all. Since we used `calloc` to allocate the object, we know that any memory "off the end" that got allocated due to `malloc` allocating more memory than necessary will be zeroed, and so any NULL pointer will be a signal to stop. This is what the dealloc method looks like:

```
        self->dealloc = Block_copy(^{
            size_t size = malloc_size(self);
            for(void **methodPtr = (void **)self;
                 *methodPtr && ((intptr_t)methodPtr + sizeof(*methodPtr) - 1 - (intptr_t)self) < size;
                 methodPtr++)
                Block_release(*methodPtr);
            free(self);
        });
```

Finally, we define the `copyDescription` method (using a method of the as-yet-unseen `String` class) and return the new object:

```
        self->copyDescription = Block_copy(^{
            return Alloc(String)->initWithFormat("<Object %p>", self);
        });
        
        return self;
    }
```

**Creating New Classes**  
 Now that we've done all of that, how do we make a subclass? Let's go ahead and create the `String` class, since the root class depends on it anyway.

As mentioned before, a subclass gets a `struct` for its parent at the top, and then follows with its own methods, like so:

```
    struct String
    {
        struct RootObject parent;
        
        struct String *(^initWithFormat)(char *fmt, ...);
        const char *(^cstring)(void);
    };
```

Then it just needs a `NewString` function to create one. As with `NewRootObject`, the first part of the function is for "instance variables":

```
    struct String *NewString(size_t size)
    {
        __block char *str = NULL;
```

And next, just like before, we allocate the object. Only this time, instead of allocating raw memory, we call through to the parent's `New` function to allocate the object.

```
        struct String *self = (void *)NewRootObject(size);
```

Next up, we want to override a couple of methods from the root object. The first one we want to override is `copyDescription`. Since we don't want to call through to the original implementation, we can just release the old block, then assign a new one:

```
        Block_release(self->parent.copyDescription);
        self->parent.copyDescription = Block_copy(^{
            self->parent.retain();
            return self;
        });
```

Next, we need to override `dealloc` to free the `str` variable. This is a little trickier, though, because we need to call through to the old implementation once we're done. To do this, we'll save off the old implementation into a local variable, and call through to it. We also have to take care of releasing the old implementation:

```
        void (^superdealloc)(void) = self->parent.dealloc;
        self->parent.dealloc = Block_copy(^{
            free(str);
            superdealloc();
        });
        Block_release(superdealloc);
```

This is some tricky memory management business. At first blush this looks good, but if you look deeper you'll realize that `Block_release(superdealloc)` is being called too early! The body of the new `dealloc` block won't run until the object is destroyed, but the `Block_release` runs while the object is still being created.

This actually ends up working perfectly fine, because the compiler automatically does a `Block_copy` on the `superdealloc` instance variable when it gets captured by the new block referencing it. There's a bit of automatic reference counting going on behind the scenes, and this ensures that the block stays alive for as long as it's needed.

Finally, we'll define the `String`-specific methods and return the new object:

```
        self->initWithFormat = Block_copy(^(char *fmt, ...){
            va_list args;
            va_start(args, fmt);
            vasprintf(&str, fmt, args);
            va_end(args);
            
            return self;
        });
        self->cstring = Block_copy(^{ return (const char *)str; });
        
        return self;
    }
```

We now have a fully functioning, albeit simplistic and a bit verbose, object system.

**Custom Classes** Let's create one more class just to reinforce how it's done. We'll call this one `MyObject`, and it will just hold two numbers. Here's the class struct:

```
    struct MyObject
    {
        struct RootObject parent;
        
        struct MyObject *(^initWithNumbers)(int a, int b);
    };
```

And here's the function to create a new one:

```
    struct MyObject *NewMyObject(size_t size)
    {
        __block int numbers[2];
        
        struct MyObject *self = (void *)NewRootObject(size);
        
        // override parent methods
        Block_release(self->parent.copyDescription);
        self->parent.copyDescription = Block_copy(^{
            return Alloc(String)->initWithFormat("<MyObject %d %d>", numbers[0], numbers[1]);
        });
        
        self->initWithNumbers = Block_copy(^(int a, int b){
            numbers[0] = a;
            numbers[1] = b;
            return self;
        });
        
        return self;
    }
```

Finally, here's some example code that actually uses it:

```
    struct MyObject *myobj = Alloc(MyObject);
    myobj->initWithNumbers(42, 65535);
    description = myobj->parent.copyDescription();
    printf("myobj is %s\n", description->cstring());
    description->parent.release();
    myobj->parent.release();
```

Which produces the output you'd expect:

```
    myobj is <MyObject 42 65535>
```

To summarize, here's what you need to do to create a new class using this system:

1. Define a new struct with the appropriate name.
2. As the first member of the struct, add a struct for the parent class.
3. For subsequent members of the struct, add block pointers for each method.
4. Pause for breath.
5. Define an appropriately-named `New` function.
6. At the top, define any "instance variables" you need using the `__block` qualifier.
7. Allocate the object by calling through to the superclass's `New` function.
8. Override any parent methods by releasing the original block pointer and reassigning it. If you need to call through to the old implementation, save it into a local variable, and release that local variable after the reassingnment.
9. Initialize any new methods by assigning to them.

**Advantages and Disadvantages**  
 This is an unusual object system. To be clear, this is _not_ what Objective-C (or C++ or Java or...) is doing behind the scenes. (For information on what Objective-C _is_ doing behind the scenes, check out [my series on the Objective-C runtime](https://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html).) It more closely resembles the prototype-based object systems found in languages like JavaScript.

Some of these differences are good, and some are bad. Let's take tha bad first. There are a lot of them.

- It's pretty ugly and verbose. Almost everything is defined by convention, not syntax. Calling through to an overridden superclass implementation is particularly bad, but overall there's a lot of redundancy in there. A carefully crafted set of macros could help this.
- The per-object memory footprint is large. In a language like Objective-C, an object is a single chunk of memory containing a pointer to its class followed by any instance-specific data that object's class requires. An object's size grows only with the amount of data it contains. In this system, an object is a chunk of memory containing one pointer per method implemented by the object's class. Each of those points to a new chunk of memory which is not shared with other objects of that class. Finally, they all point to chunks of shared storage for the object's class's "instance variables", and for each superclass's "instance variables". That's a lot of memory allocations, and their quantity and size dwarfs what you'd find in a language like Objective-C.
- Object creation and destruction is very slow. All of these allocations need to be created and filled out.
- The hierarchy of a class is forcibly exposed to client code because of how superclass methods are accessed. If `MyObject` starts to inherit from `String` instead of `RootObject`, any calls to `myobj->parent.release()` would have to be replaced with `myobj->parent.parent.release()`.
- There's absolutely no metadata or introspection available.
- The result of the pointer casting stuff going on to achieve subtype polymorphism does not actually have a defined result in the C language, although it works in almost any real implementation you'll find.

In my defense, this object system was not meant to be practical, and I built it in about an hour.

Despite all of this, there are some advantages to it:

- It works in plain old C (with Apple's blocks extension), no need for Objective-C or C++ or anything like that.
- Since it's a single struct member load followed by a block call (which is just another struct member load followed by a function pointer invocation), invoking a method should be faster than in Objective-C.
- Methods can be dynamically replaced on individual objects at any time. For example, this is how I tested to make sure that the `dealloc` method really is invoked when an object's retain count reaches zero:

  ```
      obj = Alloc(RootObject);
      void (^olddealloc)(void) = obj->dealloc;
      obj->dealloc = Block_copy(^{
          printf("dealloc was called!\n");
          olddealloc();
      });
      obj->release();
      Block_release(olddealloc);
  ```

  This sort of thing is much more difficult to accomplish in Objective-C.
- Overriding a parent method is a completely separate action from implementing a new method in a child class, eliminating accidental overrides and allowing a child to implement a completely separate method which happens to have the same name.
- The whole object system fits in a page and can be readily understood in a short time.

Again, I don't recommend actually using this object system for anything practical, but it's an interesting construct just the same.

**Conclusion**  
 We now have a fully functional, albeit strange, object system based on blocks, and one that's less than 100 lines long. This object system, while not entirely practical, is an interesting illustration of the sort of power that blocks add to the language.

That wraps up this week's Friday Q&A. Come back next week for another exciting edition. Since Friday Q&A is driven by your suggestions, be sure to send them in! If you liked this week's article and want to see more like it, give me some more ideas along these lines. On the other hand, if you hated it and don't want to see any more like it, give me some ideas in other directions! Whatever your idea, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-10-16-creating-a-blocks-based-object-system.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
