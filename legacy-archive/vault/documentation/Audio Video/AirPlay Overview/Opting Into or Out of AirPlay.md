---
title: AirPlay Overview
apple_id: TP40011045
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AirPlayGuide/OptingInorOutofAirPlay/OptingInorOutofAirPlay.html
archived_at: '2026-07-15T05:21:02.002807Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AirPlay Overview](About%20AirPlay.md)


[Next](Enriching%20the%20AirPlay%20Experience%20in%20Your%20App.md)[Previous](Preparing%20Your%20Media%20and%20Server%20for%20AirPlay.md)

# Opting Into or Out of AirPlay

Audio content (except for system sounds) and media played via iTunes or the Music app are always available to AirPlay. Video playing in your app or from your website can be enabled for AirPlay or not, at your discretion.

Before iOS 5.0, you needed to opt into AirPlay to enable your media to be played over Apple TV. In apps compiled with the base SDK set to iOS 5.0 and later, AirPlay is enabled by default; if you do not want iOS-based devices to be able to play your video over Apple TV, you must disable AirPlay explicitly.

In iOS 5.0 and later, Safari opts in for web content by default.

To enable video on your website to be viewable via AirPlay, embed it in your webpage using the HTML5 `<video>` tag. See _[Safari HTML5 Audio and Video Guide](../Safari%20HTML5%20Audio%20and%20Video%20Guide/About%20HTML5%20Audio%20and%20Video.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrt)_ for details.

To explicitly opt in to AirPlay, set the `x-webkit-airplay` attribute for the `video` tag or the `airplay` attribute for the `embed` tag to `"allow"`, as shown in Listing 2-1.

__Listing 2-1__  Allowing AirPlay to use your video

```
<video src="myPlaylist.m3u8"
       height="300" width="400"
       x-webkit-airplay="allow" >

  <embed airplay=”allow”
       src="movie.mov"
       width=400
       height=300
       mime-type="video/quicktime">
  </embed>

</video>
```

To explicitly opt out of AirPlay, set `x-webkit-airplay` attribute for the `video` tag or the `airplay` attribute for the `embed` tag to `"deny"`, as shown in Listing 2-2.

__Listing 2-2__  Disallowing AirPlay to use your video

```
<video src="myPlaylist.m3u8"
       height="768" width="1024"
       x-webkit-airplay="deny" >

</video>

<!-- or -->

<embed airplay="deny"
       src="movie.mov"
       width=320
       height=240
       mime-type="video/quicktime">

</embed>
```


AirPlay is automatically enabled for video when your app uses AV Foundation, the [MPMoviePlayerController](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller) class, or the [UIWebView](https://developer.apple.com/documentation/uikit/uiwebview) class to display video. If necessary, you can explicitly disable AirPlay for your app’s video. The exact method depends on the API you use for video playback.

- If your app uses the [AVPlayer](https://developer.apple.com/documentation/avfoundation/avplayer) class to display video, you can explicitly enable AirPlay by setting the [allowsAirPlayVideo](https://developer.apple.com/documentation/avfoundation/avplayer/1624258-allowsairplayvideo) property to `YES`.
- To disable AirPlay, set the [allowsAirPlayVideo](https://developer.apple.com/documentation/avfoundation/avplayer/1624258-allowsairplayvideo) property to `NO`.
- To determine whether your video is playing over AirPlay, test the state of the [airPlayVideoActive](https://developer.apple.com/documentation/avfoundation/avplayer/1624259-airplayvideoactive) property.

- If your app uses the [MPMoviePlayerController](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller) class to display video, you can explicitly enable AirPlay by setting the [allowsAirPlay](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620781-allowsairplay) property to `YES`.
- To disable AirPlay, set the [allowsAirPlay](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620781-allowsairplay) property to `NO`.
- To determine whether your video is playing over AirPlay, test the state of the [airPlayVideoActive](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620906-isairplayvideoactive) property.

- If your app uses the [UIWebView](https://developer.apple.com/documentation/uikit/uiwebview) API to display video, you can explicitly enable AirPlay by setting the [mediaPlaybackAllowsAirPlay](https://developer.apple.com/documentation/uikit/uiwebview/1617973-mediaplaybackallowsairplay) property to `YES`. In addition, the content you are displaying in the web view must not disallow AirPlay.
- To disable AirPlay, set the [mediaPlaybackAllowsAirPlay](https://developer.apple.com/documentation/uikit/uiwebview/1617973-mediaplaybackallowsairplay) property to `NO`.

[Next](Enriching%20the%20AirPlay%20Experience%20in%20Your%20App.md)[Previous](Preparing%20Your%20Media%20and%20Server%20for%20AirPlay.md)

