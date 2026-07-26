---
title: Races on collections and other APIs
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/races-on-collections-and-other-apis
source_url: 'https://developer.apple.com/documentation/xcode/races-on-collections-and-other-apis'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/races-on-collections-and-other-apis.json'
content_hash: 'sha256:3fb3acce4c703c1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing memory, thread, and crash issues early](diagnosing-memory-thread-and-crash-issues-early.md)

# Races on collections and other APIs

<sub>Article</sub>

Detects when one thread accesses a mutable object while another thread is writing to it.

## Overview

In Xcode 9 and later, the Thread Sanitizer detects unsafe thread accesses of [Foundation](../foundation.md) and [Core Foundation](../corefoundation.md) framework APIs. This feature applies to the following collection types:

- [NSMutableArray](../foundation/nsmutablearray.md)
- [NSMutableDictionary](../foundation/nsmutabledictionary.md)
- [CFMutableArray](../corefoundation/cfmutablearray.md)
- [CFMutableDictionary](../corefoundation/cfmutabledictionary.md)

### Collection race with a mutable array

In the following example, the code enumerates a mutable array in one thread while writing to the array from another without synchronizing access:

**Swift**

```swift
let array: NSMutableArray = []
var sum: Int = 0
// Executed on Thread #1
for value in array {
    sum += value as! Int
}
// Executed on Thread #2
array.add(42)
```

**Objective-C**

```objc
NSMutableArray *array = [NSMutableArray new];
NSInteger sum = 0;
// Executed on Thread #1
for (id value in array) {  
    sum += [value integerValue];
} 
// Executed on Thread #2
[array addObject:@42];
```

#### Solution

Use [Dispatch](../dispatch.md) APIs to coordinate access to `array` across multiple threads.

### Collection race with a mutable dictionary

In the following example, the code enumerates a mutable dictionary in one thread while writing to the dictionary from another without synchronizing access:

```swift
let dictionary: NSMutableDictionary = [:]
var sum: Int = 0
// Executed on Thread #1
for key in dictionary.keyEnumerator() {
    sum += dictionary[key] as! Int
}
// Executed on Thread #2
dictionary["forty-two"] = 42
```

**Objective-C**

```objc
NSMutableDictionary *dictionary = [NSMutableDictionary new];
NSInteger sum = 0;
// Executed on Thread #1
for (id key in dictionary) {
    sum += [dictionary[key] integerValue];
}
// Executed on Thread #2
dictionary[@"forty-two"] = @42;
```

#### Solution

Use [Dispatch](../dispatch.md) APIs to coordinate access to `dictionary` across multiple threads.

## See Also

### Thread Sanitizer

- [Data races](data-races.md) — Detects unsynchronized access to mutable state across multiple threads.
- [Swift access races](swift-access-races.md) — Detects unsynchronized access to mutable state across multiple threads in Swift.
- [Uninitialized mutexes](uninitialized-mutexes.md) — Detects when you use an uninitialized mutex.
- [Thread leaks](thread-leaks.md) — Detects when you don’t close threads after use.
