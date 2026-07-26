---
title: 'Friday Q&A 2014-06-06: Secrets of dispatch_once'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-06-06-secrets-of-dispatch_once.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b123985c08c83fa4'
translated: false
---

> 原文：[Friday Q&A 2014-06-06: Secrets of dispatch_once](https://www.mikeash.com/pyblog/friday-qa-2014-06-06-secrets-of-dispatch_once.html)　·　mikeash.com Friday Q&A

Posted at 2014-06-06 13:27 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2014-06-20: Interesting Swift Features](https://www.mikeash.com/pyblog/friday-qa-2014-06-20-interesting-swift-features.html)  
Previous article: [Friday Q&A 2014-05-23: A Heartbleed-Inspired Paranoid Memory Allocator](https://www.mikeash.com/pyblog/friday-qa-2014-05-23-a-heartbleed-inspired-paranoid-memory-allocator.html)  
Tags: [atomic](https://www.mikeash.com/pyblog/?tag=atomic) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [threading](https://www.mikeash.com/pyblog/?tag=threading)

Friday Q&A 2014-06-06: Secrets of dispatch_once

by [Mike Ash](https://www.mikeash.com/)

**The API**  
The behavior of `dispatch_once` is in the name. It does something once and only once.

It takes two parameters. The first is a predicate that tracks the "once". The second is a block to execute on the first call. Calls look like this:

```
    static dispatch_once_t predicate;
    dispatch_once(&predicate, ^{
        // some one-time task
    });
```

It's a great API for lazily initializing shared state, whether it's a global dictionary, a singleton instance, a cache, or anything else that needs a bit of setup the first time through.

In a single-threaded world, this call would be kind of boring and could be replaced with a simple `if` statement. However, we live in a multithreaded world, and `dispatch_once` is thread safe. It's guaranteed that multiple simultaneous calls to `dispatch_once` from multiple threads will only execute the block once, and all threads will wait until execution is complete before `dispatch_once` returns. Even that is not _too_ hard to accomplish on your own, but `dispatch_once` is also extremely fast, and that is really tough to pull off.

**Single-Threaded Implementation**  
Let's first look at a simplistic single-threaded implementation of the function. This is just about useless in a practical sense, but it's good to be have a concrete view of the semantics. Note that `dispatch_once_t` is just a `typedef` for `long`, initialized to zero, and with the meaning of other values left up to the implementation. Here's the function:

```
    void SimpleOnce(dispatch_once_t *predicate, dispatch_block_t block) {
        if(!*predicate) {
            block();
            *predicate = 1;
        }
    }
```

The implementation is easy: if the predicate contains zero, call the block and set it to one. Subsequent calls will see the one and not call the block again. Exactly what we want, aside from being completely unsafe in a multithreaded environment. Two threads could hit the `if` statement simultaneously, causing them both to call the block, and that's bad. Unfortunately, as is often the case, making this code thread safe means a substantial performance hit.

**Performance**  
When talking about the performance of `dispatch_once`, there are really three different scenarios to consider:

1. The first ever call to `dispatch_once` with a given predicate, which executes the block.
2. Calls to `dispatch_once` after the first call, but before the block finishes executing. Here, callers have to wait for the block before they proceed.
3. Calls to `dispatch_once` after the first call and after the block has executed. No waiting is required and they can immediately proceed.

The performance of scenario #1 is largely unimportant, as long as it's not absurdly slow. It only happens once, after all.

The performance of scenario #2 is similarly unimportant. It could happen potentially several times, but it only happens while the block is executing. In most cases, it never happens at all. If it does, it probably only happens once. Even in a torture test where lots of threads call `dispatch_once` simultaneously and the block takes a long time to execute, the number of calls is still going to be limited to thousands. Those calls all have to wait for the block anyway, so it's not that big of a deal if they burn some unnecessary CPU time while they do it.

The performance of scenario #3 is enormously important. Calls of this nature could happen potentially millions or billions of times as a program executes. We want to be able to use `dispatch_once` to protect one-time calculations whose results are used all over the place. Ideally, sticking `dispatch_once` on a computation should cost no more than explicitly doing the computation ahead of time and returning the result from some global variable. In other words, once you hit scenario #3, we really want these two chunks of code to perform identically:

```
    id gObject;

    void Compute(void) {
        gObject = ...;
    }

    id Fetch(void) {
        return gObject;
    }

    id DispatchFetch(void) {
        static id object;
        static dispatch_once_t predicate;
        dispatch_once(&predicate, ^{
            object = ...;
        });
        return object;
    }
```

When inlined and optimized, the `SimpleOnce` function comes close to achieving this. In my testing, on my computer, it takes about half a nanosecond to execute. That, then, will be the gold standard for thread-safe versions.

**Locks**  
The standard way to make something thread safe is to surround all access to shared data with a lock. It's a little tricky here, because there isn't a good place to put the lock next to the data it's protecting. `dispatch_once_t` is just a long, and there's no room for a lock.

We could just modify the API to take a structure that contains a lock and a flag. But in the interests of retaining the same signature as `dispatch_once`, and because this is just illustrative code, I decided to go with a single global lock instead. The code uses a `static pthread_mutex_t` to protect all accesses to the predicate. In a real program, with many different predicates, this would be a terrible idea, as unrelated predicates would still wait on each other. For a quickie example where I'm only testing with one predicate anyway, it's fine. The code is the same as before, except with a lock around it:

```
    void LockedOnce(dispatch_once_t *predicate, dispatch_block_t block) {
        static pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

        pthread_mutex_lock(&mutex);
        if(!*predicate) {
            block();
            *predicate = 1;
        }
        pthread_mutex_unlock(&mutex);
    }
```

This code is thread safe, but unfortunately it's much slower. On my computer, it takes about 30 nanoseconds per call, compared to half a nanosecond for the previous version. Locks are pretty fast, but not when nanoseconds count.

**Spinlocks**  
A spinlock is a way to implement a lock that tries to minimize overhead in the lock itself. The name comes from how a spinlock implementation "spins" on the lock when it has to wait, repeatedly polling it to see if it's been released. A normal lock will coordinate with the OS to sleep waiting threads, and wake them up when the lock is released. This saves CPU time, but the additional coordination doesn't come for free. By cutting down on that, a spinlock saves time in the case where the lock isn't held, at the expense of less efficient behavior when multiple threads try to take the lock at the same time.

OS X provides [a convenient API for spinlocks](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man3/spinlock.3.html) with the `OSSpinLock` functions. Implementing `LockedOnce` with `OSSpinLock` is just a matter of changing out a few names:

```
    void SpinlockOnce(dispatch_once_t *predicate, dispatch_block_t block) {
        static OSSpinLock lock = OS_SPINLOCK_INIT;

        OSSpinLockLock(&lock);
        if(!*predicate) {
            block();
            *predicate = 1;
        }
        OSSpinLockUnlock(&lock);
    }
```

This is a considerable improvement, clocking in at about 6.5 nanoseconds per call on my computer, versus 30 nanoseconds per call for the `pthread_mutex` version. However, it's still well short of the half-nanosecond time of the unsafe version.

**Atomic Operations**  
Atomic operations are low-level CPU operations that are always thread safe even without locks. (Technically, they use locks at the hardware level, but that's an implementation detail.) They are what you use to implement locks in the first place. When locks carry too much overhead, directly using atomic operations can be a way to improve performance. Threaded programming without locks can be extremely tricky, so it's not a good idea to do it unless you really, really need it. In this case, we're talking about an OS library that could get a lot of use, so it probably qualifies.

The building block of atomic operations is the compare and swap. This is a single operation that performs the equivalent of:

```
    BOOL CompareAndSwap(long *ptr, long testValue, long newValue) {
        if(*ptr == testValue) {
            *ptr = newValue;
            return YES;
        }
        return NO;
    }
```

In words, it tests to see if a location in memory contains a particular value, and replaces it with a new value if so. It returns whether the value matched. Because compare and swap is implemented as an atomic CPU instruction, you're guaranteed that if multiple threads all try to do the same compare-and-swap on a memory location, only one will succeed.

The implementation strategy for this version of the function is to assign three values to the predicate. `0` means that it's never been touched. `1` indicates that the block is currently being executed, and any callers should wait for it. `2` indicates that the block has completed and all callers can return.

A compare and swap will be used to check for `0` and atomically transition to `1` in that case. If that succeeds, then that thread is the first one to make the call, and it will then run the block. After running the block, it will set the predicate to `2` to indicate that it's done.

If the compare and swap fails, then it will just enter a loop, checking for `2` repeatedly until it succeeds. This will cause it to wait for the other thread to finish executing the block.

The first step is to convert the predicate pointer into a `volatile` pointer, to convince the compiler that the value could be changed by other threads in the middle of the function:

```
    void AtomicBuiltinsOnce(dispatch_once_t *predicate, dispatch_block_t block) {
        volatile dispatch_once_t *volatilePredicate = predicate;
```

Then comes the compare and swap. Gcc and clang both provide various builtin functions beginning with `__sync` that implement atomic operations. There are also newer ones beginning with `__atomic`, but for this experiment I stuck with what I knew. This call does an atomic compare and swap on predicate, testing for `0` and setting it to `1` if it matches:

```
        if(__sync_bool_compare_and_swap(volatilePredicate, 0, 1)) {
```

The function returns `true` if the operation succeeded. In this case, that means that the predicate was `0` and this call is the first one. That means that the next task is to call the block:

```
            block();
```

Once the block completes, it's time to set the predicate to `2` to indicate that fact to any waiting threads, and to any future callers. However, before that, we need a memory barrier to ensure that everyone sees the proper ordering of reads and writes. More on that in a little bit. The `__sync_synchronize` builtin function performs a memory barrier:

```
            __sync_synchronize();
```

Then the predicate can safely be set:

```
            *volatilePredicate = 2;
        } else {
```

If the predicate was not `0`, then enter a loop to wait for it to become `2`. If it's already `2`, this loop will terminate immediately. If it's `1`, then it will sit on the loop, constantly retesting the predicate value, until it becomes `2`:

```
            while(*volatilePredicate != 2)
                ;
```

Before returning, there needs to be a memory barrier here as well, to match the barrier above. Again, more on this in a little bit:

```
            __sync_synchronize();
        }
    }
```

This works, and should be safe. (Lockless threaded code is tricky enough that I don't want to declare that outright without more thought than I've put into it already. But this is a fairly simple scenario, and in any case we're not actually trying to build something production-worthy here.)

How's performance? Turns out, not so good. On my computer, it takes about 20 nanoseconds per call, quite a bit higher than the spinlock version.

**Early Bailout**  
There's an obvious optimization that can be applied to this code. The common case is when `predicate` contains `2`, but the code first tests for `0`. By first testing for `2` and bailing out early, the common case can be made faster. The code for this is simple: add a check for `2` at the top of the function, and if it succeeds, return after a memory barrier:

```
    void EarlyBailoutAtomicBuiltinsOnce(dispatch_once_t *predicate, dispatch_block_t block) {
        if(*predicate == 2) {
            __sync_synchronize();
            return;
        }

        volatile dispatch_once_t *volatilePredicate = predicate;

        if(__sync_bool_compare_and_swap(volatilePredicate, 0, 1)) {
            block();
            __sync_synchronize();
            *volatilePredicate = 2;
        } else {
            while(*volatilePredicate != 2)
                ;
            __sync_synchronize();
        }
    }
```

This is a decent improvement over the first version of the code, at about 11.5 nanoseconds per call. However, this is still much slower than the goal of half a nanosecond, and it's even slower than the spinlock code.

Memory barriers aren't free, and that explains why this code is so much slower than the goal. As for why it's slower than spinlocks, there are different kinds of memory barriers available. `__sync_synchronize` generates an `mfence` instruction, which is the most paranoid one possible, working with such exotica as SSE4 streaming reads/writes, while `OSSpinLock` sticks with a cheaper one suitable for normal code. We could fiddle around with the precise barrier used in this code to get better performance, but it's apparent that the cost is still going to be higher than we want, so I'll skip over that.

**Unsafe Early Bailout**  
Let's look at one more version of the code. It's identical to the previous one, except it gets rid of the memory barriers:

```
    void UnsafeEarlyBailoutAtomicBuiltinsOnce(dispatch_once_t *predicate, dispatch_block_t block) {
        if(*predicate == 2)
            return;

        volatile dispatch_once_t *volatilePredicate = predicate;

        if(__sync_bool_compare_and_swap(volatilePredicate, 0, 1)) {
            block();
            *volatilePredicate = 2;
        } else {
            while(*volatilePredicate != 2)
                ;
        }
    }
```

Unsurprisingly, this performs just as fast as `SimpleOnce` at about half a nanosecond per call. Since `*predicate == 2` is by far the common case, nearly every call just performs that check and returns. This performs the same amount of work as `SimpleOnce` in the case where the block has already been called.

However, as the name indicates, the lack of memory barriers makes it unsafe. Why?

**Branch Prediction, Out of Order Execution, and You**  
We imagine that our CPUs are simple machines. We tell them to do one thing, and they do it. Then we tell them to do the next thing, and they do it. This repeats until we get bored or the power goes out.

Once upon a time, this was actually true. Old CPUs really were simple machines that worked exactly like this. They fetched an instruction, and they executed it. Then they fetched the next instruction, and they executed it.

Unfortunately, while this approach is simple, cheap, and easy, it's also not very fast. Moore's Law has blessed us with an ever-growing number of transistors to pile into CPUs. The 8086 was built from about 29,000 transistors. An Intel Haswell-architecture CPU contains well over a billion transistors.

The market, desiring better computer games (as well as a few people wanting to more quickly perform various boring business tasks that aren't really worth mentioning) demanded that CPU makers use these advances for better performance. The modern CPU is the product of decades of work to turn more transistors into faster computers.

There are a lot of tricks that go into making CPUs faster. One of those is pipelining. When you look at what goes into executing a single CPU instruction, there are a lot of little steps:

```
    1. Load the instruction from memory.
    2. Decode the instruction. (That is, figure out which instruction it is, and figure out what the operands are.)
    3. Load the input data.
    4. Perform the operation on the input data.
    5. Save the output.
```

On an early CPU, the sequence of work would look something like:

```
    load instruction
    decode
    load data
    operation
    save data
    load instruction
    decode
    load data
    operation
    save data
    ...
```

But as long as you have the resources for it, you can actually perform many of these actions in parallel. On a pipelined CPU, the sequence of work can end up looking more like this:

```
    load instruction
    decode                load instruction
    load data             decode                load instruction
    operation             load data             decode
    save data             operation             load data
                          save data             operation
                                                save data
```

This is a lot faster! With enough transistors, things can become even more complex, with many instructions executing in parallel simultaneously.

Going even beyond this, instructions can be executed completely out of order if it looks like this will speed things up. Unlike the simplified example above, real-world instructions tend to require more steps _and_ there is a lot of variance in how many steps they take. For example, reads and writes to main memory can take an enormous amount of time. By executing other work that comes afterwards in the instruction stream, the CPU can engage in productive work instead of sitting idle. Because of this, the CPU may find it advantageous to issue memory reads and writes out of order from how the corresponding instructions appear in the instruction stream.

The end result of all this stuff is that your code doesn't always run in the order it looks like it runs in. If you write:

```
    x = 1;
    y = 2;
```

Your CPU can perform the write to `y` first. The compiler can also reorder statements like this in some cases, but even if you eliminate that, the CPU can still do it. If you have more than one CPU in your system (as we pretty much always do these days) then other CPUs will see these out of order writes. Even if the writes are performed in order, other CPUs can perform out of order _reads_. Put it all together, and another thread that's reading `x` and `y` can see `y = 2` while still seeing the old value for `x`.

Sometimes you absolutely need these values to be written and read in the proper order, and that's where memory barriers come in. Adding a memory barrier to the above code ensures that `x` is written first:

```
    x = 1;
    memory_barrier();
    y = 2;
```

Similarly, a barrier when reading ensures that reads are performed in the proper order:

```
    use(x);
    memory_barrier();
    use(y);
```

However, because the memory barrier's entire purpose in life is defeating the CPU's attempts to go faster, there is an inherent performance penalty.

This comes into play with `dispatch_once` and lazy initialization because there are multiple reads and writes done in sequence and their order is extremely important. For example, the typical lazy object initialization pattern looks like:

```
    static SomeClass *obj;
    static dispatch_once_t predicate;
    dispatch_once(&predicate, ^{ obj = [[SomeClass alloc] init]; });
    [obj doStuff];
```

If `obj` was read before `predicate`, then it's possible that this code could read it when it still contains `nil`, right before another thread writes the final value out to the variable and sets `predicate`. This code could then read `predicate` as indicating that the job is done, and thus proceed with using the uninitialized `nil`. It's even conceivable that this code could read the correct value for `obj` but read uninitialized values from the memory allocated for the object, causing a crash when trying to send `doStuff`.

Thus, `dispatch_once` needs a memory barrier. But as we've seen, memory barriers are relatively slow, and we don't want to pay that price in the common case if we can avoid it.

**Branch Prediction and Speculative Execution**  
The pipelined, out-of-order model works great for a linear sequence of instructions, but trouble arises for conditional branches. The CPU doesn't know where to start fetching more instructions until the branch condition can be evaluated, which typically depends on the immediately preceding instructions. The CPU has to stop, wait for the previous work to finish, then evaluate the branch condition and resume execution. This is called a pipeline stall, and can cause a significant performance penalty.

In order to compensate for that, CPUs engage in speculative execution. When they see a conditional branch, they make a guess as to which way they think the branch will go. Modern CPUs have sophisticated branch prediction hardware that can typically guess correctly over 90% of the time. They begin executing instructions from the guessed branch, instead of just waiting for the branch condition to be evaluated. If it turns out that the guess was correct, then it just keeps going. If the guess was wrong, it throws away all of the speculative execution and restarts on the other branch.

It is specifically this scenario that's at play on the read side of `dispatch_once`, the side that we want to make as fast as possible. There is a conditional branch on the value of `predicate`. The CPU should predict that the branch will take the common path, which bypasses running the block and immediately returns. During speculative execution of this branch, the CPU might load subsequent values from memory before they have been initialized by another thread. If that guess ended up being correct, then it commits the speculative execution which used uninitialized values.

**Unbalancing Barriers**  
Write barriers generally need to be symmetrical. There's one on the write side to ensure that writes are done in the proper order, and one on the read side to ensure that reads are done in the proper order. However, our performance needs in this particular case are completely asymmetrical. We can tolerate a huge slowdown on the write side, but we want the read side to be as fast as possible.

The trick is to defeat the speculative execution that causes the problem. When the branch prediction is incorrect, the results of the speculative execution are discarded, and that means discarding the potentially uninitialized values in memory. If `dispatch_once` can _force_ a branch mispredict after the initialized values become visible to all CPUs, the problem is avoided.

There's a critical interval of time between the earliest possible speculative memory read after the conditional branch on `predicate` and when the conditional branch is actually evaluated. The exact length of that interval will depend on the design of the specific CPU, but it will generally be in the low dozens of CPU cycles at most.

If the write side waits at least that much time between writing out the initialized values and writing the final value to `predicate`, all is well. It gets a bit tricky to ensure, though, since all of that crazy out-of-order execution comes into play once again.

On Intel CPUs, `dispatch_once` abuses the `cpuid` instruction for this purpose. The `cpuid` instruction exists to get information about the identity and capabilities of the CPU, but it also forcibly serializes the instruction stream and takes a decent amount of time to execute, hundreds of cycles on some CPU models, which is enough to do the job.

If you look at the implementation of `dispatch_once`, you'll see no barriers whatsoever on the read side:

```
    DISPATCH_INLINE DISPATCH_ALWAYS_INLINE DISPATCH_NONNULL_ALL DISPATCH_NOTHROW
    void
    _dispatch_once(dispatch_once_t *predicate, dispatch_block_t block)
    {
        if (DISPATCH_EXPECT(*predicate, ~0l) != ~0l) {
            dispatch_once(predicate, block);
        }
    }
    #define dispatch_once _dispatch_once
```

This is in the header, and always inlined into the caller. `DISPATCH_EXPECT` is a macro that tells the compiler to emit code that tells the CPU that the branch where `*predicate` is `~0l` is the more likely path. This can improve the success of branch prediction, and thus improve performance. Ultimately, this is just a plain `if` statement with no barriers of any kind. Performance testing bears this out: calls to the real `dispatch_once` match the 0.5ns goal.

The write side can be found in the implementation. After calling the block and before doing anything else, `dispatch_once` uses this macro:

```
    dispatch_atomic_maximally_synchronizing_barrier();
```

On Intel, the macro generates a `cpuid` instruction, and it generates the appropriate assembly when targeting other CPU architectures.

**Conclusion**  
Multithreading is a strange and complicated place, made all the more so by modern CPU designs which can do many things behind your back. Memory barriers allow you to inform the hardware when you really need things to happen in a certain order, but they come at a cost. The unique requirements of `dispatch_once` allow it to work around the problem in an unconventional way. By waiting a sufficiently long time between the relevant memory writes, it ensures that readers always see a consistent picture without needing to pay the cost of a memory barrier on every access.

That's it for today. Come back next time for more exciting stuff, probably about Swift since that's all the talk these days. If you have a topic you'd like to see covered here, and it's something besides "talk about Swift" (which is a fine topic but has sufficient requests at this point), please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2014-06-06-secrets-of-dispatch_once.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
