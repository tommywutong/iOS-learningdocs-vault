---
title: previously explored building NSNotificationCenter
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-07-08-lets-build-nsnotificationcenter.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6c11a41cc9bd4a81'
translated: false
---

> 原文：[previously explored building NSNotificationCenter](https://www.mikeash.com/pyblog/friday-qa-2011-07-08-lets-build-nsnotificationcenter.html)　·　mikeash.com Friday Q&A

Posted at 2011-07-08 16:11 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2011-07-22: Writing Unit Tests](https://www.mikeash.com/pyblog/friday-qa-2011-07-22-writing-unit-tests.html)  
Previous article: [Friday Q&A Delayed Again](https://www.mikeash.com/pyblog/friday-qa-delayed-again.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [notifications](https://www.mikeash.com/pyblog/?tag=notifications)

Friday Q&A 2011-07-08: Let's Build NSNotificationCenter

by [Mike Ash](https://www.mikeash.com/)

**Code**  
The code that I built is available as a complete unit on github at [https://github.com/mikeash/MANotificationCenter](https://github.com/mikeash/MANotificationCenter). While I don't believe it's useful for practical work (you might as well just use `NSNotificationCenter`), it can be interesting to look at it in its entirety.

**Interface**  
The goal is to essentially reimplement `NSNotificationCenter` as a class which I'll call `MANotificationCenter`, but to make things a little bit easier, I decided to cut down the API a bit. `NSNotificationCenter` started out with an API for observing based on an observer/selector pair, then in 10.6 added a second method for using a block as an observer instead. Since blocks are ultimately much more natural for this sort of work, my version of the API just has a blocks-based method:

```
    - (id)addObserverForName: (NSString *)name object: (id)object block: (void (^)(NSNotification *note))block;
```

Like with `NSNotificationCenter`, this method returns an opaque object which the caller is expected to use to remove the observer:

```
    - (void)removeObserver: (id)observer;
```

The older object/selector API can be implemented in terms of this one, so we don't lose any functionality by only offering this. The basic idea of how things work under the hood is also essentially the same, the only difference is whether you call a block or send a selector to an object when it comes time to notify observers.

Finally we need to be able to post a notification:

```
    - (void)postNotification: (NSNotification *)note;
```

`NSNotificationCenter` has other posting methods which take objects and names directly, but those simply construct the `NSNotification` object and then call through to this, so again, we lose nothing by not having the other methods. They are really just one-line wrappers around this one.

And that's it for the API. It's pretty simple. It's interesting to note that `NSNotificationCenter` isn't all that much more complicated. It only has seven instance methods, and two of them are just convenience wrappers.

**Implementation**  
Before we get to actual _code_, let's talk some theory.

A notification is defined by the object that posts the notification, the notification's name, and arbitrary user info that's attached to the notification. The object and name are used to determine which observers need to be notified.

That last part is the key. In essence, the notification center maps `object, name` pairs to observers. In this case, since `MANotificationCenter` is blocks-based, it will map those pairs to observer blocks. Multiple observer can be registered on a single `object, name` pair, so they need to map to a collection that will hold multiple observer blocks.

In Cocoa terms, when we say "map", this usually means a dictionary. Unfortunately, using pairs as dictionary keys is a little inconvenient, because `NSDictionary` only takes a single object as the key. To mitigate this, we'll create a separate "key" class which holds the pair and can be a single object for the dictionary key. For the collection of observer blocks, we don't care about order, so we can just use an `NSMutableSet`.

This class will therefore have a master `NSMutableDictionary` which maps keys to `NSMutableSet` instances which then contain the individual observer blocks. And that's really all there is to it.

**The Key Class**  
The key class is pretty simple, but it's worth discussing just how it works so everybody is on the same page. It's just a small class which holds a name and an object and implements equality, hashing, and copying appropriately. One small detail, the object reference needs to be a weak reference, as the notification system isn't supposed to retain the objects it manages (which frequently deregister themselves in response to being deallocated, so that would be problematic).

On a side note, I frequently warn of the dangers of plain weak references, and recommend using a zeroing weak reference class like my own [`MAZeroingWeakRef`](https://github.com/mikeash/MAZeroingWeakRef/) instead. However, in the interest of brevity and clarity, I'm going to use plain, dangerous, regular weak references in this code.

The interface for this class is simple: two instance variables, and one public class method to make instances:

```
    @interface _MANotificationCenterDictionaryKey : NSObject
    {
        NSString *_name;
        id _object;
    }

    + (_MANotificationCenterDictionaryKey *)keyForName: (NSString *)name object: (id)obj;

    @end
```

That public method just does the typical dance of `alloc`, `init`, `autorelease`, using a private `init` method:

```
    + (_MANotificationCenterDictionaryKey *)keyForName: (NSString *)name object: (id)obj
    {
        return [[[self alloc] _initWithName: name object: obj] autorelease];
    }
```

The `init` and `dealloc` methods are likewise simple, just setting and cleaning up the instance variables:

```
    - (id)_initWithName: (NSString *)name object: (id)obj
    {
        if((self = [self init]))
        {
            _name = [name copy];
            _object = obj;
        }
        return self;
    }

    - (void)dealloc
    {
        [_name release];
        [super dealloc];
    }
```

Next comes equality. I want this class to be able to handle `nil` for either the name or the object (or both), as this will come in handy later when implementing `nil` catchall observers, where an observer can register for a `nil` name to mean "all notifications from the given object", register for a `nil` object to mean "all notifications with a given name", and register with `nil` for both to catch all notifications sent through the system. However, notification names need to be compared with `isEqual:`, which doesn't play nice with `nil`. To make this simpler, I created a really quick equality-checking helper which correctly handles `nil` and only uses `isEqual:` when both objects exist:

```
    static BOOL Equal(id a, id b)
    {
        if(!a && !b)
            return YES;
        else if(!a || !b)
            return NO;
        else
            return [a isEqual: b];
    }
```

With that helper in place, the implementation of `isEqual:` is simple and follows the standard pattern of checking the class of the other object and then comparing instance variables:

```
    - (BOOL)isEqual: (id)other
    {
        if(![other isKindOfClass: [_MANotificationCenterDictionaryKey class]])
            return NO;

        _MANotificationCenterDictionaryKey *otherKey = other;
        return Equal(_name, otherKey->_name) && _object == otherKey->_object;
    }
```

The implementation of `hash` just gets the hashes of the two instance variables and squishes them together:

```
    - (NSUInteger)hash
    {
        return [_name hash] ^ (uintptr_t)_object;
    }
```

Finally, to be a dictionary key, we need `copyWithZone:`. Since this class is immutable, that method can just retain `self` and return it:

```
    - (id)copyWithZone: (NSZone *)zone
    {
        return [self retain];
    }
```

That takes care of keys. On to the notification center itself.

**Notification Center Implementation**  
The `init` and `dealloc` implementations are short. There's an `NSMutableDictionary *_map` instance variable, and they just set it up and tear it down:

```
    - (id)init
    {
        if((self = [super init]))
        {
            _map = [[NSMutableDictionary alloc] init];
        }
        return self;
    }

    - (void)dealloc
    {
        [_map release];
        [super dealloc];
    }
```

Next up is the implementation of `-addObserverForName:object:block:`, which is where most of the work takes place. The first thing it needs to do is grab a key object so it can use that to work with the observers dictionary:

```
    - (id)addObserverForName: (NSString *)name object: (id)object block: (void (^)(NSNotification *note))block
    {
        _MANotificationCenterDictionaryKey *key = [_MANotificationCenterDictionaryKey keyForName: name object: object];
```

Next, it needs to grab the `NSMutableSet` of observers for that key. This is a straightforward `objectForKey:` lookup, except for the fact that the observers set might not exist yet. If that's the case, we create it on demand and put it into the observers dictionary:

```
        NSMutableSet *observerBlocks = [_map objectForKey: key];
        if(!observerBlocks)
        {
            observerBlocks = [NSMutableSet set];
            [_map setObject: observerBlocks forKey: key];
        }
```

Next, shove the observation block into the set. Since an `NSMutableSet` will only retain its objects, and blocks _must_ be copied if they're kept around, we'll copy it ourselves before handing it off to the set:

```
        void (^copiedBlock)(NSNotification *note);
        copiedBlock = [block copy];

        [observerBlocks addObject: copiedBlock];

        [copiedBlock release];
```

That's just about it. Everything is now in place in the observers dictionary for `-postNotification:` to do its job. There's just one piece missing in this method: the return value. This method is supposed to return some sort of object which, when passed to `-removeObserver:`, causes the observation entry to be removed.

This object would generally encapsulate everything needed to find the entry again and remove it. In this particular case, it would need to hold the key and the copied block. These two objects could be stored in some sort of Cocoa collection like an `NSArray` or an `NSDictionary`, but that causes a lot of unpleasant boxing and unboxing activity as you construct the objects and extract the values from them. They could be stored in a custom class, but it's irritating to build a whole extra custom class just for this tiny use case.

After some thought, I decided to return a block. All of the information needed to remove the observation entry is available in the current scope, and so can be captured by the block. As a bonus, we can capture the existing `observerBlocks` variable so that the set doesn't have to be looked up a second time. `-removeObserver:` can then just call this block, and everything is happy. I decided to go with this, and I think it turned out pretty well.

The removal block first just pulls the block out of the observers set:

```
        void (^removalBlock)(void) = ^{
            [observerBlocks removeObject: copiedBlock];
```

Next, if the observers set is empty, it removes that entry from the observers dictionary entirely. This keeps empty `NSMutableSet` instances from building up in the dictionary after objects are destroyed:

```
            if([observerBlocks count] == 0)
                [_map removeObjectForKey: key];
        };
```

That's it for the removal block. All that's left is to return it to the caller, and we're done:

```
        return [[removalBlock copy] autorelease];
    }
```

With this implementation, the `-removeObserver:` method becomes really short. It just converts the object into the proper block type and then calls it:

```
    - (void)removeObserver: (id)observer
    {
        void (^removalBlock)(void) = observer;
        removalBlock();
    }
```

Next up is a helper method which actually handles the sending of a notification. This is separate from `-postNotification:` so that we can properly handle `nil` catch-all observations. More on that in a moment. This method takes a notification, a name, and an object (yes, those are stored in the notification, but again, this helps with catch-all handling), looks up the set of observers in the master dictionary, and then calls all of the corresponding blocks:

```
    - (void)_postNotification: (NSNotification *)note name: (NSString *)name object: (id)object
    {
        _MANotificationCenterDictionaryKey *key = [_MANotificationCenterDictionaryKey keyForName: name object: object];
        NSSet *observerBlocks = [_map objectForKey: key];
        for(void (^block)(NSNotification *) in observerBlocks)
            block(note);
    }
```

Finally we have `-postNotification:`. A simple implementation would be call the above method, passing `[note name]` and `[note object]` as the last two parameters. However, to handle catch-all observers, we'll actually call the above method four times in a row. The first time, it's called with the name and object. The second time it's called with only the name, and a `nil` object. This notifies catch-all observers registered for the name. Next, it's called with a `nil` name and the notification's object, which notifies catch-all observers on the object. Finally, it's called with `nil` for both parameters, which notifies universal catch-all observers.

Here's what the method looks like:

```
    - (void)postNotification: (NSNotification *)note
    {
        NSString *name = [note name];
        id object = [note object];

        [self _postNotification: note name: name object: object];
        [self _postNotification: note name: name object: nil];
        [self _postNotification: note name: nil object: object];
        [self _postNotification: note name: nil object: nil];
    }
```

By making `-addObserverForName:object:block:` accept `nil`, little else needs to be done to implement the catch-all behavior. A `nil` object or name is treated much like any other name, except that all notifications are sent to `nil` as well as the specific objects they're targeted for.

**A Few Caveats**  
Since this code is intended mainly for educational purposes, it doesn't quite have everything that a real, practical implementation would have.

First, it doesn't have a way to get a singleton instance. That is really useful for notifications, because the entire point of notifications is often to have objects communicate when they don't otherwise know very much about each other, and having to pass around notification center instances would kind of defeat the point. This is, of course, pretty simple to add.

Second, it's not thread safe. Adding and removing observers mutates shared data structures which would need to be protected by a lock. Making it thread safe could get complicated, since the simplest implementation would hold the lock while posting notifications, but notification observers might then try to come back and twiddle with the notification center, leading to a deadlock. A better approach might be to use a dispatch queue, so that all mutations can be enqueued and executed later if the notification center is busy.

Last, it's also not reentrant. If a notification observer manipulates the notification center, it could end up mutating the `observerBlocks` set that the center is currently iterating over, causing a mutation exception to be thrown. It could even cause the set to be deallocated entirely, resulting in a crash. Some sort of queue to hold modifications, whether a dispatch queue or something else, would solve this. Another option, albeit slower, would be to simply copy `observerBlocks` before iterating over it, so that modifications can't touch the iterated copy.

**Conclusion**  
Having a working implementation of something like `NSNotificationCenter` lets us get a better idea of just what's going on inside. Most importantly, it makes it clear that there's no magic going on inside. Notifications aren't some special language feature that's hard to understand, it's actually just a simple dispatch mechanism where a basic implementation can fit in around a hundred lines of code.

A common question about notifications is just when and where they run. Many people see the word "notification" and start thinking in terms of complicated cross-thread communication or delayed delivery mechanisms. However, we can see that this simply isn't how things work. When `-postNotification:` is called, the various observers are called one by one right in the method, and it doesn't return until they're all done. (Note: this does not apply to the `NSNotificationCenter` method which takes a block and an `NSOperationQueue`. When a queue is provided for that method, the observation block runs asynchronously.)

That wraps things up for this week. Come back soon for another edifying Friday Q&A about daring and unusual topics. As always, those topics come from reader suggestions, so if you have a topic that you would like to see covered here, please [send it in](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
