---
title: One for the Unicode Nerds
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/06/one-for-the-unicode-nerds/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b5c705001870fb5f'
translated: false
---

> 原文：[One for the Unicode Nerds](https://oleb.net/blog/2014/06/one-for-the-unicode-nerds/)　·　Ole Begemann

# One for the Unicode Nerds

```
capitalism = "\u{1F1FA}\u{1F1F8}" # US flag
# => "🇺🇸"
opposite_of_capitalism = capitalism.reverse
# => "🇸🇺"
```

(This is Ruby code, but you could do the same in any language. **Update July 22, 2014:** Except in Swift, where the opposite of capitalism is just capitalism. [Because Swift is smart with strings](https://oleb.net/blog/2014/07/swift-strings/).)

The [lack of support](https://en.wikipedia.org/wiki/Regional_Indicator_Symbol) for a full set of [national flags](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#SU) in most emoji fonts kind of kills the joke, I know. It’s a shame.

I filed an [enhancement request with Apple to add more flags](http://www.openradar.me/radar?id=4747136218431488) to their emoji font. Feel free to do the same if you also want to see this.
