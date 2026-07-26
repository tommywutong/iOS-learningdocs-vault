---
title: 'Friday Q&A 2015-07-17: When to Use Swift Structs and Classes'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-07-17-when-to-use-swift-structs-and-classes.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:cf7eb7ccb13698ca'
translated: false
---

> 原文：[Friday Q&A 2015-07-17: When to Use Swift Structs and Classes](https://www.mikeash.com/pyblog/friday-qa-2015-07-17-when-to-use-swift-structs-and-classes.html)　·　mikeash.com Friday Q&A

Posted at 2015-07-17 12:54 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2015-07-31: Tagged Pointer Strings](https://www.mikeash.com/pyblog/friday-qa-2015-07-31-tagged-pointer-strings.html)  
Previous article: [Friday Q&A 2015-07-03: Address Sanitizer](https://www.mikeash.com/pyblog/friday-qa-2015-07-03-address-sanitizer.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2015-07-17: When to Use Swift Structs and Classes

by [Mike Ash](https://www.mikeash.com/)

**Values Versus References**  
The answer is actually really simple: use `struct`s when you need value semantics, and use `class`es when you need reference semantics. That's it!

Come back next week for....

**Wait**  
What?

**That Doesn't Answer It**  
What do you mean? It's right there.

**Yes, But...**  
What?

**What Are Value and Reference Semantics?**  
_Oh,_ I see. Maybe I should talk about that, then.

**And How They Relate to `struct` and `class`**  
Right.

It all comes down to data and where it's stored. We store stuff in local variables, parameters, properties, and globals. There are fundamentally two different _ways_ to store that stuff in all these places.

With value semantics, the data exists directly in the storage location. With reference semantics, the data exists elsewhere, and the storage location stores a _reference_ to it. This difference isn't necessarily apparent when you access the data. Where it makes itself known is when you copy the storage. With value semantics, you get a new copy of the data. With reference semantics, you get a new copy of the reference to the same data.

This is all really abstract. Let's look at an example. To remove the question of Swift from the picture for a moment, let's look at an Objective-C example:

```
    @interface SomeClass : NSObject 
    @property int number;
    @end
    @implementation SomeClass
    @end

    struct SomeStruct {
        int number;
    };

    SomeClass *reference = [[SomeClass alloc] init];
    reference.number = 42;
    SomeClass *reference2 = reference;
    reference.number = 43;
    NSLog(@"The number in reference2 is %d", reference2.number);

    struct SomeStruct value = {};
    value.number = 42;
    struct SomeStruct value2 = value;
    value.number = 43;
    NSLog(@"The number in value2 is %d", value2.number);
```

This prints:

```
    The number in reference2 is 43
    The number in value2 is 42
```

Why the difference?

The code `SomeClass *reference = [[SomeClass alloc] init]` creates a new instance of `SomeClass` in memory, then puts a reference to that instance in the variable. The code `reference2 = reference` places a reference to that same object into the new variable. Then `reference.number = 43` modifies the number stored in the object both variables now point to. The result is that when the log prints the value from the object, it prints `43`.

The code `struct SomeStruct value = {}` creates a new instance of `SomeStruct` in the variable. The code `value2 = value` copies that instance into the second variable. Each variable contains a separate chunk of data. The code `value.number = 43` only modifies the one in `value`, and when the log prints the number from `value2` it still prints 42.

This example maps directly to Swift:

```
    class SomeClass {
        var number: Int = 0
    }

    struct SomeStruct {
        var number: Int = 0
    }

    var reference = SomeClass()
    reference.number = 42
    var reference2 = reference
    reference.number = 43
    print("The number in reference2 is \(reference2.number)")

    var value = SomeStruct()
    value.number = 42
    var value2 = value
    value.number = 43
    print("The number in value2 is \(value2.number)")
```

As before, this prints:

```
    The number in reference2 is 43
    The number in value2 is 42
```

**Experience With Value Types**  
Value types aren't new. But for a lot of people they _feel_ new. What's the deal?

`struct`s aren't used that often in most Objective-C code. We occasionally touch them in the form of `CGRect` and `CGPoint` and friends, but rarely make our own. For one thing, they aren't very functional. It's really difficult to correctly store references to objects in a `struct` in Objective-C, especially when using ARC.

Lots of other languages don't have anything like `struct` at all. Many languages like Python and JavaScript where "everything is an object" just have reference types. If you've come to Swift from a language like that, the concept might be even more foreign to you.

But wait! There's one area where almost every language uses value types: numbers! The following behavior shouldn't surprise any programmer with more than a few weeks of experience, regardless of the language:

```
    var x = 42
    var x2 = x
    x++
    print("x=\(x) x2=\(x2)")
    // prints: x=43 x2=42
```

This is so obvious and natural to us that we don't even realize that it acts differently, but it's right there in front of us. You've been working with value types for as long as you've been programming, even if you didn't realize it.

Lots of languages actually implement numbers as reference types, because they're hard-core on the "everything is an object" philosophy. However, they're _immutable_ types, and the difference between a value type and an immutable reference type is hard to detect. They act like value types act, even if they might not be implemented that way.

This is a big part of understanding value and reference types. The distinction only matters, in terms of language semantics, when mutating data. If your data is immutable, then the value/reference distinction disappears, or at least turns into a mere question of performance rather than semantics.

This even shows up in Objective-C with [tagged pointers](https://www.mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html). An object stored within the pointer value, as happens with a tagged pointer, is a value type. Copying the storage copies the object. This difference isn't apparent, because the Objective-C libraries are careful to only put immutable types in tagged pointers. Some `NSNumber`s are reference types and some are value types but it doesn't make a difference.

**Making the Choice**  
Now that we know how value types work, how do you make the choice for your own data types?

The fundamental difference between the two is what happens when you use `=` on them. Value types get copied, and reference types just get another reference.

Thus the fundamental question to ask when deciding which one to use is: does it make sense to copy this type? Is copying an operation you want to make easy, and use often?

Let's look at some extreme, obvious examples first. Integers are obviously copyable. They should be value types. Network sockets can't be sensibly copied. They should be reference types. Points, as in x, y pairs, are copyable. They should be value types. A controller that represents a disk can't be sensibly copied. That should be a reference type.

Some types _can_ be copied but it may not be something you want to happen all the time. This suggests that they should be reference types. For example, a button on the screen can conceptually be copied. The copy will not be quite identical to the original. A click on the copy will not activate the original. The copy will not occupy the same location on the screen. If you pass the button around or put it into a new variable you'll probably want to refer to the original button, and you'd only want to make a copy when it's explicitly requested. That means that your button type should be a reference type.

View and window controllers are a similar example. They might be copyable, conceivably, but it's almost never what you'd want to do. They should be reference types.

What about model types? You might have a `User` type representing a user on your system, or a `Crime` type representing an action taken by a `User`. These are pretty copyable, so they should probably be value types. However, you probably want updates to a `User`'s `Crime` made in one place in your program to be visible to other parts of the program. This suggests that your `User`s should be managed by some sort of user controller which would be a reference type.

Collections are an interesting case. These include things like arrays and dictionaries, as well as strings. Are they copyable? Obviously. Is copying something you want to happen easily and often? That's less clear.

Most languages say "no" to this and make their collections reference types. This is true in Objective-C and Java and Python and JavaScript and almost every other language I can think of. (One major exception is C++ with STL collection types, but C++ is the raving lunatic of the language world which does everything strangely.)

Swift said "yes," which means that types like `Array` and `Dictionary` and `String` are `struct`s rather than `class`es. They get copied on assignment, and on passing them as parameters. This is an entirely sensible choice as long as the copy is cheap, which Swift tries very hard to accomplish.

**Nesting Types**  
There are four possibile combinations when nesting value and reference types. Life gets interesting with just one of them.

If you have a reference type which contains another reference type, nothing much interesting happens. Anything which has a reference to either the inner or outer value can manipulate it, as usual. Everyone will see any changes made.

If you have a value type which contains another value type, this effectively just makes the value bigger. The inner value is part of the outer value. If you put the outer value into some new storage, it all gets copied, including the inner value. If you put the inner value into some new storage, it gets copied.

A reference type which contains a value type effectively makes the referenced value bigger. Anyone with a reference to the outer value can manipulate the whole thing, included the nested value. Changes to the nested value are visible to everyone with a reference to the outer value. If you put the inner value into some new storage, it gets copied there.

A value type which contains a reference type is not so simple. You can effectively break value semantics without being obvious that you're doing it. This can be good or bad, depending on how you do it. When you put a reference type inside a value type, then the outer value is copied when you place it into new storage, but the copy has a reference _to the same nested object as the original_. Here's an example:

```
    class Inner {
        var value = 42
    }

    struct Outer {
        var value = 42
        var inner = Inner()
    }

    var outer = Outer()
    var outer2 = outer
    outer.value = 43
    outer.inner.value = 43
    print("outer2.value=\(outer2.value) outer2.inner.value=\(outer2.inner.value)")
```

This prints:

```
    outer2.value=42 outer2.inner.value=43
```

While `outer2` gets a copy of `value`, it only copies the _reference_ to `inner`, and so the two `struct`s end up sharing the same instance of `Inner`. Thus an update to `outer.inner.value` affects `outer2.inner.value`. Yikes!

This behavior can be really handy. When used with care, it allows you to create `struct`s which perform a copy on write, to allow efficient implementations of value semantics that don't copy a ton of data everywhere. This is how Swift's collections work, and you can build your own as well. For more information on how to do that, see [Let's Build Swift.Array](https://www.mikeash.com/pyblog/friday-qa-2015-04-17-lets-build-swiftarray.html).

It can also be extremely dangerous. For example, let's say you're making a Person type. It's a model type that's sensibly copyable, so it can be a `struct`. In a fit of nostalgia, you decide to use `NSString` for the Person's name:

```
    struct Person {
        var name: NSString
    }
```

Then you build up a couple of Persons, constructing the name from parts:

```
    let name = NSMutableString()
    name.appendString("Bob")
    name.appendString(" ")
    name.appendString("Josephsonson")
    let bob = Person(name: name)

    name.appendString(", Jr.")
    let bobjr = Person(name: name)
```

Print them out:

```
    print(bob.name)
    print(bobjr.name)
```

This produces:

```
    Bob Josephsonson, Jr.
    Bob Josephsonson, Jr.
```

Eek!

What happened? Unlike Swift's `String` type, `NSString` is a reference type. It's immutable, but it has a mutable subtype, `NSMutableString`. When `bob` was created, it created a reference to the string held in `name`. When that string was subsequently mutated, the mutation was visible through `bob`. Note that this effectively mutates `bob` even though it's a value type stored in a `let` binding. It's not _really_ mutating `bob`, merely mutating a value that `bob` holds a reference to, but since that value is part of `bob`'s data, in a semantic sense, it _looks_ like a mutation of `bob`.

This sort of thing happens in Objective-C _all the time_. Every Objective-C programmer with some experience gets in the habit of sprinkling defensive copies all over the place. Since an `NSString` might actually be an `NSMutableString`, you define properties as `copy`, or write explicit `copy` calls in your initializers, to avoid a catastrophe. The same goes for the various Cocoa collections.

In Swift, the solution here is simpler: use value types rather than reference types. In this case, make `name` be a `String`. There is then no worry about inadvertently sharing references.

In other cases, the solution may be less simple. For example, you may create a `struct` containing a view, which is a reference type, and can't be changed to a value type. This is _probably_ a good indication that your type shouldn't be a `struct`, since you can't make it maintain value semantics anyway.

**Conclusion**  
Value types are copied whenever you move them around, whereas reference types just get new references to the same underlying object. That means that mutations to reference types are visible to everything that has a reference, whereas mutations to value types only affect the storage you're mutating. When choosing which kind of type to make, consider how suitable your type is for copying, and lean towards a value type for types that are inherently copyable. Finally, beware of embedding reference types in value types, as terrible things can happen if you're not careful.

That wraps things up for today, for real this time. Come back next time for more fun. Friday Q&A is driven by reader suggestions, so if you have an idea for a topic you'd like to see covered, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
