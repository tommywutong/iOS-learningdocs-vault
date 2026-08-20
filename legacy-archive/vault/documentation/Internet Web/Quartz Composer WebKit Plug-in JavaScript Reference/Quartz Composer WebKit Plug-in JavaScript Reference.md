---
title: Quartz Composer WebKit Plug-in JavaScript Reference
apple_id: TP40004517
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2009-01-06'
source_url: https://developer.apple.com/library/archive/documentation/InternetWeb/Conceptual/QuartzComposer_PlugIn_ProgGuide/QCPluginReference/QCPluginReference.html
archived_at: '2026-07-15T07:43:37.582797Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Composer WebKit Plug-in JavaScript Reference](Introduction%20to%20Quartz%20Composer%20WebKit%20Plug-in%20JavaScript%20Reference.md)


[Next](Document%20Revision%20History.md)[Previous](Introduction%20to%20Quartz%20Composer%20WebKit%20Plug-in%20JavaScript%20Reference.md)

# Quartz Composer WebKit Plug-in JavaScript Reference

The JavaScript API provided by the Quartz Composer WebKit plug-in includes methods for changing a composition’s state and manipulating its published inputs and outputs. To learn how to include a Quartz Composer composition in a web page or Dashboard widget, read [Webpages and Widgets](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzComposer/qc_webkit/qc_webkit.html#//apple_ref/doc/uid/TP40001357-CH3).

**_Composition Metadata_**
: - [attributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcnq)

**_Composition Playback_**
: - [pause](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknlto)
- [play](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltq)
- [stop](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknlts)

**_Composition Status_**
: - [loaded](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcmq)
- [paused](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcma)
- [playing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcmi)

**_Pasteboard Operations_**
: - [copyImageToPasteboard](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcny)

**_Working with Published Values_**
: - [getInputValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknlti)
- [getOutputValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltm)
- [inputKeys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcmy)
- [outputKeys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcna)
- [setInputValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltk)

Returns an array of strings with the composition’s attributes.

```
composition.attributes()
```

**_Discussion_**
: The attributes returned are the composition’s metadata, including its name, copyright, and description values, along with information about each port of the composition.

Copies the current context of the composition to the pasteboard.

```
composition.copyImageToPasteboard()
```

**_Discussion_**
: Use this method in conjunction with an `oncopy` handler.

Returns the value of a published input.

```
composition.getInputValue("key")
```

**_Discussion_**
: The value of `key` is any of the inputs that you published in Quartz Composer.

If the returned value is a color, an object is returned with `red`, `green`, `blue`, and `alpha` properties. Each value is a floating-point number, on a scale from `0` to `1`. Call `htmlColor()` on the object to return its HTML hexadecimal color value or `cssColor()` to return its `rgba` value.

No images are returned when calling `getInputValue`.

**_See Also_**
: [inputKeys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcmy)

[outputKeys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcna)

[setInputValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltk)

[getOutputValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltm)

Returns the value of a published output.

```
composition.getOutputValue("key")
```

**_Discussion_**
: The value of `key` is any of the outputs that you published in Quartz Composer.

If the returned value is a color, an object is returned with `red`, `green`, `blue`, and `alpha` properties. Each value is a floating-point number, on a scale from `0` to `1`. Call `htmlColor()` on the object to return its HTML hexadecimal color value or `cssColor()` to return its `rgba` value.

No images are returned when calling `getOutputValue`.

**_See Also_**
: [outputKeys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcna)

[inputKeys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcmy)

[setInputValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltk)

[getInputValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknlti)

Returns an array of strings with the names of a composition’s published inputs.

```
composition.inputKeys()
```

**_See Also_**
: [setInputValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltk)

[getInputValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknlti)

[outputKeys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcna)

[getOutputValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltm)

Returns whether the composition is loaded.

```
composition.loaded()
```

**_See Also_**
: [playing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcmi)

[paused](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcma)

Returns an array of strings with the names of a composition’s published outputs.

```
composition.outputKeys()
```

**_See Also_**
: [getOutputValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltm)

[inputKeys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcmy)

[setInputValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltk)

[getInputValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknlti)

Pauses playback of a composition.

```
composition.pause()
```

**_Discussion_**
: If a composition wasn’t playing, calling this method does nothing.

**_See Also_**
: [play](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltq)

[stop](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknlts)

Returns whether the composition is paused.

```
composition.paused()
```

**_Discussion_**
: If the composition is stopped (as opposed to paused), paused returns `false`.

**_See Also_**
: [playing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcmi)

[loaded](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcmq)

Begins or pauses playback of a composition.

```
composition.play()
```

**_Discussion_**
: The `play` method starts playback of a composition if it was stopped or hasn’t played yet, pauses playback if the composition is already playing, and resumes playback if the composition was paused.

**_See Also_**
: [pause](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknlto)

[stop](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknlts)

Returns whether the composition is playing.

```
composition.playing()
```

**_See Also_**
: [paused](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcma)

[loaded](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcmq)

Gives the composition the provided value for published input.

```
composition.setInputValue("key", value)
```

**_Discussion_**
: The value of `key` is any of the inputs that you published in Quartz Composer.

If you’re setting an input to a color value, you can pass in:

- An object like that returned by [getInputValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknlti) and [getOutputValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltm), with `red`, `green`, `blue`, and `alpha` properties
- An HTML hexadecimal color value, like `#FFFFFF`
- An HTML color name, like `red` or `green`
- A CSS `rgb` or `rgba` value

If the input value can’t be parsed, no change is made. Also, images aren’t allowed as an input value.

**_See Also_**
: [inputKeys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcmy)

[outputKeys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltcna)

[getInputValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknlti)

[getOutputValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltm)

Stops playback of a composition.

```
composition.stop()
```

**_Discussion_**
: The `stop` method releases all resources associated with the composition and clears its visuals from the page. After calling `stop`, you can call `play` to restart the composition.

**_See Also_**
: [play](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknltq)

[pause](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjxfvbuqnbnknlto)

[Next](Document%20Revision%20History.md)[Previous](Introduction%20to%20Quartz%20Composer%20WebKit%20Plug-in%20JavaScript%20Reference.md)

