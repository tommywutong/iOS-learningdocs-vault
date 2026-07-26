---
title: Faking Instance Variables in Objective-C Categories With Associative References
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/05/faking-ivars-in-objc-categories-with-associative-references/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:77d0eb63a6ed5e00'
translated: false
---

> 原文：[Faking Instance Variables in Objective-C Categories With Associative References](https://oleb.net/blog/2011/05/faking-ivars-in-objc-categories-with-associative-references/)　·　Ole Begemann

# Faking Instance Variables in Objective-C Categories With Associative References

In OS X 10.6 and iOS 3.1, Apple added [Associative References](http://developer.apple.com/library/ios/#documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocAssociativeReferences.html) to the Objective-C runtime. Essentially, this means that each and every object has an optional dictionary you can add arbitrary key/value pairs to.

This is a great feature, especially considering that Objective-C has forever had a feature to add _methods_ to existing classes: [categories](http://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocCategories.html#//apple_ref/doc/uid/TP30001163-CH20-SW1). Categories, however, do not permit you to add instance variables. Using associative references, it’s easy to fake ivars.

In the C API of the Objective-C runtime, you add a key/value pair to an object and read it again with these two functions:

```
void objc_setAssociatedObject(id object, const void *key, id value, objc_AssociationPolicy policy)
id objc_getAssociatedObject(id object, const void *key)
```

If we wrap these calls in a property’s custom getter and setter, we can make the implementation of our fake “ivar” totally opaque to the user of our API.

# Using objects to tag UIViews

As an example, say we want to add the ability to add an arbitrary object as a tag to a `UIView` (`UIView`’s existing `tag` property only takes integers, which can be limiting at times). The interface of our “object tag” category could look like this:

```
@interface UIView (ObjectTagAdditions)

@property (nonatomic, retain) id objectTag;

- (UIView *)viewWithObjectTag:(id)object;

@end
```

Using associative references, the implementation of the property is straightforward:

```
#import <objc/runtime.h>

static char const * const ObjectTagKey = "ObjectTag";

@implementation UIView (ObjectTagAdditions)
@dynamic objectTag;

- (id)objectTag {
    return objc_getAssociatedObject(self, ObjectTagKey);
}

- (void)setObjectTag:(id)newObjectTag {
    objc_setAssociatedObject(self, ObjectTagKey, newObjectTag, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
}

...
```

By specifying `OBJC_ASSOCIATION_RETAIN_NONATOMIC`, we tell the runtime to retain the value for us. Other possible values are `OBJC_ASSOCIATION_ASSIGN`, `OBJC_ASSOCIATION_COPY_NONATOMIC`, `OBJC_ASSOCIATION_RETAIN`, `OBJC_ASSOCIATION_COPY`, corresponding to the familiar property declaration attributes.

**Update December 22, 2011:** It’s important to note that the key for the association is a void pointer `void *key`, not a string. That means that when retrieving an associated reference, you have to pass the exact same pointer to the runtime. It would not work as intended if you used a C string as the key, then copied the string to another place in memory and tried to access the associated reference by passing the pointer to the copied string as a key.

Finally, here is the code for the recursive `-viewWithObjectTag:` method:

```
- (UIView *)viewWithObjectTag:(id)object {
    // Raise an exception if object is nil
    if (object == nil) {
        [NSException raise:NSInternalInconsistencyException format:@"Argument to -viewWithObjectTag: must not be nil"];
    }

    // Recursively search the view hierarchy for the specified objectTag
    if ([self.objectTag isEqual:object]) {
        return self;
    }
    for (UIView *subview in self.subviews) {
        UIView *resultView = [subview viewWithObjectTag:object];
        if (resultView != nil) {
            return resultView;
        }
    }
    return nil;
}
```

**Update May 16, 2011:** Vadim Shpakovski [asked on Twitter](https://twitter.com/vadimshpakovski/status/69894923800952832) why, when the argument to `viewWithObjectTag:` is `nil`, I chose to generate an exception over returning `nil` to the caller. The reason is that returning `nil` would be ambiguous since it means that no view with the specified `objectTag` could be found. Since `nil` is the default value of `objectTag`, this is highly unlikely.

A good alternative to raising an exception is to return the first view whose `objectTag` actually is `nil`, just like `viewWithTag:` does. I chose not to do that because I imagine it’s more likely that calling `-viewWithObjectTag:` with a `nil` argument is a programmer error than intended usage. It’s just a matter of preference, though.

---

**Update December 22, 2011:** Improved the declaration of the `ObjectTagKey` pointer and added a missing `#import` statement to the code sample.
