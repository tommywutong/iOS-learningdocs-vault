---
title: 'Supersequent implementation | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/03/supersequent-implementation.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:01e36e97df0e52e8'
translated: false
---

> 原文：[Supersequent implementation | Cocoa with Love](https://www.cocoawithlove.com/2008/03/supersequent-implementation.html)　·　Cocoa with Love (Matt Gallagher)

Ever wanted to override a method using a category but still invoke the default method from the category? Like invoking the super method on a super class, this example will show you how to invoke any "supersequent" method no matter if its on the super class, the current class or even another category on the current class.

## Method swizzling

In my opinion, the most fun feature of Objective-C's dynamic method lookup is being able to replace methods at runtime. For example, if you wanted to know when the -[NSWindow dealloc] method gets called and you're not using a subclass of NSWindow, you can exchange the normal -[NSWindow dealloc] method with one of your own methods and set a breakpoint or perform any logging work in your own code, before calling the original implementation.

This is done through an approach called method swizzling. An example of Method swizzling to replace -[NSWindow dealloc] method would work like this:

- Create a class, MyClass, with a class method, +(void)myReplacementMethod
- Put the following code at the start of your main() function:

```objc
Method myReplacementMethod =
    class_getClassMethod([MyClass class], @selector(myReplacementMethod));
Method windowDealloc =
    class_getInstanceMethod([NSWindow class], @selector(dealloc));
method_exchangeImplementations(myReplacementMethod, windowDealloc);
```

Prior to Objective-C 2.0 (in Mac OS X 10.5 Leopard) this code was a lot uglier. Google ["method swizzling"](http://www.google.com/search?hl=en&safe=off&q=%22method+swizzling%22&btnG=Search) and you'll see how people used to do it. Jonathan Rentzsch even wrote [a library to handle all the different variations](http://rentzsch.com/trac/wiki/JRSwizzle).

The contents of myReplacementMethod will now be called instead of NSWindow's dealloc. Conversely, if you wanted to invoke the original NSWindow method instead, all you need to do is invoke [MyClass myReplacementMethod]. This allows you to invoke the original implementation from your replacement implementation if you want to do so.

## Limitations to method swizzling

The biggest limitation to method swizzling is that it only works if the method is implemented at the level you are trying to replace.

In the above example, this means that NSWindow must implement dealloc for us to replace it. If it merely uses an inherited version of dealloc then we must replace it at the NSResponder or NSObject level, affecting all NSResponder or NSObject objects, even if we only wanted to replace it for the NSWindow objects.

In addition, documentation rarely reveals whether classes implement overrides of inherited methods. So if you're trying to swizzle a specific method at a specific level in a hierarchy, you don't really know if it will be there until the swizzling fails or succeeds. And since overrides are typically "unpublished", you don't have any guarantee that it will remain there in the future.

It would be nice to have an approach which could replace at the NSWindow level, whether or not the method is implemented at that level.

## A better proposal

I would like to be able to create a Category on a Class that overrides the method to replace but still lets me invoke the original method, like a "super" invocation but where it doesn't matter if the "super" method is on the current class or a super-class.

In the -[NSWindow dealloc] example, I just want to create -[NSWindow(MyOverrideCategory) dealloc] and still be able to invoke -[NSWindow dealloc] from my override.

Objective-C lets you create overrides in Categories but it prevents you from invoking the original implementation. This limitation occurs because Objective-C's "super" invocations only ever start from the super-class but Categories override methods on the same class.

This means, is that if you invoke [super dealloc] inside -[NSWindow(MyOverrideCategory) dealloc] it will invoke -[NSResponder dealloc] not the default NSWindow version.

I want to be able to invoke the "method immediately before the current method in the method lookup, no matter if its on the current or a super class".

## Supersequent implementation

I didn't invent the word "supersequent" but I've never seen it applied to method lookup before. It seems about right in this case because we're looking up the next implementation in the "super" direction but it may not necessarily be a "super" method.

An invocation of the supersquent method implementation follows. This example shows a Category of NSWindow overriding dealloc and then invoking the default version.

```objc
@implementation NSWindow (MyOverrideCategory)

- (void)dealloc
{
    invokeSupersequent();
}

@end
```

Obviously, the magic is contained in invokeSupersequent(). This is a C preprocessor macro whose implementation is shown below.

No parameters to invokeSupersequent are needed here but the macro takes a variable argument list. The full set of method parameters (dealloc has no parameters) must be passed into invokeSupersequent() to be received by the supersequent implementation. The compiler will not warn you if you get this parameter list wrong, so you must be careful with it.

You can also use "return invokeSupersequent();" if you want to return the result of the supersequent invocation.

The lookup itself is relatively safe in that it will invoke any "super" implementation instead, if an appropriate next implementation is not found on the current class. The current implementation (shown below) is a little rough in that it tries to invoke nil when no "super" implementation exists at all but you could easily test for a nil result if you were concerned about that possibility.

## The solution

The process works like this:

1. Find the [IMP of the current method](https://www.cocoawithlove.com/2008/02/imp-of-current-method.html).
2. Look through the current Class's hierarchy and find the next method in the list _after_ the current method (identified using the IMP from step 1) that responds to the same selector.
3. Invoke that method

Step one comes from my [earlier post of the same name](https://www.cocoawithlove.com/2008/02/imp-of-current-method.html).

Step two is just a series of iterations over the current Class' methods. It looks like this:

```objc
@implementation NSObject (SupersequentImplementation)

// Lookup the next implementation of the given selector after the
// default one. Returns nil if no alternate implementation is found.
- (IMP)getImplementationOf:(SEL)lookup after:(IMP)skip
{
    BOOL found = NO;
    
    Class currentClass = object_getClass(self);
    while (currentClass)
    {
        // Get the list of methods for this class
        unsigned int methodCount;
        Method *methodList = class_copyMethodList(currentClass, &methodCount);
        
        // Iterate over all methods
        unsigned int i;
        for (i = 0; i < methodCount; i++)
        {
            // Look for the selector
            if (method_getName(methodList[i]) != lookup)
            {
                continue;
            }
            
            IMP implementation = method_getImplementation(methodList[i]);
            
            // Check if this is the "skip" implementation
            if (implementation == skip)
            {
                found = YES;
            }
            else if (found)
            {
                // Return the match.
                free(methodList);
                return implementation;
            }
        }
    
        // No match found. Traverse up through super class' methods.
        free(methodList);

        currentClass = class_getSuperclass(currentClass);
    }
    return nil;
}

@end
```

And finally, step 3 is encapsulated in a macro which handily invokes the other two steps for you.

```objc
#define invokeSupersequent(...) \
    ([self getImplementationOf:_cmd \
        after:impOfCallingMethod(self, _cmd)]) \
            (self, _cmd, ##__VA_ARGS__)
```

I've been unable to get this macro to work on the iPhone when passing no parameters because it is not correctly stripping the final comma. In this case, I use the following:

```objc
#define invokeSupersequentNoParameters() \
   ([self getImplementationOf:_cmd \
      after:impOfCallingMethod(self, _cmd)]) \
         (self, _cmd)
```

## Warning about these macros

These macros use the `IMP` in an uncast way. This means that the compiler will treat the method as though it returns `id` and takes a variable argument list (since this is how an `IMP` is declared).

If your method returns something that is passed differently to an `id` (like a `double` or a `struct`) or some of your method arguments are `struct`s or integer values shorter than a pointer, then you will need to cast the `IMP` to the correct signature before using or the parameters won't be passed correctly.

So for a method that takes a `char` and an `unsigned short` parameter and returns a `double` you would need:

```objc
IMP superSequentImp =
    [self getImplementationOf:_cmd after:impOfCallingMethod(self, _cmd)];
double result =
    ((double(*)(id, SEL, char, unsigned short))superSequentImp)
        (self, _cmd, someChar, someUShort);
```

Hideous but required if any of the following is true:

- your return type is not a pointer or smaller size value (`float`s are acceptable)
- your parameters not pointers, pointer sized integers (`long` or `NSInteger`) or `double`s.

## Conclusion

Yes, you can invoke the default class implementation from a category on that class. In most cases though, since it is slower at runtime than method swizzling, it is primarily only useful for debugging where 5 lines less code makes it much easier to use.

The speed at runtime is slower than method swizzling because it bypasses cached method lookup. Where cached method lookup takes about 5 nanoseconds on newer machines, this approach takes about 5 microseconds on typical objects with around 50 methods in their hierarchy (slightly slower than uncached method lookup) and like uncached method lookup, it can take longer for classes with very large method tables.

There are a few other limitations as well. This approach will not work on message forwarding classes (like NSProxy) or where other fallbacks are used to handle messages when no method is found. Also, the compiler won't warn you if no supersequent implementation exists or you've passed the wrong number or type of parameters into invokeSupersequent().

Despite these three drawbacks, I still use this approach when I'm debugging. It is just one line to invoke and makes it very easy to replace a method on someone else's class.
