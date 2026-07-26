---
title: 'Friday Q&A 2011-02-18: Compound Literals'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-02-18-compound-literals.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:15cb620acf9d6e19'
translated: false
---

> 原文：[Friday Q&A 2011-02-18: Compound Literals](https://www.mikeash.com/pyblog/friday-qa-2011-02-18-compound-literals.html)　·　mikeash.com Friday Q&A

Posted at 2011-02-18 16:20 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2011-03-04: A Tour of OSAtomic](https://www.mikeash.com/pyblog/friday-qa-2011-03-04-a-tour-of-osatomic.html)  
Previous article: [Complete Friday Q&A Direct-Sell ePub, PDF, and Print on Demand](https://www.mikeash.com/pyblog/complete-friday-qa-direct-sell-epub-pdf-and-print-on-demand.html)  
Tags: [c99](https://www.mikeash.com/pyblog/?tag=c99) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2011-02-18: Compound Literals

by [Mike Ash](https://www.mikeash.com/)

Compound literals are a relatively unknown feature in C. They are fairly new. Introduced as part of the C99 standard in 2000, they've been around for a while, but for a language that dates to the 1960s, it's a recent addition.

C99 added a lot of useful features to the language that modern Mac and iOS programmers tend to take for granted. Many of these existed as compiler extensions beforehand. Simple features like `//` comments, the `long long` type, and the ability to mix variable declarations and code are all new in C99. Compound literals are much less well known than these features, but are equally standard and can be handy, and this is why I want to talk about them today.

**Compound Literal Basics**  
 Compound literals provide a way to write values of arbitrary data types in code. An expression like `"hello"` is a string literal that has type `char *`. A compound literal is simply a different kind of expression that has whatever type you're after. For example, it's possible to create an expression which produces the same C string as the string literal, but with explicit character-by-character construction:

```
    (char []){ 'h', 'e', 'l', 'l', 'o', '\0' }
```

This is not particularly useful, of course. However, more useful things can be done with the syntax as well:

```
    (NSSize){ 1, 2 }
```

This is equivalent to `NSMakeSize(1, 2)` but without the need for an external function. Similar syntax will work for any type, even custom-defined structs.

Compound literal syntax closely matches variable initialization syntax. For example:

```
    NSSize s = { 1, 2 };
    (NSSize){ 1, 2 }; // same value
    
    int x[] = { 3, 4, 5 };
    (int []){ 3, 4, 5 }; // same
```

And in general, if a variable is declared with an initializer, then a compound literal with the same type and value can be written by sticking the type in parentheses and placing the initializer immediately after it:

```
    Type name = { val };
    (Type){ val };
```

There is one exception to this rule. Primitive types (like `int`) don't require `{}` to be initialized, but `{}` is still required to create a compound literal. It is _not_ the same to write `(int)3` and `(int){ 3 }`, although they act similarly in many cases. The former simply takes the integer constant `3` and uselessly casts it to `int`, whereas the latter is essentially a variable declaration with no name.

**Basic Tricks**  
 The ability to create custom struct values is probably the most useful obvious application of compound literals. Although Cocoa takes care of its most common types with `NSMakeRect` and friends, there are still places to put compound literals to good use.

For example, a `CGRect` is really just an `CGPoint` and an `CGSize`. `CGRectMake` takes four discrete numbers, but sometimes it's more convenient to just deal with those two elements. Compound literals let you do that inline:

```
    [layer setFrame: (CGRect){ origin, size }];
```

The ability to create array literals can also be useful. For example, this creates a string containing a copyright symbol:

```
    [NSString stringWithCharacters: (unichar []){ 0x00a9 } length: 1]
```

**Scope**  
 A compound literal is essentially an anonymous variable declaration and initialization. As such, it follows the same scoping rules as regular variables. For example, this is perfectly legal:

```
    int *ptr;
    ptr = (int []){ 42 };
    NSLog(@"%d", *ptr);
```

The compound literal is still in scope when the `NSLog` executes, so it is legal to dereference the pointer. This, however, is not legal:

```
    int *ptr;
    do {
        ptr = (int []){ 42 };
    } while(0);
    NSLog(@"%d", *ptr);
```

The compound literal's lifetime is tied to the scope of the `do`/`while` loop, and it no longer exists afterwards. The `NSLog` statement may print junk or crash.

**Mutability**  
 One really unintuitive thing about compound literals is that, unless you declare their type as `const`, they produce mutable values. The following is perfectly legal, albeit completely pointless, code:

```
    (int){ 0 } = 42;
```

Less uselessly, this fact means that you can take the address of compound literals, and it's safe to pass them to code which will modify the pointed-to value. There are a lot of functions which take a pointer as a parameter purely to allow passing different data types, but ultimately they just want a primitive. Using compound literals, you can pass that primitive value inline instead of having to create a temporary variable.

For example, a common operation on sockets is to set the `SO_REUSEADDR` option. This tells the OS to free up the socket's port for use as soon as the socket is closed, instead of the default behavior of waiting a few minutes first. This option is set using `setsockopt`. It can be used to set various parameters which need different argument types, so it simply takes a `void *` and a length. This is how it's normally used to set this option:

```
    int yes = 1;
    setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(yes));
```

Using compound literals, we can make it look more natural:

```
    setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &(int){ 1 }, sizeof(int));
```

This is a fairly minor aesthetic thing, but it is a bit cleaner and more readable. It'll also clutter up the debugger with one fewer local variable.

Another place where this comes in handy is writing methods which take an `NSError **` parameter to pass error information to the caller. By convention, it's legal to pass `NULL` as the pointer to indicate that the caller doesn't care about the error. This means that at every place where an error can occur, the pointer must be checked. This gets a bit tedious:

```
    - (BOOL)doWithError: (NSError **)error
    {
        if(fail1)
        {
            if(error)
                *error = [NSError ...];
            return NO;
        }
        if(fail2)
        {
            if(error)
                *error = [NSError ...];
            return NO;
        }
        if(fail3)
        {
            if(error)
                *error = [NSError ...];
            return NO;
        }
        
        return YES;
    }
```

By using a compound literal to create some local storage, you can ensure that the error pointer is always valid, and thus eliminate the constant checks:

```
    - (BOOL)doWithError: (NSError **)error
    {
        error = error ? error : &(NSError *){ nil };
        
        if(fail1)
        {
            *error = [NSError ...];
            return NO;
        }
        if(fail2)
        {
            *error = [NSError ...];
            return NO;
        }
        if(fail3)
        {
            *error = [NSError ...];
            return NO;
        }
        
        return YES;
    }
```

This costs some efficiency, because it creates error objects unnecessarily if the parameter is `NULL`, but that generally wouldn't matter, and the result is somewhat more readable. It also allows the method to call other error-returning methods in a natural way and make use of the result before returning the error to the caller:

```
    - (BOOL)doWithError: (NSError **)error
    {
        error = error ? error : &(NSError *){ nil };
        
        BOOL success = [obj doWithError: error];
        if(!success)
        {
            // don't bail out if we can work around it
            if(![[*error domain] isEqual: CanWorkAroundDomain])
                return NO;
        }
        
        if(fail1)
        {
            *error = [NSError ...];
            return NO;
        }
        
        return YES;
    }
```

**Vararg Macros**  
 I discussed using compound literals and macros a bit in [my post on C macros](https://www.mikeash.com/pyblog/friday-qa-2010-12-31-c-macro-tips-and-tricks.html), but it's useful enough that it bears repeating. By using a compound literal to create an array, you can easily create a macro which takes variable arguments and then does something useful with them. As an example, this macro makes it simpler to create `NSArray` objects:

```
    #define ARRAY(...) [NSArray \
                         arrayWithObjects: (id []){ __VA_ARGS__ } \
                         count: sizeof((id []){ __VA_ARGS__ }) / sizeof(id)]
```

By using the `id []` syntax with compound literals, and by using `sizeof` on the resulting array, you can create macros which do useful things with an arbitrary number of arguments.

**Conclusion**  
 Compound literals are a nice trick to simplify and clarify code. They are not universally applicable, and you must take care not to use them in situations where they hurt more than they help. However, they are a nice tool to have in your bag of tricks, and they help make C a little more useful and generic.

That's it for this time. I _hope_ to be back to my regular schedule now, so look for another post in two weeks. Until then keep sending your ideas. Friday Q&A is (usually!) driven by reader suggestions, so if you have a topic that you would like to see covered here, [send it to me](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-02-18-compound-literals.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
