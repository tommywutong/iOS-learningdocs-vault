---
title: Porting Drivers to OS X
apple_id: TP30001169
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2009-05-06'
source_url: https://developer.apple.com/library/archive/documentation/Porting/Conceptual/PortingDrivers/other-language/other-language.html
archived_at: '2026-07-18T01:50:43.183034Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Porting Drivers to OS X](Introduction%20to%20Porting%20Drivers%20to%20OS%20X.md)


[Next](Document%20Revision%20History.md)[Previous](I-O%20Kit%20Considerations.md)

# C++ Language Considerations

Because your driver will probably be written as a combination of C and C++ code, there are some potential pitfalls that you should try to avoid. Many of these are described in this chapter.

The I/O Kit as a whole is written in a subset of C++. The following features are not allowed:

- exceptions
- templates
- multiple inheritance
- non-trivial constructors

  (memory allocation and similar should be done in the `init` function)
- standard run-time type identification (RTTI)

  (RTTI-like functionality provided with OSDynamicCast)
- initialization lists

For more information, see _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ and the Object Creation and Destruction section of _[IOKit Device Driver Design Guidelines](../../Device%20Drivers/IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_.

One of the most common errors when porting a C driver core to the I/O Kit is assuming that a data type in C will have the same size as a data type with a similar name in C++. This is not always the case.

A good rule is to always make sure you use _exactly_ the same data type (with the same name) on both sides when passing data between the C and C++ portions of your driver. This can save you lots of headaches and unnecessary debugging in the future.

C code cannot call class methods directly. This poses a bit of a problem if you are writing code where a C++ method needs to be passed as a callback into your C core code.

To get around this issue, you should create an intermediate relay function within a C++ file. This function is a standard C function, but compiled using the C++ compiler. This function can then be called by C functions and easily make calls into C++ class methods.

The following rules must be followed:

- The C++ function must be declared `static`.
- One of its argument must be a pointer to an instance of your class.
- Calls to class functions must then be made with respect to that pointer.

For example, you might write a relay function that looks like this:

```swift
static int org_mklinux_iokit_swim3_driver_dosomething(
    org_mklinux_iokit_swim3_driver *self, int something_arg)
{
    dIOLog(DEBUG_GENERAL, "dosomething: enter (0x%x)\n",
        (unsigned int)self);

    self->dosomething(something_arg);
}
```

For your callback, you would need to pass two things into the C core code: the address of the class instance (the value of the `this` pointer), and the address of this function. After that, the C code can call the class function `dosomething` by doing something like this:

```
ret = (*funcptr)(classptr, argument);
```

where `funcptr` is a pointer to the relay function, `classptr` is a pointer to the class instance whose `dosomething` method is to be called, and `argument` is the argument to be passed to the `dosomething` method.

[Next](Document%20Revision%20History.md)[Previous](I-O%20Kit%20Considerations.md)

