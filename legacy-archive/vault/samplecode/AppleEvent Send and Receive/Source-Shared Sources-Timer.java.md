---
title: AppleEvent Send and Receive
apple_id: DTS10000215
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/AppleEvent_Send_and_Receive/Listings/Source_Shared_Sources_Timer_java.html
archived_at: '2026-07-18T03:01:08.935334Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AppleEvent Send and Receive](AppleEvent%20Send%20and%20Receive.md)


[Next](Source-Shared%20Sources-TimerCallback.java.md)[Previous](Source-Shared%20Sources-NativeException.java.md)

# Source/Shared Sources/Timer.java

```
/**
 * Apple Worldwide Developer Technical Support
 *
 * Sample showing how to send and receive AppleEvents using JDirect 2.
 *
 * File: Timer.java
 *
 * A simple timer class.
 * @see TimerCallback
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
public class Timer
{
    /**
     * Instantiates a new Timer.
     * @param the amount of time for the timer to run before calling
     * the callback (time in milliseconds).
     * @param the TimerCallback object to call when the time is up.
     */
    public Timer(int sleepTime, TimerCallback callback)
    {
        this.sleepTime = sleepTime;
        this.callback = callback;
        runObj = new RunObj();
    }

    /**
     * Starts the timer running.
     * If the timer is currently running, it will be reset.
     * @see #stop
     */
    public void start()
    {
        if (thread == null || !thread.isAlive())
        {
            thread = new Thread(runObj);
            thread.start();
        }
        else
        {
            thread.stop();
            thread = null;
            start();
        }
    }

    /**
     * Stops the timer immediately.
     * @see #start
     */
    public void stop()
    {
        thread.stop();
        thread = null;
    }

    /**
     * Simply contains the body of the running thread
     */
    class RunObj implements Runnable
    {
        public void run()
        {
            try
            {
                Thread.sleep(sleepTime);
                callback.timeIsUp();
            }
            catch (InterruptedException exc) { }
        }
    }

    protected int sleepTime;
    protected TimerCallback callback;
    protected Thread thread;
    protected RunObj runObj;
}
```

[Next](Source-Shared%20Sources-TimerCallback.java.md)[Previous](Source-Shared%20Sources-NativeException.java.md)

