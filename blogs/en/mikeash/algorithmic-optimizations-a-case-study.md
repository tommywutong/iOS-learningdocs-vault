---
title: 'Algorithmic Optimizations: a Case Study'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/algorithmic-optimizations-a-case-study.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:00e3b5369e45327d'
translated: false
---

> 原文：[Algorithmic Optimizations: a Case Study](https://www.mikeash.com/pyblog/algorithmic-optimizations-a-case-study.html)　·　mikeash.com Friday Q&A

Posted at 2007-11-26 01:08 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Leopard: First Impressions](https://www.mikeash.com/pyblog/leopard-first-impressions.html)  
Previous article: [Perform Better With Garbage Collection](https://www.mikeash.com/pyblog/perform_better_with_garbage_collection.html)  
Tags: [c++](https://www.mikeash.com/pyblog/?tag=c%2B%2B) [casestudy](https://www.mikeash.com/pyblog/?tag=casestudy) [performance](https://www.mikeash.com/pyblog/?tag=performance) [stl](https://www.mikeash.com/pyblog/?tag=stl)

Algorithmic Optimizations: a Case Study

by [Mike Ash](https://www.mikeash.com/)

I've been working on a little project that needed a dictionary file format. This file format was intended to be something that could be memory mapped and searched efficiently without having to access most of the file for any individual search. In order to allow the rest of the file to store constant-size records and make it easier to work with, I moved all of the strings into a separate string table which is stored at the end of the file.

In order to reduce storage requirements, this string table is treated as a big blob, and strings are indicated using a pointer and a length, so that storage can be shared between longer strings and their substrings. Here's an example:

```
        "Renew my books."    "book"
        offset 42 length 15  offset 51 length 4
                     |        |
                     v        v
    ...a little lamb.Renew my books.Frog blast the...
                       ^   ^
                       |   |
                       |  "my"
                       |  offset 48 length 2
                       |
                    "new"
                    offset 44 length 3
```

These offset/length pairs are stored throughout the file to indicate strings. When a string is loaded, the offset and length are used to load it out of the string table. This arrangement is very simple for the reader.

It's a lot more complicated for the string table generator, though. It's easy to make a naive generator which just writes the strings one-by-one and generates the offsets for each one, but it's much harder to write a smart generator which makes good use of shared storage for substrings.

The basic algorithm for the generator which I decided to use was this:

```
    addString(str)
        get offset of blob in str
        if offset does not exist
            offset is current length of blob
            append str to end of blob
```

By sorting the strings by length from largest to smallest, it's guaranteed that any string which is a substring of another string will be able to share storage. Storage can also be shared across string boundaries but it's less likely to happen, so I didn't put any effort into optimizing the arrangement of the blob for that.

This algorithm is pretty straightforward, but the "get offset of blob in str" line is the killer. The obvious technique would be to use a function like `strstr()` or, since this was sometimes using non-ASCII (UTF-16) data, `memmem()`.

Of course one problem is that there is no `memmem()` function in the standard C library. Not to fear, I'll just write my own:

```
static const void *memmem( const void *big, size_t biglen,
                           const void *small, size_t smalllen )
{
	if( smalllen > biglen )
		return NULL;
	
	size_t offset = 0;
	while( offset <= biglen - smalllen )
	{
		if( memcmp( big + offset, small, smalllen ) == 0 )
			return big + offset;
		offset++;
	}
	return NULL;
}
```

Of course some of the more perceptive readers out there might notice that the performance of this function totally blows. In fact it was too slow to build a dictionary of any reasonable size in any reasonable amount of time, so I started looking around for better ways.

The first better way I tried was using the C++ STL's [search algorithm](http://www.sgi.com/tech/stl/search.html). When given a `char *` it works almost exactly like `memmem()`. Performs almost exactly like it too. It's too general to be able to use a better algorithm so the only performance gain came from being able to inline all those pesky `memcmp()` calls. I went searching further.

(I can hear you screaming back there. Yes, you in the last row. The one constantly yelling, "Use Boyer-Moore!" I heard you the first time you said it. Just sit down and be patient, I'm getting there.)

After asking around a little, I found out that the standard algorithm for these searches is called the [Boyer-Moore string search algorithm](http://en.wikipedia.org/wiki/Boyer-Moore_string_search_algorithm). This algorithm uses some ridiculously clever ideas to skip over large portions of the string being searched so that the running time doesn't get worse the longer the smaller string is. In fact it tends to perform better the longer it is. I even found a [very nice implementation](http://srcvault.scali.eu.org/cgi-bin/Syntax/Syntax.cgi?BoyerMoore.c) of this algorithm under very generous terms of use, so I grabbed it and used it in place of my `memmem()` function.

And speed was attained! The new algorithm made it practical to build larger dictionaries. I started working with a data set that produced about 6MB of output and it took around ten minutes to build. It was slightly annoying when I discovered a bug and had to rebuild it, but it was entirely doable.

A little later I started working with a data set that produced about 24MB of output and its running time returned to being essentially impossible. It took over an hour and a half just to build the string table, and a couple of minutes more to parse the file and build the rest of the output, and I kept discovering bugs in the parser that only showed up _after_ I used it to build the file, so the turnaround time was getting to be somewhat insane. I decided to look into more improvements.

After some cogitating I hit upon an idea to trade memory for speed. I would build a gigantic hash table containing the offsets of every string of a certain constant length. Then when performing the search, I could examine only the offsets in the hash table, and nothing more. If there were no offsets, or if none of the offsets contained a match, then the string didn't exist in the table.

I finally settled on using a three-byte string prefix and simply gluing those three bytes together to produce a 24-bit value. I then created the offsets table to index using the prefix directly, meaning it contained 16.8 million entries. Each entry would be a pointer to a list of offsets, so this table of pointers would be 64MB, plus the space taken up by the offsets. There is approximately one offset for each byte in the string table (minus two, since it can't go all the way to the end) and each offset is four bytes, so this carries an additional four-to-one overhead over the size of the string table. With this data set the total overhead would be something around 150MB, an entirely reasonable tradeoff for smoething that will never run on a user's computer.

To better illustrate, here is a diagram of what the offsets table looks like in mid-run:

```
    +-----+
    |"aaa"|-->(532, 557, 1989)
    +-----+
    |"aab"|-->X
    +-----+
    |"aac"|-->X
    +-----+
    |"aad"|-->(1008)
    +-----+
      ...
    +-----+
    |"bon"|-->(3, 499, 2012)
    +-----+
    |"boo"|-->(12, 51, 732, 888)
    +-----+
    |"bop"|-->X
    +-----+
      ...
    +-----+
    |"zzx"|-->X
    +-----+
    |"zzy"|-->(2501)
    +-----+
    |"zzz"|-->(2600)
    +-----+
```

Each three-character entry in the offsets table is a pointer to a list of offsets. Any entry which doesn't exist in the string table is a NULL pointer.

When adding the string "book" to the table, the "boo" entry is consulted. Offset 12 starts with "boolean logic" and is rejected. Next, offset 51 is examined. It starts with "book" and so 51 is used as the offset for this string.

When adding the string "bonus" to the table, the "bon" list is consulted. Offset 3 starts with "bon is" and is rejected. Offsets 499 and 2012 likewise do not contain "bonus", so the string "bonus" is appended to the end. This adds five new three-character prefixes to the string table, three in "bonus" itself and two for the last two characters in the string table, and these new prefixes and their offsets are added to the offsets table.

As you can see, this search strategy considerably reduces the amount of text which needs to be searched.

One last question is what to do with strings under three characters. One possibility would be to compute all the three-character prefixes which contain the string in question, and then search all of those offsets. Another possibility would be to pad with zero bytes and generate three prefixes for each offset. But I chose to keep things simple and just fall back to Boyer-Moore for this case, as such small strings are not all that common in my data. (Of course Boyer-Moore's speed advantage is basically useless for such small strings, but I already have the code handy, so why not?)

And what were the results? The small data set now generates its string table in about ten seconds. The large data set which used to take 100 minutes to generate the string table now takes about 2.5 minutes, for a speedup of roughly a factor of 40. I'm sure that even an insanely micro-optimized and vectorized Boyer-Moore would have a tough time being anywhere near 40 times faster than the original, once again showing how algorithmic improvements can totally beat the pants off more obvious and "traditional" micro-optimization.

Performance analysis shows that the code is spending most of its time in `memcmp()`, so additional speedups could potentially be gained from inlining the initial comparisons, or by expanding the length of the prefix so as to help provide fewer offsets to examine per prefix. The current level of performance is acceptable to me, however, so I plan to leave it be for now.

Interestingly the asymptotic running time of this algorithm is actually worse than the Boyer-Moore case. Boyer-Moore is `O(n)`, where `n` is the size of the large string. The worst case of my new algorithm is `O(n*m)`, where m is the size of the small string. The hashing is effectively a constant-time divisor to that `n*m`, which as we all know does not affect the big-O performance of an algorithm. However, since the divisor is about 16.8 million, it would take a really huge data set before the Boyer-Moore version really does start to perform better, and as can be seen from my real-world data sets, the multi-megabyte sizes I'm dealing with attain much better performance with the prefix table algorithm.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
