---
title: Safari HTML5 Audio and Video Guide
apple_id: TP40009523
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/Using_HTML5_Audio_Video/AudioandVideoTagBasics/AudioandVideoTagBasics.html
archived_at: '2026-07-15T05:21:32.472145Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML5 Audio and Video Guide](About%20HTML5%20Audio%20and%20Video.md)


[Next](iOS-Specific%20Considerations.md)[Previous](About%20HTML5%20Audio%20and%20Video.md)

# Audio and Video HTML

In their simplest form, the `<audio>` and `<video>` tags require only a `src` attribute to identify the media, although you generally want to set the `controls` attribute as well. Safari allocates space, provides a default controller, loads the media, and plays it when the user clicks the play button. It’s all automatic.

There are optional attributes as well, such as `autoplay`, `loop`, `height`, and `width`.

The attributes for the `<audio>` and `<video>` tags are summarized in [Table 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrtfvbuqmrnknlte). The only difference between the `<audio>` and `<video>` tag attributes is the option to specify a height, width, and poster image for video.

__Table 1-1__   Attributes of the `<audio>` and `<video>` elements

| Attribute | Value | Description |
| preload  _This attribute was formerly named autobuffer, and was boolean._ | `none | metadata | auto` | `none`—Safari should not preload media data.  `metadata`—Safari should preload only media metadata.  `automatic`—Safari should preload all media data. |
| autoplay | Boolean—any value sets this to `true` | If present, asks the browser to play the media automatically. |
| controls | Boolean—any value sets this to `true` | If present, causes the browser to display the default media controls. |
| height (video only) | _pixels_ | The height of the video player. |
| loop | Boolean—any value sets this to `true` | If present, causes the media to loop indefinitely. This attribute is supported in iOS 5.0 and later. |
| poster (video only) | _url of image file_ | If present, shows the poster image until the first frame of video has downloaded. |
| src | _url_ | The URL of the media. |
| width (video only) | _pixels_ | The width of the video player. |

The `preload` attribute is a hint to the browser, telling it your preferences. There is no guarantee that you will get the behavior that you prefer. Safari does not support all preferences on all devices, and does not currently support the Metadata preference on any device. For more information, see [iOS-Specific Considerations](iOS-Specific%20Considerations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrtfvbuqnjnknltc).

Listing 1-1 shows an HTML page that autoplays a video at a specified height and width with the built-in user controls.

__Listing 1-1__  Creating a simple movie player

```
<!doctype html>
<html>
   <head>
      <title>Simple Movie Player</title>
   </head>
   <body>
      <video src="http://example.com/path/mymovie.mov"
             controls
             autoplay
             height="270" width="480">
      </video>
  </body>
</html>
```


There are several ways you can control media playback directly in HTML by setting attributes appropriately.

In Safari on iOS, the native size of the video is unknown until the user initiates a download. If no height or width is specified, a default size of 150 x 300 pixels is allocated in the webpage. On iPad, the video currently plays in this default space. On iPhone or iPod touch, the video plays in fullscreen mode once the user initiates it, and the default space is allocated to a placeholder on the webpage.

In Safari on the desktop, the movie metadata is downloaded automatically whenever possible, so the native video size is used as the default. If only the `height` or `width` parameter is specified, the video is scaled up or down to that height or width while maintaining the native aspect ratio of the movie. If both height and width are specified, the video is presented at that size. If neither is specified, the video is displayed at its native size.

In Safari, the default video controller is slightly translucent and is overlaid on the bottom of the video. The controller is not normally visible when the movie is playing—it appears only when the movie is paused, when the user touches the video, or when the mouse pointer hovers over the playing movie. In cases where it is crucial that the bottom of the video never be obscured, omit the `controls` attribute. (You cannot set the attribute to `false` explicitly in HTML—you set it to `false` _implicitly_ by leaving the attribute out.)

If you do not set the `controls` attribute, you must either set the `autoplay` attribute, create a controller using JavaScript, or play the movie programmatically from JavaScript. Otherwise the user has no way to play the movie.

If you set the `preload` attribute to `auto`, it tells Safari you want the specified media file to start buffering immediately, making it more likely that it will begin promptly and play through smoothly when the user plays it.

If you have multiple movies on the page, you should set the `preload` attribute to `none`, to prevent all the movies from downloading at once.

Safari does not currently support the `metadata` setting.

Setting a poster image normally has a transitory effect—the poster image is shown only until the first frame of the video is available, which is typically a second or two. On iOS, however, the first frame is not shown until the user initiates playback, and a poster image is recommended, as shown in Listing 1-2.

__Listing 1-2__  Showing a poster

```
<!doctype html>
<html>
   <head>
      <title>Movie Player with Poster</title>
   </head>
   <body>
      <video src="http://example.com/path/mymovie.mov"
             controls
             height=340 width=640
             poster="http://example.com/path/poster.jpg">
      </video>
  </body>
</html>
```


Not all types of audio and video can play on all devices and browsers. Fortunately, the `<audio>` and `<video>` elements allow you to list as many `<source>` elements as you like. The browser iterates through them until it finds one it can play or runs out of sources. Instead of using the `src` attribute in the media element itself, follow the `<audio>` or `<video>` tag with one or more `<source>` elements, prior to the closing tag.

List the alternate media sources in the order of most desirable to least desirable. The browser chooses the first listed source that it thinks it can play. For example, if you have an AAC audio file, an Ogg Vorbis audio file, and a WAVE audio file, listed in that order, Safari plays the AAC file. A browser that cannot play AAC but can play Ogg plays the Ogg file. A browser that can play neither Ogg nor AAC might still be able to play the WAVE file.

Listing 1-3 is a simple example of using multiple sources for an audio file.

__Listing 1-3__  Specifying multiple audio sources

```
<!doctype html>
<html>
   <head>
      <title>Multi-Source Audio Player</title>
   </head>
   <body>
      <audio controls autoplay >
             <source src="http://example.com/path/MyAudio.m4a">
             <source src="http://example.com/path/MyAudio.oga">
             <source src="http://example.com/path/MyAudio.wav">
      </audio>
  </body>
</html>
```

The `<source>` element can have a `type` attribute, specifying the MIME type, to help the browser decide whether or not it can play the media without having to load the file.

```
<audio controls>
    <source src="mySong.aac" type="audio/mp4">
    <source src="mySong.oga" type="audio/ogg">
</audio>
```

The `type` attribute can take an additional `codecs` parameter, to specify exactly which versions of which codecs are needed to play this particular media.

```
<audio controls>
    <source src="mySongComplex.aac" type="audio/mp4; codecs=mp4a.40.5">
    <source src="mySongSimple.aac" type="audio/mp4; codecs=mp4a.40.2">
</audio>
```

Notice that you don’t have to know which browsers support what formats, and then sniff the user agent string for the browser name to decide what to do. Just list your available media, preferred format first, second choice next, and so on. The browser plays the first one it can.

Currently, most browsers support low-complexity AAC and MP3 audio and basic profile MPEG-4. Most browsers that do not support these formats support Theora video and Vorbis audio using the Ogg file format. Generally speaking, if you provide media in MPEG-4 (basic profile) and Ogg formats, your media can play in browsers that support HTML5.

You can also use multiple source elements to specify different delivery schemes. Let’s say you have a large real-time video streaming service that uses RTSP streaming, and you want to add support for Safari on iOS, including iPad, using HTTP Live Streaming, along with a progressive download for browsers that can’t handle either kind of streaming. As shown in Listing 1-4, with HTML5 video it’s quite straightforward.

__Listing 1-4__  Specifying multiple delivery schemes

```
<!doctype html>
<html>
   <head>
      <title>Multi-Scheme Video Player</title>
   </head>
   <body>
      <video controls autoplay >
             <source src="http://HttpLiveStream.m3u8">
             <source src="rtsp://LegacyStream.3gp">
             <source src="http://ProgressiveDownload.m4v">
      </video>
  </body>
</html>
```

Again, the browser picks the first source it can handle. Safari on the desktop plays the RTSP stream, while Safari on iOS plays the HTTP Live stream. Browsers that support neither m3u8 playlists nor RTSP URLs play the progressive download version.

HTML5 does not support selection from multiple sources based on data rate. If you supply multiple sources, the browser chooses the first it can play based on scheme, file format, profile, and codecs. Bandwidth is not tested. To provide multiple bandwidths, you must provide a `src` attribute that specifies a source capable of supporting data rate selection itself.

For example, if one of your sources is an HTTP Live Stream, the playlist file can specify multiple streams, and Safari selects the best stream for the current bandwidth dynamically as network bandwidth changes. For more information, see _[HTTP Live Streaming Overview](../../Networking%20Internet/HTTP%20Live%20Streaming%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzs)_.

Similarly, if the source is a QuickTime reference movie, it can include alternate sources at different data rates, and Safari chooses the best source for the current bandwidth when the video is first requested (though it does not dynamically switch between sources if available bandwidth subsequently changes). For more information, see [Technical Note TN2266 "Creating Reference Movies—MakeRefMovie"](https://developer.apple.com/mac/library/technotes/tn2010/tn2266.html)

It’s easy to specify fallback behavior for browsers that don’t support the `<audio>` or `<video>` elements—just put the fallback content between the opening and closing media tags, after any `<source>` elements. See Listing 1-5.

__Listing 1-5__  Adding simple fallback behavior

```swift
<!DOCTYPE html>
<html>
   <head>
      <title>Simple Movie Player with Trivial Fallback Behavior</title>
   </head>
   <body>
      <!-- opening tag -->
      <video src="mymovie.mov" controls>

       <!-- fallback content -->
       Your browser does not support the video element.

      <!-- closing tag -->
      </video>
  </body>
</html>
```

Browsers that don’t support the `<audio>` or `<video>` tags simply ignore them. Browsers that support these elements ignore all content between the opening and closing tags (except `<source>` tags).

There is a simple way to fall back to the QuickTime plug-in that works for nearly all browsers—download the prebuilt JavaScript file provided by Apple, `ac_quicktime.js`, from _[HTML Video Example](../../../samplecode/HTML%20Video%20Example/HTML%20Video%20Example.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydonzsgm)_ and include it in your webpage by inserting the following line of code into your HTML head:

```
<script src="ac_quicktime.js" type="text/javascript"></script>
```

Once you’ve included the script, add a call to `QT_WriteOBJECT()` between the opening and closing tags of the `<audio>` or `<video>` element, passing in the URL of the movie, its height and width, and the version of the ActiveX control for Internet Explorer (just leave this parameter blank to use the current version). See Listing 1-6 for an example.

__Listing 1-6__  Falling back to the QuickTime plug-in

```
<!doctype html>
<html>
   <head>
      <title>Simple Movie Player with QuickTime Fallback</title>
      <script src="ac_quicktime.js" type="text/javascript"></script>
   </head>
   <body>
      <video controls>
         <source src="myMovie.mov" type="video/quicktime">
         <source src="myMovie.3gp" type="video/3gpp">
       <!-- fallback -->
       <script type="text/javascript">
           QT_WriteOBJECT('myMovie.mov' , '320', '240', '');
       </script>
      </video>
  </body>
</html>
```

You can pass more than twenty additional parameters to the QuickTime plug-in. For more about how to work with the QuickTime plug-in and the `ac_quicktime.js` script, see _[HTML Scripting Guide for QuickTime](../../Quick%20Time/HTML%20Scripting%20Guide%20for%20QuickTime/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmrv)_.

Since most browsers now support the `<audio>` and `<video>` elements, you can simplify the process of coding for plug-ins by including only the version of the `<object>` tag that works with Internet Explorer as your fallback for HTML5 media.

Listing 1-7 uses HTTP Live Streaming for browsers that support it, MPEG-4 and Ogg Vorbis by progressive download for browsers that support those formats, and falls back to a plug-in for versions of Internet Explorer that don’t support HTML5.

__Listing 1-7__  Falling back to a plug-in for IE

```
<!doctype html>
<html>
<head>
    <title>Simple Movie Player with Plug-In Fallback</title>
</head>
<body>
    <video controls>
        <source src="HttpLiveStream.m3u8" type="vnd.apple.mpegURL">
        <source src="ProgressiveDowload.mp4" type="video/mp4">
        <source src="OggVorbis.ogv" type="video/ogg">
        <!-- fallback -->
        <object classid="clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B"
                codebase="http://www.apple.com/qtactivex/qtplugin.cab"
                height="320"
                width="240">
            <param name="src" value="ProgressiveDownload.mp4">
        </object>
    </video>
</body>
</html>
```

Listing 1-7 uses the QuickTime plug-in. To use a different plug-in, change the `CLASSID` and `CODEBASE` parameters to those of your preferred plug-in and provide the `PARAM` tags the plug-in requires.

[Next](iOS-Specific%20Considerations.md)[Previous](About%20HTML5%20Audio%20and%20Video.md)

