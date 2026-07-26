---
title: 'Friday Q&A 2010-08-12: Implementing NSCoding'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-08-12-implementing-nscoding.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bedbbc37d6bf9ee9'
translated: false
---

> 原文：[Friday Q&A 2010-08-12: Implementing NSCoding](https://www.mikeash.com/pyblog/friday-qa-2010-08-12-implementing-nscoding.html)　·　mikeash.com Friday Q&A

Posted at 2010-08-13 16:35 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-08-27: Defensive Programming in Cocoa](https://www.mikeash.com/pyblog/friday-qa-2010-08-27-defensive-programming-in-cocoa.html)  
Previous article: [Friday Q&A 2010-07-30: Zeroing Weak References to CoreFoundation Objects](https://www.mikeash.com/pyblog/friday-qa-2010-07-30-zeroing-weak-references-to-corefoundation-objects.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [nscoding](https://www.mikeash.com/pyblog/?tag=nscoding) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [serialization](https://www.mikeash.com/pyblog/?tag=serialization)

Friday Q&A 2010-08-12: Implementing NSCoding

by [Mike Ash](https://www.mikeash.com/)

**Serialization**  
 Objects in memory can't be directly saved or moved to other programs. They contain data, such as pointers, which are only valid in the context of your process's memory space. Move the contents of an object into another program and all of those pointers suddenly make no sense. Serialization is the process of converting the non-portable, in-memory representation of an object into a portable stream of bytes that can be stored and moved between processes.

Cocoa offers two built-in serialization methods. The most commonly-used method is property list serialization, implemented in the `NSPropertyListSerialization` class. Property list serialization is fast and produces output that's easy to understand, but is fairly limited in what it can do. It can only store a limited number of classes which support property list serialization, such as `NSDictionary` and `NSString`, and it's not possible to extend the classes it supports.

The other method offered by Cocoa is archiving. Archiving can serialize arbitrary objects connected in arbitrary ways, and reconstitute the entire thing on demand. It's extremely powerful, however it's not completely automatic, and requires the programmer to write some code in order to allow their classes to be archived.

Archiving is split into two pieces. One piece is the actual archiver and unarchiver classes. These are `NSKeyedArchiver` and `NSKeyedUnarchiver` (and their non-keyed equivalents). They handle the nuts and bolts of translating a bunch of objects into a bunch of bytes.

The other piece is the `NSCoding` protocol. This is code that _you_ implement in order to tell the archiver how to encode and decode instances of your class.

**`NSCoding`**  
 The `NSCoding` protocol is short and simple, containing only two methods:

```
    @protocol NSCoding
    
    - (void)encodeWithCoder:(NSCoder *)aCoder;
    - (id)initWithCoder:(NSCoder *)aDecoder;
    
    @end
```

You implement

to tell the archiver how to serialize your object into bytes, and

to tell the archiver how to transform the serialized representation into a new object. It is necessary to implement both methods.

Note that the parameter to `encodeWithCoder:`, although typed as `NSCoder`, is actually the particular archiver instance (for example, an `NSKeyedArchiver`) that you're working with. Likewise, the parameter to `initWithCoder:` is actually the particular unarchiver instance (e.g. `NSKeyedUnarchiver`) that you're using.

**Basic Implementation of `NSCoding`**  
 To implement `encodeWithCoder:`, you should go through all of the essential properties of your object and use the various methods on `NSCoder` to encode them. For object properties, just use `encodeObject:forKey:`. The key can just be a short string that describes the property being encoded:

```
    - (void)encodeWithCoder: (NSCoder *)coder
    {
        [coder encodeObject: [self name] forKey: @"name"];
        [coder encodeObject: [self title] forKey: @"title"];
    }
```

The

implementation is then more or less symmetrical. However, there are a few different ways to implement it, depending on your particular taste.

One way is to implement it as a normal initializer, directly setting your instance variables:

```
    - (id)initWithCoder: (NSCoder *)coder
    {
        if((self = [self init]))
        {
            _name = [[coder decodeObjectForKey: @"name"] retain];
            _title = [[coder decodeObjectForKey: @"title"] retain];
        }
        return self;
    }
```

if you use this style and are not using garbage collection,

. It's easy to forget to do this, but this method follows the standard Cocoa memory management rules and returns an object that you do not own. If you don't retain it, it will disappear and you will crash.

Another way is to use setter methods rather than setting the instance variables directly:

```
    - (id)initWithCoder: (NSCoder *)coder
    {
        if((self = [self init]))
        {
            [self setName: [coder decodeObjectForKey: @"name"]];
            [self setTitle: [coder decodeObjectForKey: @"title"];
        }
        return self;
    }
```

Whether it's better to use a setter or set the instance variable directly is, of course,

a matter of some debate

.

Finally, you can implement it in terms of your normal initializer. Decode the objects first, then call through to your normal initializer:

```
    - (id)initWithCoder: (NSCoder *)coder
    {
        NSString *name = [coder decodeObjectForKey: @"name"];
        NSString *title = [coder decodeObjectForKey: @"title"];
        
        return [self initWithName: name title: title];
    }
```

Of all the possibilities, this last one probably makes things simplest overall. Among other things, it gives your class a single override point for subclasses that need to implement initializers.

**Keyed Versus Unkeyed Archiving**  
 If you look at `NSCoder`, you'll notice that most methods have one variant that takes a key, and one variant that doesn't. For example:

```
    - (void)encodeObject:(id)object;
    - (void)encodeObject:(id)objv forKey:(NSString *)key;
```

So why are there two?

Back in the dark days before Mac OS X 10.2 shipped, the non-keyed variants were all that existed. They require that the exact same sequence of calls be made to encode and decode. Any variation causes an error, because the archiver has no way of knowing what you intended. This caused enormous problems when making changes to a code base over time. If you add a third property that needs to be encoded and you want your code to still be able to read old archives (using a default value for the new property) then you had to jump through many painful hoops.

The keyed variants are enormously more flexible. You can encode and decode in any order. You can encode data and neglect to decode it. When decoding, you can check for the presence of a key and supply a default value or take a different action if it's missing.

Today, there is essentially no reason to support non-keyed archiving. (It can still be useful if you're using `NSPortCoder` with Distributed Objects, but that is an extremely rare situation.) Therefore, in general, you should write your `NSCoding` implementation to assume keyed coding, and use `NSKeyedArchiver` and `NSKeyedUnarchiver`.

If for some reason you do need to support both, you can simply check `[coder allowsKeyedCoding]` to see what kind you're dealing with, and take the appropriate actions.

**Conditional Encoding**  
 The great thing about `NSCoding` is that it makes it easy to encode large, complex object graphs. The coder automatically ensures that cyclical references don't cause an infinite loop, and that multiple references to the same object don't result in multiple copies of that object being encoded.

However, sometimes you don't want to encode the entire object graph. Imagine an implementation of a board game, with a class for the board and for the pieces:

```
    @interface GameBoard : NSObject <NSCoding>
    {
        NSMutableArray *_gamePieces;
    }
    @end
```

```
    @interface GamePiece : NSObject <NSCoding>
    {
        GameBoard *_gameBoard; // weak reference to avoid retain cycles
    }
    @end
```

You want to be able to serialize an entire board and have all of the pieces automatically included. This is easy, of course: just have

encode its

array. You also want to ensure that the

back reference to the board is preserved. This can be done by simply encoding it and decoding it. Since it's a weak reference, you would decode it and not retain it.

This approach works fine as long as you're serializing an entire board. But perhaps you also want to serialize a single piece by itself. What happens then?

With the simple approach to implementing `NSCoding`, you'll end up serializing not only the piece, but the board that it's a part of, every other piece on the board, and any other data that's part of the game board. Worse, because the `_gameBoard` reference is weak, the board will be destroyed after decoding, causing a dangling pointer. Your archives are large and your code sometimes mysteriously crashes when loading them. Not what you want!

In order to solve this problem, `NSCoder` provides _conditional objects_. This allows you to encode an object _only if something else unconditionally encodes it_. If nothing _needs_ the object, then it doesn't get encoded. In that situation, when you decode, you get `nil`.

Conditional objects are perfect for encoding just one piece of a larger object graph. The `GamePiece` can use a conditional object when encoding `_gameBoard`. If you explicitly encode the entire board, then the conditional object will point to it. However, if you encode an individual game piece, then the board will _not_ be encoded, because nothing ever encoded it unconditionally.

Thus, to solve this problem, you simply change `-[GamePiece encodeWithCoder:]` to look like this:

```
    - (void)encodeWithCoder: (NSCoder *)coder
    {
        [coder encodeConditionalObject: _gameBoard forKey: @"gameBoard"];
    }
```

In general, anything that's a weak reference in memory should be a conditional object in your

implementation.

**Encoding Non-Object Data**  
 So far I've talked a lot about encoding objects, but what about all of that non-object data floating around?

For primitives, `NSCoder` provides a variety of methods to encode various integer and floating-point types. You can simply call `encodeInteger:forKey:` or `encodeDouble:forKey:` to save your individual values. For types that aren't supported, for example `short`, you can simply encode as a bigger compatible type that is supported, like `int`.

Structs can get more difficult. Non-keyed archiving actually supported encoding and decoding of arbitrary structs, but for some reason this capability was removed in the keyed archivers. Perhaps because it made things too fragile; you couldn't alter the struct without breaking all of your archives.

In general, the best way to handle a struct is to simply encode and decode each field of the struct separately. If that is too unwieldy, then you should consider rewriting the struct as an Objective-C class that supports `NSCoding` itself, so that you can just directly encode instances of it.

For built-in Cocoa structs like `NSRect`, use the built-in functions to transform them to `NSString`. For example, call `NSStringFromRect` and encode the resulting string, and call `NSRectFromString` on the decoded object. This is somewhat less efficient, but much easier to code and debug.

The worst part is arrays. There is no built-in support for archiving C arrays. There are a few workarounds you can use, depending on how big your arrays are and how much code you want to write:

1. containing instances of

  , and encode that. You can either construct a temporary

  from your C array in your

  implementation, or you can do a complete conversion use the

  throughout.
2. ```
          for(int i = 0; i < arrayLength; i++)
              [coder encodeInt: intArray[i] forKey: [NSString stringWithFormat: @"intArray%d", i]];
  ```

  And then a similar loop on decoding.
3. . This requires paying special attention to things like endianness and data type issues. (If you have an array of

  or

  , they will

  be the same size between machines. If you have an array of any multi-byte values, they may not be in the same format between machines.) How to handle these issues is somewhat beyond the scope of this article, but research on endianness and serializing raw C data should cover it.

For C strings, which are a special case of arrays, the simplest way to handle it is probably to simply convert it to an

and encode that. It would also be safe to run a C string through

.

**Reading Old Archives**  
 If your code lives long enough, eventually you'll change what you encode and decode. Normally, you still want your code to be able to read old archives despite the changes.

For simple changes, like adding a new property to a class, you often don't need to do anything. Your call to `decodeObject:forKey:` will return `nil`. Calls to methods like `decodeIntForKey:` will return `0`. Write your new code to tolerate this, and your job is done.

Sometimes you need to do more. If your changes are complicated enough, you may want to create two separate code paths, one for the old data structure and one for the new. In that case, it's easy to differentiate between the two by adding a `version` key to your `NSCoding` implementation. Check the value of the key when decoding, and you'll know which path to take.

Note that adding a `version` key isn't something that needs to be done ahead of time. You can add it in your new code. The lack of a `version` key in the old archives will identify them as such. If you encode a simple integer, set the new version as `1`, and then trying to get the version of an old archive will conveniently give you `0`, and you'll have room to expand further if you need more changes.

If you refactor your code, you might change class names. If these classes are archived, then you have an incompatibility. The old class name exists in the old archive, and when the unarchiver tries to find it at decoding time, it will fail.

This can be worked around by using the `-setClass:forClassName:` before unarchiving:

```
    [unarchiver setClass: [NewClass class] forClassName: @"OldClass"];
```

**Reading New Archives With Old Code**  
 You often want to go in reverse as well. Just because you added some new information to your archive format doesn't mean you want to make new archives incompatible with old versions of your software. It's not always possible to maintain backwards compatibility, but if your changes are simple then it can be easy.

If you add a new property to a class, ensure that the existing properties remain consistent amongst each other, and complete in terms of what the old version of your software needs. Then old versions will continue to work with little effort. For example, imagine if you add a `title` property to a `Person` class. The old version will only see the old `name` property, and will lose `title`, but will otherwise continue to work.

If you completely revamp a class, you might consider archiving both the new properties _and_ a set of compatibility properties intended for old code. New code can read the new properties, and old code can read the old properties and continue to work, at least in some fashion.

Finally, if you rename a class, that will break old versions of the software unless you compensate for it, just as renaming a class will break old archives. To fix this, you can tell the archiver to save your class under its old name using the `setClassName:forClass:` method:

```
    [archiver setClassName: @"OldClass" forClass: [NewClass class]];
```

Backwards compatibility can be difficult, particularly if you add a lot of new data or capabilities. It's also generally much less important than forward compatibility. Consider all of the tradeoffs involved and don't be afraid to break backwards compatibility. Just ensure that, if you do, trying to load a new archive into an old version of your software fails gracefully.

**Conclusion**  
 `NSCoding` is a powerful way to serialize objects so that you can pass them between processes or save it to a file. Implement the `NSCoding` protocol on your custom objects that you want to serialize, then use `NSKeyedArchiver` to serialize them and `NSKeyedUnarchiver` to deserialize them.

That's it for this edition of Friday Q&A. Come back next time for another exciting adventure in the world of Mac programming. Until then, if you have an idea that you would like to see covered here, please [send me your suggestions](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
