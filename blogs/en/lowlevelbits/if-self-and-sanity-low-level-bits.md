---
title: '''if (self)'' and Sanity - Low Level Bits 🇺🇦'
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/if-self-and-sanity/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5bdcac939debd010'
translated: false
---

> 原文：['if (self)' and Sanity - Low Level Bits 🇺🇦](https://lowlevelbits.org/if-self-and-sanity/)　·　Low Level Bits (Alex Denisov)

# 'if (self)' and Sanity

_Published on May 05, 2015_

Imagine that there is a power in the universe that said to Apple: “Hey, convince developers to do a silly thing and you’ll get $1 for the every demonstration of silliness**”.

I believe it was a hard task, but Apple managed to find that thing:

```objective
self = [super init];
if (self) { // <- this is silly
}
return self;
```

**_Don’t want to offend you, I did this silly thing for years_

**TL;DR;**

Check the value of `self` in constructor only if you use ivars.

### Why?

[Documentation](https://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSObject_Class/index.html#//apple_ref/occ/instm/NSObject/init) of NSObject’s `-init` method says:

> Return Value

> An initialized object, or nil if an object could not be created for some reason that would not result in an exception.

Which is completely OK, but **why should we check if self is nil or not**?

To get the answer let’s take a look at a few possible variations of a constructor:

- `super.init` returns `nil`, programmer uses properties (send messages)

```objective
self = [super init];
self.foo = @"Foo";
return self;
```

- `super.init` returns `nil`, programmer uses ivars

```objective
self = [super init];
_foo = @"Foo";
return self;
```

_I skipped options when `super.init` returns a valid object, because they’re considered correct and valid in any situation_

#### Nil object and messaging

In a first case an assignment expression just converts into a function call:

```objective
// note: 'self' is nil
self.foo = @"Foo";
// converts into
objc_msgSend(self, @selector(setFoo:), @"Foo");
```

What happens when you send a message to a Nil object?

Well, nothing happens.

#### Nil object and pointers

The second constructor also has a different final form:

```objective
// note: 'self' is nil
_foo = @"Foo";
// actually means
self->_foo = @"Foo";
```

OK, another question: what happens when you dereference null pointer?

Behaviour in this case is undefined, but for iOS/OS X platforms it’s usually a crash.

### Conclusion

Based on the statements above we can conclude that we don’t need to check `self` in every constructor, but only when ivars are used.

As far as I see some developers do this check, but they don’t know why.

The reason, imho, is obvious: ObjC is an old language and tons of documentation/examples were written when properties were not introduced yet and programmers had to use ivars.

After doing this for a years it’s just turned into a habit.

Nowadays we have properties, that allow us to write clean and robust code, so let’s do it and, please, **check the value of `self` in constructor only if you use ivars.**

Happy and sane hacking!
