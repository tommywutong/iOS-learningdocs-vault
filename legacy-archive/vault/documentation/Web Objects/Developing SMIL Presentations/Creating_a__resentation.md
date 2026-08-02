---
title: Developing SMIL Presentations
apple_id: TP40000999
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-03-29'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/CreatingPresentations/Creating_a__resentation.html
archived_at: '2026-07-18T02:19:50.794191Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Developing SMIL Presentations](toc.md)


[!](Creating%20Presentations.md) [!](Creating_an_resentation.md)

## Creating a Static Presentation

This section shows you how to create a simple SMIL presentation
that includes a text media object.

### Creating the SMIL Project

To create a SMIL presentation, you start by creating a WebObjects
Application project in Project Builder.

1. Launch Project
   Builder.
2. Choose File > New Project.
3. Select WebObjects Application as the project type and click
   Next.
    ![[image: ../art/newsmilapp.gif]](../art/newsmilapp.gif)
4. Name the project, choose a location for it, and click Next.
   ![[image: ../art/newsmilapp2.gif]](../art/newsmilapp2.gif)
5. Add the JavaWOSMIL framework. In the Choose Frameworks pane
   of the Assistant:
   1. Click Add.
   2. Navigate to `/System/Library/Frameworks/JavaWOSMIL.framework`.
   3. Click Choose and then click Finish.
   ![[image: ../art/newsmilapp3.gif]](../art/newsmilapp3.gif)

### Creating a Text File and Adding It to the Project

Using a text editor, create a file containing the text "`Hello,
World.` " and save it as `hello.txt` in
your project directory (make sure that the string ends with a space
and a return character).

 ![[image: ../art/hellotxt.gif]](../art/hellotxt.gif)

In Project Builder add `hello.txt` to
the Web Server Resources group.

1. Select Web
   Server Resources in the Groups & Files list.
2. Choose Project > Add Files.
3. Select `hello.txt` and
   click Open.
4. Select the Web Server target and click Add.

### Creating a SMIL Component

Add a new WebObjects component to the project.

1. Select Web
   Components in the Groups & Files list.
2. Choose File > New File.
3. In the New File pane of the Assistant, select Component under
   WebObjects, and click Next.
4. In the New Component pane, name the component `Hello`,
   ensure the Application Server target is selected, and click Finish.

Now prepare the component so that you can add SMIL elements
to it.

1. Double-click `Hello.wo` in
   the Groups & Files list to open the component in WebObjects Builder.
2. Choose Partial Document from the pop-up menu in the Static
   Inspector pane of the Page Inspector window. This removes the standard
   HTML tags from the component.
    ![[image: ../art/pageinspector_partialdoc.gif]](../art/pageinspector_partialdoc.gif)
3. Display the WOSMIL Palette window by choosing Window >
   Palette, and select the SMIL palette.
4. Put a WOSMILDocument element on the layout area. (You accomplish
   this by dragging the element from the palette onto the layout area.)
   ![[image: ../art/smilpalettedrag.gif]](../art/smilpalettedrag.gif)
5. Put a WOSMILHead element inside the WOSMILDocument element.
6. Put a WOSMILHeadLayout element inside the WOSMILHead element.
7. Put a WOSMILBody element inside the WOSMILDocument element,
   below the WOSMILHead element.
8. Put a WOSMILRootLayout element inside the WOSMILHeadLayout
   element.

### Adding the Appropriate SMIL Elements to the Component

Now you're ready to add the SMIL elements that will make
up your presentation.

1. Put a WOSMILRegion
   element to the right of the WOSMILRootLayout element.
2. Put a WOSMILMediaObject element inside the WOSMILBody element.

[Figure 3-1](#apple-infeerscizauo) shows what the `Hello.wo` component
should look like when you're done.

__Figure
3-1 Hello.wo component in WebObjects Builder__

![[image: ../art/hellowo.gif]](../art/hellowo.gif)

Finally, enter values for the bindings that provide information
to your presentation viewer, such as the size of the window, the
position of the regions within the window, and information on the
media objects to be displayed.

1. Enter information
   for the WOSMILRootLayout element.
   1. Select the WOSMILRootLayout
      element in the layout area.
   2. Choose Window > Inspector to display the WOSMILRootLayout
      Binding Inspector window (if it's not already displayed).
   3. Enter `"#FFFFFF"` for
      the `bgcolor` binding.
   4. Enter `200` for the `height` and `width` bindings.
2. Enter information for the WOSMILRegion element.
   1. Select the WOSMILRegion
      element next to the WOSMILRootLayout element.
   2. Enter `75` for the `height` binding.
   3. Enter `200` for the `width` binding.
   4. Enter `0` for the `top` and `left` bindings.
   5. Enter `"Region1"` for
      the `regionID` binding.
   6. Enter `"meet"` for
      the `fit` binding.
3. Enter information for the WOSMILMediaObject element.
   1. Select the WOSMILMediaObject
      element inside the WOSMILBody element.
   2. Enter `"hello.txt"` for
      the `filename` binding.
   3. Enter `"app"` for
      the `framework` binding.
   4. Enter `"text"` for
      the `mediaObjectName` binding.
   5. Enter `"Region1"` for
      the `regionID` binding.

### Building and Running the Application

Now you're ready to test the application. To make things
easier, you should add two build settings to the project: `WOPort` and `WOAutoOpenInBrowser`.

1. Display the
   Targets pane in Project Builder.
2. Select Smile in the Targets list.
3. Display the Executables pane.
4. Click Add.
5. Under Launch Arguments, enter the following text:

   ```
   -WOPort 1234 -WOAutoOpenInBrowser false
   ```

Build and run the application by choosing Build > Build
and Run. Copy the application URL to the application from the run
pane.

 ![[image: ../art/helloapprun.gif]](../art/helloapprun.gif)

### Viewing the Presentation

Now that the application is running, you're ready to view
the Hello presentation. Launch QuickTime Player, choose File >
Open URL, paste the application's URL in the text field of the
Open URL window, add `/wo/Hello.wo` to
it, and click OK. (This points your player to the SMIL component
you created in the previous sections instead of the default component, `Main.wo`.)

You should see a window similar to the one in [Figure 3-2](#apple-infeer2girdes).

__Figure
3-2 Hello presentation in QuickTime Player__

![[image: ../art/qtphello.gif]](../art/qtphello.gif)

This is the code your viewer receives:

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
        </layout>
    </head>
    <body id="0.0.1.1.0">
    <text src="http://ebruce:1234/cgi-bin/WebObjects/Smile.woa/ wr?wodata=%2FUsers%2Fernest%2FWebObjects%2FProjects%2FSMIL%2FSmile%2Fhello.txt"
        region="Region1" id="0.0.1.1.0.1.0.0">
    </text>
    </body>
</smil>
```

Notice that WebObjects generates `id` attributes
and their corresponding values for the SMIL tags so that you don't
have to come up with them. In some cases, however, you have to add
an `elementID` binding
to SMIL elements in WebObjects Builder. For example, event-based
presentations may require references between media objects. In that
case, you should add `elementID` bindings
with values that can be understood at a glance. See ["Creating an Event-Based Presentation"](Creating_an_resentation.md#apple-infeeskkjbceo) for an example of this.

[!](Creating%20Presentations.md) [!](Creating_an_resentation.md)

---

© 2002 Apple Computer, Inc. (Last Updated March 29, 2002)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
