---
title: My Little (String) Optimization, Part 2
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2018/03/My-Little-String-Optimization-2/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:74b6037c75d921d0'
translated: false
---

> 原文：[My Little (String) Optimization, Part 2](https://belkadan.com/blog/2018/03/My-Little-String-Optimization-2/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [My Little Optimization: The Compiler Is Magic](https://belkadan.com/blog/2018/03/My-Little-Optimization/)

["FIXME" Doesn't Always Mean "Fix Me"](https://belkadan.com/blog/2018/04/FIXME/) »

« [My Little Optimization: The Compiler Is Magic](https://belkadan.com/blog/2018/03/My-Little-Optimization/?tag=cxx)

## [My Little (String) Optimization, Part 2](#)

[Previously](https://belkadan.com/blog/2018/03/My-Little-Optimization/), I talked about how Clang is smart enough to optimize a series of comparisons against constant strings in C++ by starting out with a switch on the length. I left off with the idea that while this is good, you might be able to do better if your strings have a unique character at a certain offset. Today we’re going to see what that looks like.more

Once again, the goal is to take something like this:

```
bool isOneOfTheStringsICareAbout(std::string_view s) {
  return isInSet(s, "Battler", "George", "Jessica", "Maria", "Beatrice");
}
```

and end up with generated code that looks like this:

```
bool isOneOfTheStringsICareAbout(std::string_view s) {
  if (s.size() < 5) { return false; }
  switch (s[2]) {
  case 't': return s == "Battler";
  case 'o': return s == "George";
  case 's': return s == "Jessica";
  case 'r': return s == "Maria";
  case 'a': return s == "Beatrice";
  default: return false;
  }
}
```

That is, we only want to write the name of each string once, and we don’t want to hardcode which offset to check. My idea for how to approach this went something like this:

1. is unique for every string.
2. where this is true.
3. do the comparison like last time, checking the

  th character.

The first step went smoothly. That code looks like this:

```
template <size_t I, size_t N>
__attribute__((always_inline))
static constexpr bool isUniqueCharacter(const char (&first)[N]) {
  return true;
}

template <size_t I, size_t N, size_t N2, size_t ...RestN>
__attribute__((always_inline))
static constexpr bool isUniqueCharacter(const char (&first)[N],
                                        const char (&next)[N2],
                                        const char (&...rest)[RestN]) {
  static_assert(I < N - 1, "too big");
  if (first[I] == next[I]) {
    return false;
  }
  return isUniqueCharacter<I>(first, rest...) &&
         isUniqueCharacter<I>(next, rest...);
}
```

This is a very silly algorithm that checks every string against every other string. If I wanted something that was going to be computed at run time, I’d do something cleverer, like setting bits in a 256-bit value, to see if there were any collisions. However, I’m still in the “getting something working” stages, and this is also going to run at compile-time anyway.

The next step was a little harder.

```
template <size_t I = 0, size_t ...Ns>
__attribute__((always_inline))
static constexpr size_t
uniquelyIdentifyingCharacter(const char (&...strs)[Ns]) {
  if constexpr (I + 1 >= std::min({Ns...})) {
    return std::string_view::npos;
  } else {
    if (isUniqueCharacter<I>(strs...)) {
      return I;
    } else {
      return uniquelyIdentifyingCharacter<I+1>(strs...);
    }
  }
}
```

If you just ignore that “`if constexpr`”, this function isn’t _too_ complicated. “If the index we’re trying to look at is at the end of any of the strings, give up and return `npos`. Otherwise, if it’s a unique index, great! And finally, try the next index.”

So what’s the `if constexpr` for? That’s [a C++17 feature](https://blog.tartanllama.xyz/if-constexpr/) that makes sure the compiler only looks at one branch of the `if`. And that’s important because of that `static_assert` we had back in `isUniqueCharacter`—without `if constexpr`, the compiler would try to generate `isUniqueCharacter<I>` even if `I` was well out of bounds. Heck, it would try to generate `uniquelyIdentifyingCharacter<I+1>` too—recursion with no base case!

There are ways in earlier versions of C++ to deal with this, but they’re all clunkier and I always have to look up how they work. `if constexpr` just lets me write the condition I want, as long as it really is a constant expression.

What I _really_ wanted to do with `uniquelyIdentifyingCharacter` was `static_assert` if there’s no unique character offset for the strings that get passed in. Unfortunately, that would require making the _second_ `if` into `if constexpr`, so that we could avoid recursing. That doesn’t work because arguments can’t be used in constant expressions, even if the arguments are going to be constant whenever we use this function. So I had to return a placeholder value, [`std::string_view::npos`](http://en.cppreference.com/w/cpp/string/basic_string_view/npos) instead.

Anyway, this function works too! So now to just plug it in to the original `isInSet` from the first post:

```
__attribute__((always_inline))
static bool isInSetImpl(std::string_view s, size_t offset) {
  return false;
}

template <size_t N, size_t ...RestN>
__attribute__((always_inline))
static bool isInSetImpl(
    std::string_view s,
    size_t offset, // NEW!
    const char (&first)[N], // "reference to array of size N"
    const char (&...rest)[RestN] // "a bunch more references to arrays"
) {
  if (s[offset] == first[offset]) { // NEW!
    if (s == first) {
      return true;
    }
  }
  return isInSetImpl(s, offset, rest...);
}

// NEW!
template <size_t ...Ns>
__attribute__((always_inline))
static constexpr bool isInSet(
  std::string_view s,
  const char (&...strs)[Ns]
) {
  if (s.size() < std::min({Ns...}) - 1) {
    return false;
  }
  size_t offset = uniquelyIdentifyingCharacter(strs...);
  assert(offset != std::string_view::npos &&
         "no uniquely identifying character");
  return isInSetImpl(s, offset, strs...);
}

bool isOneOfTheStringsICareAbout(std::string_view s) {
  return isInSet(s, "Battler", "George", "Jessica", "Maria", "Beatrice");
}
```

And, well, hm. This does compile, and is even smart enough to only load the one character (the third letter of each name is unique), but it looks like Clang wants to make it into a [series of `if`s instead](https://godbolt.org/#z:OYLghAFBqd5QCxAYwPYBMCmBRdBLAF1QCcAaPECAKxAEZSAbAQwDtRkBSAJgCFufSAZ1QBXYskwgA5NwDMeFsgYisAag6yAwkwbAShBAFsN2DgAYAgnIVKVmdVsEFiC4AH0AbnkwB3E%2BasueUVlNQ1NZCZBQUxiAn9LAIJMQwAHZmSHTUE8AC9MNwJVAElSVRz8wtUAOQSLNzcmAmc8ACMRZIaoHR8mAE9BNwUGBUwASjGApya8ZFU0FidMAA9U4lVW1FQGVTxBAFUWPABHEUxNBCZiJmRk4ggFp3nL9YhuADYAMzxiJ0mAVh4tX%2BABExuoAOw8VTETAEMQsVTOM4aaEcCEggJJFLpJr2cIVApFUrlPJEmplQlVapcSlkqoAOiZACVME5arJTJYGk0Wu1Om5ugxegMhiwRixxpNLNMCLN5qhFslVutNttdgcjqdzi8bncHoqnsgXqo3lwvj8/hxAcCQaQAqpHU7nS7XW73c7HkVjVdTR9JcsCACgVxrXaHR7I1GPV7nr6ze8mQzYVbAaz2WHwei%2BJZHbLZo1orECBBilkaqoALSqejqLhcIioDZ4YDcLiTWQ5iyOvCfU3fX7xQHFMMOTGyEGqANDngj0FZqERx2w%2BHERGfHQxVER9GY3MwuEIjWHE5nC5XPWxcIjzkQAdOMopghJrPmj5L117E/a8/XW5XrQb2wCBp0fNlnyZDsu13HdLGSNIMnxRx6WJMdVDMOlKiKJNqkEOoeWaFx%2BQKQUIB6fpBmGUYJimAgZjmL0VjWUksNUEQtTOBg%2BmKLAWDlT4%2BlcX9L3uWMfVeD4kycX5g1wzNIS7Hs%2B0YlVTTLfgawcUwJ3KAh0BAEBDAUN4oVwpNdwmBSPxXI8nH0kBpNcTxvB8AyWFSVA8M7HcMVUTAGBiKz9yU00vw4nUL3/YhrxMCBpMEF8F0Ul0bLXEpt2CyE927J1UsRdjT387jeP4wS2GEqKYt4WhYvil8MpymDEgxAICL5DoSKFEVKPFajpQsfM5jVHY9mKFgAGU4WKBC4r0gzHLYZzfHKTDyVQT5PhiIMgpyvLVA3ALMAapqrDgnFEKyKkimqVbGRZcCOS5epGkItoOq6MjhQosUJSlWj6I2LYRsEMbJoIab0jeTK7PmlpFq8ZbBHtaGUNUdbNrhMoAHosZqbAAHUwDAD8xJNBN7yDa0gTDbHcbbWFPliTBFHsIhVCua4%2BjRvtCRqNsScNb0yckpkn2DdMCFtVQcbrLgmA2djjVUQwSHsBmmZZwQkSbDmKP5ywkojXtTTwwF0a20cNHHScKap824Xk7Npdx6oCaJj9jbiscrf2y1tuzD9l0PNLkSO7zMpOx1I%2Bd1RWWQMQckVInVHxgw0clVQGDZLWrmAERDGZggygIBA9iRPAC/M/c9tGiappmpHuYxouDycerw6sFrEksGXXcJ4mzoQvFLtRnCvKetqiPe0jyNFKjJRomU6LlIagY1UG4Vm%2ByFvcBGfBWhUlTjCTzSk5xBFk02wR2kK4oZQkICzLRdPsoyWBMoEEqZCyqxrQ3Mr2gdLcHco5dxyldJuW00IFW1FxHihdexlWABVfUdVIINUdFEGIcQID2yKO7HSMMHJw13i5NyHktbvjfJlF0bYWBNhgZxLmeASqINcMfESbYoIRhriDOu4MG5lDwZSc%2B7doJgICMNDUAB5SU0jPgABUECYHGiQkG2hYQWE2B0LesMXDwxcuUf%2Bu1g6IlrmDOKZQ2w8F5FnaK9YrH1gAOKYBIMAI6DjZYACls6zCYG2RxXAACyVw8D%2BM8dYzATQXASC4cdMBUgxiMGkP8KQpAWDSDMGk1A0hND8A0sIMQEg6yyFoGkggmTElJIANYgAACyyAZFwf4AAOFpABOWg7w6n/HaW0uptIGDSDqWkjJUgsmkByVINJggQAYQqeMxJpA4CwBgIgFAqA0h4DseQSgaAtl2JQMwNg7wzAYW%2BAwO4syICtEqaQVoCgrh9GkGU0g%2ByC58VkVxF5aSsCGFYMALOdz8CwluHgDwbI7krEwPHZIPzyB8X8nclohgflJOOewfJvBGBtFmZAJJqBUhykNNISsdkracF4PwWgEIqzSNkFWFIhBKwMAYB4QwMzRDiEkPQXonyiVjU%2BFMsp6KUmjLuVM5YLT3iVm6fMDFqhExmAZGYU0uBCAkBKbWTQmzUjbNiFq8EeSqW8HKZUiYpBan/GVRCNp/x7WyBaVwFpEI6m0H%2BMkqQIzSCoutekiV0gZlzNIAsrJSSVnrP2XqnZFADQHNiEcgFpzznbKuZQW5iz7mPOIM8qQrz3mFy%2BbmiZfyAVAszSCmFcoIWzMzdC2Fkg81pIUMkIZmaUXmsYAClAWKBAjFaHix%2BkyiV4BJVIMlekKW9ppXS2QnKik8tIHygg0iBUsCFWiz1qT/WZsldK2VdT5UAsVSqlVar8BEHWHIbVur9VXqCO2VQxq%2BCmpDeapJyimBYGIJQUVXq0m%2BowmMiZUyg3zPfZakA/xEyutoLQMwLTZD/DqWYODrTPVzp3SBwNb7FkWrbVwcVu6cOhqqaQCFvxR0ZLqUAA).

I’ll pause at this point to say _a series of ifs isn’t bad._ Unlike before, where the chain of ifs tested the size but might have to fall back to comparing the whole string, this time we’re just checking the single unique character. That’s something that a CPU can race through pretty quickly without touching memory or calling a function or anything.

But the goal of this exercise was to get something that looked like a switch, so I decided to go further. What if I held off on doing the full string comparison until the end?

```
// NEW!
__attribute__((always_inline))
static constexpr std::string_view findPossibleMatch(
  char otherChar,
  size_t offset
) {
  return std::string_view();
}

// NEW!
template <size_t N, size_t ...RestN>
__attribute__((always_inline))
static constexpr std::string_view findPossibleMatch(
    char searchChar,
    size_t offset,
    const char (&first)[N],
    const char (&...rest)[RestN]
) {
  if (searchChar == first[offset]) {
    return std::string_view(first, N-1);
  }
  return findPossibleMatch(searchChar, offset, rest...);
}

template <size_t ...Ns>
__attribute__((always_inline))
static constexpr bool isInSet(
  std::string_view s,
  const char (&...strs)[Ns]
) {
  if (s.size() < std::min({Ns...}) - 1) {
    return false;
  }
  size_t offset = uniquelyIdentifyingCharacter(strs...);
  assert(offset != std::string_view::npos &&
         "no uniquely identifying character");
  // NEW!
  std::string_view possibleMatch =
      findPossibleMatch(s[offset], offset, strs...);
  return s == possibleMatch;
}

bool isOneOfTheStringsICareAbout(std::string_view s) {
  return isInSet(s, "Battler", "George", "Jessica", "Maria", "Beatrice");
}
```

And _this_ code ends up compiling to something interesting. Rather than a switch, [it generates code that does something like this](https://godbolt.org/#z:OYLghAFBqd5QCxAYwPYBMCmBRdBLAF1QCcAaPECAKxAEZSAbAQwDtRkBSAJgCFufSAZ1QBXYskwgA5NwDMeFsgYisAag6yAwkwbAShBAFsN2DgAYAgnIVKVmdVsEFiC4AH0AbnkwB3E%2BasueUVlNQ1NZCZBQUxiAn9LAIJMQwAHZmSHTUE8AC9MNwJVAElSVRz8wtUAOQSLNzcmAmc8ACMRZIaoHR8mAE9BNwUGBUwASjGApya8ZFU0FidMAA9U4lVW1FQGVTxBAFUWPABHEUxNBCZiJmRk4ggFp3nL9YhuADYAMzxiJ0mAVh4tX%2BABExuoAOx8SyqVTETAEMQsVTOM4aaFWCEggJJFLpJr2cIVApFUrlPIkmplYlVapcakUqoAOhZACVME5arJTJYGk0Wu1Om5ugxegMhiwRixxpNLNMCLN5qhFslVutNttdgcjqdzi8bncHsqnsgXqo3lwvj8/hxAcCQaQArDnS7XW73R7XY8iqaruaPtLlgQAUCuLaHU7PVHo57vc8/Rb3iymfCbYD2Zzw%2BCOFDI/LZo1orECBBilkaqoALSqejqLhcIioDZ4YDcLiTWQY2F4T7m76/eKA4rhhzY2Qg1SBwc8Yeg7O5mHO%2BGI4jIz46GLoyM57GL5dIrWHE5nC5XA2xcLD7kQftOMqpgjJ7OWj6R917I%2B60/XW4XrRX7AICne8OUfFkOwxHdt0sZI0gyQlHEZUlR1UMwGUqIpk2qQQ6j5ZoXEFAphQgHp%2BkGYZRgmKYCBmOZvRWNZyQw1QRB1M4GD6YosBYBVPj6Vxv3Pe4419V4PmTJxfhDbCs0hLtdl7ei1XNMt%2BBrBxTHHcoCHQEAQEMBQ3ihbDkx3CY5LfOEEQPJxdJASTXE8bwfD0lhUlQHDO23LFVEwBgYgsxdu17CAPzYvUz1/YhLxMCBJMEJ953kl191XEotyCyFdwsFLrLS1jjz8zjuN4/i2EEqKYt4WhYvip8MpyrKcSxHFLAAejampsAAdTAMAAjwgUOiIkUxXIyVKNlCx8zo41VUY2y9IctgnN8VRvhYdAAAUPJyVoGEwABZJpTTeRdRNUVACAQWJv0dRcaSKVBPk%2BGJ4ksJLI1S5FFvsloVq8XwIAg5rsoCDqut6/qYLxeCskeqkmMpZMMwILkeXqRp8LaYauhI0UyIlKUZWo2ilRVBj1l%2B5b3EBnx1oUbbdraA7joIU7LIumIrlNO7LIR57XoRe7GthESzUTW9g1tIFwxFl1xYTcSWQfENUftAJPsXHtzW58QEG/UcNAnKWZcFt7ZJzZKrJXH6dKW/7aecm9rQIMpqkrWgQcXKC9zytdGZ26IWaOk6EDizAeYNl4ynN4WrKceqvMSFrEjTiwIeqHq%2BtxOCCXhpDVCwzyMcGgjceI0jxQo6UqLlGiFTmDUdj2YoWAAZQROL7b%2BlwAec8oykVsTLQk5xBGknC50CxqdbipliWB8tfoMlgjKBBKWTMqsay10WbYPdd/MwBrYV9xqBZet6UIK3UOK4zAeJ7MrgAqw06vA0/VCiGI4ggOOig5y0tTR2q0XIgDch5Os7xXyZVdG2FgTZb7sT6LsEqz9XDxh/HcNs3sL49xpmA1Q7lg77VDuzBARs4EM02kHParMw5xTNlfBEctLosLdtpX4Sd5LfXKEbLSJD6HkNNA1c%2BARm5agAPLSikZ8AAKjddujtBDFG0PCCwmwOjdzsoQum5Q96wj4a3DuXdBBlDbDwfkB1or1gsfWAA4pgEgwAT52LrFwAAUhyHIkQ2z2K4MdFwTB/EeJ4JHFoEhcFiNThYKQYxGDSH%2BFIUgLBpBmBSagaQmh%2BBqWEGICQdZZC0BSQQdJ8SEkAGsQAABZZBMi4P8AAHE0gAnLQd4NT/itJaTU%2BkDBpA1JSWkqQGTSBZKkCkwQIA0JlNGfE0gcBYAwEQCgVAaQ8A2PIJQNAGybEoGYGwd4Zg0LfAYHcaZEBWjlNIK0BQVw%2BjSBKaQXZhhH4EBkRxJ5KSsCGFYMAA6Nz8DwluHgDwHIbkrEwMgYa3zyA8T8jclohhvkJMOewXJvBGBtGmZABJqBUgKmNNISstljacF4PwWgEIqxSNkFWFIhBKwMAYB4QwUzRDiEkPQXoPEpGErbp8CZJS0VJOGTciZywmnvErJ0%2BY6LVBJjMEyMw5pcCEBIEU2smh1mpE2bELV4IcmUt4KU8pExSDVP%2BMqiELT/j2tkE0rgTSIQ1NoP8RJUghmkBRda1JErpBTJmaQOZGSElLNWbsvVWyKBGj2bEA5/zjmnM2Rcyg1z5m3PucQR5UhnmvPeZ83NYzfn/MBZm4F0KFTgumZmqFMLkhwoUMkAZmbkXmsYP8lAmKBAjFaLi4G4zCV4GJVIUlOlyU9upbS2QHKCnctILyj5AqWBCtRZ65J/rM2SulbKmp8r/mKpVSqtV%2BAiDrDkNq3V%2BqL1BHbKoY1fBTUhvNQkm6TAsDEEoKKr1KTfVoRGWMiZQbZmvstSAf4SZXW0FoGYJpsh/g1LMDB5pnrZ1bqA4Gl98yLWtq4OK7dWHQ0VNIOC34I60k1KAA):

```
std::string_view stringsICareAbout[] = {
  "Battler",
  "George",
  "Jessica",
  "Maria",
  "Beatrice"
};
size_t index = determineIndexFromOffsetCharacter(s, offset);
return stringsICareAbout[index] == s;
```

Which brings us to an insightful comment by my coworker [David Smith](https://twitter.com/Catfish_Man/) on the _last_ post: trying to find a single byte that uniquely identifies the entire string is a specific instance of trying to find a [perfect hash function](https://en.wikipedia.org/wiki/Perfect_hash_function). If `determineIndexFromOffsetCharacter` really existed, that’s what it would be doing: “if this value is in the set of strings I care about, here’s where it would be”.

In practice the compiler isn’t _exactly_ doing `determineIndexFromOffsetCharacter`; instead, it just makes a table with some extra slots in it and…I’m actually not quite sure how it works, it might be doing an unnecessary comparison if the length is the same as one of the other strings. Still, it only ever does one full string comparison, which was the original goal.

It turns out this is incredibly order-dependent: if we put “Beatrice” first [we actually do get a `switch`](https://godbolt.org/#z:OYLghAFBqd5QCxAYwPYBMCmBRdBLAF1QCcAaPECAKxAEZSAbAQwDtRkBSAJgCFufSAZ1QBXYskwgA5NwDMeFsgYisAag6yAwkwbAShBAFsN2DgAYAgnIVKVmdVsEFiC4AH0AbnkwB3E%2BasueUVlNQ1NZCZBQUxiAn9LAIJMQwAHZmSHTUE8AC9MNwJVAElSVRz8wtUAOQSLNzcmAmc8ACMRZIaoHR8mAE9BNwUGBUwASjGApya8ZFU0FidMAA9U4lVW1FQGVTxBAFUWPABHEUxNBCZiJmRk4ggFp3nL9YhuADYAMzxiJ0mAVh4tX%2BABExuoAOx8SyqVTETAEMQsVTOM4aaFWCEggJJFLpJr2cIVApFUrlPIkmplYlVapcakUqoAOhZACVME5arJTJYGk0Wu1Om5ugxegMhiwRixxpNLNMCLN5qhFslVutNttdgcjqdzi8bncHsqnsgXqo3lwvj8/hxAcCQaQArDnS7XW73R7XY8iqaruaPtLlgQAUCuLaHU7PVHo57vc8/Rb3iymfCbYD2Zzw%2BCOFDI/LZo1orECBBilkaqoALSqejqLhcIioDZ4YDcLiTWQY2F4T7m76/eKA4rhhzY2Qg1SBwc8Yeg7O5mHO%2BGI4jIz46GLoyM57GL5dIrWHE5nC5XA2xcLD7kQftOMqpgjJ7OWj6R917I%2B60/XW4XrRX7AICne8OUfFkOwxHdt0sZI0gyQlHEZUlR1UMwGUqIpk2qQQ6j5ZoXEFAphQgHp%2BkGYZRgmKYCBmOZvRWNZyQw1QRB1M4GD6YosBYBVPj6Vxv3Pe4419V4PmTJxfhDbCs0hLtdl7ei1XNMt%2BBrBxTHHcoCHQEAQEMBQ3ihbDkx3CY5LfOEEQPJxdJASTXE8bwfD0lhUlQHDO23LFVEwBgYgsxdu17CAPzYvUz1/YhLxMCBJMEJ953kl191XEotyCyFdwsFLrLS1jjz8zjuN4/i2EEqKYt4WhYvip8MpyrKcSxHFLAAejampsAAdTAMAAjwgUOiIkUxXIyVKNlCx8zo41VUY2y9IctgnN8VRvhYdAAAUPJyVoGEwABZJpTTeRdRNUVACAQWJv0dRcaSKVBPk%2BGJ4ksJLI1S5FFvsloVq8XwIAg5rsoCDqut6/qYLxeCskeqkmMpZMMwILkeXqRp8LaYauhI0UyIlKUZWo2ilRVBj1l%2B5b3EBnx1oUbbdraA7joIU7LIumIrlNO7LIR57XoRe7GthESzUTW9g1tIFwxFl1xYTcSWQfENUftAJPsXHtzW58QEG/UcNAnKWZcFt7ZJzZKrJXH6dKW/7aecm9rQIMpqkrWgQcXKC9zytdGZ26IWaOk6EDizAeYNl4ynN4WrKceqvMSFrEjTiwIeqHq%2BtxOCCXhpDVCwzyMcGgjceI0jxQo6UqLlGiFTmDUdj2YoWAAZQROL7b%2BlwAec8oykVsTLQk5xBGknC50CxqdbipliWB8tfoMlgjKBBKWTMqsay10WbYPdd/MwBrYV9xqBZet6UIK3UOK4zAeJ7MrgAqw06vA0/VCiGI4ggOOig5y0tTR2q0XIgDch5Os7xXyZVdG2FgTZb7sT6LsEqz9XDxh/HcNs3sL49xpmA1Q7lg77VDuzBARs4EM02kHParMw5xTNlfBEctLosLdtpX4Sd5LfXKEbLSJD6HkNNA1c%2BARm5agAPLSikZ8AAKjddujtBDFG0PCCwmwOjdzsoQum5Q96wj4a3DuXdBBlDbDwSOLQJBtgsfWHg/IDrRXrPYrgABxTAJBgAn1cXWLgAApDkORIh2P8cdFwTBcFiNThYKQYxGDSH%2BFIUgLBpBmBSagaQmh%2BBqWEGICQdZZC0BSQQdJ8SEkAGsQAABZZBMi4P8AAHE0gAnLQd4NT/itJaTU%2BkDBpA1JSWkqQGTSBZKkCkwQIA0JlNGfE0gcBYAwEQCgVAaQ8DOPIJQNAGznEoGYGwd4Zg0LfAYHcaZEBWjlNIK0BQVw%2BjSBKaQXZhhH4EBkRxJ5KSsCGFYMAA6Nz8DwluHgDwHIbkrEwMgYa3zyA8T8jclohhvkJMOewXJvBGBtGmZABJqBUgKmNNISstljacF4PwWgEIqxSNkFWFIhBKwMAYB4QwUzRDiEkPQXoPEpGErbp8CZJS0VJOGTciZywmnvErJ0%2BY6LVBJjMEyMw5pcCEBIEU2smh1mpE2bELV4IcmUt4KU8pExSDVP%2BMqiELT/j2tkE0rgTSIQ1NoP8RJUghmkBRda1JErpBTJmaQOZGSElLNWbsvVWyKBGj2bEA5/zjmnM2Rcyg1z5m3PucQR5UhnmvPeZ83NYzfn/MBZm4F0KFTgumZmqFMLkhwoUMkAZmbkXmsYP8lAmKBAjFaLi4G4zCV4GJVIUlOlyU9upbS2QHKCnctILyj5AqWBCtRZ65J/rM2SulbKmp8r/mKpVSqtV%2BAiDrDkNq3V%2BqL1BHbKoY1fBTUhvNQkm6TAsDEEoKKr1KTfVoRGWMiZQbZmvstSAf4SZXW0FoGYJpsh/g1LMDB5pnrZ1bqA4Gl98yLWtq4OK7dWHQ0VNIOC34I60k1KAA). Clearly the compiler thinks it should make different tradeoffs in the two different cases! I haven’t dug into why this is, but it’s something related to the last case getting used as a default instead of the empty `string_view` written in the source.

Anyway, that’s enough for now. As another coworker [David Ungar](https://twitter.com/senderPath/status/974685102809600002) pointed out, this sort of optimization depends on a lot more than just eyeballing the code that gets generated. But once again, it’s cool how much compilers can do these days.

…

Okay, okay, one more thing. You’ll notice I’ve been sneaking `constexpr` into all of these helper functions, meaning that if all the arguments are compile-time constants, the result should be too. And it turns out that if I mark `isOneOfTheStringsICareAbout` `constexpr` as well, _this actually works:_

```
static_assert(isOneOfTheStringsICareAbout("Beatrice"),
              "Beatrice is important");
static_assert(!isOneOfTheStringsICareAbout("Ange"),
              "Apparently Ange is not?");
```

…at least when using [libc++](https://libcxx.llvm.org), which marks up enough of `string_view` as `constexpr` to use in constant expressions like this. Pretty cool, right?

This entry was posted on [March](https://belkadan.com/blog/2018/03) 22, [2018](https://belkadan.com/blog/2018) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [C++](https://belkadan.com/blog/tags/cxx)
