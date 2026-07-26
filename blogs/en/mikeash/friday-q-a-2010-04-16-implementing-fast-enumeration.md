---
title: 'Friday Q&A 2010-04-16: Implementing Fast Enumeration'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-04-16-implementing-fast-enumeration.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f1bdc977e3421779'
translated: false
---

> 原文：[Friday Q&A 2010-04-16: Implementing Fast Enumeration](https://www.mikeash.com/pyblog/friday-qa-2010-04-16-implementing-fast-enumeration.html)　·　mikeash.com Friday Q&A

Posted at 2010-04-16 16:35 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Mistakes and Chains of Events](https://www.mikeash.com/pyblog/mistakes-and-chains-of-events.html)  
Previous article: [An Objective-C Continuations Library](https://www.mikeash.com/pyblog/an-objective-c-continuations-library.html)  
Tags: [enumeration](https://www.mikeash.com/pyblog/?tag=enumeration) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2010-04-16: Implementing Fast Enumeration

by [Mike Ash](https://www.mikeash.com/)

**Basics**  
 There are two benefits to implementing Fast Enumeration. One is that you can then use your object as the target in a `for`/`in` loop. The other is that, with a good implementation, such enumeration will be fast.

Implementing Fast Enumeration is accomplished by implementing the `NSFastEnumeration` protocol. This protocol contains only a single method:

```
    - (NSUInteger)countByEnumeratingWithState:(NSFastEnumerationState *)state objects:(id *)stackbuf count:(NSUInteger)len;
```

Easy enough, right? But what's that `NSFastEnumerationState` thing?

```
    typedef struct {
        unsigned long state;
        id *itemsPtr;
        unsigned long *mutationsPtr;
        unsigned long extra[5];
    } NSFastEnumerationState;
```

This starts to get a little bit complex....

**Deciphering Fields and Parameters**  
 To understand how to implement this method, you need to understand what all of the fields and parameters mean, as well as the return value. I'll take these out of order.

The objective of this method is to return a series of arrays of objects. Each call returns one array, which allows objects to be returned in bulk. For speed, this uses a C array, which means that it needs a pointer and a length.

The length is provided by the return value of the method. That's what the `count` refers to in the name of the method. The array is actually the `itemsPtr` field of the `NSFastEnumerationState` struct. These two values together define the array returned by the method.

`NSFastEnumeration` is designed to allow returning a pointer to internal storage. However, not all data structures fit well with that, so it's also designed to allow copying objects into an array provided by the caller. That caller-provided array is `stackbuf`, and its size is given by `len`.

`NSFastEnumeration` is also designed to detect when a collection is mutated while being enumerated, and throw an exception if this occurs. `mutationsPtr` is indended to be pointed to a value which changes if the collection is mutated.

That's just about everything. The only fields I haven't covered yet are the `state` and `extra` fields of `NSFastEnumerationState`. These are just freeform fields which the callee can use to store whatever values it finds useful.

**Generated Loop Code**  
 Now we know what all these things are for, but to really understand how this stuff works, it's best to understand what kind of code the compiler generates. You write this:

```
    for(id obj in collection)
    {
        // body
    }
```

What really goes on behind the scenes?

The compiler creates an `NSFastEnumerationState` on the stack, as well as a stack buffer. It creates two nested loops, one which repeatedly calls `countByEnumeratingWithState:...` and one which loops over the array it returns. It ends up being something like this:

```
    // declare all the local state needed
    NSFastEnumerationState state = { 0 };
    id stackbuf[16];
    BOOL firstLoop = YES;
    long mutationsPtrValue;
    
    // outer loop
    NSUInteger count;
    while((count = [collection countByEnumeratingWithState: &state objects: stackbuf count: 16]))
    {
        // check for mutation, but only after the first loop
        // (note that I'm not sure whether the real compiler puts this
        // in the inner loop or outer loop, and it could conceivably
        // change from one compiler version to the next)
        if(!firstLoop && mutationsPtrValue != *state.mutationsPtr)
            @throw ..mutation exception...
        firstLoop = NO;
        mutationsPtrValue = *state.mutationsPtr;
        
        // inner loop over the array returned by the NSFastEnumeration call
        id obj;
        for(NSUInteger index = 0; index < count; index++)
        {
            obj = state.itemsPtr[index];
            // body
        }
    }
```

Notice how this code never touches or examines the `state` and `extra` fields. As I mentioned before, these are provided purely for the use of the collection, and to facilitate that, their value is preserved between calls while within the same loop.

**Returning One Object At a Time**  
 A major point of `NSFastEnumeration` is to achieve speed through bulk enumeration. Returning one object at a time defeats that point. However, it's easy to implement, and still gets you the benefit of being able to use `for`/`in` syntax. In the spirit of avoiding premature optimization, if returning one object at a time is easy, then go for it.

As an example, imagine you have a linked list class:

```
    @implementation LinkedList : NSObject
    {
        struct Node *listHead;
    }
```

Now let's implement `NSFastEnumeration` for this class, in the simplest possible way, by returning one object at a time:

```
    - (NSUInteger)countByEnumeratingWithState:(NSFastEnumerationState *)state objects:(id *)stackbuf count:(NSUInteger)len
    {
        // plan of action: extra[0] will contain pointer to node
        // that contains next object to iterate
        // because extra[0] is a long, this involves ugly casting
        if(state->state == 0)
        {
            // state 0 means it's the first call, so get things set up
            // we won't try to detect mutations, so make mutationsPtr
            // point somewhere that's guaranteed not to change
            state->mutationsPtr = (unsigned long *)self;
            
            // set up extra[0] to point to the head to start in the right place
            state->extra[0] = (long)listHead;
            
            // and update state to indicate that enumeration has started
            state->state = 1;
        }
        
        // pull the node out of extra[0]
        struct Node *currentNode = (struct Node *)state->extra[0];
        
        // if it's NULL then we're done enumerating, return 0 to end
        if(!currentNode)
            return NULL
        
        // otherwise, point itemsPtr at the node's value
        state->itemsPtr = &currentNode->value
        
        // update extra[0]
        if(currentNode)
            state->extra[0] = (long)currentNode->next;
        
        // we're returning exactly one item
        return 1;
    }
```

This is really not bad at all. It gets a little ugly with the pointer/integer casting, but that's C for you....

**Returning Copied Objects in Bulk**  
 Let's say that it turns out the above method really is too slow and you want to make it faster. You can do this by returning objects in bulk. Because the objects in the linked list aren't stored contiguously, you have to do this by copying objects into the `stackbuf`. While no guarantee is given as to the size of `stackbuf`, we can assume that it's made large enough to justify this sort of thing. Here's how the code would look:

```
    - (NSUInteger)countByEnumeratingWithState:(NSFastEnumerationState *)state objects:(id *)stackbuf count:(NSUInteger)len
    {
        // plan of action: pretty much the same as before,
        // with extra[0] pointing to the next node to use
        // we just iterate over multiple nodes at once
        if(state->state == 0)
        {
            state->mutationsPtr = (unsigned long *)self;
            state->extra[0] = (long)listHead;
            state->state = 1;
        }
        
        // pull the node out of extra[0]
        struct Node *currentNode = (struct Node *)state->extra[0];
        
        // keep track of how many objects we iterated over so we can return
        // that value
        NSUInteger objCount = 0;
        
        // we'll be putting objects in stackbuf, so point itemsPtr to it
        state->itemsPtr = stackbuf;
        
        // loop through until either we fill up stackbuf or run out of nodes
        while(currentNode && objCount < len)
        {
            // fill current stackbuf location and move to the next
            *stackbuf++ = currentNode->value
            
            // move to next node
            currentNode = currentNode->next;
            
            // and keep our count
            objCount++;
        }
        
        // update extra[0]
        if(currentNode)
            state->extra[0] = (long)currentNode->next;
        
        return objCount;
    }
```

This is not too much harder, and will significantly reduce the number of message sends that occur in the `for`/`in` loop.

**Returning a Bulk Interior Pointer**  
 For best efficiency, you can return a pointer to contiguously stored objects. For example, say you have a simple array class like this:

```
    @interface Array : NSObject
    {
        id *pointer;
        NSUInteger count;
    }
```

Implementing `NSFastEnumeration` for this class is really easy. It can return a single interior pointer to all of the objects, and that's it

```
    - (NSUInteger)countByEnumeratingWithState:(NSFastEnumerationState *)state objects:(id *)stackbuf count:(NSUInteger)len
    {
        if(state->state == 0)
        {
            state->mutationsPtr = (unsigned long *)self;
            state->itemsPtr = pointer;
            state->state = 1;
            return count;
        }
        else
            return 0;
    }
```

That was easy! It'll also be really fast, because the enumeration loop will basically devolve into a straight C `for` loop.

This technique can also be used, with some care, for more complex data structures. If you have a series of contiguous object pointers, you can return pointers to each one in turn, which will result in efficient enumeration over all of the objects in sequence. You can make good use of the `extra` values to keep track of where you are in your internal data structure.

**A Note on Temporary Objects**  
 You may find it useful to store Objective-C objects in the `extra` values:

```
    state->extra[1] = (long)[NSArray arrayWith...];
```

But beware! This will break with this completely legal enumeration code:

```
    NSAutoreleasePool *pool = [NSAutoreleasePool new];
    for(id obj in collection)
    {
        // do stuff with obj
        [pool release];
        pool = [NSAutoreleasePool new];
    }
    [pool release];
```

When the autorelease pool goes away, it'll take your array with it, and the next time you try to access it, you'll explode. And you can't retain the array, either, because there's no guarantee the caller will loop all the way to the end to let you release it; they might `break` out of the loop early, and then you've leaked the object.

There's really no general way to solve this. (I've concocted a completely insane scheme which involves tracking the position of the stack pointer to know when it's safe to destroy temporary objects, but it's, well, completely insane.) If you can, try to avoid storing temporary Objective-C objects in `extra` like this. And if you must do it, just keep in mind that you have to be careful with autorelease pools in the `for`/`in` loops that you use with this object. Since you're likely to be the only client of your `NSFastEnumeration` implementation, this is a reasonable constraint to make, but it's something that you have to be aware of.

**Conclusion**  
 Implementing `NSFastEnumeration` allows you to use nice, simple syntax for enumerating over your custom objects which are conceptually collections of other objects. As a bonus, it will usually speed up that enumeration as well. And while `NSFastEnumeration` can look daunting at first glance, it's actually pretty easy to write an implementation of it, depending on just how hard-core you want to get and how complex your internal data structures are.

That's it for this week's Friday Q&A. Come back in another seven days for more gooey goodness. Friday Q&A is driven by user submissions, so in the meantime, if you have an idea for a topic that you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-04-16-implementing-fast-enumeration.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
