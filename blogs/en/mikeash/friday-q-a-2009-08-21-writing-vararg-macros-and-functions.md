---
title: 'Friday Q&A 2009-08-21: Writing Vararg Macros and Functions'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-08-21-writing-vararg-macros-and-functions.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e5458f5dfecbb470'
translated: false
---

> 原文：[Friday Q&A 2009-08-21: Writing Vararg Macros and Functions](https://www.mikeash.com/pyblog/friday-qa-2009-08-21-writing-vararg-macros-and-functions.html)　·　mikeash.com Friday Q&A

Posted at 2009-08-21 15:15 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Reading Between the Lines of Apple's FCC Reply](https://www.mikeash.com/pyblog/reading-between-the-lines-of-apples-fcc-reply.html)  
Previous article: [Friday Q&A 2009-08-14: Practical Blocks](https://www.mikeash.com/pyblog/friday-qa-2009-08-14-practical-blocks.html)  
Tags: [c](https://www.mikeash.com/pyblog/?tag=c) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [macro](https://www.mikeash.com/pyblog/?tag=macro) [vararg](https://www.mikeash.com/pyblog/?tag=vararg)

Friday Q&A 2009-08-21: Writing Vararg Macros and Functions

by [Mike Ash](https://www.mikeash.com/)

**Macros**  
 Writing a vararg macro is pretty simple in principle. Note that unlike functions, vararg macros are new as of C99, so they won't work with earlier dialects. You create one by putting `...` at the end of the macro's argument list, like so:

```
    #define vararg_macro(a, b, c, ...)
```

And then you access them by using `__VA_ARGS__`, which just expands to the arguments provided, separated by commas just like they were provided.

Here's an example of a debug logging macro using this technique:

```
    #define DEBUG_LOG(...) do { \
        if(gDebugLoggingEnabled) { \
            fprintf(stderr, "Debug log:" __VA_ARGS__); \
            fprintf(stderr, "\n") \
        } \
    } while(0)
```

If you haven't seen it before, the `do`/`while` construct is a common way to construct a multi-statement macro which is actually a single statement. The worth of this can be seen in this hypothetical code:

```
    if(!condition)
        DEBUG_LOG("condition was false!");
    else
        do_something_important();
```

If this macro were written without the `do`/`while` wrapping, this code would fail in hilarious ways.

Now let's say we wanted to add logging of the file name and line number where the log is, using the `__FILE__` and `__LINE__` macros. We could do this by adding a third `fprintf` line, but imagine we want to combine it into the first line instead. This is easy enough to do:

```
    #define DEBUG_LOG(fmt, ...) do { \
        if(gDebugLoggingEnabled) \
            fprintf(stderr, "Debug log, %s:%d: " fmt "\n", __FILE__, __LINE__, __VA_ARGS__); \
    } while(0)
```

This works, but it has a problem: it requires at least one argument besides the format string. You can't just do `DEBUG_LOG("condition was false!")` anymore, because that leaves a dangling comma at the end.

The easiest solution to this is to take advantage of a gcc-specific extension. Putting `##` in between the comma and the `__VA_ARGS__` will remove the comma when `__VA_ARGS__` is empty:

```
    #define DEBUG_LOG(fmt, ...) do { \
        if(gDebugLoggingEnabled) \
            fprintf(stderr, "Debug log, %s:%d: " fmt "\n", __FILE__, __LINE__, ## __VA_ARGS__); \
    } while(0)
```

Now everything works as expected! Of course this code is not strictly C99 compliant anymore, so beware.

**Functions**  
 Vararg functions aren't that much harder. The declaration is pretty much the same as for a macro: put `...` at the end of the argument list. One important difference can be seen here: the `...` _must not_ be the only parameter the function takes. In other words, a vararg function must take at least one fixed parameter.

In the body of the function, you'll want to make sure to do `#include ` to get the appropriate declarations, then you can use some simple functions to work with the argument list. The `va_list` type describes a variable argument list. Then you call `va_start` on it to initialize it. To do your actual work, call `va_arg` in a loop to pop arguments, and when you're all done you call `va_end` to terminate processing.

Note that these are the only three operations supported. It's not possible to query the argument list for length, for type, or anything else like that. You must take care of these things yourself by arranging a convention with the caller.

Let's write a quick example. Imagine that for some reason you find yourself frequently needing to post several `NSNotification`s at a time. To cut down on the work required, we can write a vararg function that takes a number of notifications as the parameters. This is what the declaration will look like:

```
    void PostNotifications(id obj, NSString *firstNotificationName, ... /* terminate with nil */)
```

Notice how I just document that the caller must terminate the list with `nil`. Since I can't query for the length of the list, that's how we'll know when to stop. Also notice how `firstNotificationName` is a fixed parameter. This will make the following code a little simpler.

Next, we'll set up the `va_list`:

```
    {
        va_list args;
        va_start(args, firstNotificationName);
```

To call `va_start` we have to tell it what the last fixed parameter is. This is why there needs to be at least one fixed parameter.

Next, we'll run a loop to post the notifications:

```
        NSString *notificationName = firstNotificationName;
        while(notificationName)
        {
            [[NSNotificationCenter defaultCenter] postNotificationName:notificationName object:obj];
            notificationName = va_arg(args, NSString *);
        }
```

Then clean up:

```
        va_end(args);
    }
```

Now we can use it like so:

```
    PostNotifications(self, FirstNotificationName, SecondNotificationName, ThirdNotificationName, nil);
```

Easy!

This is kind of fragile, because you'll crash if the caller forgets to terminate the list, and anything could happen if he passes in something of the wrong type (like a `float`) by accident, but that's just how vararg functions work in C.

**Conclusion**  
 That wraps up this week's Friday Q&A. Vararg macros and functions are a little strange but they can be handy, and once you know the basics they're not too hard to make at all.

Come back next week for another exciting edition. As always, Friday Q&A is driven by you, the reader. If you have any suggestions for a future topic of discussion, post it in the comments or [e-mail it to me](mailto:mike@mikeash.com). Without your suggestions, Friday Q&A could not happen, so send them in!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-08-21-writing-vararg-macros-and-functions.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
