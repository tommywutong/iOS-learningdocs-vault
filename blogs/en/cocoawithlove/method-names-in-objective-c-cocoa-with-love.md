---
title: 'Method names in Objective-C | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/06/method-names-in-objective-c.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:fcc676132c117f72'
translated: false
---

> 原文：[Method names in Objective-C | Cocoa with Love](https://www.cocoawithlove.com/2009/06/method-names-in-objective-c.html)　·　Cocoa with Love (Matt Gallagher)

Compared to other languages, method names in Objective-C are weird. They're long, they're wordy, they include names for the parameters and they seem to repeat information you can get elsewhere. Despite these apparent negatives, Objective-C method naming can save you time and effort. I'll show you how methods are named so that you can predict them without documentation and understand how methods work and how they use their parameters from their names alone.

## Introduction: Objective-C is an ugly duckling

Along with square-brackets and its largely Apple-exclusive nature, method names are one of the most commonly decried parts of Objective-C. I've seen them criticized for being:

- Long and wordy
- Repetitious or redundant
- Filled with names for each parameter
- Camel-case

While every one of these points is true, none of them is really a negative — although camel-case is a subjective, aesthetic point and I'll ignore it since I'll only consider the _structural_ aspects of method naming conventions in this post.

Objective-C methods names are some of the most predictable, regular, self-descriptive methods in any C-derivative language — and it is these points that allow it to be so. Of course, these benefits are lost unless you know the conventions well enough to understand and predict them.

## Background: naming conventions in other C-like languages

To help you understand the reasoning behind Objective-C's method names, I'll start by describing how methods and functions are named in C. I'm starting with C because Objective-C's method naming is, in some respects, an extension of C's naming style, adapted to overcome the limitations.

### Standard C's naming style

Yes, Standard C does have some implicit naming conventions. Many standard C functions are composed of three parts:

1. An indication of the data type acted upon
2. The action
3. A description of the secondary object

We can see examples of these in these functions:

- - "s" (acts upon a

  ), "scan" (extract character data from the string), "f" (format string is the secondary object)
- - "f" (acts upon a

  ), "print" (outputs character data to the file), "f" (format string is the secondary object)
- - "str" (acts upon a

  ), "len" (compute the length). No secondary object.
- - "fe" (acts upon the "floating point environment"), "set" (changes a state value), "round" (a new rounding value is the secondary object).

### Standard C's naming style fails

For these methods, this style works well. The problem is that components are so short (often single letters) that it is difficult to know for certain to what they refer. Many of the methods in math.h show these limitations:

- - "l" (no longer an "acts upon", this first part now indicates "returns a

  "), "round" (round to the nearest integer). No description of the primary parameter — you are expected to assume a

  .
- - The "l" in this case is the primary parameter and means

  whereas it meant

  in the

  method above. The "a" here is not a prefix, it is part of the action component.

This is where naming styles in C break down — while math.h does have naming conventions, they are all its own. You can learn the tricks of math.h but they are unique to that library, not a standard that applies to all functions.

Beyond these issues C, suffers from a broader lack of adherence to _any_ convention, let alone a consistent one. Most functions are really just a 4 to 6 character description of the action performed. While this may be all that is required at a technical level, it makes it almost impossible to know how to use functions like `system`, `raise`, `atexit` or even `malloc` for the first time without reading the documentation.

### Other languages

Few other languages have a distinct approach to method structure. The overriding convention in the main languages I use (C++, C#, Java) is simply a short verb plus possible modifier.

Some languages do have their own aesthetics (for example, the C++ Standard Library uses terse underscore delimited words) but this doesn't represent a structural convention.

The reason why these languages have abandoned the three part style of Standard C functions is that:

1. The data type acted upon is now the object upon which the method is invoked, removing the need to explain this part.
2. Parameter overloading means that a description of any parameter needs to be vague (since the parameter itself may be used inconsistently).

So methods end up being little more than a verb plus an optional modifier term.

The result is that methods with subtle actions or that use their parameters in specific ways can only be used by thoroughly examining the documentation.

## Method naming conventions in Objective-C

Objective-C aims to be substantially more self-documenting than its peers. The intent is that all methods in all classes should be able to follow the same set of rules so that subtleties of behavior are easy to see and understand — even when you are new to the class.

This aim combines with the named parameters in Objective-C to produce methods which are quite distinct compared to other languages.

Given the lack of convention in other languages and the unusual nature of Objective-C's named parameters, it's no so surprising that method names in Objective-C are confronting to new Objective-C programmers.

### Structure of an Objective-C method name

Objective-C methods are composed of a few different components. I'll list the components here, examples follow:

1. If there is a return value, the method should begin with the property name of the return value (for accessor methods), or the class of the return value (for factory methods).
2. A verb describing either an action that changes the state of the receiver or a secondary action the receiver may take. Methods that don't result in a change of state to the receiver often omit this part.
3. A noun if the first verb acts on a direct object (for example a property of the receiver) and that property is not explicit in the name of the first parameter.
4. If the primary parameter is an indirect object to the main verb of the method, then a preposition (i.e. "by", "with", "from") is used. This preposition partly serves to indicate the manner in which the parameter is used but mostly serves to make the sentence more legible.
5. If a preposition was used and the first verb doesn't apply to the primary parameter or isn't present then another verb describing direct action involving the primary parameter may be used.
6. A noun description (often a class or class-like noun) of the primary parameter, if this is not explicit in one of the verbs.
7. Subsequent parameter names are noun descriptions of those parameters. Prepositions, conjunctions or secondary verbs may precede the name of a subsequent parameter but only where the subsequent parameter is of critical importance to the method. These extra terms are a way to highlight importance of secondary parameters. In some rarer cases secondary parameter names may be a preposition without a noun to indicate a source or destination.

In addition, an Objective-C method should be maximally readable — its reading should flow like a sentence and abbreviations should be avoided except where they are universally known (and even then, abbreviations to syllables rather than single letters are preferred).

That's a lot to consider. Fortunately, most components are only relevant to specific kinds of method.

### Applying the naming convention to property accessors

```objc
length
```

This method is shows the typical form of a getter method for a property or calculated value. Only the first component of the method name applies.

The biggest point to note with respect to other languages is that getter methods don't use the verb "get" because no explicit action or state change is required to extract this property (implicit actions or actions taken for internal reasons should not be communicated through the method name).

```objc
encodedLength
```

This method shows a variant length method where a modifier is used to describe the length. We put the modifier before the property name because a structure like `lengthWhenEncoded` gets too close to `lengthForEncoding:` which would be used if the encoding was passed in as a parameter.

```objc
sharedApplication
```

Singleton accessors (like this accessor for the global `UIApplication` object) and other global data accessors take exactly the form as instance accessors. A description of the return value ("Application" in this case) plus an adjective to disambiguate it (in this case, disambiguation is required because a class name on its own is expected to be a factory method — see below). The term "shared" is used by convention to identify singletons.

```objc
doubleValue
```

This method has the same structure as the previous method but shows how the returned class is sometimes the modifier when used in conjunction with an abstract property like "value".

```objc
isEditable
```

This method is actually an exception to the conventional rules. The verb "is" shouldn't be there — verbs are normally reserved for describing state change or secondary action.

I guess that this style for accessors that return a `BOOL` developed to make the method read more like a sentence. You could also argue that "is" is a passive verb so it isn't indicating an action.

```objc
setLength:
```

The setter method is not composed in the same way as the getter. With no return value, the first part is a verb describing the action: "set".

The second part, "Length" may be considered to the direct object of the verb component (i.e. the internal property). In this case, it is also the name of the first parameter. Since they communicate the same information, only one is used.

Setter methods with prepositions before the first parameter like `setValueUsingDouble:` and `setValueUsingNumber:` are rarely used, even though they may seem like a good way to unambiguously set a property like "value" using different data types. Instead, the property itself is normally give a different name (i.e. `setDoubleValue:` or `setNumberValue:`). In this way, there is only ever one setter for a given property (although properties may contain dependencies).

### Applying the naming convention to factory methods

```objc
string
```

This `NSString` method returns an empty string. It takes exactly the same format as a getter method, except that you invoke it on a class object, not an instance and it doesn't include a property name.

It may seem like this method is providing redundant information — we already know that a factory method for a class will return an instance of the same class — but identifying the return type here has two purposes:

- factory method are identified precisely because they start with the class' name
- it maintains consistency (always describe the return value when it is the purpose of the method)

A quick follow up to that second point though: the return value only needs to be described when it is the purpose of the method. `BOOL` values returned as an error indicator and other cases where the return value is a secondary effect (like `autorelease` which returns the receiver) do not need to describe the return value.

```objc
stringWithString:
```

The parameter here is named "String", indicating that it is an instance of `NSString` with no other constraints. The correct way to read this method is that it creates a new string in the simplest way possible from its string parameter — i.e. a copy of the string.

The preposition here is of little semantic purpose except to make the method name read like a sentence. The choice of preposition is simply: whatever is most appropriate if you read it like a sentence. For this reason class factory methods normally use "With" but instance factory methods normally use "By" because it implies some involvement of the receivers data (like `stringByAppendingString:`).

The `NSArray` method `isEqualToArray` shows a state interrogation with a preposition but again, the preposition is chosen simply to make the method name read like a sentence.

### Applying the naming convention to action methods

```objc
release
```

This is an example of a simple action method: a verb describing how the method changes state or performs secondary actions.

```objc
addObject:
```

Again, a very simple method: verb plus a noun describing the first parameter (any "Object").

```objc
addObserver:forKeyPath:options:context:
```

The important addition to see here is the use of the preposition "for" in front of the second parameter. Yes, "KeyPath" is the indirect object of the method's verb "add" but the real purpose here is to highlight the importance of this parameter — pointing out that this parameter is more important than parameters which follow.

To explain this, consider that the method is not `addObject:forKeyPath:usingOptions:andContext:` — the options and context are really peripheral parameters whereas keyPath is an important consideration, despite being the second parameter.

This method can be compared to the very similar `NSNotificationCenter` method `addObserver:selector:name:object:`. In the case of the `NSNotificationCenter` method, `name:` is the corresponding parameter to `forKeyPath:` and yet no preposition is used (it is not `forName:`). This reflects the fact that the name parameter is optional (can be `nil`).

However you should not infer that lack of preposition means "optional" — far from it. Instead, the correct meaning is preposition means more important than other secondary parameters. The `selector:` parameter of the `addObserver:selector:name:object:` method is mandatory but is given no special status in the method. It is necessary for routing the notification but much of the time will simply reflect the notifications it observes (i.e. `@selector(windowWillCloseNotification:)`).

### A small exception: delegate methods

```objc
windowDidChangeScreen:
```

This method begins with the name of a class but it is not a factory method nor a method which returns a mutated version of the receiver. It is actually a delegate method and delegate methods don't really follow any of the conventions.

If it were following the conventional standard its name would be `receiveWindowDidChangeScreenNotification:`. You could argue that delegate methods are passive — the delegate isn't being asked to perform an action, it is being told that something else performed an action — so omitting a verb is permissible. For my part, the break with convention makes me sad inside.

Further confusing things, the first parameter of the delegate method is rarely identified by the closest noun. Instead the first parameter is either the object sending the notification or it is a notification object (which will contain the sender). In the example above, the closest noun is "screen" but the first parameter is an `NSNotification`. In the case of `applicationOpenUntitledFile:` the closest noun is "File" but the parameter is the `NSApplication` object that sent the message.

## Summary

In describing method formats, I've repeated myself quite a few times. The reality is that Objective-C uses one method naming convention almost everywhere.

Objective-C method names are very regular. So regular that you should be able to predict the names for methods without checking the documentation — start typing the method name as you guess it, then autocomplete. More than simply predicting the name, you can normally predict how parameters are used, so again you avoid documentation and know what you need.

Looking at the criticisms levelled at Objective-C method names that I listed at the start:

### Long and wordy

Yes, Objective-C methods are made to read like sentences. They contain prepositions (something almost never seen in other languages), they contain type of the return parameter, they use full words instead of abbreviations.

The purpose is to make the method as quick to read as possible.

This is a good trade to make since you will read a method many times but only type it once (with code completion, less than once).

### Repetitious or redundant

While methods like `+[UIApplication sharedApplication]` may seem redundant, the reality is that `+[UIApplication shared]` would have a different meaning (it would be an accessor for the static class property named "shared") and `+[UIApplication singleton]` by omitting a class name fails to communicate that the method also works as a factory method on the first invocation — repeating the class name has meaning, it is not redundant.

### Filled with names for each parameter

Yes they are but these names makes it much easier to determine what each parameter is and allows metadata like importance to be conveyed.

### Camel-case

Yes. The choice over underscore delimited words is largely aesthetic. Although the choice over Pascal-case (same as camel-case but where the first letter of the first word is uppercase not lowercase) is because uppercase initial letters are reserved for names with global scope — like class names, function names and global constants.

## Conclusion

Few other languages have conventions that are as rigourously applied as those in Objective-C. Conventions are annoying to learn — as they may seem arbitrary and unnecessary at first glance — but once learned, they are regular and predictable with few surprises. When trying to get the computer to obey, that's good.

Further reading:

- Naming conventions in the Objective C 2.0 Language Summary
- Coding Guidelines for Cocoa: Naming Methods
