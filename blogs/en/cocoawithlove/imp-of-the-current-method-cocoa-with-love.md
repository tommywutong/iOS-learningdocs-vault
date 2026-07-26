---
title: 'IMP of the current method | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/02/imp-of-current-method.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:002349661d70e986'
translated: false
---

> 原文：[IMP of the current method | Cocoa with Love](https://www.cocoawithlove.com/2008/02/imp-of-current-method.html)　·　Cocoa with Love (Matt Gallagher)

I wanted to get my new blog started with something that's unlikely to be found anywhere else. This is an obscure hack to access a fundamental piece of Objective-C data.

## Not a trivial question

The section title doesn't lie, this isn't a trivial question. Objective-C (a language renowned for its ability to look everything up at runtime) has no variables, functions, operators or identifiers which directly access this value.

Pragmatic readers might ask: "Why should I care?"

Honestly, these readers should stop being difficult. I've only been writing this blog for 7 sentences now and already they're giving me grief. As George Mallory famously said: "Because it's there". Indeed, the mountain certainly was there and it killed him.

If this is still insufficient for you, then I promise to give a reason in a future post _[**edit**: have a look at [this future post](https://www.cocoawithlove.com/2008/03/supersequent-implementation.html)]_. I'm holding out for now because I want repeat readers and to get on with this post.

## What is the IMP?

IMP is short for "implementation". It is the memory address of the start of a code block that implements a Method. It can be invoked just like a C function if needed. Normally though, you send a message to an Objective-C object, and the Objective-C runtime finds the Method associated with that message and invokes the IMP for you.

There are rare cases though, where you may want to bypass the typical "[object method:parameter];" syntax and the objc_msgSend() function. In these cases you'll need to invoke the IMP directly. Herein lies its usefulness and the reason why you might wish to access it directly.

## IMPs in the Objective-C runtime data

In Objective-C, every method of every class in your program has a data structure constructed for it at runtime. In Objective-C 2.0, this structure is officially "opaque" (it's still there but you access its contents through functions instead of directly).

Let's look at what a Method structure contains...

```objc
struct objc_method
{
  SEL method_name;
  char * method_types;
  IMP method_imp;
};
typedef objc_method Method;
```

So the method has 3 properties:

- method_name describes the signature of the method; its value is shared by all methods with the same name and parameter names
- method_types describes the types of the parameters to the method.
- method_imp is the function pointer, i.e. the address of the code invoked when this method is selected for invocation.

It's this "method_imp" that we are challenged to find. The IMP of a method is the address of its code, also known as its function pointer.

## So where's the problem?

It would seem like the IMP of the current method should be easy. Every method has a self parameter and a rarely used _cmd parameter and using these we can invoke:

```objc
[(NSObject *)[self class] instanceMethodForSelector:_cmd];
```

Except that this only ever returns the _default_ IMP.

Selectors like _cmd are not unique; they are shared by every method override, so if a Class hierarchy has multiple implementations at multiple depths in the hierarchy corresponding to _cmd, you can't differentiate them.

This is deliberate on the part of the Objective-C designers. The construction of the class hierarchy is supposed to determine which IMP you get for a given SEL.

I'm being picky here: I wish to access the current Method implementation, regardless of whether it's the default.

Don't mistake me: if you _are_ after the default IMP (probably the common case), you _should_ use +[NSObject instanceMethodForSelector:] or one of the similar methods or functions. However, this article concerns the case where you're after a specific, not necessarily default, IMP.

## Can't you just reference the function, same as in C?

In pure C getting the equivalent of an IMP is easy, as in the following example:

```objc
void myFunction()
{
   void *myImplementation = myFunction;
  
   ...
}
```

In C, getting the function pointer of the current function is as easy as using the name of the function as an identifier (it's always in scope inside itself).

There was a time when it was this simple in Objective C too. You used to be able to reference a method by its mangled name. Like this:

```objc
- (void)myMethodWithParam1:(int)someParameter andParam2:(int)otherParameter
{
   void *myImplementation = _i_MyClass_MyCategory_myMethodWithParam1_andParam2_;
  
   ...
}
```

That time is long gone and mangled names are no longer available. So how do you get the address of the start of the function that you're in?

## The solution

My solution begins with a little-known GCC "built-in" function.

```objc
__builtin_return_address(0)
```

This function gives the return address from the current stack frame. You can pass numbers other than zero (to get other stack frames) but only zero is guaranteed to work.

So how does this help, given that the return address into the middle of a function is not the same as the IMP which points to the start of the function?

Well, we know:

- a Method implementation is contiguous
- __builtin_return_address(0)

  in a child function of the Method implementation of interest will be an address somewhere inside the implementation of interest

These two facts combined guarantee that if we invoke __builtin_return_address(0) in child function of a Method implementation, then the Method implementation's IMP must be the closest preceding IMP in the program to the result given by __builtin_return_address(0).

Since we can get the set of all Method IMPs for a Class from the method "self" parameter, we now have an approach to solve the problem:

1. During an invocation of the Method of interest,
2. self

  and

  _cmd

  from the method into our "find IMP" function.
3. Inside this function, get the set of all Methods from the object's class and super-classes.
4. __builtin_return_address(0)

  and store its result.
5. method_name

  is equal to the

  _cmd

  and whose

  method_imp

  is closest to the result from

  __builtin_return_address(0)

  without going over.
6. method_imp

  is the IMP of the Method of interest.

So here's the code:

```objc
#import &lt;objc/objc-class.h&gt;
IMP impOfCallingMethod(id lookupObject, SEL selector)
{
    NSUInteger returnAddress = (NSUInteger)__builtin_return_address(0);
    NSUInteger closest = 0;
    
    // Iterate over the class and all superclasses
    Class currentClass = object_getClass(lookupObject);
    while (currentClass)
    {
        // Iterate over all instance methods for this class
        unsigned int methodCount;
        Method *methodList = class_copyMethodList(currentClass, &methodCount);
        unsigned int i;
        for (i = 0; i < methodCount; i++)
        {
            // Ignore methods with different selectors
            if (method_getName(methodList[i]) != selector)
            {
                continue;
            }
            
            // If this address is closer, use it instead
            NSUInteger address = (NSUInteger)method_getImplementation(methodList[i]);
            if (address &lt; returnAddress &amp;&amp; address &gt; closest)
            {
                closest = address;
            }
        }
    
        free(methodList);
        currentClass = class_getSuperclass(currentClass);
    }
    
    return (IMP)closest;
}
```

The code is fairly straightforward: iterate over the hierarchy of Classes, and the Methods on each of these Classes (ignoring Methods that don't correspond to our selector) and track the closest preceding IMP to the __builtin_return_address(0) result.

We can now invoke it like this:

```objc
- (void)myMethodWithParam1:(int)someParameter andParam2:(int)otherParameter
{
   void *myImplementation = impOfCallingInstanceMethod([self class], _cmd);
  
   ...
}
```

## Conclusion

I like the satisfaction of being able to access any value in my program. Having access to the method's selector and the current object by default in a function is okay but ambiguous. Knowing I can retrieve the IMP makes things seem more tidy.

This approach does need to iterate over all methods in the current class' hierarchy. Technically, a faster approach would be to read the return address from the current (rather than a child) function and traversing backwards through the instructions at that location to find the "call" or equivalent instruction which invoked the current function. This would be tricky and platform dependent.

Anyone keen to try that?
