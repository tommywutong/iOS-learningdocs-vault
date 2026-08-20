---
title: Developing SMIL Presentations
apple_id: TP40000999
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-03-29'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/CreatingPresentations/Creating_a_1resentation.html
archived_at: '2026-07-18T02:19:37.555002Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Developing SMIL Presentations](toc.md)


[!](Creating_an_resentation.md) [!](Linking_Presentations.md)

## Creating a Sequence-Based Presentation

You can create a presentation that contains media objects
that are displayed sequentially to the viewer instead of in parallel.
To do that, you use the WOSMILSeq element.

This section shows you how to create a presentation with two
video elements that are presented sequentially. The component contains
a WORepetition element that uses the keys `movies` and `movieName` to
lay out the video elements of the presentation.

1. Add two movie
   files to the Web Server Resources group of the Smile project.
   ![[image: ../art/moviefiles.gif]](../art/moviefiles.gif)

2. Add a new component to the Smile project, as described in ["Creating a SMIL Component"](Creating_a__resentation.md#apple-infeerkkijcuo).
   Name the component `Movies`.
3. Enter values for the bindings of the WOSMILRootLayout element.
   1. Enter `370` for
      the `height` binding.
   2. Enter `480` for the `width` binding.
4. Put a WOSMILRegion element inside the WOSMILHeadLayout element,
   after the WOSMILRootLayout element.
   1. Enter `"meet"` for
      the `fit` binding.
   2. Enter `370` for the `height` binding.
   3. Enter `0` for the `left` binding.
   4. Enter `"Region1"` for
      the `regionID` binding.
   5. Enter `0` for the `top` binding.
   6. Enter `480` for the `width` binding.
5. Put a WOSMILSeq element inside the WOSMILBody element. Enter `"Movie
   sequence"` for its `title` attribute.
6. Add the `movies` key
   to the component as an array of Strings (no accessor methods are required).
   1. Choose Edit > Edit
      Source > Add Key.
   2. Enter `movies` in
      the Name text field.
   3. Select "Array of" as the key's type and make sure "String
      (`java.lang.String`)"
      is selected in the pop-up menu.
   4. Ensure that "An instance variable" is selected under "Generate
      source code for," and click Add.
   ![[image: ../art/movieskey.gif]](../art/movieskey.gif)
7. Add the `movieName` key
   as a String. Like `movies`,
   no accessor methods are needed.
8. Put a WORepetition element inside the WOSMILSeq element. Bind `list` to `movies` and `item` to `movieName`.
   ![[image: ../art/movieswo_bindingkeys.gif]](../art/movieswo_bindingkeys.gif)
9. Replace the text "Repetition" inside the WORepetition
   with a WOSMILMediaObject.
   1. Enter `movieName` for
      the `filename` binding.
   2. Enter `"app"` for
      the `framework` binding.
   3. Enter `"video"` for
      the `mediaObjectName` binding.
   4. Enter `"Region1"` for
      the `regionID` binding.
10. Edit the constructor in `Movies.java` so
    that it looks like the following.

    ```
    public Movies(WOContext context) {
        super(context);
        NSMutableArray availableMovies = new NSMutableArray();
        availableMovies.addObject("ipod_60_480.mov");
        availableMovies.addObject("ipod_intro_m240.mov");
        movies = new NSArray(availableMovies);
    }
    ```

Build and run the application, and connect to it using the
appropriate URL, which should look like

```
http://<host>:<port>/cgi-bin/WebObjects/Smile.woa/wo/Movies.wo
```

After clicking Play, you should see the movies in sequence
in QuickTime Player.

 ![[image: ../art/ipodad.gif]](../art/ipodad.gif)

[!](Creating_an_resentation.md) [!](Linking_Presentations.md)

---

© 2002 Apple Computer, Inc. (Last Updated March 29, 2002)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
