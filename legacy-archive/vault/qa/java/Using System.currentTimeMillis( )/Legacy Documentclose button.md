---
title: Using System.currentTimeMillis( )
apple_id: DTS10001395
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-02-02'
source_url: https://developer.apple.com/library/archive/qa/java/java20.html
archived_at: '2026-07-18T02:29:41.994679Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA20Using System.currentTimeMillis( ) |

|  |  |
| --- | --- |
| ---   Q: My Java application relies on the values returned by `System.currentTimeMillis( )` for its internal timing. This routine seems to return incorrect values on portable Macintosh computers. For example, I have some code:   |  | | --- | | ``` import java.text.*; public class CurrentTimeChecker implements Runnable {     Thread thread = new Thread(this);     long[] times = new long[500];     long lastT = 0;     int timesCursor = 0;     public boolean timeToStop = false;     NumberFormat nf = null;     public CurrentTimeChecker()     {         initNF();         thread.start();     }     void initNF()     {         nf = NumberFormat.getNumberInstance();         nf.setMinimumFractionDigits(0);         nf.setMaximumFractionDigits(0);         int numDigits = Long.toString(Long.MAX_VALUE).length();         nf.setMinimumIntegerDigits(numDigits);         nf.setMaximumIntegerDigits(numDigits);     }     static public void main(String[] args)     {         new CurrentTimeChecker();     }      public void run()     {         while(! timeToStop)         {             try             {                 Thread.sleep(1000);             }             catch(InterruptedException e) {}             long t = System.currentTimeMillis();             if ( t > lastT )                 System.out.println(nf.format(t));             if ( t < lastT )             {                 System.out.println(nf.format(t) + "  <---- ");                 java.awt.Toolkit.getDefaultToolkit().beep();             }             times[timesCursor++] = t;             if (timesCursor >= times.length)                 timesCursor = 0;             lastT = t;         }         System.out.println("Finished...");     } } // class CurrentTimeChecker ``` |    My code sleeps for a certain interval, then calculates the elapsed time. On my PowerBook, sometimes I get negative time intervals. Why does this happen?  A: This is the result of a bug in MRJ 2.1.4. It is not the `sleep( )`that is causing the problem, it is the call to `System.currentTimeMillis( )` that is causing this behavior. This problem may occur for ANY interval calculation regardless of whether `sleep( )` is called or not. As of MRJ 2.2, the issue has been resolved. Incidentally, the fix was discovered as a consequence of long file name testing on Mac OS 9.  Mac OS 9 has a millisecond accurate time service available that works with "modern" hardware. Older systems and older hardware have to make do with unreconciled fast timers and the 1-second granular clock. Previous MRJ versions would sample the 1-second granule clock, mark that sample as being .0, and count milliseconds forward from the timer clock. This algorithm would restart every minute. The effect is that every minute MRJ would report times being up to plus/minus one second from the previous time. There may even have been cases where reported time intervals would briefly go backwards.  The new behavior on Mac OS 9 and "modern" hardware (G3 for the most part) is to let Mac OS do it for us. Otherwise, we pause on startup and note and track (with the timer) the transition of the 1-second granule clock. This calibration is repeated after an interval of several minutes.  This new fix is present in MRJ 2.2. Developers may download MRJ 2.2 from the [MRJ 2.2 Download page](https://developer.apple.com/java/text/download.html).  For developers who do not wish to update to the lastest version, we recommend that you use Mac OS 9, which should minimize this problem on new hardware. If you need to do timing on previous operating systems or older machines, we recommend that you check out [Greg Guerin's](mailto:glguerin@amug.org) example on how to use the Macintosh microsecond timer, instead. Not only will you not experience this problem, but you will also be able to get finer grained control:  "If you're interested, the [source for my test program](http://www.amug.org/~glguerin/sw/hax/Anti-time-bandit.sit.bin) has a class that will read the free-running microsecond timer under MRJ. Obviously, it won't work on other platforms, but you can write platform-sensing Java code to pick between implementations. As far as I can tell, this counter is completely free-running, and counts microseconds since last restart, though I don't know if it has PowerBook peculiarities in low-power modes. Also, it doesn't seem to be subject to the backwards-time drift correction currently observable in MRJ. While this won't help sleep(long) or wait(long), it should let you calculate elapsed times without worrying about drift-correcting adjustments botching the calculation." [Feb 02 2000] |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
