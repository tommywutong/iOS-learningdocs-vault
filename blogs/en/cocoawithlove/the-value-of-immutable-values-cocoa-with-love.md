---
title: 'The value of immutable values | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/04/value-of-immutable-values.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:d325b0312ce73812'
translated: false
---

> 原文：[The value of immutable values | Cocoa with Love](https://www.cocoawithlove.com/2008/04/value-of-immutable-values.html)　·　Cocoa with Love (Matt Gallagher)

This is an explanation of why Cocoa contains immutable value classes and why the value classes you create in your own program should be immutable too..

## Mea culpa

In 2002, I wrote the BigFloat class that would end up being the floating-point number class in my calculator, Magic Number Machine.

When I wrote this class, I was new to Cocoa programming and didn't really understand some of its design philosophies. Specifically, I didn't understand why Cocoa chooses to store its values in immutable classes.

Without this understanding as I wrote the BigFloat class, I designed the operator methods (add:, subtract:, multiplyBy:, divideBy:) to store their result in the receiving object, thereby changing or "mutating" the receiving object.

For example, in Magic Number Machine's BigFloat class, [a add:b] adds "b" to "a" and stores the result in "a".

Storing the result in the same location as one of the operands is common in assembly language and lots of classes have methods that change the underlying object. But this is the wrong approach for an Objective-C value class.

So let's look at why value objects in Cocoa should be immutable where possible.

## Immutable objects in Cocoa

It may be useful to clarify what is meant by "immutable":

> In object-oriented and functional programming, an immutable object is an object whose state cannot be modified after it is created. This is in contrast to a mutable object, which can be modified after it is created.
> 
> From [http://en.wikipedia.org/wiki/Immutable_object](http://en.wikipedia.org/wiki/Immutable_object)

It may sound like immutable classes are worse than mutable classes since they contain less functionality. It may then be surprising how many Cocoa classes are immutable. Immutable classes in Cocoa include:

- NSValue
- NSNumber
- NSURL
- NSDate
- NSString
- NSArray
- NSColor
- NSEvent
- NSFont

The reality is that these classes don't necessarily do _less_ than their mutable equivalent but they do always return changes in a newly allocated object instead of changing themselves.

A further trait in common is that all of these classes can be considered "value" classes. They store an indivisible piece of data which is intended to be read and used in its entirety.

## The problem with mutable value objects

### Objective-C shared references

In Objective-C, it is common to retain objects returned from other classes. "Get" accessor methods often return objects owned by another object that you are free to retain as though it is your own.

The result is that multiple parent objects often maintain references to the same child object. Even if you're using Garbage Collection and you don't explicitly type "retain", it doesn't matter, the effect is the same: multiple objects have a pointer to the same object.

This leads to the biggest problem with mutable values: if one of the sharing objects changes the value object, then both sharing objects see a changed value. This is fine if the value object is supposed to be a shared state object between the sharing objects but is very bad in all other cases.

To prevent external objects changing your internal state without permission, all internal state should be returned immutable. If no immutable class exists, you will need to copy the internal object first and return the copy.

### Threading concerns

Multiple objects sharing references to the same data can also create race conditions in threaded code.

Immutable objects largely avoid race conditions because one value can be swapped for another atomically.

### Consecutive Use

Another problem with mutable values, is that the original value is lost if you don't make a copy before applying an operator.

This causes problems depending on usage pattern. If value objects are ever used in a situation where more than one operator needs to be applied to the original object you must remember to copy the original object before applying an operator.

For example, if you have value X, it is common to want to calculate X + Y and X + Z. In a mutable object world, if calculating X + Y destroys X, then you must pre-copy X so that it still exists when you want to calculate X + Z.

### Aesthetic reasons

A final reason to make your value classes immutable is aesthetic.

When writing a description of an operation using mathematical syntax, we write:

```objc
result = function(operand1, operand2)
```

or

```objc
result = operand1 operator operand2 
```

In both cases, the mathematical notation is modelling a case where "operand1" and "operand2" are immutable and a new value "result" is created. To closely reflect this model, "function" and "operator" must act on the operands in an immutable fashion.

## When to avoid immutable objects

Any of the following traits can rule out the use of immutable design:

- Very large data size - since any change to an immutable object requires copying
- Lazily or progressively constructed data - since immutable objects require all data at construction
- Classes containing structured data, especially where child elements of the structure are exchanged or manipulated
- Where a class is intended as a container for shared state

This normally rules out most classes which can't be described as values. For example, you'll never see an immutable application control, view or document state class, like Windows or Views or Documents.

Compound objects like collections (NSArray, NSSet, NSDictionary, etc) regularly exist in both mutable and immutable forms. They are normally mutable when they are progressively constructed, contain large data sets or are used for maintaining shared structural state. But they are often immutable to take advantage of immutable traits (read-only internal access and thread-safe).

Some value objects with large data or structural values (large blocks of text for example) can create gray area where the choice can be hard to make. In the case of text, Cocoa includes the immutable NSString and NSAttributedString as well as the mutable NSMutableString and NSTextStorage to cover different sizes and usage patterns for text.

## Conclusion

As a word, "immutable" may sound like it is removing potential functionality from a class. In reality, using it where appropriate can make your interfaces between classes cleaner and easier to control. It also allows you to create code which closely reflects the aspects of values.

I have spent most of this post talking about immutable "value" classes. This is because classes which model entities that can be described as "values" are the canonical case for immutable classes.

Values are a good match for "immutable" design because an operator which acts on a value usually creates a completely new value. Values are also typically small objects (a few bytes to a few kilobytes).

Magic Number Machine's BigFloat class is still mutable since I never took the time to rewrite it. It didn't prevent the program working, it just required lots of careful copying and careful passing between classes. It also made the code for invoking operators less aesthetically pleasing.
