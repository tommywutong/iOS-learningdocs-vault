---
title: Developing SMIL Presentations
apple_id: TP40000999
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-03-29'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/CreatingPresentations/Creating_an_resentation.html
archived_at: '2026-07-18T02:20:13.655768Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Developing SMIL Presentations](toc.md)


[!](Creating_a__resentation.md) [!](Creating_a_1resentation.md)

## Creating an Event-Based Presentation

One of the features that makes SMIL presentations interesting
is the ability to define when a media object gets displayed. For
instance, you can have an image displayed five seconds after the
presentation is started and have another media object appear two
seconds after the first image appears. This section shows you how
to do just that. You'll modify the `Hello.wo` component
of the Smile project created in ["Creating a Static Presentation"](Creating_a__resentation.md#apple-infeerkgijeem).

1. Open the
   Smile project in Project Builder if it's not already open.
2. Add two images to the Web Server Resources group.
   ![[image: ../art/smileprojwsr.gif]](../art/smileprojwsr.gif)

3. Open `Hello.wo` in
   WebObjects Builder if it's not already open.
4. Put a second WOSMILRegion element inside the WOSMILHeadLayout
   element.
   1. Enter `75` for
      the `top` binding.
   2. Enter `0` for the `left` binding.
   3. Enter `100` for the `height` binding.
   4. Enter `100` for the `width` binding.
   5. Enter `"meet"` for
      the `fit` binding.
   6. Enter `"Region2"` for
      the `regionID` binding.
5. Put a WOSMILPar element inside the WOSMILBody element, below
   the WOSMILMediaObject element.
6. Select the WOSMILMediaObject element and choose Edit >
   Cut.
7. Put the cursor inside the WOSMILPar element and choose Edit
   > Paste.
8. Put a second WOSMILMediaObject element inside the WOSMILPar
   element, below the existing WOSMILMediaObject element and enter
   the appropriate values for its bindings.

   To make the media
   object appear five seconds after the presentation starts, you have
   to add the `begin` binding
   to the element.

   1. Make sure the second
      WOSMILMediaObject is selected.
   2. Click anywhere in the WOSMILMediaObject Binding Inspector
      window.
   3. Press Return. A new binding appears titled `binding1`.
   4. Change the binding's name to `begin` and
      enter `"5s"` as
      its value.
   5. Add a binding named `dur` and
      set its value to `"10s"`.
   6. Assign this media object to Region2 by entering `"Region2"` for
      the `regionID` binding.
   7. Enter `"img"` for
      the `mediaObjectType` binding.
   ![[image: ../art/ipodimgbindings.gif]](../art/ipodimgbindings.gif)

Now `Hello.wo` should
look like [Figure 3-3](#apple-infeeq2kizdec).

__Figure
3-3 Hello.wo component after adding second
WOSMILMediaObject element__

![[image: ../art/hellowo2.gif]](../art/hellowo2.gif)

Save `Hello.wo`.
If the Smile application is not running, start it. In QuickTime
Player, connect to the application using the appropriate URL, which
should similar to the following one:

```
http://<host>:<port>/cgi-bin/WebObjects/Smile.woa/wo/Hello.wo
```

Click Play in QuickTime Player. The image appears after five
seconds have passed.

Now you'll add a media object whose display is tied to the
appearance of another media object instead of the beginning of the
presentation.

1. Add an `elementID` binding
   to the second WOSMILMediaObject element and set its value to `"MediaObject2"`.
2. Put a third WOSMILMediaObject element inside the WOSMILPar
   element.
   1. Add
      a `begin` binding and set
      its value to `"id(MediaObject2)(2s)"`.
      This makes this WOSMILMediaObject appear two seconds after the second
      WOSMILMediaObject (with `"MediaObject2"` as
      its `elementID`) is displayed.
   2. Add a `dur` binding
      and set its value to `"8s"`.
   3. Set the `regionID` binding
      to `"Region1"`.
   4. Set the mediaObjectName binding to `"img"`.
   5. Bind `filename` to
      the second image file you added to the project.
   ![[image: ../art/poweredbywobindings.gif]](../art/poweredbywobindings.gif)

Save `Hello.wo` and
reconnect to the application using QuickTime Player. After playing
the presentation, you should see a window similar to the one in [Figure 3-4](#apple-infeescdinbum).

__Figure
3-4 Hello SMIL presentation with two images__

![[image: ../art/qtphelloipod.gif]](../art/qtphelloipod.gif)

This is the code your SMIL viewer receives when you connect
to the application:

```
<smil id="0.0">
    <head id="0.0.1.0.0">
        <layout id="0.0.1.0.0.1.0.0">
            <root-layout background-color="#FFFFFF" skip-content="true"
                width="200" height="200" id="0.0.1.0.0.1.0.0.1.0.0">
            </root-layout>
            <region z-index="0" skip-content="true" width="200" height="75"
                left="0" fit="meet" top="0" id="Region1">
            </region>
            <region z-index="0" skip-content="true" width="100"
                height="100" left="0" fit="meet" top="75" id="Region2">
            </region>
        </layout>
    </head>
    <body id="0.0.1.1.0">
        <par region="Region1" id="0.0.1.1.0.1.0.0">
            <text dur="5s" src="http://ebruce:1234/cgi-bin/WebObjects/Smile.woa/ wr?wodata=%2FUsers%2Fernest%2FWebObjects%2FProjects%2FSMIL%2FSmile%2Fhello.txt"  region="Region1" id="0.0.1.1.0.1.0.0.1.0.0">
            </text>
            <img dur="10s" src="http://ebruce:1234/cgi-bin/WebObjects/Smile.woa/ wr?wodata=%2FUsers%2Fernest%2FWebObjects%2FProjects%2FSMIL%2FSmile%2Fipod.jpg"  region="Region2" id="MediaObject2" begin="5s">
            </img>
            <img dur="8s" src="http://ebruce:1234/cgi-bin/WebObjects/Smile.woa/ wr?wodata=%2FUsers%2Fernest%2FWebObjects%2FProjects%2FSMIL%2FSmile%2Fpoweredbywebo bjects.gif" region="Region1" id="0.0.1.1.0.1.0.0.1.2.0"  begin="id(MediaObject2)(2s)">
            </img>
        </par>
    </body>
</smil>
```

Notice that the `id` attribute
of the second media object is now `"MediaObject2"` instead
of the one generated by WebObjects.

[!](Creating_a__resentation.md) [!](Creating_a_1resentation.md)

---

© 2002 Apple Computer, Inc. (Last Updated March 29, 2002)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
