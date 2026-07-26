---
title: 'Friday Q&A 2012-01-20: Fork Safety'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-01-20-fork-safety.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:932e62fc4b596219'
translated: false
---

> 原文：[Friday Q&A 2012-01-20: Fork Safety](https://www.mikeash.com/pyblog/friday-qa-2012-01-20-fork-safety.html)　·　mikeash.com Friday Q&A

Posted at 2012-01-20 14:07 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [The Mac Toolbox: Followup](https://www.mikeash.com/pyblog/the-mac-toolbox-followup.html)  
Previous article: [Plausible Labs is Hiring](https://www.mikeash.com/pyblog/plausible-labs-is-hiring.html)  
Tags: [fork](https://www.mikeash.com/pyblog/?tag=fork) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [posix](https://www.mikeash.com/pyblog/?tag=posix) [process](https://www.mikeash.com/pyblog/?tag=process) [safety](https://www.mikeash.com/pyblog/?tag=safety) [threading](https://www.mikeash.com/pyblog/?tag=threading)

Friday Q&A 2012-01-20: Fork Safety

by [Mike Ash](https://www.mikeash.com/)

**Fork/Exec**  
The `fork` call is the standard UNIX way to create a new process. It's an unusual call in that it returns twice for each call: once in the original process, and once in the new one.

If you aren't already familiar with the concept, it can be tough to wrap your head around it. A little example may help:

```
    pid_t processID = fork();
    // if successful, fork returns twice here
    // in the parent, it returns with processID set to the pid of the child
    // in the child, it returns with processID set to 0

    // check for errors first
    if(processID == -1)
    {
        // handle the error here
    }
    else if(processID == 0)
    {
        // this code only runs in the child process
    }
    else
    {
        // this code only runs in the parent process, and processID
        // contains the child's process identifier
    }
```

Unlike most OSes, UNIX separates the concept of creating a new process from starting a new program. The `fork` call creates a new process which runs the same program as before. The `exec` family of calls is the companion which runs a new program, without creating a new process. To start a new program in a new process, the standard way to do it in UNIX is to call `fork`, then `exec`.

For example, the code to start a shell in a subprocess and pass it a command would look something like this:

```
    pid_t processID = fork();

    if(processID == 0)
    {
        execl("/bin/sh", "/bin/sh", "-c", "some shell command here", (char *)NULL);
        // if successful, exec never returns, because the new program
        // begins executing, replacing the old one
        // any code which runs at this point is therefore due to failure
        char errstr[] = "Error calling execl, exiting the child.\n";
        write(STDERR_FILENO, errstr, sizeof(errstr));
        _exit(1);
    }

    // parent is the only one that could be running here
    // proceed from here with the new process running
```

This technique is losing favor these days, as newer, more efficient APIs like `posix_spawn` come along. Still, this is a common way to do things.

**Safe Code in the Child Process**  
You'll notice that the error handling code in the example above is a little weird. Normal error handling code in a case like that would call `fprintf` and then `exit`.

The environment in the child process is harsh and makes it difficult to write correct code to run there. Anything you do beyond a direct call to an `exec` function has to be done with great care. That's why the error handling code is written the way it is.

To understand why this is, it's best to think of how `fork` would be implemented in the kernel and what implications that has for the child process.

At the most basic, conceptual level, `fork` simply makes a duplicate of the calling process. The kernel just takes all of the stuff associated with the process, like open file descriptors, memory, and execution state, and replicates it into a new process. (Memory is typically done with a copy-on-write scheme for efficiency.) The copy is modified slightly to give a different return value from `fork`, and then the new process is started.

Back in the early days, that was it. The new process is the same as the old, and they can go their separate ways.

Then multithreading came along and messed everything up. In the early days of UNIX, a process's execution state contained only a single thread, which was, of course, the one calling `fork`. Once a process has multiple threads, though, what do you do with them when you copy the process?

If you copy all of the threads, then you're in serious trouble when the child process starts up. Imagine, for example, that one thread in the parent calls `fork` while another one is writing some data to a file. After the `fork` completes, the parent continues writing to the file. Meanwhile, the child starts up and it also continues writing to the file, resulting in a bunch of corrupted data. Not good!

If all threads were copied, then all threads would need to be aware of any calls to `fork` and prepare themselves accordingly. This would defeat any hope of modularity in any program that called `fork`.

The solution is to only copy the thread that called `fork`. All others get left behind in the parent. (In practice, the other threads' stacks would be copied, in case there are any references to them from elsewhere, but not their execution state.) From the point of view of the child, it looks like all other threads were killed by the call to `fork`.

This is better, but still bad. Killing threads is violent and dangerous. You can often get away with it, but if the thread was in the middle of something important, it will never finish (from the point of view of the child). If the thread held a lock, that lock will never be unlocked.

That last part is important. Locks are used all over the place to make code safe when called from multiple threads. For example, `malloc` uses locks. So, occasionally, does `objc_msgSend`, which is called every time you write a `[]` message send expression in Objective-C.

Imagine that another thread was in the middle of a call to `malloc`, with a lock held, when you call `fork`. Afterwards, in the child process, you call `malloc` (or call something which calls something which calls `malloc`) and it tries to take the same lock. It will see that the lock is already held, and wait. It will wait forever, since the thread that was going to release it is now dead.

Thus, you can only safely call code that's guaranteed not to suffer from this problem. As it happens, the allowed APIs are the same as those can be called [from a signal handler](https://www.mikeash.com/pyblog/friday-qa-2011-04-01-signal-handling.html). See the `sigaction` man page for the full list.

You'll notice that this list is really small. `fprintf` is not on it, and neither is `exit`. However, `write` is allowed, as is `_exit`. Therefore you can see why I wrote the error handling code the way I did. (If you're wondering, `_exit` is a sort of shortcut way to exit your process which skips a lot of cleanup.)

**Working Around the Limits**  
You can make very few calls in the child process after a `fork`. Yet, you often have setup that you want to do before calling `exec` to start a new executable. How can you reconcile these two opposing forces?

In general, the answer is to do as much as possible before the call to `fork`. This may entail doing some cleanup in the parent afterwards, which is annoying but ultimately necessary for correct code. For example, you might write this incorrect code to get the `exec` path from an `NSString`:

```
    pid_t processID = fork();

    if(processID == 0)
    {
        execl([path fileSystemRepresentation], ...);
```

This is incorrect due to running unsafe code in the child process. The call to `-fileSystemRepresentation` invokes `objc_msgSend`, probably allocates memory, and may make any number of other unsafe calls. The fix here is easy, though. Just fetch the path beforehand:

```
    const char *pathCStr = [path fileSystemRepresentation];

    pid_t processID = fork();

    if(processID == 0)
    {
        execl(pathCStr, ...);
```

We don't need any cleanup code in the parent, since `pathCStr` is effectively autoreleased. There's a slight performance penalty here, since `pathCStr` has to be deallocated in the parent, but it's negligible and a small price to pay for correctness.

As another example, you may have a list of file descriptors that need to be closed in the child. Here's an incorrect example of fetching those descriptors from an `NSArray`:

```
    pid_t processID = fork();

    if(processID == 0)
    {
        for(NSNumber *fdObj in fdArray)
            close([fdObj intValue]);
```

Enumerating over the array and calling `intValue` are both unsafe. However, this code can't simply be moved earlier, since we don't want to close these file descriptors in the parent, only the child. The answer here is to convert the array into a data structure we can safely access in the child, like a C array:

```
    NSUInteger fdArrayCount = [fdArray count];

    int *fdArrayC = malloc(fdArrayCount * sizeof(*fdArrayC));
    int *fdArrayCursor = fdArrayC;

    for(NSNumber *fdObj in fdArray)
        *fdArrayCursor++ = [fdObj intValue];

    pid_t processID = fork();

    if(processID == 0)
    {
        for(NSUInteger i = 0; i < fdArrayCount; i++)
            close(fdArrayC[i]);
        ...
    }

    free(fdArrayC);
```

One place where this gets trickier is when customizing the child's environment. The most natural way to do this would be to call `setenv` to set the customized environment variables. However, there's no good plase to call that function. You can't do it after the `fork`, as it's not a safe API. You can't do it before the `fork`, as the environment is shared state and another thread may overwrite your change before you get to the `fork`.

Fortunately, this can be worked around by skipping `setenv` altogether, and instead setting the environment simultaneous with starting the new executable by calling `execve`. This call takes a path, and array of arguments, and an array of environment variables. Of course, you must be sure to allocate and fill out these arrays before calling `fork`, but that can be done without too much trouble.

**Writing a Safe API**  
If for some reason you want to create an API that needs to work on the child side of a `fork`, you need to exercise the same caution as when writing child-side code directly. Your use of APIs must be extremely limited. As such, it's usually not practical to do this.

However, if you really want to do it, you may find yourself needing to do some extra work around the `fork` call to prepare. It's impractical to require every call to `fork` to also contain your API's preparation code, but fortunately there's a built-in facility for this. You can register callbacks using `pthread_atfork`. You register one callback to run before the `fork`, then one to run afterwards in the parent, and a third to run afterwards in the child. You could use this to force the `fork` to wait for locks to be released and data structures to be consistent, or you could simply use it to put the child side into a special mode which avoids unsafe operations.

Overall, though, you generally want to `fork` and then immediately `exec`, so designing an API to be safely used in between is mostly pointless.

**Conclusion**  
There's little call to use `fork` these days (and you can't use it at all on iOS), but it does occasionally pop up. Unsafe code after a `fork` is extremely common, so beware. Even if you never write a `fork` call yourself, the history and constraints behind it offer an interesting perspective on how the system as a whole is put together.

That's it for today. Come back next time for another exciting dive into weird programming stuff. In case this is your first time reading, it just so happens that Friday Q&A is driven by reader ideas, so if you have an idea for a topic that you'd like to see covered, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-01-20-fork-safety.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
