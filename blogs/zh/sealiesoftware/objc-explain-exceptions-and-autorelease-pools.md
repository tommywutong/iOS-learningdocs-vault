---
title: '[objc explain]：异常与自动释放池'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2008/09/16/objc_explain_Exceptions_and_autorelease_pools.html'
original_language: en
published: 2008-09-16
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ed4838a993414424'
translated: true
---

> 原文：[[objc explain]：异常与自动释放池](http://sealiesoftware.com/blog/archive/2008/09/16/objc_explain_Exceptions_and_autorelease_pools.html)　·　Hamster Emporium (Greg Parker)

[![](http://sealiesoftware.com/hamster.jpg)](http://sealiesoftware.com/blog/index.html)  
  
 **博客**  
 [最近](http://sealiesoftware.com/blog/index.html)  
 [归档](http://sealiesoftware.com/blog/archive/index.html)  
 [twitter](http://twitter.com/gparker)  
   
 **项目**  
 [Mac OS X](http://www.apple.com/macosx/)  
 [Keyboard](http://sealiesoftware.com/keyboard/index.html)  
 [backlight](http://sealiesoftware.com/keyboard/index.html)  
 [CSC Menu](http://sealiesoftware.com/cscmenu/index.html)  
 [Valgrind](http://sealiesoftware.com/valgrind/index.html)  
 [Fringe Player](http://sealiesoftware.com/fringe/index.html)  
 [pssh](http://sealiesoftware.com/pssh/index.html)  
 [Peal](http://sealiesoftware.com/peal/index.html)  
 [Frankenmouse](http://sealiesoftware.com/frankenmouse/index.html)

## Hamster Emporium 归档

\<\< [[objc explain]：你在 objc_msgSend() 里崩溃了](http://sealiesoftware.com/blog/archive/2008/09/22/objc_explain_So_you_crashed_in_objc_msgSend.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]：发给 nil 的消息的返回值](http://sealiesoftware.com/blog/archive/2007/4/21/objc_explain_return_value_of_message_to_nil.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2008/09/16/objc_explain_Exceptions_and_autorelease_pools.html)

**[objc explain]：异常与自动释放池** ([2008-09-16 2:45 PM](http://sealiesoftware.com/blog/archive/2008/09/16/objc_explain_Exceptions_and_autorelease_pools.html))

自动释放池会在异常发生后被自动清理。如果你想写出异常安全的代码，那么自动释放池就是一个很有用的工具。

异常对象本身应该被自动释放（autorelease）。`+[NSException exceptionWithName:...]` 和 `+[NSException raise:...]` 都会替你完成这件事。

自动释放池能帮你让其他内存也变得异常安全。下面这两种写法，即便有异常抛出，也能正确地释放内存。（用 GC 的话你还有第三种选择——什么都不做——不过下面这两种写法在 GC 下同样也能用。）

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

`-autorelease` 这种写法是这样工作的。自动释放池会组成一个栈。当前的自动释放池就是这个栈的栈顶。如果你对一个不是当前池的自动释放池调用 `[pool drain]`，那么你这个池*以及它之后所有更新的池*都会被销毁。

当一个异常展开调用栈时，有些 `-drain` 调用会被跳过。但那些池并不会泄漏。异常最终会在某个池的作用域内被捕获。当到达那个池对应的 `[pool drain]` 时，被异常绕过的其他那些池也会一并被销毁。

如果你自己写了一个带自动释放池和异常处理器的处理循环，一定要在捕获并处理完异常之后删除你的池。否则那些被绕过的池，要等到你返回到外层的下一个自动释放池（如果有的话）时才会被销毁。

如果你写了 `@catch` 或 `@finally` 处理器，不要在处理器内部清空（drain）你的局部自动释放池。异常对象可能就在那个池里（或者在它内部的另一个池里），你现在还不想把它删掉。取而代之，只要放弃你的池，交给外层的下一个池去处理就行了。（你可以自由地在 `@catch` 或 `@finally` 内部创建并销毁一个新池；只是不要清空任何在此之前就已创建的池。）

换句话说，不要这样写：

```
   NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
   @try {
       // stuff
   } @finally {
       [pool drain];  WRONG
   }
```

而要这样写：

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
