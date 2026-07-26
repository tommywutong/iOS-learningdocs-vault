---
title: 'In defense of Objective-C 2.0 Properties | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/08/in-defense-of-objective-c-20-properties.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:90f495d07d4fc709'
translated: false
---

> 原文：[In defense of Objective-C 2.0 Properties | Cocoa with Love](https://www.cocoawithlove.com/2008/08/in-defense-of-objective-c-20-properties.html)　·　Cocoa with Love (Matt Gallagher)

Of all the new features in Objective-C 2.0, none were as controversial as declared properties. Judging from the attacks, much of the controversy stems from a misunderstanding about the role that properties occupy in a class. In this post, I'll explain why properties are useful in Objective-C — and it isn't auto-generated getters and setters or the dot syntax.

## Confusion, controversy and hate

My esteemed colleagues in the world of Objective-C blogging are not universally friendly towards Objective-C 2.0's Properties. In case you've missed the vitriol, let me draw your attention to:

- Cocoa Is My Girlfriend — A case against dot syntax
- Stuff on fire — Does Objective-C Really Need Properties?
- Cocoadev — Are Objective-C 2.0 Properties Ugly?
- Bitquabit — Objective-C 2.0: the Bad, the Horrible, and the Ugly

I love a good drama. And next season, I hear that the show's writers are really going to knock it up another notch.

## Not the purpose

The syntax used for accessing properties is the direct target of most hatred. Detractors claim that the syntax is a pointless, foreign addition and that existing method syntax could be used instead. I think such complainants misunderstand the purpose of properties which leads to misunderstanding the purpose of the dot syntax.

So let's start by clarifying the purpose of properties. Let me state very clearly:

1. to provide auto-generated getter and setter methods.
2. to replace method syntax with dot syntax.
3. to make attributes public in a different way.

Obviously, these things can occur through properties but if they do, then they are an artefact or convenience offered by the implementation while working towards the real purpose.

As support for these statements, let me point out:

1. Auto-generated methods are a convenience permitted because properties clearly declare how they are accessed. But they are a convenience, not a rationale. Many properties do not use the @synthesize feature.
2. Properties and methods are distinct concepts and should never be used with the other's syntax. Syntax interchange is possible as an artefact of Objective-C's implementation of properties, not an invitation to exploit confusion.
3. Properties do not require an ivar of the same name. They may use a different ivar or store the data in a completely different form. Properties and attributes are not directly related.

## The purpose

> A clean, abstracted way to expose state values of an object.
> 
> Properties are one of two metaphors exposed by an object, the other being Methods (which are "a clean, abstracted way to perform an action").

Attributes (ivars) do not occupt the same role as properties (even when public) because they are not abstracted. You cannot override an attribute. You cannot change how an attribute is stored and maintain interface compatibility.

Methods can perform the same work as a property (to fetch state or to set state) but they do so by contract not by design.

Prior to the introduction of properties, methods were required to perform the work of a property. To enable this, documentation had to explain that the method existed to access state, not perform an action. The same documentation also became filled with getter methods referring to their corresponding setter methods. Setter methods pointing out the appropriate getter methods.

Prior to properties, get and set access to state-like values existed but only because code in multiple places was loosely coupled to present a concept unsupported by the underlying language. Properties declare the existence of state values clearly and eliminate the separation between getter and setter methods.

## New syntax is foreign but it needs to be new

The key complaint about the dot syntax is that the syntax looks foreign compared to Objective-C's message send syntax. Why use a new syntax at all? Why not simply invoke the underlying getter or setter methods directly?

Because properties are a different metaphor and imply different behavior and expectations than a method invocation.

Also, dot syntax allows the same syntax to be used for both get and set, keeping these two concepts properly tied together. Further, it keeps state access separate from performing actions.

That getter and setter methods are used to implement a property should be viewed as an implementation detail, not really part of the interface. To maintain abstraction, you should never directly invoke the methods of a property.

## Abstraction overload

It is true that properties represent a new abstraction concept in Objective-C and there are some people who view more abstractions as bad as they lead to [leaky abstractions](http://en.wikipedia.org/wiki/Leaky_abstraction). This is a fair complaint: don't use a new abstraction unless you are comfortable with it and you feel your code needs it. Do not use properties just because they are there.

Use properties if you want to separate state and action, gaining the advantage of implicitly conveyed meanings.

With respect to traditional accessor methods, properties imply "always accessible" (no special setup required). Properties imply "short and simple" (no complicated calculations). Reading from a property implies "nothing will change". Properties are independent of other each other in most cases.

With an accessor method, as opposed to a property, there is the implication of "invoker beware" — more powerful but requiring greater understanding to ensure that the method will succeed.
