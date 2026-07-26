---
title: 'Objective-C 2.0: Fast enumeration clarifications | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/05/fast-enumeration-clarifications.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:512f5f074ad6b6f5'
translated: false
---

> 原文：[Objective-C 2.0: Fast enumeration clarifications | Cocoa with Love](https://www.cocoawithlove.com/2008/05/fast-enumeration-clarifications.html)　·　Cocoa with Love (Matt Gallagher)

Fast enumeration in Objective-C 2.0 is a doubly useful addition: it results in code that looks better and runs faster. Its documentation though, still contains a few points which are ambiguous or misleading. Here are some clarifications that I've uncovered.

## Things you should already know

In case you've never heard of it, fast enumeration is an addition in Objective-C 2.0 which allows you to turn an Objective-C 1.0 NSSet (or other collection) enumeration from:

```objc
NSSet *objectSet = &lt;#setaccess#&gt;;
NSEnumerator *enumerator = [objectSet objectEnumerator];
id setObject;
while ((setObject = [enumerator nextObject]) != nil)
{
    &lt;#!loopcontents#&gt;
}
```

to:

```objc
for (id setObject in &lt;#setaccess#&gt;)
{
    &lt;#!loopcontents#&gt;
}
```

Your code will also run faster because the internal implementation reduces message send overhead and increases pipelining potential.

The resulting syntax is more aesthetic and better reflects the programmer's intent. Faster and better looking, it's like a sports car for nerds (without the higher sticker price or jokes about mid-life crises).

## Documentation Clarifications

### How do you enumerate backwards? Or enumerate dictionary objects instead of keys?

Apple have noted throughout the Cocoa documentation that you can use Fast Enumeration instead of NSEnumerator in Mac OS X 10.5. In the documentation for -[NSArray reverseObjectEnumerator] they have stated: "On Mac OS X v10.5 and later, it is more efficient to use the fast enumeration protocol".

This statement may seem a little puzzling, since Fast Enumeration does not let you choose the enumeration direction. What Apple mean in this case though, is that you can use the reverse NSEnumerator object itself for Fast Enumeration. Just get the reverse object enumerator and pass it in as though it were the collection.

Like this:

```objc
for (id object in [someArray reverseObjectEnumerator])
```

The latest downloadable XCode Documentation Set still omits the fact that NSEnumerator actually implements NSFastEnumeration. The [documentation for NSEnumerator at developer.apple.com](http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Classes/NSEnumerator_Class/Reference/Reference.html) has finally fixed this omission and it is in the Mac OS X 10.5 header files, so the above code is actually valid syntax.

This will then work for any NSEnumerator returning method, including NSDictionary's objectEnumerator.

### Will the "collection" expression code be invoked each time?

In the above case, you may wonder if -[NSArray reverseObjectEnumerator] would be run on every iteration of the loop — potentially slowing down the code. Not very serious in this case but what if your code looked like this:

```objc
for (id object in [someObject generateArrayInTimeConsumingCode])
```

In a normal C for loop, you would expect the for expression to be evaluated on every iteration. The [Objective-C 2.0 Programming Language: Fast Enumeration](http://developer.apple.com/documentation/Cocoa/Conceptual/ObjectiveC/Articles/chapter_7_section_1.html) page implies that it would be evaluated on every invocation of countByEnumeratingWithState:objects:count: (every handful of iterations).

By using a test class that implements its own countByEnumeratingWithState:objects:count:, I was able to determine that _neither_ is the case. The "collection" expression is only evaluated once, when the for loop begins. This is the best case, since you can safely put an expensive function in the "collection" expression without impacting upon the per-iteration performance of the loop.

### Must the data returned be object pointers ("id"s)?

No. The compiler generates no code that reads from the data returned, so it doesn't care.

Even though the pointer to enumeration data is declared as:

```objc
id *itemsPtr;
```

you can return an array of any data you want, provided it is contained in a pointer-sized array. For example, pointers to structs is okay, as are char values (provided they are spaced sizeof(id) apart).

### What happens to Fast Enumeration code in 10.4?

The documentation clearly states that Fast Enumeration will not work in Mac OS X 10.4 and the compiler will give you warnings if you try to compile it.

But that's not completely true.

If you compile against the Mac OS X 10.5 SDK libraries but set your minimum required OS to Mac OS X 10.4, you will get warnings that "for...in" constructs aren't supported. Within certain bounds though, you can ignore these warnings.

For Fast Enumeration of your own classes, "for...in" constructs will work under 10.4 without modification.

Two potentially serious issues exist with attempting to run Fast Enumeration code under 10.4:

- countByEnumeratingWithState:objects:count:

  methods of your own design into them at runtime when running under Mac OS X 10.4.
- objc_enumerationMutation

  function doesn't exist under 10.4, so if you mutate a collection while iterating, you won't throw an exception, you'll crash.

Obviously, you shouldn't do it unless you have a strong compelling case but the option is there if you're prepared to shoulder the extra effort.
