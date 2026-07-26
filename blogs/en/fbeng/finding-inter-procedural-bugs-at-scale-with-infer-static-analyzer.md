---
title: Finding inter-procedural bugs at scale with Infer static analyzer
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2017/09/06/android/finding-inter-procedural-bugs-at-scale-with-infer-static-analyzer/'
original_language: en
published: 2017-09-06
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a042af039921fcdf'
translated: false
---

> 原文：[Finding inter-procedural bugs at scale with Infer static analyzer](https://engineering.fb.com/2017/09/06/android/finding-inter-procedural-bugs-at-scale-with-infer-static-analyzer/)　·　Meta Engineering — iOS

The capabilities of static analyzers, which catch bugs before programs are run, are steadily improving. During our work on the [Infer static analyzer](http://www.fbinfer.com/), we often were asked about the differences between Infer and other open source analysis tools like [Findbugs](http://findbugs.sourceforge.net/), [Error-prone](http://errorprone.info), and [Clang Static Analyzer](https://clang-analyzer.llvm.org/). A main difference is inter-procedural bugs, or bugs that involve interactions between multiple procedures.

We’ll take a look at two examples of inter-procedural bugs that Infer found in Java and C — one from the open source DuckDuckGo Android app, and the other from the OpenSSL C code. These bugs cannot be found by the tools mentioned above, which perform only intra-procedural analysis, or — in the case of Clang Static Analyzer — only intra-file analysis (possibly inter-procedural, but confined to the procedures in one translation unit, a file-with-includes).

Inter-procedural bugs are significant, as they make up the majority of several types of bugs Infer has found. Facebook developers have fixed thousands of such bugs, which suggests that static analysis for finding them can have a large impact; we include some data on inter-procedural bug frequency from Infer’s deployment at Facebook. As we have found, inter-procedural analysis can be deployed to large and rapidly changing codebases that consist of millions of lines of code and undergo thousands of modifications per day.

## DuckDuckGo

The code for the Android app of DuckDuckGo, a privacy-oriented internet search engine, is available on GitHub. A DuckDuckGo developer fixed the [following issue](https://github.com/duckduckgo/android-search-and-stories/issues/207) on an earlier version of the app after Infer reported it:

```clike
src/com/duckduckgo/mobile/android/activity/DuckDuckGo.java:867: error: NULL_DEREFERENCE
object `feedObject` last assigned on line 866 could be null and is dereferenced by call to `feedItemSelected(...)` at line 867.
    
864.
865. public void feedItemSelected(String feedId) {
866. FeedObject feedObject = DDGApplication.getDB().selectFeedById(feedId);
867. feedItemSelected(feedObject);
```

Along with this report, Infer produced an inter-procedural error trace consisting of 18 steps, which advanced through the procedures `getDB()`, `selectFeedById(feedId)`, and `feedItemSelected(feedObject)`. There are two distinct `feedItemSelected()` methods, one that accepts a `FeedObject` as a parameter and the other a `String`. Here is the code accessed by the call `selectFeedById(feedId)` on line 866:

```clike
src/com/duckduckgo/mobile/android/db/DdgDB.java:483: start of procedure selectFeedById(...)
    
482.
483. public FeedObject selectFeedById(String id){
484. FeedObject out = null;
485. Cursor c = null;
486. try {
487.   c = this.db.query(FEED_TABLE, null, "_id=?", new String[]{id}, null, null, null);
488.   if (c.moveToFirst()) {
489.    out = getFeedObject(c);
490.   }
491.  } finally {
492.      if(c!=null) {
493.            c.close();
494.      }
495.  }
496.  return out;
497. }
```

There is a possibility of `selectFeedById()` returning null, namely when the `Cursor c` returned by `db.query()` on line 487 is the empty cursor. The call to `c.moveToFirst()` at line 488 will then return `false`.

When analyzing the original code in `feedItemSelected()` where the null issue is flagged, Infer needs to become aware that null is a possibility at line 866. The error is actually reported at line 867, which is another method call, in this case involving the following method:

```clike
src/com/duckduckgo/mobile/android/activity/DuckDuckGo.java:842: start of procedure feedItemSelected(...)
    
841.
842.  public void feedItemSelected(FeedObject feedObject) {
843. // keep a reference, so that we can reuse details while saving
844.    DDGControlVar.currentFeedObject = feedObject;
845.    DDGControlVar.mDuckDuckGoContainer.sessionType = SESSIONTYPE.SESSION_FEED;
846.
847     String url = feedObject.getUrl();
```

Here we see that `feedObject` is dereferenced at line 847. We therefore will have a null pointer dereference if `feedObject` is null.

We have an inter-procedural bug where the source of null is in one method, the sink of null is in a second procedure, and the source and sink procedures are called from a third procedure. We need inter-procedural reasoning to find this issue, because purely intra-procedural tools will not find this error.

Findbugs, Error-prone, and other tools could find this bug if annotations about nullability and non-nullability were added to the code. However, finding the bug in the bare code as it’s written requires inter-procedural reasoning.

### Theory: Specs and summaries

Infer found this DuckDuckGo issue using a technique called compositional, summary-based analysis. Instead of re-evaluating a method each time it is encountered, Infer consults a summary or approximation of what the method might do. A compositional analyzer calculates summaries without looking at all the call sites of methods; Infer tries to compute as general a summary as possible in a single pass over a procedure.

Infer represents its summaries as specifications in a program logic. In more detail, a specification is a pair (pre,post) of a precondition and a postcondition (familiar from [Hoare logic](https://en.wikipedia.org/wiki/Hoare_logic) or its more modern incarnation, [separation logic](https://en.wikipedia.org/wiki/Separation_logic)). A (pre,post) pair means that if the logical property pre holds before executing a procedure, post will hold afterward. Sometimes several posts will be used to represent the disjunction (the “or”) of posts. A summary is a collection of pre/post pairs, and one of the pre properties needs to be matched at a call site for reasoning to proceed.

For the method `selectFeedById(String id)`, Infer calculates

```clike
PRE: this.db |→ - (db is non-null and points to a valid object)
    
POST1: return == null (we are returning a null feed object)
POST2: return |→ - (we are returning a valid, non-null feed object)
```

That is, there is a single pre/post pair in the summary, where the post is the disjunction POST1 OR POST2. Symbolic execution in the original procedure, `feedItemSelected(String feedId)`, will then consider two cases for `feedObject` at line 866: the null and non-null cases according to the two postconditions. Then, for the next statement at line 867, we must consider the null argument for the call `feedItemSelected(feedObject)`. Again we deal with this by consulting a calculated pre/post spec for `feedItemSelected`. The summary has five pre/post specs, but all of them contain

```clike
PRE: feedObject |→ - (feedObject is a valid, non-null object)
```

Infer selects this as the precondition because we need `feedObject` to be non-null; otherwise, an error (a NullPointerException) will occur. Now, when symbolic execution attempts `feedItemSelected(feedObject)` but with `feedObject == null`, we are unable to satisfy the precondition. It is at this point that we fail in our attempt to construct a logical proof that there is no runtime error, and an error is reported.

The important point is that the reasoning about the code

```clike
864.
865.  public void feedItemSelected(String feedId) {
866. FeedObject feedObject = DDGApplication.getDB().selectFeedById(feedId);
867. feedItemSelected(feedObject)
```

could be done using just the summaries of the procedures it calls, without delving into their bodies (again). For Infer to operate at scale, this application of the principle of procedural abstraction is crucial, as is the ability for the summaries to be constructed independently of calling sites.

There is additional nuance to Infer’s notion of summary, which is more detailed than the pre/post specs as mentioned above. In order for Infer to report [a trace for the error](http://www0.cs.ucl.ac.uk/staff/p.ohearn/InterproceduralBlog/DuckDuckGoErrorTrace.txt), it remembers trace information showing paths through the code in summaries in addition to the pre/post specs. And, the pre/post specs themselves are more complicated than those presented above, which are simplified manually for the purpose of illustration. You can find the detailed specs that Infer calculates for these procedures [here.](http://www0.cs.ucl.ac.uk/staff/p.ohearn/InterproceduralBlog/DuckDuckGoNPECodeAndSpecs.txt)

## OpenSSL

We’ve shown how summary-based compositional program analysis can effectively find inter-procedural errors at scale in Java. It also applies to the C family of languages. For example, in 2014 [we submitted to GitHub](https://rt.openssl.org/Ticket/Display.html?id=3403&user=guest&pass=guest) 15 null dereferences and memory leaks Infer found in OpenSSL, which one of the project’s core developers fixed. Some of the null dereferences were rather complex, which illustrates a point we want to make about the rate of false positives — errors that cannot occur in any run of a program.

Here is one of the reports from Infer:

```clike
apps/ca.c:2780: error: NULL_DEREFERENCE
pointer `revtm` last assigned on line 2778 could be null and is dereferenced at line 2780, column 6
2778. revtm = X509_gmtime_adj(NULL, 0);
2779.
2780.  i = revtm→length + 1;
```

The issue is that the procedure `X509_gmtime_adj()` can return null in some circumstances. Overall, the error trace found by Infer has 61 steps. Furthermore, the source of null, the call to `X509_gmtime_adj`, has 36 steps in its subtrace before it returns null; the trace goes five procedures deep, and it eventually encounters a return of null at call-depth 4 in procedure `ASN1_TIME_adj()` from the file crypto/asn1/a_time.c.

```clike
crypto/asn1/a_time.c:113:6: Condition is true
111.
112. ts=OPENSSL_gmtime(&t,&data);
113. if (ts == NULL)
114.   {
115.      ASN1err(ASN1_F_ASN1_TIME_ADJ, ASN1_R_ERROR_GETTING_TIME);
116.       return NULL;
117. }
```

Altogether, the trace goes through eight procedures and six distinct files. You can [see the entire trace here](http://www0.cs.ucl.ac.uk/staff/p.ohearn/InterproceduralBlog/openssl_trace.txt).

The conditions under which `X509_gmtime_adj(NULL, 0)` returns null are somewhat complex, and Infer does not establish that they definitely can occur in a run of a program. Infer does not construct a trace that goes all the way back to main() every time it reports a potential error. Rather, in the process of trying to construct a logical proof showing conditions where bugs occur, Infer will sometimes report the difficulties it encountered in constructing such a proof.

In this case, an OpenSSL developer fixed the issue. There were other places in the codebase where an Infer report was blocked because `OPENSSL_gmtime()` came with a null check, which confirmed further that the issue was one worth raising.

We also ran the Clang Static Analyzer on OpenSSL. It has the capability to perform intra-file analysis, a subset of which could be inter-procedural, but not between files as far as we know. This example required inter-file analysis; indeed, when we ran CSA on OpenSSL-1.0h, it did not find the bug. It’s worth noting that CSA reports a different set of bugs than Infer did, so it makes sense to run both analyzers on C code — and similarly, to run Findbugs and Error-prone for Java analysis.

An interesting question is whether this OpenSSL report is a false positive or a true bug. We were still unsure, even after a number of hours. This is not uncommon when working with static analysis at scale: For large code, sometimes neither the tool nor the human is sure whether a bug can occur. This is a reason that we assign less importance to the concept of the false positive rate after having deployed static analysis than we did when we were learning its principles. With large and changing codebases, this rate is, for all practical purposes, unmeasurable. A more knowable concept, which better speaks to the value an analysis brings to programmers, is the fix rate: the proportion of analyzer issues that are removed as a result of developers’ code changes. We plan to write in more detail on this point in the future; [this talk](https://www.youtube.com/watch?v=xc72SYVU2QY&t=23m30s) has additional information.

### Speed and incrementalism

To illustrate Infer’s performance on OpenSSL, a codebase consisting of over 300,000 lines of code and 700 files, we analyzed the code, changed it to fix the bug described above, and then re-analyzed it in an incremental fashion.

```clike
$ # compile to infer's intermediate language
$ time infer capture -- make
[...]
real 5m0.545s
user 4m10.563s
sys 1m3.104s
    
$ # analyze the entire OpenSSL project, using one CPU only
$ time infer -j 1 analyze
[...]
real 22m20.320s
user 20m24.831s
sys 1m31.722s

$ # fix the bug
$ vi apps/ca.c
[...]
    
$ # run infer incrementally, using one CPU only
$ time infer -j 1 run -reactive -- make 
[...]
real 0m41.296s
user 0m36.920s
sys 0m2.379s
```

Infer runs considerably faster on the code change than on the entire project. The reactive mode does the translation work of capture and analysis for only the changed file. The code fix in `apps/ca.c` as given by OpenSSL developers involves inserting a simple null check.

```clike
2778 revtm = X509_gmtime_adj(NULL, 0);
2779
2780 if (!revtm)
2781 return NULL;
2782
2783 i = revtm→length + 1;
```

This faster incremental analysis is helpful for [Infer’s deployment model at Facebook](https://research.fb.com/publications/moving-fast-with-software-verification/), where it is integrated with the code review system; even a linear time analysis would be too slow if it had to operate on the whole program when presented with a code change.

## Frequency of inter-procedural fixes

People sometimes ask, rightly, whether inter-procedural analysis would catch many bugs local analyses do not, and whether we even need inter-procedural analysis. After all, the local tools go after some of the same categories of bugs that we talk about with Infer (for example, null dereferences).

We looked at 100 recent Infer reports that Facebook developers had fixed, in several bug categories. Because inter-file bugs are necessarily classified as inter-procedural, note that the inter-procedural bugs are those in the two rightmost columns in the table below.

Intra-procedural means the bug took place within the scope of a single function. Intra-file but inter-procedural means that the bug trace goes through more than one procedure or function, touching several procedures but with the supporting trace and reasoning confined to a single file. Inter-file is an inter-procedural bug that spans more than one file.

![](https://engineering.fb.com/wp-content/uploads/2017/09/GNKjQQEHp86za2kAAAAAAAC2Awl6bj0JAAAB.jpg)

<sub>100 recent fixes in several bug categories</sub>

We find that the majority of null dereferences fixed in Java are inter-procedural. In Objective-C, a larger proportion is intra-procedural. Part of the reason for the difference is that we have implemented a number of intra-procedural checks that search for ObjC-specific code patterns, based on input from Facebook developers. Inter-procedural bugs still count for a non-negligible proportion.

Thread Safety is a check for data races between methods in Java classes annotated with @ThreadSafe. Again, the majority are inter-procedural and even inter-file. The data races are on accesses to fields or calls to containers that often are in different classes than the one annotated @ThreadSafe. For the purposes of this table, when we have a read/write race involving two procedures but where the accesses are within the procedures themselves, we consider it an intra-procedural race. Discovering it requires two pieces of intra-procedural reasoning, about two procedures.

Allocates Memory is a check for whether an allocation is reachable from a procedure annotated with @NoAllocation.

Thread Safety and Allocates Memory are based on specialized inter-procedural analysis, distinct from the [Separation Logic-based one](http://dl.acm.org/citation.cfm?id=2049700) referred to in the example bugs from DuckDuckGo and OpenSSL. Thread Safety uses a concept of summary that records access and locking information rather than more general memory properties; it is tailored to the specific problem of reporting races. Allocates Memory is part of an analyzer for annotation reachability whose summaries store trace information. These two analyzers use a framework, Infer.AI, for writing compositional static analyzers in Infer.

Bad Pointer Comparison is a lint check for Objective-C that identifies when a boxed primitive type such as `NSNumber *` is coerced to a Boolean in a comparison. It is written in AL, our [AST language](https://engineering.fb.com/posts/277643589367408/al-a-new-declarative-language-for-detecting-bugs-with-infer/). We include it for balance, as an example of a useful check that does not require inter-procedural reasoning.

## Conclusion

As static analyzers become increasingly common, they often are used to perform simple procedure-local (intra-procedural) checks. Such analyses, exemplified by the open source tools Findbugs, Error-prone, Clang Static Analyzer, and Android Lint, are deployed relatively broadly and provide positive value. For instance, a [Google static analysis team reports](https://research.google.com/pubs/pub43322.html) that it uses internal intra-procedural checks widely but avoids inter-procedural analysis at scale. Facebook deploys several linting and intra-procedural analysis solutions internally, and Infer includes its own in the [AL Language](https://engineering.fb.com/posts/277643589367408/al-a-new-declarative-language-for-detecting-bugs-with-infer/).

By comparison, inter-procedural analysis appears to be deployed less often, but there have been other key developments. Two significant deployments were Microsoft’s [Prefix and Static Driver Verifier](https://www.microsoft.com/en-us/research/wp-content/uploads/2004/05/ieee_sw_righting_software.pdf); Static Driver Verifier has limited scaling capabilities, whereas Prefix works in a bottom-up fashion, like an earlier version of Infer, and is scaled to large codebases. The [proprietary static analyzer from Coverity](http://popl.mpi-sws.org/2014/andy.pdf)also supports inter-procedural analysis, using some techniques that are similar to those of Infer and others that are different. These efforts provide context, but we haven’t made a detailed comparison. An [independent study of several advanced static-analysis tools found that they catch different sets of bugs](http://techdigest.jhuapl.edu/TD/td3202/32_02-Pendergrass-Lee.pdf), which suggests that there is no single best analyzer that supersedes all others.

Because Infer is compositional, meaning that summaries of procedures are generated independently of calling contexts, it can scale to large codebases and work incrementally on frequent code modifications. Generally speaking, we feel that there is much unlocked potential for advanced static analysis techniques beyond linting, such as those that check for inter-procedural and other deeper bugs. In particular, compositional program analysis is an area that would benefit from further development, both in academics and industry.
