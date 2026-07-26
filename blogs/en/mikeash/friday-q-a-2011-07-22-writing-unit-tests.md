---
title: 'Friday Q&A 2011-07-22: Writing Unit Tests'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-07-22-writing-unit-tests.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1ab8a778b04dba3a'
translated: false
---

> 原文：[Friday Q&A 2011-07-22: Writing Unit Tests](https://www.mikeash.com/pyblog/friday-qa-2011-07-22-writing-unit-tests.html)　·　mikeash.com Friday Q&A

Posted at 2011-07-22 16:16 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2011-08-05: Method Signature Mismatches](https://www.mikeash.com/pyblog/friday-qa-2011-08-05-method-signature-mismatches.html)  
Previous article: [Friday Q&A 2011-07-08: Let's Build NSNotificationCenter](https://www.mikeash.com/pyblog/friday-qa-2011-07-08-lets-build-nsnotificationcenter.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [testing](https://www.mikeash.com/pyblog/?tag=testing)

Friday Q&A 2011-07-22: Writing Unit Tests

by [Mike Ash](https://www.mikeash.com/)

**Setting Up Unit Tests in Xcode**  
I'm not going to cover how to set up unit tests in Xcode, as that's already been well covered in many other places, and I have no special expertise there. For how to set up tests using Xcode's built in unit testing facilities, I suggest reading [Unit Testing Applications](http://developer.apple.com/library/ios/#DOCUMENTATION/Xcode/Conceptual/iphone_development/135-Unit_Testing_Applications/unit_testing_applications.html) and [Xcode: Unit Testing Cocoa Applications](http://chanson.livejournal.com/120263.html). There are also third-party testing frameworks like [GHUnit](https://github.com/gabriel/gh-unit), and it's also pretty easy to make your own simple testing harnesses as I've done for some of my frameworks like [MAObjCRuntime](https://github.com/mikeash/MAObjCRuntime/blob/master/main.m). (MAObjCRuntime is also handy for building your own testing frameworks by making it easy to enumerate and invoke the methods of arbitrary classes.)

Instead, my goal is to discuss how to write the test code itself. The fundamentals don't depend on which testing framework you use. All that differs is how you write asserts, how you name your test methods, etc., all of which is fairly trivial. The interesting part is just how you write your test code so that it's useful and adds value to your project. For the purposes of this article I will write code targeting OCUnit, which means test methods which start with `test` and macros like `STAssert`, but the code will all easily translate to other systems.

**A Quick Note on Terminology**  
In debates over the merits of unit testing, I've occasionally seen large controversies erupt over things like "system tests" versus "unit tests". To be entirely honest, I don't know what the difference is, and I don't care. I will use the terms "automated tests" and "unit tests" interchangeably here, to mean any sort of reasonably rigorous automated testing of your code. Debates about what terms to use just get in the way.

**Why Test?**  
The use of automated testing in programming circles is curiously uneven. On one end of the spectrum, you have people who rigorously practice [test-driven development](http://en.wikipedia.org/wiki/Test-driven_development) for every piece of code they write. On the other end, you have people who hate automated testing and never use it. Lots of people sit somewhere in between.

I'm one of those people who sits in between. I've developed code in the style of test-driven development, I've developed code that has no automated tests, and I've done lots of code that sits in the middle. While I don't agree with the dogmatic position that tests must be written for every piece of code before the code itself is written, I've seen tons of benefits from testing when used in the right situations. It confers a few major advantages.

First, unit tests make it easier to discover subtle bugs in the initial implementation. Nobody in their right mind writes code without doing any testing at all. However, manual testing is often light and haphazard. Automated tests can more comprehensively cover many different cases, making it more likely to discover corner cases.

Second, they make it more likely that you'll detect bugs added to the code later on. Whether it's a change made to the code itself, or a change made to a completely different subsystem which that chunk of code happens to rely on, having tests which are constantly run means that they'll catch obvious breaks, and quite possibly less obvious breaks.

Third, because of the above, tests allow much more _freedom_ of coding. Unit tests add a safety net. Without them, you're a bit like a tightrope walker high above a concrete floor. You have to worry that any wrong move may result in a catastrophe. You'll test your changes, of course, but if you're making extensive changes it can be really hard to test them thoroughly. With good tests in place, you can be reasonably confident that your code is being thoroughly tested all the time, and that obvious breaks are likely to be uncovered soon.

Unit tests are not perfect and they won't solve all of your problems. It's not hard to write a bug which isn't uncovered by your tests. However, they help a great deal, and I believe that in many cases they save far more time than they take to write. Unit tests shouldn't be thought of extra effort that you put in to make your code better, but rather as a technique that you can use to put in _less_ effort overall.

**What to Test?**  
In my experience, not all code is worth writing automated tests for. In the standard model-view-controller design for a typical graphical application, the "model" side is where tests should generally go. Writing tests for the UI side of things is complex and doesn't have a good return on investment. I know that there are some people who will argue with this, and who write tests to go through and verify all of the actions and bindings and such for their UI controls, but I don't see this as being worthwhile personally.

Just about all model code can be tested, at least in theory, but it's not always reasonable to do so. A major goal of unit tests should be that they run quickly. A test suite that takes an hour to run isn't going to be used very much, which will negate a lot of the advantages of automated testing. It may be better to avoid automated tests for code that takes a long time to test, or at least arrange it so those tests don't run by default.

Code which relies heavily on external entities is also difficult to test. For example, a wrapper around a Twitter API or something which relies on a MySQL database won't be easy to test. It's possible to work around this using techniques like dependency injection and mock objects, but it's not quite as straightforward.

Purely functional and self-contained code is easy to test. There are defined inputs and defined outputs, so write code to check these. Code which does nothing but manipulate pure data is an excellent candidate for testing.

A lot of code may appear to rely on external entities but can be self contained with a little work. For example, code which deals with files can be tested by supplying test files for it to work on, and having it write out files to a temporary directory. A generic HTTP client can be tested by starting up a local HTTP server and pointing the client to that. A custom network protocol can be tested by spinning up both client and server ends in the same test and having them talk to each other.

**Writing Tests**  
All of this theory is probably making you look for more interesting stuff to read, so let's get to some code. Let's take a simple Cocoa method, like `-[NSString stringByAppendingString:]`, and write some tests for it.

The first thing we should do is just test the basic functionality:

```
    NSString *s1 = @"hello";
    NSString *s2 = @"world";
    STAssertEqualObjects([s1 stringByAppendingString: s2], @"helloworld", @"bad string output");
```

If you aren't familiar, `STAssertEqualObjects` does pretty much what it says: compare two objects using `-isEqual:`, and fail the test if they don't match. The `bad string output` at the end is just a diagnostic to print in the event of failure.

This gives a really basic test, but we should be sure to try some edge cases as well. For example, we should try some empty strings:

```
    STAssertEqualObjects([s1 stringByAppendingString: @""], s1, @"bad string output");
    STAssertEqualObjects([@"" stringByAppendingString: s1], s1, @"bad string output");
    STAssertEqualObjects([@"" stringByAppendingString: @""], @"", @"bad string output");
```

If the method is supposed to accept `nil` as an argument, this would also be a good thing to test. In this case, it's not, so we won't bother to test it. (It's documented as raising an exception, so if you want to be extremely thorough you could test for _that_, but I think that's going a little beyond what's really useful.)

This is probably good enough, but sometimes it can be useful to do a real torture test to expose deep flaws. For this, I will generate a series of random strings, which I will then split and re-append to ensue that the result is the same as the original:

```
    unsigned short seed[3] = { 0 };

    for(int i = 0; i < 100; i++)
    {
        int len = nrand48(seed) % 100;
        NSMutableData *data = [NSMutableData data];
        while(len--)
        {
            int32_t value = jrand48(seed);
            [data appendBytes: &value length: sizeof(value)];
        }

        NSString *string = [data description];
        for(unsigned split = 0; split <= [string length]; split++)
        {
            NSString *s1 = [string substringToIndex: split];
            NSString *s2 = [string substringFromIndex: split];
            STAssertEqualObjects([s1 stringByAppendingString: s2], string, @"bad string output");
        }
    }
```

The idea here is to try to expose any data-dependent bugs the code may have. While something as simple as `stringByAppendingString:` is unlikely to have that sort of bug, it can be a handy test to make.

Also note that, while this test generates pseudorandom strings, it does so completely deterministically. It uses a fixed random seed (in this case, all zeroes) and so will produce the same sequence each time. This will help in the event that the test ever finds a bug. Because the test is ultimately deterministic, it will run the same sequence each time. That means that if you apply a fix, re-run the test, and the test passes, you can be confident that you actually fixed the bug, and didn't just get unlucky with a sequence that didn't exercise it.

A more truly random test could read from `/dev/random`, but it would not allow reliable repetition. On the other hand, it might occasionally turn up really subtle and rare bugs.

For another example, let's do a little testing of `NSMutableArray`. We'll slice and dice it a bit and make sure every step is correct. This code uses the `ARRAY` macro from [MACollectionUtilities](https://github.com/mikeash/MACollectionUtilities) to make things a little more concise:

```
    NSMutableArray *array = [NSMutableArray array];
    STAssertEqualObjects(array, ARRAY(), @"bad array");

    [array addObject: @"one"];
    STAssertEqualObjects(array, ARRAY(@"one"), @"bad array adding object");

    [array addObject: @"two"];
    [array addObject: @"three"];
    STAssertEqualObjects(array, ARRAY(@"one", @"two", @"three"), @"bad array adding more objects");

    [array addObject: @"one"];
    STAssertEqualObjects(array, ARRAY(@"one", @"two", @"three", @"one"), @"bad array adding duplicate object");

    [array removeObjectAtIndex: 1];
    STAssertEqualObjects(array, ARRAY(@"one", @"three", @"one"), @"bad array removing object by index");

    [array removeObject: @"one"];
    STAssertEqualObjects(array, ARRAY(@"three"), @"bad array removing object by identity");

    [array removeObject: @"three"];
    STAssertEqualObjects(array, ARRAY(), @"bad array removing object by identity");
```

**Testing Asynchronous Code**  
Writing tests for synchronous data-processing code is pretty easy: figure out what the code should do, then exercise it. Testing asynchronous code is a little trickier, though. The basic technique is to wrap the asynchronous code in something that makes it synchronous by waiting until it finishes.

Here's a quick example of testing `dispatch_async`. All it does is spin off a block and then wait for it to finish by continuously checking a shared `volatile` variable:

```
    __block volatile BOOL finished = NO;
    dispatch_async(dispatch_get_global_queue(0, 0), ^{
        finished = YES;
    });
    while(!finished)
        ; // do nothing
```

Normally, polling a shared flag like that is a bad idea. It will burn up CPU time for no good purpose. It would be better to use a proper synchronization primitive, like a condition variable or a semaphore. However, since this is test code where we expect the code to complete quickly, it does no harm to be a little lazy.

There's a bigger problem here. If the code being tested fails, this test code will loop forever. This isn't a very nice way to indicate failure. It would be much better to loop with a timeout, and fail after a certain amount of time passes.

This timeout can be fairly long. Tests need to run quickly when they're successful in order to be used regularly, but they can afford to take a while to fail, since that shouldn't be the usual outcome. Here's a version of the above code which fails if the flag isn't set after ten seconds:

```
    __block volatile BOOL finished = NO;
    dispatch_async(dispatch_get_global_queue(0, 0), ^{
        finished = YES;
    });

    NSTimeInterval start = [[NSProcessInfo processInfo] systemUptime];
    while(!finished && [[NSProcessInfo processInfo] systemUptime] - start <= 10)
        ; // do nothing
    STAssertTrue(finished, @"dispatch_async never ran its code");
```

This works pretty well, but gets a little repetitive to write over and over again. Let's factor the waiting code out into a separate function. We'll have it take a block which contains the condition to test:

```
    BOOL WaitFor(BOOL (^block)(void))
    {
        NSTimeInterval start = [[NSProcessInfo processInfo] systemUptime];
        while(!block() && [[NSProcessInfo processInfo] systemUptime] - start <= 10)
            ; // do nothing
        return block();
    }
```

This returns the final outcome so we can easily use `WaitFor` in a test assert. Now we can rewrite the above test using this helper function:

```
    __block volatile BOOL finished = NO;
    dispatch_async(dispatch_get_global_queue(0, 0), ^{
        finished = YES;
    });
    STAssertTrue(WaitFor(^{ return finished; }, @"dispatch_async never ran its code");
```

For asynchronous code which is scheduled on the current runloop, the same basic approach can be used. Here's a version of the helper function which runs the runloop while waiting:

```
    BOOL WaitFor(BOOL (^block)(void))
    {
        NSTimeInterval start = [[NSProcessInfo processInfo] systemUptime];
        while(!block() && [[NSProcessInfo processInfo] systemUptime] - start <= 10)
            [[NSRunLoop currentRunLoop] runMode: NSDefaultRunLoopMode beforeDate: [NSDate date]];
        return block();
    }
```

Since this modified version polls the runloop, it can still be used for testing threaded code as shown above. Now, however, it also works for asynchronous runloop-oriented code. For example, let's say we have a simple asynchronous URL loader wrapped around `NSURLConnection` that we want to test:

```
    __block NSData *data = nil;
    __block NSError *error = nil;

    LoadURL(@"http://www.google.com/", ^(NSData *inData, NSError *inError) {
        data = [inData retain];
        error = [inError retain];
    });

    STAssertTrue(WaitFor(^BOOL { return data || error; }), @"async URL loading failed");
    STAssertNotNil(data, @"failed to load data from URL");
    STAssertNil(error, @"got an error when loading URL");
```

Because the hypothetical URL loader is runloop based, this code doesn't have to worry about thread safety issues that would arise from sharing variables like `data` between threads.

The wisdom of hitting an external web site like `google.com` in a unit test is debatable. On one hand, it's almost certain to be up, and it means you're testing the code in more realistic conditions. On the other hand, it means that the test requires internet access in order to pass. Depending on your needs, it may be better to start a local web server and test against that rather than relying on an external site.

**Test, Then Code?**  
The obvious way to create unit tests is to either write tests for existing code, or write code and then write tests to exercise it. However, a lot of people advocate writing tests _before_ writing the code that it exercises, and there are some significant advantages to doing this.

First, a subtle but important advantage is that it makes it easy to verify that your tests are actually doing something. You can write your tests without any code for them to test, run them, and watch them fail. By doing this, you know that the tests are actually running, and that they _can_ fail. It's often easy to write tests which never run by accident. With Xcode's built in facilities, for example, methods which start with `test` get executed as unit tests, and a typo in the method name is all it takes to silently disable it. It gives some peace of mind to write the tests, run them, and get a failure message. You can then go ahead and implement the code being tested to get rid of the failure.

A bigger benefit is that writing the tests first help you better design and think about the API and the implementation of the code that you're writing. Rather than come up with an API that sounds good and then implement it, you come up with an API that sounds good and then write some code that uses that API to get something done. This can help to expose conceptual weaknesses in the API before you've written a line of the implementation.

Finally, by writing the tests first, it makes it easier to fix the bugs that the tests uncover. You can write code and then immediately run the tests. If they fail, the original implementation is still fresh in your mind.

Writing tests at all is far more important than whether you write tests before or after writing the code they're supposed to test, but it can still be helpful and worthwhile to write tests first in cases where it makes sense.

**Conclusion**  
Unit tests are a valuable addition to just about any project. They allow implementing and altering code with confidence, and often catch problems that manual testing misses.

Unit tests may not be appropriate for all code. Especially in cases like GUI views and controllers, unit tests take a lot of effort to create and don't offer a big return. Manual testing is often much easier in these cases. However, for straightforward model code, unit testing can bring enormous benefits, and can easily offer a large return on the time invested in creating them.

That's it for today. Come back in two weeks for another one. As always, Friday Q&A is driven by its readers, so if you have a topic that you would like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
