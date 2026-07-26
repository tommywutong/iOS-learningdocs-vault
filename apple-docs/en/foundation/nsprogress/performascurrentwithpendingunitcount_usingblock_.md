---
title: 'performAsCurrentWithPendingUnitCount:usingBlock:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsprogress/performascurrentwithpendingunitcount:usingblock:'
source_url: 'https://developer.apple.com/documentation/foundation/nsprogress/performascurrentwithpendingunitcount:usingblock:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsprogress/performascurrentwithpendingunitcount%3Ausingblock%3A.json'
content_hash: 'sha256:85165be6002cfd98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# performAsCurrentWithPendingUnitCount:usingBlock:

<sub>Instance Method</sub>

Retrieves the current thread’s progress object, executes the specified block, and increments the progress object by the specified units of work.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) performAsCurrentWithPendingUnitCount:(int64_t) unitCount usingBlock:(void (^)()) work;
```

## Discussion

Use this function as a convenience method to wrap an existing method or block to increment the current progress object. This function retrieves the current progress object, does the work you specify in the block. When the block is complete, this function increments the current progress object. This function is the same as calling [- becomeCurrentWithPendingUnitCount:](<../progress/becomecurrent(withpendingunitcount_).md>), doing the work you specify in the block, and calling [- resignCurrent](<../progress/resigncurrent().md>).

## See Also

### Accessing the Current Progress Object

- [+ currentProgress](<../progress/current().md>) — Returns the progress instance, if any.
- [- becomeCurrentWithPendingUnitCount:](<../progress/becomecurrent(withpendingunitcount_).md>) — Sets the progress object as the current object of the current thread, and assigns the amount of work for the next suboperation progress object to perform.
- [- resignCurrent](<../progress/resigncurrent().md>) — Restores the previous progress object to become the current progress object on the thread.
