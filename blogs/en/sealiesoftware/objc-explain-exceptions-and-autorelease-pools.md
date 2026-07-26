---
title: '[objc explain]: Exceptions and autorelease pools'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2008/09/16/objc_explain_Exceptions_and_autorelease_pools.html'
original_language: en
published: 2008-09-16
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ed4838a993414424'
translated: false
---

> 原文：[[objc explain]: Exceptions and autorelease pools](http://sealiesoftware.com/blog/archive/2008/09/16/objc_explain_Exceptions_and_autorelease_pools.html)　·　Hamster Emporium (Greg Parker)

[![](http://sealiesoftware.com/hamster.jpg)](http://sealiesoftware.com/blog/index.html)  
  
 **blog**  
 [recent](http://sealiesoftware.com/blog/index.html)  
 [archive](http://sealiesoftware.com/blog/archive/index.html)  
 [twitter](http://twitter.com/gparker)  
   
 **projects**  
 [Mac OS X](http://www.apple.com/macosx/)  
 [Keyboard](http://sealiesoftware.com/keyboard/index.html)  
 [backlight](http://sealiesoftware.com/keyboard/index.html)  
 [CSC Menu](http://sealiesoftware.com/cscmenu/index.html)  
 [Valgrind](http://sealiesoftware.com/valgrind/index.html)  
 [Fringe Player](http://sealiesoftware.com/fringe/index.html)  
 [pssh](http://sealiesoftware.com/pssh/index.html)  
 [Peal](http://sealiesoftware.com/peal/index.html)  
 [Frankenmouse](http://sealiesoftware.com/frankenmouse/index.html)

## Hamster Emporium archive

\<\< [[objc explain]: So you crashed in objc_msgSend()](http://sealiesoftware.com/blog/archive/2008/09/22/objc_explain_So_you_crashed_in_objc_msgSend.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]: return value of message to nil](http://sealiesoftware.com/blog/archive/2007/4/21/objc_explain_return_value_of_message_to_nil.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2008/09/16/objc_explain_Exceptions_and_autorelease_pools.html)

**[objc explain]: Exceptions and autorelease pools** ([2008-09-16 2:45 PM](http://sealiesoftware.com/blog/archive/2008/09/16/objc_explain_Exceptions_and_autorelease_pools.html))

Autorelease pools are automatically cleaned up after exceptions. If you want to write exception-safe code, then autorelease pools are a useful tool.

Exception objects themselves should be autoreleased. `+[NSException exceptionWithName:...]` and `+[NSException raise:...]` do this for you.

Autorelease pools can help make your other memory exception-safe. These two patterns will correctly free memory even if an exception is thrown. (With GC you have a third option - do nothing - but these two also work there.)

```
    id obj = [[[MyClass alloc] init] autorelease];
    CodeThatMightThrow();
```

```
    id obj = [[MyClass alloc] init];
    @try {
        CodeThatMightThrow();
    } @finally {
        [obj release];
    }
```

The `-autorelease` version works like this. Autorelease pools form a stack. The current autorelease pool is the top of that stack. If you call `[pool drain]` on an autorelease pool that is not the current pool, then your pool _and every more recent pool after it_ is destroyed.

When an exception unwinds the stack, some `-drain` calls are skipped. But those pools don't leak. Eventually the exception is caught, inside the scope of some pool. When the `[pool drain]` for that pool is reached, the other pools bypassed by the exception are also destroyed.

If you write your own processing loop with an autorelease pool and an exception handler, be sure to delete your pool after you catch and handle an exception. Otherwise the bypassed pools won't be destroyed until you return to the next autorelease pool out, if any.

If you write `@catch` or `@finally` handlers, don't drain your local autorelease pool inside the handler. The exception object might be in that pool (or another pool inside that), and you don't want to delete it yet. Instead, just abandon your pool and let the next pool out take care of it. (You're free to create and destroy a new pool inside `@catch` or `@finally`; just don't drain any pool that was created before.)

In other words, don't do this:

```
   NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
   @try {
       // stuff
   } @finally {
       [pool drain];  WRONG
   }
```

Do this instead:

```
   NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
   @try {
       // stuff
   } @finally {
       // cleanup things other than pool itself
   }
   [pool drain];
```

[Sealie Software](http://sealiesoftware.com/index.html)
