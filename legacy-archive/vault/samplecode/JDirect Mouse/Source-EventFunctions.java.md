---
title: JDirect Mouse
apple_id: DTS10000217
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/JDirect_Mouse/Listings/Source_EventFunctions_java.html
archived_at: '2026-07-18T03:13:09.188169Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [JDirect Mouse](JDirect%20Mouse.md)


[Next](Source-JDirectMouse.java.md)[Previous](JDirect%20Mouse.md)

# Source/EventFunctions.java

```
import  com.apple.mrj.macos.libraries.InterfaceLib;

/**
 * Apple Worldwide Developer Technical Support
 *
 * A simple example of how to obtain the mouse location using the Mac OS Toolbox through JDirect 2.
 *
 * File: EventFunctions.java
 *
 * The class <CODE>EventFunctions</CODE> contains static native methods for all functions 
 * defined in the C header <CODE>Events.h</CODE><BR>
 * <BR>
 * These native methods are invoked via JDirect 2.0 which can bind directly to the MacOS 
 * shared library InterfaceLib.  Unlike JNI, no intermediate glue code is neeeded.<BR>
 *
 * @author Apple Computer, Inc.
 *
 * Copyright ©1999 Apple Computer, Inc.
 * All rights reserved.
 *
 * @version 1.0
 * 4/15/1999 Shipped as 'JDirectMouse' sample.
 *
 * You may incorporate this sample code into your applications without
 * restriction, though the sample code has been provided "AS IS" and the
 * responsibility for its operation is 100% yours.  However, what you are
 * not permitted to do is to redistribute the source as "Apple Sample
 * Code" after having made changes. If you're going to re-distribute the
 * source, we require that you make it clear in the source that the code
 * was descended from Apple Sample Code, but that you've made changes.
 */
public class EventFunctions implements InterfaceLib
{
    /**
     * No need to instantiate this class.  All methods are static.
     */
    private EventFunctions() {};

    /**
     * @param mouseLoc      in C: <CODE>Point *mouseLoc</CODE>
     */
    public static void GetMouse(PointStruct mouseLoc) {
        GetMouse(mouseLoc.getByteArray());
    }
    public native static void GetMouse(byte[] mouseLoc);
}
```

[Next](Source-JDirectMouse.java.md)[Previous](JDirect%20Mouse.md)

