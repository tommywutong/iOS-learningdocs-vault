---
title: 'Friday Q&A 2009-07-17: Format Strings Tips and Tricks'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-07-17-format-strings-tips-and-tricks.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0f781586c1a003b8'
translated: false
---

> 原文：[Friday Q&A 2009-07-17: Format Strings Tips and Tricks](https://www.mikeash.com/pyblog/friday-qa-2009-07-17-format-strings-tips-and-tricks.html)　·　mikeash.com Friday Q&A

Posted at 2009-07-17 15:21 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-08-14: Practical Blocks](https://www.mikeash.com/pyblog/friday-qa-2009-08-14-practical-blocks.html)  
Previous article: [Friday Q&A 2009-07-10: Type Specifiers in C, Part 3](https://www.mikeash.com/pyblog/friday-qa-2009-07-10-type-specifiers-in-c-part-3.html)  
Tags: [c](https://www.mikeash.com/pyblog/?tag=c) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2009-07-17: Format Strings Tips and Tricks

by [Mike Ash](https://www.mikeash.com/)

**Introduction**  
 Almost everyone doing C or Objective-C programming uses format strings. In C, they're used by the `printf` family of functions. In Cocoa, `NSLog` and `NSString` both use them. They're a powerful way to build strings, but many people only know the basics. This week I'll delve into some hidden corners to take full advantage of the power it offers. Note that if you _don't_ know the basics already, this article isn't going to make a lot of sense to you, so read up on a good `printf` tutorial before continuing.

**Finding the Documentation**  
 Hopefully all my readers know this, but just in case: if you type `man printf` at your shell prompt, you will get a bunch of confusing stuff that does not appear relevant to C programming. That's because you're actually reading the documentation for the shell command `printf`, not the C function. To see documentation on the C function, you need to type `man 3 printf`. The Cocoa documentation also contains information on format strings, but since the only significant difference in Cocoa format strings is the addition of the `%@` specifier for printing the `-description` of objects, I like to just use the `printf` documentation.

**Varags and Type Promotion**  
 Format strings are always used with a function (or method) that takes variable arguments. This is important for several reasons.

First, the more obvious reason is that C doesn't provide any mechanism for the called function to know how many or what type of variable arguments it got. This means that your format string _must_ exactly match the arguments you provide. Any mismatch could lead to bad output or a crash.

The less obvious reason is that C promotes types in values that get passed as variable arguments. In short, anything smaller than an `int` gets promoted to `int`, and `float` gets promoted to `double`. So when you pass in a `char`, you'll use a format specifier for `int` to print it, and likewise with passing a `float` and using a `double` specifier.

**Types of Unknown Size**  
 Frequently when programming in C or Cocoa you'll use a `typedef` whose definition is not guaranteed. Examples of this are `size_t`, `socklen_t`, `NSInteger`, and `CGFloat`.

For `size_t` it's easy: `printf` actually has a format specifier for `size_t`: use the `z` with one of the standard `int` specifiers.

For `CGFloat` it's also easy: because `float` gets promoted to `double`, the same `%f` specifier will work with either. No need to change anything.

For `socklen_t` and `NSInteger` you need to get a little cleverer. You can't use `%d` because they might be bigger than an `int`. You can't use `%ld` or `%lld` because they might be smaller than those, and type promotion doesn't carry over. They could even be bigger than those. What you'll want to do here is make an explicit cast to your variable to a size you know will be large enough to hold it, and then use that specifier. For example:

```
    printf("%jd", (intmax_t)myNSInteger);
```

**Strings of Limited Length**  
 The `%s` specifier will print a C string. This is tremendously handy. However sometimes you want to print a sequence of characters that isn't necessarily a C string. For this, you can use the `.` (that's a period) modifier to specify a length. For example, here is a convenient way to turn a `FourCharCode` into an NSString:

```
    uint32_t valSwapped = CFSwapInt32HostToBig(fcc); // FCCs are stored backwards on Intel
    NSString *str = [NSString stringWithFormat:@"%.4s", &valSwapped;];
```

The

tells

that the string is only four characters long, which keeps it from running off the end.

Sometimes you don't know the length ahead of time. This used to happen a lot with Pascal strings, but they're getting pretty rare these days. For this, you can use `*` as your length, and then it will read the length as a separate argument. (Note that this separate argument must be of type int, so beware types of unknown size!)

Here's an example of that:

```
    printf("%.*s", length, charbuffer);
```

And here's how you can use that to print a Pascal string, in case you ever run into one:

```
    printf("%.*s", pstring[0], pstring + 1);
```

Printing pointers is a handy thing to do but many people don't know how to do it right. You often see code like this:

```
    printf("0x%x", pointer);
```

This is wrong! Not only is the output ugly (you don't get leading zeroes) but it's not guaranteed to work at all, because you're passing a pointer but specifying an

.

The correct way is easy: just use the `%p` specifier. You get nice hexadecimal output and the type always matches.

**Beware of NULL**  
 This one is so commonly ignored that `gcc` and `clang` actually have a workaround just for this, but it's still interesting to know. `NULL` can legally just be a `#define` to `0`, like so:

```
    #define NULL 0
```

If you then try to pass

as a pointer argument to a vararg function like

, your code is no longer conformant, because you're really passing an

! For example, this is, strictly speaking, wrong:

```
    printf("%p", NULL);
```

(Note that the same goes for

.)

This is easy to fix: if you ever need to do this sort of thing, you can just cast the `NULL` to a pointer type like so:

```
    printf("%p", (void *)NULL);
```

Note that this problem is most commonly encountered in functions which need a

-terminated list of arguments, like

or

. Yes, that means all of the code out there which looks like this is, strictly speaking, wrong:

```
    [NSArray arrayWithObjects:a, b, c, nil];
```

How do we get away with it? The compiler helps. As I mentioned before,

and

have a workaround for this. They

to be a magic symbol which has either pointer or integer type depending on the context in which it's used, so the correct pointer value is passed into the function.

**Always Constant Format Strings**  
 I see far too much code which does this:

```
    NSLog(someString);
```

This works most of the time, but what if

contains the character sequence

, or another format specifier? Then you probably crash.

It gets worse. What if you do this with `printf` or similar instead, and `someString` comes from a source outside your control, like off the internet? Then horrible things can occur.

One of the format specifiers supported by `printf` (but not Cocoa) is the `%n` specifier. This is very different from the other specifiers, in that it actually gives you a value back instead of taking one from you. It wants an `int *` argument, and will write the number of characters written so far into that argument. For example:

```
    printf("%d%n%d", a, &howmany, b);
```

After this executes,

will contain the width of the first integer being printed.

If an attacker has control over the format string, then they can use the `%n` specifier to write an arbitrary value to a location in memory! This can then be used to take over your program. [This attack is not theoretical](http://en.wikipedia.org/wiki/Format_string_attack).

In general, you should not pass anything other than a constant string as a format string. Every so often it is useful to build a format string dynamically first, but think hard before you do this whether you can accomplish your goal without that, and if you do it, then take extra care to ensure that your string will always be valid.

**Random Access Arguments**  
 Typical format string usage is straight through start to finish. The first specifier uses the first argument, the second specifier uses the second argument, etc. However this is not mandatory! You can actually have any specifier use any argument. This is done by adding `n$` to the format specifier, where `n` is the argument number to print. Arguments count from 1. For example, this prints the two arguments in reverse order:

```
    printf("a = %2$d  b = %1$d", b, a);
```

You can even reuse the same argument more than once. This can be handy when writing out a long string and you need to use the same variable string, for example a name, multiple times.

```
    printf("%1$s could not be accessed, error %d. Try rebooting %1$s.", name, err);
```

Note that if you do this, you

skip any arguments. For example, this is invalid:

```
    printf("a = %2$d", b, a);
```

The reason for this is revealed in the fact that C does not tell the called function about the arguments. It has to retrieve all type information and argument counts from the format string itself. Here you're giving it incomplete information. It knows there are two arguments, but it has no idea of the type of the first argument. This means that it cannot know how to access the second argument, so the result of making this call is undefined.

**Conclusion**  
 That wraps up this week's Friday Q&A. There's a lot more to what format strings can do than what I discussed today. Read the man page and take a look at how you can control precision, padding, output formats, and more.

Friday Q&A will be going on hiatus for at least one week and probably two due to various things which are going to keep me busy in that time.

In the meantime, keep those suggestions coming in. The more topics I have to choose from, the better topics you'll be able to read, so [send them in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
