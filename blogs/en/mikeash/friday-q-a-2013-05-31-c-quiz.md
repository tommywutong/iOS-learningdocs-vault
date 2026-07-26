---
title: 'Friday Q&A 2013-05-31: C Quiz'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-05-31-c-quiz.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:de4489678164d4da'
translated: false
---

> 原文：[Friday Q&A 2013-05-31: C Quiz](https://www.mikeash.com/pyblog/friday-qa-2013-05-31-c-quiz.html)　·　mikeash.com Friday Q&A

Posted at 2013-05-31 13:46 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2013-06-14: Reachability](https://www.mikeash.com/pyblog/friday-qa-2013-06-14-reachability.html)  
Previous article: [Friday Q&A 2013-05-17: Let's Build stringWithFormat:](https://www.mikeash.com/pyblog/friday-qa-2013-05-17-lets-build-stringwithformat.html)  
Tags: [c](https://www.mikeash.com/pyblog/?tag=c) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [quiz](https://www.mikeash.com/pyblog/?tag=quiz)

Friday Q&A 2013-05-31: C Quiz

by [Mike Ash](https://www.mikeash.com/)

**Questions**  
Here are the questions. The answers will follow. Try to answer all of the questions yourself before reading the answers. Try to do it from memory alone first, then check the answer using your compiler, the language spec, or whatever else you want to use. Keep in mind that answers found by testing your compiler may only reflect your environment, and will not necessarily be generally correct.

1. ?
2. ?
3. ? How about

  ?
4. ?
5. ?
6. ?
7. , what is the value of

  ?
8. , what is the value of

  within the function body?
9. ?
10. ?
11. ?
12. for types

  ,

  ,

  ,

  , and

  ?
13. using

  ?
14. using

  ?
15. using

  ?
16. using

  ?
17. ?
18. ?
19. ?
20. ?
21. ?

**Intermission**  
Let's give a little space for people whose eyes drifted down while reading the last few questions.

A little more space than that, I think.

Just another paragraph or two.

Did you try to figure out the answers yourself? You should give it a shot before you continue on.

Last chance! Answers follow.

**1. What is the type of the character literal `'a'`?**  
This one's easy. It's a character literal, so its type is `char`. Right?

Nope. The type is `int`. I'm not entirely sure why, but that's what the standard says. The value is still what you'd expect, so there's little practical consequence to this. Generally, you'd only notice if you tried to use `sizeof` on one.

**2. What is the type of the expression `a == b`?**  
The natural response for someone coming from a more sane language would be `BOOL`, or `bool`, or maybe even `_Bool`, which is C's official built-in boolean type as of the C99 standard. However, this is not the case: comparison expressions always have type `int`.

**3. What is the value of the expression '1 == 1'? How about '0 == 1'?**  
Although the type is always `int`, at least some sanity prevails: the value is always `1` when the comparison is true, and `0` when false. The answers here are, respectively, `1` and `0`.

**4. What is the value of the expression `42 || 0`?**  
The `||` operator is just like the `==` in that it always returns `1` or `0`. The same is true of all other logical and comparison operators. In this case, since at least one of the operands is non-zero, the value of the expression is `1`. This can be an unpleasant surprise if you're used to languages where the logical or returns the first true value it sees, which in this case would be `42`.

**5. What is the value of the expression `-1 < 1`?**  
This is as obvious as it looks: the value is `1`, because the comparison is true. This question is really only here to set up the next one.

**6. What is the value of the expression `-1 < 1U`?**  
This should be the same as before... but it's not. The type of `-1` is `int`, while the type of `1U` is `unsigned int`. In order to make the comparison, the `-1` is converted to an `unsigned int` and the resulting value compared with `1`. The resulting value is larger than `1`, so the comparison is false, and the expression yields `0`.

**7. Given a local variable declared as `char a[10]`, what is the value of `sizeof(a)`?**  
The answer is pretty simple: `a` is an array of `10` `char`s, and the value of `sizeof(a)` is `10`. You might be tempted to answer `10 * sizeof(char)`, which is technically correct, but redundant. By definition, `sizeof(char)` is always `1`. Although the C standard talks about "bytes", it has its own peculiar definition of the word, which corresponds to the `char` type. Even on an exotic system where `char` is 32 bits, `sizeof(char)` is still `1`. If you want to know how big a `char` is in absolute terms, the `CHAR_BIT` macro will tell you how many bits it contains.

**8. Given a function declared as `void f(char a[10])`, what is the value of `sizeof(a)` within the function body?**  
This is the same as the previous question, so the answer is `10`, right?

You surely know better than that by now.

This is a seriously weird corner of C. Function parameters declared as array types are invisibly converted to pointer types. These two function prototypes are _exactly the same_:

```
    void f(char a[10]);
    void f(char *a);
```

The array notation is basically just a way for the programmer to document the code a bit. We can read this as saying that `f` takes an array of `10` `char`s. To the compiler, it just says that `f` takes a pointer to `char`.

Accordingly, `sizeof(a)` is whatever the size of a pointer is on your system. On Apple platforms, it'll be `4` or `8` depending on whether you're running in 32-bit mode or 64-bit mode.

**9. What is the value of `UINT_MAX + 1`?**  
In a language full of pitfalls and undefined behavior the moment you step outside the rules, the behavior of `unsigned` types is comfortingly well-specified. All results are computed modulo the largest representable number plus one. Thus, `UINT_MAX + 1` simply produces zero.

**10. What is the value of `INT_MAX + 1`?**  
Our joy is short-lived. You might think this would also be zero, or that it would wrap around to `INT_MIN`, or that it would clamp to `INT_MAX`. All of these are possible. The value can also be `42`, or a randomly generated number. Or executing the statement could cause your web browser to visit [zombo.com](http://html5zombo.com), reboot your computer, or erase everything in `~`. Signed integer overflow is undefined behavior, which means the compiler is allowed to do basically whatever it wants at this point.

**11. What is the type of `NULL`?**  
It's a pointer type, so it must be some kind of pointer. Maybe `void *`?

It can be `void *`. It can also be `int` or another integer type! The standard says that `NULL` is a null pointer constant, which in turn is "An integer constant expression with the value 0, or such an expression cast to type `void *`...."

Because of this, you have to be careful when passing `NULL` (or `nil`) into a variadic function, since the type isn't well defined unless you cast it. This is technically incorrect:

```
    printf("%p", NULL);
```

Although modern compilers are generally good about ensuring that this is safe. Clang, for example, uses a compiler built-in for `NULL` which behaves appropriately here.

**12. What is `sizeof` for types `char`, `short`, `int`, `long`, and `long long`?**  
The answer for `char` is, of course, `1`. The answers for the rest are, "it depends".

It would be perfectly legal for a C implementation to make `char` be a 64-bit quantity, and have the size of every data type on this list be `1`. I'm not sure if this has ever been done, but there _are_ some environments, such as digital signal processors, where `char` is a 32-bit quantity, and `sizeof` everything up to `int` is `1`.

However, while the "it depends" answer is technically correct, it's also useful to know the actual quantities for the systems we use. For Apple platforms, the numbers are:

- `sizeof(char) == 1`
- `sizeof(short) == 2`
- `sizeof(int) == 4`
- in 32-bit code, and

  in 64-bit code
- `sizeof(long long) == 8`

Note that you should still use the `uintXX_t` types from `stdint.h` when precise sizes are important in your code, rather than relying on the above quantities. You'll be glad you did when Apple's next big platform suddenly has weird sizes for everything.

**13. What is the format specifier for printing an `int` using `printf`?**  
There's no trickery here: it's either `%d` or `%i`, depending entirely on your preference.

**14. What is the format specifier for printing a `short` using `printf`?**  
You use an `h` modifier to indicate that the argument is a `short`, e.g. `%hd`. However, this is unnecessary: you can simply use the format specifier for `int`. Types smaller than `int` are promoted to `int` when passed as a variable argument to a variadic function like `printf`. That means that `%d` works not only for `int`, but also `short` and `char`.

(Technically, `%d` may not be valid for `char`. _If_ `char` is `unsigned`, and _if_ `sizeof(int) == 1`, _then_ a `char` will be promoted to an `unsigned int` instead of an `int`. Then, _if_ the value of the `char` can't be represented in a `signed int`, attempting to treat it as one is invalid. This is unlikely to be a concern on any platform you encounter.)

**15. What is the format specifier for printing a `double` using `printf`?**  
Another easy one: `%f` is the most common one, and `printf` also supports `%F`, `%e`, `%E`, `%g`, `%G`, `%a`, and `%A`. See the documentation for an explanation of what all these variants are for.

**16. What is the format specifier for printing a `float` using `printf`?**  
This is another trick question due to argument promotion. When used as a variable argument, `float` is promoted to `double`, so all of the format specifiers for `double` also work for `float`.

**17. What is the value of the expression `*(char *)NULL`?**  
A common response to this would be "it crashes", which is certainly one possible outcome. However, this is yet another instance of undefined behavior: you're simply not allowed to dereference `NULL`, and when you try, the compiler is allowed to do anything. In particular, if the compiler can figure out _at compile time_ that you're trying to dereference `NULL`, it's free to do things like assume that code can never actually execute (because it would be illegal) and optimize out branches accordingly. Don't write the above to intentionally cause a crash; call `abort()` instead.

**18. What is the type of the string literal `"abcde"`?**  
String literals are `char` arrays with the appropriate size. The specific string literal has type `char[6]`. Note the extra array element for the terminating `NUL` character.

It is illegal to modify the contents of a string literal, but the type is _not_ `const char[6]`. This is a holdover from the days when C had no `const` keyword. You're just supposed to know that you can't modify them.

**19. What is the value of `sizeof("abcde")`?**  
This should be obvious given the previous answer: `6`. Again, note the extra element for the terminating `NUL`. It's easy to count five characters in the string and mistakenly think that the size is `5`. Also note that, while string literals are usually treated as `char *`, they are arrays, not pointers, and so `sizeof` returns the size of the array, not the size of a pointer.

**20. What is the result of executing `free(NULL)`?**  
This is my favorite question of the bunch, because it's so poorly known despite being so simple. I've encountered many smart people who I'd have no qualms describing as "C experts" who get this wrong.

The answer is: nothing. `free(NULL)` is defined as a no-op by the standard. Every time you see an `if` guard on a `free` call, it can be removed:

```
    if(ptr != NULL) // unnecessary!
        free(ptr);
```

Of course, there's nothing wrong with leaving the check for clarity if you prefer.

Virtually everyone I've talked to about this thought that the check is necessary and `free(NULL)` would crash or otherwise invoke undefined behavior. I'm not sure where that idea came from, but it's fascinating.

**21. What is the result of executing `realloc(NULL, sizeof(int))`?**  
`realloc` is, conceptually, a `malloc`, `memcpy`, and a `free`. Much like `free(NULL)` is a no-op, `realloc` on `NULL` just allocates some fresh memory. The above is exactly equivalent to `malloc(sizeof(int))`. This can be convenient when you have a dynamically-resized buffer. You can start the pointer out as `NULL` and use the same `realloc` for the initial allocation as for resizes.

**Conclusion**  
That's it for today. I hope you know a little more about C than you did before.

Friday Q&A is driven by reader suggestions. If you have something you'd like to see covered here, [send it in](https://www.mikeash.com/pyblog/mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
