---
title: FingerTips
apple_id: DTS40008124
resource_type: Sample Code
platform: Safari
topic: null
technology: null
published: '2008-12-09'
source_url: https://developer.apple.com/library/archive/samplecode/FingerTips/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:08:43.770129Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [FingerTips](FingerTips.md)


[Next](data.js.md)[Previous](FingerTips.md)

# ReadMe.txt

```
### FingerTips ###

===========================================================================
DESCRIPTION:

"FingerTips" demonstrates how to use CSS Transforms and Transitions extensions and iPhone multi-touch events to render, animate, and interact with objects in 3D space. It displays a 3D carousel that contains a list of iPhone Finger Tips video posters. Users can flick upward or downward the list, tap on any poster to slide to an info pane from which the associated video can be played.

= Populating the Carousel Content =

The "index.html" file contains a template that is dynamically populated. First, the contents of the carousel are added within the <ol id="ring"> element as the init() function in script.js is called upon document loading and directly calls populate_ring(). The populate_ring() function then iterates through the data structure provided in the "data.js" file to create an <li> element for each cell in the carousel, setting a transform that will translate the cell forward on the z-axis and rotate by a decrement of 30 degrees. Finally, each cell has a "touchstart" event registered so that the ring controller can later identify the beginning of an interaction with the carousel and track what cell was at its origin.

= Carousel Interaction =

Further interactions with the carousel will all be routed through the ring_controller.handleEvent() function, where the touch events information will be dispatched to various functions depending on their type. When we initially get a "touchstart", handled by ring_controller.interactionStart(), we set up the dragging interaction by register for "touchmove" and "touchend" events on the whole window, thus making our carousel capture all touch interactions from that point on. We also track the location of the first touch, current rotation of our carousel and the cell that initiated the interaction.

Then as the user drags his finger across the screen, the ring_controller.interactionMove() function is called, updating the rotation of the carousel based on the current touch location and initial states set in ring_controller.interactionStart(). Rotation of the whole carousel is perfomed by updating the transform of the <ol id="ring">, which contains all the various cells. At this point, it's important to note that, in "style.css", we set "-webkit-transform-style: preserve-3d" on our ring container, using the "#ring" selector, letting the contents of the ring be rotated in 3D space as opposed to transforming a flat 2D plane, which is the traditional model in CSS. Try removing this property to see the difference as you interact with the carousel.

Finally, as the interaction ends, the ring_controller.interactionEnd() function is called, and we remove the "touchmove" and "touchend" event listeners on our window. Additionally, we track if the ring_controller.touchMoved variable we set to "false" in ring_controller.interactionStart() is still "false", or if it were changed to "true" in calls to ring_controller.interactionMove(). This allows us to identify if we actually dragged the carousel around or simply tapped a cell in the carousel, which will result in centering the tapped item to the center of the carousel and triggering a sliding transition to reveal the info pane to the right.

= Entering the Info Pane =

This selection mechanism is performed by the ring_controller.performSelection() function, where we figure out the new rotation for the carousel needed to center the tapped cell, turning transitions on for the carousel's transform so that we get a nice and smooth animation. The sliding part of the selection mechanism is performed in ring_controller.selectionTransitionDone(), which is automatically called when the centering transition ended. Indeed, back in ring_controller.init(), we registered an event listener for the "webkitTransitionEnd" event so that we would track when a transition on the carousel would complete, allowing us to chain transitions. So when we get this event, and ring_controller.selectionTransitionDone() is called, we turn transitions off on our carousel again, so that rotation updates during dragging interactions are performed as discrete changes, and call item_selected() which will trigger the sliding transition and update the contents of the info pane with update_info_pane().

= Video Playback =

Within the info pane, we have text and graphics, but also the <img id="info-play-button" src="ui/play_button.png"> play button that was wired, back in init(), to call the play_movie() function when it's touched. We also have the <embed id="movie" type="video/quicktime"> media element inside the pane, and this element get its url set dynamically, based on what item in the carousel we selected, by a call to .SetURL() and finally is played by calling .Play(), which also enters full-screen video mode for the best iPhone media playback experience.

= Exiting the Info Pane =

Finally, just as we had set a touch interaction on the play button, we also added such an interaction on the <div id="info-back-button">Finger Tips</div> element, which looks like an iPhone back button, to call the go_back() function, triggering a slide transition bringing the carousel back in the scene.

= Miscellaneous =

You'll also notice that we have the <div id="ring-aligner"> element as part of the carousel tree. This element is styled within style.css, with the "#ring-aligner" selector, to push the whole carousel back in the z axis. Indeed, as we built the items in populate_ring(), we used a z-axis translation to project the elements and create the 3D carousel, but in order to have nicely rendered text and graphics, we translate the whole carousel with an inverse z-axis translation to have the item in the center of the carousel exactly positioned at z=0.

= Further Reading =

Read the following references to learn about all the CSS properties used in this sample, as well as Touch Events:

http://developer.apple.com/webapps/docs/documentation/InternetWeb/Conceptual/SafariVisualEffectsProgGuide/
http://developer.apple.com/webapps/docs/documentation/AppleApplications/Reference/SafariJSRef/TouchEvent/TouchEvent.html

= Using the Sample =

Place this sample's files on your own webserver (eg. Mac OS X Personal Web Server). Open index.html in an iPhone or iPod touch running OS 2.0 or iPhone Simulator with iPhone OS 2.0 (/Developer/Platforms/iPhoneSimulator.platform/Developer/Applications). Drag your fingers across the screen to rotate the carousel and select items.

===========================================================================
BUILD REQUIREMENTS:

iPhone OS 2.0

===========================================================================
RUNTIME REQUIREMENTS:

iPhone OS 2.0

===========================================================================
PACKAGING LIST:

index.html -- the main HTML file to load in the browser
style.css -- the CSS file
script.js -- the JavaScript file
data.js --  the JavaScript data source
ui/ -- the directory containing various images used across the UI
posters/ -- the directory containing the PNG images displayed on the carousel
movies/ -- the directory containing the movies

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.0
- First version.

===========================================================================
Copyright (C) 2008 Apple Inc. All rights reserved.
```

[Next](data.js.md)[Previous](FingerTips.md)

