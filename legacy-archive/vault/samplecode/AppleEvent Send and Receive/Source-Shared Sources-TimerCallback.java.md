---
title: AppleEvent Send and Receive
apple_id: DTS10000215
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/AppleEvent_Send_and_Receive/Listings/Source_Shared_Sources_TimerCallback_java.html
archived_at: '2026-07-18T03:01:08.885782Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AppleEvent Send and Receive](AppleEvent%20Send%20and%20Receive.md)


[Next](Document%20Revision%20History.md)[Previous](Source-Shared%20Sources-Timer.java.md)

# Source/Shared Sources/TimerCallback.java

```
/**
 * Apple Worldwide Developer Technical Support
 *
 * Sample showing how to send and receive AppleEvents using JDirect 2.
 *
 * File: TimerCallback.java
 *
 * This interface should be implemented by classes who want a callback from the Timer class.
 * @see Timer
 *
 * @author Levi Brown
 * @author Apple Computer, Inc.
 *
 * Copyright ©1999 Apple Computer, Inc.
 * All rights reserved.
 *
 * @version 1.0
 * 4/15/1999 Shipped as 'AppleEvent Send and Receive' sample.
 *
 * You may incorporate this sample code into your applications without
 * restriction, though the sample code has been provided "AS IS" and the
 * responsibility for its operation is 100% yours.  However, what you are
 * not permitted to do is to redistribute the source as "Apple Sample
 * Code" after having made changes. If you're going to re-distribute the
 * source, we require that you make it clear in the source that the code
 * was descended from Apple Sample Code, but that you've made changes.
 */
public interface TimerCallback
{
    /**
     * This function gets called by the timer when the elapsed time reaches the sleep time.
     */
    public void timeIsUp();
}
```

[Next](Document%20Revision%20History.md)[Previous](Source-Shared%20Sources-Timer.java.md)

