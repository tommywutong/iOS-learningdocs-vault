---
title: 'Friday Q&A 2011-04-01: Signal Handling'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-04-01-signal-handling.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e9a6ec75d7235ac1'
translated: false
---

> 原文：[Friday Q&A 2011-04-01: Signal Handling](https://www.mikeash.com/pyblog/friday-qa-2011-04-01-signal-handling.html)　·　mikeash.com Friday Q&A

Posted at 2011-04-01 15:21 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Link: Implementing imp_implementationWithBlock](https://www.mikeash.com/pyblog/link-implementing-imp_implementationwithblock.html)  
Previous article: [Friday Q&A 2011-03-18: Random Numbers](https://www.mikeash.com/pyblog/friday-qa-2011-03-18-random-numbers.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [kqueue](https://www.mikeash.com/pyblog/?tag=kqueue) [signal](https://www.mikeash.com/pyblog/?tag=signal)

Friday Q&A 2011-04-01: Signal Handling

by [Mike Ash](https://www.mikeash.com/)

**Signals**  
 Signals are one of the most primitive forms of interprocess communication imaginable. A signal is just a small integer sent to a process. You can send a signal using the `kill` command, which also has a corresponding function available from C.

When a signal is delivered, it can terminate the process, pause/resume the process, be ignored, or invoke some custom code. That last option is called signal handling, and that is what I want to discuss today.

The list of defined signals can be seen in the header `sys/signal.h`. Many of these are used for familiar purposes. `SIGINT` is the signal generated when you press control-C in the shell. `SIGABRT` is used to kill your program when you call `abort()`, and `SIGSEGV` is the infamous segmentation fault, which pops up when you dereference a bad pointer.

Signal handling is esoteric and most programs don't need to worry about it at all. However, there are cases where it can be useful. For terminal and server programs, it's handy to catch `SIGHUP`, `SIGINT`, and other similar signals to do cleanup before exiting, as a sort of low-level version of Cocoa's `applicationWillTerminate:`. The `SIGWINCH` signal is handy for sophisticated terminal applications. `SIGUSR1` and `SIGUSR2` are user-defined signals which you can use for your own purposes.

**`sigaction`**  
 The lowest level interface for signal handling is the `sigaction` function. It provides some sophisticated and arcane options, but the important part is that it allows you to specify a function which is called when the signal in question is delivered:

```
    static void Handler(int signal)
    {
        // signal came in!
    }
    
    struct sigaction action = { 0 };
    action.sa_handler = Handler;
    sigaction(SIGUSR1, &action, NULL);
```

Nice and simple, right?

_Wrong._

**Reentrancy**  
 The problem is that signals are delivered asynchronously, and the function registered here is also invoked asynchronously. Code always has to run on a thread somewhere. Depending on how the signal is generated, the handler is either run on the thread that the signal is associated with (for example, a `SIGSEGV` handler will run on the thread that segfaulted) or it will run on an arbitrary thread in the process. The problem is that it's essentially an interrupt in userland, and whatever code was running when it came in will be paused until the handler is done.

As anyone who was around in the classic Mac days knows, writing code that runs in an interrupt is hard. The problem is _reentrancy_. Many people confuse reentrancy with thread safety, but they are not the same concept, although they are somewhat similar.

Thread safety means that a particular piece of code can run on multiple threads at the same time safely. Thread safety is most commonly accomplished by using locks. A call acquires a lock, does work, releases the lock. A second thread that comes along in the middle will block until the first thread is done.

If code is _reentrant_ that means that a particular piece of code can run multiple times _on the same thread_ safely. This is different and considerably harder.

What if you take the thread safety approach of locking and apply it to reentrancy? The first call acquires the lock. While it's active, the code is called again. It tries to acquire the lock, but the lock is already taken, so it blocks. However, the first call can't run until the second call is done. The second call can't run until the first call is done. The result is a frozen program.

Writing reentrant code is _hard_, and as a result very few system functions are reentrant. Because a signal handler functions as an interrupt, it can only call reentrant code. You can't call something as simple as `printf` safely, because `printf` could take a lock, and if there's already an active call to `printf` on the thread where the handler runs, you'll deadlock.

The `sigaction` man page gives a list of functions you are allowed to call from a signal handler. It's pretty limited.

The complete list is: `_exit()`, `access()`, `alarm()`, `cfgetispeed()`, `cfgetospeed()`, `cfsetispeed()`, `cfsetospeed()`, `chdir()`, `chmod()`, `chown()`, `close()`, `creat()`, `dup()`, `dup2()`, `execle()`, `execve()`, `fcntl()`, `fork()`, `fpathconf()`, `fstat()`, `fsync()`, `getegid()`, `geteuid()`, `getgid()`, `getgroups()`, `getpgrp()`, `getpid()`, `getppid()`, `getuid()`, `kill()`, `link()`, `lseek()`, `mkdir()`, `mkfifo()`, `open()`, `pathconf()`, `pause()`, `pipe()`, `raise()`, `read()`, `rename()`, `rmdir()`, `setgid()`, `setpgid()`, `setsid()`, `setuid()`, `sigaction()`, `sigaddset()`, `sigdelset()`, `sigemptyset()`, `sigfillset()`, `sigismember()`, `signal()`, `sigpending()`, `sigprocmask()`, `sigsuspend()`, `sleep()`, `stat()`, `sysconf()`, `tcdrain()`, `tcflow()`, `tcflush()`, `tcgetattr()`, `tcgetpgrp()`, `tcsendbreak()`, `tcsetattr()`, `tcsetpgrp()`, `time()`, `times()`, `umask()`, `uname()`, `unlink()`, `utime()`, `wait()`, `waitpid()`, `write()`, `aio_error()`, `sigpause()`, `aio_return()`, `aio_suspend()`, `sem_post()`, `sigset()`, `strcpy()`, `strcat()`, `strncpy()`, `strncat()`, `strlcpy()`, `strlcat()`.

Finally, the list ends with this amusing note: "...and perhaps some others." "Perhaps" is not a nice word to run into in this sort of documentation.

You can call your own reentrant code, but you probably don't have any, because it's hard to write, it can't call any system functions except from the above list, and you never had any reason to write it before. For the Objective-C types, note that `objc_msgSend` is not reentrant, so you cannot use any Objective-C from a signal handler.

There is very little that you can do safely. There is so little that I'm not even going to discuss how to get anything done, because it's so impractical to do so, and instead will simply tell you to avoid using signal handlers unless you really know what you're doing and you enjoy pain.

Fortunately, there are better ways to do these things.

**`kqueue`**  
 One of those better ways is to use `kqueue`. This is a low level operating service which allows a program to monitor many different events, and one of the events it can monitor is signals. You can create a `kqueue` just for signal handling, or you can add a signal handling event to an existing `kqueue` you already have within your program.

Setting things up is a bit more involved, but all in all not too hard. First, the `kqueue` is created:

```
    int fd = kqueue();
```

Next, add the signal filter to the queue:

```
    struct kevent event = { SIGUSR1, EVFILT_SIGNAL, EV_ADD, 0, 0 };
    kevent(fd, &event, 1, NULL, 0, NULL);
```

This tells the

to watch for

being delivered to the process. Note that

exists separately from the lower level

handling. Because we don't want the program to terminate when the signal is delivered, which is the default behavior, we also have to tell

to ignore it:

```
    struct sigaction action = { 0 };
    action.sa_handler = SIG_IGN;
    sigaction(SIGUSR1, &action, NULL);
```

The

is now ready. We can wait for it to receive an event by calling

again, this time not adding anything, but having it give us an event:

```
    struct kevent event;
    int count = kevent(fd, NULL, 0, &event, 1, NULL);
    if(count == 1)
    {
        if(event.filter == EVFILT_SIGNAL)
            printf("got signal %d\n", (int)event.ident);
    }
```

Note that because the handler runs normally, we can safely use

or any other code when handling the signal. Convenient!

`kqueue` isn't always all that convenient to use in real programs, though. There are two reasonable ways to do it. One way is to have a dedicated signal handling thread which sits in a loop calling `kevent` repeatedly. Another way is to add the `kqueue` file descriptor to your runloop using something like `CFFileDescriptor` to integrate it with your Cocoa runloop. However neither of these is particularly great.

**GCD**  
 Finally we reach a signal handling solution which is extremely easy to use: Grand Central Dispatch. In addition to the better-known multiprocessing capabilities, GCD also includes a full suite of event monitoring abilities which match those of `kqueue`. (And in fact, GCD implements them using `kqueue` internally.)

To handle a signal with GCD, we create a dispatch source to monitor the signal:

```
    dispatch_source_t source = dispatch_source_create(DISPATCH_SOURCE_TYPE_SIGNAL, SIGUSR1, 0, dispatch_get_global_queue(0, 0));
```

Next, we set its event handler with a block to execute, and then resume the source to make it active:

```
    dispatch_source_set_event_handler(source, ^{
        printf("got SIGUSR1\n");
    });
    dispatch_resume(source);
```

Like with

, this exists separately from

, so we have to tell

to ignore the signal:

```
    struct sigaction action = { 0 };
    action.sa_handler = SIG_IGN;
    sigaction(SIGUSR1, &action, NULL);
```

That's it! Every time a `SIGUSR1` comes in, the handler is called. Because the source targets a global queue, the handler automatically runs in a background thread without interfering with anything else. If you prefer, you can give GCD a custom queue, or even the main queue, to control where the handler runs. Like with `kqueue`, because the handler runs normally on a normal thread, it's safe to do anything in it that you would do in any other piece of code. GCD makes signal handling convenient, easy, and safe.

**Conclusion**  
 Signal handling is a rare requirement, but sometimes useful. Using the low level `sigaction` to handle signals makes life unbelievably hard, as the signal handler is called in such a way as to place extreme restrictions on the code it contains. This makes it almost impossible to do anything useful in such a signal handler.

The best way to handle a signal in almost every case is to use GCD. Signal handling with GCD is easy and safe. On the rare occasions where you need to handle signals, GCD lets you do it with just a few lines of code.

If you can't or don't want to use GCD but still want to avoid `sigaction`, `kqueue` provides a good middle ground. While it's more complicated to set up and manage than the GCD approach, it still works well to handle signals in a reasonable manner.

That wraps up today's April Fool's edition of Friday Q&A. Come back in two weeks for the next one. Until then, as always, keep sending me your ideas for topics. Friday Q&A is driven by reader suggestions, so if you have something you would like to see covered, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
