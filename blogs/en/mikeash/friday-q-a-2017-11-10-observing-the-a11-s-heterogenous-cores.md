---
title: 'Friday Q&A 2017-11-10: Observing the A11''s Heterogenous Cores'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2017-11-10-observing-the-a11s-heterogenous-cores.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4c5e10eb1de642d8'
translated: false
---

> 原文：[Friday Q&A 2017-11-10: Observing the A11's Heterogenous Cores](https://www.mikeash.com/pyblog/friday-qa-2017-11-10-observing-the-a11s-heterogenous-cores.html)　·　mikeash.com Friday Q&A

Posted at 2017-11-10 12:41 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2017-12-08: Type Erasure in Swift](https://www.mikeash.com/pyblog/friday-qa-2017-12-08-type-erasure-in-swift.html)  
Previous article: [Friday Q&A 2017-10-27: Locks, Thread Safety, and Swift: 2017 Edition](https://www.mikeash.com/pyblog/friday-qa-2017-10-27-locks-thread-safety-and-swift-2017-edition.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hardware](https://www.mikeash.com/pyblog/?tag=hardware) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Friday Q&A 2017-11-10: Observing the A11's Heterogenous Cores

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Hungarian (translation by Szabolcs Csintalan)](http://fertlond.com/megfigyeljuk-az-a11-heterogen-mag/).

(Yes, I'm aware that A11 devices could be obtained weeks ago when the iPhone 8 came out, but I didn't know anybody who got one, and it was hard to work up much excitement for it with the iPhone X coming not long after.)

**Brief Review**  
Multicore CPUs have been around in the Apple world since at least the Power Mac G5, which was available with up to two cores per CPU, and up to two CPUs in one machine.

They've become the norm in many parts of the computing world. They're a natural response to increasing transistor counts as silicon chip fabrication technology continues its [asymptotic march toward infinity](https://en.wikipedia.org/wiki/Moore%27s_law). CPU designers always want to use more transistors to make their hardware faster, but there are diminishing returns. Rather than put more transistors into speeding up single-threaded performance, those transistors can be used to effectively put multiple CPUs onto a single chip. Those became known as CPU cores.

These days you can buy CPUs with dozens or even hundreds of cores. That's often not the best tradeoff, since a lot of software won't take advantage of that many. It can be better to have fewer, faster cores instead. These days, typical user-facing computers have somewhere in the neighborhood of between two and 16 cores.

Usually, all of the cores in a system are identical. Software can run on any or all of them and it doesn't make a bit of difference. If you dig deeply enough, some CPUs have sets of cores which can transfer data within the group more quickly than outside the group. It thus makes sense to put multiple threads working on the same data together within such a group. This is one of the reasons for the [thread affinity API](https://developer.apple.com/library/content/releasenotes/Performance/RN-AffinityAPI/index.html). Even so, the individual cores are still the same, they just aren't connected 100% symmetrically.

Last year, Apple introduced their A10 CPU with heterogeneous cores. It's a four-core CPU, but those cores are not identical. Instead, it has two high-performance cores and two high-efficiency cores. The high-efficiency cores are slower, but consume much less power. For tasks that don't need to be completed as quickly as possible, running on the high-efficiency cores makes them use much less power. The system would switch between running software on the high-performance cores or the high-efficiency cores depending on the workload at any given time.

This is a great idea, since iPhones are battery-powered and really want to use as little power as possible, and a lot of the work that iPhones do is relatively mundane tasks that don't need to be super fast, like downloading the latest tweets from your stream or loading the next chunk of audio data from the flash storage. It's a bit wasteful, though, since you have two cores just sitting there doing nothing at any given time. That's what you want in high-efficiency mode, since the whole idea is to run less hardware in order to consume less power, but in high-performance mode it's unfortunate that it can't take advantage of the two idle high-efficiency cores.

This year, Apple introduced the A11 which takes the concept a step further. It has six cores: two high-performance and four high-efficiency. And unlike the A10, the A11 is able to use all six cores simultaneously. If the workload requires it, the A11 can run two threads on the high-performance cores while at the same time running four more threads on the high-efficiency cores.

**Planning**  
I started thinking about how we could catch it in the act. The system probably moves threads around regularly, so timing a long-running computation probably wouldn't reveal much. Short-running computations would be hard to manage, since we'd want to ensure there were exactly six going simultaneously.

I decided to write a test that would do a lot of small computations on each thread. It would then sample the timing of a few of those small computations during the process. Hopefully they would happen quickly enough that they would be unlikely to migrate between cores during the sample.

The next question was what sort of computation to perform. I started out doing a SHA-256 of the current iteration count, but I was afraid that special cryptographic instructions might interfere with the results. I then tried a simple square root algorithm on the current iteration count. I thought this might be placing too much emphasis on floating-point performance, so I finally redid it to do an integer square root instead. Ultimately, all three gave the same basic results. I stuck with the integer square root since integer computations seem like the predominant workload in most software.

My theory was that this should show a strongly bimodal distribution of running times on the A11. Did it work? Read below to find out!

**Code**  
Each thread runs a function which takes a number of iterations to perform, and a sampling interval. It returns the runtimes for each sample in an array, expressed in terms of the units provided by the `mach_absolute_time` call:

```
    func ThreadFunc(iterations: UInt64, interval: UInt64) -> [UInt64] {
```

It creates an array that will eventually hold all of the sampled running times:

```
        var times: [UInt64] = []
```

Then it enters a loop for the given number of iterations:

```
        for i in 1 ... iterations {
```

Before it does any work, it grabs the current time. It does this regardless of whether or not this is a run to sample, in an attempt to make the non-sampled iterations as similar as possible to the sampled iterations:

```
            let start = mach_absolute_time()
```

`iterations` is a `UInt64` but we want to work on `Int64` numbers, so convert it and stash it in a variable:

```
            let x = Int64(i)
```

I implemented the [Babylonian method](https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method) for computing a square root. This consists of making a guess at the square root, then iteratively refining that guess by computing the average of `guess` and `x / guess`. Iterate until the desired precision is reached. It's not a very fast method, but we don't care about speed here, other than for consistency. I implemented this algorithm to run `1024` iterations, which is way too many for any sort of reasonable result, but it provides a nice amount of work for our benchmarking purposes:

```
            var guess = x
            for _ in 0 ... 1024 {
                guess = (guess + x / guess) / 2
            }
```

I had to make sure that the compiler would actually perform this computation and not throw away the whole thing as unnecessary. That meant I had to use the result somehow. I added a dummy check to see if the computed square root was way off from the actual one, with a print (which can't be optimized away) in that case:

```
            if abs(guess * guess - x) > 1000000000 {
                print("Found a really inexact square root! \(guess * guess) \(x)")
            }
```

None of my actual runs ever hit the print, so there was no IO to skew the timing.

With the work completed, it gets the current time again:

```
            let end = mach_absolute_time()
```

If this is a sampling iteration, add the total runtime for this iteration to the `times` array:

```
            if i % interval == 0 {
                times.append(end - start)
            }
        }
```

Once all of the iterations are complete, return the times:

```
        return times
    }
```

That's the code for a single thread. We also need code to spawn these threads and analyze the results. That code starts with some constants for the number of threads to spawn, the number of iterations to run, and the sampling interval:

```
    let threadCount = 6
    let iterations: UInt64 = 1000000
    let interval = iterations / 20
```

It makes an array in which to gather all of the sampled times:

```
    var times: [UInt64] = []
```

It will use an `NSCondition` object to synchronize access to `times` and wait for results to come in:

```
    let cond = NSCondition()
```

We'll track the number of active threads so we can know when they've all completed:

```
    var runningThreads = threadCount
```

With the initial setup complete, it starts spawning threads:

```
    for _ in 0 ..< threadCount {
        Thread.detachNewThread({
```

The first thing each thread does is call `ThreadFunc` to do the work and gather results:

```
            let oneTimes = ThreadFunc(iterations: iterations, interval: interval)
```

Once the results come back, it appends them to `times` and signals that this thread has completed:

```
            cond.lock()
            times.append(contentsOf: oneTimes)
            runningThreads -= 1
            cond.signal()
            cond.unlock()
        })
    }
```

Back in the controlling code, it waits for all of the running threads to complete:

```
    cond.lock()
    while runningThreads > 0 {
        cond.wait()
    }
    cond.unlock()
```

At this point, it has all samples in the `times` array. Those samples are in terms of the units returned by `mach_absolute_time`, which aren't all that useful on their own, although their relative values are still instructive. We'll convert them to nanoseconds:

```
    let nanoseconds = times.map({ machToNanoseconds($0) })
```

Next, it runs a really simple clustering algorithm, which just steps through the samples and looks for gaps where the the relative difference between two samples is greater than some threshold. I wasn't sure which threshold value would be appropriate, so I had it try a bunch:

```
    for threshold in [0.01, 0.02, 0.03, 0.04, 0.05, 0.1] {
        print("Threshold: \(threshold)")
        let clusters = cluster(nanoseconds, threshold: threshold)
```

This returns each cluster as an array of values within the cluster. The code then computes the mean, median, and standard deviation for each cluster ard prints them out:

```
        for cluster in clusters {
            let mean = cluster.reduce(0, +) / Double(cluster.count)
            let median = cluster[cluster.count / 2]
            let stddev = sqrt(cluster.map({ ($0 - mean) * ($0 - mean) }).reduce(0, +) / Double(cluster.count))

            print("count: \(cluster.count) - mean: \(mean) - median: \(median) - stddev: \(stddev)")
        }
        print("----------")
    }
```

That's it! We're ready to see the results.

**Results**  
I first ran it in on my iPhone 6+ to generate something of a baseline. The threshold of 0.05 seemed to provide the best clustering. Here are those results:

```
    Threshold: 0.05
    count: 120 - mean: 10993.4027777778 - median: 10958.3333333333 - stddev: 75.1148490502343
```

Each sample takes almost the same amount of time. They're around 11 microseconds, with a standard deviation of only 75 nanoseconds.

Here are the results from the iPhone X:

```
    Threshold: 0.05
    count: 54 - mean: 6969.90740740741 - median: 6958.33333333333 - stddev: 24.6068190109599
    count: 65 - mean: 9082.69230769231 - median: 9250.0 - stddev: 278.358695652034
    count: 1 - mean: 14125.0 - median: 14125.0 - stddev: 0.0
```

There's one outlier, which which shows up pretty consistently across multiple runs. I'm not entirely sure why it would be so consistent. Maybe it takes a moment to ramp the CPU up to full speed? Ignoring the outlier, we see the heterogeneous cores clearly. There's one narrow cluster centered around ~7 microseconds, and another narrow cluster centered around ~9 microseconds, and nothing in between.

The speed difference is smaller than I expected, but in my experiments it varied quite a bit depending on the type of work being done. This particular microbenchmark is probably bottlenecked on integer division, which is not the most representative task.

Regardless, the signal is clear, with one chunk of samples running significantly faster than the other chunk, illustrating the high-performance and high-efficiency cores working simultaneously.

**Conclusion**  
It's been interesting to follow the development of Apple's CPUs, and the heterogeneous cores in their latest iteration are really nifty. I expected it to take some work to observe them, but it ended up being straightforward. By running a long sequence of quick computations on multiple threads and sampling a few of them, the disparate cores become obvious.

That's it for today! Friday Q&A will be back next time with more fun and games. In the meantime, if you have a topic you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2017-11-10-observing-the-a11s-heterogenous-cores.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
