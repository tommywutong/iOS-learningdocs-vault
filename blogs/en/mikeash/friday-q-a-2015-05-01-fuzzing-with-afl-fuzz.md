---
title: 'Friday Q&A 2015-05-01: Fuzzing with afl-fuzz'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-05-01-fuzzing-with-afl-fuzz.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:acc756e5627d519e'
translated: false
---

> 原文：[Friday Q&A 2015-05-01: Fuzzing with afl-fuzz](https://www.mikeash.com/pyblog/friday-qa-2015-05-01-fuzzing-with-afl-fuzz.html)　·　mikeash.com Friday Q&A

Posted at 2015-05-01 13:24 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2015-05-29: Concurrent Memory Deallocation in the Objective-C Runtime](https://www.mikeash.com/pyblog/friday-qa-2015-05-29-concurrent-memory-deallocation-in-the-objective-c-runtime.html)  
Previous article: [Friday Q&A 2015-04-17: Let's Build Swift.Array](https://www.mikeash.com/pyblog/friday-qa-2015-04-17-lets-build-swiftarray.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [fuzzing](https://www.mikeash.com/pyblog/?tag=fuzzing) [security](https://www.mikeash.com/pyblog/?tag=security)

Friday Q&A 2015-05-01: Fuzzing with afl-fuzz

by [Mike Ash](https://www.mikeash.com/)

**Fuzzing**  
American Fuzzy Lop, or `afl-fuzz`, is a fuzzing tool. To understand what it does and how to use it, you must first understand the basic concept of fuzzing.

The idea is to stress-test programs by feeding them large quantities of computer-generated input. It's similar in concept to what you as a programmer might do when writing unit tests. You'd come up with what you think are some representative inputs and run them through the code being tested to make sure it behaves properly. With a fuzzer, the computer is generating the inputs and constantly trying your program with them. Rather than testing for correct output, it's searching for bugs that manifest in the form of crashes, hangs, or assertion failures.

There are different kinds of fuzzers, based on how they generate the input. It's possible to write a fuzzer that generates purely random inputs, but this won't produce useful results for many types of programs. An XML parser, for example, will return an error almost immediately when presented with pure random data, meaning that most of the code in the parser goes untested.

One way to improve on this is to give the fuzzer knowledge of what kind of structure the program expects. For the example of an XML parser, you might make a fuzzer that generates random legal XML documents and tests against that. Minor illegal variations on legal XML would help test error handling and edge cases. This can work extremely well, but requires a lot of domain-specific work to give the fuzzer knowledge of the program's inputs.

Another approach is to start with examples, and then produce test cases by mutating the examples by flipping bits, shuffling data around, inserting or removing data, or mixing data from multiple examples. Coming up with examples to give to the fuzzer is typically much less work than coding it to produce good examples on its own, but the fuzzer will be limited to things similar to the examples given.

**`afl-fuzz`**  
`afl-fuzz` is an open source fuzzer that runs on various UNIX-like OSes, including Mac OS X. It can be found here:

[http://lcamtuf.coredump.cx/afl/](http://lcamtuf.coredump.cx/afl/)

It takes an interesting approach that combines certain aspects of the usual approaches. It uses example inputs and mutation to generate new inputs. However, it intelligently guides these mutations using the target's behavior to select interesting inputs for further mutation.

The target's behavior is monitored by injecting additional code at compile time. `afl-fuzz` provides a wrapper around either `gcc` or `clang`. If you compile a program using the wrapper, the resulting binary has the necessary instrumentation injected. (`afl-fuzz` is also able to monitor uninstrumented binaries by running them in QEMU, but this currently doesn't work on the Mac.)

The instrumentation monitors branches taken by the program. Any given input to the program will produce a sequence of branches. Moving from one branch to another branch is a transition, and each transition is recorded. The fuzzer then favors inputs which generate new transitions, with the result that inputs are generated which explore new paths through the code. Unusual paths through the code are more likely to turn up bugs, and this helps generate those unusual paths.

In short, `afl-fuzz` searches for inputs that make your program behave differently. When it finds such inputs, it then alters them further to see if it can make your program behave even more differently. This lets it cover large chunks of your program's potential execution space without any special knowledge of the structure of the input it expects.

**Building**  
The source code for `afl-fuzz` can be obtained from its web page above. It builds out of the box on Mac OS X by simply typing `make` inside the source directory. It's a fairly small program and the build completes nearly instantaneously. The built binaries are placed in the source directory. You can install them wherever you want, or just leave them in place and run them using the appropriate path.

**Creating Test Cases**  
You can't typically take an arbitrary program, compile it with `afl-fuzz`, and run it in the fuzzer. It won't know how your program expects to receive input. To settle this question, `afl-fuzz` passes inputs to the program by sending them on standard input. If your program doesn't already read from standard input, you'll need to write a small test harness that reads from `stdin` and then invokes the code you want to fuzz.

If you're using Cocoa (and yes, `afl-fuzz` works fine with Objective-C), such a test harness could be written like this:

```
    int main(int argc, char **argv) {
        @autoreleasepool {
            NSFileHandle *stdin = [NSFileHandle fileHandleWithStandardInput];
            NSData *data = [stdin readDataToEndOfFile];

            // Do something interesting with data here
        }
    }
```

Just what you do with the data is up to you. If you're testing a UTF-8 parser, you'd pass the data to your parser. If you have an image decoder, treat the data like an image and try to decode it. If you're testing a data structure, you could treat each line of input as a piece of data to insert or delete. Note that while non-instrumented libraries like the ones provided by the system will happily run under `afl-fuzz`, the lack of instrumentation means that they're a black box to the fuzzer, and only the behavior of your own code informs its explorations. So don't try `[NSImage imageWithData: data]` and expect anything interesting to happen.

Of course, it's not necessary to use `NSFileHandle` like this. If your code deals with input byte-by-byte, calling `getchar()` in a loop works nicely. If your code wants an `NSStream`, create one from `/dev/stdin` and pass it in.

**Compiling Test Cases**  
To compile a test case, compile it as you normally would at the command line, but use the `afl-clang` tool rather than the normal `clang` command. `afl-clang` will compile your code with `clang`, inserting the necessary instrumentation as it goes along. For a simple test case that doesn't use anything besides the standard C library, you can compile it by just passing the name of the source file:

```
    afl-clang test-case.c
```

This creates an executable named `a.out` which you can then run directly, or have the fuzzer work on.

For Objective-C programs, you need to also link against the Foundation framework, or the Cocoa framework if you use any of the UI parts:

```
    afl-clang -framework Foundation test-case.m
```

If your test case encompasses multiple files, you can compile them all together by passing them all into the command:

```
    afl-clang -framework Foundation test-case.m support-file1.m support-file2.m
```

If you prefer a name other than `a.out`, you can specify it with `-o`:

```
    afl-clang -framework Foundation test-case.m -o test-case
```

**Running**  
`afl-fuzz` needs at least example test case to start from. You can provide more than one if you like. The test cases are plain files that live in a subdirectory that you pass to the fuzzer. We'll call it `testcases`:

```
    mkdir testcases
    echo "Test case here." > testcases/case1
```

Fuzzer results go in another subdirectory, which we'll call `findings`. There's no need to create it, as `afl-fuzz` will create it when needed. We can then run `afl-fuzz` on the test case, giving it the `testcases` and `findings` directories:

```
    afl-fuzz -i testcases -o findings ./a.out
```

This doesn't quite work properly on a standard Mac. `afl-fuzz` distinguishes between hangs and crashes by waiting for a timeout to expire. If the program is still running when the timeout fires, it's considered a hang. If the program crashes before that, it's a crash. Otherwise it's a successful run. The problem is that the OS X crash reporter triggers when the test case crashes, and generating the crash report takes substantially longer than `afl-fuzz`'s default timeout of 20 milliseconds. This causes `afl-fuzz` to report all crashes as hangs.

The best workaround for this would be to disable the system crash reporter while fuzzing. A simpler workaround is simply to increase the timeout, which can be done by passing the `-t` flag. I used 20000 milliseconds instead of the default. This will seriously hurt performance if there are hangs, but works well enough:

```
    afl-fuzz -i testcases -o findings -t 20000 ./a.out
```

This will present you with a nice terminal interface:

```
                            american fuzzy lop 1.67b (a.out)

    ┌─ process timing ─────────────────────────────────────┬─ overall results ─────┐
    │        run time : 0 days, 0 hrs, 37 min, 5 sec       │  cycles done : 2      │
    │   last new path : 0 days, 0 hrs, 5 min, 13 sec       │  total paths : 112    │
    │ last uniq crash : none seen yet                      │ uniq crashes : 0      │
    │  last uniq hang : none seen yet                      │   uniq hangs : 0      │
    ├─ cycle progress ────────────────────┬─ map coverage ─┴───────────────────────┤
    │  now processing : 48* (42.86%)      │    map density : 108 (0.16%)           │
    │ paths timed out : 0 (0.00%)         │ count coverage : 6.41 bits/tuple       │
    ├─ stage progress ────────────────────┼─ findings in depth ────────────────────┤
    │  now trying : splice 17             │ favored paths : 3 (2.68%)              │
    │ stage execs : 948/1000 (94.80%)     │  new edges on : 6 (5.36%)              │
    │ total execs : 875k                  │ total crashes : 0 (0 unique)           │
    │  exec speed : 641.7/sec             │   total hangs : 0 (0 unique)           │
    ├─ fuzzing strategy yields ───────────┴───────────────┬─ path geometry ────────┤
    │   bit flips : 0/23.2k, 0/23.2k, 0/23.2k             │    levels : 4          │
    │  byte flips : 0/2906, 0/2019, 0/2421                │   pending : 87         │
    │ arithmetics : 0/88.7k, 0/31.0k, 0/11.7k             │  pend fav : 0          │
    │  known ints : 0/9017, 0/71.1k, 0/116k               │ own finds : 17         │
    │  dictionary : 0/0, 0/0, 0/0                         │  imported : n/a        │
    │       havoc : 0/156k, 17/309k                       │  variable : 0          │
    │        trim : 7.43%/1872, 43.63%                    ├────────────────────────┘
    └─────────────────────────────────────────────────────┘             [cpu: 39%]
```

There's a lot of info here, most of which I'll leave you to explore on your own. There are a few bits that are particularly interesting:

- and

  show how many crashes and hangs have been discovered so far. The moment these say something other than zero, you've found something interesting!
- is how long it's been since the fuzzer found a new path through the program. This is an indication of how much progress it's making. If it's been a long time since the fuzzer found a new path, it may no longer be able to find any interesting inputs.
- is how quickly it's able to run test cases. The higher this number, the more test cases the fuzzer can run through, and the faster it can discover interesting things.

As the fuzzer runs, it places information in the `findings` directory. Inputs that cause crashes are placed in files in the `crashes` subdirectory. Inputs that cause hangs go in the `hangs` subdirectory. The `queue` subdirectory contains the inputs that are interesting but haven't caused any crashes or hangs, and can be used to get an idea of the fuzzer's progress, and what kind of inputs it's working with.

**Example**  
I wrote a small test case that quickly exercises the fuzzer and verifies that it's working as expected. This test case reads standard input and calls `abort()` if the input starts with `deadbeef`:

```
    int main(int argc, char **argv) {
        @autoreleasepool {
            NSFileHandle *stdin = [NSFileHandle fileHandleWithStandardInput];
            NSData *data = [stdin readDataToEndOfFile];
            const char *ptr = [data bytes];
            if(ptr[0] == 'd') {
                if(ptr[1] == 'e') {
                    if(ptr[2] == 'a') {
                        if(ptr[3] == 'd') {
                            if(ptr[4] == 'b') {
                                if(ptr[5] == 'e') {
                                    if(ptr[6] == 'e') {
                                        if(ptr[7] == 'f') {
                                            abort();
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
```

The structure of this program is pretty weird. A single `memcmp` call could be used instead of the massive nested `if` statements. I wrote it this way to take advantage of the fact that the fuzzer instruments branches. With a `memcmp` call, the fuzzer is unlikely to ever discover the magic `deadbeef` input needed to crash the program. With each character checked separately, the fuzzer's branch instrumentation can discover them one by one.

The program also doesn't bother to check the length of the input. As a result, if it receives fewer than eight bytes, it'll end up reading garbage. Since the intent of the program is to have problems for the fuzzer to find, this really is a feature, not a bug.

Let's compile it and make sure it works as intended:

```
    $ afl-clang -framework Foundation deadbeef-test.m
    $ echo hello | ./a.out
    $ echo deadbeef | ./a.out
    Abort trap: 6
```

Perfect! Let's make a simple test case and get the fuzzer started:

```
    $ echo > testcases/foo
    $ afl-fuzz -i testcases -o findings -t 20000 ./a.out
```

Eventually, `uniq crashes` goes to one; the fuzzer reports a crash. This took a couple of hours on my computer. We can see what input the fuzzer found to trigger a crash:

```
    $ ls findings/crashes/
    README.txt
    id:000000,sig:06,src:000007,op:havoc,rep:2
    $ cat findings/crashes/id\:000000\,sig\:06\,src\:000007\,op\:havoc\,rep\:2 
    deadbeef
```

Exactly as expected.

It's interesting to look at the other interesting inputs the fuzzer generated along the way:

```
    $ for f in findings/queue/*; do echo $f:; cat $f; echo; echo ---; done
    findings/queue/id:000000,orig:foo:

    ---
    findings/queue/id:000001,src:000000,op:havoc,rep:64,+cov:
    d
    ---
    findings/queue/id:000002,src:000001,op:havoc,rep:4,+cov:
    deSd
    ---
    findings/queue/id:000003,src:000002,op:havoc,rep:2,+cov:
    deae
    ---
    findings/queue/id:000004,src:000002,op:havoc,rep:1,+cov:
    dead
    ---
    findings/queue/id:000005,src:000004,op:havoc,rep:2,+cov:
    deadbbdd
    ---
    findings/queue/id:000006,src:000005,op:flip4,pos:5,+cov:
    deadbe�d
    ---
    findings/queue/id:000007,src:000006,op:havoc,rep:2,+cov:
    deadbeea
    ---
```

The progression shows up clearly, as the fuzzer works out the sequence byte by byte by seeing what triggers a new code path. There's some garbage at the end of some of the inputs, which is to be expected since it's a randomized process and surplus suffixes don't affect how the program operates.

This same principle works on more complex programs, with the fuzzer generating input that takes it down new and interesting paths in the code, and potentially finding bugs along the way.

**Conclusion**  
There isn't much that's more entertaining than feeding crazy inputs to your programs and watching them crash. `afl-fuzz` automates the process and makes it much more likely that something amusing will occur. It can help you make your code more secure too, which is a nice bonus.

That's it for today. Come back next time for more computer amusements. Friday Q&A is driven by reader suggestions, so if you have an idea for a topic to cover next time or any other time, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
