---
title: 'Friday Q&A 2010-02-05: Error Returns with Continuation Passing Style'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-02-05-error-returns-with-continuation-passing-style.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:13229d1602e60e73'
translated: false
---

> 原文：[Friday Q&A 2010-02-05: Error Returns with Continuation Passing Style](https://www.mikeash.com/pyblog/friday-qa-2010-02-05-error-returns-with-continuation-passing-style.html)　·　mikeash.com Friday Q&A

Posted at 2010-02-05 18:36 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-02-12: Trampolining Blocks with Mutable Code](https://www.mikeash.com/pyblog/friday-qa-2010-02-12-trampolining-blocks-with-mutable-code.html)  
Previous article: [Friday Q&A 2010-01-29: Method Replacement for Fun and Profit](https://www.mikeash.com/pyblog/friday-qa-2010-01-29-method-replacement-for-fun-and-profit.html)  
Tags: [blocks](https://www.mikeash.com/pyblog/?tag=blocks) [continuations](https://www.mikeash.com/pyblog/?tag=continuations) [errorhandling](https://www.mikeash.com/pyblog/?tag=errorhandling) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2010-02-05: Error Returns with Continuation Passing Style

by [Mike Ash](https://www.mikeash.com/)

**`NSError **`**  
 The standard Cocoa convention for signalling errors to a caller is to return the error by way of an extra parameter pointing to a `NSError *` variable, like so:

```
    NSError *error;
    NSString *string = [[NSString alloc] initWithContentsOfFile: path encoding: NSUTF8StringEncoding error: &error];
    if(!string)
        // do something with error
```

This works, but is a bit painful to type. It's also painful to implement, because the code needs to set the error and return

as two separate steps. The error parameter is also optional, so the method needs to do a

check for every error case, like so:

```
    if(failure)
    {
        if(error)
            *error = [NSError errorWith...];
        return nil;
    }
```

Other languages handle this quite a bit nicer. For example, the equivalent in Python is:

```
    string, error = someFunction(...)
```

And the return is equally easy:

```
    if failure:
        return None, createErrorObject(...)
```

This is because Python has built-in support for returning multiple values from a function, whereas Objective-C doesn't. How can we get the Objective-C side to be equally nice?

**Exceptions**  
 For languages without support for multiple return values (and often for those that do support it), the common solution for error returns is exceptions. In Objective-C, using this technique would look like this for the caller:

```
    @try
    {
        NSString *string = [[NSString alloc] init...];
        // use string
    }
    @catch(NSException *exception)
    {
        // handle exception
    }
```

This is still a bit verbose, however that is often compensated by the fact that multiple calls can be placed in the same

block, and share the same

handler.

The other end of it is nice and simple:

```
    if(failure)
        @throw [NSException exceptionWith...];
```

It also allows chaining errors very easily. If you have a method that calls another method and the inner method can error, then allowing the outer method to also error is simply a matter of not catching the exception. With other techniques, you need to explicitly check for errors at every call and propagate them up the call chain.

However, exceptions have their own problems. If a method can return an error and you ignore it, then you just lose out on some diagnostic information. If a method can throw an exception and you fail to catch it, then it can cause inconsistent states and even crashes as the exception is thrown through code that's not written to handle it. Writing exception-safe code requires more thought and care.

These problems aren't insurmountable. Exceptions are often used in other languages for this sort of thing. However, they're not traditionally used in Objective-C, which means that even if you want to use them, it can be tough to deal with all the code out there that isn't aware of them. For routine errors, it will also make it difficult to debug your programs when you end up having a serious error where an exception shouldn't be thrown at all, but is. It's very common to simply break on `objc_exception_throw` to, for example, figure out just where an exception is being thrown from within some Cocoa calls, but that technique becomes unusable if your application frequently throws exceptions as part of its routine operations.

If you don't want to use exceptions, but want something better than `NSError **`, what can you do?

**Continuation Passing Style**  
 [Continuation Passing Style](http://en.wikipedia.org/wiki/Continuation_Passing_Style), or CPS, is a style of programming using anonymous functions to replace return statements. Instead of returning a value, a function will take another function as a parameter. Then, when it gets to the point where it would have returned a value, it calls the passed-in function with the value as a parameter instead. In Objective-C, we now have anonymous functions in the form of blocks, so CPS can be achieved using blocks.

Here's an example of how CPS looks. This is the standard-style code:

```
    NSString *string = [obj stringWhatever];
    // use string
```

And here it is converted to CPS:

```
    [obj stringWhatever: ^(NSString *string) {
        // use string
    }];
```

CPS has many different uses, such as providing a convenient interface for asynchronous operations. Here, however, I want to use CPS to take advantage of a convenient fact: although Objective-C methods can only return one value, Objective-C blocks can trivially take two parameters.

Thus, the annoying error return-by-reference style can be converted into a cleaner CPS version, like this:

```
    [NSString stringWithContentsOfFile: path encoding: NSUTF8StringEncoding continuation: ^(NSString *string, NSError *error) {
        if(error)
            // handle error
        else
            // use string
    }];
```

This is nice and straightforward. As a bonus, Xcode will automatically complete the basic outline of the block for you if you hit return while on the argument placeholder.

On the other side it's pretty simple to deal with as well:

```
    + (void)stringWithContentsOfFile: (NSString *)path encoding: (NSStringEncoding)encoding continuation: (void (^)(NSString *, NSError *))continuation
    {
        // create string from path
        
        if(failure)
            continuation(nil, [NSError errorWith...]);
        else
            continuation(string, nil);
    }
```

Handing errors "up the stack" is pretty easy too. Imagine a method which does its own error reporting using this CPS technique, and which calls that NSString method. If it errors, it just wants to report the error up the chain:

```
    - (void)computeObject: (id)obj continuation: (void (^)(id, NSError *))continuation
    {
    [NSString stringWithContentsOfFile: path encoding: NSUTF8StringEncoding continuation: ^(NSString *string, NSError *error) {
        if(error)
            continuation(nil, error);
        else
        {
            ...continue processing with string...
            id result = ...;
            continuation(result, nil);
        }
    }];
```

**Two-Block Variant**  
 Since the first action of the continuation is almost certain to be to check and do something different if an error occurred, it would be reasonable to split up the continuation into two parts. This moves the check into the called method (which probably needs to have such a check anyway) and simplifies the caller. You pass an error block and a normal block, and the method will then call the appropriate one. This variant would look like this:

```
    [NSString stringWithContentsOfFile: path encoding: NSUTF8StringEncoding
        errorHandler: ^(NSError *error) {
            // handle error
        }
        continuation: ^(NSString *string) {
            // use string
        }];
```

This style also simplifies handing errors "up the stack", because the caller's error handler can just be passed straight in as the error handler for the next level:

```
    - (void)computeObject: (id)obj errorHandler: (void (^)(NSError *))errorHandler continuation: (void (^)(id))continuation
    {
        [NSString stringWithContentsOfFile: path encoding: NSUTF8StringEncoding errorHandler: errorHandler continuation: ^(NSString *string) {
            // continue processing with string
            continuation(string);
        }];
    }
```

Using CPS for error returns isn't all roses. A problem comes at the interface between CPS code and normal-style code. In other words, where you have a method which needs to return a value, but which calls CPS methods. The problem arises because using the

statement inside a block returns a value from the block, not from the enclosing function:

```
    - (NSString *)contentsOfFile: (NSString *)path
    {
        [NSString stringWithContentsOfFile: path encoding: NSUTF8StringEncoding
            errorHandler: ^(NSError *error) {
                [NSApp reportError: error];
            }
            continuation: ^(NSString *string) {
                return string; // fails! returns string from the block, not the method!
            }];
    }
```

In order to get around this problem, you need to move the value outside of the continuation using a

-qualified local variable, then return from within the main function body:

```
    - (NSString *)contentsOfFile: (NSString *)path
    {
        __block NSString *returnValue = nil;
        [NSString stringWithContentsOfFile: path encoding: NSUTF8StringEncoding
            errorHandler: ^(NSError *error) {
                [NSApp reportError: error];
            }
            continuation: ^(NSString *string) {
                // string is retained here in case there are any inner autorelease pools
                // in the NSString method that's calling this continuation
                // retaining it will keep it alive even if there is one and it is popped
                // the retain is balanced by an autorelease in the method body
                returnValue = [string retain];
            }];
        return [returnValue autorelease];
    }
```

This is not a huge inconvenience, but it is mildly annoying, and certainly removes some of the elegance of using CPS here.

A bigger downside is that, well, Cocoa doesn't do CPS error returns, it does return-by-reference. It's not too hard to write adapter methods:

```
    typedef void (^ErrorHandler)(NSError *error);
    
    @implementation NSString (CPSErrors)
    
    + (void)stringWithContentsOfFile: (NSString *)path encoding: (NSStringEncoding)encoding errorHandler: (ErrorHandler)errorHandler continuation: (void (^)(NSString *string)continuation
    {
        NSError *error;
        NSString *string = [self stringWithContentsOfFile: path encoding: encoding error: &error];
        if(string)
            continuation(string);
        else if(errorHandler)
            errorHandler(error);
    }
    
    @end
```

But obviously the annoyance of having to write adapters makes for a big hit to the niceness of using CPS for error handling.

**Conclusion**  
 The addition of blocks to Objective-C enables some completely new ways of doing things, including a new way to deal with errors. The practicality of this approach remains to be seen, but it certainly does produce nicer-looking code than the traditional Cocoa way.

That's it for this Friday Q&A. Come back in 5.56×1015 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the caesium 133 atom for the next exciting installment. Friday Q&A is driven by user submissions, so if you have a topic you would like to see covered here, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
