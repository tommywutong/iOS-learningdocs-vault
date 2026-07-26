---
title: 'My Little Optimization: The Compiler Is Magic'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2018/03/My-Little-Optimization/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:5407d4c01d948383'
translated: false
---

> 原文：[My Little Optimization: The Compiler Is Magic](https://belkadan.com/blog/2018/03/My-Little-Optimization/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Many-to-Many Protocols](https://belkadan.com/blog/2018/02/Many-to-Many-Protocols/)

[My Little (String) Optimization, Part 2](https://belkadan.com/blog/2018/03/My-Little-String-Optimization-2/) »

« [Macromancy, Part 2](https://belkadan.com/blog/2016/08/Macromancy-2/?tag=cxx)

[My Little (String) Optimization, Part 2](https://belkadan.com/blog/2018/03/My-Little-String-Optimization-2/?tag=cxx) »

## [My Little Optimization: The Compiler Is Magic](#)

Today I had the idea to play with a pretty simple optimization problem: you have a string, and you want to see if it matches one of a set of known strings (down to the same Unicode codepoints, not caring about [canonical equivalence](https://www.unicode.org/reports/tr15/#Canon_Compat_Equivalence)). The naive way to do this would be to walk through and simply check every single string:

```
bool isOneOfTheStringsICareAbout(const std::string &s) {
  return s == "Battler" ||
         s == "George" ||
         s == "Jessica" ||
         s == "Maria" ||
         s == "Beatrice";
}
```

(We’re doing this in C++ because I wanted to be able to give the compiler as much information as I could. Swift is great for a lot of things, but buffers whose contents are known at compile time is not one of them. Consequently, I’ll be using the word “character” to mean what Unicode calls a “code unit”, not a grapheme cluster.)

Assuming the `==` operator is smart, this will expand to something like this:

1. is 7 as well. If so, are those 7 characters “B-a-t-t-l-e-r”?
2. is 6 as well. If so, are those 6 characters “G-e-o-r-g-e”?
3. “Jessica” has 7 letters, so…

You get the idea, and in fact you may have already spotted the first possible optimization:

```
bool isOneOfTheStringsICareAbout(const std::string &s) {
  switch (s.size()) {
  case 7: return s == "Battler" || s == "Jessica";
  case 6: return s == "George";
  case 5: return s == "Maria";
  case 8: return s == "Beatrice";
  default: return false;
  }
}
```

Now we’ll never waste time checking strings that are the wrong length. That sounds way better, right? (But keep reading.)

The other common optimization in this space is to use something _else_ that’s easy to check: the first letter of the string.

```
bool isOneOfTheStringsICareAbout(const std::string &s) {
  switch (s[0]) {
  case 'B': return s == "Battler" || s == "Beatrice";
  case 'G': return s == "George";
  case 'J': return s == "Jessica";
  case 'M': return s == "Maria";
  default: return false;
  }
}
```

This also works, and there are two situations where it’s almost certainly going to be better: when you have a lot of strings that are the same length (and so the first technique doesn’t pull its weight), and when you might not know the length of `s`. The latter comes up when working with bare “C strings”, where the length of the string is determined by counting characters until you hit a zero value.

That said, this technique does have some downsides:

- If you _do_ have the length handy, it’s probably faster to load than the first byte of the string.
- `switch` statements are most efficient when the case values are close together; if they’re too far apart, the compiler will turn them back into a series of `if`s. First letters are probably less likely to be close together than counts in most data sets.
- Switching on the first character requires that there _is_ a first character. For `std::string` I can get away with that because an empty `std::string` is guaranteed to have a single zero value in its contents, but with a different string representation I might have to check specially for the empty string.

But still, both optimizations are valid.

### Generalization

The problem with both of these approaches is that I had to hardcode the string lengths or the first letters, and if I ever screw that up my program will just silently give me wrong answer. What I’d really like is a way to only list the strings once, but get the behavior of one of the optimized versions. I could probably hack this together with macros, but this is C++. We ought to be able to do it in a more principled way, one that won’t give me bizarre syntax errors if I screw it up.

(Okay, yes, I’m going to get bizarre template errors instead.)

So, let’s try it. To make things even simpler, I’m going to use a type called [`std::string_view`](http://en.cppreference.com/w/cpp/string/basic_string_view), which was added to C++ in C++17.[1](#fn:17) `std::string_view` is like `std::string`, but it doesn’t do any memory management; it just assumes that the buffer you created it with will stay alive as long as the `string_view` does. This simplifies the representation and hopefully gives the compiler more to work with.

I started off with a very basic implementation, just to make sure I had the right idea—

```
__attribute__((always_inline))
static bool isInSet(std::string_view s) {
  // Base case for the variadic template below.
  return false;
}

// Don't panic! This says we need at least one template argument of type
// 'size_t', followed by as many more 'size_t's as we want.
template <size_t N, size_t ...RestN>
__attribute__((always_inline))
static bool isInSet(
    std::string_view s,
    const char (&first)[N], // "reference to array of size N"
    const char (&...rest)[RestN] // "a bunch more references to arrays"
) {
  if (s == first) {
    return true;
  }
  // Recursion! With one less argument, this time...
  return isInSet(s, rest...);
}

bool isOneOfTheStringsICareAbout(std::string_view s) {
  return isInSet(s, "Battler", "George", "Jessica", "Maria", "Beatrice");
}
```

—and that was actually completely sufficient. It turns out that simply _switching to `string_view`_ gave the compiler enough information to _automatically_ turn the code I had way back at the beginning into the switch-on-length variant. This whole recursive variadic template function nonsense was cute, and does make the code a little more compact than writing a bunch of `||`s, but it’s [totally unnecessary](https://godbolt.org/#g:!((g:!((g:!((h:codeEditor,i:(j:1,lang:c%2B%2B,source:'%23include+%3Cstring_view%3E%0A%0Abool+isOneOfTheStringsICareAbout(%0A++++std::string_view+s)+%7B%0A++return+s+%3D%3D+%22Battler%22+%7C%7C%0A+++++++++s+%3D%3D+%22George%22+%7C%7C%0A+++++++++s+%3D%3D+%22Jessica%22+%7C%7C%0A+++++++++s+%3D%3D+%22Maria%22+%7C%7C%0A+++++++++s+%3D%3D+%22Beatrice%22%3B%0A%7D%0A'),l:'5',n:'0',o:'C%2B%2B+source+%231',t:'0')),k:43.25889164598842,l:'4',n:'0',o:'',s:0,t:'0'),(g:!((g:!((h:compiler,i:(compiler:clang600,filters:(b:'0',binary:'1',commentOnly:'1',demangle:'0',directives:'0',execute:'1',intel:'0',trim:'1'),lang:c%2B%2B,libs:!(),options:'-std%3Dc%2B%2B17+-O3+-emit-llvm',source:1,wantOptInfo:'1'),l:'5',n:'0',o:'x86-64+clang+6.0.0+(Editor+%231,+Compiler+%231)+C%2B%2B',t:'0')),k:50.78855538287415,l:'4',m:50,n:'0',o:'',s:0,t:'0'),(g:!((h:compiler,i:(compiler:clang600,filters:(b:'0',binary:'1',commentOnly:'0',demangle:'0',directives:'0',execute:'1',intel:'0',trim:'0'),lang:c%2B%2B,libs:!(),options:'-std%3Dc%2B%2B17+-O3',source:1,wantOptInfo:'1'),l:'5',n:'0',o:'x86-64+clang+6.0.0+(Editor+%231,+Compiler+%232)+C%2B%2B',t:'0')),header:(),l:'4',m:50,n:'0',o:'',s:0,t:'0')),k:56.74110835401158,l:'3',n:'0',o:'',t:'0')),l:'2',n:'0',o:'',t:'0')),version:4). Wow!

(I had thought this was going to take me a good chunk of time, so I was even a little _disappointed_ that the compiler was this good. What _actually_ ended up taking time was playing with my variadic template and not realizing that if I didn’t mark the functions `always_inline` or at least `static`, the compiler wouldn’t actually optimize away the recursive calls, because it _might be the case_ that something else in the program needs them, and it would be better not to use up more _code size._ Or something like that.)

Okay, so the compiler is smart and using `std::string_view` instead of `std::string` can actually be an optimization, although you have to be careful when you do it. What about the other optimization, though?

The compiler only did the original optimization for me because `string_view`’s `==` operator starts off by comparing the lengths, like I said at the beginning of the post. It’s not going to try to look at the character data because it can’t know that it’s safe to do that. (In particular, a zero-length `string_view` may have a null data pointer.) So my variadic function above wasn’t _completely_ for nothing; we just need to tweak it a bit:

```
__attribute__((always_inline))
static bool isInSet(std::string_view s) {
  // Base case for the variadic template below.
  return false;
}

// Don't panic! This says we need at least one template argument of type
// 'size_t', followed by as many more 'size_t's as we want.
template <size_t N, size_t ...RestN>
__attribute__((always_inline))
static bool isInSet(
    std::string_view s,
    const char (&first)[N], // "reference to array of size N"
    const char (&...rest)[RestN] // "a bunch more references to arrays"
) {
  if (s[0] == first[0]) { // NEW!
    if (s == first) {
      return true;
    }
  }
  // Recursion! With one less argument, this time...
  return isInSet(s, rest...);
}

bool isOneOfTheStringsICareAbout(std::string_view s) {
  if (s.empty()) { // NEW!
    return false;
  }
  return isInSet(s, "Battler", "George", "Jessica", "Maria", "Beatrice");
}
```

And if we [check the compiled code](https://godbolt.org/#g:!((g:!((g:!((h:codeEditor,i:(j:1,lang:c%2B%2B,source:'%23include+%3Cstring_view%3E%0A%0A__attribute__((always_inline))%0Astatic+bool+isInSet(std::string_view+s)+%7B%0A++//+Base+case+for+the+variadic+template+below.%0A++return+false%3B%0A%7D%0A%0A//+Don!'t+panic!!+This+says+we+need+at+least+one+template+argument+of+type%0A//+!'size_t!',+followed+by+as+many+more+!'size_t!'s+as+we+want.%0Atemplate+%3Csize_t+N,+size_t+...RestN%3E%0A__attribute__((always_inline))%0Astatic+bool+isInSet(%0A++++std::string_view+s,%0A++++const+char+(%26first)%5BN%5D,+//+%22reference+to+array+of+size+N%22%0A++++const+char+(%26...rest)%5BRestN%5D+//+%22a+bunch+more+reference+to+arrays%22%0A)+%7B%0A++if+(s%5B0%5D+%3D%3D+first%5B0%5D)+%7B%0A++++if+(s+%3D%3D+first)+%7B%0A++++++return+true%3B%0A++++%7D%0A++%7D%0A++//+Recursion!!+With+one+less+argument,+this+time...%0A++return+isInSet(s,+rest...)%3B%0A%7D%0A%0Abool+isOneOfTheStringsICareAbout(std::string_view+s)+%7B%0A++++if+(s.empty())+%7B%0A++++++return+false%3B%0A++++%7D%0A++return+isInSet(s,+%22Battler%22,+%22George%22,+%22Jessica%22,+%22Maria%22,+%22Beatrice%22)%3B%0A%7D%0A'),l:'5',n:'0',o:'C%2B%2B+source+%231',t:'0')),k:43.25889164598842,l:'4',n:'0',o:'',s:0,t:'0'),(g:!((g:!((h:compiler,i:(compiler:clang600,filters:(b:'0',binary:'1',commentOnly:'1',demangle:'0',directives:'0',execute:'1',intel:'0',trim:'1'),lang:c%2B%2B,libs:!(),options:'-std%3Dc%2B%2B17+-O3+-emit-llvm',source:1,wantOptInfo:'1'),l:'5',n:'0',o:'x86-64+clang+6.0.0+(Editor+%231,+Compiler+%231)+C%2B%2B',t:'0')),k:50.78855538287415,l:'4',m:50,n:'0',o:'',s:0,t:'0'),(g:!((h:compiler,i:(compiler:clang600,filters:(b:'0',binary:'1',commentOnly:'0',demangle:'0',directives:'0',execute:'1',intel:'0',trim:'0'),lang:c%2B%2B,libs:!(),options:'-std%3Dc%2B%2B17+-O3',source:1,wantOptInfo:'1'),l:'5',n:'0',o:'x86-64+clang+6.0.0+(Editor+%231,+Compiler+%232)+C%2B%2B',t:'0')),header:(),l:'4',m:50,n:'0',o:'',s:0,t:'0')),k:56.74110835401158,l:'3',n:'0',o:'',t:'0')),l:'2',n:'0',o:'',t:'0')),version:4), we can see that once again, the compiler is _magically clever_ enough to turn this into a switch, the very switch that matches our second optimization. I’m impressed.

### Further improvements

In both “optimized” versions of the code, we still have a case where we have to check against two different strings: “Battler” and “Jessica” have the same length, and “Battler” and “Beatrice” both start with “B”. If we had a case where two strings had the same initial character _and_ the same length, we’d be forced to do a general comparison, or move on to the _second_ character, or something like that. But sometimes we can do better, just from knowing something about our string data:

```
bool isOneOfTheStringsICareAbout(std::string_view s) {
  if (s.size() < 5) { return false; }
  switch (s[2]) { // NEW!
  case 't': return s == "Battler";
  case 'o': return s == "George";
  case 's': return s == "Jessica";
  case 'r': return s == "Maria";
  case 'a': return s == "Beatrice";
  default: return false;
  }
}
```

In this data set, every string is at least 3 characters long (actually, they’re all at least 5 characters long), and the third letter of each string is unique. So by testing the _third_ letter instead of the first, we can [immediately jump to only testing a single full string](https://godbolt.org/#g:!((g:!((g:!((h:codeEditor,i:(j:1,lang:c%2B%2B,source:'%23include+%3Cstring_view%3E%0A%0Abool+isOneOfTheStringsICareAbout(std::string_view+s)+%7B%0A++if+(s.size()+%3C+5)+%7B+return+false%3B+%7D%0A++switch+(s%5B2%5D)+%7B+//+NEW!!%0A++case+!'t!':+return+s+%3D%3D+%22Battler%22%3B%0A++case+!'o!':+return+s+%3D%3D+%22George%22%3B%0A++case+!'s!':+return+s+%3D%3D+%22Jessica%22%3B%0A++case+!'r!':+return+s+%3D%3D+%22Maria%22%3B%0A++case+!'a!':+return+s+%3D%3D+%22Beatrice%22%3B%0A++default:+return+false%3B%0A++%7D%0A%7D%0A'),l:'5',n:'0',o:'C%2B%2B+source+%231',t:'0')),k:43.25889164598842,l:'4',n:'0',o:'',s:0,t:'0'),(g:!((g:!((h:compiler,i:(compiler:clang600,filters:(b:'0',binary:'1',commentOnly:'1',demangle:'0',directives:'0',execute:'1',intel:'0',trim:'1'),lang:c%2B%2B,libs:!(),options:'-std%3Dc%2B%2B17+-O3+-emit-llvm',source:1,wantOptInfo:'1'),l:'5',n:'0',o:'x86-64+clang+6.0.0+(Editor+%231,+Compiler+%231)+C%2B%2B',t:'0')),k:50.78855538287415,l:'4',m:50,n:'0',o:'',s:0,t:'0'),(g:!((h:compiler,i:(compiler:clang600,filters:(b:'0',binary:'1',commentOnly:'0',demangle:'0',directives:'0',execute:'1',intel:'0',trim:'0'),lang:c%2B%2B,libs:!(),options:'-std%3Dc%2B%2B17+-O3',source:1,wantOptInfo:'1'),l:'5',n:'0',o:'x86-64+clang+6.0.0+(Editor+%231,+Compiler+%232)+C%2B%2B',t:'0')),header:(),l:'4',m:50,n:'0',o:'',s:0,t:'0')),k:56.74110835401158,l:'3',n:'0',o:'',t:'0')),l:'2',n:'0',o:'',t:'0')),version:4). Maybe in the future I’ll see if I can get a general function for this like I did for the initial optimizations, but that sounds a lot harder. I think I’ll save that for another day!

P.S. The LLVM project has generalized string-matching functionality in the form of the [`llvm::StringSwitch`](https://llvm.org/doxygen/classllvm_1_1StringSwitch.html) class. I tested that and it looks like it gets the switch-on-count optimization for free as well. So, LLVM folks, no need to run out and change everything to use `string_view`/`StringRef` directly!

1. If you’re on an older version of C++, you can find it as [`std::experimental::string_view`](http://en.cppreference.com/w/cpp/experimental/basic_string_view) instead. [↩︎](#fnref:17)

This entry was posted on [March](https://belkadan.com/blog/2018/03) 15, [2018](https://belkadan.com/blog/2018) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [C++](https://belkadan.com/blog/tags/cxx)
