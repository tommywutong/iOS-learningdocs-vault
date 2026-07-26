---
title: 'Objective-C Internals: Associated References A comparison of Apple’s Associated References implementation and one I wrote for historical context, with additional notes about use with tagged pointer ob'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/06/05/objc-assoc-obj'
original_language: en
published: 2023-06-05
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:fc6148cbab36b6ce'
translated: false
---

> 原文：[Objective-C Internals: Associated References A comparison of Apple’s Associated References implementation and one I wrote for historical context, with additional notes about use with tagged pointer ob](https://alwaysprocessing.blog/2023/06/05/objc-assoc-obj)　·　Always Processing (Brian T. Kelley)

# Objective-C Internals: Associated References

![Two children, each at a computer workstation, creating associations between objects on the screen.](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/ae4bf923-51a5-438e-60a7-ecd731bb7f00/public)

A comparison of Apple’s _Associated References_ implementation and one I wrote for historical context, with additional notes about use with tagged pointer objects and what the `assign` association policy actually does.

I remember eagerly awaiting the day we changed the minimum deployment target in what would become [Microsoft Office 2016 for Mac](https://en.wikipedia.org/wiki/Microsoft_Office_2016) to Mac OS X 10.6[[1](#_footnotedef_1)]. [Snow Leopard](https://en.wikipedia.org/wiki/Mac_OS_X_Snow_Leopard) introduced _a lot_ of new APIs, including [Grand Central Dispatch](https://developer.apple.com/documentation/DISPATCH) and [blocks](https://en.wikipedia.org/wiki/Blocks_(C_language_extension)). But, I was most excited to start using Objective-C [Associative References](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocAssociativeReferences.html) to replace some terrible code.

## The Old Way

Objective-C’s greatest strength (and weakness) is its [dynamic method binding](https://alwaysprocessing.blog/2023/01/02/objc-class-arch#method-dispatch). Virtually all major third-party apps (ab)use this feature to fill a functionality gap or mitigate app/system architecture impedance mismatches.

The ability to tie an object’s lifetime to the lifetime of an object instantiated and controlled by a third party (i.e., Apple) was one such functionality gap. Before the runtime provided this feature, an app could implement this functionality by, in part, pre-patching the implementation of `-[NSObject dealloc]`. The following code sample shows how a third party may have implemented _Associative References_ using this approach.

```
#import <Foundation/Foundation.h>
#import <objc/runtime.h>

static OSSpinLock s_lock;               // for main side table
static NSMapTable *s_associatedObjects; // main side table
static IMP s_NSObject_dealloc;          // original implementation

void APAssociatedObjectSet(id object, id association) {
  id previousAssociation = nil;

  // retain does not require the lock, so do it outside of the
  // lock to minimize time spent holding the lock
  [association retain];

  OSSpinLockLock(&s_lock);
  previousAssociation = [s_associatedObjects objectForKey:object];
  if (association != nil) {
    [s_associatedObjects setObject:association forKey:object];
  } else {
    [s_associatedObjects removeObjectForKey:object];
  }
  OSSpinLockUnlock(&s_lock);

  // release outside of the lock in case this is the last
  // release, as the dealloc implementation acquires the lock
  [previousAssociation release];
}

id APAssociatedObjectGet(id object) {
  OSSpinLockLock(&s_lock);
  id association = [s_associatedObjects objectForKey:object];
  // retain the associated object to ensure it's not deallocated
  // while in use by the caller in case another thread changes the
  // associated object between now and then
  [association retain];
  OSSpinLockUnlock(&s_lock);

  return [association autorelease];
}

static void APAssociatedObject_dealloc(id self, SEL _cmd) {
  // release any associated object and remove the side table entry
  APAssociatedObjectSet(self, nil);
  (*s_NSObject_dealloc)(self, _cmd);
}

void APAssociatedObjectInitialize(void) {
  s_lock = OS_SPINLOCK_INIT;
  // The key is weak to prevent the object from becoming immortal.
  // The value is weak to explicitly control the retain count to
  // prevent dealloc reentrancy deadlocks.
  s_associatedObjects=[NSMapTable mapTableWithWeakToWeakObjects];

  // Pre-patch -[NSObject dealloc] to clean up s_associatedObjects
  Method m = class_getInstanceMethod([NSObject class],
                                     @selector(dealloc));
  s_NSObject_dealloc = method_getImplementation(m);
  method_setImplementation(m, (IMP)&APAssociatedObject_dealloc);
}
```

Although the implementation is only 59 lines, including white space and comments, there are a few things I want to call out:

- This implementation supports 0 or 1 object associations but could support an arbitrary number of associations, like `objc_setAssociatedObject()`, with minor revisions. Alternatively, the client could use an `NSMutableDictionary` to associate an arbitrary number of objects.
- Every `-dealloc` needs to acquire a lock to perform bookkeeping (in addition to the runtime and allocator lock acquisition(s)). We saw in a previous post that the runtime has a [fast deallocation path](https://alwaysprocessing.blog/2023/01/19/objc-class-isa#has_assoc-has_cxx_dtor-weakly_referenced-and-has_sidetable_rc) for object instances that _do not_ have an associated reference (in addition to other criteria), enabling it to avoid locking overhead for most cases.
- Removing an association may cause the associated object to deallocate, which, in turn, may cause its associated objects to deallocate. So, the implementation must avoid recursion while holding the lock, as `OSSpinLock` is not reentrant.
- Pre-patching `-dealloc` on the class of the object gaining an association is not a viable approach for two reasons:

    1. A class hierarchy may have multiple patches. For example, after setting an associated object on an `NSObject` and another on `NSView`, all `NSView` instances, including subclasses, call into the patch twice during deallocation. An implementation could handle this case but at the cost of additional complexity.
    2. Calling into the correct `-dealloc` from the patch becomes more challenging. Continuing with the above example, if an `NSTableView` is deallocating, how does the patch know whether it should call the `-[NSView dealloc]` implementation or the `-[NSObject dealloc]` implementation? (The class identity of `self` is always `NSTableView`.) A significant amount of bookkeeping would be required to track where an object is in its dealloc chain and to handle additional deallocations that occur as part of its deallocation.
- Objective-C Automatic Reference Counting (ARC) didn’t debut until OS X 10.7 Lion. So I want to highlight two things that are no longer relevant to the modern Objective-C programmer:

    - The `retain` and `autorelease` calls in `APAssociatedObjectGet()` guarantee the returned object lives through the current autorelease scope. Without this, another thread may cause the object to deallocate between its retrieval from the map table and its return to the caller.
    - The use of _weak_ in the map table’s `mapTableWithWeakToWeakObjects` factory method does **not** have ARC’s zeroing weak reference semantics. Instead, it’s the equivalent of ARC’s `unsafe_unretained`.
- `APAssociatedObjectInitialize()` could have an `__attribute__((constructor))` to initialize the feature before `main()` is called. I left that out as major apps usually have a sophisticated initialization system that would call this function.

Next, let’s see how Apple’s Objective-C runtime implements this feature.

## The Apple Way

The above third-party implementation and commentary align shockingly well with Apple’s implementation. (I say shocking because I wrote it before looking up Apple’s implementation[[2](#_footnotedef_2)].)

First, let’s look at [`objc_setAssociatedObject()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime.mm#L657-L661), which simply calls [`_object_set_associative_reference()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L159-L220).

`runtime/objc-references.mm` lines [170-219](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L170-L219)

```
DisguisedPtr<objc_object> disguised{(objc_object *)object};
ObjcAssociation association{policy, value};

// retain the new value (if any) outside the lock.
association.acquireValue();

bool isFirstAssociation = false;
{
  AssociationsManager manager;
  AssociationsHashMap &associations(manager.get());

  if (value) {
    auto refs_result = associations.try_emplace(disguised, ObjectAssociationMap{});
    if (refs_result.second) {
      /* it's the first association we make */
      isFirstAssociation = true;
    }

    /* establish or replace the association */
    auto &refs = refs_result.first->second;
    auto result = refs.try_emplace(key, std::move(association));
    if (!result.second) {
      association.swap(result.first->second);
    }
  } else {
    auto refs_it = associations.find(disguised);
    if (refs_it != associations.end()) {
      auto &refs = refs_it->second;
      auto it = refs.find(key);
      if (it != refs.end()) {
        association.swap(it->second);
        refs.erase(it);
        if (refs.size() == 0) {
          associations.erase(refs_it);
        }
      }
    }
  }
}

if (isFirstAssociation)
  object->setHasAssociatedObjects();

// release the old value (outside of the lock).
association.releaseHeldValue();
```

Given the alignment with the previous section, I’ll simply highlight key similarities and differences relative to my implementation.

- [`DisguisedPtr`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-private.h#L983-L1031) is used to inhibit heap tracing in tools like `leaks`.
- The [`ObjcAssociation`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L49-L100) helper object implements the association policy (storage with `assign`, `retain`, or `copy` semantics, and whether reads are `atomic` or `nonatomic`).
- The [`AssociationsManager`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L108-L123) is an [RAII](https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization) convenience object to lock and unlock the [associations spinlock](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L45) (now an [unfair lock](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/Threading/darwin.h#L194-L224)).
- Object associations are stored using a hash map (specifically LLVM’s [DenseMap](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/llvm-DenseMap.h)). A [top-level hash map](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L103) maps object pointers to an [associations hash map](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L102), which maps keys to `ObjcAssociation`s (the object and its retain policy).
- Associating a `nil` value removes any previously associated object.
- When an object gains its first association, the runtime updates its state to turn off the [fast deallocation path](https://alwaysprocessing.blog/2023/01/19/objc-class-isa#has_assoc-has_cxx_dtor-weakly_referenced-and-has_sidetable_rc).
- The release of any previously associated object takes place outside of the lock.

Like the setter, [`objc_getAssociatedObject()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime.mm#L642-L646) simply calls [`_object_get_associative_reference()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L137-L157). The get path is straightforward, so there’s nothing for me to comment on! 🙊

Apple’s implementation provides a curious function, [`objc_removeAssociatedObjects()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime.mm#L663-L668). I’m honestly not sure why this is a public API—the comment in [`runtime.h`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/runtime.h#L1650-L1664) advises against using it (and for a good reason):

> The main purpose of this function is to make it easy to return an object to a "pristine state”. You should not use this function for general removal of associations from objects, since it also removes associations that other clients may have added to the object. Typically you should use `objc_setAssociatedObject` with a nil value to clear an association.

Like the getter and setter functions, `objc_removeAssociatedObjects()` calls [`_object_remove_associations()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L222-L269). But, this internal function takes one additional parameter: `bool deallocating`, which is `false` when called by `objc_removeAssociatedObjects()`. This internal function has only one other caller, [`objc_destructInstance()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L8569), which, unsurprisingly, passes `true` for `deallocating`.

So, what does the `deallocating` flag do? A [comment](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L238) in the function explains its purpose:

> If we are not deallocating, then `SYSTEM_OBJECT` associations are preserved.

Apple has an internal policy flag, [`OBJC_ASSOCIATION_SYSTEM_OBJECT`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L42), which prevents its associated objects from being removed by `objc_removeAssociatedObjects()`. You can shoot yourself in the foot using this function, but Apple will prevent you from violating their assumptions.

I suspect this is why the association key has a type of `void *`: pointer keys are hard to identify in Apple’s frameworks and subsequently (ab)use in third party-apps vs., for example, string keys which are easy-ish to find and use (e.g., `NSNotificationName`).

### Tagged Pointer Objects

What happens when setting an associated object on a [tagged pointer object](https://alwaysprocessing.blog/2023/03/19/objc-tagged-ptr)? The effect is the same as assigning the object to a global variable with the same storage policy: the object remains until a new value is assigned. So, setting an associated object on a tagged pointer object will effectively leak the associated object.

The associated object implementation has no code paths to handle tagged pointers (not even to log a warning in the console). So, the runtime stores the tagged pointer in the associations hash map where it lives indefinitely because tagged pointer objects never deallocate.

Another side effect of tagged pointer objects is that they effectively [intern all values](https://en.wikipedia.org/wiki/Interning_(computer_science)). While some types like `NSNumber` are known to implement [some form of interning](https://github.com/apple-oss-distributions/CF/blob/CF-1153.18/CFNumber.c#L1037), `NSString` did not have such behavior. But, the `NSString` tagged pointer code path is aggressive enough that [localized strings loaded from disk](https://markavitale.com/objc-tagged-pointers#the-explanation) may yield a tagged pointer object! Thus, any code setting associated objects on types of `NSString` may find associated objects stomping on each other if the string instances are tagged pointer objects instead of discrete instances.

Although the use of tagged pointer objects is considered an internal implementation detail, take a look at the [classes that use tagged pointers](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-internal.h#L447-L509) and avoid using associated objects with any objects with those types.

### A Closer Look At assign Storage

In writing the post, I realized I’ve been misusing this API for over a decade 🤦‍♂️. The comment next to the [`OBJC_ASSOCIATION_ASSIGN`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/runtime.h#L1639) policy says:

> Specifies a weak reference to the associated object.

As mentioned in [The Old Way](#the-old-way) section, before ARC, the term _weak_ is equivalent to ARC’s `unsafe_unretained`; this flag does **not** use ARC zeroing weak reference semantics. Take a look through the [implementation](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm) for any use of _weak_. There isn’t any!

I have a lot of grepping and code reviewing to do this week…​

## Conclusion

A third-party implementation of _Associated References_ can nearly match what Apple can do with a first-party implementation, with the main first-party advantage being the availability of a fast deallocation path for objects without associated objects. New runtime optimizations (i.e., tagged pointer objects) may cause unexpected behavior for code associating objects with objects whose uniqueness and lifetime may change across OS versions. And, historical context is essential—the assumptions underlying documentation may change over time, warping its meaning.

---

[1](#_footnoteref_1). By the time Office 2016 launched, macOS 10.12 Sierra was the current release. So, following the _n-2_ pattern, Office’s minimum deployment target was OS X 10.10 Yosemite.

[2](#_footnoteref_2). I did make one revision after reading through Apple’s implementation, which was to perform the associated object’s retain outside of the lock.
