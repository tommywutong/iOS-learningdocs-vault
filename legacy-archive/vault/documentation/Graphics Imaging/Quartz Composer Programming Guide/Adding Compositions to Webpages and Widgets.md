---
title: Quartz Composer Programming Guide
apple_id: TP40001357
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzComposer/qc_webkit/qc_webkit.html
archived_at: '2026-07-15T07:37:15.714046Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Composer Programming Guide](Introduction%20to%20Quartz%20Composer%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Using%20the%20QCRenderer%20Class%20to%20Play%20a%20Composition.md)

# Adding Compositions to Webpages and Widgets

The Quartz Composer WebKit plug-in, available in OS X v10.4.7 or later, lets you include Quartz Composer compositions in a webpage or Dashboard widget. The plug-in is a WebKit–style Internet plug-in, available to WebKit–based browsers, such as Safari, OmniWeb, and Shiira. It’s also available to Dashboard widgets, because Dashboard uses the WebKit to render the HTML, CSS, and JavaScript files that make widgets.

This chapter shows how to use the WebKit plug-in and how to manipulate a composition using JavaScript. It also describes the HTML attributes specific to the plug-in and discusses which Quartz Composer patches are not allowed in a composition rendered by a WebKit plug-in.

To add a Quartz Composer composition to a webpage or Dashboard widget, you need to include it in an HTML file using the `<embed>` tag, as shown in Listing 4-1.

__Listing 4-1__  The <embed> tag for a composition

```
<embed type="application/x-quartzcomposer"
       src="my_composition.qtz"
       id="myComposition"
       width="300px"
       height="150px"
       opaque="false">
</embed>
```

Some of the attributes included with the `<embed>` tag in Listing 4-1 are standard attributes found in many HTML elements. Two of the attributes in Listing 4-1 are necessary for the plug-in to be loaded properly:

- `type` tells the browser loading this element that the content to be displayed is a Quartz Composer composition. To render a Quartz Composer composition, set this attribute to `application/x-quartzcomposer`. It is important to include this attribute because without it, a browser may try to use another plug-in to render your composition.
- `src` is the uniform resource locator, or URL, to your composition. The URL can specify either a path relative to the HTML file that contains the `<embed>` tag or a fully qualified path.

The `opaque` attribute is optional and specifies whether your composition uses transparency. By default, it is set to `true`. If your composition uses transparency (that is, the composition is not completely opaque), make sure that you set the attribute to `false`.

See [HTML Attributes for the Quartz Composer WebKit Plug-in](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmznknlto) for a description of other HTML attributes that are available.

If your composition is self-contained and doesn’t require programmatic interaction through JavaScript, you’re done after you include the composition in your HTML. If your composition has changeable parameters or needs to be controlled through JavaScript, read [Manipulating a Composition Using JavaScript](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmznknlte).

The Quartz Composer WebKit plug-in allows for manipulating a composition using JavaScript, as shown in Listing 4-2.

__Listing 4-2__  Changing a composition’s values via JavaScript

```
var composition = document.getElementById("myComposition");
if (composition.playing() == true)
{
    composition.pause();
    composition.setInputValue("aPublishedInput", aValue);
    composition.setInputValue("anotherPublishedInput", anotherValue);
    composition.play();
}
```

The code in Listing 4-2 gets a composition from the DOM (Document Object Model) and queries its playback status. If the composition is playing, the code pauses playback. Then it modifies some of the composition input values. Finally, the code resumes playback.

You need to get the composition from the DOM because it returns the composition object that you can manipulate. Note that the element identifier is the same as the `id` attribute value for the composition included in [Listing 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmznknltc). You perform the rest of these actions using JavaScript methods. To learn more about the JavaScript API for Quartz Composer WebKit plug-ins, read _[Quartz Composer WebKit Plug-in JavaScript Reference](../../Internet%20Web/Quartz%20Composer%20WebKit%20Plug-in%20JavaScript%20Reference/Introduction%20to%20Quartz%20Composer%20WebKit%20Plug-in%20JavaScript%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjx)_.

The Quartz Composer WebKit plug-in provides HTML attributes that affect how a composition is rendered and triggers JavaScript functions for certain events.

**`above`**
: A Boolean value that specifies whether the composition should render above or below the window that displays a webpage. If `above` is set to `true`, no content on the page within the bounds of the composition is shown. If `above` is set to `false`, all content on the page within the composition’s bounds is shown over the composition.

This setting is most useful for Dashboard widgets, where a value of `false` lets you place elements over a composition.

The default value, used if this attribute is not specified, is `true`.

**`autoplay`**
: A Boolean value that specifies whether the composition is played automatically when it’s loaded. If `autoplay` is set to `true`, the composition begins playback when it has completed loading. If `autoplay` is set to `false`, it doesn’t play automatically.

The default value, used if this attribute is not specified, is `true`.

**`opaque`**
: A Boolean value that specifies whether the composition is opaque or transparent. If `opaque` is set to `true`, the composition is rendered with no alpha channel, meaning any transparent areas in the composition are rendered as solid and any elements placed under the composition are not visible. If `opaque` is set to `false`, the composition is rendered with an alpha channel, meaning that transparent areas in the composition are rendered using any transparency found in the composition and any elements placed under the composition are visible through transparent areas in the composition.

The default value, used if this attribute is not specified, is `true`.

**`maxfps`**
: An integer value that specifies the maximum frame rate used when rendering the composition.

The default value, used if this attribute is not specified, is `30`.

**`onload`**
: A JavaScript event handler called when the composition is finished loading. The JavaScript function you provide for this event is not passed any arguments when it is called.

**`onloading`**
: A JavaScript event handler called when the composition is in the process of loading. The JavaScript function you provide for this event is passed one argument when it is called; the argument is a float value between `0` and `1` that indicates loading progress.

The default loading animation will be used if this attribute is not specified.

**`onerror`**
: A JavaScript event handler called if the composition fails to load. The JavaScript function you provide for this event is passed one argument when it is called; the argument contains a string representing the reason the composition failed to load.

The Quartz Composer WebKit plug-in renders most, but not all, the patches available in Quartz Composer. You are _not_ allowed to use patches that:

- Access information from local files and folders, such as the Folder Images and Spotlight Images patches
- Fetch information from services, such as the Bonjour Services, Host Info, RSS Feed, and Image Downloader patches
- Communicate with certain hardware, such as the MIDI Clock, MIDI Controllers, MIDI Notes, and Audio Input patches

For detailed information about Quartz Composer patches and WebKit, see [Technical Q&A QA1505 Availability of Quartz Composer Patches in Web Kit](https://developer.apple.com/qa/qa2006/qa1505.html).

[Next](Document%20Revision%20History.md)[Previous](Using%20the%20QCRenderer%20Class%20to%20Play%20a%20Composition.md)

