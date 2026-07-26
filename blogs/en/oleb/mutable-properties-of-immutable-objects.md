---
title: Mutable Properties of Immutable Objects
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2009/11/mutable-properties-of-immutable-objects/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7cf669144fac9b1e'
translated: false
---

> 原文：[Mutable Properties of Immutable Objects](https://oleb.net/blog/2009/11/mutable-properties-of-immutable-objects/)　·　Ole Begemann

# Mutable Properties of Immutable Objects

Objects are immutable if their state cannot be changed after initialization. While less flexible than their mutable counterparts, immutable objects have a lot of advantages. For instance, callers of a method that takes an immutable object as a parameter need not fear that the method might change the object. Also, thread safety is much easier to ensure if the objects shared by multiple threads are immutable.

For these and other reasons, it is often a good idea to make your own custom classes immutable, too. If you do so, it is important that all properties of your class also return immutable objects. I found an example of what not to do in the otherwise excellent book [Cocoa Design Patterns](http://www.cocoadesignpatterns.com/) by Erik M. Buck and Donald A. Yacktman: on page 144, they define a class that has a read-only property returning an NSMutableDictionary:

```
@interface WordInformation : NSObject
{
    // ...
    NSMutableDictionary *puzzleSpecificAttributes;
}
// ...
@property (readonly, copy) NSMutableDictionary *puzzleSpecificAttributes;

@end
```

This totally defies the purpose of immutability. Even though the property itself is read-only, users of the class are free to modify the mutable dictionary that is returned by the class’s getter. If your class relies internally on the dictionary not being changed, things can get really ugly. How do we avoid this? The public-facing property must be an (immutable) NSDictionary:

```
@property (readonly) NSDictionary *puzzleSpecificAttributes;
```

But chances are that, internally, you would still like to keep the mutable dictionary. In that case, rename the instance variable so that it does not conflict with the name of the read-only property and, in the implementation of your class, write a custom getter that converts the mutable to an immutable dictionary:

```
@implementation WordInformation

@dynamic puzzleSpecificAttributes;

// ...

- (NSDictionary *)puzzleSpecificAttributes {
    // mutablePuzzleSpecificAttributes is the mutable instance variable
    return [NSDictionary dictionaryWithDictionary:mutablePuzzleSpecificAttributes];
}

// ...
@end
```
