---
title: 'Variable argument lists in Cocoa | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/05/variable-argument-lists-in-cocoa.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:dd57bc04091a5429'
translated: false
---

> 原文：[Variable argument lists in Cocoa | Cocoa with Love](https://www.cocoawithlove.com/2009/05/variable-argument-lists-in-cocoa.html)　·　Cocoa with Love (Matt Gallagher)

This week I'll talk about methods that take variable numbers of arguments, also known as variadic methods. I'll show you the Objective-C syntax and implementation, give a quick rundown of the ways that Cocoa classes provide variable argument support and I'll also show you a way to fake va_list parameters to handle Cocoa's variadic method equivalents at runtime.

## Variable arguments basics

Passing a variable number of arguments to a method is a convenient way to handle a list of variables that are in scope at compile time.

The Objective-C language handles variable arguments in the same way that Standard C does. Normally, you will encounter variable argument lists in one of two forms: "Format strings" or "Nil terminated lists".

### Format strings

The traditional example for variable arguments are format strings. Format strings contain a number of "placeholders" (escape sequences starting with a "%" sign) that are replaced with data from variables when the format string and the variable arguments are passed to the method.

```objc
NSString *myString = [NSString stringWithFormat:
    @"Number %d, String: %@, Float: %g", 123, @"SomeString", 34.5];
```

This method is declared as follows:

```objc
+ (id)stringWithFormat:(NSString *)format, ...;
```

The "..." is the variable argument.

This method declares a first parameter but everything else is "variable". This does not mean optional. Instead, it means that a number of extra parameters will be required. Exactly what number and their types depends on how the method works.

The documented behavior for `stringWithFormat:`, is that it scans the `format` string and requires 1 variable argument for every escape sequence (in this case there are 3) and the type must match the specifier for each escape sequence (in this case, "d", "@" and "g" specify `int`, `id` and `float`/`double`).

### Nil terminated lists

The other common type of variable argument list method is one that takes a list of objects terminated by nil.

In Cocoa, these are commonly used for constructing collection objects.

```objc
NSArray *myArray = [NSArray arrayWithObjects:@"One", @"Two", @"Three", nil];
```

The documented rule for this type of method is that the last argument must be `nil`.

### Getting argument numbers wrong

The details of "Format strings" and "Nil terminated lists" reveal the difficulty with variable argument lists in Objective-C: knowing how many arguments exist — i.e. when to stop reading arguments.

Objective-C, like C, does not have a runtime argument count, nor does it pass runtime argument types. So the number and types of arguments must be determined by some other policy. In the case of these two examples, the argument count is, respectively: the number of escape sequences in the "Format string" or the number of arguments before the first `nil`. For "format strings" the types are determined by the escape sequences, for "Nil terminated" lists, the arguments are always pointers.

The penalty for getting variable argument list wrong can be severe: the compiler won't typically notice a problem and your code will crash or behave very strangely at runtime. The important lesson to learn is that you should only use variable arguments in a situation where the policy for numbers and types of arguments is very clear.

> compiler flag in GCC. See below for more about how this works.

## Implementing variable arguments for your own methods

Lets look at the implementation for the example class:

```objc
@interface StringContainer : NSObject
{
    NSString *contents;
}
@end
```

Imagine we wanted a method that would set the `contents` string this class contains by concatenating a variable argument list of strings together.

In this case, we will use the `nil` terminated approach — the list of strings to concatenate will end with a `nil`, so we know when to stop reading.

The declaration for the method looks like this:

```objc
- (void)setContentByAppendingStrings:(NSString *)firstString, ...
    NS_REQUIRES_NIL_TERMINATION;
```

The `NS_REQUIRES_NIL_TERMINATION` part is a macro that tells the compiler that invocations of this method must include a `nil`-terminated list of arguments. Failure to `nil`-terminate the list will result in a compiler warning if `-Wformat` is enabled.

Annoyingly, `-Wformat` is not enabled by default. Double annoyingly, it is named "Typecheck Calls to printf/scanf" in the "GCC 4.0 Warnings" section of the "Build Settings" in Xcode, even though this setting affects the `NS_REQUIRES_NIL_TERMINATION` macro which is used commonly throughout all of Cocoa — far beyond `printf` and `scanf`.

The implementation of this method is as follows:

```objc
- (void)setContentByAppendingStrings:(NSString *)firstArg, ...
{
    NSMutableString *newContentString = [NSMutableString string];
    va_list args;
    va_start(args, firstArg);
    for (NSString *arg = firstArg; arg != nil; arg = va_arg(args, NSString*))
    {
        [newContentString appendString:arg];
    }
    va_end(args);
    
    [contents autorelease];
    contents = [newContentString retain];
}
```

The `va_list`, `va_start`, `va_arg` and `va_end` are all standard C syntax for handling variable arguments. To describe them simply:

- - A pointer to a list of variable arguments.
- - Initializes a

  to point to the first argument

  the argument specified.
- - Fetches the next argument out of the list. You must specify the type of the argument (so that

  knows how many bytes to extract).
- - Releases any memory held by the

  data structure.

Generally speaking, you can use this `for` loop for any variable argument situation where your arguments are all the same type. Other cases are a bit trickier but far less common — I'm sure you can work out how they would work if needed.

## va_list in Cocoa

A number of classes in Cocoa have methods that take variable numbers of arguments. In most cases, these classes will also have an equivalent method that takes a `va_list`.

We can see an example of these `va_list` equivalents by looking at `NSString`. `NSString` declares the class method `stringWithFormat:...` (which takes a variable number of arguments) and `NSString` also declares the instance method `initWithFormat:arguments:` (where the `arguments` parameter is a `va_list`) which handles the equivalent behavior of `stringWithFormat:...`.

These `va_list` methods are used in the situation where your class defines a method with a variable argument list and you need to pass those variable arguments into the Cocoa method. For example, if the `StringContainer` class listed above declared the method:

```objc
- (void)setContentsWithFormat:(NSString *)formatString, ...;
```

The implementation of this method would be as follows:

```objc
- (void)setContentsWithFormat:(NSString *)formatString, ...
{
    [contents autorelease];

    va_list args;
    va_start(args, formatString);
    contents = [[NSString alloc] initWithFormat:formatString arguments:args];
    va_end(args);
}
```

The `va_list` parameter allows us to pass our own variable argument list to the Cocoa method so that the Cocoa method can handle the arguments.

## Creating a fake va_list

The `va_list` methods in Cocoa are helpful if you actually have a variable argument list.

There is another situation you many encounter though: you want to use a method like `-[NSString initWithFormat:arguments:]` using a runtime generated array of arguments. There is no `NSString` format method that takes an `NSArray` of arguments, so how could we handle a format string at runtime?

The answer lies in how `va_list` works. While GCC makes it very clear that `va_list` is "platform specific", the reality is that on Mac and iPhone Objective-C platforms, it is simply a byte buffer containing the arguments. In fact, if you've ever used an ABI inspection tool (like [class-dump-x](http://iphone.freecoder.org/classdump_en.html)) on a method taking a variable argument list, you'll see that it is simply a `char *`.

To show how we can use this knowledge, consider the following method on the `StringContainer` class:

```objc
- (void)setContentsWithFormat:(NSString *)formatString arguments:(NSArray *)arguments;
```

If we assume that all of the variable arguments required fro the `formatString` are objects, then we can implement this method as follows:

```objc
- (void)setContentsWithFormat:(NSString *)formatString arguments:(NSArray *)arguments
{
    [contents autorelease];

    char *argList = (char *)malloc(sizeof(NSString *) * [arguments count]);
    [arguments getObjects:(id *)argList];
    
    contents = [[NSString alloc] initWithFormat:formatString arguments:argList];
    
    free(argList);
}
```

What I've done here is simply copied the `NSArray` to a C-style byte buffer and then passed that buffer to the `initWithFormat:arguments:` method.

If your arguments are not all Objective-C objects, you'd need to take greater care to assemble the byte buffer but the principles would be the same.

## Some variadic notes

### NSInvcation incompatibility

`NSInvocation` does not support variadic methods. I'm not sure why this is — maybe `NSInvocation` wants to avoid making assumptions about `va_list`, maybe it is because `NSMethodSignature` can't describe the storage requirements of variable arguments for `NSInvocation` or maybe the Cocoa developers have families and just wanted to go home early.

### Variadic macros

You can also write variadic macros, much like variadic methods, by using the `##__VA_ARGS__` placeholder in your macros. See the macros near the bottom of my post titled [Supersequent Implementation](https://www.cocoawithlove.com/2008/03/supersequent-implementation.html) for an example of how this works. As discussed briefly in that article, the version of GCC used for iPhone development handles variadic macros slightly differently, so pay attention to the differences when targetting the iPhone platform.

## Conclusion

Variadic methods require a degree more care than regular methods because variable argument lists have no "introspection" (you cannot ask for the number and type of arguments) — so their usage relies on documentation and implicit agreements between the sender and receiver.

In your own code, variadic methods should be used sparingly — passing variables in an `NSArray` or `NSDictionary` is safer (if slightly slower and syntactically more verbose) due to the fact that these classes _do_ offer introspection.

When the implicit sender/receiver agreement is clear, variadic methods work well. They certainly make creating instances of `NSArray`, `NSSet`, `NSDictionary` easier and they are the only way to create a formatted `NSString` in a single invocation.
