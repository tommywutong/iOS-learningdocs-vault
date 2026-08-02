---
title: How to play a sequence of movies in a Web page
apple_id: DTS40007918
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2008-08-08'
source_url: https://developer.apple.com/library/archive/qa/qa1593/_index.html
archived_at: '2026-07-18T02:32:21.911499Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1593

# How to play a sequence of movies in a Web page

## Q:  I'm putting QuickTime content in my Web page and I'd like to have the QuickTime plug-in play a sequence of movies, one after the other. Is this possible?

A: I'm putting QuickTime content in my Web page and I'd like to have the QuickTime plug-in play a sequence of movies, one after the other. Is this possible?

Yes, the QuickTime plug-in has many special features that you can control from HTML by inserting parameters in the page using the `<EMBED>` tag. You can specify the `QTNEXT` parameter in the `<EMBED>` tag in your HTML to tell the QuickTime plug-in to play a sequence of movies, one after the other, to create an endlessly repeating playlist. When the current movie finishes, the next movie in the list starts. This can also be a good way to deliver a long movie; users never need to store more than a small piece of it on their computers at any time.

Here's how to specify the `QTNEXT` parameter:


```
QTNEXTn="<Filename> T<Target>" or "GOTOn"
```

Here's an example:


```
<EMBED SRC="First.mov" HEIGHT="176" WIDTH="120"    QTNEXT1="<Second.mov> T<myself>" QTNEXT2="<Third.mov> T<myself>">
```

You have to append a number between 1 and 255 to each `QTNEXT`. They execute in numerical order.

`"<Filename> T<Target>"`

Set `<Filename>` to the name of the file you want to play next. You can include a relative path or the full URL.

The `T<Target>` parameter is optional. It specifies where the movie plays. If it's not specified, the next movie replaces the current browser window or frame, and any subsequent `QTNEXT` statements are lost. The special value of `T<myself>` targets the QuickTime plug-in and is normally the value you want; the next movie replaces the current movie, and subsequent `QTNEXT` statements are executed in turn. The target can also be the name of a browser window or frame. If no window or frame of that name exists, a new browser window with that name is created. You can also specify `T<quicktimeplayer>` as a target, which opens the movie in QuickTime Player.

Each `QTNEXT` statement has an index number, which is the order in which the movies play.

The special index value of `0` is assigned to the original movie named in the `SRC` parameter (or the `QTSRC` parameter, if it was specified).

Why have index numbers? Because instead of a filename, you can specify `GOTOn`, where `n` is the index of the `QTNEXT` you want to go to. You normally do this to create a simple loop:


```
<EMBED SRC="First.mov" HEIGHT="176" WIDTH="120" QTNEXT1="<Second.mov> T<myself>" QTNEXT2="<Third.mov> T<myself>" QTNEXT3=GOTO0 >
```

This example plays `First.mov`, then `Second.mov`, then `Third.mov`, then goes back to `First.mov` (index `0`), in an endless loop. You can use values other than `0` to cause `QTNEXT` statements to play in arbitrary order, or to start looping from some midpoint. For example,


```
<EMBED SRC="Intro.mov" HEIGHT="176" WIDTH="120" QTNEXT1="<First.mov> T<myself>" QTNEXT2="<Second.mov> T<myself>" QTNEXT3=GOTO1 >
```

would play the `Intro.mov` just once, then play `First.mov` and `Second.mov` in an endless loop.

The `EMBED` tag alone will work just fine on Safari and on Firefox. However, we recommend you use an `EMBED` tag nested within an `OBJECT` tag because Internet Explorer will automatically offer to download and install the QuickTime ActiveX control if the user doesn't already have it. In Firefox and Safari, the `OBJECT` tag code is ignored.

Here's what the nested code looks like:


```
<object classid="clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B" width="320" height="256"      codebase="http://www.apple.com/qtactivex/qtplugin.cab">         <param name="src" value="First.mov">         <param name="controller" value="true">         <param name="autoplay" value="true">         <param name="qtnext1" value="<second.mov>T<myself>E<controller=true autoplay=true>">         <param name="qtnext2" value="<third.mov>T<myself>E<controller=true autoplay=true>">     <embed         src="First.mov"         width="320" height="256"         controller="true"         autoplay="true"         qtnext1="<second.mov>T<myself>E<controller=true autoplay=true>"         qtnext2="<third.mov>T<myself>E<controller=true autoplay=true>"         pluginspage="http://www.apple.com/quicktime/download/">     </embed> </object>
```

Also, in early 2006, Microsoft made available an updated version of Internet Explorer browser for Windows. This new Internet Explorer for Windows handles QuickTime and other ActiveX controls in a new way. Your website may be affected if it features QuickTime content that is contained in an HTML web page using `OBJECT`, `EMBED`, or `APPLET` tags. See [Instructions for Updating Websites to Include QuickTime Content](https://developer.apple.com/internet/ieembedprep.html) for more information.

The `QTNEXT` parameter can also support sub-parameters for each movie.

Here's example HTML code:

In the `OBJECT` tag:


```
<PARAM NAME="qtnext1" VALUE="<second.mov>T<myself>E<CONTROLLER=true AUTOPLAY=true>">
```

In the `EMBED` tag:


```
qtnext1="<second.mov>T<myself>E<CONTROLLER=true AUTOPLAY=true>"
```


- [Including QuickTime Content in a Web Page](http://www.apple.com/quicktime/tutorials/embed.html)
- [Instructions for Updating Websites to Include QuickTime Content](https://developer.apple.com/internet/ieembedprep.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-08-08 | New document that how to have the QuickTime plug-in play a sequence of movies, one after the other, in a Web page |

