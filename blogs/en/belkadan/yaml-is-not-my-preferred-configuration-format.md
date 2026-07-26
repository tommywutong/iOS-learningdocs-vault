---
title: YAML is (not) my preferred configuration format
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2026/03/YAML-Is-Not-My-Preferred-Configuration-Format/'
original_language: en
published: 2026-03-17
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e696826bb5cc90a7'
translated: false
---

> 原文：[YAML is (not) my preferred configuration format](https://belkadan.com/blog/2026/03/YAML-Is-Not-My-Preferred-Configuration-Format/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [What's in a Button?](https://belkadan.com/blog/2025/11/Whats-in-a-Button/)

« [Protobuf Is Almost Streamable](https://belkadan.com/blog/2023/12/Protobuf-Is-Almost-Streamable/?tag=encoding)

## [YAML is (not) my preferred configuration format](#)

Sometimes you have configuration files or simple data files that you want to maintain by hand, in a text editor. There are dozen of reusable formats for this, but only a few of them really support _hierarchical_ entries. You can argue that configuration files should stay relatively flat, but if you eventually run into a situation where you _need_ hierarchy, you’ll be unhappy not to have it.

These days, the starting point for such a file is probably something like [JSON](https://www.json.org), at least if you need hierarchy. Everyone can parse it, since it’s used as a program-program interchange format, and its model matches the natural nesting of structs in many languages. Its type system is maybe not ideal, but it’s “good enough” for most use cases.

```
{
  "user": "jrose",
  "showDevTools": true,
  "bookmarks": [
    "https://signal.org",
    "https://swift.org",
    "https://belkadan.com"
  ],
  "accounts": {
    "@jrose": {
      "description": "main account"
    },
    "@rokkenjima_radio": {
      "description": "side project"
    }
  }
}
```

What it’s not great at is being written by humans. Having to quote all the keys feels unnecessary, not allowing trailing commas makes diffs non-uniform, and most frustratingly there’s no comment syntax. All of these are fixed in a format called [JSON5](https://json5.org), and if you want you can just go switch your JSON to JSON5 immediately (assuming it’s available in your environment).

```
{
  user: "jrose",
  showDevTools: true,
  bookmarks: [
    // Current employer
    "https://signal.org",
    // Past project
    "https://swift.org",
    // Personal site
    "https://belkadan.com",
  ],
  accounts: {
    "@jrose": {
      description: "main account",
    },
    "@rokkenjima_radio": {
      description: "side project",
    },
  },
}
```

But if you’re no longer trying to be the strict JSON that’s supported everywhere, why stop there? JSON5 syntax is still noisier than it needs to be. If we use indentation and list markers to describe the same hierarchies, we end up with a syntax that’s basically as simple as the flat formats when we don’t need hierarchy, but smoothly allows nesting and collections when we do.

```
user: "jrose"
showDevTools: true
bookmarks:
  # Current employer
  - "https://signal.org"
  # Past project
  - "https://swift.org"
  # Personal site
  - "https://belkadan.com"
accounts:
  "@jrose":
    description: "main account"
  "@rokkenjima_radio":
    description: "side project"
```

That’s my favored configuration format, at least at this time. Unfortunately, that’s not what [YAML](https://yaml.org) is. YAML _does_ support all of that, although you might have noticed its comment syntax is different from JSON5’s, but the problem is it _also_ supports a zillion other things:

- Values can be unquoted, not just keys
- Keys can be anything, not just strings
- YAML 1.1 specified [several unquoted ways to write booleans](https://yaml.org/type/bool.html) (and other types), not just `true` and `false`. 1.2 and later (from 2009!) are stricter, but unless either the parser or the document specifically says it wants to be YAML 1.2, you might not be in that mode. If you want a consistent rule, you need to quote all your strings all the time, _including your keys._ (Even without this, knowing whether a string needs to be quoted is a bit murky.)
- YAML isn’t just for object _trees;_ it actually supports object _graphs_ with “anchor” and “alias” syntax. How does your YAML parser fare when your data types weren’t expecting recursion?
- YAML has a syntax for putting multiple top-level documents in one file. I won’t deny this is useful! But once again, what does your YAML parser do with it?
- Finally, YAML allows attaching an arbitrary type tag to _every node._ So much for a simple data structure! And if your parser blithely uses these tags to direct deserialization, you now have a potential vulnerability in your program, depending on what you were using the YAML for.
- YAML also has some complicated ways to write multiline strings but honestly I don’t mind that one so much—it doesn’t get in the way of “normal” use, and your data model doesn’t have to know about it.

All of these have reasons for existing, and in fact I think I have had occasion to use all of them throughout my career. But it also means YAML’s not a “simple” format by any means, and that means it’s prone to mistakes and misuse…and it’s going to be overkill for configuration files. Even hierarchical ones.

So my favorite configuration format is not, in fact, YAML. It’s a hypothetical subset of YAML that’s just JSON, but nicer to write. And that, unfortunately, does not exist.

---

The format I’d actually recommend today is probably [TOML](https://toml.io), because TOML 1.1 also basically turns back into “nicer JSON” once you get more than one level of nesting (assuming you want to keep the visual indication of nesting).^[1](#fn:pygments)

```
user = "jrose"
showDevTools = true
bookmarks = [
  # Current employer
  "https://signal.org",
  # Past project
  "https://swift.org",
  # Personal site
  "https://belkadan.com",
]

[accounts]
"@jrose" = {
  description = "main account",
}
"@rokkenjima_radio" = {
  description = "side project",
}
```

TOML is Fine. Not quite as nice for nesting structures inline, even if it has other syntax to compensate. It is weird to me that it has dates and times as built-in formats, particularly _local_ dates and times. And its features to incrementally build up an object (“table”) or array of tables make it a little more complicated and introduce some new kinds of possible errors. But it’s probably a safer choice these days than YAML or some bespoke YAML subset library.

I will note that one reason you might be uncomfortable using TOML is that “Tom” is Tom Preston-Werner, formerly CEO of GitHub, who specifically resigned because he and his wife were [harassing an employee](https://techcrunch.com/2014/03/15/julie-ann-horvath-describes-sexism-and-intimidation-behind-her-github-exit/). But Preston-Werner hasn’t been directly involved in TOML for years, and I don’t feel like using TOML today is giving him much power, which is what I care about. (Nor, for posterity, have I seen any complaints about him that made the news since the mess in 2014.)

1. At the time of publishing, my highlighter, [pygments](https://pygments.org), didn’t know that TOML 1.1 added multi-line inline tables, so it marked that syntax as an error. If you’re reading this in the future, though, that may have been fixed by me updating locally and rebuilding the site. [↩︎](#fnref:pygments)

This entry was posted on [March](https://belkadan.com/blog/2026/03) 17, [2026](https://belkadan.com/blog/2026) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Encoding](https://belkadan.com/blog/tags/encoding)
