---
title: 'Friday Q&A 2014-08-15: Swift Name Mangling'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-08-15-swift-name-mangling.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f7e5d3e2c0a59cd9'
translated: false
---

> 原文：[Friday Q&A 2014-08-15: Swift Name Mangling](https://www.mikeash.com/pyblog/friday-qa-2014-08-15-swift-name-mangling.html)　·　mikeash.com Friday Q&A

Posted at 2014-08-15 14:20 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2014-08-29: Swift Memory Dumping](https://www.mikeash.com/pyblog/friday-qa-2014-08-29-swift-memory-dumping.html)  
Previous article: [Friday Q&A 2014-08-01: Exploring Swift Memory Layout, Part II](https://www.mikeash.com/pyblog/friday-qa-2014-08-01-exploring-swift-memory-layout-part-ii.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [guest](https://www.mikeash.com/pyblog/?tag=guest) [namemangling](https://www.mikeash.com/pyblog/?tag=namemangling) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2014-08-08: Swift Name Mangling

by [Gwynne Raskind](http://blog.darkrainfall.org/)

---

In a language such as C, where there can only ever be one function or piece of data by any given name (a _symbol_), name mangling is not required. Even so, if you look at the symbol table of a typical pure-C binary, you will find that each function name has had an `_` (underscore) prepended to it. For example:

```
    $ echo 'int main() { return 0; }' | xcrun clang -x c - -o ./test
    $ xctest nm ./test
    0000000100000000 T __mh_execute_header
    0000000100000f80 T _main
                     U dyld_stub_binder
    $
```

This simple "mangling" is now largely historical, serving little useful purpose, but remains intact for compatibility and consistency reasons. By convention, names defined in C will have an underscore, while global symbols defined by pure assembly will not (although many assembly language writers will prepend the underscore anyway for consistency).

Objective-C also does not have collisions between symbol names; Objective-C method implementations are always of the form `-[class selector]`, and Objective-C does not allow overloading of identical selectors on the same class with different type signatures.

**Okay, let's mangle some names already!**  
Matters become more complicated in languages where a simple name without any further information might be more ambiguous. Consider this example in C++:

```
    $ cat | xcrun clang -x c++ - -o test
    int foo(int a) { return a * 2; }
    int foo(double a) { return a * 2.0; }
    int main() { return foo(1) + foo(1.0); }
    ^D
    $ xcrun nm -a test
    0000000100000f30 T __Z3food
    0000000100000f10 T __Z3fooi
    0000000100000000 T __mh_execute_header
    0000000100000f60 T _main
                     U dyld_stub_binder
```

Because `foo` refers to two different functions with different signatures, which is legal in C++, it is impossible to simply generate two `_foo` symbols; the linker would not know which was which. As a result, the C++ compiler "mangles" the symbols, using a strict set of encoding rules.

Unlike C and Objective-C, in C++ and Swift function names by themselves are not enough to tell apart each individual implementation of a function. Functions with the same name which take different parameter types (`foo(int)` and `foo(double)`, for example) require more information to set them apart. Using the full signature given in code (such as "`foo(int)`") would lead to a lot of extra code in the linker and confusion when multiple type names map to the same underlying type (such as `unsigned` and `unsigned int`). Instead, in C++, the language's somewhat arcane type promotion and conversion rules are applied, and the result is mangled into a form the compiler and linker can use easily and without any confusion. The process is similar for Swift.

The simple example of `foo` above is trivially broken down:

1. First, the leading `_` common to C-style symbols.
2. Next, `_Z`, a prefix marking the symbol as a mangled global C++ name.
3. The number defines how many characters appear in the next identifier in the name; in this case 3. `3foo` thus means "the name 'foo'".
4. The `d` and `i` are respectively `double` and `int` builtin type names; return values are not part of a function's signature in C++, so the parameter list simply follows the function's full name.

For more information on how typical C++ compilers mangle names, see the [Itanium C++ ABI documentation](http://mentorembedded.github.io/cxx-abi/abi.html#mangling).

**That's all very interesting, but for a Swift article, you're taking a long time to get there!**  
Swift's name mangling is somewhat different from C++'s. Swift uses an encoding clearly based on the C++ scheme in principle, but containing considerably more information and expressing concepts only available in a more mature type system.

I'll jump right in with a complex example. Consider the following excessively contrived and completely useless Swift code:

```
        $ xcrun swiftc -emit-library -o test -
        struct e {
                enum f {
                        case G, H, I
                }
        }
        class a {
                class b {
                        class c {
                                func d(y: a, x w: b, v u: (x: Int) -> Int) -> e.f {
                                        return e.f.G
                                }
                        }
                }
        }
        ^D
        $ xcrun nm -g test
        ...
        0000000000001c90 T __TFCCC4test1a1b1c1dfS2_FTS0_1xS1_1vFT1xSi_Si_OVS_1e1f
    ...
    $
```

Swift will have generated over 100 more symbols, but this is the complex mangled name we'll tear apart: `__TFCCC4test1a1b1c1dfS2_FTS0_1xS1_1vFT1xSi_Si_OVS_1e1f`

Let's take it in order:

1. Sure enough, the leading extra `_` is there even for Swift symbols.
2. `_T` is the marker for a Swift global symbol.
3. `F` tells us that the overall type of the symbol is a function.
4. `C` represents a "class" type. In this case, we're dealing with three nested classes, so it appears 3 times.
5. `4test` is the "module name", and `1a` is the class name itself, yielding a class named `test.a`.
6. At this point, the Swift parser will set up a stack of parsed names, looking for the first non-name token in the mangled name. In this case, it will find `f` after `1d`. It then goes back and unwinds the stack of nested types from the inside out, yielding `test.a`, `test.a.b`, and `test.a.b.c` as class names. Since `1d` has no corresponding nesting type (there were only three `C`s), it becomes the innermost part of the symbol's name- `test.a.b.c.d`.
7. The lowercase `f` marks this symbol as an "uncurried function" type- in this case, a class method taking an implicitly bound first parameter, the instance itself.
8. Because we're now parsing a function type, the list of argument types comes next, followed by the return type. For an uncurried function type, the curried parameter(s) come first. `S2_` is a substitution, meaning it will use the third non substituted _type_ encountered during parsing of the name thus far (the index is zero-based). In this case, this would be `test.a.b.c` (the third class type).
9. `F` now marks the beginning of the function's parameter list, in the guise of a fresh function type. By now, it should be very obvious that the name mangling is heavily oriented around types.
10. `T` marks the beginning of a "tuple", which in this context is a list of types.
11. `S0_` is a substitution of the first type encountered in parsing, in this case `test.a`; the first parameter has this type.
12. `1x` is the external name of the second parameter. Notice that Swift does not encode internal names as part of the mangled signature.
13. `S1_` is a substitute of the second type encountered in parsing, in this case `test.a.b`; the second parameter has this type and the name `x`.
14. `1v` is the external name of the third parameter.
15. `F` marks the start of another function type.
16. `T` marks the start of another tuple, the function's parameters (the function type is unnamed).
17. `1x` is the external name of the closure's first parameter.
18. `Si` is `Swift.Int`, a shorthand for the `Int` builtin type.
19. `_` marks the end of the closure's arguments tuple.
20. `Si` is another `Int`, the closure's return type
21. `_` marks the end of the uncurried function's arguments tuple.
22. `O` marks the start of an `enum` type.
23. `V` marks the start of a `struct` type, which will contain the `enum`. (As we saw with the classes earlier, types are nested from the inside out in mangled names).
24. `S_` substitutes the (only) seen module name, `test`. Notice that this is _not_ a type substitution!
25. `1e` is the name of the `struct`.
26. `1f` is the name of the `enum`.
27. The parser sees the end of the mangled name and unwinds through the two parsed names as it did with the class names earlier.

We thus have an uncurried function, named `test.a.b.c.d`, taking a bound parameter of type `test.a.b.c`, parameters of names and types `(test.a, x: test.a.b, v: (x: Swift.Int) -> Swift.Int)`, and return type `test.e.f`. As `swift-demangle` shows us, the "official" demangling of this symbol is:

```
    $ xcrun swift-demangle _TFCCC4test1a1b1c1dfS2_FT1zS0_1xS1_1vFT1xSi_Si_OVS_1e1f
    _TFCCC4test1a1b1c1dfS2_FT1zS0_1xS1_1vFT1xSi_Si_OVS_1e1f ---> test.a.b.c.d (test.a.b.c)(z : test.a, x : test.a.b, v : (x : Swift.Int) -> Swift.Int) -> test.e.f
```

**So what does it all mean?**  
Well, to most people, not a lot. Reading mangled names is fairly straightforward, in an algorithmic sense, but needlessly difficult for human eyes. That's why demangling tools exist; should you run across mangled symbol names in practice, there's no need to squint and mentally parse it all out. There are many, many, _many_ more variations on mangled symbol names; I haven't touched on operator overloads, generics, protocols, or Objective-C compatible types, just to name a few. Here are just a few examples the compiler provided for free from the Swift code given above:

```
    _TFV4test1eCfMS0_FT_S0_ ---> test.e.init (test.e.Type)() -> test.e
    _TMLCCC4test1a1b1c ---> lazy cache variable for type metadata for test.a.b.c
    _TMmCCC4test1a1b1c ---> metaclass for test.a.b.c
    _TMnCC4test1a1b ---> nominal type descriptor for test.a.b
    _TTWOV4test1e1fSs9EquatableFS2_oi2eeUS2___fMQPS2_FTS3_S3__Sb ---> protocol witness for Swift.Equatable.== infix <A : Swift.Equatable>(Swift.Equatable.Self.Type)(Swift.Equatable.Self, Swift.Equatable.Self) -> Swift.Bool in conformance test.e.f : Swift.Equatable
    _TWoFC4test1aCfMS0_FT_S0_ ---> witness table offset for test.a.__allocating_init (test.a.Type)() -> test.a
    _TWoFCCC4test1a1b1c1dfS2_FT1zS0_1xS1_1vFT1xSi_Si_OVS_1e1f ---> witness table offset for test.a.b.c.d (test.a.b.c)(z : test.a, x : test.a.b, v : (x : Swift.Int) -> Swift.Int) -> test.e.f
```

And so on.

To top it off, the Swift name mangling algorithm is completely undocumented and subject to change, as with most things Swift-related. The above examples were all produced using Xcode 6 beta 5.

**In conclusion**  
Apple has taken a concept pioneered by C++ and expanded on it, based on Swift's unique and powerful type system. While Swift mangling shares some basic concepts with C++ mangling, it is in fact considerably different, and in some ways more powerful. It will be exciting to see whether Apple open sources, or at least documents, the logic behind Swift in general and the name mangling logic in particular, and opens up the secrets behind Swift's innovative design.

**Easter egg**  
In case anyone was wondering, here's what happens when you add Unicode to the mix:

```
    $ xcrun swiftc -emit-library -o test -
    func 💛 (lhs: Int, rhs: Int) -> Int {
            return 0;
    }
    ^D
    $ nm -g test
    ...
        0000000000001420 T __TF4testX4GrIhFTSiSi_Si
    ...
    $ xcrun swift-demangle __TF4testX4GrIhFTSiSi_Si
    _TF4testX4GrIhFTSiSi_Si ---> test.💛 (Swift.Int, Swift.Int) -> Swift.Int
```

`X4GrIh` translates to:

- `X`: eXtended character set
- `4`: the encoded length of the name
- `GrIh`: the modified-Punycode encoding of the 💛 emoji (`U+1F49B`)

Swift does not use standard Punycode encoding as used in DNS domain names, but it is similar. For more information, see [RFC3492](http://www.ietf.org/rfc/rfc3492.txt), the Punycode standard.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2014-08-15-swift-name-mangling.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
