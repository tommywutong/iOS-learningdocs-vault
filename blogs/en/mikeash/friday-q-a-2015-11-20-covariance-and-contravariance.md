---
title: 'Friday Q&A 2015-11-20: Covariance and Contravariance'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-11-20-covariance-and-contravariance.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3934a849227484db'
translated: false
---

> 原文：[Friday Q&A 2015-11-20: Covariance and Contravariance](https://www.mikeash.com/pyblog/friday-qa-2015-11-20-covariance-and-contravariance.html)　·　mikeash.com Friday Q&A

Posted at 2015-11-20 14:16 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2015-12-11: Swift Weak References](https://www.mikeash.com/pyblog/friday-qa-2015-12-11-swift-weak-references.html)  
Previous article: [Friday Q&A 2015-11-06: Why is Swift's String API So Hard?](https://www.mikeash.com/pyblog/friday-qa-2015-11-06-why-is-swifts-string-api-so-hard.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [oop](https://www.mikeash.com/pyblog/?tag=oop) [theory](https://www.mikeash.com/pyblog/?tag=theory)

Friday Q&A 2015-11-20: Covariance and Contravariance

by [Mike Ash](https://www.mikeash.com/)

**Subtypes and Supertypes**  
We all know what subclassing is. When you create a subclass, you're creating a subtype. To take a classic example, you might subclass `Animal` to create `Cat`:

```
    class Animal {
        ...
    }

    class Cat: Animal {
        ...
    }
```

This makes `Cat` a subtype of `Animal`. That means that all `Cat`s are `Animal`s, but not all `Animal`s are `Cat`s.

Subtypes can typically substitute for supertypes. It's obvious to any programmer who's been around a little while why in this Swift code the first line works and the second line doesn't:

```
    let animal: Animal = Cat()
    let cat: Cat = Animal()
```

This is true for function types as well:

```
    func animalF() -> Animal {
        return Animal()
    }

    func catF() -> Cat {
        return Cat()
    }

    let returnsAnimal: () -> Animal = catF
    let returnsCat: () -> Cat = animalF
```

All of this works in Objective-C too, using blocks. The syntax is much uglier, though, so I decided to stick with Swift.

Note that this does not work:

```
    func catCatF(inCat: Cat) -> Cat {
        return inCat
    }

    let animalAnimal: Animal -> Animal = catCatF
```

Confused yet? Not to worry, this whole article is going to explore exactly why the first version works while the second version doesn't, and hit on some more practical stuff along the way.

**Overridden Methods**  
Similar things are at work with overridden methods. Imagine this class:

```
    class Person {
        func purchaseAnimal() -> Animal
    }
```

Now let's subclass it, override that method, and change the return type:

```
    class CrazyCatLady: Person {
        override func purchaseAnimal() -> Cat
    }
```

Is this legal? Yes. Why?

The [Liskov substitution principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle) is the guiding principle for subclassing. It says, in short, that an instance of a subclass can always be substituted for an instance of its superclass. Anywhere you have an `Animal`, you can replace it with a `Cat`. Anywhere you have a `Person`, you can replace it with a `CrazyCatLady`.

Here's some code that uses a `Person`, with explicit type annotations for clarity:

```
    let person: Person = getAPerson()
    let animal: Animal = person.purchaseAnimal()
    animal.pet()
```

Imagine that `getAPerson` returns a `CrazyCatLady`. Does this code still work? `CrazyCatLady.purchaseAnimal` will return a `Cat`. That instance is placed into `animal`. A `Cat` is a valid `Animal`, so it can do everything an `Animal` can do, including `pet`. Having `CrazyCatLady` return `Cat` is valid.

Let's imagine we want to move the `pet` operation into `Person`, so we can have a particular person pet a particular animal:

```
    class Person {
        func purchaseAnimal() -> Animal
        func pet(animal: Animal)
    }
```

Naturally, `CrazyCatLady` only pets cats:

```
    class CrazyCatLady: Person {
        override func purchaseAnimal() -> Cat
        override func pet(animal: Cat)
    }
```

Is this legal? _No!_

To understand why, let's look at some code that uses this method:

```
    let person: Person = getAPerson()
    let animal: Animal = getAnAnimal()
    person.pet(animal)
```

Imagine that `getAPerson()` returns a `CrazyCatLady`. This line is still good:

```
    let person: Person = getAPerson()
```

Imagine that getAnAnimal() returns a `Dog`, which is a subclass of `Animal` with decidedly different behaviors from `Cat`. This line is still good as well:

```
    let animal: Animal = getAnAnimal()
```

Now we have a `CrazyCatLady` in `person` and a `Dog` in `animal` and we do this:

```
    person.pet(animal)
```

Kaboom! `CrazyCatLady`'s `pet` method is expecting a `Cat`. It has no idea what to do with a `Dog`. It's probably going to be accessing properties and calling methods that `Dog` doesn't have.

This code is perfectly legal. It gets a `Person`, it gets an `Animal`, then it calls a method on `Person` that takes an `Animal`. The problem lies above, when we changed `CrazyCatLady.pet` to take a `Cat`. That broke the Liskov substitution principle: no longer can a `CrazyCatLady` be used anywhere a `Person` is used!

Thankfully, the compiler has our back. It knows that using a subtype for an overridden method's parameter is not legal, and will refuse to compile this code.

Is it ever legal to use a different type in an overridden method? Yes, actually: you can use a _supertype_. For example, imagine that `Animal` subclasses `Thing`. It would then be legal to override `pet` to take `Thing`:

```
    override func pet(thing: Thing)
```

This preserves substitutability. If treated as a `Person`, then this method will always be passed `Animal`s, which are `Thing`s.

This is a key rule: function return values can changed to _subtypes_, moving _down_ the hierarchy, whereas function parameters can be changed to _supertypes_, moving _up_ the hierarchy.

**Standalone Functions**  
The subtype/supertype relationship is obvious enough when it comes to classes. It directly follows the class hierarchy. What about functions?

```
    let f1: A -> B = ...
    let f2: C -> D = f1
```

When is this legal, and when is it not?

This is basically a miniature version of the Liskov substitution principle. In fact, you can think of functions as little mini-objects with just one method. When you have two different object types, when can you mix them like this? When the original type is a subtype of the destination. And when is a method a subtype of another method? As we saw above, it's when parameters are supertypes and the return value is a subtype.

Applied here, the above code works if `A` is a supertype of `C`, and if `B` is a subtype of `D`. Put concretely:

```
    let f1: Animal -> Animal = ...
    let f2: Cat -> Thing = f1
```

The two parts move in opposite directions. This may not be what you want, but it's the only way it can actually work.

This is another key rule: functions are subtypes of other functions if the parameter types are _supertypes_ and the return types are _subtypes_.

**Properties**  
Read-only properties are pretty simple. Subclass properties must be subtypes. A read-only property is essentially a function which takes no parameters and returns a value, and the same rules apply.

Read-write properties are also pretty simple. Subclass properties must be the exact same type as the superclass. A read-write property is essentially a pair of functions. The getter is a function with no parameters that returns a value, and the setter is a function with one parameter and no return value:

```
    var animal: Animal
    // This is like:
    func getAnimal() -> Animal
    func setAnimal(animal: Animal)
```

As we saw above, function parameters move up while function return types move down. Since both the parameter and the return value are forced to be the same type, that type can't change:

```
    // This doesn't work:
    override func getAnimal() -> Cat
    override func setAnimal(animal: Cat)

    // Neither does this:
    override func getAnimal() -> Thing
    override func setAnimal(animal: Thing)
```

**Generics**  
How about generics? Given some type with a generic parameter, when does this work?

```
    let var1: SomeType<A> = ...
    let var2: SomeType<B> = var1
```

In theory, it depends on how the generic parameter is used. A generic parameter does nothing on its own, but is used as property types, method parameter types, and method return types.

If the generic parameter was used purely for method return types and read-only properties, then it would work if `B` were a supertype of `A`:

```
    let var1: SomeType<Cat> = ...
    let var2: SomeType<Animal> = var1
```

If the generic parameter was used purely for method parameter types, then it would work if `B` were a subtype of `A`:

```
    let var1: SomeType<Animal> = ...
    let var2: SomeType<Cat> = var1
```

If the generic parameter was used both ways, then it would only work if `A` and `B` were identical. This is also the case if the generic parameter was used as the type for a read-write property.

That's the theory. It's a bit complex and subtle. That's probably why Swift takes the easy way out. For two generic types to be compatible in Swift, they must have identical generic parameters. Subtypes and supertypes are never allowed, even when the theory says it would be acceptable.

Objective-C actually does this a bit better. A generic parameter in Objective-C can be annotated with `__covariant` to indicate that subtypes are acceptable, and `__contravariant` to indicate that supertypes are acceptable. This can be seen in the interface for `NSArray`, among others:

```
    @interface NSArray<__covariant ObjectType> : NSObject ...
```

**Covariance and Contravariance**  
The astute reader may notice that the title of the article contains these two terms which I have carefully avoided using this whole time. Now that we're firm on the concepts, let's talk about the terminology.

_Covariance_ is when subtypes are accepted. Overridden read-only properties are covariant.

_Contravariance_ is when supertypes are accepted. The parameters of overridden methods are contravariant.

_Invariance_ is when neither supertypes nor subtypes are accepted. Swift generics are invariant.

_Bivariance_ is when both supertypes and subtypes are accpted. I can't think of any examples of bivariance in Objective-C or Swift.

You may find the terminology hard to remember. That's OK! It's not really that important. As long as you understand subtyping, supertyping, and what causes a subtype or supertype to be acceptable in any given place, you can just look up the terminology in the unlikely event that you need it.

**Conclusion**  
Covariance and contravariance determines when a subtype or supertype can be used in place of a type. It most commonly appears when overriding a method and changing the argument or return types, in which case the return type must be a subtype, and the arguments must be supertypes. The guiding principle behind this is Liskov substitution, which means that an instance of a subclass must be usable anywhere an instance of the superclass can be used. Subtype and supertype requirements can be derived from this principle.

That's it for today. Come back for more exciting adventures. Or just come back for exciting adventures; "more" is probably out of place, since covariance is not exciting. In any case, Friday Q&A is driven by reader suggestions, so if you have a suggestion for an article here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
