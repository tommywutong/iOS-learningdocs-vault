---
title: 'NSArray or NSSet, NSDictionary or NSMapTable | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/08/nsarray-or-nsset-nsdictionary-or.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:56561f873993626f'
translated: false
---

> 原文：[NSArray or NSSet, NSDictionary or NSMapTable | Cocoa with Love](https://www.cocoawithlove.com/2008/08/nsarray-or-nsset-nsdictionary-or.html)　·　Cocoa with Love (Matt Gallagher)

Some types of data can be held in more than one kind of collection. Unordered objects that are already guaranteed unique can be sensibly held in an NSArray or an NSSet. Anything an NSDictionary can hold can be held in an NSMapTable. In this post, I measure the performance of creating and using these different options to help you choose which one is right for you.

## Disambiguation

A few weeks ago, I wrote about how [NSMapTable and NSDictionary](https://www.cocoawithlove.com/2008/07/nsmaptable-more-than-nsdictionary-for.html) can hold different types of data in different ways. Someone immediately asked: "Which is faster when holding the _same_ data?" I could guess but I didn't really know.

Then I starting thinking about other collections choices which may be ambiguous. I realised that I was writing code that holds a collection of guaranteed unique, unordered objects — just so that I could iterate over them. I used an NSSet for the purpose (since that class defines "unique and unordered") but since the objects were already guaranteed unique before I created the set, I wondered: how much more efficient would my code be if I used an NSArray instead?

So there are two situations to test for performance:

- NSArray versus NSSet
- NSDictionary versus NSMapTable

Remember that these tests will only apply to situations where either collection is technically capable of holding the same data.

## Methodology

You can [download the code I used for the tests](https://www.cocoawithlove.com/assets/objc-era/MapTablePerformanceTest.m.zip).

To summarise, I create two arrays of data:

- the "keys" — an array of NSString where each string is a 10 digit string containing being a string representation of its index.
- the "objects" — an array of NSNumbers where each number is an integer set to its index.

I tested with one million objects in each of these arrays (n = 1,000,000).

The arrays were in turn used to provide the data for the collections that I would test. The one column collections (NSArray and NSSet) are created and tested with objects from the "objects" source array only. The two column collections (NSMapTable and NSDictionary) created and tested with objects from the "keys" and objects" source arrays.

My test machine was a PPC G5 2x2Ghz. Long live dying platforms!

## Results

### NSArray versus NSSet

| Test | Time taken for NSArray | Time taken for NSSet |
|---|---|---|
| Creating incrementally (capacity not set) | 0.582256 seconds | 2.67101 seconds |
| Creating incrementally (capacity set correctly) | 0.572139 seconds | 0.930725 seconds |
| Iterating contents | 0.004713 seconds | 0.025864 seconds |

Incidentally, constructing an NSSet using setWithArray: takes the same time as the "capacity not set", so if you know the objects in the array are unique, it would be best to set the capacity and copy the data yourself.

### Lookup in NSArray versus NSSet

_Note_: these results were generated with n = 10,000

| Test | Time taken for NSArray | Time taken for NSSet |
|---|---|---|
| Searching for all objects | 29.2667 seconds (indexOfObject:) 0.185051 seconds (indexOfObjectIdenticalTo:) | 0.00833601 seconds |

These results should not be surprising. This test is included for completeness because both collections are capable of inclusion testing.

Searching an array for an objects works well for n \< 100. As you can see, by n = 10,000 the O(n^2) behavior of the NSArray tests (an O(n) lookup times n lookups) makes it a bad choice compared to the O(n) of the NSSet tests (constant time lookup times n lookups). I wasn't going to wait for this test with n = 1,000,000 but I assure you, both NSArray approaches would take an amount of time in the minutes or maybe hours.

### NSDictionary versus NSMapTable

| Test | Time taken for NSDictionary | Time taken for NSMapTable |
|---|---|---|
| Construction | 3.45922 seconds | 2.32607 seconds |
| Iterating keys and querying each object | 0.60859 seconds | 0.770289 seconds |

## Conclusions

Yes, NSArray is faster than NSSet for simply holding and iterating. As little as 50% faster for constructing and as much as 500% faster for iterating. Lesson: if you only need to iterate contents, don't use an NSSet.

Of course, if you need to test for inclusion, work hard to avoid NSArray. Even if you need both iteration _and_ inclusion testing, you should probably still choose an NSSet. If you need to keep your collection ordered and also test for inclusion, then you should consider keeping two collections (an NSArray and an NSSet), each containing the same objects.

NSDictionary is slower to construct than NSMapTable — since it needs to copy the key data. It makes up for this by being faster to lookup. Of course, the two have different capabilities so most of the time, this determination should be made on other factors.
