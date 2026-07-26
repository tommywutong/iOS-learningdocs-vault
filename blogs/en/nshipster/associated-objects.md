---
title: Associated Objects
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/associated-objects/'
original_language: en
published: 2014-02-10
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:038a0783667a83c7'
translated: false
---

> 原文：[Associated Objects](https://nshipster.com/associated-objects/)　·　NSHipster (Mattt)

# [Associated Objects](https://nshipster.com/associated-objects/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  February 10^th, 2014

```
#import <objc/runtime.h>
```

Objective-C developers are conditioned to be wary of whatever follows this ominous incantation. And for good reason: messing with the Objective-C runtime changes the very fabric of reality for all of the code that runs on it.

In the right hands, the functions of `<objc/runtime.h>` have the potential to add powerful new behavior to an application or framework, in ways that would otherwise not be possible. In the wrong hands, it drains the proverbial [sanity meter](https://en.wikipedia.org/wiki/Eternal_Darkness:_Sanity's_Requiem#Sanity_effects) of the code, and everything it may interact with (with [terrifying side-effects](https://www.youtube.com/watch?v=RSXcajQnasc#t=0m30s)).

Therefore, it is with great trepidation that we consider this [Faustian bargain](https://en.wikipedia.org/wiki/Deal_with_the_Devil), and look at one of the subjects most-often requested by NSHipster readers: associated objects.

---

Associated Objects—or Associative References, as they were originally known—are a feature of the Objective-C 2.0 runtime, introduced in OS X Snow Leopard (available in iOS 4). The term refers to the following three C functions declared in `<objc/runtime.h>`, which allow objects to associate arbitrary values for keys at runtime:

- `objc_setAssociatedObject`
- `objc_getAssociatedObject`
- `objc_removeAssociatedObjects`

Why is this useful? It allows developers to **add custom properties to existing classes in categories**, which [is an otherwise notable shortcoming for Objective-C](https://developer.apple.com/library/ios/documentation/cocoa/conceptual/ProgrammingWithObjectiveC/CustomizingExistingClasses/CustomizingExistingClasses.html).

```
@interface NSObject (AssociatedObject)
@property (nonatomic, strong) id associatedObject;
@end

@implementation NSObject (AssociatedObject)
@dynamic associatedObject;

- (void)setAssociatedObject:(id)object {
     objc_setAssociatedObject(self, @selector(associatedObject), object, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
}

- (id)associatedObject {
    return objc_getAssociatedObject(self, @selector(associatedObject));
}
```

It is often recommended that they key be a `static char`—or better yet, the pointer to one. Basically, an arbitrary value that is guaranteed to be constant, unique, and scoped for use within getters and setters:

```
static char kAssociatedObjectKey;

objc_getAssociatedObject(self, &kAssociatedObjectKey);
```

However, a much simpler solution exists: just use a selector.

> Since `SEL`s are guaranteed to be unique and constant, you can use `_cmd` as the key for `objc_setAssociatedObject()`. [#objective](https://twitter.com/search?q=%23objective&src=hash)-c [#snowleopard](https://twitter.com/search?q=%23snowleopard&src=hash)
> 
> — Bill Bumgarner (@bbum) [August 28, 2009](https://twitter.com/bbum/statuses/3609098005)

## Associative Object Behaviors

Values can be associated onto objects according to the behaviors defined by the enumerated type `objc_AssociationPolicy`:

| Behavior | `@property` Equivalent | Description |
|---|---|---|
| `OBJC_ASSOCIATION_ASSIGN` | `@property (assign)` or `@property (unsafe_unretained)` | Specifies a weak reference to the associated object. |
| `OBJC_ASSOCIATION_RETAIN_NONATOMIC` | `@property (nonatomic, strong)` | Specifies a strong reference to the associated object, and that the association is not made atomically. |
| `OBJC_ASSOCIATION_COPY_NONATOMIC` | `@property (nonatomic, copy)` | Specifies that the associated object is copied, and that the association is not made atomically. |
| `OBJC_ASSOCIATION_RETAIN` | `@property (atomic, strong)` | Specifies a strong reference to the associated object, and that the association is made atomically. |
| `OBJC_ASSOCIATION_COPY` | `@property (atomic, copy)` | Specifies that the associated object is copied, and that the association is made atomically. |

Weak associations to objects made with `OBJC_ASSOCIATION_ASSIGN` are not zero `weak` references, but rather follow a behavior similar to `unsafe_unretained`, which means that one should be cautious when accessing weakly associated objects within an implementation.

## Removing Values

One may be tempted to call `objc_removeAssociatedObjects()` at some point in their foray into associated objects. However, [as described in the documentation](https://developer.apple.com/library/mac/documentation/Cocoa/Reference/ObjCRuntimeRef/Reference/reference.html#//apple_ref/c/func/objc_removeAssociatedObjects), it’s unlikely that you would have an occasion to invoke it yourself:

> The main purpose of this function is to make it easy to return an object to a “pristine state”. You should not use this function for general removal of associations from objects, since it also removes associations that other clients may have added to the object. Typically you should use objc_setAssociatedObject with a nil value to clear an association.

## Patterns

### Adding private variables to facilitate implementation details

When extending the behavior of a built-in class, it may be necessary to keep track of additional state. This is the _textbook_ use case for associated objects.

### Adding public properties to configure category behavior.

Sometimes, it makes more sense to make category behavior more flexible with a property, than in a method parameter. In these situations, a public-facing property is an acceptable situation to use associated objects.

### Creating an associated observer for KVO

When using [KVO](https://nshipster.com/key-value-observing/) in a category implementation, it is recommended that a custom associated-object be used as an observer, rather than the object observing itself.

## Anti-Patterns

### Storing an associated object, when the value is not needed

A common pattern for views is to create a convenience method that populates fields and attributes based on a model object or compound value. If that value does not need to be recalled later, it is acceptable, and indeed preferable, not to associate with that object.

### Storing an associated object, when the value can be inferred

For example, one might be tempted to store a reference to a custom accessory view’s containing `UITableViewCell`, for use in `tableView:accessoryButtonTappedForRowWithIndexPath:`, when this can retrieved by calling `cellForRowAtIndexPath:`.

### Using associated objects instead of _X_

…where X is any one the following:

- [Subclassing](https://developer.apple.com/library/ios/documentation/cocoa/conceptual/ProgrammingWithObjectiveC/CustomizingExistingClasses/CustomizingExistingClasses.html) for when inheritance is a more reasonable fit than composition.
- [Target-Action](https://developer.apple.com/library/ios/documentation/general/conceptual/Devpedia-CocoaApp/TargetAction.html) for adding interaction events to responders.
- [Gesture Recognizers](https://developer.apple.com/library/ios/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/GestureRecognizer_basics/GestureRecognizer_basics.html) for any situations when target-action doesn’t suffice.
- [Delegation](https://developer.apple.com/library/ios/documentation/general/conceptual/DevPedia-CocoaCore/Delegation.html) when behavior can be delegated to another object.
- [NSNotification & NSNotificationCenter](https://nshipster.com/nsnotification-and-nsnotificationcenter/) for communicating events across a system in a loosely-coupled way.

---

Associated objects should be seen as a method of last resort, rather than a solution in search of a problem (and really, categories themselves really shouldn’t be at the top of the toolchain to begin with).

Like any clever trick, hack, or workaround, there is a natural tendency for one to actively seek out occasions to use it—especially just after learning about it. Do your best to understand and appreciate when it’s the right solution, and save yourself the embarrassment of being scornfully asked “why in the name of $DEITY” you decided to go with _that_ solution.
