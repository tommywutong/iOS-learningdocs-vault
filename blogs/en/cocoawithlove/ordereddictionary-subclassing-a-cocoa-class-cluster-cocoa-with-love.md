---
title: 'OrderedDictionary: Subclassing a Cocoa class cluster | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/12/ordereddictionary-subclassing-cocoa.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:e7bf4626c60f5b5f'
translated: false
---

> 原文：[OrderedDictionary: Subclassing a Cocoa class cluster | Cocoa with Love](https://www.cocoawithlove.com/2008/12/ordereddictionary-subclassing-cocoa.html)　·　Cocoa with Love (Matt Gallagher)

The default Cocoa collection classes are highly capable but there are situations where you may need to override them to alter their functionality. I'll explain when and how you should do this with an example class: OrderedDictionary (an NSMutableDictionary subclass that maintains ordering of its keys).

## Best practice: don't subclass

This post is going to discuss subclassing `NSMutableDictionary`. You should note that this is a special case; most of the time when you add functionality to a collection class, you should not override it.

Most classes are not designed with subclassing in mind. If you are not the author of a class, choosing to override it incurs a risk that your additions won't maintain implicit or private values and behaviors of the object correctly.

Increased risk due to subclassing does not apply to classes that are intended to be subclassed before use. Prominent examples include `NSObject`, `NSWindowController`, `NSView`, `NSControl` and `NSCell`. With classes designed for use through subclasses, any risk associated with the subclassing itself is more than outweighed by the well-tested base functionality that they provide, which cannot be accessed unless the class is subclassed.

### Aside: design patterns that customize behavior without subclassing

1. Put the custom functionality in the parent which contains the non-overridden object, rather than in the non-overridden object itself. This is "[has-a](http://en.wikipedia.org/wiki/Has-a)" design instead of "[is-a](http://en.wikipedia.org/wiki/Is-a)".
2. Use a [Decorator](http://en.wikipedia.org/wiki/Decorator_pattern) object instead. A Decorator is a wrapper around the non-overridden class. All messages to the contained class go through the Decorator first, so the Decorator can control or supplement the behavior of the contained class.
3. Use an [Observer](https://www.cocoawithlove.com/2008/06/five-approaches-to-listening-observing.html) to keep the non-overridden object synchronized with dependent objects so that their combined state achieves custom behavior, even though each of the objects remains non-custom. In this case, the Observer acts as a Controller/Manager to the dependent objects.

## Choosing to override a collection class

The collection classes in Cocoa are [class clusters](http://developer.apple.com/DOCUMENTATION/Cocoa/Conceptual/CocoaFundamentals/CocoaObjects/chapter_3_section_9.html). In some respects, this means that they _are_ intended to be overridden, since the base class is functionally abstract and contains none of the required concrete functionality.

Default concrete functionality for a class cluster is provided by hidden subclasses, returned transparently by the base class. Since this is transparent, you are not normally expected to write the subclasses yourself. Despite this expectation, the interface _has_ been designed with subclassing in mind, so we can easily implement the required subclass behavior ourselves instead of relying upon one of the default implementations.

The functionality which constitutes "concrete" behavior for a class cluster is given in Apple's documentation as the "primitive" methods of the cluster. For collection classes (like `NSMutableDictionary`), these "primitive" methods provide all behavior for the collection's storage. Since we inherit no default behavior for these primitive methods, this means that the decision to make subclass of a collection class in Cocoa is a decision to reimplement the storage.

## Design of an Ordered NSMutableDictionary subclass

I have chosen to implement an ordered version of `NSMutableDictionary`, named `OrderedDictionary`. This requires ordered storage of dictionary keys but `NSDictionary` stores its keys in a hash table, which is unordered by design. Since this lack of order is fundamental to the hash table storeage, our subclassing of `NSMutableDictionary` (and hence reimplementation of the storage) is appropriate.

However, I will reimplement basic storage for my subclass by storing all objects and keys in an unmodified `NSMutableDictionary`. From a design point-of-view, this will make my subclass a Decorator around the unmodified `NSMutableDictionary`, rather than a pure subclass.

As messages are passed from the "primitive" methods on my subclass through to the contained `NSMutableDictionary`, I will also store the dictionary's keys in a separate `NSMutableArray`, thereby allowing the `OrderedDictionary` to keep the ordering for the keys, in addition to standard `NSMutableDictionary` functionality.

## Implementing the primitive methods

Apple's documentation lists the following "primitive" methods for `NSMutableDictionary`:

- `count`
- `objectForKey:`
- `keyEnumerator`
- `setObject:forKey:`
- `removeObjectForKey:`

In reality, the following method is also required, despite not being listed:

- `initWithCapacity:`

In accordance with the Decorator pattern that I've chosen, almost all of these are implemented by passing the message through to the contained `NSMutableDictionary` (named "`dictionary`"), with keys also added to the `NSMutableArray` (named "`array`") and the `keyEnumerator` method returning the `objectEnumerator` of "`array`":

```objc
- (id)initWithCapacity:(NSUInteger)capacity
{
    self = [super init];
    if (self != nil)
    {
        dictionary = [[NSMutableDictionary alloc] initWithCapacity:capacity];
        array = [[NSMutableArray alloc] initWithCapacity:capacity];
    }
    return self;
}

- (void)dealloc
{
    [dictionary release];
    [array release];
    [super dealloc];
}

- (void)setObject:(id)anObject forKey:(id)aKey
{
    if (![dictionary objectForKey:aKey])
    {
        [array addObject:aKey];
    }
    [dictionary setObject:anObject forKey:aKey];
}

- (void)removeObjectForKey:(id)aKey
{
    [dictionary removeObjectForKey:aKey];
    [array removeObject:aKey];
}

- (NSUInteger)count
{
    return [dictionary count];
}

- (id)objectForKey:(id)aKey
{
    return [dictionary objectForKey:aKey];
}

- (NSEnumerator *)keyEnumerator
{
    return [array objectEnumerator];
}
```

You can [download the complete OrderedDictionary class here](https://www.cocoawithlove.com/assets/objc-era/OrderedDictionary.zip) (2kb). I've further added `init`, `insertObject:forKey:atIndex:`, `keyAtIndex:`, `reverseKeyEnumerator` and `descriptionWithLocale:indent:` methods to the downloadable version to fill out some non-essential functionality.

## Conclusion

Creating a subclass of `NSMutableDictionary` is made relatively simple by the clean set of "primitive" methods for the class cluster. With these implemented, the remaining rich functionality of `NSDictionary` and `NSMutableDictionary` become available; no further work required.

My point about the risks of subclassing should become apparent with the undocumented requirement of `initWithCapacity:`. The necessity of this method is not mentioned in the documentation, so I was forced to use feedback from debugging information to rework the design of the class to reach a functional implementation — trivial in this case but annoying nonetheless.

The inclusion of the `descriptionWithLocale:indent:` method in the class is another lesson along the same lines: the default implementation of this method assumes it can reorder the keys returned from `keyEnumerator` without causing problems. After seeing erroneous results during testing, I was required to replace this method to remove the incorrect assumption.
