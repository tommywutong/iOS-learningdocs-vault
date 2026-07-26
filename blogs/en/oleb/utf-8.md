---
title: UTF-8
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/09/utf-8/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e012f8ccd59a4ef7'
translated: false
---

> 原文：[UTF-8](https://oleb.net/blog/2012/09/utf-8/)　·　Ole Begemann

# UTF-8

[UTF-8](https://en.wikipedia.org/wiki/UTF-8) is 20 years old this month. Today, UTF-8 is the [dominant character encoding on the web](https://googleblog.blogspot.com/2012/02/unicode-over-60-percent-of-web.html) and the basis for pretty much every new internet protocol or API. UTF-8 has some very unique features that have contributed to its success:

- It is backward-compatible with [ASCII](https://en.wikipedia.org/wiki/ASCII).
- It is very space-efficient for English and other Latin-based alphabets. That includes common control sequences such as HTML and XML tags, regardless of the document language.
- It does not have to deal with endianness (unlike [UTF-16](https://en.wikipedia.org/wiki/UTF-16)), and the byte order mark is optional.
- It is self-synchronizing, meaning the start byte of a character can be easily identified even in a partial data stream.
- Its unique binary signature makes it easy to autodetect UTF-8 encoding in code.

In short, UTF-8 is a pretty great design.

# Was it a good idea to make UTF-8 ASCII-compatible?

I do wonder about one of the design decisions, though: was it the right choice in hindsight to make UTF-8 backward-compatible with ASCII? At first glance, there is little reason to doubt this. After all, ASCII compatibility meant that many APIs that were written with ASCII in mind would work with UTF-8 strings with little or even no modification. That certainly helped adoption.

In addition, UTF-8-aware software could communicate with legacy ASCII-based code and the result, if not perfectly correct, would often be readable enough for users (at least for Latin-based alphabets). For example, a UTF-8-encoded e-mail that contained accented characters would still be understood by the recipient even if the receiving e-mail client did not understand UTF-8 and displayed it in ASCII or a similar encoding.

## Can lead to undiscovered bugs

On the other hand, that same benefit might have made the transition to a fully Unicode-aware software stack longer than necessary. Judging from my own experience, it took ages to rid software of most character encoding issues – in fact, the process is not even finished because we developers are constantly introducing new bugs. I suspect that UTF-8’s ASCII compatibility in particular has masked many bugs in text-handling code that was written in the last two decades.

The problem is that many developers (especially in the English-speaking world) only deal with ASCII characters all the time. As a consequence, I suppose many tend to test their UTF-8-aware software only with ASCII characters, too. Any encoding-related bugs are easily missed that way.

Now, if UTF-8 had a totally different mapping of characters to bytes for the first 127 characters, any mixup between UTF-8-encoded and ASCII-encoded text would be readily apparent.^[1](#fn:1) No-one would ever ship software that contained such a bug.

## Subtle changes can be dangerous

In the case of UTF-8, I think the creators made the right decision. The easier adoption outweighed the negative potential for new bugs.

However, I do believe we can take away a lesson from this example: the simple, subtle changes to an API are not always the best. Sometimes, it can be better to break backward compatibility in order to avoid confusion.

1. I realize that the developers of the UTF-8 standard followed the Unicode standard, which maps the ASCII characters one-to-one to the Unicode code points 0-127. While theoretically possible, it would have been awkward for UTF-8 to assign different byte codes to these characters while still retaining them in the 0-127 range. From that point of view, it may have been a good idea to apply this new ordering scheme directly to the underlying Unicode code points when the Unicode standard was created. [↩︎](#fnref:1)
