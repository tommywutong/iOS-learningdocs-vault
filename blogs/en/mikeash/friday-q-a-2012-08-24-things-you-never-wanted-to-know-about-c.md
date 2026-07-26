---
title: 'Friday Q&A 2012-08-24: Things You Never Wanted To Know About C'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-08-24-things-you-never-wanted-to-know-about-c.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2428aa6f5d2d0565'
translated: false
---

> 原文：[Friday Q&A 2012-08-24: Things You Never Wanted To Know About C](https://www.mikeash.com/pyblog/friday-qa-2012-08-24-things-you-never-wanted-to-know-about-c.html)　·　mikeash.com Friday Q&A

Posted at 2012-08-24 13:15 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-08-31: Obtaining and Interpreting Image Data](https://www.mikeash.com/pyblog/friday-qa-2012-08-31-obtaining-and-interpreting-image-data.html)  
Previous article: [Friday Q&A 2012-08-10: A Tour of CommonCrypto](https://www.mikeash.com/pyblog/friday-qa-2012-08-10-a-tour-of-commoncrypto.html)  
Tags: [c](https://www.mikeash.com/pyblog/?tag=c) [evil](https://www.mikeash.com/pyblog/?tag=evil) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [guest](https://www.mikeash.com/pyblog/?tag=guest) [linux](https://www.mikeash.com/pyblog/?tag=linux) [preprocessor](https://www.mikeash.com/pyblog/?tag=preprocessor)

Friday Q&A 2012-08-24: Things You Never Wanted To Know About C

by [Gwynne Raskind](http://blog.darkrainfall.org/)

---

**Error handling in C**  
C, being something of a bare-metal language by today's standards, lacks any advanced facilities for managing control flow when errors happen. Most platforms have found their own ways of coping with the situation, some with language features, some with framework conventions, and others by not coping at all.

**Exceptions**  
The best known, and also perhaps most debated, means of handling control flow for error conditions is exceptions. C++, Java, Objective-C, PHP, and many others all have some form of exception handling construct. In Objective-C, exceptions look like this:

```
    @try {
        if (![someObject doSomethingInteresting]) {
            @throw [NSException exceptionWithName:NSInternalInconsistencyException reason:@"Failed to frobulate the glockenspiel!" userInfo:nil];
        }
        return YES;
    } @catch (NSException *exception) {
        NSLog(@"Either die in the vacuum of space, or tell me what you thought of my poem.");
        return NO;
    } @finally {
        [prognosticator cleanupAfterSlithyToves];
    }
```

Fortunately, Apple realized how ridiculous this tends to look in Cocoa and deprecated exceptions for error handling, instead opting for the NSError model. The use of exception handling in Objective-C is now reserved (at least in theory) for truly "exceptional" conditions, particularly programmer error.

C does have a primitive sort of exception handling in the [`setjmp`](http://pubs.opengroup.org/onlinepubs/7908799/xsh/setjmp.html)/[`longjmp`](http://pubs.opengroup.org/onlinepubs/7908799/xsh/longjmp.html) functions. However, they're extremely weird, not very full featured, and highly error-prone, so they make a poor choice.

_Historically, exceptions in Objective-C were implemented with these functions, but Apple quite sensibly replaced the unwieldy macros with a compiler feature which calls into the C++ exception implementation. In essence, `@try` in Objective-C and `try` in C++ are now the same thing, though they're still not interchangeable due to the separation of class heirarchies._

**Grafting exceptions onto C**  
The first question asked is _why_ anyone would want to put exceptions into pure C. My answer is that this code is just too ugly to let live:

```
    struct whatever *make_a_whatever(int alpha, const char *beta, const char *gamma, size_t delta)
    {
        struct whatever *brillig = malloc(sizeof(struct whatever));
        int fd = -1, r = 0;

        if (!brillig)
            return NULL;
        brillig->alpha = alpha;
        brillig->beta = strdup(beta);
        if (!brillig->beta) {
            free(brillig);
            return NULL;
        }
        if ((fd = open(gamma, O_RDONLY)) == -1) {
            free(brillig->beta);
            free(brillig);
            return NULL;
        }
        brillig->gamma = malloc(delta);
        if (!brillig->gamma) {
            close(fd);
            free(brillig->beta);
            free(brillig);
            return NULL;
        }
        if ((r = read(fd, brillig, delta)) != delta) {
            close(fd);
            free(brillig->gamma);
            free(brillig->beta);
            free(brillig);
            return NULL;
        }
        close(fd);
        return brillig;
    }
```

Admittedly, the example is contrived and could be reorganized to require less repetition, but in the real world I've ended up with code that looks a lot like this. One possible solution is a dumb `goto`:

```
    struct whatever *make_a_whatever(int alpha, const char *beta, const char *gamma, size_t delta)
    {
        struct whatever *brillig = malloc(sizeof(struct whatever));
        int fd = -1, r = 0;

        if (!brillig) goto error;
        brillig->alpha = alpha;
        if (!(brillig->beta = strdup(beta))) goto error;
        if ((fd = open(gamma, O_RDONLY)) == -1) goto error;
        if (!(brillig->gamma = malloc(delta))) goto error;
        if ((r = read(fd, brillig, delta)) != delta) goto error;
        close(fd);
        return brillig;
    error:
        if (fd != -1) close(fd);
        if (brillig) {
            free(brillig->gamma);
            free(brillig->beta);
            free(brillig);
        }
        return NULL;
    }
```

This is certainly better, but still litters the code with a nest of tightly clustered `if` branches. The next step to readability is to macroize the branches:

```
    #define error_if(c)     do { if (!(c)) goto error; }
    #define error_ifnull(p) do { if ((p) == NULL) goto error; }
    #define error_ifneg1(e) do { if ((e) == -1) goto error; }

    struct whatever *make_a_whatever(int alpha, const char *beta, const char *gamma, size_t delta)
    {
        struct whatever *brillig = malloc(sizeof(struct whatever));
        int fd = -1;

        error_ifnull(brillig);
        brillig->alpha = alpha;
        error_ifnull(brillig->beta = strdup(beta));
        error_ifneg1(fd = open(gamma, O_RDONLY));
        error_ifnull(brillig->gamma = malloc(delta));
        error_if(read(fd, brillig, delta) == delta);
        close(fd);
        return brillig;
    error:
        if (fd != -1) close(fd);
        if (brillig) {
            free(brillig->gamma);
            free(brillig->beta);
            free(brillig);
        }
        return NULL;
    }
```

Now, what if you want to know what went wrong? You have no exceptions to pass information up the call stack, nor any place to stuff an error message besides printing to `stderr`, which may not be appropriate for an internal function. What if you have significant cleanup that has to be done regardless of whether or not errors occurred? What if you want to be able to return early from the function but have your cleanup code still run?

**The Solution: Preprocessor Abuse 101**  
For the sake of brevity, I'll skip a few steps in the process that leads to the solution I came up with for these problems and just show it. I needed error handling that:

- Can be applied easily to any function
- Can pass information about specific errors up the call chain
- Can run cleanup code regardless of whether an error ocurrred
- Can run cleanup code regardless of whether the function returns early
- Can be used with both Clang and GCC

That last is a doozy. One might imagine blocks as a fairly simple solution to several of these issues at once, but blocks don't exist in GCC outside of Apple's obsolete customized version.

First, here is what our `make_a_whatever` function looks like with the error handling I wrote:

```
    struct whatever *make_a_whatever(int alpha, const char *beta, const char *gamma, size_t delta, error_t **error)
    {
        struct whatever *brillig = NULL:
        int fd = -1;

        error_enter() {
            on_nullerror(brillig = malloc(sizeof(struct whatever)), ENOMEM, "can't allocate our brillig!");
            brillig->alpha = alpha;
            on_nullerror(brillig->beta = strdup(beta), ENOMEM, "can't allocate beta for brilling with alpha %d!", alpha);
            on_errno(fd = open(gamma, O_RDONLY), "can't open gamma %s!", gamma);
            on_nullerror(brillig->gamma = malloc(delta), ENOMEM, "can't allocate gamma either!");
            on_readerr(fd, brillig, delta, "delta's not in gamma!");
            return brillig;
        } error_handler() {
            if (brillig) {
                free(brillig->gamma);
                free(brillig->beta);
                free(brillig);
            }
            return NULL;
        } error_finally() {
            if (fd != -1)
                close(fd);
        } error_exit(error);
    }
```

Whether or not you find this more readable is a matter of opinion, of course, but it's certainly more functional. For any given error, a formatted message is available, and the error is returned by reference if and only if one occurred. Here's an example call:

```
    error_t *error = NULL;
    struct whatever *whatever = make_a_whatever(1, "gyre", "gimble", SIZE_WABE, &error);

    if (!whatever)
        error_write(error, STDERR_FILENO, true);
```

For convenience, the `error_write` function can optionally free the `error_t` object (this is the third parameter).

There's a good bit of magic behind these macros and functions. Here they are in order of appearance:

**`error_enter`**  
Prepare yourself:

```
    #define error_enter()   do {    \
        __label__ _error_start, _error_exit, _error_finally, _error_done;   \
        __block error_t *_last_error = NULL;    \
        do {    \
            CLEANUP_DECL    \
        _error_start:;
```

Yuck, huh?

First, the entry macro declares several "local" labels. A local label is simply a label whose name is local to its enclosing scope. This is a GCC extension supported by Clang. These four labels are used by the rest of the macros to manage the function's control flow. Notice that because the labels are used across multiple macros, error handling scopes can not be nested.

Next, an `error_t` is declared to hold any error that occurs within this error handling scope. It is marked `__block`, as the Clang implementation of the "finally" clause uses blocks and must update this variable from inside one. For the GCC build, `__block` is `#define`d to nothing.

Next, the "cleanup declaration" takes place, then the "start" label is marked. The main function body goes underneath this.

**`CLEANUP_DECL` and friends**  
The cleanup delcaration and several other pieces of the cleanup implementation are macros, as the implementation is significantly different between GCC and Clang:

```
    #ifndef __has_feature
    #define __has_feature(f) 0
    #endif

    #if __has_feature(blocks)
    typedef void (^_error_cleanup_block_t)(void);
    static inline void _error_cleanup_block(_error_cleanup_block_t *b) { (*b)(); }
    #define CLEANUP_DECL _error_cleanup_block_t _error_cleanup __attribute__((cleanup(_error_cleanup_block),unused)) = NULL;    \
                         goto _error_finally;
    #define CLEANUP_ASSIGN _error_cleanup = ^
    #define CLEANUP_DONE_ASSIGN goto _error_start
    #elif __GNUC__
    #define __block
    typedef void (*_error_cleanup_func_t)(void);
    #define CLEANUP_DECL auto void _error_cleanup_f(_error_cleanup_func_t *f);  \
                         void (*_error_cleanup)(void) __attribute__((cleanup(_error_cleanup_f),unused)) = NULL;
    #define CLEANUP_ASSIGN  void _error_cleanup_f(_error_cleanup_func_t *f)
    #define CLEANUP_DONE_ASSIGN
    #endif
```

For Clang (and any potential future GCC which adopts blocks), a typedef is declared for a cleanup block, just your basic takes-and-returns-void. A `static inline` C function is defined (in the header, remember, not as part of the macro expansion) for running the block.

The cleanup delcaration for Clang declares an `_error_cleanup_block_t` with the `cleanup` attribute. This attribute (another extension originally from GCC) says "run this C function when this variable goes out of scope". It is also marked `unused` to avoid warnings when `-Wunused-variable` is turned on. Next, it jumps to the "finally" label, _before_ the function's main body runs. As we'll see later, this is necessary to make sure the cleanup block is properly set up before any potential return from the function.

For GCC, which has no blocks, a similar process takes place, but `__block` is defined to nothing, and instead of declaring a cleanup block, the code declares a "nested function" to serve for cleanup.

Nested functions are a GCC-only extension which Clang refused to adopt as being not worth the trouble when blocks provide a much better solution for scope-specific functions. The nested function exists only within its parent function and has the same ability to capture from the lexical scope of the parent that a block does. As a nested function can not be used outside its parent function, unlike blocks, it has no need for a special qualifier to specify the memory management around captured variables.

Lastly, the GCC version does not jump to the "finally" label, as the nested function does not need to be assigned anywhere to work; the prototype is enough to use it.

The `auto` keyword, otherwise pretty much useless in C, marks the delcaration as the prototype for a nested function, rather than as a standard function prototype. This is a nonstandard use of a standard keyword and yet another GCC extension.

**`on_everything`**  
For the sake of brevity, again, I will not paste every single one of the `on_*()` macros here, as they're all largely the same.

```
    // Common macros, do not call directly
    #if DEBUG
    #define _error_fail(e, msg, ...)    do {    \
        _last_error = error_newf(e, __LINE__, __FILE__, __PRETTY_FUNCTION__, msg, ## __VA_ARGS__);  \
        goto _error_exit;   \
    } while (0)
    #else
    #define _error_fail(e, msg, ...)    do {    \
        _last_error = error_newf(e, msg, ## __VA_ARGS__);   \
        goto _error_exit;   \
    } while (0)
    #endif
    #define _error_throw() do { goto _error_exit; } while (0)

    // Use e as the error code when (e) < 0.
    // Intended for POSIX routines that return an error code, such as pthread_*()
    #define on_error(e, msg, ...)       do {    \
        int _error_code __attribute__((unused)) = (e);  \
        if (_error_code < 0)    \
            _error_fail(_error_code, msg, ## __VA_ARGS__);  \
    } while (0)

    // Re-throw an error when (e) == false.
    // Intended for chaining error-returning methods.
    #define on_falsethrow(e) do { if (!(e)) _error_throw(); } while (0)
```

Each `on_*()` macro checks its own particular condition for an error, saves off any relevant error code for use by the formatting function, and calls the `_error_fail()` macro.

In turn, the `_error_fail()` macro sets the `_last_error` variable to a new `error_t` based on the passed error code, message, and in debug mode, the file, line, and function in which the error occurred. It then jumps to `_error_exit`, which takes it to the "catch" handler (see below).

The "throw" versions of these macros are intended for passing errors up the call chain; the existing `error_t` object is simply left as is and the "catch" handler is invoked directly. For example:

```
    bool make_many_whatevers(size_t n, struct whatever **list, error_t **error)
    {
        struct whatever *mimsy = NULL;
        size_t i = 0;

        error_enter() {
            for (i = 0; i < n; ++i) {
                on_nullthrow(mimsy = make_a_whatever(/* etc */, error));
            }
            return true;
        } error_handler() {
            for (size_t j = 0; j < i; ++j)
                free_a_whatever(list[i]);
            return false;
        } error_finally() {
        } error_exit(error);
    }
```

The caller will receive whatever the underlying error was.

**`error_handler`**  
And now the "catch" block:

```
    #define error_handler() \
            goto _error_done;   \
        _error_exit: __attribute__((unused));
```

The `error_handler()` macro comes immediately before the "something went wrong" part of the function. Immediately after the main body of the function, it jumps to the "done" label. This is the "normal exit" from function case, making the main body look like this:

```
    _error_start:
        // main body
        goto _error_done;
    _error_exit:
        // something went wrong
```

The `_error_exit` label is declared unused so that the compiler doesn't complain if the function has no `on_*()` statements, which could happen if you're future-proofing a routine for adding error handling later but haven't gotten there yet. This is where the "catch" code goes, handling any errors.

**`error_finally`**  
And finally, the "finally":

```
    #define error_finally() \
            goto _error_done;   \
        _error_finally:;    \
            CLEANUP_ASSIGN {
```

This is where the fun happens. The "finally" part, coming after the "catch", jumps to "done" at the end of it. Notice that this means the "finally" code is never directly executed in normal control flow! In fact, in the GCC version, the lines under `_error_finally` are _never_ executed at all.

`CLEANUP_ASSIGN` in Clang takes the `_error_cleanup` block that was declared in `CLEANUP_DECL` and actually assigns the "finally" code to it. Hence, any variables whose values need to be modified by the "finally" handler must be declared `__block`. This is why, as we saw above, the "start" jumps to here before actually executing the function's main body; if the block wasn't assigned at that time, no cleanup would ever be executed.

The GCC version simply starts the nested function which was declared earlier. In either case, the "finally" code ends up as part of a function which is not part of the normal control flow, and will be executed by the `cleanup` attribute on the `_error_cleanup` variable. Notice that the GCC version never bothers assigning any value to that variable, since the nested function will simply be called by name instead of jumped to by value as a block would be.

**`error_exit`**  
Time to clean up after ourselves:

```
    #define error_exit(error_param) \
                if (_last_error && error_param) \
                    *error_param = _last_error; \
            };  \
            CLEANUP_DONE_ASSIGN;    \
        _error_done:;   \
        } while (0);    \
    } while (0)
```

As part of the "finally" block, the error parameter which was passed to this macro, if non-`NULL`, is given the value of `_last_error`, if any. The "finally" block is ended, and under Clang, control jumps back to the "start", continuing the main body of the function. (Again, under GCC the extra bit of control-flow trickery doesn't need to happen.)

The "done" label, which marks the final end of all this mess, shows up here, and the error handler scope is closed out.

So, here are the steps in execution order:

1. Declare an error variable and a cleanup block.
2. In Clang only, jump to the "finally" handler to assign the code to the cleanup block.
3. In Clang only, jump back to the function's main body.
4. On error only, assign the error variable, and run the error handler.
5. Execute the "finally" handler.
6. Update any error parameter.

**The `error_*()` functions**  
There's one group of code we haven't looked at yet: The functions which actually manage the `error_t` type. They're pretty straightforward; there's no hackery involved in this part. Well, maybe just a little to cover the differences between the debug and non-debug cases and grab the executable's name:

```
    typedef struct {
        int error_code;
        char *message;
    #if DEBUG
        int line;
        char *file;
        char *function;
    #endif
    } error_t;

    #if DEBUG
    #define DEBUG_PARMS , int line, const char *file, const char *function
    #define DEBUG_PASS(f) , line, f(file), f(function)
    #define DEBUG_FNUM 5
    #define DEBUG_VNUM 6
    #else
    #define DEBUG_PARMS
    #define DEBUG_PASS(f)
    #define DEBUG_FNUM 2
    #define DEBUG_VNUM 3
    #endif

    static inline error_t __attribute__((malloc)) *error_new(int error_code DEBUG_PARMS, char *message)
    {
        error_t *r = calloc(1, sizeof(error_t));

        *r = (error_t){ error_code, strdup(message) DEBUG_PASS(strdup) };
        return r;
    }

    static inline error_t __attribute__((format(printf,DEBUG_FNUM,0),malloc)) *error_newvf(int error_code DEBUG_PARMS,
                                                                                           char *format, va_list args)
    {
        error_t *r = calloc(1, sizeof(error_t));

        *r = (error_t){ error_code, NULL DEBUG_PASS(strdup) };
        if (vasprintf(&r->message, format, args) < 0)
            r->message = strdup(format);
        return r;
    }

    static inline error_t __attribute__((format(printf,DEBUG_FNUM,DEBUG_VNUM),malloc)) *error_newf(
        int error_code DEBUG_PARMS, char *format, ...)
    {
        error_t *r = NULL;
        va_list args;

        va_start(args, format);
        r = error_newvf(error_code DEBUG_PASS(), format, args);
        va_end(args);
        return r;
    }

    static inline void error_free(error_t *error)
    {
    #if DEBUG
        free(error->function);
        free(error->file);
    #endif
        free(error->message);
        free(error);
    }

    static inline void error_write(error_t *error, int fd, bool do_free)
    {
    #ifdef MACOSX
        extern char **_NSGetProgname(void);
        char *progname = *_NSGetProgname();
    #elif defined(LINUX)
        char buf[MAXPATHLEN + 1] = {0}, *progname = buf;
        if (readlink("/proc/self/exe", buf, MAXPATHLEN) < 0)
            progname = "unknown";
    #endif
    #if DEBUG
        dprintf(fd, "%s: %s (in %s at %s:%d)\n", basename(progname), error->message, error->function, error->file, error->line);
    #else
        dprintf(fd, "%s: %s\n", basename(progname), error->message);
    #endif
        if (do_free)
            error_free(error);
    }
```

The only really interesting part of this code is the part in `error_write()` which grabs the executable's name. Since it's not assumed that `argv` is available directly, some platform-specific code is invoked. On OS X, the `_NSGetProgname()` function from `crt_externs.h` is used, whereas on Linux, the contents of `/proc/self/exe` symlink are read. `dprintf()` is just `fprintf()` that takes a descriptor instead of a `FILE *`.

_For the curious, `__attribute__((malloc))` marks the function as returning a pointer that is guaranteed not to be aliased by any other pointers, which is useful for optimization purposes. `__attribute__((format(printf,n,m)))` simply tells the compiler to do the same checking of the format string and arguments that it would do for the `printf()` family of functions. These and the other attributes are documented in the [GCC Manual](http://gcc.gnu.org/onlinedocs/gcc-4.6.3/gcc/Attribute-Syntax.html#Attribute-Syntax)._

**Conclusion**  
This error handling trick takes a hybrid exception/error-object approach to the problem, and comes with a laundry list of drawbacks:

- Relies heavily on lots of compiler-specific language extensions which are definitely not universally portable
- , a qualifier which makes no sense to anyone looking at the code on Linux
- Severely abuses the preprocessor, making the actual functionality of the code obscure to a newcomer
- Severely abuses goto, resulting in a non-linear and unobvious control flow.
- Any variable that needs to be available in more than one of the blocks of the function must be declared outside the error handler scope
- Empty "catch" or "finally" handlers can't be ommitted
- Error handling scopes can't be nested
- The macros are somewhat poorly named in this implementation
- object around is cumbersome unless you're used to the

  style of error handling
- Probably isn't thread-safe (I haven't tested this)
- Doesn't emulate either exceptions or error objects perfectly, meaning experience from neither can be fully applied
- Is in no way superior to simply using C++'s exceptions unless you have an aversion to, or are unable to use, C++

This code is hastily designed, organically grown, has obvious inefficiencies, and is definitely not useful in a production environment in this form. Mostly, it's just a cool way of playing with the language. Still, it shows just how much a determined (and perhaps slightly unbalanced) mind can do with relatively crummy tools.

For some even more extreme examples of doing strange and unbelievable things in both C and Objective-C, I recommend looking into Justin Spahr-Summers' [`libextc`](https://github.com/jspahrsummers/libextc) and [`libextobjc`](https://github.com/jspahrsummers/libextobjc) libraries, which served as partial inspiration for the code I presented here. Both contain some of the most amazing and arcane uses of macros, `switch`, `if`, `for`, and [Duff's Device](http://en.wikipedia.org/wiki/Duff's_device) that I've ever encountered outside of the [IOCCC](http://www.ioccc.org/). To top it off, `libextc` manages to do all of its work while being completely platform- and compiler-agnostic, which is a true accomplishment.

That's about all for this week. Stay tuned for Mike's next article, coming to you a week from today. Thanks for reading!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
