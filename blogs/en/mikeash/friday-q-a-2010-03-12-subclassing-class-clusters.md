---
title: 'Friday Q&A 2010-03-12: Subclassing Class Clusters'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-03-12-subclassing-class-clusters.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:8ae1efc459150fb8'
translated: false
---

> 原文：[Friday Q&A 2010-03-12: Subclassing Class Clusters](https://www.mikeash.com/pyblog/friday-qa-2010-03-12-subclassing-class-clusters.html)　·　mikeash.com Friday Q&A

Posted at 2010-03-12 18:51 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A Skips a Week](https://www.mikeash.com/pyblog/friday-qa-skips-a-week.html)  
Previous article: [Friday Q&A 2010-03-05: Compound Futures](https://www.mikeash.com/pyblog/friday-qa-2010-03-05-compound-futures.html)

Friday Q&A 2010-03-12: Subclassing Class Clusters

by [Mike Ash](https://www.mikeash.com/)

**Abstract Classes**  
 To subclass a class cluster, you need to know what it is, and to understand class clusters you must first understand the concept of _abstract classes_. It's an easy concept, though.

An _abstract class_ is a class which is not fully functional on its own. It must be subclassed, and the subclass must fill out the missing functionality.

An abstract class is not necessarily an empty shell. It can still contain a lot of functionality all on its own, but it's not complete without a subclass to fill in the holes.

**Class Clusters**  
 A class cluster is a hierarchy of classes capped off by a public abstract class. The public class provides an interface and a lot of auxiliary functionality, and then core functionality is implemented by private subclasses. The public class then provides creation methods which return instances of the private subclasses, so that the public class can be used without knowledge of those subclasses.

Take `NSArray` as an example. It's an abstract class which requires its subclasses to provide implementations of the `count` and `objectAtIndex:` methods. It then provides a bunch of methods built on top of those two, such as `indexOfObject:`, `objectEnumerator`, `makeObjectsPerformSelector:`, and many more.

The core functionality is then implemented in private subclasses such as `NSCFArray`. The `NSArray` creation methods such as `+arrayWithObjects:` or `-initWithContentsOfFile:` then produce instances of those private subclasses.

From the outside, the cluster nature of `NSArray` is not readily apparent most of the time. It usually makes itself known if you start introspecting the classes of objects, and confuses programmers when they create an `NSArray` and then start getting messages about an `NSCFArray`. Other than that, `NSArray` mostly looks and acts like any other class.

There is one place where the cluster nature is hugely important, and that's if you subclass the public class yourself.

**Subclassing**  
 Subclassing a class cluster (which means subclassing an abstract class) is completely different from subclassing a normal class.

When subclassing a normal class, your superclass provides full functionality for whatever it does. A subclass with an empty implementation is completely valid in this case, and will behave just like the superclass. You can then add methods to your implementation to add new functionality or override existing functionality.

When subclassing a class cluster, your superclass does _not_ provide full functionality. It provides a lot of ancillary functionality, but you must provide the core yourself. This means that an empty subclass is _not_ valid. There is a minimum set of methods that you must implement.

In class cluster teminology, those methods that you must implement are called _primitive methods_. How do you find them? There are two easy ways.

The first way is to crack open the documentation for the cluster class and search it for the word "primitive". The docs will tell you which methods you have to override.

The second way is to open the header for the cluster class. Primitive methods are always found in the class's main `@interface` block. Additional methods provided by the cluster are always found in categories.

Watch out when looking at cluster classes which are themselves subclasses of another cluster class. The result inherits all primitive methods, and you must implement both sets. For example, `NSMutableArray` has five primitive methods of its own _plus_ the two from `NSArray`. If you subclass `NSMutableArray`, you must provide implementations for all seven.

**Techniques**  
 Now you know what to implement, but how? There are three main ways.

First, you can simply provide your own implementation of the primitive methods, implementing them all from scratch. For example, imagine you're writing a specialized array optimized for holding two elements:

```
    @interface MyPairArray : NSArray
    {
        id _objs[2];
    }
    
    - (id)initWithFirst: (id)first second: (id)second;
    
    @end
    
    @implementation MyPairArray
    
    - (id)initWithFirst: (id)first second: (id)second
    {
        if((self = [self init]))
        {
            _objs[0] = [first retain];
            _objs[1] = [second retain];
        }
        return self;
    }
    
    - (void)dealloc
    {
        [_objs[0] release];
        [_objs[1] release];
        [super dealloc];
    }
    
    - (NSUInteger)count
    {
        return 2;
    }
    
    - (id)objectAtIndex: (NSUInteger)index
    {
        if(index >= 2)
            [NSException raise: NSRangeException format: @"Index (%ld) out of bounds", (long)index];
        return _objs[index];
    }
    
    @end
```

Precisely how you implement the primitives depends, of course, on precisely what you want them to do.

Second, you can keep a working instance around, obtained from the public API, and pass your calls through to it:

```
    @interface MySpecialArray : NSArray
    {
        NSArray *_realArray;
    }
    
    - (id)initWithArray: (NSArray *)array;
    
    @end
    
    @implementation MySpecialArray
    
    - (id)initWithArray: (NSArray *)array
    {
        if((self = [self init]))
        {
            _realArray = [array copy];
        }
        return self;
    }
    
    - (void)dealloc
    {
        [_realArray release];
        [super dealloc];
    }
    
    - (NSUInteger)count
    {
        return [_realArray count];
    }
    
    - (id)objectAtIndex: (NSUInteger)index
    {
        id obj = [_realArray objectAtIndex: index];
        // do some processing with obj
        return obj;
    }
    
    // maybe implement more methods here
    
    @end
```

This technique allows you to reuse the existing implementations of the primitive methods, and then add more functionality.

The third technique is to simply add a category to the cluster class instead of subclassing it. People often subclass simply to add new methods, and not to modify existing functionality. In Objective-C, you can add new methods in a category:

```
    @interface NSArray (FirstObjectAdditions)
    
    - (id)my_firstObject;
    
    @end
    
    @implementation NSArray (FirstObjectAdditions)
    
    - (id)my_firstObject
    {
        return [self count] ? [self objectAtIndex: 0] : nil;
    }
    
    @end
```

(The method is prefixed to prevent a conflict if Apple should ever add a

method.)

**Conclusion**  
 Class clusters are different from normal classes, but are easy to subclass once you understand the differences and what they mean. You're required to implement the class cluster's _primitive methods_, which you can do by providing a from-scratch implementation, or by passing through to another instance. Finally, if your only purpose in subclassing is to add new methods, create a category instead.

That's it for this week. Come back in seven days for another crunchy post. Until then, keep your ideas coming. Friday Q&A is driven by reader ideas, so if you have a topic that you would like to see covered here, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
