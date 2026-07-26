---
title: a post on defensive programming
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-10-09-defensive-programming.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5a8e1ca53887c821'
translated: false
---

> 原文：[a post on defensive programming](https://www.mikeash.com/pyblog/friday-qa-2009-10-09-defensive-programming.html)　·　mikeash.com Friday Q&A

Posted at 2009-10-09 16:03 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [XBolo is Out!](https://www.mikeash.com/pyblog/xbolo-is-out.html)  
Previous article: [Friday Q&A 2009-10-02: Care and Feeding of Singletons](https://www.mikeash.com/pyblog/friday-qa-2009-10-02-care-and-feeding-of-singletons.html)  
Tags: [defensive](https://www.mikeash.com/pyblog/?tag=defensive) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2009-10-09: Defensive Programming

by [Mike Ash](https://www.mikeash.com/)

**Evolution of the Programmer**  
 If you're like most programmers, your first enemy when learning to program was the compiler. You'd type in a perfectly good program, but the thing would spit out these cryptic errors at you. You'd go poring over the code looking for that missing semicolon or misspelled variable.

Eventually, you tamed the compiler. Your programs maybe didn't compile right away, but writing syntactically acceptable code became routine. Your goal then moved on to writing programs that behaved correctly. You put in `2+2` and it gives you `5`, oops. Once you found the broken code and it gave you `4`, you were overjoyed.

A lot of programmers stop here. There are plenty of refinements to be had, here. Algorithms, data structures, design patterns. All are different ways of approaching the task of building a program that behaves correctly. Writing correctly behaving programs becomes routine, even when they don't always behave properly right away, and that's as far as it goes.

But there's one more level, one which many programmers aren't even really aware of. At this level, the goal is to write programs _which fail gracefully_. This takes even more thought and care than making programs which behave correctly, and this is what I want to address today.

**What Happens If It Fails?**  
 This question is the key to writing programs which fail gracefully. Let's take a fairly common line that you might find in any average Cocoa program:

```
    NSData *data = [NSData dataWithContentsOfFile: path];
```

Cocoa makes this so easy that we can be lulled into a false sense of security. How much can go wrong from one line of code?

Actually, quite a lot:

1. Maybe the file doesn't exist at that path, maybe it exists but the permissions don't allow you to read it, etc.
2. Maybe the file got trashed by another program. Or by yours!
3. Especially possible for files outside your app bundle.
4. Ditto.
5. 2TB drives can be had for well under $200 now, and a single file could be enormous. What happens if the file you're pointing at is 2TB long?
6. Network filesystems like AFP are extremely common these days, and networks can be slow.

How many of these failure modes does a typical Cocoa program actually handle in any sort of explicit fashion? Generally zero. Depending on the context, these failures could lead to a freeze, a crash, weird behavior, or nothing going wrong at all.

Even extremely mundane code can "fail". For example:

```
    int x = y + z;
```

What happens if the sum of

is greater than

, or less than

? The result, while not a "failure" in the sense of a freeze or crash, may not be what the code expects.

**Ways to Fail**  
 There are a lot of ways that a program can respond to a failure. Ranked from worst to best:

1. Corrupt/delete user data
2. Crash/freeze
3. Fail silently
4. Display an error
5. Work around the failure

It should be obvious why #1 is the worst. No matter how much your program crashes or fails to do its job, the worst it can do is be useless. But if you destroy your user's data, then your program can actually acquire

value. When he discover the culprit, the user will wish he had never tried your program, and he will tell all of his friends about this.

Everything after #1 is acceptable to some degree. Working around the failure isn't always possible; what if the user is opening a file and the file isn't readable? Ideally, displaying an error is the worst that would ever happen. In reality, it's not practical to trap every failure so that you can display an error message.

**Working Around Failures**  
 How and whether this is possible will depend entirely on what you're doing, so I can't say much beyond generalities.

If there are multiple ways to accomplish the same task, then you can write code to try each way in sequence. It's pointless to do this if all the different ways funnel through the same mechanism in the end; there's no reason to fall back to `open/read` if your `NSData` file reader fails, for example. For a case where it's worthwhile, imagine saving a file with some user-provided metadata. You use that metadata to synthesize a useful filename. However, the synthesized filename may contain characters which are illegal on your target filesystem, and there's no way to know which characters are allowed in advance. Thus, if the file write fails, try it again with a more simplified filename.

Another example is when connecting to a network server. It's common for a server to advertise multiple addresses through a normal DNS entry or through ZeroConf. If your first attempt fails, try the other addresses before giving up. It's incredibly common, especially in a LAN environment with mixed IPv4/IPv6 addresses and ZeroConf advertisements, for half of a server's addresses to produce failures of some kind, and for the other half to work fine.

Occasionally it can be useful to simply retry the same operation more than once. Networking is a prime example of this. I can't count how many times I've loaded up Twitterrific on my iPhone and had it tell me that it couldn't connect to Twitter, only to have it work perfectly fine when I told it to try again. It would be great if it would try several times on its own before giving up.

Above all, make sure you test these fallback and retry paths! Many errors are rare, and it's not uncommon to have an error path which has never been executed. This can be fine, and even common, where your handler is just a log statement, but it's a very bad policy if you're actually doing real work there. If at all possible, set up unit tests to expose the error handling path. Even if you can't, be sure to at least manually test it after writing it to make sure that it works the way you want. An error handler which misbehaves is worse than one which simply logs the relevant information and gives up.

**Displaying Errors**  
 There's nothing complex here, it's just a bunch of annoying grunt work. Detect every useful error you can think of, and make it display an alert of some kind. Not much fun, and not much thought needed. The trick is that you can only do this for errors you anticipate, so you're limited.

**Providing Diagnostics**  
 When you're unable to work around the failure or display an error, you've gone beyond the realm of helping the user, but that doesn't mean that there's nothing else to do. Once you reach the point of crashing, freezing, or failing without an error message, you should consider how easy your code will be to debug.

As illustration, consider these two scenarios.

1. Your application crashes in a dealloc method called from NSPopAutoreleasePool called from the main event loop. No messages are logged.
2. after logging:

Your response to #1 is likely that nameless dread that we get when seeing a really difficult bug. Your response to #2 is, "Oh, I guess I should put a more intelligent handler in

."

There are two big tricks to making your app be more like #2.

First, always check for errors. I'll say it again: _always check for errors_. You don't have to handle them intelligently, but at least log them when you get one that's unexpected, and consider aborting, depending on the circumstances.

I'll make an exception to this for calls which do adequate logging on their own, such as `malloc`. There's no point in trying to recover from a `malloc` failure on OS X, because by the time you detect the failure and try to recover, your process is likely to already be doomed. There's no need to do your own logging, because `malloc` itself does a good job of that. And finally there's no real need to even explicitly abort, because any `malloc` failure is virtually guaranteed to result in an instantaneous crash with a good stack trace.

Some of you may have heard of Steinbach's Rule, which goes: "Never test for an error condition you don't know how to handle." This rule is tongue in cheek, but is partially correct. You should always _check_ for errors, but if you don't know how to handle them, then don't try. It's much better to have a program which produces clear logs and an obvious crash when something really unexpected happens than to have a program run a bunch of poorly thought out and poorly tested code to try to handle the error "properly" when you don't have a clear idea of what that actually means.

The second trick is to be liberal with asserts. The trick with asserts is that they should be used with conditions that you _know_ must be true, but which are somehow doubtful. Don't use an assert for something that could definitely fail unless there's absolutely way to continue execution afterwards. For example, this is not a good way to go:

```
    int fd = open(...);
    assert(fd >= 0);
```

You can easily have

fail, and you'll want better handling than just asserting and blowing up. This is the sort of thing you should be able to get back to the user in the form of a real error message somehow, even if it's not a very useful one. If the error message can't be useful, and the failure isn't considered "normal", consider logging more thorough information right at the site of failure so that the console logs will at least be informative to you.

On the other hand, this is a good way to use asserts:

```
    void DoSomethingWithFileDescriptor(fd)
    {
        assert(fd >= 0);
        ...
    }
```

Many failures are not due to external events, like files being unavailable, but are simply an internal clash of assumptions or outright bugs. By sprinkling asserts around on the conditions you know to be true, you ensure that your program will fail in an informative fashion when it turns out that your assumptions have been violated somehow.

**Conclusion**  
 While these techniques are all useful for defensive programming, overall it's largely a matter of attitude. You need to get used to asking the question, "What if it fails?" It's easy to get fixated on simply making sure that the code works. After all, that's hard enough as it is. But as you're writing the code, take the time to ask, "What if it fails?" The result will be a more robust program that behaves better, crashes less, and is easier to debug.

That's it for this week. Come back in seven days for another exciting edition of Friday Q&A. As always, Friday Q&A is driven by your ideas, so [send them in](mailto:mike@mikeash.com)! The more ideas I get, the better this series can be, so don't be shy.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
