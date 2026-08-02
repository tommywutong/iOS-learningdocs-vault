---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOQuickTimeView.html
archived_at: '2026-07-15T08:11:44.957379Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOQuickTimeView

> **__Inherits
> from:__**
> : javax.swing.JPanel
> javax.swing.JComponent
> java.awt.Container :
> java.awt.Component :
>
> Object

> **__Package:__**
> : com.apple.client.eointerface

---

## Class Description

---

The EOQuickTimeView class is used to display
QuickTime movies in Java Client applications.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.yellow.eointerface package. |

## Constants

---

EOQuickTimeView defines the following `int` constants
to identify resizing behavior:

- QuickTimeCanvasNoResizing
- QuickTimeCanvasAspectResizing
- QuickTimeCanvasFreeResizing
- QuickTimeCanvasIntegralResizing
- QuickTimeCanvasPerformanceResizing
- QuickTimeCanvasHorizontalResizing
- QuickTimeCanvasVerticalResizing

These same constants are also defined in quicktime.app.display.QTCanvas.
They are duplicated in EOQuickTimeView for convenience. For information
on the resizing behavior associated with these constants, see the
QTCanvas documentation.

## Method Types

---

> **Determining if the QuickTime
> system is available**
> : [isQuickTimeAvailable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvnfrwwvdjnvsvm2lfo4xws42rovuwg22unfwwkqlwmfuwyylcnrsq)
>
> **Setting the QuickTime
> movie and player**
> : [movie](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wsy3lkruw2zkwnfsxol3nn53gszi)
> : [setMovie](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wsy3lkruw2zkwnfsxol3tmv2e233wnfsq)
> : [setMovieFromURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wsy3lkruw2zkwnfsxol3tmv2e233wnfsum4tpnvkveta)
> : [player](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wsy3lkruw2zkwnfsxol3qnrqxszls)
> : [setPlayer](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wsy3lkruw2zkwnfsxol3tmv2fa3dbpfsxe)
>
> **Configuring resizing
> behavior**
> : [setCanvasResizing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wsy3lkruw2zkwnfsxol3tmv2egyloozqxgutfonuxu2lom4)
> : [canvasResizing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wsy3lkruw2zkwnfsxol3dmfxhmyltkjsxg2l2nfxgo)
>
> **Painting**
> : [getPreferredSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wsy3lkruw2zkwnfsxol3hmv2fa4tfmzsxe4tfmrjws6tf)
> : [setBounds](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wsy3lkruw2zkwnfsxol3tmv2ee33vnzshg)

## Static Methods

---

### isQuickTimeAvailable

`public static boolean isQuickTimeAvailable()`

Returns `true` if
the QuickTime for Java classes are in the class path and are loaded; `false` otherwise. If the
classes are in the class path but aren't loaded, this method attempts
to load them.

---

## Instance Methods

---

### canvasResizing

`public int canvasResizing()`

Returns an integer that identifies
the receiver's resizing behavior. The return
value is one of the following constants (defined in EOQuickTimeView):

- [QuickTimeCanvasNoResizing](#apple-ijceiqscjfbec)
- [QuickTimeCanvasAspectResizing](#apple-ijceirsijjcuc)
- [QuickTimeCanvasFreeResizing](#apple-ijceirkdjfdek)
- [QuickTimeCanvasIntegralResizing](#apple-ijceirkfizbek)
- [QuickTimeCanvasPerformanceResizing](#apple-ijceiq2hjjcuu)
- [QuickTimeCanvasHorizontalResizing](#apple-ijceiskji5cus)
- [QuickTimeCanvasVerticalResizing](#apple-ijceirsgirbui)

For
more information on the resizing constants, see ["Constants"](#apple-ijceircji5aug).

---

### getPreferredSize

`public java.awt.Dimension getPreferredSize()`

See the method description
for `getPreferredSize` in Sun's JComponent
class documentation.

---

### movie

`public Object movie()`

Returns the receiver's QuickTime
movie, a quicktime.std.movies.Movie.

---

### player

`public Object player()`

Returns the receiver's QuickTime
player, a quicktime.app.players.QTPlayer.

---

### setBounds

`public void setBounds(
int  x,
int  y,
int  width,
int  height)`

See the method description
for `setBounds` in Sun's Component class
documentation.

---

### setCanvasResizing

`public void setCanvasResizing(int  canvasResizing)`

Sets the resizing behavior
of the receiver. The  _canvasResizing_ argument
should be one of the following constants (defined in EOQuickTimeView):

- [QuickTimeCanvasNoResizing](#apple-ijceiqscjfbec)
- [QuickTimeCanvasAspectResizing](#apple-ijceirsijjcuc)
- [QuickTimeCanvasFreeResizing](#apple-ijceirkdjfdek)
- [QuickTimeCanvasIntegralResizing](#apple-ijceirkfizbek)
- [QuickTimeCanvasPerformanceResizing](#apple-ijceiq2hjjcuu)
- [QuickTimeCanvasHorizontalResizing](#apple-ijceiskji5cus)
- [QuickTimeCanvasVerticalResizing](#apple-ijceirsgirbui)

The
default resizing behavior is [QuickTimeCanvasAspectResizing](#apple-ijceirsijjcuc).
For more information on these constants, see ["Constants"](#apple-ijceircji5aug).

---

### setMovie

`public void setMovie(Object  movie)`

Sets the receiver's QuickTime
movie to  _movie,_ a quicktime.std.movies.Movie.

---

### setMovieFromURL

`public void setMovieFromURL(String  url)`

Sets the
receiver's QuickTime movie to the movie at  _url._

---

### setPlayer

`public void setPlayer(Object  player)`

Sets the receiver's QuickTime
player to  _player,_ a quicktime.app.players.QTPlayer.

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
