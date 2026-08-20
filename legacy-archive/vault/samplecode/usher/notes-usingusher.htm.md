---
title: usher
apple_id: DTS10001057
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/usher/Listings/notes_usingusher_htm.html
archived_at: '2026-07-26T19:53:08.415007Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [usher](usher.md)


[Next](sources-AppSupport.c.md)[Previous](usher.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# notes/usingusher.htm

```

<BODY BGCOLOR="#FFFFFF">
    <h2>USING USHER</h2>
    <ul>
        <li>If you will be sending video, attach the video camera to the computer first
        <li>Drop an .xml file onto the application (2 sample ones can be found in the folder /usher/notes)
        <li>Select &quot;Settings&quot; from the Presentation menu to configure the broadcast.  Select the appropriate capture device (video camera, audio source) and the compression you want to use.     <li>Press the &quot;Start&quot; button to start the broadcast
        <li>Press the button again to stop the broadcast

        <li>To view the broadcast, drop the corresponding .sdp file onto QuickTime Player.
    </ul>
    <p></p>
    <h2>KNOWN PROBLEMS/LIMITATIONS</h2>
    <ul>
        <li>Menus do not disable correctly; menus beep instead of showing up as disabled
        <li>Info window doesn't scroll
        <li>The presentation cannot be configured after the broadcast has started
        <li>If you stop the broadcast, you cannot start it again
    </ul>
    <h2></h2>
    <h2>BUILDING USHER</h2>
    <ul>
        <li>Place the QuickTime SDK headers and libraries in a folder called &quot;QTSDK&quot; at the same level as the usher folder (i.e. you will have a folder that contains the QTSDK folder and the usher folder).
        <li>Launch /uhser/cwproject/usher.mcp in Code Warrior 6
        <li>Build the project
        <li>The usher application will be built in the folder /usher/output/
    </ul>
    <h2></h2>
    <h2></h2>
</BODY>
```

[Next](sources-AppSupport.c.md)[Previous](usher.md)

